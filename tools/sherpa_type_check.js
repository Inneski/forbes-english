#!/usr/bin/env node
// Measure what tools/sherpa_type.py promises: every Sherpa page is set in
// Faktum, and the bigger type breaks nothing that was not already broken.
//
//   node tools/sherpa_type_check.js                 # all 26 pages, the hub in all ten languages
//   node tools/sherpa_type_check.js <page.html> ... # just these
//   node tools/sherpa_type_check.js --base <rev>    # compare against another revision (default HEAD)
//
// Serves the repo itself (no other server needed), and serves the same page
// at the base revision under /__base__/, so each page is measured twice, in
// the same browser, at 390, 768 and 1280 wide. Fails on:
//   - Latin text not in Faktum, or Faktum not loaded;
//   - the page scrolling sideways;
//   - text spilling out of a box (a card, button or chip whose content is
//     taller or wider than the box);
//   - SVG labels that collide (two labels overlapping, a label straddling
//     the edge of a bar, a label outside its diagram);
// but only where the base revision did not already do the same thing: those
// are listed once, as "already so", so they stay visible without failing.
const http = require('http');
const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));

const argv = process.argv.slice(2);
const bi = argv.indexOf('--base');
const BASE = bi >= 0 ? argv.splice(bi, 2)[1] : 'HEAD';
const files = argv.length ? argv : fs.readdirSync(ROOT).filter(f => /^sherpa-tensing-.*\.html$/.test(f)).sort();
const WIDTHS = [390, 768, 1280];
const LANGS = ['en', 'de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja'];
const TYPES = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg',
  '.png': 'image/png', '.js': 'text/javascript', '.css': 'text/css', '.json': 'application/json' };

// the base revision's pages, read once: a git call per request stalled every
// other load in the queue until Chromium gave up on some (ERR_ABORTED)
const BASE_PAGES = {};
for (const f of files) {
  try { BASE_PAGES[f] = execFileSync('git', ['-C', ROOT, 'show', `${BASE}:${f}`]); } catch (e) { /* new page */ }
}

function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      let u = decodeURIComponent(req.url.split('?')[0]);
      let body = null;
      if (u.startsWith('/__base__/')) {
        u = u.slice('/__base__'.length);
        body = BASE_PAGES[u.slice(1)] || null;
      }
      if (!body) {
        const f = path.join(ROOT, u);
        if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
        body = fs.readFileSync(f);
      }
      rsp.writeHead(200, { 'Content-Type': TYPES[path.extname(u)] || 'application/octet-stream' });
      rsp.end(body);
    });
    srv.listen(0, '127.0.0.1', () => res(srv));
  });
}

