# Proofread status — what has had the Oxford University Press pass, and what has not

Asked for on 2026-09-27: *"list ones you have not proofread like Oxford
University Press."* Measured 2026-09-29 against `tools/lessons.json` (324
rows) and every audit entry in `docs/HANDOFF.md`. Regenerate rather than
trust: the method is at the bottom.

## What "proofread" means here

The standard is the 2026-09-27 IELTS pass, which Innes asked for in these
words: *"proofread IELTS like you are an Oxford University Press proofreading
expert … must be easy for students to understand the instructions."* Its
method, so the next pass is the same pass:

1. Extract the **visible text** of the page, one block per line, tagged by
   element, and read it **as a reader sees it** — not the source.
2. Read for the reader: instructions a student can follow first time,
   one name for one thing across the whole family, exam wording exactly as
   the exam gives it, consistent case, curly quotes, cited words in italics,
   no comma splices, numbering that matches.
3. Fix **at source** (the builder, the routes file, the data file), regenerate,
   and diff the extracted text before and after so only intended changes go
   out.
4. Record what was changed and what is a judgement left for Innes.

That is different from what a rebuild does. A rebuild **audits** a lesson —
answer keys, second-correct distractors, the longest-option tell, gates,
overflow — and fixes content errors it meets on the way. It does not read the
finished English end to end as a student would, and the German and Spanish
it writes are marked *"written in-session, no native check"* in nearly every
entry since 2026-09-04. So there are three states:

| state | meaning | count |
|---|---|---|
| **Proofread** | the OUP pass above, recorded in HANDOFF | 7 pages, plus the instruction lines of 25 decks |
| **Audited** | rebuilt or audited by a session; keys and content checked; English not read as a reader | 115 decks, 14 Block Camp RPGs, 26 Sherpa pages, 28 scrolling pages |
| **Never read** | no session has read the lesson at all | **116 scrolling pages**, plus the At Work series |

## 1. Proofread (done)

The IELTS family, 2026-09-27 (`HANDOFF.md` "IELTS proofread"): `ielts.html`,
the five route pages (`ielts-writing.html`, `ielts-reading.html`,
`ielts-listening.html`, `ielts-speaking.html`, `ielts-vocabulary.html`), the
Question Bank, and the instruction lines of all 25 IELTS decks (34k words of
slide text swept). Five queries are still open for Innes in that entry —
*Section* against *Part* on the whole Listening route, three sets of names
for the five essay types, *Grammar* against *Grammatical Range and Accuracy*
on the Speaking deck — so even the done list carries a to-do.

**Not covered by that pass, though in the family:** the bodies of the 25
IELTS decks (only their instruction lines were swept) and the three scrolling
Writing pages (Bar Chart, Maps & Data, Writing Studio), which the 2026-09-23
audit read for errors but the proofread did not re-read.

## 2. The one Innes named: Forbes English at Work (the OUP reimagining)

`docs/at-work/` — five coursebooks, 75 units, about 65,000 words across the
five level files, drafted 2026-09-21 as a "conceptual reimagining" of an
Oxford University Press series (the OUP names were removed; the working title
is still a placeholder). **Every dialogue, exercise, listening script and
answer key is an AI draft.** Book 1 has been laid out three times (112 pages,
`build_book.py 1`) and re-styled to Innes's notes, but no pass has read a
unit as a student or a teacher would. It is the largest single unproofread
body of text in the repo and the one most likely to be printed.

What a pass would check, per unit: the can-do line against what the unit
actually practises; the model dialogue's grammar target appears where the
grammar row says it does; the phrase box matches *In the Room*; the homework
key is right; the two artwork subjects match the page; nothing names a real
company, product or person. Books 2–5 have no `content_book<n>.py` yet, so
their exercises do not exist to proofread — the level files are the whole
text.

## 3. Never read by any session (116 scrolling pages)

Every catalogued lesson that is still a scrolling page and appears in no
audit entry, no rebuild entry and no audit document. No session has opened
these except to count them. Ordered by filename. (The nine Minecraft
time-signals pages and the five deck-viewers are in this list too: they are
left alone by the artwork list, but nobody has read them either.)

