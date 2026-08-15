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
| `forbes-nature-agency-part1.html` | `NatureAgency/` (hero, lake, station, prairie) | **BUILT — 36 slides, checker clean** (`381754c`). An earlier finished rebuild of this same lesson was lost to an unpushed branch first — see the warning under Publishing in `CLAUDE.md`. |
| `forbes-nature-agency-part2.html` | `NatureAgency2/`: `hero-otter.jpg` (cover), `hide.jpg` (the hide slide), `loch.jpg` (scene-setting + results), `reeds.jpg` (dividers), `shore.jpg` (activation) | **BUILT — 59 slides, checker clean.** `build_nature2.py` + `i18n_nature2.py`. |
| `forbes-english-b2-lesson.html` | `TopGearB2/hero.jpg` | **BUILT — 37 slides, checker clean.** `lesson-template/build/build_topgear.py` + `i18n_topgear.py`. Audit at `docs/topgear-b2-audit.md`. Not yet pushed. |
| `forbes-geoscience-phrases.html` | `Geoscience/` (5 images) | **BUILT — 39 slides, checker clean.** `build_geo.py` + `i18n_geo.py`. Audit at `docs/geoscience-audit.md`. Not yet pushed. |
| `stranger-things-test.html` | `StrangerThings/hero.jpg` | **BUILT — 38 slides, checker clean, English + German + Spanish.** `build_stranger_test.py` + `i18n_stranger_test.py`. Merged the interactive test and the German worksheet; `stranger-things-test-german.html` is now a redirect stub. Not yet pushed. |

### Decisions taken on Nature Agency Part 2 (Innes, this session)

- **Artwork: a new hero is coming.** `NatureAgency2/hero.jpg` and `plain.jpg`
  are African savanna elephants; the lesson is European temperate wetland
  conservation and they depict nothing in it. Innes is supplying a
  wetland hero — otter, reed bed, river, bird hide. **Do not build the palette
  from the elephants**, and do not ship them as the cover.
- **Setting: make it British.** Rename the agency. "Federal Agency for Nature
  Conservation" is Germany's *Bundesamt für Naturschutz*, but the bylaws, the
  Wildlife Act, the licence spelling, the roundabout, the car park, the visitor
  centre, the bird hide and the yew-grove folklore are all British, as is the
  whole of Part 1. Keep the vocabulary and geography; change the name. In the
  same pass: `offense`/`offenses` → `offence`/`offences`, `bylaw` → `byelaw`.
- Everything else in the audit's priority list proceeds without further asking.

**Built.** The wetland hero arrived as `NatureAgency2/hero-otter.jpg` (otter on
a bank, reed line, open water) with `reeds.jpg` as the per-slide background for
the three section dividers and the results slide. Light theme, palette derived
with `--light`, every contrast row PASS. 59 slides, all ten gates clean.
`hide.jpg` sits behind a dedicated slide for *the hide*, the deck's
highest-risk piece of jargon, and is the only background doing teaching work.

**The agency is The Nature Agency**, in both parts and in both Supabase
titles (ids 130, 131). Part 2 briefly shipped as the "Wildlife and
Countryside Agency" while Part 1 said "The Nature Agency" and the library
cards still said "Federal Agency for Nature Conservation" — three names for
one two-part set. If you touch either part, keep the name. The Wildlife and
Countryside **Act** is real and stays; only the agency was renamed.

Two notes for whoever does Part 1:

- **The shared match engine still cannot be lost**, so Section 3 here is three
  `sort_slide` activities binned by sense rather than a `match` slide. Sorting
  scores the first placement only. Part 1 has the identical defect and the
  same workaround applies. Changing `deck.py`'s match engine is a deliberate
  decision affecting ~30 shipped lessons and was **not** made here.
- **`deck.py`'s `mc()` writes one explanation per slide**, which is what makes
  right and wrong feedback identical. `build_nature2.py` injects a per-option
  `data-explain` after calling `D.mc` rather than changing the shared builder;
  the engine already prefers an option's own explanation. If a third lesson
  needs it, promote it to an optional `explains=` argument on `D.mc`.

All palettes derived with `extract-palette.py`, every contrast row
passing.

**Standing constraint on the B2 lesson:** do not rename Clarkson,
Hammond or May in the published Stranger Gears build, and the Stranger
Gears front-page image is not to be questioned. Check whether that
lesson belongs to the Stranger Gears family before touching a name.

### Top Gear B2 — built

`forbes-english-b2-lesson.html`, 37 slides, all ten gates clean, dark
theme, palette verbatim from `extract-palette.py TopGearB2/hero.jpg`.
760 KB → 126 KB: the 714 KB base64 hero is now
`--hero: url('TopGearB2/hero.jpg')`. Clarkson, Hammond, May and the Stig
all stay; what went is the invented speech attributed to them, and the
four factual errors in the audit's C8. `library.html` has the thumbnail.
Full reasoning is in the builder docstring. Four things a later session
should not have to rediscover:

- **The match engine still cannot be lost** — third lesson in a row. The
  five matching pairs became five one-per-slide "identify the structure"
  MC items, which also cleared the 592px overflow the ten-row board
  measured. `deck.py` untouched, same call as Nature Agency.
- **This was the third lesson needing per-option `data-explain`, and it
  was still injected after `D.mc` rather than promoted to an `explains=`
  argument.** Promoting it now looks right; the cost is re-running
  `check-lesson.js` over every shipped deck to prove no regression, which
  is a job of its own and was not this build's.
- **One gap per `.gap-row`, always.** `checkGaps` marks
  `r.querySelector('.gap')` — the *first* gap in each row — while
  `maxScore` counts every `.gap` on the slide. Two inputs inside one row
  therefore create a point nobody can score. The two-error correction
  item here is two rows for exactly that reason, and it is what makes it
  worth two points.
- **`applyLang` assigns placeholders as a DOM property**, so `&rsquo;` in
  an `actPlaceholder` renders as literal `&rsquo;` once the language is
  applied — the §13 entity trap in its attribute form. Use the real
  character. Same applies to `resPerfect`/`resStrong`/`resMid`/`resLow`,
  which reach `scoreMsg` through `textContent`.

Gap tolerance (whitespace, curly apostrophe, `-ise`/`-ize`) is done at
build time in `build_topgear.py`'s `alts()` by expanding each answer into
every accepted spelling, not by changing the engine's `gapOk`. A
lesson that deliberately tests BrE against AmE spelling would be broken
by a blanket engine change; per-lesson data is not.

### The Language of Geoscience — built

`forbes-geoscience-phrases.html`, 39 slides, all ten gates clean, light
theme. `build_geo.py` + `i18n_geo.py`, English + German both complete.
Nineteen scored points, the same nineteen the old file had: six phrases
in context, six field-note gaps, seven report terms. Full reasoning is in
the builder docstring. Five things a later session should not have to
rediscover:

- **The images in `Geoscience/` are not what the audit says they are.**
  `docs/geoscience-audit.md` Part E describes `hero.jpg` as "banded
  sedimentary strata above a red plain" and approves it for the cover.
  `hero.jpg` is an **erupting stratovolcano over the sea**. The picture
  the audit is describing is `buttes.jpg` (Monument Valley). The other
  three are also volcanic: a second ash-column cone, a linear curtain of
  fire, and a banded escarpment above what its filename says is a lava
  plain. Since the lesson has zero volcanic content — that is the audit's
  own reason for banning eruption imagery — the hero here is
  `buttes.jpg`, the palette is derived from it, and the build asserts
  that none of the other four paths appears anywhere in the deck. **Look
  at an image before trusting a filename or an audit's description of
  it.**
- **The match engine still cannot be lost** — fourth lesson in a row. The
  seven pairs became seven one-per-slide "what does the term mean"
  multiple-choice items, which also gave the activity the per-item
  explanations and worked example sentences it never had. `deck.py`
  untouched, same decision as Nature Agency and Top Gear.
- **This was the fourth lesson needing per-option `data-explain`**, and it
  was still injected after `D.mc` rather than promoted to an `explains=`
  argument on `D.mc`. Four lessons is past the point where that looks
  optional; the cost is still re-running `check-lesson.js` over every
  shipped deck to prove no regression, which is a job of its own.
- **Per-item word banks trip the BANK gate once the answers are
  deranged.** The gate walks `.bank-chip` in deduplicated document order,
  so with one small bank per gap slide the answers appear in ascending
  positions no matter how each bank is shuffled — the chips of slide 2
  simply come after those of slide 1. The fix here is **one shared
  twelve-chip bank repeated on all six gap slides**: the positions are
  then fixed by the bank's own order and can be deliberately deranged
  ([7, 0, 2, 6, 1, 8]). It is also better teaching — every chip in that
  bank is defined on a language slide first.
- **`build_topgear.py`'s `assert_no_answer_is_shown` needs one change to
  work on a bank lesson.** A word bank legitimately contains the answer,
  so the bank block has to be stripped from the slide head before the
  "answer readable before it is given" check; without that the assertion
  fires on every gap slide. The placeholder half of the check is
  unchanged and still absolute: no scored input carries a placeholder at
  all.

### Stranger Things — the English test — built, and two files became one

