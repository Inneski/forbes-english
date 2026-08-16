// Forbes English — paywall tests.
//
//   node deploy/test-paywall.mjs        (run from the repo root)
//
// Run this after ANY change to src/index.js. The cases that matter are the
// bypasses: Cloudflare serves /foo from foo.html, so a gate that only looks
// for '.html' is not a gate. Percent-encoding is the same trap.
//
import { readFileSync } from 'fs';
const src = readFileSync('src/index.js', 'utf8');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));

const PRO = ['forbes-c1-negotiation.html', 'koolhas & Lamb.html', 'Race Day - The Falcon Racing Story (B1 F1 RPG).html'];
const env = {
  SITE_URL: 'https://x.test',
  SUPABASE_URL: 'https://sb.test',
  SUPABASE_ANON_KEY: 'anon',
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
  if (u.includes('/rest/v1/lessons')) return new Response(JSON.stringify(PRO.map(f => ({file:f}))), {status:200});
  if (u.includes('/rest/v1/profiles')) {
    const auth = (opts?.headers?.Authorization) || '';
    if (auth === `Bearer ${activeToken}`) return new Response(JSON.stringify([{subscription_status:'active'}]), {status:200});
    return new Response('{"message":"JWT expired"}', {status:401});
  }
  throw new Error('unexpected fetch ' + u);
};
const store = new Map();
globalThis.caches = { default: {
  async match(k){ const v = store.get(k.url); return v ? new Response(v) : undefined; },
  async put(k,v){ store.set(k.url, await v.text()); },
}};
const ctx = { waitUntil: (p) => p };

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
  ['/snack-attack-a1.html',       null, 'lesson', 'free lesson, no session'],
  ['/library.html',               null, 'lesson', 'library is never gated'],
  ['/',                           null, 'lesson', 'root'],
  ['/Ukraine/rebuild-hero.jpg',   null, 'lesson', 'image in a folder'],
  ['/sb-client.js',               null, 'lesson', 'script'],
];

let pass = 0, fail = 0;
for (const [path, cookie, want, why] of cases) {
  const res = await get(path, cookie);
  const body = await res.clone().text();
  const kind = body.includes('GATE PAGE') || body.includes('Subscribers only') ? 'gate' : 'lesson';
  // A gate must answer 200 or it can never be indexed; see locked() in src.
  const ok = kind === want && res.status === 200;
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  ${kind.padEnd(6)} ${String(res.status).padEnd(4)} (want ${want})  ${path.slice(0,46).padEnd(48)} ${why}`);
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

console.log(`\n  ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
