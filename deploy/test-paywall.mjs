// Forbes English — paywall tests.
//
//   node deploy/test-paywall.mjs        (run from the repo root)
//
// Run this after ANY change to src/index.js, and deploy/test-ranges.mjs
// beside it (the media byte ranges). The cases that matter here are the
// bypasses: Cloudflare serves /foo from foo.html, so a gate that only looks
// for '.html' is not a gate. Percent-encoding is the same trap.
//
import { readFileSync } from 'fs';
// cloudflare:email exists only in the Workers runtime; a stand-in class
// lets Node load the module (deploy/test-webhook.mjs checks the mail).
const src = readFileSync('src/index.js', 'utf8').replace(
  /^import \{ EmailMessage \} from "cloudflare:email";$/m,
  'class EmailMessage { constructor(f, t, r) { this.from = f; this.to = t; this.raw = r; } }');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));

const PRO = ['forbes-c1-negotiation.html', 'koolhas & Lamb.html', 'Race Day - The Falcon Racing Story (B1 F1 RPG).html', 'block-camp/last-train-home-rpg.html'];
// Per-track pricing: lessons carry a track, and the one-off plans in
// user_plans open their own track (2026-10-04: no longer Sherpa as well).
// Block Camp lessons also carry a term and a mission (the weekly drip,
// pricing go-live 2026-10-04): mission M opens M-1 whole weeks after the
// clock starts. Mission 1 is free.
const TRACK = {
  'block-camp/last-train-home-rpg.html': ['blockcamp', 1, 11],
  'blockcamp-demo.html':                 ['blockcamp', 1, 2],
  'blockcamp-m3.html':                   ['blockcamp', 1, 3],
  'blockcamp-term2.html':                ['blockcamp', 2, null],
  'blockcamp-term2-m1.html':             ['blockcamp', 2, 1],
  'blockcamp-t1-unnumbered.html':        ['blockcamp', 1, null],
  'block-camp/special-rpg.html':         ['blockcamp', null, null],
  'forbes-english-ielts-demo.html':      ['ielts'],
  'sherpa-tensing-demo.html':            ['sherpa'],
};
PRO.push('blockcamp-demo.html', 'blockcamp-m3.html', 'blockcamp-term2.html', 'blockcamp-term2-m1.html',
  'blockcamp-t1-unnumbered.html', 'block-camp/special-rpg.html',
  'forbes-english-ielts-demo.html', 'sherpa-tensing-demo.html');
