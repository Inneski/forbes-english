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
// The one-off products (pricing go-live, 2026-10-04; IDs in docs/HANDOFF.md).
// Checkout for a product whose price is unset answers 500 and nothing else
// changes:
//   STRIPE_PRICE_ID_BLOCKCAMP       €19, Block Camp Term 1
//   STRIPE_PRICE_ID_IELTS           €25, IELTS
//   STRIPE_PRICE_ID_IELTS_MARKING   €69, IELTS + two marked essays
//   STRIPE_PRICE_ID_MARKING         €49, two marked essays on any account
//   STRIPE_PROMO_FOUNDER            promo_… for FOUNDER (€7 off Term 1, 50 uses)
// Optional: MARKING_MAIL, a Cloudflare send_email binding, plus
// MARKING_MAIL_FROM — the marking inbox is told when credits are bought.

// Email Routing's message type, for the marking-inbox note (notifyMarking).
import { EmailMessage } from "cloudflare:email";

const PLAN_ENV_KEYS = {
  monthly: "STRIPE_PRICE_ID_MONTHLY",
  semiannual: "STRIPE_PRICE_ID_SEMIANNUAL",
  annual: "STRIPE_PRICE_ID_ANNUAL",
};

// What the pricing page can buy, by the key its buttons send. All are single
// payments through Managed Payments (Stripe as seller of record: it charges
// and remits the VAT). What a purchase grants is read back from the Stripe
// *product's* metadata in the webhook, not from this table, so a Payment
// Link sold outside this page grants the same thing.
const CHECKOUT_PRODUCTS = {
  blockcamp:     { envKey: "STRIPE_PRICE_ID_BLOCKCAMP", founder: true },
  ielts:         { envKey: "STRIPE_PRICE_ID_IELTS" },
  ielts_marking: { envKey: "STRIPE_PRICE_ID_IELTS_MARKING" },
  marking:       { envKey: "STRIPE_PRICE_ID_MARKING" },
};

// The tracks a `user_plans` row opens, by its `product`. The full plan (held
// on `profiles`) opens every track, Sherpa Tensing included; a one-off opens
// only its own. Marking opens no lessons: it only carries credits.
// A lesson's track is `lessons.track` (deploy/schema-tracks.sql).
const PLAN_TRACKS = {
  blockcamp: ["blockcamp"],
  ielts: ["ielts"],
  marking: [],
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

    // The founder offer's places left, for the pricing page's strip.
    if (url.pathname === "/api/founder-status") {
      return handleFounderStatus(env, ctx);
    }

    // ── RETIRED URLS ─────────────────────────────────────────────────
    // The three FireShield pages were merged into one lesson on 2026-09-07.
    // Students have bookmarks and Google has the old URLs, so they redirect
    // rather than 404. Permanent, so crawlers move their weight across.
    {
      const retired = {
        "/fireshield-pitch-roleplay.html": "/fireshield-pitch.html",
        "/fireshield-pitch-part2.html":    "/fireshield-pitch.html",
        "/fireshield-pitch-part3.html":    "/fireshield-pitch.html",
      };
      const to = retired[url.pathname] || retired[url.pathname + ".html"];
      if (to) return Response.redirect(url.origin + to, 301);
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
    return withRanges(request, await env.ASSETS.fetch(request));
  },
};

/**
 * Byte ranges for audio and video. The asset binding answers a Range request
 * with the whole file and a 200 (measured 2026-09-22 on
 * BlockCamp/hub-flythrough.mp4), and Safari will not play a <video> it
 * cannot fetch by range: it asks for bytes=0-1 first and gives up on a 200.
 * So for media, and only media, the range is cut here. Anything the header
 * does not describe as one plain range gets the whole file, which the spec
 * allows; only a range past the end is a 416.
 */
