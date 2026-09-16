# Artwork shopping list — the 52 lessons that cannot be converted until pictures exist

Started from one question — *why is `harry-quebert-b2.html` not in house style, and
what would it take?* — and finished as the answer for every lesson in the same
position. Quebert is not a special case. It is one of **52 catalogued lessons that
are still scrolling pages and have no picture good enough to build a deck from.**

Everything below is a Midjourney brief. Innes generates; a later session builds.
Nothing here can be done from a session alone, which is why it is written down
rather than queued.

---

## 1. Why Quebert is blocked, and what "like this" means

`harry-quebert-b2.html` is a 23 KB scrolling page: a synopsis card, a narrative-tenses
teach card, then sixteen questions in three parts (6 vocabulary, 6 narrative tenses,
4 reading comprehension) and a results card. Against the six rules in
`lesson-template/HOUSE-STYLE.md` §0 it fails four of them:

| Rule | State |
|---|---|
| 1. 16:9 slides, never a scrolling page | fails — one long scroll |
| 2. Landscape hero on the cover | fails — no hero anywhere in the file |
| 3. That hero repeating behind every slide | fails — no background image at all |
| 5. Language switcher, every language complete | fails — English only, no `data-i18n` |
| 6. Activation stage (speaking + writing) | fails — it ends on a score |
| 4. Palette derived from the hero | moot until there is a hero |

Rules 1, 5 and 6 are a rebuild — a session can do those from what is in git today.
**Rules 2, 3 and 4 cannot be done at all**, because the only picture the lesson owns
is `LibraryCards/harry-quebert.jpg` at 1200×512. That is under the §3 minimum (1400px
wide) and it is not even 16:9 — 2.34:1, a web card crop. There is nothing to derive a
palette from and nothing to put behind the slides.

So "a lesson like Quebert" is defined as: **catalogued, still a scrolling page, and
owning no image of at least 1400px.** That is the list in §5 and §6. It is the
§14 *"no hero image exists and none was supplied"* case, fifty-two times over.

---

## 2. How this was measured

```bash
python3 tools/audit-artwork.py              # the summary table below
python3 tools/audit-artwork.py --blocked    # the 52 in §5 and §6
python3 tools/audit-artwork.py --topups     # the 56 in §8
```

`tools/audit-artwork.py` is new and reads only what is in git — no Supabase, no
network — so it gives the same answer in a cloud session as on Innes's machine.
Regenerate rather than trust this file, because the previous counts in `docs/`
disagree with each other and with the tree. What it does:

1. Every entry in `tools/lessons.json` (317 catalogued lessons) resolved to its file.
2. Classified from the file itself, not from the `deck` column: a **deck** has
   `<section class="slide` *and* `fitStage`; an **RPG** has a `window.*_GAME_DATA`;
   the rest are **scrolling pages**. Deliberately-not-a-deck families are excluded —
   Sherpa Tensing, the Block Camp time-signals pages, Sailing the Seas, the `.pptx`
   deck-viewers.
3. Artwork found three ways: images the page itself references (`src`, `url(...)`,
   `data-bg`), the folder its `LESSON_IMAGES` card points at, and any root artwork
   folder whose name matches the lesson slug. JPEG/PNG headers read for real pixel
   dimensions.
4. **Usable** means ≥1400px wide (§3). `FORBES ENGLISH/` and `HOUSE STYLE/` are
   excluded from matching — they are brand and reference dumps, and matching on
   `forbes-english-*` made every lesson look supplied.

### The numbers

| | |
|---|---|
| Catalogued lessons | 317 |
| House-style decks | 130 |
| RPGs / deck-viewers / not-a-deck families | 55 |
| **Scrolling lessons** | **132** |
| — with no usable image at all | **52** |
| — with exactly one | 28 |
| — with two to four | 28 |
| — with five or more | 24 |

The 52 split two ways, and the difference matters when you generate:

- **19 own a picture that is too small** (900–1200px web cards). The subject is
  usually right; it is the file that is wrong. These want the *same idea* generated
  at spec, not a new idea.
- **33 own nothing at all.** Free choice of subject.

**`docs/artwork-needed.md` is stale** — it was generated against `LESSON_IMAGES`
presence alone, before §5c existed, and it lists lessons that have since been given
art. This file supersedes it for the "what do I generate" question.

---

## 3. The spec every prompt below shares

Unchanged from the IELTS and Foundations lists — repeated so this file stands alone.

- **16:9, 2000px or wider.** 1400px is the floor in §3; 2000px is what
  `prep-artwork.py` normalises to, so generate above it.
- **No text, no numbers, no lettering** anywhere in the picture.
- **Subject off-centre, middle readable.** The cover carries the stacked
  Forbes/ENGLISH lockup and the title; a centred subject fights both.
- **One look per lesson.** Every frame in a folder comes off the same stem, the same
  palette and the same light. The hero sets the palette for the whole deck
  (`extract-palette.py`), so if one frame has to be perfect, it is that one.
- **Bright stays bright, dark stays dark.** A bright hero makes a light deck
  (`--light`, `data-theme="light"`); a dark one makes a dark deck. Mixing luminance
  inside a folder is what produced the muddy backgrounds §5 warns about.
- **Drop into `incoming/<folder>/<slot>/`** — several variants per slot is fine and
  expected; the building session picks. `incoming/` is gitignored.
- **Never commit a raw Midjourney PNG.** `python3 tools/prep-artwork.py <incoming-folder>
  --into <Folder>` resizes to 2000px q85, refuses duplicates and four-up repeats, and
  flags a wrong aspect ratio or a frame too dark for a light deck.

### Slot names

`hero`, then `bg02`, `bg03`, … one per teaching section, and the **last slot is always
the activation stage** (§0 rule 6 — every rebuilt deck gets a speaking and writing
task, including the ones that currently end on a score). This is the naming the
shipped builders already read.

Where one folder serves two lessons — a language edition, or a Part I/Part II pair —
the second lesson's cover is `hero-b` and the numbering runs straight on. Only the
lessons marked that way share a folder; everywhere else it is one folder per lesson,
because three decks off one pool is what produced the Block Camp repetition.

---

## 4. Three stems

