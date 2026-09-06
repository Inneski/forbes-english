# Brief for ChatGPT — build an RPG export that lands close to house style

**How to use this file.** Copy everything below the line into ChatGPT,
followed by the lesson brief (grammar point, level, the story world, the
number of questions). Ask it for the one HTML file. Then attach that file
to a Claude cloud task, with `Inneski/forbes-english` added as a source,
and send: *"Rebuild this RPG export as a Block Camp RPG, to the standard in
lesson-template/build/rpg/README.md."* Claude finishes it — fonts, glowing
objects, sound, hub card, library, catalogue — and the closer ChatGPT gets
to this brief, the less there is to finish.

What ChatGPT is *not* asked to do: the Monocraft font, the glass panel, the
pop-out animation, the sound, the hub and library. Those come from the
engine on our side and are the same for every game. ChatGPT's job is the
**content** in the **right shape**: the story, the questions, the
explanations, the briefing, the pictures, the translations, and a
suggested object on every picture.

---

## The prompt

You are writing a single-player grammar adventure game for English
learners. Deliver **one self-contained HTML file** that plays in a browser
with no external files, and that embeds all of its game data in exactly the
structure described below. The styling of your file does not matter: it
will be rebuilt on a fixed template. The **data and pictures** are what
will be kept, so get those exactly right.

### 1. The game

- One grammar point per game, named in the brief (e.g. Past Continuous,
  Present Perfect, Modals of Obligation). Every question tests that point
  and nothing else.
- A story world from the brief, told in short chapters. Blocky voxel
  Minecraft-style art, one picture per scene.
- 15–25 question scenes, 2–3 route-choice scenes, 2–3 endings.
- Each question: a one-line story beat, a one-line visual clue that
  contains the evidence for the answer, a question, and **three** options:
  one correct, two wrong. Wrong options must be *real learner errors* for
  this grammar point (wrong auxiliary, wrong tense, missing -ing), never
  nonsense.
