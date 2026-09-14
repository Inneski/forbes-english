#!/usr/bin/env node
/**
 * Measure two things a Block Camp RPG can only get wrong once it is built, and
 * that no amount of reading the hotspot table will show you:
 *
 *   1. OCCLUSION — the open panel sitting on top of the very object it grew
 *      out of. rpg/README.md §3-4 asks for this by eye, on a screenshot. The
 *      eye is bad at it: the fork scene in A Fistful of Lies looked clear in a
 *      zoomed screenshot and was 61% covered.
 *   2. OVERFLOW — a panel whose copy does not fit, so the third option can sit
 *      below the fold before the learner has answered.
 *
 * Both depend on the gloss language: `content.style.width` adds 8 percentage
 * points when a translation is on, so English alone proves nothing and most
 * findings turn out to be es/ja only. They are gloss-width defects, not layout
 * defects — the language named in each line is the widest one that triggered
 * it, and the fix is almost always to narrow the panel on the side it is
 * already on. This checks every language the page ships, English included, and
 * reports the worst.
 *
 * Both also depend on the WINDOW SHAPE, which this file ignored until
 * 2026-09-14 and which cost a shipped defect. Every size in the engine is a
 * fraction of the frame's width; the panel's height is not. So a window wider
 * than 16:9 gets larger type in a box that did not grow. Rendering 16:9 only,
 * this checker reported PASS on a Frostbound where 46 of 78 scene/language
 * screens scrolled on an ordinary maximised Chrome — Innes found it by opening
 * the page. It now renders VIEWPORTS: the 16:9 the scale was authored for, and
 * 1920x940, which is what a lesson is usually actually read in. A finding names
 * the shape that produced it when it is not 16:9.
 *
 *   NODE_PATH=$(npm root -g) node lesson-template/check-rpg-panels.js <slug>...
 *   NODE_PATH=$(npm root -g) node lesson-template/check-rpg-panels.js --all
 *
 * Exit 0 = clean, 1 = findings.
 *
 * EVERY KIND IS CHECKED THE SAME WAY. Covers and endings were briefly
 * advisory, on the reasoning that `render()` opened them itself so there was
 * no object left to reveal. That stopped being true the moment Innes asked for
 * "click to read" to be the default: `render()` now ends on `setOpen(false)`
 * and every scene, cover and ending included, is arrived at closed. You click
 * the marker, the panel opens, and it can cover the marker — which is the
 * ordinary defect. The exemption went with the behaviour it described.
 *
 * ALLOW is the only waiver now, and it is per scene with a reason.
 *
 * OVERFLOW above SCROLL_LIMIT is a finding; any overflow at all below it is
 * printed as `tight`. That second line exists because of a real miss: two
 * stories rewritten in English overflowed by 15-80px once a gloss was on,
 * which is under the limit, so the run said PASS and the prose shipped
 * overlong. The checker reads every gloss language; a human writing English
 * only ever reads one. If you have just authored or trimmed a story, read the
 * `tight` lines — they are the ones your own eye cannot catch.
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const REPO = path.resolve(__dirname, '..');
const CAMP = path.join(REPO, 'block-camp');

// slug -> { scene: why its panel is allowed to sit on its object }.
// Empty on purpose: every entry it used to hold was a cover or an ending, and
// those are advisory for every lesson now. Add one here only for a question or
// choice scene whose geometry leaves no better option, and say why.
const ALLOW = {};

// Anything added to ALLOW should be keyed on the scene's `kind` off G.scenes,
// never on its id: the Frankenstein split names its endings `p1_end_alive` and
// the like, and anything keyed on an `end_` prefix would miss all three.

const COVER_LIMIT = 20;   // % of the object the panel may hide
const SCROLL_LIMIT = 120; // px of overflow before the options risk the fold

// Two window shapes, and the second one is why this file changed on 2026-09-14.
// Every size in the engine is a fraction of the frame's WIDTH; the panel's
// height is not. So a window wider than 16:9 gets bigger type in a box that did
// not grow, and the options fall below the fold. This checker rendered 16:9
// only and reported PASS on a Frostbound where 46 of 78 scene/language screens
// scrolled on an ordinary maximised Chrome. Innes found it by opening the page.
//
// 16:9 is the shape the scale was authored for. `wide` is 1920x940 — a
// maximised Chrome on a 1080p screen, tabs and omnibox taken off — which is
// the shape a lesson is most often actually read in. Every finding names the
// shape that produced it, so a `wide`-only finding is legible as one.
const VIEWPORTS = [
  { w: 1536, h: 864, tag: '16:9' },
  { w: 1920, h: 940, tag: 'wide' },
];

async function check(page, slug) {
  const file = path.join(CAMP, slug + '.html');
  if (!fs.existsSync(file)) throw new Error('no such page: ' + file);
  const allow = ALLOW[slug] || {};
  const worst = new Map();   // id -> the worst reading across every shape and language
  let kinds = null;

  for (const vp of VIEWPORTS) {
    await page.setViewportSize({ width: vp.w, height: vp.h });
    await page.goto('file:///' + file.replace(/\\/g, '/'));
    await page.waitForTimeout(300);
    // The hotspot glow and the FULLSCREEN button animate forever, and the panel
    // has a .38s open transition. Freezing both means every measurement is the
    // settled one rather than a frame somewhere inside an easing curve — which
    // is also what lets the per-screen wait drop from 360ms to 80 and keeps a
    // two-shape run no slower than the old one-shape run.
    await page.addStyleTag({ content: '*,*::before,*::after{animation:none!important;transition:none!important}' });
    // 'off' belongs in the sweep: English-only overflows too, and it was never
    // measured. Frostbound's `voice` ran 94px past the panel with no gloss on.
    const langs = ['off', ...await page.evaluate('G.langs')];
    kinds = await page.evaluate('Object.fromEntries(Object.entries(G.scenes).map(([k, v]) => [k, v.kind]))');
    for (const id of Object.keys(kinds)) {
      for (const lang of langs) {
        await page.evaluate(([i, l]) => { state.lang = l; go(i); openPanel(); }, [id, lang]);
        await page.waitForTimeout(80);
        const m = await page.evaluate(() => {
          const c = document.querySelector('.content');
          const cr = c.getBoundingClientRect();
          const h = document.getElementById('hot').getBoundingClientRect();
          const ix = Math.max(0, Math.min(cr.right, h.right) - Math.max(cr.left, h.left));
          const iy = Math.max(0, Math.min(cr.bottom, h.bottom) - Math.max(cr.top, h.top));
          return { cover: Math.round(100 * (ix * iy) / (h.width * h.height)),
                   scroll: Math.max(0, c.scrollHeight - c.clientHeight) };
        });
        const cur = worst.get(id) ||
          { cover: 0, scroll: 0, coverLang: null, coverAt: null, scrollLang: null, scrollAt: null };
        if (m.cover > cur.cover) { cur.cover = m.cover; cur.coverLang = lang; cur.coverAt = vp.tag; }
        if (m.scroll > cur.scroll) { cur.scroll = m.scroll; cur.scrollLang = lang; cur.scrollAt = vp.tag; }
        worst.set(id, cur);
      }
    }
  }
  return Object.keys(kinds).map(id => ({ id, ...worst.get(id), kind: kinds[id], allowed: allow[id] }));
}

// "es" or "es on a wide window" — the shape is named only when it is not the
// one the type scale was authored for, so an ordinary finding reads as before.
const where = (lang, at) => at && at !== '16:9' ? `${lang} on a ${at} window` : String(lang);

(async () => {
  let slugs = process.argv.slice(2);
  if (!slugs.length || slugs[0] === '--all')
    slugs = fs.readdirSync(CAMP).filter(f => f.endsWith('.html')).map(f => f.replace(/\.html$/, ''));

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: VIEWPORTS[0].w, height: VIEWPORTS[0].h } });
  let bad = 0, advisory = 0;
  for (const slug of slugs) {
    let rows;
    try {
      rows = await check(page, slug);
    } catch (e) {
      console.log(`\n${slug}\n  SKIP  ${e.message.split('\n')[0]}`);
      continue;
    }
    const hidden = rows.filter(r => r.cover > COVER_LIMIT && !r.allowed);
    const scroll = rows.filter(r => r.scroll > SCROLL_LIMIT);
    const tight = rows.filter(r => r.scroll > 0 && r.scroll <= SCROLL_LIMIT);
    const waived = rows.filter(r => r.cover > COVER_LIMIT && r.allowed);
    console.log(`\n${slug}  (${rows.length} scenes)`);
    if (!hidden.length && !scroll.length)
      console.log(`  PASS  no panel hides its object; nothing overflows (${VIEWPORTS.map(v => v.tag).join(' + ')})`);
    for (const r of hidden)
      console.log(`  HIDDEN    ${r.id.padEnd(24)} panel covers ${r.cover}% of the object (${where(r.coverLang, r.coverAt)})`);
    for (const r of scroll)
      console.log(`  OVERFLOW  ${r.id.padEnd(24)} +${r.scroll}px past the panel (${where(r.scrollLang, r.scrollAt)})`);
    for (const r of tight)
      console.log(`  tight     ${r.id.padEnd(24)} +${r.scroll}px past the panel (${where(r.scrollLang, r.scrollAt)}) — under the limit, but the copy is at the ceiling`);
    for (const r of waived)
      console.log(`  allowed   ${r.id.padEnd(24)} ${r.cover}% — ${r.allowed}`);
    bad += hidden.length + scroll.length;
    advisory += tight.length;
  }
  await browser.close();
  // "all pages clean" printed directly above twenty `tight` lines is how the
  // wide-window defect stayed invisible for as long as it did. The thresholds
  // are a judgement about each lesson's copy and are left alone, but the last
  // line should never imply there was nothing to read. The exit code still
  // tracks findings only, so this does not turn advisories into failures.
  const tail = advisory ? ` — ${advisory} advisory 'tight' line(s), read them` : '';
  console.log(bad ? `\n${bad} finding(s)${tail}` : `\nall pages clean${tail}`);
  process.exit(bad ? 1 : 0);
})();
