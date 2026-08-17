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
| `forbes-geoscience-phrases.html` | `Geoscience/` (5 images) | **audited, see `docs/geoscience-audit.md`** |
| `forbes-english-lesson (flow).html` | `FlowState/` (hero, bg-pattern) | **BUILT — 15 slides, all 12 gates clean, 19/19 play-tested.** `build_flow.py` + `i18n_flow.py`. Catalogue row 41 corrected in Supabase. |

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

---

## Escape from Grammar Jail, and 103 junk meta descriptions

`full_grammar_test.html` (id 183) is renamed **Escape from Grammar Jail** —
Innes's wording, agreed as "Escape from" rather than "Get out the". The name is
in the catalogue, the page title, the topbar, the footer and the eyebrow in all
ten languages. The lesson NAME stays in English everywhere, the way a film
title does; only the "· All Topics" half after the separator is localised.
Translating the pun ten ways would have produced ten different lessons.

The real problem was that it had no `LESSON_IMAGES` entry, so it was one of the
66 shipping as "Coming soon" and unavailable. It now has one, and the
coming-soon count is 65.

Artwork: `grammarjail/escape-the-cliff.jpg`, cropped from the Alcatraz set Innes
sent, to the 3376x1440 shape the other three images in that folder already use.
It is the library card and it opens the results screen — you sit the test in the
exam hall (`jail-test-room.jpg`, already on the intro) and you finish on a
figure climbing out. Seven of the eight images he sent are unplaced; ask before
scattering them.

**`grammarjail/jail-cell-bars.jpg` and `jail-desk-window.jpg` are unreferenced**
— 1.2 MB of good artwork nothing points at, same defect class as the
`NatureAgency/` strays. Place them or remove them.

### `<p[^>]*>` also matches `<path>`

`seo.py`'s `describe()` falls back to "the first real paragraph" via
`<p[^>]*>(.*?)</p>`. That pattern matches **`<path>`, `<picture>`, `<pre>` and
`<progress>`**. Every page whose logo is an inline SVG opens with a `<path>`, so
the "first paragraph" ran from that path to the first genuine `</p>` much
further down and swallowed the entire header on the way.

The grammar test's Google snippet was, verbatim:

> Forbes EnglishGrammar · Full Test 0 / 45 0 / 45 ENGLISH Cheat Sheet Test ·
> Alle Themen 🇬🇧English 🇩🇪Deutsch 🇮🇹Italiano 🇪🇸…

**103 pages** were carrying a description of that shape. Fixed by requiring a
word boundary — `<p(?:\s[^>]*)?>` — and measured by capturing every description
before and after the run. Nine pages fell back to the built generic sentence
because their standfirst is not in a `<p>`; a `class="sub|subtitle|lede|
standfirst"` pattern with a lower length floor recovered two of them, and the
remaining seven now read "An interactive B1 English lesson from Forbes English:
<title>." — worse than a real sentence, far better than chrome soup. **Those
seven are worth a hand-written description each.**

### The fifth stale-base clobber — coming-soon deleted from seo.py