The art style is a parameter (`docs/CHATGPT-RPG-BRIEF.md` §4a). Each lesson below
names the stem it wants. Every prompt is `<subject>, <stem>`.

**Stem A — flat vector, bright.** The house stem. A1–B1 grammar, sport, food, kids,
anything that should be a light deck.

```text
flat vector illustration, cel-shaded, solid flat colour, minimalist, Noma Bar style,
wide landscape, cream and dusty pink and coral with slate-blue and black silhouettes,
bright and airy, subject off-centre, no text --ar 16:9
```

**Stem B — flat editorial, two-tone, grainy.** The IELTS stem. Business, exam,
professional and technical lessons.

```text
flat editorial illustration, two-tone palette of slate blue and warm salmon, heavy
grain and stipple texture, hard single light source, deep shadow, no people, no text,
wide negative space --ar 16:9 --style raw
```

**Stem C — the same editorial grammar, after dark.** *New here.* Stem B's texture and
discipline on a night palette, for the fiction, thriller and floodlit lessons that
have no business being bright. A deck built from stem C runs `extract-palette.py`
**without** `--light`.

```text
flat editorial illustration, two-tone palette of deep navy and warm amber, heavy grain
and stipple texture, single low light source, long shadows, no people, no text, wide
negative space --ar 16:9 --style raw
```

Stems B and C say *no people*. Where a lesson genuinely needs a figure — roleplay,
sport, a taekwondo pattern — use stem A, whose silhouettes are part of the look.

---

## 5. Wave 1 — the nineteen lessons whose picture is simply too small

These already look supplied. They are not: every file below is a 900–1200px web card,
under the §3 minimum, and several are cropped to 2.34:1 rather than 16:9. Regenerating
them is the cheapest way to unblock nineteen rebuilds, and the subject is already
decided — the brief keeps it.

**Quebert first**, because it is the one that was asked about.

### `quebert/` — B2: The Truth About the Harry Quebert Affair — stem C, 6 frames

Has: `LibraryCards/harry-quebert.jpg`, 1200×512.
Sections: the case file · narrative tenses · thriller vocabulary · the tenses in use ·
reading the evidence · activation.

```text
hero  a clapboard lake house at dusk seen across still water, one upstairs window lit, subject to the right
bg02  a spade standing upright in freshly turned earth beside a taped-off garden, long evening shadow
bg03  three station clocks on a bare wall showing three different times, the middle one stopped
bg04  a typewriter on a desk with one sheet half typed, a lamp throwing a hard circle of light
bg05  a bundle of handwritten letters tied with string, spilling from an opened shoebox
bg06  an empty chair facing a second empty chair under one hanging lamp in a bare room
```

The three clocks are deliberate: the lesson teaches past simple, past continuous and
past perfect as three positions in time, and §5a gives each a colour. One background
that already says *three times, one of them stopped* does the teaching for the slide.

### `material-space/` — C1: Material & Space (vocabulary) — stem B, 5 frames

Has: `LibraryCards/architectural-vocab.jpg`, 1200×672. 16 items.
Sections: materials & making · space & structure · judgement & style · activation.

```text
hero  a concrete stair turning against a plain wall, one shaft of light across the treads, subject to the left
bg02  raw materials stacked on a workshop floor — sawn timber, a coil of copper, one sheet of glass
bg03  an empty gallery room with a single doorway and a skylight, the floor bare
bg04  two chairs side by side on a plain floor, one ornate, one stripped to its frame
bg05  a drawing board with a roll of plans half unrolled and a scale rule laid across it
```

### `material-space-speaking/` — C1: Material & Space, Speaking & Debate — stem B, 5 frames

Has: `LibraryCards/architectural-vocab-2.jpg`, 1200×672. 12 timed stations, three
topic groups. Same look as the folder above, different frames — a companion lesson
that reuses its partner's backgrounds reads as the same deck twice.
Sections: warm-up · materials & making · space & structure · judgement & style.

```text
hero  a long table with twelve cards face down in a row, one turned face up, subject to the right
bg02  an hourglass on a bare table, the sand a third through
bg03  two material samples held side by side against a plain wall, one rough, one polished
bg04  a model of a building cut in half to show the floors, on a plinth
bg05  a lectern facing an arc of empty chairs in a bright room
```

### `contingency/` — C1: Contingency Plans & Trade-offs — stem B, 6 frames

Has: `LibraryCards/contingency.jpg`, 1200×672. 28 questions in three sections plus a
full glossary.
Sections: planning & risk · materials & moisture · retrofitting & decisions · the
glossary · activation.

```text
hero  an unopened umbrella lying beside a drain running full on a flat pavement, subject to the left
bg02  two roads leaving one junction, the signpost's arms blank
bg03  a bucket under a ceiling drip in an empty room, a ring already stained on the floor
bg04  a wall half stripped back to brick, new insulation stacked against it
bg05  a card index drawer pulled open, one card standing proud of the rest
bg06  brass weights on a balance that is not quite level
```

### `dailies-review/` — C1: Dailies Review: Giving Feedback Diplomatically — stem B, 5 frames

Has: `LibraryCards/dailies-review.jpg`, 1200×512. 10 questions plus a phrase toolkit.
Sections: the review room · softening the note · asking for the thinking · activation.

```text
hero  a darkened screening room with one lit screen and two empty seats in the front row, subject to the right
bg02  a red pencil resting on a contact sheet, one frame lightly circled
bg03  a flipbook fanned open on a desk, one page held back by a thumb
bg04  a chair pulled up beside a desk, angled to face it rather than across it
bg05  a blank sticky note on a monitor bezel, a mug beside it
```

### `vapour-barriers/` — B2: Bringing a Membrane to Market — stem B, 6 frames

Has: `LibraryCards/vapour-barriers.jpg`, 1200×512. 18 questions in five sections.
Sections: word stress · prepositions with test/install/keep · adverb placement ·
tenses for finished and unfinished time · activation.

```text
hero  a roll of membrane half unrolled across bare roof joists against a flat sky, subject to the left
bg02  a tuning fork standing upright on a workbench beside a row of identical bolts
bg03  a knife, a tape roll and one seam of membrane lapped over a joint
bg04  a spirit level on a beam, the bubble just off centre
bg05  a finished roof seen from the ridge, the last sheet laid and the tools down
bg06  a sample board on a trestle table in an empty exhibition hall
```

