#!/usr/bin/env node
// Collect every piece of text on each Sherpa lesson page that a learner reads,
// for tools/sherpa_lesson_i18n.py to translate.
//
//   node tools/sherpa_lesson_strings.js [page.html ...]   # default: the 25 lesson pages
//
// Writes lesson-template/sherpa-i18n/<slug>.json, keeping any translations
// already in it. Each item: the English exactly as the page has it (inner
// HTML, whitespace collapsed), where it sits, and a first guess at its kind:
//   chrome   explanation, heading, note, hint: translated in place
//   example  a model English sentence: stays, with a translation line under it
//   keep     the English being taught (forms tables, quiz stems and options)
//   ?        undecided (mixed tables and lists): the translator decides
// The quiz is script-driven, so its hints, explanations and results messages
// come from the page's own `questions` array and source, not the DOM.
const fs = require('fs');
const path = require('path');
const http = require('http');
const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'lesson-template', 'sherpa-i18n');
const { chromium } = require(path.join(ROOT, 'node_modules', 'playwright'));
const files = process.argv.slice(2).length ? process.argv.slice(2)
  : fs.readdirSync(ROOT).filter(f => /^sherpa-tensing-.*\.html$/.test(f) && f !== 'sherpa-tensing-route-map.html'
      && f !== 'sherpa-tensing-the-climb.html' && f !== 'sherpa-tensing-the-descent.html').sort();  // the games have its own strings