- `active_passive_refinery_quiz_part2.html` — Active & Passive Voice — Quiz Part 2 (B2)
- `alchemist_present_perfect_lesson.html` — Present Perfect Simple vs Continuous (B2) (B2)
- `breaking-bad-present-continuous-deck-viewer.html` — Breaking Bad — Present Continuous (A2)
- `busch_gardens_english_lesson.html` — Past Simple | Busch Gardens Tampa (A2)
- `case-file-b2-roleplay.html` — Case File: The Silver Pines Mystery (B2)
- `champions_league_english.html` — Champions League (C1)
- `cheat_sheet.html` — Grammar Cheat Sheet — 18 Structures (DE support) (B1)
- `cheat_sheet_italian.html` — Grammar Cheat Sheet — 18 Structures (IT support) (B1)
- `cheat_sheet_part2.html` — Grammar Cheat Sheet — Question Forms (DE support) (B1)
- `dailies-review-feedback.html` — Dailies Review: Giving Feedback Diplomatically (C1)
- `ecommerce-vocabulary-b1.html` — E-commerce Vocabulary (B1) (B1)
- `ecuador_english_lesson.html` — English Through Ecuador — Interactive Lesson (A2)
- `ecuador_english_lesson_part2.html` — English Through Ecuador — Part 2 (B1)
- `eintracht-gerunds-lesson.html` — SGE English — Gerunds as Subjects & Objects (B1)
- `english-lesson-gerunds.html` — Gerunds · English for German Speakers (B1)
- `fashion_english_exercises (2).html` — Business Grammar (B2)
- `fashion_english_exercises.html` — Business English — Fashion & Film (B2)
- `fashion_grammar_lesson.html` — Voice & Vision (B2)
- `feedback-that-lands.html` — Feedback That Lands — Four Professionals on Giving Feedback (B2)
- `Forbes English - Buying Selling Sharing Online (B2).html` — Buying, Selling & Sharing Online (B2) (B2)
- `Forbes English - Decision-Making Under Uncertainty.html` — Decision-Making Under Uncertainty (C1)
- `forbes-architectural-vocabulary-part2.html` — Material & Space: Speaking & Debate (C1) (C1)
- `forbes-architectural-vocabulary.html` — Material & Space (C1) (C1)
- `forbes-b2-past-simple-type6.html` — Past Simple: Honda Civic Type 6 (B2)
- `forbes-coding-interview-c1.html` — Tech Interview Masterclass — Coding Engineer (C1) (C1)
- `forbes-dartboard-c1.html` — Electronic Dartboards: Bar Placement & Japan Tournaments (C1) (C1)
- `forbes-dnd-rpg-part2.html` — The Parisian Conquest II: The Long Winter — Business RPG (C1) (C1)
- `forbes-dnd-rpg.html` — The Parisian Conquest — Business D&D RPG (C1) (C1)
- `forbes-english-architecture-c1 (1).html` — Architectural Presentations C1 (C1)
- `forbes-english-b1-adjective-order-escape-room.html` — The Locked Study | Adjective Order (B1) (B1)
- `forbes-english-b1-modal-verbs-fire-brigade.html` — On Call: Modal Verbs for the Fire Brigade (B1) (B1)
- `forbes-english-bronte-lesson.html` — The Brontë Sisters (B2)
- `forbes-english-c1-scooter-tricks.html` — Sending It: The Language of Scooter Tricks (C1) (C1)
- `forbes-english-c2-barbi-executive-roleplays.html` — The COO Briefings — Roleplay Dossiers (C2) (C2)
- `forbes-english-c2-barbi-phrase-test.html` — The COO Briefings — Phrase Test (C2) (C2)
- `forbes-english-common-mistakes-b1-b2.html` — Common Mistakes: Get It Right (B1-B2) (B1-B2)
- `forbes-english-common-mistakes-review-part2.html` — Common Mistakes Review — Part 2 (B1)
- `forbes-english-common-mistakes-review-part3.html` — Common Mistakes Review — Part 3 (B1)
- `forbes-english-common-mistakes-review.html` — Common Mistakes Review (B1)
- `forbes-english-frankfurt-2-lesson.html` — Eintracht Frankfurt C1 Lesson (C1)
- `forbes-english-golf-lesson.html` — Past Simple vs Present Perfect (Golf) (B1)
- `forbes-english-hiking-c1-part2.html` — Solo Hiking Safety Part 2 (C1) (C1)
- `forbes-english-lesson (B2).html` — AI & Learning Lesson (B2)
- `forbes-english-lesson (data).html` — C1 Lesson: Climate Data & Policy (C1)
- `forbes-english-negotiating part2.html` — Negotiations & Handling Objections (B2)
- `forbes-english-skiing-B1.html` — Skiing at the Resort | B1 Lesson (B1)
- `forbes-english-skiing-lesson.html` — Skiing at the Resort | B2 Lesson (B2)
- `forbes-english-speaking-2.html` — Professional Speaking Lesson (B2)
- `forbes-english-swiss-mistakes-a2-part2.html` — Swiss Precision Part 2 (A2) (A2)
- `forbes-english-swiss-mistakes-a2.html` — Swiss Precision: Common Mistakes for German Speakers (A2) (A2)
- `forbes-english-tennis-present-perfect-a2.html` — Present Perfect | Tennis Club (A2) (A2)
- `forbes-english-the-ten-year-bet-C1.html` — The Ten-Year Bet (C1)
- `forbes-english-tolle (2).html` — The Power of Now: Eckhart Tolle (C1)
- `forbes-english-us-civics-b1.html` — U.S. Civics & Government Vocabulary (B1) (B1)
- `forbes-english-vocab-test.html` — Vocabulary Test (B2)
- `forbes-gaming-youtube-b2.html` — Gaming YouTuber (B2) (B2)
- `forbes-geoscience-business-idioms-v2.html` — Ground-Level Business Idioms (Geoscience, C1) (C1)
- `forbes-geoscience-idioms.html` — Business Idioms for Geoscience Professionals (C1)
- `forbes-linking-devices-cars.html` — Linking Devices: The World of Cars (B2)
- `forbes-reddit-french-market-c1.html` — Reddit × French Market Prospecting (C1) (C1)
- `forbes-roleplay-reddit-french-TEST-p3.html` — Reddit French Market — Role-Play Negotiation (C1) (C1)
- `forbes-tennis-a2.html` — Tennis Club English (A2) (A2)
- `forbes-ukraine-presentations-c1.html` — Giving Presentations: Reconstructing Ukraine (C1) (C1)
- `Forbes_English_A0_Question_Words.html` — Question Words (A0) (A1)
- `Forbes_English_A0_Water_Polo.html` — Water Polo Vocabulary (A0) (A1)
- `Forbes_English_A1_Water_Polo_Part2.html` — Water Polo: Ask & Answer (A1) — Part 2 (A1)
- `forbes_english_c2_architecture_brutalism.html` — C2 Architecture: Brutalism and the City (C2)
- `forbes_english_filmmaking_lesson.html` — Filmmaking in English · B2 (B2)
- `friedrich_prepositions_c1.html` — Friedrich I of Prussia · Prepositions C1 (C1)
- `full-vocabulary-test.html` — Vocabulary Test (B2)
- `future-simple-will.html` — Future Simple: Time Signals (Minecraft ed.) (A1)
- `geopolitics-english-class.html` — Questions & If-Clauses in Geopolitics (C2) (C2)
- `german_firefighter_happy.html` — Feuerwehr Modalverben — Vergangenheit & Zukunft (DE) (B2)
- `going-to-infinitive.html` — Be Going To + Infinitive: Time Signals (Minecraft ed.) (A1)
- `grammar-dojo.html` — 文法道場 Grammar Dojo — Must vs Have To (Coding ed.) (A2)
- `grammar_formulas.html` — German Grammar Formula Reference — Part I (B1)
- `grammar_formulas_part2.html` — German Grammar Formula Reference — Part II (B1)
- `harry-potter-present-continuous-deck-viewer.html` — Harry Potter and the Present Continuous (A1)
- `harry-quebert-b2.html` — B2: The Truth About the Harry Quebert Affair (B2)
- `lesson1_gerunds_football.html` — Verbs + Gerunds (Football) (B1)
- `marilyn_prepositions.html` — Marilyn Monroe & Prepositions (B1)
- `might_vs_going_to_test.html` — Might vs Going To — A2 Test (DE support) (A2)
- `mtb-english-lesson.html` — MTB English — B1 Lesson (B1)
- `mtb-perfect-vs-simple.html` — MTB English — Present Perfect vs Past Simple (B1)
- `past-continuous-time-signals.html` — Past Continuous: Time Signals (Minecraft ed.) (A1)
- `past-perfect-time-signals.html` — Past Perfect: Time Signals (Minecraft ed.) (B1)
- `past-simple-time-signals.html` — Past Simple: Time Signals (Minecraft ed.) (A1)
- `penguins_past_simple (2).html` — Penguins of the Past (A1)
- `phrasal_verbs_test.html` — Phrasal Verbs: make, do, take, put (B1)
- `prepositions_crime_lesson (fixed).html` — The Preposition Files — Crime Grammar Lesson (A2)
- `present-continuous-time-signals.html` — Present Continuous: Time Signals (Minecraft ed.) (A1)
- `present-perfect-continuous-time-signals.html` — Present Perfect Continuous: Time Signals (Minecraft ed.) (A1)
- `present-perfect-time-signals.html` — Present Perfect: Time Signals (Minecraft ed.) (A1)
- `present-simple-time-signals.html` — Present Simple: Time Signals (Minecraft ed.) (A1)
- `present_perfect_test.html` — Present Perfect — Ultra-Clear Test (DE support) (B1)
- `present_simple_continuous_de.html` — Present Simple vs Present Continuous (Supereasy) (A1)
- `preview.html` — Possessive Pronouns A1 (A1)
- `Race Day - The Falcon Racing Story (B1 F1 RPG).html` — Race Day: The Falcon Racing Story (B1)
- `reading-a-room-cafe-kowloon.html` — Reading a Room: Cafe Kowloon (C1)
- `ridgeline_run.html` — The Ridgeline Run — C1 Roleplay · Mountain Biking (C1)
- `snack-attack-a1.html` — Snack Attack! (A1) (A1)
- `star-wars-question-words-deck-viewer.html` — Star Wars: Question Words (EN-DE) (A1)
- `stranger-things-prepositions-deck-viewer.html` — Stranger Things — Prepositions (A2)
- `taekwondo-english-kids.html` — Taekwondo English for Kids — Must, Have To & Should Have (A2)
- `taekwondo-exercises.html` — Taekwondo Grammar Exercises — Must, Have To & Should Have (B2)
- `taekwondo-regrets.html` — Taekwondo Past Regrets — Should Have (DE support) (B2)
- `takingitaparta2es.html` — Taking It Apart (with Spanish support) (A2)
- `teil3_part2_test.html` — Adverbs, Will & So/Neither — Test (DE support) (B1)
- `thornwick-deduction.html` — The Thornwick Deduction (B2)
- `twin-peaks-deck-viewer.html` — Twin Peaks Prepositions — Between Two Worlds (Slide Deck, in progress) (C1)
- `under-load-b1-b2-es.html` — Under Load (with Spanish support) (B2)
- `vapour-barriers-lesson.html` — Bringing a Membrane to Market (B2)
- `vw_grammar_atelier_final.html` — Grammar Atelier (B1)
- `wild-frame-part-2.html` — Wild Frame Part II — The Palace Set (B2) (B2)
- `wild-frame.html` — Wild Frame — Documentary Filmmaker Career Quest (B1-B2) (B1-B2)
- `workplace-roleplay-live.html` — Workplace Roleplay: Live Speaking Practice (B2)

