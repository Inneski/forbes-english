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