const TYPES = { '.html': 'text/html', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.jpg': 'image/jpeg', '.png': 'image/png' };

function serve() {
  return new Promise(res => {
    const srv = http.createServer((req, rsp) => {
      const u = decodeURIComponent(req.url.split('?')[0]);
      const f = path.join(ROOT, u);
      if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { rsp.writeHead(404); return rsp.end(); }
      rsp.writeHead(200, { 'Content-Type': TYPES[path.extname(u)] || 'application/octet-stream' });
      rsp.end(fs.readFileSync(f));
    });
    srv.listen(0, '127.0.0.1', () => res(srv));
  });
}

function collect() {
  const norm = s => s.replace(/\s+/g, ' ').trim();
  const INLINE = new Set(['EM', 'STRONG', 'B', 'I', 'SPAN', 'A', 'BR', 'CODE', 'SUP', 'SUB', 'SMALL', 'MARK', 'ABBR', 'U', 'S', 'Q']);
  // regions handled elsewhere: the shared UI strings, the quiz (from its data), translations
  const SKIP = 'script,style,noscript,svg,.sr-only,.ex-tr,#tr-bar,.voice-bar,.up-link,#q-prompt,#options,#q-hint,#feedback,' +
    '#progress-text,#score-text,#next-btn,#final-score,#final-message,#retry-btn,.topo-sheen';
  const kindOf = el => {
    if (el.closest('.ex, p.example, .use-ex, .ft-example, .example')) return 'example';
    if (el.closest('.opt-btn, .q-prompt')) return 'keep';
    if (el.closest('td, th, li, .signal-box, table')) return el.tagName === 'TH' ? 'chrome' : '?';
    return 'chrome';
  };
  const where = el => {
    const parts = [];
    for (let a = el; a && a !== document.body && parts.length < 3; a = a.parentElement) {
      const cls = a.getAttribute && a.getAttribute('class');
      parts.unshift(a.tagName.toLowerCase() + (cls ? '.' + cls.trim().split(/\s+/)[0] : '') + (a.id ? '#' + a.id : ''));
    }
    const camp = el.closest('.camp');
    const h = camp && camp.querySelector('h2');
    return (h ? '[' + norm(h.textContent) + '] ' : '') + parts.join(' > ');
  };
  // the section a globe would translate: the camp it sits in, or the hero
  const section = el => {
    const c = el.closest('.camp[id], section[id], .camp');
    if (c && c.id) return c.id;
    if (c) return 'camp-' + [...document.querySelectorAll('.camp')].indexOf(c);
    return el.closest('.wordmark') ? 'wordmark' : 'hero';
  };
  const items = [];
  const seen = new Set();
  // a "block": an element whose children are all inline, holding text of its own
  for (const el of document.body.querySelectorAll('*')) {
    if (el.closest(SKIP) || INLINE.has(el.tagName)) continue;
    const kids = [...el.childNodes];
    if (!kids.some(n => n.nodeType === 3 && n.textContent.trim())) {
      // no direct text: a block only if its element children are all inline and hold text
      if (!kids.length || kids.some(n => n.nodeType === 1 && !INLINE.has(n.tagName))) continue;
      if (!norm(el.textContent)) continue;
    } else if (kids.some(n => n.nodeType === 1 && !INLINE.has(n.tagName))) {
      // mixed block and text: take the text runs' parent anyway, as its own innerHTML minus blocks
      continue;
    }
    const en = norm(el.innerHTML);
    if (!/[A-Za-z]{2}/.test(el.textContent) || seen.has(en)) continue;
    seen.add(en);
    items.push({ en, kind: kindOf(el), where: where(el), section: section(el) });
  }
  // diagram labels (camp one translates its own): text only, one per <text>, the classifier
  // decides between a caption (translate) and a grammar form or time word (keep)
  for (const t of document.querySelectorAll('svg text')) {
    if (t.closest('defs,.topo-sheen,.sherpa-sky')) continue;
    const en = norm(t.textContent);
    if (!/[A-Za-z]{2}/.test(en) || seen.has('svg:' + en)) continue;
    seen.add('svg:' + en);
    items.push({ en, kind: '?', where: 'svg text ' + (t.closest('svg').getAttribute('class') || ''), section: section(t), svg: true });
  }
  // the quiz, from its data
  const qs = (typeof questions !== 'undefined' && Array.isArray(questions)) ? questions : [];
  // as the browser will serialise it once the quiz puts it on the page ("&#39;" comes back as "'"),
  // since that is what the runtime looks up
  const asDom = s => { const d = document.createElement('div'); d.innerHTML = s; return norm(d.innerHTML); };
  qs.forEach((q, i) => {
    for (const f of ['hint', 'explain']) {
      const en = q[f] ? asDom(q[f]) : '';
      if (en && !seen.has(en)) { seen.add(en); items.push({ en, kind: 'chrome', where: `quiz ${i + 1} ${f}`, section: 'quiz' }); }
    }
  });
  return items;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const srv = await serve();
  const b = await chromium.launch();
  for (const f of files) {
    const p = await b.newPage({ viewport: { width: 1280, height: 900 } });
    await p.route(/^https?:\/\/(?!127\.0\.0\.1)/, r => r.abort());
    await p.goto(`http://127.0.0.1:${srv.address().port}/${f}`, { waitUntil: 'load' });
    const items = await p.evaluate(collect);
    // the results messages live only in the script source
    const src = fs.readFileSync(path.join(ROOT, f), 'utf8');
    for (const m of src.matchAll(/msg = "([^"]+)";/g)) {
      // set with textContent, so read back as the browser serialises text
      const en = await p.evaluate(s => { const d = document.createElement('div'); d.textContent = JSON.parse('"' + s + '"'); return d.innerHTML.replace(/\s+/g, ' ').trim(); }, m[1]);
      if (!items.some(x => x.en === en)) items.push({ en, kind: 'chrome', where: 'quiz results message', section: 'results-camp' });
    }
    await p.close();
    const slug = f.replace(/^sherpa-tensing-|\.html$/g, '');
    const file = path.join(OUT, slug + '.json');
    const old = fs.existsSync(file) ? JSON.parse(fs.readFileSync(file, 'utf8')) : { items: [] };
    const key = x => (x.svg ? 'svg:' : '') + x.en;
    const prev = new Map(old.items.map(x => [key(x), x]));
    const merged = items.map(x => prev.has(key(x)) ? { ...x, kind: prev.get(key(x)).kind || x.kind, tr: prev.get(key(x)).tr || {} } : { ...x, tr: {} });
    fs.writeFileSync(file, JSON.stringify({ page: f, items: merged }, null, 1) + '\n');
    const count = k => merged.filter(x => x.kind === k).length;
    console.log(`${slug.padEnd(42)} ${String(merged.length).padStart(4)} items: ${count('chrome')} chrome, ${count('example')} example, ${count('?')} undecided, ${count('keep')} keep`);
  }
  await b.close();
  srv.close();
})();