## 4. Audited but not proofread

### Scrolling pages a session has read or part-read (28)

- `beyond-the-handlebars.html` — Beyond the Handlebars: Cycling Vocabulary and Inference (B2-C1): a wrong key and chrome-only DE/ES fixed 2026-09-26; English read
- `expressions_take_put_ES.html` — Expressions: take & put (ES support) (B2): as above
- `expressions_take_put_PL.html` — Expressions: take & put (PL support) (B2): as above
- `expressions_take_put_v2.html` — Expressions: take & put (B2): support structure diffed; one broken promise found (translations promised after every answer, absent in activity 4); English not read
- `forbes-english-b2-lego-cars.html` — Brick by Brick: Building Lego Cars (B2) (B2): family audit 2026-09-04 (eight of 26 keys are the longest option; retire)
- `forbes-english-body-parts-c1-zh.html` — Anatomy of a Sentence (C1, ZH support) (C1): "untouched" (body parts entry 2026-09-19)
- `forbes-english-construction-presentations.html` — Construction Presentations C1 (C1): answer keys audited 2026-09-16 (five of seven MC items had a second right answer)
- `forbes-english-ielts-bar-charts-c1.html` — IELTS Writing Task 1: The Bar Chart (C1): read in the IELTS audit 2026-09-23 (errors fixed); the 2026-09-27 proofread covered the hub and routes, not this body
- `forbes-english-ielts-maps-and-data-c1.html` — IELTS Writing Task 1: Maps & Accurate Data (C1): IELTS audit 2026-09-23 ("located", "Two modules"); the 2026-09-27 pass touched one line
- `forbes-english-ielts-writing-studio-part3.html` — The Writing Studio (IELTS Part 3) (C1): IELTS audit 2026-09-23 (pie charts printed no percentages)
- `forbes-english-lego-lesson.html` — LEGO Prepositions & Phrasal Verbs (B1): family audit 2026-09-04 (disjoint from the car pair; not read in detail)
- `forbes-english-lesson-TopGear.html` — Active & Passive Voice (Top Gear) (B1): named "unaudited" in docs/topgear-b2-audit.md
- `forbes-english-skyline-lego-b2.html` — Nissan Skyline GTR LEGO (B2) (B2): family audit 2026-09-04 (four content errors, 15 items without explanation)
- `forbes-english-venezuela.html` — Used To & Be Used To — Venezuela Edition (B1): one defect fixed (El Zar entry); not read end to end
- `forbes-interior-design-c1.html` — Interior Design Presentation Phrases (C1) (C1): three scoring bugs fixed and the content read (Interior Design pair entry)
- `forbes-nietzsche-c1.html` — Making a Film About Nietzsche | C1 (C1): family audit 2026-09-04 (fixed-order keys: pressing B scores 13/17)
- `impostor_syndrome_lesson.html` — Impostor Syndrome — English Lesson (B2): "Not audited" (artwork-staged queue)
- `interior-design-vocabulary.html` — Interior Design Vocabulary (C1): "audited clean" (Interior Design pair entry)
- `kraken-black-tide-rpg.html` — The Kraken: A Tale of the Deep — Present Perfect West Highland RPG (B1) (B1): nine languages, hotspots and right/wrong lines reworked 2026-09-23; English read
- `must-have-to-lego-polish.html` — Must & Have To — LEGO Grammar Factory (PL support) (B1): family audit 2026-09-04
- `nietzsche-grammar-test-part2.html` — Nietzsche Grammar Test — Part II (C1): family audit 2026-09-04 (one build with Part I)
- `nietzsche-grammar-test-part3.html` — Nietzsche Grammar — Part III: The Final Trial (C1): family audit 2026-09-04 (Q15 unanswerable as printed)
- `nietzsche-grammar-test-part4.html` — Lights, Camera, Nietzsche — Vocabulary Test Part IV (C1): family audit 2026-09-04 (named grammar, contains film vocabulary)
- `nietzsche-grammar-test.html` — Nietzsche Grammar Test — Part I (C1): family audit 2026-09-04 (A2–B1 content labelled C1)
- `present-simple-vs-continuous.html` — Present Simple vs Present Continuous (A2): rebuilt 2026-09-08; the sorting logic read
- `sailing-the-seas-of-grammar.html` — Sailing the Seas of Grammar — Gerunds and Infinitives (B1): hero art and hotspots 2026-09-10; text read
- `stranger-gears-rpg.html` — Stranger Gears: The Last Broadcast — Stranger Things RPG (B2) (B2): longest-key sweep only; three structural gates still fail
- `top-gear-skiing-lesson.html` — Past Simple — Top Gear on the Slopes (B1): named "unaudited" in docs/topgear-b2-audit.md

