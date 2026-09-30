#!/usr/bin/env node
/* Phone gate for the Block Camp decks (the layer in block-camp/camp-phone.*).

   check-lesson.js measures the 1280x720 canvas at 1400x820, where the phone
   layout is off, so it cannot see any of this. This opens a deck as an iPhone
   in portrait (390x844) and landscape (844x390), walks every slide, and FAILS:
     - anything inside the active slide that runs off its sides (the slide
       scrolls down, never across);
     - content text under 11px (the canvas drew questions at 7px on a phone);
     - a tap target (option, match/sort item, chunk, button, nav) under 40px;
     - a deck-bar control outside the screen.
   It needs a local server (fetch and video need http):
     py -m http.server 8765 --bind 127.0.0.1
     node lesson-template/checker/check-phone.mjs [deck.html ...] [--shots DIR] [--lang de]
*/
import { chromium, devices } from 'playwright';
import fs from 'fs';

const args = process.argv.slice(2);
const shots = args.includes('--shots') ? args[args.indexOf('--shots') + 1] : null;
const lang = args.includes('--lang') ? args[args.indexOf('--lang') + 1] : 'en';
const skip = new Set([shots, lang]);
let decks = args.filter(a => a.endsWith('.html') && !skip.has(a));
if (!decks.length) decks = fs.readdirSync('.').filter(f => /^blockcamp-.*\.html$/.test(f)).sort();
const BASE = process.env.BASE || 'http://127.0.0.1:8765/';

const MEASURE = `(() => {
  const s = document.querySelector('.slide.is-active');
  const out = { overflow: [], small: [], targets: [], bar: [] };
  if (!s) return out;
  const sr = s.getBoundingClientRect();
  const visible = e => { const r = e.getBoundingClientRect(); const cs = getComputedStyle(e);
    return r.width > 0 && r.height > 0 && cs.visibility !== 'hidden' && cs.display !== 'none' && +cs.opacity !== 0; };
  const name = e => (e.className && typeof e.className === 'string' ? '.' + e.className.trim().split(/\\s+/).slice(0, 2).join('.') : e.tagName.toLowerCase()) + ' "' + (e.textContent || e.value || '').trim().slice(0, 30) + '"';
  for (const e of s.querySelectorAll('*')) {
    if (!visible(e)) continue;
    const r = e.getBoundingClientRect();
    // Up: a flex body centred in a fixed height spilled OVER the title.
    if (s.scrollTop === 0 && r.top < sr.top - 1.5 && !e.closest('.slide-head')) {
      out.overflow.push('ABOVE THE SLIDE ' + name(e) + ' y ' + Math.round(r.top) + ' < ' + Math.round(sr.top));
    }
    if (r.right > sr.right + 1.5 || r.left < sr.left - 1.5) {
      if (!e.closest('.sup:not([data-lang])')) out.overflow.push(name(e) + ' x ' + Math.round(r.left) + '..' + Math.round(r.right) + ' in ' + Math.round(sr.left) + '..' + Math.round(sr.right));
    }
    const own = [...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
    if (own) { const fs = parseFloat(getComputedStyle(e).fontSize); if (fs < 11) out.small.push(name(e) + ' ' + fs + 'px'); }
  }
  for (const e of s.querySelectorAll('.opt, .match-item, .sort-item, .chunk, .btn, button')) {
    if (!visible(e)) continue;
    const r = e.getBoundingClientRect();
    if (r.height < 40 && !e.disabled) out.targets.push(name(e) + ' ' + Math.round(r.height) + 'px');
  }
  const bar = document.querySelector('.deck-bar');
  for (const e of bar.children) {
    if (!visible(e) || e.classList.contains('progress')) continue;
    const r = e.getBoundingClientRect();
    if (r.left < -1 || r.right > innerWidth + 1 || r.top < 0 || r.bottom > innerHeight + 1) out.bar.push(name(e) + ' at ' + Math.round(r.left) + '..' + Math.round(r.right));
    if ((e.matches('button, a, select')) && r.height < 40) out.targets.push('bar ' + name(e) + ' ' + Math.round(r.height) + 'px');
  }
  out.slideScrollX = s.scrollWidth - s.clientWidth;
  return out;
})()`;

const browser = await chromium.launch({ channel: 'msedge' });
let fails = 0, slidesSeen = 0;
for (const [label, dev] of [['portrait', devices['iPhone 13']], ['landscape', devices['iPhone 13 landscape']]]) {
  const ctx = await browser.newContext({ ...dev });
  for (const deck of decks) {
    const page = await ctx.newPage();
    const errs = []; page.on('pageerror', e => errs.push(e.message));
    await page.goto(BASE + deck); await page.waitForTimeout(1200);
    if (lang !== 'en') { await page.evaluate(`(() => { const s = document.getElementById('langSelect'); if (s && [...s.options].some(o => o.value === '${lang}')) { s.value = '${lang}'; s.dispatchEvent(new Event('change')); } })()`); await page.waitForTimeout(300); }
    const mode = await page.evaluate(`document.documentElement.className`);
    if (!/bc-phone/.test(mode)) { console.log(`FAIL ${deck} ${label}: phone mode is not on (${mode})`); fails++; await page.close(); continue; }
    const n = await page.evaluate('document.querySelectorAll(".slide").length');
    for (let i = 0; i < n; i++) {
      await page.evaluate(`show(${i})`); await page.waitForTimeout(450);
      const m = await page.evaluate(MEASURE);
      slidesSeen++;
      const probs = [];
      if (m.overflow.length) probs.push('overflow: ' + m.overflow.slice(0, 3).join('; '));
      if (m.slideScrollX > 1) probs.push('scrolls sideways by ' + m.slideScrollX + 'px');
      if (m.small.length) probs.push('text under 11px: ' + m.small.slice(0, 3).join('; '));
      if (m.targets.length) probs.push('small targets: ' + m.targets.slice(0, 3).join('; '));
      if (m.bar.length) probs.push('bar off screen: ' + m.bar.join('; '));
      if (probs.length) { fails++; console.log(`FAIL ${deck} ${label} slide ${i + 1}: ${probs.join(' | ')}`); }
      if (shots) {
        fs.mkdirSync(shots, { recursive: true });
        await page.screenshot({ path: `${shots}/${deck.replace('.html', '')}-${label}-${String(i + 1).padStart(2, '0')}.png` });
      }
    }
    if (errs.length) { fails++; console.log(`FAIL ${deck} ${label}: page errors ${errs.join(' | ')}`); }
    await page.close();
  }
  await ctx.close();
}
await browser.close();
console.log(`${decks.length} decks, ${slidesSeen} slide views (${lang}): ${fails ? fails + ' FAIL' : 'PASS'}`);
process.exit(fails ? 1 : 0);
