// Forbes English — checkout, founder count and Stripe webhook tests.
//
//   node deploy/test-webhook.mjs        (run from the repo root)
//
// Run beside deploy/test-paywall.mjs after any change to src/index.js.
// Stripe and Supabase are stubbed, and the stubs behave like the real
// services when a detail is missing (an unexpanded product is an id, a
// duplicate insert without the ignore-duplicates header is a 409), so a
// case cannot pass because the stub was forgiving. Every request the Worker
// makes is recorded and each case asserts what was actually sent.
//
import { readFileSync } from 'fs';
const STUB_MAIL = 'class EmailMessage { constructor(f, t, r) { this.from = f; this.to = t; this.raw = r; } }';
const SRC = readFileSync('src/index.js', 'utf8').replace(
  /^import \{ EmailMessage \} from "cloudflare:email";$/m, STUB_MAIL);
const load = (src) => import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));
const mod = await load(SRC);
// The same Worker with the marking products taken off Managed Payments, to
// prove the per-product flag is honoured.
const OFF = SRC.replace('ielts_marking: { envKey: "STRIPE_PRICE_ID_IELTS_MARKING", managed: true }',
  'ielts_marking: { envKey: "STRIPE_PRICE_ID_IELTS_MARKING", managed: false }');
if (OFF === SRC) throw new Error('could not find the ielts_marking entry to flip');
const modOff = await load(OFF);

const SECRET = 'whsec_test';
const sent = [];
const env = {
  SITE_URL: 'https://x.test',
  SUPABASE_URL: 'https://sb.test',
  SUPABASE_ANON_KEY: 'anon',
  SUPABASE_SERVICE_ROLE_KEY: 'service',
  STRIPE_SECRET_KEY: 'sk_test',
  STRIPE_WEBHOOK_SECRET: SECRET,
  STRIPE_PRICE_ID_MONTHLY: 'price_monthly',
  STRIPE_PRICE_ID_BLOCKCAMP: 'price_bc',
  STRIPE_PRICE_ID_IELTS: 'price_ielts',
  STRIPE_PRICE_ID_IELTS_MARKING: 'price_im',
  STRIPE_PRICE_ID_MARKING: 'price_mk',
  STRIPE_PROMO_FOUNDER: 'promo_founder',
  MARKING_MAIL: { send: async (m) => { sent.push(m); } },
  MARKING_MAIL_FROM: 'noreply@forbesenglish.com',
  MARKING_MAIL_TO: 'marking@forbesenglish.com',
  ASSETS: { fetch: () => new Response('x') },
};

// ── stubs ────────────────────────────────────────────────────────────────
let calls, promo, sessionFail, lineItems, insertFail, patchFails, lineItemsFail, inserted;
let subs, piSessions, logs, holdings, holdFail;
// Guest checkout: the accounts Supabase knows (email -> auth user), the
// Checkout Sessions Stripe would return by id, guest_checkouts rows, and
// the funnel rows written.
let accounts, authUsers, createFail, linkFail, stripeSessions, guestRows, funnel;
const USERS = { 'tok-1': { id: 'user-1', email: 'p@example.com' } };
const prefer = (opts) => String(opts.headers?.Prefer || '');

function li(product, meta, name) {
  return [{ quantity: 1, price: { id: 'price_x', product: { id: 'prod_x', name: name || product, metadata: { product, ...meta } } } }];
}

