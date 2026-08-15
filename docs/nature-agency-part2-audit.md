# Audit: forbes-nature-agency-part2.html

Read-only audit ahead of rebuilding as a 16:9 deck. File not modified.
Checked against the six-point recurring defect pattern in `docs/HANDOFF.md`:
**five of six confirmed, one confirmed absent**, plus four defect classes not
on that list.

Supabase: id 131, `access: pro`, level C1.

---

## A — INVENTORY

Title "Federal Agency for Nature Conservation — Vocabulary Assessment, Part 2".
Audience: a fictional new field officer, six weeks in. **English only** — no
`UI_I18N` block, no second language anywhere. Not a deck: no
`data-type="activate"`, no `.fe-logo`, no `stage-wrap`.

| Section | Type | Items |
|---|---|---|
| 1 — Word Choice | 4-option MCQ, single attempt | 17 |
| 2 — Complete the Briefing | free-text gap fill, exact string match | 17 |
| 3 — Match the Terms | click word → click definition | 16 |

**50 scored items.** **No reading passage of any kind** — the longest prose is
the 115-word intro. Stems average 18.1 words (S1) and 16.9 (S2).

Unscored: intro, section headings, 17 S2 hints (**Section 1 has no hint field
at all**), 34 explanations, four results-band messages, one decorative agency
logo SVG.

---

## B — SLIDE BUDGET

| Section | Slides |
|---|---|
| Cover | 1 |
| Scenario (115 w) | 2 |
| **Teaching (new)** | **14** |
| S1 — 17 MCQ | 17 |
| S2 — 17 gaps | 17 |
| S3 — 16 pairs | 4 |
| Results | 1 |
| **Activation (new, mandatory)** | **2** |
| **As-is** | **43** |
| **Rebuild total** | **57** |

53 is achievable by lifting the repeated 8-word S1 question line into a static
instruction chip and pairing the eight shortest S2 gaps two per slide. **57 with
one gap per slide is recommended** — S2 is free recall and each item needs its
own reveal.

---

## C — DEFECTS

### C1. Longest-option tell — **ABSENT. Do not "fix" this.**

All 68 options are single words. The key is outright longest in **1 of 17**
(`s1q13` *logical* vs *decent*, ratio 1.17 — breaches the ratio rule but passes
the four-character floor), tied in 2. Chance is 25%. Mean key 7.9 chars against
8.2 for distractors. The ANSWERS gate passes and should keep passing.

### C2. Positional patterns — confirmed, and worse than recorded

- **All 17 `correct:` values are 0** (L603–731). The runtime shuffle hides it;
  a static rebuild inherits a 100% "always A" key unless deranged at build time.
- **Option B is the sibling confusable in 12 of 17.** A is the key, B is the
  near-miss, C and D are filler. Spot that and the item is a coin toss.
- **The pair design leaks answers between items.** Eight confusable pairs are
  each tested from both sides (`s1q1/q2`, `q3/q4`, `q5/q6`, `q7/q8`, `q12/q13`,
  `q14/q15`). Six of 17 items carry no independent information.
- **`section3Pairs` (L856–873) is perfectly aligned** word-to-definition. Live,
  both columns shuffle at runtime so the BANK gate passes; **a static render in
  array order publishes the entire key.**

### C3. Scored items with no explanation

S1 and S2: none missing. **S3: 16 of 16 have no explanation, no feedback and no
example sentence** — `{id, word, definition}` and nothing else. 32% of the
assessment teaches by one-line gloss. Identical to Part 1.

### C4. Identical feedback right and wrong — confirmed

- **S1, all 17** (L990–991): `(isCorrect ? "Correct. " : "Not quite. ") +
  q.explanation`. The body is byte-identical.
- **S2, all 17** (L1087–1091): the wrong branch appends the answer, but the
  explanation body is the same string either way. No per-distractor field exists.
- **S3:** no feedback at all. A wrong match flashes red for 550ms and says
  nothing.
- **New: the S2 explanation restates its own pre-answer hint.** Content-word
  overlap: `s2q6` **100%**, `s2q7` **100%**, `s2q10` 86%, `s2q16` 83%, `s2q14`
  80%, mean ~60%. `s2q7` hint "To complain in a bad-tempered way" against
  explanation "'Grumble' means to complain, typically in a low-level,
  bad-tempered way." The learner is told nothing after answering.