function measure() {
  const out = { notFaktum: [], overflowX: 0, spill: [], svg: [], faktum: null };
  const vis = el => { const s = getComputedStyle(el); return s.display !== 'none' && s.visibility !== 'hidden' && +s.opacity > 0; };
  out.faktum = document.fonts.check('400 16px Faktum') && document.fonts.check('600 16px Faktum');
  // the wordmark is a name: it must sit on one line (it broke in two on a phone once it grew)
  const brand = document.querySelector('.wordmark .brand');
  if (brand) {
    const lines = brand.getClientRects().length > 1 ? brand.getClientRects().length
      : Math.round(brand.getBoundingClientRect().height / (parseFloat(getComputedStyle(brand).fontSize) * 1.25));
    if (lines > 1) out.spill.push(`wordmark "${brand.textContent.trim()}" breaks over ${lines} lines +0x0px`);
  }
  out.overflowX = Math.max(0, document.documentElement.scrollWidth - innerWidth);
  const LATIN = /[A-Za-zÀ-ɏ]/;
  const seen = new Set();
  const tw = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  let n;
  while ((n = tw.nextNode())) {
    const t = n.textContent.trim();
    if (!t) continue;
    const el = n.parentElement;
    if (el.closest('script,style,noscript,.sr-only') || !vis(el)) continue;
    if (!LATIN.test(t)) continue;
    const fam = getComputedStyle(el).fontFamily.split(',')[0].replace(/["']/g, '').trim();
    if (fam !== 'Faktum' && !seen.has(el)) { seen.add(el); out.notFaktum.push(`${el.tagName.toLowerCase()} "${t.slice(0, 24)}" in ${fam}`); }
  }
  // boxes: an element that paints a background or border and whose content outgrows it
  for (const el of document.body.querySelectorAll('*')) {
    if (el.closest('svg,script,style') || !vis(el)) continue;
    const s = getComputedStyle(el);
    // a box paints a ground or a whole border; a lone rule (the hub's counts have
    // only a top border) is not one, and content running past it shows nothing
    const boxed = s.backgroundColor !== 'rgba(0, 0, 0, 0)' ||
      ['Top', 'Right', 'Bottom', 'Left'].every(e => parseFloat(s['border' + e + 'Width']) > 0);
    if (!boxed || !el.textContent.trim() || el.clientWidth === 0) continue;
    if (el === document.body || el === document.documentElement) continue;
    const dx = el.scrollWidth - el.clientWidth, dy = el.scrollHeight - el.clientHeight;
    const scrollable = /(auto|scroll)/.test(s.overflowX + s.overflowY);
    if (!scrollable && (dx > 1 || dy > 1)) {
      const k = `${el.tagName.toLowerCase()}.${[...el.classList].join('.')} "${el.textContent.trim().slice(0, 24)}"`;
      out.spill.push(`${k} +${dx}x${dy}px`);
    }
  }
  // SVG labels
  const area = r => Math.max(0, r.width) * Math.max(0, r.height);
  const inter = (a, b) => area({ width: Math.min(a.right, b.right) - Math.max(a.left, b.left), height: Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top) });
  for (const svg of document.querySelectorAll('svg')) {
    if (!vis(svg) || svg.closest('[aria-hidden="true"]') && svg.getBoundingClientRect().width < 40) continue;
    const sr = svg.getBoundingClientRect();
    if (sr.width < 60) continue;                         // icons
    const texts = [...svg.querySelectorAll('text')].filter(t => vis(t) && t.textContent.trim())
      .map(t => ({ t, r: t.getBoundingClientRect(), s: t.textContent.trim().slice(0, 28) })).filter(o => o.r.width > 0);
    const shapes = [...svg.querySelectorAll('rect,path,polygon,circle,ellipse')].filter(sh => {
      if (!vis(sh) || sh.closest('defs,clipPath,mask,pattern')) return false;
      const s = getComputedStyle(sh);
      if (!s.fill || s.fill === 'none' || /rgba\([^)]*,\s*0\)/.test(s.fill) || +s.fillOpacity < 0.3 || +s.opacity < 0.3) return false;
      const r = sh.getBoundingClientRect();
      return area(r) < 0.6 * area(sr) && r.width > 2 && r.height > 2;   // not the diagram's own ground
    }).map(sh => ({ sh, r: sh.getBoundingClientRect() }));
    const svgKey = (svg.getAttribute('class') || svg.id || 'svg').split(/\s+/)[0];
    // a label with SVG's halo (a paper outline behind its glyphs) may sit on a bar's edge
    const probe = document.createElement('i');
    probe.style.color = getComputedStyle(document.documentElement).getPropertyValue('--paper').trim();
    document.body.appendChild(probe);
    const paper = getComputedStyle(probe).color;
    probe.remove();
    const haloed = t => { const s = getComputedStyle(t); return s.paintOrder.startsWith('stroke') && s.stroke === paper && parseFloat(s.strokeWidth) >= 2; };
    for (const a of texts) {
      if (a.r.left < sr.left - 2 || a.r.right > sr.right + 2 || a.r.top < sr.top - 2 || a.r.bottom > sr.bottom + 2)
        out.svg.push(`${svgKey}: "${a.s}" outside its diagram`);
      for (const b of texts) {
        if (b === a || b.s <= a.s && b.s === a.s) continue;
        if (a.s < b.s && inter(a.r, b.r) > 0.12 * Math.min(area(a.r), area(b.r)))
          out.svg.push(`${svgKey}: "${a.s}" overlaps "${b.s}"`);
      }
      for (const b of shapes) {
        if (haloed(a.t)) break;
        const f = inter(a.r, b.r) / area(a.r);
        if (f > 0.12 && f < 0.88) out.svg.push(`${svgKey}: "${a.s}" straddles a ${b.sh.tagName} edge (${Math.round(f * 100)}%)`);
      }
    }
  }
  out.svg = [...new Set(out.svg)];
  out.spill = [...new Set(out.spill)];
  return out;
}

