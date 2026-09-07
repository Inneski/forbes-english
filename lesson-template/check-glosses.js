#!/usr/bin/env node
/*
 * check-glosses.js <lesson>.html — script-consistency audit for multilingual RPGs.
 *
 * The defect it measures: a gloss that carries characters from another
 * language's writing system. It happens when a translation is assembled by
 * hand and a fragment of the neighbouring language survives the edit — a
 * Cyrillic word inside the Japanese, a Chinese clause inside the Russian.
 * It is invisible in a diff of 12-language T() calls and invisible on the
 * slide unless you happen to switch to that language.
 *
 * It also flags a gloss identical to its English (never translated), an
 * empty gloss, and a scene missing a language the deck ships.
 *
 * Exit 0 = clean, 1 = findings. Run it after every translation change.
 */
const fs = require('fs');

const file = process.argv[2];
if (!file) { console.error('usage: check-glosses.js <lesson>.html'); process.exit(2); }
const src = fs.readFileSync(file, 'utf8');

// --- pull `const scenes={...}` out of the page and evaluate it with a T()
//     that keeps every language.
const langsM = src.match(/const LANGS=\[([^\]]+)\]/);
if (!langsM) { console.error('no const LANGS in ' + file); process.exit(2); }
const LANGS = langsM[1].split(',').map(s => s.trim().replace(/^'|'$/g, ''));
const ALL = ['en', ...LANGS];

const i = src.indexOf('\nconst scenes={');
const j = src.indexOf('\nconst HOT=');
if (i < 0 || j < 0) { console.error('no scenes/HOT block in ' + file); process.exit(2); }
const blk = src.slice(i, j).replace(/^\s*const scenes=/, '').trim().replace(/;$/, '');
const T = (en, ...r) => { const o = { en }; LANGS.forEach((l, k) => o[l] = r[k]); return o; };
let scenes;
try { scenes = eval('(' + blk + ')'); }
catch (e) { console.error('scenes block did not parse: ' + e.message); process.exit(2); }

// --- the writing system each language is expected to be written in.
//     `bad` are the ranges that must not appear at all; `needs` is a script
//     the string must contain at least one of (skipped for very short or
//     digit/punctuation-only strings).
const CYR = '\\u0400-\\u04FF', ARAB = '\\u0600-\\u06FF\\u0750-\\u077F';
const HAN = '\\u4E00-\\u9FFF\\u3400-\\u4DBF', KANA = '\\u3040-\\u30FF';
const HANGUL = '\\uAC00-\\uD7AF', GREEK = '\\u0370-\\u03FF', HEB = '\\u0590-\\u05FF';
const LAT = 'A-Za-z\\u00C0-\\u024F';

const RULES = {
  fr: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  it: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  pt: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  pl: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  es: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  de: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  tr: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  en: { bad: [CYR, ARAB, HAN, KANA, HANGUL, GREEK, HEB], needs: LAT },
  ru: { bad: [ARAB, HAN, KANA, HANGUL, HEB], needs: CYR },
  ar: { bad: [CYR, HAN, KANA, HANGUL, GREEK, HEB], needs: ARAB },
  zh: { bad: [CYR, ARAB, HANGUL, HEB], needs: HAN },
  ja: { bad: [CYR, ARAB, HANGUL, HEB], needs: HAN + KANA },
};
// Latin inside zh/ja/ru/ar is normal for a name or an initialism, but a long
// Latin run is a leaked fragment. Three or more Latin words in a row.
const LATIN_RUN = new RegExp('[' + LAT + ']+(?:[ \'’-][' + LAT + ']+){2,}');

const findings = [];
const walk = (node, path) => {
  if (node === null || typeof node !== 'object') return;
  if (typeof node.en === 'string') { checkT(node, path); return; }
  for (const k of Object.keys(node)) walk(node[k], path ? path + '.' + k : k);
};

function checkT(o, path) {
  for (const l of ALL) {
    if (!(l in o)) { findings.push([path, l, 'MISSING', 'no ' + l + ' gloss']); continue; }
    const s = o[l];
    if (typeof s !== 'string' || !s.trim()) { findings.push([path, l, 'EMPTY', 'blank gloss']); continue; }
    if (l !== 'en' && s.trim() === o.en.trim() && /[A-Za-z]{4}/.test(s)) {
      findings.push([path, l, 'UNTRANSLATED', 'identical to English']);
    }
    const r = RULES[l];
    if (!r) continue;
    for (const range of r.bad) {
      const m = s.match(new RegExp('[' + range + ']+'));
      if (m) findings.push([path, l, 'FOREIGN SCRIPT', 'contains "' + m[0] + '"']);
    }
    // A gloss left identical to the English is already reported as advisory
    // (BLOCULA is a proper name); do not report it a second time as script.
    const sameAsEn = l !== 'en' && s.trim() === o.en.trim();
    if (r.needs && !sameAsEn && !new RegExp('[' + r.needs + ']').test(s) && s.replace(/[\s\d\p{P}\p{S}]/gu, '').length > 0) {
      findings.push([path, l, 'WRONG SCRIPT', 'no ' + l + ' characters at all']);
    }
    if (['zh', 'ja', 'ru', 'ar'].includes(l) && LATIN_RUN.test(s)) {
      findings.push([path, l, 'LATIN RUN', 'contains "' + s.match(LATIN_RUN)[0] + '"']);
    }
  }
}

walk(scenes, '');

// --- two answer options that read identically in some language.
// The distractors differ by tense in English; a gloss that collapses two of
// them leaves that language's learner choosing between two identical lines.
for (const [id, s] of Object.entries(scenes)) {
  if (!Array.isArray(s.opts) || s.opts.length < 2) continue;
  for (const l of ALL) {
    const seen = new Map();
    s.opts.forEach((o, k) => {
      const v = (o && o[l] || '').trim().replace(/\s+/g, ' ');
      if (!v) return;
      if (seen.has(v)) findings.push([`${id}.opts[${seen.get(v)}] = opts[${k}]`, l, 'DUPLICATE OPT',
        'both read "' + v + '"']);
      else seen.set(v, k);
    });
  }
}

// LABELS too — the HUD words are learner-facing.
const lm = src.match(/const LABELS=\{[\s\S]*?\n\};/);
if (lm) { try { walk(eval('(' + lm[0].replace(/^const LABELS=/, '').replace(/;$/, '') + ')'), 'LABELS'); } catch (e) {} }

// UNTRANSLATED is advisory: a title that is a proper name (BLOCULA) and a
// French label that genuinely coincides with the English (CORRECT · +5
// POINTS) are both correct. Everything else is a defect that fails the run.
const n = Object.keys(scenes).length;
const warn = findings.filter(f => f[2] === 'UNTRANSLATED');
const errs = findings.filter(f => f[2] !== 'UNTRANSLATED');
const show = rows => rows.forEach(([p, l, kind, msg]) =>
  console.log(`  ${kind.padEnd(15)} ${l.padEnd(3)} ${p}\n${' '.repeat(20)}${msg}`));

if (warn.length) { console.log(`\n${warn.length} advisory (gloss identical to English — check each is a proper name):\n`); show(warn); }
if (!errs.length) {
  console.log(`\nPASS  ${file} — ${n} scenes, ${ALL.length} languages, no script, coverage or duplicate-option defects`);
  process.exit(0);
}
console.log(`\nFAIL  ${file} — ${errs.length} defect(s) across ${n} scenes\n`);
show(errs);
process.exit(1);
