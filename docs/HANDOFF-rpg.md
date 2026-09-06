# Handoff — building a Block Camp RPG to house style

**For:** a fresh Claude session, started with `Inneski/forbes-english` added
as a GitHub source, given one standalone RPG export as a chat attachment.
**Goal:** the export becomes a published Block Camp adventure — glowing
object on every picture, text that pops out of it, Monocraft headings over
Courier New reading text, sound effects, nine languages, hub card, library
card — and goes live on forbesenglish.com.

The prompt Innes will send with the file is one line:

> Rebuild this RPG export as a Block Camp RPG, to the standard in
> lesson-template/build/rpg/README.md.

Start immediately. Do not ask about audience, level, tone or scope — the
level is on the export, the look is defined below, the scope is the whole
game. `lesson-template/HOUSE-STYLE.md` §14 lists the only four reasons to
stop and ask; none of them is "which font".

---

## 1. What "perfect house style" means for an RPG

Two RPGs already meet it and are your reference: **The Lost Yellow Road**
(`block-camp/lost-yellow-road-rpg.html`, Past Continuous, A1–A2) and
**Wonderland: The Stolen Now** (`block-camp/wonderland-stolen-now-rpg.html`,
Present Continuous, A1–A2). Open either in a browser first. Everything
below is what you are looking at.

1. **One full-bleed picture per scene, one glowing object on it.** The
   object is the thing the clue talks about (the axe, the lantern, the
   compass). Clicking it — or Enter — pops the text panel out of that spot.
   ✕, Esc or a click on the picture folds it away. Cover and endings open
   with the panel up; every other scene starts closed.
2. **Dark glass panel, big type.** Story 1.65cqw, options 1.4cqw, title
   3cqw, panel 46% of the frame. Phones get a bottom sheet. Never shrink
   type to fit; widen the panel for that scene (`width`) or cut copy.
3. **Monocraft for display, Courier New for reading.** Titles, kickers, HUD
   badges, buttons, answer keys and the "click to read" label are
   Monocraft (embedded, 8 KB a weight). Story, clue, question, options,
   feedback and glosses are Courier New, glosses italic. Innes asked for
   exactly this split; the first two RPGs shipped all-Monocraft and he sent
   them back.
4. **Sound effects.** Two tones, square for right and sawtooth for wrong,
   behind a HUD toggle and the S key, off by default, remembered per
   browser. The engine provides them; you cannot forget them.
5. **Nine languages, English on top, gloss beneath.** Spanish, German,
   French, Italian, Portuguese, Russian, Arabic, Chinese, Japanese — on
   every title, kicker, story, clue, prompt, explanation, briefing card,
   route choice, ending and chip. Never a gloss instead of the English.
   Options are glossed only if the export glossed them; otherwise they
   stay English — they are the language being taught.
6. **The camp colour is the only accent.** Take it from `CAMP` in
   `lesson-template/build/block-camp-hub/build.py` for the tense (Past
   Continuous `#F1D779`, Present Continuous `#E66085`, …). A grammar point
   with no camp uses the hub's gold `#e8c04a`.
7. **A rules briefing before the first question** (up to five form cards
   and a note) and **one explanation line under every answer**, right or
   wrong. Exports have neither. Write them; they are the lesson.
8. **HUD: points · tiles/relics · chances or progress**, translate menu,
   sound, fullscreen. Keys 1–3 answer, L cycles language, S sound, F
   fullscreen. The corner help line is translated too.
9. **The export's own game rules stay.** Points per question, tiles or
   relics, chances or repair-until-correct, route rewards, ending
   thresholds — keep them exactly. You are restyling, not redesigning.
10. **Learner-facing text never mentions a previous version.** "The old
    page" belongs in the builder docstring and the commit, not on a scene.

The binding document is `lesson-template/build/rpg/README.md`. This
handoff is the walk-through; if they ever disagree, the README wins and
you fix this file.

## 2. The pipeline, in order