### Sherpa Tensing (26 pages)

Translations in all nine course languages had **native reviews merged**
(`bca412b1`, 2026-09-27) and the tables were checked (three faults found in
camps one and two). The English of the 26 pages has not had a reader's pass.
Innes stopped the deck redesign on 2026-09-25; the pages stay as they are.

### Block Camp RPGs (14)

Nine languages each, hotspots and right/wrong lines reworked deck by deck
(Kraken, Wonderland, Frankenstein, Sherlock, Nautilus entries). The
2026-09-10 note stands: *"a pronoun that is merely vague in English is wrong in
nine languages"* — which is what a reader's pass catches and a gate cannot.
Not proofread.

- `block-camp/dracula-castle-of-if.html` — Blocula — Conditionals & Passive Voice RPG (B2) (B2)
- `block-camp/fistful-of-lies-rpg.html` — A Fistful of Lies — Past Simple Voxel Western RPG (A1-A2) (A1-A2)
- `block-camp/frankenstein-consequences-rpg.html` — Frankenstein Part II: Consequences — Going To Voxel RPG (A2) (A2)
- `block-camp/frankenstein-green-prometheus-rpg.html` — Frankenstein Part I: Ambitions — Going To Voxel RPG (A2) (A2)
- `block-camp/frostbound-river-rpg.html` — Frostbound: The River Remembers — Present Simple Frozen North RPG (A1-A2) (A1-A2)
- `block-camp/last-bounty-rpg.html` — The Last Bounty — Past Simple Voxel Western RPG (A2) (A2)
- `block-camp/last-train-home-rpg.html` — The Last Train Home — Future Simple Cybervoxel RPG (A1-A2) (A1-A2)
- `block-camp/long-way-home-rpg.html` — The Long Way Home — Narrative Tenses Odyssey RPG (B1) (B1)
- `block-camp/lost-yellow-road-rpg.html` — The Lost Yellow Road — Past Continuous Voxel Oz RPG (A1-A2) (A1-A2)
- `block-camp/nautilus-black-archive-deep-rpg.html` — Nautilus: The Black Archive — Present Perfect Deep-Sea RPG (B1) (B1)
- `block-camp/nautilus-black-archive-rpg.html` — Nautilus: The Black Archive — Present Perfect Voxel RPG (B1) (B1)
- `block-camp/sherlock-blue-hour-rpg.html` — Sherlock Holmes: The Blue Hour — Present Simple London RPG (A2) (A2)
- `block-camp/twenty-thousand-leagues-rpg.html` — Twenty Thousand Leagues: The Sealed Log — Past Perfect Deep-Sea RPG (B1-B2) (B1-B2)
- `block-camp/wonderland-stolen-now-rpg.html` — Wonderland: The Stolen Now — Present Continuous Voxel RPG (A1-A2) (A1-A2)