const FREE_BC = { 'blockcamp-m1.html': ['blockcamp', 1, 1] };
const DAY = 86400000;
const ago = (days) => new Date(Date.now() - days * DAY).toISOString();
const PAST = ago(1);
const FUTURE = new Date(Date.now() + DAY).toISOString();
// token -> [profile row, user_plans rows]. 'good-token' is the full plan.
const USERS = {
  // A Term 1 buyer 8 days in: Missions 1-2 open, 3 opens on day 14.
  'bc-token':      [{id: 'u-bc', subscription_status: null}, [{product: 'blockcamp', status: 'active', ends_at: null, term: 1, starts_at: ago(8)}]],
  // A Term 1 buyer 80 days in: everything in Term 1 open (Mission 11 needs 70).
  'bc-old':        [{id: 'u-bco', subscription_status: null}, [{product: 'blockcamp', status: 'active', ends_at: null, term: 1, starts_at: ago(80)}]],
  // A subscriber who has never opened Block Camp: the clock starts now.
  'sub-new':       [{id: 'u-new', subscription_status: 'active', blockcamp_first_open: null}, []],
  // A subscriber who started Block Camp 9 days ago and also bought Term 1
  // today: either way in is enough.
  'sub-and-term':  [{id: 'u-st', subscription_status: 'active', blockcamp_first_open: ago(9)},
                    [{product: 'blockcamp', status: 'active', ends_at: null, term: 1, starts_at: ago(0)}]],
  'ielts-token':   [{subscription_status: null}, [{product: 'ielts', status: 'active', ends_at: FUTURE}]],
  'ielts-expired': [{subscription_status: null}, [{product: 'ielts', status: 'active', ends_at: PAST}]],
  'bc-canceled':   [{subscription_status: null}, [{product: 'blockcamp', status: 'canceled', ends_at: null, term: 1, starts_at: ago(80)}]],
  'bc-refunded':   [{subscription_status: null}, [{product: 'blockcamp', status: 'refunded', ends_at: null, term: 1, starts_at: ago(80)}]],
  'owner-token':   [{subscription_status: 'canceled', owner: true}, []],
};
const env = {
  SITE_URL: 'https://x.test',
  SUPABASE_URL: 'https://sb.test',
  SUPABASE_ANON_KEY: 'anon',
  SUPABASE_SERVICE_ROLE_KEY: 'service',
  // Distinct bodies per asset. Since the gate began answering 200 (so that a
  // gated lesson can be indexed at all), the status alone no longer tells a
  // gate from a lesson — the body has to, or these tests pass vacuously.
  ASSETS: { fetch: (req) => {
    const p = decodeURIComponent(new URL(req.url).pathname);
    if (p === '/locked.html') return new Response(
      '<html><head><title>x</title><!-- LESSON:head --></head><body>' +
      '<!-- LESSON:intro -->GATE PAGE<!-- /LESSON:intro --></body></html>',
      { status: 200, headers: {'Content-Type':'text/html'} });
    if (p === '/lesson-meta.json') return new Response(JSON.stringify({
      'forbes-c1-negotiation.html': { title: 'Negotiation & Persuasion', level: 'C1',
        description: 'Register, nuance and precision under pressure.', access: 'pro' },
    }), { status: 200, headers: {'Content-Type':'application/json'} });
    return new Response('LESSON BODY', { status: 200, headers: {'Content-Type':'text/html'} });
  } },
};
let activeToken = 'good-token';
globalThis.fetch = async (url, opts) => {
  const u = String(url);
  const auth = (opts?.headers?.Authorization) || '';
  const user = USERS[auth.replace('Bearer ', '')];
  if (u.includes('/rest/v1/lessons')) {
    const row = (f, access, [track, term, mission] = []) => ({ file: f, track: track || 'general', access, term: term ?? null, mission: mission ?? null });
    return new Response(JSON.stringify([
      ...PRO.map((f) => row(f, 'pro', TRACK[f])),
      ...Object.entries(FREE_BC).map(([f, t]) => row(f, 'free', t)),
    ]), {status:200});
  }
  if (u.includes('/rest/v1/profiles') && opts?.method === 'PATCH') {
    patched.push({ url: u, body: JSON.parse(opts.body), auth: opts.headers?.Authorization });
    return new Response(null, {status:204});
  }
  // The full-plan user's user_plans read is left to throw (below): a failed
  // plans read must never cost a full subscriber their access.
  if (u.includes('/rest/v1/user_plans') && user) return new Response(JSON.stringify(user[1]), {status:200});
  if (u.includes('/rest/v1/profiles')) {
    if (user) return new Response(JSON.stringify([user[0]]), {status:200});
    if (auth === `Bearer ${activeToken}`) return new Response(JSON.stringify([{id: 'u-good', subscription_status:'active', blockcamp_first_open: ago(100)}]), {status:200});
    return new Response('{"message":"JWT expired"}', {status:401});
  }
  throw new Error('unexpected fetch ' + u);
};
const patched = [];
const store = new Map();
globalThis.caches = { default: {
  async match(k){ const v = store.get(k.url); return v ? new Response(v) : undefined; },
  async put(k,v){ store.set(k.url, await v.text()); },
}};
const pending = [];
const ctx = { waitUntil: (p) => { pending.push(p); } };
const settle = async () => { while (pending.length) await pending.shift(); };

async function get(path, cookie) {
  const headers = cookie ? { Cookie: cookie } : {};
  const req = new Request('https://x.test' + path, { headers });
  return mod.default.fetch(req, env, ctx);
}

