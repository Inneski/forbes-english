# Brief for ChatGPT — write a lesson that rebuilds into a 16:9 deck fast

**How to use this file.** Copy everything between the two rules into ChatGPT,
then add five lines of your own: the topic, the level, the art style, roughly
how long the lesson should run, and anything the lesson must contain. Ask for
the one HTML file. Then hand that file to Claude — a local session with the
file in `incoming/`, or a cloud task with `Inneski/forbes-english` added as a
source — and say: *"Rebuild this as a deck, to house style."*

This is the deck counterpart to `docs/CHATGPT-RPG-BRIEF.md`, and it exists for
one measured reason. **Beyond the Handlebars, 2026-09-17, arrived as a good
lesson inside a file of which not one byte survived.** Its chrome, CSS,
JavaScript, fonts and layout were all discarded — the deck is generated on our
own template — and then the content had to be *excavated* out of what was left:
the questions were in a `const Q={…}` at the tail, the twelve rider types and
twenty-two bike parts in two more arrays, the teacher notes in a third, and the
twenty-one illustrations were base64 blobs keyed by UUIDs like
`f46d591c-717a-4200-aaa3-e15c20215657_3`, so every picture had to be matched to
its slide by reading alt text. All of that is avoidable, and this brief avoids
it.

**What our engine supplies, and ChatGPT must not try to reproduce:** Playfair
Display, DM Sans and DM Mono; the palette, which is derived mechanically from
the hero image and is never chosen; the 1280×720 stage and its scaler; the
text plates; the language switcher; the progress bar and scoring; the
activation stage; the print stylesheet; the SEO block. Those are identical on
every lesson and come from `lesson-template/`. ChatGPT's job is the **content,
in the shape the builder reads.**

---

You are writing an English lesson that will be rebuilt as a 16:9 slide deck.
Deliver **one self-contained HTML file**.

Your file's own styling does not matter. It is a preview, for checking the
words and the pictures. It will be rebuilt on a fixed template that takes only
the JSON and the images. **The data, the words and the pictures are the whole
deliverable** — get those right and nothing else about the file matters.

## 0. The two blocks that are the actual deliverable

Everything the rebuild needs lives in exactly two places in your file.

**A. One data object.** A single `<script>` at the end of `<body>` containing
one assignment and nothing else:

```html
<script>
window.DECK_DATA = { ...the whole lesson... };
</script>
```

**B. One art block.** A single JSON script tag holding every picture:

```html
<script type="application/json" id="embedded-art">
{ "hero": "data:image/webp;base64,...", "workshop": "data:image/webp;base64,..." }
</script>
```

Three hard rules about these:

- **Nothing in the markup.** Do not render the first question, the first
  teaching card or the first anything into the HTML body. If a string a
  learner reads is not reachable from `window.DECK_DATA`, it does not exist.
- **Semantic art keys.** `hero`, `workshop`, `cafe`, `rider-commuter`. Not
  UUIDs, not `image_4`, not the Midjourney job id. The key is the filename we
  ship, so it should read like one: lowercase, hyphens, no spaces.
- **Send the source file, not a saved page.** Build it, then hand over the
  file you built. Do not open it, click through it and save the DOM — that
  bakes in computed inline styles and whatever state you left it in, and it
  silently drops every question after the first.

## 1. The shape of `window.DECK_DATA`

```jsonc
{
  "meta": {
    "title":  "Beyond the Handlebars",      // short; the <em> goes on the last word
    "subtitle": "One sentence saying what the learner will be able to do.",
    "level":  "B2-C1",                      // A1 A2 B1 B2 C1 C2, or a span: B1-B2
    "focus":  "Precision & inference",      // 2-4 words for the cover chip
    "minutes": 80
  },

  "slides": [ ...in teaching order... ],

  "activation": {
    "chips":  ["cadence", "traction", "lose traction", "..."],  // 8-14 target items
    "speak":  ["Three tasks, one line each — what the learner DOES."],
    "write":  "Write 150-180 words: <prompt>. Use four target expressions, one concession and one conditional."
  },

  "i18n": { "de": { ...see §5... }, "es": { ... } },

  "teacher": {
    "route":   "How the lesson runs, and roughly how long each stage takes.",
    "support": "What to do with a weaker group; what to demand from a stronger one.",
    "key":     "The answer key, in order."
  }
}
```

