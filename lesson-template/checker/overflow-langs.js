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
  const langs = await page.evaluate(() => [...document.getElementById('langSelect').options].map(o => o.value));
  const report = {};
  for (const L of langs) {
    report[L] = await page.evaluate((L) => {
      const sel = document.getElementById('langSelect');
      sel.value = L; sel.dispatchEvent(new Event('change'));
      const slides = [...document.querySelectorAll('.stage section.slide')];
      const out = [];
      slides.forEach((s, i) => {
        const anim = s.style.animation; s.style.animation = 'none';
        const was = s.classList.contains('is-active');
        s.classList.add('is-active');
        let worst = 0, culprit = '';
        [s, ...s.querySelectorAll('.slide-body, .cover-inner, .opts, .card')].forEach(b => {
          const over = b.scrollHeight - b.clientHeight;
          if (over > worst) { worst = over; culprit = (b.className || '').split(' ')[0]; }
        });
        const scale = s.getBoundingClientRect().width / 1280 || 1;
        const cs = getComputedStyle(s);
        let stack = 0;
        [...s.children].forEach(c => {
          const m = getComputedStyle(c);
          stack += c.getBoundingClientRect().height + parseFloat(m.marginTop) + parseFloat(m.marginBottom);
        });
        const needed = Math.round(stack / scale + parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom));
        const over = Math.max(needed - 720, Math.round(worst / scale));
        if (over > 1) out.push({ n: i + 1, over, culprit });
        if (!was) s.classList.remove('is-active');
        s.style.animation = anim;
      });
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
