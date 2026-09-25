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
the coral sky — the best thing in the picture — goes to mud.

> **Superseded 2026-09-24, and left here for the reasoning.** Innes chose the
> Noma Bar flat-vector house style over the desert look (§5), which retires
> `desert-building-sunset-clouds.jpg` as the hero. The numbers above describe a
> picture the deck will no longer use, so **the palette has to be re-derived
> from the new hero** when it lands — do not paste the block above into the
> builder.
>
> The *conclusion* almost certainly survives: Noma Bar is flat, bright, solid
> colour on a cream or pink ground, which is squarely §4a's "bright and airy",
> so expect `--light` and `data-theme="light"`. Confirm it rather than assume
> it — run the extractor both ways on the real hero and read the contrast
> report, as §4 requires.

**Whatever the hero turns out to be, the set has to hold together.** Run
`prep-artwork.py` over all seven at once so it reports the luminance of each,
and keep them inside a band of roughly ±20 of the hero's. Anything under 90 is
an automatic refusal for a light deck.

## 4. House style 2 — the panel layout, not the washed hero

**Innes's instruction, 2026-09-25, and it is the one that decides the deck.**
"House style 2" is not an art direction. It is the *second slide treatment*
in `lesson-template.html`, and the template states the distinction itself:

> §5 washes the hero to 0.72 and plates the text on top of it, which is right
> when the artwork is atmosphere. **It is wrong when the artwork is the point —
> a flat-vector illustration dimmed by a quarter and covered by a card is
> neither legible nor worth looking at.**
>
> So: the picture owns `--panel-w` of the stage at FULL opacity, bleeding off
> three edges, and the text owns what is left, on flat `--void`. […] Nothing is
> plated here, because nothing is over anything. Do not add a wash, a scrim or
> a card to the text column.
>
> — `lesson-template.html`, the PANEL block

So the two styles are:

| | Style 1 — washed hero (§5) | Style 2 — panel |
|---|---|---|
| Picture | behind everything at `--bg-opacity: .72`, under a wash | owns a column at **full opacity**, bleeding off three edges |
| Text | in a translucent `.card` over the artwork | in a clean column on flat `--void`, nothing plated |
| Right for | photographic or atmospheric artwork | **flat-vector illustration** |

The Noma Bar batch is flat-vector illustration, so style 2 is not a preference
here — style 1 would actively wreck it. `deck.py` already has both:
`D.panel()` and `D.divider()` against `D.teach()`.

**The worked reference is `build_twinpeaks2.py`** — 23 slides on **five**
pictures, alternating sides, `pos=` re-cropping the same file for each reuse.
Read it before writing this builder.

### Inverted panels

`D.panel(..., side='right')` emits `data-side="right"`, and the template flips
the row:

```css
.slide[data-layout="panel"][data-side="right"] { flex-direction: row-reverse; }
```

The CSS comment gives the reason: *"Alternate the side down the deck: it stops
a long deck reading as one template, and lets each picture be cropped toward
the side its subject actually occupies."* On a forty-slide deck that is not
decoration, it is the thing that stops it feeling like a form. Alternate every
panel, as Twin Peaks does.

### The crop — this changes the art brief

A panel picture occupies `--panel-w`, **548px by default, of a 1280×720
stage**, painted `cover`. That is a **548×720 portrait window, aspect 0.76** —
a tall vertical slice taken out of a 16:9 source. Most of the width is thrown
away.

Three consequences:

- **The subject has to survive a tall narrow crop.** Noma Bar suits this better
  than the desert scenes did — one object on an empty ground crops cleanly,
  where a wide landscape loses its composition entirely.
- **`pos=` picks the slice** (`--pic-pos`), e.g. `pos='38% 50%'`. Twin Peaks
  uses it on three of its five pictures. Budget for tuning each one by eye.
- **`width=` widens the column** (`--panel-w`) for a picture that needs it.

The cover still wants a true 16:9 — it is the one full-bleed slide — and so do
the `divider()` openers, which show a picture whole across the stage.

### The slide plan

Each section opens with a `divider()` showing its picture whole, then a
`panel()` carrying the section instruction with the same picture cropped to a
column, then its question slides on flat `--void`.

