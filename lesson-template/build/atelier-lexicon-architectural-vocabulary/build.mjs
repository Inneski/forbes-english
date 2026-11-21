// Builds ../../../atelier-lexicon-architectural-vocabulary.html from source.html
// (Innes's "Atelier Lexicon" quiz, sent 2026-11-21: 30 architecture terms in five groups,
// each with its own inline SVG drawing; quiz mode, illustrated study deck, results).
// One self-contained page: Tailwind compiled here from the page's own classes, nothing
// loaded from a CDN except the two Google Fonts the page asks for itself.
//   cd lesson-template/build/atelier-lexicon-architectural-vocabulary && npm install && node build.mjs
// Then run tools/build_hubs.py and tools/seo.py from the repo root.
//
// source.html is Innes's file unchanged. The build applies exact patches (each must match
// the stated number of times, or the build stops) and writes page.build.html:
//
//   - Tailwind's CDN compiler, a development script that rebuilt the stylesheet in every
//     visitor's browser, is replaced by the same config compiled here. tailwind.config.cjs
//     is the page's own config, moved, values unchanged.
//   - Helper language (the 🌐 pill in the header): once a question is answered, on an
//     opened study card and in the results' review list, the term and the WHOLE example
//     sentence appear in the learner's language. Never before the answer: a translation
//     of the sentence or the definition would hand over the term. English is the source
//     and shows no helper line. Switching re-renders in place, so a quiz in progress
//     keeps its score.
//   - Content. Each of these would have marked a defensible answer wrong or given the
//     answer away:
//        5  "An ___ kitchen triangle": ergonomic was the only vowel-initial option in its
//           group, so the article answered the question. Now "The ergonomic kitchen
//           triangle …".
//        9  "The library features ___ floor-to-ceiling walnut joinery" took tactile,
//           unadorned and monolithic as well as bespoke. Now "The library's
//           floor-to-ceiling walnut joinery is bespoke: every shelf was made to measure
//           for the room." Only "made to measure" explains the gap.
//       10  "A ___ stone island serves as the visual anchor of the room" takes bespoke too:
//           9 is never offered as a distractor for 10 (notWith, read by
//           generateOptionsForItem).
//       19  "The visual weight of exposed brick and sleek blackened steel defines the loft"
//           is good English. "juxtaposition of exposed brick WITH sleek blackened steel"
//           leaves juxtaposition the only noun that fits.
//       25  "The oversized Persian rug softens the acoustics" is true of a rug: 27 is never
//           offered for 25.
//       26  "Maximize natural ingress" is not an English collocation. The example already
//           teaches the real one, "maximize the ingress of natural light", which is now
//           the term; the meaning follows it ("To let in as much daylight as possible.").
//       30  "The renovation blurs the boundary between heritage preservation and modern
//           livability" is good English: 29 is never offered for 30.
//   - Study deck: "Reveal All Notes" and "Quiz These (n)" filtered without the category
//     match the card grid uses, so a search for "lighting" showed six cards, said
//     "Quiz These (6)" and started a quiz of one.
//   - A "← Forbes English" link to the library: a line of its own in the footer, floating
//     bottom-left only from 1280px. Fixed at every width, it sat over the answer buttons on a
//     phone, where a tap meant for answer 3 left the quiz.
//   - Phones: the 🌐 pill drops its language code and the Menu button its word (arrow kept,
//     aria-label added), so the header's right side is no wider than the source's Menu
//     button and the brand subtitle stays on two lines. The category label on the picture
//     uses its short name and truncates; it ran under the DEFINITION / IN CONTEXT badge.
//
// Translations: i18n/<lang>.json is {"source": <hash>, "t": [[term, example], …]}, one
// pair per term in source order (ids 1-30). "source" is a hash of the English keys; when
// source.html or a patch changes an English string the hash changes and every language
// prints LEFT OUT until it is re-translated, so no language ships misaligned
// (HOUSE-STYLE rule 5: a language in the menu is complete, or it is not in the menu).
import { execFileSync } from 'node:child_process';
import { readFileSync, writeFileSync, existsSync, readdirSync } from 'node:fs';
import { createHash } from 'node:crypto';
import { createRequire } from 'node:module';
const require = createRequire(import.meta.url);