async function withRanges(request, res) {
  if (res.status !== 200 || !/^(video|audio)\//.test(res.headers.get("Content-Type") || "")) return res;
  const m = /^bytes=(\d*)-(\d*)$/.exec((request.headers.get("Range") || "").trim());
  if (request.method !== "GET" || !m || (m[1] === "" && m[2] === "")) {
    const out = new Response(res.body, res);
    out.headers.set("Accept-Ranges", "bytes");
    return out;
  }
  const body = await res.arrayBuffer();
  const size = body.byteLength;
  const start = m[1] === "" ? Math.max(size - Number(m[2]), 0) : Number(m[1]);   // "-500" = the last 500
  const end = m[1] === "" || m[2] === "" ? size - 1 : Math.min(Number(m[2]), size - 1);
  if (start >= size || start > end) {
    return new Response(null, { status: 416, headers: { "Content-Range": `bytes */${size}` } });
  }
  const headers = new Headers(res.headers);
  headers.delete("Content-Encoding");
  headers.set("Accept-Ranges", "bytes");
  headers.set("Content-Range", `bytes ${start}-${end}/${size}`);
  headers.set("Content-Length", String(end - start + 1));
  return new Response(body.slice(start, end + 1), { status: 206, headers });
}

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

  if ((await callerAccess(request, env)).covers(proFiles.get(file))) {
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
  // Lessons sit at the root or one directory down (block-camp/<slug>.html --
  // the RPGs). The catalogue stores that path with its directory, so the
  // returned name has to keep it. Until 2026-09-08 any path with a slash
  // returned null here, which meant every Pro RPG was served ungated while
  // wearing a Pro badge. Deeper paths are picture and slide directories.
  if (p.split("/").length > 2) return null;
  if (p.toLowerCase().endsWith(".html")) return p;
  if (/\.[a-z0-9]{2,5}$/i.test(p)) return null; // an image, a PDF, a script
  return `${p}.html`;
}

/**
 * The lesson filenames that require a subscription, mapped to their track, read from the
 * `lessons` table and cached at the edge. Cached for five minutes so flipping
 * a lesson to free in the database takes effect without a deploy, while a
 * burst of traffic does not become a burst of Supabase queries.
 */
async function getProFiles(env, ctx) {
  // v2: the cached body became [file, track] pairs when tracks arrived; a new
  // key means a stale v1 array is never read as pairs.
  const cacheKey = new Request(`${env.SITE_URL}/__internal/pro-lessons-v2`);
  const cache = caches.default;

  const cached = await cache.match(cacheKey);
  if (cached) {
    try {
      return new Map(await cached.json());
    } catch {
      /* fall through and re-fetch */
    }
  }

  let files;
  try {
    const res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/lessons?select=file,track&access=eq.pro`,
      { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${env.SUPABASE_ANON_KEY}` } }
    );
    if (!res.ok) return null;
    files = (await res.json()).map((r) => [r.file, r.track || "general"]);
  } catch {
    return null;
  }

  const body = JSON.stringify(files);
  const toCache = new Response(body, {
    headers: { "Content-Type": "application/json", "Cache-Control": "max-age=300" },
  });
  if (ctx && ctx.waitUntil) ctx.waitUntil(cache.put(cacheKey, toCache));
  return new Map(files);
}

/**
 * What the caller may open. Verifies the Supabase session and reads their
 * access with their own token: PostgREST rejects an invalid or expired token
 * outright, and the row-level policies on `profiles` and `user_plans` mean
 * the rows that come back can only ever be the caller's own.
 *
 * Returns { full, tracks, covers(track) }. `full` is the owner or an active
 * whole-library subscription; `tracks` is what the standalone plans add.
 */
const NO_ACCESS = { full: false, tracks: new Set(), covers: () => false };

