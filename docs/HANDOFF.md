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
| `forbes-nature-agency-part1.html` | `NatureAgency/` (hero, lake, station, prairie) | **built & live** — `build_nature1.py`, 36 slides, checker clean |
| `forbes-nature-agency-part2.html` | `NatureAgency2/` (hero, plain) | not audited |
| `forbes-english-b2-lesson.html` | `TopGearB2/hero.jpg` | not audited |
| `forbes-geoscience-phrases.html` | `Geoscience/` (5 images) | **audited, see `docs/geoscience-audit.md`** — next in the queue |
| `make-v-do.html` | `MakeVDo/` (hero, lettering) | **built** — `build_makevdo.py`, 26 slides, checker clean |

All palettes derived with `extract-palette.py`, every contrast row
passing.

**70 catalogued lessons still have no artwork at all** — no `--hero` and no
library card image. Three of them already have a folder staged and just need
wiring (`Geoscience/`, `NatureAgency2/`, `TopGearB2/`). Three pairs are the same
lesson filed twice and should be retired before anyone commissions art for
both halves. Full inventory, method and merge analysis: **`docs/HERO-QUEUE.md`**.

**Only one course exists as a course.** 213 of 239 lesson files have no
inbound link from any other lesson — Sherpa Tensing's route map is the sole
piece of course navigation on the site. Everything else is a latent course:
coherent sets with no sequencing. 78 lessons (33%) also have no CEFR level, so
they cannot be ordered even in principle. Course-by-course analysis and the
missing instalments (Emails Parts 1–2, Ordering Food Part 1, JFK Part 1,
Active/Passive Quiz Part 1): **`docs/COURSES.md`**.

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
  live. **Correction:** the claim that "a static deck rebuild inherits a
  100% 'always A' key" is wrong — `lesson-template.html` shuffles `.opt`
  children on first view, and shuffles the `sort` pool too, both on
  purpose ("so option order is never a tell"). Source-order keys are
  therefore never learner-visible in a deck either. Deranging the source
  is still worth doing — printed hand-outs, readability, insurance if the
  shuffle is ever dropped — but it is hygiene, not a defect fix, and the
  distinction matters when triaging a lesson.
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

Section 1 looks like a list of unrelated words. It isn't. **It is built
as five polysemy contrasts — ten of the seventeen items** — and the
section reveals each contrast only *after* grading. Every item tests
whether the learner can pick the right **sense** of a word they already
know, usually the formal, technical or idiomatic one. Teach that, not a
word list:

> **Corrected on the rebuild.** This section previously read "eight
> polysemy contrasts", naming `report`, `critic`, `decay` and
> `reconcile`. Those are four pairs — eight *items*, not eight
> contrasts — and there is a fifth: **`dwelled` / `dwell on` at
> Q9/Q10**, same shape, adjacent items, contrast never drawn. Ten items
> in five pairs, plus seven singles.
>
> The example words quoted here (*domineering, receipt, encyclopedia,
> skirting, laundry*) are from **Section 3**, not Section 1.

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

**Caveat resolved.** The polysemy reading of *skirting*, *receipt*,
*laundry* and *encyclopedia* was inference. The stems were checked on
the rebuild and it does **not** hold: Section 3 gives each word a single
definition, and three of the four target the plain everyday sense —
*receipt* is the slip of paper, *laundry* is the washing,
*encyclopedia* is the book. Only **`skirting`** is defined in its
less-obvious sense (the board at the foot of a wall, not the verb).
Section 3 is a flat glossary, not a polysemy set. The formal senses
(*in receipt of*, *laundering*, the *decay* of an institution) are worth
teaching, but as material added on top — they are not latent in the
items.

**Not fixed, needs a deliberate decision.** The template's `match`
engine has the same unloseable defect Section 3 had: `score++` on a
correct pair, no penalty and no cap on wrong ones. The template says so
itself, and asks for the change to be made deliberately rather than as a
side effect of one rebuild — so Part 1 routes its sorting through `sort`
slides (which do forfeit the point on a wrong first placement) and
leaves `match` alone. Roughly thirty shipped lessons would get stricter
overnight if the engine is changed; the fix is the `missed` WeakSet the
`sort` engine already uses.

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

