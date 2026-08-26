#!/usr/bin/env node
/* check-library.js — verify LESSON_IMAGES in library.html.
 *
 * This exists because of a silent regression. A session uploaded a
 * library.html built from a base that predated another session's commit;
 * the web uploader replaces a file wholesale, so an unrelated entry was
 * removed. Nobody noticed, because the entry count did not change — one
 * was added as one was dropped — and because a lesson with no entry falls
 * back to a category gradient that looks like a deliberate placeholder
 * rather than a hole.
 *
 * A rule nobody measures gets skipped. A failing exit code does not.
 *
 *   node lesson-template/check-library.js            # check the working copy
 *   node lesson-template/check-library.js --vs-origin  # also diff against origin/main
 *
 * The second form is the one to run BEFORE uploading library.html: it
 * reports any entry that exists on origin and not in your copy, which is
 * exactly the clobber this file is named after.
 */
const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

const ROOT = path.resolve(__dirname, '..');
const LIB = path.join(ROOT, 'library.html');
const RED = '\x1b[31m', GRN = '\x1b[32m', YEL = '\x1b[33m', DIM = '\x1b[2m', OFF = '\x1b[0m';

function parseMap(src) {
  const m = src.match(/LESSON_IMAGES\s*=\s*\{([\s\S]*?)\n\s*\};/);
  if (!m) return null;
  const out = [];
  const re = /"([^"]+\.html)"\s*:\s*"([^"]*)"/g;
  let x;
  while ((x = re.exec(m[1]))) out.push({ lesson: x[1], image: x[2] });
  return out;
}

const src = fs.readFileSync(LIB, 'utf8');
const entries = parseMap(src);
if (!entries) { console.log(RED + 'FAIL  no LESSON_IMAGES object found' + OFF); process.exit(1); }

let fail = 0, warn = 0;
const say = (ok, label, detail) => {
  if (ok === 'warn') { warn++; console.log('  ' + YEL + 'WARN' + OFF + '  ' + label + (detail ? '\n' + detail : '')); }
  else if (ok) console.log('  ' + GRN + 'PASS' + OFF + '  ' + label);
  else { fail++; console.log('  ' + RED + 'FAIL' + OFF + '  ' + label + (detail ? '\n' + detail : '')); }
};

console.log('\n  library.html — ' + entries.length + ' thumbnail entries\n');

/* ── duplicate keys ──────────────────────────────────────────────────
   A duplicate is invisible: the object literal keeps the last value and
   the earlier line does nothing, so the map silently holds fewer entries
   than it has lines. */
const seen = new Map(), dupes = [];
for (const e of entries) {
  if (seen.has(e.lesson)) dupes.push(e.lesson + '  (' + seen.get(e.lesson) + '  vs  ' + e.image + ')');
  seen.set(e.lesson, e.image);
}
say(!dupes.length, 'no duplicate keys', dupes.map(d => '        ' + d).join('\n'));

/* ── every image exists on disk ─────────────────────────────────────── */
const missingImg = entries.filter(e => e.image && !fs.existsSync(path.join(ROOT, e.image)))
                          .map(e => e.lesson + ' -> ' + e.image);
say(!missingImg.length, 'every thumbnail file exists', missingImg.map(d => '        ' + d).join('\n'));

/* ── every key is a real lesson ─────────────────────────────────────── */
const missingLesson = [...seen.keys()].filter(l => !fs.existsSync(path.join(ROOT, l)));
say(!missingLesson.length, 'every entry points at a lesson that exists',
    missingLesson.map(d => '        ' + d).join('\n'));

/* ── every deck has an entry ─────────────────────────────────────────
   A scrolling lesson without a card is a choice. A finished 16:9 deck
   without one is an oversight — it had a hero derived for it. */
/* The template is deck-shaped by definition and is not a lesson: it has no
   hero, no Supabase row and nothing to put on a card. Excluding it here is
   the fix for a gate that had been failing on it since the day it landed. */
const NOT_A_LESSON = new Set(['lesson-template.html']);
const decks = fs.readdirSync(ROOT).filter(f =>
  f.endsWith('.html') && !NOT_A_LESSON.has(f)
  && fs.readFileSync(path.join(ROOT, f), 'utf8').includes('class="stage-wrap"'));
const deckNoCard = decks.filter(d => !seen.has(d));
say(!deckNoCard.length, decks.length + ' decks, all with a card',
    deckNoCard.map(d => '        ' + d).join('\n'));

/* ── the card should be the lesson's own hero ────────────────────────
   Advisory, not a failure: a lesson may legitimately want a different
   crop or a detail shot on its card. But a mismatch is usually a stale
   entry, so it is worth seeing. */
const mismatched = [];
for (const d of decks) {
  const img = seen.get(d);
  if (!img) continue;
  const h = fs.readFileSync(path.join(ROOT, d), 'utf8').match(/--hero:\s*url\('([^']+)'\)/);
  if (h && h[1] !== img) mismatched.push(d + '\n            card ' + img + '\n            hero ' + h[1]);
}
say(mismatched.length ? 'warn' : true, 'each deck\'s card is its own hero',
    mismatched.map(d => '        ' + d).join('\n'));

/* ── the clobber check ───────────────────────────────────────────────
   Run this before uploading. library.html is one long literal that every
   session edits, and the uploader replaces it wholesale, so an entry
   added on origin since you cloned disappears without changing anything
   you can see. */
if (process.argv.includes('--vs-origin')) {
  console.log('\n  against origin/main:\n');
  try {
    execSync('git fetch origin -q', { cwd: ROOT, stdio: 'ignore' });
    const theirs = parseMap(execSync('git show origin/main:library.html', { cwd: ROOT }).toString());
    const mine = new Map(seen);   // lesson -> image
    const lost = theirs.filter(e => !mine.has(e.lesson)).map(e => e.lesson + ' -> ' + e.image);
    say(!lost.length, 'no entry on origin is missing from this copy',
        lost.map(d => '        ' + d).join('\n') +
        (lost.length ? '\n        ^ uploading this file would delete those cards' : ''));

    /* Presence is not enough. On 2026-08-25 an IELTS upload passed the check
       above and still reverted a thumbnail: the entry was present in both
       copies, with a stale VALUE, because the local base predated the commit
       that changed it. A key that exists is not a key that matches. */
    const stale = theirs
      .filter(e => mine.has(e.lesson) && mine.get(e.lesson) !== e.image)
      .map(e => e.lesson + '\n          origin ' + e.image + '\n          yours  ' + mine.get(e.lesson));
    say(!stale.length, 'no entry on origin is silently changed by this copy',
        stale.map(d => '        ' + d).join('\n') +
        (stale.length ? '\n        ^ uploading this file would revert those thumbnails' : ''));
  } catch (e) {
    console.log('  ' + YEL + 'SKIP' + OFF + '  could not read origin/main (' + e.message.split('\n')[0] + ')');
  }
}

console.log('');
if (fail) { console.log('  ' + RED + fail + ' failure(s)' + OFF + (warn ? DIM + ', ' + warn + ' warning(s)' + OFF : '') + '\n'); process.exit(1); }
console.log('  ' + GRN + 'all checks passed' + OFF + (warn ? DIM + ' (' + warn + ' warning)' + OFF : '') + '\n');
