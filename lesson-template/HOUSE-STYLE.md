# Forbes English — Lesson House Style

**This document is binding. Follow it to the letter.**

Every lesson on forbesenglish.com is built to one standard. If a request is
"add an image to lesson X", "revamp lesson Y", or "build a new lesson on Z",
this document defines what the finished thing must look like. There is no
"just do the one thing that was asked" — a lesson you touch is a lesson you
bring up to this standard.

Working template: **`lesson-template/lesson-template.html`**
Palette tool: **`lesson-template/extract-palette.py`**
Pre-ship checker: **`lesson-template/check-lesson.js`** — must exit clean.

---

## 0. The six rules

1. **16:9 slides, never a scrolling page.** A lesson is a deck. One idea per
   screen. The learner reads what is on the page and clicks to the next one.
2. **The cover is a landscape hero image** with the stacked Forbes/ENGLISH
   logo and the lesson title over it.
3. **That same hero image becomes the background pattern** on every following
   slide, at reduced opacity, with the content legible on top of it.
4. **The colour palette is derived from the hero image**, mechanically, using
   the supplied script. Never hand-picked.
5. **Every lesson ships with a language switcher**, and every language it
   offers is complete. Unfinished languages stay out of the menu entirely.
6. **Every lesson ends with an activation stage** — a speaking task and a
   writing task, so the learner *produces* the language instead of only
   recognising it.

If you cannot satisfy all six, stop and say so. Do not ship a partial version
and describe it as done.

---

## 1. Start from the template. Do not build from scratch.

```bash
cp lesson-template/lesson-template.html <lesson-name>.html
mkdir -p <lesson-name>/            # hero + any lesson images live here
```

The template is a working, tested lesson: cover, teaching slide, multiple
choice, gap-fill, results, keyboard navigation, scoring, language switching
and PDF export all function on first open. You are filling it in, not
reinventing it.

Only two regions of the file are yours to edit. They are marked
`REPLACE 1 of 2` (hero + palette) and `REPLACE 2 of 2` (the slides).
**Do not restructure the engine below them.** If you think the engine needs a
change, that change belongs in the template so every lesson inherits it — say
so rather than forking the behaviour into one file.

---

## 2. The logo

Forbes sits **stacked on top of** ENGLISH. Both lines are set to the **same
optical width** — this is the whole point, and the most common thing to get
wrong.

The exact lockup is in `lesson-template/forbes-logo.svgfrag` and is already
embedded in the template. Copy it verbatim. Its geometry is:

- `viewBox="0 0 200 78"`
- Forbes glyph: `transform="translate(-42.74,-30.22) scale(0.099477)"`
- ENGLISH: `x="100" y="72.6"`, `font-size="20.8"`, `letter-spacing="8"`,
  `font-weight="600"`, DM Sans

Both lines then render 148.4 units wide, left edge at x=25.8. Do not nudge
these numbers. If the two lines are different widths, the lockup is wrong.

**Colour:** the Forbes mark takes `var(--accent)`; ENGLISH takes
`var(--text)`. Both come from the palette, so the logo belongs to each
lesson's own scheme.

**The contrasting option.** The palette also yields `--contrast`, a colour
rotated roughly 150° from the accent and pushed until it is legible. On a
pink-dominant lesson that lands on lime; on coral it lands on spring green.
Running the mark in it makes the logo a deliberate counterpoint rather than
another tone in the wash. It is a one-line switch:

```css
--logo-mark: var(--contrast);
```

Use it when the accent is close to the hero's dominant colour and the mark
is disappearing into the artwork, or simply when the lesson wants more snap.
Leave it off when the accent already stands clear. If the accent is so light
or so loud that the mark stops reading, `var(--text)` for both is the safe
fallback.

**The font must actually be loaded before the wordmark shows.** DM Sans at
`letter-spacing: 8` is what makes ENGLISH exactly as wide as Forbes; in a
fallback face the balance collapses. The template handles this — the wordmark
is hidden until `document.fonts.ready` resolves (with a 1.5s failsafe). Keep
that mechanism.

Size: `232px` on the cover, `152px` anywhere else.

---

## 3. Hero image