// 'gate'   = the subscribe page went out, and the lesson did not
// 'lesson'  = the real file went out
const cases = [
  // [path, cookie, expected kind, why]
  ['/forbes-c1-negotiation.html', null, 'gate', 'pro lesson, no session'],
  ['/forbes-c1-negotiation',      null, 'gate', 'pro lesson WITHOUT .html — the obvious bypass'],
  ['/forbes-c1-negotiation.html', 'fe_at=good-token', 'lesson', 'pro lesson, subscriber'],
  ['/forbes-c1-negotiation.html', 'fe_at=expired',    'gate', 'pro lesson, expired token'],
  ['/forbes-c1-negotiation.html', 'other=1; fe_at=good-token; z=2', 'lesson', 'cookie among others'],
  ['/koolhas%20%26%20Lamb.html',  null, 'gate', 'percent-encoded space and ampersand'],
  ['/koolhas%20%26%20Lamb',       null, 'gate', 'percent-encoded, no extension'],
  ['/Race%20Day%20-%20The%20Falcon%20Racing%20Story%20(B1%20F1%20RPG)', null, 'gate', 'parens and spaces, no extension'],
  // The RPGs live one directory down. Until 2026-09-08 lessonFileFor()
  // returned null for any path with a slash, so every Pro RPG was served
  // ungated while wearing a Pro badge.
  ['/block-camp/last-train-home-rpg.html', null, 'gate', 'pro RPG in block-camp/, no session'],
  ['/block-camp/last-train-home-rpg',      null, 'gate', 'pro RPG in block-camp/, no extension'],
  ['/block-camp/last-train-home-rpg.html', 'fe_at=good-token', 'lesson', 'pro RPG, subscriber'],
  ['/block-camp/last-train-home-rpg/01_cover.webp', null, 'lesson', 'picture inside an RPG folder'],
  ['/snack-attack-a1.html',       null, 'lesson', 'free lesson, no session'],
  ['/library.html',               null, 'lesson', 'library is never gated'],
  ['/',                           null, 'lesson', 'root'],
  ['/Ukraine/rebuild-hero.jpg',   null, 'lesson', 'image in a folder'],
  ['/sb-client.js',               null, 'lesson', 'script'],
  // Tracks. Full covers all, Sherpa included; since the pricing go-live
  // (2026-10-04) each one-off plan opens its own track and nothing else.
  ['/blockcamp-demo.html',            'fe_at=good-token',    'lesson', 'full plan opens Block Camp (clock 100 days old)'],
  ['/forbes-english-ielts-demo.html', 'fe_at=good-token',    'lesson', 'full plan opens IELTS'],
  // The weekly drip. 'notyet' = the "Mission N opens on ..." page.
  ['/blockcamp-demo.html',            'fe_at=bc-token',      'lesson', 'Term 1, day 8: Mission 2 open'],
  ['/blockcamp-m3.html',              'fe_at=bc-token',      'notyet', 'Term 1, day 8: Mission 3 not yet (opens day 14)'],
  ['/block-camp/last-train-home-rpg', 'fe_at=bc-token',      'notyet', 'Term 1, day 8: Mission 11 RPG not yet'],
  ['/block-camp/last-train-home-rpg', 'fe_at=bc-old',        'lesson', 'Term 1, day 80: Mission 11 RPG open'],
  ['/blockcamp-term2.html',           'fe_at=bc-old',        'gate',   'Term 1 buyer does NOT get a Term 2 lesson'],
  ['/block-camp/special-rpg.html',    'fe_at=bc-old',        'lesson', 'Term 1 buyer gets the specials (no term)'],
  ['/block-camp/special-rpg.html',    'fe_at=bc-token',      'lesson', 'the specials open from day one, not by the week'],
  ['/block-camp/special-rpg.html',    'fe_at=bc-refunded',   'gate',   'a refunded Term 1 buyer does not keep the specials'],
  ['/block-camp/special-rpg.html',    'fe_at=ielts-token',   'gate',   'an IELTS buyer does not get Block Camp specials'],
  ['/blockcamp-term2-m1.html',        'fe_at=bc-old',        'gate',   'Term 1 buyer does NOT get Term 2 Mission 1, numbered or not'],
  ['/blockcamp-t1-unnumbered.html',   'fe_at=bc-old',        'gate',   'Term 1 buyer does NOT get a Term 1 lesson with no mission'],
  ['/blockcamp-m1.html',              null,                  'lesson', 'Mission 1 is free to everyone'],
  ['/blockcamp-demo.html',            'fe_at=sub-new',       'notyet', 'subscriber, first Block Camp visit: Mission 2 not yet'],
  ['/blockcamp-term2.html',           'fe_at=sub-new',       'lesson', 'subscriber: an unnumbered lesson is not dripped'],
  ['/blockcamp-demo.html',            'fe_at=sub-and-term',  'lesson', 'subscriber clock (day 9) opens Mission 2 although the term clock (day 0) does not'],
  ['/blockcamp-m3.html',              'fe_at=sub-and-term',  'notyet', 'Mission 3 at day 9: closed by both clocks'],
  ['/blockcamp-demo.html',            'fe_at=bc-refunded',   'gate',   'refunded Term 1 is closed'],
  ['/blockcamp-m3.html',              'fe_at=owner-token',   'lesson', 'owner is never dripped'],
  ['/sherpa-tensing-demo.html',       'fe_at=bc-token',      'gate',   'Block Camp plan does NOT open Sherpa (full plan only)'],
  ['/forbes-english-ielts-demo.html', 'fe_at=bc-token',      'gate',   'Block Camp plan does NOT open IELTS'],
  ['/forbes-c1-negotiation.html',     'fe_at=bc-token',      'gate',   'Block Camp plan does NOT open general'],
  ['/forbes-english-ielts-demo.html', 'fe_at=ielts-token',   'lesson', 'IELTS plan in term opens IELTS'],
  ['/sherpa-tensing-demo.html',       'fe_at=ielts-token',   'gate',   'IELTS plan does NOT open Sherpa (full plan only)'],
  ['/sherpa-tensing-demo.html',       'fe_at=good-token',    'lesson', 'full plan opens Sherpa Tensing'],
  ['/blockcamp-demo.html',            'fe_at=ielts-token',   'gate',   'IELTS plan does NOT open Block Camp'],
  ['/forbes-english-ielts-demo.html', 'fe_at=ielts-expired', 'gate',   'IELTS plan past its term is closed'],
  ['/blockcamp-demo.html',            'fe_at=bc-canceled',   'gate',   'canceled Block Camp plan is closed'],
  ['/forbes-english-ielts-demo.html', 'fe_at=owner-token',   'lesson', 'owner opens everything'],
];

