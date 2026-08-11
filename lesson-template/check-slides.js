/**
 * Forbes English — slide overflow checker.
 *
 *   node lesson-template/check-slides.js <lesson.html>
 *
 * Walks every slide, measures its real content height against the 720px
 * canvas, and reports any that overflow. "It looked fine" is not a check —
 * this is. Run it before shipping any lesson.
 */
const { chromium } = require('playwright');
const path = require('path');

const file = process.argv[2];
if (!file) { console.error('usage: node check-slides.js <lesson.html>'); process.exit(1); }

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(1800);

  const report = await page.evaluate(() => {
    const slides = [...document.querySelectorAll('.slide')];
    const out = [];
    slides.forEach((s, i) => {
      const wasActive = s.classList.contains('is-active');
      const anim = s.style.animation;
      s.style.animation = 'none';
      s.classList.add('is-active');

      // Measure the real content stack against the space the slide gives it.
      // A flex child with min-height:0 silently absorbs overflow, so compare
      // scrollHeight to clientHeight on every block inside the slide.
      let worst = 0, culprit = '';
      const boxes = [s, ...s.querySelectorAll('.slide-body, .cover-inner, .opts, .card')];
      boxes.forEach(b => {
        const over = b.scrollHeight - b.clientHeight;
        if (over > worst) { worst = over; culprit = b.className.split(' ')[0]; }
      });

      // Also sum the slide's direct children against the usable canvas.
      const padT = parseFloat(getComputedStyle(s).paddingTop);
      const padB = parseFloat(getComputedStyle(s).paddingBottom);
      let stack = 0;
      [...s.children].forEach(c => {
        const r = c.getBoundingClientRect();
        const ms = getComputedStyle(c);
        stack += r.height + parseFloat(ms.marginTop) + parseFloat(ms.marginBottom);
      });
      const scale = s.getBoundingClientRect().width / 1280 || 1;
      const needed = Math.round(stack / scale + padT + padB);

      out.push({
        n: i + 1,
        type: s.dataset.type,
        needed,
        over: Math.round(worst / scale),
        culprit,
        label: (s.querySelector('.slide-title, .cover-title, .q-stem')?.textContent || '').trim().slice(0, 40)
      });

      if (!wasActive) s.classList.remove('is-active');
      s.style.animation = anim;
    });
    return out;
  });

  const LIMIT = 720;
  let bad = 0;
  console.log(`\n  slide  type      height   ${'label'.padEnd(46)}`);
  console.log('  ' + '─'.repeat(74));
  for (const r of report) {
    const over = r.needed > LIMIT || r.over > 1;
    if (over) bad++;
    const flag = over ? `OVER by ${Math.max(r.needed - LIMIT, r.over)}px (${r.culprit})`.padEnd(28) : 'ok'.padEnd(28);
    console.log(`  ${String(r.n).padStart(3)}    ${(r.type || '').padEnd(9)} ${String(r.needed).padStart(5)}px  ${flag} ${r.label}`);
  }
  console.log('  ' + '─'.repeat(74));
  console.log(`  ${report.length} slides, ${bad} overflowing (canvas is ${LIMIT}px)`);
  if (errors.length) console.log('  JS errors:', errors);
  await browser.close();
  process.exit(bad ? 1 : 0);
})();