async function callerAccess(request, env) {
  const token = readCookie(request.headers.get("Cookie"), SESSION_COOKIE);
  if (!token) return NO_ACCESS;
  const headers = { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}` };

  // Read in parallel, fail separately: a missing table or a failed read of
  // user_plans costs the standalone plans only, never a full subscriber.
  const plansRead = fetch(`${env.SUPABASE_URL}/rest/v1/user_plans?select=product,status,ends_at`, { headers })
    .then((r) => (r.ok ? r.json() : []))
    .catch(() => []);
  let profile;
  try {
    const pr = await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?select=subscription_status,owner&limit=1`, { headers });
    if (!pr.ok) return NO_ACCESS;           // a bad token fails here
    profile = (await pr.json())[0];
  } catch {
    return NO_ACCESS;
  }
  const plans = await plansRead;
  if (!profile) return NO_ACCESS;

  // `owner` is deliberately separate from subscription_status: the person who
  // runs the site should not lose access to it because of a billing event.
  const full = profile.owner === true || ACTIVE_STATUSES.has(profile.subscription_status);
  const tracks = new Set();
  const now = Date.now();
  for (const p of Array.isArray(plans) ? plans : []) {
    if (!ACTIVE_STATUSES.has(p.status)) continue;
    if (p.ends_at && Date.parse(p.ends_at) <= now) continue;
    for (const t of PLAN_TRACKS[p.product] || []) tracks.add(t);
  }
  return { full, tracks, covers: (track) => full || tracks.has(track) };
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
// Which plans open a lesson, by its track (lesson-meta.json carries it from
// lessons.track). Must agree with PLAN_TRACKS above and with pricing.html.
const PLAN_LINE = {
  general:   "is part of Forbes English Pro.",
  blockcamp: "is part of Block Camp Term 1, and of Forbes English Pro.",
  ielts:     "is part of IELTS, and of Forbes English Pro.",
  sherpa:    "is part of Forbes English Pro.",
};

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
  // What the lesson teaches, in its own rule sentences — lifted from the
  // teach cards by tools/seo.py. It is printed on the page below as well,
  // because a crawler and a visitor must see the same words.
  const teaches = Array.isArray(m.teaches) ? m.teaches.filter((t) => typeof t === "string").slice(0, 8) : [];
  const hubs = Array.isArray(m.topics) ? m.topics.filter((t) => t && t.url && t.name) : [];
  if (teaches.length) ld.teaches = teaches;
  if (hubs.length) ld.isPartOf = hubs.map((t) => ({ "@type": "Collection", name: `${t.name} lessons`, url: `${url.origin}${t.url}` }));

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
    // The public excerpt. This is the part of a gated page that has
    // something to rank on: the rules the deck states, in the deck's own
    // words, and the topic pages where the free lessons on the same point
    // are. Without it a Pro lesson's page is a title and two sentences.
    teaches.length
      ? `<section class="teaches"><h2>What this lesson teaches</h2><ul>${teaches
          .map((t) => `<li>${escapeHtml(t)}</li>`).join("")}</ul></section>`
      : "",
    hubs.length
      ? `<p class="topics">More on this: ${hubs
          .map((t) => `<a href="${escapeHtml(t.url)}">${escapeHtml(t.name)}</a>`)
          .join(" &middot; ")}${level ? ` &middot; <a href="/level-checker.html">Check your level</a>` : ""}</p>`
      : "",
    `<p class="lede paywalled">The lesson itself &mdash; every slide, every exercise and`,
    ` the answers &mdash; ${PLAN_LINE[m.track] || PLAN_LINE.general}`,
    ` Plenty of the library is free and always will be.</p>`,
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
  const access = await callerAccess(request, env);

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
    callerSubscribed: access.full,
    callerTracks: [...access.tracks],
    hasBlockCampPrice: Boolean(env.STRIPE_PRICE_ID_BLOCKCAMP),
    hasIeltsPrice: Boolean(env.STRIPE_PRICE_ID_IELTS),
    hasIeltsMarkingPrice: Boolean(env.STRIPE_PRICE_ID_IELTS_MARKING),
    hasMarkingPrice: Boolean(env.STRIPE_PRICE_ID_MARKING),
    hasFounderPromo: Boolean(env.STRIPE_PROMO_FOUNDER),
    hasMarkingMail: Boolean(env.MARKING_MAIL && env.MARKING_MAIL_FROM),
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

  const { userId, userEmail, plan, product } = body;
  if (!userId || !userEmail) {
    return json({ error: "userId and userEmail are required" }, 400);
  }
  if (product) return createProductCheckout(env, userId, userEmail, product);

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
    // Back to where they started: account.html ignores ?checkout=cancelled,
    // pricing.html says "no charge was made".
    cancel_url: `${env.SITE_URL}/pricing.html?checkout=cancelled`,
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

/**
 * Checkout for a one-off product (Block Camp Term 1, IELTS, IELTS + Marking,
 * Marking). Kept apart from the full plan so the full plan's params are
 * untouched. Every product is a single payment through Managed Payments:
 * Stripe is the seller of record, charges the VAT inside the VAT-inclusive
 * price and remits it, and sends the receipt. Managed Payments forbids the
 * tax, payment-method, shipping and receipt-email parameters, so none are
 * sent. Block Camp gets the FOUNDER code applied for the buyer while places
 * remain; nobody has to type it.
 */
