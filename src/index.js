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
// Email (step 9): RESEND_API_KEY (a secret) and MAIL_FROM (an address on
// a domain verified in Resend) send the weekly "Mission N is open" email
// from the daily cron, and tell MARKING_MAIL_TO when essay credits are
// bought. Without them nothing is sent and nothing else changes. (A
// Cloudflare send_email binding, MARKING_MAIL + MARKING_MAIL_FROM, still
// works for the marking inbox alone.)
// TERMS_URL (the terms page): once set, checkout asks EU buyers to agree
// to the terms and to immediate access (see addConsent).

// Email Routing's message type, for the marking-inbox note (notifyMarking).
import { EmailMessage } from "cloudflare:email";

const PLAN_ENV_KEYS = {
  monthly: "STRIPE_PRICE_ID_MONTHLY",
  semiannual: "STRIPE_PRICE_ID_SEMIANNUAL",
  annual: "STRIPE_PRICE_ID_ANNUAL",
};

// What the pricing page can buy, by the key its buttons send. All are single
// payments. `managed` sends the sale through Managed Payments (Stripe as
// seller of record: it charges and remits the VAT). Stripe's eligibility
// rules exclude a product that "involves human intervention", which a
// teacher-marked essay is; whether the two marking products stay managed is
// Innes's call (docs/HANDOFF.md, pricing step 4). A sale with it off is
// taxed like the full plan: not at all by Stripe.
// What a purchase grants is read back from the Stripe *product's* metadata
// in the webhook, not from this table. The buyer's account comes only from
// the session's metadata.supabase_user_id, which this checkout sets: an
// anonymous Payment Link sale is charged but grants nothing (it is logged).
const CHECKOUT_PRODUCTS = {
  blockcamp:     { envKey: "STRIPE_PRICE_ID_BLOCKCAMP", managed: true, founder: true },
  ielts:         { envKey: "STRIPE_PRICE_ID_IELTS", managed: true },
  ielts_marking: { envKey: "STRIPE_PRICE_ID_IELTS_MARKING", managed: true },
  marking:       { envKey: "STRIPE_PRICE_ID_MARKING", managed: true },
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
  // The daily cron (wrangler.toml [triggers]): the weekly mission emails.
  async scheduled(event, env, ctx) {
    ctx.waitUntil(sendMissionEmails(env, event && event.scheduledTime ? event.scheduledTime : Date.now()));
  },

  async fetch(request, env, ctx) {
    const res = await route(request, env, ctx);
    // The funnel count (noteVisit) never changes or holds up a response.
    try { noteVisit(request, res, env, ctx); } catch { /* a lost count, never a lost page */ }
    return res;
  },
};

async function route(request, env, ctx) {
    const url = new URL(request.url);

    // www is the apex. One host for Google, one for cookies, one for the
    // Stripe return URLs (SITE_URL is the apex).
    if (url.hostname === "www.forbesenglish.com") {
      url.hostname = "forbesenglish.com";
      return Response.redirect(url.toString(), 301);
    }

    if (request.method === "POST" && url.pathname === "/api/create-checkout-session") {
      return handleCreateCheckoutSession(request, env, ctx);
    }

    if (request.method === "POST" && url.pathname === "/api/stripe-webhook") {
      return handleStripeWebhook(request, env, ctx);
    }

    // The success page of a checkout made without signing in: the account
    // the purchase went to, and a one-time sign-in into it when the purchase
    // made it (handleClaimCheckout).
    if (request.method === "POST" && url.pathname === "/api/claim-checkout") {
      return handleClaimCheckout(request, env, ctx);
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
        // live for one night under its first name; Innes renamed it 2026-10-06
        "/block-camp/sun-was-sinking-rpg.html": "/block-camp/welcome-to-the-jungle-rpg.html",
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
}

// ── THE FUNNEL ───────────────────────────────────────────────────────────
// What happens between an ad and a sale. Cloudflare Web Analytics counts
// visits; it cannot see a Buy click, a checkout or a payment, and two
// campaigns in October 2026 brought 274 visits and no sale with nothing to
// say where they stopped. A row is an event, never a person: no IP, no
// account id, no cookie (so nothing to consent to). Rows go to
// public.funnel_events in the background; a failed write loses a count,
// never a page. FUNNEL=off in the environment stops all of it.
// Read it with: select * from funnel_daily order by day desc;

// Pages worth counting every visit to: the doors into a sale. Anything else
// is counted only when it is a campaign landing (a utm_ tag or a click id).
const FUNNEL_PAGES = new Set(["/", "/pricing", "/block-camp", "/blockcamp-present-simple",
  "/block-camp/frostbound-river-rpg", "/ielts", "/account", "/library"]);
// Link previews and crawlers are not visitors (the Facebook in-app browser
// is: it says FBAN/FBAV, not facebookexternalhit).
const BOT_UA = /bot|crawl|spider|slurp|preview|externalhit|facebookcatalog|embedly|whatsapp|telegram|discord|slack|curl|wget|python|httpclient|headless|lighthouse|monitor|scanner/i;
const CLICK_IDS = ["fbclid", "gclid", "ttclid", "msclkid", "igshid"];

function recordEvent(env, ctx, row) {
  if (env.FUNNEL === "off" || !env.SUPABASE_URL || !env.SUPABASE_SERVICE_ROLE_KEY) return;
  const p = fetch(`${env.SUPABASE_URL}/rest/v1/funnel_events`, {
    method: "POST", headers: supabaseHeaders(env), body: JSON.stringify(row),
  }).then((r) => { if (!r.ok) console.error(`funnel: ${row.event} not recorded (HTTP ${r.status})`); })
    .catch((err) => console.error(`funnel: ${row.event} not recorded (${err && err.message})`));
  if (ctx && typeof ctx.waitUntil === "function") ctx.waitUntil(p);
}

// Where a request came from, without saying who: country (Cloudflare's
// two letters), phone or not, and the referring host.
function visitFields(request) {
  const ua = request.headers.get("User-Agent") || "";
  let refHost = null;
  try { refHost = new URL(request.headers.get("Referer") || "").hostname || null; } catch { /* no referrer */ }
  return {
    country: (request.cf && request.cf.country) || null,
    mobile: /Mobi|Android|iPhone|iPad/i.test(ua),
    ref_host: refHost,
  };
}

// A page view, counted if it is a campaign landing or one of FUNNEL_PAGES.
// Only a 200 answer to a browser asking for HTML: the .html → clean-URL
// redirect, images, the API and link previews are not visits.
function noteVisit(request, res, env, ctx) {
  if (request.method !== "GET" || !res || res.status !== 200) return;
  const url = new URL(request.url);
  if (url.pathname.startsWith("/api/")) return;
  const ua = request.headers.get("User-Agent") || "";
  if (!(request.headers.get("Accept") || "").includes("text/html") || !ua || BOT_UA.test(ua)) return;
  const path = url.pathname.replace(/\.html$/, "").replace(/\/index$/, "/") || "/";
  const q = url.searchParams;
  const click = CLICK_IDS.find((k) => q.has(k)) || null;
  const tag = (k) => (q.get(`utm_${k}`) || "").slice(0, 100) || null;
  const landing = Boolean(click || q.has("utm_source") || q.has("utm_campaign"));
  if (!landing && !FUNNEL_PAGES.has(path)) return;
  recordEvent(env, ctx, {
    event: landing ? "landing" : "view",
    path: path.slice(0, 200),
    utm_source: tag("source"), utm_medium: tag("medium"),
    utm_campaign: tag("campaign"), utm_content: tag("content"),
    click,
    ...visitFields(request),
  });
}

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
const WEEK_MS = 7 * 86400000;

/**
 * Returns a Response when the request is for a gated lesson the caller may
 * not have, or null to let the request continue to the static assets.
 */
async function gateLessonRequest(request, url, env, ctx) {
  if (request.method !== "GET" && request.method !== "HEAD") return null;

  const file = lessonFileFor(url.pathname);
  if (!file) return null;

  const catalogue = await getCatalogue(env, ctx);
  // Fail OPEN, not closed: if Supabase is unreachable we would rather serve a
  // pro lesson to a stranger than show every paying subscriber a paywall.
  if (!catalogue) return null;
  const lesson = catalogue.get(file);
  if (!lesson) return null;

  if (lesson.access !== "pro") {
    // A free Block Camp lesson (Mission 1) is where a subscriber's weekly
    // clock should start, so a signed-in visit is noted -- in the
    // background: the lesson goes out at once, it never waits on Supabase.
    // (block-camp/camp-full.js re-asks with a fresh cookie when the reader
    // arrived signed in but with the hour-long cookie already gone.)
    if (lesson.track === "blockcamp" && ctx && ctx.waitUntil &&
        readCookie(request.headers.get("Cookie"), SESSION_COOKIE)) {
      ctx.waitUntil(callerAccess(request, env)
        .then((access) => startBlockCampClock(access, env))
        .catch(() => {}));
    }
    return null;
  }

  const access = await callerAccess(request, env);
  const verdict = lesson.track === "blockcamp"
    ? blockCampVerdict(lesson, access, Date.now())
    : { open: access.covers(lesson.track) };
  if (verdict.startClock) {
    const write = startBlockCampClock(access, env);
    if (ctx && ctx.waitUntil) ctx.waitUntil(write);
  }

  if (verdict.open) {
    // Serve it, but marked private. A pro lesson must never sit in a shared
    // cache where the next person through gets it without the check.
    const res = await env.ASSETS.fetch(request);
    const out = new Response(res.body, res);
    out.headers.set("Cache-Control", "private, no-store");
    out.headers.set("Vary", "Cookie");
    return out;
  }

  return locked(request, url, env, ctx, lesson, verdict.notYet || null, access, catalogue);
}

/**
 * Block Camp opens one mission a week (Innes, 2026-10-03): a lesson tagged
 * mission M opens once M-1 whole weeks have passed since the clock started.
 * Owners are exempt. Two ways in, and either is enough:
 *
 *  - The full plan. The clock is profiles.blockcamp_first_open, set on the
 *    subscriber's first Block Camp visit. A lesson with no mission number
 *    (Term 2 until it is numbered, the mixed-tense specials) is not dripped.
 *  - A term bought outright (user_plans, product blockcamp). The clock is
 *    that row's starts_at, the moment of payment. Lessons tagged with the
 *    row's term and a mission open this way, a week at a time; a Term 1
 *    buyer does not get Term 2. The specials (no term) open at once.
 *
 * Returns { open } or { open: false, notYet: { mission, opensAt, openNow,
 * term } } when the caller holds the lesson but its week has not come
 * (openNow: the highest mission open on the clock that opens it soonest),
 * plus startClock when a subscriber's clock has not been started yet -- on
 * any Block Camp lesson they open, numbered or not.
 */
function blockCampVerdict(lesson, access, now) {
  if (access.owner) return { open: true };
  const mission = Number(lesson.mission) || null;
  const opensAfter = (start) => start + (mission - 1) * WEEK_MS;
  let notYet = null;
  const later = (start) => {
    const opensAt = opensAfter(start);
    if (!notYet || opensAt < notYet.opensAt) {
      notYet = { mission, opensAt, term: Number(lesson.term) || 1,
                 openNow: Math.floor((now - start) / WEEK_MS) + 1 };
    }
  };
  let startClock = false;

  if (access.full) {
    if (!mission) return { open: true, startClock: !access.blockCampFirstOpen };
    let start = access.blockCampFirstOpen;
    if (!start) { start = now; startClock = true; }
    if (now >= opensAfter(start)) return { open: true, startClock };
    later(start);
  }

  // The specials -- Block Camp lessons in no term (Grand Hotel, Nautilus
  // Deep, Dracula, the passive extras) -- come with any term bought, open
  // from day one (Innes, 2026-10-04). Tagging one into a term later would
  // take it away from buyers who already have it.
  if (!lesson.term && access.blockCampPlans.length) return { open: true, startClock };

  if (mission && lesson.term) {
    for (const plan of access.blockCampPlans) {
      if ((plan.term || 1) !== Number(lesson.term)) continue;
      if (now >= opensAfter(plan.startsAt)) return { open: true, startClock };
      later(plan.startsAt);
    }
  }
  return { open: false, notYet, startClock };
}

/**
 * Records a subscriber's first Block Camp visit, once. The browser cannot
 * write profiles (deploy/schema-pricing.sql), so this uses the service key;
 * the is.null filter makes it a no-op once set, however many requests race.
 */
function startBlockCampClock(access, env) {
  if (!access.full || access.owner || access.blockCampFirstOpen || !access.userId) return Promise.resolve(true);
  // Without the key the clock can never be saved, and a subscriber's
  // Mission 2 would never open: /api/paywall-status reports the key.
  if (!env.SUPABASE_SERVICE_ROLE_KEY) {
    console.error(`blockcamp clock not saved for ${access.userId}: SUPABASE_SERVICE_ROLE_KEY unset`);
    return Promise.resolve(false);
  }
  return fetch(
    `${env.SUPABASE_URL}/rest/v1/profiles?id=eq.${encodeURIComponent(access.userId)}&blockcamp_first_open=is.null`,
    { method: "PATCH", headers: supabaseHeaders(env), body: JSON.stringify({ blockcamp_first_open: new Date().toISOString() }) }
  ).then((res) => {
    if (!res.ok) console.error(`blockcamp clock not saved for ${access.userId}: PATCH profiles ${res.status}`);
    return res.ok;
  }).catch((err) => {
    console.error(`blockcamp clock not saved for ${access.userId}: ${err && err.message}`);
    return false;
  });
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
 * The lessons the gate has to look at: every pro lesson, plus every Block
 * Camp lesson (the free Mission 1 starts a subscriber's weekly clock), each
 * with its track, access, term and mission, read from the `lessons` table
 * and cached at the edge for five minutes, so flipping a lesson to free in
 * the database takes effect without a deploy, while a burst of traffic does
 * not become a burst of Supabase queries.
 */
async function getCatalogue(env, ctx) {
  // v3: rows became objects carrying access/term/mission (pricing go-live);
  // a new key means a stale v2 array of pairs is never read as rows.
  const cacheKey = new Request(`${env.SITE_URL}/__internal/gate-catalogue-v3`);
  const cache = caches.default;

  const cached = await cache.match(cacheKey);
  if (cached) {
    try {
      return new Map(await cached.json());
    } catch {
      /* fall through and re-fetch */
    }
  }

  let rows;
  try {
    const res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/lessons?select=file,track,access,term,mission&or=(access.eq.pro,track.eq.blockcamp)`,
      { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${env.SUPABASE_ANON_KEY}` } }
    );
    if (!res.ok) return null;
    rows = (await res.json()).map((r) => [r.file, {
      track: r.track || "general",
      access: r.access === "free" ? "free" : "pro",
      term: r.term ?? null,
      mission: r.mission ?? null,
    }]);
  } catch {
    return null;
  }

  const toCache = new Response(JSON.stringify(rows), {
    headers: { "Content-Type": "application/json", "Cache-Control": "max-age=300" },
  });
  if (ctx && ctx.waitUntil) ctx.waitUntil(cache.put(cacheKey, toCache));
  return new Map(rows);
}