- **Landscape.** 16:9 or wider. Minimum 1400px wide.
- Lives at `<lesson-name>/hero.jpg`. JPEG, quality 82–88, optimised.
- Convert anything supplied as PNG:
  ```python
  from PIL import Image
  Image.open(src).convert('RGB').save(dst, 'JPEG', quality=85, optimize=True)
  ```
- Set it once, in CSS: `--hero: url('<lesson-name>/hero.jpg');`
  That single line drives the cover, the background on every slide, and the
  PDF export. There is no second place to update.

The cover carries a built-in centre scrim so that title text stays legible
over a light, dark or busy image. Do not remove it — it is what makes an
arbitrary supplied image safe to drop in.

---

## 4. Palette — derived, not invented

```bash
python3 lesson-template/extract-palette.py <lesson-name>/hero.jpg
```

Paste the emitted `:root` block over the palette block in the template. That
is the whole procedure. The script pulls the canvas, surfaces, accent and
secondary out of the image itself, keeps a whisper of the image's hue in the
darks so the page reads as *that picture, darkened* rather than generic dark
mode, and prints a WCAG contrast report.

Use `--light` for a paper/light theme when the hero is bright and airy.

**Every body-text row in the contrast report must read PASS.** If one fails,
adjust `--text` until it passes. Do not ship a failing palette.

Ten variables come out, and they mean:

| Variable | Use |
|---|---|
| `--void` | page canvas, letterbox area |
| `--surface` / `--surface2` | cards, option buttons |
| `--border` | hairlines, card and option borders |
| `--text` / `--text-dim` | body copy, secondary copy |
| `--accent` | logo mark, progress fill, primary buttons |
| `--accent-bright` | headings emphasis, eyebrows, highlighted words |
| `--accent-dim` | pressed/!hover states |
| `--secondary` | second data colour when you need one |
| `--contrast` | deliberate counterpoint — logo mark, a highlight that must not blend |

Never introduce a hex value into a lesson body. If you need a colour that is
not on this list, you are solving the wrong problem.

---

## 5. Background pattern and legibility

The hero repeats behind every non-cover slide at `--bg-opacity: 0.34`,
desaturated to `saturate(0.75)`, under a vertical wash.

- **Start at 0.34.** This has been set too faint repeatedly in the past and
  corrected each time. It is a floor, not a starting guess to tune downward.
- Range 0.30–0.40. Go lower only if a specific hero is so busy that text
  suffers, and say that you did.
- **All reading content sits inside `.card`.** The card is translucent
  (`82%`) so the picture still shows through, plus a 3px backdrop blur that
  keeps text crisp over detailed artwork. Text placed directly on the
  background with no card is the single most common legibility failure —
  don't do it.

---

## 5a. The tense colour system

The site already publishes a colour per tense: the Sherpa Tensing route map
assigns thirteen, and each camp page is themed from its own. A learner who has
used the route map has started associating brown with past simple and navy
with present simple.

**When a lesson teaches, contrasts or labels specific tenses, use these
colours rather than inventing new ones.** They are in
`lesson-template/tense-palette.css` — copy in the lines you need.

| Tense | | Tense | |
|---|---|---|---|
| Present continuous | `#C2185B` | Future simple | `#E8632A` |
| Present simple | `#16345C` | Present perfect continuous | `#2FA6A1` |
| Past simple | `#B08968` | Future continuous | `#F0A500` |
| Present perfect | `#0F6E56` | Past perfect | `#6E0B24` |
| Going to | `#639922` | Past perfect continuous | `#4B1A7A` |
| Past continuous | `#FFD400` | Future perfect | `#454545` |
| | | Future perfect continuous | `#B0B0B0` |

Two cautions. Several are dark — maroon, navy, dark grey — and will not read
on a dark canvas; lighten with `color-mix(in srgb, var(--t-past-perfect) 55%,
white)` to keep the hue and raise the lightness, then check contrast. And
never put more than three tense colours on one slide: past that it stops
being a code and becomes decoration.

When a lesson is not about tenses, ignore this entirely and use the
hero-derived palette.

---

## 6. Slide budget — the hard constraint

The canvas is exactly **1280 × 720** with 64px padding. Roughly **1150 × 590**
of usable space. It is scaled to fit the viewport by the engine; you author
against the fixed size.