### `speaking-2/` — B1+: Product Speaking — roofing membrane, cladding, vapour barrier — stem B, 5 frames

Has: `LibraryCards/speaking-2.jpg`, 1200×512. Four speaking stages built on the same
product world as `vapour-barriers/` — **same stem, same palette, different frames.**
Sections: the product · the questions buyers ask · the fitter's answer · activation.

```text
hero  three material samples propped against a wall in a bare showroom, subject to the right
bg02  a cladding panel held up to a facade, the gap it will fill still open
bg03  two mugs on a site table either side of an open folder
bg04  a tool belt hanging on a nail beside a half-clad wall
bg05  a flip chart on an easel in an empty meeting room, the sheet blank
```

### `workplace-roleplay/` — B2→C1: Workplace Roleplay, Live Speaking — stem B, 7 frames

Has: `LibraryCards/workplace-roleplay.jpg`, 1200×512. Six scenes, each acted twice
with roles swapped — so six section backgrounds, and the hero is the seventh frame.
Scenes: the missed deadline · the intake · the partnership · the coaching call ·
the bad news · the boardroom.

```text
hero  two chairs facing each other across the corner of a production office, subject to the right
bg02  a wall planner with one card three columns behind the rest
bg03  an open notebook and a pen on a desk, the page ruled and empty
bg04  two name cards on a meeting table, one turned away from the room
bg05  a whiteboard with a schedule half rubbed out and redrawn over itself
bg06  a laptop open and turned to face the other side of the desk
bg07  a long boardroom table with one chair at the head pulled out
```

### `linking-devices-cars/` — B2: Linking Devices, The World of Cars — stem B, 5 frames

Has: `LibraryCards/linking-devices-cars.jpg`, 1200×600. 15 items in three activities.
Sections: choosing the linker · dragging it into the gap · reordering the sentence ·
activation.

```text
hero  a motorway junction from above, two carriageways merging into one, subject to the left
bg02  a jump lead clipped to a battery terminal, the other clip hanging free
bg03  a timing chain laid out on a workshop cloth, one link opened
bg04  a tow rope pulled taut between two bumpers on an empty road
bg05  a roundabout seen from above with five exits and one car on it
```

### `decision-making/` — C1: Decision-Making Under Uncertainty — stem B, 5 frames

Has: `LibraryCards/decision-making.jpg`, 1200×512. Three parts plus roleplay.
Sections: vocabulary in context · discussion · roleplay · activation.

```text
hero  a fork in a road running into fog, the signpost legible and the road not, subject to the right
bg02  a weather map pinned to a wall, the isobars crossing the coast, one pin holding it
bg03  a round table with five chairs, one pushed back from the table
bg04  a coin standing on its edge on a bare desk under hard light
bg05  a torch beam thrown down a corridor that turns before it ends
```

### `ChampionsLeague/` — C1: Champions League English — stem C, 6 frames

Has: `ChampionsLeague/trophy-hero.jpg`, 1200×671. Five sections, all of them night
football — this is the clearest stem C candidate in the list.
Sections: vocabulary · commentary · grammar · visual English · the quiz · activation.

```text
hero  an empty stadium bowl under floodlights at night, one gate standing open, subject to the left
bg02  nine cards face down on a bare surface, one turned face up
bg03  a commentary desk with two headsets and one microphone, the pitch out of focus beyond
bg04  a tactics board with a back four pushed up as a single line
bg05  a fourth official's board held up, its panel blank
bg06  an empty plinth in a floodlit corridor, the trophy not on it
```

### `RidgelineRun/` — C1: The Ridgeline Run (roleplay) — stem A, 7 frames

Has: `RidgelineRun/cliff-ridge-hero.jpg`, 1200×671. Seven scenes on a branching
roleplay with a Trail Confidence meter, Basque foothills at first light — keep every
frame bright, the deck stays light.

```text
hero  a ridge line dropping away into the Basque foothills at first light, subject to the right
bg02  a bike leaning against a gate at the trailhead, mist in the valley below
bg03  a fire road forking, one branch rutted and one smooth
bg04  a rock slab with a single tyre line across it
bg05  a beech wood with the trail disappearing between the trunks
bg06  a punctured tyre and a pump laid on the grass at the side of a trail
bg07  a col at the top with the whole range visible beyond, one bike laid down
```

### `FeedbackThatLands/` — B2–C1: Feedback That Lands — stem B, 6 frames

Has: `FeedbackThatLands/group-feedback-hero.jpeg`, 900×504 — the smallest file in the
whole list. Four professionals, a BBC Reel video to watch first, eight languages
already in the switcher.
Sections: watch first · vocabulary · the four readings · grammar · activation.

```text
hero  four chairs in a loose circle on a plain floor, one turned slightly inward, subject to the left
bg02  a screen on a stand in a dim room, the frame lit and blank
bg03  a stack of four folders on a desk, each a different thickness
bg04  a hand-width gap between two stacked books on an otherwise full shelf
bg05  a mirror propped against a wall facing an empty chair
bg06  two coffee cups on a low table, one full and one drained
```

### `UnderLoad/` — B2: Under Load (Spanish support) — stem B, 5 frames

Has: `UnderLoad/hero.jpg`, 1200×671. Three stages — CLINIC, FORM, PRESENT — and 48
points.
Sections: the clinic · the form · the presentation · activation.

```text
hero  a steel beam carrying the floor above it, a single prop under its centre, subject to the right
bg02  a dial gauge with the needle well into the upper third of its scale
bg03  a truss drawn out in chalk on a concrete floor
bg04  a lectern with a clicker on it facing an empty hall
bg05  a microphone on a stand in an empty seminar room, one chair turned outward
```

### `TakingItApart/` — A2: Taking It Apart (Spanish support) — stem A, 5 frames

Has: `TakingItApart/hero.jpg`, 1200×671. Stages READ, TEST, PRESENT; the verbs on the
page are SCAN, UNSCREW, LIFT, REMOVE, SORT, so the frames follow that sequence.
Sections: the reading · the test · the presentation · activation.