globalThis.fetch = async (url, opts = {}) => {
  const u = String(url);
  const method = opts.method || 'GET';
  const body = opts.body instanceof URLSearchParams ? Object.fromEntries(opts.body) : opts.body;
  calls.push({ url: u, method, body, headers: opts.headers || {} });
  if (u === 'https://sb.test/auth/v1/user') {
    const tok = String(opts.headers?.Authorization || '').replace(/^Bearer /, '');
    return USERS[tok] ? new Response(JSON.stringify(USERS[tok]), { status: 200 }) : new Response('{"msg":"bad jwt"}', { status: 401 });
  }
  if (u.startsWith('https://api.stripe.com/v1/promotion_codes/')) {
    return promo ? new Response(JSON.stringify(promo), { status: 200 }) : new Response('{}', { status: 500 });
  }
  if (u === 'https://api.stripe.com/v1/checkout/sessions' && method === 'POST') {
    if (sessionFail && body['discounts[0][promotion_code]']) return sessionFail();
    return new Response(JSON.stringify({ url: 'https://checkout.stripe.test/s' }), { status: 200 });
  }
  const lm = u.match(/^https:\/\/api\.stripe\.com\/v1\/checkout\/sessions\/([^/?]+)\/line_items/);
  if (lm) {
    if (lineItemsFail) return new Response('{}', { status: 500 });
    const expanded = new URL(u).searchParams.getAll('expand[]').includes('data.price.product');
    const data = (lineItems[decodeURIComponent(lm[1])] || []).map((i) =>
      expanded ? i : { ...i, price: { ...i.price, product: i.price.product.id } });
    return new Response(JSON.stringify({ data }), { status: 200 });
  }
  if (u.startsWith('https://api.stripe.com/v1/checkout/sessions?')) {
    const pi = new URL(u).searchParams.get('payment_intent');
    return new Response(JSON.stringify({ data: piSessions[pi] ? [piSessions[pi]] : [] }), { status: 200 });
  }
  const sm = u.match(/^https:\/\/api\.stripe\.com\/v1\/subscriptions\/([^/?]+)$/);
  if (sm) {
    const s = subs[decodeURIComponent(sm[1])];
    return s ? new Response(JSON.stringify(s), { status: 200 }) : new Response('{}', { status: 500 });
  }
  if (u.startsWith('https://sb.test/rest/v1/user_plans') && method === 'POST') {
    if (insertFail) return new Response('{"message":"boom"}', { status: 500 });
    const row = JSON.parse(opts.body);
    const ignoring = u.includes('on_conflict=stripe_checkout_session_id') &&
      /resolution=ignore-duplicates/.test(opts.headers?.Prefer || '');
    if (inserted.has(row.stripe_checkout_session_id)) {
      return ignoring ? new Response('[]', { status: 201 }) : new Response('{"code":"23505"}', { status: 409 });
    }
    inserted.set(row.stripe_checkout_session_id, { ...row });
    const wantRows = /return=representation/.test(opts.headers?.Prefer || '');
    return wantRows ? new Response(JSON.stringify([row]), { status: 201 }) : new Response(null, { status: 201 });
  }
  // What the buyer already holds, read before a checkout.
  if (u.startsWith('https://sb.test/rest/v1/user_plans?select=') && method === 'GET') {
    if (holdFail) return new Response('{"message":"down"}', { status: 503 });
    const product = new URL(u).searchParams.get('product').replace(/^eq\./, '');
    return new Response(JSON.stringify(holdings.plans.filter((r) => r.product === product)), { status: 200 });
  }
  if (u.startsWith('https://sb.test/rest/v1/profiles?select=subscription_status') && method === 'GET') {
    if (holdFail) return new Response('{"message":"down"}', { status: 503 });
    return new Response(JSON.stringify(holdings.profile ? [holdings.profile] : []), { status: 200 });
  }
  if (u === 'https://sb.test/rest/v1/funnel_events' && method === 'POST') {
    funnel.push(JSON.parse(opts.body));
    return new Response(null, { status: 201 });
  }
  // A Checkout Session by id (the success page's claim).
  const gs = u.match(/^https:\/\/api\.stripe\.com\/v1\/checkout\/sessions\/([^/?]+)$/);
  if (gs && method === 'GET') {
    const s = stripeSessions[decodeURIComponent(gs[1])];
    return s ? new Response(JSON.stringify(s), { status: 200 }) : new Response('{"error":{}}', { status: 404 });
  }
  // The account for an email, as PostgREST's ilike would match it (case
  // ignored, "_" any one character) so the exact comparison is the Worker's.
  if (u.startsWith('https://sb.test/rest/v1/profiles?select=id,email') && method === 'GET') {
    const pat = decodeURIComponent(new URL(u).searchParams.get('email').replace(/^ilike\./, ''));
    const re = new RegExp('^' + pat.replace(/[.+?^${}()|[\]\\]/g, '\\$&').replace(/_/g, '.').replace(/[%*]/g, '.*') + '$', 'i');
    const rows = [...accounts].filter(([e]) => re.test(e)).map(([email, id]) => ({ id, email }));
    return new Response(JSON.stringify(rows), { status: 200 });
  }
  if (u === 'https://sb.test/auth/v1/admin/users' && method === 'POST') {
    const b = JSON.parse(opts.body);
    if (createFail) return new Response('{"msg":"boom"}', { status: 500 });
    if ([...accounts.keys()].some((e) => e.toLowerCase() === b.email)) return new Response('{"error_code":"email_exists"}', { status: 422 });
    const id = `new-${accounts.size + 1}`;
    accounts.set(b.email, id);
    authUsers[id] = { id, email: b.email, email_confirm: b.email_confirm, user_metadata: b.user_metadata, last_sign_in_at: null };
    return new Response(JSON.stringify(authUsers[id]), { status: 200 });
  }
  const au = u.match(/^https:\/\/sb\.test\/auth\/v1\/admin\/users\/([^/?]+)$/);
  if (au && method === 'GET') {
    const usr = authUsers[decodeURIComponent(au[1])];
    return usr ? new Response(JSON.stringify(usr), { status: 200 }) : new Response('{}', { status: 404 });
  }
  if (u === 'https://sb.test/auth/v1/admin/generate_link' && method === 'POST') {
    if (linkFail) return new Response('{}', { status: 500 });
    const b = JSON.parse(opts.body);
    return new Response(JSON.stringify({ action_link: `https://sb.test/auth/v1/verify?token=x&type=magiclink`, hashed_token: `th-${b.email}`, email: b.email }), { status: 200 });
  }
  if (u.startsWith('https://sb.test/rest/v1/guest_checkouts')) {
    const q = new URL(u).searchParams;
    const sid = (q.get('session_id') || '').replace(/^eq\./, '');
    if (method === 'GET') return new Response(JSON.stringify(guestRows.has(sid) ? [guestRows.get(sid)] : []), { status: 200 });
    if (method === 'POST') {
      const row = JSON.parse(opts.body);
      if (guestRows.has(row.session_id)) return new Response('[]', { status: 201 });
      guestRows.set(row.session_id, { ...row, claimed_at: null });
      return new Response(JSON.stringify([row]), { status: 201 });
    }
    if (method === 'PATCH') {
      const row = guestRows.get(sid);
      const ok = row && (q.get('claimed_at') !== 'is.null' || row.claimed_at === null);
      if (ok) Object.assign(row, JSON.parse(opts.body));
      return /return=representation/.test(prefer(opts))
        ? new Response(JSON.stringify(ok ? [row] : []), { status: 200 }) : new Response(null, { status: 204 });
    }
  }
  if (u.startsWith('https://sb.test/rest/v1/') && method === 'PATCH') {
    if (patchFails) return new Response('{}', { status: 500 });
    // A user_plans row by its Checkout Session: changed for real, and sent
    // back when asked, as PostgREST does (an empty list when nothing matched).
    const cs = new URL(u).searchParams.get('stripe_checkout_session_id');
    const matched = [];
    if (u.startsWith('https://sb.test/rest/v1/user_plans?') && cs) {
      const row = inserted.get(cs.replace(/^eq\./, ''));
      if (row) { Object.assign(row, JSON.parse(opts.body)); matched.push(row); }
    }
    return /return=representation/.test(opts.headers?.Prefer || '')
      ? new Response(JSON.stringify(matched), { status: 200 })
      : new Response(null, { status: 204 });
  }
  throw new Error('unexpected fetch ' + method + ' ' + u);
};
const store = new Map();
globalThis.caches = { default: {
  async match(k) { const v = store.get(k.url); return v ? new Response(v) : undefined; },
  async put(k, v) { store.set(k.url, await v.text()); },
}};
const ctx = { waitUntil: (p) => p };
const realError = console.error;
console.error = (...a) => logs.push(a.join(' '));

function reset() {
  calls = []; sent.length = 0; store.clear(); logs = [];
  promo = { active: true, max_redemptions: 50, times_redeemed: 13 };
  sessionFail = null; lineItems = {}; insertFail = false; patchFails = false; lineItemsFail = false;
  inserted = new Map(); subs = {}; piSessions = {};
  holdings = { plans: [], profile: null }; holdFail = false;
  accounts = new Map([['p@example.com', 'user-1'], ['Old.Parent@example.com', 'old-1']]);
  authUsers = { 'user-1': { id: 'user-1', email: 'p@example.com', user_metadata: {}, last_sign_in_at: '2026-10-01T00:00:00Z' } };
  createFail = false; linkFail = false; stripeSessions = {}; guestRows = new Map(); funnel = [];
}

