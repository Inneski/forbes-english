# Block Camp RPGs — the standard and how to build one

**A standalone RPG export means: rebuild it as a Block Camp RPG, to this
standard. Start immediately.** Innes sends one HTML file (3–5 MB, pictures
inlined, a `window.*_GAME_DATA` object holding the game) and expects the
published adventure back — glowing object on every picture, text that pops
out of it, Monocraft, the hub card, the library entry. Do not publish the
export itself, and do not ask about audience, level or tone: the level is on
the export, the look is defined here.

This file is binding for anything under `block-camp/`. It exists because the
standard was set by hand — Innes's Blocula rebuild of 2026-09-04 (`e6056ab`,
"object hotspots, 11-language glosses") — and then applied to The Lost Yellow
Road on 2026-09-05, which is where the engine in this directory comes from.
His brief for that one, verbatim: *"Text should be bigger and pop up when a
glowing object is clicked … make these RPGs standard like the others in Block
Camp with Monocraft."*

## 1. What a Block Camp RPG is

- **One full-bleed 3:2 picture per scene, nothing on it but the HUD and one
  glowing object.** The picture is the lesson; the text waits behind the
  object. Clicking the object (or Enter) pops the panel out of that spot;
  ✕, Esc or a click on the picture folds it away. The cover and the endings
  open with the panel already up — everything else starts closed.
- **Dark glass panel, Monocraft, big.** Story 1.65cqw, options 1.4cqw, title
  3cqw, on a 46%-wide panel — a step up from Blocula (1.36 / 1.04 / 3.6 at
  42%), because Monocraft is wider than Pixelify and because the brief said
  bigger. Phones get a bottom sheet in fixed px. Do not shrink these to
  make a long scene fit; widen the panel for that scene (`width`) or cut the
  copy.
- **Monocraft everywhere.** Both weights are embedded from
  `fonts/` (8 KB each), so the page makes no font request. The hub uses
  the same face for its headings; the 24 camp decks stay in Pixelify Sans +
  Silkscreen — that is deck chrome, not RPG chrome, and is not up for
  change here.
- **The camp colour is the accent.** Title, kicker, chips, hotspot label,
  the buttons — one colour, taken from the route map's stop for the tense
  (`CAMP` in `block-camp-hub/build.py`: Past Continuous is `#F1D779`,
  Future Simple `#F0723F`, …). A conditionals or narrative-tenses RPG with
  no single camp uses the hub's gold `#e8c04a`. Never a second accent.
- **HUD: points · tiles · chances**, translate menu, fullscreen. Keys 1–3
  answer, L cycles the language, F toggles fullscreen. The corner help
  line names all of that and is itself translated.
- **English on top, gloss beneath.** Every learner-facing string is
  `{en, es, de, …}`; the engine prints the English and the gloss under it,
  never the gloss alone. Options are glossed too (Blocula does the same) —
  the English stays. **Spanish and German are the minimum**
  (HOUSE-STYLE §8); ship only languages you have finished, because
  `assemble()` refuses a string with a missing language and the menu is
  built from what ships.
- **A rules briefing before the first question** (kind `rules`: up to five
  form cards and a note), and **one explanation line under every answer**
  (`fb`), right or wrong. The exports have neither; both are the difference
  between a quiz and a lesson.
- **Learner-facing text never mentions a previous version** — not the
  export, not "the old page". That goes in the builder docstring.

## 2. The pipeline

```bash
python3 lesson-template/build/rpg/extract_standalone.py <export.html> <slug>
#   -> block-camp/<slug>/NN_name.webp   (the pictures, as named in the export)
#   -> lesson-template/build/rpg/<slug>/data.json   (the text)
#   and prints the scene list you fill the hotspot table from
cp lesson-template/build/build_lost_yellow_road.py lesson-template/build/build_<slug>.py
#   edit: HOT, KICKER, FB, RULES, the spec block (title, accent, file)
python3 lesson-template/build/build_<slug>.py          # -> block-camp/<slug>.html
python3 lesson-template/build/block-camp-hub/build.py  # the hub card (after adding to ADVENTURES)
node   lesson-template/check-library.js --vs-origin    # before touching library.html
python3 tools/seo.py                                   # ALWAYS last — and read the diff (CLAUDE.md)
```

`<slug>` is `<name>-rpg` (`last-train-home-rpg`, `long-way-home-rpg`,
`lost-yellow-road-rpg`, `wonderland-stolen-now-rpg`); Blocula's
`dracula-castle-of-if` predates the convention. The page and its picture
folder share the slug.

