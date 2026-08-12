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
  ASSETS: { fetch: (req) => new Response('LESSON BODY', { status: 200, headers: {'Content-Type':'text/html'} }) },
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

const cases = [
  // [path, cookie, expected status, why]
  ['/forbes-c1-negotiation.html', null, 402, 'pro lesson, no session'],
  ['/forbes-c1-negotiation',      null, 402, 'pro lesson WITHOUT .html — the obvious bypass'],
  ['/forbes-c1-negotiation.html', 'fe_at=good-token', 200, 'pro lesson, subscriber'],
  ['/forbes-c1-negotiation.html', 'fe_at=expired',    402, 'pro lesson, expired token'],
  ['/forbes-c1-negotiation.html', 'other=1; fe_at=good-token; z=2', 200, 'cookie among others'],
  ['/koolhas%20%26%20Lamb.html',  null, 402, 'percent-encoded space and ampersand'],
  ['/koolhas%20%26%20Lamb',       null, 402, 'percent-encoded, no extension'],
  ['/Race%20Day%20-%20The%20Falcon%20Racing%20Story%20(B1%20F1%20RPG)', null, 402, 'parens and spaces, no extension'],
  ['/snack-attack-a1.html',       null, 200, 'free lesson, no session'],
  ['/library.html',               null, 200, 'library is never gated'],
  ['/',                           null, 200, 'root'],
  ['/Ukraine/rebuild-hero.jpg',   null, 200, 'image in a folder'],
  ['/sb-client.js',               null, 200, 'script'],
];

let pass = 0, fail = 0;
for (const [path, cookie, want, why] of cases) {
  const res = await get(path, cookie);
  const ok = res.status === want;
  ok ? pass++ : fail++;
  console.log(`${ok ? ' PASS' : ' FAIL'}  ${String(res.status).padEnd(4)} (want ${want})  ${path.slice(0,52).padEnd(54)} ${why}`);
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
const open_ = down.status === 200;
open_ ? pass++ : fail++;
console.log(`${open_ ? ' PASS' : ' FAIL'}  fails open when Supabase is unreachable (${down.status})`);
globalThis.fetch = realFetch;

console.log(`\n  ${pass} passed, ${fail} failed`);
process.exit(fail ? 1 : 0);
