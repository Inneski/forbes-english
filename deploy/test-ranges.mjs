// Forbes English — byte-range tests for the Worker's media path.
//
//   node deploy/test-ranges.mjs        (run from the repo root)
//
// The asset binding ignores Range, and Safari will not play a <video> that
// cannot be fetched by range. withRanges() in src/index.js cuts ranges for
// audio/video only; these cases pin that, and pin that nothing else changed.
import { readFileSync } from 'fs';
const src = readFileSync('src/index.js', 'utf8');
const mod = await import('data:text/javascript;base64,' + Buffer.from(src).toString('base64'));
const MP4 = readFileSync('BlockCamp/hub-flythrough.mp4');
const env = { SITE_URL: 'https://x.test', ASSETS: { fetch: async (req) => {
  const p = new URL(req.url).pathname;
  if (p.endsWith('.mp4')) return new Response(req.method === 'HEAD' ? null : MP4, { status: 200, headers: { 'Content-Type': 'video/mp4', 'ETag': '"abc"', 'Content-Length': String(MP4.length) } });
  if (p.endsWith('.jpg')) return new Response('JPEGBYTES', { status: 200, headers: { 'Content-Type': 'image/jpeg' } });
  if (p.endsWith('.gone.mp4')) return new Response('nf', { status: 404 });
  return new Response('<html>', { status: 200, headers: { 'Content-Type': 'text/html' } });
} } };
globalThis.caches = { default: { match: async () => undefined, put: async () => {} } };
globalThis.fetch = async () => new Response('[]', { status: 200 });
const go = (path, range, method = 'GET') => mod.default.fetch(new Request('https://x.test' + path, { method, headers: range ? { Range: range } : {} }), env, { waitUntil() {} });
const N = MP4.length; let fail = 0;
const check = async (label, path, range, want, method) => {
  const r = await go(path, range, method);
  const body = method === 'HEAD' ? Buffer.alloc(0) : Buffer.from(await r.arrayBuffer());
  const got = { status: r.status, cr: r.headers.get('Content-Range'), ar: r.headers.get('Accept-Ranges'), len: body.length, etag: r.headers.get('ETag') };
  let ok = got.status === want.status && (want.cr === undefined || got.cr === want.cr) && (want.len === undefined || got.len === want.len) && (want.ar === undefined || got.ar === want.ar);
  if (ok && want.slice) ok = body.equals(MP4.subarray(want.slice[0], want.slice[1] + 1));
  if (!ok) fail++;
  console.log(ok ? 'PASS' : 'FAIL', label.padEnd(34), JSON.stringify(got));
};
await check('safari probe bytes=0-1', '/BlockCamp/hub-flythrough.mp4', 'bytes=0-1', { status: 206, cr: `bytes 0-1/${N}`, len: 2, ar: 'bytes', slice: [0, 1] });
await check('open-ended bytes=1000-', '/BlockCamp/hub-flythrough.mp4', 'bytes=1000-', { status: 206, cr: `bytes 1000-${N - 1}/${N}`, len: N - 1000, slice: [1000, N - 1] });
await check('middle bytes=500-999', '/BlockCamp/hub-flythrough.mp4', 'bytes=500-999', { status: 206, len: 500, slice: [500, 999] });
await check('suffix bytes=-100', '/BlockCamp/hub-flythrough.mp4', 'bytes=-100', { status: 206, cr: `bytes ${N - 100}-${N - 1}/${N}`, slice: [N - 100, N - 1] });
await check('end past size clamps', '/BlockCamp/hub-flythrough.mp4', `bytes=${N - 10}-${N + 999}`, { status: 206, len: 10, slice: [N - 10, N - 1] });
await check('start past size 416', '/BlockCamp/hub-flythrough.mp4', `bytes=${N}-`, { status: 416, cr: `bytes */${N}` });
await check('bytes=-0 416', '/BlockCamp/hub-flythrough.mp4', 'bytes=-0', { status: 416 });
await check('multi-range -> whole file', '/BlockCamp/hub-flythrough.mp4', 'bytes=0-1,5-6', { status: 200, len: N, ar: 'bytes' });
await check('no range -> whole + Accept-Ranges', '/BlockCamp/hub-flythrough.mp4', null, { status: 200, len: N, ar: 'bytes' });
await check('HEAD with range -> 200', '/BlockCamp/hub-flythrough.mp4', 'bytes=0-1', { status: 200, ar: 'bytes' }, 'HEAD');
await check('image untouched by range', '/BlockCamp/hub-hero.jpg', 'bytes=0-1', { status: 200, len: 9, ar: null });
await check('page untouched', '/block-camp.html', 'bytes=0-1', { status: 200, ar: null });
console.log(fail ? `${fail} FAILED` : 'all range cases pass');
process.exit(fail ? 1 : 0);
