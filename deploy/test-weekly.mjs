// Forbes English — the weekly "Mission N is open" email (pricing step 9).
//
//   node deploy/test-weekly.mjs        (run from the repo root)
//
// Runs the Worker's scheduled() handler against stubbed Supabase and Resend
// at fixed times, and asserts who is mailed, what the email says, that a
// mission is never mailed twice, and that a failed send is retried.
//
import { readFileSync } from 'fs';
const src = readFileSync('src/index.js', 'utf8').replace(
  /^import \{ EmailMessage \} from "cloudflare:email";$/m,
  'class EmailMessage { constructor(f, t, r) { this.from = f; this.to = t; this.raw = r; } }');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));

const DAY = 86400000;
const NOW = Date.parse('2026-11-02T06:00:00Z');
const at = (days) => new Date(NOW - days * DAY).toISOString();
const env = {
  SITE_URL: 'https://forbesenglish.com', SUPABASE_URL: 'https://sb.test',
  SUPABASE_ANON_KEY: 'anon', SUPABASE_SERVICE_ROLE_KEY: 'service',
  RESEND_API_KEY: 're_test', MAIL_FROM: 'Forbes English <info@forbesenglish.com>',
  MAIL_REPLY_TO: 'info@forbesenglish.com', MARKING_MAIL_TO: 'info@forbesenglish.com',
};
const LESSONS = [];
for (let m = 1; m <= 12; m++) {
  LESSONS.push({ file: `blockcamp-m${m}.html`, title: `Block Camp — Deck ${m}`, mission: m });
  if (![4, 8, 12].includes(m)) LESSONS.push({ file: `block-camp/quest-${m}.html`, title: `Quest ${m}`, mission: m });
}

let PLANS, PROFILES, claims, mails, resendFails, readFail, calls;
function reset() {
  PLANS = []; PROFILES = []; claims = new Map(); mails = []; resendFails = 0; readFail = false; calls = [];
}
// PostgREST's paging, so a read that forgot it would be cut off at 1000.
const page = (rows, u) => {
  const q = new URL(u.replace(/ /g, '%20')).searchParams;
  const off = Number(q.get('offset') || 0), lim = Math.min(Number(q.get('limit') || 1000), 1000);
  return rows.slice(off, off + lim);
};
const profile = (id, extra = {}) => ({ id, email: `${id}@example.com`, owner: false, subscription_status: 'inactive',
  blockcamp_first_open: null, blockcamp_emails: true, ...extra });

globalThis.fetch = async (url, opts = {}) => {
  const u = decodeURIComponent(String(url));
  const method = opts.method || 'GET';
  calls.push(`${method} ${u}`);
  if (u === 'https://api.resend.com/emails') {
    const body = JSON.parse(opts.body);
    if (resendFails > 0) { resendFails--; return new Response('{"message":"boom"}', { status: 500 }); }
    mails.push({ ...body, key: opts.headers['Idempotency-Key'], auth: opts.headers.Authorization });
    return new Response('{"id":"e1"}', { status: 200 });
  }
  if (readFail && method === 'GET') return new Response('{}', { status: 500 });
  if (u.startsWith('https://sb.test/rest/v1/user_plans')) return new Response(JSON.stringify(page(PLANS.map(({ user_id, term, starts_at }) => ({ user_id, term, starts_at })), u)));
  if (u.startsWith('https://sb.test/rest/v1/profiles?select=id&')) {
    return new Response(JSON.stringify(page(PROFILES.filter((p) => p.blockcamp_first_open && ['active', 'trialing'].includes(p.subscription_status)).map((p) => ({ id: p.id })), u)));
  }
  if (u.startsWith('https://sb.test/rest/v1/profiles?select=id,email')) {
    const ids = u.match(/id=in\.\(([^)]*)\)/)[1].split(',');
    if (ids.length > 100) return new Response('{"message":"URL too long"}', { status: 400 });
    return new Response(JSON.stringify(PROFILES.filter((p) => ids.includes(p.id))));
  }
  if (u.startsWith('https://sb.test/rest/v1/lessons')) return new Response(JSON.stringify(LESSONS));
  if (u.startsWith('https://sb.test/rest/v1/blockcamp_mission_emails') && method === 'GET') {
    const ids = u.match(/user_id=in\.\(([^)]*)\)/)[1].split(',');
    if (ids.length > 100) return new Response('{"message":"URL too long"}', { status: 400 });
    const rows = [...claims].map(([k, v]) => { const [user_id, term, mission] = k.split('/'); return { user_id, mission: Number(mission), ...v }; })
      .filter((r) => ids.includes(r.user_id));
    return new Response(JSON.stringify(rows));
  }
  if (u.startsWith('https://sb.test/rest/v1/blockcamp_mission_emails') && method === 'POST') {
    const row = JSON.parse(opts.body);
    const k = `${row.user_id}/${row.term}/${row.mission}`;
    if (claims.has(k)) return new Response('[]', { status: 201 });
    claims.set(k, { claimed_at: row.claimed_at, sent_at: null });
    return new Response(JSON.stringify([row]), { status: 201 });
  }
  if (u.startsWith('https://sb.test/rest/v1/blockcamp_mission_emails') && method === 'PATCH') {
    const m = u.match(/user_id=eq\.([^&]+)&term=eq\.(\d+)&mission=eq\.(\d+)/);
    const k = `${m[1]}/${m[2]}/${m[3]}`;
    const row = claims.get(k);
    const body = JSON.parse(opts.body);
    const lt = (u.match(/claimed_at=lt\.([^&]+)/) || [])[1];
    const ok = row && (!u.includes('sent_at=is.null') || row.sent_at === null) && (!lt || Date.parse(row.claimed_at) < Date.parse(lt));
    if (ok) Object.assign(row, body);
    return new Response(JSON.stringify(ok ? [row] : []), { status: 200 });
  }
  throw new Error('unexpected fetch ' + method + ' ' + u);
};