Ninety minutes after `8c68f2c` shipped, commit `1e485ae` ("seo.py: fetch
lessons in sort_order then id, matching sb-client.js") landed from another
session. Its stated change is four lines. Its actual diff is **+19 / −70**:
it uploaded a `seo.py` built on a base that predated the coming-soon work and
took the whole feature out with it —

- `coming_soon()` itself
- the `noindex,follow` branch in `seo_block()`
- the sitemap exclusion, the crawlable-list exclusion, the llms.txt exclusion
- the `coming_soon: true` flag in `lesson-meta.json` that the Worker reads to
  serve a gate page instead of an unfinished lesson

Live effect until it was noticed: **65 heroless, unfinished lessons back in the
sitemap, indexable, and served as if they were real.** The sitemap went from 182
URLs to 247 and nobody would have seen a thing.

Restored by starting from `8c68f2c:tools/seo.py` and applying only the genuine
`sort_order` change on top. Re-running then rewrote **0 pages** — proof the
restore is exact and not a second clobber in the other direction. The three
`describe()` fixes are in the same merged file.

**This is the fifth time.** The four earlier ones are further down this file.
The uploader route makes it easy: you upload a whole file, so any staleness in
your local copy silently reverts whatever landed while you were working.
`git fetch origin && git diff origin/main -- <file>` before every upload is the
only thing that catches it, and it takes two seconds.

### seo.py was feeding its own output back to itself

Found while fixing the above. `describe()` reads the page's existing
`<meta name="description">` as its third choice, and it was handed the raw
source — including the SEO block `seo.py` itself wrote last time. So whatever
description a page got on its first pass was frozen there permanently: rewriting
the page could never improve it. The block is now stripped before `describe()`
runs. Eleven pages picked up a correction on the first run after the fix (all
had been missing the level word, e.g. "An interactive English lesson" →
"An interactive C1 English lesson").

**Both of these were invisible.** Nothing checks meta descriptions, and the two
faults hid each other — the freeze meant the `<path>` bug's output persisted
even after a page was rewritten. A `--check` mode that flags a description
containing the site chrome ("0 / 45", a flag emoji, "ENGLISH" as a bare word)
would have caught it years earlier.

---

## IELTS: five lessons published, and the shelf now has a series

`forbes-english-ielts-*.html`, catalogue ids 245-249, all C1, all pro, all
`deck: false` — they are Innes's own scrolling pages, uploaded as-is rather than
rebuilt as 16:9 decks, which is what he asked for. Card artwork in `IELTS/`.

| File | Catalogue title |
|---|---|
| `forbes-english-ielts-academic-writing-part1.html` | IELTS Academic Writing (Part 1) |
| `forbes-english-ielts-writing-lab-part2.html` | The IELTS Writing Lab (Part 2) |
| `forbes-english-ielts-writing-studio-part3.html` | The Writing Studio (IELTS Part 3) |
| `forbes-english-ielts-maps-and-data-c1.html` | IELTS Writing Task 1: Maps & Accurate Data |
| `forbes-english-ielts-bar-charts-c1.html` | IELTS Writing Task 1: The Bar Chart |

The `IELTS` category already existed in `library.html` with no lessons in it;
it derives from `/\bielts\b/` against `title + ' ' + file`, so the filenames
alone are enough.

### The cards are placeholders cut from the lessons themselves

Innes sent no artwork, and a lesson with no `LESSON_IMAGES` entry ships as
"Coming soon" and unavailable — which would have defeated the point. Each card
is therefore a 1600x900 crop of that page's own most distinctive visual,
padded onto its own paper colour: the paragraph-flow diagram, the five-essay-
type grid, the two pie charts, the map with its compass rose. **Nothing was
invented and nothing was borrowed from another lesson.** `bar-charts.jpg` is
the exception and the best of them — that page already carried a 1400x783
base64 JPEG hero (a typewriter, books and a city skyline), extracted straight
out of the HTML. If real artwork arrives, these are one line each in
`library.html`.

### "The Liz Method" is not a phrase this site uses

Innes: *"dont say the LIZ METHOD"*. Part 1 was titled "IELTS Academic Writing,
the Liz Method" in both languages and named her in four quiz explanations; Part
3 said "Plan It — Liz's Steps" and "using Liz's own steps". All of it is gone,
en and de. The agreed replacement for the planning stage is **"The Four
Steps"** (`Die vier Schritte`), confirmed by Innes. The advice itself is
unchanged — only the attribution.

### The longest-key defect, found again in three of the five

Every one of these pages shuffles its options at render time, so key *position*
is a non-issue here. Key *length* was not. Ten questions had a key that was the
only longest option by 4+ characters:

- `maps-and-data`: `mapsMCQ` Q1, Q2, Q4 and `dataMCQ` Q1, Q2, Q3
- `bar-charts`: `MCQ` Q2, Q3, Q4, Q5 — worst was 102 characters against a
  76-character field
- `academic-writing-part1`: `c2_recap_items` Q1, Q4, Q5, in English *and*
  German
- `maps-and-data`: `dataCloze[3]`, the one cloze offender — "considerably more
  than" at 22 characters against 9, 13, 14

All fixed the house way: **distractors lengthened, keys untouched.** Two keys
were the exception and are worth knowing about:

- `mapsMCQ` Q4's key carried two claims joined by an em dash, the second of
  which duplicated the explanation verbatim. Split rather than padded — the
  explanation already said "write them in normal lower case".
- The same question's key was also the only option not starting with
  "Because". All four now match, so the grammatical tell is gone too. **Check
  option *shape*, not just option length** — a key that is the only one in a
  different grammatical form is as much of a giveaway as a long one, and no
  gate looks for it.

`dataMCQ` Q2's distractors were replaced with the genuine full band lists from
the lesson's own reference card, which fixed the length problem and taught more
at the same time.

### The paragraph-builder was printing its own answer key

Found on a second pass, after the first audit had already shipped. `renderReorder`
in Parts 1 and 2 filled each slot like this:

```js
`<span class="tag">${data.sentences[s].tag}</span>${data.sentences[st.slots[s]].text}`
```

The **tag** is the role slot `s` wants. The **text** is whatever the learner put
there. So the moment anything landed in slot 1 the slot announced "Topic",
slot 2 "Explanation", slot 3 "Example", slot 4 "Concluding" — before any
checking. Two failures at once:

1. **It hands over the key.** Drop any sentence anywhere, read the label, and
   the exercise tells you what belongs in that position. All four slots do it.
   A learner never has to judge a single sentence.
2. **It mislabels the learner's own work.** Put the concluding sentence in slot
   1 and the page tells them it is a topic sentence — on an activity whose
   entire purpose is recognising paragraph roles, at C1.

The tag is *feedback*, so it now waits for the check: nothing before, all four
roles plus correct/incorrect styling after. Verified both ways in both files.

**Look for this shape wherever a slot, bin or drop-zone renders a label from
its own index rather than from what was placed in it.** The sort slides are the
obvious next place to check.

### What the second pass actually ran

The first audit covered four defect classes — JS errors, key position, key
length, cloze-answer length — and reported the lessons as done. That was too
narrow, and the paragraph-builder defect above is what it missed. The full pass:

- **perfect play-through, driven from each lesson's own data arrays.** Maps
  20/20, Accurate Data 20/20, Bar Charts 20/20 — five each on multiple choice,
  fill-in-the-blank, sentence building and matching, so the advertised maximum
  is genuinely reachable. Parts 1 and 2: every activity to full marks
  (5/5, 5/5, 5/5, 5/5, 6/6, 5/5, 5/5, 5/5 and 10/10, 4/4, 8/8, 8/8, 5/5, 5/5).
- **advertised maximum vs reachable maximum.** All three score pills say "/ 20"
  and all three sum to 20 across their four activity arrays.
- **every cloze answer is present in its own options list** — an answer missing
  from its options is a point nobody can score. All fifteen pass.
- **no explanation prints its own markup** in any of the five, after answering
  every question.
- **Part 3 has no scoring at all**, by design. What was checked instead: word
  count and its threshold class, the countdown timer, the essay-type check, the
  five-item checklist, and the download — which produces a real 1.6 KB text
  file with the plan, the writing and the checklist in it.

### These are not deck-template lessons

`check-lesson.js` does not apply to them — no `.slide` sections, no shared
engine. What was run instead: a Playwright load of each page (no JS errors on
any; the only console noise is Google Fonts failing in the sandbox, which is
network, not code), plus two purpose-written audits that read the quiz arrays
out of the live page and check key position, key length and cloze-answer
length. Both are worth rewriting if more of these arrive.

---

## The Language of Flow (B2) — rebuilt, and two things worth keeping

`forbes-english-lesson (flow).html` was a four-part scrolling page: watch a
TED-Ed talk, click eight vocabulary cards to reveal their definitions, answer
five questions, read four discussion prompts. It is now a 15-slide deck.
`lesson-template/build/build_flow.py` + `i18n_flow.py` (en + de). Artwork
`FlowState/flow-hero.jpg` (cover) and `flow-bg-pattern.jpg` (interior).
Dark palette, all twelve gates clean, play-tested to 19/19.

What the audit found, and what the build does about it:

- **The five keys sat at positions `[1, 2, 2, 1, 2]`** — never A, never D.
  Always guess B or C and you beat chance on every item. Rebalanced to
  `[2, 3, 0, 1, 3]`. `build_flow.py` now carries `assert_keys_deranged()`,
  which fails the build if any of the four positions goes unused. **This is a
  general defect and there is no gate for it** — `check-lesson.js` checks key
  *length*, not key *position*. `football_c1_roleplay` has all eleven keys at
  index 0 and is still live. Promoting the assert to a gate is the obvious
  next move.
- Two keys were the longest option by a wide margin (Q2: 23 chars against a
  14-char field; Q5: 57 against 49). Distractors lengthened, keys untouched.
- The vocabulary was click-to-reveal, which scores nothing. Eight terms are now
  taught on two slides, matched against plain-English glosses, and used in
  eight marked gap-fills.
- The four discussion prompts are now the activation stage proper.

### A slide-level gap explanation was never once displayed

`deck.gap(..., why=...)` puts one pooled explanation on the slide instead of
one per row. `checkGaps()` only ever touched feedback found **inside** a
`.gap-row`, so the pooled note sat in the DOM with no code path to reach it:
the learner pressed Check, saw the gaps go green, and got no explanation at
all. Fixed in `lesson-template/lesson-template.html` — `markGroup()` now
returns the missed gaps rather than a boolean, and `checkGaps()` fills the
pooled note with the misses pooled across every row.

Swept every lesson in the repo. Exactly one other deck used the pattern:
`forbes-english-food-ordering-a1-part1.html`, whose `WHY_A`/`WHY_B` had never
displayed since it shipped. Rebuilt from `build_food_a1.py`, verified against a
deliberately-wrong answer, checker clean. The static regex sweep over-reports
(it flagged `english_firefighter_v3`, `forbes-gap-fill`,
`ukraine-reconstruction-lesson`); the DOM check cleared all three.

Related: `deck.teach()` emitted `data-i18n="None"` for a card whose note has no
translation key — a five-item card passes `c[3]` straight through. Guarded.

### Why the gap slides use a pooled note at all

Four rows each carrying their own `.feedback` reserve 46px apiece whether or
not anyone has pressed Check, which put both gap slides 51px past the canvas.
One pooled note per screen is what `build_food_a1` already does. If you need
per-row explanations on a four-row gap slide, it will not fit — use three rows.

### One background for the whole deck, not two alternating

The set ships two images: `flow-hero.jpg`, the full illustration, and
`flow-bg-pattern.jpg`, a deliberately murky crop of it (mean luminance 0.139
against the hero's 0.42 — a factor of three). The first build alternated them,
because `deck.py` falls back to the root `--hero` on any slide with no
`data-bg`. The result swung between a bright desert and a near-black screen
every second slide. **A slide with no `data-bg` does not get "no background" —
it gets the hero.** If a deck ships a second background image, give it to every
interior slide or to none.

Now: the cover carries the illustration (the template renders `.on-cover` at
opacity 1 regardless of `--bg-opacity`), and everything after it is the quiet
crop. `deck.activate()` gained `folder`/`bg` parameters so the activation slide
could join in; it was the only builder with no way to set a background.

`--bg-opacity` was then measured with `lesson-template/bgmeasure.py` rather than
guessed. Against the hero it was tight — 0.46 → 6.97 (fails 7:1), 0.44 → 7.32.
Against the crop there is no contest: 0.44 → 16.45, 1.0 → 14.38. Shipped at
**1.0**, which is as visible as that image can be made and still 14:1 for body
text.

### Three shipped decks were running a stale copy of the engine

`lesson-template.html` is inlined into every generated deck, so a template fix
only reaches a lesson when that lesson's builder is re-run. Re-running all of
them as a regression check on the `deck.py` change turned up three that had
drifted:

| Deck | Drift |
|---|---|
| `forbes-english-b2-lesson.html` | 395 lines |
| `forbes-nature-agency-part2.html` | 395 lines |
| `forbes-english-food-ordering-a1-part2.html` | 43 lines |

They were missing the sort-bin backdrop fix and the gap-scoring rewrite, among
others. All three were rebuilt, re-checked (37 / 59 / 16 slides, twelve gates
each) and shipped in this session. `build_food_a1` came back byte-identical,
so it was already current.

**Re-run every builder after touching `lesson-template.html` or `deck.py`**, not
just the lesson you are working on — `for f in lesson-template/build/build_*.py;
do python3 $f; done`, then `python3 tools/seo.py` to put the metadata back. It
takes under a minute and it is the only thing that catches this.
(`build_ua.py` fails on a missing `/tmp/ua_mc.json`; that is pre-existing and
unrelated — its data was never committed.)

### Supabase IS reachable — via the MCP tool, not the sandbox

`tools/seo.py` still prints *"supabase unreachable (403 Forbidden)"* and falls
back to `tools/lessons.json`. That is true of the sandbox's HTTP path only.
**The `mcp__Supabase__*` tools work.** Project `tusioporxpjtegjlqkkb`
(`forbes-english`), table `lessons`. Row 41 was updated live this session:

```sql
update lessons set title = 'The Language of Flow', deck = true, video = true
where id = 41;
```

It had been `"Flow State Lesson"`, `deck false`, `video false` — all three
wrong once it became a deck with a video. `tools/lessons.json` was mirrored to
match. **Check the catalogue row after every rebuild**: a deck that ships with
`deck: false` never appears under the deck filter, and nothing in the pipeline
catches it. Teaching `seo.py` to read Supabase through the MCP path is worth
doing.

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

## Escape from Alcatraz (A2) — built, and three new engine mechanics

`escape-from-alcatraz-a2.html`, 43 slides, 50 scored points, all ten
gates clean, dark theme, palette verbatim from `extract-palette.py
Alcatraz/hero.jpg` (every contrast row PASS). `build_alcatraz.py` +
`i18n_alcatraz.py`. **All ten languages complete** — the second deck
after `forbes-c1-negotiation.html` to carry the full set.

New in the shared engine, so every future lesson inherits them:

- **`search`** — timed identify-the-object hunt over unlabelled line
  drawings (`lesson-template/build/icons.py`, 20 objects). Names hidden
  until answered; the clock pauses on leaving a slide and resumes on
  return.
- **`lock`** — combination lock, first attempt scores, unlimited
  attempts after that so the story can finish.
- **the rail** — stops along the bottom that remember which room you are
  in and what you picked up. `D.at(slide, stop, take)` tags a slide.
  Hidden unless a lesson declares stops.

Four things a later session should not have to rediscover:

- **A background on a `display:none` slide is never fetched, and
  `page.pdf()` does not wait for the ones that print media reveals.** A
  deck printed without visiting every slide first exported black
  interiors while the screen looked correct. Fixed in the template:
  every `data-bg` is decoded at boot (`new Image().src`). This affected
  every deck with per-slide artwork, not just this one — Nature Agency
  and Top Gear are both worth re-checking.
- **`.sort-bin` now carries the card's backdrop** (`--surface` 78% plus a
  3px blur) instead of the near-transparent `--inset`. Over a bright hero
  the bins and their labels had disappeared and the board read as loose
  chips floating on artwork.
- **`deck.teach` takes an optional key for a card's *body*.** Six-item
  cards translate the body; five-item cards behave exactly as before. At
  A2 the rule itself has to be readable in the learner's language and
  only the worked examples stay English — the B2 split is wrong at this
  level. `EXAMPLE_KEYS` in `i18n_alcatraz.py` copies the English examples
  into all nine other languages so they cannot drift.
- **The wash is raised on this deck** to 0.17 / 0.36 (§5 permits it, per
  lesson, measured). Four of the twenty-three illustrations are
  cream-and-coral at full brightness. `bgmeasure.py` reads 0.046 mean
  with text at 7.58:1 — inside the dark-theme band.

The artwork is sixteen Black Isler illustrations plus a later set of
nine guard, surveillance and composite scenes; the guards carry the
final-check section, which is a nine-item mixed test with no rule on the
screen.

### Three defects in the shared builders, found by playing the deck

All three were silent — nothing threw, nothing failed a gate, and the
slides looked correct. Innes found the first two by using the lesson.

1. **`deck.order` emitted `data-action="check"`** while the engine routed
   sentence-building through `check-order`. The click landed in
   `checkGaps`, threw on a null input, and **the Check button did nothing
   on every deck generated with the shared `order()`**. Fixed in
   `deck.py`; `checkGaps` now routes a gap-less slide to the slide's own
   checker rather than throwing.
2. **`deck.gap` renders one answer per `______`, not alternatives.** A
   row written `['aren't', 'are not']` looks like two accepted spellings
   and is in fact two blanks — with one marker in the sentence, the
   second spelling is silently dropped and a correct learner is marked
   wrong. Alternatives go in one pipe-separated string:
   `["aren't|are not"]`. `deck.gap` now asserts that a row has at least
   as many markers as answers, which also catches the next one.
3. **`build_modals.py` had five "repair the sentence" items with no
   `______` at all**, so the B1 modal-verbs deck shipped a whole activity
   with no input boxes and five points nobody could score.

`assert_bank_is_not_a_key` was also failing open: with pipe-separated
answers nothing matched the bank, `all()` over an empty list is true, and
it fired on lessons that were fine. It now splits on `|` and needs two
found positions before it can fail.

**New checker gate: ACTIONS.** It walks the deck, presses what the
learner would press on every scored slide, and requires the slide to end
up marked. Verified failing first — it flagged exactly the two dead order
slides here and twelve across five shipped decks — then passing after the
fix.

Rebuilt and re-checked clean: `forbes-english-modal-verbs-B1.html`,
`forbes-english-lesson-managing energy.html`,
`forbes-english-photography-b2.html`,
`active_passive_refinery_lesson.html`, `exam-prep-5hour-courseEXP.html`.
**Run the new gate over the rest of the deck library** — a partial sweep
timed out, so most of it is still unchecked. It already found one more,
not fixed here because it needs a content decision per item:

> **`forbes-construction-contracts.html` — Activity 1, six MC slides,
> and not one option carries `data-correct`.** Every learner scores 0/6
> on it, whatever they pick, and the deck reports the result as if it
> were earned. The right answer is stated inside each item's
> `data-explain`, so the fix is to mark the matching option — but that is
> six judgements about which option the explanation means, and this is
> the light-theme benchmark file, so it deserves a careful pass rather
> than a regex. There is no builder for it; it would want one.

---

## SEO — the site had none, and now has a generator

`tools/seo.py`, run last in the pipeline (see `CLAUDE.md`). Before it: 246
pages with **no meta description, no Open Graph, no structured data**, two
canonicals, four pages titled "Lesson Library", and no sitemap. Three
structural problems mattered more than any of that:

1. **Nothing was discoverable.** `library.html` builds its list from Supabase
   in the browser, so the HTML a crawler receives had five links and 77 words.
   236 lessons sat behind it, reachable only by a URL you already knew. The
   generator writes a static list of all 236 *inside* `<div id="grid">` — the
   element the page's own script empties on start-up, so a visitor never sees
   it. When Supabase is unreachable it is also the fallback the visitor gets,
   which used to be a blank page.
2. **The gate answered 402.** Google does not index a non-2xx response, so all
   195 Pro lessons were unindexable whatever else was done. `locked()` now
   answers **200** carrying `isAccessibleForFree: false` and a `hasPart`
   marking the withheld region — Google's documented way to declare gated
   content. Same page for crawler and visitor: nothing here is cloaking.
3. **Every gate page was identical.** All 195 served the same generic
   `locked.html`. It now takes the lesson's own title, level and description
   from `lesson-meta.json` (generated by `seo.py` from the `lessons` table)
   and fills slots marked `<!-- LESSON:head -->` and `<!-- LESSON:intro -->`.

`deploy/test-paywall.mjs` was updated with it and still passes 16/16. **It now
asserts on the body, not the status** — once the gate answers 200 like a
lesson does, status alone cannot tell them apart and the bypass tests would
have passed vacuously. There is also a new case requiring the gate page to
name the lesson it is gating.

Left for a human:

- **`level` is null on 77 lessons.** It goes into the title, the description
  and `educationalLevel`, and it is what people actually search ("A2 English
  lesson"). Filling those 77 rows in Supabase is the single cheapest SEO win
  left, and `seo.py` picks it up on the next run with no code change.
- `front-page.html` and `index_1.html` are near-duplicates of `index.html`.
  They are `noindex,follow` with a canonical for now; deleting them is a
  content decision.
- The sitemap is static. Regenerate (`python3 tools/seo.py`) whenever lessons
  are added, or it goes stale.
- Nobody has verified any of this in Search Console — submit the sitemap.

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

## The SEO pass reverted a finished deck — third stale-base clobber

`c5b2bc6` ("SEO/GEO metadata — lesson pages 1/3") took
`harari_davos_c2_lesson_v2.html` from **125,615 bytes back to 66,667** — the
24-slide deck replaced by the pre-rebuild scrolling page with an SEO block
bolted on. The deck had landed forty minutes earlier in `d9154e9`.

Swept the other two SEO commits the same way; **Harari was the only casualty**:

```bash
# every .html that SHRANK by >5 KB inside a commit — a shrink means content was lost
for c in $(git log --format=%h origin/main | head -40); do
  git diff --numstat $c~1 $c -- '*.html' | while read a d f; do
    b=$(git cat-file -s $c~1:"$f" 2>/dev/null||echo 0); n=$(git cat-file -s $c:"$f" 2>/dev/null||echo 0)
    [ "$b" -gt 0 ] && [ $((b-n)) -gt 5000 ] && echo "$c $f $b -> $n"; done; done
```

**This is the same failure as the `library.html` clobber, one level worse.**
That one dropped two card entries. This one silently reverted a whole rebuilt
lesson, and it would have gone unnoticed indefinitely: the page still loaded,
still had a title, still had activities. It only surfaced because the checker
was re-run and reported four gates failing on a file nobody had touched.

Recovered by re-running `build_harari.py` — the deck came back byte-identical
(`54e443c9`), which is the argument for every deck being generated rather than
hand-edited.

**Two rules follow, and they cost nothing:**

1. **A site-wide pass must start from a fresh `git fetch` + `reset --hard
   origin/main`, not from a checkout of unknown age.** Any pass that touches
   every page — SEO, logo swaps, title rewrites — is a clobber waiting to
   happen, and the batch commits (`1/3`, `2/3`, `3/3`) mean a stale base
   damages a third of the catalogue at a time.
2. **Re-run `check-lesson.js` over every file a site-wide pass touched, not
   just the ones you meant to change.** The shrink sweep above is the cheaper
   version and catches the same thing.

### Order of operations, now that `tools/seo.py` exists

    build_<name>.py  →  check-lesson.js  →  tools/seo.py  →  upload

`seo.py` writes into the *generated* HTML, so re-running a builder strips it.
If you rebuild anything, re-run `seo.py` before uploading or the page ships
with no metadata. Running the checker again after `seo.py` is worth the two
seconds — that is what caught this.

**`seo.py` cannot reach Supabase from the sandbox** (proxy 403) and falls back
to `tools/lessons.json`. That cache is stale: it still has
`forbes-conservation-c1` at `deck: false` although the flag is now true in the
table, so `lesson-meta.json` and the deck category will lag until the cache is
refreshed from a session that can reach the database.

## Confirmed: what `seo.py` actually emits for JSON-LD

Asked for before claiming the schema win over enghub.pro. Measured across the
generated pages rather than read off the source:

| | |
|---|---|
| Root `.html` pages | 246 |
| Carrying JSON-LD | **237** |
| Parse cleanly as JSON | **all of them** |

| `@type` | count |
|---|---|
| `Organization` | 237 |
| `LearningResource` | 236 |
| `Course` (as `isPartOf`) | 236 |
| `WebPageElement` (the withheld region on Pro pages) | 195 |
| `WebSite` | 1 |
| `EducationalOrganization` | 1 |

**All 236 `LearningResource` nodes now carry `educationalLevel`.** That is only
true as of `19d9565`; before the CEFR fill, 77 of them had nothing to put there.

### The claim is right, with three holes worth naming

enghub.pro emits no JSON-LD at all, so "we are ahead on structured data" holds.
But the gap list used to make that comparison names five types, and **we are
missing three of them**:

- **`BreadcrumbList` — absent site-wide.** Cheap, and it is the one Google
  actually renders in results. Nothing else in the stack has to change.
- **`ItemList` on `library.html` — absent, and this is the worst of the three.**
  The catalogue is the most linkable page on the site, it now carries a static
  list of all 236 lessons for crawlers, and it has *no structured data at all*.
  It is one of the nine pages below with no JSON-LD.
- **`Product` / `Offer` on `pricing.html` — absent.** A paid product with no
  offer markup.

`FAQPage` is also absent, but there is no FAQ content to mark up, so that one
is not a hole — do not add it to hit a checklist.

### The nine pages with no JSON-LD, triaged

| Page | Verdict |
|---|---|
| `library.html` | **Fix.** Needs `ItemList`. |
| `pricing.html` | **Fix.** Needs `Product`/`Offer`. |
| `account.html` | Fine — private, should not be indexed. |
| `locked.html` | Fine — it is the gate template; the 195 real gate pages get theirs injected. |
| `front-page.html`, `index_1.html` | Fine — the noindex near-duplicates of `index.html`. |
| `full_grammar_test_italian.html`, `stranger-things-test-german.html` | Fine — redirect stubs. |
| `falklands-lesson.html` | Not in the `lessons` table at all. An orphan, same as the two index duplicates — catalogue it or delete it. |

### Two KNOWN LIMITS in the SEO handoff are already closed

- ~~`level` is null on 77 lessons~~ — **done** (`19d9565`). All 236 have a
  level; 75 were transcribed from their own title or filename, two resolved
  from a sibling lesson. Zero nulls in the table and in `lesson-meta.json`.
- ~~`lessons.json` cache is stale, wrong on the conservation deck flag~~ —
  **done** (`db34fbc`). Refreshed from the live table: 236 rows, zero null
  levels, deck flags current. `seo.py` still cannot reach Supabase from the
  sandbox, so the cache will drift again — refresh it whenever the table
  changes.

---

# Restored after a fourth stale-base clobber

Everything from here to the end was lost when `6fc8f3f` uploaded a
`docs/HANDOFF.md` built from a checkout that predated it — 35,224 bytes down
to 21,971, seven sections gone. Recovered from `e30f874`. Two sections
describe state that has since moved on and carry a correction at the top.

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

## The artwork was American and the lesson was British

Part 1 shipped on a bison hero with a prairie and a US ranger station behind the
teaching slides, over a lesson about a badger cull, a town council, a marsh
harrier, hides and a car park. Part 2 had already hit exactly this — its African
elephants were rejected and replaced with `hero-otter.jpg` — so it is a repeat,
not a one-off, and worth treating as a class of defect rather than a taste call.

Five replacement images are now in `NatureAgency/`, drawn from the lesson's own
content rather than from "nature" in the abstract:

| File | Picture | Where it lands |
|---|---|---|
| `hero.jpg` | marsh harrier, daylight, bird upper-left | cover, and the library card |
| `harrier-dusk.jpg` | marsh harrier, dusk silhouette, bird upper-right | the `report` teaching slide, and sort 1 |
| `peatland.jpg` | cut hags, dark water, poppies, hills | `decay`, `prevalent`/`rampant`, and 6 MC slides |
| `restoration.jpg` | hag face, tractor, cattle, a worker | "three tells", register, and the 3 odd gap slides |
| `hags.jpg` | lone tree on a hag, cottongrass fringe | `dwell`, and 6 MC slides |

Two decisions worth not re-litigating:

- **The daylight harrier is the cover, not the dusk one**, even though the dusk
  frame is the better picture. `.cover-inner` centres its text and the scrim is
  a radial at 50%/46%, so a centred title needs a clear centre. The daylight
  frame keeps its bird upper-left; the dusk frame flies straight through where
  the title goes. The dusk frame backs the `report` slide instead, which is the
  right home anyway — the harrier *is* the bird Elena has to report within 24
  hours, and that slide is where the verb sense is taught.
- **`--bg-opacity` stays at 0.40.** It was set there for the bison hero and the
  reason still holds for the new set, but it was **re-measured rather than
  carried over**: `lesson-template/bgmeasure.py` on the four background images
  gives `text_vs_brightest_bg` of 6.33–6.87 at 0.40 and **2.62–2.98 at the
  template's default 0.72** — a fail. `hags.jpg` is the worst case both ways.

**Watch out for `bgmeasure.py`'s slide index.** It indexes
`document.querySelectorAll('.slide')`, which is *not* the same sequence as
`<section class="slide` in the source — the source count is N+1, the same
off-by-one the slide-count chip has. Measuring by source index silently reads
slides that have no `data-bg` at all and returns the bare-wash number for every
one of them, which looks like a clean pass. Enumerate the indices from the DOM
first.

`lake.jpg`, `prairie.jpg` and `station.jpg` are unreferenced now but still in
the repo, because the web uploader cannot delete. `git rm` them from the first
session that has a working push.

**Nothing checks that a lesson's art matches its setting.** `check-lesson.js`
verifies the hero resolves; `docs/HERO-QUEUE.md` verifies the file exists. Both
catches so far came from reading the lesson text and looking at the picture.

## `library.html` loses card entries to stale-base overwrites

`forbes-geoscience-phrases` and `forbes-nature-agency-part1` both had a card
image, and both silently lost it. Not a gap — a regression:

```
9497eb4  Library: thumbnail for Nature Agency Part 1     <- both entries present
5066174  Merge the two Stranger Things tests             <- both entries gone
```

`5066174` did not touch either lesson. It uploaded a `library.html` built from
a base that predated them, and the web uploader replaces a file wholesale, so
two unrelated entries went with it. `LESSON_IMAGES` is a single 166-line
literal that every session edits, which makes it the most collision-prone file
in the repo — and the collision is invisible, because a missing card falls back
to a category-gradient placeholder that looks deliberate.

**Before uploading `library.html`, diff its map against origin's**, and treat
any key that disappears without a matching lesson deletion as a clobber:

```bash
ext() { git show "$1:library.html" | python3 -c "
import sys,re
m=re.search(r'const LESSON_IMAGES = \{(.*?)\n\};', sys.stdin.read(), re.S).group(1)
[print(k,'=>',v) for k,v in re.findall(r'\"([^\"]+\.html)\":\s*\"([^\"]+)\"', m)]" | sort; }
diff <(ext origin/main) <(ext HEAD)
```

The same check caught a second thing worth knowing: **the map had a duplicate
key.** `english_firefighter_v3.html` appeared at two lines with two different
images, so 167 source lines parsed to 166 entries and the earlier line did
nothing. The dead line is removed and live behaviour is unchanged — the card
still shows `Fire Brigade/fire-2-truck.png`, which is what was winning.

**But that lesson's card and its own cover now disagree**: the deck's
`--hero` is `firefighter/hero.jpg` while the card is the fire truck. Every
other entry in the map matches its lesson's hero. It is one line either way;
it was left as-is rather than changed inside an unrelated commit.

A gate for this would be cheap — parse the map, assert no duplicate keys, and
assert each value matches the lesson's own `--hero` where the lesson declares
one. Not written yet.

## library.html: run the checker, do not run a diff from memory

`node lesson-template/check-library.js --vs-origin` before you upload
`library.html`. It is not optional and it takes a second.

The clobber went **both ways** and neither session noticed:

| commit | added | silently removed |
|---|---|---|
| `5066174` | `stranger-things-test` | `forbes-nature-agency-part1` |
| `c5a9625` | Alcatraz + five decks | `stranger-things-test` |
| `0a39b5b` | restored two cards | — but not the one `c5a9625` took |

The restore commit fixed the two losses it knew about and missed the one
its own predecessor had caused. That is the shape of this failure: it is
invisible three ways over. The entry count does not change when one is
swapped for another; a lesson with no card falls back to a category
gradient that looks deliberate; and the session that clobbers is never the
session that notices.

The checker also verifies what a diff cannot: that every thumbnail file
exists, that every key is a real lesson, that no key is duplicated (a
duplicate keeps the last value, so the earlier line silently does
nothing), and that every finished deck has a card at all. Its first run
found two decks with none — `make-v-do` had never had one, and
`stranger-things-test` had been clobbered an hour earlier.

The one advisory it prints is a mismatch between a deck's card and its own
`--hero`. Two lessons differ on purpose or by accident and nobody knows
which: `english_firefighter_v3` (card `Fire Brigade/fire-2-truck.png`,
hero `firefighter/hero.jpg`) and `forbes-ai-productive-struggle-c1` (card
`AILearning/c1-lesson-thumb.jpg`, hero `AILearning/retro-desk-sunset.jpg`).
Left alone pending a decision; a deliberate detail-shot card is legitimate.

## CORRECTION: take/put support is per-item after all — and the merge is still easy

An earlier note in this file said the take/put ES and PL support was chrome
only and merged cleanly. **That was wrong, and it was wrong for an avoidable
reason.** The test used was "does any string in the JS carry Spanish or Polish
diacritics" — and most of these glosses do not. `tomar la iniciativa`,
`correr un riesgo` and `poner por escrito` are all pure ASCII. The check
reported zero and the conclusion was drawn from it.

What is actually there, counted by object key rather than by accent:

| File | Field | S1 | S2items | S3data | S4left/right |
|---|---|---|---|---|---|
| `expressions_take_put_v2.html` | `de:` | 7/7 | 18/18 | 7/7 | **0/12** |
| `expressions_take_put_ES.html` | `es:` | 7/7 | 18/18 | 7/7 | **0/12** |
| `expressions_take_put_PL.html` | `pl:` | 7/7 | 18/18 | 7/7 | **0/12** |

Two things follow.

**The "base" file is the German edition.** `expressions_take_put_v2.html` is
not language-neutral with two translations bolted on; it is DE, and ES and PL
are its siblings. Three editions, not one-plus-two.

**The merge is easy anyway, and it destroys nothing.** The support is a
*parallel field on identical item objects* — `{lbl, cat, de}` against
`{lbl, cat, es}` — so merging is `{lbl, cat, de, es, pl}` and a renderer that
picks the field by current language. This is nothing like `cheat_sheet` DE/IT,
where the divergent strings were whole example sentences. The general blocker
(`UI_I18N` cannot reach `data-explain`) does not bite here because the gloss
never goes through `data-i18n` at all — it is read straight off the item.

### Innes's decision on the promises

All three files tell the learner that translations appear after every answer.
That is true for activities 1–3 (32 items) and **false for activity 4**, the
dialogue-matching board — 12 items with no gloss in any language.

**Instruction: keep or delete all promises — no partially-kept ones. Spanish
takes priority over Polish.**

So, in the merge: add the missing activity-4 glosses so the claim is true, and
where a language cannot be completed to standard, delete that language's claim
rather than ship it half-kept. Spanish is the one to complete first; Polish is
the one to drop the claim from if something has to give.

Six expressions need a gloss (the right-hand replies are not glossed anywhere
and do not need to be — the existing pattern glosses the *expression*, not the
sentence). Spanish drafted, matching the `'x \/ y'` two-option house format
used in S1 and S3:

| id | expression | `es:` |
|---|---|---|
| L1 | put my foot in it | `meter la pata \/ decir algo inoportuno` |
| L2 | take a break | `tomar un descanso \/ hacer una pausa` |
| L3 | take the lead | `tomar la iniciativa \/ ponerse al frente` |
| L4 | put in writing | `poner por escrito \/ dejar constancia escrita` |
| L5 | put it behind you | `pasar página \/ dejarlo atrás` |
| L6 | take advantage of | `aprovechar \/ sacar partido de` |

L3 deliberately reuses the exact string already on `S2items` for *take the
lead*, so the same expression does not get two different glosses in one lesson.
Check the other five against S1/S2/S3 for the same reason before adding them.

## Queue: lessons with artwork staged

> **Updated.** Conservation Travel has since been **built and shipped** (21
> slides, `a3b7791`). Three remain: Impostor Syndrome, Contingency &
> Trade-offs, and the take/put merge. Artwork for all three is on `origin/main`.

Innes sent four URLs in quick succession. Harari is **built and pushed**. The
other three have their artwork committed and their groundwork done; none is
built. Pick them up in any order.

| Lesson | Artwork | State |
|---|---|---|
| `impostor_syndrome_lesson.html` | `Impostor2/hero.jpg` — a woman at a podium with a drink, audience in silhouette, Noma Bar treatment. **Ultra-wide (3376×1440), not 16:9** — crop or letterbox before deriving the palette. | Not audited. Note `Impostor/` is already taken by `impostor_syndrome_advanced_JP.html`, which is why the folder is `Impostor2/`. |
| `contingency-trade-offs-vocab.html` | `Construction3/`: `hero.jpg` (crane, red sun, dusk), `a.jpg` (unfinished concrete frame, palms), `b.jpg` (four-panel site strip), `c.jpg` (tower crane against cloud) | Not audited. 22 KB, the smallest of the four — likely a short vocab list rather than a full lesson. `Construction/` and `Construction2/` are both taken. |
| `expressions_take_put_v2` + `_ES` + `_PL` → one lesson | `TakePut/hero.jpg` (car on a road at dusk) | **A real merge, not a dedupe.** Innes asked for it explicitly. |
| `forbes-conservation-c1.html` | `Conservation/` (9): `reef-lagoon.jpg`, `reef-canyon.jpg`, `island.jpg`, `turtles.jpg`, `frog.jpg`, `wildfire.jpg`, `plantation.jpg`, `ama-boat.jpg`, `ama-dusk.jpg` | **Audited — see below.** Innes sent the art with no URL; it was matched to this lesson by content — the lesson is subtitled "From Cloud Forests to Coral Reefs" and runs Ecuador cloud forest → coral reef → Japan's *ama* divers, so the frog, the reef and the turtles are its own material. 60 KB, three activities, 6 MC questions. |

### The take/put merge is the awkward one

`docs/HERO-QUEUE.md` lists these under "checked and *not* doubles": 56–87 of
~150 strings shared, and **the ES and PL versions share more with each other
than either shares with the base**. So this is not the `full_grammar_test`
shape, where the only difference was chrome and the merge was free.

Worse, it runs straight into the blocker already recorded above: per-item L1
support lives in `data-explain`, which `UI_I18N` never reaches. If the ES and
PL support is per-item rather than chrome, merging destroys the thing that
makes the second and third files worth having — exactly the reason
`cheat_sheet` DE/IT was left alone.

**Diff the three before building anything.** If the support is per-item, the
per-item translation fix has to come first, and that is a `deck.py` change
affecting every shipped deck rather than a one-lesson job. Innes has asked for
the merge, so if it turns out to be blocked, say so and say why rather than
shipping a merge that silently drops the Spanish and Polish.

### Two process notes from this batch

**Never `git reset --hard` while staged artwork is untracked.** A
`git stash -u && git reset --hard && git stash pop` sequence in this session
silently lost four artwork folders — the stash did not survive — and reverted a
finished deck to its pre-rebuild state. Both were recoverable only because the
source PNGs were still in the uploads directory and the commit was still in the
reflog. Commit artwork as soon as it is staged.

**The uploader's "Commit changes" click fails silently more often than the
existing note suggests.** Two of four commits in this batch did not land, and
the page looked identical either way. The hash check is not optional, and it
must cover *every* file in the batch — `check-library.js --vs-origin` caught
that a `library.html` about to be uploaded would have wiped two cards another
session had added forty minutes earlier.

### ~~The take/put merge is NOT blocked after all~~ — SUPERSEDED, THIS WAS WRONG

> **Do not act on this section.** It claimed the ES and PL support was chrome
> only. It is not: all three files carry 32 per-item glosses each. The error and
> the real picture are in **"CORRECTION: take/put support is per-item after
> all"** at the end of this file. The paragraph below is kept only so the
> mistake is legible, because the *method* that produced it — testing for
> diacritics rather than counting object keys — is the reusable lesson.

~~Every Spanish-bearing text node in `expressions_take_put_ES.html` is chrome —
headings, task instructions, button labels, the section intros. There is no
`data-explain`, and no Spanish or Polish anywhere in the JS data.~~

The one part of this section that held up: **both files promise something they
do not fully contain.** The ES page says *"Las traducciones al español aparecen
en rojo después de cada respuesta"* and the PL page says the same in Polish.
True for activities 1–3, false for activity 4. Same class of defect as the
Harari transcript claim — a checkable promise the file does not keep.

### Artwork is committed the moment it is staged

Learned the hard way this session — see the `reset --hard` note above. Every
folder in the queue table is already on `origin/main`, so the next session
starts with the art in hand and nothing depends on a sandbox surviving.

## Conservation Travel C1 — audited, and now built

> **Built and shipped** as a 21-slide deck (`a3b7791`), all twelve gates clean.
> Every defect below was fixed; the audit is kept because the defects are the
> reusable part.

`forbes-conservation-c1.html`, 60 KB, three activities: 6 MC, 6 gap-fill, 5
sentence-ordering, plus discussion prompts. Artwork is in `Conservation/`
(nine images, listed in the queue table).

**The word bank is the answer key, in order.** Not correlated with it — the
same list:

```
bank    : rare  retraining  traditional  millennia  Cultural  extinction
answers : rare  retraining  traditional  millennia  Cultural  extinction
```

A learner reads the bank top to bottom, fills the gaps top to bottom, and
scores 6/6 without reading a single sentence. This is the most blatant
instance of the `assert_bank_is_not_a_key` defect in the catalogue — every
previous case was a bank that merely leaked the order; this one *is* the key.
Fix by sorting the bank, which is what the guard wants and what
`build_nature1.py` does.

`Cultural` is capitalised in the bank, which separately tells the learner that
gap begins a sentence. Sorting alone does not fix that; either lower-case it in
the bank or move the gap off a sentence boundary.

**The MC keys run 1 1 1 2 1 1** — five of six on index 1 — and **the key is the
longest option in 3 of 6** (up to +12 chars). Same pair of tells as Harari,
milder. Derange the keys and lengthen the three distractors; do not shorten a
key.

The ordering activity was not measured — check whether it can be lost before
trusting it, since the `match` engine's equivalent could not be.

The reading itself is good and should survive: Ecuador cloud forest, coral reef
restoration, Japan's *ama* divers. That last is what the `ama-boat.jpg` and
`ama-dusk.jpg` frames are for, and the lesson names the tradition explicitly,
so those two backgrounds do teaching work rather than decoration.

---

## The fourth clobber, and the hole in the check I was using

`6fc8f3f` took `docs/HANDOFF.md` from **35,224 bytes to 21,971** and dropped
seven sections. Same cause as the other three: a file uploaded from a checkout
that predated the work it overwrote.

This one is worth more attention than the others, because **the file it
destroyed is the one whose entire job is to survive between sessions.** Losing
a card entry costs a thumbnail. Losing a deck costs a rebuild. Losing the
handoff costs every session after it the reason anything was done.

### The check I was running does not catch this

Before uploading `HANDOFF.md` I had been running:

```python
mine.startswith(open(origin_version).read())   # "am I a clean superset of origin?"
```

That answers *"am I about to clobber origin?"* It does **not** answer *"has
origin already lost work of mine?"* — and after `6fc8f3f`, origin was the
clobbered version, so my append passed the check and quietly built on top of
the damage. I appended twice more before noticing.

**The check has to be against the last version known to contain your work, not
against whatever origin happens to be now:**

```bash
# every ## section that existed in <known-good> and is missing from the file now
python3 - <<'EOF'
import re, subprocess
def secs(t): return {p.split('\n')[0].strip(): p
                     for p in re.split(r'(?m)^(?=## )', t) if p.startswith('## ')}
old = secs(subprocess.run(['git','show','<known-good-sha>:docs/HANDOFF.md'],
                          capture_output=True, text=True).stdout)
new = secs(open('docs/HANDOFF.md', encoding='utf-8').read())
for k in old:
    if k not in new: print('LOST', k)
EOF
```

The byte-size trend is the cheap version of the same signal: **`HANDOFF.md`
should only ever grow.** Any commit where it shrinks is a clobber until proven
otherwise. Same rule as the deck shrink-sweep, applied to the one file that
cannot be regenerated from a builder.

### Four instances now, all the same shape

| Commit | What it overwrote | Cost |
|---|---|---|
| `5066174` | two `library.html` card entries | thumbnails |
| `a3b7791` | an SEO block in `library.html` (mine) | metadata, self-repaired by luck |
| `c5b2bc6` | the Harari deck, 125,615 → 66,667 bytes | a full rebuild |
| `6fc8f3f` | `HANDOFF.md`, 35,224 → 21,971 bytes | seven sections of institutional memory |

Two of those four were mine. The pattern is not carelessness by one session —
it is that **the web uploader replaces files wholesale and nothing in the loop
compares against what was there.** Until `git push` works, the diff before
upload is the only defence, and it has to be run against the right baseline.

## The longest-key defect, swept and cleared

Measured across all 41 decks, then fixed. **Every deck now passes the ANSWERS
gate.**

| Deck | Was | Fix |
|---|---|---|
| `forbes-c1-negotiation` | 10 of 12 items | 10 distractors rewritten |
| `football_c1_roleplay` | 10 of 11 items | 10 distractors rewritten |
| `stranger-gears-rpg` | 2 items | 2 distractors extended |
| `forbes_english_lesson` | word bank in gap order | bank sorted |

### None of these had a builder — which is why editing the HTML was correct

`forbes-c1-negotiation`, `football_c1_roleplay` and `forbes_english_lesson`
predate the generator. `CLAUDE.md`'s rule that hand-editing generated HTML "works
once and is then overwritten" applies to files a builder can regenerate. These
have none, so the edit is permanent. `build_stranger.py` exists but outputs
`stranger-things-b1-lesson.html`, not `stranger-gears-rpg.html`.

If anyone later writes builders for these four, the distractor text must be
carried across or the defect returns.

### Padding was the wrong fix on two of them, and why

**`forbes-c1-negotiation` teaches formal contract register.** Six of its items
ask "which is the most formal version", and formal contract English is
genuinely wordier than plain English — so length was *correlated with the
answer*, not accidentally attached to it. Padding a distractor with more formal
language would have produced a second plausible key.

Each rewritten distractor is instead made long by becoming **more
conversational** — hedges, filler, first-person commentary, vague quantifiers.
It ends up as long as the key and more obviously wrong on register. That is a
better item than the one it replaced: the learner now judges register instead
of counting words.

**`stranger-gears-rpg`'s two items test verb form** (`must have opened` against
`must opened`). The distractors were extended by completing their noun phrase to
match the key — `below it` → `below the chamber` — so the only remaining
difference is the verb form, which is the thing being tested. The error itself
is untouched. Note those strings appear **ten times each** in that file; all ten
were replaced, or the copies drift apart.

### `football_c1_roleplay` has a second defect, not fixed

**All 11 keys sit at index 0.** The template shuffles `.opt` children on first
view so it is not learner-visible — the same situation as Nature Agency's
all-zero keys, hygiene rather than a live fault. Deranging it means reordering
whole `<button>` blocks by hand in a file with no builder. Worth doing, not done.

### `stranger-gears-rpg` still fails three structural gates

No `activate` slide, no `UI_I18N`, no `.fe-logo`. It is a pre-house-style page,
not a scoring problem, and bringing it up to standard is a rebuild. **It carries
the standing Stranger Gears constraints** — Clarkson, Hammond and May keep their
names and the front-page image is not up for discussion — so that rebuild is a
deliberate decision, not a tidy-up.

### The screening sweep over-reports — use `check-lesson.js` to decide

A static regex sweep is useful for finding candidates across 41 decks quickly,
but it disagreed with the checker on seven items, in two ways, both mine:

1. **It used only the 4-char floor.** The real rule in `check-lesson.js` is
   `key > maxOther * 1.10 && key - maxOther >= 4` — a **ratio and** a floor. The
   comment there explains why: in a closed option set of modals, "should" beats
   "must" by 50% while carrying no information.
2. **It mis-parses options carrying a `data-explain` attribute**, pulling the
   explanation text into the option and inflating the length. That is what made
   `forbes-english-lesson (2)` look like a 1.38x offender when it passes.

Screen with the sweep; decide with the checker, which reads a real DOM.

## Recolouring a deck: Breaking Bad, orange to pink

Innes: *"give this same treatment of font and pink tones instead of orange."*
`breaking-bad-present-continuous-deck-viewer.html`, 16 slides, A2, deck, pro,
catalogue id 244.

**Measure both palettes before writing the transform.** Breaking Bad's warm sat
at hue 0-20, S 0.5-0.6; the Harry Potter pink at hue 340-350, S 0.3-0.4.

**Rotate the hue. Do not touch saturation or value.** The first attempt did all
three — 22 degrees, minus 28% saturation, plus 2% value — and Innes came back
with *"the pink has overpowered subtle neighbouring tones."* He was right, and
it is measurable: multiplicative desaturation compresses the *absolute* gap
between tones, so the saturation spread of the warm family fell by roughly half
on every slide. The coral wall, the terracotta recesses, the skin and the dusty
rose all converged on one flat pink.

| | slide 1 | slide 7 | slide 11 | slide 13 |
|---|---|---|---|---|
| original spread | 0.122 | 0.378 | 0.121 | 0.107 |
| v1 (rot + desat) | 0.061 | 0.225 | 0.079 | 0.075 |
| **v2 (rot only)** | **0.109** | **0.349** | **0.108** | **0.099** |

A pure hue rotation preserves S and V per pixel, so every tonal difference in
the original survives and only the hue moves.

### Then he asked for much less saturated — SUBTRACT, do not multiply

Those two requests are only in tension if you desaturate the wrong way:

```
s * 0.72    multiplies: a 0.12 gap between two tones becomes 0.086.
            The tones converge, the picture goes flat. This was v1.
s - 0.15    subtracts: a 0.12 gap stays 0.12. Every tone drops by the same
            amount and the separation between them is untouched.
```

Final settings: rotate 20 degrees, subtract 0.15 from saturation with a soft
floor at 0.06 so the palest washes cannot clip to grey, leave value alone.
Median saturation of the warm family falls from 0.50 to about 0.36 while the
spread survives. `#F27D6B` ends up `#F28FA3`.

**The general rule: to change how saturated something looks, subtract. To
change the relationship between tones — which is almost never what you
want — multiply.**

**Keep the band tight so the neighbours survive.** v1 ramped out at +35, which
dragged the tans and terracotta (hue 20-40) into the pink along with everything
else and left nothing for it to sit against. v2 is at full strength only from
-8 to +12 and back to zero by +24. Blues, greys and blacks never enter the
band either way. Applied to all 14 media images **and** to `srgbClr` values in
the XML — `#F27D6B` (26 uses) becomes `#F2738C`.

### Slide 2 was the only one with no artwork

Every text box on it stopped by x=1530 of 1920, so the right third was empty,
and the three column boxes behind SUBJECT / AM-IS-ARE / VERB+ING existed with
no fill, so the table read as three floating words. Gave the boxes a 16% tint
of the deck pink with a 9% corner radius, and put a tall crop of the Jessie
picture — the same media part slide 4 uses, a second relationship to it — in
the empty third. **A tall panel needs `srcRect`, not a squash**: the panel is
320x1080 (aspect 0.30) and the source is 1600x900, so the crop has to be about
17% of the source width or the picture comes out at half width.

### Recolouring changes contrast, so re-measure the text afterwards

Pink is lighter than the coral it replaced, so every cream or pink caption lost
contrast against it. A sweep of all 16 slides found three text blocks that were
invisible in the render:

| Slide | Text | Orange | Pink | Fixed to |
|---|---|---|---|---|
| 8 | "Where are they standing?" | 1.20:1 | **1.01:1** | `#10272B` → 7.2:1 |
| 13 | "Gustav is adjusting his tie" | 2.86:1 | 2.35:1 | `#10272B` → 6.3:1 |
| 16 | "SUBJECT + BE + VERB-ING" | 1.01:1 | 1.01:1 | `#FFF8E8` → 14.6:1 |

Two of those the recolour made worse; slide 16 was already broken. All three
were fixed with colours the deck already uses.

**The per-block sweep over-reports.** Sampling the median inside a text box
includes the glyphs and any second background the box overlaps, so a wide box
spanning two tones scores low even when the text is perfectly legible — it
flagged 21 blocks and only 3 were real. Use it to shortlist, then crop and look
at each one.

### "All Courier New" needed the theme changing too

The deck named Courier New on 43 runs and left 16 inheriting, and the theme's
`majorFont`/`minorFont` were **Calibri** — so `pdffonts` showed a
LiberationSans alongside the two Courier faces. Setting the theme to Courier
New *and* giving those 16 runs an explicit face cleared it. `pdffonts` is again
the check: two Courier entries and nothing else.

---

## The four presentation decks: top of the shelf, and a maximise mode

`star-wars`, `twin-peaks`, `breaking-bad`, `harry-potter` — the four decks
built from a `.pptx` behind `*-deck-viewer.html`. Innes: *"the only true
presentation decks, should be at top of list."*

`library.html` now sorts into three bands, derived from the filename like
every other state there, so a fifth deck lands in the right band on its own:

```js
const band = l => comingSoon(l) ? 2 : (/-deck-viewer\.html$/.test(l.file) ? 0 : 1);
```

### Mobile: `vh` is the bug, `dvh` is the fix

*"When I try to open any lesson on mobile must switch to landscape and address
bar sticks."* Three separate things, worth keeping straight:

1. **`vh` is the LARGEST viewport** — the one with the mobile address bar
   hidden. Size a box `100vh` with the bar showing and its bottom runs off the
   screen, taking the footer with it. That is the "address bar sticks" symptom.
   **`dvh` tracks the bar as it moves.** Every `vh` in the four viewers now has
   a `dvh` twin written after it: browsers that understand `dvh` take the
   second line, older ones keep the first.
2. **The green sandwich costs ~130px** of a landscape phone's ~390px — a third
   of the screen. A `Maximise` control now hides header and footer.
3. **Landscape** cannot be forced. `screen.orientation.lock('landscape')` only
   works inside fullscreen and only on Android/Chrome; iOS has no equivalent.
   It is called in a try/catch and the user turns the phone if it does not
   take.

Measured on a 844x390 landscape phone viewport, slide area after maximise:
**+62%** on three of them, **+103%** on Star Wars.

**iPhone Safari has no `Element.requestFullscreen`.** It is feature-detected,
and the button is still worth having there: it reclaims the chrome and `dvh`
handles the bar. Never assume fullscreen exists.

**Two viewer shapes, both need covering.** Three viewers cap the `<img>` with
`max-height:calc(100vh - 130px)`; **Star Wars sizes the `.slide-wrap`** with
`height:calc(100vh - 130px)` plus an `aspect-ratio` and lets the image fill it.
A first pass only rewrote `max-height` rules and Star Wars gained **0%** — it
measured as fixed while the other three moved. If you touch this again, check
all four, and check the number, not the diff.

---

## Publishing a .pptx: the slide-viewer pattern

Innes sends a finished PowerPoint and says "upload to decks". There is no
`decks/` folder — the established shape, set by `twin-peaks-deck-viewer.html`
and `star-wars-question-words-deck-viewer.html`, is four artefacts:

```
<name>.pptx                       the source, at the repo root, for download
<name>-slides/slide-01.jpg …      one 1920x1080 render per slide
<name>-deck-viewer.html           the page: one <img>, arrows, dots, download
catalogue row + LESSON_IMAGES     deck=true, thumbnail = slide-01
```

Rendering:

```bash
python3 <pptx-skill>/scripts/office/soffice.py --headless --convert-to pdf deck.pptx
pdftoppm -jpeg -jpegopt quality=88 -r 144 deck.pdf slide     # gives 1921px — resize
```

`pdftoppm` at 144dpi returns **1921x1080**, one pixel wide. Resize to exactly
1920x1080 before committing or the images are subtly non-standard. JPEG q86
progressive lands each slide at 200-400KB; the twin-peaks PNGs average 1.4MB
each for no visible gain, so use JPEG.

### CHECK THE FONT BEFORE YOU PUBLISH — `pdffonts`, every time

The first render of this deck went out in the wrong typeface and Innes spotted
it. The deck asks for **Courier New**, which is not installed here.
Fontconfig resolves it to **Liberation Mono**, which is *metric-compatible* —
so nothing overflows, nothing shifts, every QA check passes — and looks nothing
like Courier: a neutral grotesque with none of the typewriter slabs. A
substituted font is invisible to every check we run. The only reliable tell:

```bash
pdffonts deck.pdf     # BAAAAA+LiberationMono-Bold  <- wrong
                      # BAAAAA+CourierNew-Bold      <- right
```

**Fontconfig alone cannot fix it.** LibreOffice consults its own substitution
table first and that table maps Courier New to Liberation Mono; a
`<match target="pattern">` rule for the family never gets a look in. Two things
that also do not work: `ttf-mscorefonts-installer` (its postinst fetches from
SourceForge and fails in this sandbox), and pointing at "Nimbus Mono PS"
by name in a fontconfig alias.

What works is giving LibreOffice an exact family-name match. Nimbus Mono PS is
URW's clone of Adobe Courier — the face Courier New was itself drawn from — so
install it under the name it is standing in for:

```python
from fontTools.ttLib import TTFont
f = TTFont('/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf')
for rec in f['name'].names:
    if rec.nameID in (1, 16): rec.string = 'Courier New'
    elif rec.nameID == 4:     rec.string = 'Courier New Bold'
    elif rec.nameID == 6:     rec.string = 'CourierNew-Bold'
f.save('/usr/share/fonts/opentype/couriersub/CourierNew-Bold.otf')   # then fc-cache -f
```

Do all four styles. This is a **render-time substitution inside the sandbox** —
no font ships, and the container is rebuilt every session, so **this has to be
redone every time a deck using Courier New is rendered.** The same trap waits
for any deck naming a font Office ships and Linux does not: Calibri, Cambria,
Aptos. `pdffonts` is the check.

**The `LESSON_IMAGES` entry is not optional any more** — without it the lesson
renders as "Coming soon" and is excluded from the sitemap. Point it at
`slide-01.jpg`.

### Harry Potter and the Present Continuous — uploaded, with one fix

`harry-potter-present-continuous-deck-viewer.html`, 10 slides, A1, deck, pro,
catalogue id 243. Eight verbs — talk, tell, discuss, fly, play, buy, fight,
escape — one per slide over Harry Potter artwork, opening on the form and
closing on a recap grid.

**Slide 8 shipped without its eyebrow.** Every other verb slide carries
`VERB → IS VERB-ING` above the title; slide 8 had an empty text box named
`Prompt 8` sitting top-left in Arial 12.75pt, while its siblings use a
Courier New 13.5pt box positioned above the title. Not a rendering artefact —
`markitdown` showed no text in it either. Replaced with a copy of slide 6's
`Grammar 9` shape, `PLAY` → `FIGHT`, x shifted to 7176135 to sit over slide 8's
own title. `validate.py --original` passes.

**Slide 2 carried a duplicate eyebrow.** Two shapes with the same text: the
correct one (`Grammar 9`, black `tx1`, above the title) and a stray
(`Grammar 2`, salmon `E85F5B`, parked in the top-left corner over the pink
panel, where it was near-invisible but present). Innes asked for it to be
black; it already was — the salmon one was a second copy in the wrong place.
Deleted.

**The uploaded `.pptx` is therefore two shapes different from the file Innes
sent** — slide 8's eyebrow added, slide 2's duplicate removed — and the
download button serves that corrected copy.

### Branding: the logo, and where it can actually go

The deck arrived with no Forbes English mark at all. Precedent from the two
older pptx decks: **Star Wars puts it bottom-right on the cover only; Twin
Peaks also puts it in the bottom-right of interior slides.** Innes asked for it
"green like the website" — that is `--green-deep #1b3a28` and
`--green-light #4a8f61`, both straight out of `library.html`.

`logo-forbes-english_1.png` (692x360, RGBA, transparent) is the only usable
asset. The five files in `HOUSE STYLE/` are photographs of business cards.
Recolour by rewriting RGB and keeping alpha — a flat monotone mark, which is
what both older decks use.

**Placement had to be measured, not guessed.** This artwork is dark in almost
every corner: the bottom-left of the ten slides runs L=0.01 to 0.54 and the
bottom-right L=0.01 to 0.33, so neither green reads everywhere and there is no
one corner that works across the set. First attempt put the cover logo just
below the subtitle at 106px tall and "ENGLISH" landed in the treeline. What
worked:

- **Cover** — bottom-right, **on the black bag**, right-aligned to the page
  number above it. The bag is as close to pure black as the deck gets
  (median L=0.003), so the light green measures **5.4:1** — the best contrast
  anywhere on the ten slides.
- **Back page** — the identical corner and identical size, so the two pages
  book-end. Darkest patch there is L=0.055; same light green, **3.3:1**.

Same green on both, deliberately: different tints in the same corner on the
two pages read as a mistake. An earlier attempt put the cover mark in the
cloud strip under the subtitle in the deep green — legible at 5.2:1, but the
bag is both darker and the corner Innes asked for.

Interior slides carry no mark, matching Star Wars. Twin Peaks brands its
interiors, so **if Innes wants all ten, the per-slide colour has to be chosen
from the local luminance** — a single colour will disappear on some of them.

Worth knowing for next time: every *visible* run in this deck is Courier New.
The Arial that shows up in a naive font scan is only in paragraph defaults
(`defRPr`) and in two empty leftover boxes, `Prompt 7` and `Prompt 8`. Check
`<a:r>` runs, not `<p:sp>` shapes, before reporting a font inconsistency —
`Prompt 7` is still in the file, empty and invisible.

### Two departures from the twin-peaks viewer, both deliberate

- **Neighbour preloading.** At ~250KB a slide, every arrow press showed an
  empty frame while the next image downloaded. `warm(idx±1)` after each render.
- **Swipe.** A deck on a phone that only advances by hitting a 40px circle is a
  deck nobody reaches the end of. Horizontal intent is required
  (`|dx| > 45 && |dx| > |dy| * 1.5`) or scrolling flips slides.

Also: the back link goes to `library.html`, not `index.html`. Both older
viewers say "← Back to catalog" and point at `index.html`, which is the home
page, not the catalogue. **Those two are still wrong** — a one-line fix each,
not done here.

---

## The gap engine scored one blank per row — fixed, and swept clean

Found by play-testing Food A1 Part 1: a perfect run finished **18/19**. The
missing point was a dialogue line carrying two blanks.

`checkGaps()` marked a `.gap-row` by its **first** input and stopped, while
`maxScore` counted every input on the slide:

```js
rows.forEach(r => markGap(r.querySelector('.gap'), r.querySelector('.feedback')));
```

So a second blank in the same row was worth a point nobody could earn, and it
was never explained either: the learner typed both words correctly, watched the
score go up by one, and had no way to tell which half had supposedly failed. A
slide with several gaps and **no** `.gap-row` at all was worse — the fallback
branch marked exactly one input for the whole slide.

### The fix is in the engine, not in the content

The first instinct was to split every multi-blank row and add an assert to
`deck.gap()` forbidding them. That is wrong, and exam-prep is why: its
"Write the question" items read `______ she ______ an alien?` — the auxiliary
and the bare verb are **one** question, and splitting them into two rows
destroys the exercise.

`lesson-template.html` now has `markGroup(gaps, fb)`: it marks every input in
the group, and writes one piece of feedback naming **every** answer missed
rather than only the first. `markGap` no longer touches feedback at all. Both
branches of `checkGaps` go through it, so a slide with no `.gap-row` is handled
too. Behaviour for a single-blank row is byte-identical.

`deck.gap()`'s assert was relaxed to match: blanks must equal answers (a
mismatch is a builder typo), and multi-blank rows are legal again.