### House-style decks (115 outside IELTS)

Every one was audited at rebuild — keys, distractors, gates, overflow in every
language it ships — and most carry a builder docstring of content fixes. None
has had the OUP pass on its finished text, and the non-English is
in-session translation without a native check unless the entry says
otherwise. Grouped so a pass can go family by family.

**Block Camp I and II (26):** one shared engine and one shared slide
list per tense, so one reader's pass on the chrome covers all of them and
the per-deck text is short.

- `blockcamp-future-simple-2.html` — Block Camp — Future Simple 1b: Will Or Going To? (B1)
- `blockcamp-future-simple.html` — Block Camp — Future Simple 1a: The Future You Believe In (A2)
- `blockcamp-going-to-2.html` — Block Camp — Going To 1b: Evidence, the Edge & the Plan That Failed (A2)
- `blockcamp-going-to.html` — Block Camp — Going To 1a: The Plan You Already Made (A1)
- `blockcamp-passive-future-simple.html` — Block Camp II — Passive 14: Future Simple Passive (B1)
- `blockcamp-passive-going-to.html` — Block Camp II — Passive 13: Going To Passive (B1)
- `blockcamp-passive-past-continuous.html` — Block Camp II — Passive 12: Past Continuous Passive (B1)
- `blockcamp-passive-past-perfect.html` — Block Camp II — Passive 17: Past Perfect Passive (B1)
- `blockcamp-passive-past-simple.html` — Block Camp II — Passive 11: Past Simple Passive (A2)
- `blockcamp-passive-present-continuous.html` — Block Camp II — Passive 10: Present Continuous Passive (A2)
- `blockcamp-passive-present-perfect.html` — Block Camp II — Passive 15: Present Perfect Passive (B1)
- `blockcamp-passive-present-simple.html` — Block Camp II — Passive 9: Present Simple Passive (A2)
- `blockcamp-passive-trial.html` — Block Camp II — Passive 16: The Trial (B1)
- `blockcamp-past-continuous-2.html` — Block Camp — Past Continuous 1b: The Thing That Cut Across It (A2)
- `blockcamp-past-continuous.html` — Block Camp — Past Continuous 1a: You Were In The Middle Of It (A1)
- `blockcamp-past-perfect.html` — Block Camp — Past Perfect 1a: The Earlier Past (B1)
- `blockcamp-past-simple-2.html` — Block Camp — Past Simple 1b: Telling the Story (A2)
- `blockcamp-past-simple.html` — Block Camp — Past Simple 1a: It Is Finished (A1)
- `blockcamp-present-continuous-2.html` — Block Camp — Present Continuous 1b: Plans, Trends & Photos (A2)
- `blockcamp-present-continuous.html` — Block Camp — Present Continuous 1a: Happening Now (A1)
- `blockcamp-present-perfect-2.html` — Block Camp — Present Perfect 1b: How Long, And From When (B1)
- `blockcamp-present-perfect-continuous-2.html` — Block Camp — Present Perfect Continuous 1b: The Activity, Not The Result (B1)
- `blockcamp-present-perfect-continuous.html` — Block Camp — Present Perfect Continuous 1a: How Long, And The Mud On Your Boots (B1)
- `blockcamp-present-perfect.html` — Block Camp — Present Perfect 1a: It Still Counts (A2)
- `blockcamp-present-simple-2.html` — Block Camp — Present Simple 1b: States, Timetables & Steps (A2)
- `blockcamp-present-simple.html` — Block Camp — Present Simple 1a: Habits & Facts (A1)

