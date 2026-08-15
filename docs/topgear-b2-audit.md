I have everything measured. Here is the audit.

---

# Audit: `forbes-english-b2-lesson.html`

Read-only. File not modified. Checked against the six-point recurring defect pattern in `docs/HANDOFF.md`: **five of six confirmed present**, one confirmed absent, plus a seventh defect not on that list that is more damaging than any of them.

**Family:** Stranger Gears. `stranger-gears-rpg.html` and `StrangerGears/` are in the repo; Clarkson (14 mentions), Hammond (6), James May (2), the Stig (3), Top Gear (13). Names and front-page image are settled and are not questioned below. Invented quotations are noted in C8 as findings only.

---

## PART A — INVENTORY

**Title:** `<title>B2 Grammar Lesson</title>` (generic); on-page H1 "Advanced Grammar in Context".
**Level:** B2 (intro eyebrow "B2 · Grammar Lesson", tag chip "B2 Level"). Results copy claims a 90%+ score is "C1-level performance".
**Audience:** unstated. Framing is "all through the lens of Top Gear."
**Languages:** **English only.** Zero `UI_I18N`, zero `LANGS`/`RTL_LANGS`, zero `data-i18n` attributes. No switcher.
**Format:** old scrolling page, `max-width: 840px`. No `stage-wrap`, no `<section class="slide">`, no `data-type`.

| # | Activity | Type | Items | Points |
|---|---|---|---|---|
| 1 | Multiple Choice | 4-option MCQ, single attempt, no shuffle | 5 | 5 |
| 2 | Fill in Blank | free-text, exact string match | 5 | 5 |
| 3 | Error Correction | free-text repair, 1–2 input fields | 5 | 5 |
| 4 | Matching | click sentence → click grammar label | 5 | 5 |

**Total scored items: 20** (`TOTAL = mcData.length + fitbData.length + errorData.length + matchData.left.length` = 20, L420). The intro chip "20 Questions" is correct. Activity 3 item 1 has **two** input fields but scores **one** point — 21 things to get right for 20 points.

**Reading passages: none.** There is no continuous text of any length. Longest prose in the file:

| Content | Words |
|---|---|
| Grammar Focus note (4 boxes) | 84 |
| Four results-band messages | 19 / 20 / 20 / 24 |
| Intro subtitle | 18 |
| Longest MC explanation (`mc[1]`) | 51 |
| Longest error explanation (`err[3]`) | 42 |
| Entire static HTML body | 173 |

Stems: MC mean **13.4w** (range 7–20); gap sentences mean **12.8w** (10–14); error sentences mean **14.8w** (9–21).

**Unscored content:** intro title/subtitle/4 tag chips; the 84-word Grammar Focus note (4 boxes: Reported Speech / Mixed Conditionals / Cleft Sentences / Complex Passives); 4 activity tab labels; 4 instruction boxes; 5 gap hints; 3 inter-activity "done" cards; 20 explanations; 4 results bands; the score ring.

### Why the file is 760 KB

**One line.** Line 162 is a single `<img src="data:image/jpeg;base64,…">` of **714,312 bytes — 94% of the whole file.** Strip it and the lesson is **46 KB / 758 lines.**

It is not duplicated CSS (one `<style>`, ~130 lines, near-zero dead rules), not inlined data (all four data arrays together are ~5 KB), and not a framework (no dependencies beyond a Google Fonts `<link>`).

Consequences for the rebuild:
- The base64 hero is a **near-duplicate of `TopGearB2/hero.jpg`** (187,592 bytes on disk vs. 714,312 base64 ≈ 535 KB raw — so the inlined copy is ~2.9× larger, i.e. re-encoded at a much higher quality or larger dimensions than needed).
- House style §3 requires `--hero: url('TopGearB2/hero.jpg')` set once in CSS. Doing that alone cuts the file **from 760 KB to 46 KB before a single content change**, and makes the image cacheable across slides and the PDF export instead of re-decoded per use.
- The current image is also inside `.hero-image-wrap` — a bordered box in the page flow. That is the §5b prohibition ("do not put an `<img>` in a card") in its purest form: the hero is a pasted-in picture, not a background.

---

## PART B — SLIDE BUDGET (1280×720, 64px padding → ~1150×590 usable)

Measured loads, words:

| Item | Stem/sentence | Options/inputs | Feedback | Slide total |
|---|---|---|---|---|
| `mc[0]` | 18 | 54 (4 opts, 77–82ch) | 47 | **73** + fb |
| `mc[1]` | 7 | 50 (67–73ch) | 51 | 57 + fb |
| `mc[2]` | 20 | 59 (81–86ch) | 43 | **79** + fb |
| `mc[3]` | 10 | 46 (67–74ch) | 43 | 56 + fb |
| `mc[4]` | 11 | 8 (5–14ch) | 47 | 19 + fb |
| `fitb[0–4]` | 10–14 | 3–5w answer | 24–31 | 41–56 |
| `err[0]` | 16 | 2 fields + 2 labels | 29 | 55 |
| `err[2]` | 21 | 1 field | 25 | 52 |
| `err[3]` | 9 | 1 field | 42 | 56 |
| Match (whole) | 44 (5 left) | 35 (5 right) | per-pair | **79 in 10 rows** |
| Grammar note | — | 4 boxes | — | **84** |

| Section | Content | Slides |
|---|---|---|
| Cover | hero + stacked logo + title | 1 |
| Orientation | title, subtitle, what the lesson covers | 1 |
| **Teaching — Reported speech** | **new** | **3** |
| **Teaching — Conditionals** | **new** | **3** |
| **Teaching — Clefts** | **new** | **3** |
| **Teaching — Complex passives** | **new** | **3** |
| **Teaching — Terminology** | **new** | **1** |
| Activity 1 — MC | 5 items, 1 per slide | 5 |
| Activity 2 — gap fill | 5 items, 1 per slide | 5 |
| Activity 3 — error correction | 5 items, 1 per slide | 5 |
| Activity 4 — identify the structure | 5 items, 1 per slide (converted from matching) | 5 |
| Results | 1 |
| **Activation** | **new, mandatory** | **1** |
| **Straight port, no teaching added** | | **22** (+1 activate = **23**) |
| **Recommended rebuild total** | | **37** |

**Teaching slides needed on top of the port: 14** (13 new + 1 orientation). See Part D for what each covers.

37 exceeds §7's "beyond about twenty-four, split into Part I and Part II". Precedent supports shipping one deck (`stranger-things-b1-lesson` 42, `alchemist_b2` 31, `forbes-nature-agency-part2` 58). If a split is wanted, the natural seam is after the conditionals block: **Part I** = reported speech + conditionals (cover + 8 teach + 10 questions + results + activate = 21); **Part II** = clefts + complex passives (cover + 7 teach + 10 questions + results + activate = 20). Either way the intro chip "~30 minutes" is no longer true — 37 slides is 45–55 minutes.

### Items that cannot fit a slide

**Nothing single-item is unfittable.** Two things flagged:

1. **The matching activity cannot be one slide at house-style type.** 10 rows; at 19–20px in a 545px column the 11-word and 10-word left items wrap to two lines, giving ~80px rows → 5×80 + 4×8 gaps = 432px per column, plus title block ~110px and instruction chip ~50px = **592px against 590 usable**. It is over by a hair with zero margin, and any German string pushes it further. Split it. (There is a stronger reason to split it — see C-Unloseable.)
2. **The 84-word Grammar Focus note is 1.5× the ~55-word practical capacity.** It must become at least 2 slides as a straight port, and is being replaced by 13 teaching slides anyway.
3. **`mc[2]` at 79 words of stem+options is the heaviest single question slide** and `mc[0]` at 73 is second. Both are the explicitly-allowed "stem plus four options" shape, so both fit — but `mc[0]`'s stem contains a nested `<div style="background:…;padding:12px 16px;margin-top:10px">` quotation box (presentation baked into the data string, L239). Render the quotation as a pull-quote line rather than a boxed div inside the stem, or the slide gains ~60px it does not have.

---

## PART C — DEFECTS

Line numbers are from the source file as shipped (identical to the redacted working copy; only line 162 differs).

### C1. The correct option is the longest — **PARTIALLY PRESENT, and the gate would pass**

Full measurement, all 20 options, tag-stripped:

| Item | Key | Key len | Longest distractor | Ratio | Δ | Verdict |
|---|---|---|---|---|---|---|
| `mc[0]` L240–247 | B (idx 1) | 82ch / 14w | 81ch | 1.012 | **+1ch** | strictly longest |
| `mc[1]` L251–257 | B (idx 1) | 73ch / 13w | 73ch | 1.000 | 0 | tied longest |
| `mc[2]` L262–268 | B (idx 1) | 86ch / 15w | 86ch | 1.000 | 0 | tied longest |
| `mc[3]` L273–279 | A (idx 0) | 74ch / 13w | 68ch | 1.088 | **+6ch** | strictly longest |
| `mc[4]` L284–290 | A (idx 0) | 8ch / 2w | 14ch | 0.571 | −6ch | shortest |

Key strictly longest in **2 of 5** (chance 25%); tied in 2 more. Mean key **64.6ch** vs mean distractor **61.9ch**. Against the ANSWERS gate (ratio >1.10 **and** Δ ≥ 4ch): `mc[0]` fails the ratio, `mc[3]` reaches 1.088 — **0.8 characters short of tripping the gate.** Nothing fails. **The length discipline here is genuinely acceptable and should not be "fixed" by shortening keys.**

### C1b. The real MCQ defect the gate cannot see — **every distractor is broken English in 4 of 5 items**

This is worse than the length tell because it is invisible to `check-lesson.js`.

| Item | Distractors that are ill-formed sentences in *any* reading | Solvable by ear? |
|---|---|---|
| `mc[0]` | 0 of 3 — A, C and D are all grammatical sentences | **No — good item** |
| `mc[1]` | 3 of 3 — "If Hammond *wouldn't crash*", "If Hammond *hasn't crashed in 2006*", "If Hammond *didn't crash in 2006*, he would have…" | **Yes** |
| `mc[2]` | 0 of 3 — A/C/D differ only in the verb form; all grammatical | **No — best item in the set** |
| `mc[3]` | 3 of 3 — B has a doubled verb, C has **no verb at all**, D is missing "What" | **Yes** |
| `mc[4]` | 3 of 3 — "*is being known* to have", "*knows* to have", "*has known* to have" | **Yes** |

**In 4 of 5 items a learner who has never heard of a cleft, a mixed conditional or a complex passive scores by picking the only option that reads as English.** Only `mc[2]` requires the taught rule. Fix by rewriting distractors as *well-formed sentences that are wrong for a taught reason* — §6's "three plausible same-length wrong answers is the work."

### C2. Answer-position patterns — **CONFIRMED, and the answers live in four different formats**

The five `correct:` keys you saw are the whole of format 1. The other fifteen answers are stored in three further formats:

| Format | Location | Answer storage |
|---|---|---|
| 1. MCQ index | `mcData[].correct` L246, 256, 268, 279, 290 | integer index |
| 2. Gap alternatives | `fitbData[].accepted` L301, 309, 317, 325, 333 | array of strings |
| 3. Correction alternatives | `errorData[].accepted` L348, 358, 368, 378, 388 | array of arrays |
| 4. Match map | `matchData.pairs` L407 | `{l1:'r1', l2:'r2', l3:'r3', l4:'r4', l5:'r5'}` |

Findings:

- **`correct[] = [1, 1, 1, 0, 0]` — A twice, B three times, C never, D never.** Two of the four positions carry zero probability across the whole activity.
- **There is no shuffle anywhere in the file.** `grep`: `Math.random` = 0 occurrences, `shuffle` = 0, `sort(` = 0. `renderMC` (L473–476) prints `q.options` in authored order and stamps A/B/C/D on top. Unlike Nature Agency Part 1, where a runtime shuffle concealed the "always index 0" key, **here the pattern is fully exposed to the learner**, is identical for every learner, and survives `restartLesson()` unchanged. A learner on a second attempt sees the same letters in the same places.
- **`matchData.pairs` is perfectly aligned `l1:r1 … l5:r5`** (L407). The *displayed* right column is deliberately deranged (`r3, r1, r5, r2, r4`, L401–405), so the on-screen order does not leak — this is the one place the file does the right thing. **But the DOM element ids do:** `renderMatch` writes `id="ml-l3"` and `id="mr-r3"` (L639, 645), so the complete key is readable from dev tools, and if any future build prints `matchData` in array order it publishes the answers whole. Do not.
- Within-item structure: in `mc[0]` and `mc[2]` the key is B and the near-miss confusable is C; in `mc[3]` and `mc[4]` the key is A and the near-miss is B. The key is adjacent to its closest confusable in 4 of 5.

### C3. Identical feedback right and wrong — **CONFIRMED, 15 of 20 items**

Three render sites, all the same shape — the explanation body is byte-identical on both branches, and only a two-word prefix and a bold line differ:

- `checkMC` L500–502: `${ok ? '✓ Correct!' : '✗ Not quite.'}` + `<strong>${ok ? 'Excellent!' : 'Correct answer: ' + q.options[q.correct]}</strong>` + `${q.explanation}` — **all 5 MC items.**
- `checkFITB` L551–553: same shape, `'Perfect form!'` vs `'Correct answer: <em>…</em>'` + `${q.explanation}` — **all 5 gap items.**
- `checkError` L625–627: same shape, `'Error found and fixed!'` vs `'Correct answer: <em>…</em>'` + `${q.explanation}` — **all 5 error items.**

**No per-distractor explanation field exists in any data array.** A learner who picked option A in `mc[1]` and one who picked C receive the same paragraph; neither is told what *their* choice was wrong about, even though every explanation contains that information ("Option A uses past simple instead of past perfect. Option C uses 'wouldn't' which is never used in if-clauses.") — it is written and then shown to everyone regardless.

