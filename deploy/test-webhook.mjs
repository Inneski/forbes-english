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
let subs, piSessions, logs;
const USERS = { 'tok-1': { id: 'user-1', email: 'p@example.com' } };

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
    inserted.add(row.stripe_checkout_session_id);
    const wantRows = /return=representation/.test(opts.headers?.Prefer || '');
    return wantRows ? new Response(JSON.stringify([row]), { status: 201 }) : new Response(null, { status: 201 });
  }
  if (u.startsWith('https://sb.test/rest/v1/') && method === 'PATCH') {
    return patchFails ? new Response('{}', { status: 500 }) : new Response(null, { status: 204 });
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
  inserted = new Set(); subs = {}; piSessions = {};
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
  const none = await checkout({ product: 'ielts' }, { token: null });
  check(none.res.status === 401 && sessionsPosted().length === 0, 'no sign-in -> 401, nothing sent to Stripe');
  const bad = await checkout({ product: 'ielts' }, { token: 'forged' });
  check(bad.res.status === 401 && sessionsPosted().length === 0, 'a token Supabase rejects -> 401');
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
  const r = await webhook(paidEvent('cs_anon', { metadata: {} }));
  check(r.status === 200 && calls.length === 0 && logs.some((l) => /cs_anon.*parent@example\.com/.test(l)),
    'paid session with no site user (a Payment Link) -> logged with the buyer, nothing granted');
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
  piSessions.pi_1 = { id: 'cs_r1', mode: 'payment' };
  const full = await webhook({ type: 'charge.refunded', data: { object: { id: 'ch_1', payment_intent: 'pi_1', refunded: true } } });
  const p = patches()[0];
  check(full.status === 200 && p && p.url.includes('user_plans?stripe_checkout_session_id=eq.cs_r1') &&
    p.body.status === 'refunded' && p.body.marking_credits === 0,
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

console.error = realError;
console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