/**
 * What the caller may open. Verifies the Supabase session and reads their
 * access with their own token: PostgREST rejects an invalid or expired token
 * outright, and the row-level policies on `profiles` and `user_plans` mean
 * the rows that come back can only ever be the caller's own.
 *
 * Returns { owner, full, tracks, covers(track), blockCampPlans,
 * blockCampFirstOpen, userId }. `full` is the owner or an active
 * whole-library subscription; `tracks` is what the one-off plans add;
 * `blockCampPlans` are the active Block Camp terms with their start times.
 */
const NO_ACCESS = {
  owner: false, full: false, tracks: new Set(), covers: () => false,
  blockCampPlans: [], blockCampFirstOpen: null, userId: null, checked: false,
};

async function callerAccess(request, env) {
  const token = readCookie(request.headers.get("Cookie"), SESSION_COOKIE);
  if (!token) return NO_ACCESS;
  const headers = { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}` };

  // Read in parallel, fail separately: a missing table or a failed read of
  // user_plans costs the one-off plans only, never a full subscriber.
  let plansOk = true;
  const plansRead = fetch(`${env.SUPABASE_URL}/rest/v1/user_plans?select=product,status,ends_at,starts_at,term`, { headers })
    .then((r) => (r.ok ? r.json() : (plansOk = false, [])))
    .catch(() => (plansOk = false, []));
  let profile;
  try {
    const pr = await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?select=id,subscription_status,owner,blockcamp_first_open&limit=1`, { headers });
    if (!pr.ok) return NO_ACCESS;           // a bad token fails here
    profile = (await pr.json())[0];
  } catch {
    return NO_ACCESS;
  }
  const plans = await plansRead;
  if (!profile) return NO_ACCESS;

  // `owner` is deliberately separate from subscription_status: the person who
  // runs the site should not lose access to it because of a billing event.
  const owner = profile.owner === true;
  const full = owner || ACTIVE_STATUSES.has(profile.subscription_status);
  const tracks = new Set();
  const blockCampPlans = [];
  const now = Date.now();
  for (const p of Array.isArray(plans) ? plans : []) {
    if (!ACTIVE_STATUSES.has(p.status)) continue;
    if (p.ends_at && Date.parse(p.ends_at) <= now) continue;
    for (const t of PLAN_TRACKS[p.product] || []) tracks.add(t);
    if (p.product === "blockcamp") {
      const startsAt = Date.parse(p.starts_at);
      if (Number.isFinite(startsAt)) blockCampPlans.push({ term: Number(p.term) || 1, startsAt });
    }
  }
  const firstOpen = profile.blockcamp_first_open ? Date.parse(profile.blockcamp_first_open) : NaN;
  return {
    owner, full, tracks, blockCampPlans,
    covers: (track) => full || tracks.has(track),
    blockCampFirstOpen: Number.isFinite(firstOpen) ? firstOpen : null,
    userId: profile.id || null,
    // Both reads came back with this caller's own rows: what the gate
    // decided from them is final, and the page's retry would change nothing.
    checked: plansOk,
  };
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
async function locked(request, url, env, ctx, lesson = null, notYet = null, access = NO_ACCESS, catalogue = null) {
  const page = await env.ASSETS.fetch(new Request(`${url.origin}/locked.html`));
  let html = page.ok ? await page.text() : "<h1>This lesson comes with a plan.</h1>";

  const file = lessonFileFor(url.pathname);
  const meta = await getLessonMeta(request, url, env, ctx);
  const m = file && meta ? meta[file] : null;
  html = personaliseGate(html, m, url, lesson, notYet, access, catalogue);

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
// What a lesson belongs to, for the gate page's label: Block Camp Term 1
// (its own missions and the specials), IELTS, or Forbes English Pro.
function planName(track, term) {
  if (track === "blockcamp" && (Number(term) === 1 || !term)) return "Block Camp Term 1";
  if (track === "ielts") return "IELTS";
  return "Forbes English Pro";
}

// Which plans open a lesson, by its track and, for Block Camp, its term (the
// gate's own catalogue row; lesson-meta.json as the fallback). Must agree
// with PLAN_TRACKS above and with pricing.html. Only Term 1 is on sale.
function planLine(track, term) {
  // Term 1 and the specials (no term) both come with Block Camp Term 1.
  if (track === "blockcamp" && (Number(term) === 1 || !term)) return "is part of Block Camp Term 1, and of Forbes English Pro.";
  if (track === "ielts") return "is part of IELTS, and of Forbes English Pro.";
  return "is part of Forbes English Pro.";
}

function personaliseGate(html, m, url, lesson = null, notYet = null, access = NO_ACCESS, catalogue = null) {
  const checked = Boolean(access && access.checked);
  if (!m) {
    // No metadata row: the page stays generic, but its script still needs
    // to know what it is gating and whether the answer is final.
    if (!notYet) {
      const flags = gateFlags(lesson, {}, null, checked);
      html = html.replace("<!-- LESSON:head -->", flags);
      return checked ? finalOffer(html) : html;
    }
    m = {};
  }
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
    `<div class="eyebrow">${planName(lesson ? lesson.track : m.track, lesson ? lesson.term : null)}${level ? ` &middot; ${level}` : ""}</div>`,
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
    ` the answers &mdash; ${planLine(lesson ? lesson.track : m.track, lesson ? lesson.term : null)}`,
    ` Plenty of the library is free and always will be.</p>`,
  ].join("");

  const flags = gateFlags(lesson, m, notYet, checked);

  let out = html
    .replace(/<title>[\s\S]*?<\/title>/, `<title>${title || "Not open yet"} | Forbes English</title>`)
    .replace("<!-- LESSON:head -->", `${head}\n${flags}`);

  if (notYet) {
    // The caller holds this mission; its week has not come. Not a sales
    // page: no price, no "subscribers only", just when it opens. The date is
    // printed in UTC and the page's script re-renders it in the reader's own
    // time zone.
    const when = new Date(notYet.opensAt);
    const utc = when.toLocaleString("en-GB", { weekday: "long", day: "numeric", month: "long",
      hour: "2-digit", minute: "2-digit", timeZone: "UTC", timeZoneName: "short" });
    // "Next camp" and the end card link straight to the next mission, which
    // may not be open yet: name the one that is, and link to it.
    const current = openMissionDeck(catalogue, notYet.term, notYet.openNow);
    const waiting = [
      `<div class="eyebrow">Block Camp &middot; Mission ${notYet.mission}</div>`,
      `<h1>${title || `Mission ${notYet.mission}`}</h1>`,
      `<p class="lede">Mission ${notYet.mission} opens on <strong><time datetime="${when.toISOString()}" data-local>${utc}</time></strong>.`,
      ` One new mission opens each week, and every mission stays open once it has.</p>`,
    ].join("");
    const buttons = [
      current ? `<a class="btn" href="/${escapeHtml(current)}">Mission ${notYet.openNow} is open now</a>` : "",
      `<a class="btn${current ? " ghost" : ""}" href="/block-camp.html">Back to Block Camp</a>`,
    ].join("");
    out = out
      .replace(/<!-- LESSON:intro -->[\s\S]*?<!-- \/LESSON:intro -->/,
               `<!-- LESSON:intro -->${waiting}<!-- /LESSON:intro -->`)
      .replace(/<!-- GATE:offer -->[\s\S]*?<!-- \/GATE:offer -->/,
               `<!-- GATE:offer --><div class="actions">${buttons}</div><!-- /GATE:offer -->`);
    return out;
  }

  out = out.replace(/<!-- LESSON:intro -->[\s\S]*?<!-- \/LESSON:intro -->/,
                    `<!-- LESSON:intro -->${intro}<!-- /LESSON:intro -->`);
  return checked ? finalOffer(out) : out;
}