async function sign(payload, t = Math.floor(Date.now() / 1000)) {
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(SECRET),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(`${t}.${payload}`));
  return { t, v1: [...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, '0')).join('') };
}
async function webhook(event, { header, envOverride } = {}) {
  const payload = JSON.stringify(event);
  const s = await sign(payload);
  const req = new Request('https://x.test/api/stripe-webhook', {
    method: 'POST', body: payload,
    headers: { 'stripe-signature': header ? header(s, payload) : `t=${s.t},v1=${s.v1}` },
  });
  return mod.default.fetch(req, envOverride || env, ctx);
}
async function checkout(body, { token = 'tok-1', cookie, worker = mod } = {}) {
  const headers = { 'Content-Type': 'application/json' };
  if (token) headers.Authorization = `Bearer ${token}`;
  if (cookie) headers.Cookie = cookie;
  const req = new Request('https://x.test/api/create-checkout-session', {
    method: 'POST', body: JSON.stringify(body), headers,
  });
  const res = await worker.default.fetch(req, env, ctx);
  return { res, data: await res.json() };
}
const sessionsPosted = () => calls.filter((c) => c.url === 'https://api.stripe.com/v1/checkout/sessions' && c.method === 'POST').map((c) => c.body);
const insertsMade = () => calls.filter((c) => c.url.includes('/rest/v1/user_plans') && c.method === 'POST').map((c) => JSON.parse(c.body));
const patches = () => calls.filter((c) => c.method === 'PATCH').map((c) => ({ url: c.url, body: JSON.parse(c.body) }));
const stripeCalls = () => calls.filter((c) => c.url.startsWith('https://api.stripe.com'));
// Every parameter Managed Payments forbids on a one-time session
// (docs.stripe.com/payments/managed-payments/update-checkout).
const MP_FORBIDDEN = /^(?:adaptive_pricing|automatic_tax|tax_id_collection|payment_method_types|payment_method_configuration|excluded_payment_method_types|shipping_address_collection|shipping_options|invoice_creation)(?:\[|$)|^customer_update\[(?:name|address)\]|^payment_intent_data\[(?:shipping|application_fee_amount|on_behalf_of|transfer_data|transfer_group|statement_descriptor|statement_descriptor_suffix|receipt_email)\]/;
const paidEvent = (id, extra = {}, type = 'checkout.session.completed') => ({
  type, created: 1791200000,
  data: { object: { id, mode: 'payment', payment_status: 'paid',
    metadata: { supabase_user_id: 'user-1', product: 'x' },
    customer_details: { email: 'parent@example.com' }, ...extra } },
});
const decodeSubject = (raw) => {
  const m = raw.match(/^Subject: (.*)$/m)[1];
  const e = m.match(/^=\?UTF-8\?B\?(.+)\?=$/);
  return e ? Buffer.from(e[1], 'base64').toString('utf8') : m;
};

let pass = 0, fail = 0;
function check(ok, what) { ok ? pass++ : fail++; console.log(`${ok ? ' PASS' : ' FAIL'}  ${what}`); }

// ── founder status ───────────────────────────────────────────────────────
reset();
{
  const get = () => mod.default.fetch(new Request('https://x.test/api/founder-status'), env, ctx);
  const r = await get(); const s = await r.json();
  check(r.status === 200 && s.limit === 50 && s.remaining === 37, `founder status: 13 used of 50 -> 37 left (${JSON.stringify(s)})`);
  promo = { active: true, max_redemptions: 50, times_redeemed: 49 };
  const again = await (await get()).json();
  check(again.remaining === 37 && stripeCalls().length === 1, 'founder status is cached for a minute (one Stripe read)');
  store.clear(); promo = { active: false, max_redemptions: 50, times_redeemed: 3 };
  check((await (await get()).json()).remaining === 0, 'a deactivated code reports no places left');
  store.clear(); promo = null; calls = [];
  const down = await get();
  const down2 = await get();
  check(down.status === 503 && down2.status === 503 && stripeCalls().length === 1,
    'Stripe unreadable -> 503 (page keeps €19), and the failure is cached too: one Stripe read');
}

// ── checkout: who is buying ──────────────────────────────────────────────
reset();
{
  // Not signed in: a guest checkout. Stripe asks for the email; nothing
  // names an account, and the success page gets the session id to claim.
  const none = await checkout({ product: 'ielts' }, { token: null });
  const g = sessionsPosted()[0];
  check(none.res.status === 200 && none.data.url && g['metadata[guest]'] === '1' && !g['metadata[supabase_user_id]'] &&
    !g.customer_email && g.success_url === 'https://x.test/account.html?checkout=success&cs={CHECKOUT_SESSION_ID}&claim={CHECKOUT_SESSION_ID}',
    'no sign-in -> a guest checkout: no account, no email, the success page can claim it');
  check(funnel.some((f) => f.event === 'checkout' && f.guest === true && f.outcome === 'created' && f.product === 'ielts'),
    'the guest checkout is counted (funnel: checkout, guest, created)');
  calls = [];
  const bad = await checkout({ product: 'ielts' }, { token: 'forged' });
  check(bad.res.status === 200 && sessionsPosted()[0]['metadata[guest]'] === '1' && !sessionsPosted()[0]['metadata[supabase_user_id]'],
    'a token Supabase rejects -> a guest checkout, never the account it claims to be');
  calls = [];
  const viaCookie = await checkout({ product: 'ielts' }, { token: null, cookie: 'x=1; fe_at=tok-1' });
  check(viaCookie.data.url && sessionsPosted()[0]['metadata[supabase_user_id]'] === 'user-1', 'the fe_at cookie signs the buyer in too');
  calls = [];
  await checkout({ product: 'ielts', userId: 'victim-9', userEmail: 'victim@example.com' });
  const s = sessionsPosted()[0];
  check(s['metadata[supabase_user_id]'] === 'user-1' && s.customer_email === 'p@example.com',
    'ids in the body are ignored: the purchase goes to the signed-in account');
}

// ── checkout: what is bought ─────────────────────────────────────────────
reset();
{
  const { data } = await checkout({ product: 'blockcamp' });
  const s = sessionsPosted()[0];
  check(data.url && s.mode === 'payment' && s['managed_payments[enabled]'] === 'true' &&
    s['line_items[0][price]'] === 'price_bc' && s['discounts[0][promotion_code]'] === 'promo_founder' &&
    s['metadata[product]'] === 'blockcamp' && s['metadata[supabase_user_id]'] === 'user-1',
    'Block Camp: one-off, Managed Payments on, FOUNDER applied, user and product in metadata');
  check(s.cancel_url === 'https://x.test/pricing.html?checkout=cancelled', 'cancel returns to pricing.html');
  check(s.success_url === 'https://x.test/account.html?checkout=success&cs={CHECKOUT_SESSION_ID}',
    'success returns to the account page with the session id for Stripe to fill in');
  for (const [product, price] of [['ielts', 'price_ielts'], ['ielts_marking', 'price_im'], ['marking', 'price_mk']]) {
    calls = [];
    await checkout({ product });
    const t = sessionsPosted()[0];
    check(t['line_items[0][price]'] === price && !t['discounts[0][promotion_code]'] && t['managed_payments[enabled]'] === 'true' &&
      !stripeCalls().some((c) => c.url.includes('promotion_codes')),
      `${product}: its own price, no founder code, no promo lookup`);
  }
  calls = [];
  for (const product of ['blockcamp', 'ielts', 'ielts_marking', 'marking']) await checkout({ product });
  const banned = sessionsPosted().flatMap((p) => Object.keys(p).filter((k) => MP_FORBIDDEN.test(k)));
  check(sessionsPosted().length === 4 && banned.length === 0, `no product sends a parameter Managed Payments forbids (${banned.join(',') || 'none'})`);
  calls = [];
  await checkout({ product: 'ielts_marking' }, { worker: modOff });
  check(sessionsPosted()[0]['managed_payments[enabled]'] === 'false', 'a product flagged managed:false is sold with Managed Payments off');
  const bad = await checkout({ product: 'sherpa' });
  check(bad.res.status === 400, 'unknown product -> 400');
  const missing = await mod.default.fetch(new Request('https://x.test/api/create-checkout-session', {
    method: 'POST', body: JSON.stringify({ product: 'marking' }), headers: { Authorization: 'Bearer tok-1' } }),
    { ...env, STRIPE_PRICE_ID_MARKING: '' }, ctx);
  check(missing.status === 500, 'price not configured -> 500');
  calls = [];
  await checkout({ plan: 'monthly' });
  const f = sessionsPosted()[0];
  check(f.mode === 'subscription' && f['managed_payments[enabled]'] === 'false' && f['line_items[0][price]'] === 'price_monthly' &&
    f['metadata[supabase_user_id]'] === 'user-1' && f.cancel_url === 'https://x.test/pricing.html?checkout=cancelled',
    'full plan: subscription, Managed Payments off, signed-in account, cancels back to pricing.html');
}

// ── checkout: the founder code under failure ─────────────────────────────
reset();
sessionFail = () => new Response('{"error":{"type":"invalid_request_error","param":"discounts[0][promotion_code]","message":"This promotion code cannot be redeemed because it has been used the maximum number of times."}}', { status: 400 });
{
  const { data } = await checkout({ product: 'blockcamp' });
  const posts = sessionsPosted();
  check(data.url && posts.length === 2 && !posts[1]['discounts[0][promotion_code]'] && logs.some((l) => /FOUNDER refused/.test(l)),
    'last founder place gone mid-checkout -> retried at full price, and logged');
}
for (const [status, what] of [[429, 'rate limited'], [500, 'Stripe 5xx']]) {
  reset();
  sessionFail = () => new Response('{"error":{"message":"try again"}}', { status });
  const { res } = await checkout({ product: 'blockcamp' });
  check(res.status === 502 && sessionsPosted().length === 1, `${what} with the founder code -> 502, never retried at full price`);
}
reset();
sessionFail = () => new Response('{"error":{"param":"customer_email","message":"Invalid email address"}}', { status: 400 });
{
  const { res } = await checkout({ product: 'blockcamp' });
  check(res.status === 502 && sessionsPosted().length === 1, 'a 400 about something else -> 502, the code is kept');
}
reset(); promo = { active: true, max_redemptions: 50, times_redeemed: 50 };
{
  await checkout({ product: 'blockcamp' });
  check(!sessionsPosted()[0]['discounts[0][promotion_code]'], 'founder places all used -> no discount sent');
}

// ── webhook: signature ───────────────────────────────────────────────────
reset();
{
  lineItems.cs_sig = li('ielts', {});
  const bad = await webhook(paidEvent('cs_sig'), { header: (s) => `t=${s.t},v1=${'0'.repeat(64)}` });
  check(bad.status === 400 && insertsMade().length === 0, 'bad signature -> 400, nothing written');
  const payload = JSON.stringify(paidEvent('cs_sig'));
  const old = await sign(payload, Math.floor(Date.now() / 1000) - 3600);
  const replay = await mod.default.fetch(new Request('https://x.test/api/stripe-webhook', {
    method: 'POST', body: payload, headers: { 'stripe-signature': `t=${old.t},v1=${old.v1}` } }), env, ctx);
  check(replay.status === 400 && insertsMade().length === 0, 'correctly signed but an hour old (a replay) -> 400');
  const rolled = await webhook(paidEvent('cs_sig'), { header: (s) => `t=${s.t},v1=${s.v1},v1=${'f'.repeat(64)}` });
  const rolled2 = await webhook(paidEvent('cs_sig2'), { header: (s) => `t=${s.t},v1=${'f'.repeat(64)},v1=${s.v1}` });
  check(rolled.status === 200 && rolled2.status === 200, 'two v1 signatures (secret being rolled): either one matching is accepted');
}

// ── webhook: one-off grants ──────────────────────────────────────────────
reset(); lineItems.cs_bc = li('blockcamp', { term: '1', marking_credits: '0' }, 'Block Camp Term 1');
{
  const r = await webhook(paidEvent('cs_bc'));
  const row = insertsMade()[0];
  check(r.status === 200 && row && row.product === 'blockcamp' && row.term === 1 && row.ends_at === null &&
    row.marking_credits === 0 && row.starts_at === new Date(1791200000 * 1000).toISOString() &&
    row.stripe_checkout_session_id === 'cs_bc' && row.user_id === 'user-1' && row.status === 'active',
    'Block Camp: term 1, drip starts at payment, never ends');
  check(sent.length === 0, 'Block Camp sends no marking email');
}
reset(); lineItems.cs_ie = li('ielts', { marking_credits: '0' }, 'IELTS');
{
  await webhook(paidEvent('cs_ie'));
  const row = insertsMade()[0];
  check(row.product === 'ielts' && row.ends_at === null && row.term === null && row.marking_credits === 0, 'IELTS: no end date, no credits');
}
reset(); lineItems.cs_im = li('IELTS ', { marking_credits: '2' }, 'IELTS + Marking');
{
  await webhook(paidEvent('cs_im'));
  const row = insertsMade()[0];
  check(row.product === 'ielts' && row.marking_credits === 2, 'IELTS + Marking: product normalised to ielts, 2 credits');
  check(sent.length === 1 && sent[0].to === 'marking@forbesenglish.com' && /parent@example\.com/.test(sent[0].raw) &&
    decodeSubject(sent[0].raw) === 'Marking bought: 2 essays (IELTS + Marking)',
    'IELTS + Marking emails the marking inbox once, naming the buyer');
}
reset(); lineItems.cs_mk = li('marking', { marking_credits: '2' }, 'Marking — two essays');
{
  await webhook(paidEvent('cs_mk'));
  const row = insertsMade()[0];
  check(row.product === 'marking' && row.marking_credits === 2 && row.ends_at === null, 'Marking add-on: its own row with 2 credits');
  const subj = sent[0].raw.match(/^Subject: (.*)$/m)[1];
  check(sent.length === 1 && /^=\?UTF-8\?B\?/.test(subj) && decodeSubject(sent[0].raw) === 'Marking bought: 2 essays (Marking — two essays)',
    'the em dash in the subject is RFC 2047 encoded, and decodes back');
  const again = await webhook(paidEvent('cs_mk'));
  check(again.status === 200 && insertsMade().length === 2 && inserted.size === 1 && sent.length === 1,
    'redelivered event: the insert asks to ignore the duplicate, no second row, no second email');
}
reset(); lineItems.cs_un = li('blockcamp', { term: '1' });
{
  const r = await webhook(paidEvent('cs_un', { payment_status: 'unpaid' }));
  check(r.status === 200 && insertsMade().length === 0, 'completed but unpaid (delayed bank payment) -> nothing granted yet');
  const r2 = await webhook(paidEvent('cs_un', {}, 'checkout.session.async_payment_succeeded'));
  check(r2.status === 200 && insertsMade().length === 1, 'async_payment_succeeded grants it');
}
reset(); insertFail = true; lineItems.cs_f = li('ielts', {});
check((await webhook(paidEvent('cs_f'))).status === 500, 'Supabase write fails -> 500 so Stripe redelivers');
reset(); lineItemsFail = true;
{
  const r = await webhook(paidEvent('cs_x'));
  check(r.status === 500 && insertsMade().length === 0, 'line items unreadable -> 500, nothing written');
}
reset(); lineItems.cs_odd = li('sherpa', {});
{
  const r = await webhook(paidEvent('cs_odd'));
  check(r.status === 200 && insertsMade().length === 0 && logs.some((l) => /cs_odd/.test(l)),
    'product metadata not recognised -> logged, nothing granted, no retry loop');
}
reset();
{
  const r = await webhook(paidEvent('cs_anon', { metadata: {}, customer_details: {} }));
  check(r.status === 200 && insertsMade().length === 0 && logs.some((l) => /cs_anon/.test(l)),
    'paid session with no site user and no email -> logged by its session id, nothing granted');
  check(!logs.some((l) => /@example\.com/.test(l)), 'no buyer\'s email address is written to the log');
}
reset();
{
  lineItems.cs_nm = li('marking', { marking_credits: '2' });
  const r = await webhook(paidEvent('cs_nm'), { envOverride: { ...env, MARKING_MAIL: undefined } });
  check(r.status === 200 && insertsMade().length === 1 && sent.length === 0, 'no mail binding: credits still granted, no email');
  lineItems.cs_nt = li('marking', { marking_credits: '2' });
  await webhook(paidEvent('cs_nt'), { envOverride: { ...env, MARKING_MAIL_TO: '' } });
  check(insertsMade().length === 2 && sent.length === 0, 'binding but no inbox address: granted, no email attempted');
}

// ── webhook: the full plan ───────────────────────────────────────────────
reset();
{
  const ev = { type: 'checkout.session.completed', data: { object: { id: 'cs_full', mode: 'subscription',
    customer: 'cus_1', subscription: 'sub_1', metadata: { supabase_user_id: 'user-1', plan: 'monthly' } } } };
  subs.sub_1 = { id: 'sub_1', status: 'active', customer: 'cus_1', items: { data: [{ current_period_end: 1793000000 }] }, metadata: { plan: 'monthly' } };
  const r = await webhook(ev);
  const p = patches()[0];
  check(r.status === 200 && p.url.includes('/profiles?id=eq.user-1') && p.body.subscription_status === 'active' &&
    p.body.current_period_end === new Date(1793000000 * 1000).toISOString() && p.body.stripe_customer_id === 'cus_1',
    'full plan checkout activates the profile, status and period read from Stripe');
  calls = []; subs.sub_1.status = 'canceled';
  await webhook(ev);
  check(patches()[0].body.subscription_status === 'canceled', 'the same checkout event redelivered after a cancellation writes canceled, not active');
  calls = []; patchFails = true; subs.sub_1.status = 'active';
  check((await webhook(ev)).status === 500, 'profile write fails -> 500 so Stripe redelivers');
  calls = []; patchFails = false; delete subs.sub_1;
  check((await webhook(ev)).status === 500 && patches().length === 0, 'subscription unreadable -> 500, nothing written');
}
reset();
{
  subs.sub_2 = { id: 'sub_2', status: 'canceled', customer: 'cus_2', items: { data: [] }, metadata: {} };
  const stale = { type: 'customer.subscription.updated', data: { object: { id: 'sub_2', customer: 'cus_2', status: 'active', metadata: {} } } };
  await webhook(stale);
  const p = patches()[0];
  check(p.url.includes('stripe_customer_id=eq.cus_2') && p.body.subscription_status === 'canceled',
    'a late "updated: active" after the cancellation writes what Stripe has now (canceled)');
  calls = [];
  await webhook({ type: 'customer.subscription.deleted', data: { object: { id: 'sub_2', customer: 'cus_2', status: 'canceled', metadata: {} } } });
  check(patches()[0].body.subscription_status === 'canceled', 'full plan cancellation still closes the profile');
}

// ── webhook: refunds and disputes ────────────────────────────────────────
reset();
{
  piSessions.pi_1 = { id: 'cs_r1', mode: 'payment', metadata: { supabase_user_id: 'user-1', product: 'ielts_marking' } };
  inserted.set('cs_r1', { stripe_checkout_session_id: 'cs_r1', product: 'ielts', status: 'active', marking_credits: 2 });
  const full = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_1', payment_intent: 'pi_1', refunded: true } } });
  const p = patches()[0];
  check(full.status === 200 && p && p.url.includes('user_plans?stripe_checkout_session_id=eq.cs_r1') &&
    p.body.status === 'refunded' && p.body.marking_credits === 0 &&
    inserted.get('cs_r1').status === 'refunded' && insertsMade().length === 0,
    'a full refund closes the one-off and clears its credits');
  calls = [];
  await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_1', payment_intent: 'pi_1', refunded: false } } });
  check(patches().length === 0, 'a partial refund leaves the grant alone');
  await webhook({ type: 'charge.dispute.closed', data: { object: { id: 'dp_1', payment_intent: 'pi_1', status: 'lost' } } });
  check(patches()[0]?.body.status === 'disputed', 'a lost chargeback closes the one-off');
  calls = [];
  await webhook({ type: 'charge.dispute.closed', data: { object: { id: 'dp_2', payment_intent: 'pi_1', status: 'won' } } });
  check(patches().length === 0, 'a won dispute leaves the grant alone');
  piSessions.pi_sub = { id: 'cs_sub', mode: 'subscription' };
  await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_2', payment_intent: 'pi_sub', refunded: true } } });
  check(patches().length === 0, 'a refunded full-plan invoice writes no user_plans row');
  patchFails = true;
  const r = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_1', payment_intent: 'pi_1', refunded: true } } });
  check(r.status === 500, 'revoke write fails -> 500 so Stripe redelivers');
}

// ── webhook: a refund that arrives before its grant ──────────────────────
// The grant failed once and Stripe is still retrying it when the refund
// comes in. The refund must not be lost, and the late grant must not open.
reset(); lineItems.cs_late = li('ielts', { marking_credits: '2' }, 'IELTS + Marking');
{
  piSessions.pi_late = { id: 'cs_late', mode: 'payment', payment_status: 'paid',
    metadata: { supabase_user_id: 'user-1', product: 'ielts_marking' } };
  insertFail = true;
  const first = await webhook(paidEvent('cs_late'));
  insertFail = false;
  const refund = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_l', payment_intent: 'pi_late', refunded: true } } });
  const held = inserted.get('cs_late');
  check(first.status === 500 && refund.status === 200 && held && held.status === 'refunded' &&
    held.marking_credits === 0 && held.product === 'ielts' && held.user_id === 'user-1',
    'refund before the grant: a closed row is left under the same Checkout Session');
  const late = await webhook(paidEvent('cs_late'));
  check(late.status === 200 && inserted.get('cs_late').status === 'refunded' && inserted.size === 1 && sent.length === 0,
    'the late grant finds that row: nothing opens, no credits, no marking email');
}
reset();
{
  piSessions.pi_d = { id: 'cs_d', mode: 'payment', metadata: { supabase_user_id: 'user-1', product: 'blockcamp' } };
  const r = await webhook({ type: 'charge.dispute.closed', data: { object: { id: 'dp_l', payment_intent: 'pi_d', status: 'lost' } } });
  const held = inserted.get('cs_d');
  check(r.status === 200 && held && held.status === 'disputed' && held.product === 'blockcamp' && held.term === 1,
    'a lost dispute before the grant is held closed too');
}
reset();
{
  piSessions.pi_a = { id: 'cs_a', mode: 'payment', metadata: {} };
  const r = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_a', payment_intent: 'pi_a', refunded: true } } });
  check(r.status === 200 && insertsMade().length === 0, 'a refunded sale the site could never grant (no buyer account) writes no row');
  piSessions.pi_u = { id: 'cs_u', mode: 'payment', metadata: { supabase_user_id: 'user-1', product: 'sherpa' } };
  const u = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_u', payment_intent: 'pi_u', refunded: true } } });
  check(u.status === 200 && insertsMade().length === 0, 'nor one for a product the site does not sell');
  piSessions.pi_f = { id: 'cs_f', mode: 'payment', metadata: { supabase_user_id: 'user-1', product: 'ielts' } };
  insertFail = true;
  const f = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_f', payment_intent: 'pi_f', refunded: true } } });
  check(f.status === 500, 'the closed row cannot be written -> 500 so Stripe redelivers the refund');
}

// ── checkout: buying what the buyer already has ──────────────────────────
reset();
{
  holdings.plans = [{ product: 'blockcamp', status: 'active', ends_at: null, term: 1 }];
  const bc = await checkout({ product: 'blockcamp' });
  check(bc.res.status === 409 && bc.data.owned === true && /already have Block Camp Term 1/.test(bc.data.error) &&
    sessionsPosted().length === 0 && !stripeCalls().some((c) => c.url.includes('promotion_codes')),
    'Term 1 already bought -> 409 with a reason, no checkout, no founder place spent');
  calls = [];
  const ie = await checkout({ product: 'ielts' });
  check(ie.data.url && sessionsPosted().length === 1, 'owning Block Camp does not stop buying IELTS');

  holdings.plans = [{ product: 'ielts', status: 'active', ends_at: null, term: null }];
  calls = [];
  const again = await checkout({ product: 'ielts' });
  const bundle = await checkout({ product: 'ielts_marking' });
  check(again.res.status === 409 && bundle.res.status === 409 && /€49/.test(bundle.data.error) && sessionsPosted().length === 0,
    'IELTS already bought -> IELTS and IELTS + Marking both 409, pointing at marking on its own');
  holdings.plans.push({ product: 'marking', status: 'active', ends_at: null, term: null });
  calls = [];
  const mk = await checkout({ product: 'marking' });
  check(mk.data.url && sessionsPosted().length === 1, 'marking can always be bought again: credits add up');

  holdings.plans = [{ product: 'blockcamp', status: 'refunded', ends_at: null, term: 1 }];
  calls = [];
  check((await checkout({ product: 'blockcamp' })).data.url, 'a refunded Term 1 can be bought again');
  holdings.plans = [{ product: 'blockcamp', status: 'active', ends_at: null, term: 2 }];
  check((await checkout({ product: 'blockcamp' })).data.url, 'a Term 2 row does not count as owning Term 1');

  holdings = { plans: [], profile: { subscription_status: 'active' } };
  calls = [];
  const pro = await checkout({ plan: 'monthly' });
  check(pro.res.status === 409 && /Forbes English Pro/.test(pro.data.error) && /info@forbesenglish\.com/.test(pro.data.error) &&
    sessionsPosted().length === 0, 'an active Pro subscriber cannot start a second subscription');
  const keep = await checkout({ product: 'blockcamp' });
  check(keep.data.url, 'a Pro subscriber may still buy Term 1 to keep');
  holdings.profile = { subscription_status: 'canceled' };
  check((await checkout({ plan: 'monthly' })).data.url, 'a cancelled subscriber can subscribe again');

  holdings = { plans: [{ product: 'ielts', status: 'active', ends_at: null }], profile: { subscription_status: 'active' } };
  holdFail = true; calls = []; logs = [];
  const down = await checkout({ product: 'ielts' });
  const down2 = await checkout({ plan: 'monthly' });
  check(down.data.url && down2.data.url && logs.some((l) => /letting the sale through/.test(l)),
    'Supabase unreadable -> the sale goes ahead (and it is logged)');
}

// ── checkout: consent to immediate access ────────────────────────────────
reset();
{
  await checkout({ product: 'ielts' });
  await checkout({ plan: 'monthly' });
  check(sessionsPosted().every((s) => !Object.keys(s).some((k) => /^consent_collection|^custom_text/.test(k))),
    'no TERMS_URL -> no consent asked (Stripe would refuse it without a terms page)');
  calls = [];
  const withTerms = { ...env, TERMS_URL: 'https://x.test/terms.html' };
  for (const body of [{ product: 'blockcamp' }, { product: 'marking' }, { plan: 'monthly' }]) {
    await mod.default.fetch(new Request('https://x.test/api/create-checkout-session', {
      method: 'POST', body: JSON.stringify(body), headers: { Authorization: 'Bearer tok-1' } }), withTerms, ctx);
  }
  const posted = sessionsPosted();
  check(posted.length === 3 && posted.every((s) => s['consent_collection[terms_of_service]'] === 'required' &&
    /\[terms\]\(https:\/\/x\.test\/terms\.html\)/.test(s['custom_text[terms_of_service_acceptance][message]']) &&
    /14-day right/.test(s['custom_text[terms_of_service_acceptance][message]'])),
    'TERMS_URL set -> every checkout asks for the terms and immediate access, linking the page');
  const banned = posted.flatMap((p) => Object.keys(p).filter((k) => MP_FORBIDDEN.test(k)));
  check(banned.length === 0, 'and the consent parameters are not ones Managed Payments forbids');
}

// ── guest checkout: the full plan, and the owned refusal is counted ─────
reset();
{
  const { res } = await checkout({ plan: 'monthly' }, { token: null });
  const s = sessionsPosted()[0];
  check(res.status === 200 && s.mode === 'subscription' && s['metadata[guest]'] === '1' && s['subscription_data[metadata][guest]'] === '1' &&
    !s.customer_email && !s['metadata[supabase_user_id]'] && /&claim=\{CHECKOUT_SESSION_ID\}$/.test(s.success_url),
    'guest Forbes English Pro: subscription, guest in both metadata, claimable success page');
  holdings.plans = [{ product: 'blockcamp', status: 'active', ends_at: null, term: 1 }];
  await checkout({ product: 'blockcamp' });
  check(funnel.some((f) => f.event === 'checkout' && f.outcome === 'owned' && f.guest === false), 'an "already have it" refusal is counted as owned');
}

// ── guest checkout: the webhook finds or makes the account ──────────────
const guestEvent = (id, email, extra = {}, type) => paidEvent(id, { metadata: { guest: '1', product: 'blockcamp' },
  customer_details: { email }, ...extra }, type);
reset(); lineItems.cs_g1 = li('blockcamp', { term: '1' }, 'Block Camp Term 1');
{
  const r = await webhook(guestEvent('cs_g1', 'New.Parent@Example.com'));
  const row = insertsMade()[0];
  const made = Object.values(authUsers).find((x) => x.email === 'new.parent@example.com');
  check(r.status === 200 && made && made.email_confirm === true && made.user_metadata.via === 'checkout' && made.user_metadata.needs_password === true,
    'guest, new email: the account is made, confirmed, marked as made by checkout, email lower-cased');
  check(row && row.user_id === made.id && row.product === 'blockcamp' && guestRows.get('cs_g1').user_id === made.id &&
    guestRows.get('cs_g1').created_account === true, 'and the purchase is on it, recorded in guest_checkouts');
  check(funnel.filter((f) => f.event === 'paid').length === 1 && funnel.find((f) => f.event === 'paid').guest === true, 'the sale is counted once, as a guest sale');
  const again = await webhook(guestEvent('cs_g1', 'new.parent@example.com'));
  check(again.status === 200 && Object.keys(authUsers).length === 2 && funnel.filter((f) => f.event === 'paid').length === 1,
    'redelivered: no second account, no second count');
}
reset(); lineItems.cs_g2 = li('ielts', {}, 'IELTS');
{
  const r = await webhook(guestEvent('cs_g2', 'old.parent@EXAMPLE.com'));
  check(r.status === 200 && insertsMade()[0].user_id === 'old-1' && Object.keys(authUsers).length === 1 &&
    guestRows.get('cs_g2').created_account === false, 'guest, email of an existing account (any case): the purchase goes on it, nothing made');
}
reset(); lineItems.cs_g3 = li('ielts', {}, 'IELTS');
{
  // The buyer's "_" is a one-letter wildcard to ilike, so "o_ther" also
  // finds "oxther"; only the exact comparison keeps the two apart.
  accounts.set('oxther@example.com', 'other-1');
  const r = await webhook(guestEvent('cs_g3', 'o_ther@example.com'));
  check(r.status === 200 && insertsMade()[0] && insertsMade()[0].user_id !== 'other-1' &&
    Object.values(authUsers).some((x) => x.email === 'o_ther@example.com'),
    'an "_" in the buyer\'s address does not match another account; theirs is made');
}
reset(); lineItems.cs_g4 = li('ielts', {}, 'IELTS'); createFail = true;
{
  const r = await webhook(guestEvent('cs_g4', 'fresh@example.com'));
  check(r.status === 500 && insertsMade().length === 0 && !guestRows.has('cs_g4'), 'account cannot be made -> 500, Stripe redelivers, nothing granted');
}
reset();
{
  subs.sub_g = { id: 'sub_g', status: 'active', customer: 'cus_g', items: { data: [{ current_period_end: 1793000000 }] }, metadata: { plan: 'monthly', guest: '1' } };
  const ev = { type: 'checkout.session.completed', created: 1791200000, data: { object: { id: 'cs_gsub', mode: 'subscription', customer: 'cus_g',
    subscription: 'sub_g', metadata: { guest: '1', plan: 'monthly' }, customer_details: { email: 'sub.parent@example.com' } } } };
  const r = await webhook(ev);
  const made = Object.values(authUsers).find((x) => x.email === 'sub.parent@example.com');
  const p = patches().find((x) => x.url.includes('/profiles?id='));
  check(r.status === 200 && made && p && p.url.includes(`id=eq.${made.id}`) && p.body.subscription_status === 'active' && p.body.plan === 'monthly',
    'guest Forbes English Pro: account made, subscription written onto it');
  check(funnel.some((f) => f.event === 'paid' && f.product === 'monthly' && f.guest === true), 'and counted as a guest sale');
}

// ── the success page's claim ─────────────────────────────────────────────
async function claim(cs) {
  const res = await mod.default.fetch(new Request('https://x.test/api/claim-checkout', {
    method: 'POST', body: JSON.stringify({ cs }), headers: { 'Content-Type': 'application/json' } }), env, ctx);
  return { res, data: await res.json() };
}
const NOW = Math.floor(Date.now() / 1000);
const guestSession = (id, email, extra = {}) => ({ id, object: 'checkout.session', mode: 'payment', status: 'complete', payment_status: 'paid',
  created: NOW - 60, metadata: { guest: '1', product: 'blockcamp' }, customer_details: { email }, ...extra });
reset(); lineItems.cs_live_c1aaaaaaaaaa = li('blockcamp', { term: '1' }, 'Block Camp Term 1');
{
  stripeSessions.cs_live_c1aaaaaaaaaa = guestSession('cs_live_c1aaaaaaaaaa', 'claim.me@example.com');
  const a = await claim('cs_live_c1aaaaaaaaaa');
  const made = Object.values(authUsers).find((x) => x.email === 'claim.me@example.com');
  check(a.res.status === 200 && a.data.state === 'new_account' && a.data.token_hash === 'th-claim.me@example.com' && a.data.email === 'claim.me@example.com',
    'claim before the webhook: the account is made and the buyer gets a one-time sign-in');
  check(insertsMade().length === 1 && insertsMade()[0].user_id === made.id && guestRows.get('cs_live_c1aaaaaaaaaa').claimed_at,
    'and the purchase is already on it (fulfilled by the claim), the claim marked used');
  const b = await claim('cs_live_c1aaaaaaaaaa');
  check(b.data.state === 'existing_account' && !b.data.token_hash, 'a second claim of the same checkout gets no sign-in');
  const w = await webhook(guestEvent('cs_live_c1aaaaaaaaaa', 'claim.me@example.com'));
  check(w.status === 200 && Object.keys(authUsers).length === 2 && inserted.size === 1 && funnel.filter((f) => f.event === 'paid').length === 1,
    'the webhook arriving afterwards: same account, same row, one sale counted');
}
reset(); lineItems.cs_live_c2aaaaaaaaaa = li('blockcamp', { term: '1' });
{
  stripeSessions.cs_live_c2aaaaaaaaaa = guestSession('cs_live_c2aaaaaaaaaa', 'signed.in@example.com');
  await webhook(guestEvent('cs_live_c2aaaaaaaaaa', 'signed.in@example.com'));
  const made = Object.values(authUsers).find((x) => x.email === 'signed.in@example.com');
  made.last_sign_in_at = '2026-10-09T10:00:00Z';
  const a = await claim('cs_live_c2aaaaaaaaaa');
  check(a.data.state === 'existing_account' && !a.data.token_hash, 'an account made by checkout but already signed into: no sign-in handed out');
}
reset(); lineItems.cs_live_c3aaaaaaaaaa = li('ielts', {});
{
  stripeSessions.cs_live_c3aaaaaaaaaa = guestSession('cs_live_c3aaaaaaaaaa', 'p@example.com');
  const a = await claim('cs_live_c3aaaaaaaaaa');
  check(a.data.state === 'existing_account' && a.data.email === 'p@example.com' && !a.data.token_hash && insertsMade()[0].user_id === 'user-1',
    'email of an existing account: the purchase goes on it, and the buyer is asked to log in');
}
reset();
{
  stripeSessions.cs_live_c4aaaaaaaaaa = guestSession('cs_live_c4aaaaaaaaaa', 'slow@example.com', { payment_status: 'unpaid' });
  stripeSessions.cs_live_c5aaaaaaaaaa = guestSession('cs_live_c5aaaaaaaaaa', 'gone@example.com', { status: 'open', payment_status: 'unpaid' });
  stripeSessions.cs_live_c6aaaaaaaaaa = guestSession('cs_live_c6aaaaaaaaaa', 'p@example.com', { metadata: { supabase_user_id: 'user-1', product: 'ielts' } });
  check((await claim('cs_live_c4aaaaaaaaaa')).data.state === 'processing', 'paid by a method that clears later -> processing, nothing made');
  check((await claim('cs_live_c5aaaaaaaaaa')).data.state === 'not_paid', 'checkout not completed -> not_paid');
  check((await claim('cs_live_c6aaaaaaaaaa')).data.state === 'signed_in_purchase', 'bought while signed in -> nothing to claim');
  check(Object.keys(authUsers).length === 1 && insertsMade().length === 0, 'none of those made an account or granted anything');
  check((await claim('not-a-session')).res.status === 400, 'not a session id -> 400');
  check((await claim('cs_live_unknownaaaaaa')).res.status === 404, 'a session Stripe does not know -> 404');
}
reset(); lineItems.cs_live_c7aaaaaaaaaa = li('blockcamp', { term: '1' });
{
  stripeSessions.cs_live_c7aaaaaaaaaa = guestSession('cs_live_c7aaaaaaaaaa', 'late@example.com', { created: NOW - 3 * 86400 });
  const a = await claim('cs_live_c7aaaaaaaaaa');
  check(a.data.state === 'existing_account' && !a.data.token_hash && insertsMade().length === 1,
    'a success page opened three days later: the purchase is there, but no sign-in from an old link');
}
reset(); lineItems.cs_live_c8aaaaaaaaaa = li('blockcamp', { term: '1' }); linkFail = true;
{
  stripeSessions.cs_live_c8aaaaaaaaaa = guestSession('cs_live_c8aaaaaaaaaa', 'nolink@example.com');
  const a = await claim('cs_live_c8aaaaaaaaaa');
  check(!a.data.token_hash && insertsMade().length === 1, 'sign-in link cannot be made: no token, the purchase still granted');
}

// ── the funnel count of page views ───────────────────────────────────────
async function visit(path, headers = {}) {
  funnel.length = 0;
  await mod.default.fetch(new Request('https://x.test' + path, { headers: { Accept: 'text/html,*/*', 'User-Agent': 'Mozilla/5.0 (iPhone) FBAN/FBIOS', ...headers } }), env, ctx);
  return funnel.slice();
}
reset();
{
  const home = await visit('/', { Referer: 'https://m.facebook.com/' });
  check(home.length === 1 && home[0].event === 'view' && home[0].path === '/' && home[0].ref_host === 'm.facebook.com' && home[0].mobile === true,
    'the home page is counted: view, from m.facebook.com, on a phone (Facebook\'s in-app browser is a visitor)');
  const ad = await visit('/library.html?utm_source=facebook&utm_medium=paid&utm_campaign=bc-oct&fbclid=abc');
  check(ad.length === 1 && ad[0].event === 'landing' && ad[0].path === '/library' && ad[0].utm_source === 'facebook' &&
    ad[0].utm_campaign === 'bc-oct' && ad[0].click === 'fbclid', 'a tagged ad click is a landing, with its tags');
  check((await visit('/past-simple.html')).length === 0, 'an untagged visit to an ordinary page is not counted');
  check((await visit('/pricing', { 'User-Agent': 'facebookexternalhit/1.1' })).length === 0, 'a link preview is not counted');
  check((await visit('/pricing', { Accept: 'image/webp' })).length === 0, 'a request that is not for a page is not counted');
  funnel.length = 0;
  await mod.default.fetch(new Request('https://x.test/pricing', { headers: { Accept: 'text/html', 'User-Agent': 'Mozilla/5.0' } }), { ...env, FUNNEL: 'off' }, ctx);
  check(funnel.length === 0, 'FUNNEL=off counts nothing');
  const priv = await visit('/pricing?email=someone@example.com');
  check(priv.length === 1 && !JSON.stringify(priv).includes('someone@'), 'a query string is never stored, only utm_ tags');
}

console.error = realError;
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