```text
hero  a device laid open on a bench with its parts in a neat row beside it, subject to the left
bg02  a screwdriver upright in a screw head, three loose screws in a shallow dish
bg03  a magnifying glass over a circuit board on a cutting mat
bg04  four shallow trays on a bench, each holding one kind of part
bg05  a reassembled device standing upright, one spare screw on the bench beside it
```

### `mtb2/` — B1: MTB English — stem A, 5 frames

Has: `mtb2/two-riders-hero.jpg`, 1200×600. Four sections. **Do not borrow from
`MTB/`** — that folder's single frame belongs to `mtb-perfect-vs-simple.html`, and two
lessons on one picture is how the Block Camp repetition started.
Sections: vocabulary · reading · grammar · speaking (which is the activation).

```text
hero  two riders on a ridge at first light with the trail dropping away in front of them, subject to the right
bg02  a wall of bike parts on hooks in a workshop, one hook empty
bg03  a fire road curving into pine forest with tyre tracks in the dust
bg04  a fork and a pair of grips laid out on a workshop cloth
bg05  a finish arch at the foot of a hill, nobody through it yet
```

### `Golf/` — B1 **(free)**: Golf Edition, Past Simple vs Present Perfect — stem A, 6 frames

Has: `Golf/fairway-dusk-hero.jpg`, 1200×671. **This one is free to the public**, which
makes it the highest-traffic lesson in Wave 1 and the one to generate first after
Quebert.
Sections: theory · past simple · present perfect · the contrast · activation.

```text
hero  a fairway at dusk with one flag on a distant green, subject to the left
bg02  a scorecard and a pencil on a bench, the card blank
bg03  a replaced divot in the turf, the ball already gone
bg04  a bag of clubs standing on the tee with one slot in the row empty
bg05  a leaderboard frame with every slot empty
bg06  a putting green with one ball resting on the lip of the hole
```

### `Venezuela/` — B1–B2: Venezuela Edition, *used to* — stem A, 5 frames

Has: `Venezuela/hacienda-hero.jpg`, 1200×671. The grammar is habits and states that
ended, so every frame should be a thing that is no longer used.
Sections: the grammar · practice · the oil years · activation.

```text
hero  a low hacienda on an open plain under a huge sky, subject to the right
bg02  a rocking chair on a veranda, still
bg03  a nodding-donkey oil pump standing on an empty plain, long shadow
bg04  a long table laid for more people than are coming, the chairs pushed in
bg05  a dirt road running to the horizon with a bicycle leaning on a fence post
```

### `FashionFilm/` — B1–B2: The Grammar Atelier (Vivienne Westwood) — stem A, 6 frames

Has: six frames at 1000×559 — all of them under spec, so the whole folder is
regenerated. Two collections: Syntax & Form, and Extension — Real Mistakes.
Sections: collection I theory · collection I practice · collection II · the mistakes ·
activation.

```text
hero  a tailor's dummy in a half-pinned jacket under a bare bulb, subject to the left
bg02  a bolt of tartan half unrolled across a cutting table
bg03  a paper pattern pinned flat with the seam lines drawn on it
bg04  a rail of finished garments with one hanger empty
bg05  scissors and a pincushion on a mirror-backed shelf
bg06  a runway seen end-on, empty, the lights up
```

---

## 6. Wave 2 — the thirty-three lessons with no picture at all (thirty-two briefed)

Nothing on disk, nothing in the card map. The subject is a free choice, so each brief
below picks one that carries the grammar rather than decorating it.

`preview.html` is deliberately absent — see §7.

### A1–A2

**`question-words-a0/` — A0–A1: Question Words (German support) — stem A, 5 frames**
Sections: the pattern · who/what/where · when/why/how · practice · activation.

```text
hero  a signpost with six blank arms at a crossroads on an open plain, subject to the left
bg02  a doorbell panel with six unmarked buttons beside a front door
bg03  a lost-property shelf with one glove, one umbrella and one hat on it
bg04  a railway platform clock and an empty bench beneath it
bg05  a map spread on a table with one pin in it and a magnifying glass beside it
```

**`penguins/` — A1: Penguins of the Past (German support) — stem A, 6 frames**
Sections: the story · the past simple · positive · negative · question · activation.

```text
hero  a line of penguins crossing an ice shelf toward open water, subject to the right
bg02  a single set of webbed tracks in snow leading away from the camera
bg03  an ice floe with one penguin standing on it under a low sun
bg04  a colony seen from a distance as small dark marks on white
bg05  a penguin diving, seen from under the surface as a silhouette
bg06  an empty nest hollow in a pebble field with two pebbles beside it
```

**`present-simple-continuous-de/` — A1: Present Simple vs Continuous (Supereasy) — stem A, 4 frames**
Sections: the two tenses · the practice · activation.

```text
hero  a bus stop with a timetable board on one side and a bus arriving on the other, subject to the left
bg02  a kettle on a stove with the steam just starting
bg03  a wall calendar with the same mark on every Monday
bg04  a front door half open with a coat going through it
```

**`busch-gardens/` — A2: Past Simple, Busch Gardens Tampa (Spanish support) — stem A, 6 frames**
Sections: vocabulary · the grammar · positive · negative · questions · activation.

```text
hero  a wooden rollercoaster seen against a flat Florida sky, one empty car at the top, subject to the right
bg02  a park map board and a turnstile at an open gate
bg03  a big cat asleep on a rock in a savannah enclosure
bg04  a ferris wheel stopped with all its cars empty
bg05  a queue rail folded back and forth with nobody in it
bg06  a souvenir photo booth with a blank screen and a bench in front of it
```

**`swiss-mistakes/` — A2: Swiss Precision English, Part 1 — stem A, 6 frames**
32 items for German speakers. SBB world — clocks, platforms, precision.
Sections: false friends · word order · prepositions · verb forms · activation.

```text
hero  a station clock on a platform canopy with a train just leaving, subject to the left
bg02  two identical suitcases side by side, one tag turned the wrong way
bg03  a departure board frame with all its flaps blank
bg04  a funicular halfway up a slope, the cable running out of frame
bg05  a pocket watch open on a workbench beside a loupe
bg06  a bench on an empty platform with one coat left on it
```