async function run(b, url, w, tries = 2) {
  const p = await b.newPage({ viewport: { width: w, height: 900 } });
  await p.route(/googletagmanager|google-analytics|supabase|plausible/, r => r.abort());
  try {
    await p.goto(url, { waitUntil: 'load', timeout: 60000 });
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(300);
    return await p.evaluate(measure);
  } catch (e) {
    if (tries > 1) return run(b, url, w, tries - 1);
    return { error: String(e.message || e).split('\n')[0] };
  } finally { await p.close(); }
}

(async () => {
  const srv = await serve();
  const port = srv.address().port;
  const b = await chromium.launch();
  const jobs = [];
  for (const f of files) {
    const langs = f === 'sherpa-tensing-route-map.html' ? LANGS : ['en'];
    for (const l of langs) for (const w of WIDTHS) jobs.push({ f, l, w });
  }
  let fails = 0;
  const already = new Set();
  const lines = [];
  const q = jobs.slice();
  await Promise.all(Array.from({ length: 6 }, async () => {
    while (q.length) {
      const { f, l, w } = q.shift();
      const qs = l === 'en' ? '' : `?lang=${l}`;
      const [now, base] = await Promise.all([
        run(b, `http://127.0.0.1:${port}/${f}${qs}`, w),
        run(b, `http://127.0.0.1:${port}/__base__/${f}${qs}`, w)]);
      const tag = `${f.replace('sherpa-tensing-', '')}${l === 'en' ? '' : ' [' + l + ']'} @${w}`;
      if (now.error || base.error) { lines.push(`FAIL ${tag}: could not load: ${now.error || base.error}`); fails++; continue; }
      if (!now.faktum) { lines.push(`FAIL ${tag}: Faktum did not load`); fails++; }
      for (const x of now.notFaktum) { lines.push(`FAIL ${tag}: not Faktum: ${x}`); fails++; }
      if (now.overflowX > 1) {
        if (base.overflowX > 1) already.add(`${tag}: page scrolls sideways (${base.overflowX}px before, ${now.overflowX}px now)`);
        else { lines.push(`FAIL ${tag}: page scrolls sideways by ${now.overflowX}px`); fails++; }
      }
      const strip = s => s.replace(/ \+-?\d+x-?\d+px$/, '');
      const baseSpill = new Set(base.spill.map(strip));
      for (const x of now.spill) {
        if (baseSpill.has(strip(x))) already.add(`${tag}: spills: ${x}`);
        else { lines.push(`FAIL ${tag}: spills its box: ${x}`); fails++; }
      }
      const baseSvg = new Set(base.svg.map(s => s.replace(/ \(\d+%\)$/, '')));
      for (const x of now.svg) {
        if (baseSvg.has(x.replace(/ \(\d+%\)$/, ''))) already.add(`${f.replace('sherpa-tensing-', '')} @${w}: ${x}`);
        else { lines.push(`FAIL ${tag}: ${x}`); fails++; }
      }
    }
  }));
  await b.close();
  srv.close();
  lines.sort().forEach(l => console.log(l));
  if (already.size) {
    console.log(`\nalready so at ${BASE} (not failing, still worth fixing):`);
    [...already].sort().forEach(l => console.log('  ' + l));
  }
  console.log(fails ? `\nFAIL: ${fails} problem(s)` : `\nPASS: ${files.length} pages (${jobs.length} renders against ${BASE}): Faktum everywhere, nothing new overflows or collides`);
  process.exit(fails ? 1 : 0);
})();