async function createProductCheckout(env, userId, userEmail, product) {
  const def = CHECKOUT_PRODUCTS[product];
  if (!def) {
    return json({ error: `product must be one of: ${Object.keys(CHECKOUT_PRODUCTS).join(", ")}` }, 400);
  }
  const priceId = env[def.envKey];
  if (!priceId) {
    return json({ error: `Server is missing the ${def.envKey} environment variable` }, 500);
  }

  const params = new URLSearchParams({
    mode: "payment",
    "managed_payments[enabled]": "true",
    "line_items[0][price]": priceId,
    "line_items[0][quantity]": "1",
    customer_email: userEmail,
    "metadata[supabase_user_id]": userId,
    "metadata[product]": product,
    success_url: `${env.SITE_URL}/account.html?checkout=success`,
    cancel_url: `${env.SITE_URL}/pricing.html?checkout=cancelled`,
  });

  const founder = def.founder && env.STRIPE_PROMO_FOUNDER ? await getFounderStatus(env) : null;
  if (founder && founder.remaining > 0) {
    params.set("discounts[0][promotion_code]", env.STRIPE_PROMO_FOUNDER);
  }

  let stripeRes = await createCheckoutSession(env, params);
  // The last founder place can go between the count and this call. Stripe
  // then refuses the code; the buyer still gets a checkout, at €19, rather
  // than an error.
  if (!stripeRes.ok && params.has("discounts[0][promotion_code]")) {
    params.delete("discounts[0][promotion_code]");
    stripeRes = await createCheckoutSession(env, params);
  }
  if (!stripeRes.ok) {
    return json({ error: "Stripe error", detail: await stripeRes.text() }, 502);
  }
  return json({ url: (await stripeRes.json()).url });
}

