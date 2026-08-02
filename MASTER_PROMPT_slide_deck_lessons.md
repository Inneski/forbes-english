# Master prompt — Forbes English slide-deck lesson format

Use this prompt (fill in the bracketed parts) whenever creating or rebuilding a Forbes English interactive lesson. It locks in the no-scroll, click-to-advance format.

---

Build a self-contained interactive HTML English lesson for Forbes English on the topic of **[TOPIC]**, level **[CEFR LEVEL]**, with **[LANGUAGE SUPPORT, e.g. "German toggle" or "none"]**.

**Structural requirements — these are non-negotiable:**

0. **Whenever a new image is supplied for an existing lesson, this is a full reboot, not a decoration pass.** Remove the old graphics entirely — hand-drawn SVG illustrations, emoji heroes, decorative icon sets, everything the image is replacing. Rebuild the CSS palette (ink/background/accent colours) by eyeballing the actual dominant tones in the new image — don't leave a mismatched legacy colour scheme sitting next to a photo that doesn't relate to it. And confirm the lesson ends with a genuinely free-response speaking or writing activation round (open prompts, no single correct answer, a place for the learner to produce language rather than just select it) — add one if the lesson doesn't already have it. This is the default; it doesn't need to be asked for separately each time.

1. **No scrolling, ever.** The page is a slide deck: `html, body { height:100%; overflow:hidden; margin:0; }`. Every screen — intro, each exercise, results — is its own full-viewport slide (`.lesson-page { position:fixed; inset:0; bottom:60px; overflow-y:auto; display:none; } .lesson-page.active { display:flex; flex-direction:column; justify-content:center; }`). If a slide's content is too long to fit, split it into two slides — never let a slide scroll internally except as a rare last resort, and never let the outer page scroll.

2. **Fixed bottom nav bar** on every slide: Back button, page-dot progress indicator (one dot per slide, current dot highlighted), Next button, and the language toggle if applicable. This bar is `position:fixed; bottom:0;` and is identical across all slides.

3. **Image on one side, content on the other — not stacked.** On viewports ≥900px: a `.layout-shell { display:flex; }` with a sticky `.image-panel` (35–45% width, `position:sticky; top:[nav height]; height:calc(100vh - [nav height])`) holding a full-bleed image (`object-fit:cover`), and a `.content-col` (remaining width, its own `overflow-y:auto` if a slide genuinely needs it) holding the exercise. Below 900px: stack image-on-top (fixed height, e.g. 35–42vh), content below, same slide-based navigation.

4. **A different image per major section**, not one banner reused everywhere. Each slide/section (warm-up, vocab, reading, grammar, speaking, results) gets its own image from the same visual set, swapped via JS as the learner navigates (`document.getElementById('stepImg').src = ...`), with a quick opacity fade on change.

5. **Palette derived from the actual images**, not a generic template. Pick 5–6 CSS custom properties (ink/background/accent/accent-light) by eyeballing the dominant colours in the hero image — don't default to a stock navy/gold or green/gold scheme unless the images actually are that colour.

6. **JS-driven navigation**, not anchor links: `let current = 0; function goPage(delta) { current += delta; render(); }`, wired to Back/Next buttons and dot clicks. `renderStep()` (or equivalent) re-renders the current slide's content into a single mount element — don't pre-render all slides into the DOM at once if the lesson has randomised/shuffled question order.

7. **If language support is requested**: a single toggle button in the nav bar (not per-section), driving a `body.show-[lang]` class. Every translatable string gets a co-located `<span class="[lang]-block">` (block-level content) or `<span class="[lang]-line">` (inline), default `display:none`, shown via `body.show-[lang] .{lang}-block { display:block }`. Translate **everything** — titles, instructions, passage text, question stems or at minimum full explanations — not just the vocab glossary. Partial coverage is the single most common failure mode; check every render function before calling it done.

8. **Score/progress tracking**: sticky or fixed score chip showing correct/total, progress bar filling as the learner advances, gated Next button (disabled until the current question is answered).

9. **Verification before delivery**: run a syntax check (`node --check` equivalent) and a full click-through simulation of every slide/question path. Confirm zero page-level scrolling at a standard viewport (1280×800) and that the split layout doesn't overlap or clip on mobile widths.

**Content to include:** [warm-up/activation, vocabulary section, reading passage + comprehension, grammar focus, speaking/discussion round, results screen — adjust as needed for the topic]

**Images:** [describe the image set — how many, what they depict, where each is used]

---

## Why this exists

Earlier lessons on this site were single long scrolling pages with a banner image stitched on top — image and content fought each other, and multi-language support was frequently bolted on to only one section (usually the feedback/explanation text) rather than applied throughout. This prompt exists to make every new or rebuilt lesson default to: full-screen slides, image and content side-by-side, and language support that's actually complete if requested at all.
