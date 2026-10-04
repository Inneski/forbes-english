// Forbes English — checkout, founder count and Stripe webhook tests.
//
//   node deploy/test-webhook.mjs        (run from the repo root)
//
// Run beside deploy/test-paywall.mjs after any change to src/index.js.
// Stripe and Supabase are stubbed; every request the Worker makes is
// recorded, so each case asserts what was actually sent.
//
import { readFileSync } from 'fs';
const src = readFileSync('src/index.js', 'utf8').replace(
  /^import \{ EmailMessage \} from "cloudflare:email";$/m,
  'class EmailMessage { constructor(f, t, r) { this.from = f; this.to = t; this.raw = r; } }');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));

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
let calls = [];
let promo = { active: true, max_redemptions: 50, times_redeemed: 13 };
let rejectDiscount = false;           // Stripe refuses the founder code
let lineItems = {};                   // session id -> line items
let insertMode = 'new';               // 'new' | 'dup' | 'fail'
let patchFails = false;
let lineItemsFail = false;

const PRODUCT = (product, extra = {}) => ({ name: extra.name || product, metadata: { product, ...extra.meta } });
function li(product, meta, name) {
  return [{ quantity: 1, price: { id: 'price_x', product: PRODUCT(product, { meta, name }) } }];
}

globalThis.fetch = async (url, opts = {}) => {
  const u = String(url);
  const body = opts.body instanceof URLSearchParams ? Object.fromEntries(opts.body) : opts.body;
  calls.push({ url: u, method: opts.method || 'GET', body });
  if (u.startsWith('https://api.stripe.com/v1/promotion_codes/')) {
    return promo ? new Response(JSON.stringify(promo), { status: 200 }) : new Response('{}', { status: 500 });
  }
  if (u === 'https://api.stripe.com/v1/checkout/sessions') {
    if (rejectDiscount && body['discounts[0][promotion_code]']) {
      return new Response('{"error":{"message":"This promotion code cannot be redeemed because it has been used the maximum number of times."}}', { status: 400 });
    }
    return new Response(JSON.stringify({ url: 'https://checkout.stripe.test/s' }), { status: 200 });
  }
  const m = u.match(/^https:\/\/api\.stripe\.com\/v1\/checkout\/sessions\/([^/]+)\/line_items/);
  if (m) {
    if (lineItemsFail) return new Response('{}', { status: 500 });
    return new Response(JSON.stringify({ data: lineItems[decodeURIComponent(m[1])] || [] }), { status: 200 });
  }
  if (u.startsWith('https://sb.test/rest/v1/user_plans') && opts.method === 'POST') {
    if (insertMode === 'fail') return new Response('{"message":"boom"}', { status: 500 });
    return new Response(insertMode === 'dup' ? '[]' : JSON.stringify([JSON.parse(opts.body)]), { status: 201 });
  }
  if (u.startsWith('https://sb.test/rest/v1/') && opts.method === 'PATCH') {
    return patchFails ? new Response('{}', { status: 500 }) : new Response(null, { status: 204 });
  }
  throw new Error('unexpected fetch ' + u);
};
const store = new Map();
globalThis.caches = { default: {
  async match(k) { const v = store.get(k.url); return v ? new Response(v) : undefined; },
  async put(k, v) { store.set(k.url, await v.text()); },
}};
const ctx = { waitUntil: (p) => p };

function reset() {
  calls = []; sent.length = 0; store.clear();
  promo = { active: true, max_redemptions: 50, times_redeemed: 13 };
  rejectDiscount = false; insertMode = 'new'; patchFails = false; lineItemsFail = false;
}

