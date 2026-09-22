// Screenshot every slide of a deck by driving its own Next button, then tile
// them into one contact sheet. `shot2.js` does the same one slide at a time
// but pins the sandbox's Chromium path, which does not exist on Windows.
//
//   node lesson-template/build/sherpa/shots.js <deck.html> <out.png> [lang]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [file, out, lang] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + path.resolve(file));
  await p.waitForTimeout(1500);
  if (lang) {
    await p.evaluate(l => { window.setLang ? window.setLang(l) : (document.querySelector(`[data-lang="${l}"]`) || {}).click?.(); }, lang);
    await p.waitForTimeout(400);
  }
  const n = await p.evaluate(() => document.querySelectorAll('.slide[data-type]').length);
  const shots = [];
  for (let i = 0; i < n; i++) {
    if (i) { await p.click('.nav-btn[data-action="next"]'); await p.waitForTimeout(420); }
    shots.push(await p.locator('.stage').screenshot());
  }
  await b.close();
  const fs = require('fs');
  const dir = out.replace(/\.png$/, '');
  fs.mkdirSync(dir, { recursive: true });
  shots.forEach((s, i) => fs.writeFileSync(path.join(dir, `s${String(i + 1).padStart(2, '0')}.png`), s));
  console.log(`${n} slides -> ${dir}/`);
})();