// What the gate page's own script needs to know: the track, so the
// "already subscribed?" retry can recognise a one-off plan; and whether a
// retry can help at all. It cannot on a mission the reader holds but whose
// week has not come ("not-yet"), nor when the Worker read the reader's own
// rows and still said no ("checked"): only a missing or expired token is
// worth a fresh session and a reload.
function gateFlags(lesson, m, notYet, checked) {
  return [
    `<meta name="fe-track" content="${escapeHtml((lesson && lesson.track) || m.track || "general")}">`,
    notYet ? `<meta name="fe-gate" content="not-yet">`
      : checked ? `<meta name="fe-gate" content="checked">` : "",
  ].filter(Boolean).join("\n");
}

// A final refusal keeps the way to the plans and the free lessons, and drops
// "Already bought it? ... this page will let you straight through", which
// would not be true.
function finalOffer(html) {
  return html.replace(/<!-- GATE:offer -->[\s\S]*?<!-- \/GATE:offer -->/,
    `<!-- GATE:offer --><div class="actions"><a class="btn" href="/pricing.html">See plans &amp; what's free</a>` +
    `<a class="btn ghost" href="/library.html?free=1">Browse free lessons</a></div><!-- /GATE:offer -->`);
}

// The deck for a given mission of a term (the decks are blockcamp-*.html;
// the quests that share the mission sit in block-camp/).
function openMissionDeck(catalogue, term, mission) {
  if (!catalogue || !(mission > 0)) return null;
  for (const [file, l] of catalogue) {
    if (l.track === "blockcamp" && Number(l.term) === term && Number(l.mission) === mission &&
        file.startsWith("blockcamp-")) return file;
  }
  return null;
}

// ─────────────────────────────────────────────────────────────────────────
// GET /api/paywall-status  — is the gate actually on?
// ─────────────────────────────────────────────────────────────────────────