### C5. Section 3 cannot be lost — confirmed, identical to Part 1

`selectMatchTile` L1141–1180: `s3Score++` fires only on a correct match; the
wrong branch applies a CSS class and a 550ms timeout, **no penalty, no record,
no attempt cap**; the exit gate reveals the continue button only at
`s3Matched === 16`, and there is no other route to the results screen.

**Every learner who reaches the results screen scores exactly 16/16.** With 16
free of 50, reported percentage is `0.68 × real + 32`:

| real accuracy (of 34) | reported | band shown |
|---|---|---|
| 0% | 32% | "This vocabulary needs more time" |
| 41% | 60% | **"Solid foundation"** |
| 65% | 76% | "Strong result" |
| 85% | 90% | "Outstanding… ready for the field" |

`res-s3` prints `s3Score + " / 16"` (L1213) — a score display that can only ever
show one value.

### C6. Items that mark correct English wrong

`normalizeAnswer` (L1060–1062) trims, lowercases and collapses whitespace. No
punctuation stripping, no article tolerance, **no alternatives array** — `answer`
is a single string. **11 of 17 S2 items reject at least one fully correct
answer:**

| id | line | key | correct English rejected |
|---|---|---|---|
| **s2q2** | 744 | into account | **into consideration** — same idiom, matches the hint exactly. Also *on board*. Strongest case in the file. |
| **s2q7** | 779 | grumble | **complain** — the hint's own first word. Also *moan, grouse, gripe*. |
| **s2q4** | 758 | soothe | **calm** — the hint's own word. |
| **s2q17** | 849 | features | **attributes** — the hint's own word. Also *elements, characteristics*. |
| **s2q13** | 821 | prefer | **prefers** — standard collective-noun agreement. Marking this wrong is the worst class of error here. |
| s2q16 | 842 | entangle | *trap, ensnare, tangle, snag*. |
| s2q8 | 786 | optician | **optometrist** — in the UK the person who tests eyesight; the explanation's own wording describes an optometrist. |
| s2q5 | 765 | gossip | *rumours, word, talk*. |
| s2q6 | 772 | praise | *recognition, acclaim, commendation*. |
| s2q3 | 751 | lectern | *podium, rostrum* (near-universal in AmE). |
| s2q14 | 828 | gig | *concert, show, booking*. |

Low-risk, accept as-is: `s2q1` cleavage, `s2q9` wheelchair, `s2q10` roundabout,
`s2q11` rotunda, `s2q12` value, `s2q15` people person.

**Section 1 keys are all sound** — its problems are structural, not key errors.

**S3 ambiguity:** `s3p10` *survey* (L866) is defined as land measurement only,
but the file uses "survey" five times and **never once in that sense** (habitat
survey, survey forms, survey team, site survey). The learner matches a
definition that contradicts every other use of the word in the same document.

### C7. Factual audit

**Confirmed error — `s2q17`, L850:** "an old **flint quarry** now used by
nesting **sand martins**." Sand martins are obligate burrow-excavators: they dig
50–100 cm tunnels into friable vertical faces of sand or fine gravel. Flint is
hard silica within chalk; neither can be excavated. **Correction: "an old sand
pit" or "a disused gravel pit."** Same class as Part 1's otter/pesticide error.

