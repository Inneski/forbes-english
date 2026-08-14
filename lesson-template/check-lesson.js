/**
 * Forbes English — pre-ship lesson checker.
 *
 *   node lesson-template/check-lesson.js <lesson.html>
 *
 * Checks the things that have actually gone wrong on this site, mechanically,
 * so they cannot be missed by eye:
 *
 *   LAYOUT   every slide fits the 1280x720 canvas, and nothing scrolls
 *   ANSWERS  the correct MC option is not simply the longest one
 *   BANK     a word bank does not hand over the gap answers in gap order
 *   EXPLAIN  every scored question carries an explanation
 *   ACTIVATE every lesson ends with a speaking + writing production task
 *   SORT     every sorting slide has 2+ bins, no stray items, no empty bin
 *   I18N     at least one language besides English is complete, and every data-i18n
 *            attribute resolves to a real key
 *   LOGO     Forbes and ENGLISH render to the same optical width
 *   RUNTIME  no JS errors
 *
 * Exit code is non-zero if anything fails. Run it before every push.
 */
const { chromium } = require('playwright');
const path = require('path');

const file = process.argv[2];
if (!file) { console.error('usage: node check-lesson.js <lesson.html>'); process.exit(1); }

const RED = s => `\x1b[31m${s}\x1b[0m`;
const GRN = s => `\x1b[32m${s}\x1b[0m`;
const DIM = s => `\x1b[2m${s}\x1b[0m`;

