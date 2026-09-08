# Syllabus gaps — what the catalogue does not teach yet

Measured 2026-09-08 against `tools/lessons.json` (294 rows) with the script
described at the bottom. For each point on a standard A1–C2 grammar and
skills syllabus it counted lessons whose **title** names the point (a
lesson *about* it) and lessons whose **body** merely mentions it (touched
inside something else). "Own" is the number that matters; "touched" is
the weak signal and is often a stray word in a story.

Innes's own example — *used to* + infinitive against *be/get used to* +
-ing — is **covered**: `sherpa-tensing-cloud-used-to.html`,
`sherpa-tensing-cloud-be-used-to.html`, and the contrast lesson
`forbes-english-venezuela.html` ("Used To & Be Used To — Venezuela
Edition"). *Would* for past habits, the third member of that family, has
no lesson.

## Where the site is strong

The tense line is complete twice over. Every one of the thirteen tenses
has Sherpa Tensing, and the eight most-used have Block Camp (active and
passive) and a Minecraft time-signals drill as well. Passive voice has 24
lessons of its own. Prepositions has 12. Modals of obligation, past
modals, presentations and the IELTS route are all well served.

## Missing entirely — no lesson of its own

Grouped by where a coursebook would put them. Level is where the point is
normally introduced.

### A1–A2 (the foundations under everything else)

| Point | Touched in | Note |
|---|---|---|
| Articles (a / an / the) | 26 | The single biggest gap for German and Spanish speakers; Swiss Precision touches it in passing |
| Countable / uncountable, some / any | 22 | |
| Quantifiers (much / many / few / little) | 3 | |
| Comparatives and superlatives | 13 | Nothing at all at A2, where it belongs |
| Adverbs of frequency | 5 | The `adverbs-of-frequency-0-100.png` in the root suggests one was planned |
| Demonstratives, there is / there are | 4 | |
| Too / enough / so / such | 4 | |
| Modals of ability and permission (can / could / may) | 11 | Every modal lesson starts at obligation |
| Zero conditional | 3 | |
| Say / tell / speak / talk | 0 | Make / do / take / put is done five times; this pair never |
| Numbers, dates, telling the time | 1 | |
| Giving directions | 2 | |
| Health / at the doctor | 3 | |
| Small talk / socialising | 4 | |
| Describing a picture | 5 | `english_class_picture_description.html` is in the catalogue but its title does not say so, so nobody searching for it finds it |
| Pronunciation and word stress | 8 | Nothing on the site is about sound |

### B1–B2 (the exam and the office)

| Point | Touched in | Note |
|---|---|---|
| Reported speech | 11 | A category exists in `library.html`; only `sherlock-scarlet-star.html` is tagged into it by hand |
| Reporting verbs (suggest, deny, admit…) | 6 | |
| Question tags | 0 | Absent |
| Indirect questions (could you tell me…) | 3 | |
| Relative clauses, defining | 17 | |
| Relative clauses, non-defining | 2 | |
| Verb patterns (stop to / stop -ing, remember, try, forget) | 0 | Absent. Gerunds & infinitives has six lessons but none on the meaning-changing pairs |
| Dependent prepositions (depend on, interested in) | 5 | Twelve preposition lessons, all place and time |
| Wish / if only | 6 | |
| Mixed conditionals | 4 | The three conditional lessons teach 1st, 2nd and 3rd together; none teaches one on its own |
| Unless / as long as / provided that | 75 | Touched everywhere, taught nowhere |
| Future in the past (was going to, would) | 8 | |
| Would for past habits | 2 | Completes the *used to* family |
| Collocations | 41 | |
| Word formation (prefixes, suffixes) | 54 | An IELTS and Cambridge staple |
| Register: formal vs informal | 128 | The most-touched, least-taught point on the site |
| Punctuation and spelling | 25 | |

### C1–C2 (what a C1 student asks for by name)

| Point | Touched in | Note |
|---|---|---|
| Inversion (never have I…, not only…) | 17 | |
| Cleft sentences (what I need is…) | 8 | |
| Participle clauses | 3 | |
| Emphasis (do / did, so / such) | 6 | |
| Ellipsis and substitution | 7 | |
| Subjunctive and formal structures (I suggest he go) | 5 | |

## Thin — exactly one lesson, and often at the wrong level

| Point | The one lesson | Problem |
|---|---|---|
| Present continuous for the future | Block Camp — Present Continuous 1b | Only as a slide inside a tense deck |
| Modals of possibility (may / might / could) | Might vs Going To — A2 Test | A test, not a lesson |
| Modals of deduction | The Thornwick Deduction | Good, but alone |
| Causative (have / get something done) | Sherpa Tensing — The Moon | |
| Adjective order | The Locked Study | |
| Adverbs vs adjectives | Adverbs, Will & So/Neither — Test | A test, not a lesson |
| Hedging and diplomatic language | Dailies Review | |
| Email writing | Emails, Calls & Follow-ups (Part 3) | Parts 1 and 2 are not in the catalogue |
| Telephone calls | Emails, Calls & Follow-ups (Part 3) | Same lesson |
| Meetings | Say it in your own words | Open-answer practice, not the language of meetings |
| Job interviews | Tech Interview Masterclass (C1) | Nothing at B1/B2, where most candidates are |
| Travel / hotel / airport | Conservation Travel (C1) | Nothing at A2 |
| Complaints | Escalating a Complaint (C1) | Nothing at B1 |
| Listening | IELTS Listening Part 9 | The four audio lessons are still "in build" |
| Past perfect continuous, future continuous, future perfect continuous | Sherpa Tensing only | No Block Camp and no time-signals drill for these three |

## What this means for the queue

Three things fall out of the table, in order of return:

1. **A2 foundations series.** Articles, countable/uncountable, quantifiers,
   comparatives, adverbs of frequency, can/could/may, say/tell. Seven
   decks, all short, and between them they close the largest hole for the
   German and Spanish speakers the site is built for. Block Camp's format
   fits them exactly — one point, one camp.
2. **The B1–B2 grammar the exams test and the office needs:** reported
   speech and reporting verbs, relative clauses, verb patterns, question
   tags and indirect questions, register. Reported speech first — the
   category already exists and is empty.
3. **A business route**, which is where the thin rows point: meetings,
   emails (Parts 1 and 2), calls, interviews at B2, complaints at B1,
   small talk. That is the syllabus for the Business hub the collections
   page now has a card for.

## How it was measured

A Python script with a table of 90 syllabus points, each with a title
regex and a body regex, run over every catalogue row: title against
`title + file`, body against the lesson HTML with tags and scripts
stripped and the JS string literals kept (decks hold their text in JS).
The regexes are deliberately generous on the body side, which is why
"touched" over-counts — treat it as "not zero", nothing more. A point
with own = 0 and touched = 0 is genuinely absent from the site. Re-run it
after a batch of new lessons; if the script is not to hand, the table
above is the spec.
