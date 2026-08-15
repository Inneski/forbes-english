const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const file = process.argv[2], idxs = process.argv[3].split(',').map(Number), out = process.argv[4];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1400, height: 820 } });
  await p.goto('file://' + path.resolve(file));
  await p.waitForTimeout(1200);
  let cur = 0;
  for (const i of idxs) {
    while (cur < i) { await p.click(".nav-btn[data-action=\"next\"]"); cur++; await p.waitForTimeout(250); }
    await p.waitForTimeout(500);
    await p.locator('.stage').screenshot({ path: `${out}-${i}.png` });
  }
  await b.close();
})();