| Slides | Content | Layout |
|---|---|---|
| 1 | Cover | full-bleed `hero.jpg` |
| 2–3 | Section 1 divider, then instruction panel | `s1-clipboard.jpg`, panel left |
| 4–13 | 10 multiple-choice, one per slide | flat `--void` |
| 14–15 | Section 2 divider + panel | `s2-clock.jpg`, panel **right** |
| 16–20 | Elena's story as a panel, then 4 gap slides of 2 | panel left, then flat |
| 21–22 | Section 3 divider + panel | `s3-key-padlock.jpg`, panel **right** |
| 23–28 | 6 true/false | flat `--void` |
| 29–30 | Section 4 divider + panel | `s4-index-cards.jpg`, panel left |
| 31–35 | 5 `order` slides | flat `--void` |
| 36–37 | Section 5 divider + panel | `s5-tool-roll.jpg`, panel **right** |
| 38–43 | 6 error-correction gaps | flat `--void` |
| 44 | Results | flat `--void` |
| 45 | Activation — speaking + writing | `activate-notepad.jpg`, panel left |

**§5c is satisfied differently under style 2, and better.** The rule wants a
distinct picture per section; here each section's picture is shown *whole* on
its divider and again *cropped* on its panel, at full opacity both times,
rather than being dimmed to a ghost behind ten question slides. Question slides
carry no artwork at all — flat `--void`, which is what the panel block means by
"nothing is plated because nothing is over anything". Do not also set `data-bg`
on them; that would reintroduce style 1 underneath style 2.

**Forty-five slides, and that is deliberate.** §7's "split beyond twenty-four"
is written for a teaching lesson; a 35-item test does not split usefully, and
this is already Part 1 of two. The precedent is the exam decks, which run to 50
and 69 slides (`exam-prep-5hour-course-part2.html`,
`exam-prep-5hour-courseEXP.html`). Style 2 adds five over the earlier plan —
the divider and panel per section are what give the artwork its full-opacity
moment, and they are the reason the deck can carry forty-five slides without
reading as one template.

If Innes would rather it ran shorter, the one lever that does not cost content
is folding Section 3 into two `sort` slides of three statements into TRUE /
FALSE bins — 45 becomes 41. Both bins receive items (4 true, 2 false), so the
SORT gate is satisfied. Dropping the panels to save slides is the wrong lever:
it is the house style 2 instruction.

## 5. Shopping list — seven images for Part 1

**Style: Noma Bar flat vector.** Innes's call, 2026-09-24. That is the stem
already documented in `docs/PLAN-foundations-grammar-business.md` and
`docs/minecraft-artwork-plan.md`, and the style filling the `HOUSE STYLE/`
reference folder at the repo root — flat shapes, two to four solid colours, one
idea carried by negative space, no texture and no depth.

```
flat vector illustration, cel-shaded, solid flat colour, minimalist,
Noma Bar style, negative space, wide landscape, cream and dusty pink and
coral with slate-blue and black silhouettes, subject off-centre with the
middle of the frame empty, no text, no lettering, no numbers --ar 16:9
--no photorealistic, gradient, texture, grain, depth of field, perspective
```

**The `--no` clause is not optional, and here is the evidence.** Nine PNGs at
the repo root are named
`blackisler_flat_vector_illustration_cel-shaded_solid_flat_col_*` and **none of
them is flat vector** — the one opened to check is a painterly Minecraft sunset
with gradients, atmospheric haze and depth of field. The words in the stem did
not survive the generation. Check the four-up against `HOUSE STYLE/` before
keeping anything, and do not trust a filename as evidence of style.

### Writing a Noma Bar brief

This is a different brief from a scene, and the earlier desert list will not
translate line for line. Noma Bar is **one substitution, read at a glance**: a
brain that is also a barbell, a face whose negative space is a second face. So
each subject below names an *idea*, not a place, and the test is whether it
still reads at thumbnail size.

Three constraints the editorial originals do not have, all from the deck:

- **The cover wants an empty middle.** The stacked Forbes/ENGLISH lockup and
  the 62px title both land dead centre (§2, §6). Push the idea to one third and
  let flat colour carry the rest. This applies to `hero.jpg` and to the
  `divider()` openers, which show a picture whole across the stage.