**Everything else (89):**

- `-dinosaurs C1.html` — Dino-Craft Part 0: The Briefing (C1)
- `active_passive_refinery_lesson.html` — Active & Passive Voice — Refinery Deputy Lead (B2)
- `alchemist_b2_lesson.html` — The Alchemist (B2) (B2)
- `b1_prepositions_double_lesson.html` — Prepositions Double Lesson (B1) (B1)
- `b2_prepositions_advanced_lesson.html` — Advanced Prepositions (B2) (B2)
- `b2_prepositions_advanced_lesson_part2.html` — Advanced Prepositions (B2) — Part 2 (B2)
- `carrying-the-load-c1.html` — Carrying the Load — Dealing with a Co-worker Who Doesn't Pull Their Weight (C1) (C1)
- `contingency-trade-offs-vocab.html` — Contingency Plans & Trade-offs (C1)
- `english_class_picture_description.html` — Describing a Picture (B1)
- `english_firefighter_v3.html` — Modal Verbs for Firefighters — English for German Speakers (B2)
- `escape-from-alcatraz-a2.html` — Escape from Alcatraz (A2)
- `exam-prep-5hour-course-part2.html` — Out of This World — 5-Hour Test Prep · Part II (A2)
- `exam-prep-5hour-courseEXP.html` — Out of This World — 5-Hour Test Prep · Part I (A2)
- `fireshield-pitch.html` — The FireShield Pitch (B2)
- `football_c1_roleplay.html` — Full-Time Pressure — C1 Football Role-Play (C1)
- `Forbes English - Product Strategy & Market Research Speaking (2).html` — Product Strategy & Market Research Speaking (C1)
- `forbes-ai-productive-struggle-c1.html` — AI, Learning & the Productive Struggle (C1) (C1)
- `forbes-alan-watts-b1.html` — The Art of Being Present — Alan Watts, Reading & Vocabulary (B1) (B1)
- `forbes-c1-negotiation.html` — C1 Negotiation Language (C1)
- `forbes-campaign-review-b2.html` — The Monthly Review: Reporting a Campaign in English (B2) (B2)
- `forbes-conservation-c1.html` — Conservation Travel — Global Projects (C1) (C1)
- `forbes-construction-contracts.html` — Construction Contracts (B2)
- `forbes-el-zar-c2.html` — El Zar — Words of Force and Effect (C2)
- `forbes-english-B1-grammar-court-part2.html` — Grammar Court — B1, Part II (B1)
- `forbes-english-B1-grammar-court.html` — Grammar Court — B1, Part I (B1)
- `forbes-english-b1-mixed-grammar-test-part2.html` — B1 Mixed Grammar Test — Part 2 (B1)
- `forbes-english-b1-mixed-grammar-test.html` — B1 Mixed Grammar Test (B1)
- `forbes-english-b2-lesson.html` — Top Gear — Advanced Grammar in Context (B2) (B2)
- `forbes-english-body-parts-c1.html` — Anatomy of a Sentence (C1) (C1)
- `forbes-english-credit-where-its-due-c1.html` — Credit Where It's Due: Claiming Your Work in English (C1)
- `forbes-english-dinosaur-minecraft-part2.html` — Dino-Craft Part II: The Lost Biome (C1)
- `forbes-english-dinosaur-minecraft.html` — Dino-Craft Part I: The Expedition (C1)
- `forbes-english-dinosaurs.html` — Advanced Dinosaur Facts | C1 (C1)
- `forbes-english-emails calls part3.html` — Emails, Calls & Follow-ups (Part 3) (B2)
- `forbes-english-food-ordering-a1-part1.html` — Ordering Food & Drink — A1 Part 1 (A1)
- `forbes-english-food-ordering-a1-part2.html` — Ordering Food & Drink — A1 Part 2 (A1)
- `forbes-english-football-b1.html` — Football Vocabulary (B1) (B1)
- `forbes-english-hiking-c1.html` — Solo Hiking Safety (C1) (C1)
- `forbes-english-holding-the-line-c1.html` — Holding the Line: Answering an Unreasonable Manager (C1)
- `forbes-english-lego-lesson-part2.html` — LEGO Prepositions & Phrasal Verbs — Part 2 (B2)
- `forbes-english-lego-passive-active.html` — Active & Passive Voice (LEGO ed.) (B1)
- `forbes-english-lesson (2).html` — Business Conditionals (B2)
- `forbes-english-lesson (flow).html` — The Language of Flow (B2)
- `forbes-english-lesson (talking with clients).html` — Talking with Clients (B2)
- `forbes-english-lesson-2.html` — The Design Pitch (B2)
- `forbes-english-lesson-curious incident.html` — Conditionals in The Curious Incident (B2)
- `forbes-english-lesson-managing energy.html` — Managing Energy Projects (B2)
- `forbes-english-lesson_self-improvement (self).html` — The Language of Self-Improvement (B1)
- `forbes-english-meetings.html` — Say it in your own words — open answer practice (B2)
- `forbes-english-minecraft-b1.html` — Minecraft B1 Lesson (B1)
- `forbes-english-minecraft-c1.html` — Minecraft C1 Lesson (C1)
- `forbes-english-minecraft-editorial.html` — Minecraft Trivia Lesson (B1)
- `forbes-english-modal-verbs-B1.html` — Modal Verbs (B1)
- `forbes-english-past-modals-minecraft.html` — Past Modals in Minecraft (B2)
- `forbes-english-photography-b2.html` — Advanced Photography (B2) (B2)
- `forbes-english-possessive-pronouns-a1.html` — Mine, Yours, Hers (A1)
- `forbes-english-present-perfect-lego-b1.html` — Present Perfect with Lego (B1) (B1)
- `forbes-english-product-speaking.html` — Talking About Your Product (B1)
- `forbes-english-the-docket-b2.html` — The Docket (B2) (B2)
- `forbes-english-the-square-a2.html` — The Square — 44 Everyday Words (A2)
- `forbes-english-writers-nightmare.html` — The Writer's Nightmare (B2)
- `forbes-escalating-a-complaint-c1.html` — Escalating a Complaint: Taking It to the Next Level (C1) (C1)
- `forbes-gap-fill.html` — Gap Fill: Talking with Clients (B1)
- `forbes-geoscience-phrases.html` — Technical Geoscience Phrases (C1)
- `forbes-lego-b2-part2.html` — Lego Car Building — Part 2 (B2) (B2)
- `forbes-lego-b2.html` — Lego Car Building (B2) (B2)
- `forbes-nature-agency-part1.html` — The Nature Agency — Part 1 (C1)
- `forbes-nature-agency-part2.html` — The Nature Agency — Part 2 (C1)
- `forbes-risk-management-c1-c2.html` — Managing Risk: Exposure, Calibration and Ownership (C1/C2) (C1-C2)
- `forbes_english_lesson.html` — Refinery Safety & Turnaround (B1)
- `full_grammar_test.html` — Escape from Grammar Jail (B1)
- `harari_davos_c2_lesson_v2.html` — C2 Lesson: Harari at Davos (v2) (C2)
- `impostor_syndrome_advanced_JP.html` — Impostor Syndrome — Advanced English · C1 (C1)
- `jfk_prepositions_b2.html` — JFK & Prepositions Part 2 (B2)
- `koolhas & Lamb.html` — B2 Lesson: Koolhaas & Lamb (B2)
- `make-v-do.html` — Make v Do (A2)
- `minecraft-lesson.html` — Must & Have To — Minecraft Edition (A2)
- `must-have-to-vfb-stuttgart.html` — Must & Have To — VfB Stuttgart (B1)
- `nietzsche-film-vocab-c1-part5.html` — Nietzsche on Film — C1 Vocabulary · Part V (C1)
- `reading-the-elevation-c1.html` — Reading the Elevation: Describing Buildings (C1)
- `saving-fawns-mower-b1-b2.html` — Saving Fawns from the Mower (B1-B2) (B2)
- `saving-fawns-mower-b1.html` — Saving Fawns from the Mower (B1) (B1)
- `sherlock-scarlet-star.html` — The Scarlet Star (B1)
- `stranger-things-b1-lesson.html` — Stranger Things B1 (B1)
- `stranger-things-test.html` — Stranger Things English Test (A2)
- `tense-review-minecraft.html` — Tense Review — Minecraft Edition (B2)
- `twin-peaks-b2-discussion.html` — Behind the Curtains: Discussing Twin Peaks (B2)
- `twin_peaks_prepositions_v5.html` — Between Two Worlds — Advanced Prepositions (v5) (C1)
- `ukraine-reconstruction-lesson.html` — Presenting on the Reconstruction of Ukraine (C1) (C1)