## 2. The slide types, and what each one takes

Use only these. They map one-to-one onto our builders, which is what makes the
rebuild quick. **Every slide takes an optional `"art"`** naming a key from the
art block.

| `type` | what it is | fields |
|---|---|---|
| `teach` | 2–3 cards that teach before anything is tested | `eyebrow`, `title`, `cards[]` |
| `mc` | one multiple-choice question | `eyebrow`, `title`, `stem`, `options[]`, `correct`, `why`, `explains[]` |
| `gap` | sentences with blanks, filled from a shared bank | `eyebrow`, `title`, `hint`, `bank[]`, `rows[]` |
| `match` | terms to meanings | `eyebrow`, `title`, `hint`, `pairs[]`, `why` |
| `sort` | items into 2–3 labelled bins | `eyebrow`, `title`, `hint`, `bins[]`, `items[]`, `why` |
| `order` | words dragged into a sentence | `eyebrow`, `title`, `hint`, `items[]`, `why` |
| `read` | a reading passage, 2–3 paragraphs | `eyebrow`, `title`, `paras[]`, `ask` |
| `roleplay` | two role cards and a phrase bank | `eyebrow`, `title`, `roles[]`, `phrases[]`, `model[]` |
| `discuss` | a prompt to talk about, one at a time | `eyebrow`, `title`, `hint`, `prompts[]` |

A `teach` card is `{ "head": "...", "body": "...", "note": "..." }`. A `gap`
row is `{ "text": "She shifted ______ a lower gear.", "answers": ["into"],
"why": "..." }` — six underscores marks a blank. A `roleplay` role is
`{ "name": "A · The rider", "brief": "...", "task": "..." }`.

**Teach before you test.** Every word a question asks about must have appeared
on a `teach` card first. A deck that opens with six vocabulary questions is
testing what the learner walked in with.

## 3. The slide budget — this is a wall, not a target

The canvas is **1280 × 720 with 64px padding**, and nothing scrolls, ever. A
slide that overflows is broken, not scrollable.

| element | aim | max |
|---|---|---|
| slide `title` | 3–5 words | **7 words** |
| `eyebrow` | 2–3 words | **4 words** |
| teach card `head` | 2–4 words | **6 words** |
| teach card `body` | 18 words | **30 words** |
| teach card `note` | 8 words | **14 words** |
| question `stem` | 12 words | **22 words** |
| each option | 30 characters | **65 characters** |
| `why` / `explains` | 14 words | **26 words** |
| `read` paragraph | 45 words | **65 words** |
| whole `read` slide | 110 words | **150 words** |
| cover `subtitle` | 18 words | **28 words** |

Practical capacity is one heading plus about **55 words**. When a stage does
not fit, **split it across two slides — never shrink the type.** More slides
cost the learner a click. Less type costs them the lesson.

## 4. The three question gates

These are checked mechanically and the build **fails** on them, so they are
worth getting right first time.

1. **The correct option must never be conspicuously the longest.** Fix it by
   lengthening the distractors, never by shortening the key. This is the
   single most common defect in what we receive: one deck arrived with a
   66-character key against distractors of 45 and 47 — a free point for a
   learner who never read the passage. Aim for three options within a few
   characters of each other.

2. **Deal the key across the slots.** The options render in the order you
   write them. Spread the correct answer roughly evenly across first, second
   and third; no slot may hold more than 40% of the keys.

3. **A word bank must not list its answers in gap order.** Alphabetise it.
   A bank in gap order is an answer key.

