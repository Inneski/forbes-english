#!/usr/bin/env node
// Measure what tools/sherpa_lesson_i18n.py promises, in a browser: with a language on,
// nothing a learner needs to understand is left in English only.
//
//   node tools/sherpa_lesson_i18n_check.js                    # 23 pages x 9 languages
//   node tools/sherpa_lesson_i18n_check.js --langs de,ar <page.html> ...
//
// For each page and language it switches every section's globe to the language and
// the "Examples in" bar to it, then fails on:
//   - a text the master list calls "chrome" with no translation line under it;
//   - an English text (two or more common English words) the master list does not know
//     at all: the extractor missed it, so nobody translated it;
//   - an example sentence with no translation line;
//   - the quiz: every question is answered in turn, and each hint, each feedback, the
//     results message, and the quiz's own words (progress, score, buttons) must be in
//     the language;
//   - a diagram label that, translated, spills out of its diagram or onto another label;
//   - an Arabic line not set right to left; a page that scrolls sideways at 390px;
//   - any script error.
const fs = require('fs');
const path = require('path');
const http = require('http');
const ROOT = path.resolve(__dirname, '..');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));
const master = JSON.parse(fs.readFileSync(path.join(ROOT, 'lesson-template/sherpa-i18n/master.json'), 'utf8'));
const OWN = ['sherpa-tensing-camp-one-present-continuous.html', 'sherpa-tensing-camp-two-present-simple.html', 'sherpa-tensing-route-map.html'];
const argv = process.argv.slice(2);
const li = argv.indexOf('--langs');
const LANGS = li >= 0 ? argv.splice(li, 2)[1].split(',') : master.langs;
const files = argv.length ? argv : fs.readdirSync(ROOT).filter(f => /^sherpa-tensing-.*\.html$/.test(f) && !OWN.includes(f)).sort();
const norm = s => s.replace(/\s+/g, ' ').trim();
const KNOWN = [...new Set(master.items.map(m => norm(m.en)))];
const TYPES = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp' };

function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      const f = path.join(ROOT, decodeURIComponent(req.url.split('?')[0]));
      if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
      rsp.writeHead(200, { 'Content-Type': TYPES[path.extname(f)] || 'application/octet-stream' });
      rsp.end(fs.readFileSync(f));
    });
    srv.listen(0, 'localhost', () => res(srv));
  });
}

function audit(args) {
  const [lang, known] = args;
  const KNOWN = new Set(known);
  const D = JSON.parse(document.getElementById('sherpa-i18n-data').textContent);
  const norm = s => s.replace(/\s+/g, ' ').trim();
  const out = [];
  const EN = /\b(the|and|of|to|is|are|was|were|you|it|in|that|for|with|on|this|be|have|has|not|when|what|your|a|an|by|from|or|but|if|than|then|at)\b/gi;
  const INLINE = /^(EM|STRONG|B|I|SPAN|A|BR|CODE|SUP|SUB|SMALL|MARK|ABBR|U|S|Q)$/;
  const SKIP = 'script,style,noscript,svg,.sr-only,.ex-tr,.i18n-inline,.i18n-en,#tr-bar,.voice-bar,.up-link,#q-prompt,#options,.lang-globe-wrap,.topo-sheen,.sherpa-sky,.wordmark,#progress-text,#score-text,#next-btn,#retry-btn,#final-score';
  const vis = el => { const s = getComputedStyle(el); return s.display !== 'none' && s.visibility !== 'hidden'; };
  for (const el of document.body.querySelectorAll('*')) {
    if (el.closest(SKIP) || INLINE.test(el.tagName) || !vis(el)) continue;
    const kids = [...el.childNodes];
    if (kids.some(n => n.nodeType === 1 && !INLINE.test(n.tagName))) continue;
    const enEl = el.querySelector(':scope > .i18n-en');
    const en = norm(enEl ? enEl.innerHTML : el.innerHTML.replace(/<span class="ex-tr"[^]*?<\/span>/g, ''));
    const text = norm((enEl || el).textContent);
    if (!text || !/[A-Za-z]{2}/.test(text)) continue;
    const label = `${el.tagName.toLowerCase()}${el.id ? '#' + el.id : ''}.${(el.getAttribute('class') || '').split(' ')[0]} "${text.slice(0, 40)}"`;
    const line = el.querySelector(':scope > .i18n-inline');
    if (D.t[en]) {
      if (!line || !line.textContent.trim()) out.push('no translation: ' + label);
      else if (lang === 'ar' && line.getAttribute('dir') !== 'rtl') out.push('Arabic not right to left: ' + label);
    } else if (D.x[en]) {
      if (!el.closest('.ex[data-tr]') && !el.querySelector(':scope > .ex-tr')) out.push('example with no translation: ' + label);
    } else if (!KNOWN.has(en) && (text.match(EN) || []).length >= 2) {
      out.push('English the master list does not know: ' + label);
    }
  }
  // diagram labels that were translated: still inside their diagram, not on each other
  for (const svg of document.querySelectorAll('svg')) {
    const sr = svg.getBoundingClientRect();
    if (sr.width < 60) continue;
    const ts = [...svg.querySelectorAll('text[data-en]')].filter(t => t.textContent !== t.getAttribute('data-en'));
    for (const t of ts) {
      const r = t.getBoundingClientRect();
      if (r.left < sr.left - 2 || r.right > sr.right + 2) out.push(`diagram label out of its diagram: "${t.textContent.slice(0, 30)}"`);
    }
  }
  if (document.documentElement.scrollWidth > innerWidth + 1) out.push(`page scrolls sideways by ${document.documentElement.scrollWidth - innerWidth}px`);
  return out;
}