**`swiss-mistakes-2/` — A2: Swiss Precision English, Part 2 — stem A, 5 frames**
Pronunciation, vocabulary and word order. Same look, different frames.
Sections: pronunciation · vocabulary · word order · activation.

```text
hero  a cog railway climbing out of a valley under a hard blue sky, subject to the right
bg02  a tuning fork on a marble sill beside an open window
bg03  a row of cowbells on a rail, one out of line
bg04  three signposts on one post pointing three ways
bg05  a cable car cabin stopped mid-span with the valley below
```

**`grammar-dojo/` — A2: Grammar Dojo, must vs have to (coding edition) — stem C, 5 frames**
Sections: must · have to · mustn't vs don't have to · the ranked practice · activation.

```text
hero  a dojo floor at night lit by one low window, a single mat square lighter than the rest, subject to the left
bg02  a folded belt on a bare wooden step
bg03  a rack of practice staves, one slot empty
bg04  a sliding screen half open onto a dark corridor
bg05  a low table with a single cushion behind it, facing the room
```

**`might-vs-going-to/` — A2: Might vs Going To (German support) — stem A, 4 frames**
Sections: might · be going to · the 15-item test · activation.

```text
hero  a sky split between clear blue and a bank of cloud over a flat plain, subject to the right
bg02  a coin mid-spin on a table top
bg03  a packed suitcase standing by a door with a ticket on top of it
bg04  two umbrellas in a stand by a doorway, one open to dry
```

### B1

**`cheat-sheets/` — B1: Grammar Cheat Sheet ×3 (DE, IT, Question Forms) — stem A, 6 frames**
Three reference lessons off one folder — the two language editions are the same
eighteen structures, so they take the same hero, and Part 2 takes its own.
Allocation: `hero`, `bg02`, `bg03` for the eighteen-structure pair; `hero-b`, `bg04`,
`bg05` for Question Forms.

```text
hero    a pegboard with eighteen small tools hung in rows, every hook filled, subject to the left
bg02    a card index open at one divider, the cards behind it square in the drawer
bg03    a set of measuring spoons on a ring, laid out in size order
hero-b  a door with a spyhole in it seen from the inside of a bare hall, subject to the right
bg04    a row of pigeonholes with one envelope in one of them
bg05    a bell push on a plain wall with a wire running away from it
```

**`ecommerce-b1/` — B1: E-commerce Vocabulary (Italian support) — stem B, 5 frames**
18 items, one quiz.
Sections: browsing and buying · checkout and delivery · returns and refunds · activation.

```text
hero  a stack of parcels on a doorstep against a plain door, subject to the left
bg02  a shopping basket on a bare floor with one item in it
bg03  a card reader on a counter with the terminal screen dark
bg04  a parcel with the tape already cut, the flaps standing up
bg05  a delivery locker bank with one door open
```

**`gerunds-de/` — B1: Subjects, Objects & the Gerund (German speakers) — stem B, 6 frames**
Sections: the theory · German vs English · the exercises · the advanced set · activation.

```text
hero  three blocks in a row on a plain surface, the middle one turned ninety degrees, subject to the right
bg02  a sentence of wooden type set in a composing stick
bg03  two identical toolboxes open side by side, the contents arranged differently
bg04  a conveyor belt carrying one box toward a gap in a wall
bg05  a stack of rings on a post, one lifted clear above the rest
bg06  a bare desk with one open notebook and a pen laid across it
```

**`common-mistakes-1/`, `-2/`, `-3/`, `-b1-b2/` — B1 / B1–B2: Common Mistakes Review — stem A, 5 frames each, 20 in total**
Four lessons in one series (three Spanish-support parts plus the B1–B2 review).
**One folder each, not one pool.** Three decks off a shared pool is exactly the
allocation bug logged against Block Camp; four five-frame folders cost the same to
generate and cannot repeat.
Each: hero · two practice sections · one review section · activation.

```text
common-mistakes-1
hero  a proof sheet on a desk with one line marked in the margin, subject to the left
bg02  a pair of shoes by a door, one facing in and one facing out
bg03  two mugs on a shelf, one upside down
bg04  a light switch plate with one switch up and one down
bg05  a blank postcard and a pen on a café table

common-mistakes-2
hero  a row of hooks with coats on all but one, subject to the right
bg02  a bicycle with one pedal at the top of its stroke
bg03  a chess board mid-game with one piece off the board beside it
bg04  a jar of buttons with one button on the table beside the jar
bg05  an open window with a curtain drawn half across it

common-mistakes-3
hero  a set of keys on a ring with one key separated from the rest, subject to the left
bg02  a staircase with one tread a different colour
bg03  a bookshelf with one book pulled out an inch
bg04  a plug beside a socket, not in it
bg05  a notebook open at a page with one line written

common-mistakes-b1-b2
hero  a long corridor of identical doors with one standing ajar, subject to the right
bg02  a tiled wall with one tile set at a slight angle
bg03  a stack of plates with the top one offset
bg04  a line of parked bicycles with one wheel turned out
bg05  a table set for two with one chair pulled out
```

**`us-civics/` — B1: Civics & Government Vocabulary — stem B, 6 frames**
20 questions in four activities.
Sections: how government works · key facts and numbers · term and definition ·
fact or myth · activation.

```text
hero  a domed capitol seen down a long avenue in flat morning light, subject to the left
bg02  three columns of a portico, one taller than the other two
bg03  a ballot box on a trestle table in an empty hall
bg04  a gavel and its block on a bare bench
bg05  a flag folded into a triangle on a shelf
bg06  a lectern with a microphone facing an empty room
```

**`grammar-formulas/` — B1: German Grammar Formula Reference I & II — stem A, 4 frames**
Two reference lessons, thirteen structures each.
Allocation: `hero`, `bg02` for Part I; `hero-b`, `bg03` for Part II.

```text
hero    a set of stencils laid out in a row on a drawing table, subject to the right
bg02    a slide rule open on a bare desk
hero-b  a printer's tray of type with the compartments part filled, subject to the left
bg03    a folding ruler opened into a shape on a workbench
```

**`present-perfect-test-de/` — B1: Present Perfect, Übungsheft Teil 3 — stem A, 5 frames**
Sections: the structure · already / yet / just · ever / never · activation.