### Swept, at runtime rather than statically

A static sweep for `.gap-row` elements holding more than one `.gap` is the
wrong instrument now that the engine handles them — it reports false failures.
The right test drives the page: fill every gap on a slide with its own
`data-answer`, click Check, and assert the score chip rose by the number of
inputs.

```js
gaps.forEach(g => { g.value = g.dataset.answer.split('|')[0]; });
btn.click();
if (chip() - before !== gaps.length) /* unscorable */;
```

**46 files carry gap-fills. All 46 now score every gap.** Before the fix, seven
points were unreachable across three lessons, on top of the six in Food Part 2
and the one in Part 1:

| File | Was losing | Fix |
|---|---|---|
| `forbes-english-food-ordering-a1-part2.html` | 6 | rebuilt through `deck.gap()` |
| `exam-prep-5hour-courseEXP.html` | 5 | rebuilt; content unchanged |
| `alchemist_b2_lesson.html` | 1 | rebuilt; content unchanged |
| `forbes_english_lesson.html` | 1 | **no builder** — engine patched in place |
| `forbes-english-food-ordering-a1-part1.html` | 1 | dialogue restructured |

**`forbes_english_lesson.html` has no builder**, so its inlined copy of the
engine was edited directly. Its copy is an older variant — `fb.textContent`,
no full stop after the answer — and the patch was written to match rather than
to import the current shape. If a builder is ever written for it, that patch
disappears with the rest of the hand-edits.

