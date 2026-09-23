// ANSWERED-STATE LAYOUT — the measurement check-lesson.js does not make.
//
//   node lesson-template/checker/answered-overflow.js <deck.html> [lang ...]
//
// check-lesson's LAYOUT gate measures every slide unanswered. Once a learner
// answers, the explanation and the "Answer:" line appear, and on 2026-09-23
// that pushed 20-odd IELTS slides 3-159px past the bottom of the canvas in
// every language (Matching Headings, Summary Completion, Line Graph, Writing
// Lab 2b, the Listening decks). This answers every scored slide WRONGLY (the
// fullest state), activates it alone as LAYOUT does, and reports overflow.
// Run it with each language the deck offers, e.g.  ... deck.html en de es
// Exit code is 0 either way; read the output. Candidate for a gate.
//
// The language switch goes through the menu, as a learner's does. It first
// called applyLang(lang), but applyLang() takes no argument — it re-applies
// whatever currentLang already is — so every "de" and "es" run in the
// 2026-09-23 audit measured the English deck again and reported it as fitting.
// A language the menu does not offer, or a switch that does not take, is now
// reported as an error instead of being measured in English.
const { chromium } = require('playwright');
const path = require('path');

const file = process.argv[2];
const langs = process.argv.slice(3).length ? process.argv.slice(3) : ['en'];

(async () => {
  const browser = await chromium.launch();
  let bad = 0;
  for (const lang of langs) {
    const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
    await page.goto('file://' + path.resolve(file));
    await page.waitForTimeout(600);
    await page.evaluate(() => document.fonts.ready);
    const res = await page.evaluate(async (lang) => {
      const sel = document.getElementById('langSelect');
      if (lang !== 'en') {
        if (!sel || ![...sel.options].some(o => o.value === lang))
          return [{ n: 0, type: '-', err: `language "${lang}" is not in the menu` }];
        sel.value = lang;
        sel.dispatchEvent(new Event('change'));
        if (typeof currentLang !== 'undefined' && currentLang !== lang)
          return [{ n: 0, type: '-', err: `the switch to "${lang}" did not take` }];
      }
      const wait = () => new Promise(r => setTimeout(r, 60));
      const style = document.createElement('style');
      style.textContent = '*{transition:none!important;animation:none!important}';
      document.head.appendChild(style);
      const slides = [...document.querySelectorAll('.slide')];
      const out = [];
      for (let i = 0; i < slides.length; i++) {
        const s = slides[i], type = s.dataset.type;
        if (!['mc', 'gap', 'order', 'match', 'sort'].includes(type)) continue;
        slides.forEach((x, n) => x.classList.toggle('is-active', n === i));
        try {
          if (type === 'mc') {
            const o = s.querySelector('.opt:not([data-correct])'); if (o) o.click();
          } else if (type === 'gap') {
            s.querySelectorAll('input.gap').forEach(g => { g.value = 'zzzz'; });
            const b = s.querySelector('[data-action="check"]'); if (b) b.click();
          } else if (type === 'order') {
            [...s.querySelectorAll('.chunk')].sort((a, b) => +b.dataset.i - +a.dataset.i).forEach(c => c.click());
            const b = s.querySelector('[data-action="check-order"], [data-action="check"]'); if (b) b.click();
          } else if (type === 'match') {
            const terms = [...s.querySelectorAll('.match-item.term')];
            terms.forEach(t => {
              t.click();
              const d = [...s.querySelectorAll('.match-item.def')].find(x => x.dataset.key === t.dataset.key && !x.classList.contains('done'));
              if (d) d.click();
            });
          } else if (type === 'sort') {
            [...s.querySelectorAll('.sort-item')].forEach(it => {
              it.click();
              const bins = [...s.querySelectorAll('.sort-bin')];
              const wrong = bins.find(b => b.dataset.bin !== it.dataset.bin) || bins[0];
              if (wrong) wrong.click();
            });
            const b = s.querySelector('[data-action="check-sort"], [data-action="check"]'); if (b) b.click();
          }
        } catch (e) { out.push({ n: i + 1, type, err: e.message }); continue; }
        await wait();
        let worst = 0, culprit = '';
        [s, ...s.querySelectorAll('.slide-body, .opts, .card')].forEach(b => {
          const over = b.scrollHeight - b.clientHeight;
          if (over > worst) { worst = over; culprit = (b.className || '').split(' ')[0]; }
        });
        if (worst > 1) out.push({ n: i + 1, type, over: worst, culprit });
      }
      return out;
    }, lang);
    res.forEach(r => { bad++; console.log(`  ${lang} slide ${r.n} [${r.type}] ` + (r.err ? 'threw ' + r.err : `overflows by ${r.over}px (${r.culprit}) when answered`)); });
    await page.close();
  }
  console.log(bad ? `${path.basename(file)}: ${bad} answered-state overflow(s)` : `${path.basename(file)}: answered state fits (${langs.join(', ')})`);
  await browser.close();
})();