```text
hero  a suitcase by a front door with the labels of several journeys still on it, subject to the left
bg02  a glass on a table with a ring of condensation beside it where another stood
bg03  a tube of toothpaste squeezed flat, cap off
bg04  a passport open flat with the pages stamped, no dates legible
bg05  a wall of photographs with one frame hanging empty
```

**`teil3-part2/` — B1: Adverbs, Will & So/Neither — stem A, 5 frames**
15 questions, three topics.
Sections: adverbs · will and won't · so / neither · activation.

```text
hero  a runner's shadow long across an empty track, subject to the right
bg02  a metronome on a piano lid, the weight near the top
bg03  a weather vane against a flat sky
bg04  two identical chairs side by side facing the same way
bg05  a pair of footprints in sand, side by side, walking out of frame
```

### B2

**`buying-selling-online/` — B2: Buying, Selling & Sharing Online — stem B, 6 frames**
Sections: vocabulary and common mistakes · prepositions and collocations · the Italian
gloss · spot the correct sentence · activation.

```text
hero  a kitchen table set up as a packing station, one parcel taped and one open, subject to the left
bg02  a phone face up on a desk beside a stack of coins
bg03  a set of bathroom scales with a parcel on them
bg04  two hands' worth of gap between a shelf and the box that came off it
bg05  a doorstep with a parcel and a chalk mark beside it
bg06  a market stall trestle, bare, with one crate underneath
```

**`honda-type6/` — B2: Past Simple, Honda Civic Type 6 — stem A, 6 frames**
Four acts plus a grammar reference.
Sections: regular verbs · irregular verbs · the car, past and present · mixed
practice · activation.

```text
hero  a low coupé in three-quarter view on an empty road under a flat sky, subject to the right
bg02  a rev counter with the needle at rest
bg03  a workshop pit with a car above it and one lamp on
bg04  two badges side by side on a bench, one worn and one new
bg05  a gear lever in an empty cabin, the gate visible
bg06  an empty starting grid box painted on tarmac
```

**`vocab-test-b1/` — B1+: Vocabulary Test (30 points, four activities) — stem B, 5 frames**
Sections: match the definition · the gap fill · the collocations · activation.

```text
hero  a wall of small labelled drawers, one pulled half out, subject to the left
bg02  a dictionary open flat with a ribbon marker across the gutter
bg03  a keyring with five keys, one held apart from the rest
bg04  a pegboard with tools grouped by kind, three hooks empty
bg05  a blank index card and a pencil on a plain desk
```

**`full-vocabulary-test/` — B2: Vocabulary Test, full word list — stem B, 5 frames**
32 questions in three sections plus a glossary. Shares its word list with
`contingency/` (durability, airtight, shortfall, retrofit) — **same stem and palette,
different frames**, so the two read as a pair without repeating.
Sections: the newer set · the review set · words with two meanings · the glossary.

```text
hero  a long shelf of identical jars, one with its lid off, subject to the right
bg02  a tape measure extended across a workbench and left there
bg03  a sealed box with one corner of tape lifted
bg04  a coin balanced on its edge showing neither face
bg05  a card index drawer closed but for one card standing proud
```

**`gaming-youtube/` — B2: Gaming YouTubers — stem C, 5 frames**
16 questions in three activities.
Sections: channel knowledge · gaming vocabulary · strategy reordering · activation.

```text
hero  a desk at night lit only by a monitor, an empty chair pushed back, subject to the left
bg02  a ring light on a stand facing an empty stool
bg03  a stack of game cases beside a controller on a rug
bg04  a mixing desk with one fader up and the rest down
bg05  a wall of small screens all showing the same blank frame
```

### C1–C2

**`body-parts/` — C1: Anatomy of a Sentence — stem B, 6 frames**
61 points in five sections. Serves both `forbes-english-body-parts-c1.html` and the
Chinese-support build `-c1-zh.html` — one lesson, two language editions, one folder.
Sections: face & neck · torso & organs · limbs & extremities · idioms in context ·
actions & purposes · activation.

```text
hero  an anatomical mannequin on a stand against a plain wall, subject to the right
bg02  a barber's mirror and chair in an empty shop
bg03  a ribcage of curved timber formers on a boatbuilder's floor
bg04  a row of gloves and boots drying on pegs, unmatched
bg05  a set of hand tools laid out in size order on a cloth
bg06  a single footprint in wet cement on a pavement
```

**`coding-interview/` — C1: Tech Interview Masterclass — stem B, 6 frames**
22 questions in four activities.
Sections: talking through your thinking · technical vocabulary · interview strategy ·
sentence transformation · activation.

```text
hero  a whiteboard wiped clean but for one faint diagram, a marker on the tray, subject to the left
bg02  a flowchart drawn in chalk on a dark floor, one branch unfinished
bg03  a patch panel with the cables run neatly but two ports empty
bg04  a chess clock on a bare table with both flags up
bg05  a stack of index cards fanned slightly, all blank
bg06  a chair on one side of a desk and two on the other
```

**`barbi-coo/` — C2: The COO Briefings, executive roleplays — stem B, 7 frames**
Six dossiers, three target phrases each; the hero is the seventh frame.
Scenes: the escalation · the intake · the partnership · the coaching · the bad news ·
the boardroom.

```text
hero  a corner office at dusk with one lamp on and the desk clear, subject to the right
bg02  a phone off its cradle on an otherwise empty desk
bg03  a folder open at the first page on a meeting table
bg04  two chairs drawn up to the same side of a table
bg05  a coffee cup and a notebook on a windowsill above a city
bg06  a closed door with a light showing underneath it
bg07  a long table with a single glass of water at the head
```

**`barbi-phrase-test/` — C2: The COO Briefings, companion phrase test — stem B, 5 frames**
22 items in four parts, all produced out loud — no multiple choice.
Sections: cloze from the dossiers · matching · transformation · freestyle.

```text
hero  a lectern in an empty room with a single sheet on it, face down, subject to the left
bg02  a sentence of wooden type with three sorts lifted out and set aside
bg03  two cards face down on a table, slightly apart
bg04  a hand-turned mangle with a sheet half through it
bg05  an open window onto a street, the curtain lifting
```

---

## 7. One of the 52 is a decision, not a commission

