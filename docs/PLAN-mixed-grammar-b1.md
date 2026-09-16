# B1 Mixed Grammar Test — audit and artwork shopping list

`forbes-english-b1-mixed-grammar-test.html` (and its sibling
`forbes-english-b1-mixed-grammar-test-part2.html`).

**Verdict: not house style, and blocked on artwork.** The content is sound and
should be ported as-is; the format is an old scrolling page and has to be
rebuilt as a deck. It cannot be converted yet because it has **one** image for
**five** sections, and HOUSE-STYLE §5c wants one background per section plus
one for the activation stage. The shopping list at the bottom is the six
pictures that unblock it.

Written 2026-09-16. Nothing has been built yet — no builder exists, and the
live page is untouched.

---

## 1. What is wrong with it

Measured against `lesson-template/HOUSE-STYLE.md`, not eyeballed.

| # | Rule | What the file does |
|---|---|---|
| 1 | §0.1 — 16:9 deck, never a scrolling page | `.page { max-width: 720px }`, one long column. No `class="stage-wrap"` (§10a's test), and no `data-type="activate"` and no `UI_I18N` block either (the sharper test in HANDOFF's deltas). Not a deck on any reading. |
| 2 | §0.2/§5b — hero is the cover and the background | The hero is an `<img>` inside a card (`heroImg.src = …` in `renderIntro`). §5b: *"Do not put an `<img>` in a card."* |
| 3 | §0.4/§4 — palette derived from the hero | Hand-picked. Paper `#EDF1EC`, green accent `#2F6B4F` — a mint-and-forest scheme over a **coral and slate desert sunset**. The palette and the picture have nothing to do with each other. |
| 4 | §6 — fonts | Fraunces + Work Sans. The site's three faces are Playfair Display, DM Sans, DM Mono, across 216 lessons. |
| 5 | §2 — the logo lockup | `viewBox="0 0 200 62"`, `x="100"`, `letter-spacing="8"`, fills hardcoded `#1E2A38` / `#1F4A36`. House geometry is viewBox `0 0 200 78`, `x="105.205"`, `y="72.6"`, `letter-spacing="10.41"`, mark on `var(--accent)` and ENGLISH on `var(--text)`. At `x=100`/`ls=8` ENGLISH renders ~9.75% narrower than Forbes — the LOGO gate fails. |
| 6 | §0.5/§8 — language switcher, EN+DE+ES minimum | There is no switcher. The `EN ↔ ES` badge is decoration over a CSS tooltip (`content: " (" attr(data-es) ")"`) on **six** vocabulary words. No `LANGS`, no `UI_I18N`, no German at all. |
| 7 | §0.6/§10b — activation stage | Absent. The lesson ends on a score band. Zero speaking or writing tasks in the file. |
| 8 | §5a — the published tense colour system | Twelve `--tense-*` hexes invented locally, all close to but none equal to the site's values. Present simple is `#2F6FB0` here and `#7A93B5` in `lesson-template/tense-palette.css`; past continuous `#E0B93C` vs `#F1D779`; future simple `#C99A3E` vs `#F0723F`. A learner coming off the Sherpa route map sees a different colour for the same tense. |
| 9 | Standing constraint — no hardcoded white/black | `--card-bg: rgba(255, 255, 255, 0.78)`. |
| 10 | §5c — one background per section | **This is the blocker.** Five sections plus an activation stage want six backgrounds; the folder holds one landscape image and a square thumbnail. |

One thing that does **pass**: the multiple-choice set clears the ANSWERS gate.
Only one key is the longest option at all — `was cooking` at 11 characters
against `am cooking` at 10 — and the gate needs the key to beat the longest
distractor *both* by more than 10% and by at least four characters. This is
exactly 10% and one character, so it clears on both counts. The distractors
were written properly. Do not rewrite them.

## 2. What is good, and must survive the rebuild

Thirty-five scored items across five sections, each carrying a grammar tag and
a written explanation. That is the asset (§10.1) and none of it gets dropped:

| Section | Items | Points |
|---|---|---|
| 1 · Multiple Choice | 10 sentences, 10 different grammar points | 10 |
| 2 · Reading & Fill in the Blank | Elena's story, 8 gaps | 8 |
| 3 · True or False | 6 grammar rules, some of them myths | 6 |
| 4 · Sentence Reordering | 5 sentences | 5 |
| 5 · Error Correction | 6 sentences, type the correction | 6 |
| | | **35** |

Part 2 is structurally identical — 10 / 8 / 6 / 5 / 6, all new sentences.

### Four content fixes to make while porting

Found reading the data, not the markup. They are bugs in the current live
lesson as well as things to get right in the deck.