**And one structural rule that no rewrite can fix.** If a question's options
are a *closed set reused across several questions* — three idioms asked three
times, four modals asked six times — then on the item whose key is the longest
member of that set, gate 1 is unsatisfiable, because the options *are* the
answer set. **Write those as a `gap` with a shared alphabetised bank instead.**
It tests the same thing and cannot leak the answer by length.

Alongside every question, write `explains[]` — one line per option saying why
*that* option is wrong. A learner who picks a distractor should be told why
their answer failed, not why the key succeeded. Use `null` for the key.

## 5. German and Spanish are not optional

**Every lesson ships English, German and Spanish as a minimum.** A language
that is incomplete stays out of the menu entirely, so a partial German is
worse than none.

**Translate the chrome, never the target language.** Titles, eyebrows, hints,
role briefs, discussion prompts, the activation briefs: those translate.
Question stems, options, gap sentences, collocations, reading passages and the
explanations of English usage stay **in English** — they are the thing under
test, and translating them removes the test.

Supply them as a flat map per language, keyed the same as the English:

```jsonc
"i18n": {
  "de": { "coverTitle": "Jenseits des Lenkers", "ridersTitle": "...", ... },
  "es": { "coverTitle": "Más allá del manillar", ... }
}
```

Where a card teaches an English term, the German and Spanish `head` may gloss
it once in brackets — `"Cadence (Trittfrequenz)"` — and then leave the example
sentence in English. That bracket is the bilingual glossary a vocabulary
lesson wants.

## 6. Pictures

- **16:9, at least 1600px wide, WebP, under 300 KB each.** One picture per
  slide that needs one; not every slide needs one.
- A **hero**: landscape, with quiet space somewhere for the logo and title. It
  drives the whole colour palette, so it decides how the deck looks. Send the
  best one.
- **Portraits are the exception** and must be flagged: if a picture is meant
  to sit inline in a column rather than behind a slide, name it
  `portrait-<something>` so it is not treated as a background.
- **One style across the whole set**, on one palette, written down in a line
  or two. A set that drifts between plate 3 and plate 11 has to be reshot.
- Flat vector and illustration styles are welcome, but know that **large
  near-white areas force us to darken every text plate on the deck.** If the
  art can be a little less bright, the type gets easier to read for free.

## 7. Two things that will be removed, so do not spend effort on them

- **No third-party trademarks.** Do not brand a diagram, a product or a vehicle
  with a real company's name or logo, however incidental. It is a commercial
  site; it gets stripped.
- **No credits to other lesson sites.** Do not cite, link or "draw on" another
  English-teaching site's pages in the teacher notes or anywhere else. Write
  original tasks.

Also skip: a download button, a save-my-notes button, a print view, a teacher
overlay, a scoring readout, a language menu, a progress bar. Every one of those
already exists in the template and yours will be deleted.

## 8. Before you hand it over

- Every string a learner reads is reachable from `window.DECK_DATA`.
- Every `art` key on a slide exists in the art block, and every key in the art
  block is used by a slide.
- No question's key is the longest option; the keys are spread across slots.
- Any closed-set item is a `gap`, not an `mc`.
- Every word tested appeared on a `teach` card first.
- German and Spanish are complete, and neither touches the English under test.
- No slide exceeds the §3 budget.
- No trademark, no competitor credit.

---

## For the session doing the rebuild

With a file in this shape the job is: run `prep-artwork.py` over the art block
(the keys are already the filenames), derive the palette from `hero`, write
`build_<name>.py` mapping §2 slide types onto `deck.py`'s builders, lift `i18n`
into `i18n_<name>.py`, then the usual `check-lesson.js` → catalogue row →
`library.html` line → `build_hubs.py` → `seo.py`.

What still cannot be outsourced, and should not be attempted upstream:
anything measured against the real template. Slide overflow, plate contrast
and the palette are all properties of our CSS and the supplied hero, and they
are only knowable after the first build. Budget for a measure-and-fix pass
whatever the export looks like.