## 5. Site chrome

Proofread on 2026-09-27: `ielts.html` and its five routes. **Not proofread:**
`index.html`, `library.html` (its search help, tags and the hub-plate hero
added 2026-09-27), `pricing.html`, `grammar.html` and the per-topic hub pages
(`present-perfect.html` …, generated by `tools/build_hubs.py` from
`tools/topics.py`), `rpg.html`, `block-camp/quest.html`, the Sherpa route map,
and the gate page the Worker builds from `lesson-meta.json`. The hub pages
and the gate copy are generated, so one fix at source reaches all of them —
the cheapest proofread on the site per page.

## Where to start

1. **Forbes English at Work, Book 1** — the printed one, the biggest, and
   named by Innes.
2. **The site chrome** — one pass reaches every visitor.
3. **The Block Camp chrome** — one pass reaches 40 decks.
4. Then the never-read scrolling pages, in the order the artwork list
   rebuilds them (`docs/ARTWORK-revamp-shopping-list.md`): a rebuild is the
   moment a page gets read anyway, so proofread and rebuild in one sitting.
5. The house-style decks last, family by family, by the IELTS method.

## Method, so this can be regenerated

```text
1. Which catalogued files are decks (stage-wrap), RPGs, Sherpa or scrolling: the shopping list's method.
2. Which have been read: for each filename, the HANDOFF sections (split on "^## ") and the docs/*.md that
   name it. A mention in artwork-needed.md or HERO-QUEUE.md is a count, not a read; an entry whose heading
   says audit, rebuilt, shipped or fixed is a read. The IELTS proofread entry is the only entry that is a
   proofread.
```
