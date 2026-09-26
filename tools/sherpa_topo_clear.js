#!/usr/bin/env node
// Measure what tools/sherpa_topo.py promises: no contour line touches a glyph,
// on any Sherpa page, at any width, and no halo shows up as a glow.
//
//   node tools/sherpa_topo_clear.js            # every sherpa-tensing-*.html but the map
//   node tools/sherpa_topo_clear.js <page.html> ...
//
// Opens each page from disk (no server) at 390, 768, 1280 and 1920 wide.
// The lines may run anywhere on the paper, so the rule does not depend on
// where the areas are:
//   1. every text run straight on the paper (no ancestor paints a background)
//      carries a text-shadow in the paper colour (the halo);
//   2. every text run wearing that halo sits on the paper, not on a card,
//      chip or button (where it would show as a glow);
//   3. SVG text needs a filled shape under it (a bar, or the diagram's own
//      paper rectangle), since a halo is not reliable on SVG text.
// Exit 1 on any failure.
const path = require('path');
const fs = require('fs');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));

const files = process.argv.slice(2).length ? process.argv.slice(2)
  : fs.readdirSync(ROOT).filter(f => /^sherpa-tensing-.*\.html$/.test(f) && f !== 'sherpa-tensing-route-map.html').sort();
const WIDTHS = [390, 768, 1280, 1920];

function measure() {
  const before = getComputedStyle(document.body, '::before');
  if (before.content === 'none' || !/url\(/.test(before.maskImage || before.webkitMaskImage || '')) return { missing: true };
  // the paper, as computed style writes it
  const probe = document.createElement('i');
  probe.style.color = getComputedStyle(document.documentElement).getPropertyValue('--paper').trim();
  document.body.appendChild(probe);
  const paper = getComputedStyle(probe).color;
  probe.remove();
  const ground = new Map();                 // element -> the first background up the tree, or null for the paper
  const groundOf = el => {
    if (!el || el === document.body || el === document.documentElement) return null;
    if (ground.has(el)) return ground.get(el);
    const s = getComputedStyle(el);
    const own = s.backgroundColor !== 'rgba(0, 0, 0, 0)' || s.backgroundImage !== 'none' ? s.backgroundColor : undefined;
    const v = own !== undefined ? own : groundOf(el.parentElement);
    ground.set(el, v);
    return v;
  };
  const out = [];
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    if (!n.textContent.trim()) continue;
    const el = n.parentElement;
    if (el.closest('script,style,noscript')) continue;
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || +cs.opacity === 0) continue;
    const rg = document.createRange();
    rg.selectNodeContents(n);
    const rc = rg.getBoundingClientRect();
    if (!rc.width || !rc.height) continue;
    const label = `${el.tagName.toLowerCase()}.${(el.getAttribute('class') || '').trim().replace(/\s+/g, '.')} "${n.textContent.trim().slice(0, 28)}"`;
    const g = groundOf(el);
    const svg = el.closest('svg');
    if (svg) {
      if (g !== null) continue;              // the svg sits on a card
      window.scrollTo(0, rc.top + scrollY - innerHeight / 2);
      const r2 = rg.getBoundingClientRect();
      const hits = document.elementsFromPoint(r2.left + r2.width / 2, r2.top + r2.height / 2);
      let shape = getComputedStyle(svg).backgroundColor !== 'rgba(0, 0, 0, 0)';
      for (const h of hits) {
        if (shape || h === svg) break;
        if (h.closest && h.closest('svg') === svg && !/^(text|tspan)$/i.test(h.tagName)) {
          const s = getComputedStyle(h);
          if (s.fill && s.fill !== 'none' && +s.fillOpacity > 0.3 && +s.opacity > 0.3) shape = true;
        }
      }
      if (!shape) out.push(`svg text on the bare paper: ${label}`);
      continue;
    }
    const halo = cs.textShadow && cs.textShadow !== 'none' && cs.textShadow.includes(paper);
    if (g === null && !halo) out.push(`no halo: ${label}`);
    if (g !== null && halo && g !== paper) out.push(`halo on ${g}, a glow: ${label}`);
  }
  return { out };
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
  console.log(bad ? `FAIL: ${bad} text run(s)`
    : `PASS: ${files.length} pages x ${WIDTHS.length} widths: every text on the paper has its halo, no halo on anything else`);
  process.exit(bad ? 1 : 0);
})();
