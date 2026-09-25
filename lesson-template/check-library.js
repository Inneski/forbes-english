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
 *   node lesson-template/check-library.js --vs-origin --expect <lesson.html>
 *                                   # ...when you repointed that row on purpose
 *   node lesson-template/check-library.js --self-test  # prove the origin gate
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

/* ── this copy against origin, as a pure function so it can be tested ──
   theirs: origin/main's entries. mine: this copy, lesson -> image. base: the
   map at merge-base(HEAD, origin/main), or null if it cannot be read.
   expect: the lessons this session repointed ON PURPOSE (--expect).

   An entry whose value differs from origin used to fail outright. That is
   right for the two incidents this gate exists for — a stale base
   (2026-08-25) and a stale in-memory copy written back over a fresh file
   (f6be885) — and wrong for the one thing a session is supposed to do here:
   repoint a rebuilt lesson at its new hero. That differs from origin by
   definition until it is pushed, so the gate could only be passed by not
   making the change (2026-09-25, the Mixed Grammar rebuild).

   A three-way check alone cannot tell those apart: after the in-memory
   revert, base and origin agree and only this copy differs, which is
   exactly what a deliberate change looks like. So intent has to be SAID.
   A difference passes only if the session names the lesson with --expect
   AND origin still holds the base's value for it — that second half is
   what stops a declared change from overwriting a newer one on origin.
   Everything else still fails, as before. */
function againstOrigin(theirs, mine, base, expect) {
  const lost = theirs.filter(e => !mine.has(e.lesson)).map(e => e.lesson + ' -> ' + e.image);
  const differ = theirs.filter(e => mine.has(e.lesson) && mine.get(e.lesson) !== e.image);
  const ours = differ.filter(e => expect.has(e.lesson) && base !== null
                                  && base.get(e.lesson) === e.image);
  const stale = differ.filter(e => !ours.includes(e));
  return { lost, stale, ours };
}

const EXPECT = new Set();
process.argv.forEach((a, i, all) => {
  if (a === '--expect' && all[i + 1]) EXPECT.add(all[i + 1]);
  else if (a.startsWith('--expect=')) a.slice(9).split(',').forEach(l => l && EXPECT.add(l));
});

/* Measured, not trusted: every case the gate has to get right, including
   the two it was written for. Run after touching againstOrigin(). */
