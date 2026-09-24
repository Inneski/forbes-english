/**
 * answer-width.js — find answer boxes that are far wider than their answer.
 *
 *   node lesson-template/checker/answer-width.js <page.html> [<page.html> …] [--json]
 *
 * Innes asked for short answer boxes on 2026-09-12 ("the answer boxes dont
 * need to be so long") and the template was fixed that day: .opt became
 * width: fit-content. On 2026-09-24 he sent a screenshot of a live deck with
 * "Overview", "Introduction" and "Body Paragraph" in three bars running the
 * full width of the slide: 79 pages still carried the old width: 100% rule,
 * 26 editorial decks overrode the fix, and some thirty other pages had their
 * own CSS. A template fix does not reach a page that is never rebuilt, so the
 * defect is measured here, on the rendered page, whatever the CSS family.
 *
 * Method: every slide is forced visible (decks show one at a time), then each
 * element that looks like an answer — .opt, and buttons or [role=button]
 * inside an option group — is measured against the other answers in its
 * group (its parent's children of the same kind). A box is STRETCHED when it
 * is at least 400px wide and even the longest answer in the group needs less
 * than 60% of it. So a full-width bar holding "Overview" fails, a two-up grid
 * cell holding "has lived" fails, and bars of one width sized to the longest
 * answer pass. Long answers that genuinely fill the row are left alone.
 */
const { chromium } = require('playwright');
const path = require('path');

const args = process.argv.slice(2);
const asJson = args.includes('--json');
const files = args.filter(a => !a.startsWith('--'));
if (!files.length) {
  console.error('usage: node answer-width.js <page.html> [...] [--json]');
  process.exit(2);
}

(async () => {
  const pinned = '/opt/pw-browsers/chromium';
  const browser = await chromium.launch(
    require('fs').existsSync(pinned) ? { executablePath: pinned } : {});
  const results = [];
  for (const file of files) {
    const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
    let res;
    try {
      await page.goto('file://' + path.resolve(file), { waitUntil: 'load', timeout: 30000 });
      await page.waitForTimeout(600);
      res = await page.evaluate(() => {
        // Force every slide/section into view so hidden questions can be measured.
        const st = document.createElement('style');
        st.textContent = `.slide,section,[class*="slide"],[class*="screen"],[class*="question"],[class*="step"],[class*="panel"]
          { display:block !important; visibility:visible !important; opacity:1 !important; }
          [hidden] { display:block !important; }`;
        document.head.appendChild(st);
        const sel = [
          '.opt', '.option', '.choice', '.answer', '.answer-btn', '.ans',
          '.opts button', '.options button', '.choices button', '.answers button',
          '[class*="option"] button', '[class*="choice"] button', '[class*="answer"] button',
          'button[data-correct]', '[role="radio"]',
        ].join(',');
        const needOf = el => {
          // Width of the widest LINE of text: every text run on one line counts,
          // so "Record and <em>record</em>" is measured whole, not as its longest
          // piece. The key letter is text too; an empty badge adds its width.
          const lines = [];
          const walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
          for (let t; (t = walk.nextNode());) {
            if (!t.textContent.trim()) continue;
            const range = document.createRange(); range.selectNodeContents(t);
            for (const q of range.getClientRects()) {
              if (q.width < 1) continue;
              const mid = (q.top + q.bottom) / 2;
              const l = lines.find(l => Math.abs(l.mid - mid) < 8);
              if (l) { l.a = Math.min(l.a, q.left); l.b = Math.max(l.b, q.right); }
              else lines.push({ mid, a: q.left, b: q.right });
            }
          }
          let extra = 0;
          for (const c of el.children) if (!(c.innerText || '').trim()) extra += c.getBoundingClientRect().width;
          return Math.max(0, ...lines.map(l => l.b - l.a)) + extra;
        };
        const seen = new Set(); const groups = new Map();
        for (const el of document.querySelectorAll(sel)) {
          if (seen.has(el)) continue; seen.add(el);
          const r = el.getBoundingClientRect();
          if (r.width < 1 || r.height < 1) continue;
          const text = (el.innerText || '').trim();
          if (!text || text.length > 140) continue;
          const par = el.parentElement; if (!par) continue;
          if (!groups.has(par)) groups.set(par, []);
          groups.get(par).push(el);
        }
        const out = [];
        for (const group of groups.values()) {
          const needs = group.map(needOf);
          const most = Math.max(...needs);
          group.forEach((el, k) => {
            const w = el.getBoundingClientRect().width;
            if (w >= 400 && most < w * 0.6) {
              out.push({ text: (el.innerText || '').trim().slice(0, 50), w: Math.round(w), need: Math.round(needs[k]) });
            }
          });
        }
        return { stretched: out.length, sample: out.slice(0, 3), boxes: [...groups.values()].reduce((n, g) => n + g.length, 0) };
      });
    } catch (e) {
      res = { error: String(e).slice(0, 120) };
    }
    await page.close();
    results.push({ file, ...res });
    if (!asJson) {
      if (res.error) console.log(`ERR   ${file}: ${res.error}`);
      else if (res.stretched) console.log(`LONG  ${file}: ${res.stretched} stretched answer box(es), e.g. "${res.sample[0].text}" ${res.sample[0].w}px for ${res.sample[0].need}px of content`);
      else if (!res.boxes) console.log(`none  ${file}: no answer boxes on the page as loaded`);
      else console.log(`ok    ${file}`);
    }
  }
  await browser.close();
  if (asJson) console.log(JSON.stringify(results));
  process.exit(results.some(r => r.stretched) ? 1 : 0);
})();