async function sign(payload) {
  const t = Math.floor(Date.now() / 1000);
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(SECRET),
    { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(`${t}.${payload}`));
  return `t=${t},v1=${[...new Uint8Array(sig)].map((b) => b.toString(16).padStart(2, '0')).join('')}`;
}
async function webhook(event, { badSig = false } = {}) {
  const payload = JSON.stringify(event);
  const req = new Request('https://x.test/api/stripe-webhook', {
    method: 'POST', body: payload,
    headers: { 'stripe-signature': badSig ? 't=1,v1=00' : await sign(payload) },
  });
  return mod.default.fetch(req, env, ctx);
}
async function checkout(body) {
  const req = new Request('https://x.test/api/create-checkout-session', {
    method: 'POST', body: JSON.stringify(body), headers: { 'Content-Type': 'application/json' },
  });
  const res = await mod.default.fetch(req, env, ctx);
  return { res, data: await res.json() };
}
const sessionsPosted = () => calls.filter((c) => c.url === 'https://api.stripe.com/v1/checkout/sessions').map((c) => c.body);
const inserts = () => calls.filter((c) => c.url.includes('/rest/v1/user_plans') && c.method === 'POST').map((c) => JSON.parse(c.body));
const paidEvent = (id, extra = {}, type = 'checkout.session.completed') => ({
  type, created: 1791200000,
  data: { object: { id, mode: 'payment', payment_status: 'paid',
    metadata: { supabase_user_id: 'user-1', product: 'x' },
    customer_details: { email: 'parent@example.com' }, ...extra } },
});

let pass = 0, fail = 0;
function check(ok, what) { ok ? pass++ : fail++; console.log(`${ok ? ' PASS' : ' FAIL'}  ${what}`); }

// ── founder status ───────────────────────────────────────────────────────
reset();
{
  const r = await mod.default.fetch(new Request('https://x.test/api/founder-status'), env, ctx);
  const s = await r.json();
  check(r.status === 200 && s.limit === 50 && s.remaining === 37, `founder status: 13 used of 50 -> 37 left (${JSON.stringify(s)})`);
  promo = { active: true, max_redemptions: 50, times_redeemed: 49 };
  const again = await (await mod.default.fetch(new Request('https://x.test/api/founder-status'), env, ctx)).json();
  check(again.remaining === 37, 'founder status is cached for a minute (one Stripe read)');
  store.clear(); promo = { active: false, max_redemptions: 50, times_redeemed: 3 };
  const off = await (await mod.default.fetch(new Request('https://x.test/api/founder-status'), env, ctx)).json();
  check(off.remaining === 0, 'a deactivated code reports no places left');
  store.clear(); promo = null;
  const down = await mod.default.fetch(new Request('https://x.test/api/founder-status'), env, ctx);
  check(down.status === 503, 'Stripe unreadable -> 503, so the page keeps €19');
}

