# Brief for ChatGPT — build an RPG export that lands house-style-perfect

**How to use this file.** Copy everything between the two rules into
ChatGPT, then add five lines of your own: the grammar point, the level, the
story world, the art style, and how many questions. Ask for the one HTML
file. Then hand that file to Claude — a local session with the file in
`incoming/`, or a cloud task with `Inneski/forbes-english` added as a source — and say:
*"Rebuild this RPG export as a Block Camp RPG, to the standard in
lesson-template/build/rpg/README.md."*

**What our engine supplies, and ChatGPT must not try to reproduce:**
Monocraft and Courier New, the dark glass panel, the pop-out animation, the
glow marker, the two sound tones, the HUD, the language menu, the hub card,
the library entry. Those are the same in every Block Camp RPG and they come
from `rpg.py`. ChatGPT's job is the **content in the exact shape the engine
reads**, written to fit that chrome. The prompt below describes the chrome
anyway, because the chrome is what the word budgets and the picture rules
are *for* — not so ChatGPT can imitate it.

**The art style is a parameter, not a constant.** The first six adventures are
blocky voxel Minecraft art because that is what Block Camp is. Sherlock: The
Blue Hour, 2026-09-10, is painted Victorian London — and it is the cleanest
export we have received, passing `check-rpg-panels.js` on the first run, which
no voxel one has. So **name the style on your brief.** Nothing in the engine
cares: it takes 3:2 WebP plates and puts a glow on one object in each. What
does care is §4a — a style that is not voxel needs a written style contract,
or the hero's face changes between plate 4 and plate 17.

The version of this brief before 2026-09-07 got three things wrong, each of
which cost a session. It did not forbid patch-script revisions — Frankenstein
V32 arrived as twenty-two stacked `<script>` blocks, 118 MB, and every regex
over it read a superseded draft. It did not state the answer-key gates — that
same export had the key in slot 0 on all 44 questions. And it did not say the
glowing object has to be bright enough to see a marker on — six of Blocula's
markers landed on objects too dark to read.

---

You are writing a single-player grammar adventure game for English
learners. Deliver **one self-contained HTML file** that plays in a browser
with no external files, and that embeds all of its game data in exactly the
structure described below.

Your file's own styling does not matter — it is a preview for checking the
content. The file will be rebuilt on our fixed template, which takes only
the JSON and the pictures. The **data, the words and the pictures** are the
whole deliverable: get those exactly right and nothing else matters.

## 0. What the finished game looks like, so you know what you are writing for

Each scene is **one full-bleed picture** with nothing on it but a small HUD
and **one glowing object**. The text is not on the screen: the player clicks
the glowing object and a dark glass panel **pops out of that spot**, about
46% of the width, holding the story line, the clue, the question and three
buttons. Titles are in a pixel face (Monocraft), the reading text is Courier
New, and both are large. A right or wrong answer plays a short tone and puts
one explanation line under the buttons.

Three consequences for your writing, and they are hard limits:

- **The panel does not scroll.** A scene whose text overflows is broken, not
  scrollable. Word budgets are in §2.
- **The panel covers half the picture.** So the glowing object goes on one
  side and the other side stays visually quiet (§4).
- **Every scene stands alone.** The player reads one panel at a time and the
  previous one is gone. Never write "as we saw" or any line that only works
  with the last panel still on screen.

## 1. The shape of the game

- **One grammar point per game**, named in the brief (Past Continuous,
  Present Perfect, *going to*, Modals of Obligation). Every question tests
  that point and nothing else.
- **One question per scene, one picture per scene.** No scene asks two
  questions; no two scenes share a picture (the endings may reuse the cover).
- **15–25 question scenes**, 2–3 route-choice scenes, 4 endings.
- Route choices are real: two or three branches that rejoin later. **Both
  branches must carry the same number of questions**, or two players score
  out of different totals.
