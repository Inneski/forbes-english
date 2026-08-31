// Before/after for one slide with the SHUFFLE FROZEN.
// Options and match pairs are shuffled on every load, so two screenshots of
// the same slide differ in word order and a layout change is invisible next
// to it - Innes: "cant tell difference (maybe also a mistaken file)". Seeding
// Math.random before the deck's script runs makes the words identical in both
// frames, so the only thing that can differ is the thing being judged.
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');

const SEED = () => {
  let s = 12345;
  Math.random = () => { s = (s * 1103515245 + 12345) % 2147483648; return s / 2147483648; };
};

(async () => {
  const [fileA, fileB, list, outdir, tagA, tagB] = process.argv.slice(2);
  fs.mkdirSync(outdir, { recursive: true });
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const [file, tag] of [[fileA, tagA || 'before'], [fileB, tagB || 'after']]) {
    const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
    await p.addInitScript(SEED);
    await p.goto('file://' + path.resolve(file));
    await p.waitForTimeout(700);
    for (const nRaw of list.split(',')) {
      const n = +nRaw;
      await p.evaluate((n) => {
        const s = document.querySelectorAll('.slide');
        s.forEach(x => x.classList.remove('is-active'));
        s[n-1].classList.add('is-active');
        const st = document.querySelector('.stage');
        st.classList.remove('on-cover');
        st.style.setProperty('--hero', s[n-1].dataset.bg ? `url('${s[n-1].dataset.bg}')` : '');
      }, n);
      await p.waitForTimeout(400);
      await p.locator('.stage').screenshot({
        path: path.join(outdir, `${path.basename(fileB, '.html')}-p${n}-${tag}.png`) });
    }
    await p.close();
  }
  await b.close();
})();
