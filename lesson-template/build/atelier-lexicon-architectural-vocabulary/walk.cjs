// Headless walk-through of atelier-lexicon-architectural-vocabulary.html: a 30-question quiz at 1920 and 375,
// option generation (notWith bans, 4 distinct options), blanks, key leaks, language switching,
// Arabic RTL, and layout at eight widths. Needs the site served (.claude/launch.json "site").
//   node walk.cjs [port] [screenshot-dir]      exit 1 and a list on any failure
const { chromium } = require('playwright');
const path = require('path');
const OUT = process.argv[3] || require('os').tmpdir();
const port = process.argv[2] || '8099';
const URL = `http://localhost:${port}/atelier-lexicon-architectural-vocabulary.html`;
const fails = [];
const ok = (cond, msg) => { if (!cond) fails.push(msg); };

(async () => {
  const b = await chromium.launch();
  // Layout at every width Innes or a student is likely to use, home and quiz views.
  for (const w of [360, 375, 414, 768, 1024, 1280, 1440, 1920]) {
    const p = await (await b.newContext({ viewport: { width: w, height: w < 700 ? 812 : 900 } })).newPage();
    await p.goto(URL + '?lang=de', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);
    for (const view of ['home', 'quiz', 'study']) {
      if (view === 'quiz') { await p.evaluate(() => { startQuiz(); selectAnswer(state.questions[0].options[0].id); }); }
      if (view === 'study') { await p.evaluate(() => { goHome(); setHomeMode('study'); toggleStudyCard(1); }); }
      await p.waitForTimeout(450);
      const m = await p.evaluate(() => {
        const R = (e) => e.getBoundingClientRect();
        const h = R(document.querySelector('header')), t = document.querySelectorAll('#brandHomeBtn div span');
        const title = R(t[0]), sub = R(t[1]), lang = R(document.querySelector('.fe-lang')), brand = R(document.querySelector('#brandHomeBtn'));
        const lines = Math.round(sub.height / parseFloat(getComputedStyle(t[1]).lineHeight));
        const home = document.querySelector('.fe-home'), fixed = getComputedStyle(home).position === 'fixed';
        if (!fixed) home.scrollIntoView({ block: 'center' });
        const hb = R(home), hit = document.elementFromPoint(hb.left + hb.width / 2, hb.top + hb.height / 2);
        const main = R(document.querySelector('main section') || document.querySelector('main'));
        const cat = document.querySelector('.fe-cat'), badge = cat && cat.parentNode.querySelectorAll('span.absolute')[1];
        const catOver = cat && badge ? R(cat).right > R(badge).left : false;
        window.scrollTo(0, 0);
        return { sw: document.documentElement.scrollWidth, iw: innerWidth, lines, titleTop: title.top, subBottom: sub.bottom, hBottom: h.bottom,
          brandLang: brand.right <= lang.left, homeHit: !!hit && (hit === home || home.contains(hit)), fixed,
          homeOverMain: fixed && hb.right > main.left && hb.bottom > main.top && hb.top < main.bottom, catOver };
      });
      const tag = `${w}/${view}`;
      ok(m.sw <= m.iw, `${tag}: sideways scroll ${m.sw} > ${m.iw}`);
      ok(m.lines <= 2 && m.titleTop >= 0 && m.subBottom <= m.hBottom, `${tag}: brand overflows header (lines ${m.lines}, top ${m.titleTop}, bottom ${m.subBottom}/${m.hBottom})`);
      ok(m.brandLang, `${tag}: brand runs into the language pill`);
      ok(m.homeHit, `${tag}: library link not hittable`);
      ok(m.fixed === (w >= 1280), `${tag}: library link fixed=${m.fixed}`);
      ok(!m.homeOverMain, `${tag}: floating library link covers the content column`);
      ok(!m.catOver, `${tag}: category label runs under the question-type badge`);
    }
    await p.close();
  }
  for (const vp of [{ w: 1920, h: 1080, tag: 'desk' }, { w: 375, h: 812, tag: 'phone' }]) {
    const ctx = await b.newContext({ viewport: { width: vp.w, height: vp.h }, deviceScaleFactor: 1, locale: 'en-GB' });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', (e) => errs.push(String(e)));
    p.on('console', (m) => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto(URL + '?lang=de', { waitUntil: 'networkidle' });
    await p.evaluate(() => document.fonts.ready);

    // Layout: no sideways scroll, header pieces do not overlap, controls are hittable.
    const lay = await p.evaluate(() => {
      const r = (s) => { const e = document.querySelector(s); return e ? e.getBoundingClientRect().toJSON() : null; };
      const hit = (s) => { const e = document.querySelector(s); if (!e) return 'missing'; const b = e.getBoundingClientRect();
        const t = document.elementFromPoint(b.left + b.width / 2, b.top + b.height / 2); return t && (t === e || e.contains(t)) ? 'ok' : (t ? t.outerHTML.slice(0, 80) : 'null'); };
      return { sw: document.documentElement.scrollWidth, iw: innerWidth, brand: r('#brandHomeBtn'), lang: r('.fe-lang'), ctrl: r('#headerControls'),
        header: r('header'), hitLang: hit('.fe-lang select'), hitHome: hit('.fe-home'), code: document.getElementById('feLangCode').textContent,
        opts: [...document.querySelectorAll('#feLangSelect option')].map((o) => o.value) };
    });
    ok(lay.sw <= lay.iw, `${vp.tag}: page scrolls sideways (${lay.sw} > ${lay.iw})`);
    ok(lay.brand.right <= lay.lang.left, `${vp.tag}: brand overlaps the language pill (${lay.brand.right} > ${lay.lang.left})`);
    ok(lay.lang.bottom <= lay.header.bottom && lay.brand.bottom <= lay.header.bottom + 0.5, `${vp.tag}: header content taller than the header`);
    ok(lay.hitLang === 'ok', `${vp.tag}: language select not hittable: ${lay.hitLang}`);
    ok(lay.code === 'DE', `${vp.tag}: pill shows ${lay.code}, expected DE`);
    ok(lay.opts.length === 11, `${vp.tag}: ${lay.opts.length} languages in the menu`);
    await p.screenshot({ path: path.join(OUT, `${vp.tag}-1-home.png`) });

    if (vp.tag === 'desk') {
      // Engine checks, straight against the page's own functions.
      const eng = await p.evaluate(() => {
        const out = { banned: [], sizes: [], blanks: [], leaks: [] };
        for (let n = 0; n < 300; n++) for (const it of VOCAB_DATA) {
          const opts = generateOptionsForItem(it), ids = opts.map((o) => o.id);
          if (opts.length !== 4 || new Set(ids).size !== 4 || !ids.includes(it.id)) out.sizes.push(it.id);
          for (const bad of it.notWith || []) if (ids.includes(bad)) out.banned.push(it.id + '<-' + bad);
        }
        for (const it of VOCAB_DATA) {
          const s = createFillInBlankSentence(it);
          if (s === it.example) out.blanks.push(it.id);
          const bare = s.replace(/<[^>]+>/g, ' ').toLowerCase();
          if (bare.includes(it.term.toLowerCase()) || bare.includes((it.highlightText || '').toLowerCase())) out.leaks.push(it.id);
          if (it.meaning.toLowerCase().includes(it.term.toLowerCase())) out.leaks.push('m' + it.id);
        }
        out.notWith = VOCAB_DATA.filter((v) => v.notWith).map((v) => v.id + ':' + v.notWith.join(','));
        out.t26 = VOCAB_DATA[25].term;
        return out;
      });
      ok(!eng.banned.length, `banned distractor offered: ${[...new Set(eng.banned)].join(' ')}`);
      ok(!eng.sizes.length, `option set wrong for ${[...new Set(eng.sizes)].join(' ')}`);
      ok(!eng.blanks.length, `no blank made for ${eng.blanks.join(' ')}`);
      ok(!eng.leaks.length, `key visible in its own prompt: ${eng.leaks.join(' ')}`);
      ok(eng.notWith.join(' ') === '10:9 25:27 30:29', `notWith = ${eng.notWith.join(' ')}`);
      ok(eng.t26 === 'Maximize the ingress of natural light', `term 26 = ${eng.t26}`);
    }

    // Full quiz, all 30, mixed. Answer wrong on every 4th question.
    await p.click('text=Begin Illustrated Quiz');
    let seen = 0, glossSeen = 0, contextQs = 0, defQs = 0;
    for (let i = 0; i < 30; i++) {
      const q = await p.evaluate(() => ({ idx: state.currentIndex, id: state.questions[state.currentIndex].item.id,
        type: state.questions[state.currentIndex].questionType, opts: state.questions[state.currentIndex].options.map((o) => o.id),
        prompt: document.querySelector('main h2').textContent.trim(), glossBefore: !!document.querySelector('.fe-gloss') }));
      ok(q.idx === i, `quiz index ${q.idx} at step ${i}`);
      ok(!q.glossBefore, `gloss shown before answering (item ${q.id})`);
      if (q.type === 'context') { contextQs++; ok(q.prompt.includes('______'), `context prompt has no blank (item ${q.id})`); } else defQs++;
      const pick = i % 4 === 3 ? q.opts.findIndex((id) => id !== q.id) : q.opts.indexOf(q.id);
      const btns = await p.$$('main button[onclick^="selectAnswer"]');
      ok(btns.length === 4, `${btns.length} answer buttons (item ${q.id})`);
      await btns[pick].click();
      const fb = await p.evaluate(() => ({ gloss: document.querySelector('.fe-gloss') ? document.querySelector('.fe-gloss').innerText : '',
        next: !!document.querySelector('button[onclick="nextQuestion()"]') }));
      ok(fb.next, `no Next button after answering (item ${q.id})`);
      ok(fb.gloss.includes('DEUTSCH') || fb.gloss.includes('Deutsch'), `no German gloss after answering (item ${q.id})`);
      if (fb.gloss) glossSeen++;
      if (i === 2) await p.screenshot({ path: path.join(OUT, `${vp.tag}-2-answered.png`), fullPage: vp.tag === 'phone' });
      if (i === 4) { // switch language mid-quiz: re-renders in place, score kept
        const before = await p.evaluate(() => state.score);
        await p.selectOption('#feLangSelect', 'es');
        const after = await p.evaluate(() => ({ score: state.score, idx: state.currentIndex, gloss: (document.querySelector('.fe-gloss') || {}).innerText || '', url: location.search, code: document.getElementById('feLangCode').textContent }));
        ok(after.score === before && after.idx === 4, `language switch lost the quiz state`);
        ok(/ESPAÑOL|Español/.test(after.gloss), `gloss did not switch to Spanish: ${after.gloss.slice(0, 40)}`);
        ok(after.url.includes('lang=es') && after.code === 'ES', `url/pill not updated: ${after.url} ${after.code}`);
        await p.selectOption('#feLangSelect', 'en');
        ok(await p.evaluate(() => !document.querySelector('.fe-gloss')), 'English still shows a gloss');
        await p.selectOption('#feLangSelect', 'de');
      }
      seen++;
      await p.click('button[onclick="nextQuestion()"]');
    }
    const res = await p.evaluate(() => ({ view: state.view, total: state.history.length, correct: state.history.filter((h) => h.isCorrect).length,
      missedCards: document.querySelectorAll('main .fe-gloss').length, h1: document.querySelector('main h1').textContent.trim() }));
    ok(res.view === 'results' && res.total === 30, `results: view ${res.view}, ${res.total} answered`);
    ok(res.correct === 30 - 7, `results: ${res.correct} correct, expected 23`);
    ok(res.missedCards === 7, `results review list shows ${res.missedCards} glosses, expected 7`);
    ok(contextQs === 15 && defQs === 15, `mixed mode gave ${defQs} definition / ${contextQs} context`);
    await p.screenshot({ path: path.join(OUT, `${vp.tag}-3-results.png`), fullPage: vp.tag === 'phone' });

    // Study deck: search "lighting" — grid, button count and the quiz it starts must agree.
    await p.click('text=Return to Menu');
    await p.click('text=Illustrated Study Deck');
    await p.fill('#studySearchInput', 'lighting');
    const sd = await p.evaluate(() => ({ cards: document.querySelectorAll('main article').length,
      btn: [...document.querySelectorAll('main button')].map((b) => b.textContent.trim()).find((t) => t.startsWith('Quiz These')) }));
    ok(sd.cards === 6 && sd.btn === 'Quiz These (6)', `study search: ${sd.cards} cards, button "${sd.btn}"`);
    await p.click('text=Reveal All Notes');
    const rv = await p.evaluate(() => ({ glosses: document.querySelectorAll('main article .fe-gloss').length, btn: [...document.querySelectorAll('main button')].some((b) => b.textContent.trim() === 'Hide All Notes') }));
    ok(rv.glosses === 6 && rv.btn, `reveal all: ${rv.glosses} glosses, hide button ${rv.btn}`);
    await p.screenshot({ path: path.join(OUT, `${vp.tag}-4-study.png`), fullPage: vp.tag === 'phone' });
    await p.click('text=Quiz These (6)');
    const qn = await p.evaluate(() => state.questions.length);
    ok(qn === 6, `Quiz These (6) started a quiz of ${qn}`);

    // Arabic: gloss runs right to left.
    await p.selectOption('#feLangSelect', 'ar');
    const opt0 = await p.$$('main button[onclick^="selectAnswer"]');
    await opt0[0].click();
    const ar = await p.evaluate(() => { const g = document.querySelector('.fe-gloss'); return g ? getComputedStyle(g).direction : 'none'; });
    ok(ar === 'rtl', `Arabic gloss direction ${ar}`);
    await p.screenshot({ path: path.join(OUT, `${vp.tag}-5-arabic.png`), fullPage: vp.tag === 'phone' });

    ok(!errs.length, `${vp.tag}: console errors: ${errs.join(' | ').slice(0, 300)}`);
    console.log(`${vp.tag}: ${seen} questions walked, ${glossSeen} glosses shown`);
    await ctx.close();
  }
  await b.close();
  console.log(fails.length ? 'FAIL\n  ' + fails.join('\n  ') : 'PASS — every check');
  process.exit(fails.length ? 1 : 0);
})();