```bash
# 1. pictures + text out of the export
python3 lesson-template/build/rpg/extract_standalone.py <export.html> <slug>
#    -> block-camp/<slug>/NN_name.webp   and   lesson-template/build/rpg/<slug>/data.json
#    (works for the Oz kind of export; see §3 for the other kind)

# 2. a builder for this lesson — copy the closest one and edit
cp lesson-template/build/build_lost_yellow_road.py lesson-template/build/build_<name>.py

# 3. build; the validator names every hotspot off the picture, every dangling
#    `next`, and every string missing a language — fix until it prints "wrote"
python3 lesson-template/build/build_<name>.py

# 4. wire in
#    - ADVENTURES table in lesson-template/build/block-camp-hub/build.py, then
python3 lesson-template/build/block-camp-hub/build.py
#    - one line in LESSON_IMAGES in library.html (cover picture), then
node   lesson-template/check-library.js --vs-origin       # must PASS
#    - one row in tools/lessons.json after the last RPG (sort_order 0, deck false)

# 5. ALWAYS last, then read `git diff` on library.html, llms.txt,
#    lesson-meta.json and sitemap.xml — additions only, or restore what it removed
python3 tools/seo.py
```

`<slug>` is `<name>-rpg`: `lost-yellow-road-rpg`, `wonderland-stolen-now-rpg`.
The page and its picture folder share it.

## 3. The two kinds of export, and how to read a third

- **Oz kind** (`…Sherpa_Yellow_Standalone….html`): one
  `window.*_GAME_DATA` JSON object, `local.es/.de` blocks, 3:2 pictures.
  `extract_standalone.py` handles it whole. Builder to copy:
  `build_lost_yellow_road.py`.
- **Wonderland kind** (`…_V1.html`): `EMBEDDED_SCENES` plus
  `const ACT_ONE = [q(…)]` tables in the script, 16:9 pictures, two-blank
  "cake" items, repair-until-correct scoring. The text is JavaScript, not
  JSON: slice the script from `const q =` to `function resetState`, run it
  in node, print the tables as JSON; the cover, prologue, fork, briefing
  and decision prose live in its render functions and are transcribed by
  hand. Builder to copy: `build_wonderland_stolen_now.py`. Pass
  `img_w`/`img_h` in the spec.
- **ChatGPT kind** (made from `docs/CHATGPT-RPG-BRIEF.md`): the Oz kind
  plus `meta`, `briefing`, per-scene `hotspot` and `explanation`, and nine
  languages in `local`. Extract as Oz; the tail of the brief says which
  field feeds which part of the spec.
- **A third kind:** read its whole script before anything else. Find
  where the pictures are (base64 map), where the questions are (a table or
  an object), what the scoring rule is, and which of the two builders is
  closer. Say in the builder docstring which kind it was and how you got
  the text out. If it has a mechanic the engine lacks, add it to
  `rpg/rpg.py` generically (the way `repair`, split options and gated
  routes were added), never as a one-off in the page.

## 4. Hotspots — the part that needs eyes, every time

1. Make gridded contact sheets of every picture (the snippet is in README
   §3; four pictures to a sheet, 10% gridlines with labels).
2. Look at each one and write `HOT[scene] = ([cx, cy, w, h], side, valign)`
   in percent of the picture. The object is the one the clue names. The
   panel goes on the empty side; the object on the other, so the panel
   never covers what it grew out of. Route-choice scenes use `center`,
   `top`. Widen the briefing to 56%.
3. Build, then screenshot **every scene closed** at 768×432 and tile them.
   A hotspot that missed is obvious in the thumbnail and invisible in the
   table. Fix, rebuild, re-shoot until every glow sits on its object.

## 5. Translations — nine, no exceptions

1. Build once with `LANGS = ['es', 'de']` to get the game right.
2. Dump the English strings: build the spec, collect every dict with an
   `en` key (a ten-line script; `build_lost_yellow_road.py` shows the spec
   shape). Expect 200–250.
3. Write `lesson-template/build/rpg/<slug>/translations/<lang>.json` for
   `fr it pt ru ar zh ja` — a flat `{"English string": "translation"}`
   map. Keep grammar formulas in English (the engine hides a gloss that
   equals its English). For wrong options, gloss the meaning and add
   "(wrong form)" in that language; do not invent grammatical nonsense.
4. Set `LANGS = rpg.NINE` and wrap the build:
   `rpg.assemble(rpg.apply_translations(build(), <translations dir>))`.
   The validator lists every string still missing a language; it refuses
   to build until none is.