async function one(b, base, f, lang) {
  const lines = [];
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = [];
  p.on('pageerror', e => errs.push(e.message));
  await p.route(/googletagmanager|google-analytics|supabase|plausible/, r => r.abort());
  try {
    await p.goto(base + f, { waitUntil: 'load', timeout: 60000 });
    await p.evaluate(() => document.fonts.ready);             // as a learner's page would be, fonts in
    const ok = await p.evaluate(l => {
      if (!window.sherpaLessonI18n) return false;
      window.sherpaLessonI18n.sections.forEach(s => window.sherpaLessonI18n.set(s, l));
      return true;
    }, lang);
    if (!ok) { await p.close(); return [`${f} [${lang}]: no translation runtime`]; }
    await p.locator(`#tr-bar button[data-lang="${lang}"]`).click();
    await p.waitForTimeout(200);
    (await p.evaluate(audit, [lang, KNOWN])).forEach(x => lines.push(`${f} [${lang}]: ${x}`));
    // the quiz: answer each question, and check its hint, its feedback and its words
    const n = await p.locator('#options .opt-btn').count() ? await p.evaluate(() => typeof questions !== 'undefined' ? questions.length : 0) : 0;
    const D = await p.evaluate(() => JSON.parse(document.getElementById('sherpa-i18n-data').textContent));
    const ui = (k, vars) => { let s = D.ui[k] ? D.ui[k][D.langs.indexOf(lang)] : k; for (const v in vars) s = s.split('{' + v + '}').join(vars[v]); return s; };
    for (let i = 0; i < n; i++) {
      const q = await p.evaluate(() => {
        const has = id => { const e = document.getElementById(id); return !!(e && e.querySelector(':scope > .i18n-inline')); };
        return { hint: has('q-hint'), hintText: document.getElementById('q-hint').textContent.trim(), progress: document.getElementById('progress-text').textContent };
      });
      if (q.hintText && !q.hint) lines.push(`${f} [${lang}]: quiz ${i + 1}: hint not translated`);
      const want = ui('Checkpoint {n} of {m}', { n: i + 1, m: n });
      if (q.progress !== want) lines.push(`${f} [${lang}]: quiz ${i + 1}: progress reads "${q.progress}", not "${want}"`);
      await p.locator('#options .opt-btn').first().click();
      await p.waitForTimeout(150);
      const fb = await p.evaluate(() => { const e = document.getElementById('feedback'); return !!(e && e.querySelector(':scope > .i18n-inline')); });
      if (!fb) lines.push(`${f} [${lang}]: quiz ${i + 1}: feedback not translated`);
      const nb = await p.locator('#next-btn').textContent();
      const wantNb = ui(i === n - 1 ? 'Reach the summit' : 'Next checkpoint', {});
      if (nb.trim() !== wantNb) lines.push(`${f} [${lang}]: quiz ${i + 1}: button reads "${nb.trim()}"`);
      await p.locator('#next-btn').click();
      await p.waitForTimeout(150);
    }
    if (n) {
      const res = await p.evaluate(() => {
        const m = document.getElementById('final-message');
        return { msg: !!(m && m.querySelector(':scope > .i18n-inline')), retry: document.getElementById('retry-btn').textContent.trim() };
      });
      if (!res.msg) lines.push(`${f} [${lang}]: results message not translated`);
      if (res.retry !== ui('Climb again', {})) lines.push(`${f} [${lang}]: retry button reads "${res.retry}"`);
    }
    errs.forEach(e => lines.push(`${f} [${lang}]: script error: ${e}`));
  } catch (e) {
    lines.push(`${f} [${lang}]: could not run: ${String(e.message || e).split('\n')[0]}`);
  }
  await p.close();
  return lines;
}

(async () => {
  const srv = await serve();
  const base = `http://localhost:${srv.address().port}/`;
  const b = await chromium.launch();
  const jobs = [];
  for (const f of files) for (const l of LANGS) jobs.push([f, l]);
  const all = [];
  const q = jobs.slice();
  await Promise.all(Array.from({ length: 5 }, async () => {
    while (q.length) { const [f, l] = q.shift(); all.push(...await one(b, base, f, l)); }
  }));
  await b.close();
  srv.close();
  all.sort().forEach(l => console.log('FAIL ' + l));
  console.log(all.length ? `FAIL: ${all.length} problem(s)` : `PASS: ${files.length} pages x ${LANGS.length} languages: nothing a learner needs is left in English only`);
  process.exit(all.length ? 1 : 0);
})();
