// Screenshot named slides. Usage: node shots.js deck.html 12,14 outdir
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [deck, list, outdir] = process.argv.slice(2);
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + path.resolve(deck));
  await p.waitForTimeout(800);
  const base = path.basename(deck, '.html');
  for (const nRaw of list.split(',')) {
    const n = +nRaw;
    await p.evaluate((n) => {
      const s = document.querySelectorAll('.slide');
      s.forEach(x => x.classList.remove('is-active'));
      s[n - 1].classList.add('is-active');
      const stage = document.querySelector('.stage');
      stage.classList.toggle('on-cover', s[n - 1].dataset.type === 'cover');
      stage.style.setProperty('--hero', s[n - 1].dataset.bg ? `url('${s[n - 1].dataset.bg}')` : '');
    }, n);
    await p.waitForTimeout(500);
    await p.locator('.stage').screenshot({ path: path.join(outdir, `${base}-p${n}.png`) });
  }
  await b.close();
})();
