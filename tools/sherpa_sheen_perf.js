#!/usr/bin/env node
// What the sheen (tools/sherpa_sheen.py) costs, on a phone-sized page with the
// CPU slowed 4x, with and without it.
//
//   node tools/sherpa_sheen_perf.js [page.html ...]   # default: two lesson pages and the route map
//
// Two situations, measured separately because they differ:
//   AT REST (reading): nothing on the page asks for frames. The light is a
//     transform animation, so the compositor moves it and the main thread
//     should do nothing: the style recalcs and main-thread time per second
//     are measured over five seconds. Fails if the sheen adds more than two
//     recalcs a second or 5% of main-thread time.
//   BUSY: something else drives a frame every 16ms (a requestAnimationFrame
//     loop, as a page animation would). Then Blink also updates the running
//     CSS animations on each frame, which does cost a little; frame times
//     are reported for both, and the difference is printed, not failed.
// The first version of this tool measured only the busy case, which made the
// sheen look like a main-thread animation; it is not one (2026-09-26).
const path = require('path');
const http = require('http');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));
const files = process.argv.slice(2).length ? process.argv.slice(2)
  : ['sherpa-tensing-camp-one-present-continuous.html', 'sherpa-tensing-descent-ten-past-perfect-passive.html', 'sherpa-tensing-route-map.html'];
const TYPES = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png' };

function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      const u = decodeURIComponent(req.url.split('?')[0]);
      const f = path.join(ROOT, u);
      if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
      rsp.writeHead(200, { 'Content-Type': TYPES[path.extname(u)] || 'application/octet-stream' });
      rsp.end(fs.readFileSync(f));
    });
    srv.listen(0, '127.0.0.1', () => res(srv));
  });
}

async function sample(b, url, sheen) {
  const ctx = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, isMobile: true, hasTouch: true });
  const p = await ctx.newPage();
  await p.goto(url, { waitUntil: 'load' });
  if (!sheen) await p.addStyleTag({ content: '.topo-sheen{display:none!important}' });
  const cdp = await ctx.newCDPSession(p);
  await cdp.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  await cdp.send('Performance.enable');
  await p.waitForTimeout(1500);
  const metrics = async () => Object.fromEntries((await cdp.send('Performance.getMetrics')).metrics.map(m => [m.name, m.value]));
  // at rest
  const a0 = await metrics();
  await p.waitForTimeout(5000);
  const a1 = await metrics();
  const rest = { recalcs: (a1.RecalcStyleCount - a0.RecalcStyleCount) / 5, task: (a1.TaskDuration - a0.TaskDuration) / 5 };
  // busy
  const frames = await p.evaluate(() => new Promise(done => {
    const t = [];
    const step = ts => { t.push(ts); if (ts - t[0] < 5000) requestAnimationFrame(step); else done(t); };
    requestAnimationFrame(step);
  }));
  await ctx.close();
  const d = frames.slice(1).map((x, i) => x - frames[i]).sort((x, y) => x - y);
  const q = f => d[Math.min(d.length - 1, Math.floor(d.length * f))];
  return { rest, busy: { fps: d.length / 5, p50: q(0.5), p95: q(0.95) } };
}

(async () => {
  const srv = await serve();
  const base = `http://127.0.0.1:${srv.address().port}/`;
  const b = await chromium.launch();
  let bad = 0;
  for (const f of files) {
    const off = await sample(b, base + f, false);
    const on = await sample(b, base + f, true);
    const r = x => `${x.rest.recalcs.toFixed(1)} style recalcs/s, main thread ${(x.rest.task * 100).toFixed(1)}%`;
    const y = x => `${x.busy.fps.toFixed(0)} fps, p50 ${x.busy.p50.toFixed(1)}ms, p95 ${x.busy.p95.toFixed(1)}ms`;
    console.log(`${f}\n  at rest   without: ${r(off)}\n            with:    ${r(on)}` +
      `\n  busy      without: ${y(off)}\n            with:    ${y(on)}`);
    if (on.rest.recalcs > off.rest.recalcs + 2) { console.log('  FAIL: at rest, the sheen makes the page recalculate style'); bad++; }
    if (on.rest.task > off.rest.task + 0.05) { console.log('  FAIL: at rest, the sheen takes main-thread time'); bad++; }
  }
  await b.close();
  srv.close();
  console.log(bad ? `FAIL: ${bad}` : 'PASS: at rest the sheen costs the main thread nothing measurable');
  process.exit(bad ? 1 : 0);
})();