const logs = [];
console.log = ((orig) => (...a) => { logs.push(a.join(' ')); })(console.log);
console.error = (...a) => logs.push(a.join(' '));
const out = [];
let pass = 0, fail = 0;
function check(ok, what) { ok ? pass++ : fail++; out.push(`${ok ? ' PASS' : ' FAIL'}  ${what}`); }

async function run(time = NOW, e = env) {
  const pending = [];
  await mod.default.scheduled({ scheduledTime: time }, e, { waitUntil: (p) => pending.push(p) });
  await Promise.all(pending);
}

// A Term 1 buyer whose Mission 4 opened 12 hours ago.
reset();
PROFILES = [profile('buyer')];
PLANS = [{ user_id: 'buyer', term: 1, starts_at: new Date(NOW - 21 * DAY - 12 * 3600000).toISOString() }];
await run();
{
  const m = mails[0];
  check(mails.length === 1 && m.to[0] === 'buyer@example.com' && m.subject === 'Mission 4 is open — Block Camp' &&
    m.from === env.MAIL_FROM && m.reply_to === 'info@forbesenglish.com' && m.auth === 'Bearer re_test',
    'Term 1 buyer, Mission 4 opened 12h ago: one email, from MAIL_FROM, replies to the site address');
  check(/Deck: Deck 4/.test(m.text) && !/Quest:/.test(m.text) && /https:\/\/forbesenglish\.com\/blockcamp-m4\.html/.test(m.text) &&
    /Missions 1 to 4 are open now\. Mission 5 opens on /.test(m.text) && /To stop these emails, reply/.test(m.text) &&
    /href="https:\/\/forbesenglish\.com\/blockcamp-m4\.html"/.test(m.html),
    'the email names the deck (Mission 4 has no quest), links to it, says when the next one opens, and how to stop');
  check(m.key === 'mission-buyer-1-4' && claims.get('buyer/1/4') && claims.get('buyer/1/4').sent_at,
    'claimed before sending, marked sent after, with an idempotency key');
  check(/^<mailto:info@forbesenglish\.com\?subject=Stop%20Block%20Camp%20emails>$/.test((m.headers || {})['List-Unsubscribe'] || ''),
    'a List-Unsubscribe header points at the reply address');
  check(/Mission 5 opens on \w+day \d+ \w+ at \d\d:\d\d UTC\./.test(m.text), 'the next opening says its time, in UTC');
  await run(NOW + 3600000);
  check(mails.length === 1, 'the next run the same day sends nothing more');
}

// Who is not mailed.
reset();
PROFILES = [profile('fresh'), profile('late'), profile('owner', { owner: true }), profile('optout', { blockcamp_emails: false }),
  profile('noemail', { email: null }), profile('exempt', { subscription_status: 'active', blockcamp_first_open: at(84) })];
PLANS = [
  { user_id: 'fresh', term: 1, starts_at: at(0.5) },    // Mission 1: opens on purchase, not mailed
  { user_id: 'late', term: 1, starts_at: at(25) },      // Mission 4 opened 4 days ago: too late
  { user_id: 'owner', term: 1, starts_at: at(7.2) },
  { user_id: 'optout', term: 1, starts_at: at(7.2) },
  { user_id: 'noemail', term: 1, starts_at: at(7.2) },
];
await run();
check(mails.length === 0, 'not mailed: Mission 1, a mission opened 4 days ago, the owner, an opt-out, no address, a subscriber exempted at go-live');

// A subscriber counts from their first Block Camp visit; Mission 12 says it is the last.
reset();
PROFILES = [profile('sub', { subscription_status: 'active', blockcamp_first_open: at(14.2) }), profile('last')];
PLANS = [{ user_id: 'last', term: 1, starts_at: at(77.5) }];
await run();
{
  const sub = mails.find((m) => m.to[0] === 'sub@example.com');
  const last = mails.find((m) => m.to[0] === 'last@example.com');
  check(sub && sub.subject.startsWith('Mission 3 ') && /Quest: Quest 3/.test(sub.text), 'subscriber 14 days in: Mission 3, deck and quest');
  check(last && last.subject.startsWith('Mission 12 ') && /last mission of Term 1/.test(last.text), 'Mission 12: says it is the last, nothing "opens next"');
}