### The engine lives inside every generated deck

`lesson-template.html`'s script is inlined into each build, so an engine fix
reaches a deck only when its builder is re-run. Every deck is now one rebuild
behind on `markGroup`. That costs nothing today — the runtime sweep says no
other lesson has a multi-blank row — but a deck rebuilt later will silently
pick it up, and one that is never rebuilt keeps the old code. Do not treat a
template fix as shipped until the affected decks are rebuilt.

Also worth noting: `check-lesson.js` passed all twelve gates on every one of
these files throughout. The ACTIONS gate asks whether a scored slide *can* be
answered, not whether every answer on it *counts*. **A thirteenth gate that
drives the page and compares the score chip against the input count is the
obvious next addition** — it is about fifteen lines, and it is the only one of
the gates that would have caught this.

---

## "Coming soon": a lesson with no hero is not available

Innes: *"Write coming soon on any lesson without a hero and make them
unavailable."* 66 of 237 catalogue rows have no entry in `LESSON_IMAGES`.

The rule is **derived, never stored**. There is no column, no list, no second
place to update: `comingSoon(l)` is `!LESSON_IMAGES[l.file]` in `library.html`,
and `coming_soon(row, images)` is the same test in `tools/seo.py`. A lesson
becomes available the moment its artwork lands in `LESSON_IMAGES` — which is
already the last step of every rebuild.

