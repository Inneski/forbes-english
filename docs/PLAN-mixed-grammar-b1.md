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

## 4. The slide plan, and where each picture goes

Backgrounds are `data-bg` swaps per §5b, set on **every slide in the section**,
not only its divider, so each section reads as one place.

| Slides | Content | Background |
|---|---|---|
| 1 | Cover | `hero.jpg` |
| 2–12 | Divider + 10 multiple-choice, one per slide | `s1-doors.jpg` |
| 13–18 | Divider, Elena's story as a `teach` slide, then 4 gap slides of 2 | `s2-cup-clock.jpg` |
| 19–25 | Divider + 6 true/false | `s3-thumb-shadow.jpg` |
| 26–31 | Divider + 5 `order` slides | `s4-bars-arrow.jpg` |
| 32–38 | Divider + 6 error-correction gaps | `s5-eraser-bulb.jpg` |
| 39 | Results | `hero.jpg` |
| 40 | Activation — speaking + writing | `activate-two-bubbles.jpg` |

**Forty slides, and that is deliberate.** §7's "split beyond twenty-four" is
written for a teaching lesson; a 35-item test does not split usefully, and this
is already Part 1 of two. The precedent is the exam decks, which run to 50 and
69 slides (`exam-prep-5hour-course-part2.html`,
`exam-prep-5hour-courseEXP.html`). If Innes would rather it ran shorter, the
one lever that does not cost content is folding Section 3 into two `sort`
slides of three statements into TRUE / FALSE bins — 40 slides becomes 36. Both
bins receive items (4 true, 2 false), so the SORT gate is satisfied.

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

Two constraints the editorial originals do not have, both from the deck:

- **16:9 with an empty middle.** Noma Bar's own work is mostly square or
  portrait with the pun dead centre. Ours cannot be — the cover lockup sits in
  the middle of the frame (§2) and the interior slides put a `.card` there.
  Push the idea to one third and let flat colour carry the rest.
- **Bright.** Light deck, so a light ground. See §3.

**Spec.** 16:9, 2000px or wider on the long edge. No lettering anywhere in the
picture. Run everything through `prep-artwork.py` rather than saving by hand.

| File | The idea |
|---|---|
| `MixedGrammarPart1/hero.jpg` | a pen nib, and the split down its centre is also a fork in a road running to the horizon — one object, two readings |
| `MixedGrammarPart1/s1-doors.jpg` | four identical flat doors in a row, three shut and one ajar, the wedge of space behind the open one forming a tick |
| `MixedGrammarPart1/s2-cup-clock.jpg` | a coffee cup seen from directly above, the dark circle of coffee also a clock face with no numerals, one hand near seven |
| `MixedGrammarPart1/s3-thumb-shadow.jpg` | a thumbs-up in flat colour whose cast shadow is unmistakably a thumbs-down |
| `MixedGrammarPart1/s4-bars-arrow.jpg` | five flat bars of different lengths in a jumbled stack, the gaps between them resolving into a single arrow pointing right |
| `MixedGrammarPart1/s5-eraser-bulb.jpg` | an eraser part-way along a line, and the cleared space behind it is the shape of a lightbulb |
| `MixedGrammarPart1/activate-two-bubbles.jpg` | two speech bubbles overlapping, and the lens of overlap between them is a pen nib |

**The hero is now on the list, and that is the cost of the style change.**
`desert-building-sunset-clouds.jpg` is a good picture but it is the *other*
style, and §0.3 makes the hero the background of every slide — a cinematic
cover over six flat-vector interiors is worse than either style alone. So the
count goes from six to seven. The two desert pictures stay on disk unreferenced
rather than being deleted; they are good enough to carry a lesson of their own
later, and git keeps the blobs regardless. **If you would rather keep the
desert covers and save two generations, say so** — it is a defensible call and
it is yours, not mine.

### And seven more for Part 2, for the same sitting

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

The builder is `lesson-template/build/build_mixedgrammar1.py` and does not
exist yet. It wants `deck.py` and `chrome_i18n.py` as usual, and
`assemble(..., langs=('en', 'de', 'es'))` **passed explicitly** — the default is
still `('en', 'de')` and nothing fails if it is forgotten. Teach cards in the
six-item form, so the German and Spanish rule text travels with its heading.
