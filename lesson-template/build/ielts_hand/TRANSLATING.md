# Translating a hand-written IELTS deck

One folder per deck. `en.json` is the whole English dictionary, written by
`ielts_hand_i18n.py extract` from the deck itself. `content.json` is the
part a translator writes: the English keys that no shared source covers.
Buttons, the score chip, the results messages and the ledger labels come
from `chrome_i18n.CHROME` and `ielts_langs.TAIL_MORE` and are overlaid at
inject time, so they are not in `content.json` and must not be retyped.

A translation is one file per language, `<code>.json`, with **exactly the
keys of `content.json`**, in the same order, every value a string. A key
missing from the file leaves the whole language out of the deck's menu
(HOUSE-STYLE §8: a partial language is a failure, not a work in progress).
A key that is not in `content.json` is dropped with a warning.

    py lesson-template/build/ielts_hand_i18n.py status <deck.html>

reports, per language, "complete" or the keys that are missing, plus
warnings (tags that differ from the English, a value identical to the
English, quoted English outside `<bdi>` in Arabic). Run it before you stop.

## The ten languages and their register

`ielts_langs.py` fixes these so that a deck's own text and its buttons speak
with one voice:

| code | language | address the learner as | notes |
|---|---|---|---|
| de | German | du | already written; the reference for every decision below |
| es | Spanish | tú | |
| fr | French | vous | |
| it | Italian | tu | |
| pt | Portuguese | tu | **European** Portuguese: *Seguinte*, *Carrega*, *diapositivo* |
| ru | Russian | вы | |
| ar | Arabic | — | Modern Standard Arabic, **Western digits** (20%, 150, 2010), see the `<bdi>` rule |
| zh | Chinese | 你 | Simplified, full-width punctuation （，。：；！？） |
| ja | Japanese | — | です／ます |

## What stays English

The deck teaches English. HOUSE-STYLE §8: translate the chrome and the
rule; never the English under test. In practice, for these decks:

- **Words and phrases the learner is being taught to write or say** stay
  English, in every language: *steadily*, *roughly*, *just under half*,
  *Overall*, *outweigh*, *To what extent*, the linking words, the
  paraphrase pairs (*shows* → *illustrates*). They are usually marked
  `<strong>` or `<em>`, or quoted. Keep the marking, keep the English.
- **Example sentences and model-answer extracts** stay English. The
  sentence around them (what it shows, why it works) translates.
- **Reference banks** (`lw…` keys, "Reference · not scored") stay English
  where the German kept them English.
- **IELTS vocabulary**: *Task 1*, *Task 2*, *Band 7*, *IELTS*, *C1*,
  *Overview*, *Introduction*, *Body 1* follow the German: where the German
  kept the English word, keep it; where the German translated it
  (Überblick, Einleitung, Hauptteil), translate it.
- **Chart categories and data** (Streaming, Socialising, 18–30, 60+) follow
  the German.

**The German is the reference.** Open `de.json` beside `content.json` and
match its decisions key by key: what stays English, how long the sentence
is, whether a title is a statement or a fragment. Where `de.json` lacks a
key (the explanations, `x…`), decide by the rules above and by the German's
treatment of the neighbouring explanation-like strings.

## Form

- **Same HTML, same structure.** Keep every `<strong>`, `<em>`, `<br>`,
  `<i>` the English has, round the same words; add none, drop none. The
  only exception is Arabic's `<bdi>`.
- **`…Svg` keys** are a diagram as an SVG string. Translate the text
  between `>` and `</text>` only; every attribute stays byte for byte.
  Keep each label about as long as the German's — the boxes are 170px.
- **Placeholders** (`actPlaceholder`) are plain text: no tags, no
  entities.
- **Characters, not entities.** Write — … “ ” → · as characters, as the
  English does. Do not introduce `&ldquo;` where the English has `"`.
- **Quotation marks** round English words stay as the English has them
  (straight `"` or curly “ ”). Your own language's quotes (« », „ “, 「」)
  are for your own language's text, if you need any.
- **Arrows and separators** (`→`, `·`) stay.
- **Length.** The slides are a fixed 16:9 canvas and the German already
  fits. Aim at the German's length or shorter — Russian and Portuguese run
  long; cut words, not meaning. `answered-overflow.js` measures the result;
  anything that overflows comes back to you.
- **No reference to any earlier version of the lesson** in any string.

## Arabic: `<bdi>`

Any run of English inside Arabic text — a quoted word, a phrase in
`<em>`, a word followed by more English — goes inside **one** `<bdi>…</bdi>`
round the whole run, quotes and tags included:

    في الجزء 1: <bdi>“Do you enjoy cooking?”</bdi> وفي الجزء 3
    الكلمة <bdi><em>steadily</em></bdi> لا تعني

`check-lesson.js` fails the deck on quoted English outside a `<bdi>` and on
an `<em>` that splits an English run round an Arabic word.

## Keys you will meet

- `coverTitle`, `coverSub`, `chip…`/`chipLevel`/`chipFocus`/`chipCount`:
  the cover. `<em>` on the cover title marks the part of the title that is
  set in the accent colour; keep it on the same words' translation.
- `s<N>Eyebrow`/`s<N>Title`/`s<N>ColA…`/`s<N>Note`/`s<N>Ctx`: slide N's
  eyebrow, title, columns, note, context line.
- `q<N>…`, `x<NN><a-z>`: question titles and explanations. An
  explanation is read aloud to the learner after an answer: one or two
  sentences, direct, naming why the answer is right or wrong.
- `act…`: the activation slide — the task instructions translate; the
  English the learner must produce (chips, model fragments) does not.
- `orderHint`, `mCtx` and other instructions: the mechanics of the slide.
- `resNext`, `actTitle`, `actSpeakKind`, `actWriteKind` appear only when
  the deck overrides the template's wording; translate the deck's wording.

## Writing the files

UTF-8, no BOM, LF line endings, `json.dump(..., ensure_ascii=False,
indent=1)` is the house format. Write each language's file as soon as it is
finished rather than all at the end, and check it parses:

    py -c "import json; json.load(open('lesson-template/build/ielts_hand/<slug>/<code>.json', encoding='utf-8'))"

Then `status`. Then stop; `inject` and the checker are the integrator's.