The correlation is worth knowing: **all 66 heroless rows are `deck=false`** —
every one is an old scroll page that has never been rebuilt. The converse is
not true, though: 124 non-deck lessons *do* have heroes and stay available. So
"no hero" is a much narrower rule than "not a deck", and it is the right one.

What "unavailable" means, concretely:

- **In the library** the card is a `<div>`, not an `<a>` — no href, no hover
  lift, `aria-disabled`. An `<a>` with no href is still focusable and still
  announced as a link; a keyboard user would have got a worse answer than a
  mouse user. Dashed border, greyed artwork, a `COMING SOON` ribbon across the
  image and a `Coming soon` badge where `Pro` would be.
- **Sorted to the end.** Interleaved, a third of the shelf was dead cards and
  the catalogue read as half-built. Stable sort, so the order inside each group
  is unchanged.
- **The count line** reads `171 lessons · 66 coming soon`.
- **Out of the index**: no sitemap entry, no line in `llms.txt`, not in the
  crawlable list inside `library.html`, and `<meta name="robots"
  content="noindex,follow">` on the page itself. `follow`, not `none` — the
  internal links are still worth crawling, and it all reverses when artwork
  lands.
- **`lesson-meta.json` carries `"coming_soon": true`** on those 66 entries. The
  Worker reads that file to build each gate page, so the flag is the hook for
  serving a real coming-soon page instead of an unfinished lesson. **The Worker
  does not read it yet — that change has not been made.**

