# The Climb — Sherpa Tensing's tense game

`sherpa-tensing-the-climb.html` is generated. Edit the files here and rebuild; a hand edit to the page is overwritten.

| File | What it is |
|---|---|
| `content.py` | Every English word the learner reads: the cast, the camps, the items, the summit push. The schema is in its docstring. |
| `build.py` | Validates the content, reads the route map, fills the template, applies the Sherpa family blocks, and writes the page and `i18n/strings.json`. |
| `template.html` / `.css` / `.js` | The page. The builder inlines all three, so the output is one file (plus images, fonts and `block-camp/camp-music.js`). |
| `i18n/<lang>.json` | One flat `{"English": "translation"}` file per language (de es fr it pt ru ar zh ja). |
| `i18n/strings.json` | Generated: every string to translate, with a note on where it appears. |
| `test_climb.js` | Plays the game in Playwright at 1280×800 and 390×844, runs the no-scroll gate at five more sizes, and unit-tests the typed-answer canon. |

## Build

```bash
py lesson-template/build/sherpa-climb/build.py            # write the page (only when it changes)
py lesson-template/build/sherpa-climb/build.py --check    # exit 1 if the page on disk is not a fresh build
py lesson-template/build/sherpa-climb/build.py --strict   # also fail on any language not fully translated
```

The build is deterministic: build twice and you get the same bytes. If `tools/seo.py` has written its SEO block into the page, the builder carries it over, so `seo.py` and `--check` do not fight.

Three options are for drafts and tests. `--content <file.py>` builds from another content file. `--i18n <dir>` builds with another translations folder. `--out <file.html>` writes (or `--check`s) another file instead of the page: a test variant, which `test_climb.js --page <file.html>` serves at the page's own URL. `strings.json` always comes from the real `content.py`.

### What the builder reads, and from where

- **From the route map** (`sherpa-tensing-route-map.html`), by regex: the 13 camp colours, inks, levels, tense names and camp-page links (from its colour key rows, cross-checked against its markers), the ascent mountain (`#epic-day-v2` and every def it uses, the 13 markers and 12 route segments), its `:root` tokens, and the language names in its menu.
  - Nothing is copied. The map has been recoloured several times.
- **Derived from those colours** in OKLCh, never picked by hand:
  - each camp's text colour (darkened along its hue to 4.5:1 on the paper);
  - its highlighter (the same hue, light);
  - the team's pack colours.
- **Where the card sits on a computer:** on the quieter side of each scene, measured from the picture (edge density at 200px wide, left 5–45% against right 57–97%; the card moves left only when the right is clearly busier). A camp dict may set `'side': 'left'` or `'right'` to overrule it.
- **Tokens:** every custom property of the map's `:root` blocks (colours, `--radius`, `--lift`). The build refuses a `var(--x)` in `template.css` that nothing defines.
- **The sheen** is `tools/sherpa_sheen.py`'s own block, with its two colours greyed to the map's `MAP_CHROMA`, as the map's are, because this page wears the map's greyed chrome. The override is one class stronger than the tool's block and leaves the block as the tool writes it.
- **The family look** comes from the tools' own functions: `sherpa_type`, `sherpa_topo`, `sherpa_sheen`, `sherpa_sky` (with the existing cloud sizes, so the clouds are not re-rendered) and `sherpa_arrive`. The wordmark is `sherpa_links.BRAND_NEW` + `SUB_NEW`, byte for byte.
  - So every `tools/sherpa_*.py --check` passes on the page as built, and the builder re-runs them on its own output before writing.

### Gates: the build refuses, naming the item

- Ids must be unique.
- `who` must be in `CAST`; `via` must be in `VIA`.
- **choose:** exactly 3 distinct options, with `options[0] == answer`.
  - The key may not be the longest option by more than 10% *and* 4 characters.
  - The key may not be the shortest by more than 1.5× *and* 10 characters. This is the answer-key rule from `rpg.py`.
  - The gaps must match: a `'...'` answer needs 2 gaps, otherwise 1. At most one `'...'`, in every option alike, and no empty part.
- **type:** one gap; `answer` must be in a non-empty `accept`.
- **spot:** exactly one `[ ]` and no gap; `answer == options[0]`; three distinct camp numbers that exist on the route map. A camp's spot line may mark another camp's tense, and should sometimes: if it always marks the camp's own, the camp chip on the card answers it.
- **fb:** at least one CAPS token, and no form cited in 'single quotes'.
- **tip:** must have a CAPS form.
- Every `**bold**` must be paired.
- **Translations:**
  - every CAPS token and `{placeholder}` of the English must survive;
  - `**` must stay paired;
  - a broken translation stops the build.

## Test