- Scoring: 5 points a question, 4 tiles/relics collected at four named
  question scenes, 3 chances. A 15-question path is `max: 75`, `pass: 65`.
  State it on the cover as three chips: `+5 CORRECT`, `4 ROAD TILES`,
  `3 CHANCES`. If the brief asks for repair-until-correct instead, say so in
  `meta.scoring` with `"chances": 0` and keep the points chip.
- **A rules briefing before the first question**: two to five cards, each a
  bold heading and one example sentence, plus one note. This is the grammar
  reference the player can consult; keep it readable at the stated level.
- **An explanation on every question**, right or wrong, one sentence, naming
  the rule rather than repeating the answer: *"Was blowing: an action in
  progress at a past moment. Past Continuous = was/were + -ing."*
- **Four endings**, keyed `master` (full score), `complete` (pass), `missing`
  (finished but short of tiles) and `failed` (out of chances). `master` and
  `complete` may share a picture.

## 2. Word budgets — this is what makes the pop-out panel work

Measured off the shipped games. Treat the maximum as a wall.

| field | aim | max |
|---|---|---|
| `title` (scene title) | 3–4 words | **5 words** |
| `act` (chapter kicker) | 4 words | **6 words** |
| `story` | 7–10 words | **28 words** |
| `clue` | 10 words | **16 words** |
| `prompt` (the question) | 7 words | **13 words** |
| each answer option | 25 characters | **45 characters** |
| `explanation` | 12 words | **25 words** |
| cover `lead` | 25 words | **35 words** |
| briefing card `text` | one example sentence | **12 words** |

A 68-word story line is not a long scene, it is a broken one — that is the
single defect that has cost us the most rework. Split it across two scenes
or cut it.

## 3. The questions, and the two answer-key gates

- Three options: one correct, two wrong. Wrong options are **real learner
  errors** for this grammar point — wrong auxiliary, wrong tense, missing
  *-ing*, *he don't*, *did went*. Never nonsense, never a joke option.
- **The correct option must never be the longest one.** This is a hard gate
  and our builder refuses to build when it is broken. Fix it by lengthening
  the distractors, never by shortening the key. Three options of equal length
  is the target; ties give nothing away.
- **Deal the key across the three slots.** Our engine renders the options in
  the order you write them — the first option really is the first button, on
  every play. Aim for roughly a third in each slot; **no slot may hold more
  than 40% of the keys**. A shipped game runs 8 / 7 / 3 over eighteen
  questions. An export with the answer in slot 0 every time is unusable.
- The clue carries the **evidence** for the answer, never the answer. If the
  clue already uses the target form, the question is free.
- No question depends on knowing the story world, only on the grammar.

## 4. Pictures, the art style and the glowing object

- One picture per scene, plus a cover. **WebP, 1536 × 1024 (3:2), each under
  200 KB.** No PNG, no JPEG.
- **The art style is the one named on the brief** — blocky voxel, painted
  illustration, ink and wash, cel animation, gouache storybook, noir
  photoreal. Whatever it is, it is the same style in every plate, on one
  palette, and it is written down (§4a). If the brief names no style, use
  painted illustration.
- **No lettering anywhere in the art.** No words on signposts, shop fascias,
  book pages, maps or labels. An image model's English comes out garbled at
  1536 px, and a broken word on a language lesson reads as a mistake in the
  lesson. A signpost is fine; a signpost with writing on it is not.
- **Every picture has exactly one clear object that the clue is about** — the
  tornado, the lantern, the axe, the ship's wheel. That object is what the
  player clicks and where the panel grows from.
- The object goes on **one side**; the **other side stays visually quiet**,
  because that is where the panel sits. Do not centre the object. Do not
  fill both sides with detail.
- **The object must be light enough to wear a glow.** Our marker takes its
  colour from the object underneath it, so a dark object on a dark ground
  produces a marker nobody can see. If the natural object is a black cauldron
  at night, light it — a lantern on it, a rim of moonlight — or choose a
  different object the clue can name.
