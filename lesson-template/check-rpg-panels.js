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
 * already on. This checks every language the page ships and reports the worst.
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

async function check(page, slug) {
  const file = path.join(CAMP, slug + '.html');
  if (!fs.existsSync(file)) throw new Error('no such page: ' + file);
  await page.goto('file:///' + file.replace(/\\/g, '/'));
  await page.waitForTimeout(400);
  const langs = await page.evaluate('G.langs');
  const kinds = await page.evaluate('Object.fromEntries(Object.entries(G.scenes).map(([k, v]) => [k, v.kind]))');
  const ids = Object.keys(kinds);
  const allow = ALLOW[slug] || {};
  const rows = [];
  for (const id of ids) {
    let worst = { cover: 0, scroll: 0, lang: null };
    for (const lang of langs) {
      await page.evaluate(([i, l]) => { state.lang = l; go(i); openPanel(); }, [id, lang]);
      await page.waitForTimeout(360);
      const m = await page.evaluate(() => {
        const c = document.querySelector('.content');
        const cr = c.getBoundingClientRect();
        const h = document.getElementById('hot').getBoundingClientRect();
        const ix = Math.max(0, Math.min(cr.right, h.right) - Math.max(cr.left, h.left));
        const iy = Math.max(0, Math.min(cr.bottom, h.bottom) - Math.max(cr.top, h.top));
        return { cover: Math.round(100 * (ix * iy) / (h.width * h.height)),
                 scroll: Math.max(0, c.scrollHeight - c.clientHeight) };
      });
      if (m.cover > worst.cover || m.scroll > worst.scroll)
        worst = { cover: Math.max(worst.cover, m.cover), scroll: Math.max(worst.scroll, m.scroll), lang };
    }
    rows.push({ id, ...worst, kind: kinds[id], allowed: allow[id] });
  }
  return rows;
}

(async () => {
  let slugs = process.argv.slice(2);
  if (!slugs.length || slugs[0] === '--all')
    slugs = fs.readdirSync(CAMP).filter(f => f.endsWith('.html')).map(f => f.replace(/\.html$/, ''));

  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1536, height: 864 } });
  let bad = 0;
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
    if (!hidden.length && !scroll.length) console.log('  PASS  no panel hides its object; nothing overflows');
    for (const r of hidden)
      console.log(`  HIDDEN    ${r.id.padEnd(24)} panel covers ${r.cover}% of the object (${r.lang})`);
    for (const r of scroll)
      console.log(`  OVERFLOW  ${r.id.padEnd(24)} +${r.scroll}px past the panel (${r.lang})`);
    for (const r of tight)
      console.log(`  tight     ${r.id.padEnd(24)} +${r.scroll}px past the panel (${r.lang}) — under the limit, but the copy is at the ceiling`);
    for (const r of waived)
      console.log(`  allowed   ${r.id.padEnd(24)} ${r.cover}% — ${r.allowed}`);
    bad += hidden.length + scroll.length;
  }
  await browser.close();
  console.log(bad ? `\n${bad} finding(s)` : '\nall pages clean');
  process.exit(bad ? 1 : 0);
})();
