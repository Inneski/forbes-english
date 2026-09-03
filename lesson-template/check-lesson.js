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
 *   KEYS     the key is not parked at the same option letter every time, and
 *            the runtime shuffle that hides its position is a real shuffle
 *   BANK     a word bank does not hand over the gap answers in gap order
 *   EXPLAIN  every scored question carries an explanation
 *   RESOLVE  and that explanation is words, not an unresolved i18n key
 *   ACTIVATE every lesson ends with a speaking + writing production task
 *   SORT     every sorting slide has 2+ bins, no stray items, no empty bin
 *   I18N     at least one language besides English is complete, and every data-i18n
 *            attribute resolves to a real key
 *   HEAD     the page carries a real <title> and a generated SEO block —
 *            not the template's "Lesson Title" placeholder
 *   ART      every background and hero the page names exists on disk
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
  // The sandbox pins its own Chromium; on any other machine (Innes's Windows
  // box, with playwright installed globally) that path does not exist, so fall
  // back to whatever browser playwright installed for itself.
  const pinned = '/opt/pw-browsers/chromium';
  const browser = await chromium.launch(
    require('fs').existsSync(pinned) ? { executablePath: pinned } : {});
  const page = await browser.newPage({ viewport: { width: 1400, height: 820 } });
  const jsErrors = [];
  page.on('pageerror', e => jsErrors.push(e.message));
  await page.goto('file://' + path.resolve(file));
  await page.waitForTimeout(2000);

  const r = await page.evaluate(() => {
    const out = { layout: [], answers: [], explain: [], resolve: [], i18n: [], logo: null, scroll: null, bank: null, markup: null, sort: [] };
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

  // ── ACTIONS ───────────────────────────────────────────────────────
  // Every scored slide must actually be answerable. This exists because
  // `deck.order` emitted a plain [data-action="check"] button while the
  // engine routed sentence-building through "check-order": the click
  // landed in checkGaps, threw on a null input, and the Check button did
  // nothing on every deck with an order slide. Nothing measured it —
  // the LAYOUT pass never clicks, and a thrown handler is silent. So:
  // walk the deck, press the thing the learner would press, and require
  // that the slide ends up marked.
  const dead = await page.evaluate(async () => {
    const out = [];
    const slides = [...document.querySelectorAll('.slide')];
    const wait = () => new Promise(r => setTimeout(r, 40));
    for (let i = 0; i < slides.length; i++) {
      const s = slides[i];
      const type = s.dataset.type;
      if (!['mc', 'gap', 'order', 'sort', 'search', 'lock'].includes(type)) continue;
      slides.forEach((x, n) => x.classList.toggle('is-active', n === i));
      try {
        if (type === 'mc') {
          const o = s.querySelector('.opt[data-correct]'); if (o) o.click();
        } else if (type === 'gap') {
          s.querySelectorAll('input.gap').forEach(g => {
            g.value = (g.dataset.answer || '').split('|')[0];
          });
          const b = s.querySelector('[data-action="check"]'); if (b) b.click();
        } else if (type === 'order') {
          [...s.querySelectorAll('.chunk')]
            .sort((a, b) => +a.dataset.i - +b.dataset.i)
            .forEach(c => c.click());
          const b = s.querySelector('[data-action="check-order"], [data-action="check"]');
          if (b) b.click();
        } else if (type === 'sort') {
          [...s.querySelectorAll('.sort-item')].forEach(it => {
            it.click();
            const bin = s.querySelector(`.sort-bin[data-bin="${it.dataset.bin}"]`);
            if (bin) bin.click();
          });
        } else if (type === 'search') {
          const f = s.querySelector('.find[data-correct]'); if (f) f.click();
        } else if (type === 'lock') {
          const code = (s.querySelector('.lock').dataset.code || '').split('');
          const keys = [...s.querySelectorAll('.lock-key')];
          code.forEach(d => { const k = keys.find(x => x.textContent === d); if (k) k.click(); });
          const go = s.querySelector('.lock-keys .btn'); if (go) go.click();
        }
      } catch (e) {
        out.push({ n: i + 1, type, why: 'threw: ' + e.message });
        continue;
      }
      await wait();
      const marked = s.querySelector('.feedback.show')
        || s.querySelector('.opt.correct, .gap.correct, .order-target.correct, '
                           + '.sort-item.placed, .find.correct, .lock-cell.ok');
      if (!marked) out.push({ n: i + 1, type, why: 'answering it correctly changed nothing' });
    }
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

  // ── KEYS ────────────────────────────────────────────────────────
  // Two questions, both about the same failure: can a student score above
  // chance without reading the option?
  //
  // 1. Where is the key in the SOURCE? By the time the page is measurable the
  //    engine has already reordered the options, so this is invisible in the
  //    browser — which is why it survived until a student noticed. It still
  //    leaks through print and PDF export.
  // 2. Is the reordering a real shuffle? `arr.sort(() => Math.random() - .5)`
  //    is not one. Array.prototype.sort is entitled to anything at all when
  //    the comparator is inconsistent, and what V8 actually does with four
  //    elements is leave the first where it is 35.9% of the time against a
  //    fair 25%. Authored-first plus that comparator is a scoreable pattern.
  // ── RESOLVE ───────────────────────────────────────────────────────────
  // Answer the questions and read what the learner is actually shown.
  //
  // data-explain may hold the sentence itself, which is what most of the
  // library does, or a UI_I18N key so the explanation translates with the rest
  // of the deck. Both Grammar Court decks shipped keys into an engine with no
  // way to look one up, and eighty questions read "Correct. c1i1exp" on the
  // live site for three weeks. Every existing gate passed: the attribute was
  // present (EXPLAIN), it carried no tags to print (MARKUP), every data-i18n
  // node resolved (I18N), nothing threw (RUNTIME) and the deck still scored
  // 41/41. Nothing short of reading the rendered feedback can see it, so this
  // runs last, after every other measurement, and answers the paper to do it.
  const resolveMisses = await page.evaluate(() => {
    const misses = [];
    const slides = [...document.querySelectorAll('.slide')];
    slides.forEach(s => {
      const type = s.dataset.type;
      if (type !== 'mc' && type !== 'gap') return;
      slides.forEach(x => x.classList.remove('is-active'));
      s.classList.add('is-active');
      if (type === 'mc') {
        const key = [...s.querySelectorAll('.opt')].find(o => o.hasAttribute('data-correct'));
        if (key) key.click();
      } else {
        s.querySelectorAll('.gap').forEach(g => { g.value = (g.dataset.answer || '').split('|')[0]; });
        const btn = s.querySelector('[data-action="check"]');
        if (btn) btn.click();
      }
      // Whatever this slide names in data-explain — on the row, on an option,
      // on a single gap — must not come back out on screen verbatim. A written
      // explanation is a sentence and contains spaces, so it can never trip
      // this; only a key can, and a key on screen is the bug.
      const named = [s, ...s.querySelectorAll('[data-explain]')]
        .map(el => (el.dataset && el.dataset.explain || '').trim())
        .filter(v => v && !/\s/.test(v));
      s.querySelectorAll('.feedback').forEach(f => {
        const shown = f.textContent.trim();
        if (!shown) return;
        named.forEach(k => {
          if (new RegExp('(^|\\s)' + k.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '($|[\\s.,;:!?])').test(shown)) misses.push(k);
        });
      });
    });
    return [...new Set(misses)];
  });

  const src = require('fs').readFileSync(path.resolve(file), 'utf8');
  const optsBlocks = [...src.matchAll(/<div class="opts[^"]*">([\s\S]*?)<\/div>/g)];
  const keyAt = [];
  optsBlocks.forEach(b => {
    const btns = [...b[1].matchAll(/<button[^>]*class="opt"[^>]*>/g)].map(m => m[0]);
    const at = btns.findIndex(t => /\sdata-correct/.test(t));
    if (at >= 0 && btns.length > 1) keyAt.push({ at, of: btns.length });
  });
  const badShuffle = /\.sort\(\(\)\s*=>\s*Math\.random\(\)/.test(src);
  head('KEYS');
  let keysOk = true;
  if (keyAt.length >= 4) {
    const tally = {};
    keyAt.forEach(k => { tally[k.at] = (tally[k.at] || 0) + 1; });
    const [top, count] = Object.entries(tally).sort((a, b) => b[1] - a[1])[0];
    const share = count / keyAt.length;
    // One letter carrying most of the keys is a pattern; four questions all
    // answering A is the version of it that a student finds in a minute.
    if (share >= 0.8) {
      keysOk = false;
      bad(`the key is option ${'ABCDEFGH'[top]} in ${count} of ${keyAt.length} questions ` +
          `(${Math.round(share * 100)}%). Deal them across the letters in the source.`);
    }
  }
  if (badShuffle) {
    keysOk = false;
    bad('options are reordered with `sort(() => Math.random() - .5)`, which is not a shuffle');
    console.log(DIM('          Measured in V8 at n=4: the first element stays first 35.9% of the'));
    console.log(DIM('          time, not 25%. Use Fisher-Yates, or sort by a random key.'));
  }
  if (keysOk) ok(`the key moves around${keyAt.length ? ` across ${keyAt.length} questions` : ''}, and the shuffle is uniform`);

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

  head('ACTIONS');
  if (!dead.length) ok('every scored slide can actually be answered');
  else dead.forEach(d => bad(`slide ${d.n} (${d.type}): ${d.why}`));

  head('EXPLAIN');
  if (!r.explain.length) ok('every scored question has an explanation');
  else r.explain.forEach(e => bad(`slide ${e.n} (${e.type}) has a question with no data-explain`));

  head('RESOLVE');
  if (!resolveMisses.length) ok('answered feedback reads as words, not as an i18n key');
  else {
    bad(`the feedback prints its own key instead of the explanation: ` +
        `${resolveMisses.slice(0, 6).join(', ')}` +
        `${resolveMisses.length > 6 ? ` +${resolveMisses.length - 6} more` : ''}`);
    console.log(DIM('          A learner answering correctly reads "Correct. c1i1exp".'));
    console.log(DIM('          Either write the explanation into data-explain, or carry the'));
    console.log(DIM('          engine change that resolves a key through UI_I18N.'));
  }

  head('ACTIVATION');
  if (r.hasActivation) ok('lesson ends with an activation stage');
  else bad('no data-type="activate" slide — every lesson must end with a speaking + writing task');

  head('I18N');
  if (!r.i18n.length) ok(`${r.langs} complete language(s) offered; no partial ones; all data-i18n resolve`);
  else r.i18n.forEach(i => bad(`${i.kind}: ${i.list.slice(0, 8).join(', ')}${i.list.length > 8 ? ` +${i.list.length - 8} more` : ''}`));

  head('HEAD');
  {
    const title = (src.match(/<title>([\s\S]*?)<\/title>/) || [])[1];
    const hasSeo = /<!--\s*SEO:start\s*-->/.test(src) && /<!--\s*SEO:end\s*-->/.test(src);
    const canon  = /<link[^>]+rel="canonical"/.test(src);
    const placeholder = !title || /^\s*(Lesson Title|The Lesson Title)\b/i.test(title.trim());
    if (placeholder)
      bad(`<title> is still the template placeholder${title ? ` ("${title.trim()}")` : ' (missing)'} — set it, or run tools/seo.py which writes it from the Supabase row`);
    else if (!hasSeo)
      bad('no <!-- SEO:start --> block — run tools/seo.py so the page has a description, og tags and JSON-LD');
    else if (!canon)
      bad('SEO block present but no rel="canonical" — the block looks hand-written; run tools/seo.py');
    else
      ok(`head is complete — "${title.trim().slice(0, 58)}${title.trim().length > 58 ? '…' : ''}"`);
  }

  // ── ART ─────────────────────────────────────────────────────────────
  // A DECK CAN REFERENCE ARTWORK THAT IS NOT IN THE REPO, AND NOTHING SAID SO.
  // blockcamp-future-simple-2 shipped with --hero pointing at
  // future-simple-will/bg22-flip.jpg, a horizontally mirrored bg22 that was
  // made in the sandbox that built the deck and never committed - it has no
  // git history at all. The page does not error: a background-image that 404s
  // just paints nothing, so the cover went out black and stayed that way until
  // Innes opened it. "https://forbesenglish.com/blockcamp-future-simple-2 has
  // no cover."
  // Every gate here ran green on that page. They all measure the DOM, and the
  // DOM was fine; the file was missing on disk. So this one reads the disk.
  // Comments are stripped first - the authoring note in every deck names
  // data-bg="folder/other.jpg" as an example, and it is not a reference.
  head('ART');
  {
    const fs = require('fs');
    const src = fs.readFileSync(file, 'utf8').replace(/<!--[\s\S]*?-->/g, '');
    const dir = path.dirname(path.resolve(file));
    const refs = new Set();
    for (const m of src.matchAll(/--hero:\s*url\('([^']+)'\)/g)) refs.add(m[1]);
    for (const m of src.matchAll(/data-bg="([^"]+)"/g)) refs.add(m[1]);
    const gone = [...refs].filter(u => !/^(https?:|data:)/.test(u)
                                    && !fs.existsSync(path.join(dir, u)));
    if (gone.length) {
      bad(`${gone.length} image reference(s) point at a file that is not in the repo`);
      gone.forEach(u => console.log(DIM('          ' + u)));
      console.log(DIM('          A missing background paints nothing and throws nothing.'));
    } else {
      ok(`every one of ${refs.size} image reference(s) resolves on disk`);
    }
  }

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
