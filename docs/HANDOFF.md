# Handoff — read this before rebuilding a lesson

This file exists because the working notes used to live only in a
claude.ai Project, which does **not** reach a Cowork sandbox. If you are
a session that was told to read `claude/lesson-queue-handoff.md` and
could not find it: this is that document. It is in git now, so any
session can read it.

**`lesson-template/HOUSE-STYLE.md` in this repo is out of date.** The
deltas are listed at the bottom of this file. Follow the deltas over the
stale copy.

---

## Open queue — artwork staged, none built

| Lesson | Artwork | State |
|---|---|---|
| `forbes-nature-agency-part1.html` | `NatureAgency/` (hero, lake, station, prairie) | **audited, see below** |
| `forbes-nature-agency-part2.html` | `NatureAgency2/` (hero, plain) | not audited |
| `forbes-english-b2-lesson.html` | `TopGearB2/hero.jpg` | not audited |
| `forbes-geoscience-phrases.html` | `Geoscience/` (5 images) | **audited, see `docs/geoscience-audit.md`** |

All palettes derived with `extract-palette.py`, every contrast row
passing.

**Standing constraint on the B2 lesson:** do not rename Clarkson,
Hammond or May in the published Stranger Gears build, and the Stranger
Gears front-page image is not to be questioned. Check whether that
lesson belongs to the Stranger Gears family before touching a name.

---

## Nature Agency Part 1 — audit

**It is not a lesson. It is a 50-item autograded assessment with no
teaching content at all.** No table, no rule box, no worked example.
Every explanatory sentence sits inside a post-answer `explanation:`
string or a pre-answer `hint:`.

- **All 17 Section 1 keys are `correct: 0`.** A runtime shuffle hides it
  live; a static deck rebuild inherits a 100% "always A" key unless the
  options are deliberately deranged.
- **Section 3 cannot be lost.** `s3Score++` fires only on a correct
  match, wrong matches carry no penalty and no attempt cap, and the exit
  gate requires all 16 matched — so every learner scores exactly 16/16.
  A third of the total is free, and 41% real accuracy reports as "Solid
  foundation".
- **Feedback is byte-identical right and wrong** on all 34 graded items;
  only the `"Correct. "` / `"Not quite. "` prefix differs. No
  per-distractor feedback field exists in the data.
- **The key is the longest option in 10 of 17** (59% against 25%
  chance); mean key 62.1 chars against 50.3 for distractors.
- **`s2q3` rejects `shoegaze` while its own explanation offers it.**
  `s2q11` rejects unhyphenated *hunky dory*. ~15 items reject natural
  alternatives.
- **`s2q2`'s hint contradicts its stem**: stem "A **small** ___", hint
  "A **large** number of people".
- Section 3's 16 items have no explanation, no feedback and no example
  sentences.
- **Question shuffling breaks four explanations** that cross-reference a
  sibling item ("Compare this with the verb sense…") — after a shuffle
  the sibling may not be adjacent or may not have been seen.
- 23 rules identified; 21 exist only in post-answer feedback and 4 are
  not in the file at all.

**Factual:** the otter decline is blamed on water quality declining "in
the 1980s". The cause was organochlorine pesticides from the late 1950s;
the 1980s are when otters began to **recover**. The intro promises
"formal and legal" vocabulary and there is not one legal item among the
fifty. `parking lot` appears in an otherwise entirely British file
(badger cull, town council, marsh harrier, hides).

Budget: 37 slides as-is, 51 with the ~14 teaching slides it needs.
`s1q1` runs 83 words with its options and must be trimmed.

### What Section 1's teaching content should cover

Section 1 looks like 17 unrelated words (*domineering, receipt,
encyclopedia, skirting, laundry…*). It isn't. **It is built as eight
polysemy contrasts** — `report`, `critic`, `decay` and `reconcile` are
each tested twice — and the section reveals each contrast only *after*
grading. Every item tests whether the learner can pick the right
**sense** of a word they already know, usually the formal, technical or
idiomatic one. Teach that, not a word list:

1. **Name the skill** before the first item.
2. **The method:** disambiguate from the collocation, the grammar (which
   preposition follows, transitive or not), and the register.
3. **The contrasts, taught as contrasts.** Two the lesson never draws
   despite putting them in adjacent items:
   - **prevalent vs rampant** — both mean widespread, but *prevalent* is
     neutral and *rampant* means bad **and** unchecked. For a
     conservation agency this is the most useful pair on the page: a
     species is *prevalent*, an invasive species is *rampant*.
   - **reconcile X with Y vs reconcile with Y** — the syntax tells you
     the sense. Reconciling field notes *with* a survey is making two
     things fit; reconciling *with* a colleague is repairing a
     relationship.
4. **Register.** Teach the formal senses these words actually carry —
   *in receipt of*, *laundering*, the *decay* of an institution — which
   is also what a field officer writing reports needs, and which would
   make good on the "formal and legal" promise.

Two ordering fixes: **`report` = the sound of a gunshot** currently
appears only as an unexplained distractor, and deserves teaching in a
lesson about a conservation agency. **`domineering` is used to define
`humble`** in a Section 1 feedback string but isn't taught until Section
3.

Caveat: the polysemy reading of *skirting*, *receipt*, *laundry* and
*encyclopedia* is inference from the words themselves; the audit only
confirmed the doubling for the four it named. Check the actual stems.

---

## Recurring defect pattern

Check for these first in anything not yet rebuilt. Every lesson audited
so far has had several:

1. The correct option is the longest — roughly half of all MCQ items.
2. Answer positions patterned: always B, never D, a perfect a-b-a-b, or
   every key at index 0.
3. Right and wrong show identical feedback, because one string is
   rendered with a different two-word prefix.
4. The rule tested exists only inside that feedback string, so it can
   only be learned by getting the item wrong.
5. A word bank listing the gap answers in gap order.
6. Items that cannot be answered from the text, or that mark correct
   English wrong.

**Learner-facing text must never mention a previous version of the
lesson.** Two decks shipped with notes like "the old version marked this
wrong" on the slide itself and had to be cleaned. That belongs in the
builder docstring and the commit message.

---

## Deltas — where `lesson-template/HOUSE-STYLE.md` is wrong

- **Rollout list.** It names five converted lessons. The real figure is
  31 of 216. Regenerate rather than trusting it: a file is a deck if it
  has both `data-type="activate"` and a `UI_I18N` block. Take slide
  counts from `check-lesson.js`'s own header line — counting
  `<section class="slide` returns N+1.
- **The checker has nine gates, not seven.** Added since: **BANK** (a
  word bank listing gap answers in gap order) and **MARKUP** (an
  explanation printing its own `<strong>` as literal text, from
  `textContent` where `innerHTML` was needed), plus **SORT**.
- **ANSWERS is a ratio *and* an absolute floor.** The key must not
  exceed the longest distractor by more than 10% *and* by at least four
  characters. The floor matters: on one-word options from a closed set
  (`can / could / must / should`), "should" beats "must" by 50% while
  carrying no information.
- **I18N no longer means "German covers English".** It means English
  plus at least one finished language. A complete Japanese with an empty
  German is a legitimate finished state.
- **There is a `sort` slide type** — labelled bins and a pool of items,
  native HTML5 drag with click-to-place as the touch fallback, one point
  per item, and a wrong placement costs that item's point.
- **Publishing.** `git push` is blocked by the proxy (403). Everything
  goes through GitHub's web uploader, **one directory per commit**:
  `/upload/main/<folder>` for images, then `/upload/main` for HTML.
  Verify byte-for-byte rather than trusting the upload — `git fetch
  origin`, compare `git hash-object <file>` against `git rev-parse
  origin/main:<file>`, then `git reset --hard origin/main`. The live
  site runs 30–60 minutes behind `origin/main`, so a stale page straight
  after a push is the host catching up.
- **Builders are in `lesson-template/build/`.** Every deck is generated;
  edit the builder and re-run, don't hand-edit the HTML. Use `deck.py`,
  don't rewrite it.
