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
 * Both depend on the gloss language: a translated panel is 8 percentage points
 * wider and taller, so English alone proves nothing. This checks the worst of
 * whatever languages the page ships.
 *
 *   NODE_PATH=$(npm root -g) node lesson-template/check-rpg-panels.js <slug>...
 *   NODE_PATH=$(npm root -g) node lesson-template/check-rpg-panels.js --all
 *
 * Exit 0 = clean, 1 = findings. Some occlusion is deliberate and is listed in
 * ALLOW below with the reason — a cover panel is open from the first frame and
 * has no object to reveal, so a centred cover is a design choice, not a defect.
 */
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const REPO = path.resolve(__dirname, '..');
const CAMP = path.join(REPO, 'block-camp');

// scene -> why its panel is allowed to sit on its object
const ALLOW = {
  'frankenstein-green-prometheus-rpg': {
    cover: 'Innes asked for centred cover copy, 2026-09-09; a cover opens with the panel up',
    p1_end_alive: 'an ending opens with the panel up too — setOpen(kind==="intro"||kind==="ending"), '
                + 'so like a cover it has no object left to reveal',
  },
  'frankenstein-consequences-rpg': {
    end_warning: 'an ending opens with the panel up; nothing to reveal',
  },
};

const COVER_LIMIT = 20;   // % of the object the panel may hide
const SCROLL_LIMIT = 120; // px of overflow before the options risk the fold

async function check(page, slug) {
  const file = path.join(CAMP, slug + '.html');
  if (!fs.existsSync(file)) throw new Error('no such page: ' + file);
  await page.goto('file:///' + file.replace(/\\/g, '/'));
  await page.waitForTimeout(400);
  const langs = await page.evaluate('G.langs');
  const ids = Object.keys(await page.evaluate('G.scenes'));
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
    rows.push({ id, ...worst, allowed: allow[id] });
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
    const waived = rows.filter(r => r.cover > COVER_LIMIT && r.allowed);
    console.log(`\n${slug}  (${rows.length} scenes)`);
    if (!hidden.length && !scroll.length) console.log('  PASS  no panel hides its object; nothing overflows');
    for (const r of hidden)
      console.log(`  HIDDEN    ${r.id.padEnd(24)} panel covers ${r.cover}% of the object (${r.lang})`);
    for (const r of scroll)
      console.log(`  OVERFLOW  ${r.id.padEnd(24)} +${r.scroll}px past the panel (${r.lang})`);
    for (const r of waived)
      console.log(`  allowed   ${r.id.padEnd(24)} ${r.cover}% — ${r.allowed}`);
    bad += hidden.length + scroll.length;
  }
  await browser.close();
  console.log(bad ? `\n${bad} finding(s)` : '\nall pages clean');
  process.exit(bad ? 1 : 0);
})();