const OUT = '../../../atelier-lexicon-architectural-vocabulary.html';
// The title tools/seo.py last wrote is kept on a rebuild; TITLE is only the first one.
const TITLE = (existsSync(OUT) && (readFileSync(OUT, 'utf8').match(/<title>([^<]*)<\/title>/) || [])[1])
  || 'Atelier Lexicon — Architectural Vocabulary Quiz (C1) | Forbes English';
const DESC = 'An illustrated C1 quiz on 30 architecture terms and design phrases, from cantilevered ' +
  'to chiaroscuro, each with its own drawing, definition and example.';  // <= 155 chars: seo.py trims there
let src = readFileSync('source.html', 'utf8').replace(/\r\n/g, '\n');

// [from, to, times]
const PATCHES = [
  // Tailwind: CDN compiler and inline config out, compiled CSS in.
  [/  <!-- Tailwind CSS CDN -->\n  <script src="https:\/\/cdn\.tailwindcss\.com"><\/script>\n  <script>\n    tailwind\.config = \{[\s\S]*?\n    \};\n  <\/script>\n/,
   '  <style>/*__CSS__*/</style>\n', 1],
  [/<title>[^<]*<\/title>/, `<title>${TITLE}</title>`, 1],

  // Header: the helper-language pill beside the page's own controls.
  ['      <!-- Header Right Status / Navigation -->\n      <div id="headerControls" class="flex items-center gap-2 sm:gap-3">',
   '      <!-- Header Right Status / Navigation -->\n      <div class="flex items-center gap-2 sm:gap-3 shrink-0">\n' +
   '      <label class="fe-lang" title="Helper language"><span aria-hidden="true">🌐</span>' +
   '<span class="fe-lang-code" id="feLangCode" aria-hidden="true">EN</span>' +
   '<select id="feLangSelect" aria-label="Helper language"></select></label>\n' +
   '      <div id="headerControls" class="flex items-center gap-2 sm:gap-3">', 1],
  ['      </div>\n    </div>\n  </header>', '      </div>\n      </div>\n    </div>\n  </header>', 1],

  // A standfirst for anyone without JavaScript. tools/seo.py reads p.lede as the page's
  // description; the page renders everything else from script, so without this it got
  // the generic "An interactive C1 English lesson…" line.
  ['  <main id="appRoot" class="flex-1 max-w-5xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10">\n',
   '  <main id="appRoot" class="flex-1 max-w-5xl w-full mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-10">\n' +
   `    <noscript><p class="lede text-graphite text-sm sm:text-base leading-relaxed max-w-xl">${DESC}</p>` +
   '<p class="text-stone text-xs mt-3">The quiz needs JavaScript.</p></noscript>\n', 1],
  // The runtime, ahead of the page's own script.
  ['  <script>\n    /* ============================================================================\n       ATELIER LEXICON',
   '  <script>/*__I18N__*/</script>\n' +
   '  <script>\n    /* ============================================================================\n       ATELIER LEXICON', 1],
  // The library link: its own line in the footer; it floats bottom-left only from 1280px,
  // where the margin beside the 64rem column is wide enough that it covers nothing.
  ['  <footer class="border-t border-hairline mt-auto py-5 px-4 sm:px-6 text-center text-xs text-stone">\n',
   '  <footer class="border-t border-hairline mt-auto py-5 px-4 sm:px-6 text-center text-xs text-stone">\n' +
   '    <div class="fe-home-row"><a class="fe-home" href="/library">&larr; Forbes English</a></div>\n', 1],
  // Phones: the Menu button keeps its arrow and drops the word, so the 🌐 pill fits beside it
  // without pushing the brand's subtitle onto a third line (measured: 2 lines in the source).
  ['onclick="goHome()"\n            class="inline-flex items-center gap-1.5 text-xs sm:text-sm',
   'onclick="goHome()"\n            aria-label="Menu"\n            class="inline-flex items-center gap-1.5 text-xs sm:text-sm', 1],
  ['            <span>Menu</span>\n', '            <span class="hidden sm:inline">Menu</span>\n', 1],
  // Phones: the category label on the picture ran under the DEFINITION / IN CONTEXT badge
  // ("MATERIALS, SURFACES & CR[IN CONTEXT]" at 375px, in the source too). Short name below
  // 640px, and it truncates rather than overlap.
  ['<span class="absolute top-2.5 left-2.5 px-2.5 py-1 rounded-md bg-paper/90 backdrop-blur-sm border border-hairline text-[10px] uppercase tracking-[0.16em] text-charcoal font-semibold">\n' +
   '                  ${item.category}\n                </span>',
   '<span class="fe-cat absolute top-2.5 left-2.5 px-2.5 py-1 rounded-md bg-paper/90 backdrop-blur-sm border border-hairline text-[10px] uppercase tracking-[0.16em] text-charcoal font-semibold">\n' +
   '                  <span class="sm:hidden">${(CATEGORIES.find((c) => c.id === item.categoryId) || {}).short || item.category}</span><span class="hidden sm:inline">${item.category}</span>\n                </span>', 1],

  // Content (see the header of this file).
  ["example: 'An ergonomic kitchen triangle minimizes unnecessary movement while cooking.',",
   "example: 'The ergonomic kitchen triangle minimizes unnecessary movement while cooking.',", 1],
  ["example: 'The library features bespoke floor-to-ceiling walnut joinery.',",
   "example: \"The library's floor-to-ceiling walnut joinery is bespoke: every shelf was made to measure for the room.\",", 1],
  ["highlightText: 'monolithic',", "highlightText: 'monolithic',\n        notWith: [9],", 1],
  ["example: 'The juxtaposition of exposed brick and sleek blackened steel defines the loft.',",
   "example: 'The juxtaposition of exposed brick with sleek blackened steel defines the loft.',", 1],
  ["highlightText: 'anchors the seating area',", "highlightText: 'anchors the seating area',\n        notWith: [27],", 1],
  ["term: 'Maximize natural ingress',\n        meaning: 'To bring in as much daylight or airflow as possible.',",
   "term: 'Maximize the ingress of natural light',\n        meaning: 'To let in as much daylight as possible.',", 1],
  ["highlightText: 'strikes a balance between',", "highlightText: 'strikes a balance between',\n        notWith: [29],", 1],
  ['(v) => v.categoryId === targetItem.categoryId && v.id !== targetItem.id\n      );',
   '(v) => v.categoryId === targetItem.categoryId && v.id !== targetItem.id &&\n          !(targetItem.notWith || []).includes(v.id)\n      );', 1],

  // Study deck: the two button handlers filter the way the grid does.
  ['          item.example.toLowerCase().includes(q);\n        return matchesCat && matchesSearch;',
   '          item.example.toLowerCase().includes(q) ||\n          item.category.toLowerCase().includes(q);\n        return matchesCat && matchesSearch;', 2],

  // Helper line after the example: answered question, opened card, results review.
  ['                        <p class="text-graphite italic leading-relaxed bg-paper/90 p-3 rounded-lg border border-hairline">\n' +
   '                          &ldquo;${highlightExampleSentence(item)}&rdquo;\n                        </p>',
   '                        <p class="text-graphite italic leading-relaxed bg-paper/90 p-3 rounded-lg border border-hairline">\n' +
   '                          &ldquo;${highlightExampleSentence(item)}&rdquo;\n                        </p>\n                        ${feGloss(item)}', 1],
  ['                                    <p class="text-xs text-graphite italic leading-relaxed bg-alabaster p-2.5 rounded-lg border border-hairline/70">\n' +
   '                                      &ldquo;${highlightExampleSentence(item)}&rdquo;\n                                    </p>',
   '                                    <p class="text-xs text-graphite italic leading-relaxed bg-alabaster p-2.5 rounded-lg border border-hairline/70">\n' +
   '                                      &ldquo;${highlightExampleSentence(item)}&rdquo;\n                                    </p>\n                                    ${feGloss(item)}', 1],
  ['<p class="text-xs text-graphite italic">&ldquo;${highlightExampleSentence(item)}&rdquo;</p>',
   '<p class="text-xs text-graphite italic">&ldquo;${highlightExampleSentence(item)}&rdquo;</p>\n                            ${feGloss(item)}', 1],
];
for (const [from, to, times] of PATCHES) {
  const n = typeof from === 'string' ? src.split(from).length - 1
    : (src.match(new RegExp(from.source, 'g')) || []).length;
  if (n !== times) throw new Error(`patch matched ${n} times, expected ${times}: ${String(from).slice(0, 80)}`);
  src = typeof from === 'string' ? src.split(from).join(to) : src.replace(from, () => to);
}
writeFileSync('page.build.html', src);