- **The panel slides crop to a tall column — see §4.** `--panel-w` is 548px of
  a 1280×720 stage, so a panel takes a **548×720 portrait slice** out of the
  16:9 source and throws the rest away. A single object on an empty ground
  survives that; a composition spread across the width does not. Keep the idea
  inside a vertical third, and expect to tune each one with `pos=`.
- **Bright.** Light deck, so a light ground. See §3.

**Spec.** 16:9, 2000px or wider on the long edge. No lettering anywhere in the
picture. Run everything through `prep-artwork.py` rather than saving by hand.

**Style 2 uses pictures harder, so it needs fewer of them.**
`build_twinpeaks2.py` runs 23 slides on five. If one of the seven below is weak
at full size, reusing a strong one at a different `pos=` beats shipping a poor
picture — that is exactly what the reference build does.

### One style per deck — Part 1 Noma Bar, Part 2 desert

**Settled 2026-09-25.** Innes has generated both families and both are good;
§0.3 is what stops them being mixed, since the hero becomes the background of
every slide and a flat-vector cover over cinematic interiors is worse than
either alone. So each deck takes one family whole. Nothing is wasted, and the
two sibling decks end up visually distinct, which they should be anyway.

### Part 1 — Noma Bar, and six of the seven already exist

Six files in `Documents\FORBES\incoming` map onto the five sections and the
activation stage almost exactly — four rows with three ticked for multiple
choice, cards knocked over for reordering, a tool roll for error correction, a
notepad and pencil for the speaking-and-writing stage. That is not
coincidence; the batch was generated for this lesson.

**The right-hand column is read off filenames in a screenshot, so confirm it
against `prep-artwork.py --dry-run` before committing.** Rename on the way in
with `--names`; the Midjourney names do not belong in the repo.

| File | Where it comes from |
|---|---|
| `MixedGrammarPart1/hero.jpg` | **to generate** — see the cover brief below |
| `MixedGrammarPart1/s1-clipboard.jpg` | have — `a_clipboard_with_four_rows_three_ticked_and_the_fo…` |
| `MixedGrammarPart1/s2-clock.jpg` | have — `a_large_clock…`, or `a_first-floor_apartment_window_early_morning_curta…` if that reads better for Elena's morning |
| `MixedGrammarPart1/s3-key-padlock.jpg` | have — `a_brass_key_lying_beside_a_padlock_the_teeth_plain…` |
| `MixedGrammarPart1/s4-index-cards.jpg` | have — `a_box_of_index_cards_knocked_over_the_cards_fanned…` |
| `MixedGrammarPart1/s5-tool-roll.jpg` | have — `a_canvas_tool_roll_unrolled_flat_on_a_bench_tools…` |
| `MixedGrammarPart1/activate-notepad.jpg` | have — `a_desk_with_a_notepad_and_a_pencil_wide_negative_s…` |

Spares in the same batch, if one of the above disappoints at full size:
`a_departure_board_mid-flip_negative_space…` (reordering),
`a_bare_light_bulb_hanging_from_a_cord_switched_on…` (error correction),
`a_jigsaw…` (reordering), `a_crisp_card_folder_with_three_identical_sheets…`.

#### The cover brief — the one still to generate

Innes's call, 2026-09-25: the cover is Noma Bar. It has to sit in the same
family as the six above — an everyday desk object, flat, muted, wide empty
space — rather than being a cleverer idea in a different register.

> **a single pencil lying low and to the left on a plain pale ground, its cast
> shadow curving away from it into a question mark, the rest of the frame
> empty**

Stem and `--no` clause as above. The empty middle matters more here than
anywhere else: the stacked Forbes/ENGLISH lockup and the 62px cover title both
land dead centre (§2, §6), so the pencil belongs in the lower-left third and
the shadow should sweep away from the middle, not through it.

### Part 2 — the desert set, which is already half-bought

`MixedGrammarPart2/desert-gas-station-sunset.jpg` (2200×1232, mean luminance
148) is already in the repo and is a good hero, so Part 2 needs no cover at
all. Three section backgrounds are in `incoming` already:

