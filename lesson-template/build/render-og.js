const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  const file = 'file://' + path.resolve(__dirname, 'og-image.html').replace(/\\/g, '/');
  await p.goto(file);
  await p.waitForTimeout(200);
  await p.screenshot({ path: path.resolve(__dirname, '../../og-forbes-english.png') });
  await b.close();
  console.log('done');
})();
