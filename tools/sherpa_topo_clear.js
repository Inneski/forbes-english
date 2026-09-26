#!/usr/bin/env node
// Measure what tools/sherpa_topo.py promises: no text sits straight on the
// paper under a contour line, on any Sherpa page, at any width.
//
//   node tools/sherpa_topo_clear.js            # every sherpa-tensing-*.html but the map
//   node tools/sherpa_topo_clear.js <page.html> ...
//
// Opens each page from disk (no server) at 1100, 1280, 1600 and 1920 wide,
// and reads the two bands from the page's own CSS: body::before (top) and
// body::after (foot), their heights, and the column carve from the mask.
// A text node is "bare" when no ancestor up to <body> paints a background.
// Fixed text (the passive gate's bar) is tested where it meets each band:
// the top one scrolled to the top, the foot one scrolled to the bottom. It
// passes if it is outside both bands, inside the carved-out column, or
// carries a text-shadow (a halo).
// Exit 1 on any failure.
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));

const files = process.argv.slice(2).length ? process.argv.slice(2)
  : fs.readdirSync(ROOT).filter(f => /^sherpa-tensing-.*\.html$/.test(f) && f !== 'sherpa-tensing-route-map.html').sort();
const WIDTHS = [1100, 1280, 1600, 1920];

function measure() {
  const W = innerWidth, H = document.body.scrollHeight;
  const before = getComputedStyle(document.body, '::before');
  const after = getComputedStyle(document.body, '::after');
  if (before.content === 'none' || after.content === 'none') return { missing: true };
  const top = [0, parseFloat(before.height)];
  const foot = [H - parseFloat(after.height), H];
  // the carve: the nearest 'calc(50% - Npx)' stop in the mask is the column's
  // clear edge (computed style writes 'transparent' as rgba, so match the calc)
  const mask = before.maskImage || before.webkitMaskImage || '';
  const stops = [...mask.matchAll(/calc\(50% - (\d+(?:\.\d+)?)px\)/g)].map(x => +x[1]);
  if (!stops.length) return { nocarve: true };
  const half = Math.min(...stops);
  const clear = [W / 2 - half, W / 2 + half];
  const bareCache = new Map();
  const isBare = el => {
    if (!el || el === document.body) return true;
    if (bareCache.has(el)) return bareCache.get(el);
    const s = getComputedStyle(el);
    const v = s.backgroundColor === 'rgba(0, 0, 0, 0)' && s.backgroundImage === 'none'
      && isBare(el.parentElement);
    bareCache.set(el, v);
    return v;
  };
  const isFixed = el => {
    for (let a = el; a && a !== document.body; a = a.parentElement)
      if (getComputedStyle(a).position === 'fixed') return true;
    return false;
  };
  const out = [];
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (el.closest('script,style')) continue;
    const rg = document.createRange();
    rg.selectNodeContents(n);
    for (const rc of rg.getClientRects()) {
      if (!rc.width || !rc.height) continue;
      // fixed text rides the viewport: it meets the top band scrolled to the
      // top, and the foot band scrolled to the bottom
      const fixed = isFixed(el);
      const y0 = rc.top + (fixed ? 0 : scrollY), y1 = rc.bottom + (fixed ? 0 : scrollY);
      const low = fixed ? H - innerHeight : 0;
      const inBand = (y1 > top[0] && y0 < top[1]) || (y1 + low > foot[0] && y0 + low < foot[1]);
      const inMargin = rc.left < clear[0] || rc.right > clear[1];
      if (!inBand || !inMargin || !isBare(el)) continue;
      const ts = getComputedStyle(el).textShadow;
      if (ts && ts !== 'none') continue;
      out.push(`${el.tagName.toLowerCase()}.${el.getAttribute('class') || ''} "${n.textContent.trim().slice(0, 30)}"`
        + ` x ${Math.round(rc.left)}-${Math.round(rc.right)} y ${Math.round(y0)}`);
    }
  }
  return { out, clear: clear.map(Math.round) };
}

async function one(b, f) {
  const lines = [];
  const p = await b.newPage({ viewport: { width: WIDTHS[0], height: 900 } });
  await p.route(/^https?:/, r => r.abort());                // no fonts or analytics: geometry only
  await p.goto('file:///' + (path.isAbsolute(f) ? f : path.join(ROOT, f)).replace(/\\/g, '/'), { waitUntil: 'load' });
  await p.evaluate(() => {                                   // every hidden panel shown, so its text is measured
    document.querySelectorAll('[hidden]').forEach(e => e.removeAttribute('hidden'));
  });
  for (const w of WIDTHS) {
    await p.setViewportSize({ width: w, height: 900 });
    await p.waitForTimeout(150);
    const r = await p.evaluate(measure);
    if (r.missing) { lines.push(`FAIL ${f}: no contour block`); break; }
    if (r.nocarve) { lines.push(`FAIL ${f}: the mask has no column carve`); break; }
    for (const o of r.out) lines.push(`FAIL ${f} @${w}: ${o}`);
  }
  await p.close();
  return lines;
}

(async () => {
  const b = await chromium.launch();
  let bad = 0;
  const queue = files.slice();
  await Promise.all(Array.from({ length: 6 }, async () => {
    while (queue.length) {
      const lines = await one(b, queue.shift());
      lines.forEach(l => console.log(l));
      bad += lines.length;
    }
  }));
  await b.close();
  console.log(bad ? `FAIL: ${bad} text run(s) under a line`
    : `PASS: ${files.length} pages x ${WIDTHS.length} widths, no bare text under a line`);
  process.exit(bad ? 1 : 0);
})();