| File | Where it comes from |
|---|---|
| `MixedGrammarPart2/hero.jpg` | have — `git mv` the existing `desert-gas-station-sunset.jpg` |
| `MixedGrammarPart2/s1-crossroads.jpg` | have — `a_desert_crossroads_at_dusk_four_blank_signposts_p…` |
| `MixedGrammarPart2/s2-window.jpg` | have — `a_first-floor_apartment_window_early_morning_curta…` |
| `MixedGrammarPart2/s4-siding.jpg` | have — `a_desert_rail_siding_at_dusk_five_freight_cars_bei…` |
| `MixedGrammarPart2/s3-fork.jpg` | **to generate** — a two-lane road forking around a rock outcrop, one lane in low sun and the other in shadow, a single figure where they split |
| `MixedGrammarPart2/s5-shutter.jpg` | **to generate** — a roadside diner at dusk with one shutter hanging crooked, a ladder against the wall, a figure halfway up straightening it |
| `MixedGrammarPart2/activate-tailgate.jpg` | **to generate** — two figures on a pickup tailgate at dusk, turned to face each other mid-conversation, an open notebook between them |

Those three take the **desert** stem, not the Noma Bar one:

```
flat vector illustration, cel-shaded, solid flat colour, minimalist,
mid-century American Southwest roadside at dusk, coral and salmon sky with
slate-blue and pale concrete solids, black silhouettes, ochre sand, subtle
halftone grain, wide landscape, subject off-centre with the middle of the
frame readable, no text, no lettering, no numbers --ar 16:9
```

`MixedGrammarPart1/desert-building-sunset-clouds.jpg` is now spare. It is the
same family as Part 2, so it is the obvious fallback there if one of the three
above never gets generated — or it keeps for a lesson of its own. Do not
delete it; git keeps the blob either way and it costs nothing to leave.

**Both library thumbnails want recutting** once the heroes settle — Part 1's
from the new Noma Bar cover, Part 2's from the gas station. `LibraryCards/` at
1200×512, per the publish skill.

### Superseded — the all-Noma-Bar list for Part 2

Identical five sections, identical problem. Different ideas rather than
recoloured twins, so the two decks do not read as one.

| File | The idea |
|---|---|
| `MixedGrammarPart2/hero.jpg` | a question mark whose curve straightens into a road running to a low horizon |
| `MixedGrammarPart2/s1-keys.jpg` | four flat keys hanging in a row, one casting a shadow shaped like a keyhole |
| `MixedGrammarPart2/s2-book-bird.jpg` | an open book seen edge-on, its two pages becoming the wings of a bird lifting off |
| `MixedGrammarPart2/s3-coin.jpg` | a coin caught mid-spin, one visible face a tick and the blurred other face a cross |
| `MixedGrammarPart2/s4-zip.jpg` | a zip half done up, the two ragged sides interlocking into one clean line |
| `MixedGrammarPart2/s5-inverted.jpg` | a row of identical flat shapes with exactly one upside down, the gap it leaves forming an exclamation mark |
| `MixedGrammarPart2/activate-mic-pencil.jpg` | a microphone whose stand tapers into a sharpened pencil |

## 6. What happens when the pictures land

Local session, in this order. `prep-artwork.py` does the resize, the quality
and the duplicate check — **do not commit raw Midjourney PNGs**, `.git` is
already ~700 MB with no LFS.

```bash
# --dry-run first: it prints each file's luminance and aspect, and picks
# between Midjourney's near-identical four-up variants.
python3 tools/prep-artwork.py "incoming/B1 test" --into MixedGrammarPart1 --dry-run

python3 tools/prep-artwork.py "incoming/B1 test" --into MixedGrammarPart1 \
  --names hero,s1-doors,s2-cup-clock,s3-thumb-shadow,s4-bars-arrow,s5-eraser-bulb,activate-two-bubbles

python3 lesson-template/extract-palette.py MixedGrammarPart1/hero.jpg --light   # every row PASS
python3 lesson-template/build/build_mixedgrammar1.py                            # to be written
node   lesson-template/check-lesson.js forbes-english-b1-mixed-grammar-test.html # must exit clean
python3 tools/build_hubs.py
python3 tools/seo.py
```

`--names` is positional — `names[i]` goes to the *i*th source in the order
`prep-artwork.py` lists them — and it **exits if the count does not match the
number of source files**, which a folder of Midjourney four-ups will trip
immediately. Read the `--dry-run` output, confirm the pairing, and split the
four-ups down to seven files first. On Windows it is `py`, not `python3`.