(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
  const jsErrors = [];
  page.on('pageerror', e => jsErrors.push(e.message));
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(2000);

  const r = await page.evaluate(() => {
    const out = { layout: [], answers: [], explain: [], i18n: [], logo: null, scroll: null, bank: null, markup: null, sort: [] };
    const slides = [...document.querySelectorAll('.slide')];

    // ── LAYOUT ──────────────────────────────────────────────────────
    slides.forEach((s, i) => {
      const wasActive = s.classList.contains('is-active');
      const anim = s.style.animation;
      s.style.animation = 'none';
      s.classList.add('is-active');

      let worst = 0, culprit = '';
      [s, ...s.querySelectorAll('.slide-body, .cover-inner, .opts, .card')].forEach(b => {
        const over = b.scrollHeight - b.clientHeight;
        if (over > worst) { worst = over; culprit = (b.className || '').split(' ')[0]; }
      });
      const scale = s.getBoundingClientRect().width / 1280 || 1;
      const cs = getComputedStyle(s);
      let stack = 0;
      [...s.children].forEach(c => {
        const m = getComputedStyle(c);
        stack += c.getBoundingClientRect().height
               + parseFloat(m.marginTop) + parseFloat(m.marginBottom);
      });
      const needed = Math.round(stack / scale + parseFloat(cs.paddingTop) + parseFloat(cs.paddingBottom));
      const over = Math.max(needed - 720, Math.round(worst / scale));
      if (over > 1) out.layout.push({ n: i + 1, over, culprit });

      // ── ANSWERS: is the key simply the longest option? ────────────
      if (s.dataset.type === 'mc') {
        const opts = [...s.querySelectorAll('.opt')];
        const key = opts.find(o => o.hasAttribute('data-correct'));
        if (key) {
          const txt = o => o.textContent.replace(/^[A-D]\s*/, '').trim().length;
          const kl = txt(key);
          const others = opts.filter(o => o !== key).map(txt);
          const maxOther = Math.max(...others);
          // Flag only a NOTICEABLE excess. A two-character difference is not
          // something a learner can scan for; 10%+ on a full option is.
          // The ratio alone is not enough: on one-word options (a modal-verb
          // lesson offering can / could / must / should) "should" beats "must"
          // by 50% while carrying no information at all, because the option
          // set is closed and the learner can see all of it. So the excess has
          // to clear an absolute floor as well.
          if (kl > maxOther * 1.10 && kl - maxOther >= 4) {
            out.answers.push({ n: i + 1, key: kl, maxOther, ratio: +(kl / maxOther).toFixed(2) });
          }
        }
      }

      // ── EXPLAIN ──────────────────────────────────────────────────
      if (['mc', 'gap', 'order'].includes(s.dataset.type)) {
        const fbs = [...s.querySelectorAll('.feedback')];
        // Either every option explains itself, or the slide explains the answer.
        const opts = [...s.querySelectorAll('.opt')];
        const perOption = opts.length > 0 && opts.every(o => o.dataset.explain);
        const missing = !perOption && (fbs.length === 0 || fbs.some(f => !f.dataset.explain));
        if (missing) out.explain.push({ n: i + 1, type: s.dataset.type });
      }

      if (!wasActive) s.classList.remove('is-active');
      s.style.animation = anim;
    });

    // ── MARKUP: does any explanation print its own tags? ────────────
    // Explanations mark the word being taught with <strong>/<em>. If the
    // engine writes them with textContent instead of innerHTML the learner
    // reads the tags. Shipped on 26 pages of one family and 19 of another
    // before it was caught, so it is measured here rather than remembered:
    // answer the first scored question and look at what actually rendered.
    {
      const marked = [...document.querySelectorAll('[data-explain]')]
        .filter(el => /<(strong|em|b|i|code)\b/i.test(el.dataset.explain));
      if (marked.length) {
        const slide = marked[0].closest('.slide');
        const opt = slide && slide.querySelector('.opt');
        const check = slide && slide.querySelector('[data-action="check"]');
        if (opt) opt.click(); else if (check) check.click();
        const shown = [...document.querySelectorAll('.feedback.show')]
          .map(e => e.textContent || '')
          .filter(t => /<(strong|em|b|i|code)\b/i.test(t));
        if (shown.length) out.markup = shown.map(t => t.slice(0, 70));
      }
    }

    // ── BANK: does a word bank give the answers away? ───────────────
    // A bank listing the answers in the same order as the gaps below it is
    // not a scaffold, it is an answer key: the learner reads straight down.
    // Shipped twice before it was caught, so it is measured here now.
    {
      const seen = [];
      [...document.querySelectorAll('.bank-chip')].forEach(c => {
        const t = c.textContent.trim();
        if (t && !seen.includes(t)) seen.push(t);
      });
      const answers = [...document.querySelectorAll('input.gap[data-answer]')]
        .map(g => g.dataset.answer.split('|')[0].trim());
      const pos = answers.map(a => seen.indexOf(a));
      const found = pos.filter(p => p >= 0);
      // Two or more answers present AND appearing in gap order is the failure.
      const ascending = found.length >= 2 &&
        found.every((v, i, arr) => i === 0 || arr[i - 1] < v);
      if (ascending) out.bank = { answers, positions: pos, bank: seen.slice(0, 12) };
    }

    // ── SORT ────────────────────────────────────────────────────────
    // A sorting slide stops being a decision in two ways: an item that
    // points at a bin which does not exist (unplaceable, and it will sit
    // in the pool for ever), or a bin that receives nothing — sorting
    // into a box that nothing goes in is a choice the learner cannot get
    // wrong, and its presence makes the real choice easier by one.
    [...document.querySelectorAll('.sort')].forEach((box, n) => {
      const bins = (box.dataset.bins || '').split('|').map(x => x.trim()).filter(Boolean);
      const items = [...box.querySelectorAll('.sort-item')];
      const targets = items.map(i => +i.dataset.bin);
      const stray = items.filter(i => !(+i.dataset.bin >= 0 && +i.dataset.bin < bins.length));
      if (bins.length < 2) out.sort.push({ n: n + 1, why: `only ${bins.length} bin(s) — a sort needs at least two` });
      if (stray.length) out.sort.push({ n: n + 1, why: `${stray.length} item(s) point at a bin that does not exist: ` + stray.map(i => i.textContent.trim()).join(', ') });
      const empty = bins.map((b, i) => [b, i]).filter(([, i]) => !targets.includes(i));
      if (empty.length) out.sort.push({ n: n + 1, why: 'bin(s) receive no items: ' + empty.map(([b]) => `"${b}"`).join(', ') });
    });

    // ── I18N ────────────────────────────────────────────────────────
    if (typeof UI_I18N !== 'undefined') {
      const en = Object.keys(UI_I18N.en || {});
      // The house minimum is English plus one finished language. It used to
      // be checked as "German covers English", which was right for every
      // deck until the first one shipped English + Japanese: a complete ja
      // and an empty de is a legitimate finished state, and the gate failed
      // it while passing a deck with no second language at all. What the
      // rule actually says is "at least one language besides English is
      // complete" — so that is what is measured.
      const complete = Object.keys(UI_I18N)
        .filter(c => c !== 'en' && Object.keys(UI_I18N[c] || {}).length >= en.length);
      if (!complete.length) {
        const started = Object.keys(UI_I18N)
          .filter(c => c !== 'en' && Object.keys(UI_I18N[c] || {}).length > 0);
        out.i18n.push({
          kind: 'no second language is complete — English plus one finished language is the minimum',
          list: started.length
            ? started.map(c => `${c}: ${Object.keys(UI_I18N[c]).length}/${en.length}`)
            : ['every language other than English is empty'],
        });
      }
      // A partially-filled language is the dangerous state: it shows in the
      // menu but silently falls back to English mid-interface.
      if (typeof LANGS !== 'undefined') {
        LANGS.filter(l => l.code !== 'en').forEach(l => {
          const n = Object.keys(UI_I18N[l.code] || {}).length;
          if (n > 0 && n < en.length) {
            out.i18n.push({ kind: `${l.label} is partial (${n}/${en.length}) — finish it or empty it`, list: [] });
          }
        });
      }
      out.langs = (typeof LANGS !== 'undefined' ? LANGS : [])
        .filter(l => l.code === 'en' || Object.keys(UI_I18N[l.code] || {}).length >= en.length).length;
      const unresolved = [...document.querySelectorAll('[data-i18n]')]
        .map(e => e.dataset.i18n)
        .filter(k => !(UI_I18N.en || {})[k]);
      if (unresolved.length) out.i18n.push({ kind: 'data-i18n with no English key', list: [...new Set(unresolved)] });
    } else {
      out.i18n.push({ kind: 'no UI_I18N found', list: [] });
    }

    // ── LOGO balance ────────────────────────────────────────────────
    const svg = document.querySelector('.fe-logo');
    if (svg) {
      const mark = svg.querySelector('g');
      const word = svg.querySelector('text');
      if (mark && word) {
        const a = mark.getBoundingClientRect().width;
        const b = word.getBoundingClientRect().width;
        out.logo = { mark: Math.round(a), word: Math.round(b), diff: +(Math.abs(a - b) / Math.max(a, b) * 100).toFixed(1) };
      }
    }

    out.scroll = {
      y: document.documentElement.scrollHeight > window.innerHeight,
      x: document.documentElement.scrollWidth > window.innerWidth
    };
    out.hasActivation = slides.some(s => s.dataset.type === 'activate');
    out.slideCount = slides.length;
    return out;
  });

  let fails = 0;
  const head = t => console.log('\n  ' + t);
  const ok = m => console.log('    ' + GRN('PASS') + '  ' + m);
  const bad = m => { fails++; console.log('    ' + RED('FAIL') + '  ' + m); };

  console.log(`\n  ${path.basename(file)} — ${r.slideCount} slides`);

  head('LAYOUT');
  if (!r.layout.length) ok('every slide fits the 1280x720 canvas');
  else r.layout.forEach(l => bad(`slide ${l.n} overflows by ${l.over}px (${l.culprit})`));
  if (!r.scroll.y && !r.scroll.x) ok('no scrolling');
  else bad(`page scrolls (y:${r.scroll.y} x:${r.scroll.x})`);

  head('ANSWERS');
  if (!r.answers.length) ok('no multiple-choice answer is conspicuously the longest');
  else {
    r.answers.forEach(a => bad(
      `slide ${a.n}: correct option is longest — ${a.key} chars vs ${a.maxOther} (${a.ratio}x). ` +
      `A learner can score by picking the longest.`));
    console.log(DIM('          Fix by lengthening the distractors, not by shortening the key.'));
  }

  head('BANK');
  if (!r.bank) ok('no word bank hands over the answers in order');
  else {
    bad(`the word bank lists the gap answers in gap order: ${r.bank.answers.join(' → ')}`);
    console.log(DIM(`          bank reads: ${r.bank.bank.join(' · ')}`));
    console.log(DIM('          Sort the bank, or shuffle it — a learner must not be able to read straight down.'));
  }

  head('MARKUP');
  if (!r.markup) ok('explanations render their markup instead of printing it');
  else r.markup.forEach(m => bad(`an explanation prints its own tags: ${m}…`));

  head('SORT');
  if (!r.sort || !r.sort.length) ok('every sorting slide is actually sortable');
  else r.sort.forEach(x => bad(`sort slide ${x.n}: ${x.why}`));

  head('EXPLAIN');
  if (!r.explain.length) ok('every scored question has an explanation');
  else r.explain.forEach(e => bad(`slide ${e.n} (${e.type}) has a question with no data-explain`));

  head('ACTIVATION');
  if (r.hasActivation) ok('lesson ends with an activation stage');
  else bad('no data-type="activate" slide — every lesson must end with a speaking + writing task');

  head('I18N');
  if (!r.i18n.length) ok(`${r.langs} complete language(s) offered; no partial ones; all data-i18n resolve`);
  else r.i18n.forEach(i => bad(`${i.kind}: ${i.list.slice(0, 8).join(', ')}${i.list.length > 8 ? ` +${i.list.length - 8} more` : ''}`));

  head('LOGO');
  if (!r.logo) bad('no .fe-logo found — the stacked lockup is required');
  else if (r.logo.diff <= 4) ok(`Forbes and ENGLISH match (${r.logo.mark}px / ${r.logo.word}px)`);
  else bad(`Forbes ${r.logo.mark}px vs ENGLISH ${r.logo.word}px — ${r.logo.diff}% apart, should be under 4%`);

  head('RUNTIME');
  const real = jsErrors.filter(e => !/ERR_TUNNEL|ERR_INTERNET|fonts\.googleapis/.test(e));
  if (!real.length) ok('no JS errors');
  else real.forEach(e => bad(e));

  console.log('\n  ' + (fails ? RED(`${fails} check(s) failed`) : GRN('all checks passed')) + '\n');
  await browser.close();
  process.exit(fails ? 1 : 0);
})();