Sitemap went 240 → 174 URLs. That is deliberate: an indexed result that lands
on an unfinished lesson is worse than no result, and Innes has said he wants
the site fixed before he drives traffic to it.

---

## Ordering Food & Drink A1 — Part 1 BUILT, and Part 2 repaired

`forbes-english-food-ordering-a1-part1.html` — **18 slides, checker clean,
19/19 on a play-through.** `build_food_a1.py` + `i18n_food_a1.py`. Catalogue
row `id 242`, A1, deck, pro, to match Part 2. Thumbnail
`FoodA1P1/two-at-bar.jpg`.

Innes attached the source after the artifact URL proved unreadable. What the
audit found in it, and what the rebuild did:

- **The answer key was in the HTML.** Every blank carried its own answer as a
  literal argument — `onclick="fillBlank('fib-1','table')"` — and the handler
  did not even use it. Answers now live in `data-answer` like every other deck.
- **Q6 failed ANSWERS and taught bad grammar.** 48 characters against a
  33-character field, and the key read *"I'm allergic to nuts. **Is** there any
  in this dish?"* — `nuts` is plural. A grammar error inside the key of an A1
  item is the worst place to have one. Rewritten to *"Does this dish have
  any?"*; distractors lengthened to close the gap, key never shortened.
- **No activation stage and no teaching.** Both added: three polite openings
  (`Can I…?` / `Could we…?` / `I'd like…`) and four words before any question.