let pass = 0, fail = 0;
for (const [path, cookie, want, why] of cases) {
  const res = await get(path, cookie);
  const body = await res.clone().text();
  const kind = body.includes('name="fe-gate" content="not-yet"') ? 'notyet'
    : body.includes('GATE PAGE') || body.includes('name="fe-track"') ? 'gate' : 'lesson';
  // A gate must answer 200 or it can never be indexed; see locked() in src.
  const ok = kind === want && res.status === 200;
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  ${kind.padEnd(6)} ${String(res.status).padEnd(4)} (want ${want})  ${path.slice(0,46).padEnd(48)} ${why}`);
}

// A subscriber's first Block Camp visit starts their clock: one PATCH, with
// the service key, guarded by is.null; a free Mission 1 visit counts.
{
  await settle();
  const writes = patched.filter((p) => p.url.includes('id=eq.u-new'));
  const ok = writes.length >= 1 && writes.every((p) => p.url.includes('blockcamp_first_open=is.null') &&
    p.auth === 'Bearer service' && typeof p.body.blockcamp_first_open === 'string') &&
    !patched.some((p) => /u-good|u-st|u-bc|owner/.test(p.url));
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  only a subscriber without a clock gets one, via the service key, guarded by is.null`);
  await settle(); patched.length = 0;
  const m1 = await get('/blockcamp-m1.html', 'fe_at=sub-new');
  const servedAtOnce = m1.status === 200 && (await m1.text()).includes('LESSON BODY');
  await settle();
  const free = servedAtOnce && patched.some((p) => p.url.includes('id=eq.u-new'));
  free ? pass++ : fail++;
  console.log(`${free ? ' PASS' : ' FAIL'}  opening the free Mission 1 serves it at once and starts a subscriber's clock in the background`);
  patched.length = 0;
  await get('/blockcamp-term2.html', 'fe_at=sub-new');
  await settle();
  const unnumbered = patched.some((p) => p.url.includes('id=eq.u-new'));
  unnumbered ? pass++ : fail++;
  console.log(`${unnumbered ? ' PASS' : ' FAIL'}  a Pro Block Camp lesson with no mission starts the clock too`);
}