// Keys: each term and its example, in source order.
const STR = String.raw`'((?:[^'\\]|\\.)*)'|"((?:[^"\\]|\\.)*)"`;
const read = (field) => [...src.matchAll(new RegExp(`\\n        ${field}: (?:${STR}),`, 'g'))]
  .map((m) => (m[1] !== undefined ? m[1].replace(/\\'/g, "'") : JSON.parse(`"${m[2]}"`)));
const terms = read('term'), examples = read('example');
if (terms.length !== 30 || examples.length !== 30) throw new Error(`read ${terms.length} terms, ${examples.length} examples; expected 30 each`);
const keys = terms.flatMap((t, i) => [t, examples[i]]);
writeFileSync('i18n/_keys.json', JSON.stringify(terms.map((t, i) => [t, examples[i]]), null, 1) + '\n');
const SOURCE = createHash('sha256').update(JSON.stringify(keys)).digest('hex').slice(0, 12);

const data = {};
for (const f of readdirSync('i18n').filter((f) => /^[a-z]{2}\.json$/.test(f)).sort()) {
  const lang = f.slice(0, 2), file = JSON.parse(readFileSync('i18n/' + f, 'utf8'));
  if (file.source !== SOURCE || !Array.isArray(file.t) || file.t.length !== 30) {
    console.log(`  ${lang}: LEFT OUT — written for source ${file.source} with ${file.t && file.t.length} pairs; now ${SOURCE} with 30. Re-translate the changed lines.`);
    continue;
  }
  const bad = file.t.map((p, i) => (!Array.isArray(p) || p.length !== 2 ||
    p.some((s) => typeof s !== 'string' || !s.trim() || s !== s.trim())) ? i + 1 : 0).filter(Boolean);
  if (bad.length) { console.log(`  ${lang}: LEFT OUT — bad pairs for terms ${bad.join(', ')}`); continue; }
  data[lang] = Object.fromEntries(file.t.flatMap((p, i) => [[terms[i], p[0]], [examples[i], p[1]]]));
}
console.log(`  source ${SOURCE} · 30 terms · helper languages: en, ${Object.keys(data).join(', ') || '(none)'}`);

execFileSync(process.execPath, [require.resolve('tailwindcss/lib/cli.js'),
  '-c', 'tailwind.config.cjs', '-i', 'input.css', '-o', 'out.css', '--minify'], { stdio: 'inherit' });
const css = readFileSync('out.css', 'utf8') + `
.fe-lang{position:relative;display:inline-flex;align-items:center;gap:5px;height:34px;padding:0 11px 0 9px;border:1px solid #E2DDD5;border-radius:9999px;background:#FCFBF8;color:#1E1E1C;font:500 12px/1 Inter,system-ui,-apple-system,sans-serif;letter-spacing:.08em;cursor:pointer;transition:border-color .15s}
.fe-lang:hover,.fe-lang:focus-within{border-color:#B85D3B}
.fe-lang select{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:pointer;font-size:16px}
@media (max-width:639.98px){.fe-lang{padding:0 9px}.fe-lang .fe-lang-code{display:none}}
.fe-home-row{display:flex;justify-content:center;margin:0 auto 12px}
.fe-home{display:inline-flex;align-items:center;padding:9px 13px;border:1px solid #E2DDD5;border-radius:10px;background:#FCFBF8;color:#1E1E1C;font:500 13px/1 Inter,system-ui,-apple-system,sans-serif;text-decoration:none;box-shadow:0 2px 6px rgba(30,30,28,.06),0 12px 30px -15px rgba(30,30,28,.1)}
.fe-home:hover{border-color:#B85D3B;color:#B85D3B}
@media (min-width:1280px){.fe-home-row{margin:0}.fe-home{position:fixed;left:12px;bottom:12px;z-index:40}}
.fe-cat{max-width:calc(100% - 7.5rem);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.fe-gloss{padding:9px 12px;border-inline-start:3px solid #4A7C59;border-radius:8px;background:#E6F0E9;color:#1E1E1C;font-size:13px;line-height:1.5;font-style:normal;text-align:start}
.fe-gloss-lang{display:block;margin-bottom:2px;color:#4A7C59;font-size:10px;font-weight:600;letter-spacing:.16em;text-transform:uppercase}
.fe-gloss-term{display:block;font-weight:600}
.fe-gloss-ex{display:block;color:#56544F;font-style:italic}
`;

const RUNTIME = `(function () {
  var DATA = ${JSON.stringify(data).replace(/</g, '\\u003c')};
  var NAMES = { en: 'English', de: 'Deutsch', es: 'Español', fr: 'Français', it: 'Italiano', pt: 'Português',
    hr: 'Hrvatski', ru: 'Русский', ar: 'العربية', zh: '中文', ja: '日本語' };
  var LANGS = ['en', 'de', 'es', 'fr', 'it', 'pt', 'hr', 'ru', 'ar', 'zh', 'ja'].filter(function (l) { return l === 'en' || DATA[l]; });
  function ok(l) { return l && LANGS.indexOf(l) >= 0 ? l : null; }
  var q = null, saved = null;
  try { q = new URLSearchParams(location.search).get('lang'); } catch (e) {}
  try { saved = localStorage.getItem('atelier-lexicon-lang'); } catch (e) {}
  var nav = (navigator.languages || [navigator.language || '']).map(function (l) { return String(l).slice(0, 2).toLowerCase(); });
  var lang = ok(q) || ok(saved) || nav.map(ok).filter(Boolean)[0] || 'en';
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  window.feGloss = function (item) {
    var d = DATA[lang], term = d && d[item.term], ex = d && d[item.example];
    if (!term || !ex) return '';
    return '<div class="fe-gloss" lang="' + lang + '" dir="auto"><span class="fe-gloss-lang">' + esc(NAMES[lang]) +
      '</span><span class="fe-gloss-term">' + esc(term) + '</span><span class="fe-gloss-ex">' + esc(ex) + '</span></div>';
  };
  var sel = document.getElementById('feLangSelect'), code = document.getElementById('feLangCode');
  function show() { document.documentElement.setAttribute('data-helper-lang', lang); if (code) code.textContent = lang.toUpperCase(); }
  show();
  if (!sel) return;
  if (LANGS.length < 2) { sel.parentNode.style.display = 'none'; return; }
  sel.innerHTML = LANGS.map(function (l) { return '<option value="' + l + '"' + (l === lang ? ' selected' : '') + '>' + NAMES[l] + '</option>'; }).join('');
  sel.addEventListener('change', function () {
    lang = ok(sel.value) || 'en';
    try { localStorage.setItem('atelier-lexicon-lang', lang); } catch (e) {}
    try { var u = new URL(location.href); u.searchParams.set('lang', lang); history.replaceState(null, '', u.toString()); } catch (e) {}
    show();
    if (typeof window.render === 'function') window.render();
  });
})();`;

let seo = '';
if (existsSync(OUT)) {
  const m = readFileSync(OUT, 'utf8').match(/<!-- SEO:start -->[\s\S]*?<!-- SEO:end -->/);
  if (m) seo = m[0];
}
let page = src.split('/*__CSS__*/').join(css.replace(/<\/style/gi, '<\\/style'))
  .split('<script>/*__I18N__*/</script>').join(`<script>${RUNTIME.replace(/<\/script/gi, '<\\/script')}</script>`);
if (seo) page = page.replace(/(<meta name="viewport"[^>]*>)/, (m) => `${m}\n${seo}`);
writeFileSync(OUT, page);
console.log('wrote', OUT, Math.round(readFileSync(OUT).length / 1024) + ' KB');
