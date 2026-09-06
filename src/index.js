// Cloudflare Worker entry point.
//
// This project serves static files (the whole site) via the [assets]
// binding in wrangler.toml, but a plain static-assets Worker has nowhere
// to run server-side code — which is why /api/* endpoints need an actual
// Worker script. This file is that script: it handles the two API routes
// below directly, and for every other request just falls through to the
// static asset binding so the rest of the site keeps working exactly as
// before.
//
// Required environment variables (Cloudflare dashboard → Workers & Pages →
// forbes-english → Settings → Variables and secrets — see
// deploy/06-environment-variables.md for the full list):
//   STRIPE_SECRET_KEY, STRIPE_PRICE_ID_MONTHLY, STRIPE_PRICE_ID_SEMIANNUAL,
//   STRIPE_PRICE_ID_ANNUAL, STRIPE_WEBHOOK_SECRET, SITE_URL,
//   SUPABASE_URL, SUPABASE_ANON_KEY, SUPABASE_SERVICE_ROLE_KEY

const PLAN_ENV_KEYS = {
  monthly: "STRIPE_PRICE_ID_MONTHLY",
  semiannual: "STRIPE_PRICE_ID_SEMIANNUAL",
  annual: "STRIPE_PRICE_ID_ANNUAL",
};

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);

    if (request.method === "POST" && url.pathname === "/api/create-checkout-session") {
      return handleCreateCheckoutSession(request, env);
    }

    if (request.method === "POST" && url.pathname === "/api/stripe-webhook") {
      return handleStripeWebhook(request, env);
    }

    // A read-only health check for the paywall. The gate deliberately fails
    // OPEN, which means a misconfiguration looks exactly like a working site
    // — the lessons just quietly stay public. This makes that visible without
    // having to guess. It reports no secrets: only whether each piece is
    // wired up, and how many lessons the gate can see.
    if (url.pathname === "/api/paywall-status") {
      return handlePaywallStatus(request, url, env, ctx);
    }

    // ── THE PAYWALL ──────────────────────────────────────────────────
    // This is the only place a paywall can actually work on this site.
    // Lessons are static .html files on the asset CDN; they never pass
    // through Postgres, so no Supabase RLS policy can protect them, and
    // anything done in page JavaScript arrives after the file has already
    // been delivered. The check has to happen here, before the bytes go out.
    const gate = await gateLessonRequest(request, url, env, ctx);
    if (gate) return gate;

    // Everything else (every page, image, etc.) is a static file.
    return env.ASSETS.fetch(request);
  },
};

// ─────────────────────────────────────────────────────────────────────────
// Paywall
// ─────────────────────────────────────────────────────────────────────────

const SESSION_COOKIE = "fe_at";
const ACTIVE_STATUSES = new Set(["active", "trialing"]);

/**
 * Returns a Response when the request is for a gated lesson the caller may
 * not have, or null to let the request continue to the static assets.
 */
async function gateLessonRequest(request, url, env, ctx) {
  if (request.method !== "GET" && request.method !== "HEAD") return null;

  const file = lessonFileFor(url.pathname);
  if (!file) return null;

  const proFiles = await getProFiles(env, ctx);
  // Fail OPEN, not closed: if Supabase is unreachable we would rather serve a
  // pro lesson to a stranger than show every paying subscriber a paywall.
  if (!proFiles) return null;
  if (!proFiles.has(file)) return null;

  if (await hasActiveSubscription(request, env)) {
    // Serve it, but marked private. A pro lesson must never sit in a shared
    // cache where the next person through gets it without the check.
    const res = await env.ASSETS.fetch(request);
    const out = new Response(res.body, res);
    out.headers.set("Cache-Control", "private, no-store");
    out.headers.set("Vary", "Cookie");
    return out;
  }

  return locked(request, url, env, ctx);
}

/**
 * Maps a request path to the lesson filename it would serve, or null if the
 * request is not for a page at all. Cloudflare serves `/foo` from `foo.html`,
 * so both spellings have to resolve to the same lesson — otherwise dropping
 * the extension walks straight past the gate.
 */
function lessonFileFor(pathname) {
  let p;
  try {
    p = decodeURIComponent(pathname);
  } catch {
    return null;
  }
  p = p.replace(/^\/+/, "");
  if (!p || p.endsWith("/")) return null;
  if (p.includes("/")) return null;            // lessons all sit at the root
  if (p.toLowerCase().endsWith(".html")) return p;
  if (/\.[a-z0-9]{2,5}$/i.test(p)) return null; // an image, a PDF, a script
  return `${p}.html`;
}

