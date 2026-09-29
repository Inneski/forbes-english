# Artwork shopping list — every lesson still outside the house style

Asked for on 2026-09-27: *"find the non house style lessons and create art
shopping list for revamp."* Measured 2026-09-29 against `tools/lessons.json`
(324 rows), the files on disk and the artwork folders. Regenerate rather than
trust: the method is at the bottom.

## The numbers

| | |
|---|---|
| Catalogued lessons | 324 |
| House-style decks (`class="stage-wrap"` in the file) | **140** — the catalogue's `deck` flag says 136; ten decks are flagged false and six non-decks flagged true, see §12 |
| Block Camp RPGs (`block-camp/`, their own standard) | 14 |
| Sherpa Tensing pages (their own pattern; deck redesign stopped by Innes 2026-09-25) | 26 |
| **Still a scrolling page, not to house style** | **144** |
| — of which leave alone (§11: art quarry, Innes's own decks, finished RPGs) | 19 |
| — **revamp candidates** | **125** |
| — of which merge or retire before ordering art (§10) | 11 |
| **Rows in the list** | **110** (a row is a lesson, a pair or a family; 11 of them order nothing) |
| **Plates to order** | **545** (of 655 slots; 105 usable pictures already on disk) |

How "need" is counted, per HOUSE-STYLE §5c and the panel briefs since
2026-09-23: **one cover, one plate per section or activity, one for the
activation stage**, capped at eight (a page with more sections than that
becomes two decks). "On disk" counts only pictures at least 1400 px wide and
landscape, in the lesson's own folder or one it already borrows from; library
thumbnails (`LibraryCards/`, `*-thumb.jpg`, 1200×671 cards) and the IELTS
placeholder cards are not artwork and count as zero. **Nothing on disk has
been checked by eye for style** — a 2944×1648 Midjourney render is counted
as usable, and the 2026-09-24 note stands: a filename is not evidence of
style. Expect some of the "have" pictures to be photographic or painterly and
to need re-rendering once the family is opened.

## The style, stated once

Innes's call of 2026-09-24: **Noma Bar** — flat shapes, solid colour, one
idea in negative space. Reference set: `HOUSE STYLE/` at the repo root. The
layout is **house style 2, the panel** (HANDOFF 2026-09-25): every plate is
used full-bleed on a divider *and* as a 548×720 portrait slice beside the text,
so the subject must sit inside one vertical third of the frame. Every prompt
below is `<subject>, <stem>`:

```text
flat vector illustration, cel-shaded, solid flat colour, minimalist, Noma Bar style, one idea in negative space, wide landscape, cream and dusty pink and coral with slate-blue and black silhouettes, bright and airy, no text, no letters, no logos, no signage, no faces, subject contained in the <THIRD> of the frame with empty flat ground either side --ar 16:9 --style raw --no photorealistic, gradient, texture, grain, depth of field, perspective
```

- `<THIRD>` is `left third`, `centre` or `right third`. Alternate sides down
  a deck; the builder's `pos=` picks the slice. Covers keep the middle calm
  (the lockup sits there).
- The palette words are per family, not per lesson: business decks have used
  slate blue and warm salmon; the editorial pair slate, blush and brick.
  Swap the colour phrase, keep the rest.
- **Activation plates are a pair-speaking motif** — two seats, two cups, two
  stools — never a still life (Mixed Grammar and Contingency briefs).
- **No text in any picture.** Several subjects below are documents,
  signs or screens: ruled lines and blocks, never letters.
- Deliver at 2000 px wide or more, upscaled; anything under 1400 px is
  skipped by `prep-artwork.py`. Drop batches in `incoming/<lesson>/`, five
  files a batch, then `/publish`.
- Subjects are written as *ideas*, not scenes, because a Noma Bar brief that
  names a place gets you a place. Where a family already owns a picture the
  new plates should sit beside it, so the "have" column names what is there.

Columns: **need** = slots the deck wants; **have** = usable on disk;
**order** = need minus have, or the full count where the disk art is the
wrong picture. The plate list runs cover first, activation last.

---

## 1. Already briefed, do these first

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `forbes-english-body-parts-c1.html` + `forbes-english-body-idioms-c1.html` (decks, shipped on hand-drawn interim SVG; Innes: *"we need proper artwork which I will provide"*) | C1 | 7 | 0 | **7** | brief is in HANDOFF 2026-09-19 "The art slots": HERO parts, BG_FACE, BG_TORSO, BG_LIMBS, HERO idioms, BG_IDIOM, BG_TALK | the three labelled charts stay as they are; the `-bg` slots must be wordless |
| `impostor_syndrome_lesson.html` — 6 tabs: warm-up, vocabulary, reading, comprehension, language focus, discussion | B2 | 8 | 1 (`Impostor2/hero.jpg`, ultra-wide 3376×1440, crop to 16:9) | **7** | *(have)* woman at a podium, audience in silhouette | a mask held on a stick beside an empty chair; an open dictionary as a flat block; a lectern with one microphone, spotlight; a tick and a cross as two cut-out shapes; a speech bubble as a solid shape with a smaller one inside; two cups on a table |
| `expressions_take_put_v2.html` + `_ES` + `_PL` → **one lesson** (merge ordered by Innes; per-item glosses in all three, so the per-item translation fix comes first) | B2 | 6 | 1 (`TakePut/hero.jpg`) | **5** | *(have)* car on a road at dusk | a hand lifting a cup from a saucer (take); a hand setting a box on a shelf (put); a coat on a hook (put on); a suitcase at a door (take away); two chairs at a café table |
| `forbes-english-body-parts-c1-zh.html` | C1 | 0 | – | **0** | redirect to `forbes-english-body-parts-c1.html?lang=zh` once the Chinese gloss is added; no art of its own | |

---

## 2. Grammar reference sheets (the Übungsheft family, German and Italian support)

Five files, four lessons: the DE/IT cheat sheet merge is blocked on per-item
translation (HERO-QUEUE), so the Italian file shares the German one's set
and orders nothing.

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `cheat_sheet.html` — 18 structures: modals, tenses, conditionals | B1 | 5 | 0 | **5** | a small folded card tucked into a shirt pocket, shirt as flat field, right third | a signpost with three arms, one coral (modals); three clock faces in a row, hands at different hours (tenses); a door ajar with light behind it (conditionals); two chairs facing |
| `cheat_sheet_italian.html` — the same 18 structures, Italian chrome | B1 | 5 | shares | **0** | reuse the set above | |
| `cheat_sheet_part2.html` — question forms | B1 | 5 | 0 | **5** | one large question mark cut from paper, its shadow the only other thing | a raised hand silhouette (asking); a magnifying glass over a flat field (wh-questions); a coin mid-flip (yes/no); two stools |
| `grammar_formulas.html` — 13 structures, Part I | B1 | 5 | 0 | **5** | a row of five flat building blocks, one coral, on a cream shelf | a heavy padlock (have to); an hourglass half run (tenses); two ladders of different heights (comparatives); two cups |
| `grammar_formulas_part2.html` — 6 structures, Part II | B1 | 5 | 0 | **5** | a stack of three books, the top one open, left third | a trail of footprints ending at a pair of shoes (present perfect); a fan of paint swatches (adjectives); a ruler and pencil crossed; two chairs |

## 3. Übungsheft tests and drills (German support, A1–B1)

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `might_vs_going_to_test.html` — two structures, 15 questions | A2 | 5 | 0 | **5** | an umbrella half open under a single cloud, right third | a cloud with one drop (might); a train on a straight track to the horizon (going to); a stopwatch (the test); two stools |
| `present_perfect_test.html` — structure, already/yet/just, ever/never | B1 | 5 | 0 | **5** | a suitcase with one travel sticker, centred small | a ticked checklist as blocks, no words (already); a bare hook (yet); a passport as a flat block (ever/never); two cups |
| `teil3_part2_test.html` — adverbs, will, so/neither | B1 | 5 | 0 | **5** | three dice stacked, each a different colour | a snail and a hare as silhouettes (adverbs); a crystal ball on a stand (will); two identical cups side by side (so/neither); two chairs |
| `phrasal_verbs_test.html` — make, do, take, put, 16 questions | B1 | 3 | 0 | **3** | four hands from the four edges of the frame, each holding one object | a workbench with one tool; two stools |
| `present_simple_continuous_de.html` — "Supereasy", 10 questions | A1 | 3 | 0 | **3** | a kettle on a hob, steam as one flat shape | a wall clock beside a running tap; two cups |
| `Forbes_English_A0_Question_Words.html` — who, what, where, when, why, how | A1 | 5 | 0 | **5** | six coloured doors in a row, one open | a silhouette at a signpost; a map pin on a flat field; a calendar page as a block; two chairs |
| `preview.html` — "Possessive Pronouns A1" | A1 | 0 | – | **0** | **retire**: it is the pre-rebuild original of the shipped deck `forbes-english-possessive-pronouns-a1.html` ("Mine, Yours, Hers"), catalogued under a filename that says preview | |

## 4. Vocabulary tests and word lists

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `forbes-english-vocab-test.html` — definition match, gap, odd one out, in context (rename: shares the title "Vocabulary Test" with the next row) | B2 | 6 | 0 | **6** | a jar of buttons with one on the table, right third | a key beside a keyhole (definition); a wall with one brick missing (gap); four eggs, one blue (odd one out); an open book with a leaf pressed in it (context); two cups |
| `full-vocabulary-test.html` — the full word list in one run | B2 | 3 | 0 | **3** | a long shelf of identical jars, one label-less jar turned round | a scale weighing one word-block; two stools |
| `ecommerce-vocabulary-b1.html` — 18 words, one run | B1 | 3 | 0 | **3** | a parcel on a doormat, left third | a basket icon as a cut-out with one item inside; two chairs |
| `Forbes English - Buying Selling Sharing Online (B2).html` — vocabulary, mistakes, prepositions, spot the sentence | B2 | 6 | 0 | **6** | a price tag hanging from a string, the only object | a shop bell on a counter; a red pencil on a page of ruled lines (mistakes); an arrow into a box (prepositions); a speech bubble with a tick; two cups |

## 5. Common mistakes (for Spanish and German speakers)

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `forbes-english-common-mistakes-b1-b2.html` — notebook, three activities, speaking | B1-B2 | 6 | 0 | **6** | a notebook with one page folded down, centre | a red pencil across a ruled page; two matching socks, one inside out; a fork in a road (second conditional); a lightbulb as a cut-out; two chairs |
| `forbes-english-common-mistakes-review.html` — 14 questions, Spanish support | B1 | 3 | 0 | **3** | an eraser on a desk with one shaving | a traffic light showing one colour; two stools |
| `forbes-english-common-mistakes-review-part2.html` — false friends and prepositions | B1 | 3 | 0 | **3** | two identical masks, one turned away | an arrow entering a box from the side; two cups |
| `forbes-english-common-mistakes-review-part3.html` — "think before you choose" | B1 | 3 | 0 | **3** | a chess pawn on an empty board, right third | two doors, one open; two chairs |
| `forbes-english-swiss-mistakes-a2.html` — word choice, fix the mistake, complete, business match | A2 | 6 | 0 | **6** | a pocket watch on a cream field, left third | a fork in the rails (choose); a cracked cup mended (fix); a jigsaw with one piece out; a briefcase as a block; two stools |
| `forbes-english-swiss-mistakes-a2-part2.html` — sounds, stress, hotel review, natural word order, café vocabulary | A2 | 7 | 0 | **7** | a bell on a hotel desk, the only object | a tuning fork; a see-saw with one heavy end (stress); a hotel key on a tag, no letters; a row of five blocks, one out of line (word order); a croissant on a plate; two cups |

## 6. Business and professional English (B2–C2)

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `Forbes English - Decision-Making Under Uncertainty.html` — vocabulary in context, discussion, roleplay | C1 | 5 | 0 | **5** | a coin balanced on its edge, centre | a compass with no needle; a die in mid-air; a pair of scales with one pan empty (roleplay); two chairs at a table |
| `dailies-review-feedback.html` — 10 questions, phrase toolkit (animation studio) | C1 | 4 | 0 | **4** | a film frame with one drawn flipbook corner, right third | a light table with one sheet; two director's chairs |
| `workplace-roleplay-live.html` — six production scenarios (animation studio; same series as the row above) | B2 | 8 | 0 | **8** | a clapperboard as a flat block, open, no letters | a wall calendar with one day circled; a rising graph line as a cut-out; a phone off its hook; a storyboard of empty frames; a coffee cup ring on a desk; a kanban board of blank cards; two stools |
| `forbes-english-speaking-2.html` — products and people, say it better, carpenter interview, retailer pitch (Ireland), strategy update | B2 | 7 | 0 | **7** | a wooden chair on a plinth, left third | a set square and a plane on a bench; a megaphone as a cut-out; a shop window with one product; a rolled plan on a table; a bar chart of three flat bars; two chairs |
| `forbes-coding-interview-c1.html` — talking through your thinking, technical vocabulary, reorder and match, transformation | C1 | 6 | 0 | **6** | a whiteboard with one box-and-arrow shape, no letters, right third | a thought bubble as a solid shape; a keyboard as a flat block; a flow of boxes joined by arrows; a knot turning into a straight line; two chairs across a desk |
| `forbes-english-c2-barbi-executive-roleplays.html` — six COO dossiers | C2 | 8 | 0 | **8** | a card folder with one tab, on a dark table | a long boardroom table, chairs empty; a lift button lit; a graph falling off its axis; a bridge with the middle span missing; a handshake as two silhouettes; a door with light under it; two chairs face to face |
| `forbes-english-c2-barbi-phrase-test.html` — 20 phrases, one run | C2 | 3 | 0 | **3** | the same folder, closed, a stamp mark on it (no letters) | a stopwatch on a table; two cups |
| `feedback-that-lands.html` — video, reading, vocabulary, grammar (already in eight languages) | B2 | 5 | 0 (`FeedbackThatLands/` holds a 900 px thumb) | **5** | a paper plane landing on a desk, centre | a play button as a cut-out; a newspaper folded as a block; a jar of marbles, one out; a hinge (grammar); two cups |
| `forbes-english-negotiating part2.html` — objections, terms, closing | B2 | 5 | 1 (`negotiating/boardroom-meeting.jpg`) | **4** | *(have)* boardroom | a wall with a hand pushing it (objection); a pair of scales level (terms); a pen over a signature line, no letters; two chairs |
| `forbes-english-lesson (B2).html` — AI, learning and the productive struggle (TED talk) | B2 | 5 | 2 (`AILearning/`) | **3** | *(have)* retro desk at sunset | a climber halfway up a flat rock face; a brain as a cut-out with one lit window; two cups |
| `forbes-english-lesson (data).html` — data, media and climate diplomacy; five activities | C1 | 7 | 2 (`climate/`) | **5** | *(have)* smokestack at sunset | a bar chart as three flat columns; a microphone on a stand; a globe as a plain disc with one pin; a jigsaw of two pieces joining; two chairs |
| `forbes-reddit-french-market-c1.html` + `forbes-roleplay-reddit-french-TEST-p3.html` (a pair; share `RedditFrench/`) | C1 | 8 | 2 (`RedditFrench/`) | **6** | *(have)* café; office silhouette | a magnifying glass over a map pin (prospecting); a ladder to a high window (top brass); a telephone with a long cord; a red pencil on ruled lines (spot the mistake); a stethoscope on a folder (diagnose); two cups |
| `vapour-barriers-lesson.html` — word stress, prepositions, product launch vocabulary (the Contingency deck's sibling: `Construction3/hero.jpg`, `a`, `b`, `c` are unused and match) | B2 | 5 | 4 (borrow `Construction3/` site set) | **1** | *(have)* crane at dusk | *(have)* concrete frame; four-panel site; tower crane; new: a roll of membrane half unrolled on a roof; two site stools |
| `forbes-english-the-ten-year-bet-C1.html` — read, hedging, disagreement, vocabulary, grammar, discuss (hero is Innes's own Black Isler illustration "Two halves, one face": keep) | C1 | 8 | 1 | **7** | *(have)* | a robot arm and a human hand from opposite edges; a fence with a figure sitting on it (hedging); two arrows crossing; a dictionary as a block; a calendar with ten pages fanned; a crystal ball; two chairs |
| `forbes-english-tolle (2).html` — reading, vocabulary in context, concept match | C1 | 5 | 1 (`PowerOfNow/tolle-hero.jpg`) | **4** | *(have)* | a single stone on still water; a candle with a flat flame; two puzzle pieces; two cushions on a floor |
| `forbes-ukraine-presentations-c1.html` — opening, signposting, structure, correct the presenter, phrase to function | C1 | 7 | 7 (`Ukraine/`) | **0** | wire the set; `ukraine-presentations-thumb.jpg` is the only thumb | |
| `forbes-english-construction-presentations.html` — MC, gap fill, ordering (audited 2026-09-16) | C1 | 5 | 1 (`Construction2/construction-site-pink.jpg`) | **4** | *(have)* pink site | a lectern with a hard hat on it; a wall with one brick missing; five blocks in a row, one out of order; two site stools |
| `forbes-architectural-vocabulary.html` + `…-part2.html` — 16-question quiz, then speaking and debate in three groups (a pair; one folder) | C1 | 6 | 0 | **6** | a single arch as a cut-out on a cream ground, centre | a stack of three slabs (materials); a doorway with light through it (space); a spirit level (judgement); a lectern; two chairs |
| `forbes-english-architecture-c1 (1).html` — MC, gap fill, categorise and match (`Architecture/` hero is a 9 MB PNG: re-encode) | C1 | 5 | 1 | **4** | *(have)* | a set of drawing instruments as three shapes; a wall with a window cut out; four boxes, one filled; two chairs |
| `forbes-interior-design-c1.html` — MC, gap, drag and drop, matching (audited and fixed) | C1 | 6 | 1 (`InteriorDesignPhrases/hero.jpg`) | **5** | *(have)* | a single chair in a bare room; a lamp on a side table; a fabric swatch fan; a sofa as one block; two stools |
| `interior-design-vocabulary.html` — 24 questions, one run (audited clean) | C1 | 3 | 1 (`InteriorDesignVocab/hero.jpg`) | **2** | *(have)* threshold | a picture rail with one frame; two chairs |
| `forbes-geoscience-idioms.html` + `forbes-geoscience-business-idioms-v2.html` — two lessons on the same idiom field, three activities each (check for duplication before ordering; `Geoscience/` is volcanoes and buttes and is the wrong picture for business idioms) | C1 | 10 | 0 | **10** | a rock stratum as flat bands with one fault line, right third | a drill bit into a flat ground; a seismograph needle as one line; a core sample as a striped cylinder; a boardroom table; a hard hat on a desk; a compass rose; a fissure with light in it; two chairs |
| `forbes-dartboard-c1.html` — bar placement, revenue share, Japan pitch, terminology | C1 | 6 | 1 (`Dartboard/darts-arcade-row.jpg`) | **5** | *(have)* | a dartboard as concentric flat rings, one dart; a bar stool under a wall light; a coin split in two; a paper lantern; two bar stools |
| `forbes-english-c1-scooter-tricks.html` — terminology, pavement to podium, inversion, talk it through | C1 | 5 | 1 (`scooter/scooter-trick-jump.jpg`) | **4** | *(have)* | a scooter deck as a flat plank; a podium of three blocks; an arrow that flips over (inversion); two kerb-stones as seats |
| `forbes-linking-devices-cars.html` — MC, gap, reorder | B2 | 5 | 0 | **5** | a tow bar joining two car silhouettes, centre | a chain of three links; a road with one gap; a row of cars out of order; two bucket seats |
| `harry-quebert-b2.html` — case file, narrative tenses | B2 | 4 | 0 | **4** | a typewriter as a flat block with one sheet in it, no letters, left third | a lighthouse on a flat sea; a clock with two hands far apart (narrative tenses); two deck chairs |
| `forbes-english-frankfurt-2-lesson.html` — tactics MC, pundit gap fill, term match, reordering | C1 | 6 | 3 (`Frankfurt/`) | **3** | *(have)* | a whiteboard with arrows (no letters); a microphone on a desk; two stadium seats |
| `champions_league_english.html` — vocabulary, commentary, grammar, visual English, quiz | C1 | 7 | 0 (`ChampionsLeague/trophy-hero.jpg` is 1200 px) | **7** | a trophy silhouette on a plinth, right third, re-rendered at size | a football on the penalty spot; a commentator's microphone; a referee's whistle; a camera on a tripod; a scoreboard of blank blocks; two stadium seats |
| `forbes-english-skyline-lego-b2.html` — vocabulary, technical language, reading (four content errors, fifteen items without explanation: audit 2026-09-04) | B2 | 5 | 1 (`skyline/`) | **4** | *(have)* | a single brick as a flat block; a spanner; an open manual with blank blocks; two stools |
| `forbes-english-lego-lesson.html` — prepositions and phrasal verbs Part 1: MC, gap, drag and match, reorder (its card borrows the Lego car deck's art; `LegoPart2/lego-brick-wall.jpg` can be shared) | B1 | 6 | 1 (share) | **5** | a brick on a baseplate, alone, left third | a brick in, on, under a box (three small shapes); a wall with one brick missing; two bricks joining; four bricks in a row out of order; two brick stools |
| `must-have-to-lego-polish.html` — the lesson and four exercises, ten languages | B1 | 6 | 4 (`lego-polish/`) | **2** | *(have)* skyline | a padlock built of bricks; two brick chairs |
| `forbes-english-us-civics-b1.html` — how government works, facts and numbers, term and definition, citizen knowledge | B1 | 6 | 0 | **6** | a domed building as one flat silhouette, centre | three columns (branches); a ballot box with one slot; a gavel; a star cut-out; two chairs |
| `forbes-gaming-youtube-b2.html` — MC, gap, reordering | B2 | 5 | 0 | **5** | a game controller as a flat block, right third | a play button; a headset; a level bar of blocks, one gap; two gaming chairs |
| `takingitaparta2es.html` — read, test, present (robot arm, Spanish support; two pictures inline in the file: check them first) | A2 | 5 | 0 | **5** | a robot arm holding one screw, left third | a device with its back off, parts laid in a row; a screwdriver; a lectern; two stools |
| `under-load-b1-b2-es.html` — error clinic, form, present (same series as the row above) | B2 | 5 | 0 | **5** | a stack of blocks with the bottom one cracked | a red pencil on ruled lines; a chain of three gears; a lectern; two stools |
| `english-lesson-gerunds.html` — theory, DE vs EN, exercises, advanced | B1 | 6 | 0 | **6** | a running figure silhouette leaving a trail of dots, right third | a mirror with two silhouettes (DE vs EN); a bench with a dumbbell; a mountain path; two chairs |
| `eintracht-gerunds-lesson.html` — nine sections on the gerund (SGE) | B1 | 8 | 1 (`Eintracht/`) | **7** | *(have)* stadium goal | a football mid-flight (subject); a goal net (object); a whistle (always gerund); a magnifying glass over a line; a mirror (DE → EN); a fork in the road (meaning changes); two stadium seats |
| `lesson1_gerunds_football.html` — seven questions, one run (English for graphic designers) | B1 | 3 | 1 (`FootballGerunds/`) | **2** | *(have)* | a pencil and a football; two stools |

## 7. Sport, outdoors and place

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `forbes-english-golf-lesson.html` — theory, MC, gap, correct the error (free) | B1 | 6 | 0 (`Golf/` hero is 1200 px) | **6** | a golf ball on a tee on a flat green, left third | a flag in a hole; a scorecard as ruled blocks; a divot beside a club; a red pencil; two golf bags as seats |
| `forbes-english-tennis-present-perfect-a2.html` — reference and six activities | A2 | 8 | 1 (`Tennis/racket-court-net.jpg`) | **7** | *(have)* | a trophy on a shelf (present perfect); a net with one ball over it; a ball machine; a racket with one broken string (error); a scoreboard of blank blocks; two plain flags on one pole (DE and EN); two courtside chairs |
| `forbes-tennis-a2.html` — receptionist instructions: MC, gap, matching | A2 | 5 | 0 (`Tennis/track-serve-hero.jpg` is 1200 px) | **5** | a reception desk bell beside a racket | a signboard with blank lines; a locker with one key; two clipboards; two chairs |
| `forbes-english-skiing-B1.html` — vocabulary, true/false, complete, build | B1 | 6 | 1 (`Skiing/birch-forest-cross-country.jpg`) | **5** | *(have)* | a chairlift chair; a piste marker pole; a ski boot; a pair of skis crossed; two chairlift seats |
| `forbes-english-skiing-lesson.html` — vocabulary in context, terms, grammar in action | B2 | 6 | 1 (`Skiing/downhill-cliff-jump.jpg`) | **5** | *(have)* | a gondola cabin; a snow gauge; a mogul field as bumps; a goggles silhouette; two deckchairs on snow |
| `mtb-english-lesson.html` — vocab, reading, grammar, speaking | B1 | 6 | 0 (`mtb2/` is 1200 px) | **6** | a mountain bike on a ridge line, right third | a helmet; a trail sign as a blank arrow; a chain and cog; a water bottle; two logs as seats |
| `mtb-perfect-vs-simple.html` — identify, choose, gap, error correction | B1 | 6 | 1 (`MTB/ridge-jump-sunset.jpg`) | **5** | *(have)* | a finish-line tape; a fork in the trail; a tyre with one gap in the tread; a red pencil; two logs |
| `ridgeline_run.html` — seven scenes, Basque foothills roleplay | C1 | 8 | 0 (`RidgelineRun/` is 1200 px) | **8** | a ridge as one line against a pale sky, first light, centre-left | a headlamp beam; three riders as silhouettes in a line; a fire road climbing; a cairn on a ridge; a rock under a tyre; a signpost of blank arms; a lodge fireplace with two chairs |
| `Forbes_English_A0_Water_Polo.html` + `…_A1_Water_Polo_Part2.html` — four sections each (a pair; `Water Polo/` holds two 1456 px PNGs) | A1 | 12 | 2 | **10** | *(have)* swimmer; splash | a ball on a flat pool; a cap with a blank number patch; a goal in water; a whistle; a question-mark buoy; a starting block; a lane rope; a scoreboard of blocks; two poolside chairs; two lockers |
| `busch_gardens_english_lesson.html` — vocabulary, grammar, four exercises (Spanish speakers, Miami) | A2 | 7 | 0 | **7** | a roller-coaster loop as one line, right third | a palm tree; a park map as a blank fold-out; a ticket stub, no letters; a carousel horse; a big cat silhouette; two picnic chairs |
| `ecuador_english_lesson.html` — vocabulary, Galápagos reading, comparatives, quiz | A2 | 6 | 2 of `Ecuador/` (4 scenes; two per lesson) | **4** | *(have)* | a giant tortoise silhouette; two volcanoes of different heights (comparatives); a quiz sheet of blocks; two hammocks |
| `ecuador_english_lesson_part2.html` — matching and word order, food and culture, passive, quiz | B1 | 6 | 2 of `Ecuador/` | **4** | *(have)* | a market basket of flat fruit shapes; a hand pouring into a cup (passive); a quiz sheet; two market stools |
| `penguins_past_simple (2).html` — reading, grammar (DE), four exercises | A1 | 7 | 0 | **7** | one penguin on an ice edge, left third | a long dotted journey line across a flat sea; a calendar page torn off; a fish in a beak; a bucket; two ice blocks as seats |
| `forbes-english-b1-modal-verbs-fire-brigade.html` — on duty, station life, radio check, alarm, off the radio (`Fire Brigade/` PNGs are 7 MB each: re-encode) | B1 | 7 | 3 | **4** | *(have)* street | a fire pole; a radio handset; a bell; two station chairs |
| `german_firefighter_happy.html` — **a German-language lesson** (Feuerwehr Deutsch: müssen and haben zu) on the English site; decide whether it belongs before ordering | B2 | 5 | 3 (shares `Fire Brigade/`) | **2** | *(have)* | a helmet on a hook; two station chairs |
| `forbes-english-hiking-c1-part2.html` — error correction, true or false, gap, discourse ordering | C1 | 6 | 2 (`Hiking/`) | **4** | *(have)* | a red pencil on a map fold; a compass; a stack of stones (ordering); two rocks as seats |
| `forbes-english-lesson-TopGear.html` — active and passive, three activities (`Top Gear/hero.jpg` plus four vectorised copies of it: one picture; the audit calls the folder 5:3 and unaudited) | B1 | 5 | 1 | **4** | *(have)* | a car on a lift (passive); a hand on a gear stick; three cones out of order; two bucket seats |
| `top-gear-skiing-lesson.html` — ten sections, past simple (`Top Gear/` holds two distinct ski renders) | B1 | 8 | 2 | **6** | *(have)* three skiers | a starting gate; a stopwatch; a ski lodge board, blank; a trophy on snow; a crashed ski in a drift; a red pencil; two deckchairs |
| `marilyn_prepositions.html` — three activities | B1 | 5 | 2 (`Marilyn/`) | **3** | *(have)* | a subway grate with a skirt-shaped gust; a film reel; two cinema seats |
| `friedrich_prepositions_c1.html` — three activities | C1 | 5 | 2 (`Friedrich/`) | **3** | *(have)* | a crown on a cushion; a baroque window as a cut-out; two throne-like chairs |
| `forbes-english-bronte-lesson.html` — MC, gap, match and reorder | B2 | 5 | 1 (`bronte/`) | **4** | *(have)* triptych | a quill in an inkpot; a moor with one bare tree; three books out of order; two parlour chairs |
| `geopolitics-english-class.html` — question formation, if-clauses, vocabulary, exercises, discussion (free) | C2 | 7 | 2 (`Geopolitics/`) | **5** | *(have)* | a question mark made of a border line; a domino run with one gap (if-clauses); a globe as a disc; a red pencil; two chairs at a round table |
| `forbes_english_c2_architecture_brutalism.html` — warm-up, reading, register, speaking, discussion (`Brutalism/` PNGs are 8 MB each: re-encode) | C2 | 7 | 5 | **2** | *(have)* | a concrete stair as flat steps; two concrete benches |
| `forbes-b2-past-simple-type6.html` — reference, MC, gap, error correction, race report order | B2 | 7 | 0 | **7** | one hatchback in profile, right third | a calendar with a page torn; a chequered flag; a wall with a missing brick; a red pencil on a page; five cones out of order; two bucket seats |
| `forbes-english-venezuela.html` — used to, examples, be used to, in context, compare, choose | B1 | 8 | 0 (`Venezuela/` is 1200 px) | **8** | a hacienda arch on a flat field, re-rendered at size, left third | a rocking chair on a porch; a hammock; a coffee cup on a saucer; a road into hills; two roads meeting; a fork in a path; two porch chairs |
| `reading-a-room-cafe-kowloon.html` — before you start, the room, describe a room you know (free) | C1 | 5 | 1 (`CafeKowloon/kowloon-hero.jpg`) | **4** | *(have)* | a neon tube as one flat curve, no letters; a café table with one cup; a doorway with light; two café stools |
| `snack-attack-a1.html` — video, then MC, unmix, gap and extra word (free) | A1 | 5 | 1 (`SnackAttack/hero.jpg`) | **4** | *(have)* | a biscuit with one bite; a sandwich in three separated layers (unmix); a plate with one crumb; two kitchen stools |
| `alchemist_present_perfect_lesson.html` — the rules, Santiago's journey, choose, complete, discuss (`Alchemist/` belongs to the B2 deck, same book; reuse is fair) | B2 | 7 | 3 (share) | **4** | *(have)* | a footprint trail across dunes (journey so far); a signpost; a wall with one missing brick; two cushions by a fire |
| `prepositions_crime_lesson (fixed).html` — eight sections, crime grammar (free) | A2 | 8 | 2 (`PrepositionFiles/`) | **6** | *(have)* | a magnifying glass over a footprint; a key under a mat; a figure behind a lamp post; a fingerprint as one flat swirl; a witness-stand silhouette; two interview-room chairs |
| `grammar-dojo.html` — reference and quiz, Japanese support, coding edition | A2 | 4 | 0 | **4** | a black belt tied around a laptop as a flat block, centre | a training mat with one figure; two dojo cushions |
| `taekwondo-english-kids.html` + `taekwondo-exercises.html` + `taekwondo-regrets.html` — a family; `Taekwondo/` holds four usable pictures | A2/B2 | 13 | 4 | **9** | *(have)* hero, handshake, pads drill, solo kick | a spilt cup (should have); a heart as a cut-out (must); a rule board with blank lines (have to); a belt on a hook; a punch bag; a trophy shelf; a broken board; two dojo cushions; two benches |
| `vw_grammar_atelier_final.html` — two collections (Vivienne Westwood) | B1 | 4 | 0 (`FashionFilm/` thumbs are 1000 px) | **4** | a tartan swatch on a tailor's dummy, right third | a pair of scissors and a tape; a red pencil on a pattern piece; two fitting-room stools |
| `fashion_english_exercises.html` — Fashion and Film business grammar exercises | B2 | 5 | 0 (thumbs) | **5** | a black gown silhouette on a rail, re-rendered at size | a runway as one long strip; a clapperboard; a tape measure coiled; two front-row chairs |
| `fashion_english_exercises (2).html` — "Business Grammar", the sibling file (diverged, not a duplicate) | B2 | 5 | 3 (`fashion/`) | **2** | *(have)* figures panel | a mannequin with one pin; two front-row chairs |
| `fashion_grammar_lesson.html` — Voice and Vision: active and passive through fashion, seven sections | B2 | 7 | 3 (`fashion/`) | **4** | *(have)* McQueen runway | a hand with a needle (active); a dress on a form, no hand (passive); a sketchbook with blank pages; two atelier stools |
| `forbes_english_filmmaking_lesson.html` — five activities and pitch a scene | B2 | 7 | 5 (`Filmmaking/`) | **2** | *(have)* | a director's viewfinder; two director's chairs |
| `forbes-nietzsche-c1.html` + `nietzsche-grammar-test.html` + `…-part2/3/4.html` — five pages, six shared heroes; the audit says I+II are one build and IV is the film-vocabulary deck's twin, so plan on three lessons: the C1 anchor (8), a grammar trial (5) and a vocabulary test (4) | C1 | 17 | 6 (`Nietzsche/`) | **11** | *(have)* | a moustache as one flat shape; a mountain path to a hut; an abyss as a black band; a lectern; a film camera on a tripod; a red pencil; a hammer; a mask; a script as ruled blocks; a spotlight circle; two chairs |

## 8. Story, roleplay and quest pages (own engines, still scrolling)

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `case-file-b2-roleplay.html` — Silver Pines, ten scenes (`CaseFileSilverPines/` cover is 4:3) | B2 | 8 | 0 | **8** | a road into pines under one lamp, right third, 16:9 | a sheriff's star; a footprint in sawdust; a curtain with a gap; a torn red swatch; a running figure; a tape recorder; a pinboard with string and no notes; two diner stools |
| `forbes-dnd-rpg.html` + `forbes-dnd-rpg-part2.html` — Parisian Conquest I and II, five rooms each; one shared hero | C1 | 14 | 1 (`dnd-rpg/`) | **13** | *(have)* | a telephone (cold call); a pitch hall lectern; a labyrinth as one line; a treasury chest; a throne; a metronome (cadence); a fence line (scope); a fire extinguisher (crisis); a falling graph (numbers); a handshake (renewal); two chairs; two armchairs |
| `Race Day - The Falcon Racing Story (B1 F1 RPG).html` — team roleplay (one hero, one inline picture) | B1 | 8 | 1 (`RaceDay/`) | **7** | *(have)* | a pit-lane light gantry; a tyre on a stand; a radio headset; a rain cloud over a track; a podium; a chequered flag; two pit-wall chairs |
| `wild-frame.html` + `wild-frame-part-2.html` — documentary career quest, eight checkpoints each; one 1456 px hero each | B1-B2 | 16 | 2 (`WildFrame/`) | **14** | *(have)* | a camera on a tripod in long grass; a storm cloud; a pitch envelope; a squirrel silhouette; a passport; a film can; a red-carpet strip; a palace gate; a boom mic; a clapperboard; a train window; a cutting-room bin; a festival laurel as a plain wreath; two canvas chairs |
| `forbes-english-b1-adjective-order-escape-room.html` — study, vault, final door | B1 | 5 | 1 (`LockedStudy/`) | **4** | *(have)* study | a vault wheel; a keyhole with light; a door swinging open; two library chairs |
| `thornwick-deduction.html` — 1.2 MB with eight pictures inlined and a 1500×640 hero | B2 | – | own | **0** | extract the inline pictures to `Thornwick/` first; count after | |

## 9. IELTS: the three scrolling pages

Innes's own pages, uploaded as-is (HANDOFF "IELTS: five lessons published").
The 2026-09-23 audit: *"Converting each needs a hero and one background per
section (§5c) — an art order first."* Use the IELTS stem (slate blue and warm
salmon, HANDOFF 2026-09-13) so they sit with the route. The `IELTS/` cards
are crops of the pages' own diagrams and are not artwork.

| lesson | level | need | have | order | cover | plates |
|---|---|---|---|---|---|---|
| `forbes-english-ielts-bar-charts-c1.html` — introduction, overview, body A, body B, 20 questions | C1 | 6 | 0 | **6** | five flat bars of different heights, one salmon, right third | a magnifying glass over one bar; a horizon line over the bars (overview); two bars side by side; a ruler; two exam chairs |
| `forbes-english-ielts-maps-and-data-c1.html` — describing maps, accurate data language | C1 | 5 | 0 | **5** | a compass rose on a folded map, no letters | a map with one road and one new block; five stepped blocks from small to large (bands of precision); a set of scales; two exam chairs |
| `forbes-english-ielts-writing-studio-part3.html` — Task 1 prompt, Task 2 prompt, how to use the pack | C1 | 5 | 0 | **5** | a desk lamp over a blank sheet, left third | two pie charts as plain discs; an essay as ruled blocks in two columns; a folder with one tab; two exam chairs |

---

## 10. Merge or retire before ordering (saves ~11 heroes)

| what | why | saves |
|---|---|---|
| `preview.html` | pre-rebuild original of the shipped possessives deck, catalogued as a lesson | 1 lesson |
| `forbes-english-body-parts-c1-zh.html` | redirect to the rebuilt deck with a Chinese gloss | 1 |
| `expressions_take_put_v2/_ES/_PL` → one | Innes's decision; per-item translation fix first | 2 |
| `cheat_sheet_italian.html` | shares the German sheet's set until the merge is unblocked | 1 |
| `forbes-english-b2-lego-cars.html` | audit 2026-09-04: weakest of three lessons on one word list; salvage its reading into `forbes-lego-b2` | 1 |
| `nietzsche-grammar-test.html` + `-part2` ; `-part4` + `nietzsche-film-vocab-c1-part5` | one build re-skinned, twice (audit 2026-09-04) | 2 |
| `forbes-geoscience-idioms.html` + `…-business-idioms-v2.html` | two lessons on one idiom field: diff them first | up to 1 |
| `forbes-english-vocab-test.html` / `full-vocabulary-test.html` | not duplicates, but one catalogue title: rename one | 0 |
| `german_firefighter_happy.html` | a German lesson on an English site: decide before spending | up to 1 |
| `active_passive_refinery_quiz_part2.html` | ten questions, one run; `refinery/` already holds four pictures from Part 1 — wire, order nothing | 0 |

## 11. Not on this list, on purpose (19 files)

- **The nine Minecraft time-signals pages** (seven `*-time-signals.html`,
  plus `future-simple-will.html` and `going-to-infinitive.html`) — free, 41
  pictures each, and the artwork quarry for all 24 Block Camp decks (audit 2026-09-12:
  "converting them may be self-defeating"). Leave.
- **The five `*-deck-viewer.html` pages** (Breaking Bad, Harry Potter, Star
  Wars, Stranger Things prepositions, Twin Peaks) — Innes's own `.pptx`
  decks served through the slide-viewer pattern; every slide is a picture.
- **`beyond-the-handlebars.html`** — Innes's own design, hand-maintained
  (HANDOFF 2026-09-17 "ships as Innes designed it. READ THIS FIRST").
- **`kraken-black-tide-rpg.html`** — finished RPG on its own engine, 80
  pictures, nine languages.
- **`stranger-gears-rpg.html`** — slide RPG on its own engine; the
  front-page image is not up for discussion (CLAUDE.md). It still fails three
  structural gates, which is a code job, not an art order.
- **`present-simple-vs-continuous.html`** — the falling-card game, rebuilt
  2026-09-08 with `build_pt.py` on `PresentTenses/` (two pictures).
- **`sailing-the-seas-of-grammar.html`** — the illustrated chart with
  hotspots, `build_sailing.py`, its own art.

## 12. Catalogue rows whose `deck` flag is wrong

Ten decks are `deck: false` in Supabase: `escape-from-alcatraz-a2`,
`forbes-english-b1-mixed-grammar-test` and `-part2`, `forbes-english-body-parts-c1`,
`forbes-english-lego-lesson-part2`, `forbes-english-writers-nightmare`,
`full_grammar_test`, `minecraft-lesson`, `must-have-to-vfb-stuttgart`,
`twin_peaks_prepositions_v5` (and `contingency-trade-offs-vocab` until
`2ee3e602`). Six non-decks are `deck: true`: the five deck-viewers and
`beyond-the-handlebars`. The library's Deck filter and the hub pages read
that flag. One SQL statement each; Innes's to run.

## Order of work

1. §1 — three briefs already exist; two of them have a hero staged.
2. §10 — the merges and retirements, which cost nothing and stop art being
   bought twice.
3. Families where the art is nearly complete (order ≤ 2): Ukraine, Brutalism,
   Filmmaking, Lego Polish, vapour barriers, interior vocabulary, refinery.
   Each is a rebuild waiting on one or two plates.
4. Then by family, largest first: the story and quest pages (§8), sport (§7),
   business (§6), the DE-support families (§2–3), IELTS (§9).

## Method, so this can be regenerated

```bash
# 1. every catalogued file: deck or not
py - <<'PY'
import json,os
for r in json.load(open('tools/lessons.json',encoding='utf-8')):
    f=r['file']; s=open(f,encoding='utf-8',errors='replace').read() if os.path.exists(f) else ''
    print('DECK' if 'class="stage-wrap"' in s else '----', f)
PY
# 2. usable art: PIL over every image in the lesson's folders, keep width>=1400 and w/h>=1.5, drop *pattern*, thumbs, LibraryCards/, IELTS/
# 3. need = 2 + sections (h2 / tab / activity headings), capped at 8
```

Nothing above has been run through `prep-artwork.py --dry-run`; that step
belongs to the session that receives the pictures.