// A refusal the Worker reached from the reader's own rows is final: the page
// says so (fe-gate=checked), so its script does not reload, and it drops
// "Already bought it? ... let you straight through". With no cookie the
// Worker could not tell, so the retry stays.
{
  const real = readFileSync('locked.html', 'utf8');
  const realEnv = { ...env, ASSETS: { fetch: (req) => {
    const p = decodeURIComponent(new URL(req.url).pathname);
    if (p === '/locked.html') return new Response(real, { status: 200 });
    return env.ASSETS.fetch(req);
  } } };
  const fetchReal = (path, cookie) => mod.default.fetch(new Request('https://x.test' + path,
    { headers: cookie ? { Cookie: cookie } : {} }), realEnv, ctx).then((r) => r.text());
  const term2 = await fetchReal('/blockcamp-term2.html', 'fe_at=bc-old');
  const anon = await fetchReal('/blockcamp-term2.html', null);
  const headOf = (h) => h.split('</head>')[0];
  const ok = headOf(term2).includes('name="fe-gate" content="checked"') && !term2.includes('Already bought it?') &&
    term2.includes('See plans') && !headOf(anon).includes('name="fe-gate"') && anon.includes('Already bought it?');
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  a final refusal is marked "checked" and drops the retry promise; an anonymous one keeps it`);

  // The page's own script, run against both pages for a signed-in Term 1
  // buyer: on the "checked" page it must not reload (it would only fetch the
  // same refusal); on the page without the flag, the same reader is reloaded,
  // which proves the harness can see a reload at all.
  const { runInNewContext } = await import('vm');
  const runGateScript = async (html) => {
    const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((m) => m[1]).find((s) => s.includes('gateMeta'));
    // Only the head's tags: the script's own comments quote these tags too.
    const head = html.split('</head>')[0];
    const metas = Object.fromEntries([...head.matchAll(/<meta name="([^"]+)" content="([^"]*)">/g)].map((m) => [m[1], m[2]]));
    let reloads = 0;
    const store = new Map();
    const query = (rows) => ({ select: () => ({ limit: () => Promise.resolve({ data: rows }), then: (f) => f({ data: rows }) }) });
    const sb = {
      auth: { getSession: async () => ({ data: { session: { access_token: 't' } } }) },
      from: (t) => query(t === 'profiles' ? [{ subscription_status: null, owner: false }]
        : [{ product: 'blockcamp', status: 'active', ends_at: null }]),
    };
    const page = {
      document: {
        querySelector: (sel) => { const n = (sel.match(/meta\[name="([^"]+)"\]/) || [])[1]; return n && n in metas ? { content: metas[n] } : null; },
        querySelectorAll: () => [],
        getElementById: () => ({ classList: { add() {}, remove() {} } }),
      },
      sessionStorage: { getItem: (k) => store.get(k) ?? null, setItem: (k, v) => store.set(k, v), removeItem: (k) => store.delete(k) },
      location: { pathname: '/blockcamp-term2.html', reload: () => { reloads++; } },
      Date, Promise, console,
    };
    page.window = { sb };
    runInNewContext(script, page);
    await new Promise((r) => setTimeout(r, 20));
    return reloads;
  };
  const checkedReloads = await runGateScript(term2);
  const anonReloads = await runGateScript(anon);
  const noLoop = checkedReloads === 0 && anonReloads === 1;
  noLoop ? pass++ : fail++;
  console.log(`${noLoop ? ' PASS' : ' FAIL'}  the gate page's script does not reload a "checked" refusal (reloads: checked ${checkedReloads}, unflagged ${anonReloads})`);
  const titled = !/subscribers/i.test(real.match(/<title>[\s\S]*?<\/title>/)[0]);
  titled ? pass++ : fail++;
  console.log(`${titled ? ' PASS' : ' FAIL'}  the gate page's own title does not say "subscribers"`);

  const ny = await fetchReal('/blockcamp-m3.html', 'fe_at=bc-token');
  const link = ny.includes('href="/blockcamp-demo.html">Mission 2 is open now</a>') && ny.includes('Back to Block Camp') &&
    !ny.includes('Already bought it?') && /UTC<\/time>/.test(ny);
  link ? pass++ : fail++;
  console.log(`${link ? ' PASS' : ' FAIL'}  not-yet page links to the mission that is open now; its no-JS date says UTC`);
}