**Two generators have sent exports so far, and they differ.** The Oz kind
(`Sherpa_Yellow_Standalone`) holds the game in one `window.*_GAME_DATA`
JSON object with `local.es/.de` blocks — `extract_standalone.py` handles it.
The Wonderland kind (`…_V1.html`, `EMBEDDED_SCENES` + `const ACT_ONE = [q(…)]`
tables, 16:9 pictures, 10 points a question and repair-until-correct) keeps
its text in JavaScript; `build_wonderland_stolen_now.py`'s docstring says
how it was pulled out (slice the script from `const q =` to
`function resetState`, run it in node, print the tables as JSON) and the
cover / prologue / fork / briefing prose, which lives in its render
functions, was transcribed by hand. A third kind means: read its script
first, then decide which of the two it is closer to.

Every page is **generated**: edit the builder, re-run it. The builder keeps
the fenced SEO block from the file on disk, so a re-run without `seo.py`
does not strip the metadata — but `seo.py` still runs last, every time.

`check-lesson.js` does not apply — an RPG is not a deck. The checks that do:
`assemble()`'s own validation (every hotspot on the picture, every `next`
resolving, every string in every language), the Playwright screenshots in
§4, and `check-library.js --vs-origin`.

## 3. Hotspots — the part that needs eyes

`HOT` maps every scene id to `([cx, cy, w, h], side, valign[, width])`:

- `cx cy w h` are **percent of the picture** (1536×1024, 3:2), centre and
  size. Not of the browser frame — the engine converts, and on a portrait
  phone it slides the picture so the object is still on screen.
- `side` is where the panel sits: `left`, `right` or `center`. Put it on
  the empty side of the picture, and put the hotspot on the other side so
  the panel does not cover the object it grew out of. `center` is for the
  route-choice scenes (panel 64% wide, `valign` `top`).
- `width` overrides the panel width for one scene — the rules briefing
  wants 56%, a scene with long options 50%, a scene whose picture is busy
  on both sides 38%.

**The object is the one the clue talks about.** "His axe stayed on the
ground" → the axe. "Aunt Em's lantern was lit" → the lantern. A route-choice
scene glows where the road divides. Endings glow on the destination
(Emerald City) or the wreckage. If the clue names nothing, the character
whose action the question asks about.

To pick them, make a gridded contact sheet — the only way to read
percentages off a picture reliably:

```python
from PIL import Image, ImageDraw
im = Image.open('block-camp/<slug>/07_q5_scarecrow.webp').resize((768, 512)); d = ImageDraw.Draw(im)
for p in range(10, 100, 10):
    d.line([(768*p//100, 0), (768*p//100, 512)], fill='white'); d.line([(0, 512*p//100), (768, 512*p//100)], fill='white')
    d.text((768*p//100+2, 2), str(p), fill='yellow'); d.text((2, 512*p//100+2), str(p), fill='yellow')
im.save('sheet.jpg')
```

(`pip install pillow` if it is missing; a cloud session has network.) Four
pictures to a sheet, read them with the image viewer, write the numbers
down, build, then screenshot every scene closed (§4) — a hotspot that
missed is obvious in the thumbnail and invisible in the table.

## 4. Check it before shipping

Chromium and Playwright are on every cloud sandbox
(`NODE_PATH=$(npm root -g)`), so this is not optional:

```js
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(), p = await b.newPage({ viewport: { width: 1536, height: 864 } });
  await p.goto('file:///home/user/forbes-english/block-camp/<slug>.html');
  for (const id of Object.keys(await p.evaluate('G.scenes'))) {
    await p.evaluate(`go('${id}')`); await p.waitForTimeout(400);
    await p.screenshot({ path: `${id}-closed.jpg`, quality: 60 });          // is the glow on the object?
    await p.evaluate('openPanel()'); await p.waitForTimeout(500);
    await p.screenshot({ path: `${id}-open.jpg`, quality: 60 });            // does the text fit? cover anything?
  }
  await b.close();
})();
```

Then the same three at `390×844` (a phone), with the language on
(`state.lang='de'; render()`), and one answered question
(`openPanel(); answer(0)`) to see the feedback and CONTINUE. Read the
screenshots; do not trust the run because it printed no errors.

What to look for: the glow sits on the named object; the open panel does
not hide the object's side of the picture; nothing needs scrolling except
an answered question (that one scrolls itself to the feedback); the title
wraps to at most two lines; the German is not longer than the panel.

## 5. Publishing the lesson (the parts outside `block-camp/`)

