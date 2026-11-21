// Library card / og image: a 1200x675 render of the page's own opening screen.
//   node render-card.cjs [port]      (needs the site served: .claude/launch.json "site", port 8099)
// Writes ../../../atelier-lexicon-architectural-vocabulary/hero.jpg
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const port = process.argv[2] || '8099';
  const out = path.join(__dirname, '../../../atelier-lexicon-architectural-vocabulary');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 675 }, deviceScaleFactor: 1 });
  await p.goto(`http://localhost:${port}/atelier-lexicon-architectural-vocabulary.html?lang=en&render=${Date.now()}`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  // The opening screen without the site's own chrome (language pill, library link).
  await p.addStyleTag({ content: '.fe-lang,.fe-home-row{display:none!important}' });
  await p.waitForTimeout(600);
  await p.screenshot({ path: path.join(out, 'hero.jpg'), type: 'jpeg', quality: 86 });
  await b.close();
  console.log('wrote', path.join(out, 'hero.jpg'));
})();