// The not-yet page says when, in a machine-readable time the page localises.
{
  const res = await get('/blockcamp-m3.html', 'fe_at=bc-token');
  const body = await res.text();
  const m = body.match(/<time datetime="([^"]+)" data-local>/);
  const due = m ? Date.parse(m[1]) : NaN;
  const want = Date.parse(USERS['bc-token'][1][0].starts_at) + 14 * DAY;
  const ok = Math.abs(due - want) < 1000 && body.includes('Mission 3 opens on') && !body.includes('GATE PAGE') &&
    (res.headers.get('Cache-Control') || '').includes('no-store');
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  not-yet page: "Mission 3 opens on" the right date (${m && m[1]}), not cached`);
}

// The gate page must carry THIS lesson's title and description, not a generic
// one: 195 identical pages is what made four fifths of the library invisible.
{
  const res = await get('/forbes-c1-negotiation.html', null);
  const body = await res.text();
  const named = body.includes('Negotiation &amp; Persuasion') &&
                body.includes('Register, nuance and precision') &&
                body.includes('"isAccessibleForFree":false');
  named ? pass++ : fail++;
  console.log(`${named ? ' PASS' : ' FAIL'}  the gate page names the lesson it is gating, and declares itself gated`);
}

// A served pro lesson must not be cacheable by a shared cache.
const sub = await get('/forbes-c1-negotiation.html', 'fe_at=good-token');
const cc = sub.headers.get('Cache-Control') || '';
const priv = cc.includes('private') || cc.includes('no-store');
priv ? pass++ : fail++;
console.log(`${priv ? ' PASS' : ' FAIL'}  subscriber response is private (Cache-Control: ${cc})`);

// Supabase down => fail OPEN, never lock out paying users.
const realFetch = globalThis.fetch;
store.clear();
globalThis.fetch = async () => { throw new Error('network down'); };
const down = await get('/forbes-c1-negotiation.html', null);
const open_ = down.status === 200 && (await down.text()).includes('LESSON BODY');
open_ ? pass++ : fail++;
console.log(`${open_ ? ' PASS' : ' FAIL'}  fails open when Supabase is unreachable (${down.status})`);
globalThis.fetch = realFetch;

// The gate page is the one page served at somebody else's URL: locked()
// returns its HTML, as a 200, at the gated lesson's own path. So a relative
// link in it resolves against that lesson's directory. When the gate began
// covering block-camp/ RPGs on 2026-09-08, "sign in" on the gate started
// pointing at /block-camp/account.html and returning 404 -- and the gate's
// own scripts 404'd with it, so the "you may already be subscribed" retry
// silently stopped running. Resolve every URL the way a browser would, from
// the deepest path the gate can be served at.
{
  const realLocked = readFileSync('locked.html', 'utf8');
  const base = 'https://x.test/block-camp/last-train-home-rpg.html';
  const urls = [...realLocked.matchAll(/(?:href|src)="([^"#]+)"/g)].map((m) => m[1]);
  const escapes = urls.filter((u) => {
    if (/^(https?:|\/\/|#|mailto:|data:|tel:)/.test(u)) return false;
    return new URL(u, base).pathname.startsWith('/block-camp/');
  });
  const ok = urls.length > 0 && escapes.length === 0;
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  every URL on the gate page resolves to the site root, not the lesson's folder` +
    (escapes.length ? `\n        leaks: ${escapes.join(', ')}` : ''));
}

// The free Mission 1 never waits on Supabase: with the reader's profile read
// hanging, the lesson still goes out (the clock is noted in the background).
{
  const hang = globalThis.fetch;
  globalThis.fetch = (url, opts) => (String(opts?.headers?.Authorization || '').includes('hang-token')
    ? new Promise(() => {}) : hang(url, opts));
  const res = await Promise.race([get('/blockcamp-m1.html', 'fe_at=hang-token'),
    new Promise((r) => setTimeout(() => r(null), 500))]);
  const ok = res && res.status === 200 && (await res.text()).includes('LESSON BODY');
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  free Mission 1 is served even while Supabase hangs (the clock waits, the reader does not)`);
  globalThis.fetch = hang;
  pending.length = 0;
}

console.log(`\n  ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