// ── checkout ─────────────────────────────────────────────────────────────
reset();
{
  const { data } = await checkout({ userId: 'user-1', userEmail: 'p@example.com', product: 'blockcamp' });
  const s = sessionsPosted()[0];
  check(data.url && s.mode === 'payment' && s['managed_payments[enabled]'] === 'true' &&
    s['line_items[0][price]'] === 'price_bc' && s['discounts[0][promotion_code]'] === 'promo_founder' &&
    s['metadata[product]'] === 'blockcamp' && s['metadata[supabase_user_id]'] === 'user-1',
    'Block Camp: one-off, Managed Payments on, FOUNDER applied, user and product in metadata');
  check(s.cancel_url === 'https://x.test/pricing.html?checkout=cancelled', 'cancel returns to pricing.html');
  const banned = ['automatic_tax[enabled]', 'payment_method_types[0]', 'invoice_creation[enabled]', 'tax_id_collection[enabled]',
    'payment_intent_data[receipt_email]', 'shipping_address_collection[allowed_countries][0]'].filter((k) => k in s);
  check(banned.length === 0, 'no parameter Managed Payments forbids');
}
reset(); rejectDiscount = true;
{
  const { data } = await checkout({ userId: 'user-1', userEmail: 'p@example.com', product: 'blockcamp' });
  const posts = sessionsPosted();
  check(data.url && posts.length === 2 && !posts[1]['discounts[0][promotion_code]'],
    'last founder place gone between count and checkout -> retried at full price, buyer still gets a checkout');
}
reset(); promo = { active: true, max_redemptions: 50, times_redeemed: 50 };
{
  await checkout({ userId: 'user-1', userEmail: 'p@example.com', product: 'blockcamp' });
  check(!sessionsPosted()[0]['discounts[0][promotion_code]'], 'founder places all used -> no discount sent');
}
reset();
{
  for (const [product, price] of [['ielts', 'price_ielts'], ['ielts_marking', 'price_im'], ['marking', 'price_mk']]) {
    calls = [];
    await checkout({ userId: 'user-1', userEmail: 'p@example.com', product });
    const s = sessionsPosted()[0];
    check(s['line_items[0][price]'] === price && !s['discounts[0][promotion_code]'] && s['managed_payments[enabled]'] === 'true' &&
      !calls.some((c) => c.url.includes('promotion_codes')),
      `${product}: its own price, no founder code and no promo lookup`);
  }
  const bad = await checkout({ userId: 'user-1', userEmail: 'p@example.com', product: 'sherpa' });
  check(bad.res.status === 400, 'unknown product -> 400');
  const missing = await mod.default.fetch(new Request('https://x.test/api/create-checkout-session', {
    method: 'POST', body: JSON.stringify({ userId: 'u', userEmail: 'e', product: 'marking' }) }),
    { ...env, STRIPE_PRICE_ID_MARKING: '' }, ctx);
  check(missing.status === 500, 'price not configured -> 500, nothing sent to Stripe');
  calls = [];
  await checkout({ userId: 'user-1', userEmail: 'p@example.com', plan: 'monthly' });
  const f = sessionsPosted()[0];
  check(f.mode === 'subscription' && f['managed_payments[enabled]'] === 'false' && f['line_items[0][price]'] === 'price_monthly' &&
    f.cancel_url === 'https://x.test/pricing.html?checkout=cancelled',
    'full plan unchanged: subscription, Managed Payments off, now cancels back to pricing.html');
}