**Confirmed setting incoherence, pervasive:** "Federal Agency for Nature
Conservation" is the official English name of Germany's *Bundesamt für
Naturschutz*. Every piece of legal and geographic furniture around it is
British: *bylaw*, *the Wildlife Act* (the UK statute is the Wildlife and
Countryside Act 1981; Germany's is the Bundesnaturschutzgesetz), *licence*,
*roundabout*, *car park*, *visitor centre*, *the hide*, *boardwalk*, reed
warblers, salmon netting, yew-grove folklore — plus Part 1's badger cull, town
council and marsh harrier. **The UK has no federal agencies.** Either the agency
is German and the law and geography change, or it is British and gets renamed.

**Spelling:** `offense`/`offenses` ×5 (American) against `licence`, `centre`,
`Modelling`, `travelling` (British). Fix to `offence`; `bylaw` → `byelaw`.

**Wrong primary sense — `s3p14` *crane* (L870):** defined solely as "a tall
machine used to lift and move heavy objects." In a national nature-conservation
lesson **crane is first a bird** — *Grus grus*, one of Europe's flagship
conservation successes, with Germany the continent's principal staging country.
It sits two rows from `s3p15` *flock*. This is the exact polysemy structure
Part 1's Section 1 was secretly built on, here left unexploited.

**Checked and correct — do not "fix":** `s2q1` cleavage in slate; `s2q6` otter
reintroduction (the Otter Trust released ~117 otters in eastern England
1983–1999); `s1q16` canine tooth in a fox; `s1q12` licensed cull.

### C8. Authoring artefacts

| Line | Defect |
|---|---|
| 1221, 1223 | Results bands tell the learner to revise "**before moving to Part 2**". This *is* Part 2 — copy carried over unedited. |
| 576 | Results label reads "Definitions" for Section 1. Section 1 is *Word Choice*; Section 3 is the definitions activity. |
| 600 | `s1q1` closing quotation mark with no opening one. |
| 893, 896, 978, 1076 | `correctOnAttempt` assigned on every item, **never read**. |
| 904, 1185 | `state.currentSection` assigned, **never read**. |
| 1171–1176 | **Live bug.** On a wrong match `s3Selection` resets immediately but a 550ms timeout still strips `match-selected` from the old tiles. Re-select inside that window and the UI shows nothing selected while a selection is live. |
| 397–400 | `#s3-continue-btn` auto margins never apply — it is `inline-block` inside a `text-align:center` wrapper. |
| 1119, 1145 | `.match-word` is both a visual class and the selection-state query selector. Restyling breaks the interaction. `.match-def` has no CSS rule at all. |
| 510 | Progress reads "Question 1 of 50" on the intro screen. |
| 588 | "You've now completed all 100 items…" renders unconditionally, including at 16/50. |

### C9. Unfair or level-mismatched

**19 words appear only as distractors and are defined nowhere.** **12 of the 19
are Part 1 vocabulary** (*reconcile, critic, prevalent, rampant, contribution,
domineering, ersatz, assessor, occupy, programmer, insufficient, decent*) —
**Part 2 silently assumes Part 1 was completed and never says so.** The other 7
(*incisor, molar, premolar, offender, offenses, assessors, contributions*) are
taught in neither part.

**Distractor recycling:** `revoke` appears as a distractor 4× and as the key of
`s1q11`. `insufficient` 3×, `prevalent` 3×.

**Level.** Roughly **26 of 50 items sit at B1 or below** against a C1 badge
(*prefer, value, opposite, wheelchair, matchstick, flock, praise, gossip,
roundabout, features, memorize, philosophers*…). Genuinely C1 items number about
12 (*pithy, slick, fraudulent, ebb and flow, defraud, swindle, revoke, mystical,
canine, cleavage, rotunda, removed*). A CEFR estimate, not a measurement — but
the spread is too wide for one badge.

**Free recall with no support.** 17 low-frequency nouns typed from memory, no
word bank, no first letter, no letter count. *Rotunda*, *lectern* and *cleavage*
are know-it-or-don't.

**Off-topic items:** `s3p1` *removed* ("of a cousin, separated by a number of
generations") is genealogy in a conservation assessment; `s3p6` *philosophers*
and `s3p9` *opposite* likewise.

**Jargon in stems, glossed nowhere:** **the hide** (L696 — highest risk; read as
a verb, "moving the hide further from the nest" collapses), **cull** (L688),
**bylaw** (L632), **flint quarry / sand martins** (L850).

---

## D — TEACHING GAPS

**This is not a lesson. It is a 50-item autograded assessment with zero teaching
content** — no table, no rule box, no worked example. Identical to Part 1.

**Section 1 has no hint field on any item, so all 17 of its rules are learnable
only by answering first.** Eleven distinct rules, including the most useful
thing in the section — **`swindle sb OUT OF sth`** (L676), a syntactic pattern
invisible until the item is graded.

Section 2's hints are pre-answer, but with ~60% mean overlap into the
explanation they add nothing after the fact. Section 3 has no teaching at all.

**Rules absent from the file entirely:** the `-ian`/`-ist`/`-er` agent-noun
pattern (the file contains *physician, optician, physicist, programmer,
offender, assessor* and never names it); `defraud` ↔ `fraudulent` (same root,
different sections, never linked); BrE `offence` / AmE `offense`; **crane the
bird** and a **flock** of them; **survey** in the habitat sense; **spark** as a
verb (`s1q8` literally opens an inquiry; `s3p4` teaches only the noun);
*take into account / into consideration / bear in mind / factor in*;
collective-noun agreement (which `s2q13` silently depends on); **register** —
which of *stressy, gig, gossip, grumble, people person, slick* a field officer
may put in a written report.

**14 teaching slides required.** Organising principle, same as Part 1: do not
present 17 unrelated words — present **eight confusable pairs and name the
disambiguation method** (collocation, the grammar that follows, register).
Section 1 is already built as pairs; it just never says so.

---

## E — ARTWORK FIT

`NatureAgency2/hero.jpg` and `plain.jpg`, both 2944×1648, 16:9, ample
resolution.

**`hero.jpg`** — stylised flat illustration, **African savanna at sunset**: a
tusked African elephant and calf on a grassy bank, a broad still lake, small
mammals and tall wading birds at the waterline, a granite inselberg, fan palms
framing both edges. Coral / peach / slate-blue / cream.

**`plain.jpg`** — same style. A single African bush elephant in full profile
with a calf at its feet, dry golden grassland, **a lone human figure holding a
long stick or spear**, pink-red hills, plain blue sky.

**Neither image depicts anything in this lesson.** The lesson's world is
European temperate wetland conservation — otters, swans, reed warblers, sand
martins, salmon, a yew grove, a bird hide, a boardwalk, a flood, a visitor
centre, a Wildlife Act. There is no African content, no elephant, no savanna and
no human field figure in any of the 50 items or the intro. **The artwork and the
text are about different continents.**

If used, the honest placement is atmospheric and **uncaptioned**: `hero.jpg` on
the cover and as the palette source (extraction verified — coral `#eeb093`,
slate `#6b8894`, teal contrast on near-black green, **every contrast row
PASSES**); `plain.jpg` behind section dividers and the results slide.

Two caveats for the builder:

- The only defensible lexical hook is **`flock`** (`s3p15`) — `hero.jpg` shows a
  line of wading birds. The birds are not identifiable to species, so **do not
  call them cranes** even though *crane* is on the word list.
- The derived palette is coral and slate, which replaces the file's current
  forest-green `#1F4D3B` / gold `#C9A227` identity entirely. That identity is
  not recoverable from this hero, and per house style it must not be hand-picked
  back in.

---

## HIGHEST-PRIORITY FIXES

1. **Derange the Section 1 key.** All 17 are index 0, and the "A = key, B = the
   confusable" structure holds in 12 of 17. Break both. Verify the built
   distribution before shipping.
2. **Make Section 3 losable.** A wrong match must cost that item's point, and
   the exit gate must not require all 16. Measure it against a deliberately
   wrong run before trusting it.
3. **Add accepted alternatives to all 17 Section 2 items** — eleven currently
   reject correct English. Minimum list in C6.
4. **Fix `s2q17` (L850):** flint quarry → **sand pit** or **disused gravel pit**.
5. **Resolve the setting** — German agency or British law and geography, not
   both. Same pass: `offense` → `offence`, `bylaw` → `byelaw`.
6. **Add 14 teaching slides**, Section 1 taught as eight confusable pairs plus a
   named method. Priorities: `swindle sb out of sth`, the `-ian/-ist/-er`
   pattern, `offence`/`offender`, the `defraud → fraudulent` family, and a
   register slide separating report English from pub English.
7. **Add `crane` = bird and the habitat sense of `survey`** — both are
   contradictions inside the same document.
8. **Give right and wrong different feedback on all 34 graded items**, and give
   Section 3's 16 pairs an explanation and an example each.
9. **Gloss the stem jargon pre-answer:** *the hide*, *cull*, *byelaw*, *sand
   martin*. Section 1 needs a hint field it does not have.
10. **Rebase the level or re-badge**, and state that Part 1 is a prerequisite —
    or replace the 12 distractors borrowed from it.
11. **Sweep the artefacts** in C8, starting with the two results bands telling a
    Part 2 learner to prepare "before Part 2".
12. **Satisfy the three failing gates:** ACTIVATION (2 slides, speaking +
    writing), I18N (English plus one finished language), LOGO. **ANSWERS passes
    and should keep passing.**
13. **Never print `section3Pairs` in array order** — it is the complete key.
14. **Budget 57 slides** (43 as-is + 14 teaching), or 53 compressed.
