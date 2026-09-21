// Render docs/at-work/book-<n>.html to book-<n>.pdf at A4 with Playwright's
// Chromium. Usage: node docs/at-work/print_book.js 1
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

(async () => {
  const n = process.argv[2] || '1';
  const src = path.resolve(__dirname, `book-${n}.html`);
  const out = path.resolve(__dirname, `book-${n}.pdf`);
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file:///' + src.replace(/\\/g, '/'), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  await page.emulateMedia({ media: 'print' });
  await page.pdf({ path: out, format: 'A4', printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await browser.close();
  const kb = Math.round(fs.statSync(out).size / 1024);
  console.log(`${path.basename(out)}: ${kb} KB`);
})();