**`preview.html` — A1 Possessive Pronouns.** Do not generate art for it until it has
been diffed against `forbes-english-possessive-pronouns-a1.html`, which is already a
17-slide deck on `Possessives/hero.jpg` (2944×1648). Same level, same grammar
(possessive adjectives and pronouns taught together), same German support, same worked
examples down to *my bag → it's mine* and the classroom coats. The filename is the
tell: `preview.html` reads as a pre-rebuild original that was never retired.

Follow the 2026-09-03 method — **diff the question data, not the filenames** — and if
it is the same lesson, it becomes a ~950-byte redirect stub at the deck, exactly as
`forbes-english-ope- say in your words.html` did. That is one lesson off this list for
no artwork at all, and it is the cheapest item in the file.

Two more entries are one lesson wearing two files, and are already briefed that way
above: `forbes-english-body-parts-c1.html` / `-c1-zh.html` (one folder, two language
editions) and the two `cheat_sheet` language editions.

---

## 8. What this file does **not** cover — the §5c top-up queue

§5c (one background per section, plus activation) also catches lessons that *do* have
a usable hero but not enough of them. They are not blocked the way the 52 are — a
session can start one and stop at the shortfall — so they get a list, not briefs.
**Count images against sections before starting any of these** (§5c), and commission
the gap rather than reusing the hero across sections.

**One usable image only (28).** `snack-attack-a1` · `forbes-english-tennis-present-perfect-a2` ·
`forbes-tennis-a2` · `Race Day - The Falcon Racing Story` · `eintracht-gerunds-lesson` ·
`forbes-english-b1-adjective-order-escape-room` · `forbes-english-b1-mixed-grammar-test` ·
`-part2` · `mtb-perfect-vs-simple` · `phrasal_verbs_test` · `case-file-b2-roleplay` ·
`expressions_take_put_ES` · `_PL` · `_v2` · `forbes-english-bronte-lesson` ·
`forbes-english-negotiating part2` · `forbes-english-skyline-lego-b2` ·
`forbes-english-writers-nightmare` · `impostor_syndrome_lesson` · `thornwick-deduction` ·
`forbes-dartboard-c1` · `forbes-dnd-rpg` · `-part2` · `forbes-english-architecture-c1 (1)` ·
`forbes-english-c1-scooter-tricks` · `forbes-english-the-ten-year-bet-C1` ·
`forbes-interior-design-c1` · `interior-design-vocabulary`.

`Impostor2/hero.jpg` (3376×1440) is on disk and referenced by nothing — check it
against `impostor_syndrome_lesson` before ordering anything for that one.

**Two to four (28).** The Water Polo pair · Ecuador pair · Skiing pair · Tennis pair ·
fashion trio · Wild Frame pair · Reddit French pair · `prepositions_crime_lesson (fixed)` ·
`present-simple-vs-continuous` · `forbes-english-b1-modal-verbs-fire-brigade` ·
`marilyn_prepositions` · `active_passive_refinery_quiz_part2` ·
`alchemist_present_perfect_lesson` · `forbes-english-lesson (B2)` ·
`forbes-english-construction-presentations` · `forbes-english-frankfurt-2-lesson` ·
`forbes-english-hiking-c1-part2` · `forbes-english-lesson (data)` ·
`forbes-english-tolle (2)` · `friedrich_prepositions_c1` · `reading-a-room-cafe-kowloon` ·
`geopolitics-english-class`.

Skiing, Tennis and Water Polo are the three families the 2026-09-13 §5c entry already
flagged as open on a two-image set; they are still open, and still not audited
section-by-section.

---

## 9. After the pictures land

Nothing in this file is finished by generating images. The rest is a session's work,
and it is the standard pipeline:

```bash
python3 tools/prep-artwork.py incoming/<folder> --into <Folder>   # 2000px q85, refuses repeats
python3 lesson-template/extract-palette.py <Folder>/hero.jpg      # --light if the hero is bright
python3 lesson-template/build/build_<name>.py                     # new builder, deck.py + chrome_i18n.py
node   lesson-template/check-lesson.js <lesson>.html              # must exit clean
node   lesson-template/check-library.js --vs-origin               # must PASS before library.html moves
python3 tools/build_hubs.py
python3 tools/seo.py                                              # ALWAYS last
```

Three things that apply to every lesson on this list specifically:

1. **Fifty-one of the 52 are English-only or English plus one gloss language** —
   German, Spanish, Italian or Chinese, usually as inline translation rather than a
   switcher. The exception is `feedback-that-lands.html`, which already carries eight.
   The standing minimum since 2026-09-04 is EN + DE + ES, so
   `assemble(langs=('en','de','es'))` — and the Spanish has to be written; it is not a
   missing argument sitting behind a default.
2. **Only one of the 52 has an activation stage** — `feedback-that-lands.html` again.
   The rest end on a score. Rule 6 means the rebuild adds a speaking and a writing
   task, which is why the last frame in nearly every brief above is an activation
   background. The six speaking lessons on the list — `workplace-roleplay`,
   `barbi-coo`, `barbi-phrase-test`, `ridgeline_run`, `speaking-2` and
   `material-space-speaking` — are production from end to end, so their last frame
   frames the task rather than introducing a new one.
3. **Check the MC keys before trusting the source data.** Every lesson here predates
   `deck.assert_no_key_is_longest` and the ANSWERS gate; the recurring defect is all
   keys at index 0 and the correct option written longest. Read the question data with
   that in mind rather than porting it wholesale.

---

## 10. The totals

| | Lessons | Folders | Frames |
|---|---|---|---|
| Wave 1 — picture too small | 19 | 19 | 106 |
| Wave 2 — no picture at all | 32 | 28 | 149 |
| Decide, don't commission | 1 | — | — |
| **Total** | **52** | **47** | **255** |

Generate in this order, and each step is independently useful:

1. **`quebert/`** — the lesson that was asked about, 6 frames.
2. **`Golf/`** — the only free lesson on the list, so the only one a visitor can hit
   without subscribing, 6 frames.
3. **The rest of Wave 1** — 19 rebuilds unblocked for 106 frames, and the subject is
   already decided for every one of them.