5. Screenshot Japanese, Arabic (right-to-left), Russian and Chinese. CJK
   and Arabic fall back to the system face at gloss size; that is fine.

## 6. Check before you ship

Chromium and Playwright are on every cloud sandbox
(`NODE_PATH=$(npm root -g)`). Not optional. Shoot at 1536×864 and 390×844:

- the cover, the briefing, a question closed and open, a wrong answer, a
  right answer, a route choice, the ending — in English and in one gloss
  language;
- all scenes closed, tiled (§4);
- the sound toggle on;
- Japanese, Arabic, Russian, Chinese (§5).

Read the pictures. "No errors" from the script proves nothing. What to
look for: glow on the object; open panel not hiding the object's side;
nothing scrolls except an answered question; titles wrap to two lines at
most; glosses shorter than the panel; split options not squashed on a
right-hand panel.

## 7. Ship it, and mean it

The live site serves **`origin/main` only**. A push to your branch is not
on the site. Cloudflare builds a preview of every PR branch at
`<branch>.forbes-english.pages.dev` and the bot links it on the PR; that
preview is not the site either, and it has fooled Innes once ("I saw it
last night and now it has vanished").

1. Commit and push your branch. Deliver files first, ask afterwards.
2. Open the pull request, with main merged in and no conflicts.
3. Innes wants it live. If he says so ("put them back", "not on the site"),
   merge it yourself; he has done that through Claude twice. Otherwise
   give him the PR link and say merging is the one click.
4. **After the merge**, insert the catalogue row — never before, a row
   whose page 404s is a dead library card:

   ```sql
   insert into lessons (file, title, level, access, deck, video, sort_order)
   select 'block-camp/<slug>.html', '<Title> — <Grammar> <World> RPG (<level>)', '<level>', 'pro', false, false, 0
   where not exists (select 1 from lessons where file = 'block-camp/<slug>.html');
   ```

   The Supabase MCP tools work from a cloud session even though `urllib`
   does not. Titles follow *The Lost Yellow Road — Past Continuous Voxel
   Oz RPG (A1-A2)*.
5. Record it in `docs/HANDOFF.md`: what shipped, what the export lacked,
   what you added, the PR number, the row id, and "nothing left to run".

## 8. Traps that have already cost a day

- **Getting the file.** A cloud session cannot see Downloads, and the
  Google Drive connector drops a 7.5 MB file. Only a chat attachment or a
  file committed to the repo reaches you. Say so in one sentence if the
  file has not arrived; do not go looking.
- **`seo.py` in a cloud session** uses `tools/lessons.json` and deletes
  from four indexes anything not in that cache. Add your row to the cache
  first, run it last, read the diff.
- **`library.html`** — run `check-library.js --vs-origin` before touching
  it; a stale copy silently drops other lessons' thumbnails.
- **A re-run of a builder is byte-identical** and keeps the SEO block. If
  it is not, something is wrong with your builder, not with the page.
- **Do not restyle the older three RPGs** (Last Train Home, Blocula, Long
  Way Home) as a side effect. Moving them onto the engine is its own job,
  listed under Open in `docs/HANDOFF.md`.
- **Do not create a second accent, a second display face, or a print
  button.** All three were tried and removed.

## 9. Where everything is

| What | Where |
|---|---|
| The standard, binding | `lesson-template/build/rpg/README.md` |
| The engine (CSS, JS, `assemble()`, validation, translations loader) | `lesson-template/build/rpg/rpg.py` |
| Export → pictures + JSON (Oz kind) | `lesson-template/build/rpg/extract_standalone.py` |
| Monocraft subsets and how to regenerate them | `lesson-template/build/rpg/fonts/` |
| Reference builders | `lesson-template/build/build_lost_yellow_road.py`, `build_wonderland_stolen_now.py` |
| Per-lesson text and translations | `lesson-template/build/rpg/<slug>/data.json`, `…/translations/*.json` |
| Hub card table | `lesson-template/build/block-camp-hub/build.py` → `ADVENTURES` |
| Camp colours | same file → `CAMP` |
| Site-wide rules (the default action, publishing, seo.py) | `CLAUDE.md` |
| House style for everything | `lesson-template/HOUSE-STYLE.md` |
| The running log, newest first | `docs/HANDOFF.md` |