**Nothing scrolls. Ever.** If content does not fit:

> **Split it across more slides. Never shrink the type.**

That is the rule, and it is not negotiable. A grammar explanation that wants
eight sentences becomes three slides of three. A reading passage with eight
gaps becomes four slides of two. Learners get more clicks; they never get a
6-point font or a hidden overflow.

Type scale — do not deviate:

| Element | Size |
|---|---|
| Cover title | 62px Playfair Display 900 |
| Slide title | 38px Playfair Display 700 |
| Question stem | 25px DM Sans |
| Body / options | 19–20px DM Sans |
| Eyebrow / chips | 11.5–12px DM Mono, uppercase, tracked |

Practical capacity per slide: one heading plus **~55 words**, or one question
stem plus four options, or two side-by-side cards of ~40 words each. When in
doubt, put less on the slide.

Fonts are Playfair Display (display), DM Sans (UI/body), DM Mono (labels).
These are the site's fonts across 216 lessons. Do not introduce others.

---

## 7. Authoring slides

Each screen is one `<section class="slide" data-type="...">`. Types:
`cover`, `teach`, `mc`, `gap`, `results`.

**Multiple choice.** Mark the right answer with `data-correct`. Order is
shuffled at runtime and A/B/C/D labels are applied after shuffling, so never
write "the answer is C".

> **The correct option must never be the longest one.** This is a hard gate,
> not a preference, and `check-lesson.js` enforces it.

A correct answer written longer or more precisely than its distractors lets a
learner score without knowing any of the language being taught. It is the most
common quality defect found on this site — the C1 negotiation lesson had it in
10 of 12 items, several at nearly twice the length of every distractor.

It is especially easy to introduce when the *teaching point itself* is that
formal register is more elaborate. That is exactly when it does the most
damage: the learner learns "pick the long one", not the register.

**Fix it by lengthening the distractors, never by shortening the key.** A good
distractor is the same length as the answer and wrong for a reason the lesson
has taught — wrong register, imprecise term, a commitment the speaker did not
intend. Three plausible same-length wrong answers is the work; it is also the
part that makes the question worth asking.

**Gap fill.** `data-answer="was postponed|got postponed"` — pipe-separated
alternatives, matched case-insensitively and whitespace-tolerantly.
Several gaps can share a slide: wrap each in `<div class="card gap-row">` with
its own `.feedback`. Each gap is then scored and explained individually — the
engine counts gaps, not slides, so a 2-gap slide is worth 2 points. List
every genuinely acceptable answer; a learner who is right and marked wrong is
worse than one who is wrong and marked right.

**Explanations.** Put the "why" in `data-explain` on the `.feedback` element.
It shows after answering, right or wrong. Every question gets one. A quiz
that only says "Not quite" teaches nothing.

**Recommended shape for a lesson:** cover → 1–3 teaching slides → 6–12
question slides → results. Twelve to eighteen slides total is a comfortable
class; beyond about twenty-four, split into Part I and Part II.

---

## 8. Translation

Structure is `LANGS` / `RTL_LANGS` / `UI_I18N` / `t()`, already wired.

**A language appears in the menu only if it is actually finished.** The
switcher is built from `UI_I18N` at runtime and skips any language whose key
count is short of English, so an empty or half-done scaffold is simply not
offered. Never ship a dropdown with names in it that fall back to English when
selected — a dead option is worse than no option.

That leaves two honest states, and the checker enforces them:

- **Complete** — every key English defines. It shows in the menu.
- **Empty** — `{}`. It stays in the code as a placeholder for a later pass and
  does not show.

**Partial is a failure**, not a work-in-progress: it puts a language in the
menu that silently reverts to English halfway down the screen.

English and German are the minimum. Beyond that, finish what you start: the
nine-language set is Spanish, French, Italian, Portuguese, Russian, Arabic,
Chinese and Japanese alongside German, and `forbes-c1-negotiation.html` carries
all nine as the worked reference.

**Scope boundary — this holds and does not change:** translate the app's own
chrome. **Do not translate the English being taught** — question stems,
options, gap sentences, example sentences and word banks stay in English.
Translating the target language defeats the lesson. Note that this applies to
the activation stage too: the task instructions translate, the target-language
chips do not.

