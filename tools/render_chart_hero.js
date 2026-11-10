// Render a sea chart's hero from its own clickable chart: the clean painting
// with the live label layer on it, in the first reading mode.
//
//   node tools/render_chart_hero.js sailing-the-seas-phrasal-verbs [port]
//
// Needs the site served locally (.claude/launch.json "site", port 8099) so
// the page's fonts load. Writes <art>/hero.jpg at 1536x1024. Used where the
// painted hero's lettering no longer matches the lesson (the Particle
// Ferries, rebuilt 2026-11-09): the hero and the chart then say the same.
const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const slug = process.argv[2];
  const port = process.argv[3] || '8099';
  if (!slug) { console.error('usage: node tools/render_chart_hero.js <slug> [port]'); process.exit(2); }
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1920, height: 1300 }, deviceScaleFactor: 1 });
  await p.goto(`http://localhost:${port}/${slug}.html?render=${Date.now()}`, { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const box = await p.evaluate(() => {
    const btn = document.querySelector('#name-bar button[data-mode=place]');
    if (btn) btn.click();
    const w = document.querySelector('.chart-toggle-wrap');
    w.style.cssText += ';width:1536px!important;height:1024px!important;max-width:none!important;' +
                       'position:fixed!important;left:0!important;top:0!important;z-index:2147483647!important;margin:0!important;';
    const img = w.querySelector('.chart-photo');
    img.style.cssText += ';width:1536px!important;height:1024px!important;max-width:none!important;';
    return w.getBoundingClientRect().toJSON();
  });
  if (Math.round(box.width) !== 1536 || Math.round(box.height) !== 1024) {
    console.error('chart is ' + box.width + 'x' + box.height + ', not 1536x1024'); process.exit(1);
  }
  const out = path.join(slug, 'hero.jpg');
  await p.screenshot({ path: out, type: 'jpeg', quality: 88, clip: { x: 0, y: 0, width: 1536, height: 1024 } });
  console.log('wrote', out);
  await b.close();
})();
