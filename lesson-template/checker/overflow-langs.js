// Per-language layout check: the same measurement check-lesson.js makes for
// English, repeated with every offered language switched on. Usage:
//   NODE_PATH="$(npm root -g)" node lesson-template/checker/overflow-langs.js <deck.html>
// check-lesson.js measures English only; the always-on .sup glosses and the
// translated UI strings change every slide's height, and on 2026-09-03 this
// found es/fr/it/pt overflowing present-simple slide 2 and pt slide 7 while
// the English run passed. A clean run here is a measurement, not a guess.
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = process.argv[2];
  const pinned = '/opt/pw-browsers/chromium';
  const browser = await chromium.launch(
    require('fs').existsSync(pinned) ? { executablePath: pinned } : {});
  const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
  const errs = [];
  page.on('pageerror', e => errs.push(e.message));
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(1500);
  // Wait for the faces, not just the clock. A slide measured while the text is
  // still in a fallback wraps wider and reports about one extra line of
  // overflow that is not there. The deck itself already knows this — it hides
  // the wordmark until fonts.ready with a 1.5s failsafe — so the page was
  // ahead of its checker. (This did NOT turn out to be the cause of the
  // blockcamp-present-continuous-2 +29px phantom: fonts report "loaded" at
  // t=0 there and a fresh-page sweep at 0/100/300/800/1500/3000ms measures 0
  // every time. Correct anyway, and cheap.)
  await page.evaluate(() => document.fonts.ready);
  const langs = await page.evaluate(() => [...document.getElementById('langSelect').options].map(o => o.value));
  const report = {};
  for (const L of langs) {
    // A FRESH PAGE PER LANGUAGE. Switching language in one page and measuring
    // again can read a stale layout. Reduced to a minimal case on
    // blockcamp-present-continuous-2 slide 8: a pass in German alone measures
    // 0, and an English pass followed by a German one measures 32 — same DOM,
    // same six .sup glosses, same 1784 characters of markup, different heights
    // (.slide-body client 416 against 427). A learner opens the page in one
    // language, so that is what the checker should do.
    //
    // HONEST LIMIT: this did NOT silence that deck's +29px, which still
    // reports on a fresh page and is deterministic across five runs. So the
    // reload is correct on its own merits and the phantom has a different
    // cause that I did not find. Ruled out: fonts (status is "loaded" at t=0,
    // and a fresh-page sweep at 0/100/300/800/1500/3000ms measures 0), gloss
    // duplication (identical innerHTML), and self-pollution from walking the
    // slides. Do not trust that one number until someone explains it.
    await page.goto('file://' + path.resolve(file));
    await page.waitForTimeout(1500);
    await page.evaluate(() => document.fonts.ready);
    report[L] = await page.evaluate((L) => {
      const sel = document.getElementById('langSelect');
      sel.value = L; sel.dispatchEvent(new Event('change'));
      const slides = [...document.querySelectorAll('.stage section.slide')];
      const out = [];
      // Measure one slide at a time and no more. Adding .is-active to slide N
      // without taking it off the slide that already had it leaves TWO slides
      // displayed, and in a flex column that changes the heights you are about
      // to measure: blockcamp-present-continuous-2 de slide 8 reported +29px
      // that way and fits when measured alone. Restore the real one at the end.
      const wasActive = slides.filter(s => s.classList.contains('is-active'));
      slides.forEach(s => s.classList.remove('is-active'));
      slides.forEach((s, i) => {
        const anim = s.style.animation; s.style.animation = 'none';
        s.classList.add('is-active');
        let worst = 0, culprit = '';
        [s, ...s.querySelectorAll('.slide-body, .cover-inner, .opts, .card')].forEach(b => {
          const over = b.scrollHeight - b.clientHeight;
          if (over > worst) { worst = over; culprit = (b.className || '').split(' ')[0]; }
        });
        const scale = s.getBoundingClientRect().width / 1280 || 1;
        const cs = getComputedStyle(s);
        // Same stack measurement as check-lesson.js's LAYOUT gate, and it has
        // to stay the same: two checkers that disagree about whether a slide
        // fits are worse than one. I had deleted this outright after it
        // reported +720px on twin_peaks_prepositions_v5 and +29px on
        // blockcamp-present-continuous-2, both fiction. Deleting it was the
        // wrong repair — the Between Two Worlds session found the actual bug
        // in the same week. Summing every child assumes the slide stacks them
        // vertically, and two real layouts break that: a child out of flow
        // contributes nothing to its parent's content height, and a ROW is as
        // tall as its tallest child, not as tall as all of them added up.
        const isRow = cs.display.includes('flex')
                   && (cs.flexDirection || '').startsWith('row');
        let stack = 0;
        [...s.children].forEach(c => {
          const m = getComputedStyle(c);
          if (m.position === 'absolute' || m.position === 'fixed') return;
          const h = c.getBoundingClientRect().height
                  + parseFloat(m.marginTop) + parseFloat(m.marginBottom);
          stack = isRow ? Math.max(stack, h) : stack + h;
        });
        const needed = Math.round(stack / scale + parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom));
        const over = Math.max(needed - 720, Math.round(worst / scale));
        if (over > 1) out.push({ n: i + 1, over, culprit });
        s.classList.remove('is-active');
        s.style.animation = anim;
      });
      wasActive.forEach(s => s.classList.add('is-active'));
      return { slides: slides.length, over: out };
    }, L);
  }
  await browser.close();
  for (const L of Object.keys(report)) {
    const r = report[L];
    console.log(L.padEnd(3), r.over.length ? r.over.map(o => `slide ${o.n} +${o.over}px (${o.culprit})`).join('; ') : 'fits');
  }
  if (errs.length) console.log('JS errors:', errs);
})();