Arabic is in `RTL_LANGS`; the engine sets `dir="rtl"` and the layout mirrors.
Check it when you touch layout.

Mark translatable chrome with `data-i18n="key"` and add the key to `en` and
`de`. Anything without a `data-i18n` attribute will never translate — that is
the usual cause of a stubbornly English button.

---

## 9. PDF and PowerPoint export

Already built and verified. `Ctrl/Cmd-P` → Save as PDF → **Landscape,
margins None, Background graphics ON** produces one 1280×720 page per slide,
backgrounds intact, ready to place into PowerPoint at 16:9.

The print stylesheet gives each slide its own background layer rather than
relying on the on-screen one, and hides the navigation chrome. If you add a
new slide type, confirm it still exports — render the PDF and look at it.

---

## 10. Revamping an existing lesson

Old lessons are long scrolling pages. **Converting one means rebuilding it as
a 16:9 deck** — not bolting a hero onto a scrolling page.

1. **Read the existing lesson and inventory it**: every explanation, question,
   answer, and explanation string. This content is the asset; the markup is
   not. Nothing pedagogical may be silently dropped in conversion.
2. **Identify the hero.** Use the image supplied with the request. If the
   lesson already has a good landscape image, use that. If neither exists,
   stop and ask — do not invent a lesson's visual identity unprompted.
3. `cp lesson-template/lesson-template.html` over a working copy and set
   `--hero`.
4. **Derive the palette from that hero** and paste it in. The revamped lesson
   takes its colours from its cover image, not from whatever palette the old
   file happened to use. This is the point of the exercise: the lesson should
   look like it belongs to its own artwork.
5. **Re-flow the content into slides** at the budget in §6. Long explanations
   split across slides. Stacked question lists become one question per slide.
6. **Port German** if the old file had any; otherwise write it fresh.
7. Run the QA checklist in §12.
8. Keep the **same filename** so the live URL does not change.

Where the old lesson has bespoke hand-built SVG diagrams or illustrations,
keep them — drop them into a `teach` slide. They are usually the best thing in
the file. Scale them to fit the 1280×720 canvas rather than cropping.

---

## 10b. The activation stage — required

A lesson that ends on a score has tested recognition and stopped. Recognising
the right register in four options is not the same skill as producing it in
front of a client. **Every lesson ends with an `activate` slide**, after the
results, and it is the last thing the learner sees.

It carries **two tracks, both live at once**:

- **🗣 Discussion** — three prompts for pair or small-group work. Write
  *situations*, not comprehension questions: "Your client wants 12% off. Push
  back without closing the door." A prompt the learner can answer in one word
  is not a speaking task.