function createCheckoutSession(env, params) {
  return fetch("https://api.stripe.com/v1/checkout/sessions", {
    method: "POST",
    headers: {
      "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}`,
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: params,
  });
}

// ─────────────────────────────────────────────────────────────────────────
// GET /api/founder-status  — the founder offer's places left
// ─────────────────────────────────────────────────────────────────────────

/**
 * Reads the FOUNDER promotion code from Stripe: its limit and how often it
 * has been redeemed. Cached for a minute at the edge, so a busy pricing page
 * is not a Stripe request per visitor. Anything other than a clean read is
 * null, and the page then shows the plain €19: it must never advertise an
 * offer that may have run out.
 */
async function getFounderStatus(env, ctx) {
  if (!env.STRIPE_PROMO_FOUNDER || !env.STRIPE_SECRET_KEY) return null;
  const cacheKey = new Request(`${env.SITE_URL}/__internal/founder-status-v1`);
  const cache = typeof caches !== "undefined" ? caches.default : null;
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) {
      try { return await hit.json(); } catch { /* re-read */ }
    }
  }
  let status;
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/promotion_codes/${encodeURIComponent(env.STRIPE_PROMO_FOUNDER)}`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } }
    );
    if (!res.ok) return null;
    const promo = await res.json();
    const limit = Number(promo.max_redemptions);
    const used = Number(promo.times_redeemed) || 0;
    if (!(limit > 0)) return null;
    status = { limit, remaining: promo.active ? Math.max(0, limit - used) : 0 };
  } catch {
    return null;
  }
  if (cache) {
    const put = cache.put(cacheKey, new Response(JSON.stringify(status), {
      headers: { "Content-Type": "application/json", "Cache-Control": "max-age=60" },
    }));
    if (ctx && ctx.waitUntil) ctx.waitUntil(put); else await put;
  }
  return status;
}

async function handleFounderStatus(env, ctx) {
  const status = await getFounderStatus(env, ctx);
  if (!status) return json({ error: "Founder status unavailable" }, 503);
  return new Response(JSON.stringify(status), {
    headers: { "Content-Type": "application/json", "Cache-Control": "public, max-age=60" },
  });
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
  // A write that fails answers 500, so Stripe redelivers the event (it
  // retries for three days). Until 2026-10-04 every write's result was
  // ignored and the webhook said 200 regardless: a Supabase hiccup at the
  // wrong moment was a sale that never granted anything.
  const failed = () => new Response("Could not record the event; Stripe will retry", { status: 500 });

  switch (event.type) {
    case "checkout.session.completed":
    case "checkout.session.async_payment_succeeded": {
      const session = event.data.object;
      const userId = session.metadata?.supabase_user_id;

      if (session.mode === "payment") {
        // A delayed method (a bank debit) completes the session unpaid and
        // pays later; the grant waits for async_payment_succeeded.
        if (session.payment_status !== "paid" && session.payment_status !== "no_payment_required") break;
        // A sale not started from the site (no signed-in user) has nothing
        // to attach to. It is in the Stripe dashboard; nothing to do here.
        if (!userId) break;
        if (!(await grantOneOff(env, event, session, userId))) return failed();
        break;
      }

      // The full plan: a subscription, held on the profile as before.
      if (event.type !== "checkout.session.completed" || !userId) break;
      const plan = session.metadata?.plan;
      const ok = await updateProfile(env, userId, {
        stripe_customer_id: session.customer,
        stripe_subscription_id: session.subscription,
        subscription_status: "active",
        ...(plan ? { plan } : {}),
      });
      if (!ok) return failed();
      break;
    }
    case "customer.subscription.updated": {
      const sub = event.data.object;
      const plan = sub.metadata?.plan;
      // A standalone subscription updates its own row. None is sold any more
      // (every product is one-off since 2026-10-04); kept so a row made by
      // the 2026-09-28 plans can still be closed.
      if (sub.metadata?.product) {
        if (!(await updateUserPlanBySubscription(env, sub.id, { status: sub.status }))) return failed();
        break;
      }
      // Since Stripe API 2025-03-31 the period end lives on the subscription
      // item, not the subscription. Reading sub.current_period_end gave
      // undefined -> Invalid Date -> toISOString() threw, so every
      // subscription.updated event would have 500'd. Fall back to the old
      // field for older payloads, and skip the date rather than crash.
      const periodEnd = sub.items?.data?.[0]?.current_period_end ?? sub.current_period_end;
      const ok = await updateProfileByCustomer(env, sub.customer, {
        subscription_status: sub.status,
        ...(typeof periodEnd === "number"
          ? { current_period_end: new Date(periodEnd * 1000).toISOString() }
          : {}),
        ...(plan ? { plan } : {}),
      });
      if (!ok) return failed();
      break;
    }
    case "customer.subscription.deleted": {
      const sub = event.data.object;
      if (sub.metadata?.product) {
        if (!(await updateUserPlanBySubscription(env, sub.id, { status: "canceled" }))) return failed();
        break;
      }
      if (!(await updateProfileByCustomer(env, sub.customer, { subscription_status: "canceled" }))) return failed();
      break;
    }
    default:
      // Ignore anything we haven't subscribed to.
      break;
  }

  return json({ received: true });
}

/**
 * Records a one-off purchase as a `user_plans` row. What it grants comes
 * from the Stripe product's metadata (set in the dashboard; see the table in
 * docs/HANDOFF.md): `product` (blockcamp | ielts | marking), `term`, and
 * `marking_credits`. One row per purchase, keyed by the Checkout Session, so
 * a redelivered event is a no-op: a marking add-on is a new row with its two
 * credits rather than "+2" on an older row, because an increment cannot be
 * made safe against redelivery. An account's credits are the sum of its rows.
 * Nothing bought here expires (Innes, 2026-10-04): ends_at stays null.
 * Returns false only when the purchase could not be recorded.
 */
async function grantOneOff(env, event, session, userId) {
  let items;
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(session.id)}/line_items?expand[]=data.price.product&limit=10`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } }
    );
    if (!res.ok) return false;
    items = (await res.json()).data || [];
  } catch {
    return false;
  }

  const item = items.find((li) => {
    const p = String(li.price?.product?.metadata?.product || "").trim().toLowerCase();
    return Object.prototype.hasOwnProperty.call(PLAN_TRACKS, p);
  });
  // A paid session whose product carries no recognised metadata is a
  // dashboard mistake, not a retryable failure: say so in the log and stop.
  if (!item) {
    console.error(`checkout ${session.id}: no line item with product metadata blockcamp|ielts|marking`);
    return true;
  }

  const meta = item.price.product.metadata;
  const product = String(meta.product).trim().toLowerCase();
  const qty = Number(item.quantity) || 1;
  const credits = Math.max(0, parseInt(meta.marking_credits, 10) || 0) * qty;
  const term = parseInt(meta.term, 10);
  const paidAt = new Date((event.created || Date.now() / 1000) * 1000).toISOString();

  const inserted = await insertUserPlan(env, {
    user_id: userId,
    product,
    status: "active",
    stripe_checkout_session_id: session.id,
    // The weekly drip counts from here for a term buyer.
    starts_at: paidAt,
    ends_at: null,
    term: product === "blockcamp" ? (term > 0 ? term : 1) : null,
    marking_credits: credits,
  });
  if (inserted === null) return false;

  // Only a first delivery that actually made the row tells the marking
  // inbox; a redelivery would otherwise send the same email again.
  if (inserted && credits > 0) {
    await notifyMarking(env, {
      credits,
      productName: item.price.product.name || product,
      buyer: session.customer_details?.email || session.customer_email || "",
      userId,
      sessionId: session.id,
      paidAt,
    });
  }
  return true;
}