> **Mostly applied as of `f9d75d8`.** That commit folded these corrections into
> `HOUSE-STYLE.md` itself, so the binding doc is no longer wrong and this list
> is no longer the thing to follow. Two items were checked and are *not* yet
> reflected there — the rollout figure (36 of 216) and the gate count — so
> those two still stand. The rest is kept below only as a record of what
> changed and why. Delete the section once someone has confirmed all of it
> landed.

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

---

## Emails, Calls & Follow-ups Part 3 — gap 1 repaired

`build_emails3.py`. The item read *"I am writing to ______ an appointment for
next week at your earliest convenience"*, keyed to `request`, and it was broken
twice over.

Its feedback argued against `demand` and `reserve`, **neither of which is in the
word bank**, and said nothing at all about `arrange` — the first chip in the
bank and the answer a learner actually reaches for. The bank carries ten chips
and only five are ever the answer, so `arrange` was a live decoy with no
rebuttal anywhere in the lesson. The old wording also implied `arrange an
appointment` is not standard English, which is false; it is in every learner's
dictionary. That is recurring defect 6 — marking correct English wrong.

The stem also contradicted itself: `for next week` fixes the timing while `at
your earliest convenience` hands it to the reader, and that phrase belongs to
their *reply*, not to the appointment.

Now: *"I am writing to ______ an appointment; please let me know which times
next week would suit you."* Asking them to supply the times is what makes
`request` uniquely right — it rules out `arrange` and `schedule`, which both
presume the appointment is already agreed. The feedback names those two and
`propose`, all three of which are really in the bank.

**Rejected repair, and why.** `Could we arrange a time to meet next week?` reads
well alone, but gap 3 is already *"I would like to ______ a time to speak this
week"* keyed to `schedule`, and `arrange` and `schedule` are interchangeable in
both. Two gaps each answerable with the other's key is a worse defect than the
one being fixed. When repairing a gap, check it against the other gaps sharing
its bank.

## Builders that read from /tmp

`build_pt.py` and `build_emails3.py` both did `sys.path.insert(0, '/tmp')` and
loaded their data from there, so neither could run in a fresh container — the
trap `build/README.md` describes. Both now resolve paths from `__file__`, and
`pt_data.json` was recovered out of a shipped HTML and committed beside its
builder. I then grepped the rest. **69 of the 86 builders reference `/tmp`, and these
14 read their actual content from a `/tmp` JSON that no longer exists** — so
those lessons cannot currently be regenerated from source at all:

  - `build_ai.py` &larr; `/tmp/ai.json`, `/tmp/ai_stage1.html`
  - `build_dnd2.py` &larr; `/tmp/dnd2_rooms.js`
  - `build_ff.py` &larr; `/tmp/ff_stage1.html`
  - `build_full_grammar_test.py` &larr; `/tmp/all_questions_i18n.json`, `/tmp/sections_i18n.json`, `/tmp/ui_i18n.json`
  - `build_gf.py` &larr; `/tmp/gf_stage1.html`
  - `build_hike.py` &larr; `/tmp/hike.json`, `/tmp/hike_stage1.html`
  - `build_jfk.py` &larr; `/tmp/jfk_stage1.html`
  - `build_kool.py` &larr; `/tmp/kool.json`
  - `build_pp.py` &larr; `/tmp/pp_stage1.html`
  - `build_pp2.py` &larr; `/tmp/pp_stage1.html`, `/tmp/pp_stage2.html`
  - `build_pp3.py` &larr; `/tmp/pp_stage2.html`
  - `build_ua.py` &larr; `/tmp/ua_mc.json`, `/tmp/ua_stage1.html`
  - `i18n_ff.py` &larr; `/tmp/ff_stage1.html`
  - `i18n_jfk.py` &larr; `/tmp/jfk_stage1.html`

Recovering each is the same move that worked for `pt_data.json`: the data is
still inline in the shipped HTML, so parse it back out, commit it beside its
builder, and repoint the path at `__file__`. Until that is done, treat those
lessons as hand-editable only, and do not assume re-running a builder will
reproduce what is live.

