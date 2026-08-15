const { chromium } = require('playwright');
(async () => {
  const files = process.argv.slice(2);
  const b = await chromium.launch();
  for (const f of files) {
    const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
    await p.goto('file://' + f);
    await p.waitForTimeout(300);
    const out = '/tmp/' + f.split('/').pop().replace('.svg', '.png');
    await p.screenshot({ path: out });
    console.log(out);
    await p.close();
  }
  await b.close();
})();