/**
 * The set of lesson filenames that require a subscription, read from the
 * `lessons` table and cached at the edge. Cached for five minutes so flipping
 * a lesson to free in the database takes effect without a deploy, while a
 * burst of traffic does not become a burst of Supabase queries.
 */
async function getProFiles(env, ctx) {
  const cacheKey = new Request(`${env.SITE_URL}/__internal/pro-lessons`);
  const cache = caches.default;

  const cached = await cache.match(cacheKey);
  if (cached) {
    try {
      return new Set(await cached.json());
    } catch {
      /* fall through and re-fetch */
    }
  }

  let files;
  try {
    const res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/lessons?select=file&access=eq.pro`,
      { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${env.SUPABASE_ANON_KEY}` } }
    );
    if (!res.ok) return null;
    files = (await res.json()).map((r) => r.file);
  } catch {
    return null;
  }

  const body = JSON.stringify(files);
  const toCache = new Response(body, {
    headers: { "Content-Type": "application/json", "Cache-Control": "max-age=300" },
  });
  if (ctx && ctx.waitUntil) ctx.waitUntil(cache.put(cacheKey, toCache));
  return new Set(files);
}

/**
 * Verifies the caller's Supabase session and checks their subscription in a
 * single request: PostgREST rejects an invalid or expired token outright, and
 * the row-level policy on `profiles` means the row that comes back can only
 * ever be the caller's own. There is no way to ask it for somebody else's.
 */
async function hasActiveSubscription(request, env) {
  const token = readCookie(request.headers.get("Cookie"), SESSION_COOKIE);
  if (!token) return false;

  let rows;
  try {
    const res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/profiles?select=subscription_status,owner&limit=1`,
      { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}` } }
    );
    if (!res.ok) return false;
    rows = await res.json();
  } catch {
    return false;
  }

  if (!Array.isArray(rows) || rows.length === 0) return false;
  // `owner` is deliberately separate from subscription_status: the person who
  // runs the site should not lose access to it because of a billing event.
  return rows[0].owner === true || ACTIVE_STATUSES.has(rows[0].subscription_status);
}

function readCookie(header, name) {
  if (!header) return null;
  for (const part of header.split(";")) {
    const [k, ...v] = part.trim().split("=");
    if (k === name) return decodeURIComponent(v.join("="));
  }
  return null;
}

/**
 * The gate page, built for the lesson that was asked for.
 *
 * **200, not 402.** The old status was the honest one and it cost every pro
 * lesson its place in search: Google does not index a non-2xx response, so
 * 195 lessons — four fifths of the library — could not appear in a result
 * however good they were. The supported way to say "this is deliberately
 * gated" is a 200 carrying `isAccessibleForFree: false` and a `hasPart`
 * marking the withheld region, which is exactly what goes out below. It is
 * not a 200 pretending the paywall is the lesson: the page says plainly, to
 * a reader and to a crawler, that the lesson is behind a subscription.
 *
 * **The same page for everybody.** Whatever a crawler is shown here, a
 * logged-out person sees too — the title, what the lesson teaches, its
 * level. Showing Google the lesson and a visitor the gate would be
 * cloaking, and this deliberately does not do that.
 *
 * The per-lesson text comes from `lesson-meta.json`, which `tools/seo.py`
 * generates from the same `lessons` table this gate reads.
 */
async function locked(request, url, env, ctx) {
  const page = await env.ASSETS.fetch(new Request(`${url.origin}/locked.html`));
  let html = page.ok ? await page.text() : "<h1>This lesson is for subscribers.</h1>";

  const file = lessonFileFor(url.pathname);
  const meta = await getLessonMeta(request, url, env, ctx);
  const m = file && meta ? meta[file] : null;
  if (m) html = personaliseGate(html, m, url);

  return new Response(html, {
    status: 200,
    headers: {
      "Content-Type": "text/html; charset=utf-8",
      "Cache-Control": "no-store",
      // Never let a CDN or proxy hold on to a paywall response and hand it to
      // a subscriber, or hold on to a lesson and hand it to a stranger.
      "Vary": "Cookie",
    },
  });
}