1. **`ec6` marks a correct answer wrong.** The item is *"The girl which is
   sitting there is my cousin"* and the only accepted answer is *"the girl
   **who** is sitting there is my cousin"*. But `tf6`'s own explanation, in the
   same test, says *"'That' can replace either in everyday speech."* The lesson
   teaches that *that* works and then rejects it. Add it.
2. **`ec2` rejects the commonest correct form.** Accepted: *"if i have time, i
   will call you"* and the same without the comma. A learner who writes
   *"If I have time, I'll call you"* is marked wrong. §7: *"a learner who is
   right and marked wrong is worse than one who is wrong and marked right."*
   Every error-correction item needs its contraction variants listed.
3. **`ec1` likewise** — *"She's lived here for five years"* is not accepted.
4. **Section 4 shuffles single words.** §7 wants an `order` slide chunked *"at
   the joints you are teaching, never mid-phrase"*. Six loose words is a jigsaw;
   three phrases is a grammar point. Rechunk as e.g.
   `This house|was built|in 1990.` and
   `The man|who lives next door|is friendly.` Scoring is unaffected — `order`
   already scores one point for the whole sentence, which is what the current
   version does too.

## 3. Theme: light. Here is the measurement.

`MixedGrammarPart1/desert-building-sunset-clouds.jpg` is 2200×1232 (AR 1.786),
mean luminance **138** — comfortably over the 90 below which
`tools/prep-artwork.py` refuses a picture for a light deck. Both palettes pass
every contrast row, so this is a judgement, and it goes to light:

```
extract-palette.py … --light   →  --void #d8cbac  --surface #e1d9c4
                                  --accent #a82702  --accent-bright #761b00
                                  --contrast #075541      (all rows PASS)
```

`--void` lands at HSL lightness 0.761, exactly the ~0.76 §4a asks for. The dark
palette resolves to `--void #0c0e0e`, and at `--bg-opacity: 0.72` over near-black
the coral sky — the best thing in the picture — goes to mud. Take the light
theme, with `data-theme="light"` on `<html>` as §4a requires.

**This decides the shopping list.** Every new image has to sit in the same
brightness band or the set breaks in half. Target mean luminance **120–160**;
under 90 is an automatic refusal.

## 4. The slide plan, and where each picture goes

Backgrounds are `data-bg` swaps per §5b, set on **every slide in the section**,
not only its divider, so each section reads as one place.

| Slides | Content | Background |
|---|---|---|
| 1 | Cover | `hero.jpg` |
| 2–12 | Divider + 10 multiple-choice, one per slide | `s1-crossroads.jpg` |
| 13–18 | Divider, Elena's story as a `teach` slide, then 4 gap slides of 2 | `s2-window.jpg` |
| 19–25 | Divider + 6 true/false | `s3-fork.jpg` |
| 26–31 | Divider + 5 `order` slides | `s4-siding.jpg` |
| 32–38 | Divider + 6 error-correction gaps | `s5-shutter.jpg` |
| 39 | Results | `hero.jpg` |
| 40 | Activation — speaking + writing | `activate-tailgate.jpg` |

**Forty slides, and that is deliberate.** §7's "split beyond twenty-four" is
written for a teaching lesson; a 35-item test does not split usefully, and this
is already Part 1 of two. The precedent is the exam decks, which run to 50 and
69 slides (`exam-prep-5hour-course-part2.html`,
`exam-prep-5hour-courseEXP.html`). If Innes would rather it ran shorter, the
one lever that does not cost content is folding Section 3 into two `sort`
slides of three statements into TRUE / FALSE bins — 40 slides becomes 36. Both
bins receive items (4 true, 2 false), so the SORT gate is satisfied.

## 5. Shopping list — six images for Part 1

Same style as the two already on disk: flat vector, mid-century American
Southwest roadside at dusk, coral sky, slate-blue and pale concrete solids,
black silhouettes. Append the stem to every subject line.

```
flat vector illustration, cel-shaded, solid flat colour, minimalist,
mid-century American Southwest roadside at dusk, coral and salmon sky with
slate-blue and pale concrete solids, black silhouettes, ochre sand, subtle
halftone grain, wide landscape, subject off-centre with the middle of the
frame readable, no text, no lettering, no numbers --ar 16:9
```

**Spec.** 16:9, 2000px or wider on the long edge (2200 matches what is already
in the folder). Mean luminance 120–160 — this is a light deck and a muddy
scene breaks the set. Nothing centred: the cover lockup sits in the middle of
the frame. No lettering anywhere in the picture — Midjourney cannot spell, and
§13 has us chasing `%20` and stray glyphs often enough already.