- **✍️ Writing** — a brief with a word count and a live text area. The word
  counter runs as they type, a Copy button lifts the text out, and the content
  is mirrored into the PDF export (a textarea's value does not print).

Run either. Run both. They are not alternatives presented as a choice — the
slide shows both because a class often does one in the room and sets the other
as homework.

Above the two tracks sits a **target-language strip**: the phrases from this
lesson the learner is expected to actually use, as chips, with "use at least
three". This is what connects production back to the material. Without it the
task is generic and the lesson's own language goes unused.

Writing the tasks:

- The speaking prompts should require the target language, not merely permit
  it. If a learner can complete the task in B1 English, the task is wrong.
- Give the writing brief a real audience and purpose — a notice to a client, a
  reply to a complaint — not "write about negotiation".
- 150–250 words is the right size for a class. State it.
- Keep the whole slide inside the canvas like any other. If both tasks will
  not fit, shorten the prompts, not the type.

---

## 10a. Rollout status — which lessons are already converted

The repo holds **216 lesson files**. Converting them is in progress, not done.
Keep this list current when you convert one, so the next session knows where
things stand.

**Converted to the 16:9 deck standard:**

- `forbes-c1-negotiation.html` — 22 slides (first conversion, 2026-08-11)

**Touched but only partly modernised** — these got a prominent hero and the
persistent background treatment while the old scrolling format was still the
standard. They are *not* yet 16:9 decks and should be converted when revisited:

- `forbes-dnd-rpg.html`
- `forbes-english-dinosaur-minecraft-part2.html`

**Everything else** is still an old-format scrolling lesson.

Do not bulk-convert without being asked. Conversion is a rebuild per lesson
(§10), and the content decisions inside it deserve a human look.

---

## 11. Publishing

1. **Thumbnail.** Add the hero to the `LESSON_IMAGES` map in `library.html`:
   `"<lesson-name>.html": "<lesson-name>/hero.jpg",`
   A lesson with no entry falls back to a styled placeholder card. That
   fallback is intentional for un-illustrated lessons and is **not** a bug to
   go fix in bulk — but any lesson you build or revamp gets a real thumbnail.
2. **Card title lives in Supabase, not the HTML.** The title shown on
   `library.html` comes from the `lessons` table in project
   `tusioporxpjtegjlqkkb`, via `sbGetLessons()` in `sb-client.js` — *not* from
   the `<title>` tag. If a title looks wrong on the library page, grepping
   HTML will mislead you; query the table. Titles carry no "Forbes English —"
   prefix.
3. **Push.** Two commits when a new folder is involved, because the GitHub web
   upload UI targets one directory at a time: images to
   `/upload/main/<lesson-name>`, then the HTML files to `/upload/main`.
   Sync after: `git fetch origin && git reset --hard origin/main`.

---

## 12. QA — run the checker, then check by eye

**First, run this. It is not optional.**

```bash
node lesson-template/check-lesson.js <lesson>.html
```

It mechanically verifies the six things that have actually gone wrong here:
every slide fits the canvas and nothing scrolls; no multiple-choice key is the
longest option; every scored question has an explanation; German covers every
English key and every `data-i18n` resolves; Forbes and ENGLISH render to the
same width; and there are no JS errors. **A lesson does not ship until it exits
clean.**

Two notes on why it exists. A checker that measures the wrong box passes
everything and teaches you nothing — the first version of this tool reported
all 22 slides fitting because it measured a flex parent that silently absorbs
overflow. And a written rule that nobody measures gets skipped; a failing exit
code does not.

Then open the file in a browser and check the things a script cannot judge:

- [ ] Cover title and logo are legible against the hero
- [ ] Background pattern is clearly visible on interior slides, not a faint ghost
- [ ] All reading content sits in a `.card`
- [ ] Palette contrast report: every body-text row PASS
- [ ] Arrow keys, on-screen arrows, and the Begin button all navigate
- [ ] Every question scores and gives feedback when answered
- [ ] Switch to German: nothing is still in English on screen
- [ ] Switch to Arabic: layout mirrors
- [ ] Print preview: one 16:9 page per slide, backgrounds present
- [ ] `library.html` thumbnail added
- [ ] The lesson still teaches what the original taught — nothing dropped

Verify by actually loading and screenshotting the page. Do not report a
lesson as finished on the strength of having written the markup.

---

## 13. Traps that have caught us before

- **`\uXXXX` escapes do not work in HTML text.** They only resolve inside JS
  string literals. In markup use the real character or an entity
  (`&middot;`, `&mdash;`). Grep `\\u00` after a copy-paste-heavy pass.
- **No spaces in filenames.** A space becomes `%20` in the live URL and looks
  broken. Use hyphens. If a URL "doesn't work", check the filename first.
- **The library title is in Supabase.** See §11.2.
- **Adjacent-sibling margins break grid columns.** `.card + .card` gets
  overridden inside `.cols` for exactly this reason. If two side-by-side cards
  do not share a top edge, that is what you are looking at.
- **Don't make a shared `--card`/`--surface` variable translucent without
  grepping every use of it first.** On question-heavy pages these variables
  often also drive option hover/selected/correct/wrong states, and turning
  them translucent quietly wrecks the contrast of interactive states.
- **"Add this image" means "bring this lesson up to house style."** Dropping
  an image into a box and leaving the rest is not the job. This has been
  raised directly and more than once.

---

## 14. When to stop and ask

Ask before proceeding if:

- No hero image exists and none was supplied.
- The content genuinely cannot be split into readable slides.
- A revamp would drop pedagogical content to fit the format.
- The request conflicts with this document.

Otherwise, apply the standard and report what you did.
