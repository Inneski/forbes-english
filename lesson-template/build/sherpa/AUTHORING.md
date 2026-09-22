# Authoring `sherpa/i18n/<slug>.json` — the per-page contract

Every Sherpa Tensing deck is built by `lesson-template/build/build_sherpa.py`
from two files: `sherpa/content/<slug>.json` (the page's English, extracted
from the old scrolling page — **never edit it**) and `sherpa/i18n/<slug>.json`
(this file, authored once per page). The manifest to work from is
`sherpa/work/<slug>.manifest.json` (regenerate with `py …/sherpa/manifest.py`).

## The file

```json
{
 "chips": ["yesterday", "last week", "…"],          // 4–8 English phrases
 "quiz": { "3": { "options": ["…", "…", "…", "…"] } },   // only the items the manifest lists under quiz_fix
 "en": { "coverSub": "…", "actTitle": "…", "actUse": "…", "actSpeakBrief": "…",
         "actSpeak1": "…", "actSpeak2": "…", "actSpeak3": "…",
         "actWriteKind": "Writing", "actWriteBrief": "…", "actPlaceholder": "…" },
 "de": { "<every key in manifest.strings>": "…", "<every key in en above>": "…" },
 "es": { "…same key set as de…" }
}
```

`de` and `es` must contain **exactly** the keys of `manifest.strings` plus the
ten authored keys. `en` may contain **only** the ten authored keys — the rest
of the English comes from the content file and is not yours to change.

Check it: `py lesson-template/build/sherpa/verify_i18n.py <slug>` must print
`OK`. Then `py lesson-template/build/build_sherpa.py <slug>` must build, and
`node lesson-template/check-lesson.js <file>` must show no LAYOUT or ANSWERS
failure (HEAD fails until `tools/seo.py` runs; that is expected).

## What translates and what does not (HOUSE-STYLE §8)

Translate the **chrome and the teaching prose**: headings, rule bodies, table
prose, diagram introductions, panel headings, quiz hints and explanations,
result messages, the cover line and the activation stage.

Do **not** translate the English being taught. Anything in double quotes in
an English string is an example sentence: **copy it verbatim**, tags and all.
English verb forms and formulas stay English: `subject + WAS / WERE + verb-ING`
becomes `Subjekt + WAS / WERE + Verb-ING` — translate *subject*, *verb*,
*question word*, *noun*, *person*, *thing*, *doer*; keep every CAPS token
exactly as it is. Table cells that are only English forms (`I had left`,
`went`) are copied unchanged. Grammar-term names follow the page's own
reference translations where the manifest carries any (camps one and two):
German keeps the English tense names (*Present Simple*, *Camp drei*); Spanish
translates them (*presente simple*, *campamento tres*). Elsewhere follow the
same convention.

Keep every HTML tag and entity as in the English (`<em>`, `<strong>`, `<br>`,
`&mdash;`, `&hellip;`). Write umlauts and accents as characters, not entities.
`actPlaceholder` must carry **no entities at all** — it is set as plain text.

## The authored English

- `coverSub` — one line under the title, at most 14 words, what this camp
  teaches in the learner's terms. Not a repeat of the title.
- `actTitle` — a short imperative heading for the activation stage
  ("Now tell the story").
- `actUse` — normally "Use these".
- `actSpeakBrief` — one sentence framing the three prompts (pairs, time).
- `actSpeak1..3` — three **situations**, not comprehension questions, each of
  which cannot be done without this camp's tense. "Tell your partner about the
  last journey you made: where you went, how you got there, what went wrong."
- `actWriteKind` — "Writing".
- `actWriteBrief` — a real audience and purpose, 150–200 words stated, and a
  requirement that forces the tense (e.g. "at least six past simple verbs,
  two irregular").
- `actPlaceholder` — an English opening line the learner could continue.
- `chips` — 4 to 8 short English target-language phrases from this camp (its
  signal words, its auxiliaries), the ones a learner should use in the tasks.

**Grammar tokens in CAPS.** In any English you write that names a form, the
form goes in CAPS and cited words go in double quotes — never lowercase
running prose. `WAS / WERE + verb-ING`, `HAVE / HAS + PAST PARTICIPLE`,
"Dorothy and Toto are "they", so the verb is WERE + running." This is a
hardwired house rule; the German and Spanish keep the same CAPS tokens.

## The quiz fixes

For every item under `quiz_fix` in the manifest the key is the longest option
by four characters or more, so a learner scores by picking the longest.
**Never shorten or change the key.** Replace one or more distractors with
forms of similar length that are wrong for a reason this camp teaches — the
neighbouring tense a learner confuses it with, a wrong participle, a wrong
auxiliary, a wrong word order — so that no longest-by-4 gap remains. Keep
four options, all distinct, all natural-looking English. Example, key
`have been walking` (17) against `are walking / have walked / walk`:
`had been walking` (16), `have been walked` (16), `are been walking` (16).
The explanation is not yours to edit.

## Where the manifest's reference translations come from

Camps one and two carried eight-language UI strings on the old pages; the
manifest's `reference` block holds them. Use them for terminology, not as a
source to copy keys from — the deck's keys are different.