- Key positions were already deranged — `[1,3,1,2,0,2]` — and the word bank was
  already not in gap order. Those two were fine.

### Light theme, and the two contrast measurements it needed

`extract-palette.py FoodA1P1/two-at-bar.jpg --light` passes every row
(`text on surface` 12.28:1). But a light theme puts **dark ink on artwork**,
and this set has hard black silhouettes in it. Two measured problems, two
targeted fixes, both in `build_food_a1.py`'s `HEAD_CSS`:

1. **Three of the six pictures have a dark band across the top** — a chalkboard
   menu, rows of pendant lamps. Sampling the rendered pixels behind the slide
   title with the text hidden gave **2.57:1 on ten of eighteen slides**. Fix:
   raise the template's top wash stop for this lesson from 26% of `--void` to
   88%, and pull the ramp down from 20% of slide height to 26% so it clears the
   title. Worst case after: 4.82:1. The middle 54% of the slide is untouched.
2. **Text sitting on the bare illustration** — question stems, order hints,
   word banks, the results lines — measured 2.5–3.0:1. Fix: the card treatment,
   as on the Geoscience and Nature Agency light decks. Not a heavier wash.

**Do not fix a light-theme contrast problem by dropping `--bg-opacity`.** That
bleaches all the artwork to save two text blocks, and it is the failure the
light theme exists to avoid. Plate the text instead.