`stranger-things-test.html`, 38 slides, all ten gates clean, dark theme,
English + German + **Spanish** all complete. `build_stranger_test.py` +
`i18n_stranger_test.py`. Twenty-eight scored points: fourteen
multiple-choice, fourteen gaps. The old `stranger-things-test-german.html`
— a printable worksheet of the same material — is retired to a
`<meta http-equiv="refresh">` stub, which the build writes and which was
verified to land on the deck. Full reasoning is in the builder docstring.
Four things a later session should not have to rediscover:

- **An L1 → English task is the one place the translation scope boundary
  has to bend.** The house rule is that the English being taught stays
  English in every language. A vocabulary section that asks "here is *der
  Herbst*, write the English" inverts that: the *prompt* is content and
  must translate, or the task does not exist for a Spanish learner. The
  prompts are i18n keys (`v1p` … `v10p`) and switch with the selector.
  **For English there is no L1**, so the English layer carries a
  definition or picture-clue instead — "the season between summer and
  winter, when the woods turn orange". Same production task, different
  route to the meaning. If another lesson needs this, copy the pattern
  rather than inventing a second one.
- **A prompt in the learner's own language can contain the answer.**
  German for a roller disco is *die Rollerdisco*, which handed the answer
  over whole. The build now resolves every prompt and hint on every gap
  slide in **every language** and checks it against every accepted
  answer; that is what caught it (the prompt is the native compound *die
  Rollschuhdisco*). `build_geo.py`'s `assert_no_answer_is_shown` only
  ever saw the English render, because that is what the builder writes.
- **`assert_no_answer_is_shown` needs to be per-slide, not per-row, once
  a slide carries two gaps.** Two rows on one slide means a clue can leak
  its *neighbour's* answer, and a row-scoped check cannot see it. The
  version here collects every answer on the slide and tests all of them
  against the whole slide's visible text.
- **The BANK gate reads the activation chips as a word bank.** It walks
  every `.bank-chip` on the page, and `D.activate` emits the target-
  language strip as `.bank-chip`. A strip listing bare headwords that
  happen to be gap answers therefore fails the gate, from a slide that
  sits *after* the results and after every gap has been marked. The fix
  is chips as phrases — `the autumn leaves`, `a rusty colour` — which is
  better production practice anyway, plus a build-time assertion
  mirroring the gate. Worth knowing before spending twenty minutes
  looking for a word bank that does not exist.

Also: **this was the fifth lesson needing per-option `data-explain`**,
and it was still injected after `D.mc` rather than promoted to an
`explains=` argument. Five is well past the point where promoting it
looks right; the cost is still a regression run of `check-lesson.js` over
every shipped deck, which is a job of its own.

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

## `--secondary` is a derived token that nothing renders

Noticed while choosing a theme for the geoscience deck: 13 of 41 shipped
decks have a `--secondary` that is invisible against their own `--surface`
(under 1.5:1), including `forbes-c1-negotiation.html`, the worked reference,
at 1.01:1, and one deck where the two values are byte-identical.

**It does not matter, and that is the point.** `var(--secondary)` appears
**zero times** in `lesson-template.html`. `extract-palette.py` derives the
token and prints it, the contrast report does not include its row, and
nothing consumes it. Thirteen decks carry an invisible colour because the
colour is never drawn.

Do not "fix" the 13, do not add a gate for it, and do not pick a theme on
the strength of that row — a light-vs-dark decision was very nearly made on
it here. Either wire `--secondary` into the template so it means something,
or drop it from `extract-palette.py`'s output. Until one of those happens,
ignore it.

## The builders imported from /tmp, and /tmp is empty in a fresh session

Committing the builders was only half the fix. **54 of them opened with
`sys.path.insert(0, '/tmp')`** and imported `deck` from there — a copy that
dies with the sandbox. Eight modules they need (`camp_diagrams`,
`camp_ten_diagram`, `cloud_diagram`, `ex_tr_sail`, `passive_diagram`,
`passive_kit`, `passive_shapes`, `sailing_map`, `trail_diagram`) existed
**only** in `/tmp` and were never committed at all.

All 54 now import from `lesson-template/build/`, and the missing modules are
in the repo. Verified the way that matters: `/tmp` was emptied and every
builder re-run — **54 reproduce their lesson from the repo alone.** The two
that do not (`build_gf.py`, `build_kool.py`) are one-shot converters that
read an already-built deck, not builders.

If you add a builder, do not point it at `/tmp`. Nothing there survives.

## Do not regenerate every deck at once

Two things bite:

- **Template drift.** Most decks were built before the `sort` slide type
  existed, so regenerating any of them pulls ~160 lines of inert sorting CSS
  and JS into the file. Harmless, but it turns a one-line fix into a
  40-file diff.
- **`sherpa-tensing-camp-one` and `camp-two` are not idempotent.** A second
  builder appends the route-timeline CSS to the already-written file without
  checking, so a repeated full build injects it twice.

Regenerate the lesson you are changing. Not the set.