async function handlePaywallStatus(request, url, env, ctx) {
  const catalogue = await getCatalogue(env, ctx);
  const pro = catalogue ? [...catalogue].filter(([, l]) => l.access === "pro") : null;
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
    catalogueReadable: catalogue !== null,
    proLessonCount: pro ? pro.length : null,
    sampleLessonIsGated: pro ? pro.some(([f]) => f === sample) : null,
    // The weekly drip needs Term 1 tagged (deploy/schema-pricing.sql step 2):
    // missions 1-12 present, Mission 1 free. Without the service key a
    // subscriber's clock is never saved and their Mission 2 never opens.
    ...(() => {
      const t1 = catalogue ? [...catalogue].filter(([, l]) => l.track === "blockcamp" && Number(l.term) === 1 && l.mission) : [];
      const missions = [...new Set(t1.map(([, l]) => Number(l.mission)))].sort((a, b) => a - b);
      return {
        term1Missions: missions,
        mission1Free: t1.some(([, l]) => Number(l.mission) === 1) &&
          t1.filter(([, l]) => Number(l.mission) === 1).every(([, l]) => l.access === "free"),
        blockCampDripReady: missions.length === 12 && missions[0] === 1 && missions[11] === 12 &&
          Boolean(env.SUPABASE_SERVICE_ROLE_KEY),
      };
    })(),
    callerBlockCampFirstOpen: access.blockCampFirstOpen ? new Date(access.blockCampFirstOpen).toISOString() : null,
    callerBlockCampPlans: access.blockCampPlans.map((b) => ({ term: b.term, startsAt: new Date(b.startsAt).toISOString() })),
    callerHasSessionCookie: Boolean(readCookie(request.headers.get("Cookie"), SESSION_COOKIE)),
    callerSubscribed: access.full,
    callerTracks: [...access.tracks],
    hasBlockCampPrice: Boolean(env.STRIPE_PRICE_ID_BLOCKCAMP),
    hasIeltsPrice: Boolean(env.STRIPE_PRICE_ID_IELTS),
    hasIeltsMarkingPrice: Boolean(env.STRIPE_PRICE_ID_IELTS_MARKING),
    hasMarkingPrice: Boolean(env.STRIPE_PRICE_ID_MARKING),
    hasFounderPromo: Boolean(env.STRIPE_PROMO_FOUNDER),
    hasMarkingMail: Boolean(env.MARKING_MAIL_TO &&
      ((env.RESEND_API_KEY && env.MAIL_FROM) || (env.MARKING_MAIL && env.MARKING_MAIL_FROM))),
    // The weekly "Mission N is open" email (the hourly cron) can send.
    hasMissionEmail: Boolean(env.RESEND_API_KEY && env.MAIL_FROM && env.SUPABASE_SERVICE_ROLE_KEY),
    // Checkout asks for the terms and immediate-access consent.
    hasTermsConsent: Boolean(env.TERMS_URL),
    // Buying without an account first (guest checkout), and the funnel
    // count (funnel_events) both need the service key.
    guestCheckout: Boolean(env.SUPABASE_SERVICE_ROLE_KEY),
    funnelOn: Boolean(env.SUPABASE_SERVICE_ROLE_KEY) && env.FUNNEL !== "off",
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

/**
 * The signed-in caller, from the Supabase access token in the Authorization
 * header (pricing.html sends it) or the fe_at cookie (sb-client.js keeps it
 * in step). Supabase checks the token; nothing in the request body is
 * trusted for who is buying.
 */
async function signedInUser(request, env) {
  const auth = request.headers.get("Authorization") || "";
  const token = (auth.match(/^Bearer\s+(.+)$/i) || [])[1] ||
    readCookie(request.headers.get("Cookie"), SESSION_COOKIE);
  if (!token) return { error: "Sign in first", status: 401 };
  try {
    const res = await fetch(`${env.SUPABASE_URL}/auth/v1/user`, {
      headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${token}` },
    });
    if (!res.ok) return { error: "Sign in first", status: 401 };
    const user = await res.json();
    if (!user || !user.id || !user.email) return { error: "Sign in first", status: 401 };
    return { id: user.id, email: user.email };
  } catch {
    return { error: "Could not check your sign-in; please try again", status: 502 };
  }
}

async function handleCreateCheckoutSession(request, env, ctx) {
  let body;
  try {
    body = await request.json();
  } catch {
    return json({ error: "Invalid JSON body" }, 400);
  }

  // The buyer is whoever is signed in. Until 2026-10-04 the account came
  // from userId/userEmail in the body, so anyone could open a checkout
  // attached to any account id; a body's ids are now ignored.
  // Nobody signed in (or a token Supabase will not confirm): the buyer pays
  // as a guest, Stripe asks for their email, and the purchase goes to the
  // account with that email, made for them if there is none
  // (accountForCheckout). Until 2026-10-09 this answered 401 and the page
  // sent a buyer off to make an account and confirm an email before they
  // could pay.
  const caller = await signedInUser(request, env);
  const guest = Boolean(caller.error);
  const userId = guest ? null : caller.id;
  const userEmail = guest ? null : caller.email;
  const { plan, product } = body;
  const what = String(product || plan || "").slice(0, 40) || null;
  const note = (outcome) => recordEvent(env, ctx, { event: "checkout", product: what, guest, outcome, ...visitFields(request) });
  const owned = guest ? null : await alreadyHas(env, userId, { plan, product });
  if (owned) {
    note("owned");
    return json({ error: owned, owned: true }, 409);
  }
  const res = product
    ? await createProductCheckout(env, userId, userEmail, product)
    : await createPlanCheckout(env, userId, userEmail, plan);
  note(res.status === 200 ? "created" : `error_${res.status}`);
  return res;
}

// What a checkout carries to say who is buying: the signed-in account, or
// "guest" (Stripe collects the email; the webhook and the success page find
// or make the account from it). A guest's success page also gets the
// session id as `claim`, for handleClaimCheckout.
function buyerParams(userId, userEmail, prefix = "") {
  return userId
    ? { customer_email: userEmail, [`${prefix}metadata[supabase_user_id]`]: userId }
    : { [`${prefix}metadata[guest]`]: "1" };
}

async function createPlanCheckout(env, userId, userEmail, plan) {
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
    ...buyerParams(userId, userEmail),
    "metadata[plan]": plan,
    ...(userId ? { "subscription_data[metadata][supabase_user_id]": userId } : { "subscription_data[metadata][guest]": "1" }),
    "subscription_data[metadata][plan]": plan,
    success_url: `${env.SITE_URL}/account.html?checkout=success` + (userId ? "" : "&claim={CHECKOUT_SESSION_ID}"),
    // Back to where they started: account.html ignores ?checkout=cancelled,
    // pricing.html says "no charge was made".
    cancel_url: `${env.SITE_URL}/pricing.html?checkout=cancelled`,
  });
  addConsent(params, env);

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
 * What the buyer already has that this checkout would sell again, as the
 * sentence to show them, or null. A second Term 1 or IELTS opens nothing
 * new (and a second Term 1 spends a founder place); a second Forbes English
 * Pro is a second subscription billing beside the first, which the site
 * cannot see. Marking is bought as often as wanted: credits add up. A Pro
 * subscriber may still buy a one-off to keep. A read that fails lets the
 * sale through: a Supabase hiccup must not stop anyone paying.
 */
async function alreadyHas(env, userId, { plan, product }) {
  const id = encodeURIComponent(userId);
  const read = async (path) => {
    const res = await fetch(`${env.SUPABASE_URL}/rest/v1/${path}`, { headers: supabaseHeaders(env) });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const rows = await res.json();
    if (!Array.isArray(rows)) throw new Error("not a list");
    return rows;
  };
  const inbox = env.MAIL_REPLY_TO || "info@forbesenglish.com";
  try {
    if (!product) {
      if (!PLAN_ENV_KEYS[plan]) return null;
      const [p] = await read(`profiles?select=subscription_status&id=eq.${id}`);
      return p && ACTIVE_STATUSES.has(p.subscription_status)
        ? `You already have Forbes English Pro. To change how you pay for it, email ${inbox}.`
        : null;
    }
    const want = product === "ielts_marking" ? "ielts" : product;
    if (want !== "blockcamp" && want !== "ielts") return null;
    const rows = await read(`user_plans?select=status,ends_at,term&user_id=eq.${id}&product=eq.${want}`);
    const now = Date.now();
    const holds = rows.some((r) => ACTIVE_STATUSES.has(r.status) &&
      (!r.ends_at || Date.parse(r.ends_at) > now) &&
      (want !== "blockcamp" || (Number(r.term) || 1) === 1));
    if (!holds) return null;
    if (product === "blockcamp") return "You already have Block Camp Term 1. It is on your account page.";
    if (product === "ielts") return "You already have IELTS. It is on your account page.";
    return "You already have IELTS, so this would sell it to you twice. Two marked essays on their own are €49: Buy marking, under the IELTS card.";
  } catch (err) {
    console.error(`checkout: could not read what ${userId} already has (${err.message}); letting the sale through`);
    return null;
  }
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
    "managed_payments[enabled]": def.managed ? "true" : "false",
    "line_items[0][price]": priceId,
    "line_items[0][quantity]": "1",
    ...buyerParams(userId, userEmail),
    "metadata[product]": product,
    // Stripe fills in the session id: account.html waits for that very
    // purchase to be recorded (the webhook can land a moment after the buyer).
    success_url: `${env.SITE_URL}/account.html?checkout=success&cs={CHECKOUT_SESSION_ID}` +
      (userId ? "" : "&claim={CHECKOUT_SESSION_ID}"),
    cancel_url: `${env.SITE_URL}/pricing.html?checkout=cancelled`,
  });
  addConsent(params, env);

  const founder = def.founder && env.STRIPE_PROMO_FOUNDER ? await getFounderStatus(env) : null;
  if (founder && founder.remaining > 0) {
    params.set("discounts[0][promotion_code]", env.STRIPE_PROMO_FOUNDER);
  }

  let stripeRes = await createCheckoutSession(env, params);
  // The last founder place can go between the count and this call. Stripe
  // then refuses the code (a 400 about the discount), and the buyer still
  // gets a checkout, at €19, rather than an error. Any other failure (a 429,
  // a 5xx) keeps the code and goes back as an error the page can retry:
  // a founder must never be charged €19 because Stripe hiccuped.
  if (!stripeRes.ok && params.has("discounts[0][promotion_code]")) {
    const text = await stripeRes.text();
    let err = {};
    try { err = JSON.parse(text).error || {}; } catch { /* not JSON */ }
    const aboutCode = stripeRes.status === 400 && (
      /^discounts/.test(String(err.param || "")) ||
      /promotion_code|coupon/.test(String(err.code || "")) ||
      /promotion code|coupon/i.test(String(err.message || "")));
    if (!aboutCode) return json({ error: "Stripe error", detail: text }, 502);
    console.error(`FOUNDER refused, checkout at full price: ${err.message || text}`);
    params.delete("discounts[0][promotion_code]");
    stripeRes = await createCheckoutSession(env, params);
  }
  if (!stripeRes.ok) {
    return json({ error: "Stripe error", detail: await stripeRes.text() }, 502);
  }
  return json({ url: (await stripeRes.json()).url });
}

// An EU consumer who buys digital content keeps a 14-day right of
// withdrawal unless they ask for access to start at once and acknowledge
// that they lose it. Checkout asks for both once a terms page exists:
// TERMS_URL switches it on. Stripe refuses consent_collection while no
// terms URL is saved in its own dashboard (Settings → Business → Public
// details), so that comes first (docs/GO-LIVE-pricing.md, A.1). Neither
// parameter is one Managed Payments forbids.
function addConsent(params, env) {
  if (!env.TERMS_URL) return;
  params.set("consent_collection[terms_of_service]", "required");
  params.set("custom_text[terms_of_service_acceptance][message]",
    `I agree to the [terms](${env.TERMS_URL}) and ask for access to start straight away. ` +
    "I understand that I then lose my 14-day right to cancel.");
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
  const cacheKey = new Request(`${env.SITE_URL}/__internal/founder-status-v2`);
  const cache = typeof caches !== "undefined" ? caches.default : null;
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) {
      try {
        const v = await hit.json();
        return v && v.limit ? v : null;
      } catch { /* re-read */ }
    }
  }
  // A failed read is cached as {} for the same minute, so a failing Stripe
  // is asked once a minute rather than once per visitor.
  let status = {};
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/promotion_codes/${encodeURIComponent(env.STRIPE_PROMO_FOUNDER)}`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } }
    );
    if (res.ok) {
      const promo = await res.json();
      const limit = Number(promo.max_redemptions);
      const used = Number(promo.times_redeemed) || 0;
      if (limit > 0) status = { limit, remaining: promo.active ? Math.max(0, limit - used) : 0 };
    }
  } catch { /* status stays {} */ }
  if (cache) {
    const put = cache.put(cacheKey, new Response(JSON.stringify(status), {
      headers: { "Content-Type": "application/json", "Cache-Control": "max-age=60" },
    }));
    if (ctx && ctx.waitUntil) ctx.waitUntil(put); else await put;
  }
  return status.limit ? status : null;
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

async function handleStripeWebhook(request, env, ctx) {
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
      if (session.mode === "payment") {
        // A delayed method (a bank debit) completes the session unpaid and
        // pays later; the grant waits for async_payment_succeeded.
        if (session.payment_status !== "paid" && session.payment_status !== "no_payment_required") break;
      } else if (event.type !== "checkout.session.completed" || !session.subscription) {
        break;
      }
      // Signed in at checkout, or not: then the account is the one with the
      // email the buyer gave Stripe, made for them if there is none. That
      // covers a Payment Link or dashboard sale too. Only a sale with no
      // email at all has nothing to attach to; it is logged by session id
      // (the logs are kept, and buyers' addresses do not belong in them).
      let userId = session.metadata?.supabase_user_id;
      if (!userId) {
        const acct = await accountForCheckout(env, session);
        if (!acct) return failed();
        if (!acct.userId) {
          console.error(`checkout ${session.id}: paid, but no account and no email to make one; nothing granted ` +
            `(find the buyer in Stripe by this session id)`);
          break;
        }
        userId = acct.userId;
        if (acct.created) await welcomeEmail(env, acct.email, session);
      }
      if (!(await fulfil(env, session, userId, event, ctx))) return failed();
      if (session.mode !== "payment") {
        recordEvent(env, ctx, { event: "paid", product: String(session.metadata?.plan || "plan").slice(0, 40),
          guest: !session.metadata?.supabase_user_id });
      }
      break;
    }
    case "customer.subscription.updated":
    case "customer.subscription.deleted": {
      const evSub = event.data.object;
      // A standalone subscription updates its own row. None is sold any more
      // (every product is one-off since 2026-10-04); kept so a row made by
      // the 2026-09-28 plans can still be closed.
      if (evSub.metadata?.product) {
        const status = event.type === "customer.subscription.deleted" ? "canceled" : evSub.status;
        if (!(await updateUserPlanBySubscription(env, evSub.id, { status }))) return failed();
        break;
      }
      // The full plan. The event says *that* something changed; what it is
      // now is read from Stripe, so events arriving out of order or again
      // after a retry all settle on the same, current state.
      const sub = await currentSubscription(env, evSub.id);
      if (!sub) return failed();
      const plan = sub.metadata?.plan;
      const ok = await updateProfileByCustomer(env, sub.customer, {
        ...subscriptionFields(sub),
        ...(plan ? { plan } : {}),
      });
      if (!ok) return failed();
      break;
    }
    case "charge.refunded":
    case "charge.dispute.closed": {
      // Nothing one-off expires, and under Managed Payments Stripe can refund
      // a buyer without asking: a full refund or a lost chargeback has to
      // close the grant, or it stays open for good. A partial refund and a
      // dispute that was won leave it alone. The full plan is not affected
      // here; its subscription status governs it.
      const obj = event.data.object;
      if (event.type === "charge.refunded" && obj.refunded !== true) break;
      if (event.type === "charge.dispute.closed" && obj.status !== "lost") break;
      const pi = typeof obj.payment_intent === "string" ? obj.payment_intent : obj.payment_intent?.id;
      if (!pi) break;
      const res = await revokeOneOff(env, pi, event.type === "charge.refunded" ? "refunded" : "disputed");
      if (!res) return failed();
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
async function grantOneOff(env, event, session, userId, ctx) {
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
  // Counted once: the row is keyed by the session, so a redelivery, or the
  // success page and the webhook both granting, make one sale.
  if (inserted) {
    recordEvent(env, ctx, { event: "paid", product: String(session.metadata?.product || product).slice(0, 40),
      guest: !session.metadata?.supabase_user_id });
  }

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
 * Gives a paid checkout what it bought, on `userId`: a one-off becomes its
 * user_plans row (grantOneOff), the full plan writes the subscription onto
 * the profile, read from Stripe as it is now (a late or redelivered event
 * must not write "active" over a cancellation made since). Both are safe to
 * run twice, which happens: the webhook and a guest's success page
 * (handleClaimCheckout) each fulfil, whichever comes first. False when it
 * could not be recorded.
 */
async function fulfil(env, session, userId, event, ctx) {
  if (session.mode === "payment") return grantOneOff(env, event, session, userId, ctx);
  const sub = await currentSubscription(env, session.subscription);
  if (!sub) return false;
  const plan = session.metadata?.plan;
  return updateProfile(env, userId, {
    stripe_customer_id: session.customer,
    stripe_subscription_id: session.subscription,
    ...subscriptionFields(sub),
    ...(plan ? { plan } : {}),
  });
}

// ── GUEST CHECKOUT ───────────────────────────────────────────────────────
// A buyer who is not signed in pays first. The account is the one with the
// email they gave Stripe; if there is none, the purchase makes it, already
// confirmed (they proved the address is theirs well enough to pay from it;
// what an impostor could do with it is own a purchase they paid for). The
// success page then signs a new account straight in (handleClaimCheckout),
// so no email has to arrive for the purchase to be usable. Supabase's own
// mail only reaches the project team's addresses until a custom SMTP server
// is set (supabase.com/docs/guides/auth/auth-smtp), which is also why the
// old "make an account, confirm your email, then pay" path could not work
// for a stranger.

/**
 * The account a checkout's purchase goes to: { userId, created, email },
 * { userId: null } when Stripe has no email for the buyer, or null when
 * Supabase could not be reached (the caller retries). The first answer for
 * a session is kept in guest_checkouts, so the webhook and the success
 * page, racing, agree on one account.
 */
async function accountForCheckout(env, session) {
  const email = String(session.customer_details?.email || session.customer_email || "").trim().toLowerCase();
  if (!email) return { userId: null };
  const rest = `${env.SUPABASE_URL}/rest/v1`;
  const headers = supabaseHeaders(env);
  const sid = encodeURIComponent(session.id);
  const readRow = async () => {
    const r = await fetch(`${rest}/guest_checkouts?select=user_id,created_account&session_id=eq.${sid}`, { headers });
    if (!r.ok) throw new Error(`guest_checkouts HTTP ${r.status}`);
    return (await r.json())[0] || null;
  };
  try {
    const seen = await readRow();
    if (seen) return { userId: seen.user_id, created: seen.created_account, email };

    let userId = await profileIdByEmail(env, email);
    let created = false;
    if (!userId) {
      const r = await fetch(`${env.SUPABASE_URL}/auth/v1/admin/users`, {
        method: "POST", headers,
        body: JSON.stringify({ email, email_confirm: true, user_metadata: { via: "checkout", needs_password: true } }),
      });
      if (r.ok) {
        userId = (await r.json()).id;
        created = true;
      } else {
        // Made a moment ago by the other path (the webhook or the success
        // page): the email is taken, so the profile is there now.
        userId = await profileIdByEmail(env, email);
        if (!userId) throw new Error(`could not make the account (auth HTTP ${r.status})`);
      }
    }
    const ins = await fetch(`${rest}/guest_checkouts?on_conflict=session_id`, {
      method: "POST",
      headers: { ...headers, "Prefer": "return=representation,resolution=ignore-duplicates" },
      body: JSON.stringify({ session_id: session.id, user_id: userId, created_account: created }),
    });
    if (!ins.ok) throw new Error(`guest_checkouts HTTP ${ins.status}`);
    if ((await ins.json()).length) return { userId, created, email };
    const row = await readRow();
    return row ? { userId: row.user_id, created: row.created_account, email } : null;
  } catch (err) {
    console.error(`checkout ${session.id}: no account for the buyer yet (${err && err.message})`);
    return null;
  }
}

// The account id for an email, from the profiles row Supabase makes for
// every account (handle_new_user). Compared whole and ignoring case: an
// ilike pattern alone would let "_" in an address match any letter.
async function profileIdByEmail(env, email) {
  const r = await fetch(`${env.SUPABASE_URL}/rest/v1/profiles?select=id,email&email=ilike.${encodeURIComponent(email)}&limit=5`,
    { headers: supabaseHeaders(env) });
  if (!r.ok) throw new Error(`profiles HTTP ${r.status}`);
  const row = (await r.json()).find((p) => String(p.email || "").toLowerCase() === email);
  return row ? row.id : null;
}

/**
 * A new account made by a purchase: the email that says it exists, with a
 * sign-in link (it lasts as long as Supabase's email OTP expiry) and the
 * way back in after that. Only with Resend set up; until then the success
 * page's own sign-in is the way in. Idempotent per account for 24 hours.
 */
async function welcomeEmail(env, email, session) {
  if (!env.RESEND_API_KEY || !env.MAIL_FROM) return;
  let link = `${env.SITE_URL}/account.html`;
  try {
    const r = await fetch(`${env.SUPABASE_URL}/auth/v1/admin/generate_link`, {
      method: "POST", headers: supabaseHeaders(env),
      body: JSON.stringify({ type: "magiclink", email, redirect_to: `${env.SITE_URL}/account.html` }),
    });
    if (r.ok) {
      const g = await r.json();
      link = g.action_link || g.properties?.action_link || link;
    }
  } catch { /* the plain account link will do */ }
  const what = session.mode === "payment" ? "your purchase" : "Forbes English Pro";
  const text = [
    `Thank you. ${what[0].toUpperCase() + what.slice(1)} is on your Forbes English account, made for this email address.`,
    "",
    `Sign in: ${link}`,
    "",
    "That link works once and only for a while. After that, open " +
      `${env.SITE_URL}/account.html, choose "Forgot your password?" and enter this address.`,
    "",
    "Forbes English",
  ].join("\n");
  await sendMail(env, { to: email, subject: "Your Forbes English account", text, key: `welcome-${session.id}` });
}

/**
 * POST /api/claim-checkout { cs }: the success page of a checkout made
 * without signing in. It fulfils the purchase at once (the webhook may land
 * a moment later and finds it done), and answers with the account it went
 * to:
 *   new_account       the purchase made this account and nobody has signed
 *                     into it yet: a one-time `token_hash` the page trades
 *                     for a session (supabase.auth.verifyOtp, type "email"),
 *                     so the buyer is signed in with no email to wait for.
 *   existing_account  the email already had an account (or this sign-in
 *                     has been used): the page asks them to log in.
 *   processing        paid by a method that clears later.
 *   not_paid          the checkout was not completed.
 *   signed_in_purchase  bought while signed in; nothing to claim.
 * The session id is the only key, and it is in the success URL Stripe sent
 * the buyer to; a sign-in is handed out once per checkout, only within two
 * days, and only into an account that has never been signed into.
 */
async function handleClaimCheckout(request, env, ctx) {
  let body;
  try { body = await request.json(); } catch { return json({ error: "Invalid JSON body" }, 400); }
  const cs = String((body && body.cs) || "");
  if (!/^cs_(test|live)_[A-Za-z0-9]{10,200}$/.test(cs)) return json({ error: "Not a checkout" }, 400);

  let session;
  try {
    const r = await fetch(`https://api.stripe.com/v1/checkout/sessions/${encodeURIComponent(cs)}`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } });
    if (r.status === 404) return json({ error: "Not a checkout" }, 404);
    if (!r.ok) return json({ error: "Could not reach the payment service; reload in a moment." }, 502);
    session = await r.json();
  } catch {
    return json({ error: "Could not reach the payment service; reload in a moment." }, 502);
  }
  const what = String(session.metadata?.product || session.metadata?.plan || "").slice(0, 40) || null;
  const answer = (state, extra = {}) => {
    recordEvent(env, ctx, { event: "claim", product: what, guest: true, outcome: state });
    return json({ state, ...extra });
  };

  if (session.metadata?.supabase_user_id) return json({ state: "signed_in_purchase" });
  if (session.status !== "complete") return answer("not_paid");
  if (session.payment_status !== "paid" && session.payment_status !== "no_payment_required") return answer("processing");

  const acct = await accountForCheckout(env, session);
  if (!acct) return json({ error: "Your payment went through, but the account is not ready yet. Reload in a moment." }, 502);
  if (!acct.userId) return json({ error: "Your payment went through, but it came without an email address. Write to info@forbesenglish.com." }, 500);
  // Fulfilled here too, so the account shows the purchase on arrival; a
  // failure is left to the webhook, which retries until it lands.
  await fulfil(env, session, acct.userId, { created: session.created }, ctx);

  const recent = Date.now() / 1000 - Number(session.created || 0) < 2 * 86400;
  let fresh = false;
  try {
    const r = await fetch(`${env.SUPABASE_URL}/auth/v1/admin/users/${encodeURIComponent(acct.userId)}`,
      { headers: supabaseHeaders(env) });
    if (r.ok) {
      const u = await r.json();
      fresh = u.user_metadata?.via === "checkout" && !u.last_sign_in_at;
    }
  } catch { /* not fresh: they log in */ }
  if (!recent || !fresh) return answer("existing_account", { email: acct.email });

  // Once per checkout: the first claim takes it.
  let claimed = false;
  try {
    const r = await fetch(`${env.SUPABASE_URL}/rest/v1/guest_checkouts?session_id=eq.${encodeURIComponent(session.id)}&claimed_at=is.null`, {
      method: "PATCH",
      headers: { ...supabaseHeaders(env), "Prefer": "return=representation" },
      body: JSON.stringify({ claimed_at: new Date().toISOString() }),
    });
    claimed = r.ok && (await r.json()).length > 0;
  } catch { /* not claimed: they log in */ }
  if (!claimed) return answer("existing_account", { email: acct.email });

  try {
    const r = await fetch(`${env.SUPABASE_URL}/auth/v1/admin/generate_link`, {
      method: "POST", headers: supabaseHeaders(env),
      body: JSON.stringify({ type: "magiclink", email: acct.email }),
    });
    if (r.ok) {
      const g = await r.json();
      const token = g.hashed_token || g.properties?.hashed_token;
      if (token) return answer("new_account", { email: acct.email, token_hash: token });
    }
    console.error(`claim ${session.id}: no sign-in link (auth HTTP ${r.status})`);
  } catch (err) {
    console.error(`claim ${session.id}: no sign-in link (${err && err.message})`);
  }
  return answer("existing_account", { email: acct.email });
}

/**
 * Tells the marking inbox that essay credits were bought. Uses a Cloudflare
 * Email Routing `send_email` binding, which can only send to a verified
 * address on the forbesenglish.com zone (enough for Innes's own inbox; a
 * parent's address needs a real transactional sender). Without the binding
 * this is a no-op, and a mail failure never fails the purchase: Stripe's
 * own payment emails to the account owner are the backstop.
 */
// A header value with non-ASCII in it (the em dash in "Marking — two
// essays") as an RFC 2047 encoded word; plain ASCII goes through untouched.
function encodeHeader(s) {
  if (/^[\x20-\x7e]*$/.test(s)) return s;
  const bytes = new TextEncoder().encode(s);
  let bin = "";
  for (const b of bytes) bin += String.fromCharCode(b);
  return `=?UTF-8?B?${btoa(bin)}?=`;
}

async function notifyMarking(env, info) {
  if (!env.MARKING_MAIL_TO) return;
  const clean = (s) => String(s).replace(/[\r\n]+/g, " ").slice(0, 200);
  const subject = `Marking bought: ${info.credits} essays (${clean(info.productName)})`;
  const text = [
    `${clean(info.buyer) || "A buyer"} bought ${clean(info.productName)}: ${info.credits} essays to mark.`,
    "",
    `Paid: ${info.paidAt}`,
    `Supabase user: ${clean(info.userId)}`,
    `Stripe checkout: ${clean(info.sessionId)}`,
  ].join("\n");
  // Resend first: it is what the weekly mission email uses, so one setup
  // covers both. The Email Routing binding is the fallback.
  if (env.RESEND_API_KEY && env.MAIL_FROM) {
    await sendMail(env, { to: env.MARKING_MAIL_TO, subject, text, key: `marking-${info.sessionId}` });
    return;
  }
  if (!env.MARKING_MAIL || !env.MARKING_MAIL_FROM) return;
  const raw = [
    `From: Forbes English <${clean(env.MARKING_MAIL_FROM)}>`,
    `To: <${clean(env.MARKING_MAIL_TO)}>`,
    `Subject: ${encodeHeader(`Marking bought: ${info.credits} essays (${clean(info.productName)})`)}`,
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
// ─────────────────────────────────────────────────────────────────────────
// Email: Resend, and the weekly "Mission N is open" (pricing step 9)
// ─────────────────────────────────────────────────────────────────────────

/**
 * Sends one email through Resend (https://resend.com/docs). `key` makes a
 * retry within 24 hours a no-op at Resend's end, on top of our own claim.
 * Returns true when Resend accepted it.
 */
async function sendMail(env, { to, subject, text, html, key, headers }) {
  if (!env.RESEND_API_KEY || !env.MAIL_FROM) return false;
  try {
    const res = await fetch("https://api.resend.com/emails", {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${env.RESEND_API_KEY}`,
        "Content-Type": "application/json",
        ...(key ? { "Idempotency-Key": key.slice(0, 256) } : {}),
      },
      body: JSON.stringify({
        from: env.MAIL_FROM, to: [to], subject, text, ...(html ? { html } : {}),
        ...(headers ? { headers } : {}),
        reply_to: env.MAIL_REPLY_TO || "info@forbesenglish.com",
      }),
    });
    // Logged by key, never by address: the logs are not where readers'
    // email addresses should end up.
    if (!res.ok) console.error(`email ${key || "(unkeyed)"} refused by Resend: ${res.status} ${await res.text().catch(() => "")}`);
    return res.ok;
  } catch (err) {
    console.error(`email ${key || "(unkeyed)"} failed: ${err && err.message}`);
    return false;
  }
}

/**
 * Every hour (the cron in wrangler.toml): every Block Camp reader whose
 * next mission opened in the last 48 hours gets one email saying so, with
 * the deck and the quest and a link. Term 1 buyers count from their
 * payment, subscribers from their first Block Camp visit, and the earlier
 * clock wins, exactly as the gate does. Mission 1 opens on purchase and is
 * not mailed; a mission that opened longer ago is never mailed late (no
 * catch-up flood for a subscriber whose clock was set back at go-live). The
 * owner, and anyone with profiles.blockcamp_emails = false, get none.
 *
 * Exactly once: each email is claimed in blockcamp_mission_emails
 * (claimed_at) before it is sent and marked sent (sent_at) only when Resend
 * accepts it. A claim left unsent for ten minutes -- a refused send, a lost
 * reply, a run cut short -- is taken again by a later run. Runs are hourly,
 * so a retry falls inside the 24 hours Resend keeps its idempotency key,
 * and an email Resend did take is not delivered twice.
 *
 * Every Supabase and Resend call counts against a per-run budget
 * (EMAIL_SUBREQUEST_BUDGET, default 40: under the Workers Free plan's 50
 * subrequests). A run that reaches it stops cleanly and the next run
 * carries on; set the budget higher on the Paid plan.
 */
const MISSION_EMAIL_WINDOW_MS = 48 * 3600000;
const STALE_CLAIM_MS = 10 * 60000;
const PAGE = 1000;

async function sendMissionEmails(env, now = Date.now()) {
  const summary = { sent: 0, failed: 0, skipped: 0, deferred: 0 };
  if (!env.RESEND_API_KEY || !env.MAIL_FROM || !env.SUPABASE_SERVICE_ROLE_KEY) {
    console.log("mission emails: not configured (RESEND_API_KEY, MAIL_FROM, SUPABASE_SERVICE_ROLE_KEY)");
    return { ...summary, off: true };
  }
  const budget = Number(env.EMAIL_SUBREQUEST_BUDGET) || 40;
  let used = 0;
  const call = (url, init) => { used++; return fetch(url, init); };
  const svc = { headers: supabaseHeaders(env) };
  const anon = { headers: { apikey: env.SUPABASE_ANON_KEY, Authorization: `Bearer ${env.SUPABASE_ANON_KEY}` } };
  const read = async (path, init = svc) => {
    const res = await call(`${env.SUPABASE_URL}/rest/v1/${path}`, init);
    if (!res.ok) throw new Error(`${path.split("?")[0]} ${res.status}`);
    return res.json();
  };
  // A list read that cannot be cut short by PostgREST's row cap.
  const readAll = async (path, order, init = svc) => {
    const out = [];
    for (let off = 0; ; off += PAGE) {
      const page = await read(`${path}&order=${order}&limit=${PAGE}&offset=${off}`, init);
      out.push(...page);
      if (page.length < PAGE) return out;
    }
  };
  const t = (ms) => new Date(ms).toISOString();

  let plans, subs, lessons;
  try {
    [plans, subs, lessons] = await Promise.all([
      readAll("user_plans?select=user_id,term,starts_at&product=eq.blockcamp&status=in.(active,trialing)", "user_id,starts_at"),
      readAll("profiles?select=id&blockcamp_first_open=not.is.null&subscription_status=in.(active,trialing)", "id"),
      read("lessons?select=file,title,mission&track=eq.blockcamp&term=eq.1&mission=not.is.null", anon),
    ]);
  } catch (err) {
    console.error(`mission emails: could not read the catalogue or the plans: ${err.message}`);
    return { ...summary, error: true };
  }

  // The profiles, a hundred ids a request: one URL with every reader in it
  // stops working at a few hundred (measured: refused at ~680 ids).
  const ids = [...new Set(plans.map((x) => x.user_id).concat(subs.map((s) => s.id)))];
  const profiles = [];
  for (let k = 0; k < ids.length; k += 100) {
    try {
      profiles.push(...await read(`profiles?select=id,email,owner,subscription_status,blockcamp_first_open,blockcamp_emails` +
        `&id=in.(${ids.slice(k, k + 100).map(encodeURIComponent).join(",")})`));
    } catch (err) {
      console.error(`mission emails: profiles ${k}-${k + 99} unreadable, skipped this run: ${err.message}`);
    }
  }

  // Who is due: no calls spent yet.
  const due = [];
  for (const p of profiles) {
    if (p.owner || p.blockcamp_emails === false || !p.email) { summary.skipped++; continue; }
    const bought = plans.filter((x) => x.user_id === p.id && (Number(x.term) || 1) === 1);
    const starts = bought.map((x) => Date.parse(x.starts_at));
    if (ACTIVE_STATUSES.has(p.subscription_status) && p.blockcamp_first_open) starts.push(Date.parse(p.blockcamp_first_open));
    const start = Math.min(...starts.filter(Number.isFinite));
    if (!Number.isFinite(start)) { summary.skipped++; continue; }
    const mission = Math.floor((now - start) / WEEK_MS) + 1;
    const opensAt = start + (mission - 1) * WEEK_MS;
    if (mission < 2 || mission > 12 || now - opensAt > MISSION_EMAIL_WINDOW_MS) { summary.skipped++; continue; }
    due.push({ p, mission, opensAt, owned: bought.length > 0 });
  }

  // What is already claimed for them, a hundred readers a request, so a
  // reader mailed earlier in the 48 hours costs this run nothing.
  const known = new Map();
  for (let k = 0; k < due.length; k += 100) {
    if (used >= budget) break;
    try {
      const rows = await read(`blockcamp_mission_emails?select=user_id,mission,sent_at,claimed_at&term=eq.1` +
        `&user_id=in.(${due.slice(k, k + 100).map((d) => encodeURIComponent(d.p.id)).join(",")})`);
      for (const r of rows) known.set(`${r.user_id}/${r.mission}`, r);
    } catch (err) {
      console.error(`mission emails: claims ${k}-${k + 99} unreadable: ${err.message}`);
    }
  }

  for (const { p, mission, opensAt, owned } of due) {
    const had = known.get(`${p.id}/${mission}`);
    if (had && had.sent_at) { summary.skipped++; continue; }
    // Claimed and not sent: another run is on it, unless the claim is stale.
    const stale = had && Date.parse(had.claimed_at) < now - STALE_CLAIM_MS;
    if (had && !stale) { summary.skipped++; continue; }

    // Claim (1), send (1), mark sent (1): stop before the budget.
    if (used + 3 > budget) { summary.deferred++; continue; }
    const row = `user_id=eq.${encodeURIComponent(p.id)}&term=eq.1&mission=eq.${mission}`;
    const claimed = await (had
      // Take the stale claim over, only if it is still unsent and stale.
      ? call(`${env.SUPABASE_URL}/rest/v1/blockcamp_mission_emails?${row}` +
          `&sent_at=is.null&claimed_at=lt.${encodeURIComponent(t(now - STALE_CLAIM_MS))}`,
          { method: "PATCH", headers: { ...supabaseHeaders(env), "Prefer": "return=representation" },
            body: JSON.stringify({ claimed_at: t(now) }) })
      : call(`${env.SUPABASE_URL}/rest/v1/blockcamp_mission_emails?on_conflict=user_id,term,mission`,
          { method: "POST", headers: { ...supabaseHeaders(env), "Prefer": "return=representation,resolution=ignore-duplicates" },
            body: JSON.stringify({ user_id: p.id, term: 1, mission, claimed_at: t(now) }) }))
      .then(async (r) => (r.ok ? (await r.json()).length > 0 : null)).catch(() => null);
    if (claimed === false) { summary.skipped++; continue; }   // another run got there first
    if (claimed === null) { summary.failed++; console.error(`mission emails: could not claim ${p.id} mission ${mission}`); continue; }

    const mail = missionEmail(env, mission, lessons, opensAt, owned);
    const optOut = env.MAIL_REPLY_TO || "info@forbesenglish.com";
    used++;
    const ok = await sendMail(env, { to: p.email, ...mail, key: `mission-${p.id}-1-${mission}`,
      headers: { "List-Unsubscribe": `<mailto:${optOut}?subject=Stop%20Block%20Camp%20emails>` } });
    if (!ok) { summary.failed++; continue; }   // the claim goes stale and a later run retries
    summary.sent++;
    await call(`${env.SUPABASE_URL}/rest/v1/blockcamp_mission_emails?${row}`,
      { method: "PATCH", headers: supabaseHeaders(env), body: JSON.stringify({ sent_at: t(now) }) })
      .catch(() => console.error(`mission emails: sent but not marked: ${p.id} mission ${mission}`));
  }
  console.log(`mission emails: ${JSON.stringify(summary)} (${used} of ${budget} calls)`);
  return summary;
}

/**
 * The email for one mission: subject, plain text and HTML. `owned` is a
 * reader who bought Term 1: only theirs is "yours to keep"; a subscriber's
 * lasts as long as the subscription.
 */
function missionEmail(env, mission, lessons, opensAt, owned) {
  const these = lessons.filter((l) => Number(l.mission) === mission);
  const deck = these.find((l) => l.file.startsWith("blockcamp-"));
  const quest = these.find((l) => !l.file.startsWith("blockcamp-"));
  const clean = (t) => String(t || "").replace(/^Block Camp\s*[—–-]\s*/, "");
  const link = `${env.SITE_URL}/${deck ? deck.file : "block-camp.html"}`;
  const next = mission < 12
    ? `Mission ${mission + 1} opens on ${new Date(opensAt + WEEK_MS).toLocaleString("en-GB",
        { weekday: "long", day: "numeric", month: "long", hour: "2-digit", minute: "2-digit",
          timeZone: "UTC", timeZoneName: "short" })}.`
    : `That is the last mission of Term 1: every mission is open now${owned ? ", and yours to keep" : ""}.`;
  const lines = [
    `Mission ${mission} of Block Camp Term 1 is open.`,
    "",
    deck ? `Deck: ${clean(deck.title)}` : "",
    quest ? `Quest: ${clean(quest.title)}` : "",
    "",
    `Open Mission ${mission}: ${link}`,
    "",
    `Missions 1 to ${mission} are open now. ${next}`,
    "",
    "Forbes English",
    "",
    "You are getting this because Block Camp is on your Forbes English account. To stop these emails, reply and say so.",
  ].filter((l, i, a) => l !== "" || a[i - 1] !== "");
  const e = escapeHtml;
  const html = [
    `<div style="font-family:Arial,Helvetica,sans-serif;font-size:16px;line-height:1.5;color:#111;max-width:520px">`,
    `<p style="font-size:20px;font-weight:bold;margin:0 0 12px">Mission ${mission} is open</p>`,
    `<p style="margin:0 0 12px">Mission ${mission} of Block Camp Term 1 is open.</p>`,
    deck ? `<p style="margin:0">Deck: <strong>${e(clean(deck.title))}</strong></p>` : "",
    quest ? `<p style="margin:0">Quest: <strong>${e(clean(quest.title))}</strong></p>` : "",
    `<p style="margin:20px 0"><a href="${e(link)}" style="background:#1b3a28;color:#faf8f3;padding:12px 22px;border-radius:999px;text-decoration:none;font-weight:bold">Open Mission ${mission}</a></p>`,
    `<p style="margin:0 0 12px">Missions 1 to ${mission} are open now. ${e(next)}</p>`,
    `<p style="margin:0 0 24px">Forbes English</p>`,
    `<p style="font-size:12px;color:#6b7a6b;margin:0">You are getting this because Block Camp is on your Forbes English account. To stop these emails, reply and say so.</p>`,
    `</div>`,
  ].join("");
  return { subject: `Mission ${mission} is open — Block Camp`, text: lines.join("\n"), html };
}

/** The subscription as Stripe has it now, or null if it cannot be read. */
async function currentSubscription(env, id) {
  try {
    const res = await fetch(`https://api.stripe.com/v1/subscriptions/${encodeURIComponent(id)}`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } });
    if (!res.ok) return null;
    return await res.json();
  } catch {
    return null;
  }
}

// Since Stripe API 2025-03-31 the period end lives on the subscription item,
// not the subscription. Reading sub.current_period_end gave undefined ->
// Invalid Date -> toISOString() threw. Fall back to the old field for older
// payloads, and skip the date rather than crash.
function subscriptionFields(sub) {
  const periodEnd = sub.items?.data?.[0]?.current_period_end ?? sub.current_period_end;
  return {
    subscription_status: sub.status,
    ...(typeof periodEnd === "number"
      ? { current_period_end: new Date(periodEnd * 1000).toISOString() }
      : {}),
  };
}

/**
 * Closes the one-off grant bought with this PaymentIntent: its row stops
 * counting (callerAccess only counts active rows) and its essay credits go.
 * True when done or when there is nothing to close (the full plan, or a
 * sale that never granted anything); null when Stripe or Supabase failed.
 *
 * The refund can arrive before the grant: the grant failed once and Stripe
 * is still retrying it, or the events simply came out of order. Then no row
 * matches, and a 200 here would lose the refund for good; the late grant
 * would make an active row nobody closes. So the refund leaves a closed row
 * of its own, keyed by the same Checkout Session, and the late grant finds
 * it already there (insertUserPlan ignores the duplicate) and does nothing.
 */
async function revokeOneOff(env, paymentIntent, status) {
  let session;
  try {
    const res = await fetch(
      `https://api.stripe.com/v1/checkout/sessions?payment_intent=${encodeURIComponent(paymentIntent)}&limit=1`,
      { headers: { "Authorization": `Bearer ${env.STRIPE_SECRET_KEY}` } });
    if (!res.ok) return null;
    session = ((await res.json()).data || [])[0];
  } catch {
    return null;
  }
  if (!session || session.mode !== "payment") return true;
  let rows;
  try {
    const res = await fetch(
      `${env.SUPABASE_URL}/rest/v1/user_plans?stripe_checkout_session_id=eq.${encodeURIComponent(session.id)}`,
      { method: "PATCH", headers: { ...supabaseHeaders(env), "Prefer": "return=representation" },
        body: JSON.stringify({ status, marking_credits: 0 }) });
    if (!res.ok) return null;
    rows = await res.json();
  } catch {
    return null;
  }
  if (Array.isArray(rows) && rows.length > 0) return true;

  // Nothing granted yet. A sale the site can never grant (no signed-in
  // buyer, a product it does not know) has nothing to hold closed.
  const userId = session.metadata?.supabase_user_id;
  const key = String(session.metadata?.product || "");
  const product = key === "ielts_marking" ? "ielts" : key;
  if (!userId || !Object.prototype.hasOwnProperty.call(PLAN_TRACKS, product)) return true;
  const made = await insertUserPlan(env, {
    user_id: userId,
    product,
    status,
    stripe_checkout_session_id: session.id,
    starts_at: new Date().toISOString(),
    ends_at: null,
    term: product === "blockcamp" ? 1 : null,
    marking_credits: 0,
  });
  if (made === null) return null;
  // The grant landed between the PATCH and this insert: close it after all.
  if (made === false) {
    return (await supabaseWrite(
      `${env.SUPABASE_URL}/rest/v1/user_plans?stripe_checkout_session_id=eq.${encodeURIComponent(session.id)}`,
      { method: "PATCH", headers: supabaseHeaders(env), body: JSON.stringify({ status, marking_credits: 0 }) })) || null;
  }
  console.log(`checkout ${session.id}: ${status} before its grant was recorded; held closed`);
  return true;
}

// Verifies the `Stripe-Signature` header using the raw request body, per
// https://docs.stripe.com/webhooks#verify-manually — implemented with the
// Web Crypto API since Cloudflare Workers don't have Node's `crypto`.
// The header can carry several v1 signatures (while the endpoint secret is
// being rolled, one per secret): any match is enough. A timestamp more than
// five minutes off is refused, so a captured event cannot be replayed later
// (Stripe re-signs every retry with a fresh timestamp). The comparison
// takes the same time whatever the input.
const SIGNATURE_TOLERANCE_SECONDS = 300;

async function verifyStripeSignature(rawBody, signatureHeader, webhookSecret) {
  if (!signatureHeader || !webhookSecret) return false;

  const items = signatureHeader.split(",").map((pair) => {
    const i = pair.indexOf("=");
    return i < 0 ? ["", ""] : [pair.slice(0, i).trim(), pair.slice(i + 1).trim()];
  });
  const timestamp = items.find(([k]) => k === "t")?.[1];
  const signatures = items.filter(([k]) => k === "v1").map(([, v]) => v);
  if (!timestamp || signatures.length === 0) return false;
  const ts = Number(timestamp);
  if (!Number.isFinite(ts) || Math.abs(Date.now() / 1000 - ts) > SIGNATURE_TOLERANCE_SECONDS) return false;

  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(webhookSecret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"]
  );
  const sigBuffer = await crypto.subtle.sign("HMAC", key, new TextEncoder().encode(`${timestamp}.${rawBody}`));
  const computed = [...new Uint8Array(sigBuffer)].map((b) => b.toString(16).padStart(2, "0")).join("");

  return signatures.some((s) => sameString(s, computed));
}

// Constant-time string equality: every character is compared, whatever the
// first difference.
function sameString(a, b) {
  if (a.length !== b.length) return false;
  let diff = 0;
  for (let i = 0; i < a.length; i++) diff |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return diff === 0;
}

function json(data, status = 200) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "Content-Type": "application/json" },
  });
}
