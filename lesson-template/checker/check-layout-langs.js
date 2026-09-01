/* Run check-lesson.js's LAYOUT measurement once per finished language.
 *
 * Why this exists. check-lesson.js renders the deck in English and only in
 * English, and German runs about a third longer than English with Spanish in
 * between. On Block Camp that gap hid twelve slides that overflowed in German
 * while passing every gate in English, one of them off the canvas entirely
 * (docs/HANDOFF.md, "Composition: the checklist that actually catches
 * things"). Until now the only way to find those was to shoot every slide in
 * every language and look.
 *
 *   node lesson-template/checker/check-layout-langs.js <lesson>.html [en,de,es]
 *
 * With no language list it measures every language the deck's own switcher
 * offers — i.e. every one that is complete, which is the same set a learner
 * can reach. Exits non-zero if any slide overflows in any of them.
 *
 * THE FONT CACHE, AND WHY A RUN WITHOUT IT LIES.
 * The decks load Playfair Display, DM Sans and DM Mono from fonts.googleapis
 * .com. A cloud sandbox's Chromium cannot reach it (the egress proxy refuses
 * the tunnel), so the page renders in a fallback face — and the fallback is
 * WIDER than DM Sans. That does not merely blur the measurement, it invents
 * failures: on the first run of this deck it reported both sort slides
 * overflowing by 5px in German and Spanish, and with the real fonts loaded
 * both fit with room to spare. Point FONTCACHE at a directory holding
 * fonts.css plus the woff2 files it names and the run is honest:
 *
 *   curl -A "$CHROME_UA" "<the deck's fonts.googleapis.com href>" -o fonts.css
 *   # then fetch each fonts.gstatic.com URL it names and rewrite the href
 *   FONTCACHE=/path/to/fonts node lesson-template/checker/check-layout-langs.js deck.html
 *
 * It prints how many faces actually loaded. If that number is 0 the run
 * downgrades every overflow to a WARN and exits 0 on purpose: a measurement
 * taken in the wrong typeface must not fail a deck, and a session that
 * trimmed real German copy to satisfy one would be deleting content to
 * please a bug. A PASS under fallback metrics is still worth having — the
 * fallback is wider, so anything that fits in it fits in DM Sans.
 */
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
const FONTS = process.env.FONTCACHE;

(async () => {
  const file = process.argv[2];
  if (!file) { console.error('usage: check-layout-langs.js <lesson>.html [en,de,es]'); process.exit(2); }

  // Same launch line as check-lesson.js, so the two run the same binary; the
  // env override is for a checkout whose browser lives somewhere else.
  const browser = await chromium.launch({
    executablePath: process.env.CHROMIUM || '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
  if (FONTS) {
    await page.route('https://fonts.googleapis.com/**', r =>
      r.fulfill({ contentType: 'text/css', body: fs.readFileSync(path.join(FONTS, 'fonts.css'), 'utf8') }));
    await page.route('**/f*.woff2', r =>
      r.fulfill({ contentType: 'font/woff2',
                  body: fs.readFileSync(path.join(FONTS, path.basename(new URL(r.request().url()).pathname))) }));
  }
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(2500);

  const faces = await page.evaluate(() => document.fonts.size);
  const langs = process.argv[3]
    ? process.argv[3].split(',')
    : await page.$$eval('#langSelect option', o => o.map(x => x.value));

  console.log(`\n  ${path.basename(file)} — ${langs.join(', ')} · ${faces} font face(s) loaded`
              + (faces ? '' : '  [fallback metrics — see the header of this file]'));

  let fails = 0, warns = 0;
  for (const lang of langs) {
    const rows = await page.evaluate((lang) => {
      currentLang = lang; applyLang();
      const out = [];
      [...document.querySelectorAll('.slide')].forEach((s, i) => {
        // Measured exactly as check-lesson.js does it, so the two agree on
        // English and any difference is the language and nothing else.
        const wasActive = s.classList.contains('is-active');
        const anim = s.style.animation;
        s.style.animation = 'none';
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
          stack += c.getBoundingClientRect().height
                 + parseFloat(m.marginTop) + parseFloat(m.marginBottom);
        });
        const needed = Math.round(stack / scale + parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom));
        const over = Math.max(needed - 720, Math.round(worst / scale));
        if (!wasActive) s.classList.remove('is-active');
        s.style.animation = anim;
        if (over > 1) out.push({ n: i + 1, over, culprit, type: s.dataset.type });
      });
      return out;
    }, lang);

    if (!rows.length) console.log(`    \x1b[32mPASS\x1b[0m  ${lang.toUpperCase()} — every slide fits`);
    else {
      if (faces) fails += rows.length; else warns += rows.length;
      const tag = faces ? '\x1b[31mFAIL\x1b[0m' : '\x1b[33mWARN\x1b[0m';
      rows.forEach(r => console.log(
        `    ${tag}  ${lang.toUpperCase()} — slide ${r.n} (${r.type}) overflows by ${r.over}px (${r.culprit})`));
    }
  }
  await browser.close();
  if (fails) console.log(`\n  \x1b[31m${fails} overflow(s)\x1b[0m\n`);
  else if (warns) console.log(
    `\n  \x1b[33m${warns} overflow(s) under fallback metrics — not a failure.\x1b[0m`
    + `\n  Re-run with FONTCACHE set before changing any copy.\n`);
  else console.log('\n  all languages fit\n');
  process.exit(fails ? 1 : 0);
})();