- The object must be **nameable in one or two words** in the clue: "the
  lantern", "the broken cart". If a scene's clue names nothing physical, use
  the character whose action the question is about, and give them room.
- Route-choice pictures glow **where the road divides**; endings glow on the
  destination or the wreckage.
- Name the files `01_cover.webp`, `02_q1_tornado.webp`, `03_q2_cellar.webp` …
  in play order, and inline every one as a base64 data URI in `images`.
- **Only ship the pictures the game uses.** No superseded art, no alternates.

## 4a. The style contract — what replaces "voxel"

Voxel art is forgiving: a character who is six cubes and a hat looks the same
in every plate. Every other style drifts. Twenty-two plates from twenty-two
prompts give you three different Holmeses unless you fix the description once
and never vary it.

- **Write the style sentence once and paste it verbatim into every image
  prompt** — medium, light, palette, camera — and put that same sentence in
  `meta.style` so we can read what you were aiming at: *"Painted digital
  illustration, Victorian London at blue hour, cool slate and gaslight amber,
  soft brush edges, no hard outlines, three-quarter view at eye level."*
- **A character sheet, one line per recurring character**, pasted into every
  prompt that character appears in: *"Holmes: tall and thin, dark grey ulster,
  no hat, black hair swept back, clean-shaven."* This rule exists because the
  Frankenstein game needed *"flat-topped green head, amber eyes, cropped dark
  hair, cross stitches, ragged layered coat"* on every prompt to stop the
  Creature growing long hair halfway through the story.
- **One palette and one light key for the whole game**, named in that
  sentence. A game that wanders from blue hour to noon to firelight looks
  like three games.
- **Every filename is a different picture.** An export with eighteen
  filenames holding ten images was thrown away whole: a player met the same
  street three times and read it as a bug. The four endings and the briefing
  may reuse a question's plate; nothing else may.
- **Dark, but never black.** The panel is dark glass and our marker takes its
  colour from the object underneath, so a night scene needs a light source in
  frame — a lamp, a lit window, moonlight on wet stone. No heavy grain, no
  lens flare, no crushed blacks: they eat the glow (§4).
- **Put the object on the same side in every scene.** Sherlock composed all
  twenty-two plates with the object right of x=60, so the panel sat left all
  game and not one scene needed adjusting — the only export that has ever
  needed none. Pick a side at the start, keep it, and leave the other side
  quiet.
- **Styles that fight the chrome:** anything on a bright flat white ground
  (the dark glass panel disappears), anything that has to be read as text
  (newspapers, diagrams, labelled maps), and anything so densely detailed
  that both halves of the frame are busy.

## 5. Language, level and typography

- The level is on the brief (A1–A2, B1, …). Short sentences, one idea per
  sentence, no idioms below B1.
- Titles in CAPITALS. Chapter labels like `CHAPTER 1 · KANSAS`.
- The player is addressed as "you"; the hero has a name.
- **Straight apostrophes and quotes only** (`'` and `"`), consistently. Three
  options where one has a curly apostrophe differ typographically as well as
  grammatically, which is a free clue.
- Never refer to a previous version of anything — not a draft, not "the old
  version", not this export.
- **The display face is a pixel font (Monocraft) whatever the art style.**
  That is our engine's chrome, identical on every adventure; it is not a
  reference to the pictures, and you do not write for it beyond the word
  budgets in §2. If the game is not voxel, say so in the words instead: no
  VOXEL in the `eyebrow`, no BLOCK in a title, and `meta.world` names the
  world as it looks — *"Victorian London"*, not *"Voxel London"*.

## 6. Translations — nine languages, glossing the final English

Every learner-facing string carries a `local` block with the same text in
`es`, `de`, `fr`, `it`, `pt`, `ru`, `ar`, `zh`, `ja`: cover, chips, briefing
cards and note, chapter labels, titles, story, clue, prompt, explanations,
route names and notes, endings.