/** The generated per-lesson title/description map, cached at the edge. */
async function getLessonMeta(request, url, env, ctx) {
  const cacheKey = new Request(`${url.origin}/__internal/lesson-meta`);
  const cache = caches.default;
  const hit = await cache.match(cacheKey);
  if (hit) {
    try {
      return await hit.json();
    } catch {
      /* fall through */
    }
  }
  try {
    const res = await env.ASSETS.fetch(new Request(`${url.origin}/lesson-meta.json`));
    if (!res.ok) return null;
    const text = await res.text();
    const data = JSON.parse(text);
    const store = new Response(text, {
      headers: { "Content-Type": "application/json", "Cache-Control": "max-age=300" },
    });
    if (ctx && ctx.waitUntil) ctx.waitUntil(cache.put(cacheKey, store));
    return data;
  } catch {
    // No metadata is not a failure — the gate still works, it is just generic.
    return null;
  }
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, (c) =>
    ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

/**
 * Fill the gate page's slots with this lesson's own words. Everything is
 * escaped: the values come from a database row, and a lesson title with an
 * ampersand in it should not be able to close a tag.
 */
function personaliseGate(html, m, url) {
  const title = escapeHtml(m.title || "");
  const desc = escapeHtml(m.description || "");
  const level = escapeHtml(m.level || "");
  const canonical = `${url.origin}${url.pathname}`;
  const image = m.image ? `${url.origin}${m.image}` : "";

  const ld = {
    "@context": "https://schema.org",
    "@type": "LearningResource",
    name: m.title,
    description: m.description,
    url: canonical,
    inLanguage: "en",
    learningResourceType: "lesson",
    isAccessibleForFree: false,
    hasPart: { "@type": "WebPageElement", isAccessibleForFree: false, cssSelector: ".paywalled" },
    provider: { "@type": "Organization", name: "Forbes English", url: `${url.origin}/` },
  };
  if (m.level) ld.educationalLevel = m.level;
  if (image) ld.image = image;

  const head = [
    `<meta name="description" content="${desc}">`,
    `<link rel="canonical" href="${canonical}">`,
    `<meta property="og:type" content="article">`,
    `<meta property="og:site_name" content="Forbes English">`,
    // The row now carries the plain title, so the brand is added here, in the
    // one place that decides how a gate page is labelled.
    `<meta property="og:title" content="${title} | Forbes English">`,
    `<meta property="og:description" content="${desc}">`,
    `<meta property="og:url" content="${canonical}">`,
    image ? `<meta property="og:image" content="${image}">` : "",
    `<meta name="twitter:card" content="summary_large_image">`,
    `<script type="application/ld+json">${JSON.stringify(ld)}</script>`,
  ].filter(Boolean).join("\n");

  const intro = [
    `<div class="eyebrow">Subscribers only${level ? ` &middot; ${level}` : ""}</div>`,
    `<h1>${title}</h1>`,
    `<p class="lede">${desc}</p>`,
    `<p class="lede paywalled">The lesson itself &mdash; every slide, every exercise and`,
    ` the answers &mdash; is part of Forbes English Pro. Plenty of the library is free`,
    ` and always will be.</p>`,
  ].join("");

  return html
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${title} | Forbes English</title>`)
    .replace("<!-- LESSON:head -->", head)
    .replace(/<!-- LESSON:intro -->[\s\S]*?<!-- \/LESSON:intro -->/,
             `<!-- LESSON:intro -->${intro}<!-- /LESSON:intro -->`);
}

// ─────────────────────────────────────────────────────────────────────────
// GET /api/paywall-status  — is the gate actually on?
// ─────────────────────────────────────────────────────────────────────────

async function handlePaywallStatus(request, url, env, ctx) {
  const proFiles = await getProFiles(env, ctx);
  const sample = "forbes-c1-negotiation.html";

  const report = {
    // Deliberately NOT reported: whether page requests reach this Worker.
    // The Worker cannot answer that about itself — a subrequest to its own
    // hostname is refused (it comes back 522), and "you are reading this"
    // proves nothing, because /api/* reaches the Worker even when nothing
    // else does. Verify it from a browser instead; see verifyBy below.
    hasSupabaseUrl: Boolean(env.SUPABASE_URL),
    hasAnonKey: Boolean(env.SUPABASE_ANON_KEY),
    hasServiceRoleKey: Boolean(env.SUPABASE_SERVICE_ROLE_KEY),
    catalogueReadable: proFiles !== null,
    proLessonCount: proFiles ? proFiles.size : null,
    sampleLessonIsGated: proFiles ? proFiles.has(sample) : null,
    callerHasSessionCookie: Boolean(readCookie(request.headers.get("Cookie"), SESSION_COOKIE)),
    callerSubscribed: await hasActiveSubscription(request, env),
  };

  report.configOk =
    report.hasAnonKey && report.catalogueReadable && report.proLessonCount > 0;
  report.note = report.configOk
    ? "Everything this Worker can check is correct. Whether the gate actually " +
      "runs depends on requests reaching the Worker at all — verify that from a browser."
    : !report.hasAnonKey
    ? "SUPABASE_ANON_KEY is missing from the Worker environment."
    : !report.catalogueReadable
    ? "The Worker could not read the lessons table from Supabase."
    : "No lessons are marked access='pro'.";
  report.verifyBy =
    "Open a pro lesson in a private window. The subscribe page instead of the " +
    "gate is live. 200 with the lesson = requests are bypassing the Worker; " +
    "check run_worker_first in wrangler.toml, which is what makes Workers " +
    "Static Assets stop serving existing files before the Worker sees them.";

  return json(report);
}

// ─────────────────────────────────────────────────────────────────────────
// POST /api/create-checkout-session
// ─────────────────────────────────────────────────────────────────────────

async function handleCreateCheckoutSession(request, env) {
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "Invalid JSON body" }, 400);
  }

  const { userId, userEmail, plan } = body;
  if (!userId || !userEmail) {
    return json({ error: "userId and userEmail are required" }, 400);
  }

  const envKey = PLAN_ENV_KEYS[plan];
  if (!envKey) {
    return json({ error: `plan must be one of: ${Object.keys(PLAN_ENV_KEYS).join(", ")}` }, 400);
  }

  const priceId = env[envKey];
  if (!priceId) {
    return json({ error: `Server is missing the ${envKey} environment variable` }, 500);
  }

  const params = new URLSearchParams({
    mode: "subscription",
        "managed_payments[enabled]": "false",
    "line_items[0][price]": priceId,
    "line_items[0][quantity]": "1",
    customer_email: userEmail,
    "metadata[supabase_user_id]": userId,
    "metadata[plan]": plan,
    "subscription_data[metadata][supabase_user_id]": userId,
    "subscription_data[metadata][plan]": plan,
    success_url: `${env.SITE_URL}/account.html?checkout=success`,
    cancel_url: `${env.SITE_URL}/account.html?checkout=cancelled`,
  });

  const stripeRes = await fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: params,
  });

  if (!stripeRes.ok) {
    const errText = await stripeRes.text();
    return json({ error: "Stripe error", detail: errText }, 502);
  }

  const session = await stripeRes.json();
  return json({ url: session.url });
}

// ─────────────────────────────────────────────────────────────────────────
// POST /api/stripe-webhook
// ─────────────────────────────────────────────────────────────────────────

async function handleStripeWebhook(request, env) {
  const signature = request.headers.get("stripe-signature");
  const rawBody = await request.text();

  const isValid = await verifyStripeSignature(rawBody, signature, env.STRIPE_WEBHOOK_SECRET);
  if (!isValid) {
    return new Response("Invalid signature", { status: 400 });
  }

  const event = JSON.parse(rawBody);

  switch (event.type) {
    case "checkout.session.completed": {
      const session = event.data.object;
      const userId = session.metadata?.supabase_user_id;
      const plan = session.metadata?.plan;
      if (userId) {
        await updateProfile(env, userId, {
          stripe_customer_id: session.customer,
          stripe_subscription_id: session.subscription,
          subscription_status: "active",
          ...(plan ? { plan } : {}),
        });
      }
      break;
    }
    case "customer.subscription.updated": {
      const sub = event.data.object;
      const plan = sub.metadata?.plan;
      await updateProfileByCustomer(env, sub.customer, {
        subscription_status: sub.status,
        current_period_end: new Date(sub.current_period_end * 1000).toISOString(),
        ...(plan ? { plan } : {}),
      });
      break;
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object;
      await updateProfileByCustomer(env, sub.customer, {
        subscription_status: "canceled",
      });
      break;
    }
    default:
      // Ignore anything we haven't subscribed to.
      break;
  }

  return json({ received: true });
}

async function updateProfile(env, userId, fields) {
  await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?id=eq.${userId}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

async function updateProfileByCustomer(env, stripeCustomerId, fields) {
  await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?stripe_customer_id=eq.${stripeCustomerId}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

function supabaseHeaders(env) {
  return {
    "apikey": env.SUPABASE_SERVICE_ROLE_KEY,
    "Authorization": `Bearer ${env.SUPABASE_SERVICE_ROLE_KEY}`,
    "Content-Type": "application/json",
    "Prefer": "return=minimal",
  };
}

// Verifies the `Stripe-Signature` header using the raw request body, per
// https://stripe.com/docs/webhooks#verify-manually — implemented with the
// Web Crypto API since Cloudflare Workers don't have Node's `crypto`.
async function verifyStripeSignature(rawBody, signatureHeader, webhookSecret) {
  if (!signatureHeader || !webhookSecret) return false;

  const parts = Object.fromEntries(
    signatureHeader.split(",").map((pair) => pair.split("="))
  );
  const timestamp = parts.t;
  const expectedSig = parts.v1;
  if (!timestamp || !expectedSig) return false;

  const signedPayload = `${timestamp}.${rawBody}`;
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(webhookSecret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sigBuffer = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(signedPayload));
  const computedSig = [...new Uint8Array(sigBuffer)]
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");

  return computedSig === expectedSig;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}
