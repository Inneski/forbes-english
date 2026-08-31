// Dump, for every slide of a Block Camp deck, where the INK actually lands
// in each of the six placements the deck can express (side x vpos).
//
// Measuring the element box was the earlier mistake: a .slide-body is a
// stretched flex column, so its rectangle says nothing about where the words
// are. Past Simple 16 has a body 61% of the frame wide holding a match grid
// 16% wide pinned to its left edge. The union of the text line rects is the
// only honest answer to "where is the text".
//
// Usage: node dump-rects.js <deck.html>
const { chromium } = require('playwright');
const path = require('path');

const COLUMN  = ['.slide-head', '.slide-body'];
const PAINTED = ['.card', '.para-block', '.exlist', '.q-stem', '.opt', '.freq',
                 '.sort-bin', '.match-item', '.gap-row', '.order-hint',
                 '.formula', '.dictum', '.step', '.mini-card'];
const SIDES = ['left', 'right'];
const VPOS  = ['top', 'center', 'bottom'];

(async () => {
  const file = path.resolve(process.argv[2]);
  const browser = await chromium.launch({
    executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('file://' + file);
  await page.waitForTimeout(600);

  const out = await page.evaluate(({ COLUMN, PAINTED, SIDES, VPOS }) => {
    const stage = document.querySelector('.stage');
    const slides = [...document.querySelectorAll('.slide')];
    const sr0 = stage.getBoundingClientRect();
    const SW = sr0.width, SH = sr0.height;

    // every rendered line of text inside el, as page rects
    function lineRects(el) {
      const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT);
      const lines = new Map();
      let n;
      while ((n = walker.nextNode())) {
        if (!n.nodeValue.trim()) continue;
        const p = n.parentElement;
        if (!p || !p.offsetParent && getComputedStyle(p).position !== 'fixed') {
          if (getComputedStyle(p).display === 'none') continue;
        }
        const r = document.createRange();
        r.selectNodeContents(n);
        for (const rect of r.getClientRects()) {
          if (rect.width < 1 || rect.height < 1) continue;
          const key = Math.round(rect.top / 4) * 4;
          const cur = lines.get(key);
          if (cur) {
            cur.l = Math.min(cur.l, rect.left); cur.r = Math.max(cur.r, rect.right);
            cur.t = Math.min(cur.t, rect.top);  cur.b = Math.max(cur.b, rect.bottom);
          } else lines.set(key, { l: rect.left, r: rect.right, t: rect.top, b: rect.bottom });
        }
      }
      return [...lines.values()];
    }

    function inkBox(el, sr) {
      const ls = lineRects(el);
      // painted boxes count as ink too - a dark card is as visible as its words
      for (const sel of PAINTED)
        for (const b of el.querySelectorAll(sel)) {
          const r = b.getBoundingClientRect();
          if (r.width > 2 && r.height > 2)
            ls.push({ l: r.left, r: r.right, t: r.top, b: r.bottom });
        }
      if (!ls.length) return null;
      const l = Math.min(...ls.map(v => v.l)), r = Math.max(...ls.map(v => v.r));
      const t = Math.min(...ls.map(v => v.t)), b = Math.max(...ls.map(v => v.b));
      let need = 0;
      for (const v of ls) need = Math.max(need, v.r - v.l);
      return { x: (l - sr.left) / SW, y: (t - sr.top) / SH,
               w: (r - l) / SW, h: (b - t) / SH, need: need / SW };
    }

    const prev = document.querySelector('.slide.is-active');
    const res = [];

    slides.forEach((sl, i) => {
      slides.forEach(s => s.classList.remove('is-active'));
      sl.classList.add('is-active');
      const entry = {
        index: i + 1, type: sl.dataset.type || '',
        side: sl.dataset.side || '', vpos: sl.dataset.vpos || '',
        bg: sl.dataset.bg || '', slots: {}, painted: []
      };

      // painted boxes, measured in the slide's own placement
      for (const sel of PAINTED)
        for (const el of sl.querySelectorAll(sel)) {
          const r = el.getBoundingClientRect();
          if (r.width < 4 || r.height < 4) continue;
          const ls = lineRects(el);
          let need = 0;
          for (const v of ls) need = Math.max(need, v.r - v.l);
          if (need <= 0) continue;
          const sr = stage.getBoundingClientRect();
          // The chrome a box is entitled to: its own padding and border. A box
          // is judged on the room it gives the TEXT, not on the box, or every
          // correctly-fitted button reads as half again too wide.
          const cs = getComputedStyle(el);
          const pad = parseFloat(cs.paddingLeft) + parseFloat(cs.paddingRight)
                    + parseFloat(cs.borderLeftWidth) + parseFloat(cs.borderRightWidth);
          entry.painted.push({ sel, x: (r.left - sr.left) / SW, y: (r.top - sr.top) / SH,
                               w: r.width / SW, h: r.height / SH,
                               need: need / SW, pad: pad / SW });
        }

      // Does anything paint outside the canvas? Nothing scrolls in this
      // format, so a slide that overflows loses a line where nobody sees it.
      {
        const sr = stage.getBoundingClientRect();
        let over = 0;
        for (const el of sl.querySelectorAll('*')) {
          const r = el.getBoundingClientRect();
          if (r.width < 2 || r.height < 2) continue;
          if (getComputedStyle(el).position === 'fixed') continue;
          over = Math.max(over, r.bottom - sr.bottom, sr.top - r.top,
                                r.right - sr.right, sr.left - r.left);
        }
        entry.overflow = Math.round(over);
      }

      // ink box in each placement the deck can express
      if (sl.dataset.side) {
        const os = sl.dataset.side, ov = sl.dataset.vpos;
        for (const side of SIDES) for (const vpos of VPOS) {
          sl.dataset.side = side;
          if (vpos === 'center') delete sl.dataset.vpos; else sl.dataset.vpos = vpos;
          sl.getBoundingClientRect();
          const sr = stage.getBoundingClientRect();
          const boxes = {};
          for (const sel of COLUMN) {
            const el = sl.querySelector(sel);
            if (el) { const b = inkBox(el, sr); if (b) boxes[sel] = b; }
          }
          entry.slots[side + '/' + vpos] = boxes;
        }
        sl.dataset.side = os;
        if (ov) sl.dataset.vpos = ov; else delete sl.dataset.vpos;
      }
      res.push(entry);
    });

    slides.forEach(s => s.classList.remove('is-active'));
    if (prev) prev.classList.add('is-active');
    return { w: SW, h: SH, slides: res };
  }, { COLUMN, PAINTED, SIDES, VPOS });

  console.log(JSON.stringify(out));
  await browser.close();
})();