Keep the filename — `forbes-english-b1-mixed-grammar-test.html` — so the live
URL does not move (§10.8). `library.html` already has a `LESSON_IMAGES` row for
it; repoint it at `MixedGrammarPart1/hero.jpg`, and run
`node lesson-template/check-library.js --vs-origin` before committing that file.
`MixedGrammarPart1/mixed-grammar-part1-thumb.jpg` is the old desert square and
becomes the odd one out on the library page too — recut the card from the new
hero (`LibraryCards/` at 1200×512, per the publish skill).
`tools/topics.py` already maps both parts to `tense-review`, so the hub picks
them up with no override needed.

## 7. The builder exists and is verified — 2026-09-25

`lesson-template/build/build_mixedgrammar1.py` and
`lesson-template/build/i18n_mixedgrammar1.py` are written, committed and
**checked end to end against placeholder artwork**, which was then deleted. All
35 items are in it, in house style 2, with panels alternating sides.

```
wrote forbes-english-b1-mixed-grammar-test.html — 45 slides
LAYOUT PASS · PAINT PASS · ENTITIES PASS · KEYS PASS · ANSWERS PASS
BANK PASS · MARKUP PASS · SORT PASS · ACTIONS PASS · EXPLAIN PASS
RESOLVE PASS · ACTIVATION PASS · I18N PASS (3 complete languages)
ART PASS (7/7) · HEAD PASS (after seo.py) · RUNTIME PASS
LOGO FAIL  ← see below
```

**Thirteen of fourteen gates pass. LOGO cannot be verified from a cloud
session and its failure here is an artifact, not a defect.** The page loads DM
Sans from Google Fonts and carries the corrected §2 geometry (`x="105.205"`,
`letter-spacing="10.41"`). The control proves it: `forbes-c1-negotiation.html`
— the deck HOUSE-STYLE names as the worked reference — fails LOGO identically
in this sandbox. `curl` reaches `fonts.googleapis.com` with a 200, but the
headless browser the checker launches does not, so ENGLISH measures in a
fallback face. **Re-run the checker locally before shipping**; that is the only
gate still outstanding.

`seo.py` was run and its diff checked against CLAUDE.md's warning: 303 sitemap
URLs before and after with an identical URL set, 295 `llms.txt` entries before
and after, `library.html` untouched. Nothing was silently dropped. The
generated HTML and those index files were then reverted, because **a deck whose
seven pictures do not exist must not go live** — the panels would paint flat
`--surface2` and the cover would have no hero.

**So the remaining work is the artwork and nothing else.** Drop the seven
files in and run:

```
python3 lesson-template/build/build_mixedgrammar1.py
node   lesson-template/check-lesson.js forbes-english-b1-mixed-grammar-test.html
python3 tools/seo.py
```

Two things in the builder are deliberately provisional and marked in the
source:

- **`PALETTE` is derived from the old desert hero.** It passes every contrast
  row so the deck builds and checks clean, but re-run `extract-palette.py` on
  the real Noma Bar cover and paste the block over it. `assemble()` derives
  `data-theme` from `--void`'s luminance, so a dark palette pasted there
  silently flips the whole deck to dark.
- **`POS = {}` is empty.** A panel crops 548×720 out of a 16:9 source (§4), so
  each picture will want a `pos='38% 50%'`-style slice chosen by eye. Centre is
  the honest default until the real artwork exists.

### What the builder carries that the old page did not

- `assemble(..., langs=('en', 'de', 'es'))` **passed explicitly** — the default
  is still `('en', 'de')` and nothing fails if it is forgotten.
- All 35 explanations as `UI_I18N` keys rather than English literals, so they
  translate with the deck. §7 calls this "the better choice on a lesson that
  ships more than one language"; this one ships three.
- The four content fixes from §2. `ec6` now accepts "that", `ec1`/`ec2` accept
  the contracted forms, and Section 4 is chunked at the joints.
- A fifth fix found while building: **the engine's `flatten()` folds case,
  quotes, dashes and whitespace but does NOT strip a trailing full stop**, so a
  learner typing a full corrected sentence with its own punctuation was marked
  wrong. `sentences()` in the builder expands every error-correction answer
  with and without it.