**Activity 4 is the inverse failure.** `selectRight` L689–690 shows the real per-pair explanation on a **correct** match only; the wrong branch (L700–703) shows one hardcoded generic string — *"Look carefully at the grammar structure of the highlighted sentence."* — identical for all 5 pairs and every wrong attempt. The learner who needs help gets nothing; the learner who already knew gets the explanation.

Fix per the Nature Agency Part 2 precedent: `deck.py`'s `mc()` writes one explanation per slide, so inject per-option `data-explain` after calling `D.mc` (the engine already prefers an option's own explanation). If this is the third lesson to need it, promote it to an optional `explains=` argument on `D.mc`.

### C4. Rules that exist only inside post-answer feedback — **CONFIRMED, 15 of ~19 rules**

Total pre-answer teaching in the entire file: **84 words**, in four boxes on the intro screen, each giving 1–2 example sentences and a one-line gloss. That screen is hidden the moment `startLesson()` fires (L433) and is unreachable without restarting — while the sub-50% results message tells the learner to *"Re-read the reference section"*, a section that does not exist under that name and is not reachable from the results screen.

| # | Rule | Where it lives | Pre-answer? |
|---|---|---|---|
| 1 | Backshift is a *table*, not "one step back" | L178 gives only "Tense shifts back one step" | partial |
| 2 | `will` → `would` **and** `said` → `had said` must shift together | `mc[0]` explanation L247 | **no** |
| 3 | `will` cannot survive a past reporting verb | `mc[0]` L247 | **no** |
| 4 | present perfect → past perfect | `mc[2]` L269 | **no** |
| 5 | Present perfect may **stay** for timeless facts reported immediately | `mc[2]` L269 | **no** — and this exception contradicts rule 2 |
| 6 | past simple passive → past perfect passive | `fitb[0]` L302 | **no** |
| 7 | `would`/`wouldn't`/`would have` never in an if-clause | `mc[1]` L258, `err[1]` L354 | **no** |
| 8 | Third conditional form | `fitb[1]` hint L308 names it; form only in explanation L310 | **name only** |
| 9 | Conditional perfect survives reporting unchanged | `fitb[4]` L334 | **no** |
| 10 | It-cleft frame `It + be + focus + that/who + rest` | `mc[3]` L280, `fitb[3]` L326 | **no** |
| 11 | `who` preferred for people; `that` also acceptable | `fitb[3]` L326 | **no** |
| 12 | It-cleft takes `that`/`which`, **never** `what` | `err[4]` L384 | **no** |
| 13 | Wh-cleft = pseudo-cleft, focuses the complement | `match l5` L413 | **no** |
| 14 | Perfect infinitive when the event precedes the reporting | `fitb[2]` L318 | **no** |
| 15 | `is thought that it` is a learner error | `err[3]` L374 | **no** |
| 16 | Stative verbs cannot take the continuous | `mc[4]` L291 — **the only occurrence of the word "stative" in the file** | **no** |
| 17 | `which` is already the subject → no resumptive `it` | `err[2]` L364 | **no** |

**15 of 17 are learnable only by answering first.** `mc[4]` is unanswerable on principle without rule 16, which appears nowhere before it.

### C5. A word bank listing the gap answers in gap order — **ABSENT**

There is no word bank. Activity 2 is free recall with a lemma hint (`'make (v.) — reported speech: past simple passive shifts to?'`). BANK gate is genuinely clean. **Do not add a word bank in the rebuild** — it would create the defect.

### C5b. The answer is printed in the input box — **CONFIRMED, 6 of 6 fields, all of Activity 3**

This is the most damaging single defect in the file and it is not on the six-point list.

`renderError` L574–578 writes `placeholder="${q.placeholders[0]}&hellip;"`. The `placeholders` array is **byte-identical to the first accepted answer** in every field:

| Item | Line | Placeholder shown in the box | Accepted | Leak |
|---|---|---|---|---|
| `err[0]` field 1 | 346 | `had always loved…` | `['had always loved']` | ✅ |
| `err[0]` field 2 | 346 | `would…` | `['would']` | ✅ |
| `err[1]` | 356 | `had apologised…` | `['had apologised']` | ✅ |
| `err[2]` | 366 | `which is…` | `['which is']` | ✅ |
| `err[3]` | 376 | `is thought to have revolutionised…` | `['is thought to have revolutionised']` | ✅ |
| `err[4]` | 386 | `that…` | `['that','which']` | ✅ |

The learner reads the grey ghost text and types it. **All 5 points of Activity 3 (25% of the lesson) are free.** Delete the `placeholders` array entirely; use a generic placeholder or none.

### C6. Items that cannot be answered from the text, or that mark correct English wrong — **CONFIRMED**