- **Do not translate the answer options.** They are the English being taught.
- **A blank stays a blank.** If a prompt contains `___`, the translation keeps
  `___` in the same slot and translates the sentence around it. A gloss that
  fills the blank in gives the answer away.
- **English grammar tokens stay English inside a translation**: *was/were +
  -ing*, *is going to*, *base verb*, *Is Victor going to…?*.
- **Each language is only itself.** No Cyrillic inside the Japanese, no kana
  inside the Chinese, no English paragraph standing in for a missing Russian
  gloss. We check this mechanically and it fails the build.
- **Glosses must match the English you actually shipped.** If you revise a
  line, revise its nine glosses in the same pass. A 21-word English line under
  a 52-word German paragraph describing an earlier draft is worse than no
  gloss at all — we throw the whole set away and re-translate.

## 7. The data structure — exact

Put **one** `<script>` at the end of the body containing exactly:

```html
<script>
window.<NAME>_GAME_DATA = { ...JSON... };
</script>
```

`<NAME>` is the game in capitals (`FRANKENSTEIN`), and the value is **valid
JSON** — double quotes, no trailing commas, no comments, no functions, no
expressions.

```json
{
  "meta": {
    "title": "THE LOST YELLOW ROAD",
    "grammar": "Past Continuous",
    "world": "Voxel Oz",
    "style": "Blocky voxel Minecraft art, Kansas dust and storm grey, flat daylight, eye-level camera",
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
    "local": { "es": { "eyebrow": "…", "title": "…", "lead": "…", "rules": ["…","…","…"], "start": "…", "small": "…" }, "de": {}, "fr": {}, "it": {}, "pt": {}, "ru": {}, "ar": {}, "zh": {}, "ja": {} }
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
    "local": { "es": { "title": "…", "cards": [ { "head": "…", "text": "…" } ], "note": "…", "button": "…" } }
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
        { "text": "It blew hard and fast." },
        { "text": "It was blowing hard.", "correct": true },
        { "text": "It were blowing hard." }
      ],
      "explanation": "An action in progress at a past moment: was + blowing. 'Blew' is finished; 'were' does not go with 'it'.",
      "points": 5,
      "relic": false,
      "correctNext": "cellar",
      "wrongNext": "cellar",
      "local": { "es": { "act": "…", "title": "…", "story": "…", "clue": "…", "prompt": "…", "explanation": "…" } }
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
      "local": { "es": { "act": "…", "title": "…", "story": "…", "choices": [ { "route": "…", "label": "…", "note": "…" } ] } }
    }
  },
  "endings": {
    "master":   { "image": "01_cover.webp",           "label": "PAST CONTINUOUS MASTER", "title": "EMERALD CITY IS OPEN", "text": "…", "local": {} },
    "complete": { "image": "01_cover.webp",           "label": "ROAD REBUILT",           "title": "THE ROAD HOLDS",       "text": "…", "local": {} },
    "missing":  { "image": "20_ending_gate.webp",     "label": "TILES MISSING",          "title": "THE ROAD IS SHORT",    "text": "…", "local": {} },
    "failed":   { "image": "21_ending_poppies.webp",  "label": "LOST IN THE POPPIES",    "title": "THE ROAD FADED",       "text": "…", "local": {} }
  },
  "images": {
    "01_cover.webp": "data:image/webp;base64,…",
    "02_q1_tornado.webp": "data:image/webp;base64,…"
  }
}
```

Rules for the structure:

- Scene ids are short lowercase words (`storm`, `cellar`, `crossroads`).
- Every `correctNext`, `wrongNext` and `next` names an **existing scene** or
  `end:<key>` (`end:master`). The last question on each branch uses
  `"correctNext": "resolve"` so the score picks the ending.
- **The graph must be complete and tight**: every scene reachable from
  `first`, no dead ends, and **no orphans** — a scene nothing points at is a
  defect, not a bonus. If you replace a scene, delete the one it replaced.