```bash
node lesson-template/build/sherpa-climb/test_climb.js              # the game in a browser, plus the canon
node lesson-template/build/sherpa-climb/test_climb.js --canon      # the canon only (reads it out of the built page)
node lesson-template/build/sherpa-climb/test_climb.js --shots DIR  # where screenshots go (default: $CLIMB_SHOTS, else %TEMP%/sherpa-climb-shots)
node lesson-template/build/sherpa-climb/test_climb.js --no-gate    # skip the five-size no-scroll gate (a quick run)
node lesson-template/build/sherpa-climb/test_climb.js --content F --page P   # a variant: build.py --content F --out P first
```

The test plays camp one with its first typed line wrong on purpose (or its first line, if it has no typed line). That line must come back last, and the score must read "First try: 7 of 8". The typed answers are written differently from the accept list ("'m writing", "dont like", "Checks."), worked out from the content, so the canon is tested in the page. It then checks:

- the save in `sherpa.climb.v1`;
- that `sherpa.progress.v1` is untouched;
- "Continue: camp 2";
- camp two, all right first time;
- flags and bests on the start screen;
- the keyboard (Enter, 1–3, S, Esc);
- that a language which is not complete is not offered;
- that there are no console errors and no sideways scroll;
- a double-click on "Next": the second click must not answer the next line;
- on a phone, that the card and every control stay inside the viewport for every item;
- **the no-scroll gate** (Innes: "NO scrolling" in a game panel): at 1366×768, 1280×720, 1024×768, 844×390 and 360×740, every arrival card, every line asked and answered wrong (its tallest state), every camp-complete card and the summit screen with 25 or more lines to look at again. The card may not scroll, and every control must be on screen;
- if the page offers more than one language, that switching in the middle of a line keeps the line, its option order, what was typed and the answer.

The card fits by design; if a long line still does not, the page tightens it a step at a time (`fit()` in `template.js`: spacing and portraits, then "Next" beside the verdict, then a size smaller). To try content longer than `content.py` holds, build a variant with `--content` and `--out` and run the test on it with `--page`.

If `content.py` has a `SUMMIT`, it also plays the summit push and checks the summit screen: no tense name on a line before it is answered, the push's `done` line and the `OUTRO`, a count per camp of the lines missed first time (four camps shown at most), and the full lines in the route map's dialog, which Esc closes without leaving the game.

The family checks to run after a build:

```bash
py tools/sherpa_type.py --check; py tools/sherpa_sheen.py --check; py tools/sherpa_sky.py --check
py tools/sherpa_topo.py --check; py tools/sherpa_arrive.py --check; py tools/sherpa_links.py --check
py tools/check_route_map.py
node tools/sherpa_type_check.js sherpa-tensing-the-climb.html
node tools/sherpa_topo_clear.js sherpa-tensing-the-climb.html
```

## Add a camp

1. Add its dict to `CAMPS` in `content.py`, in order, with:
   - `n`, `alt` (whole metres, above the camp before);
   - `arrive` (one or two lines, the form in `**bold**`), `tip` (CAPS form);
   - eight `items`;
   - `done`.
   Ids are `c<n>-<k>`, and they are stable: saves and the review list key on them.
2. The scene is `SherpaClimb/camp-NN.jpg` with a 960px `-sm` copy. All fourteen are already there.
3. Run `build.py`. It names any item a gate refuses. Then run the test.

Once all thirteen camps exist, set `SUMMIT` and `OUTRO`:

- `SUMMIT` is a camp dict with `'n': 'summit'`, `alt`, `top`, and items carrying `'camp': <1-13>`, the tense each one tests.
- `OUTRO` is a list of lines.

After camp 13 the game offers "On to the summit". A camp with no next camp yet shows only "Camps".

## Translate

1. Build once, then read `i18n/strings.json`: every English string, with a note on where it appears.
2. Fill `i18n/<lang>.json` as `{"English": "translation"}`.

What gets translated, and what does not:

- **Chrome** (buttons, headings, labels) is replaced by the translation.
- **Narrative** (arrival lines, tips, explanations, roles, "on the radio") stays in English, with the translation beneath it in italics.
- **Never translated:** the English lines, the options, tense names and CAPS forms.

A language appears in the menu only when it is complete: "complete or empty" (HOUSE-STYLE §8). The build prints the state of every language and, for a partly translated one, each missing string by name; `--strict` fails on any language that is missing strings (an empty file is missing all of them, and that list is `strings.json`).

The menu is hidden while English is the only language. The page reads and writes `sherpa.lang.v1`, the route map's key, and honours `?lang=xx`. Arabic gets `dir="rtl"` on each translated element.

## The save

The game stores everything in `localStorage['sherpa.climb.v1']`:

```
{v:1, camps:{"1":{best,total,gold,plays}}, summit:{best,total,plays}, last, misses:{<id>:true}}
```

- `best` and `gold` latch: a later, lower score never takes them back.
- `misses` holds each item missed on its first try in its latest run. It feeds "Worth another look" at the summit.

It never writes `sherpa.progress.v1`: the route map counts that store as finished camps and opens passives from it.

Sound effects are off by default (`sherpa-climb-sound`). The music button is `camp-music.js` in slot mode, which shares the `bc-music` setting with every Sherpa page.
