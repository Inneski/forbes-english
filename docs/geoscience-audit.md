# Audit: forbes-geoscience-phrases.html ("The Language of Geoscience")

Source: `forbes-geoscience-phrases.html` (1,244 lines). Audited 2026-08-15
ahead of rebuild as a 16:9 deck. Lesson file not modified.

---

## PART A — INVENTORY

**Level / audience / language:** Badges `C1 Advanced`, `Technical
English`, `Geoscience`. Subtitle: "Technical phrases and field
expressions used by practising geoscientists — from the wellsite to the
seminar room". Target learner is a working E&P professional (the final
screen references SPE papers and AAPG bulletins). **No second language**
— monolingual English, no translations anywhere.

**Structure:** 3 gated activities. Act 1: 6 MCQ ("Reading the
Formation"). Act 2: 6 word-bank gap fills ("Completing the Field
Notes"). Act 3: 7 matching pairs ("Correlating the Sections"). **19
scored items** (`totalQ = 19`).

**Reading texts:** there are **no standalone passages**. The only prose
is the subtitle (18 w), three section intros (43 / 30 / 40 w), and the
stems themselves (MCQ 22–26 w; FITB 21–28 w). Nothing exceeds 55 words.

**Unscored content:** header + logo, badges, subtitle, the three section
intros, four decorative SVGs (strata column with depth scale, seismic
section, wireline-log panel, structure-contour map), the final outcrop
SVG, the matching completion message, three tiered final messages (≥85%
"Field-ready vocabulary." / ≥60% "A productive section." / else "Every
formation rewards study."), and Restart. All 12 `exp` strings are
unscored teaching text shown only after answering.

### Activity 1 — MCQ (MCQ[0]–MCQ[5]; DOM ids `ob{qi}_{li}`, `fb{qi}`)

The tested phrase in each stem is wrapped in `<span class="q-phrase">`.
In the source data the **correct option is always index 0** (`c: true`);
options are shuffled at runtime. Feedback: the same `exp` shows whether
right or wrong; only `✓ Correct` / `✗ Incorrect` differs.

**MCQ[0] — "the reservoir exhibits dual porosity behaviour"**
Stem: "The well completion report noted that *the reservoir exhibits dual
porosity behaviour*, which had significant implications for the
production forecast model."
- ✔ (a) "The rock contains two distinct types of pore space — typically
  matrix porosity and fracture porosity — each contributing differently
  to fluid flow"
- (b) "The formation was drilled in two separate stages, each requiring
  different completion techniques and wellbore fluids"
- (c) "The reservoir pressure fluctuates between two measurable states
  depending on the seasonal recharge cycle"
- (d) "The hydrocarbon column is divided into an upper gas cap and a
  lower oil zone with a distinct fluid contact"
Feedback: **Dual porosity** = pore space in two systems, the rock matrix
(intergranular pores) and a fracture network. Matrix fluid is released
slowly into the fractures, which act as the main conduits to the
wellbore — critical for modelling flow rates.

**MCQ[1] — "stratigraphic trapping"**
Stem: "During the peer review, the panel raised concerns that the authors
had not adequately accounted for *stratigraphic trapping* as an
alternative explanation for the hydrocarbon accumulation."
- ✔ (a) "A hydrocarbon accumulation sealed laterally or vertically by a
  change in rock type or porosity, rather than by structural
  deformation"
- (b) "The physical process by which sedimentary particles become
  progressively locked together during compaction"
- (c) "A drilling hazard caused by unconsolidated sediment layers
  collapsing into the open borehole"
- (d) "A seismic artefact produced by velocity variations within layered
  sedimentary sequences"
Feedback: **stratigraphic traps** form when rock properties change — a
pinch-out, a facies change, an unconformity — rather than by folding or
faulting. Often subtle and harder to detect seismically than structural
traps.

**MCQ[2] — "well-developed cross-bedding"**
Stem: "The field geologist recorded in her notebook that the exposed
section showed *well-developed cross-bedding*, consistent with a
high-energy fluvial depositional environment."
- ✔ (a) "Inclined sedimentary layers within a larger bed, formed by the
  migration of bedforms such as dunes or ripples in a current"
- (b) "Horizontal lamination produced by low-energy suspension settling
  of fine-grained particles in standing water"
- (c) "A network of intersecting fractures cutting across multiple
  bedding planes at varying orientations"
- (d) "Alternating beds of contrasting grain size indicative of cyclic
  sea-level change"
Feedback: **cross-bedding** = inclined layers within a set, formed as
sediment avalanches down the lee face of bedforms. Angle, scale and dip
direction give palaeocurrent direction and depositional energy.

**MCQ[3] — "seal integrity"**
Stem: "The exploration team's risking assessment concluded that the
prospect carried a low probability of success, primarily because of
uncertainty over *seal integrity*."
- ✔ (a) "The capacity of the confining rock above the reservoir to
  prevent hydrocarbons from migrating further upward"
- (b) "The mechanical strength of the casing and cement bond in the upper
  sections of the planned wellbore"
- (c) "The degree to which the interpreted seismic horizon corresponds to
  a genuine geological boundary"
- (d) "The quality of the contractual terms governing confidential data
  exchange between joint venture partners"
Feedback: **seal integrity** = the cap rock's ability (shale, evaporite,
tight carbonate) to hold hydrocarbons in the trap. Failure by faulting,
fracturing or capillary leakage is a main reason prospects fail.

**MCQ[4] — "mature source rock"**
Stem: "At the basin-scale conference presentation, the speaker argued
that the region's prospectivity depended on identifying areas of *mature
source rock* within reach of viable migration pathways."
- ✔ (a) "Organic-rich rock that has been buried to sufficient depth and
  temperature to generate and expel hydrocarbons"
- (b) "Rock that has undergone complete compaction and diagenesis,
  leaving no remaining capacity for further deformation"
- (c) "Sedimentary strata that have been exposed at surface long enough
  to be accurately described and logged"
- (d) "A formation with well-established petrophysical properties
  confirmed by multiple wells within the same basin"
Feedback: maturity is set by burial depth and temperature history.
Immature rock has not generated; overmature has converted most organic
content to gas "or lost it to cracking" (**see C.8.3 — muddled**). The
oil window, "typically 60–120°C", is where liquid hydrocarbons form.

**MCQ[5] — "anomalously high water saturation"**
Stem: "The petrophysicist highlighted that the interval of interest was
characterised by *anomalously high water saturation* despite the
elevated resistivity readings, and recommended further analysis."
- ✔ (a) "A proportion of pore space occupied by water that is
  unexpectedly large given the other measured parameters"
- (b) "An unusually high concentration of dissolved salts in the
  formation water, affecting the reliability of log data"
- (c) "A borehole condition where drilling fluid has invaded the
  near-wellbore zone to an excessive depth of penetration"
- (d) "A surface geochemical indicator of shallow gas accumulation
  detected during the drilling phase"
Feedback: Sw = fraction of pore space filled with water; high Sw with
high resistivity "can indicate tight, low-porosity rock, complex pore
geometry, or the presence of conductive minerals". **See C.8.1 — the
conductive-minerals clause is wrong.**

### Activity 2 — Gap fill (FITB[0]–FITB[5]; DOM ids `bi{qi}`, `wc{qi}_{wi}`, `ffb{qi}`)

Each item has its own 5-chip bank. In the source data the **correct
answer is always bank[0]**; the bank is shuffled at runtime. Clicking a
chip locks the answer immediately — no confirm step. Feedback: same
`exp` either way; label is `✓ Correct` / `✗ The correct answer was: {ans}`.

**FITB[0]** "The geochemical analysis of the cuttings confirmed that the
formation contained {BLANK}, suggesting active generation and vertical
migration along the identified fault corridor."
Answer **residual oil shows**. Bank: residual oil shows / compressional
wave arrivals / cementation exponents / diagenetic overprinting /
reflection coefficients.
Feedback: oil shows = visible or measurable hydrocarbon traces in
cuttings, cores or mud; "residual" = immobile, possibly a
paleo-accumulation or the tail of a migrating column.

**FITB[1]** "The structure map revealed a well-defined {BLANK} at
approximately 2 400 metres subsea, with four-way closure confirmed by the
seismic interpretation."
Answer **anticlinal crest**. Bank: anticlinal crest / porosity pinch-out
/ compactional drape / overpressure gradient / isopach minimum.
Feedback: the crest is the highest point of an anticlinal fold;
hydrocarbons migrate upward and accumulate there if sealed. Four-way
closure = bounded on all sides by rock dipping away.

**FITB[2]** "Wireline log analysis across the interval indicated net pay
of 18 metres, with {BLANK} averaging 22% and hydrocarbon saturation
exceeding 70%."
Answer **effective porosity**. Bank: effective porosity / acoustic
impedance / differential compaction / vitrinite reflectance / shale
volume fraction.
Feedback: effective porosity = the interconnected portion available for
flow, excluding isolated pores and clay-bound water; a key volumetric
input. **See C.6 — "shale volume fraction" is defensible.**

**FITB[3]** "The team noted a sharp increase in {BLANK} while drilling
the overpressured shale interval, requiring an immediate increase in mud
weight to prevent a well control incident."
Answer **pore pressure**. Bank: pore pressure / overburden stress / sonic
velocity / carbonate saturation / shear wave splitting.
Feedback: pore pressure = fluid pressure in the pore spaces; where it
exceeds the normal hydrostatic gradient, blowout risk is significant if
mud weight is insufficient.

**FITB[4]** "Integration of {BLANK} data with the 3D seismic volume
allowed the team to calibrate the velocity model and significantly
improve the depth conversion of the reservoir target."
Answer **check-shot**. Bank: check-shot / permeability plug / formation
water / mud log / vitrinite.
Feedback: check-shot surveys measure travel time from surface to a
downhole receiver at known depths, calibrating the velocity model for
converting two-way time to true vertical depth.

**FITB[5]** "The reservoir model predicted that {BLANK} would be the
dominant recovery mechanism in the early production phase, given the
limited aquifer support and absence of a gas cap."
Answer **solution gas drive**. Bank: solution gas drive / stratigraphic
onlap / thermal cracking / isostatic rebound / lateral accretion.
Feedback: below the bubble point, dissolved gas exsolves and expands,
pushing oil toward the wellbore; generally less efficient than water
drive or gas cap drive.

### Activity 3 — Matching (MATCH[0]–MATCH[6]; DOM ids `ml{i}`, `mr{i}`)

Right column shuffled at runtime; correctness = left index === right
original index. **No per-pair feedback or explanation exists.**

| # | Term | Definition (verbatim) |
|---|------|-----------------------|
| 0 | vitrinite reflectance | "a measure of thermal maturity derived from the optical reflectivity of organic matter in source rock" |
| 1 | fault throw | "the vertical displacement of rock strata on either side of a fault plane" |
| 2 | capillary entry pressure | "the pressure required for a non-wetting fluid to enter and displace the wetting fluid from a pore throat" |
| 3 | gas–water contact | "the subsurface interface below which pore space is occupied by water rather than gas" |
| 4 | net-to-gross ratio | "the proportion of a formation interval that meets minimum criteria to be considered reservoir quality" |
| 5 | overpressure | "pore fluid pressure that exceeds the expected hydrostatic pressure at a given depth" |
| 6 | facies association | "a group of related sedimentary facies that together characterise a specific depositional environment" |

---

## PART B — SLIDE BUDGET (1280×720, 64px padding)

Measured: MCQ stems 22–26 w; option sets 57–73 w (stem+options 80–95 w,
MCQ[0] heaviest at 95 w); explanations 37–53 w; FITB sentences 21–28 w
plus a 5-chip bank; match definitions 13–18 w.

| Section | Content | Slides |
|---|---|---|
| Title | title, subtitle, badges, hero art | 1 |
| Act 1 intro | 43-word section desc | 1 |
| Act 1 MCQs | 6 × (stem + 4 options); Q1 (95 w) and Q2/Q6 (~86 w) need tightened options — do not add explanation text to these slides | 6 |
| Act 1 feedback | 6 exps at 37–53 w | 6 |
| Act 2 intro | 30-word section desc | 1 |
| Act 2 gap fills | long rows, each carrying its own 5-chip bank → 2 per slide | 3 |
| Act 2 feedback | 6 exps at 37–53 w | 6 |
| Act 3 intro | 40-word section desc | 1 |
| Act 3 matching | 7 pairs, defs 13–18 w → 2–3 pairs per slide | 3 |
| Results | score ring + tiered message | 1 |
| **Total as-is** | | **29** |
| Teaching slides required (Part D) | | **+5–7** |
| **Recommended** | | **~34–36** |

If feedback reveals in place on the question slide rather than as
separate slides, the deck is 17 + teaching ≈ 22–24. No passage exceeds
55 words, so nothing needs splitting.

---

## PART C — DEFECTS

### C.1 Correct answer is the longest option — 6/6 affected, 4/6 strictly by characters

- MCQ[0]: correct 146c/23w vs longest distractor 116c/20w — longest by both
- MCQ[1]: correct 133c/20w vs 106c/13w — longest by both, wide margin
- MCQ[2]: correct 122c/21w vs 108c/13w — longest by both
- MCQ[3]: correct 108c/16w vs 104c — longest by chars
- MCQ[4]: correct 109c/16w vs 113c — tied-longest by words, 2nd by chars
- MCQ[5]: correct 107c/17w vs 113c — tied-longest by words, 3rd by chars

A test-wise learner picking the longest, most-hedged option scores 4–6/6
without reading the stems. MCQ[0] and MCQ[1] add a **lexical echo**: only
the correct option for "dual porosity" contains "porosity"/"pore space";
only the correct option for "stratigraphic trapping" describes a sealed
accumulation. Fix: pad distractors and seed the keyword into one
distractor per item.

### C.2 Positional patterns

- **Correct option is `opts[0]` in 6 of 6 MCQs.** The runtime `shuffle()`
  hides it live; a static rebuild reading the data in order renders the
  answer as option A every time. Re-randomise at authoring time.
- **The gap answer is `bank[0]` in 6 of 6 FITB items** — same hazard.
- Matching data is stored aligned (left *i* pairs with right *i*); only
  the runtime shuffle disorders it. Pre-shuffle the right column.
- Banks are per-item, so the "bank lists answers in gap order" failure
  does not apply across items — but within every item the answer is first.

### C.3 Scored items with no explanation

- **All 7 matching pairs are scored with zero explanation.** The only
  feedback is the generic completion string. A learner who mismatches
  never sees which pairing was right.
- FITB wrong-answer labels restate the answer but are followed by a
  substantive exp, so they are not restatement-only. No
  restatement-only feedback in MCQ or FITB.

### C.4 Identical feedback right or wrong — 12 of 12 explained items

`pickMCQ` (line 1024) and `pickFITB` (line 1089) both build
`${correct ? "✓ Correct" : "✗ Incorrect"} ... ${exp}` — the exp is
identical either way. Picking "upper gas cap / lower oil zone" for dual
porosity gets the same paragraph as a correct answer, with no "that
describes a fluid contact, not porosity" correction. Write
distractor-specific wrong-feedback, or at minimum a one-line "why yours
was wrong" per option.

### C.5 Scoring arithmetic and gates

- **Inconsistent denominators:** the readout is
  `totalCorrect + " / " + totalAnswered` — a running ratio starting at
  "0 / 0" — while the progress bar divides by the fixed 19. Mid-lesson a
  learner sees "3 / 4" against a 21% bar; "out of 19" never appears
  until the end.
- **Matching errors cascade (fairness defect):** in `matchPick` a wrong
  pairing locks **both** items, consuming the true partners of two
  different terms. **One wrong pick forces at least one more; finishing
  with exactly one matching error is impossible.** Minimum penalty for a
  single slip is 2/19.
- **FITB scores on first click** — `fitbDone[qi] = true` on the first
  chip, no confirm, no change of mind. An accidental tap is scored.
- Gates are satisfiable and items cannot be skipped. `showFinal` divides
  by `totalAnswered`, which equals 19 by then, so the final percentage is
  sound. Restart resets all state correctly.

### C.6 Wrong, ambiguous or defensibly-alternative answers

- **FITB[2] — genuine ambiguity.** "net pay of 18 metres, with {BLANK}
  averaging 22% and hydrocarbon saturation exceeding 70%": **shale volume
  fraction** averaging 22% is grammatically perfect and petrophysically
  routine. Only convention favours effective porosity. A domain-literate
  learner is marked wrong on a defensible answer. Fix: change the figure
  so only porosity fits, or drop Vsh from the bank.
- **FITB[1] — weak alternative.** A **compactional drape** at 2 400 m
  with four-way closure is geologically coherent; drape anticlines over
  basement highs do close four ways. "Anticlinal crest" is the better
  idiom, but the distractor is not cleanly wrong.
- **FITB[0] — stem contradicts its own feedback.** See C.8.2.
- MCQ[3] distractor (b) (casing/cement bond) is really *well* integrity —
  a good near-neighbour, but close to unguessable from language alone at
  C1 without domain knowledge (C.9).

### C.7 Authoring artefacts

- **Dead duplicate build in `buildMatch()` (1112–1140):** `card.innerHTML`
  is assigned a complete first layout including empty placeholder cells
  `mr_s${i}`, then immediately reassigned after the leftover comment
  `// Better: build proper two-column layout`. The first template is dead
  code; only the overwrite prevents duplicate `ml{i}` ids. Do not port it.
- **Unreachable reselection logic in `pickFITB` (1058–1061, `.used`
  clearing at 1064):** written for a confirm-step flow that never
  shipped; `if (fitbDone[qi]) return;` means it can never run.
- **Answer key readable in the DOM:** correctness is a literal in the
  onclick attribute (`pickMCQ(0,2,true)`) and `pickMCQ` re-derives the
  correct button by string-parsing that attribute (line 1017). Fragile,
  and the key is one right-click away. Do not reproduce the trick.
- **Chip escaping** (1049): `w.replace(/'/g,"\\'")` works only because no
  bank word contains an apostrophe.
- **Learner-visible SVG glitches:** the header depth scale reads
  0m/500/1km/2km/3km/4km at *equal* spacing — a non-linear scale drawn as
  linear; the seismic panel's TWT labels 0.2/0.4/0.6/0.8 s sit at
  unequal y-spacings (32/58/72/96). A geoscientist audience will notice.
- No unclosed tags in learner-visible strings. Options are labelled A–D
  and no feedback references a letter, so no letter mismatch exists.

### C.8 Factual audit (priority)

Scope note: **the factual surface is entirely petroleum/sedimentary
subsurface geoscience.** There are no claims about plate boundaries,
eruption styles, volcanism, erosion or the geological timescale; the only
igneous token is the decorative "CRYSTALLINE BASEMENT" label.

1. **MCQ[5] feedback — factual error.** "High Sw in the presence of high
   resistivity can indicate … **the presence of conductive minerals**."
   Conductive minerals (clays, pyrite) *depress* resistivity — they cause
   the opposite anomaly (low-resistivity pay, where Sw is
   *over*estimated). They cannot explain a zone both wet and highly
   resistive. Correct: **fresh (low-salinity) formation water**, very low
   porosity / tight rock, or invasion effects. The fresh-water case — the
   textbook one — is missing entirely. Rewrite for the deck.
2. **FITB[0] stem — internally contradictory.** "contained residual oil
   shows, suggesting **active** generation and vertical migration"
   conflicts with its own feedback ("'residual' indicates the oil is
   immobile … may represent a paleo-accumulation"). Residual shows
   evidence that migration *occurred*, not that it is active. Fix to
   "…suggesting hydrocarbon migration along the identified fault corridor
   at some stage", or drop "residual".
3. **MCQ[4] feedback — imprecise.** "converted most of its organic
   content to gas **or lost it to cracking**" is muddled: cracking *is*
   the mechanism converting oil to gas. Correct: "in overmature source
   rock the kerogen has exhausted its oil potential and earlier-generated
   oil has been cracked to gas." The oil window "typically 60–120°C" is
   within commonly cited ranges — keep the hedge.
4. **MATCH[1] "fault throw" — loose but passable.** Precisely, throw is
   the *vertical component of displacement* across the fault. Tighten.
5. **MCQ[2] stem — acceptable with a caveat.** Cross-bedding "consistent
   with a high-energy fluvial environment" is fine as a field
   interpretation, but cross-bedding is equally characteristic of
   aeolian, tidal and deltaic settings. Keep "consistent with"; never
   harden to "indicates fluvial". (Matters for artwork captioning — see
   Part E, buttes.jpg.)
6. **Verified correct:** dual porosity (matrix + fracture, fractures as
   conduits); stratigraphic trap definition and its pinch-out /
   facies-change / unconformity examples; seal lithologies and failure
   modes; anticlinal crest, buoyancy and four-way closure; effective vs
   total porosity; pore pressure / overpressure / mud weight / blowout
   logic; check-shot surveys and time–depth calibration; solution gas
   drive below bubble point and its ranking below water and gas-cap
   drive; all seven MATCH definitions except the fault-throw looseness;
   the structure-map SVG's contour logic (crest 2 100 m, deepening
   outward 2 300 / 2 500 / 2 700).
7. **Unverifiable/decorative:** the header stratigraphic column
   (Quaternary → sandstone → carbonate platform → evaporite → shale
   source rock → crystalline basement) is a plausible generic column, not
   a factual claim; its depth scale is flagged in C.7.

### C.9 Unanswerable or unfair at the stated level

- **The lesson teaches nothing before testing.** There is no presentation
  stage anywhere; every definition exists only in post-answer feedback,
  and Act 3 has none at all. A C1 learner of *English* without a
  petroleum background cannot derive "check-shot" vs "mud log", or
  "solution gas drive" vs its distractors, from language skills — these
  are domain-knowledge tests wearing an English-lesson skin. Fair for
  practising geoscientists; unfair as a general C1 lesson. **The rebuild
  must decide which audience it serves** and add teaching slides.
- **23 distractor terms are never defined anywhere:** compressional wave
  arrivals, cementation exponents, diagenetic overprinting, reflection
  coefficients, porosity pinch-out, compactional drape, overpressure
  gradient, isopach minimum, acoustic impedance, differential compaction,
  shale volume fraction, overburden stress, sonic velocity, carbonate
  saturation, shear wave splitting, permeability plug, formation water,
  mud log, vitrinite, stratigraphic onlap, thermal cracking, isostatic
  rebound, lateral accretion. ("Vitrinite reflectance" appears untaught
  as a FITB[2] distractor but is defined later in Act 3.)
- **Untaught jargon inside the stems**, which the learner must parse just
  to understand the question: well completion report, risking assessment,
  four-way closure (defined only in FITB[1]'s feedback, i.e. *after* the
  stem uses it), net pay, wireline log, mud weight, well control
  incident, aquifer support, gas cap, bubble point (feedback only),
  cuttings, subsea, 3D seismic volume, depth conversion.
- **The matching cascade** (C.5) makes Act 3 additionally unfair: one
  slip costs two marks by mechanism, not by knowledge.

---

## PART D — TEACHING GAPS

There is **no teaching stage in the entire lesson**. Twelve substantive
explanations exist only as post-answer feedback, and Act 3 has none.
Insert teaching slides *before* each practice section.

**Before Act 1 (2 slides):**

- *Traps, seals and porosity* — matrix vs fracture porosity and why
  fractures are the flow conduits (MCQ[0] exp); structural vs
  stratigraphic traps, with pinch-out / facies change / unconformity as
  the stratigraphic mechanisms (MCQ[1] exp); cap rock = seal, common
  lithologies, failure by faulting / fracturing / capillary leakage
  (MCQ[3] exp).
- *Source rock and logs* — thermal maturity: immature, oil window
  (~60–120°C), overmature (MCQ[4] exp, **with the C.8.3 correction**);
  water saturation and the **corrected** high-Sw/high-resistivity
  explanation (MCQ[5] exp, **with the C.8.1 correction**); cross-bedding
  on bedform lee faces and palaeocurrent reading (MCQ[2] exp).

**Before Act 2 (2 slides):**

- *Structure and pressure* — anticline, crest, buoyancy migration, and
  **four-way closure** (currently defined only inside FITB[1]'s feedback
  although the stem uses the term); pore pressure vs hydrostatic
  gradient, overpressure, mud weight, blowout risk (FITB[3] exp).
- *Wellsite to production* — oil shows and what "residual" means (FITB[0]
  exp, corrected per C.8.2); effective vs total porosity (FITB[2] exp);
  check-shot surveys and time-to-depth conversion (FITB[4] exp); the
  three drive mechanisms — solution gas, gas cap, water — and the bubble
  point (FITB[5] exp).

**Before Act 3 (1 slide, mandatory):** a glossary preview of the 7 terms.
Without it the matching activity is the *only* exposure to them, has no
feedback, and double-punishes errors (C.5). The alternative is per-pair
feedback slides after the matching.

**Optional (+1–2):** a distractor-vocabulary key or pruned banks,
addressing the 23 untaught terms (C.9); a "who this lesson is for"
framing slide if it stays professional-audience.

**Facts that exist only inside feedback strings:** the matrix/fracture
dual-porosity flow model; pinch-out, facies change and unconformity as
trap-forming changes; strat traps being harder to see seismically; the
lee-face avalanche origin of cross-beds and their palaeocurrent use;
cap-rock lithologies and seal-failure modes; the 60–120°C oil window;
immature/overmature definitions; the Sw definition and the (flawed)
high-resistivity explanation; the oil-show definition and residual =
immobile; buoyancy accumulation at crests; the four-way closure
definition; effective-porosity exclusions and volumetrics role; the
hydrostatic gradient and blowout/mud-weight balance; the check-shot
method and TWT-to-depth conversion; bubble point, gas exsolution, and
drive-mechanism efficiency ranking.

---

## PART E — ARTWORK FIT (`Geoscience/`)

> **CORRECTION, 15 Aug.** The original version of this section had the
> filenames wrong, and the error survived into a build brief before anyone
> opened the files. What each file actually contains, verified by looking:
>
> | File | What it actually is |
> |---|---|
> | `hero.jpg` | **An erupting stratovolcano over the sea.** Ash column, lava, breaking waves. Not strata. Despite the name, this is **not** the hero. |
> | `buttes.jpg` | **Monument Valley** — layered sedimentary buttes and mesas, big sky, tan plain. **This is the hero.** |
> | `volcano.jpg` | A linear curtain of fire. |
> | `stratovolcano.jpg` | A second ash-column cone. |
> | `fissure.jpg` | A banded escarpment above what the filename calls a lava plain. |
>
> **Do not trust these filenames. Open the file.**

**Supported by lesson content:**

- **`buttes.jpg`** — the hero. Layered sedimentary rock is what this lesson is
  about wall to wall, and its own header art is a strata column. Cover,
  background pattern and palette source. Measured: mean luminance 0.366,
  median 0.352, middle third 0.412 — bright and open, so **light theme**
  (`extract-palette.py Geoscience/buttes.jpg --light`, every contrast row
  PASS). Safe captions: "sedimentary strata", "layered formations".
  **Never caption it as illustrating MCQ[2]'s "high-energy fluvial"
  cross-bedding** — those faces read as flat-lying strata, and the lesson
  itself only says cross-bedding is *consistent with* fluvial settings
  (C.8.5).

**Not supported — do not use:**

- **`hero.jpg`, `volcano.jpg`, `stratovolcano.jpg`, `fissure.jpg`** — the
  lesson contains **zero volcanic or igneous content**: no eruption styles, no
  plate boundaries, no magma, no lava. The sole igneous token is the
  decorative "CRYSTALLINE BASEMENT" label in the header SVG. There is no
  slide any of them belongs on, and the misleading filename of the first
  makes it the most dangerous of the four.
- **The lesson never mentions eruptions at all**, so there is no in-lesson
  basis for captioning any of them, and captioning a central-vent cone
  interchangeably with a fissure eruption **would be a factual error the
  lesson gives the learner no means to detect**. A stratovolcano erupts from
  a central vent, building a steep composite cone of viscous lava and
  pyroclastics; a fissure eruption issues low-viscosity basaltic lava along a
  linear crack and builds no cone. If volcanism imagery is ever wanted, a
  teaching slide making exactly that distinction must come first.

---

## Highest-priority fixes for the rebuild

1. Correct MCQ[5]'s feedback (conductive minerals — C.8.1) and FITB[0]'s
   stem ("active" migration — C.8.2).
2. Re-randomise answer positions at authoring time: the correct answer is
   data-position 1 in all 6 MCQs and all 6 banks (C.2), and pad
   distractor lengths (C.1 — longest-option tell in 4–6 of 6).
3. Add the Part D teaching slides. Act 3 must not remain feedback-free.
4. Replace identical right/wrong feedback with distractor-aware wrong
   feedback (C.4).
5. Fix scoring presentation (fixed /19 denominator); if matching stays
   interactive, decouple wrong pairs so one error does not force a second
   (C.5).
6. Use hero.jpg (title) and optionally buttes.jpg (Act 1 divider or
   results); drop all three eruption images unless a volcanism teaching
   slide is added — and never caption the cone and fissure photos
   interchangeably (Part E).