/**
 * Tells the marking inbox that essay credits were bought. Uses a Cloudflare
 * Email Routing `send_email` binding, which can only send to a verified
 * address on the forbesenglish.com zone (enough for Innes's own inbox; a
 * parent's address needs a real transactional sender). Without the binding
 * this is a no-op, and a mail failure never fails the purchase: Stripe's
 * own payment emails to the account owner are the backstop.
 */
async function notifyMarking(env, info) {
  if (!env.MARKING_MAIL || !env.MARKING_MAIL_FROM || !env.MARKING_MAIL_TO) return;
  const clean = (s) => String(s).replace(/[\r\n]+/g, " ").slice(0, 200);
  const raw = [
    `From: Forbes English <${clean(env.MARKING_MAIL_FROM)}>`,
    `To: <${clean(env.MARKING_MAIL_TO)}>`,
    `Subject: Marking bought: ${info.credits} essays (${clean(info.productName)})`,
    `Message-ID: <${clean(info.sessionId)}@forbesenglish.com>`,
    `Date: ${new Date().toUTCString()}`,
    "MIME-Version: 1.0",
    "Content-Type: text/plain; charset=utf-8",
    "Content-Transfer-Encoding: 8bit",
    "",
    `${clean(info.buyer) || "A buyer"} bought ${clean(info.productName)}: ${info.credits} essays to mark.`,
    "",
    `Paid: ${info.paidAt}`,
    `Supabase user: ${clean(info.userId)}`,
    `Stripe checkout: ${clean(info.sessionId)}`,
    "",
  ].join("\r\n");
  try {
    await env.MARKING_MAIL.send(new EmailMessage(env.MARKING_MAIL_FROM, env.MARKING_MAIL_TO, raw));
  } catch (err) {
    console.error("marking email failed:", err && err.message);
  }
}

// Each write reports whether it landed, so the webhook can ask Stripe to
// redeliver instead of dropping a purchase.
async function supabaseWrite(url, init) {
  try {
    const res = await fetch(url, init);
    return res.ok;
  } catch {
    return false;
  }
}

function updateProfile(env, userId, fields) {
  return supabaseWrite(`${env.SUPABASE_URL}/rest/v1/profiles?id=eq.${encodeURIComponent(userId)}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

function updateProfileByCustomer(env, stripeCustomerId, fields) {
  return supabaseWrite(`${env.SUPABASE_URL}/rest/v1/profiles?stripe_customer_id=eq.${encodeURIComponent(stripeCustomerId)}`, {
    method: "PATCH",
    headers: supabaseHeaders(env),
    body: JSON.stringify(fields),
  });
}

/**
 * Inserts a user_plans row, ignoring a duplicate Checkout Session (a
 * redelivered webhook). Returns true when a row was made, false when it
 * already existed, and null when the write failed.
 */
async function insertUserPlan(env, row) {
  try {
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/user_plans?on_conflict=stripe_checkout_session_id`, {
      method: "POST",
      headers: { ...supabaseHeaders(env), "Prefer": "return=representation,resolution=ignore-duplicates" },
      body: JSON.stringify(row),
    });
    if (!res.ok) return null;
    const rows = await res.json().catch(() => []);
    return Array.isArray(rows) && rows.length > 0;
  } catch {
    return null;
  }
}

function updateUserPlanBySubscription(env, stripeSubscriptionId, fields) {
  return supabaseWrite(`${env.SUPABASE_URL}/rest/v1/user_plans?stripe_subscription_id=eq.${encodeURIComponent(stripeSubscriptionId)}`, {
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
