// Screenshot one local HTML file at 1600x900. interim_art.py calls this
// because Node has playwright on Innes's machine and Python does not.
//   node render_hero.js <in.html> <out.png>
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const [file, out] = process.argv.slice(2);
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1600, height: 900 } });
  await p.goto('file://' + path.resolve(file));
  await p.waitForTimeout(900);
  await p.screenshot({ path: out });
  await b.close();
})();