// Bought twice, or a term plus the full plan: one email, from the earliest clock.
reset();
PROFILES = [profile('both', { subscription_status: 'active', blockcamp_first_open: at(7.3) })];
PLANS = [{ user_id: 'both', term: 1, starts_at: at(0.3) }];
await run();
check(mails.length === 1 && mails[0].subject.startsWith('Mission 2 '), 'term and subscription together: one email, by the earlier clock');

// A failed send gives the claim back and is retried next run.
reset();
PROFILES = [profile('retry')];
PLANS = [{ user_id: 'retry', term: 1, starts_at: at(7.2) }];
resendFails = 1;
await run();
check(mails.length === 0 && claims.get('retry/1/2') && claims.get('retry/1/2').sent_at === null,
  'Resend refuses: nothing sent, the claim stays unsent');
await run(NOW + 5 * 60000);
check(mails.length === 0, 'a run five minutes later leaves a fresh claim alone (another run may be sending)');
await run(NOW + 3600000);
check(mails.length === 1 && claims.get('retry/1/2').sent_at, 'the next hourly run takes the stale claim and sends it');

// Many readers: the profiles are read a hundred at a time, plans past the
// 1000-row cap are paged in, and the per-run budget defers the rest.
reset();
for (let k = 0; k < 1100; k++) {
  const id = `r${String(k).padStart(4, '0')}`;
  PROFILES.push(profile(id));
  PLANS.push({ user_id: id, term: 1, starts_at: k < 1099 ? at(32) : at(7.2) });   // only the last is due
}
await run(NOW, { ...env, EMAIL_SUBREQUEST_BUDGET: '1000' });
check(mails.length === 1 && mails[0].to[0] === 'r1099@example.com',
  '1100 readers: every one read (in pages and in chunks of 100), the one due is mailed');
reset();
for (let k = 0; k < 30; k++) { PROFILES.push(profile(`d${k}`)); PLANS.push({ user_id: `d${k}`, term: 1, starts_at: at(7.2) }); }
await run();
const first = mails.length;
await run(NOW + 3600000);
const second = mails.length - first;
check(first > 0 && first < 30 && second >= first && logs.some((l) => /"deferred":\d+/.test(l)),
  `the default budget stops a run cleanly (${first} of 30); the next hour carries on at the same pace (${second} more), the ones already mailed costing nothing`);

// Off, or blind: nothing sent, nothing claimed.
reset();
PROFILES = [profile('x')]; PLANS = [{ user_id: 'x', term: 1, starts_at: at(7.2) }];
await run(NOW, { ...env, RESEND_API_KEY: '' });
check(mails.length === 0 && calls.length === 0 && logs.some((l) => /not configured/.test(l)), 'no RESEND_API_KEY: the cron does nothing and says why');
readFail = true;
await run();
check(mails.length === 0 && claims.size === 0, 'Supabase unreadable: nothing sent, nothing claimed');
check(!logs.some((l) => /@example\.com/.test(l)), 'no reader\'s email address appears in the logs');

// The marking inbox goes through Resend too.
{
  reset();
  globalThis.fetch = ((inner) => async (url, opts = {}) => {
    const u = String(url);
    if (u.includes('/line_items')) return new Response(JSON.stringify({ data: [{ quantity: 1,
      price: { product: { name: 'Marking — two essays', metadata: { product: 'marking', marking_credits: '2' } } } }] }));
    if (u.includes('/rest/v1/user_plans') && opts.method === 'POST') return new Response(JSON.stringify([{}]), { status: 201 });
    return inner(url, opts);
  })(globalThis.fetch);
  const ev = { type: 'checkout.session.completed', created: NOW / 1000, data: { object: { id: 'cs_m', mode: 'payment',
    payment_status: 'paid', metadata: { supabase_user_id: 'u1' }, customer_details: { email: 'p@example.com' } } } };
  const payload = JSON.stringify(ev);
  const t = Math.floor(Date.now() / 1000);
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode('whsec'), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = [...new Uint8Array(await crypto.subtle.sign('HMAC', key, new TextEncoder().encode(`${t}.${payload}`)))].map((b) => b.toString(16).padStart(2, '0')).join('');
  const res = await mod.default.fetch(new Request('https://x.test/api/stripe-webhook', { method: 'POST', body: payload,
    headers: { 'stripe-signature': `t=${t},v1=${sig}` } }), { ...env, STRIPE_WEBHOOK_SECRET: 'whsec', STRIPE_SECRET_KEY: 'sk' }, { waitUntil() {} });
  const m = mails[0];
  check(res.status === 200 && m && m.to[0] === 'info@forbesenglish.com' && /2 essays/.test(m.subject) &&
    /p@example\.com/.test(m.text) && m.key === 'marking-cs_m', 'essay credits bought: the marking inbox is told, through Resend');
}

process.stdout.write(out.join('\n') + `\n\n${pass} passed, ${fail} failed\n`);
process.exit(fail ? 1 : 0);