4. **Wave 2 by level**, A1 upward: the A1–A2 end is where a scrolling page hurts most,
   because those learners are the least able to cope with a wall of text.

One lesson's folder is enough to start a build. Nothing here needs to arrive complete.

---

## 11. Index — every one of the 52, and where its frames go

The first nineteen are Wave 1. `frames` is blank on a lesson that shares its
folder with the line above. Cross-check with
`python3 tools/audit-artwork.py --blocked`, which prints exactly these 52 files.

| # | Lesson file | Level | Folder | Stem | Frames |
|---|---|---|---|---|---|
| 1 | `harry-quebert-b2.html` | B2 | `quebert/` | C | 6 |
| 2 | `forbes-architectural-vocabulary.html` | C1 | `material-space/` | B | 5 |
| 3 | `forbes-architectural-vocabulary-part2.html` | C1 | `material-space-speaking/` | B | 5 |
| 4 | `contingency-trade-offs-vocab.html` | C1 | `contingency/` | B | 6 |
| 5 | `dailies-review-feedback.html` | C1 | `dailies-review/` | B | 5 |
| 6 | `vapour-barriers-lesson.html` | B2 | `vapour-barriers/` | B | 6 |
| 7 | `forbes-english-speaking-2.html` | B2 | `speaking-2/` | B | 5 |
| 8 | `workplace-roleplay-live.html` | B2 | `workplace-roleplay/` | B | 7 |
| 9 | `forbes-linking-devices-cars.html` | B2 | `linking-devices-cars/` | B | 5 |
| 10 | `Forbes English - Decision-Making Under Uncertainty.html` | C1 | `decision-making/` | B | 5 |
| 11 | `champions_league_english.html` | C1 | `ChampionsLeague/` | C | 6 |
| 12 | `ridgeline_run.html` | C1 | `RidgelineRun/` | A | 7 |
| 13 | `feedback-that-lands.html` | B2 | `FeedbackThatLands/` | B | 6 |
| 14 | `under-load-b1-b2-es.html` | B2 | `UnderLoad/` | B | 5 |
| 15 | `takingitaparta2es.html` | A2 | `TakingItApart/` | A | 5 |
| 16 | `mtb-english-lesson.html` | B1 | `mtb2/` | A | 5 |
| 17 | `forbes-english-golf-lesson.html` | B1 · **free** | `Golf/` | A | 6 |
| 18 | `forbes-english-venezuela.html` | B1 | `Venezuela/` | A | 5 |
| 19 | `vw_grammar_atelier_final.html` | B1 | `FashionFilm/` | A | 6 |
| 20 | `Forbes_English_A0_Question_Words.html` | A1 | `question-words-a0/` | A | 5 |
| 21 | `penguins_past_simple (2).html` | A1 | `penguins/` | A | 6 |
| 22 | `present_simple_continuous_de.html` | A1 | `present-simple-continuous-de/` | A | 4 |
| 23 | `busch_gardens_english_lesson.html` | A2 | `busch-gardens/` | A | 6 |
| 24 | `forbes-english-swiss-mistakes-a2.html` | A2 | `swiss-mistakes/` | A | 6 |
| 25 | `forbes-english-swiss-mistakes-a2-part2.html` | A2 | `swiss-mistakes-2/` | A | 5 |
| 26 | `grammar-dojo.html` | A2 | `grammar-dojo/` | C | 5 |
| 27 | `might_vs_going_to_test.html` | A2 | `might-vs-going-to/` | A | 4 |
| 28 | `cheat_sheet.html` | B1 | `cheat-sheets/` | A | 6 |
| 29 | `cheat_sheet_italian.html` | B1 | `cheat-sheets/` | A |  |
| 30 | `cheat_sheet_part2.html` | B1 | `cheat-sheets/` | A |  |
| 31 | `ecommerce-vocabulary-b1.html` | B1 | `ecommerce-b1/` | B | 5 |
| 32 | `english-lesson-gerunds.html` | B1 | `gerunds-de/` | B | 6 |
| 33 | `forbes-english-common-mistakes-review.html` | B1 | `common-mistakes-1/` | A | 5 |
| 34 | `forbes-english-common-mistakes-review-part2.html` | B1 | `common-mistakes-2/` | A | 5 |
| 35 | `forbes-english-common-mistakes-review-part3.html` | B1 | `common-mistakes-3/` | A | 5 |
| 36 | `forbes-english-common-mistakes-b1-b2.html` | B1-B2 | `common-mistakes-b1-b2/` | A | 5 |
| 37 | `forbes-english-us-civics-b1.html` | B1 | `us-civics/` | B | 6 |
| 38 | `grammar_formulas.html` | B1 | `grammar-formulas/` | A | 4 |
| 39 | `grammar_formulas_part2.html` | B1 | `grammar-formulas/` | A |  |
| 40 | `present_perfect_test.html` | B1 | `present-perfect-test-de/` | A | 5 |
| 41 | `teil3_part2_test.html` | B1 | `teil3-part2/` | A | 5 |
| 42 | `Forbes English - Buying Selling Sharing Online (B2).html` | B2 | `buying-selling-online/` | B | 6 |
| 43 | `forbes-b2-past-simple-type6.html` | B2 | `honda-type6/` | A | 6 |
| 44 | `forbes-english-vocab-test.html` | B2 | `vocab-test-b1/` | B | 5 |
| 45 | `full-vocabulary-test.html` | B2 | `full-vocabulary-test/` | B | 5 |
| 46 | `forbes-gaming-youtube-b2.html` | B2 | `gaming-youtube/` | C | 5 |
| 47 | `forbes-english-body-parts-c1.html` | C1 | `body-parts/` | B | 6 |
| 48 | `forbes-english-body-parts-c1-zh.html` | C1 | `body-parts/` | B |  |
| 49 | `forbes-coding-interview-c1.html` | C1 | `coding-interview/` | B | 6 |
| 50 | `forbes-english-c2-barbi-executive-roleplays.html` | C2 | `barbi-coo/` | B | 7 |
| 51 | `forbes-english-c2-barbi-phrase-test.html` | C2 | `barbi-phrase-test/` | B | 5 |
| 52 | `preview.html` | A1 | `— decide first (§7)` | — |  |
| | **52 lessons** | | **47 folders** | | **255** |