- `hotspot` is the object the clue names, as a box in **percent of the
  picture**: `x`,`y` the centre, `w`,`h` the size. We check every one by eye,
  so make it honest — a guessed box is worse than none.
- `relic: true` on exactly the scenes where a tile is collected; the count
  must equal `meta.scoring.tiles`.
- `explanation` is required on every question scene.
- `local` carries all nine languages on every string; a missing key is a
  defect. Answer options carry no `local`.

## 8. How to deliver — one file, one version, final text

- **One `<script>` block holding the final data.** If you revise the game,
  re-emit the whole file with the revision already inside the JSON. Do
  **not** append patch scripts that reassign or edit the data afterwards — a
  file whose real text only exists after twenty-two stacked patches cannot be
  read by anything but a browser, and we have to run it in a VM to recover
  the lesson. One file, one truth.
- **Keep it under 25 MB.** That is roughly fifty pictures at 200 KB. If it is
  bigger, the pictures are not WebP or not compressed.
- The file also plays on its own: a minimal page that walks the graph, keeps
  score and shows each picture. Plain CSS, no frameworks, no external
  requests, no fonts fetched. That preview is for checking content only.

## 9. Before you deliver, check

1. Every question tests the named grammar point and only that.
2. Every wrong option is a plausible learner error, and no key is the longest
   option in its scene.
3. The key sits in slot 1 / 2 / 3 in roughly equal numbers; no slot over 40%.
4. Every explanation names the rule.
5. Every field is inside its word budget in §2.
6. Every picture is WebP, 1536×1024, under 200 KB, with one nameable object,
   bright enough to glow, on one side — the same side all game — and a quiet
   other side.
7. One style, one palette, one look per character, no lettering in the art,
   and no two filenames holding the same picture. `meta.style` says what the
   style was.
8. Every scene is reachable; nothing is orphaned; every `next` resolves.
9. Every `local` has all nine languages on every string, glossing the text you
   actually shipped, with `___` preserved and options untranslated.
10. The JSON parses. Count and report: scenes, questions, relics, endings,
    pictures, total file size.

Deliver the HTML file, then one table — scene id · picture · object · key
slot · correct answer · next — and nothing else.

---

## For the Claude session that receives the file

This is the **Oz kind** of export (`window.*_GAME_DATA`), with the additions
the first exports lacked: `meta`, `briefing`, per-scene `hotspot` and
`explanation`, and `local` in nine languages. `extract_standalone.py` passes
unknown keys through to `data.json` untouched, so read them in the builder:

- `briefing` → the `rules` scene; `explanation` → `fb`; `hotspot` → the first
  draft of `HOT` (still verify every one on a contact sheet and a
  closed-scene screenshot; README §3–4);
- `local` → build `translations/<lang>.json` from it, then run
  `check_translations.py` and fill whatever it lists as missing. **Check the
  glosses against the English before trusting them** — an export revised late
  glosses a version nobody reads (HANDOFF, 2026-09-07);
- `meta.accent` → check it against `CAMP` in the hub builder and use the camp
  colour if they differ; `meta.scoring` → the spec's `max`, `points`,
  `tiles`, `chances`, `complete_score`;
- `meta.style` → the builder docstring, and the world word in the catalogue
  title follows the art: *Sherlock Holmes: The Blue Hour — Present Simple
  London RPG (A2)*, not *Voxel RPG* (README §5; HANDOFF, 2026-09-10). The
  chrome does not follow it — Monocraft, the dark glass, the pop-out and the
  camp accent are the standard on every adventure whatever its pictures look
  like;
- `_check_answer_key` in `rpg.py` enforces §3 at build time. If it fires, the
  export ignored the brief: re-deal the key in the builder, never disable the
  gate.

If the file arrives without these — or as a stack of patch scripts, which is
the third kind — follow `docs/HANDOFF-rpg.md` and `README.md` §2 as written
and write the missing parts yourself.