// ── webhook ──────────────────────────────────────────────────────────────
reset();
{
  const r = await webhook(paidEvent('cs_1'), { badSig: true });
  check(r.status === 400 && inserts().length === 0, 'bad signature -> 400, nothing written');
}
reset(); lineItems.cs_bc = li('blockcamp', { term: '1', marking_credits: '0' }, 'Block Camp Term 1');
{
  const r = await webhook(paidEvent('cs_bc'));
  const row = inserts()[0];
  check(r.status === 200 && row && row.product === 'blockcamp' && row.term === 1 && row.ends_at === null &&
    row.marking_credits === 0 && row.starts_at === new Date(1791200000 * 1000).toISOString() &&
    row.stripe_checkout_session_id === 'cs_bc' && row.user_id === 'user-1' && row.status === 'active',
    `Block Camp: term 1, drip starts at payment, never ends (${JSON.stringify(row)})`);
  check(sent.length === 0, 'Block Camp sends no marking email');
}
reset(); lineItems.cs_ie = li('ielts', { marking_credits: '0' }, 'IELTS');
{
  await webhook(paidEvent('cs_ie'));
  const row = inserts()[0];
  check(row.product === 'ielts' && row.ends_at === null && row.term === null && row.marking_credits === 0,
    'IELTS: no end date, no credits');
}
reset(); lineItems.cs_im = li('IELTS ', { marking_credits: '2' }, 'IELTS + Marking');
{
  await webhook(paidEvent('cs_im'));
  const row = inserts()[0];
  check(row.product === 'ielts' && row.marking_credits === 2, 'IELTS + Marking: product normalised to ielts, 2 credits');
  check(sent.length === 1 && sent[0].to === 'marking@forbesenglish.com' && /2 essays/.test(sent[0].raw) &&
    /parent@example\.com/.test(sent[0].raw), 'IELTS + Marking emails the marking inbox once, naming the buyer');
}
reset(); lineItems.cs_mk = li('marking', { marking_credits: '2' }, 'Marking — two essays');
{
  await webhook(paidEvent('cs_mk'));
  const row = inserts()[0];
  check(row.product === 'marking' && row.marking_credits === 2 && row.ends_at === null,
    'Marking add-on: its own row with 2 credits (summed per account)');
  check(sent.length === 1, 'Marking add-on emails the marking inbox');
}
reset(); insertMode = 'dup'; lineItems.cs_mk = li('marking', { marking_credits: '2' });
{
  const r = await webhook(paidEvent('cs_mk'));
  check(r.status === 200 && sent.length === 0, 'redelivered event: no new row, no second email, still 200');
}
reset(); lineItems.cs_un = li('blockcamp', { term: '1' });
{
  const r = await webhook(paidEvent('cs_un', { payment_status: 'unpaid' }));
  check(r.status === 200 && inserts().length === 0, 'completed but unpaid (delayed bank payment) -> nothing granted yet');
  const r2 = await webhook(paidEvent('cs_un', {}, 'checkout.session.async_payment_succeeded'));
  check(r2.status === 200 && inserts().length === 1, 'async_payment_succeeded grants it');
}
reset(); insertMode = 'fail'; lineItems.cs_f = li('ielts', {});
{
  const r = await webhook(paidEvent('cs_f'));
  check(r.status === 500, 'Supabase write fails -> 500 so Stripe redelivers');
}
reset(); lineItemsFail = true;
{
  const r = await webhook(paidEvent('cs_x'));
  check(r.status === 500 && inserts().length === 0, 'line items unreadable -> 500, nothing written');
}
reset(); lineItems.cs_odd = li('sherpa', {});
{
  const r = await webhook(paidEvent('cs_odd'));
  check(r.status === 200 && inserts().length === 0, 'product metadata not recognised -> logged, nothing granted, no retry loop');
}
reset();
{
  const r = await webhook(paidEvent('cs_anon', { metadata: {} }));
  check(r.status === 200 && calls.length === 0, 'paid session with no site user -> left to the dashboard');
}
reset();
{
  const ev = { type: 'checkout.session.completed', data: { object: { id: 'cs_full', mode: 'subscription',
    customer: 'cus_1', subscription: 'sub_1', metadata: { supabase_user_id: 'user-1', plan: 'monthly' } } } };
  const r = await webhook(ev);
  const p = calls.find((c) => c.method === 'PATCH');
  check(r.status === 200 && p && p.url.includes('/profiles?id=eq.user-1') && JSON.parse(p.body).subscription_status === 'active',
    'full plan checkout still activates the profile');
  calls = []; patchFails = true;
  const r2 = await webhook(ev);
  check(r2.status === 500, 'full plan profile write fails -> 500 so Stripe redelivers');
}
reset();
{
  const r = await webhook({ type: 'customer.subscription.deleted', data: { object: { id: 'sub_1', customer: 'cus_1', metadata: {} } } });
  const p = calls.find((c) => c.method === 'PATCH');
  check(r.status === 200 && p.url.includes('stripe_customer_id=eq.cus_1') && JSON.parse(p.body).subscription_status === 'canceled',
    'full plan cancellation still closes the profile');
}
reset();
{
  const noMail = { ...env, MARKING_MAIL: undefined };
  lineItems.cs_nm = li('marking', { marking_credits: '2' });
  const payload = JSON.stringify(paidEvent('cs_nm'));
  const r = await mod.default.fetch(new Request('https://x.test/api/stripe-webhook', {
    method: 'POST', body: payload, headers: { 'stripe-signature': await sign(payload) } }), noMail, ctx);
  check(r.status === 200 && inserts().length === 1 && sent.length === 0, 'no mail binding: credits still granted, no email, no error');
}

console.log(`\n${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