if (process.argv.includes('--self-test')) {
  const M = o => new Map(Object.entries(o));
  const T = o => Object.entries(o).map(([lesson, image]) => ({ lesson, image }));
  //  name                                           base      origin    mine      expect  lost stale ours
  const cases = [
    ['deliberate repoint, declared',                 {a: 'A'}, {a: 'A'}, {a: 'B'}, ['a'], 0, 0, 1],
    ['deliberate repoint, NOT declared',             {a: 'A'}, {a: 'A'}, {a: 'B'}, [],    0, 1, 0],
    ['stale base reverts origin (2026-08-25)',       {a: 'A'}, {a: 'B'}, {a: 'A'}, [],    0, 1, 0],
    ['stale base, and the session declares it',      {a: 'A'}, {a: 'B'}, {a: 'A'}, ['a'], 0, 1, 0],
    ['in-memory copy written back (f6be885)',        {a: 'B'}, {a: 'B'}, {a: 'A'}, [],    0, 1, 0],
    ['both changed it; origin moved since the base', {a: 'A'}, {a: 'B'}, {a: 'C'}, ['a'], 0, 1, 0],
    ['already in step with origin',                  {a: 'A'}, {a: 'B'}, {a: 'B'}, [],    0, 0, 0],
    ['added on origin since the base, missing here', {},       {a: 'B'}, {},       [],    1, 0, 0],
    ['no base readable: a declaration proves nothing', null,   {a: 'A'}, {a: 'B'}, ['a'], 0, 1, 0],
    ['one declared, one not: only the declared passes',
                                         {a: 'A', b: 'X'}, {a: 'A', b: 'X'}, {a: 'B', b: 'Y'}, ['a'], 0, 1, 1],
  ];
  let bad = 0;
  for (const [name, b, o, m, ex, l, s, u] of cases) {
    const r = againstOrigin(T(o), M(m), b && M(b), new Set(ex));
    const ok = r.lost.length === l && r.stale.length === s && r.ours.length === u;
    if (!ok) bad++;
    console.log('  ' + (ok ? GRN + 'ok ' : RED + 'BAD') + OFF + '  ' + name
                + (ok ? '' : '   lost/stale/ours = ' + [r.lost.length, r.stale.length, r.ours.length]
                             + ', expected ' + [l, s, u]));
  }
  console.log('\n  ' + (bad ? RED + bad + ' case(s) wrong' : GRN + cases.length + ' cases right') + OFF + '\n');
  process.exit(bad ? 1 : 0);
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
/* A leading underscore is this repo's scratch prefix — _smoke.html, a panel
   layout test, is deck-shaped and failed this gate for exactly as long as it
   sat in the root. Scratch files are gitignored too, so one can never reach
   the site; both halves of that are needed, because the gate runs against the
   working tree, not against git. */
const NOT_A_LESSON = new Set(['lesson-template.html']);
const decks = fs.readdirSync(ROOT).filter(f =>
  f.endsWith('.html') && !NOT_A_LESSON.has(f) && !f.startsWith('_')
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
    let base = null;
    try {
      const ref = execSync('git merge-base HEAD origin/main', { cwd: ROOT }).toString().trim();
      base = new Map(parseMap(execSync('git show ' + ref + ':library.html', { cwd: ROOT }).toString())
                     .map(e => [e.lesson, e.image]));
    } catch (e) { /* no common base: nothing can be declared, every difference fails */ }
    const { lost, stale, ours } = againstOrigin(theirs, mine, base, EXPECT);
    say(!lost.length, 'no entry on origin is missing from this copy',
        lost.map(d => '        ' + d).join('\n') +
        (lost.length ? '\n        ^ uploading this file would delete those cards' : ''));

    /* Presence is not enough. On 2026-08-25 an IELTS upload passed the check
       above and still reverted a thumbnail: the entry was present in both
       copies, with a stale VALUE, because the local base predated the commit
       that changed it. A key that exists is not a key that matches.
       The one sanctioned difference is a declared one; see againstOrigin(). */
    say(!stale.length, 'no entry on origin is silently changed by this copy',
        stale.map(e => '        ' + e.lesson + '\n          origin ' + e.image
                       + '\n          yours  ' + mine.get(e.lesson)
                       + (EXPECT.has(e.lesson)
                          ? '\n          declared, but origin has changed this entry since your base:'
                            + ' re-read library.html from origin and re-apply'
                          : '')).join('\n') +
        (stale.length ? '\n        ^ uploading this file would revert those thumbnails.'
                        + ' If one is a repoint you made on purpose, name it: --expect <lesson.html>' : ''));
    if (ours.length) {
      console.log(DIM + ours.map(e => '        declared: ' + e.lesson + '\n          origin '
                                      + e.image + '\n          yours  ' + mine.get(e.lesson)).join('\n') + OFF);
    }
    const unused = [...EXPECT].filter(l => !ours.some(e => e.lesson === l)
                                           && !stale.some(e => e.lesson === l));
    if (unused.length) {
      say('warn', '--expect names a lesson this copy does not change',
          unused.map(l => '        ' + l).join('\n'));
    }
  } catch (e) {
    console.log('  ' + YEL + 'SKIP' + OFF + '  could not read origin/main (' + e.message.split('\n')[0] + ')');
  }
}

console.log('');
if (fail) { console.log('  ' + RED + fail + ' failure(s)' + OFF + (warn ? DIM + ', ' + warn + ' warning(s)' + OFF : '') + '\n'); process.exit(1); }
console.log('  ' + GRN + 'all checks passed' + OFF + (warn ? DIM + ' (' + warn + ' warning)' + OFF : '') + '\n');
