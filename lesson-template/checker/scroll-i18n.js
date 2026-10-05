// SCROLLING-PAGE I18N SMOKE TEST — for the three IELTS pages that are not
// decks (Bar Chart, Maps & Data, Writing Studio), which check-lesson.js
// cannot run against.
//
//   node lesson-template/checker/scroll-i18n.js <page.html> [lang ...]
//
// For each language (default: every language the menu offers) it switches
// through #langSelect as a learner would, then reads the whole page and
// reports: text that says "undefined" or "[object", a data-i18n node whose
// key is not in UI_I18N.en, a results/feedback message that is still the
// English string, and JS errors. Exit code 1 if anything is wrong.
const { chromium } = require('playwright');
const path = require('path');

const file = process.argv[2];
const want = process.argv.slice(3);

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 900 } });
  const errors = [];
  page.on('pageerror', e => errors.push(String(e)));
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(400);
  const menu = await page.evaluate(() => {
    const sel = document.getElementById('langSelect');
    return sel ? [...sel.options].map(o => o.value) : [];
  });
  const langs = want.length ? want : menu;
  let bad = 0;
  console.log(`${path.basename(file)}: menu offers ${menu.join(' ') || '(none)'}`);
  for (const lang of langs) {
    const r = await page.evaluate(async (lang) => {
      const sel = document.getElementById('langSelect');
      if (!sel || ![...sel.options].some(o => o.value === lang))
        return { err: `"${lang}" is not in the menu` };
      sel.value = lang;
      sel.dispatchEvent(new Event('change'));
      await new Promise(r => setTimeout(r, 150));
      const out = { lang, htmlLang: document.documentElement.lang, dir: document.documentElement.dir, problems: [] };
      const body = document.body.innerText;
      if (/\bundefined\b/.test(body)) out.problems.push('"undefined" is on the page');
      if (/\[object /.test(body)) out.problems.push('"[object" is on the page');
      document.querySelectorAll('[data-i18n]').forEach(el => {
        if (!(el.dataset.i18n in UI_I18N.en)) out.problems.push(`data-i18n="${el.dataset.i18n}" has no English key`);
      });
      if (lang !== 'en') {
        // Every data-i18n node should now differ from its English unless the
        // translation legitimately equals it (chips, English under test).
        let same = 0, total = 0;
        document.querySelectorAll('[data-i18n]').forEach(el => {
          const en = UI_I18N.en[el.dataset.i18n], tr = UI_I18N[lang] && UI_I18N[lang][el.dataset.i18n];
          if (typeof en !== 'string') return;
          total++;
          if (tr === en && en.length > 24 && / /.test(en)) same++;
        });
        out.sameAsEnglish = `${same}/${total}`;
      }
      out.sample = [...document.querySelectorAll('h1, h2, .eyebrow, .btn-primary, button.btn')]
        .slice(0, 5).map(e => e.textContent.trim().slice(0, 60));
      return out;
    }, lang);
    if (r.err) { console.log(`  ${lang}: ERROR ${r.err}`); bad++; continue; }
    const flag = r.problems.length ? 'FAIL' : 'ok  ';
    if (r.problems.length) bad++;
    console.log(`  ${flag} ${lang} (lang=${r.htmlLang} dir=${r.dir}${r.sameAsEnglish ? ' sameAsEnglish=' + r.sameAsEnglish : ''})`);
    r.problems.forEach(p => console.log('       - ' + p));
    console.log('       ' + r.sample.join(' | '));
  }
  if (errors.length) { bad++; console.log('  JS errors:'); errors.forEach(e => console.log('   - ' + e)); }
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