`checkFITB` L538 normalises with `inp.value.trim().toLowerCase()` and nothing else. **No whitespace collapsing** (weaker than Nature Agency Part 2's `normalizeAnswer`, which at least collapsed runs), **no punctuation stripping**, **no apostrophe normalisation**. `"had  been  made"` with a double space is rejected. `"hadn’t moved"` typed with an iOS smart apostrophe (U+2019) is rejected against `"hadn't moved"` (U+0027) — this will hit real learners on phones and tablets, and Activity 2 item 2 is the one item that explicitly invites an apostrophe.

Correct English currently marked wrong:

| id | Line | Key | Correct English rejected |
|---|---|---|---|
| **`mc[0]`** | 243, 247 | option B | **Option C is correct English.** "Clarkson told reporters that he would never apologise for what he said" is standard; backshifting an embedded past simple to past perfect is *optional* (Swan, PEU §275). The explanation's claim that "both tense shifts must occur together" is prescriptively over-strict, and the item marks a fluent answer wrong. Strongest case in the file. |
| **`fitb[0]`** | 301 | `had been made` | **`was made`** — with a past reporting verb, backshift of a past simple is optional and this reads more naturally in a press statement. Rejected. |
| **`fitb[2]`** | 317 | `is reported to have attracted` | `has been reported to have attracted`; `was reported to have attracted`. Both correct. |
| **`fitb[1]`** | 309 | `had not moved` / `hadn't moved` | Curly-apostrophe variant rejected (see above). |
| **`err[0]`** | 348 | `had always loved` | **`has always loved` is not an error.** A state that remains true routinely resists backshift — "Clarkson said that he has always loved fast cars" is exactly what a journalist writes. The item's own sibling rule (`mc[2]` explanation, "acceptable for timeless facts") licenses it. |
| **`err[0]`** | 348 | `would` | `would never change` rejected; only the bare modal accepted, though the label says *Fix "will"* so the risk is moderate. |
| **`err[1]`** | 358 | `had apologised` | **`had apologized`** — Oxford/AmE spelling rejected. |
| **`err[3]`** | 378 | `is thought to have revolutionised` | **`is thought to have revolutionized`** rejected. Also `is believed to have revolutionised`, `is considered to have revolutionised`. |
| **`match l1`** | 394, 402 | `r1` "Reported speech" | **`"I am resigning," he announced.` is direct speech, not reported speech.** The item asks the learner to label a direct quotation as reported speech; the explanation (L409) then correctly says "Direct speech 'I am resigning' *becomes* reported: He announced that he was resigning." The label and the sentence disagree. |

**Over-general rules that will bite later:**
- `match r3` (L401): *"It-cleft — emphasises the subject of the action."* False as a general rule. It-clefts focus objects and adjuncts freely — "It was **in 2006** that Hammond crashed", "It was **the Veyron** that he described…". The lesson's own `err[4]` sentence is an object-focus it-cleft, contradicting this label two activities later.
- `match r5` (L403): *"Wh-cleft — emphasises the object or complement."* Same problem inverted.

**Answerable-by-elimination:** Activity 4 has 5 items and 5 labels with no distractors. Get four and the fifth is free; and because the sentences are one-per-structure, three of the five are identifiable from a single surface word ("It was… who", "What I find… is", "is said to have").

**Instruction contradicts the item:** the Activity 3 instruction box (L586) reads *"Each sentence contains exactly one grammatical error, highlighted in red."* `err[0]` (L340) contains **two** errors and requires both to be fixed, and the highlighter (L569) marks only one. `q.sentence.replace(q.errorWord, …)` is a plain-string `replace` — first occurrence only. No live collision today, but it is fragile.

### C-Unloseable. Activity 4 cannot be lost — **CONFIRMED, identical to Nature Agency Parts 1 and 2**

`selectRight` L676–707:
- Correct branch: `totalAnswered++`, `totalCorrect++`, tiles locked (L679–685).
- Wrong branch (L695–704): flash red for 400ms, show a generic string. **No `totalAnswered++`, no penalty, no record, no attempt cap.**
- Exit gate L691–694: the "View My Results" button is written only when `matchedPairs === matchData.left.length` (5), and `showFinal()` has **no other caller in the file.**

**Every learner who reaches the results screen scores exactly 5/5 on Activity 4.** Brute-forcing is at most 25 clicks.

Corollary: **there is no route to the results screen except through Activity 4.** A learner who completes Activities 1–3 and skips 4 never sees a score. Conversely `goToActivity(4)` is one click on the always-visible tab bar (L203), so a learner can go straight to Activity 4, brute-force 5/5, and land on results at 5/20 = 25%.

### C-Scoring. Scoring arithmetic

**10 of 20 points (50%) require no knowledge of English:** 5 free from Activity 4 (unloseable) + 5 free from Activity 3 (the answer is in the input box).

`showFinal()` L725 computes `pct = totalCorrect / TOTAL` with `TOTAL = 20`. So reported score as a function of real accuracy on the 10 genuinely-scored items:

| Real accuracy (of 10 real items) | Reported | Band shown |
|---|---|---|
| 0% | **50%** | "Good Effort! You are building solid B2 foundations." |
| 20% | 60% | "Good Effort!" |
| 40% | **70%** | "Well Done! Strong B2 result." |
| 80% | **90%** | "Outstanding! C1-level performance… Consider moving on to C1." |

**A learner who answers 8 of 10 real items is told they are ready for C1. A learner who answers none is told they have solid B2 foundations.** The floor of the scale is 50%; the bottom band ("Keep Pushing!", <50%) is **unreachable** by anyone who finishes the lesson.

Two further arithmetic faults:
- **Two denominators in one lesson.** The header badge (L152, `updateScore` L425–428) reads `Score: totalCorrect / totalAnswered` — a running ratio out of *attempted*. The results screen reads out of `TOTAL = 20`. Because wrong matches never increment `totalAnswered`, the header can only climb during Activity 4; a learner can finish with the header showing 12/17 and the results showing 60%.
- **`err[0]` scores 1 point for 2 fields, all-or-nothing** (L611–615: `ok` starts true and any wrong field clears it). A learner who fixes the backshift but not `will` scores zero. Under the house-style gap engine ("the engine counts gaps, not slides") this is 2 points, taking the rebuilt total to **21**.

### C-Artefacts. Authoring artefacts, dead code and live bugs

| Line | Defect |
|---|---|
| **55** | `.tab-btn.completed::after{content:' \u2713';}` — **`\uXXXX` is not a CSS escape.** CSS wants `\2713`; `\u` escapes the literal character `u`, so a completed tab renders **" u2713"** instead of a tick. This is HOUSE-STYLE §13's named trap in its CSS variant. **Live bug, visible on screen.** |
| **742–754** | **Live bug: `restartLesson()` never restores panel visibility.** It resets counters and tab classes and adds `active` to `tab-1`, but never calls `goToActivity(1)` and never re-renders. Because the learner was on Activity 4 when the run ended, `#activity-1/2/3` still carry `hidden` and `#activity-4` does not. After Restart → Start Lesson, `renderMC()` populates a **hidden** `#activity-1` while the previous run's **fully-matched Activity 4 board** stays on screen, with tab 1 highlighted. |
| **422, 462, 514, 565** | `questionAnswered` is a **single global shared by three activities**, reset by whichever renderer ran last. It happens not to double-count today only because disabled inputs swallow the `keydown` handler and the Check buttons are hidden. One state-model change breaks scoring. |
| **346, 356, 366, 376, 386** | `placeholders` — the answer leak (C5b). Also entirely redundant with `accepted`. |
| **347, 357, 367, 377, 387** | `fields: N` duplicates `accepted.length`. Two sources of truth for the same fact. |
| **298, 306, 314, 322, 330** | `blank` duplicates `accepted[0]` in every gap item. |
| **342** | `correction: 'had always loved ... would'` — an ellipsis-joined pseudo-answer, printed to the learner as *"Correct answer: had always loved ... would"*. |
| **569** | `q.sentence.replace(q.errorWord, …)` — plain-string, first-occurrence-only substring replace used for the error highlight. |
| **239** | `mc[0].stem` embeds a full inline `style="background:…;border:…;border-radius:8px;padding:12px 16px;margin-top:10px;font-style:italic;font-size:14px"` block. Presentation baked into the data. |
| **145–148** | **The logo is not the house lockup.** `viewBox="0 0 260 68"` (spec: `0 0 200 78`), `font-family="Arial Black,sans-serif"` (spec: DM Sans), `font-size="32"` (spec: 20.8), `letter-spacing="4"` (spec: 8), `fill="#111111"` hardcoded (spec: `var(--accent)` / `var(--text)`). No `.fe-logo` class. The two lines do not render to the same optical width, and "Arial Black" is a fourth font family against §6's three. |
| **13–15, 39, 60, 81, 215** | **Hardcoded `rgba(0,0,0,…)` × 5** (`0.08`, `0.1`, `0.12`, `0.28`, `0.75`), **`#fff` × 4**, and **~14 raw hex values** including hand-picked `--green:#1a6e36` and `--red:#a82020`. Direct violation of the standing constraint in `CLAUDE.md` and §4a. Nothing in this file is derived from the hero. |
| **734** | Results copy: *"Re-read the reference section carefully."* There is no reference section; the Grammar Focus note is on the intro screen and is unreachable from the results screen. |
| **733** | Results copy: *"Revisit the grammar notes."* Same problem. |
| **6** | `<title>B2 Grammar Lesson</title>` — no lesson identity. (Library card title lives in Supabase per §11.2; the `<title>` still wants fixing.) |
| **162** | 714 KB base64 hero inlined instead of `--hero: url('TopGearB2/hero.jpg')`. |
| **37–39** | Hero is an `<img>` inside a bordered `.hero-image-wrap` with a captioned black bar — §5b's "do not put an `<img>` in a card". |
| — | **No entry in `library.html`'s `LESSON_IMAGES` map.** The lesson currently falls back to the placeholder card. |
| — | Dead CSS is minimal — I found no unused rule blocks. Credit where due. |

### C-Jargon. Terms used before they are defined

| Term | First appearance | Pre-answer? |
|---|---|---|
| **third conditional** | L308, L332 — **gap hints, pre-answer** | Yes, **and it is never taught anywhere in the file.** The intro covers *mixed* conditionals only. Tested 3× (`fitb[1]`, `fitb[4]`, `err[1]`) = 15% of the lesson. |
| **perfect infinitive** | L316 — `fitb[2]` hint, **pre-answer** | Yes, **never defined.** |
| **reporting verb** | L247 — `mc[0]` explanation | No. Appears 8×, defined never, and is the load-bearing term for two of the four structures. |
| **cleft sentence** | L272 — `mc[3]` **stem** | The intro box is headed "Cleft Sentences" and shows two examples but never says what a cleft *is* or that there are two kinds. |
| **It-cleft** / **Wh-cleft** (capitalised) | **L401, L403 — as Activity 4 answer options** | The capitalised terms appear nowhere in pre-answer text. Lower-case `it-cleft` first occurs at L280 in a post-answer explanation. |
| **stative verb** | L291 — `mc[4]` explanation | **Only occurrence in the file**, and `mc[4]` is unanswerable without it. |
| **pseudo-cleft** | L413 — match explanation | Only occurrence. |
| **conditional perfect** | L334 — `fitb[4]` explanation | Only occurrence. |
| **relative clause** | L364 — `err[2]` explanation | Only occurrence. |
| **complement** | L403 (answer option), L413 (explanation) | Never defined. |
| **backshift** | **0 occurrences** | The single most useful term for half this lesson is not in the file. |

---

## PART C8 — FACTUAL AUDIT

### Confirmed errors

**1. `fitb[1]`, L307 — Top Gear did not move to Amazon.**
> *"If the show had not moved to Amazon, it would have lost its original audience entirely."*

*Top Gear* did not move. It continued on BBC Two with new presenters from 2016. What moved to Amazon Prime Video were **the presenters** (Clarkson, Hammond, May) and executive producer Andy Wilman, who made a **different programme**, *The Grand Tour*, from 2016. Read as *Top Gear* — which is what "the show" refers to throughout this lesson — the sentence is false. It is also self-contradictory within the file: the very next item (`fitb[2]`) correctly treats *The Grand Tour* as a separate show.
**Correction:** *"If the presenters had not moved to Amazon, The Grand Tour would never have existed"* — or name the show: *"If The Grand Tour had not launched on Amazon…"*. Same grammar target, third-conditional negative if-clause, preserved.

**2. `fitb[3]`, L321–323 — Clarkson did not introduce the Stig, and this false claim is the graded answer.**
> *"It was Jeremy Clarkson who first introduced the Stig character to the show."*

The Stig debuted in Series 1 of the relaunched *Top Gear* in 2002. The character was a production creation, generally credited to executive producer **Andy Wilman**; the *name* comes from Clarkson's school slang at Repton for a new boy, which is a real but narrow connection. The first Stig ("the Black Stig") was **Perry McCarthy**. Crediting Clarkson personally with introducing the character is unsupported — and here it is not incidental colour: the learner must **type** `was Jeremy Clarkson who` for the point, so the false attribution *is* the key.
**Correction:** move the cleft onto something verifiable and preferably non-attributive — *"It was the Stig who set every timed lap on the Power Lap board"* — or keep an attribution and make it right: *"It was Andy Wilman who produced the relaunched show."*

**3. `mc[1]`, L253 — the key asserts the opposite of the record.**
> *"If Hammond hadn't crashed in 2006, he would still be presenting the show."*

Hammond's crash was **20 September 2006** at Elvington Airfield, Yorkshire, in a jet-powered Vampire dragster — the date is correct. But the counterfactual is backwards: he *did* crash, returned to *Top Gear* within months, presented it until 2015 and then *The Grand Tour* until 2024. The consequent ("he would still be presenting") implies he is not, which is false. Option A ("he would have continued the season") has the same problem — he did continue.
The grammar is sound; the content is not, and any learner who watches the show gets a contradiction at exactly the moment they are being asked to trust the sentence.
**Correction:** keep the mixed-conditional shape, change the proposition to something the counterfactual actually licenses — e.g. *"If Hammond hadn't crashed in 2006, the show wouldn't have such strict safety rules today."*

**4. `fitb[2]`, L315 — the viewing figure is not a documented number.**
> *"The Grand Tour is reported to have attracted over 4.5 million viewers on its opening night."*

Amazon has never published viewing figures for *The Grand Tour*. Its statements at launch were relative ("the biggest premiere ever on Prime Video"), never numeric. The figures that *were* widely reported around the 18 November 2016 premiere were piracy estimates, not viewership. **No source supports "4.5 million on opening night."** The hedge "is reported to" is doing real work here, but a precise fabricated statistic presented as an exercise sentence is exactly the class of error this repo has shipped before.
**Correction:** use a citable number about a different subject — *Top Gear*'s BBC Two audience is published and was in the 5–6 million range at its peak — or drop the figure: *"The Grand Tour is reported to have broken Amazon's premiere record."*

### Checked and correct — do not "fix"

- **`err[4]`, L381 — Clarkson and the Bugatti Veyron.** *"the greatest car ever made"* is a well-attested Clarkson line about the Veyron, used repeatedly in his *Top Gear* review and in print. The claim stands; the item's grammatical target (`what` → `that` in an it-cleft) is also sound.
- **`match l3`, L396 — "It was the Stig who drove the fastest lap."** Correct characterisation of the Stig's role (the Power Lap board).
- **`mc[2]`, L261 — "most-watched car show for a decade."** Attributed to unnamed producers, and defensible in substance: *Top Gear* held a Guinness World Record (2013) as the world's most widely watched factual television programme.
- **Spelling is consistently British throughout** — *apologise, apologised, revolutionised, encyclopaedic, most-watched*. No AmE contamination anywhere in the file. This is better than `forbes-nature-agency-part2`. The only spelling problem is downstream: the `accepted` arrays enforce BrE **only**, so `apologized` / `revolutionized` are marked wrong (see C6).
- **Geography:** the file makes no geographical claim at all. Nothing to correct.
- **Law:** the file makes no legal claim. "Suspended", "internal review", "contract" are employment description, not statute. Nothing to correct.
- **Motoring:** apart from the Amazon/Top Gear conflation above, the motoring content is accurate. No car specification is stated anywhere, so there is nothing of the "sand martins in flint" class in the technical material.

### Invented quotations and actions attributed to real people — recorded, not for removal

Per the standing constraint the characters stay. Noting these as findings only:

| Line | Attribution | Note |
|---|---|---|
| **239** | Clarkson, direct quotation: *"I will never apologise for what I said."* | Invented. Also contrary to the record — Clarkson publicly apologised in May 2014 over the unaired "eeny meeny miny mo" footage. |
| **329–331** | Hammond, reported statement: *"he would have retired from TV presenting if the accident had been more serious."* | Invented. He returned to presenting within months and has not said this. |
| **340** | Clarkson, reported statement: *"he has always loved fast cars and he will never change his mind."* | Invented, benign in content. |
| **351** | Clarkson, counterfactual: *"If Clarkson would have apologised sooner, the BBC might not have suspended him."* | The premise is contrary to record — Clarkson reported the March 2015 incident himself the following day and apologised to the producer involved. It also editorialises about a physical assault on a real, named-in-reality third party, framing it as something a timely apology would have cured. Worth rewriting the *content* while keeping the `would have` → `had` target, independent of the factual point. |
| **283** | James May: *"an encyclopaedic knowledge of aviation history."* | Invented as a specific characterisation, but broadly supported — aviation is a genuine and documented May enthusiasm alongside cars, motorcycles, wine and music. Softened further by being a hedged report ("is known to have"). Lowest-risk item in this table. |
| **261** | "The producers announced…" | Invented but unattributed and substantively defensible. |
| **297** | "A BBC spokesperson told journalists…" | Invented but generic and consistent with the real March 2015 internal investigation. |

---

## PART D — TEACHING GAPS

### What the lesson tests

| Structure | Items | Share |
|---|---|---|
| Reported speech / backshift | `mc[0]`, `mc[2]`, `fitb[0]`, `err[0]`, `match l1` | 5 (25%) |
| Conditionals — **third** | `fitb[1]`, `fitb[4]`, `err[1]` | 3 (15%) |
| Conditionals — **mixed** | `mc[1]`, `match l2` | 2 (10%) |
| Clefts (it- and wh-) | `mc[3]`, `fitb[3]`, `err[4]`, `match l3`, `match l5` | 5 (25%) |
| Complex passives | `mc[4]`, `fitb[2]`, `err[3]`, `match l4` | 4 (20%) |
| Relative pronoun as subject | `err[2]` | 1 (5%) |

### What the lesson teaches

**84 words, on a screen the learner sees once and cannot return to.** Four boxes, each one label + 1–2 example sentences + a one-line gloss. Nothing on the third conditional, nothing on what does or does not backshift, nothing on stative verbs, nothing on relative pronouns, nothing that names *it-cleft* or *wh-cleft*, and no definition of *cleft*, *reporting verb*, *perfect infinitive* or *backshift*.

**The tested/taught mismatch is total: the lesson devotes 15% of its items to a structure (the third conditional) it never teaches, and 5% to one (relative pronoun subjecthood) that appears nowhere but a single post-answer explanation.**

### What exists only in feedback

Fifteen of the seventeen rules identified in C4. The most consequential:
- **Backshift is optional in two named circumstances** — and the file *knows* this (`mc[2]` explanation) while `mc[0]` and `err[0]` mark the un-backshifted form wrong. **The lesson contradicts itself, and both halves of the contradiction live in post-answer feedback.** This is the single most important thing to fix.
- **Stative verbs** — one occurrence, post-answer, and `mc[4]` cannot be reasoned about without it.
- **`It is thought that…` as the legitimate alternative** — `err[3]` penalises *"is thought that it revolutionised"* without ever showing the learner that *"It is thought that the show revolutionised…"* is perfectly good English. The learner is left believing the `that`-clause pattern is banned.

### The 14 teaching slides the rebuild must add

| # | Slide | Covers |
|---|---|---|
| 1 | **Orientation** | The four structures, one line each, and why a B2 learner needs them. Replaces the intro Grammar Focus note. |
| 2 | **The backshift table** | present→past, past→past perfect, present perfect→past perfect, `will`→`would`, `can`→`could`, `must`→`had to`. One table, colour-coded per §5a's tense palette (present simple `#16345C`, past simple `#B08968`, past perfect `#6E0B24` — no more than three on one slide). |
| 3 | **What does *not* backshift** | Still-true statements; timeless facts; reports made immediately; modals that are already past (`would`, `could`, `should`, `might`). **The rule the lesson currently breaks.** Explicitly state that both the backshifted and un-backshifted forms are correct. |
| 4 | **Pronouns, time and place** | `this`→`that`, `here`→`there`, `tomorrow`→`the next day`, `I`→`he/she`. Currently demonstrated silently in the intro example ("*that* car") and never mentioned. |
| 5 | **Third conditional** | `if + past perfect` → `would have + past participle`. Form and meaning. **Tested three times, taught nowhere.** |
| 6 | **Mixed conditional** | `if + past perfect` → `would + infinitive` (present result), contrasted side-by-side with slide 5. This contrast *is* the teaching point of `mc[1]`. |
| 7 | **What cannot go in an if-clause** | No `would`, no `would have`. Currently in `mc[1]` and `err[1]` feedback only. |
| 8 | **It-clefts** | `It + be + FOCUS + that/who + rest`. Show subject focus, **object focus and adverbial focus** — the lesson's own `err[4]` is object focus, which its Activity 4 label wrongly denies. |
| 9 | **Wh-clefts (pseudo-clefts)** | `What + clause + be + FOCUS`. Named, defined, contrasted with slide 8. |
| 10 | **`that`/`which`, never `what`** | After an it-cleft. The `err[4]` rule, taught before it is tested. |
| 11 | **Complex passive, pattern 1** | `It is said/thought/believed that + clause`. **The legitimate `that`-clause form `err[3]` currently penalises without ever showing it.** |
| 12 | **Complex passive, pattern 2** | `Subject + is said/known/reported + to + infinitive`, and `to have + past participle` when the event is earlier. Covers `mc[4]`, `fitb[2]`, `err[3]`, `match l4`. |
| 13 | **Stative verbs and the continuous** | `know, believe, understand, own, seem`. `mc[4]` turns entirely on this. |
| 14 | **Terminology** | Chip strip: *reporting verb, backshift, perfect infinitive, cleft, focus, complement, relative pronoun*. Ten of these terms are currently used before or without definition; *backshift* is not in the file at all. |

Optional 15th if the deck is split: **the relative pronoun as subject** (`err[2]`'s resumptive-`it` rule) — otherwise fold it into slide 14 as a one-line note.

---

## PART E — ARTWORK FIT

### `TopGearB2/hero.jpg`

**1672 × 941, JPEG, RGB, 187,592 bytes. Aspect 1.777 — exactly 16:9.** Above §3's 1400px minimum. No conversion needed.

**What it depicts.** A flat-vector, posterised illustration in a limited-palette style. Three men stand in a row facing the viewer, leaning against a **British police car** — white body with the fluorescent lime-yellow and blue Battenburg side markings and a blue roof lightbar. Left: a shorter man with a moustache in a dark brown jacket over a grey shirt and blue jeans. Centre: a taller man in a grey-olive field jacket over a white top, wearing a **bright lime-green cap**. Right: a man with long curly grey hair and a moustache in an olive knit jumper and blue jeans, arm resting on the car roof. Behind them, a dark conifer treeline; above it a pale cream sky band; a red-brick building at the right edge.

It is unmistakably the three-presenter group portrait the lesson is built around, in the Stranger Gears rendering. **It depicts precisely what the lesson is about** — the opposite of the Nature Agency Part 2 situation, where the artwork and the text were about different continents. No caveat needed.

**Measured luminance:** mean relative luminance **0.2032**, **median 0.0878**, p10 0.0311, p90 0.7627. By thirds: top 0.2846, middle 0.1075, bottom 0.2095. Dominant colours: dark olive `#595732` (34.6%), slate `#272f31` (17.5%), warm grey `#57564f` (15.9%), cream `#ede3cc` (10.0%), police navy `#173853` + `#274761` (12.5%), fluorescent lime `#e3ea2e` (4.4%).

The distribution is the important number: **the median pixel is at 0.088 luminance** — this is a dark image with a bright cream band across the top ~10% that pulls the mean up. It is not "bright and airy". This is a dark-theme hero.

### Contrast tables

**Dark** (`extract-palette.py TopGearB2/hero.jpg`):

```
--void #111415  --surface #1b2122  --surface2 #242c2e  --border #84872b
--text #f5f5f2  --text-dim #bebfa3  --accent #e4ea2e  --accent-bright #c0c600
--accent-dim #a2a616  --secondary #0355ad  --contrast #4c96f0
```

| Row | Ratio | Min | Result |
|---|---|---|---|
| text on surface | **14.99:1** | 4.5 | PASS |
| text on void | **16.94:1** | 4.5 | PASS |
| text-dim on surface | **8.71:1** | 4.5 | PASS |
| accent on surface | **12.52:1** | 4.5 | PASS |
| accent-bright on surface | **8.83:1** | 4.5 | PASS |
| contrast on surface | **5.37:1** | 4.5 | PASS |
| border on surface | **4.27:1** | 1.25 | PASS |
| accent-bright vs text | **1.70:1** | 1.45 | PASS |

**Light** (`--light`):

```
--void #d8cbac  --surface #e1d9c4  --surface2 #dcd1b8  --border #94964a
--text #292a11  --text-dim #5c5e2e  --accent #515400  --accent-bright #515400
--accent-dim #bac00e  --secondary #0355ad  --contrast #0d4d9c
```

| Row | Ratio | Min | Result |
|---|---|---|---|
| text on surface | **10.45:1** | 4.5 | PASS |
| text on void | **9.17:1** | 4.5 | PASS |
| text-dim on surface | **4.82:1** | 4.5 | PASS |
| accent on surface | **5.73:1** | 4.5 | PASS |
| accent-bright on surface | **5.73:1** | 4.5 | PASS |
| contrast on surface | **5.86:1** | 4.5 | PASS |
| border on surface | **2.21:1** | 1.25 | PASS |
| accent-bright vs text | **1.83:1** | 1.45 | PASS |

Both pass every row, so contrast alone does not decide it. Three things do.

### Recommendation: **dark theme.**

1. **The image is dark.** Median luminance 0.088; the middle third — where the content sits — is 0.1075. §4a's light theme is for "a hero that is bright and airy — open sky, daylight, pale illustration." This is a conifer treeline at dusk with a cream strip along the top. Forcing it light is exactly the mistake §5 warns about in reverse.
2. **The light palette has collapsed its emphasis step.** `--accent` and `--accent-bright` are the **identical value `#515400`**, so both read 5.73:1. §4a requires `--accent-bright` to go *darker* than the accent — on paper, emphasis means more ink. Here there is no emphasis step at all: headings and buttons would be indistinguishable, and every `--accent-bright` highlight in the deck would render as a plain accent. `--border` also drops to 2.21:1 against the dark theme's 4.27:1, so card and option hairlines nearly vanish. And `--void #d8cbac` sits at roughly 0.80 lightness, above §4a's ~0.76 ceiling.
3. **The dark palette is a faithful and useful read of the picture.** `--accent #e4ea2e` is the fluorescent Battenburg lime lifted straight off the police car and the centre figure's cap; `--secondary #0355ad` and `--contrast #4c96f0` are the police blue. Hi-vis lime and police blue on near-black is a motoring/roadside identity that belongs to this lesson and to no other on the site — which is the entire point of §4.

**Logo mark:** keep `var(--accent)`. The lime is only 4.4% of the image and the dominant tones are dark olive and slate, so the mark will snap rather than blend. `--contrast #4c96f0` is available if a second data colour is needed (e.g. to colour-code it-cleft against wh-cleft), and it clears 5.37:1.

**Background treatment:** start at `--bg-opacity: 0.72` per §5 and **measure with `bgmeasure.py` before adjusting.** One thing to watch: the top ~10% cream band (top-third mean luminance 0.2846) sits exactly where the eyebrow, deck bar and progress rail live. If the eyebrow falls under 3.5:1 with the standard halo, raise `--wash-edge` **on this lesson only** — do not flatten `--wash-mid`, and do not drop the opacity below 0.65.

### Which slides it suits

| Slide | Fit |
|---|---|
| **Cover** | Ideal. Exactly 16:9, the group portrait is the lesson's frame, and the stacked logo plus a 62px title will sit over the centre scrim against the mid-grey jackets. |
| **All Activity 1 slides** | Strong. `mc[0]`, `mc[1]`, `mc[3]` and `mc[4]` are *about* the three men in the picture — the artwork is the item cast. |
| **All Activity 3 slides** | Strong, same reason (`err[0]`, `err[1]`, `err[4]` all name Clarkson). |
| **Teaching slides 2–14** | Fine as the standard reduced-opacity pattern. The dark middle band is the most legible region in the image, and every card is translucent over it. |
| **Results and activation** | Good — the group portrait as a closing image reads as a curtain call. |
| Activity 2 gap slides | Fine, but these are the text-heaviest slides; if `bgmeasure.py` shows the gap sentence struggling, these are the ones to check first. |

There is **no second image supplied for this lesson**, so every slide takes the hero and no `data-bg` overrides are needed. (`Top-Gear-Lads-Messing-Around.jpg`, 2560×1536, exists at the repo root and `Top Gear/` holds further assets, but they belong to `forbes-english-lesson-TopGear.html` and `top-gear-skiing-lesson.html`; they are 5:3 and unaudited. Do not borrow them without a decision.)

---

## Checker status (as shipped)

`node lesson-template/check-lesson.js forbes-english-b2-lesson.html` → **"0 slides", 4 checks failed.** But read the passes carefully:

| Gate | Reported | Real |
|---|---|---|
| LAYOUT | **FAIL** — page scrolls | Genuine. |
| ANSWERS | PASS | **Vacuous** — the gate reads `section.slide[data-type=mc] .opt[data-correct]`; this file has none, so it inspected nothing. My manual measurement (C1) says it would *also* pass genuinely, which is the good news. |
| BANK | PASS | Genuine — there is no word bank (C5). |
| MARKUP | PASS | Genuine — explanations go through `innerHTML`, and their `<em>` tags render (L502, L553, L627). |
| SORT | PASS | Vacuous — no sort slides. |
| EXPLAIN | PASS | **Vacuous, and misleading** — 5 of 20 items (Activity 4) have no *wrong-answer* explanation at all, and 15 of 20 have identical right/wrong feedback. |
| ACTIVATION | **FAIL** | Genuine — no `data-type="activate"`. |
| I18N | **FAIL** | Genuine — no `UI_I18N`, English only. |
| LOGO | **FAIL** | Genuine — Arial Black, wrong viewBox, wrong metrics, no `.fe-logo`. |
| RUNTIME | PASS | Genuine — no JS errors thrown, though the `\u2713` and restart bugs are silent failures a JS-error check cannot see. |

---

## HIGHEST-PRIORITY FIXES FOR THE REBUILD

1. **Delete the `placeholders` array.** Six of six input fields in Activity 3 print the exact accepted answer as ghost text — 25% of the lesson is free to anyone who looks at the box. This is the single most damaging defect in the file and the cheapest to fix.
2. **Make Activity 4 losable.** A wrong match must cost that item's point, and the completion gate must not require all five. Verify against a deliberately wrong run before trusting it. Per the Nature Agency precedent the shared match engine still cannot be lost, so **convert the five pairs to five one-per-slide "identify the structure" MC items** — which also fixes the 592px overflow measured in Part B and gives each pair the explanation it deserves. Changing `deck.py`'s match engine affects ~30 shipped lessons and is not a decision for this build.
3. **Fix the scoring scale.** With 1 and 2 done, the reported score stops being `50 + 0.5 × real`. Confirm the sub-50% band is reachable — today it is not. Score `err[0]` as **2 gaps = 2 points** (rebuilt total 21), not all-or-nothing for 1.
4. **Resolve the backshift self-contradiction.** `mc[2]`'s explanation licenses the un-backshifted form; `mc[0]` and `err[0]` mark it wrong. Teach the optionality on a slide (Part D slide 3), accept `was made` in `fitb[0]`, accept `has always loved` in `err[0]` or replace that item, and rewrite `mc[0]` so option C is genuinely wrong rather than merely less formal.
5. **Fix the four factual errors** (C8): `fitb[1]` Top Gear→Amazon; `fitb[3]` Clarkson→the Stig, where the false claim *is* the key; `mc[1]`'s backwards counterfactual about Hammond; `fitb[2]`'s undocumented 4.5-million figure. All four can be corrected without touching a grammar target and without touching a character.
6. **Rewrite the distractors in `mc[1]`, `mc[3]` and `mc[4]`.** In each, all three distractors are broken English, so the item is solvable by ear with zero knowledge of the target structure. `mc[0]` and `mc[2]` show how it should be done — same length, all grammatical, wrong for a taught reason. Keep the key lengths as they are; the ANSWERS gate is passing and should keep passing.
7. **Derange the MC key positions.** `[1,1,1,0,0]` — A twice, B three times, **never C, never D**, and nothing shuffles at runtime, so every learner sees the same letters every time including after restart. Set them at build time and verify the distribution.
8. **Add the 14 teaching slides** in Part D. Priorities: the **third conditional** (tested 3×, taught nowhere), the **backshift table and its exceptions**, **stative verbs** (`mc[4]` is unanswerable without it), **`It is thought that…`** as the legitimate alternative `err[3]` currently penalises without showing, and a **terminology slide** — *backshift* does not appear in the file at all, and ten further terms are used before they are defined.
9. **Give right and wrong different feedback on all 20 items.** Fifteen currently differ by a two-word prefix only, and Activity 4's wrong branch shows one generic string for all five pairs. Inject per-option `data-explain` after calling `D.mc`, as `build_nature2.py` does — and if this is the third lesson to need it, promote it to an `explains=` argument on `D.mc`.
10. **Normalise gap input properly.** `trim().toLowerCase()` alone rejects double spaces and curly apostrophes — the latter will hit every learner on a phone, on the one item that invites `hadn't`. Add whitespace collapsing, apostrophe normalisation, and `-ise`/`-ize` tolerance (`apologized`, `revolutionized`), plus the alternatives listed in C6.
11. **Fix the two over-general cleft labels** — "It-cleft emphasises the subject" is contradicted by the lesson's own `err[4]`, and re-label `match l1`, which asks the learner to call a direct quotation "reported speech".
12. **Reference the hero from disk.** `--hero: url('TopGearB2/hero.jpg')` in place of the 714 KB base64 blob: **760 KB → 46 KB** before any content change, plus §5b compliance (the picture becomes the background, not a captioned box). Add `"forbes-english-b2-lesson.html": "TopGearB2/hero.jpg"` to `LESSON_IMAGES` in `library.html` — there is currently no entry.
13. **Build dark**, palette pasted verbatim from `extract-palette.py TopGearB2/hero.jpg` — every row passes with margin, and the light variant has collapsed `--accent` and `--accent-bright` to the same value. Remove all 5 hardcoded `rgba(0,0,0,…)`, the 4 `#fff`, and the ~14 raw hex values including the hand-picked `--green`/`--red`. Measure the background with `bgmeasure.py`; watch the cream band at the top where the eyebrow sits.
14. **Satisfy the four failing gates:** LAYOUT (it is a scrolling page), ACTIVATION (speaking + writing + target-language strip), I18N (English plus one complete language — German is the minimum), LOGO (the file uses Arial Black at the wrong viewBox and metrics; copy `forbes-logo.svgfrag` verbatim). Note that today's ANSWERS, SORT and EXPLAIN passes are vacuous — the gates found nothing to inspect.
15. **Sweep the artefacts** in C-Artefacts: the `\u2713` CSS escape rendering as literal "u2713" on completed tabs; the restart bug that leaves the previous run's finished matching board on screen with Activity 1 hidden; the results copy pointing at a non-existent "reference section"; the "exactly one error" instruction on a two-error item; the inline `<div style>` inside `mc[0]`'s stem; the generic `<title>`.
16. **Budget 37 slides** (22 as a straight port + 14 teaching + 1 activation), or split at the conditionals seam into 21 + 20. Update the "~30 minutes" claim either way.