Each subject carries the metaphor of its own section, so the background says
what the activity is before the learner reads the heading.

| File | Subject |
|---|---|
| `MixedGrammarPart1/s1-crossroads.jpg` | a desert crossroads at dusk, four blank signposts pointing four different ways, one pickup stopped at the line, long shadows |
| `MixedGrammarPart1/s2-window.jpg` | a first-floor apartment window early in the morning, curtains half drawn, a coffee pot and a small alarm clock in silhouette on the sill, the street below still in shadow |
| `MixedGrammarPart1/s3-fork.jpg` | a two-lane road forking around a rock outcrop, one lane in low sun and the other in shadow, a single figure standing where they split |
| `MixedGrammarPart1/s4-siding.jpg` | a desert rail siding at dusk, five freight cars being shunted into line, a switchman in silhouette at the points lever |
| `MixedGrammarPart1/s5-shutter.jpg` | a roadside diner at dusk with one shutter hanging crooked, a ladder against the wall and a figure halfway up straightening it, tools on the ground |
| `MixedGrammarPart1/activate-tailgate.jpg` | two figures sitting on the tailgate of a pickup at dusk, turned to face each other mid-conversation, an open notebook on the tailgate between them, sun on the horizon |

**Already on disk, nothing to generate:**
`MixedGrammarPart1/desert-building-sunset-clouds.jpg` is a good hero and stays.
It gets `git mv`-ed to `MixedGrammarPart1/hero.jpg` at build time per §3 — it
is referenced only by the page being replaced, so the rename costs nothing and
adds no blob.

### And six more if Part 2 is going through the same Midjourney sitting

Part 2 has the identical five sections and the identical problem — one image,
`desert-gas-station-sunset.jpg` (2200×1232, mean luminance 148, also a good
hero). Listed here only so both can be generated in one pass; Part 1 does not
wait on them.

| File | Subject |
|---|---|
| `MixedGrammarPart2/s1-motel.jpg` | a motel courtyard at dusk seen along the row, four identical doors in shadow, one car parked, a pool fence and a blank sign frame |
| `MixedGrammarPart2/s2-diner.jpg` | a diner booth by a window at dusk, two coffee cups and a folded map on the table, nobody in the seats, desert outside |
| `MixedGrammarPart2/s3-billboard.jpg` | a blank two-sided billboard alone in scrubland, lit on one face by the low sun and dark on the other, a maintenance ladder up the leg |
| `MixedGrammarPart2/s4-freight.jpg` | a long freight train crossing the frame on a level crossing at dusk, a lone pickup waiting at the barrier, Joshua trees behind |
| `MixedGrammarPart2/s5-repair.jpg` | a pickup pulled onto the shoulder with its hood up at dusk, one figure leaning in over the engine, a toolbox open on the ground |
| `MixedGrammarPart2/activate-porch.jpg` | two figures on a porch at dusk, one in a chair and one on the step, talking, a radio and a notebook on the boards between them |

## 6. What happens when the pictures land

Local session, in this order. `prep-artwork.py` does the resize, the quality
and the duplicate check — **do not commit raw Midjourney PNGs**, `.git` is
already ~700 MB with no LFS.

```bash
python3 tools/prep-artwork.py incoming/MixedGrammarPart1 --into MixedGrammarPart1 \
  --names s1-crossroads,s2-window,s3-fork,s4-siding,s5-shutter,activate-tailgate
git mv MixedGrammarPart1/desert-building-sunset-clouds.jpg MixedGrammarPart1/hero.jpg

python3 lesson-template/extract-palette.py MixedGrammarPart1/hero.jpg --light   # every row PASS
python3 lesson-template/build/build_mixedgrammar1.py                            # to be written
node   lesson-template/check-lesson.js forbes-english-b1-mixed-grammar-test.html # must exit clean
python3 tools/build_hubs.py
python3 tools/seo.py
```

Keep the filename — `forbes-english-b1-mixed-grammar-test.html` — so the live
URL does not move (§10.8). `library.html` already has a `LESSON_IMAGES` row for
it; point it at `MixedGrammarPart1/hero.jpg` once the rename is done, and run
`node lesson-template/check-library.js --vs-origin` before committing that file.
`tools/topics.py` already maps both parts to `tense-review`, so the hub picks
them up with no override needed.

The builder is `lesson-template/build/build_mixedgrammar1.py` and does not
exist yet. It wants `deck.py` and `chrome_i18n.py` as usual, and
`assemble(..., langs=('en', 'de', 'es'))` **passed explicitly** — the default is
still `('en', 'de')` and nothing fails if it is forgotten. Teach cards in the
six-item form, so the German and Spanish rule text travels with its heading.