---

## Make v Do — built

`build_makevdo.py`, `MakeVDo/`, 26 slides, checker clean, stage centred to
0.0px at 390x844 / 844x390 / 1024x768 / 1440x900.

The old page was a scrolling quiz with no hero, no logo, no activation stage,
its own font stack and an invented palette. Everything scored survives — ten
gap-fills, six collocation pairs, an eight-item sort, eight phrasal verbs — but
**every rule in the lesson existed only inside post-answer feedback**, so the
one way to learn a rule was to get its item wrong. Four teaching slides now
carry the produce/perform split, the four fixed expressions that break it, and
the phrasal verbs grouped by particle instead of met one at a time in a
shuffled queue.

Source keys were all at index 0 and the sort ran make/do/make/do; deranged, but
see the correction above — the engine already shuffles both, so this was never
live in either version.

**Artwork.** The supplied image is a 3376x1440 diptych with a hard seam at
x=1688. The left panel has "MAKING. v DOING." set into it, which fights the
deck's own cover title, so the cover takes the right panel (the Mustang, clean
space for type) and the lettered panel becomes `data-bg` on the teaching
slides. Both crops are 1688x950. `--bg-opacity` is dropped to 0.34: the
template default of 0.72 assumes a photographic hero, and against flat vector
art with a metre-high wordmark in it the letterforms competed with the slide
titles and swallowed the eyebrow line.

**Content lost, and it needs an engine change.** The old page carried a German
explanation for all 24 explained items. `deck.py` writes per-item feedback into
a `data-explain` attribute and `UI_I18N` only resolves `data-i18n` keys, so
per-item feedback cannot be translated in any deck on this site. Every
converted lesson has silently dropped its non-English explanations at this
step. Worth fixing centrally — the switcher currently translates the chrome and
leaves the actual teaching in English.

## Uploading through the web uploader

The GitHub uploader's **"Commit changes" button does nothing when clicked by
element reference.** The tool reports `Clicked on element ref_N` and the form
sits there. Clicking by coordinate works. Two commits were reported as
successful and had not happened; the only reason it was caught was the
byte-for-byte hash check, which is the step that turns this from a guess into a
fact. Never skip it, and never trust the click report.

Also: `file_upload` takes **sandbox paths** (`/home/claude/...`) directly. It
rejects paths on the user's device even inside a granted folder, so staging
files across the device bridge first is wasted work.

## Full Grammar Test — merged

`full_grammar_test.html` and `full_grammar_test_italian.html` were one lesson
in two files, differing only in `let currentLang`. Now one file: starting
language from `?lang=`, default `de`; the Italian filename kept as a redirect
to `?lang=it`; the duplicate catalogue row deleted and the survivor retitled
"Full Grammar Test — 45 Questions (10 languages)". English added to the
switcher — `UI_I18N` and `SECTION_GLOSS` always carried an `en` entry that
nothing could select, and `QUESTION_I18N` has none by design, so the
per-question gloss is guarded and renders empty for English.

To restore the split if it is ever wanted:

```sql
insert into lessons (file, title, level, deck, access) values
  ('full_grammar_test_italian.html','Full Grammar Test — 45 Questions (IT support)','B1',false,'pro');
update lessons set title = 'Full Grammar Test — 45 Questions (DE support)'
  where file = 'full_grammar_test.html';
```

**Its builder was a one-shot migration script and is now a real one.** The old
`build_full_grammar_test.py` patched the pre-migration HTML into its final form
and wrote it back over the source, so a second run failed on its first assert;
it also loaded all three i18n tables from `/tmp`. Those tables are recovered and
committed (`ui_i18n.json`, `sections_i18n.json`, `all_questions_i18n.json`), the
paths are `__file__`-relative, every patch is guarded, and three consecutive
runs now produce byte-identical output. **One down, thirteen `/tmp` builders to
go.**

A trap worth knowing for the others: two of the replacements embed their own
search string inside their replacement, so an "apply if the old form is
present" guard re-wraps them on every run. Check for the *new* form first.