The measurement script is worth rebuilding when needed: screenshot each slide,
set the text `color: transparent` (not `visibility: hidden` — that hides the
plate you are trying to measure), sample the element's central band (not its
full box — the 1px border and the rounded corners dominate the 5th percentile
and report a false failure), and compare against `--text`.

### Part 2 was rebuilt too

`build_food.py`'s hand-rolled `dialogue_slide` put all four inputs inside one
`.card` with no `.gap-row`, so **six of its eight dialogue answers did not
score** — a perfect run reached 19/25 instead of 25/25. It now goes through
`deck.gap()` like everything else, with each line rewritten to carry exactly
one blank and its own explanation. Rows had to drop to 8px vertical padding to
fit the canvas; the alternative was cutting a line out of the conversation.

Rebuilding it also pulled in ~9KB of template CSS added since Part 2 was last
built. That is expected — every generated deck is one rebuild behind the
template until someone re-runs its builder.

### The bar-artwork question, answered by building it

The earlier note flagged that five of the six images are bars rather than
cafés. Built anyway: the deck's language is café and restaurant language
throughout, the pictures are backgrounds rather than comprehension material,
and the one image with a chalkboard menu and a barman serving two customers
makes a better A1 cover than either of the food shots. If Innes disagrees, the
hero is one line in `build_food_a1.py`.

---

## Ordering Food & Drink A1 — Part 1 does not exist, artwork staged

**SUPERSEDED — Part 1 is built and live. Kept for the artwork notes and the
crop warning; ignore the "two decisions waiting" at the end, both were made.**

`forbes-english-food-ordering-a1-part2.html` is live (A1, deck, pro) with
`FoodA1P2/` and a full builder set — `build_food.py`, `food_mc.py`,
`i18n_food.py`. **There is no Part 1.** Checked four ways: no matching file, no
catalogue row, no lesson whose content is about ordering food under another
name, and nothing in git history. Part 2 never refers back to a Part 1 either,
so it is not orphaned — it was simply built first.

A lesson publicly numbered "Part 2" with no Part 1 is worth fixing, and A1 is
the level least able to work out what it has missed.

### Artwork is staged; the content is not reachable

Six images in `FoodA1P1/`: `tray`, `counter-till`, `bar-shaker`, `wine-bar`,
`two-at-bar`, `drink-sign`.

**All six arrived at 3376×1440 — 2.34:1, much wider than 16:9** — and are
centre-cropped to 2560×1440. Uncropped they letterbox and the cover title lands
in a black band. Same trap as `Impostor2/hero.jpg`; check the aspect ratio of
anything from this generator before deriving a palette.

**The content lives in a claude.ai artifact that cannot be read from here.**
`https://claude.ai/public/artifacts/f089b9e1-3a4d-4d46-ad0e-8ad80cea873f`,
titled `forbes-english-food-ordering-a1.html`. `WebFetch` returns page metadata
only, the rendered preview is blank in Chrome, the code view yields nothing to
`get_page_text`, and `javascript_tool` is blocked on that origin. Ask Innes to
attach the HTML rather than re-attempting the URL.

### Two decisions waiting

- **Go light, not dark.** Innes asked for backgrounds that are not so dark. The
  pattern that causes it: derive a dark palette, then drop `--bg-opacity` to
  ~0.40 to keep text legible, which leaves the artwork as a murky wash. These
  images are bright pink and blue and the **light** palette passes every
  contrast row (`text on surface` 12.66:1), which allows a much higher opacity
  and lets the artwork actually show. Prefer `--light` whenever the hero is
  bright rather than forcing a dark theme down.
- **Five of the six images are bars** — cocktail shakers, wine, spirits. Only
  `tray.jpg` and `counter-till.jpg` read as ordinary food service. That is an
  odd fit for A1, and possibly better suited to a B1/B2 bar lesson. Raise it
  before building rather than shipping an A1 deck set in cocktail bars.