1. **Hub card.** Add a row to `ADVENTURES` in
   `lesson-template/build/block-camp-hub/build.py` — href, cover, title, a
   two-sentence blurb in the voice of the other three, grammar chips,
   level, `pro`, lead chip (`new`) — and re-run the hub builder. The tally
   strip and the "four branching adventures" lede count themselves.
2. **Library thumbnail.** One line in `LESSON_IMAGES` in `library.html`,
   pointing at the cover. Run `check-library.js --vs-origin` first, always.
3. **Catalogue row.** The title lives in Supabase, not the HTML
   (HOUSE-STYLE §11). In a cloud session add the row to
   `tools/lessons.json` (after the last RPG, `sort_order 0`, `deck false`)
   so `seo.py` writes the page's SEO block, the sitemap, `llms.txt` and
   `lesson-meta.json` — then put the SQL in `docs/HANDOFF.md` for Innes to
   run **after** the page is live on `origin/main`, never before (a row
   whose page 404s is a dead card in the live library):

   ```sql
   insert into lessons (file, title, level, access, deck, video, sort_order) values
    ('block-camp/<slug>.html', '<Title> — <Grammar> <World> RPG (<level>)', '<level>', 'pro', false, false, 0);
   ```

   Titles follow the three that exist: *The Last Train Home — Future Simple
   Cybervoxel RPG (A1-A2)*, *The Long Way Home — Narrative Tenses Odyssey
   RPG (B1)*.
4. **`seo.py` last**, and in a cloud session read `git diff` on
   `library.html`, `llms.txt`, `lesson-meta.json` and `sitemap.xml` before
   committing — the stale-cache trap in CLAUDE.md.

## 6. The spec, for reference

`assemble(spec)` takes one dict:

| key | what |
|---|---|
| `file`, `img_dir` | `block-camp/<slug>.html`, `block-camp/<slug>` |
| `title`, `description` | the `<title>` and meta description until `seo.py` replaces them |
| `langs` | gloss languages, e.g. `['es', 'de']` — every string must carry each |
| `accent`, `accent_ink`, `deep`, `panel` | the camp colour, the ink on it, the title outline, the panel glass |
| `labels` | overrides for `rpg.LABELS` (HUD words, CONTINUE, PLAY AGAIN …) |
| `start`, `scenes`, `endings` | first scene id; the scenes; `{master, complete, missing, failed}` → ending scene ids |
| `max`, `points`, `tiles`, `chances`, `complete_score` | the scoring — 75 / 5 / 4 / 3 / 65 for a 15-question path |
| `img_w`, `img_h` | picture size when it is not 1536×1024 (Wonderland is 1536×864) |
| `repair`, `total` | `repair: True` = a wrong answer explains and lets the learner try again, points on the first try only, no chances (set `chances: 0`); `total` = questions on any path, shown as a progress badge |
| `tags` | the two half-labels for split options, `{'a': {en,…}, 'b': {en,…}}` (pink NOW / blue USUAL) |

Scene kinds: `intro` (cover: `rules` chips, `start` button, `small` line),
`rules` (form cards + `note`, optional `button` text), `story` (text,
optional `rules` cards and `note`, optional `button`), `question` (`clue`,
`prompt`, `opts`, `answer`, `fb`, `points`, `relic`, `final`, `next`),
`choice` (`routes`: name, desc, route, target — a route may carry `min`
and `else`: below `min` points it goes to `else` instead), `ending`. A
question's `next` of `'resolve'` picks the ending from the score, the tiles
and whether the final question was right. Chances run out → the failed
ending on the next CONTINUE.

An option is `{en, es, de}` (glosses optional — options are the English
being taught and the check skips them) or, for a two-blank item,
`{parts: ['stays', 'is getting'], kinds: ['b', 'a']}`: two coloured halves
labelled from `tags`, first half for the first blank.

## 7. What is deliberately not here

- **Print.** The exports had a "print result" button; the three RPGs
  before this one did not, and a fullscreen game is not a worksheet.
- **A per-scene "wrong turn" branch.** The exports route right and wrong
  answers to the same next scene; the chance counter is the penalty. The
  builder asserts this and would need a `wrongNext` field if an export
  ever differs.
- **Arabic and CJK glosses.** The Monocraft family has Latin and Cyrillic
  only. Blocula carries eleven languages in Pixelify + system fallback; an
  RPG in this engine that needs `ar`, `zh` or `ja` needs a fallback face
  declared for those glyphs first — say so in HANDOFF rather than shipping
  boxes.