- **Every answer gets an explanation** of one sentence, in plain
  English, that says why the correct form is correct (e.g. "*Was blowing*:
  an action in progress at a past moment. Past Continuous = was/were +
  -ing."). This is the lesson; the story is the wrapper.
- A **rules briefing** before the first question: two to five cards, each
  with a bold heading and one example sentence, and one note. This is the
  grammar reference the player can consult. Keep it A2-readable.
- Scoring: fixed points per correct answer, a number of "tiles" or
  "relics" collected at key questions, and a number of chances (lives) —
  or, if the brief says so, "repair until correct" with no lives. State
  the rule on the cover in three short chips ("+5 CORRECT", "4 ROAD
  TILES", "3 CHANCES").
- Route choices are real choices: two or three branches that rejoin. An
  ending threshold decides between a success ending and a fallback ending.

### 2. Language level and style

- The level is on the brief (A1–A2, B1, …). Sentences short. One idea per
  sentence. No idioms at A1–A2.
- Titles in CAPITALS, short (max five words). Chapter labels like
  "CHAPTER 1 · KANSAS".
- The player is addressed as "you"; the hero is named.
- Never refer to a previous version of anything.

### 3. Pictures

- One picture per scene, plus a cover. WebP, **1536 × 1024** (3:2),
  each **under 200 KB**. Blocky voxel style, consistent palette across the
  game.
- **Every picture has exactly one clear object that the clue is about** —
  the tornado, the lantern, the axe — placed on **one side** of the frame
  with the **other side visually quiet**. The quiet side is where the text
  panel goes; the object is what the player clicks. Do not centre the
  object; do not fill both sides.
- Name the files `01_cover.webp`, `02_q1_<name>.webp`, `03_q2_<name>.webp`
  … in play order. Endings may reuse the cover.
- Inline every picture as a base64 data URI in the `images` map.

### 4. Translations

Every learner-facing string gets a `local` block with the same text in
these nine languages, keyed `es`, `de`, `fr`, `it`, `pt`, `ru`, `ar`, `zh`,
`ja`: titles, chapter labels, story, clue, prompt, explanations, briefing
cards and note, route names and notes, endings, cover text and chips.
**Do not translate the answer options** — they are the English being
taught. Keep grammar formulas ("was/were + -ing") in English inside a
translation.

### 5. The data structure — exact

Put one `<script>` at the end of the body containing exactly:

```html
<script>
window.<NAME>_GAME_DATA = { ...JSON... };
</script>
```

where `<NAME>` is the game in capitals (`FRANKENSTEIN`) and the value is
**valid JSON** (double quotes, no trailing commas, no comments, no
functions). Structure:

```json
{
  "meta": {
    "title": "THE LOST YELLOW ROAD",
    "grammar": "Past Continuous",
    "world": "Voxel Oz",
    "level": "A1-A2",
    "accent": "#F1D779",
    "scoring": { "points": 5, "tiles": 4, "chances": 3, "max": 75, "pass": 65 }
  },
  "cover": {
    "image": "01_cover.webp",
    "eyebrow": "PAST CONTINUOUS · VOXEL OZ RPG",
    "title": "THE LOST YELLOW ROAD",
    "lead": "The Witch has stolen four Yellow Road tiles. …",
    "rules": ["+5 CORRECT", "4 ROAD TILES", "3 CHANCES"],
    "start": "FOLLOW THE YELLOW ROAD",
    "small": "Single player · A1–A2 · three branching routes",
    "local": { "es": { "eyebrow": "…", "title": "…", "lead": "…", "rules": ["…","…","…"], "start": "…", "small": "…" }, "de": { … }, "fr": { … }, "it": { … }, "pt": { … }, "ru": { … }, "ar": { … }, "zh": { … }, "ja": { … } }
  },
  "briefing": {
    "image": "02_q1_tornado.webp",
    "title": "HOW THE PAST CONTINUOUS WORKS",
    "cards": [
      { "head": "was / were + -ing", "text": "The wind was blowing." },
      { "head": "Two actions at once", "text": "While Toto was barking, the door was shaking." },
      { "head": "Questions", "text": "What was the wind doing?" }
    ],
    "note": "Use it for an action in progress at a moment in the past.",
    "button": "START THE ADVENTURE",
    "local": { "es": { "title": "…", "cards": [ { "head": "…", "text": "…" }, … ], "note": "…", "button": "…" }, … }
  },
  "first": "storm",
  "scenes": {
    "storm": {
      "image": "02_q1_tornado.webp",
      "hotspot": { "object": "the tornado", "x": 72, "y": 40, "w": 26, "h": 45 },
      "act": "CHAPTER 1 · KANSAS",
      "title": "THE TORNADO ARRIVED",
      "story": "Dorothy reached the yard as the storm began.",
      "clue": "Leaves and fence rails were already moving through the air.",
      "prompt": "What was the wind doing?",
      "answers": [
        { "text": "It blew hard." },
        { "text": "It was blowing hard.", "correct": true },
        { "text": "It were blowing hard." }
      ],
      "explanation": "An action in progress at a past moment: was + blowing. 'Blew' is a finished action; 'were' does not go with 'it'.",
      "points": 5,
      "relic": false,
      "correctNext": "cellar",
      "wrongNext": "cellar",
      "local": { "es": { "act": "…", "title": "…", "story": "…", "clue": "…", "prompt": "…", "explanation": "…" }, … }
    },
    "crossroads": {
      "image": "06_choice1_crossroads.webp",
      "hotspot": { "object": "the signpost", "x": 50, "y": 45, "w": 14, "h": 40 },
      "act": "ROUTE CHOICE 1",
      "title": "WHERE DID THE ROAD BEGIN?",
      "story": "The first tile glows. Choose where Dorothy searched next.",
      "choices": [
        { "route": "CORNFIELD", "next": "scarecrow", "label": "FOLLOW THE CORNFIELD", "note": "A straw hand is moving above the corn." },
        { "route": "MUNCHKIN VILLAGE", "next": "munchkins", "label": "ENTER THE VILLAGE", "note": "Music is coming from the square." }
      ],
      "local": { "es": { "act": "…", "title": "…", "story": "…", "choices": [ { "route": "…", "label": "…", "note": "…" }, … ] }, … }
    }
  },
  "endings": {
    "master": { "success": true,  "image": "01_cover.webp", "label": "PAST CONTINUOUS MASTER", "title": "EMERALD CITY IS OPEN", "text": "…", "local": { … } },
    "lost":   { "success": false, "image": "01_cover.webp", "label": "LOST IN THE POPPIES",    "title": "THE ROAD FADED",     "text": "…", "local": { … } }
  },
  "images": {
    "01_cover.webp": "data:image/webp;base64,…",
    "02_q1_tornado.webp": "data:image/webp;base64,…"
  }
}
```

Rules for the structure:

- Scene ids are short lowercase words (`storm`, `cellar`, `crossroads`).
  Every `correctNext`, `wrongNext` and `next` must name an existing scene
  or `end:<ending key>` (e.g. `end:master`). The graph must be complete:
  no dead ends, every scene reachable from `first`.
- `hotspot` is the object the clue names, as a box in **percent of the
  picture**: `x`,`y` the centre, `w`,`h` the size. It is a suggestion; we
  check every one by eye, so make it honest.
- `relic: true` on the scenes where a tile/relic is collected; the count
  must equal `meta.scoring.tiles`.
- `explanation` is required on every question scene.
- `local` blocks carry the nine languages; missing keys are a defect.
- Answer options carry no `local`.
- The file also plays on its own: a minimal page that walks the graph,
  keeps score, and shows each picture. Plain CSS, no frameworks, no
  external requests. That is for checking the content, not for
  publishing.

### 6. Before you deliver, check

- Every question tests the named grammar point and only that.
- Every wrong option is a plausible learner error.
- Every explanation names the rule, not just the answer.
- Every picture has one object on one side and a quiet other side.
- Every `local` has all nine languages on every string.
- The JSON parses. Count: scenes, relics, endings, pictures.

Deliver the HTML file, then a short table: scene id · picture · object ·
correct answer · next. Nothing else.

---

*(end of prompt)*

## For the Claude session that receives the file

This is the **Oz kind** of export (`window.*_GAME_DATA`), with four
additions the earlier exports lacked: `meta`, `briefing`, per-scene
`hotspot` and `explanation`, and `local` in nine languages.
`extract_standalone.py` passes unknown keys through to `data.json`
untouched, so read them in the builder:

- `briefing` → the `rules` scene; `explanation` → `fb`; `hotspot` → the
  first draft of `HOT` (still verify every one on a contact sheet and a
  closed-scene screenshot; README §3–4);
- `local` → build the `translations/<lang>.json` maps from it instead of
  translating from scratch, then run the validator and fill whatever it
  lists as missing;
- `meta.accent` → check it against `CAMP` in the hub builder and use the
  camp colour if they differ; `meta.scoring` → the spec's `max`, `points`,
  `tiles`, `chances`, `complete_score`.

If the file arrives without some of these, it is the old Oz kind: follow
`docs/HANDOFF-rpg.md` as written and write the missing parts yourself.
