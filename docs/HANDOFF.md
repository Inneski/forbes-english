# Handoff — read this before rebuilding a lesson

This file exists because the working notes used to live only in a
claude.ai Project, which does **not** reach a Cowork sandbox. If you are
a session that was told to read `claude/lesson-queue-handoff.md` and
could not find it: this is that document. It is in git now, so any
session can read it.

**`lesson-template/HOUSE-STYLE.md` in this repo is out of date.** The
deltas are listed at the bottom of this file. Follow the deltas over the
stale copy.

---

## 2026-09-06 — Must & Have To (Minecraft, A2): rebuilt as a deck

`minecraft-lesson.html` was hand-built (custom pixel-art CSS, tab-based, not
the shared template) with Polish as its only L1 support, glossed inline
inside the English sentences rather than through `LANGS`/`UI_I18N`. Innes
decided the language question (see "Polish" under Still open, below):
standard EN + DE + ES, Polish dropped, no shared-template changes. Rebuilt
on `build_musthaveto.py` / `i18n_musthaveto.py`.

Also fixed along the way: gap-fills were compared with plain `===` (a known
defect class on this site — `mustn't` typed as `must not` scored wrong; both
now accepted via pipe-separated answers). The eight-question quiz reused the
same four options (must / have to / mustn't / don't have to) almost every
time, and `don't have to` — 13 characters against `must`'s 4 — was the
correct, uniquely-longest option in three of those items, which is exactly
the ANSWERS-gate defect class documented elsewhere in this file. Six MC
items now vary the option pool per question, each with a same-length-or-longer
plausible distractor. The static comparison table is now a six-pair match
activity instead — the same information, but answered rather than read.

Artwork: four flat-vector images from the shared `minecraft/` folder, none
of them claimed by Past Modals/Tense Review/Minecraft B1's dedicated
folders — `giant-golem-moonrise.jpg` (kept as the hero; it was the page's
original cover and already suits an obligation lesson), plus
`creeper-hillside-dusk.jpg`, `enderman-desert-landscape.jpg`,
`pig-creeper-building-hero.jpg`, copied into a new `MustHaveTo/` folder.
Accent rotated to creeper green (`--accent-hue=130`) — the honest derivation
is the same gold/amber Past Modals and Minecraft Editorial already use.

`library.html`'s `LESSON_IMAGES` entry and the block-camp hub thumbnail both
still point at `minecraft/giant-golem-moonrise.jpg` directly; untouched,
since the deck uses a copy of the same file rather than moving it.

---

## 2026-09-05 — Wonderland: The Stolen Now — a fifth RPG, on the same engine

The second export of the day — `Wonderland_The_Stolen_Now_Present_Continuous_V1 (2).html`,
7.5 MB, 34 pictures at 1536×864, Present Continuous, A1–A2. It reached the
session only as a chat attachment: Google Drive found it but the connector
dropped the connection three times on the size, and drive.google.com is
blocked by the sandbox proxy (now in CLAUDE.md, "Handing a file to a cloud
session").

**A different generator from the Oz one.** No `*_GAME_DATA` object; the
game is `const ACT_ONE = [q(...)]` tables in the script, with a two-blank
"cake" item (pink half = present continuous, blue half = present simple), a
repair-until-correct rule (10 points first try, a mistake explains and you
try again, 16 questions on any route, 160 points), two forks of two routes,
a boss round and a final decision with three endings (Restore → true ending
at 120+ points, hopeful below; Break → freedom). The export already had a
"time shard" glow-to-reveal and Monocraft — it had been through the "Font
styling for block camp RPGs" session earlier that day — but a fixed shard
position, not an object, and the standalone chrome.

Built as **`block-camp/wonderland-stolen-now-rpg.html`** on `rpg.py`, which
grew what the game needed and Oz did not: `repair` mode, a `total` progress
badge, split options with `tags`, `min`/`else` on a route, a per-scene
`button`, `img_w/img_h`, and a mistakes review on the ending (first-try
count, each repaired item with its rule). Options are now exempt from the
language check — they are the English being taught; a gloss is optional.
Oz rebuilt clean on the new engine (checked by screenshot).

What the export lacked and the page has: Spanish and German for all 24
question titles, prompts, explanations, kickers, route names and ending
labels (the export translated only the story lines and endings); a rules
briefing on the prologue plate; a hotspot on every one of the 35 scenes,
each checked closed. Wired in like Oz: hub plate (five adventures now, the
grid is `auto-fit`), library thumbnail, catalogue cache row, `seo.py` last —
additions only in the four indexes.

### To publish (Innes)

Same branch as Oz. After the merge is live:

```sql
insert into lessons (file, title, level, access, deck, video, sort_order) values
 ('block-camp/wonderland-stolen-now-rpg.html', 'Wonderland: The Stolen Now — Present Continuous Voxel RPG (A1-A2)', 'A1-A2', 'pro', false, false, 0);
```

---

## 2026-09-05 — The Lost Yellow Road: a fourth Block Camp RPG, and the RPG standard written down

Innes sent a standalone export — `Wizard_of_Oz_Past_Continuous_RPG_Sherpa_Yellow_Standalone_V1_4_fixedfont.html`,
4 MB, 23 pictures inlined, the game in `window.OZ_GAME_DATA` — with one
line: *"Text should be bigger and pop up when a glowing object is clicked,
you should save instructions for future to make these rpgs standard like the
others in Block Camp with Monocraft."*

Built to the standard his own Blocula rebuild set (`e6056ab`, object
hotspots): **`block-camp/lost-yellow-road-rpg.html`**, pictures in
`block-camp/lost-yellow-road-rpg/`. Past Continuous, A1–A2, EN + ES + DE,
27 scenes (cover, rules briefing, 18 questions, 3 route choices, 4 endings),
15 questions on any path, 75 points, 4 road tiles, 3 chances — the export's
scoring, unchanged. What changed:

- **Every scene has a glowing object; the text pops out of it.** Hotspots
  are in the builder's `HOT` table as % of the picture, picked from gridded
  contact sheets; every one was screenshotted closed and checked.
- **Type is Monocraft, both weights embedded (8 KB each), and a step bigger
  than Blocula** — story 1.65cqw / options 1.4cqw / title 3cqw on a 46%
  panel, against 1.36 / 1.04 / 3.6 on 42%. The export ran 15–17px Carlito.
- **A rules briefing** (five form cards + note) before the first question
  and **an explanation line under every answer**, both in three languages
  — the export had neither, and its chapter kickers were English-only in
  the ES/DE modes; translated.
- Dark glass panel, camp 4's `#F1D779` as the single accent, HUD, translate
  menu, fullscreen, keys 1–3 / L / F, corner help — the Blocula chrome.
- A portrait phone slides the picture so the hotspot stays on screen
  (Blocula centres the crop and can lose the object off the edge); an
  answered question scrolls its panel to the feedback and CONTINUE.

**The engine and the instructions are in the repo:**
`lesson-template/build/rpg/` — `rpg.py` (the page: CSS, engine, `assemble()`
with validation), `extract_standalone.py` (export → pictures + `data.json`),
`fonts/` (Monocraft subsets + the script that made them), and **`README.md`,
which is the standard**: what an RPG is, the pipeline, how to pick
hotspots, the Playwright check, publishing, the spec. The lesson's own
builder is `lesson-template/build/build_lost_yellow_road.py`; copy it for the
next export. A rebuild keeps the SEO block, and is byte-identical.

**On Monocraft:** the note above (2026-09-04, Past Perfect trio) records that
the camp decks and references run Pixelify Sans + Silkscreen and only the hub
uses Monocraft. Innes has now said the RPGs should be "with Monocraft", so
that is the RPG standard from here; it does not touch the decks, and the
three older RPGs (Pixelify Sans headings, Courier New body) are unchanged —
moving them onto `rpg.py` is a separate job, listed under Open.

**Wired in:** hub card (the Adventures section of
`block-camp-hub/build.py` is now an `ADVENTURES` table, counted like the
climb — "4 Adventures", "four branching adventures" — and the plates sit
2×2), `library.html` `LESSON_IMAGES` (`check-library.js --vs-origin`
passed), `tools/lessons.json` row, `seo.py` run last with the four-index
diff read: additions only. Pushed to `claude/glowing-object-text-popup-fxo141`.

### To publish (Innes)

Merge the branch. Then, **after** the page is live on `origin/main`:

```sql
insert into lessons (file, title, level, access, deck, video, sort_order) values
 ('block-camp/lost-yellow-road-rpg.html', 'The Lost Yellow Road — Past Continuous Voxel Oz RPG (A1-A2)', 'A1-A2', 'pro', false, false, 0);
```

`sort_order 0` puts it with the other three RPGs (−2, −1, 0) at the head of
the library; change it if the fourth should sit elsewhere. The cache row in
`tools/lessons.json` says the same and will be overwritten by the next
live `seo.py` run on your machine.

### Open

- **Move the three older RPGs onto `rpg.py`** so the line is uniform —
  Monocraft, one engine, one hotspot table each. Blocula already has its
  `HOT` table (frame-percent, 16:9 — convert to picture-percent); Last Train
  Home and Long Way Home have none and need the contact-sheet pass. Long
  Way Home also has a "codex" modal (narrative-tense reference) that the
  engine's `rules` kind covers.
- The engine embeds Latin + Cyrillic Monocraft only. An RPG with Arabic or
  CJK glosses needs a fallback face for those glyphs before it ships.

---

## 2026-09-05 — LEGO Prepositions & Phrasal Verbs, Part 2: rebuilt as a deck

Innes sent the URL for `forbes-english-lego-lesson-part2.html` — a five-tab
scrolling quiz, not a deck, and unrelated to the already-rebuilt Lego Car
Building pair (`forbes-lego-b2.html` / `forbes-lego-b2-part2.html`) despite
the similar filenames. Same house-style gap as both of those: 27 scored items
(6 MC, 5 fill-in-the-blank, 6 true/false, 5 matching, 5 error-correction) and
zero pre-teaching — every rule lived only in the per-answer feedback.

Rebuilt to a 27-slide deck (cover, 3 teach slides, then the five activities,
results, activate). All 27 items survive; nothing recounts, unlike the Lego
Car Building pair — this page's error-correction was already 4-option
multiple choice, so there was nothing to convert into gap rows. True/false
became six two-option MC slides (`options=['True','False']`, never
translated — see below); there is no dedicated true/false slide type.

New builder trio: `lesson-template/build/{build_legoprep2,legoprep2_data,
i18n_legoprep2}.py`. Hero and background are the lesson's own existing
`LegoPart2/lego-dice-brick.jpg` (cover) and `LegoPart2/lego-brick-wall.jpg`
(background swap on the teach/match/EC slides) — both already 1600×896, no
new artwork needed. Palette is `extract-palette.py`'s unedited output, dark
pink/red, every contrast row PASS. `library.html` needed no edit: the
existing `LegoPart2/lego-part2-thumb.jpg` thumbnail entry and card-title link
carried over untouched, and `tools/seo.py` reused them.

Ships en/de/es (the 2026-09-04 minimum), six-item teach cards. Checker is
fully clean: LAYOUT, ANSWERS, BANK, EXPLAIN, I18N, ACTIVATION, LOGO, HEAD,
ART, RUNTIME all PASS. Verified by screenshot at every activity type
(cover, teach ×3, MC, gap, true/false, match, error-correction, results,
activate) and with the language switched to German — nothing left in English
that shouldn't be.

`tools/seo.py` hit the cloud-session Supabase-unreachable fallback (see the
CLAUDE.md warning); diffed `lesson-meta.json` / `llms.txt` / `sitemap.xml`
before committing and confirmed the only changes were this lesson's own
description text and `lastmod` bumps — no other lesson dropped.

**Playwright had to be installed locally** (`npm install playwright
--no-save`) for `check-lesson.js` to run in this sandbox — it is gitignored
via `node_modules/`, so nothing to clean up.

**Still open:** Part 1 of this pair (`forbes-english-lego-lesson.html`, B1)
is the same old scrolling format and has not been touched — its
`library.html` thumbnail is also currently `lego/lego-b2-scene-a.jpg`, art
that belongs to the unrelated Lego Car Building deck, worth fixing whenever
Part 1 is rebuilt.

---

## 2026-09-04 — Block Camp hub remade dark (pushed, live on origin/main)

Innes: "remake block camp hub so it looks snazzy", direction chosen: dark and
immersive. `block-camp.html` is now the one page in the line that matches the
maps and the RPGs instead of the library's cream. The nav band and the fenced
SEO block are byte-identical to before; everything below the band is new.

What the page does now:

- The route map's own resting plate (tent, bridge, lookout tower) full-bleed
  behind the title, as a new file **`BlockCamp/hub-hero.jpg`** (159 KB, the
  1600x900 scene that was only ever inlined inside `block-camp-map.html`).
  Left-and-bottom gradient overlay on desktop; near-solid overlay on phones,
  where there is no "left side" to hide the copy on.
- A tally strip (16 units · 8 stations · 3 adventures · 8 references) sitting
  on the hero's bottom edge, each tile an anchor to its section.
- Every climb and descent card wears its camp's colour — the same eight as
  the map's stops (`#7A93B5 #E66085 #B08968 #F1D779 #70A43A #F0723F #2E7D65
  #46B0AB`) — as a 3px top stripe, a numbered badge and the Part/Station
  label. The badge sits BESIDE the title, not on the cover: every cover
  carries its own title top-left and a badge there hid the first letter.
  References use the same colours by tense; the Trial and the adventures
  are gold.
- Pro chips carry a padlock (matching the map's paid-link convention); Free
  chips are solid gold. Both map links are wide image strips. The three RPGs
  are three plates in a row rather than a list.
- Copy corrected: "two adventures" → three. Playfair Display dropped from the
  font request (nothing used it any more); Monocraft stays for h1/h2 only.

**The builder is in the repo this time:**
`lesson-template/build/block-camp-hub/` — `build.py` (card data + assembly),
`template.html`, and `seo.html` / `nav.html` / `monocraft.css` lifted
verbatim so those stay stable. Run `python3
lesson-template/build/block-camp-hub/build.py` from the repo root; it writes
`block-camp.html` and a downscaled self-contained preview to `$PREVIEW_DIR`
(default `/tmp`). Edit the data tables, not the HTML. **If `seo.py` ever
rewrites the hub's SEO block, copy it back into `seo.html` or the next build
reverts it.**

Verified in the sandbox: every `href`/`src`/`url()` on the page resolves to a
file in the repo; screenshots at 1280 and 390 wide; the top band unchanged.
`seo.py` was NOT run — nothing it writes changed, and a cloud run against the
stale `tools/lessons.json` cache is the documented way to lose entries.

**Applied and pushed** by a cloud session on 2026-09-04, following
`docs/HANDOFF-block-camp-hub.md`: bundle verified, fast-forwarded onto
`origin/main` (0906b02), all checks in the handoff re-run and passing
(missing refs: none; SEO/nav bands untouched; builder reproduces the
committed page byte-for-byte), pushed as `2c7cf4e`. The live-site fetch
check in that handoff's step 3 could not be run from this sandbox (egress
policy blocks `forbesenglish.com`) — someone with unrestricted network
should confirm `https://forbesenglish.com/block-camp.html` and
`https://forbesenglish.com/BlockCamp/hub-hero.jpg` load, per that doc.

**The Past Perfect trio landed right after this, same session.** The
`past-perfect-camp` bundle (see the section below) arrived and was merged
into `main` here: `block-camp.html` conflicted exactly as anticipated, and
was resolved by taking this hub's side and re-running
`lesson-template/build/block-camp-hub/build.py` — `grep -c 'Past Perfect
Passive' block-camp.html` → 1, `grep -c '>17<'` → 2, both confirmed after the
rebuild. The three cards (camp 9, station 17, the ninth reference) are in the
hub now; the tally strip and closing count read 17/9/9 without anyone
editing a number, exactly as designed below.

**It collided with the Past Perfect trio** (branch `past-perfect-camp`, its
own bundle — see `claude/past-perfect-camp-build.md`), as expected: that
branch's `block-camp.html` still targeted the OLD hub markup. Resolved by
taking THIS hub's version of `block-camp.html` and re-running the builder —
no hand-merging the three `<li>` cards, they carried the old classes and
would have rendered unstyled. Its data tables already list camp 9
(`#d66d77`, the deck's own ink), station 17 and the ninth reference, and
each card is emitted only when its page exists in the repo — tested both
ways in the sandbox, then for real.

Not done, deliberately, and worth asking Innes about: the eight "More
Minecraft Lessons" cards are the weakest artwork on the page (older heroes,
mixed aspect ratios); a parallax or lantern glint on the hero was offered but
not built. Both are small, incremental steps if he wants them.

**Dracula is done** — already uploaded and published as *Blocula*
(`2b42dc1` and earlier, on `origin/main`); no action needed.

---

## 2026-09-04 — Camp 9 / Station 17 / the ninth reference: the Past Perfect, and a builder for new camps

Innes sent a 41-slide "Past Perfect · The Maroon Memory Vault" deck (a CSS-only
radio deck, his own artwork, ES/DE, ten "memory shard" questions) and asked for
it to become an active camp, a passive station and a 41-page reference for
Block Camp. Three pages, all in this branch, none pushed — `git push` is
refused from the sandbox, so they went to him as a bundle
(`past-perfect-camp.bundle`).

**Applied, merged and pushed** by a later cloud session, same day: the bundle
merged onto `main` (which by then had the dark hub — see the section above)
as `1b56f8c`, with the anticipated `block-camp.html` conflict resolved
exactly as documented (hub side + rebuild). `check-lesson.js`,
`overflow-langs.js` and `check-colour-roles.py` all pass clean on
`blockcamp-past-perfect.html` and `blockcamp-passive-past-perfect.html`;
`check-library.js --vs-origin` passes (the one WARN — card ≠ hero — is
pre-existing across the whole Block Camp line, not new here); `seo.py
--check` reported zero rewrites needed, so it was not run for real (same
stale-cache risk as always in a cloud sandbox). The three Supabase rows
below were inserted after the push, confirmed present with no prior
duplicates. Route maps still don't know camp 9 / station 17 (see Open,
below) — untouched, as that was explicitly out of scope for this bundle.

| page | what | built by |
|---|---|---|
| `blockcamp-past-perfect.html` | **9. Past Perfect — Part 1** (B1, 22 slides, 28 pts, EN/DE/ES) | `lesson-template/camp/build_camp.py 9` ← `camp09.py` |
| `blockcamp-passive-past-perfect.html` | **17. Past Perfect Passive** (B1, 22 slides, 27 pts) | `lesson-template/descent/build_descent.py 17` ← `station17.py` |
| `past-perfect-time-signals.html` | **Past Perfect: Time Signals (Minecraft ed.)** — 41 scenes + 10 shard checks | `lesson-template/camp/build_reference.py` |

Artwork: `past-perfect-time-signals/bg01–41.jpg`, the Vault's scenes resized
1536×864 → 1280×720 (the family size). Cards: `BlockCamp/past-perfect-1a.jpg`,
`BlockCamp/passive-17-past-perfect.jpg`. Hub, `library.html` LESSON_IMAGES,
`tools/lessons.json`, sitemap/llms/lesson-meta all carry the three.

**Numbering.** Innes chose "append": camp 9 after Present Perfect Continuous in
the climb, station 17 after The Trial in the descent — station N still mirrors
camp N−8, nothing existing renumbers. `block-camp.html` prose says nine tenses /
seventeen units / nine stations / nine references now.

**Font.** The Vault embedded a 101-glyph font named "Minecraft Regular" (not
Monocraft) with a broken capital A and no accents — every ES/DE line and the
"meaning" rows fell back to Arial. Asked whether the trio should go to
Monocraft, Innes said *"change to Monocraft if that is the one used in Block
Camp by all the others"*. It is not: all 24 camp decks and the six references
run in embedded Pixelify Sans + Silkscreen; Monocraft is only on the hub and
route-map headings. So the trio matches the line. The real Monocraft v4 (OFL,
all weights, full Latin) was fetched and sits at `/home/claude/pp/Monocraft.ttc`
in the sandbox only — not needed, not committed.

### `lesson-template/camp/build_camp.py` — the climb has a builder again

The Part I generator was lost with a sandbox; `blockcamp-status.md` rightly
says the published HTML is the source of truth for camps 1–8. A NEW camp still
has to come from somewhere, so this does for the climb what `build_descent.py`
does for the descent: takes a published deck as chassis (shell, fonts, engine,
chrome strings) and replaces slides, palette, tense tokens, cover, dictionary,
`BW_TR`, part link, SEO block. Three things it learned that a future camp spec
should know:

1. **`UI_I18N` in a chassis holds the LESSON in ten languages.** Keep any
   lesson key and a learner who picks Français gets the past simple's cover
   on a past perfect deck. Every non-chrome key is dropped from every language,
   the spec supplies en/de/es, and fr..ja are **emptied, not trimmed** —
   `check-lesson.js`'s I18N gate fails a partial dictionary (33/106), while
   `initLang()` simply hides an empty one from the menu.
2. **A brand-new deck has no catalogue row, so `seo.py` skips it and the HEAD
   gate fails.** `build_camp.seo()` writes the block from `seo.py`'s own
   functions against the row the deck WILL have (`spec['row']`, `spec['card']`).
   `build_descent.py` and `build_reference.py` call the same function. When the
   row exists, `seo.py`'s normal run overwrites it with an identical block.
3. **The past perfect's ink.** `--t-past-perfect: #6E0B24` is kept at the
   route-map value for the TOKENS gate and measures 1.5:1 on the surface;
   `--t-past-perfect-ink: #d66d77` is L* 23 → 59 in Lab with hue/chroma held,
   the first step clearing 5:1. Class `.t-ppf`; participles `.pp` purple; the
   LATER action in every sentence keeps the past simple's `--t-past-ink`
   brown, so the two pasts sit side by side in two colours. `check-colour-
   roles.py`'s `AUXC` and `build_descent.py`'s `AUX_TENSE` both know `t-ppf`.

Layout lessons from this deck, all in the spec now: a one-line title is capped
at GERMAN length ("Welches Wort passt?" not "…legt die Reihenfolge fest?"); a
gap slide with a word bank, a hint and three glossed rows is the tightest slide
in the line — the hint folded into the bank row, rows at 9px padding, 150px
inputs, and stems short enough not to wrap at the checker's 1400px viewport
(a `.dim` label pushed `.q-stem` to 70px there while it looked fine at 1280);
a 6-pair match with DE glosses runs 14px into the deck bar — five pairs.

### `build_descent.py` learned three things for station 17

- `AUX_TENSE['t-ppf']` = had / had been / hadn't / hadn't been. **A bare
  'been' is written with its class in the station spec**, not as
  `class="aux"`: `tense_in_situ()` paints any lone 'been' the present
  perfect's turquoise, which was right while every lone 'been' on the descent
  belonged to 'has been'. 'Had it been locked?' is the first that does not.
- `STATION['tr']` replaces `BW_TR` wholesale. The chassis dictionary is the
  camp's, so the EN/DE panel on the eight existing stations covers almost
  none of their own stems and options (7 and 15 strings of 86 and 88 on the
  two worst — the panel's `glossRows` rescue only reaches slides with a
  `.sup`). Station 17 authors its own 70-row table. The other eight could.
- `STATION['row']` / `['card']` → the SEO block, as above.

### `build_reference.py` — the family finally has a builder

Takes `past-simple-time-signals.html` as the shell (fonts, stylesheet, chrome,
script verbatim), swaps the six colour slots, and fills 41 sections from
`reference-content.json` (kicker / title / meaning / example / FORM / YOUR TURN,
EN+ES+DE) and `reference-quiz.json`. The family had no interaction; the ten
shard slides are click-once buttons with a `SHARDS n / 10` counter in the nav
bar (`QUIZ_CSS` / `QUIZ_JS`). Measured to fit the 1080px canvas in EN, DE and
ES with the last element's bottom — the family's `check-lesson.js` gates do not
apply to these pages (no activate stage, no `UI_I18N`, no lockup, by design).
Keep the SEO fence EMPTY rather than removing it: the family head carries four
hand-written `og:` tags after `<title>`, and `seo.inject()` refuses an
unfenced page that has any.

### To publish (Innes, on his machine)

```
git fetch ~/Downloads/past-perfect-camp.bundle past-perfect-camp:incoming
git merge incoming            # four commits on aa77a0a; touches no shared file but hub/library/lessons.json/seo outputs
git push
```

Then the three Supabase rows — **after** the push, not before (a row whose
page 404s puts a dead card in the live library; see forbes-english-blockworld
memory, 2026-08-27):

```sql
insert into lessons (file, title, level, access, deck, video) values
 ('blockcamp-past-perfect.html',         'Block Camp — Past Perfect 1a: The Earlier Past',     'B1', 'pro', true,  false),
 ('blockcamp-passive-past-perfect.html', 'Block Camp II — Passive 17: Past Perfect Passive',   'B1', 'pro', true,  false),
 ('past-perfect-time-signals.html',      'Past Perfect: Time Signals (Minecraft ed.)',          'B1', 'pro', false, false);
```

### Open

- **Part 2 of camp 9** (PPF3–PPF5: backshift, third conditional, wish) —
  the cover's `partLink` points at the route map until it exists.
- **The route maps now know camp 9 / station 17 — as far as the art allows.**
  A later cloud session added both to the climb page's accessible "every
  camp" list and its narrow-viewport station nav (correct hrefs, maroon
  `#6E0B24`, no fabricated Part 2 link for camp 9), and fixed every hardcoded
  count that was still saying "eight" (both maps' pills, the climb list's
  lesson-toggle total, the hub's two hand-written "eight tenses" lines — now
  driven by a computed `{{W_TENSES}}` in `build_camp_hub/build.py` instead of
  a literal string).
  **Update: both pins landed, no new art needed after all.** A later
  session found the room this one missed — camp 9 sits on TOP of the
  existing lookout tower (the trail's short new spur climbs the tower
  itself, not the ground beyond it: `#6E0B24`, "The lookout · looking
  back"), and station 17 extends the descent's route line past the canyon
  rim into the sky at the frame's edge, reading as the path continuing out
  of view. Same source images as before, no commission needed. The SVG
  route paths on both maps were extended with real bezier segments (not
  just a floating dot), the descent's interactive panel/progress-bar JS had
  its hardcoded `8`/`7` limits generalized to `nodes.length` so it isn't
  the next place someone forgets the count changed, and the descent's
  milestone fractions were re-measured off the actual SVG path length
  (`getPointAtLength`) instead of hand-typed guesses. Merged as `6a4248a`.

  One more thing this surfaced: the hub's own copy called the descent "the
  same trail back down" in three places, which was never true — it's a
  second trail on the far side of the watchtower, a different valley, not
  the climb retraced. Innes caught it; fixed in `334bdad` (also replaced a
  fourth hardcoded "eight stations" with the existing `{{W_DESCENT}}`
  placeholder while in there).
- `library.html`'s Tenses category regex: check that "past perfect" lands in
  Tenses (the doc for the family flags the same gap for every new tense).
- The eight older stations could take a `tr` table each now that the builder
  accepts one.

## 2026-09-04 — Harari at Davos: the deck tested a text it never showed

Innes: "this is difficult to follow." It was. The 24-slide deck had condensed
the reading into six slides of commentary and then asked ten comprehension
items about moments — the autocomplete move, the cow, Vortigern, the last
line — that appeared on no slide. Anyone who had not watched the session was
guessing from the options.

Rebuilt from the same builder, now 26 slides, EN + DE + ES:

- **Five excerpt slides**, each directly before the questions that use it, so
  the order is excerpt → concept → question. Quotations are verbatim from the
  prepared address; Innes pasted its auto-captions mid-session and every line
  was checked against them. Two corrections to the online transcript came out
  of that: "rivers and **gods**", not "guards", and the "learns to lie" line is
  in the address, not the dialogue. The Tracey dialogue has no reachable
  transcript, so Vortigern and the athletics exchange are marked summaries.
- **The reporting verbs are practised before the writing task** — a three-gap
  slide (`notes / contends / concedes`, one per category) — which the deck had
  declared as its skill and never exercised.
- Ten MC → eight, three transcript gap slides → one, the learner-facing
  "Not asked in the source lesson" kicker removed, `ctx` lines dropped (they
  were the 11px overflow on every question slide).
- Rule-bearing teach cards moved to the six-item form so DE/ES translate the
  body; quotation and example cards stay five-item on purpose.

**Two things learned about the machinery:**

- A gap row reserves 44px for its hidden `.feedback` (min-height 26 + margin
  18) whether or not it ever shows. Three rows fit; a fourth overflows by ~30px
  no matter how short the sentences are. Plan gap slides at three rows.
- `check-lesson.js` LOGO fails on **every** deck on Innes's Windows machine
  (188 vs 180px, 4.4%) — verified on `tense-review-minecraft.html`, which is
  clean. It is font metrics on this PC, not the deck. Ignore it here; it passes
  in the sandbox.

`lesson-template/checker/overflow-langs.js` was what caught the DE activation
slide at +5px; the English checker cannot see that. Run it on anything
multilingual.

---

## 2026-09-04 — the Spanish minimum, five decks, and a live defect on 31 pages

Overnight session. Innes was awake for the first part and asleep for the
rest; everything below is on `origin/main` and live.

### Spanish is now a floor, not an option

**"Must have Spanish and German at least."** Every deck ships EN + DE + ES
from here. `assemble()` still defaults to `('en', 'de')`, so the builder has
to pass `langs=('en', 'de', 'es')` explicitly — that is the whole change, and
it is easy to forget because nothing fails without it. The rule is in
`CLAUDE.md` under Standing constraints now.

Three decks that had already shipped EN+DE were retrofitted and republished:
Past Modals in Minecraft, Dino-Craft Part 0, Advanced Dinosaur Facts.

Write teach cards in the **six-item form** when you add a language. The
five-item form leaves the body in English, which produces a translated
heading over an English rule — the half-finished screen §8 exists to
prevent. It is invisible to every gate; the only way to catch it is to
screenshot the non-English build.

### Every writing box on 31 decks printed `&hellip;` literally

`actPlaceholder` reaches the page as a `placeholder` attribute, set from JS
through `data-i18n-ph`. **An attribute assigned from JS never parses
entities.** Every Block Camp deck had been showing `Yesterday I&hellip;` in
its writing box, in every language, since it shipped — twenty-four of them,
plus seven others.

Nothing was wrong with the builders: every other string on a slide is HTML,
so writing `&hellip;` is the correct habit. The fix is central and already
in:

- `deck.py` has `TEXT_ONLY_KEYS` and `as_text()`; `activate()` and
  `assemble()` unescape those values on the way out. **Keep writing entities
  in builders.** They come out right.
- `check-lesson.js`'s ENTITIES gate now covers `actPlaceholder` as well as
  the four textContent keys, and reads the authored `placeholder="…"` in the
  markup too.

**The twenty-four Block Camp decks have no builder in this repo.** Grep found
none — `build_camp5.py` and `build_camp7.py` are something else. They were
edited in place, which is the one case where hand-editing generated HTML
survives, because there is no next run. If those builders ever land, re-run
them against the current `deck.py` and the fix comes back on its own.

**Two decks are behind the template.** `forbes-english-lesson-2.html` and
`reading-the-elevation-c1.html` both have builders, but re-running them pulls
in template CSS added since they were last built — 1190 and 141 lines, mostly
the exam-style audio player. Harmless, but it is a separate change and wants
a look before it ships. They were edited in place instead.

### Ten decks rebuilt

| Was | Now | Scored | Notes |
|---|---|---|---|
| `tense-review-minecraft.html` | 21 slides, light | 30 | |
| `nietzsche-film-vocab-c1-part5.html` | 21 slides | 15 | first Nietzsche deck |
| `forbes-english-present-perfect-lego-b1.html` | 24 slides, light | 26 | |
| `forbes-english-lego-passive-active.html` | 19 slides | 20 | |
| `forbes-lego-b2.html` | 17 slides | 15 | Part I of a pair |
| `forbes-lego-b2-part2.html` | 15 slides | 20 | Part II; was 15, see below |
| `forbes-english-minecraft-b1.html` | 20 slides | 26 | |
| `forbes-english-minecraft-c1.html` | 23 slides | 26 | |
| `forbes-english-minecraft-editorial.html` | 23 slides | 32 | |
| plus the three Spanish retrofits | | | |

Every one exits `check-lesson.js` clean, has no overflow in any of the three
languages (checked at 1280×720 with a headless pass, not by eye), and has
`deck = true` on its Supabase row.

The Lego B2 pair's score went from 15 to 20 because the deck engine counts
both blanks of a two-fault error-correction sentence where the old page
counted the pair as one point. That is the more honest number and nothing on
the page claims otherwise.

New artwork folder: `TenseReview/` — five flat-vector Minecraft scenes from
Downloads, cream and dusty pink, deliberately unlike the Past Modals set so
the two Minecraft decks do not read as one deck twice.

### Defects worth recognising again

Every one of these turned up in more than one lesson tonight.

- **The key was the longest option because the answer was the longest tense
  name.** Four of six on Tense Review, four of seven on the Lego passive.
  The fix is a fourth option at least as long as the key, and it has to be a
  real error, not padding.
- **A key sequence that repeats.** Nietzsche Part V ran `c, b, d, a` from
  question five to the end — and Part IV of the same series carries the
  identical sequence character for character, because they are one build
  re-skinned. `check-lesson.js` catches clustering, not periodicity.
- **A rubric that promises something the items do not deliver.** Tense
  Review's error-correction section said every sentence contained one error;
  item five contained none, and the feedback said so. A learner who trusted
  the rubric lost the point for being right.
- **An item keyed against its own stem.** Nietzsche Q6 gave the definition of
  *unprecedented* and marked *groundbreaking* correct.
- **A "matching" activity whose right-hand column holds two values.** That is
  a sort, and `match()` cannot pair six terms to two definitions. Both Lego
  pages had one.
- **Gap-fills compared with `===`.** `'ve finished` marked wrong on a B1
  lesson. Pipe-separate every reasonable contraction and spelling.

### The artwork shortage, resolved

**Fixed on 2026-09-04.** The shortage was in `minecraft/`, which is exhausted
— every flat-vector illustration there is the hero or a background of Past
Modals, Tense Review, Minecraft B1 or Minecraft C1. But Innes's Downloads
holds a large set of the same flat-vector family under names that do not say
"minecraft" first: the `*_award_winning_beautiful_minimalist_*`,
`*_Cube_pixel_art_minimalist_vector_*` and `*_Noma_Bar_style_*` batches. Search
Downloads by *style* words, not by subject, and there is plenty left.

What that gave the two decks that were on stopgaps:

- **`MinecraftB1/`** is now `hero.jpg` (a blocky figure and a bicycle under a
  wide pastel sky), `reef.jpg` (underwater, turtle, a block dissolving) and
  `grove.jpg` (a tall blue mob in coral scrub). The palette is
  `extract-palette.py --light --accent-hue=340 --accent-sat=0.65`. The accent
  is rotated because the honest derivation of that hero returns Tense Review's
  warm sand almost exactly, and two decks cannot share a palette and still
  read as two decks. The three rendered in-game scenes it used to carry
  (`temple.jpg`, `rex.jpg`) are retired.
- **`MinecraftEd/`** exists for the first time: `hero.jpg` (a blocky figure
  over a moonlit city), `ridge.jpg` (a dusk ridge, figures walking under
  poplars), `dusk.jpg` (a lone figure on a rise at sunset). Dark, cool,
  derived unrotated. The Trivia deck no longer borrows B1's folder.
- **Minecraft C1** is unchanged — three voxel studies in `MinecraftC1/`, accent
  rotated to teal.

**`MinecraftB1/temple.jpg` and `MinecraftB1/rex.jpg` removed 2026-09-05** —
`git rm`, actually pushed this time. Nothing referenced them.

### Minecraft C1's "voxel studies" were the wrong art, fixed 2026-09-05

Innes flagged it directly: new Minecraft art existed but wasn't in any deck,
and some of what *was* live "wasn't very Minecraft." Investigation confirmed
both halves.

**The repeat pattern is structural.** Every one of the three live Minecraft
decks (B1, C1, Ed) drew backgrounds from a 3-image folder, cycled twice across
six activity slides (`[a, b, c, a, b, c]`). The 2026-09-04 note above already
flagged this for C1 ("a fourth would help") but didn't fix it.

**C1's `hero.jpg` and `warrior.jpg` were not Minecraft at all.** They were
photoreal voxel-diorama renders of a classical Greek/Trojan warrior — a
Corinthian-style helmet, a shield with a ship emblem, bokeh-blurred ruins —
described in the builder's own docstring as "a voxel Odysseus for the cover."
That was apparently deliberate at the time, but it doesn't match the site's
flat-vector house style and Innes doesn't want it. Only `creatures.jpg` (a
genuine flat-vector Minecraft mob collage) was actually right.

**Fixed:** `MinecraftC1/hero.jpg` and `warrior.jpg` replaced with flat-vector
Minecraft art (a player on a cliff at sunset; a creeper-and-skeleton night
confrontation), plus a fourth image, `structure.jpg`. `MinecraftB1/` also
got a fourth, `village.jpg`. `MinecraftEd/` got a fourth too, `city.jpg`
(2026-09-06, a blocky figure on a ruined city street under a moon, same cool
nocturnal register as its other three). All three builders' `*_BG` lists now
spread four images across the slide count instead of cycling three twice;
`build_mcc1.py`, `build_mcb1.py` and `build_mced.py` docstrings carry the
detail.

**Same audit widened, 2026-09-06.** Innes asked about "these lessons" more
broadly; a scan of every `*_BG` list across all builders found `PastModals`
and `TenseReview` in the same thin state (3-4 images stretched over 5-6
slides). `TenseReview` already uses its 4 non-hero images efficiently enough
(only 2 repeats across 6 slots) to leave alone. **`PastModals` still needs a
fourth image** — only 3 activity backgrounds (`dusk.jpg`, `enderman.jpg`,
`golem.jpg`), `hero.jpg` held back for the cover — and two upload attempts for
it have both missed: the first landed nothing in `PastModals/`, the second
put two candidates in the repo root but they were painterly digital-art
renders (visible brushwork, atmospheric gradients) against a canyon, not the
flat hard-edged silhouette style `PastModals/hero.jpg` actually uses. Subject
matched, medium didn't — same lesson `MinecraftC1` already taught once with
the "voxel Odysseus." Don't accept a new image on subject match alone; open
it and compare rendering style against the folder's existing files.

**Delivery note for next time:** getting art from a chat-pasted image into
the repo doesn't work — a cloud session has no filesystem path to an inline
image, no matter how many are pasted. What worked: Innes saved the Midjourney
exports as JPG (GitHub's web uploader caps drag-and-drop at 25MB/file, well
under git's own 100MB limit, so raw PNG upscales need converting/downsizing
first) and used the web uploader — but pointed at the **repo root**, not the
target subfolder, landing all seven files as `blackisler_<prompt-text>_<seed>_<n>.jpg`
at `/`. A session with push access then had to `git checkout origin/main --
<file>` to pull them onto disk, sort them by content (not filename — the
prompt text names don't tell you which variant, of several near-duplicate
renders per prompt, actually reads as the intended composition), rename to
what the builder expects, and `git rm` the unused variants and the two wrong
old files.

**Do not use the three Twin Peaks images in `minecraft/`.** They are a
recognisable homage — the Red Room, identifiable characters, and a "Welcome
to Twin Peaks" sign legible in the corner of the widest one. Cropping the
sign does not fix what the rest of the frame is, and it is not going on a
published lesson cover. Likewise the `minecraft_lego_from_another_planet`
sets: voxel character line-ups with weapons and blood, not for a B1 class.

### Two decks now share a builder pattern worth copying

`build_mcc1.py` and `build_mced.py` both take a single `MC` list and split it
across two activities with different eyebrows, by slicing:

```python
+ "".join(D.mc(i + 1, 6, MC[i], 'mcEyebrow', 'Activity 1 · Register', ...)
          for i in range(6))
+ "".join(D.mc(i + 1, 6, MC[6 + i], 'dndEyebrow', 'Activity 2 · Collocation', ...)
          for i in range(6))
```

That is how a page's "drag and drop" activity becomes multiple choice without
merging it into activity one. Both pages had authored four candidate answers
per sentence and then poured the private pools into one shared tray; the
chips were a presentation, and each item was always four options against one
stem.

### Still open

- **Polish, resolved for one of the two pages.** `must-have-to-lego-polish.html`
  and `minecraft-lesson.html` both carried Polish as their only L1 support.
  Innes decided, 2026-09-06: standard EN + DE + ES like every other deck,
  Polish dropped, no changes to `chrome_i18n.py` or the template's `LANGS`.
  `minecraft-lesson.html` is rebuilt on that basis — see below.
  `must-have-to-lego-polish.html` is still open and still carries the
  stronger case for keeping Polish (best pre-teaching of any Lego page, a
  complete ten-language `UI_I18N` of its own) — this decision was made
  per-page, not site-wide, so don't assume it extends there without asking
  again.
- Two live scoring bugs on `must-have-to-lego-polish.html`, which is still
  the scrolling page: `checkFill()` selects all ten `input.fi` on the page,
  so Exercise 1's Check button scores and reveals Exercise 4's four answers
  before the learner sees them; and the results panel never opens, because
  `tick()` waits for 19 answers and only 18 exist.
- `sort_order` is null across the Dino-Craft series, so Part 0 does not sit
  ahead of Parts I and II.
- Tidy-up needing a session that can `git rm`: `Football/stadium-silhouette.jpg`,
  `minecraft/Skeletal_Dinosaur.webp`, four `minecraft/blackisler_*.png`.
- Whether the grey `--void` should move into `lesson-template.html` and
  `extract-palette.py` rather than being lifted per lesson. Ten builders now
  carry the same comment saying a re-derivation will put the black back.
- `forbes-english-minecraft-editorial.html` has three content problems the
  format could not fix: its matching activity restates the keys of questions
  one, three and five almost verbatim, so a learner who did activity one gets
  three of seven free; the cats explanation is circular; and the sand
  explanation invents a floor-check mechanic the game does not have.
- `forbes-english-minecraft-c1.html` question three has a defensible second
  answer, which its own explanation concedes, and question twelve's *seized
  upon* collocates perfectly well with *potential*. Both want a rewritten
  stem rather than a re-key.
- **Four decks fail the new short-key check and were not fixed.** The
  ANSWERS gate now catches a key that is conspicuously *shorter* than its
  distractors as well as longer — `alchemist_b2_lesson.html` (22 characters
  against 35), `carrying-the-load-c1.html` (28 against 74),
  `forbes-conservation-c1.html` (three items, up to 70 against 134) and
  `forbes-nature-agency-part1.html` (four items, up to 29 against 64). Each
  wants the distractors tightened, which is content work, not a re-key.

  The thresholds are deliberately stricter than the long case: 1.5x and ten
  characters, against 1.10x and four. Being the shortest of four happens by
  chance far more often than being conspicuously the longest, and at the long
  case's numbers this fired on 35 of the 105 decks — almost all of them
  closed sets where length carries nothing, like a preposition item keying
  *at* against *from*. The calibration is written into the comment beside
  the check.

### The Lego and Nietzsche queues, audited

Both families were audited in full. The findings that change what you build:

**Nietzsche (six pages).** Parts IV and V are one build re-skinned; Parts I
and II likewise. Part I is A2–B1 content labelled C1 in the title, the schema
and the library — either re-level it honestly or fold it into Part II.
`nietzsche-grammar-test-part4.html` is named grammar and contains film
vocabulary. Part III's question 15 is unanswerable as printed: the error it
asks for sits in a span that is not underlined. `forbes-nietzsche-c1.html` is
the richest page of the six and the natural anchor, but its engine writes
options in fixed order and the key is at index 1 in thirteen of seventeen
questions — always pressing B scores 13/17.

**Lego (nine pages).** No two are duplicates; the question sets are disjoint.
But three separate B2 lessons teach the same car-vocabulary field —
`forbes-english-b2-lego-cars.html`, `forbes-lego-b2` + part 2, and
`forbes-english-skyline-lego-b2.html` — 67 scored items over one word list,
with *prototype* a scored answer in all three. `forbes-english-b2-lego-cars`
is the weakest of the three and the candidate to retire: eight of its
twenty-six keys are the longest option, including four of six reading items
at +11 to +31 characters, which makes that section scorable without reading
the passage. Salvage its reading text ("From Baseplate to Bugatti") into the
`forbes-lego-b2` pair first. `forbes-english-skyline-lego-b2.html` has four
content errors including an option (*ensure*) that does not appear in its own
sentence, and fifteen of its twenty-six items have no explanation.

---

## 2026-09-03 — three duplicate lessons merged, two of them then rebuilt as decks

Started as a full house-style audit of the catalogue and turned into two
lessons. Both halves are worth carrying forward.

### The audit

All **93 deck files exit `check-lesson.js` clean** — twelve gates, zero
failures. The only file that fails is `lesson-template.html`, which is the
placeholder title and expected.

**145 catalogued lessons are still scrolling pages.** That is after excluding
every family that is deliberately not a deck: Sherpa Tensing, Sailing the Seas,
the time-signals pages, the `.pptx` deck-viewers, the block-camp RPGs and the
three IELTS scrolling pages. Grouped by whether artwork exists:

| | |
|---|---|
| artwork on disk, convertible today with nothing commissioned | **77** |
| art exists but is a 1200px library card, under the §3 hero minimum | **22** |
| no artwork at all | **46** |

The 77 cluster into families that share one artwork set — `minecraft/` covers
nine lessons, `Nietzsche/` six, `lego/` six, then pairs for Ecuador, Football,
Skiing, Tennis, Top Gear, Water Polo, Fire Brigade, fashion and Animal Welfare.
Converting by family is much cheaper than converting by date.

### Three lessons were in the catalogue twice

Same shape each time: an original, then a later **re-skin** of it filed under a
second `pro` row. Measured by diffing the question data, not by filename.

| Survivor | Retired | Row |
|---|---|---|
| `forbes-english-meetings.html` (48) | `forbes-english-ope- say in your words.html` | 54 |
| `-dinosaurs C1.html` (7) | `forbes-english-lesson (dinosoausrs c1).html` | 40 |
| `forbes-english-football-b1.html` (125) | `forbes-english-football-b1-argentina.html` | 126 |

Football's `questions` array was **byte-identical** across both files; the
dinosaur pair's `SECTIONS` differed by a single apostrophe escape; the
open-answer pair differed on six lines, all metadata.

**The re-skin is always the better build, and that is the thing to notice.**
Both re-skins had been given real artwork and a better mechanic while the
original kept emoji placeholders — Dino-Craft replaced two 🦕 with 3376×1440
illustrations, the Argentina edition added a rotating per-question background
photo. Deciding by filename or by which row is older throws that away. Diff the
question data first: if it is identical, the question is which one *looks*
better, not which one is canonical.

Retired files became **~950-byte redirect stubs** (meta refresh +
`location.replace`, canonical at the survivor, `robots: noindex, follow`),
following the `full_grammar_test` precedent. `seo.py` correctly refuses to
fence them and reports them as hand-written SEO — that warning is expected and
should be left alone. They also drop out of the sitemap, `llms.txt` and the
crawlable index, because removing their `LESSON_IMAGES` entry makes them read
as "coming soon". Right outcome, slightly indirect reason.

**`docs/HERO-QUEUE.md` is wrong about the dinosaur cluster.** It records a
"three-file cluster at 0.80–0.88" including `forbes-english-dinosaur-minecraft`.
Re-measured: the pair scores **0.92** against each other, **0.07** against
Dino-Craft Part I and 0.06 against `forbes-english-dinosaurs.html`. Three
separate lessons; only the pair is a duplicate. Following that note would have
merged two lessons that are not duplicates.

### Then the survivors were rebuilt as decks

A merge that leaves a scrolling page has not brought the lesson up to house
style — rule 1 and §10. Both convertible survivors now go through the template
and exit clean:

* **`-dinosaurs C1.html`** — 23 slides, 25 scored, EN+DE, `DinoCraft0/`.
  Renamed **Dino-Craft Part 0: The Briefing** at Innes's call: it is five
  activity types with no teaching, which is a placement test, and it belongs
  before Part I rather than beside it with a colliding name.
* **`forbes-english-football-b1.html`** — 21 slides, 14 scored, **EN+DE+ES**,
  `FootballB1/`, light palette. Spanish ships complete because the old page
  carried a Spanish gloss on every item; explanations are `UI_I18N` keys so
  the gloss lands in the Spanish build only.

Defects the rebuild removed, all of them the recurring pattern:
**every one of football's fourteen keys was at index 0**; four of five dinosaur
keys at index 1; the dinosaur **word bank listed all five answers in gap
order**; one explanation named its option by letter; ten items had no
explanation of their own; and **neither lesson taught anything** — every rule
lived only in post-answer feedback. Three teaching slides now open each deck.

**Teach cards: use the six-item form even above B2.** House style says the
five-item form (English body) is usually right at B2 and above. It renders as a
translated heading over an English rule, which is the half-translated screen §8
exists to prevent. Caught by screenshotting the Spanish build, not by any gate.

### Still to do

* **Nothing is published.** Files, images and builders were delivered by
  `SendUserFile`; `git push` returns the usual proxy 403. Local branch
  `merge-duplicate-lessons`, commits `918ae38` and `8bb3e50`.
* **Supabase, after the files are live and propagation is confirmed:**
  `delete from lessons where id in (40, 54, 126);` and
  `update lessons set title = 'Dino-Craft Part 0: The Briefing' where id = 7;`
  Consider `sort_order` so Part 0 sits ahead of Parts I and II. Until row 7 is
  retitled the deck's `<title>` reads "Dinosaurs (C1)", because `seo.py` writes
  it from the table — that is not a bug in the build.
* `Football/stadium-silhouette.jpg`, `minecraft/Skeletal_Dinosaur.webp` and the
  four `minecraft/blackisler_*.png` are now unreferenced. `git rm` them from a
  session that can push.
* The other 143 conversion candidates. Start with a family.

---

## `tools/seo.py` cannot reach Supabase from a cloud session — and fails quietly

Found while publishing the risk-management deck, and it is a trap for every
future cloud session, so it goes above the lesson notes.

`seo.py` fetches the `lessons` table over HTTPS and falls back to
`tools/lessons.json` when that fails. **In a cloud Cowork session the fetch
always fails** — the egress proxy refuses the tunnel:

```
! supabase unreachable (<urlopen error Tunnel connection failed: 403 Forbidden>)
  — using /home/claude/repo/tools/lessons.json
```

That is a one-line warning in the middle of otherwise normal output, and the
run then reports success. The cache is a **committed file that only gets
refreshed by a successful run**, so it is exactly as stale as the last machine
that could reach the database. On 2026-08-31 it was **17 rows behind**: the
sixteen `blockcamp-*` tense lessons and, of course, the new one.

Two things go wrong, and only the first is obvious:

1. **A new lesson gets no SEO block at all**, because it is not in the cache,
   so `check-lesson.js`'s HEAD gate keeps failing however many times you re-run
   the generator.
2. **Stale rows get written into live pages as fact.** The cache said
   `forbes-english-lesson (2).html` (Business Conditionals) was `pro`; the
   table says `free`. The first run duly rewrote that page's JSON-LD to
   `isAccessibleForFree: false` and added a `.paywalled` `hasPart` — silently
   paywalling a free lesson's structured data, in a file nobody had touched.
   It was caught only by reading the diff and checking the claim against the
   live table.

**So: refresh the cache before running `seo.py` in a cloud session.** The
Supabase MCP tools work even though `urllib` does not, so pull the same select
the script uses and write it to the same path:

```sql
select json_agg(t order by t.sort_order asc nulls last, t.id asc)::text
from (select id, file, title, level, access, deck, video, created_at, sort_order
      from lessons) t;
```

…then write those rows to `tools/lessons.json` and run `seo.py`. **Commit the
refreshed cache** — that is what spares the next session the same hour.

Read the diff afterwards either way. `git diff --stat` should show additions
only; anything that shrinks a page, or flips an `isAccessibleForFree`, is the
cache talking and not the database. On Innes's own machine the fetch works and
none of this applies.

---

## Managing Risk (C1/C2) — built, checked, SEO done, awaiting upload

`forbes-risk-management-c1-c2.html`, 24 slides, 38 scored points, English +
German + Spanish all complete (the other seven stay `{}` and are not offered).
Builder `lesson-template/build/build_risk.py`, strings
`lesson-template/build/i18n_risk.py`, artwork `RiskManagement/` (eleven
supplied flat-vector illustrations, one family, hero plus ten per-slide
backgrounds).

New build, not a conversion — nothing on the site covered enterprise risk.
It sits beside `forbes-c1-negotiation` and `forbes-escalating-a-complaint-c1`
without overlapping them: negotiation moves another party, escalation routes a
problem upward, this one names and grades a thing that has not happened yet.

**`check-lesson.js` now reports `all checks passed`** — every gate including
HEAD. The `lessons` row was created on Innes's explicit "upload to forbes"
(id 293, `level` `C1-C2`, `access` `pro`, `deck` **false**), the cache was
refreshed from the live table, and `tools/seo.py` ran clean.

`access` was not asked about: the table is 229 pro to 54 free and all twelve
most recent additions are pro, so pro is the house default rather than a guess.
One `update` reverses it.

**`deck` is still false and must stay false until the file actually serves.**
House style: fetch the raw HTML in a browser, confirm it carries
`data-type="activate"`, and only then

```sql
update lessons set deck = true where id = 293;   -- tusioporxpjtegjlqkkb
```

**The row is live now and the file is not.** Until the upload lands, the
published `library.html` shows this lesson as a disabled "Coming soon" card,
because the live copy of `LESSON_IMAGES` has no entry for it and
`comingSoon()` is `!LESSON_IMAGES[l.file]`. The local `library.html` does have
the entry, so the card goes straight to live the moment the files land
together. That window is the cost of creating the row before uploading, and it
was accepted deliberately rather than overlooked.

The upload itself could not be done from this session: `git push` returns the
proxy 403, and there were no Chrome tools and no linked device, so GitHub's
web uploader was unreachable too. Every changed file went out by
`SendUserFile`.

Everything is committed on the local branch `risk-management-c1-c2` and was
delivered by `SendUserFile`, because `git push` returned the usual proxy 403.

Three things worth carrying forward.

* **`check-library.js`'s "every deck has a card" failure has moved.** The note
  elsewhere in this file and in the house style says it fails on
  `lesson-template.html` and `sherlock-scarlet-star_3.html`. It now fails on
  `blockcamp-passive-intro.html` and `blockcamp-passive-present-perfect.html`
  instead. Same pre-existing class, different files — do not treat it as
  something you broke, and do not go looking for the two files the old note
  names.

* **Both builders in `lesson-template/build/` hardcode
  `sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')`**,
  a path from a sandbox that no longer exists. Anything cloned anywhere else
  imports `deck` only by luck. `build_risk.py` and `i18n_risk.py` use
  `os.path.dirname(os.path.abspath(__file__))` instead, which works from any
  checkout including Innes's Windows machine. Worth doing to the rest.

* **A flat area in a background image is worse than a busy one.** The
  binoculars illustration had a cream field across its bottom quarter — fine as
  a hero, but at 34% opacity behind translucent cards it became a bright stripe
  that ate the contrast of whatever row landed on it, visibly on the matching
  slide's last pair. Cropping the band off fixed it. The house-style advice to
  lower `--bg-opacity` for a busy hero does not apply here and would have made
  it worse: the problem was flatness and brightness, not detail.

## The negative-space gate is a filter, not a certificate

Read this before you tell Innes a deck is clean.

It measures how far each half of a plate sits from the plate's own colour
grade. That catches loud cases and it caught seventeen. Innes then found three
more on the shipped Trial, and each is a different reason the measurement
cannot work:

1. **A busy background with nobody in it.** Slide 7 has Steve on the right and
   a wall of bookshelves on the left. Wooden shelves and coloured spines are as
   far off a teal grade as a person is, so the two halves scored level (1.03).
2. **A character wearing the plate's own grade.** Slide 12's witch is teal on
   teal - robe, hat and all, only her face off-grade - while the free half
   holds glass bottles with warm corks. The gate called the half WITH the witch
   the quieter one, at 0.84. Backwards, not marginal.
3. **A small subject in a big column.** Slide 16's climber is about a twelfth
   of the column, and a top-decile mean over the whole half averages her away.

No per-half colour statistic fixes those: in each case the colour statistics
genuinely do not separate. So the gate stays as a filter, and looking is made
cheap instead:

```bash
python3 lesson-template/checker/contact-sheet.py <deck>.html   # one PNG per deck
```

Every side-pinned slide as a thumbnail with its text band shaded. One image
instead of twenty. **Run it on any deck you touch, and look at it.** The three
above are obvious in the sheet and invisible to the number.

The durable fix, not yet done, is a per-plate subject map - which horizontal
band the subject occupies, checked by eye once per plate and stored the way
`checker/pins.json` stores Innes's placement calls. After that the gate is
exact rather than statistical. About 40 plates per camp, and roughly 25 have
already been eyeballed in this session's commits.

## The descent's colour system, 2026-09-01

Innes replaced it wholesale, on two stations at once:

> white = the agent / grey = the thing / is/are being = pink / past participle
> = purple / has/have been = turquoise / past simple = brown

**The chain now carries its own tense's colour, everywhere** - not just on the
contrast grids where the idea started. One green for every auxiliary answered
"what job is this word doing", and on a descent whose whole subject is which
tense the chain is in, that is the one question a learner never needs answered.
They can see it is an auxiliary. They cannot see which tense, and the trail
already taught them a colour for each.

**The be-auxiliary keeps its own tense; the added word carries the chain.**
Innes settled this after the first version coloured whole spans by the chain,
which made `is` lime inside `is going to` and blue two slides later - "is/are
not blue consistently in document". His ruling: *"is/are always blue - then is
blue + being pink, was brown + being yellow"*. So:

| | |
|---|---|
| `is` `are` `am` | blue |
| `was` `were` | brown |
| `is being` `are being` `am being` | one unit, pink |
| `was being` `were being` | one unit, yellow |
| `is going to be` | three pieces: blue + lime + gold |
| `was going to be` | the same, with the be brown |
| `has been` | turquoise, end to end |

**Only `going to` splits**, and Innes gave the reason: *"the gain of colouring
is/are in blue for going to is to make it easier to see how questions and
sentences are constructed, and because there is a past tense version was/were
going to that can take on the brown"*. Both halves matter. A blue be at the
FRONT is what a question looks like - *Is the wall going to be built?* - so
holding it out shows the inversion; and the same `going to` rides on a present
or a past be, which is only visible if the be is coloured apart from it.
Neither is true of `being`, where the be and the marker are one piece of
grammar - which is why the first attempt, splitting the continuous chains too,
was wrong.

`has`/`have` are the one exception and it is principled: unlike be, they have
no present-simple job in this line - a bare `has` here is always the front of a
perfect - so there is nothing to hold out in front.

It is **one central rule**, not eight hand-edits: `HEAD_TENSE`, `TAIL_TENSE`
and `AUX_TENSE` in `build_descent.py` hold the complete auxiliary vocabulary of
the eight stations (grepped from the sources, not imagined) and
`tense_in_situ()` rewrites every span at build time. Anything not in the map
keeps role green, so a new word cannot go unstyled. **Add a word to a station
and add it to that map**, or it ships green in a deck where nothing else is.

**Do not hand-tag a tense class in a station source.** The two contrast grids
were hand-tagged when this was a special case, and when the split shipped they
silently kept `is being` as one pink unit while every other deck had moved -
a hand tag is invisible to the central rule by construction. They are back on
`class="aux"`.

The participle stays purple in every chain. It is the constant the decks exist
to teach.

Two colours were solved rather than picked, both against all eight descent
surfaces: the object grey `#909294` (5.24:1 at worst, 189 RGB from the agent
white, which is the only thing it must be told apart from) and the present
perfect turquoise `#70E0E0` (10.5:1 at worst, 83 from camp 8's teal). **The
turquoise deviates from `tense-palette.css`**, which has camp 7 at `#2E7D65`:
that value fails on a dark deck at 3.3:1, and Innes asked for turquoise by
name. The route map and the camp page are unchanged; only the descent moves.

Green is now the eyebrow's, on all eight stations - the auxiliaries vacated it
and a slide label is what it should go to.

**When you change this, change the checker with it.** `check-colour-roles.py`'s
three aux-keyed gates all matched on `class="aux"`, so they silently matched
nothing the moment the recolour shipped. They now match `AUXC`, which must stay
in step with `AUX_TENSE`. Both were verified firing against a deliberately
broken copy - a class with no rule, and a participle left untagged after a
tense-coloured auxiliary.

## Stop finding colour defects by eye: check-unmarked.py

Innes, on Going To 2: *"short forms of am/are/is in this doc need to be blue -
is this mistake throughout all of Block Camp? How many other blunders are there
that I have to search for?"*

Nobody could answer that, and that was the real defect. `check-colour-roles.py`
only ever asked whether a word ALREADY WEARING a role class was wearing the
right one. **A word wearing no class at all was invisible to it**, and every
contraction in the line - `I'm`, `we're`, `she's` - sat in that blind spot.

```bash
python3 lesson-template/checker/check-unmarked.py            # must PASS
python3 lesson-template/checker/check-unmarked.py --review   # the judgement calls
```

The answer turned out to be **10 contractions in 3 decks**, not the whole line.

**It fails on one thing only, on purpose.** A be-contraction carries a be
wherever it appears and no summary line is built out of one, so a bare `'m` is
always a gap. A bare `is` is not: `.formula` and `.exlist` also hold one-line
summaries - *"every one of these is TEMPORARY"* - where `is` is doing a
sentence's work. The first cut reported all of it, 73 findings, and the ten
that mattered were buried. **A gate that cries wolf stops being read**, so the
rest is a `--review` list that does not fail.

**34 of those are still unresolved, and they need a ruling, not a fix.** They
are bare auxiliaries inside example sentences in paradigm cells - *"Your boots
are filthy"*, *"We had two horses then"*. Whether the `be` inside an
illustrative sentence wears its tense colour is a teaching decision. The
descent says yes; the camp decks have never said either way. **Settle it once
and the gate can enforce it everywhere** - that single unmade decision is
behind most of this week's round trips.

## The negator is always split out

Innes, asked whether every `not` and `n't` should be magenta: **"always split"**.

A contraction is two pieces of grammar in one word, so it prints as two. The
auxiliary keeps its colour, the `n't` takes the negative's magenta:

```
was n't being        has n't been        do n't build
```

Inside a chain that leaves two same-coloured halves bracketing one magenta,
which is not a broken chain - it is the chain with the negative shown **where
English puts it**, straight after the first auxiliary. The single-colour
version was hiding a teaching point.

74 contractions split across 12 decks, raw markup and escaped dictionary
strings alike. `check-colour-roles.py` gained **NEGSPLIT**, verified firing on
a deliberately broken copy.

**`won't` is the one exception, and it is not a preference.** Every other
contraction in the line splits into a real word plus `n't`. `won't` splits into
*"wo"*, which is not a word and must never appear on a slide. It stays whole in
the modal's orange, and the gate does not look at it. `can't` and `shan't`
would be the same case; neither is in the line.

**Magenta marks the grammatical negator, not negative meaning.** `never`,
`hardly ever` and `no` are frequency and quantity words - on Present Simple
`never` is in the frequency scale wearing beacon blue. A bare `not` in prose or
an aside also stays plain: *"this is the voice of a scene, not of a fact"*,
*"(not by me!)"*. Colouring those makes the page look like it is teaching a
grammar point inside a parenthesis.

## Still open

- **Three slides' ink crosses the deck bar by ~4px** — present-perfect-2 18,
  present-continuous 17, present-continuous-2 18. All top-anchored, all long
  gap slides. `check-lesson.js` passes them because its overflow gate measures
  the canvas edge, not the bar at y=644. Measured, not fixed.
- **Sort and activation slides show nothing in the EN/DE panel** (2–4 per deck).

## Negative space is now measured — it never was, and it showed

Innes, opening a deck I had just built: *"slides 5-10 with text on wrong side —
like are you even scanning for negative space?!"* No. Nothing was.

Every gate measured whether text **fits**: overflow, scroll height, ink into the
bottom chrome, ink off the sides. All of them pass a slide whose text sits
squarely on a character's face, because that slide fits perfectly. Six rounds
of "text on the wrong side" this week were found by eye, one slide at a time.

```bash
python3 lesson-template/checker/check-negative-space.py     # must PASS — two gates
```

### The first version of this gate measured the wrong thing. Read this before trusting a metric.

v1 summed **edge-gradient magnitude** per half and called the busier half
occupied, on the theory that a plate is flat sky and flat wall with the subject
carrying the detail. That theory is wrong. Texture density is not subjecthood:
a brick wall and a starfield are pure texture, a smooth-shaded villager two
metres from camera is almost none.

Innes, after it shipped: *"Pages 8, 15, 18 have text on wrong side on past
continuous passive… again you havent done your job."* All three had **passed**,
at 0.92, 0.82 and 0.94 — the metric scored the empty half busier than the
villager. The 48 slides v1 "found" were found by a metric that cannot tell a
character from a wall; some of those flips were luck.

**What actually separates them.** These plates are graded hard to one hue per
camp — gold, pink, teal, green — and the terrain, sky and architecture all sit
inside that grade. The characters do not: Steve's teal shirt and purple legs, a
villager's brown robe, skin tones. They are the pixels that break the plate's
own colour statistics. So: CIE Lab, the plate's median colour as its grade,
every pixel scored by robust distance from it — each channel over its own
median-absolute-deviation, so a natural sky-to-ground ramp is not convicted of
being a sky. Luminance is weighted to 0.25 because a blown-out sun or a lit
window is the one non-character thing that reliably breaks a grade. Score each
half by the mean of its top decile.

**Validated as a measurement, which v1 never was.** Twelve slides labelled by
eye: Innes's three, five more confirmed to sit on a character, and four
confirmed correct — including two that a luminance-heavy variant convicted (a
warm window in a blue room, a bright sky over an empty lawn). Worst true
positive 1.30, worst true negative 1.21; `MARGIN` sits at 1.25 in that gap.
**That gap is only 8% wide.** Findings under about 1.4× are "go and look", not
proof — which is why the ratio is printed. Seven slides are in `ALLOW` with a
reason, six of them the known blind spot.

v2 found **23 slides**, of which 17 were flipped and, separately, 8 more were
lifted off the floor (below). Both gates were verified failing against a
deliberately broken copy before being trusted.

### "Too low" had a third meaning, and it was one constant again

`--rail-clear` fixed text running *into* the chrome. Per-slide nudges lifted
short blocks off the floor. Neither touched the real one: **`justify-content:
center` centres in the 720px canvas, but the bottom 76px of that canvas is the
deck bar.** The box a reader actually sees is 644 tall and its middle is higher.
Measured across all 24 decks, *every* centred side-pinned slide landed with
0.133 of the frame — 96px — more air above it than below.

```
.slide { --centre-clear: 96px; }
.slide[data-side]:not([data-vpos])::after {
  content: ''; flex: 0 1 var(--centre-clear); min-height: 0; }
.slide[data-side]:not([data-vpos]) > .slide-head,
.slide[data-side]:not([data-vpos]) > .slide-body { flex-shrink: 0; }
```

Two things about that shape, both learned by breaking it:

- **It is a shrinkable spacer, not padding.** `padding-bottom` takes the height
  whether the slide can spare it or not, and going-to 13 and 17 and
  present-continuous-2 10 immediately overflowed by 18–43px.
- **The spacer has to be the only thing that yields.** With the body still at
  `flex: 0 1 auto` the shrink was shared and the same three slides still spilled
  by 15–35px. Pinning head and body to `flex-shrink: 0` puts all of it on the
  spacer, which is exactly what a reserve is for.

That is 40-odd slides fixed by one constant. It also means DE and ES are safe by
construction: where the longer text needs the room, the spacer gives it back.

**And the bottom anchor now has its own gate.** `data-vpos="bottom"` is a
deliberate call, so it is only overruled by measurement: the same off-grade
score, turned ninety degrees, comparing the top half of the text column against
the bottom half of the *visible* column (down to the bar, not to 720). Past
1.50× the slide is anchored onto the subject. Eight were, and are now `top`.
The margin is held above `MARGIN` on purpose — a bottom anchor usually knows
something the metric does not.

### The trap when you fix these in bulk

A plate is often used by **more than one slide in a deck**. Keying a fix on
`data-bg` with `count=1` hits the same tag every time — one slide ended up with
`data-nudge="up"` three times over while the two that needed it kept sitting
low. If you script a composition fix, key it on the slide index, and audit
afterwards:

```bash
# any section tag carrying the same attribute twice
python3 - <<'EOF'
import re, glob, collections
for f in glob.glob('blockcamp-*.html'):
    for m in re.finditer(r'<section class="slide[^>]*>', open(f).read()):
        c = collections.Counter(re.findall(r'\b(data-[a-z-]+)=', m.group(0)))
        if any(v > 1 for v in c.values()): print(f, dict(c))
EOF
```

## Block Camp II is built: eight decks, stations 9 to 16

The passive descent is finished and published. Station N mirrors camp N-8 and
takes that camp's chassis, so it wears the camp's palette and re-uses its
plates — the descent runs in the same order as the climb.

| station | tense | level | access | id |
|---|---|---|---|---|
| 9  | Present Simple Passive     | A2 | **free** | 295 |
| 10 | Present Continuous Passive | A2 | pro | 297 |
| 11 | Past Simple Passive        | A2 | pro | 298 |
| 12 | Past Continuous Passive    | B1 | pro | 299 |
| 13 | Going To Passive           | B1 | pro | 300 |
| 14 | Future Simple Passive      | B1 | pro | 301 |
| 15 | Present Perfect Passive    | B1 | pro | 296 |
| 16 | The Trial                  | B1 | pro | 302 |

Station 9 is free as the entry to Part II, mirroring camp 1. **Camp 8 has no
passive** — nobody says "has been being built" — so its plates carry the Trial
instead, which is why the line is seven tense passives and a trial.

Each deck is one auxiliary harder than the last and re-teaches nothing:
station 9 carries the SWAP (object to the front, doer optional) because its
auxiliary is the smallest; 10 adds `being`; 11 is 9 one tense back and owns the
second-versus-third-form problem; 12 closes the four corners and owns the
two-clause shape; 13 owns `be` after `going to`; 14 owns the will/going-to
choice with the doer already gone; 16 removes every label and asks for voice
first, tense second.

### What building them changed in the shared machinery

- **`--mark-obj` moved off the gold.** It was #ffd633 against `--mark-inf`'s
  #eec32f — ΔE 8.5 — and station 13 puts a bare verb and an object on one page.
  The infinitive did **not** move (gold is 46 words across three published Part
  I decks). The magenta #f65af6 was searched for, not picked: every hue at
  three lightnesses and three saturations, scored on its smallest ΔE against
  all nine fixed roles and every deck accent, rejecting anything under 4.5:1.
  Min ΔE 50.5 — its distance from the participle purple, which it shares a line
  with on every passive sentence.
- **`slidekit.sec()` takes an `attrs` argument.** Until it did, a station could
  not reach any composition knob — station 16's seven-chain slide overflowed by
  204px and there was no way to say "wide" from a station file.
- **`match()`, `gap()` and `order()` take glosses**, optionally. Before this the
  two built decks covered 7 and 15 strings out of 86 and 88, the worst on the
  line. Now 51–61 rows each, with only the cover and the results slide empty.
- **`.t-past` is in the descent's role CSS.** Station 11 shipped it nine times
  with no token behind it, rendering plain white, and the ORPHANS check only
  knew six class names. It knows ten now — verified by stripping the rule from
  a real deck and watching it fail.

### Two gate gaps this found, both now closed

- **Struck-through text was being read as a model.** Station 16 prints
  `the wall was been built` on purpose. `check-colour-roles.py` drops `<s>`
  blocks now; the only alternative was to un-teach the mistake.
- **Nothing measured horizontal overflow.** `grid-auto-flow: column` put seven
  paradigm blocks in one row and three of them rendered off the right of the
  canvas — `check-lesson.js` measures `scrollHeight` and never saw it. The
  `.para` rule wraps into rows now. A slide can still overflow sideways with no
  gate to catch it, so **shoot wide slides and look**, in all three languages.

### Still open on Part II

- **Sort and activation slides show nothing in the EN/DE panel** (2–4 slides
  per deck; the rest is cover and results, which is correct). Their chips have
  no gloss mechanism, and the chassis dictionary belongs to the active camp
  these decks descend past. Adding one means a two-line sort chip, which
  changes that slide's layout — worth a look, not urgent.
- The Trial's seven-chain slide sits over Steve on camp 8's plate. Legible, but
  a different plate would be better if one is ever commissioned.

## The colour system, stated once — and the gate that now enforces it

Innes spent an evening finding mis-coloured words by eye and it was faster
than any gate I had. The system he was checking against, written down:

| role | colour | token |
|---|---|---|
| finite auxiliary (`be`/`have`/`do` **doing an auxiliary's job**) | green | `--mark-aux` #46d98a |
| `will` / `shall` / `won't` | orange | `--mark-modal` #ff8a4c |
| bare verb after a modal **or after `going to`** | gold | `--mark-inf` #eec32f |
| past participle, and the WORDS for it | purple | `--mark-pp` #b39bf5 |
| second form, and the words `PAST SIMPLE` | brown | `--t-past-simple` #B08968 |
| a sentence that has dropped to present simple | slate | `--t-present-simple` #7A93B5 |
| state vs action (Present Continuous 2b only) | blue / pink | `--mark-state`, `--mark-action` |

Two consolidations came out of that:

- **`will` was the deck accent, and on the Going To decks the accent is a
  lime.** Measured ΔE from the auxiliary green that `going to` wears: 44.5 and
  42.2. Two greens, on the one pair of decks whose whole subject is telling
  `will` from `going to`. `--mark-modal` is now one literal hex line-wide —
  the orange the Future Simple decks already used — ΔE 99.5 from aux green,
  45.0 from the gold, worst contrast anywhere 5.9:1.
- **A named word wears inverted commas.** "Only 'am / are / is' changes",
  "no 'did' with 'was' / 'were'". This is not decoration: it is what tells a
  reader (and the gate) that the word is being *named*, not *used*.

### AUXJOB, inverted

The first version convicted only on determiners. Auditing every `.aux` in the
line against the word that follows it found a whole family it could not see —
`your hands are FILTHY`, `I am EXHAUSTED`, `the ground is WET`, `you are OUT
of breath`, `there is PAINT on your hands`, `the creeper is CLOSE`. Copulas,
all green.

So the test is inverted: **an auxiliary is only an auxiliary when a verb
follows it.** A verb is an `-ing` form, an `-ed` form, a known irregular
participle, or anything at all after `do/does/did`. A pronoun means an
inverted question and is read through; so are `not` and the adverbs. Anything
else convicts. That found fourteen more nobody had reported, across six decks.

It still cannot see `is finished` or `am exhausted` — both end in `-ed` and
there is no way to tell an adjective from a participle by shape. If a third
case turns up, teach it those two words by name; do not loosen the rule.

```bash
python3 lesson-template/checker/check-colour-roles.py     # must be 0 findings
```

## Composition: the checklist that actually catches things

Six rounds of "text on the wrong side" and "too low" this session. What
worked, in order of how much it caught:

1. **`node lesson-template/checker/shots.js <deck>.html <n> <dir>`, and LOOK.**
   Every side error was invisible to every gate — the text fitted, it just sat
   on the character. The rule is simply: the block goes on the half without a
   face in it.
2. **Measure the ink, do not eyeball the height.** The deck bar starts at
   y=644. `--rail-clear: 96px` fixed the whole `data-vpos="bottom"` class at
   once, after a dozen individual nudges had been applied to symptoms.
3. **Shoot it in German.** `check-lesson.js` renders English only. German runs
   ~⅓ longer and Spanish longer still; twelve slides overflowed in German
   that were clean in English, one of them off the canvas entirely.

Knobs available, all opt-in (see the shell CSS for why each exists):
`data-w="wide"` + `--wcols`, `--col-w`, `data-boxw` + `--boxw`,
`data-tr="beside"`, `data-align="right"`, `data-nudge`, `--rail-clear`.

**Two heroes were mirrored for composition** — `future-simple-will/bg22-flip.jpg`
and `going-to-infinitive/bg25-flip.jpg` — so the cover title sits over open
scenery and the characters sit opposite it. Both are generated files, not
edits in place, because the unflipped originals are still slide backgrounds.
The first of those was missing from the repo entirely and shipped a black
cover; `check-lesson.js` now has an **ART** gate that reads the disk.

## Block Camp: the colour rule now has a gate, and four new layout knobs

Innes reported six colour defects by eye, across four separate messages —
*"green 'was'? "*, *"'had' is green for no reason"*, *"why is has/have/am in
green"*, *"green colored words — what is the logic here?"* — and
`check-colour-roles.py` passed every time. It only knew about participles.

**It now has AUXJOB.** A be/have/do form is an auxiliary only when a verb
follows it. If what follows is a determiner, if it is the whole of a paradigm
cell, or if it sits inside a translation gloss, it is the main verb and the
green is a lie. Verified failing against the pre-fix copies at `e995f7b`: it
reports six of the ones he found by eye.

The determiner list was **narrowed from a first version** that also convicted
pronouns and prepositions and produced 35 findings, 29 of them inverted
questions — "Have you eaten?", "Is she going?" — where the auxiliary is doing
exactly its job. A gate that cries wolf 29 times in 35 is a gate nobody runs.

It still **cannot see** `was small` or `is PAST SIMPLE`: those need to know an
adjective from a verb. If a third case of that shape turns up, that is the
next thing to teach it — not a wider follower list.

Run it before shipping any deck:

```bash
python3 lesson-template/checker/check-colour-roles.py      # 0 findings
```

It then found **nine more, live, that nobody had reported** — including the
German word `am` in "am Ende" and the Spanish `has` in "¿has estado cavando?",
both painted green by an automated tagger matching them as English
auxiliaries. All fixed.

### Four opt-in knobs, all in the shared shell

The shell had `data-side`, `data-vpos` and `data-nudge` and nothing else, so
"the boxes are the wrong shape" had no answer but moving the block. These are
all opt-in — a slide without them measures exactly as it did before.

| knob | what it does | why it exists |
|---|---|---|
| `data-w="wide"` + `--wcols` | widens the column past 52% and gives the cards their real columns back; also lets a card FLOW its examples instead of one per row | six slides overflowed the canvas because the narrow-column fallback stacked two or three cards into one |
| `data-boxw` + `--boxw` | pins a card group, sort pool or bank to a named width | `width: fit-content` sizes a group to its longest line, and a line of prose is an arbitrary number |
| `data-tr="beside"` | puts the ES/DE gloss to the right of the example chips | it is opt-in because at three cards to a row it squeezes the chips to a column one word deep |
| `data-align="right"` | right-aligns card prose (not the lists) | a right-pinned column whose paragraphs all fall short of its own edge |

`check-lesson.js` now **passes on all 19 Block Camp decks.** Five overflows
that had been failing since the decks shipped are gone: future-simple-2 8,
present-perfect-2 8, present-perfect-continuous 8 and present-perfect 8 by
22px, present-simple-2 6 by 14px.

### The gate renders in English only

Present Continuous 2b slide 16 fits in English and **overflowed in German**,
where every match item grows a second line — and `check-lesson.js` passed it,
because it renders the page in English. Any slide whose height depends on
translated text can do this. Until the gate loops the languages, shoot the
deck in `de` before shipping a slide with inline glosses:

```bash
node lesson-template/checker/shots.js <deck>.html <n> <outdir>   # English
# then select #langSelect = de and re-shoot; German is the longest of the three
```

### The EN/DE panel was looking in one place only

Innes: *"ENG/DE button skimps on duties a lot"*. Measured across the eighteen
decks in German: **137 of 414 slides** opened the panel and were told
"nothing here is English-only" — and the empty ones were almost always slides
1–8, the **teach** slides.

The selector list covers the exercise shapes, because those are what the
dictionary holds. A teach slide's prose is not in the dictionary at all — but
it is not untranslated: it carries its gloss inline, in a `.sup`. The panel
never looked. It does now, dictionary first and the slide's own glosses
second. **137 → 52**, and on the sixteen Part I decks the only empties left
are the cover and the results slide.

**The 19 that remain are the two passive decks.** `slidekit` was called with
`es='' de=''` on eight of their slides, so they have no inline gloss to fall
back on and their chassis dictionary belongs to the active camp they descend
past. That is authoring work on `station09.py` / `station15.py`, and it is the
next thing to do to those two decks.

### Still open

- **The two passive decks have no catalogue row**, so `seo.py` writes them no
  metadata and `check-library.js --vs-origin` reports them cardless. A
  publishing decision, not a bug.
- **The placement sweep** still needs redoing with the fixed renderer.
- `--mark-inf` (#eec32f) and `--mark-obj` (#ffd633) are 1.4° apart in hue,
  ΔE 8.5. They never share a slide yet. Going To Passive and Future Simple
  Passive will put an infinitive and an object on one page — decide at
  station 13.

## Block Camp II — the passive descent: order, source truth, and two dead mechanics

### `git push` WORKS from a Claude Code remote session

This session pushed `claude/blockcamp-station-9-passive-17vt6t` straight to
GitHub — no proxy 403, no web uploader, no `SendUserFile` fallback. The whole
uploader procedure in `CLAUDE.md` (five-file image batches, click-by-coordinate,
the silent-commit trap) is a **Cowork sandbox** problem, not a universal one.
**Try `git push` first and find out** rather than assuming you are locked out;
it costs two seconds and skips an hour of uploader choreography.

### The descent runs in the SAME ORDER as the climb

Station N mirrors camp N-8. Innes: *"present simple should start the descent
(same as the ascent order)"*.

| station | tense | camp |
|---|---|---|
| 9 | Present Simple Passive | 1 |
| 10 | Present Continuous Passive | 2 |
| 11 | Past Simple Passive | 3 |
| 12 | Past Continuous Passive | 4 |
| 13 | Going To Passive | 5 |
| 14 | Future Simple Passive | 6 |
| 15 | Present Perfect Passive | 7 |
| 16 | The Trial — mixed active and passive | — |

Camp 8, Present Perfect Continuous, has no usable passive ("has been being
built"), which is why the line is seven passives and a trial.

`build_descent.py`'s docstring table listed the **reversed** order until
2026-08-31 — an abandoned model. The published station 15 deck had been right
the whole time. Anything that contradicts the table above is the stale copy.

### A deck from after review, a source from before it

The branch carried `blockcamp-passive-present-perfect.html` as corrected in
`0c291bc`, but the matching source was never pushed — GitHub blocked it three
times — so `station09.py` (as it then was) predated Innes's review. **Rebuilding
from it reverted nine of his fixes**: the object in gold, the agent in greenish
white, PAST PARTICIPLE and THIRD in the participle's purple, "who cares?!", the
per-station scoring messages and the results-panel spacing.

Both files are now in the repo and verified: **`build_descent.py 15` followed by
`apply-placement.py` reproduces the published deck byte-identical.**

**The placement pass is part of the build, not an optional extra.** Six slides
were moved by measurement after the builder ran, so the builder alone differs on
exactly those six. Placement lives in the HTML, never in the station source —
do not back-port `data-side`/`data-vpos` into the `sec()` calls, which is a trap
this session fell into and had to undo.

    python3 build_descent.py <n>          # from lesson-template/descent/
    python3 lesson-template/checker/apply-placement.py <deck>.html

### Two dead mechanics in `slidekit.py`, both live on station 15

Found by `check-lesson.js`, which **does** apply to Block Camp decks — it is not
only for the `deck.py` family. Run it.

- **`gap()` emitted no Check button.** `checkGaps()` is reachable by a
  `[data-action="check"]` click or by Enter inside a gap; the slide offered
  neither affordance. Six points across the two gap slides scored only for a
  learner who guessed to press Enter, and the deck reported the result as earned
  either way. Measured before the fix: zero buttons on the slide, Enter marking
  all three gaps correct.
- **`mc()` emitted no `.feedback` element.** The engine's `feedback()` opens
  `const el = slide.querySelector('.feedback'); if (!el) return;` — so every
  call was a no-op. **Eighteen per-distractor explanations per deck were in the
  DOM as `data-explain` and never once shown**, and right and wrong alike
  produced no message at all. Same shape as the pooled-gap-note defect further
  down this file. `mc()` now takes an optional `why=` for the key's own reason,
  which the engine already falls back to (`ownExplain || el.dataset.explain`).

**Station 15 has been rebuilt** (it was held back one session on Innes's
instruction, then released). Both stations' MC keys now carry a `why=`, so a
right answer gives a reason rather than a bare "Correct." Placement re-applied
on both; the same six moves came back on station 15, so the measurement is
stable across a rebuild.

### Known gaps on the line, none of them blocking

- ~~German and Spanish scoring messages are still the camp's ACTIVE wording~~ —
  **fixed.** `rescore()` now scopes each substitution to its own language block
  and raises on a missing block or key. The old substitution was global with
  `count=1`, and English is always the first match in the file, so `de` and `es`
  were never rewritten: both decks told a struggling learner *"Geh zurück zum
  Merksatz"* / *"Vuelve al lema"* on a deck about the passive. **Station 15 is
  rebuilt** and no longer byte-identical to what was first published — that is
  deliberate, and it also lands its six `.feedback` elements and two gap Check
  buttons.
- **Neither descent deck is in the catalogue**, so `tools/seo.py` skips them and
  both fail the HEAD gate with no description, og tags or JSON-LD. That is a
  publishing prerequisite, not a build defect: register the row, then re-run
  `seo.py`. Neither is in `library.html`'s `LESSON_IMAGES` either, so both would
  ship as "Coming soon" today.
- **`--mark-obj` #ffd633 collides with `--mark-inf` #eec32f.** Computed here,
  not taken on trust: **CIE76 ΔE 8.48**, 1.4° of HSV hue (1.84° in CIE-LCh).
  Under 10 reads as one colour to most people, so two roles are wearing the same
  yellow. Stations 9 to 12 contain no infinitive, so nothing collides yet; it
  lands at **station 13, Going To Passive**, where "is going to be built" puts an
  infinitive and an object on one slide. Innes rules on which one moves.
- **`chassis-head.html` and `chassis-tail.html`** in `lesson-template/descent/`
  are superseded — `split()` cuts the chassis live and nothing reads them — and
  `blockcamp-passive-intro.html` is an abandoned first build, live and unlinked,
  teaching the wrong syllabus. All three are marked for deletion and were left
  in place this session on Innes's instruction.

### `check-lesson.js` KEYS is NOT a false positive — it reads the source on purpose

An earlier pass of this file called it one, on the grounds that the engine
Fisher-Yates shuffles on first view (measured: the key landed at
`031003 / 011231 / 221312 / …` over six loads). **That reasoning was wrong.**
The gate's own comment says why it reads the source:

> Where is the key in the SOURCE? By the time the page is measurable the engine
> has already reordered the options, so this is invisible in the browser — which
> is why it survived until a student noticed. **It still leaks through print and
> PDF export.**

There is no runtime shuffle in a printed deck or a PDF export, so a source that
parks the key first puts it at A on every question on paper. `slidekit.mc()` did
exactly that; it now deals the key by question number, `(n - 1) % len(options)`,
which is deterministic so a rebuild reproduces. Both descent decks read
`[0, 1, 2, 3, 0, 1]` and pass.

**The lesson is more general than the gate.** A measurement that only looks at
the rendered page cannot see a defect that lives in the artefact — print, PDF,
crawler, or reader mode. Ask what the file says, not only what the browser
shows.

### All sixteen Block Camp I decks share one unanswerable slide

Innes, on the live Past Simple deck: *"All answers should be possible and there
is nothing to say otherwise."* Gap slide 2, "Choose a time signal", was broken
three ways at once, and **the same slide with the same three faults is in all
sixteen decks — 48 unanswerable scored items, all live**:

1. **Nothing in the sentence selects a signal.** "We finished the roof ___",
   "The village bell rang ___", "Steve found the diamonds ___" — every bank chip
   fits every gap. Pure guesses, and correct English marked wrong.
2. **The bank has 4 or 5 chips against 3 gaps**, under a hint reading "Each is
   used once". One chip must go unused, so elimination misleads as well.
3. **The explanations describe the phrase, not the choice** — recurring defect
   pattern 4, further down this file.

Measured across the line rather than assumed: every word-bank gap slide in
`blockcamp-*.html` has zero `class="dim"` determiners in any stem.

`blockcamp-past-simple.html` is fixed and is the worked example. The fix uses
the deck's **own** idiom — gap slide 1 already determines its answers with a
bracketed `(live)` / `(stop)` / `(study)`:

- the hint carries the anchor the exercise counts back from, and admits the
  leftover chip: *"Today is Friday. One signal per gap — one is left over."*
- each stem names its day or its time of day: `(on Thursday)`,
  `(after dark, while the village slept)`, `(on Wednesday)`
- each explanation does the arithmetic: *"Wednesday is two days before Friday…"*
- en, de and es all updated; the stems stay English, as gap 1's already do

**The other fifteen still need it**, and they need their own sentences — the
signals differ per tense (Future Simple and the Present Perfects carry five
chips, not four). It is content authoring, not a regex.

### The sixteen WERE in the catalogue - `tools/lessons.json` was 17 rows stale

An earlier pass of this file said none of the sixteen Block Camp decks were in
the catalogue, because `tools/lessons.json` had no Block Camp rows. **They were
in Supabase the whole time** (ids 277-292). The CACHE was 17 rows behind, and
`seo.py` cannot reach Supabase from a sandbox (proxy 403) so it silently used
the stale copy. Refreshed via the `mcp__Supabase__*` tools, which do work:
267 rows -> 284. All sixteen now carry metadata and are in `sitemap.xml`
(227 -> 243 URLs), and `blockcamp-past-simple.html` passes all fifteen gates.

**The same stale cache is what kept reverting `1855e09`.** Business Conditionals
is `access: free` in the live table and always was; the cache said `pro`, and
`seo.py` does `free = row['access'] != 'pro'`. An earlier note here called it
"`pro: None`" - that was a misreading: the cache has no `pro` key at all, so
every row returned None. The column is `access`, values `free` / `pro`.

**Refresh the cache before trusting anything `seo.py` writes**, and refresh it
from the MCP path, not from `seo.py`'s own HTTP fetch. A stale cache does not
error - it quietly withholds metadata from every lesson it has not heard of, and
overwrites deliberate edits on the ones it has.

### `seo.py` reverts hand-edits to generated HTML — the pro flag is data

Running `seo.py` rewrote `forbes-english-lesson (2).html`, undoing Innes's own
commit `1855e09` ("Business Conditionals: mark as free in structured data") from
two hours earlier. `tools/lessons.json` has **`pro: None`** for id 37, so the
generator writes `isAccessibleForFree: false` and re-adds the paywall `hasPart`.
Reverted here to preserve his intent, but **the page edit will be undone by
every future `seo.py` run until the data changes**: set `pro = false` on row 37
in Supabase (reachable via the `mcp__Supabase__*` tools, not over HTTP from a
sandbox) and refresh the cache. Same class as the deck-vs-builder rule — the
generated file is never the place to record a decision.

### Running the checkers needs two things this container did not have

    pip install numpy pillow
    export NODE_PATH=/opt/node22/lib/node_modules   # playwright is global

Without numpy, `apply-placement.py` dies in an import inside `check-placement.py`
and the placement pass is silently skipped — which looks exactly like a build
that differs from the published deck for no reason.

---

## Interior Design pair — two old-format lessons fixed and shipped

`forbes-interior-design-c1.html` and `interior-design-vocabulary.html` were
both sitting as "Coming soon" — no `LESSON_IMAGES` entry, no hero art. Both
are **old-format, hand-authored lessons**, not deck-template builds (zero
`data-type` sections, no builder script in `lesson-template/build/`), so
hand-editing them directly was correct here, unlike a deck.

`interior-design-vocabulary.html` audited clean — shipped as-is.

`forbes-interior-design-c1.html` had three real bugs, all fixed in place:

- **Show-Answer scored as correct.** `fibHint()` revealed the answer and
  then let the same input still register as a correct submit — free points
  for pressing the hint button. Rewritten to reveal without scoring.
- **Static counters lagged the real question count.** Progress read "0 / 18"
  and the final score denominator read "/ 24" against an actual 22 scored
  questions (`TOTAL_Q = 22`, with a dead `TOTAL = 24` leftover comment).
  Corrected to 17/22 and /22.
- **Matching activity could complete early.** `checkMatchComplete()` gated on
  `matchDone >= TOTAL_PAIRS` (attempts made) instead of `matchScore >=
  TOTAL_PAIRS` (pairs actually correct) — wrong guesses alone could trigger
  "complete". Fixed to gate on score.

Hero art for both came from the six unused `material_and_space_architectural
_design_interiors` Midjourney images already sitting in Downloads (Aug 3) —
no new art was commissioned. Picked by content match, not just looks:
`InteriorDesignPhrases/hero.jpg` (image C2) for the Presentation Phrases
deck, `InteriorDesignVocab/hero.jpg` (image B3, a literal threshold/doorway
shot) for the Vocabulary lesson, which teaches the word "liminal". Added as
`library.html` card thumbnails only, not in-page hero banners — these are
old-format pages and don't carry a `--hero` banner slot.

Confirms the mechanism from the `library.html` section below: **"Coming
soon" is derived purely from `!LESSON_IMAGES[l.file]`.** There is no
separate stored flag to flip. Adding the two `LESSON_IMAGES` entries and
re-running `tools/seo.py` (which regenerates `lesson-meta.json`'s
`coming_soon` field from the same map) was the whole fix — no manual edit of
generated metadata.

Published as three commits via the GitHub web uploader (git push still
403s from this sandbox): `7f272b9` (Presentation Phrases hero), `692a976`
(Vocabulary hero), `269ad1b` (bug fixes + both `LESSON_IMAGES` entries +
SEO regen). `library.html` was re-fetched from `origin/main` immediately
before the final edit — `557c2ef` landed on `index.html` mid-session and
did not touch `library.html`, confirmed by re-diff. All three verified
byte-for-byte against `origin/main`, `check-library.js --vs-origin` clean.
Live cards confirmed showing real thumbnails (not "Coming soon") after a
cache-busted reload.

---

## Open queue — artwork staged, none built

| Lesson | Artwork | State |
|---|---|---|
| `forbes-nature-agency-part1.html` | `NatureAgency/` (hero, lake, station, prairie) | **BUILT — 36 slides, checker clean** (`381754c`). An earlier finished rebuild of this same lesson was lost to an unpushed branch first — see the warning under Publishing in `CLAUDE.md`. |
| `forbes-nature-agency-part2.html` | `NatureAgency2/`: `hero-otter.jpg` (cover), `hide.jpg` (the hide slide), `loch.jpg` (scene-setting + results), `reeds.jpg` (dividers), `shore.jpg` (activation) | **BUILT — 59 slides, checker clean.** `build_nature2.py` + `i18n_nature2.py`. |
| `forbes-english-b2-lesson.html` | `TopGearB2/hero.jpg` | **BUILT — 37 slides, checker clean.** `lesson-template/build/build_topgear.py` + `i18n_topgear.py`. Audit at `docs/topgear-b2-audit.md`. Not yet pushed. |
| `forbes-geoscience-phrases.html` | `Geoscience/` (5 images) | **audited, see `docs/geoscience-audit.md`** |
| `forbes-english-lesson (flow).html` | `FlowState/` (hero, bg-pattern) | **BUILT — 15 slides, all 12 gates clean, 19/19 play-tested.** `build_flow.py` + `i18n_flow.py`. Catalogue row 41 corrected in Supabase. |

### Decisions taken on Nature Agency Part 2 (Innes, this session)

- **Artwork: a new hero is coming.** `NatureAgency2/hero.jpg` and `plain.jpg`
  are African savanna elephants; the lesson is European temperate wetland
  conservation and they depict nothing in it. Innes is supplying a
  wetland hero — otter, reed bed, river, bird hide. **Do not build the palette
  from the elephants**, and do not ship them as the cover.
- **Setting: make it British.** Rename the agency. "Federal Agency for Nature
  Conservation" is Germany's *Bundesamt für Naturschutz*, but the bylaws, the
  Wildlife Act, the licence spelling, the roundabout, the car park, the visitor
  centre, the bird hide and the yew-grove folklore are all British, as is the
  whole of Part 1. Keep the vocabulary and geography; change the name. In the
  same pass: `offense`/`offenses` → `offence`/`offences`, `bylaw` → `byelaw`.
- Everything else in the audit's priority list proceeds without further asking.

**Built.** The wetland hero arrived as `NatureAgency2/hero-otter.jpg` (otter on
a bank, reed line, open water) with `reeds.jpg` as the per-slide background for
the three section dividers and the results slide. Light theme, palette derived
with `--light`, every contrast row PASS. 59 slides, all ten gates clean.
`hide.jpg` sits behind a dedicated slide for *the hide*, the deck's
highest-risk piece of jargon, and is the only background doing teaching work.

**The agency is The Nature Agency**, in both parts and in both Supabase
titles (ids 130, 131). Part 2 briefly shipped as the "Wildlife and
Countryside Agency" while Part 1 said "The Nature Agency" and the library
cards still said "Federal Agency for Nature Conservation" — three names for
one two-part set. If you touch either part, keep the name. The Wildlife and
Countryside **Act** is real and stays; only the agency was renamed.

Two notes for whoever does Part 1:

- **The shared match engine still cannot be lost**, so Section 3 here is three
  `sort_slide` activities binned by sense rather than a `match` slide. Sorting
  scores the first placement only. Part 1 has the identical defect and the
  same workaround applies. Changing `deck.py`'s match engine is a deliberate
  decision affecting ~30 shipped lessons and was **not** made here.
- **`deck.py`'s `mc()` writes one explanation per slide**, which is what makes
  right and wrong feedback identical. `build_nature2.py` injects a per-option
  `data-explain` after calling `D.mc` rather than changing the shared builder;
  the engine already prefers an option's own explanation. If a third lesson
  needs it, promote it to an optional `explains=` argument on `D.mc`.

All palettes derived with `extract-palette.py`, every contrast row
passing.

**Standing constraint on the B2 lesson:** do not rename Clarkson,
Hammond or May in the published Stranger Gears build, and the Stranger
Gears front-page image is not to be questioned. Check whether that
lesson belongs to the Stranger Gears family before touching a name.

### Top Gear B2 — built

`forbes-english-b2-lesson.html`, 37 slides, all ten gates clean, dark
theme, palette verbatim from `extract-palette.py TopGearB2/hero.jpg`.
760 KB → 126 KB: the 714 KB base64 hero is now
`--hero: url('TopGearB2/hero.jpg')`. Clarkson, Hammond, May and the Stig
all stay; what went is the invented speech attributed to them, and the
four factual errors in the audit's C8. `library.html` has the thumbnail.
Full reasoning is in the builder docstring. Four things a later session
should not have to rediscover:

- **The match engine still cannot be lost** — third lesson in a row. The
  five matching pairs became five one-per-slide "identify the structure"
  MC items, which also cleared the 592px overflow the ten-row board
  measured. `deck.py` untouched, same call as Nature Agency.
- **This was the third lesson needing per-option `data-explain`, and it
  was still injected after `D.mc` rather than promoted to an `explains=`
  argument.** Promoting it now looks right; the cost is re-running
  `check-lesson.js` over every shipped deck to prove no regression, which
  is a job of its own and was not this build's.
- **One gap per `.gap-row`, always.** `checkGaps` marks
  `r.querySelector('.gap')` — the *first* gap in each row — while
  `maxScore` counts every `.gap` on the slide. Two inputs inside one row
  therefore create a point nobody can score. The two-error correction
  item here is two rows for exactly that reason, and it is what makes it
  worth two points.
- **`applyLang` assigns placeholders as a DOM property**, so `&rsquo;` in
  an `actPlaceholder` renders as literal `&rsquo;` once the language is
  applied — the §13 entity trap in its attribute form. Use the real
  character. Same applies to `resPerfect`/`resStrong`/`resMid`/`resLow`,
  which reach `scoreMsg` through `textContent`.

Gap tolerance (whitespace, curly apostrophe, `-ise`/`-ize`) is done at
build time in `build_topgear.py`'s `alts()` by expanding each answer into
every accepted spelling, not by changing the engine's `gapOk`. A
lesson that deliberately tests BrE against AmE spelling would be broken
by a blanket engine change; per-lesson data is not.

---

## El Zar is a band, not a Tsar

Innes: *"is this really geopolitics? or music?"* Music. `library.html` had
**`el zar` hardcoded into the Geopolitics regex**, almost certainly because the
name reads as "the Tsar".

The lesson is eighteen C2 verbs of force and effect — mitigate, exacerbate,
obfuscate, corroborate, undermine, mollify, curtail — and every single example
sentence is music industry: a producer using reverb to soften a lead guitar, a
tour meant to calm a feud between two founding members, a handler obfuscating at
a press gathering, a venue contract imposing a set-list quota. The activation is
a label-versus-manager negotiation over a mismanaged tour, the writing task is a
broadsheet review, and the hero is `ElZar/studio-hero.jpg`. Zero political words
in the whole file.

Refiled as **Music + Negotiation** — the setting and the function, both real.
Music is a new category (🎸, added between Fashion and Construction) and El Zar
is currently its only member, which is fine: the site already carries Martial
Arts at three.

### `venezuela` was doing the same thing

Same rule, same mistake. "Used To & Be Used To — Venezuela Edition" is a
past-habit grammar lesson set on a hacienda — its own standfirst is "A quiet
hacienda on the llanos — the kind of place used to being visited only by dust
and time." No politics at all. **A place name is a setting, not a subject.**
Removed.

That left it with no topic category, which exposed a second gap: `used to` was
in none of the grammar rules, so all three used-to lessons (this one and two
Sherpa camps) were reachable only under ALL and Lesson plan. `used to` is now in
the Tenses rule, which takes Tenses from 26 to 29.

Geopolitics is down from 8 to 6. The two survivors worth a second opinion are
**Friedrich I of Prussia** and **JFK & Prepositions** — both are prepositions
lessons hung on a historical figure. Friedrich's own standfirst says
"prepositions of power, politics, and Baroque statecraft", so it has a claim;
JFK's is "the small words that put an event in a place, in a decade, and under
suspicion", which is really biography. There is no History category. Left as
they are rather than invent one for two lessons.

### How to check this yourself

`detectCategories()` keys off `title + ' ' + file`, lower-cased — **never the
lesson body**. So any proper noun in a title is matched against every rule, and
a name that happens to look like a topic gets filed under it. The way to audit
it is to run the real function over the catalogue rather than eyeball the
regexes: extract `NOT_ACTUALLY_SPEAKING` and `detectCategories` verbatim from
`library.html`, feed it `tools/lessons.json`, and print which lessons each
category catches. Reading the rules by hand gave me a bogus
"71 lessons uncategorised"; running the function gave the true answer, **0** —
the activity-type rules at the end of the function catch everything.

---

## Escape from Grammar Jail, and 103 junk meta descriptions

`full_grammar_test.html` (id 183) is renamed **Escape from Grammar Jail** —
Innes's wording, agreed as "Escape from" rather than "Get out the". The name is
in the catalogue, the page title, the topbar, the footer and the eyebrow in all
ten languages. The lesson NAME stays in English everywhere, the way a film
title does; only the "· All Topics" half after the separator is localised.
Translating the pun ten ways would have produced ten different lessons.

The real problem was that it had no `LESSON_IMAGES` entry, so it was one of the
66 shipping as "Coming soon" and unavailable. It now has one, and the
coming-soon count is 65.

Artwork: `grammarjail/escape-the-cliff.jpg`, cropped from the Alcatraz set Innes
sent, to the 3376x1440 shape the other three images in that folder already use.
It is the library card and it opens the results screen — you sit the test in the
exam hall (`jail-test-room.jpg`, already on the intro) and you finish on a
figure climbing out. Seven of the eight images he sent are unplaced; ask before
scattering them.

**`grammarjail/jail-cell-bars.jpg` and `jail-desk-window.jpg` are unreferenced**
— 1.2 MB of good artwork nothing points at, same defect class as the
`NatureAgency/` strays. Place them or remove them.

### `<p[^>]*>` also matches `<path>`

`seo.py`'s `describe()` falls back to "the first real paragraph" via
`<p[^>]*>(.*?)</p>`. That pattern matches **`<path>`, `<picture>`, `<pre>` and
`<progress>`**. Every page whose logo is an inline SVG opens with a `<path>`, so
the "first paragraph" ran from that path to the first genuine `</p>` much
further down and swallowed the entire header on the way.

The grammar test's Google snippet was, verbatim:

> Forbes EnglishGrammar · Full Test 0 / 45 0 / 45 ENGLISH Cheat Sheet Test ·
> Alle Themen 🇬🇧English 🇩🇪Deutsch 🇮🇹Italiano 🇪🇸…

**103 pages** were carrying a description of that shape. Fixed by requiring a
word boundary — `<p(?:\s[^>]*)?>` — and measured by capturing every description
before and after the run. Nine pages fell back to the built generic sentence
because their standfirst is not in a `<p>`; a `class="sub|subtitle|lede|
standfirst"` pattern with a lower length floor recovered two of them, and the
remaining seven now read "An interactive B1 English lesson from Forbes English:
<title>." — worse than a real sentence, far better than chrome soup. **Those
seven are worth a hand-written description each.**

### The fifth stale-base clobber — coming-soon deleted from seo.py

Ninety minutes after `8c68f2c` shipped, commit `1e485ae` ("seo.py: fetch
lessons in sort_order then id, matching sb-client.js") landed from another
session. Its stated change is four lines. Its actual diff is **+19 / −70**:
it uploaded a `seo.py` built on a base that predated the coming-soon work and
took the whole feature out with it —

- `coming_soon()` itself
- the `noindex,follow` branch in `seo_block()`
- the sitemap exclusion, the crawlable-list exclusion, the llms.txt exclusion
- the `coming_soon: true` flag in `lesson-meta.json` that the Worker reads to
  serve a gate page instead of an unfinished lesson

Live effect until it was noticed: **65 heroless, unfinished lessons back in the
sitemap, indexable, and served as if they were real.** The sitemap went from 182
URLs to 247 and nobody would have seen a thing.

Restored by starting from `8c68f2c:tools/seo.py` and applying only the genuine
`sort_order` change on top. Re-running then rewrote **0 pages** — proof the
restore is exact and not a second clobber in the other direction. The three
`describe()` fixes are in the same merged file.

**This is the fifth time.** The four earlier ones are further down this file.
The uploader route makes it easy: you upload a whole file, so any staleness in
your local copy silently reverts whatever landed while you were working.
`git fetch origin && git diff origin/main -- <file>` before every upload is the
only thing that catches it, and it takes two seconds.

### seo.py was feeding its own output back to itself

Found while fixing the above. `describe()` reads the page's existing
`<meta name="description">` as its third choice, and it was handed the raw
source — including the SEO block `seo.py` itself wrote last time. So whatever
description a page got on its first pass was frozen there permanently: rewriting
the page could never improve it. The block is now stripped before `describe()`
runs. Eleven pages picked up a correction on the first run after the fix (all
had been missing the level word, e.g. "An interactive English lesson" →
"An interactive C1 English lesson").

**Both of these were invisible.** Nothing checks meta descriptions, and the two
faults hid each other — the freeze meant the `<path>` bug's output persisted
even after a page was rewritten. A `--check` mode that flags a description
containing the site chrome ("0 / 45", a flag emoji, "ENGLISH" as a bare word)
would have caught it years earlier.

---

## IELTS: five lessons published, and the shelf now has a series

`forbes-english-ielts-*.html`, catalogue ids 245-249, all C1, all pro, all
`deck: false` — they are Innes's own scrolling pages, uploaded as-is rather than
rebuilt as 16:9 decks, which is what he asked for. Card artwork in `IELTS/`.

| File | Catalogue title |
|---|---|
| `forbes-english-ielts-academic-writing-part1.html` | IELTS Academic Writing (Part 1) |
| `forbes-english-ielts-writing-lab-part2.html` | The IELTS Writing Lab (Part 2) |
| `forbes-english-ielts-writing-studio-part3.html` | The Writing Studio (IELTS Part 3) |
| `forbes-english-ielts-maps-and-data-c1.html` | IELTS Writing Task 1: Maps & Accurate Data |
| `forbes-english-ielts-bar-charts-c1.html` | IELTS Writing Task 1: The Bar Chart |

The `IELTS` category already existed in `library.html` with no lessons in it;
it derives from `/\bielts\b/` against `title + ' ' + file`, so the filenames
alone are enough.

### The cards are placeholders cut from the lessons themselves

Innes sent no artwork, and a lesson with no `LESSON_IMAGES` entry ships as
"Coming soon" and unavailable — which would have defeated the point. Each card
is therefore a 1600x900 crop of that page's own most distinctive visual,
padded onto its own paper colour: the paragraph-flow diagram, the five-essay-
type grid, the two pie charts, the map with its compass rose. **Nothing was
invented and nothing was borrowed from another lesson.** `bar-charts.jpg` is
the exception and the best of them — that page already carried a 1400x783
base64 JPEG hero (a typewriter, books and a city skyline), extracted straight
out of the HTML. If real artwork arrives, these are one line each in
`library.html`.

### "The Liz Method" is not a phrase this site uses

Innes: *"dont say the LIZ METHOD"*. Part 1 was titled "IELTS Academic Writing,
the Liz Method" in both languages and named her in four quiz explanations; Part
3 said "Plan It — Liz's Steps" and "using Liz's own steps". All of it is gone,
en and de. The agreed replacement for the planning stage is **"The Four
Steps"** (`Die vier Schritte`), confirmed by Innes. The advice itself is
unchanged — only the attribution.

### The longest-key defect, found again in three of the five

Every one of these pages shuffles its options at render time, so key *position*
is a non-issue here. Key *length* was not. Ten questions had a key that was the
only longest option by 4+ characters:

- `maps-and-data`: `mapsMCQ` Q1, Q2, Q4 and `dataMCQ` Q1, Q2, Q3
- `bar-charts`: `MCQ` Q2, Q3, Q4, Q5 — worst was 102 characters against a
  76-character field
- `academic-writing-part1`: `c2_recap_items` Q1, Q4, Q5, in English *and*
  German
- `maps-and-data`: `dataCloze[3]`, the one cloze offender — "considerably more
  than" at 22 characters against 9, 13, 14

All fixed the house way: **distractors lengthened, keys untouched.** Two keys
were the exception and are worth knowing about:

- `mapsMCQ` Q4's key carried two claims joined by an em dash, the second of
  which duplicated the explanation verbatim. Split rather than padded — the
  explanation already said "write them in normal lower case".
- The same question's key was also the only option not starting with
  "Because". All four now match, so the grammatical tell is gone too. **Check
  option *shape*, not just option length** — a key that is the only one in a
  different grammatical form is as much of a giveaway as a long one, and no
  gate looks for it.

`dataMCQ` Q2's distractors were replaced with the genuine full band lists from
the lesson's own reference card, which fixed the length problem and taught more
at the same time.

### The paragraph-builder was printing its own answer key

Found on a second pass, after the first audit had already shipped. `renderReorder`
in Parts 1 and 2 filled each slot like this:

```js
`<span class="tag">${data.sentences[s].tag}</span>${data.sentences[st.slots[s]].text}`
```

The **tag** is the role slot `s` wants. The **text** is whatever the learner put
there. So the moment anything landed in slot 1 the slot announced "Topic",
slot 2 "Explanation", slot 3 "Example", slot 4 "Concluding" — before any
checking. Two failures at once:

1. **It hands over the key.** Drop any sentence anywhere, read the label, and
   the exercise tells you what belongs in that position. All four slots do it.
   A learner never has to judge a single sentence.
2. **It mislabels the learner's own work.** Put the concluding sentence in slot
   1 and the page tells them it is a topic sentence — on an activity whose
   entire purpose is recognising paragraph roles, at C1.

The tag is *feedback*, so it now waits for the check: nothing before, all four
roles plus correct/incorrect styling after. Verified both ways in both files.

**Look for this shape wherever a slot, bin or drop-zone renders a label from
its own index rather than from what was placed in it.** The sort slides are the
obvious next place to check.

### What the second pass actually ran

The first audit covered four defect classes — JS errors, key position, key
length, cloze-answer length — and reported the lessons as done. That was too
narrow, and the paragraph-builder defect above is what it missed. The full pass:

- **perfect play-through, driven from each lesson's own data arrays.** Maps
  20/20, Accurate Data 20/20, Bar Charts 20/20 — five each on multiple choice,
  fill-in-the-blank, sentence building and matching, so the advertised maximum
  is genuinely reachable. Parts 1 and 2: every activity to full marks
  (5/5, 5/5, 5/5, 5/5, 6/6, 5/5, 5/5, 5/5 and 10/10, 4/4, 8/8, 8/8, 5/5, 5/5).
- **advertised maximum vs reachable maximum.** All three score pills say "/ 20"
  and all three sum to 20 across their four activity arrays.
- **every cloze answer is present in its own options list** — an answer missing
  from its options is a point nobody can score. All fifteen pass.
- **no explanation prints its own markup** in any of the five, after answering
  every question.
- **Part 3 has no scoring at all**, by design. What was checked instead: word
  count and its threshold class, the countdown timer, the essay-type check, the
  five-item checklist, and the download — which produces a real 1.6 KB text
  file with the plan, the writing and the checklist in it.

### These are not deck-template lessons

`check-lesson.js` does not apply to them — no `.slide` sections, no shared
engine. What was run instead: a Playwright load of each page (no JS errors on
any; the only console noise is Google Fonts failing in the sandbox, which is
network, not code), plus two purpose-written audits that read the quiz arrays
out of the live page and check key position, key length and cloze-answer
length. Both are worth rewriting if more of these arrive.

---

## The Language of Flow (B2) — rebuilt, and two things worth keeping

`forbes-english-lesson (flow).html` was a four-part scrolling page: watch a
TED-Ed talk, click eight vocabulary cards to reveal their definitions, answer
five questions, read four discussion prompts. It is now a 15-slide deck.
`lesson-template/build/build_flow.py` + `i18n_flow.py` (en + de). Artwork
`FlowState/flow-hero.jpg` (cover) and `flow-bg-pattern.jpg` (interior).
Dark palette, all twelve gates clean, play-tested to 19/19.

What the audit found, and what the build does about it:

- **The five keys sat at positions `[1, 2, 2, 1, 2]`** — never A, never D.
  Always guess B or C and you beat chance on every item. Rebalanced to
  `[2, 3, 0, 1, 3]`. `build_flow.py` now carries `assert_keys_deranged()`,
  which fails the build if any of the four positions goes unused. **This is a
  general defect and there is no gate for it** — `check-lesson.js` checks key
  *length*, not key *position*. `football_c1_roleplay` has all eleven keys at
  index 0 and is still live. Promoting the assert to a gate is the obvious
  next move.
- Two keys were the longest option by a wide margin (Q2: 23 chars against a
  14-char field; Q5: 57 against 49). Distractors lengthened, keys untouched.
- The vocabulary was click-to-reveal, which scores nothing. Eight terms are now
  taught on two slides, matched against plain-English glosses, and used in
  eight marked gap-fills.
- The four discussion prompts are now the activation stage proper.

### A slide-level gap explanation was never once displayed

`deck.gap(..., why=...)` puts one pooled explanation on the slide instead of
one per row. `checkGaps()` only ever touched feedback found **inside** a
`.gap-row`, so the pooled note sat in the DOM with no code path to reach it:
the learner pressed Check, saw the gaps go green, and got no explanation at
all. Fixed in `lesson-template/lesson-template.html` — `markGroup()` now
returns the missed gaps rather than a boolean, and `checkGaps()` fills the
pooled note with the misses pooled across every row.

Swept every lesson in the repo. Exactly one other deck used the pattern:
`forbes-english-food-ordering-a1-part1.html`, whose `WHY_A`/`WHY_B` had never
displayed since it shipped. Rebuilt from `build_food_a1.py`, verified against a
deliberately-wrong answer, checker clean. The static regex sweep over-reports
(it flagged `english_firefighter_v3`, `forbes-gap-fill`,
`ukraine-reconstruction-lesson`); the DOM check cleared all three.

Related: `deck.teach()` emitted `data-i18n="None"` for a card whose note has no
translation key — a five-item card passes `c[3]` straight through. Guarded.

### Why the gap slides use a pooled note at all

Four rows each carrying their own `.feedback` reserve 46px apiece whether or
not anyone has pressed Check, which put both gap slides 51px past the canvas.
One pooled note per screen is what `build_food_a1` already does. If you need
per-row explanations on a four-row gap slide, it will not fit — use three rows.

### One background for the whole deck, not two alternating

The set ships two images: `flow-hero.jpg`, the full illustration, and
`flow-bg-pattern.jpg`, a deliberately murky crop of it (mean luminance 0.139
against the hero's 0.42 — a factor of three). The first build alternated them,
because `deck.py` falls back to the root `--hero` on any slide with no
`data-bg`. The result swung between a bright desert and a near-black screen
every second slide. **A slide with no `data-bg` does not get "no background" —
it gets the hero.** If a deck ships a second background image, give it to every
interior slide or to none.

Now: the cover carries the illustration (the template renders `.on-cover` at
opacity 1 regardless of `--bg-opacity`), and everything after it is the quiet
crop. `deck.activate()` gained `folder`/`bg` parameters so the activation slide
could join in; it was the only builder with no way to set a background.

`--bg-opacity` was then measured with `lesson-template/bgmeasure.py` rather than
guessed. Against the hero it was tight — 0.46 → 6.97 (fails 7:1), 0.44 → 7.32.
Against the crop there is no contest: 0.44 → 16.45, 1.0 → 14.38. Shipped at
**1.0**, which is as visible as that image can be made and still 14:1 for body
text.

### Three shipped decks were running a stale copy of the engine

`lesson-template.html` is inlined into every generated deck, so a template fix
only reaches a lesson when that lesson's builder is re-run. Re-running all of
them as a regression check on the `deck.py` change turned up three that had
drifted:

| Deck | Drift |
|---|---|
| `forbes-english-b2-lesson.html` | 395 lines |
| `forbes-nature-agency-part2.html` | 395 lines |
| `forbes-english-food-ordering-a1-part2.html` | 43 lines |

They were missing the sort-bin backdrop fix and the gap-scoring rewrite, among
others. All three were rebuilt, re-checked (37 / 59 / 16 slides, twelve gates
each) and shipped in this session. `build_food_a1` came back byte-identical,
so it was already current.

**Re-run every builder after touching `lesson-template.html` or `deck.py`**, not
just the lesson you are working on — `for f in lesson-template/build/build_*.py;
do python3 $f; done`, then `python3 tools/seo.py` to put the metadata back. It
takes under a minute and it is the only thing that catches this.
(`build_ua.py` fails on a missing `/tmp/ua_mc.json`; that is pre-existing and
unrelated — its data was never committed.)

### Supabase IS reachable — via the MCP tool, not the sandbox

`tools/seo.py` still prints *"supabase unreachable (403 Forbidden)"* and falls
back to `tools/lessons.json`. That is true of the sandbox's HTTP path only.
**The `mcp__Supabase__*` tools work.** Project `tusioporxpjtegjlqkkb`
(`forbes-english`), table `lessons`. Row 41 was updated live this session:

```sql
update lessons set title = 'The Language of Flow', deck = true, video = true
where id = 41;
```

It had been `"Flow State Lesson"`, `deck false`, `video false` — all three
wrong once it became a deck with a video. `tools/lessons.json` was mirrored to
match. **Check the catalogue row after every rebuild**: a deck that ships with
`deck: false` never appears under the deck filter, and nothing in the pipeline
catches it. Teaching `seo.py` to read Supabase through the MCP path is worth
doing.

---

## Nature Agency Part 1 — audit

**It is not a lesson. It is a 50-item autograded assessment with no
teaching content at all.** No table, no rule box, no worked example.
Every explanatory sentence sits inside a post-answer `explanation:`
string or a pre-answer `hint:`.

- **All 17 Section 1 keys are `correct: 0`.** A runtime shuffle hides it
  live; a static deck rebuild inherits a 100% "always A" key unless the
  options are deliberately deranged.
- **Section 3 cannot be lost.** `s3Score++` fires only on a correct
  match, wrong matches carry no penalty and no attempt cap, and the exit
  gate requires all 16 matched — so every learner scores exactly 16/16.
  A third of the total is free, and 41% real accuracy reports as "Solid
  foundation".
- **Feedback is byte-identical right and wrong** on all 34 graded items;
  only the `"Correct. "` / `"Not quite. "` prefix differs. No
  per-distractor feedback field exists in the data.
- **The key is the longest option in 10 of 17** (59% against 25%
  chance); mean key 62.1 chars against 50.3 for distractors.
- **`s2q3` rejects `shoegaze` while its own explanation offers it.**
  `s2q11` rejects unhyphenated *hunky dory*. ~15 items reject natural
  alternatives.
- **`s2q2`'s hint contradicts its stem**: stem "A **small** ___", hint
  "A **large** number of people".
- Section 3's 16 items have no explanation, no feedback and no example
  sentences.
- **Question shuffling breaks four explanations** that cross-reference a
  sibling item ("Compare this with the verb sense…") — after a shuffle
  the sibling may not be adjacent or may not have been seen.
- 23 rules identified; 21 exist only in post-answer feedback and 4 are
  not in the file at all.

**Factual:** the otter decline is blamed on water quality declining "in
the 1980s". The cause was organochlorine pesticides from the late 1950s;
the 1980s are when otters began to **recover**. The intro promises
"formal and legal" vocabulary and there is not one legal item among the
fifty. `parking lot` appears in an otherwise entirely British file
(badger cull, town council, marsh harrier, hides).

Budget: 37 slides as-is, 51 with the ~14 teaching slides it needs.
`s1q1` runs 83 words with its options and must be trimmed.

### What Section 1's teaching content should cover

Section 1 looks like 17 unrelated words (*domineering, receipt,
encyclopedia, skirting, laundry…*). It isn't. **It is built as eight
polysemy contrasts** — `report`, `critic`, `decay` and `reconcile` are
each tested twice — and the section reveals each contrast only *after*
grading. Every item tests whether the learner can pick the right
**sense** of a word they already know, usually the formal, technical or
idiomatic one. Teach that, not a word list:

1. **Name the skill** before the first item.
2. **The method:** disambiguate from the collocation, the grammar (which
   preposition follows, transitive or not), and the register.
3. **The contrasts, taught as contrasts.** Two the lesson never draws
   despite putting them in adjacent items:
   - **prevalent vs rampant** — both mean widespread, but *prevalent* is
     neutral and *rampant* means bad **and** unchecked. For a
     conservation agency this is the most useful pair on the page: a
     species is *prevalent*, an invasive species is *rampant*.
   - **reconcile X with Y vs reconcile with Y** — the syntax tells you
     the sense. Reconciling field notes *with* a survey is making two
     things fit; reconciling *with* a colleague is repairing a
     relationship.
4. **Register.** Teach the formal senses these words actually carry —
   *in receipt of*, *laundering*, the *decay* of an institution — which
   is also what a field officer writing reports needs, and which would
   make good on the "formal and legal" promise.

Two ordering fixes: **`report` = the sound of a gunshot** currently
appears only as an unexplained distractor, and deserves teaching in a
lesson about a conservation agency. **`domineering` is used to define
`humble`** in a Section 1 feedback string but isn't taught until Section
3.

Caveat: the polysemy reading of *skirting*, *receipt*, *laundry* and
*encyclopedia* is inference from the words themselves; the audit only
confirmed the doubling for the four it named. Check the actual stems.

---

## Escape from Alcatraz (A2) — built, and three new engine mechanics

`escape-from-alcatraz-a2.html`, 43 slides, 50 scored points, all ten
gates clean, dark theme, palette verbatim from `extract-palette.py
Alcatraz/hero.jpg` (every contrast row PASS). `build_alcatraz.py` +
`i18n_alcatraz.py`. **All ten languages complete** — the second deck
after `forbes-c1-negotiation.html` to carry the full set.

New in the shared engine, so every future lesson inherits them:

- **`search`** — timed identify-the-object hunt over unlabelled line
  drawings (`lesson-template/build/icons.py`, 20 objects). Names hidden
  until answered; the clock pauses on leaving a slide and resumes on
  return.
- **`lock`** — combination lock, first attempt scores, unlimited
  attempts after that so the story can finish.
- **the rail** — stops along the bottom that remember which room you are
  in and what you picked up. `D.at(slide, stop, take)` tags a slide.
  Hidden unless a lesson declares stops.

Four things a later session should not have to rediscover:

- **A background on a `display:none` slide is never fetched, and
  `page.pdf()` does not wait for the ones that print media reveals.** A
  deck printed without visiting every slide first exported black
  interiors while the screen looked correct. Fixed in the template:
  every `data-bg` is decoded at boot (`new Image().src`). This affected
  every deck with per-slide artwork, not just this one — Nature Agency
  and Top Gear are both worth re-checking.
- **`.sort-bin` now carries the card's backdrop** (`--surface` 78% plus a
  3px blur) instead of the near-transparent `--inset`. Over a bright hero
  the bins and their labels had disappeared and the board read as loose
  chips floating on artwork.
- **`deck.teach` takes an optional key for a card's *body*.** Six-item
  cards translate the body; five-item cards behave exactly as before. At
  A2 the rule itself has to be readable in the learner's language and
  only the worked examples stay English — the B2 split is wrong at this
  level. `EXAMPLE_KEYS` in `i18n_alcatraz.py` copies the English examples
  into all nine other languages so they cannot drift.
- **The wash is raised on this deck** to 0.17 / 0.36 (§5 permits it, per
  lesson, measured). Four of the twenty-three illustrations are
  cream-and-coral at full brightness. `bgmeasure.py` reads 0.046 mean
  with text at 7.58:1 — inside the dark-theme band.

The artwork is sixteen Black Isler illustrations plus a later set of
nine guard, surveillance and composite scenes; the guards carry the
final-check section, which is a nine-item mixed test with no rule on the
screen.

### Three defects in the shared builders, found by playing the deck

All three were silent — nothing threw, nothing failed a gate, and the
slides looked correct. Innes found the first two by using the lesson.

1. **`deck.order` emitted `data-action="check"`** while the engine routed
   sentence-building through `check-order`. The click landed in
   `checkGaps`, threw on a null input, and **the Check button did nothing
   on every deck generated with the shared `order()`**. Fixed in
   `deck.py`; `checkGaps` now routes a gap-less slide to the slide's own
   checker rather than throwing.
2. **`deck.gap` renders one answer per `______`, not alternatives.** A
   row written `['aren't', 'are not']` looks like two accepted spellings
   and is in fact two blanks — with one marker in the sentence, the
   second spelling is silently dropped and a correct learner is marked
   wrong. Alternatives go in one pipe-separated string:
   `["aren't|are not"]`. `deck.gap` now asserts that a row has at least
   as many markers as answers, which also catches the next one.
3. **`build_modals.py` had five "repair the sentence" items with no
   `______` at all**, so the B1 modal-verbs deck shipped a whole activity
   with no input boxes and five points nobody could score.

`assert_bank_is_not_a_key` was also failing open: with pipe-separated
answers nothing matched the bank, `all()` over an empty list is true, and
it fired on lessons that were fine. It now splits on `|` and needs two
found positions before it can fail.

**New checker gate: ACTIONS.** It walks the deck, presses what the
learner would press on every scored slide, and requires the slide to end
up marked. Verified failing first — it flagged exactly the two dead order
slides here and twelve across five shipped decks — then passing after the
fix.

Rebuilt and re-checked clean: `forbes-english-modal-verbs-B1.html`,
`forbes-english-lesson-managing energy.html`,
`forbes-english-photography-b2.html`,
`active_passive_refinery_lesson.html`, `exam-prep-5hour-courseEXP.html`.
**Run the new gate over the rest of the deck library** — a partial sweep
timed out, so most of it is still unchecked. It already found one more,
not fixed here because it needs a content decision per item:

> **`forbes-construction-contracts.html` — Activity 1, six MC slides,
> and not one option carries `data-correct`.** Every learner scores 0/6
> on it, whatever they pick, and the deck reports the result as if it
> were earned. The right answer is stated inside each item's
> `data-explain`, so the fix is to mark the matching option — but that is
> six judgements about which option the explanation means, and this is
> the light-theme benchmark file, so it deserves a careful pass rather
> than a regex. There is no builder for it; it would want one.

---

## SEO — the site had none, and now has a generator

`tools/seo.py`, run last in the pipeline (see `CLAUDE.md`). Before it: 246
pages with **no meta description, no Open Graph, no structured data**, two
canonicals, four pages titled "Lesson Library", and no sitemap. Three
structural problems mattered more than any of that:

1. **Nothing was discoverable.** `library.html` builds its list from Supabase
   in the browser, so the HTML a crawler receives had five links and 77 words.
   236 lessons sat behind it, reachable only by a URL you already knew. The
   generator writes a static list of all 236 *inside* `<div id="grid">` — the
   element the page's own script empties on start-up, so a visitor never sees
   it. When Supabase is unreachable it is also the fallback the visitor gets,
   which used to be a blank page.
2. **The gate answered 402.** Google does not index a non-2xx response, so all
   195 Pro lessons were unindexable whatever else was done. `locked()` now
   answers **200** carrying `isAccessibleForFree: false` and a `hasPart`
   marking the withheld region — Google's documented way to declare gated
   content. Same page for crawler and visitor: nothing here is cloaking.
3. **Every gate page was identical.** All 195 served the same generic
   `locked.html`. It now takes the lesson's own title, level and description
   from `lesson-meta.json` (generated by `seo.py` from the `lessons` table)
   and fills slots marked `<!-- LESSON:head -->` and `<!-- LESSON:intro -->`.

`deploy/test-paywall.mjs` was updated with it and still passes 16/16. **It now
asserts on the body, not the status** — once the gate answers 200 like a
lesson does, status alone cannot tell them apart and the bypass tests would
have passed vacuously. There is also a new case requiring the gate page to
name the lesson it is gating.

Left for a human:

- **`level` is null on 77 lessons.** It goes into the title, the description
  and `educationalLevel`, and it is what people actually search ("A2 English
  lesson"). Filling those 77 rows in Supabase is the single cheapest SEO win
  left, and `seo.py` picks it up on the next run with no code change.
- `front-page.html` and `index_1.html` are near-duplicates of `index.html`.
  They are `noindex,follow` with a canonical for now; deleting them is a
  content decision.
- The sitemap is static. Regenerate (`python3 tools/seo.py`) whenever lessons
  are added, or it goes stale.
- Nobody has verified any of this in Search Console — submit the sitemap.

---

## Recurring defect pattern

Check for these first in anything not yet rebuilt. Every lesson audited
so far has had several:

1. The correct option is the longest — roughly half of all MCQ items.
2. Answer positions patterned: always B, never D, a perfect a-b-a-b, or
   every key at index 0.
3. Right and wrong show identical feedback, because one string is
   rendered with a different two-word prefix.
4. The rule tested exists only inside that feedback string, so it can
   only be learned by getting the item wrong.
5. A word bank listing the gap answers in gap order.
6. Items that cannot be answered from the text, or that mark correct
   English wrong.

**Learner-facing text must never mention a previous version of the
lesson.** Two decks shipped with notes like "the old version marked this
wrong" on the slide itself and had to be cleaned. That belongs in the
builder docstring and the commit message.

---

## Deltas — where `lesson-template/HOUSE-STYLE.md` is wrong

- **Rollout list.** It names five converted lessons. The real figure is
  31 of 216. Regenerate rather than trusting it: a file is a deck if it
  has both `data-type="activate"` and a `UI_I18N` block. Take slide
  counts from `check-lesson.js`'s own header line — counting
  `<section class="slide` returns N+1.
- **The checker has nine gates, not seven.** Added since: **BANK** (a
  word bank listing gap answers in gap order) and **MARKUP** (an
  explanation printing its own `<strong>` as literal text, from
  `textContent` where `innerHTML` was needed), plus **SORT**.
- **ANSWERS is a ratio *and* an absolute floor.** The key must not
  exceed the longest distractor by more than 10% *and* by at least four
  characters. The floor matters: on one-word options from a closed set
  (`can / could / must / should`), "should" beats "must" by 50% while
  carrying no information.
- **I18N no longer means "German covers English".** It means English
  plus at least one finished language. A complete Japanese with an empty
  German is a legitimate finished state.
- **There is a `sort` slide type** — labelled bins and a pool of items,
  native HTML5 drag with click-to-place as the touch fallback, one point
  per item, and a wrong placement costs that item's point.
- **Publishing.** `git push` is blocked by the proxy (403). Everything
  goes through GitHub's web uploader, **one directory per commit**:
  `/upload/main/<folder>` for images, then `/upload/main` for HTML.
  Verify byte-for-byte rather than trusting the upload — `git fetch
  origin`, compare `git hash-object <file>` against `git rev-parse
  origin/main:<file>`, then `git reset --hard origin/main`. The live
  site runs 30–60 minutes behind `origin/main`, so a stale page straight
  after a push is the host catching up.
- **Builders are in `lesson-template/build/`.** Every deck is generated;
  edit the builder and re-run, don't hand-edit the HTML. Use `deck.py`,
  don't rewrite it.

## The SEO pass reverted a finished deck — third stale-base clobber

`c5b2bc6` ("SEO/GEO metadata — lesson pages 1/3") took
`harari_davos_c2_lesson_v2.html` from **125,615 bytes back to 66,667** — the
24-slide deck replaced by the pre-rebuild scrolling page with an SEO block
bolted on. The deck had landed forty minutes earlier in `d9154e9`.

Swept the other two SEO commits the same way; **Harari was the only casualty**:

```bash
# every .html that SHRANK by >5 KB inside a commit — a shrink means content was lost
for c in $(git log --format=%h origin/main | head -40); do
  git diff --numstat $c~1 $c -- '*.html' | while read a d f; do
    b=$(git cat-file -s $c~1:"$f" 2>/dev/null||echo 0); n=$(git cat-file -s $c:"$f" 2>/dev/null||echo 0)
    [ "$b" -gt 0 ] && [ $((b-n)) -gt 5000 ] && echo "$c $f $b -> $n"; done; done
```

**This is the same failure as the `library.html` clobber, one level worse.**
That one dropped two card entries. This one silently reverted a whole rebuilt
lesson, and it would have gone unnoticed indefinitely: the page still loaded,
still had a title, still had activities. It only surfaced because the checker
was re-run and reported four gates failing on a file nobody had touched.

Recovered by re-running `build_harari.py` — the deck came back byte-identical
(`54e443c9`), which is the argument for every deck being generated rather than
hand-edited.

**Two rules follow, and they cost nothing:**

1. **A site-wide pass must start from a fresh `git fetch` + `reset --hard
   origin/main`, not from a checkout of unknown age.** Any pass that touches
   every page — SEO, logo swaps, title rewrites — is a clobber waiting to
   happen, and the batch commits (`1/3`, `2/3`, `3/3`) mean a stale base
   damages a third of the catalogue at a time.
2. **Re-run `check-lesson.js` over every file a site-wide pass touched, not
   just the ones you meant to change.** The shrink sweep above is the cheaper
   version and catches the same thing.

### Order of operations, now that `tools/seo.py` exists

    build_<name>.py  →  check-lesson.js  →  tools/seo.py  →  upload

`seo.py` writes into the *generated* HTML, so re-running a builder strips it.
If you rebuild anything, re-run `seo.py` before uploading or the page ships
with no metadata. Running the checker again after `seo.py` is worth the two
seconds — that is what caught this.

**`seo.py` cannot reach Supabase from the sandbox** (proxy 403) and falls back
to `tools/lessons.json`. That cache is stale: it still has
`forbes-conservation-c1` at `deck: false` although the flag is now true in the
table, so `lesson-meta.json` and the deck category will lag until the cache is
refreshed from a session that can reach the database.

## Confirmed: what `seo.py` actually emits for JSON-LD

Asked for before claiming the schema win over enghub.pro. Measured across the
generated pages rather than read off the source:

| | |
|---|---|
| Root `.html` pages | 246 |
| Carrying JSON-LD | **237** |
| Parse cleanly as JSON | **all of them** |

| `@type` | count |
|---|---|
| `Organization` | 237 |
| `LearningResource` | 236 |
| `Course` (as `isPartOf`) | 236 |
| `WebPageElement` (the withheld region on Pro pages) | 195 |
| `WebSite` | 1 |
| `EducationalOrganization` | 1 |

**All 236 `LearningResource` nodes now carry `educationalLevel`.** That is only
true as of `19d9565`; before the CEFR fill, 77 of them had nothing to put there.

### The claim is right, with three holes worth naming

enghub.pro emits no JSON-LD at all, so "we are ahead on structured data" holds.
But the gap list used to make that comparison names five types, and **we are
missing three of them**:

- **`BreadcrumbList` — absent site-wide.** Cheap, and it is the one Google
  actually renders in results. Nothing else in the stack has to change.
- **`ItemList` on `library.html` — absent, and this is the worst of the three.**
  The catalogue is the most linkable page on the site, it now carries a static
  list of all 236 lessons for crawlers, and it has *no structured data at all*.
  It is one of the nine pages below with no JSON-LD.
- **`Product` / `Offer` on `pricing.html` — absent.** A paid product with no
  offer markup.

`FAQPage` is also absent, but there is no FAQ content to mark up, so that one
is not a hole — do not add it to hit a checklist.

### The nine pages with no JSON-LD, triaged

| Page | Verdict |
|---|---|
| `library.html` | **Fix.** Needs `ItemList`. |
| `pricing.html` | **Fix.** Needs `Product`/`Offer`. |
| `account.html` | Fine — private, should not be indexed. |
| `locked.html` | Fine — it is the gate template; the 195 real gate pages get theirs injected. |
| `front-page.html`, `index_1.html` | Fine — the noindex near-duplicates of `index.html`. |
| `full_grammar_test_italian.html`, `stranger-things-test-german.html` | Fine — redirect stubs. |
| `falklands-lesson.html` | Not in the `lessons` table at all. An orphan, same as the two index duplicates — catalogue it or delete it. |

### Two KNOWN LIMITS in the SEO handoff are already closed

- ~~`level` is null on 77 lessons~~ — **done** (`19d9565`). All 236 have a
  level; 75 were transcribed from their own title or filename, two resolved
  from a sibling lesson. Zero nulls in the table and in `lesson-meta.json`.
- ~~`lessons.json` cache is stale, wrong on the conservation deck flag~~ —
  **done** (`db34fbc`). Refreshed from the live table: 236 rows, zero null
  levels, deck flags current. `seo.py` still cannot reach Supabase from the
  sandbox, so the cache will drift again — refresh it whenever the table
  changes.

---

# Restored after a fourth stale-base clobber

Everything from here to the end was lost when `6fc8f3f` uploaded a
`docs/HANDOFF.md` built from a checkout that predated it — 35,224 bytes down
to 21,971, seven sections gone. Recovered from `e30f874`. Two sections
describe state that has since moved on and carry a correction at the top.

## `--secondary` is a derived token that nothing renders

Noticed while choosing a theme for the geoscience deck: 13 of 41 shipped
decks have a `--secondary` that is invisible against their own `--surface`
(under 1.5:1), including `forbes-c1-negotiation.html`, the worked reference,
at 1.01:1, and one deck where the two values are byte-identical.

**It does not matter, and that is the point.** `var(--secondary)` appears
**zero times** in `lesson-template.html`. `extract-palette.py` derives the
token and prints it, the contrast report does not include its row, and
nothing consumes it. Thirteen decks carry an invisible colour because the
colour is never drawn.

Do not "fix" the 13, do not add a gate for it, and do not pick a theme on
the strength of that row — a light-vs-dark decision was very nearly made on
it here. Either wire `--secondary` into the template so it means something,
or drop it from `extract-palette.py`'s output. Until one of those happens,
ignore it.

## The artwork was American and the lesson was British

Part 1 shipped on a bison hero with a prairie and a US ranger station behind the
teaching slides, over a lesson about a badger cull, a town council, a marsh
harrier, hides and a car park. Part 2 had already hit exactly this — its African
elephants were rejected and replaced with `hero-otter.jpg` — so it is a repeat,
not a one-off, and worth treating as a class of defect rather than a taste call.

Five replacement images are now in `NatureAgency/`, drawn from the lesson's own
content rather than from "nature" in the abstract:

| File | Picture | Where it lands |
|---|---|---|
| `hero.jpg` | marsh harrier, daylight, bird upper-left | cover, and the library card |
| `harrier-dusk.jpg` | marsh harrier, dusk silhouette, bird upper-right | the `report` teaching slide, and sort 1 |
| `peatland.jpg` | cut hags, dark water, poppies, hills | `decay`, `prevalent`/`rampant`, and 6 MC slides |
| `restoration.jpg` | hag face, tractor, cattle, a worker | "three tells", register, and the 3 odd gap slides |
| `hags.jpg` | lone tree on a hag, cottongrass fringe | `dwell`, and 6 MC slides |

Two decisions worth not re-litigating:

- **The daylight harrier is the cover, not the dusk one**, even though the dusk
  frame is the better picture. `.cover-inner` centres its text and the scrim is
  a radial at 50%/46%, so a centred title needs a clear centre. The daylight
  frame keeps its bird upper-left; the dusk frame flies straight through where
  the title goes. The dusk frame backs the `report` slide instead, which is the
  right home anyway — the harrier *is* the bird Elena has to report within 24
  hours, and that slide is where the verb sense is taught.
- **`--bg-opacity` stays at 0.40.** It was set there for the bison hero and the
  reason still holds for the new set, but it was **re-measured rather than
  carried over**: `lesson-template/bgmeasure.py` on the four background images
  gives `text_vs_brightest_bg` of 6.33–6.87 at 0.40 and **2.62–2.98 at the
  template's default 0.72** — a fail. `hags.jpg` is the worst case both ways.

**Watch out for `bgmeasure.py`'s slide index.** It indexes
`document.querySelectorAll('.slide')`, which is *not* the same sequence as
`<section class="slide` in the source — the source count is N+1, the same
off-by-one the slide-count chip has. Measuring by source index silently reads
slides that have no `data-bg` at all and returns the bare-wash number for every
one of them, which looks like a clean pass. Enumerate the indices from the DOM
first.

`lake.jpg`, `prairie.jpg` and `station.jpg` are unreferenced now but still in
the repo, because the web uploader cannot delete. `git rm` them from the first
session that has a working push.

**Nothing checks that a lesson's art matches its setting.** `check-lesson.js`
verifies the hero resolves; `docs/HERO-QUEUE.md` verifies the file exists. Both
catches so far came from reading the lesson text and looking at the picture.

## `library.html` loses card entries to stale-base overwrites

`forbes-geoscience-phrases` and `forbes-nature-agency-part1` both had a card
image, and both silently lost it. Not a gap — a regression:

```
9497eb4  Library: thumbnail for Nature Agency Part 1     <- both entries present
5066174  Merge the two Stranger Things tests             <- both entries gone
```

`5066174` did not touch either lesson. It uploaded a `library.html` built from
a base that predated them, and the web uploader replaces a file wholesale, so
two unrelated entries went with it. `LESSON_IMAGES` is a single 166-line
literal that every session edits, which makes it the most collision-prone file
in the repo — and the collision is invisible, because a missing card falls back
to a category-gradient placeholder that looks deliberate.

**Before uploading `library.html`, diff its map against origin's**, and treat
any key that disappears without a matching lesson deletion as a clobber:

```bash
ext() { git show "$1:library.html" | python3 -c "
import sys,re
m=re.search(r'const LESSON_IMAGES = \{(.*?)\n\};', sys.stdin.read(), re.S).group(1)
[print(k,'=>',v) for k,v in re.findall(r'\"([^\"]+\.html)\":\s*\"([^\"]+)\"', m)]" | sort; }
diff <(ext origin/main) <(ext HEAD)
```

The same check caught a second thing worth knowing: **the map had a duplicate
key.** `english_firefighter_v3.html` appeared at two lines with two different
images, so 167 source lines parsed to 166 entries and the earlier line did
nothing. The dead line is removed and live behaviour is unchanged — the card
still shows `Fire Brigade/fire-2-truck.png`, which is what was winning.

**But that lesson's card and its own cover now disagree**: the deck's
`--hero` is `firefighter/hero.jpg` while the card is the fire truck. Every
other entry in the map matches its lesson's hero. It is one line either way;
it was left as-is rather than changed inside an unrelated commit.

A gate for this would be cheap — parse the map, assert no duplicate keys, and
assert each value matches the lesson's own `--hero` where the lesson declares
one. Not written yet.

## library.html: run the checker, do not run a diff from memory

`node lesson-template/check-library.js --vs-origin` before you upload
`library.html`. It is not optional and it takes a second.

The clobber went **both ways** and neither session noticed:

| commit | added | silently removed |
|---|---|---|
| `5066174` | `stranger-things-test` | `forbes-nature-agency-part1` |
| `c5a9625` | Alcatraz + five decks | `stranger-things-test` |
| `0a39b5b` | restored two cards | — but not the one `c5a9625` took |

The restore commit fixed the two losses it knew about and missed the one
its own predecessor had caused. That is the shape of this failure: it is
invisible three ways over. The entry count does not change when one is
swapped for another; a lesson with no card falls back to a category
gradient that looks deliberate; and the session that clobbers is never the
session that notices.

The checker also verifies what a diff cannot: that every thumbnail file
exists, that every key is a real lesson, that no key is duplicated (a
duplicate keeps the last value, so the earlier line silently does
nothing), and that every finished deck has a card at all. Its first run
found two decks with none — `make-v-do` had never had one, and
`stranger-things-test` had been clobbered an hour earlier.

The one advisory it prints is a mismatch between a deck's card and its own
`--hero`. Two lessons differ on purpose or by accident and nobody knows
which: `english_firefighter_v3` (card `Fire Brigade/fire-2-truck.png`,
hero `firefighter/hero.jpg`) and `forbes-ai-productive-struggle-c1` (card
`AILearning/c1-lesson-thumb.jpg`, hero `AILearning/retro-desk-sunset.jpg`).
Left alone pending a decision; a deliberate detail-shot card is legitimate.

## CORRECTION: take/put support is per-item after all — and the merge is still easy

An earlier note in this file said the take/put ES and PL support was chrome
only and merged cleanly. **That was wrong, and it was wrong for an avoidable
reason.** The test used was "does any string in the JS carry Spanish or Polish
diacritics" — and most of these glosses do not. `tomar la iniciativa`,
`correr un riesgo` and `poner por escrito` are all pure ASCII. The check
reported zero and the conclusion was drawn from it.

What is actually there, counted by object key rather than by accent:

| File | Field | S1 | S2items | S3data | S4left/right |
|---|---|---|---|---|---|
| `expressions_take_put_v2.html` | `de:` | 7/7 | 18/18 | 7/7 | **0/12** |
| `expressions_take_put_ES.html` | `es:` | 7/7 | 18/18 | 7/7 | **0/12** |
| `expressions_take_put_PL.html` | `pl:` | 7/7 | 18/18 | 7/7 | **0/12** |

Two things follow.

**The "base" file is the German edition.** `expressions_take_put_v2.html` is
not language-neutral with two translations bolted on; it is DE, and ES and PL
are its siblings. Three editions, not one-plus-two.

**The merge is easy anyway, and it destroys nothing.** The support is a
*parallel field on identical item objects* — `{lbl, cat, de}` against
`{lbl, cat, es}` — so merging is `{lbl, cat, de, es, pl}` and a renderer that
picks the field by current language. This is nothing like `cheat_sheet` DE/IT,
where the divergent strings were whole example sentences. The general blocker
(`UI_I18N` cannot reach `data-explain`) does not bite here because the gloss
never goes through `data-i18n` at all — it is read straight off the item.

### Innes's decision on the promises

All three files tell the learner that translations appear after every answer.
That is true for activities 1–3 (32 items) and **false for activity 4**, the
dialogue-matching board — 12 items with no gloss in any language.

**Instruction: keep or delete all promises — no partially-kept ones. Spanish
takes priority over Polish.**

So, in the merge: add the missing activity-4 glosses so the claim is true, and
where a language cannot be completed to standard, delete that language's claim
rather than ship it half-kept. Spanish is the one to complete first; Polish is
the one to drop the claim from if something has to give.

Six expressions need a gloss (the right-hand replies are not glossed anywhere
and do not need to be — the existing pattern glosses the *expression*, not the
sentence). Spanish drafted, matching the `'x \/ y'` two-option house format
used in S1 and S3:

| id | expression | `es:` |
|---|---|---|
| L1 | put my foot in it | `meter la pata \/ decir algo inoportuno` |
| L2 | take a break | `tomar un descanso \/ hacer una pausa` |
| L3 | take the lead | `tomar la iniciativa \/ ponerse al frente` |
| L4 | put in writing | `poner por escrito \/ dejar constancia escrita` |
| L5 | put it behind you | `pasar página \/ dejarlo atrás` |
| L6 | take advantage of | `aprovechar \/ sacar partido de` |

L3 deliberately reuses the exact string already on `S2items` for *take the
lead*, so the same expression does not get two different glosses in one lesson.
Check the other five against S1/S2/S3 for the same reason before adding them.

## Queue: lessons with artwork staged

> **Updated.** Conservation Travel has since been **built and shipped** (21
> slides, `a3b7791`). Three remain: Impostor Syndrome, Contingency &
> Trade-offs, and the take/put merge. Artwork for all three is on `origin/main`.

Innes sent four URLs in quick succession. Harari is **built and pushed**. The
other three have their artwork committed and their groundwork done; none is
built. Pick them up in any order.

| Lesson | Artwork | State |
|---|---|---|
| `impostor_syndrome_lesson.html` | `Impostor2/hero.jpg` — a woman at a podium with a drink, audience in silhouette, Noma Bar treatment. **Ultra-wide (3376×1440), not 16:9** — crop or letterbox before deriving the palette. | Not audited. Note `Impostor/` is already taken by `impostor_syndrome_advanced_JP.html`, which is why the folder is `Impostor2/`. |
| `contingency-trade-offs-vocab.html` | `Construction3/`: `hero.jpg` (crane, red sun, dusk), `a.jpg` (unfinished concrete frame, palms), `b.jpg` (four-panel site strip), `c.jpg` (tower crane against cloud) | Not audited. 22 KB, the smallest of the four — likely a short vocab list rather than a full lesson. `Construction/` and `Construction2/` are both taken. |
| `expressions_take_put_v2` + `_ES` + `_PL` → one lesson | `TakePut/hero.jpg` (car on a road at dusk) | **A real merge, not a dedupe.** Innes asked for it explicitly. |
| `forbes-conservation-c1.html` | `Conservation/` (9): `reef-lagoon.jpg`, `reef-canyon.jpg`, `island.jpg`, `turtles.jpg`, `frog.jpg`, `wildfire.jpg`, `plantation.jpg`, `ama-boat.jpg`, `ama-dusk.jpg` | **Audited — see below.** Innes sent the art with no URL; it was matched to this lesson by content — the lesson is subtitled "From Cloud Forests to Coral Reefs" and runs Ecuador cloud forest → coral reef → Japan's *ama* divers, so the frog, the reef and the turtles are its own material. 60 KB, three activities, 6 MC questions. |

### The take/put merge is the awkward one

`docs/HERO-QUEUE.md` lists these under "checked and *not* doubles": 56–87 of
~150 strings shared, and **the ES and PL versions share more with each other
than either shares with the base**. So this is not the `full_grammar_test`
shape, where the only difference was chrome and the merge was free.

Worse, it runs straight into the blocker already recorded above: per-item L1
support lives in `data-explain`, which `UI_I18N` never reaches. If the ES and
PL support is per-item rather than chrome, merging destroys the thing that
makes the second and third files worth having — exactly the reason
`cheat_sheet` DE/IT was left alone.

**Diff the three before building anything.** If the support is per-item, the
per-item translation fix has to come first, and that is a `deck.py` change
affecting every shipped deck rather than a one-lesson job. Innes has asked for
the merge, so if it turns out to be blocked, say so and say why rather than
shipping a merge that silently drops the Spanish and Polish.

### Two process notes from this batch

**Never `git reset --hard` while staged artwork is untracked.** A
`git stash -u && git reset --hard && git stash pop` sequence in this session
silently lost four artwork folders — the stash did not survive — and reverted a
finished deck to its pre-rebuild state. Both were recoverable only because the
source PNGs were still in the uploads directory and the commit was still in the
reflog. Commit artwork as soon as it is staged.

**The uploader's "Commit changes" click fails silently more often than the
existing note suggests.** Two of four commits in this batch did not land, and
the page looked identical either way. The hash check is not optional, and it
must cover *every* file in the batch — `check-library.js --vs-origin` caught
that a `library.html` about to be uploaded would have wiped two cards another
session had added forty minutes earlier.

### ~~The take/put merge is NOT blocked after all~~ — SUPERSEDED, THIS WAS WRONG

> **Do not act on this section.** It claimed the ES and PL support was chrome
> only. It is not: all three files carry 32 per-item glosses each. The error and
> the real picture are in **"CORRECTION: take/put support is per-item after
> all"** at the end of this file. The paragraph below is kept only so the
> mistake is legible, because the *method* that produced it — testing for
> diacritics rather than counting object keys — is the reusable lesson.

~~Every Spanish-bearing text node in `expressions_take_put_ES.html` is chrome —
headings, task instructions, button labels, the section intros. There is no
`data-explain`, and no Spanish or Polish anywhere in the JS data.~~

The one part of this section that held up: **both files promise something they
do not fully contain.** The ES page says *"Las traducciones al español aparecen
en rojo después de cada respuesta"* and the PL page says the same in Polish.
True for activities 1–3, false for activity 4. Same class of defect as the
Harari transcript claim — a checkable promise the file does not keep.

### Artwork is committed the moment it is staged

Learned the hard way this session — see the `reset --hard` note above. Every
folder in the queue table is already on `origin/main`, so the next session
starts with the art in hand and nothing depends on a sandbox surviving.

## Conservation Travel C1 — audited, and now built

> **Built and shipped** as a 21-slide deck (`a3b7791`), all twelve gates clean.
> Every defect below was fixed; the audit is kept because the defects are the
> reusable part.

`forbes-conservation-c1.html`, 60 KB, three activities: 6 MC, 6 gap-fill, 5
sentence-ordering, plus discussion prompts. Artwork is in `Conservation/`
(nine images, listed in the queue table).

**The word bank is the answer key, in order.** Not correlated with it — the
same list:

```
bank    : rare  retraining  traditional  millennia  Cultural  extinction
answers : rare  retraining  traditional  millennia  Cultural  extinction
```

A learner reads the bank top to bottom, fills the gaps top to bottom, and
scores 6/6 without reading a single sentence. This is the most blatant
instance of the `assert_bank_is_not_a_key` defect in the catalogue — every
previous case was a bank that merely leaked the order; this one *is* the key.
Fix by sorting the bank, which is what the guard wants and what
`build_nature1.py` does.

`Cultural` is capitalised in the bank, which separately tells the learner that
gap begins a sentence. Sorting alone does not fix that; either lower-case it in
the bank or move the gap off a sentence boundary.

**The MC keys run 1 1 1 2 1 1** — five of six on index 1 — and **the key is the
longest option in 3 of 6** (up to +12 chars). Same pair of tells as Harari,
milder. Derange the keys and lengthen the three distractors; do not shorten a
key.

The ordering activity was not measured — check whether it can be lost before
trusting it, since the `match` engine's equivalent could not be.

The reading itself is good and should survive: Ecuador cloud forest, coral reef
restoration, Japan's *ama* divers. That last is what the `ama-boat.jpg` and
`ama-dusk.jpg` frames are for, and the lesson names the tradition explicitly,
so those two backgrounds do teaching work rather than decoration.

---

## The fourth clobber, and the hole in the check I was using

`6fc8f3f` took `docs/HANDOFF.md` from **35,224 bytes to 21,971** and dropped
seven sections. Same cause as the other three: a file uploaded from a checkout
that predated the work it overwrote.

This one is worth more attention than the others, because **the file it
destroyed is the one whose entire job is to survive between sessions.** Losing
a card entry costs a thumbnail. Losing a deck costs a rebuild. Losing the
handoff costs every session after it the reason anything was done.

### The check I was running does not catch this

Before uploading `HANDOFF.md` I had been running:

```python
mine.startswith(open(origin_version).read())   # "am I a clean superset of origin?"
```

That answers *"am I about to clobber origin?"* It does **not** answer *"has
origin already lost work of mine?"* — and after `6fc8f3f`, origin was the
clobbered version, so my append passed the check and quietly built on top of
the damage. I appended twice more before noticing.

**The check has to be against the last version known to contain your work, not
against whatever origin happens to be now:**

```bash
# every ## section that existed in <known-good> and is missing from the file now
python3 - <<'EOF'
import re, subprocess
def secs(t): return {p.split('\n')[0].strip(): p
                     for p in re.split(r'(?m)^(?=## )', t) if p.startswith('## ')}
old = secs(subprocess.run(['git','show','<known-good-sha>:docs/HANDOFF.md'],
                          capture_output=True, text=True).stdout)
new = secs(open('docs/HANDOFF.md', encoding='utf-8').read())
for k in old:
    if k not in new: print('LOST', k)
EOF
```

The byte-size trend is the cheap version of the same signal: **`HANDOFF.md`
should only ever grow.** Any commit where it shrinks is a clobber until proven
otherwise. Same rule as the deck shrink-sweep, applied to the one file that
cannot be regenerated from a builder.

### Four instances now, all the same shape

| Commit | What it overwrote | Cost |
|---|---|---|
| `5066174` | two `library.html` card entries | thumbnails |
| `a3b7791` | an SEO block in `library.html` (mine) | metadata, self-repaired by luck |
| `c5b2bc6` | the Harari deck, 125,615 → 66,667 bytes | a full rebuild |
| `6fc8f3f` | `HANDOFF.md`, 35,224 → 21,971 bytes | seven sections of institutional memory |

Two of those four were mine. The pattern is not carelessness by one session —
it is that **the web uploader replaces files wholesale and nothing in the loop
compares against what was there.** Until `git push` works, the diff before
upload is the only defence, and it has to be run against the right baseline.

## The longest-key defect, swept and cleared

Measured across all 41 decks, then fixed. **Every deck now passes the ANSWERS
gate.**

| Deck | Was | Fix |
|---|---|---|
| `forbes-c1-negotiation` | 10 of 12 items | 10 distractors rewritten |
| `football_c1_roleplay` | 10 of 11 items | 10 distractors rewritten |
| `stranger-gears-rpg` | 2 items | 2 distractors extended |
| `forbes_english_lesson` | word bank in gap order | bank sorted |

### None of these had a builder — which is why editing the HTML was correct

`forbes-c1-negotiation`, `football_c1_roleplay` and `forbes_english_lesson`
predate the generator. `CLAUDE.md`'s rule that hand-editing generated HTML "works
once and is then overwritten" applies to files a builder can regenerate. These
have none, so the edit is permanent. `build_stranger.py` exists but outputs
`stranger-things-b1-lesson.html`, not `stranger-gears-rpg.html`.

If anyone later writes builders for these four, the distractor text must be
carried across or the defect returns.

### Padding was the wrong fix on two of them, and why

**`forbes-c1-negotiation` teaches formal contract register.** Six of its items
ask "which is the most formal version", and formal contract English is
genuinely wordier than plain English — so length was *correlated with the
answer*, not accidentally attached to it. Padding a distractor with more formal
language would have produced a second plausible key.

Each rewritten distractor is instead made long by becoming **more
conversational** — hedges, filler, first-person commentary, vague quantifiers.
It ends up as long as the key and more obviously wrong on register. That is a
better item than the one it replaced: the learner now judges register instead
of counting words.

**`stranger-gears-rpg`'s two items test verb form** (`must have opened` against
`must opened`). The distractors were extended by completing their noun phrase to
match the key — `below it` → `below the chamber` — so the only remaining
difference is the verb form, which is the thing being tested. The error itself
is untouched. Note those strings appear **ten times each** in that file; all ten
were replaced, or the copies drift apart.

### `football_c1_roleplay` has a second defect, not fixed

**All 11 keys sit at index 0.** The template shuffles `.opt` children on first
view so it is not learner-visible — the same situation as Nature Agency's
all-zero keys, hygiene rather than a live fault. Deranging it means reordering
whole `<button>` blocks by hand in a file with no builder. Worth doing, not done.

### `stranger-gears-rpg` still fails three structural gates

No `activate` slide, no `UI_I18N`, no `.fe-logo`. It is a pre-house-style page,
not a scoring problem, and bringing it up to standard is a rebuild. **It carries
the standing Stranger Gears constraints** — Clarkson, Hammond and May keep their
names and the front-page image is not up for discussion — so that rebuild is a
deliberate decision, not a tidy-up.

### The screening sweep over-reports — use `check-lesson.js` to decide

A static regex sweep is useful for finding candidates across 41 decks quickly,
but it disagreed with the checker on seven items, in two ways, both mine:

1. **It used only the 4-char floor.** The real rule in `check-lesson.js` is
   `key > maxOther * 1.10 && key - maxOther >= 4` — a **ratio and** a floor. The
   comment there explains why: in a closed option set of modals, "should" beats
   "must" by 50% while carrying no information.
2. **It mis-parses options carrying a `data-explain` attribute**, pulling the
   explanation text into the option and inflating the length. That is what made
   `forbes-english-lesson (2)` look like a 1.38x offender when it passes.

Screen with the sweep; decide with the checker, which reads a real DOM.

## Recolouring a deck: Breaking Bad, orange to pink

Innes: *"give this same treatment of font and pink tones instead of orange."*
`breaking-bad-present-continuous-deck-viewer.html`, 16 slides, A2, deck, pro,
catalogue id 244.

**Measure both palettes before writing the transform.** Breaking Bad's warm sat
at hue 0-20, S 0.5-0.6; the Harry Potter pink at hue 340-350, S 0.3-0.4.

**Rotate the hue. Do not touch saturation or value.** The first attempt did all
three — 22 degrees, minus 28% saturation, plus 2% value — and Innes came back
with *"the pink has overpowered subtle neighbouring tones."* He was right, and
it is measurable: multiplicative desaturation compresses the *absolute* gap
between tones, so the saturation spread of the warm family fell by roughly half
on every slide. The coral wall, the terracotta recesses, the skin and the dusty
rose all converged on one flat pink.

| | slide 1 | slide 7 | slide 11 | slide 13 |
|---|---|---|---|---|
| original spread | 0.122 | 0.378 | 0.121 | 0.107 |
| v1 (rot + desat) | 0.061 | 0.225 | 0.079 | 0.075 |
| **v2 (rot only)** | **0.109** | **0.349** | **0.108** | **0.099** |

A pure hue rotation preserves S and V per pixel, so every tonal difference in
the original survives and only the hue moves.

### Then he asked for much less saturated — SUBTRACT, do not multiply

Those two requests are only in tension if you desaturate the wrong way:

```
s * 0.72    multiplies: a 0.12 gap between two tones becomes 0.086.
            The tones converge, the picture goes flat. This was v1.
s - 0.15    subtracts: a 0.12 gap stays 0.12. Every tone drops by the same
            amount and the separation between them is untouched.
```

Final settings: rotate 20 degrees, subtract 0.15 from saturation with a soft
floor at 0.06 so the palest washes cannot clip to grey, leave value alone.
Median saturation of the warm family falls from 0.50 to about 0.36 while the
spread survives. `#F27D6B` ends up `#F28FA3`.

**The general rule: to change how saturated something looks, subtract. To
change the relationship between tones — which is almost never what you
want — multiply.**

**Keep the band tight so the neighbours survive.** v1 ramped out at +35, which
dragged the tans and terracotta (hue 20-40) into the pink along with everything
else and left nothing for it to sit against. v2 is at full strength only from
-8 to +12 and back to zero by +24. Blues, greys and blacks never enter the
band either way. Applied to all 14 media images **and** to `srgbClr` values in
the XML — `#F27D6B` (26 uses) becomes `#F2738C`.

### Slide 2 was the only one with no artwork

Every text box on it stopped by x=1530 of 1920, so the right third was empty,
and the three column boxes behind SUBJECT / AM-IS-ARE / VERB+ING existed with
no fill, so the table read as three floating words. Gave the boxes a 16% tint
of the deck pink with a 9% corner radius, and put a tall crop of the Jessie
picture — the same media part slide 4 uses, a second relationship to it — in
the empty third. **A tall panel needs `srcRect`, not a squash**: the panel is
320x1080 (aspect 0.30) and the source is 1600x900, so the crop has to be about
17% of the source width or the picture comes out at half width.

### Recolouring changes contrast, so re-measure the text afterwards

Pink is lighter than the coral it replaced, so every cream or pink caption lost
contrast against it. A sweep of all 16 slides found three text blocks that were
invisible in the render:

| Slide | Text | Orange | Pink | Fixed to |
|---|---|---|---|---|
| 8 | "Where are they standing?" | 1.20:1 | **1.01:1** | `#10272B` → 7.2:1 |
| 13 | "Gustav is adjusting his tie" | 2.86:1 | 2.35:1 | `#10272B` → 6.3:1 |
| 16 | "SUBJECT + BE + VERB-ING" | 1.01:1 | 1.01:1 | `#FFF8E8` → 14.6:1 |

Two of those the recolour made worse; slide 16 was already broken. All three
were fixed with colours the deck already uses.

**The per-block sweep over-reports.** Sampling the median inside a text box
includes the glyphs and any second background the box overlaps, so a wide box
spanning two tones scores low even when the text is perfectly legible — it
flagged 21 blocks and only 3 were real. Use it to shortlist, then crop and look
at each one.

### "All Courier New" needed the theme changing too

The deck named Courier New on 43 runs and left 16 inheriting, and the theme's
`majorFont`/`minorFont` were **Calibri** — so `pdffonts` showed a
LiberationSans alongside the two Courier faces. Setting the theme to Courier
New *and* giving those 16 runs an explicit face cleared it. `pdffonts` is again
the check: two Courier entries and nothing else.

---

## The four presentation decks: top of the shelf, and a maximise mode

`star-wars`, `twin-peaks`, `breaking-bad`, `harry-potter` — the four decks
built from a `.pptx` behind `*-deck-viewer.html`. Innes: *"the only true
presentation decks, should be at top of list."*

`library.html` now sorts into three bands, derived from the filename like
every other state there, so a fifth deck lands in the right band on its own:

```js
const band = l => comingSoon(l) ? 2 : (/-deck-viewer\.html$/.test(l.file) ? 0 : 1);
```

### Mobile: `vh` is the bug, `dvh` is the fix

*"When I try to open any lesson on mobile must switch to landscape and address
bar sticks."* Three separate things, worth keeping straight:

1. **`vh` is the LARGEST viewport** — the one with the mobile address bar
   hidden. Size a box `100vh` with the bar showing and its bottom runs off the
   screen, taking the footer with it. That is the "address bar sticks" symptom.
   **`dvh` tracks the bar as it moves.** Every `vh` in the four viewers now has
   a `dvh` twin written after it: browsers that understand `dvh` take the
   second line, older ones keep the first.
2. **The green sandwich costs ~130px** of a landscape phone's ~390px — a third
   of the screen. A `Maximise` control now hides header and footer.
3. **Landscape** cannot be forced. `screen.orientation.lock('landscape')` only
   works inside fullscreen and only on Android/Chrome; iOS has no equivalent.
   It is called in a try/catch and the user turns the phone if it does not
   take.

Measured on a 844x390 landscape phone viewport, slide area after maximise:
**+62%** on three of them, **+103%** on Star Wars.

**iPhone Safari has no `Element.requestFullscreen`.** It is feature-detected,
and the button is still worth having there: it reclaims the chrome and `dvh`
handles the bar. Never assume fullscreen exists.

**Two viewer shapes, both need covering.** Three viewers cap the `<img>` with
`max-height:calc(100vh - 130px)`; **Star Wars sizes the `.slide-wrap`** with
`height:calc(100vh - 130px)` plus an `aspect-ratio` and lets the image fill it.
A first pass only rewrote `max-height` rules and Star Wars gained **0%** — it
measured as fixed while the other three moved. If you touch this again, check
all four, and check the number, not the diff.

---

## Publishing a .pptx: the slide-viewer pattern

Innes sends a finished PowerPoint and says "upload to decks". There is no
`decks/` folder — the established shape, set by `twin-peaks-deck-viewer.html`
and `star-wars-question-words-deck-viewer.html`, is four artefacts:

```
<name>.pptx                       the source, at the repo root, for download
<name>-slides/slide-01.jpg …      one 1920x1080 render per slide
<name>-deck-viewer.html           the page: one <img>, arrows, dots, download
catalogue row + LESSON_IMAGES     deck=true, thumbnail = slide-01
```

Rendering:

```bash
python3 <pptx-skill>/scripts/office/soffice.py --headless --convert-to pdf deck.pptx
pdftoppm -jpeg -jpegopt quality=88 -r 144 deck.pdf slide     # gives 1921px — resize
```

`pdftoppm` at 144dpi returns **1921x1080**, one pixel wide. Resize to exactly
1920x1080 before committing or the images are subtly non-standard. JPEG q86
progressive lands each slide at 200-400KB; the twin-peaks PNGs average 1.4MB
each for no visible gain, so use JPEG.

### CHECK THE FONT BEFORE YOU PUBLISH — `pdffonts`, every time

The first render of this deck went out in the wrong typeface and Innes spotted
it. The deck asks for **Courier New**, which is not installed here.
Fontconfig resolves it to **Liberation Mono**, which is *metric-compatible* —
so nothing overflows, nothing shifts, every QA check passes — and looks nothing
like Courier: a neutral grotesque with none of the typewriter slabs. A
substituted font is invisible to every check we run. The only reliable tell:

```bash
pdffonts deck.pdf     # BAAAAA+LiberationMono-Bold  <- wrong
                      # BAAAAA+CourierNew-Bold      <- right
```

**Fontconfig alone cannot fix it.** LibreOffice consults its own substitution
table first and that table maps Courier New to Liberation Mono; a
`<match target="pattern">` rule for the family never gets a look in. Two things
that also do not work: `ttf-mscorefonts-installer` (its postinst fetches from
SourceForge and fails in this sandbox), and pointing at "Nimbus Mono PS"
by name in a fontconfig alias.

What works is giving LibreOffice an exact family-name match. Nimbus Mono PS is
URW's clone of Adobe Courier — the face Courier New was itself drawn from — so
install it under the name it is standing in for:

```python
from fontTools.ttLib import TTFont
f = TTFont('/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf')
for rec in f['name'].names:
    if rec.nameID in (1, 16): rec.string = 'Courier New'
    elif rec.nameID == 4:     rec.string = 'Courier New Bold'
    elif rec.nameID == 6:     rec.string = 'CourierNew-Bold'
f.save('/usr/share/fonts/opentype/couriersub/CourierNew-Bold.otf')   # then fc-cache -f
```

Do all four styles. This is a **render-time substitution inside the sandbox** —
no font ships, and the container is rebuilt every session, so **this has to be
redone every time a deck using Courier New is rendered.** The same trap waits
for any deck naming a font Office ships and Linux does not: Calibri, Cambria,
Aptos. `pdffonts` is the check.

**The `LESSON_IMAGES` entry is not optional any more** — without it the lesson
renders as "Coming soon" and is excluded from the sitemap. Point it at
`slide-01.jpg`.

### Harry Potter and the Present Continuous — uploaded, with one fix

`harry-potter-present-continuous-deck-viewer.html`, 10 slides, A1, deck, pro,
catalogue id 243. Eight verbs — talk, tell, discuss, fly, play, buy, fight,
escape — one per slide over Harry Potter artwork, opening on the form and
closing on a recap grid.

**Slide 8 shipped without its eyebrow.** Every other verb slide carries
`VERB → IS VERB-ING` above the title; slide 8 had an empty text box named
`Prompt 8` sitting top-left in Arial 12.75pt, while its siblings use a
Courier New 13.5pt box positioned above the title. Not a rendering artefact —
`markitdown` showed no text in it either. Replaced with a copy of slide 6's
`Grammar 9` shape, `PLAY` → `FIGHT`, x shifted to 7176135 to sit over slide 8's
own title. `validate.py --original` passes.

**Slide 2 carried a duplicate eyebrow.** Two shapes with the same text: the
correct one (`Grammar 9`, black `tx1`, above the title) and a stray
(`Grammar 2`, salmon `E85F5B`, parked in the top-left corner over the pink
panel, where it was near-invisible but present). Innes asked for it to be
black; it already was — the salmon one was a second copy in the wrong place.
Deleted.

**The uploaded `.pptx` is therefore two shapes different from the file Innes
sent** — slide 8's eyebrow added, slide 2's duplicate removed — and the
download button serves that corrected copy.

### Branding: the logo, and where it can actually go

The deck arrived with no Forbes English mark at all. Precedent from the two
older pptx decks: **Star Wars puts it bottom-right on the cover only; Twin
Peaks also puts it in the bottom-right of interior slides.** Innes asked for it
"green like the website" — that is `--green-deep #1b3a28` and
`--green-light #4a8f61`, both straight out of `library.html`.

`logo-forbes-english_1.png` (692x360, RGBA, transparent) is the only usable
asset. The five files in `HOUSE STYLE/` are photographs of business cards.
Recolour by rewriting RGB and keeping alpha — a flat monotone mark, which is
what both older decks use.

**Placement had to be measured, not guessed.** This artwork is dark in almost
every corner: the bottom-left of the ten slides runs L=0.01 to 0.54 and the
bottom-right L=0.01 to 0.33, so neither green reads everywhere and there is no
one corner that works across the set. First attempt put the cover logo just
below the subtitle at 106px tall and "ENGLISH" landed in the treeline. What
worked:

- **Cover** — bottom-right, **on the black bag**, right-aligned to the page
  number above it. The bag is as close to pure black as the deck gets
  (median L=0.003), so the light green measures **5.4:1** — the best contrast
  anywhere on the ten slides.
- **Back page** — the identical corner and identical size, so the two pages
  book-end. Darkest patch there is L=0.055; same light green, **3.3:1**.

Same green on both, deliberately: different tints in the same corner on the
two pages read as a mistake. An earlier attempt put the cover mark in the
cloud strip under the subtitle in the deep green — legible at 5.2:1, but the
bag is both darker and the corner Innes asked for.

Interior slides carry no mark, matching Star Wars. Twin Peaks brands its
interiors, so **if Innes wants all ten, the per-slide colour has to be chosen
from the local luminance** — a single colour will disappear on some of them.

Worth knowing for next time: every *visible* run in this deck is Courier New.
The Arial that shows up in a naive font scan is only in paragraph defaults
(`defRPr`) and in two empty leftover boxes, `Prompt 7` and `Prompt 8`. Check
`<a:r>` runs, not `<p:sp>` shapes, before reporting a font inconsistency —
`Prompt 7` is still in the file, empty and invisible.

### Two departures from the twin-peaks viewer, both deliberate

- **Neighbour preloading.** At ~250KB a slide, every arrow press showed an
  empty frame while the next image downloaded. `warm(idx±1)` after each render.
- **Swipe.** A deck on a phone that only advances by hitting a 40px circle is a
  deck nobody reaches the end of. Horizontal intent is required
  (`|dx| > 45 && |dx| > |dy| * 1.5`) or scrolling flips slides.

Also: the back link goes to `library.html`, not `index.html`. Both older
viewers say "← Back to catalog" and point at `index.html`, which is the home
page, not the catalogue. **Those two are still wrong** — a one-line fix each,
not done here.

---

## The gap engine scored one blank per row — fixed, and swept clean

Found by play-testing Food A1 Part 1: a perfect run finished **18/19**. The
missing point was a dialogue line carrying two blanks.

`checkGaps()` marked a `.gap-row` by its **first** input and stopped, while
`maxScore` counted every input on the slide:

```js
rows.forEach(r => markGap(r.querySelector('.gap'), r.querySelector('.feedback')));
```

So a second blank in the same row was worth a point nobody could earn, and it
was never explained either: the learner typed both words correctly, watched the
score go up by one, and had no way to tell which half had supposedly failed. A
slide with several gaps and **no** `.gap-row` at all was worse — the fallback
branch marked exactly one input for the whole slide.

### The fix is in the engine, not in the content

The first instinct was to split every multi-blank row and add an assert to
`deck.gap()` forbidding them. That is wrong, and exam-prep is why: its
"Write the question" items read `______ she ______ an alien?` — the auxiliary
and the bare verb are **one** question, and splitting them into two rows
destroys the exercise.

`lesson-template.html` now has `markGroup(gaps, fb)`: it marks every input in
the group, and writes one piece of feedback naming **every** answer missed
rather than only the first. `markGap` no longer touches feedback at all. Both
branches of `checkGaps` go through it, so a slide with no `.gap-row` is handled
too. Behaviour for a single-blank row is byte-identical.

`deck.gap()`'s assert was relaxed to match: blanks must equal answers (a
mismatch is a builder typo), and multi-blank rows are legal again.

### Swept, at runtime rather than statically

A static sweep for `.gap-row` elements holding more than one `.gap` is the
wrong instrument now that the engine handles them — it reports false failures.
The right test drives the page: fill every gap on a slide with its own
`data-answer`, click Check, and assert the score chip rose by the number of
inputs.

```js
gaps.forEach(g => { g.value = g.dataset.answer.split('|')[0]; });
btn.click();
if (chip() - before !== gaps.length) /* unscorable */;
```

**46 files carry gap-fills. All 46 now score every gap.** Before the fix, seven
points were unreachable across three lessons, on top of the six in Food Part 2
and the one in Part 1:

| File | Was losing | Fix |
|---|---|---|
| `forbes-english-food-ordering-a1-part2.html` | 6 | rebuilt through `deck.gap()` |
| `exam-prep-5hour-courseEXP.html` | 5 | rebuilt; content unchanged |
| `alchemist_b2_lesson.html` | 1 | rebuilt; content unchanged |
| `forbes_english_lesson.html` | 1 | **no builder** — engine patched in place |
| `forbes-english-food-ordering-a1-part1.html` | 1 | dialogue restructured |

**`forbes_english_lesson.html` has no builder**, so its inlined copy of the
engine was edited directly. Its copy is an older variant — `fb.textContent`,
no full stop after the answer — and the patch was written to match rather than
to import the current shape. If a builder is ever written for it, that patch
disappears with the rest of the hand-edits.

### The engine lives inside every generated deck

`lesson-template.html`'s script is inlined into each build, so an engine fix
reaches a deck only when its builder is re-run. Every deck is now one rebuild
behind on `markGroup`. That costs nothing today — the runtime sweep says no
other lesson has a multi-blank row — but a deck rebuilt later will silently
pick it up, and one that is never rebuilt keeps the old code. Do not treat a
template fix as shipped until the affected decks are rebuilt.

Also worth noting: `check-lesson.js` passed all twelve gates on every one of
these files throughout. The ACTIONS gate asks whether a scored slide *can* be
answered, not whether every answer on it *counts*. **A thirteenth gate that
drives the page and compares the score chip against the input count is the
obvious next addition** — it is about fifteen lines, and it is the only one of
the gates that would have caught this.

---

## "Coming soon": a lesson with no hero is not available

Innes: *"Write coming soon on any lesson without a hero and make them
unavailable."* 66 of 237 catalogue rows have no entry in `LESSON_IMAGES`.

The rule is **derived, never stored**. There is no column, no list, no second
place to update: `comingSoon(l)` is `!LESSON_IMAGES[l.file]` in `library.html`,
and `coming_soon(row, images)` is the same test in `tools/seo.py`. A lesson
becomes available the moment its artwork lands in `LESSON_IMAGES` — which is
already the last step of every rebuild.

The correlation is worth knowing: **all 66 heroless rows are `deck=false`** —
every one is an old scroll page that has never been rebuilt. The converse is
not true, though: 124 non-deck lessons *do* have heroes and stay available. So
"no hero" is a much narrower rule than "not a deck", and it is the right one.

What "unavailable" means, concretely:

- **In the library** the card is a `<div>`, not an `<a>` — no href, no hover
  lift, `aria-disabled`. An `<a>` with no href is still focusable and still
  announced as a link; a keyboard user would have got a worse answer than a
  mouse user. Dashed border, greyed artwork, a `COMING SOON` ribbon across the
  image and a `Coming soon` badge where `Pro` would be.
- **Sorted to the end.** Interleaved, a third of the shelf was dead cards and
  the catalogue read as half-built. Stable sort, so the order inside each group
  is unchanged.
- **The count line** reads `171 lessons · 66 coming soon`.
- **Out of the index**: no sitemap entry, no line in `llms.txt`, not in the
  crawlable list inside `library.html`, and `<meta name="robots"
  content="noindex,follow">` on the page itself. `follow`, not `none` — the
  internal links are still worth crawling, and it all reverses when artwork
  lands.
- **`lesson-meta.json` carries `"coming_soon": true`** on those 66 entries. The
  Worker reads that file to build each gate page, so the flag is the hook for
  serving a real coming-soon page instead of an unfinished lesson. **The Worker
  does not read it yet — that change has not been made.**

Sitemap went 240 → 174 URLs. That is deliberate: an indexed result that lands
on an unfinished lesson is worse than no result, and Innes has said he wants
the site fixed before he drives traffic to it.

---

## Ordering Food & Drink A1 — Part 1 BUILT, and Part 2 repaired

`forbes-english-food-ordering-a1-part1.html` — **18 slides, checker clean,
19/19 on a play-through.** `build_food_a1.py` + `i18n_food_a1.py`. Catalogue
row `id 242`, A1, deck, pro, to match Part 2. Thumbnail
`FoodA1P1/two-at-bar.jpg`.

Innes attached the source after the artifact URL proved unreadable. What the
audit found in it, and what the rebuild did:

- **The answer key was in the HTML.** Every blank carried its own answer as a
  literal argument — `onclick="fillBlank('fib-1','table')"` — and the handler
  did not even use it. Answers now live in `data-answer` like every other deck.
- **Q6 failed ANSWERS and taught bad grammar.** 48 characters against a
  33-character field, and the key read *"I'm allergic to nuts. **Is** there any
  in this dish?"* — `nuts` is plural. A grammar error inside the key of an A1
  item is the worst place to have one. Rewritten to *"Does this dish have
  any?"*; distractors lengthened to close the gap, key never shortened.
- **No activation stage and no teaching.** Both added: three polite openings
  (`Can I…?` / `Could we…?` / `I'd like…`) and four words before any question.
- Key positions were already deranged — `[1,3,1,2,0,2]` — and the word bank was
  already not in gap order. Those two were fine.

### Light theme, and the two contrast measurements it needed

`extract-palette.py FoodA1P1/two-at-bar.jpg --light` passes every row
(`text on surface` 12.28:1). But a light theme puts **dark ink on artwork**,
and this set has hard black silhouettes in it. Two measured problems, two
targeted fixes, both in `build_food_a1.py`'s `HEAD_CSS`:

1. **Three of the six pictures have a dark band across the top** — a chalkboard
   menu, rows of pendant lamps. Sampling the rendered pixels behind the slide
   title with the text hidden gave **2.57:1 on ten of eighteen slides**. Fix:
   raise the template's top wash stop for this lesson from 26% of `--void` to
   88%, and pull the ramp down from 20% of slide height to 26% so it clears the
   title. Worst case after: 4.82:1. The middle 54% of the slide is untouched.
2. **Text sitting on the bare illustration** — question stems, order hints,
   word banks, the results lines — measured 2.5–3.0:1. Fix: the card treatment,
   as on the Geoscience and Nature Agency light decks. Not a heavier wash.

**Do not fix a light-theme contrast problem by dropping `--bg-opacity`.** That
bleaches all the artwork to save two text blocks, and it is the failure the
light theme exists to avoid. Plate the text instead.

The measurement script is worth rebuilding when needed: screenshot each slide,
set the text `color: transparent` (not `visibility: hidden` — that hides the
plate you are trying to measure), sample the element's central band (not its
full box — the 1px border and the rounded corners dominate the 5th percentile
and report a false failure), and compare against `--text`.

### Part 2 was rebuilt too

`build_food.py`'s hand-rolled `dialogue_slide` put all four inputs inside one
`.card` with no `.gap-row`, so **six of its eight dialogue answers did not
score** — a perfect run reached 19/25 instead of 25/25. It now goes through
`deck.gap()` like everything else, with each line rewritten to carry exactly
one blank and its own explanation. Rows had to drop to 8px vertical padding to
fit the canvas; the alternative was cutting a line out of the conversation.

Rebuilding it also pulled in ~9KB of template CSS added since Part 2 was last
built. That is expected — every generated deck is one rebuild behind the
template until someone re-runs its builder.

### The bar-artwork question, answered by building it

The earlier note flagged that five of the six images are bars rather than
cafés. Built anyway: the deck's language is café and restaurant language
throughout, the pictures are backgrounds rather than comprehension material,
and the one image with a chalkboard menu and a barman serving two customers
makes a better A1 cover than either of the food shots. If Innes disagrees, the
hero is one line in `build_food_a1.py`.

---

## Ordering Food & Drink A1 — Part 1 does not exist, artwork staged

**SUPERSEDED — Part 1 is built and live. Kept for the artwork notes and the
crop warning; ignore the "two decisions waiting" at the end, both were made.**

`forbes-english-food-ordering-a1-part2.html` is live (A1, deck, pro) with
`FoodA1P2/` and a full builder set — `build_food.py`, `food_mc.py`,
`i18n_food.py`. **There is no Part 1.** Checked four ways: no matching file, no
catalogue row, no lesson whose content is about ordering food under another
name, and nothing in git history. Part 2 never refers back to a Part 1 either,
so it is not orphaned — it was simply built first.

A lesson publicly numbered "Part 2" with no Part 1 is worth fixing, and A1 is
the level least able to work out what it has missed.

### Artwork is staged; the content is not reachable

Six images in `FoodA1P1/`: `tray`, `counter-till`, `bar-shaker`, `wine-bar`,
`two-at-bar`, `drink-sign`.

**All six arrived at 3376×1440 — 2.34:1, much wider than 16:9** — and are
centre-cropped to 2560×1440. Uncropped they letterbox and the cover title lands
in a black band. Same trap as `Impostor2/hero.jpg`; check the aspect ratio of
anything from this generator before deriving a palette.

**The content lives in a claude.ai artifact that cannot be read from here.**
`https://claude.ai/public/artifacts/f089b9e1-3a4d-4d46-ad0e-8ad80cea873f`,
titled `forbes-english-food-ordering-a1.html`. `WebFetch` returns page metadata
only, the rendered preview is blank in Chrome, the code view yields nothing to
`get_page_text`, and `javascript_tool` is blocked on that origin. Ask Innes to
attach the HTML rather than re-attempting the URL.

### Two decisions waiting

- **Go light, not dark.** Innes asked for backgrounds that are not so dark. The
  pattern that causes it: derive a dark palette, then drop `--bg-opacity` to
  ~0.40 to keep text legible, which leaves the artwork as a murky wash. These
  images are bright pink and blue and the **light** palette passes every
  contrast row (`text on surface` 12.66:1), which allows a much higher opacity
  and lets the artwork actually show. Prefer `--light` whenever the hero is
  bright rather than forcing a dark theme down.
- **Five of the six images are bars** — cocktail shakers, wine, spirits. Only
  `tray.jpg` and `counter-till.jpg` read as ordinary food service. That is an
  odd fit for A1, and possibly better suited to a B1/B2 bar lesson. Raise it
  before building rather than shipping an A1 deck set in cocktail bars.


## Why an image upload silently drops most of a batch

`mcp__claude-in-chrome__file_upload` caps a **single call at 10 MB combined**.
Innes's generated artwork is 2944x1648 PNG at 2.7-4.7 MB each, so a set of
eight is ~28 MB — nearly three times the limit. One image lands, the rest do
not, and it does not read as an error: the folder simply has fewer files than
the conversation did.

That is what happened to Grammar Jail. `c7e6cdb` committed exactly one file,
`escape-the-cliff.jpg`, and the lesson ended up leaning on it four times over.

**Convert before uploading.** JPEG at quality 88 takes those same images from
2.7-4.7 MB to 400-630 KB with no visible loss at deck scale — the whole set of
eight becomes 4.3 MB, one comfortable call:

```python
Image.open(src).convert('RGB').save(dst, 'JPEG', quality=88, optimize=True)
```

Check the count after uploading. `ls <folder> | wc -l` against what you were
sent is a two-second habit that would have caught this a week ago.

### grammarjail/ — eight new images, unwired

`arrival` (figure below the prison tower at sunset, flag on the wall),
`watched` (face behind a rig of camera lenses), `valves` (face among pipework),
`cliff-climb` (climbing a rope up the cliff below the lighthouse), `skating`
(the getaway, on skates), `cell-door` (figure framed in an open cell door, gull
on a block), `lookout` (sunglasses and a cigarette against the pipes),
`corridor-cat` (walking the pipe run, black cat watching).

They are **staged, not used**. `full_grammar_test.html` is a test page rather
than a deck and has slots for about two — its three current `grammarjail`
references are all SEO metadata, not visual content. Wiring eight in means a
redesign of a file another session was actively working, so it was left alone.
Palette from `arrival.jpg` derives clean, every contrast row PASS, if a deck
rebuild ever wants it.

**Now wired.** `full_grammar_test.html` is a 64-slide deck and seven of the
eight carry it — see below.

---

## Escape from Grammar Jail — rebuilt as a deck, in ten languages

`full_grammar_test.html`, **64 slides**, all eleven gates clean, same
filename. `lesson-template/build/build_full_grammar_test.py` +
`i18n_full_grammar_test.py`. Dark theme, palette verbatim from
`extract-palette.py grammarjail/arrival.jpg`, every contrast row PASS.

Cover `arrival.jpg`; the escape then runs across the deck as per-slide
backgrounds, uncaptioned — `cell-door` for the modals of obligation,
`watched` for preferences and plans, `valves` for predictions and the past,
`lookout` for the present perfect, `corridor-cat` for experience and
quantity, `skating` for the pronoun sections, `cliff-climb` for the adverbs,
the last section and the activation. `jail-test-room.jpg` keeps the
orientation slide and `escape-the-cliff.jpg` keeps the results screen.
`jail-cell-bars.jpg` and `jail-desk-window.jpg` are **still unreferenced**.

### `deck.py` has been clobbered too — the sixth stale base, and the first on a shared builder

`d11d5e1` ("Make every builder work from the repo, not /tmp") added two
things to `deck.py`, both described in its own commit message, in
`build/README.md` and in this file:

- `mc(..., explains=[...])`, so per-option feedback stops being an
  injection pass five builders each wrote by hand
- `assemble()` deriving `data-theme` from the palette's `--void`
  luminance, so a light deck cannot ship without the attribute

**`807e19c` ("Builders: Alcatraz, icon set, order/gap guards, translatable
card bodies") reverted both.** Its stated change is unrelated; its diff
against `d11d5e1` puts `def mc(...)` back to the version without
`explains`, and takes the luminance branch out of `assemble()`. Nothing
failed: no existing caller passes `explains=`, and a dark deck does not
need `data-theme`, so the loss is silent in exactly the way the
`library.html` clobbers are.

`git show d11d5e1:lesson-template/build/deck.py` still has both. Restoring
them is a small diff and a wide blast radius — `assemble()` runs for every
generated deck — so it wants its own pass with `check-lesson.js` re-run
across all of them, and it was **not** done here.

Until it is: `README.md` documents a `deck.py` that does not exist. A
builder that follows the README will `TypeError` on the first `explains=`.
**Check the function, not the README.** Grammar Jail carries a verbatim
port of the clobbered `mc()` in its own builder and says so.

### What the forty-five questions were doing wrong

All six of the recurring defects, and the counts are worth having:

| Defect | Count |
|---|---|
| Key at index 0 | **30 of 30** |
| Key is the only longest option | 1 of 30 (Q26) |
| Right and wrong print the same string | **45 of 45** |
| Rule stated only in the feedback | all 15 topics — there was no teaching stage at all |
| Hint set opens with its own answer | **10 of 15** |
| Marks correct English wrong / unanswerable | 4, plus 5 gaps rejecting a correct spelling |

Named, because they are the ones a future session should not re-introduce:

- **`It's Doris's book` was presented as a mistake**, keyed to `Doris'`,
  and explained as "when a name ends in -s, just add an apostrophe". It is
  standard English, and it contradicted the gap two questions earlier,
  which teaches apostrophe + s. Replaced with a real plural-possessive
  error.
- **`A: I have a headache. B: So do I.` was marked wrong** in favour of
  *So have I*. With lexical *have*, *So do I* is the ordinary answer.
- **`Have you ___ been to London?`** offered ever / never / yet / already.
  All four are grammatical there.
- **`I prefer the blue ___`** offered **dress** as a distractor.

Five gap answers were rejected although the item's own hint offered them:
**will not**, **have to**, **may**, **nor**, and *Tom's* with a curly
apostrophe. Expanded in the builder's `alts()`, not in the engine's
`gapOk` — a lesson that deliberately tests one spelling against another
would be broken by a blanket engine change.

And **five English feedback strings carried a German gloss inside them** —
*"'might not' = vielleicht nicht"*, *"already = schon"*, *"Whose =
wessen"*. Invisible to a Spanish learner, wrong for an English one, and
already said properly nine times over in `all_questions_i18n.json`. Same
shape as the `(= Blätter)` gloss found in the Stranger Things test.

### Per-question translations do not fit `UI_I18N`, so they are not forced in

`all_questions_i18n.json` is, per language, a 45x2 array — an L1 rendering
of the question and an L1 grammar note — with **no English column**. Two
things stop it becoming `data-i18n` keys, and the second is the one that
bites: `check-lesson.js` resolves a key by asking whether `UI_I18N.en[key]`
is **truthy**, so ninety keys whose English value is `''` would each report
as unresolved. An empty string is a legitimate value and the gate cannot
say so.

So the table stays in its own structure in the lesson, as `QUESTION_L1`,
and one `change` listener on `#langSelect` — registered after the engine's,
so `currentLang` is already updated — drives both layers. Each question
slide carries `<span class="q-l1" data-qi="N">` for the prompt, and the L1
note is **appended to every `data-explain` in that question's container**,
the slide-level one and each option's own, so it arrives with the feedback
whichever answer was picked. The engine still writes the feedback.

`ui_i18n.json` and `sections_i18n.json` *are* mapped onto deck keys, which
is where nine tenths of the ten-language coverage comes from for free:
`verdicts` become the four `res*` bands, `typeTags` become the orientation
cards, the fifteen section glosses become the eyebrows. Six strings were
written fresh — two activation briefs, three speaking prompts, a
placeholder. Everything else is lifted from `chrome_i18n.py` or from
`forbes-c1-negotiation.html`.

### `?lang=` without touching the template

The deck template always boots English. Rather than teach it about query
strings, the lesson sets `#langSelect.value` and dispatches `change` —
what a reader clicking the menu does — and keeps the URL in step
afterwards. `full_grammar_test_italian.html` still redirects to
`full_grammar_test.html?lang=it` and lands on the Italian deck, verified in
a browser.

### Layout is language-dependent, and only one language showed it

All eleven gates were re-run against a copy of the deck with each of the
ten languages forced on at load. Nine passed; **Russian overflowed the
activation slide by 5px**, because one speaking prompt wrapped to three
lines where every other language took two. Trimmed, and it is worth doing
this every time a deck ships more than two languages — `check-lesson.js`
measures whatever language the page boots in, which is always English.

```bash
python3 - <<'PY'
s = open('lesson.html', encoding='utf-8').read()
s = s.replace('</body>', '<script>(function(){var s=document.getElementById'
              '("langSelect");s.value="ru";s.dispatchEvent(new Event("change"));'
              '})();</script>\n</body>', 1)
open('_tmp_ru.html', 'w', encoding='utf-8').write(s)
PY
node lesson-template/check-lesson.js _tmp_ru.html && rm _tmp_ru.html
```

## Star Wars: the Courier New question, answered

Innes said the slide images were not in Courier New. They were not. The pptx
was correct at every level — 633 runs name Courier New explicitly, zero defer
to the Calibri theme, no embedded font parts — but **this container has no
genuine Courier New and cannot install one**. `ttf-mscorefonts-installer`
fails on `ModuleNotFoundError: No module named 'apt_pkg'`. What sits in
`/usr/share/fonts/opentype/couriersub/` is URW Nimbus Mono PS renamed to
"Courier New": 600/1000 advance, so metrically identical, so nothing reflows
and nothing looks broken — the glyphs are simply the wrong ones. That is
invisible from inside and obvious to anyone who knows the typeface.

`pdffonts` is the only reliable check. On a LibreOffice render here it reports
`BAAAAA+CourierNew-Bold`, which looks right and is not.

**The fix is to render from a PDF Innes exports on his own machine.** He sent
one (WPS Presentation, 960x540pt, 11 pages); `pdffonts` reports
`QKASJD+CourierNewPS-BoldMT` and `TYXLQB+CourierNewPSMT` — genuine Monotype.
`pdftoppm -r 150 -jpeg` gives exactly 2000x1125, which is the published size,
so no resampling is needed.

Do not re-render these eleven slides in this container. If the deck changes,
ask for a fresh PDF export.

### The logo lockup, and where it goes

"Forbes ENGLISH" is two objects, not one: `image2.svg` (the Forbes wordmark,
black, vector, **"Forbes" only**) plus a separate Courier New text run reading
ENGLISH at sz=2250. Anything that adds the logo has to add both.

On the cover the lockup sits at ink top y=1003px of 1125. On the interior
slides that position collides with the page number, which is a 20x13px block
at x 1895-1914, y 1065-1077 on every one of them. So the interior lockup is
raised to ink top y=925 (picture `<a:off y="5329682">`, text `y="5889117">`),
which stacks it above the number instead of over it.

Colour is chosen by sampling the destination: white on slides whose corner is
dark (presentation pages 2,6,7,8,11), black where light (3,4,5,9,10). Three
corners are half and half (pages 4,5,9) and get a soft opposing glow —
`outerShdw blurRad="34925" dist="0"` at 75% alpha in the pptx, a blurred
dilated alpha in the raster.

The site JPGs get the lockup **composited on top of Innes's PDF render**, so
the Courier New underneath is untouched. The stamp itself was cut from the
cover of that same PDF and keyed off the cream background, which is why the
ENGLISH glyphs on the interior slides are real Courier New too — they are the
cover's own pixels.

### Two traps in this file

`slide10.xml` is presentation page **11** (the KEY) and `slide11.xml` is page
**10** (WHICH?). Check `sldIdLst` before editing by number.

The cover's logo `<a:blip r:embed="rId1">` pointed at the **background
photograph**, not the logo; only the `svgBlip` fallback was right. Any renderer
without SVG support would have drawn a full-bleed still of Han and Chewbacca
into the corner. Fixed — it now points at `image13.png`.

---

## 2026-08-17 — the present-continuous pink and the present-simple navy were softened

Innes asked for "the pink and blue much softer/lighter". Shipped in three
commits: `d15af97` (pages), `539008a` (`lesson-template/`), `54e47f3`
(builders).

```
present continuous   #C2185B  ->  #E66085     soft rose
present simple       #16345C  ->  #7A93B5     soft slate
```

**The amount is derived, not chosen.** `lesson-template/soften.py` walks a
colour up an OKLCh path — raise lightness, drop chroma faster, hold hue —
and stops at the last step where `--accent` still clears 3:1 against its
own paper and `--accent-dark` still clears 4.5:1 as small text. That is
t=0.29 for the pink and t=0.49 for the navy. If Innes wants them softer or
firmer, change `FLOOR` in `soften.py` and re-run `apply_soften.py`; don't
hand-pick a replacement hex.

`apply_soften.py` moves every other member of each family along the same
path by the same t — the tints, the diagram gradient stops, the route-map
dots — so the ramps stay families instead of drifting stop by stop.

**Three things that will bite whoever changes a tense colour next.**

1. **Two roles, two floors.** Fills and gradient stops take the full t.
   Small text — `--accent-dark` on the italic examples and the retry
   button, the 11.5px diagram captions — takes t and then walks *back*
   until it clears 4.5:1 on its own paper. Softening those blind puts a
   caption at 2.9:1. `#7C8899` on camp two ends up unmoved for exactly
   this reason.
2. **Skip the non-accent tokens by declaration name.** Camp two's `--ink`
   is `#0C2340`, which is *also* a stop in its pyramid gradient. A blind
   hex substitution lightens the page's body text. `apply_soften.py`
   guards `--ink`, `--ink-soft`, `--paper`, `--card`, `--good`, `--bad`.
3. **The softened fills cannot carry white text.** White on the new pink
   is 3.3:1. Camp one, camp two and the route map each gained an
   `--on-accent` token (`#2E000D` and `#0A131F`) and every label sitting
   on an accent fill was repointed at it. Any new page using these two
   colours as a fill must do the same.

The Sherpa pages are hand-maintained references that build scripts splice
into, so the hexes live in **both** the HTML and the builder. Both were
rewritten. Changing only one means the next builder run silently restores
the old pink.

`library.html` was done by hand, not by the script: its pink appears in
the `.sherpa-banner` gradient, which carries white text and so takes a
smaller t (`#D23E6E` -> `#B25A76`), and in the 'Speaking activity'
category chip, which is not a tense colour and must not move.

### Measured, so nobody re-litigates it from a screenshot

On the route map the two route segments sit at **1.1–2.3:1 against the
mountain photograph in both versions**. The change moves the pink up
(1.08 -> 1.65) and the navy down (2.30 -> 1.73). Every segment is below
the 3:1 graphical floor before and after — that is a pre-existing route
map issue, not one this change introduced. Worth fixing on its own
ticket; the segments need a halo or a lighter plate under them.

### Open, for Innes to rule on

- The other eleven camps are still fully saturated, so one and two now
  read as a different generation. The same transform runs on them in one
  command if he wants the whole set softened.
- **Present perfect still forks**: the route map and camp four use
  `#1F6A70`; `tense-palette.css`, `mtb-perfect-vs-simple`, both Ecuador
  parts, impostor syndrome and `build_pp*.py` use `#0F6E56`. Both are
  published. Untouched pending his decision.

### Follow-up: the cards are renders too

Changing a page's palette leaves its library card on the old colours. The
Sherpa cards are static renders of the same diagrams, so the library kept
advertising the old pink for as long as it took Innes to notice. Four were
re-rendered in `4135216` and `dca520c`.

**Which cards are renders and which are artwork** — check before assuming:

| card | source | recolour with the page? |
|---|---|---|
| `Sherpa Tensing/thumb-route-map.png` | inline SVG | yes |
| `SherpaCamps/camp-one-ripple-rings.png` | inline SVG | yes |
| `SherpaCamps/descent-one-…-passive.jpg` | inline SVG | yes |
| `SherpaCamps/descent-two-…-passive.jpg` | inline SVG | yes |
| `SherpaCamps/camp-two-frequency-mountain.png` | **artwork** | no |

The test is one grep: if the page has `<img src="...">` pointing at the
card, the card is the source and nothing to regenerate. If the hero is an
inline `<svg>`, the card is a snapshot that has now gone stale. Camp two
is the only one of these five that is artwork — its navy belongs to the
illustration, not to the tense token.

Re-render with Playwright at **exact pixel scale** (set
`device_scale_factor` so the element's CSS width × dsf equals the target
width) rather than rendering at 3× and downsampling. Same crispness,
markedly fewer unique colours, smaller PNG.

Two things found while doing it:

- **Do not quantise these.** Palette-reducing the route map to 192 colours
  saved 250 KB and turned the orange and yellow segments muddy and the
  teal green — on a card whose entire job is colour coding. Full-colour
  PNG at 390 KB is under this library's 620 KB mean thumbnail.
- **The old route-map card was RGBA with the sky transparent**, so the
  library's card background showed through where the mountain wasn't. The
  new render is opaque. Not something anyone reported; visible only when
  the two are put side by side.

Unrelated but measured while surveying: `library.html` references **180
thumbnails averaging 620 KB, totalling roughly 110 MB**, the largest a
9 MB PNG (`Architecture/architecture-1-hero.png`). Worth its own job.

### The cover title was the actual complaint

Everything above is true and was still not the thing Innes could see. The
deck's *body* type was always Courier New; the **cover title was not**.
`QUESTION WORDS` rendered in a heavy metric-compatible slab, and once you
know to look, it is obvious next to page 2's `WHERE`.

Why: on page 1 of his export those words are not text. `page.get_images()`
returns thirty-odd small bitmaps — WPS rasterised them per glyph. The two
cover title shapes are the only ones in the file carrying **both** an
`outerShdw` on the run **and** a `<p:style>` block with `<a:fontRef
idx="major"/>`. WPS rasterises text with effects on PDF export, and when it
did, it drew them in the theme font rather than the run font. `Rectangle 3`
(the faint WHERE/WHO/WHAT column) rasterised too, for the analogous reason:
a `gradFill` at 12-24% alpha.

`<p:style>` is now stripped from both title shapes, shadow kept. If a fresh
export still comes back wrong, the shadow is the trigger and has to go.

**How the published cover was repaired without a re-export.** Every word on
that slide is a shape, so `ppt/media/image1.jpeg` is the artwork with no
text on it at all. Scale it to 2005x1129 and paste at (-4,-5) — that is
`Picture 4`'s xfrm — and you have a clean plate. Replace the title area
with it wherever the plate is brighter than luma 195, which keeps
Chewbacca's fur out of the patch, then draw the words back at the measured
baselines (173 and 300) and ink-left edges (1430 and 1482).

Draw them in **Courier New Bold extracted from Innes's own PDF**. The
embedded subsets have no `cmap` and no `name`, so rebuild those: the glyph
order is the standard Macintosh ordering, so `A`=36 and everything else
falls out of that. `/tmp` is not durable — the recipe is in this commit.

One glyph has to be made. `Q` appears nowhere else in the deck, so the
subset carries no outline for it. The one on the cover now is a genuine
Courier New Bold `O` with the tail from URW Nimbus Mono PS grafted on,
scaled so the two bowls match. Dilate the `O` by 3px, not 9, when
subtracting — at 9 the tail detaches from the ring.

## `arr.sort(() => Math.random() - .5)` is not a shuffle

Innes, on the Ukraine reconstruction lesson: *"The answers are all in sequence
and can quickly be guessed by a students."* He was right and the cause was not
where it looked.

All six of that lesson's multiple-choice keys were authored as option A. That
should have been harmless — the engine reorders options on first view — except
the reordering was the comparator idiom above. `Array.prototype.sort` is
entitled to do anything at all when the comparator is inconsistent, and what
V8 does with four elements is mostly nothing. Measured in this engine's own
runtime, 400,000 trials, for an element authored first:

| n | A | B | C | D |
|---|---|---|---|---|
| 4 | **35.9%** | 17.1% | 15.7% | **31.2%** |

Fair is 25%. "Always press A" scored 36%; "A or D" scored 67%. With every key
authored first, that held across the whole lesson.

The replacement is a sort by an independent random key —
`.map(v => [Math.random(), v]).sort((a,b) => a[0]-b[0]).map(p => p[1])` — which
is a drop-in for the same expression, so the sweep was textual and safe.
Maximum deviation from 25% after: **0.1 points, against 15.6**. The template
uses a named `shuffled()` Fisher-Yates instead; both are uniform.

**252 call sites in 93 files.** The idiom is gone from the repo.

### The authored positions were fixed too

A uniform runtime shuffle hides source order in the browser, but it still
leaks through print and PDF export. Fifteen lessons had **every** key on A —
130 questions; `stranger-things-b1-lesson` alone had 23. All dealt across the
letters with a deterministic per-file hash, balanced, no run of three.

### New KEYS gate

`check-lesson.js` gained a KEYS gate between LAYOUT and ANSWERS. It fails on
either half: one letter carrying ≥80% of the keys, or the comparator idiom
anywhere in the source. **The key-position half has to read the file, not the
DOM** — by the time the page is measurable the engine has already reordered
the options, which is exactly why this survived every previous check. Verified
failing against a deliberately broken copy first.

This closes the "no gate for key *position*" hole recorded earlier in this
file.

## A halo is one value; a hero is many

Innes, same message: *"some text is not visible without shadow behind or
glow."* There was already a glow. In a light-theme lesson it is white, and it
does nothing at all where the hero goes dark — on the Ukraine cover the same
shadow that lifts "Reconstruction" clear of the cream leaves "Presenting on"
invisible against the black building.

**How to measure this properly.** Do not blur the screenshot and call the
result the ground; on a small element the blur pulls in artwork from outside
the plate and the number is meaningless. Instead re-render with the text
elements set to `color: transparent` and the interactive furniture hidden,
screenshot that, and sample the real pixels under each element's rect. Then
WCAG-contrast them against the element's computed colour.

Ukraine before: **52 of 60 on-canvas text blocks** contained ground below AA
4.5:1, roughly a third of the area on a typical question stem, the cover
subtitle bottoming out at **1.44:1**. After: 7 blocks, none over 0.5% of area,
and that residue is the rounded corner of the plate rather than anywhere a
glyph sits.

The fix is a plate of `--surface` — what `.card` and `.opt` already sit on, so
both themes come free — applied to `.eyebrow`, `.slide-title`, `.q-stem`,
`.q-ctx`, `.order-hint`, `.slide-body > .prose`, `.cover-title`, `.cover-sub`
and `.act-target-label`.

**Grow the plate with a spread shadow, not padding.**
`box-shadow: 0 0 0 .34em <colour>` paints outside the border box and costs no
layout at all. The first attempt used padding plus a negative inline margin
and it was enough to tip the cover subtitle onto a second line.

Both changes are in `lesson-template.html`. Existing decks inline their own
copy, so only the Ukraine lesson has the plate so far — **every other
light-theme lesson with a high-contrast hero still has the halo**, and the
measurement script above is the way to find out which ones need it.

### Three archived copies have pre-existing JS syntax errors

`FORBES ENGLISH/forbes-english-lesson-2.html` (`Unexpected token '}'`),
`FORBES ENGLISH/-dinosaurs C1.html` (`Unexpected identifier 's'`) and
`FORBES ENGLISH/forbes-english-lesson-curious incident.html` (`Unexpected
identifier 'I'`) all fail RUNTIME, and did so before the sweep — checked
against `git show HEAD:<file>`. They are archive duplicates, not linked
lessons. Not fixed.

## The green text, and the mark that was never there

Innes: *"The green text is illegible."* Two separate faults under one symptom,
and the second was worse than the one he could see.

### 1. One status colour cannot do both jobs

`--ok: #3fbf7f` and `--no: #e8555f` sit in the "Fixed tokens — identical in
every lesson, do not edit" block, and they are used **both** as border/fill
colours **and** as text colours (`.feedback.ok`, `.feedback.no`,
`.gap.correct`, `.gap.wrong`). They are a mint and a coral chosen for a dark
canvas. Measured against the nine light palettes in this library they land
between **1.51:1 and 1.75:1** for the green and 2.30–2.66:1 for the red. That
is not low contrast; it is invisible.

The obvious fix — darken `--ok` — breaks the other job. Tried it: the correct
option's 20% fill went from a clear green tint to a three-level nudge,
measured `(224,212,189)` against a plain `(226,215,196)`.

So the roles are split. `--ok`/`--no` stay vivid for borders and fills;
`--ok-text`/`--no-text` are new and used for text. In the dark theme they are
`var(--ok)`/`var(--no)`; the light theme overrides them with

```css
--ok-text: color-mix(in srgb, var(--ok) 45%, var(--text));
--no-text: color-mix(in srgb, var(--no) 45%, var(--text));
```

Mixed toward the lesson's own ink rather than pinned to a hex, so it follows
the palette instead of needing re-derivation whenever the palette changes.
**45% is the ratio that clears AA 4.5:1 on every light palette shipped here** —
worst case 4.51:1 green, 5.55:1 red — while keeping the hue plainly green and
plainly red. Hand-derived hexes were tried first and thrown away: they were
tighter to 4.5 but froze the palette.

### 2. On every light lesson, the answer was never marked at all

```css
html[data-theme="light"] .opt { background: … }   /* 1 class, 1 attribute */
.opt.correct                  { background: … }   /* 2 classes  → LOSES */
```

`.opt.correct` and `.opt.wrong` were being overridden by the theme's base
rule. **Forty-four files.** Verified from the computed style, not by eye:
after answering, the key's background came back
`color(srgb 0.882 0.843 0.769 / 0.95)` — byte for byte the three distractors.
`.match-item.done` and `.match-item.miss` lost the same way.

Fixed by wrapping the theme base rules in `:where()`, which contributes no
specificity, so any two-class state rule wins:
`html[data-theme="light"] :where(.opt) { … }`. Prefer this to piling
`html[data-theme="light"] .opt.correct` overrides on top — the intent is that
state beats theme, and `:where()` says exactly that.

The ACTIONS gate never caught it because a marked `.feedback.show` also
satisfies the gate, and feedback text did appear — illegibly.

### `forbes-construction-contracts.html` was completely unscoreable

Found while gating the light lessons: **all six of its MC slides had no
`data-correct` at all.** Clicking did nothing, no feedback, no score. The keys
were recoverable without guesswork because every slide's own `data-explain`
names the answer outright — B, C, C, B, D, B. Set from those.

With keys in place the ANSWERS gate could finally see the slides, and three of
the six keys were the longest option (up to 1.51x). Distractors lengthened, as
the gate's advice says, rather than the key shortened. Its word bank also
listed the gap answers in gap order; sorted.

### Only nine lessons actually render light

Worth knowing before sweeping anything theme-related: 44 files contain the
`html[data-theme="light"]` block — every deck inlines the whole template — but
only **nine** carry `data-theme="light"` on the `<html>` element and therefore
render light. Test for the attribute on the tag, not for the CSS block:

`english_class_picture_description`, `exam-prep-5hour-course-part2`,
`exam-prep-5hour-courseEXP`, `forbes-construction-contracts`,
`forbes-el-zar-c2`, `forbes-english-food-ordering-a1-part1`,
`forbes-geoscience-phrases`, `forbes-nature-agency-part2`,
`ukraine-reconstruction-lesson`.

The `--ok-text` mix is harmless in the other 35 — the light block never
applies — and the `:where()` change is theme-agnostic.

### Still outstanding

The `.feedback.show` plate is on the Ukraine lesson only. The other eight light
lessons now have legible status text but it still sits directly on artwork, so
the plate treatment described above should follow.

## The red too — and the measurement that finally found all of it

Innes, after the green was fixed: *"The red also."* He was right again, and the
red was not the feedback text I had just fixed. It was `--accent-bright`
`#701c00` on the **Check button** and the **word-bank chips**, both of which
had `background: transparent` or a 16% tint into `transparent`. That ink reads
at **7.8:1 on the surface** and measured **1.53:1 to 1.94:1** where it actually
sat, which was on the artwork.

**A transparent background is a hole in the plate.** Plating the text elements
did nothing for text inside a component whose own fill is see-through. Fixed at
the base rule, not with a theme override — see the specificity note below.

### How to measure this properly — third attempt, and the one to use

1. Blurring the screenshot and calling it the ground is wrong: on a small
   element the blur pulls in artwork from outside the plate.
2. Sampling the element's whole rect is wrong too: a 1px accent border and a
   10px corner radius are inside the rect and nothing to do with the glyphs.
   That put the Check button at 3.01:1 when its ground was solid `--surface`.
3. **Right:** screenshot the slide twice, once normally and once with
   `* { color: transparent !important; -webkit-text-fill-color: transparent
   !important }`. Glyph pixels are where the two differ by more than ~18.
   Sample the *ground* shot at exactly those pixels. Then compare against the
   element's computed colour, with the WCAG large-text threshold of 3.0 for
   ≥18.66px or ≥14px bold, and 4.5 otherwise.

Also **skip disabled controls** — `.btn:disabled` is `opacity: .35`, so the
Check button reads 3.0:1 after it has been pressed. WCAG exempts disabled
controls, and treating that as a defect sends you chasing a deliberate design.

Run over all nine light lessons the audit found, and now clears: 0 of 154 to
814 text elements per lesson below threshold.

### Two more things it caught

**`.score-big`** — the 84px score on the results page — sat bare on artwork at
2.44:1. Now plated.

**The solid button's label.** `.btn-solid` sets `color: var(--void)`, correct on
a dark canvas where `--void` is the darkest token. Inverted, cream on the
accent red is 4.45:1 — under AA at 17px, which is not large text. Light theme
now uses `--surface` for that label: 5.00:1.

### The specificity trap, again, and why :where() does not save you here

My first attempt at the button was
`html[data-theme="light"] .btn { background: … }`. That scores one attribute
plus one type; `.btn-solid` scores one class. **The attribute counts in the same
column as the class**, so the theme rule wins on the type tiebreak, the cover's
Begin button lost its red fill, and its cream label went to 1.03:1. `:where()`
around `.btn` does not help — it zeroes the `.btn` part, not the attribute.

The audit caught it within one run of introducing it. If a component has
variants (`.btn-solid`, `.btn:hover`), change the **base declaration** and let
the variants override as they already do.

### The status ratio moved 45% -> 38%

45% cleared AA against `--surface` at full strength, but the feedback plate is
`--surface` at 94% and the artwork through the other 6% costs about a quarter
of a point — measured 4.25:1 to 4.39:1 on graded feedback across the nine.
38% carries the margin at ~4.9:1 worst case and is still plainly green and red.

**All nine light lessons now carry the plate**, not just Ukraine. The item left
open in the section above is closed.

---

## 2026-08-23 — Carrying the Load (C1), and three template defects it surfaced

New lesson, not a rebuild. Innes supplied a Liane Davey blog post on dealing
with a co-worker who does not pull their weight, and four Black Isler office
illustrations. Nothing from the post is reproduced: the four-rung escalation
model and the behaviour/impact/question unit are the ideas kept, and every
paragraph, example script and distractor is written fresh, with new names.

`carrying-the-load-c1.html` — 58 slides, 44 scored items in five sections
(8 comprehension, 8 anatomy, 8 escalation, 10 vocabulary, 10 grammar), plus a
five-paragraph reading, a four-rung reference, and an activation stage.
`build_carrying.py` + `i18n_carrying.py`. English and German interface;
the lesson content is deliberately monolingual — Innes asked for English only,
and the switcher translates the chrome, the section titles and the activation
briefs, which is what rule 5 and the checker actually require.

Catalogue row inserted in Supabase (`id 253`, access `pro`), `LESSON_IMAGES`
entry added to `library.html` on top of a fresh `origin/main` copy, `seo.py`
run last.

### Three defects, all in shared files, all fixed here

**1. `.q-ctx` was never styled.** `deck.py`'s `mc(ctx=…)` has emitted
`<p class="q-ctx">` since the argument was added, and no lesson had ever used
it. The template lists `.q-ctx` in the on-canvas plate rule and nowhere else,
so it inherited body sizing with no margin, and the stem's plate shadow painted
straight over it — the situational line was half-hidden under the question on
all eight escalation slides. `check-lesson.js` passed throughout: it measures
whether a slide fits, not whether two elements overlap. Rule added next to
`.q-stem` in the template.

**2. The branch-mode ledger showed on every deck.** `.ledger { display: flex }`
outranks the UA sheet's `[hidden] { display: none }`, so `DP 0 · TIME ••• ·
CLUES 0` rendered in the deck bar of a lesson with no ledger. The attribute is
the switch `ledgerInit()` throws; `.ledger[hidden] { display: none }` makes the
CSS respect it. Any deck built from the current template had this.

**3. `ledDp` / `ledTime` / `ledClues` had no home.** The same ledger's three
labels are `data-i18n`, but `assemble()` replaces the whole `UI_I18N` block with
the lesson's own module, so the template's copies are discarded and the checker
fails on "data-i18n with no English key". They are chrome, so they were added to
`chrome_i18n.py` for all ten languages rather than re-declared per lesson. Add
them to a module's `LIFT` to use them. Verified additive: rebuilding
`build_docket.py` with and without the change gives byte-identical output.

### Watch out

- **`tools/seo.py` cannot reach Supabase from a Cowork sandbox** — the egress
  proxy returns 403 on the tunnel, so it silently falls back to
  `tools/lessons.json`, and a lesson that exists only in Supabase gets **no SEO
  block at all**. Add the row to the cache as well as to the table. The cache
  was 244 rows against 248 in Supabase when this was written; it is stale, and
  appending is safe while a full refresh is not.
- ~~`check-library.js --vs-origin` fails on `lesson-template.html` and
  `sherlock-scarlet-star_3.html`.~~ **Both closed on 2026-08-26.** It was two
  problems sharing one message: the template is not a lesson and the gate now
  says so (`NOT_A_LESSON`, `c8e6a0b`), and `sherlock-scarlet-star_3.html` was a
  real finding the gate had been reporting all along — an unlinked pre-SEO draft
  of the Scarlet Star competing with the live page in search, deleted on Innes's
  instruction (`3645207`). The general lesson is worth keeping: **a
  long-standing "pre-existing, fails on clean main" failure is not
  automatically noise**, and quoting it forward unexamined is what kept a
  duplicate page live for months.
- `build_docket.py` no longer reproduces its shipped output: the template has
  moved on since it was built (902 insertions). Not investigated; the file was
  reverted rather than shipped.

---

## Escalating a Complaint (C1) — the builder has been reconstructed

`forbes-escalating-a-complaint-c1.html`, 21 slides, 34 scored points, EN+DE.
Supabase `lessons` row **255**, access `free`, deck `true`. `check-lesson.js`
exits clean; `check-library.js --vs-origin` reports no dropped entry.

**This entry used to say the page had no generator. It does now.**
`lesson-template/build/build_escalating.py` and `i18n_escalating.py` were
rebuilt from the shipped HTML, so the page is back under the normal rule: edit
the builder, re-run it, never hand-edit the generated file.

The history is still worth knowing. The session that first authored the deck
wrote a builder, an i18n module and a `lesson-template/textcontrast.py`
(glyph-level contrast audit) and lost all three when its container was
reclaimed; what survived was the self-contained preview HTML sent to Innes,
and the shipped page was reconstructed from it by swapping three inlined
`data:image/jpeg` URIs for repo paths. `textcontrast.py` is still gone — only
its finding survived, see below.

Rebuilding reproduces the shipped page's slides and `UI_I18N` block byte for
byte. Four things differ and all are understood:

- The `<!-- SEO -->` block is stripped, as by every builder run. `tools/seo.py`
  puts it back.
- Five palette tokens move by one unit in one channel — `--border`, `--accent`,
  `--accent-bright`, `--accent-dim`, `--contrast`. `extract-palette.py` is
  deterministic here, so this is Pillow rounding in the original sandbox. The
  builder records what the script emits today.
- `.q-ctx` and the reworded `.ledger[hidden]` comment arrive from the template,
  which moved on after the deck shipped. This deck uses no `mc(ctx=…)`.
- **`.bank-chip` went the other way, and was fixed rather than accepted.** The
  lost session had generalised the light-theme chip ground to both themes,
  after measuring every word-bank chip on the two gap slides and the activation
  slide at 1.38:1–3.03:1 against this deck's bright hero. That change existed
  only inside the shipped page's own copy of the stylesheet, so regenerating
  reverted it. It has been lifted into `lesson-template/lesson-template.html`
  (base `.bank-chip` rule now mixes into `var(--surface)`; the
  `html[data-theme="light"]` override it duplicated is gone), which is where an
  engine change belongs. Light decks are unaffected — the new base rule is the
  declaration the override already carried. **Every other deck now inherits it
  on its next rebuild.**

**One latent defect, deliberately left in place.** Nine `T['en']` values in
`i18n_escalating.py` are longer than the text the same key occupies in the
slides: `case3`, `case4`, `factNote1`, `factNote2`, `moves1`–`moves4`,
`proto2`. The HTML carries trimmed sentences, the translation table carries the
full ones, so switching to German and back to English swaps in longer copy than
the slide was laid out for. That is the signature of a hand-edit made to the
generated page after the layout gate complained. It was reproduced, not
repaired, so that the reconstruction could be verified against what shipped.
Closing it is a one-pass edit: pick one text per key, put it in the builder and
the i18n module, re-run `check-lesson.js`.

**Artwork is borrowed.** `--hero` is `DesignPitch/podium.jpg` and both
`data-bg` slides use `DesignPitch/pair.jpg`, so the palette in this deck was
derived from the Design Pitch hero, not from art of its own — and the library
card shares its thumbnail with `forbes-english-lesson-2.html`. Innes generated
four `conflict at work` illustrations (Noma Bar style, coral/slate) about
forty minutes after this deck was previewed; they are the obvious replacement.
That is now a small job: point `F`/`HERO`/`BG` at the new folder, paste in a
fresh `extract-palette.py` block, re-run the builder.

There is also a companion take-away that never entered the repo:
`escalation-audit-prompt.md`, an eleven-check audit prompt for a learner's own
escalation email. Innes has it locally. Worth a home here if the lesson keeps it.

### Fixed in passing

`carrying-the-load-c1.html` shipped while its Supabase `access` still said
`pro`; the flag was flipped to `free` afterwards. The card updated live, but
the page's JSON-LD kept `isAccessibleForFree:false` with a `.paywalled`
`hasPart`, and `library.html`'s crawlable index still read "— subscribers",
because both are written into files by `tools/seo.py`. `tools/lessons.json`
now says `free` and a `seo.py` run has corrected all three.

---

## Grammar Court B1 — audit and repair (2026-08-26)

Innes asked for a bug and grammar check on the live Part I page. All thirteen
gates passed, a headless walkthrough scored 41/41, and there were still seven
defects underneath — one of them site-wide. What follows is what changed and,
more usefully, why the gates could not see any of it.

### Every explanation printed its own i18n key

`data-explain="c1i1exp"` holds a **key**, and `feedback()` concatenated the
attribute raw. A learner answering question 1 correctly read:

> Correct. c1i1exp

All forty explanations in each deck, live, confirmed with a logged-in fetch in
Chrome. **No other deck in the library uses keys here** — the other ~200 write
the sentence into the attribute — so this was specific to the Grammar Court
revamp, which wanted explanations that translate.

Every existing gate passed it: EXPLAIN checks that a `data-explain` exists,
MARKUP checks that tags render rather than print, I18N checks that `data-i18n`
nodes resolve — `data-explain` is not one — and RUNTIME sees no error, because
there is no error. The deck still scored 41/41. **Nothing short of reading the
rendered feedback could see it**, which is exactly what the new gate does.

Fixed in the engine rather than by inlining the English, so the three
translations survive:

```js
const explainOf = v => (v && typeof v === 'string' && typeof UI_I18N.en[v] === 'string')
  ? t(v) : v;
```

A written explanation is a sentence and can never collide with a key name, so
this is inert on every deck that writes literal text. It is in
`lesson-template.html` — the authority — and in the two decks that need it now.
**The other ~200 lesson files still carry the pre-change engine.** That is safe
(the change is purely additive and they use no keys) but it is a real
divergence: they pick it up on their next rebuild from the template, not
before. A blanket propagation across every deck is a deliberate operation of
its own and was not done here.

`fillFeedback` also grew a third argument so a **single gap** can carry its own
`data-explain`, appended after the row's. `c4i4bexp` existed in all three
languages and was referenced nowhere, because one `.gap-row` holds one
`.feedback` and the participle half of *had ... eaten* had no way to be
explained at all.

### New gate: RESOLVE

`check-lesson.js` now answers every `mc` and `gap` slide and reads what comes
back. If anything the slide names in `data-explain` — on the row, on an option,
on a single gap — appears in the rendered feedback verbatim, it fails. Only a
key can trip it; an explanation contains spaces.

Verified the way this project requires: **the gate fails on the exact file that
shipped** and passes on the corrected one. It runs last, after every other
measurement, because it answers the paper to do its work. Checked against ten
other decks and the template for false positives — none.

### Two answer-key defects

- **Part I question 10** had two correct answers. *She \_\_\_ be happier if she
  \_\_\_ a job she enjoyed* keyed `would … found` while also offering
  `would … had`, and *if she had a job she enjoyed* is ordinary second
  conditional. Options shuffle, so a learner who reasoned correctly was marked
  wrong at random. The distractor is now `would … has`, the present-simple
  if-clause the case actually teaches, and the explanation no longer argues in a
  circle ("«Had» is wrong because we need the past simple of «find»" — nothing
  in the stem asked for *find*).
- **Gap tolerance.** `couldn't` and `didn't` accepted only the contraction, so
  *could not* and *did not* — correct reported speech — were marked wrong.
  Expanded in the data (`data-answer="couldn't|could not"`), never in `gapOk`;
  Part II already did this properly.

Part II's third-conditional distractors are mixed conditionals and therefore
real English (*if you hadn't told me, I wouldn't know* is arguably better than
the key). Those items are ordinary exam convention and stay, but `c2i3exp` now
says so in all three languages instead of leaving a right answer unmarked.

### Question numbering

Part I labelled its questions 1–18, then jumped to 24 and ran out at 40 against
a 41-point deck: the labels implied the five gap rows were items 19–23, but item
4.4 is worth two points. Both decks now number **multiple-choice questions
1–30**, which is what Part II already did and which cannot drift from the score.

### Site-wide: the gate page double-branded every Pro lesson

`tools/seo.py` wrote `page_title(r)` — the brand-suffixed `<title>` — into
`lesson-meta.json`. `personaliseGate()` in `src/index.js` uses that value for
the gate's `<h1>`, its `og:title` and its JSON-LD `name`, **and appends the
brand again** for `<title>`. Anonymous visitors and crawlers got:

- tab title: `Grammar Court — B1, Part I | Forbes English | Forbes English`
- `<h1>`: `Grammar Court — B1, Part I | Forbes English`

**194 of the 260 entries carried the suffix.** The other 66 escaped only
because `page_title()` drops the brand when the line would run past 65
characters, which is why it read as a handful of odd pages rather than as the
default. These are the indexed public faces of every Pro lesson.

`seo.py` now stores `clean(r['title'])`; the Worker adds the brand in the one
place that decides how a gate page is labelled, and gained an `og:site_name`.
249 titles were rewritten in `lesson-meta.json` (the brand on 194, plus the
`(level)` suffix `page_title()` appends, which the gate already shows in its own
eyebrow).

**`lesson-meta.json` was rewritten in place rather than by running `seo.py`.**
Do not run it casually: on a clean checkout it also rewrites
`forbes-english-dinosaur-minecraft.html`, which carries hand-written SEO tags
with no `SEO:start`/`SEO:end` markers, so the run **injects a second, duplicate
SEO block and replaces the `<title>` with a worse one**. That trap is still
there and is worth fixing before the next full run.

One row of `tools/lessons.json` also disagreed with the live table —
`forbes-english-dinosaur-minecraft.html`, cached as *"Dino-Craft: C1 English
Expedition (Minecraft ed.)"* against *"Dino-Craft Part I: The Expedition"* in
Supabase and in the page's own `<title>`. The table wins; the cache row was
corrected. Everything else matched: files, levels and access all hash identical
to the live table.

### Smaller things

- Four result strings (`resPerfect`/`resStrong`/`resMid`/`resLow`) were defined
  twice per language in both decks — the template's generic set, then the
  courtroom set. The later literal won, so the right one showed; the shadowed
  copies are gone.
- *"The Past Simple is **always** used with specific past time expressions"*
  overstated the rule — a past continuous takes one too (*at 8pm yesterday I
  was watching…*). Softened in all three languages.
- Spanish: *«tu pareja»* reads as a spouse. The activation is pair work, so
  *«tu compañero»*. Both decks. *«en parejas»* for the activity itself is fine.
- Straight and curly apostrophes were mixed, sometimes on one slide — Case 3's
  eyebrow said `can't` and its body `can’t`. Normalised across the slide text
  and the `UI_I18N` strings. Attribute values were left alone, and gap answers
  are unaffected either way because `flatten()` normalises both sides.

Supabase rows 192 and 193 already had `deck = true`; the post-publish step from
the revamp note was done.

### The `seo.py` duplicate-block trap is closed (2026-08-26)

The note above said a full `seo.py` run would give
`forbes-english-dinosaur-minecraft.html` a second SEO block. It would have:
that page's tags were written by hand and carried no `<!-- SEO:start -->`
fence, so `inject()` fell through to its "insert after the viewport tag" branch
and added a whole second block — a second canonical, a second `og:title`, a
second `LearningResource` — while the run printed a cheerful *"rewrote 1 page"*.

Two changes, because one of them is the file and the other is the class:

- **The file is fenced.** Its existing tags are now wrapped in
  `<!-- SEO:start -->` / `<!-- SEO:end -->`, so a run replaces them like any
  other lesson. Verified: after fencing, a real run rewrites it in place with
  exactly one canonical, one `og:title`, one `ld+json` and the right `<title>`.
- **`inject()` refuses instead.** It now returns `None` when a page has no fence
  but already carries a canonical or an `og:` tag, and the run prints a warning
  naming every such file rather than duplicating silently. A refused page still
  gets its `lesson-meta.json` row — only the file write is skipped, because
  dropping the row would hand that lesson a generic gate page.

Verified both ways: the guard fires on the pre-fence file (untouched, named in
the warning, row still in `lesson-meta.json`), and does not fire on any of the
other 259.

Two stale values were fixed by hand at the same time, both from the same source
— the Dino-Craft Part I title change that never made it out of Supabase:

- `library.html`'s crawlable list and `llms.txt` still showed *"Dino-Craft: C1
  English Expedition (Minecraft ed.)"*. One line each.
- `lesson-meta.json` named `/minecraft/3gaje02rloj51.png` as that lesson's
  image, where `library.html` has said `minecraft/dc1-hero.jpg` since the
  thumbnail was repointed at real artwork. The gate page and every share card
  were serving the old screenshot.

**`sitemap.xml` and the auto-generated descriptions were left alone.** The
sitemap diff is `lastmod` churn only, and `describe()` would replace the
hand-written *"A player's monument to the apex predator — built one block at a
time."* with a truncated sentence off the page. Both are Innes's call, not a
defect.

## Reading the Elevation (C1) — built 2026-08-30

`reading-the-elevation-c1.html`, 29 slides, 40 points, EN + DE. New lesson from
a mixed vocabulary list Innes supplied; the ~36 architecture items in it are the
syllabus. Builders: `lesson-template/build/build_elevation.py` +
`i18n_elevation.py`. Cache row id 276, access `free` — **the Supabase row still
has to be added by Innes**, `tools/seo.py` could not reach the table from this
container (403 on the tunnel) and fell back to `tools/lessons.json`.

Five Black Isler architectural illustrations came with it. The Noma Bar
cantilever is the hero at 0.51 mean luminance, so house style §4a puts it in the
LIGHT theme; `extract-palette.py --light` returned the building's own navy as
the accent and its coral as the secondary, every contrast row PASS.

Three things worth carrying to the next deck:

- **The MC key is rotated to `n % 4` at build time**, not shuffled. Same finding
  as The Last Mile: authoring every item with the key first is readable, but the
  source order survives into the PDF export and the KEYS gate fails on it.
- **A shared alphabetical word bank can still leak an answer key on one slide.**
  The bank spans all three gap slides, and the BANK gate reads each slide
  separately — the third slide's two answers sat at bank positions 2 and 3,
  ascending, until the rows were reordered meticulous-then-liminal.
- **The activation slide overflowed by 59px** and no other slide did. Cutting
  five speaking prompts to four fixed it. Check the overflow in GERMAN too: the
  checker only measures the language it loads, and German runs longer than
  English on every brief.

### Preview note: a repeated `data-bg` costs a full base64 copy each time

Inlining the artwork naively for the self-contained preview produced **3.4 MB**
from 725 KB of actual image, because the four per-slide backgrounds are
referenced 21 times and each reference carried its own copy. Storing each image
once in a map and resolving the tokens with a shim injected before the engine
script takes the same file to **0.84 MB**. Verified standalone with the network
blocked in Playwright — no JS errors, every slide's `--hero` resolves to a data
URI. Worth doing on any deck with more than a handful of `data-bg` slides; the
existing "no slide may reuse a background" note explains the cost but not the
fix.

## 2026-09-02 — Block Camp colour: two defect classes, both now gated

Two things that had gone unseen across the whole line, found only because
Innes kept reporting single instances.

**A negator wearing somebody else's colour.** Eleven negators were tagged
`.aux` or `.modal` and printed green or orange beside the auxiliary they are
supposed to contrast with — `have not seen`, `was not listening`, `does not
matter`, `will not agree` — across seven decks. Four decks had no `em.neg`
rule at all, so a negator on them had nowhere to go. `check-colour-roles.py`
now carries a **NEGCOLOUR** gate: any `not` / `n't` / `never` in a role span
that is not `.neg` fails. It found the two `.modal` ones on its own after the
first nine were fixed.

**A bare infinitive after do-support left unmarked.** `don't build`,
`did not go`, `does not matter`, `may not be` — the auxiliary and the negator
were marked, the verb they govern was not. Fixed in four decks. Not yet
gated; the shape is `<em class="aux">do/does/did</em>` (optionally a negator)
followed by a bare lowercase word, and it is worth a gate next time somebody
is in this file.

**Contrast has to be measured off the RENDER, not off the token.** Two
reports this week were the same bug wearing different clothes: Present Simple's
formula pill (a translucent plate over lit artwork, so `am/are/is` measured
4.78:1 despite a token that passes against `--surface`) and Past Simple's
`was/were` (the route map's brown #B08968 on a deck themed brown — 3.4:1).
Every gate we have compares token against token and can see neither. The lift
for the brown was derived mechanically rather than picked: L\* raised in Lab
with hue and chroma held exactly, stopping at the first step clearing 5:1,
giving `--t-past-ink: #D5AB89` local to that deck while `--t-past-simple`
keeps its published value so the TOKENS gate still holds the line together.
**A render-time contrast check — sample ink against its actual composited
background, per slide — is the single highest-value gate still missing.**

**Innes's slide numbers can run one ahead of `shots.js` indices.** On
present-simple and present-continuous they matched exactly; on past-simple
"page 6" was slide 5 and "slide 7" was slide 6. Check the content matches the
report before assuming the index does.

Still open, and still the root of most of the round trips: **whether the `be`
inside an illustrative sentence wears its tense colour.** 33 cases,
`check-unmarked.py --review` lists them. It is a teaching call, not a defect,
and until it is made the same report keeps coming back one slide at a time.

### 2026-09-02, later — past simple forms were gold, and the brown needed lifting on three decks

Innes: "past simple verbs should be brown not gold". They were not marked at
all — bare `<em>`/`<b>`, which the decks paint with the accent — so `went`,
`took`, `studied`, `-ied`, `worked`, `exploded` all read as the deck's
"learn this" gold rather than as the tense. 56 forms marked `.t-past` across
**past-simple (28), past-simple-2 (17) and past-continuous-2 (11)**; the
last of those because the standing ruling is that a past simple clause inside
a past continuous sentence is brown. `did` and `BASE VERB` stay gold — the
bare infinitive after do-support is a different thing and is correctly gold.

All three decks needed `--t-past-ink: #D5AB89`, the mechanically lifted brown
(L\* raised in Lab, hue and chroma held), because #B08968 measured 3.4 / 4.4 /
4.2 : 1 off their renders. **On past-continuous-2 the lifted brown sits closer
to that deck's yellow than it does elsewhere** — it works because the yellow
is on the -ing verb and the brown on the past simple clause, in separate
cards, but if the two are ever set in one phrase that pairing needs looking
at rather than measuring.

Two consequences worth knowing:

- **The AUXJOB gate had to be narrowed.** Its paradigm-cell rule and its
  not-followed-by-a-verb rule were reading tense classes as auxiliaries, so
  every correctly-marked `went` / `came` / `had` became a finding. Wearing
  `.aux` claims "I am a helper"; wearing a tense colour claims "I carry the
  tense", which a main verb does. Those two rules now read `.aux|.modal`
  only. Verified still firing on a broken copy. The cost is recorded in the
  file: a descent deck's be wears `t-pc`, not `.aux`, so it is no longer
  checked for following a non-verb.
- **The escaped-dictionary quoting trap bit twice in one session.** Adding a
  class to a `<b>` that also lives in a JS dictionary string writes
  `class="t-past"` into a double-quoted string and kills the deck's JS.
  `check-lesson.js`'s RUNTIME check catches it both times, so it is gated —
  but the fix is to escape the quotes on any line matching `^\s+key: "` in
  the same pass, not afterwards.

Still not gated: **a past simple form left unmarked.** It needs a verb list to
detect, which is why it went unseen. Worth doing next time somebody is in
`check-unmarked.py`, restricted to decks that define `--t-past-ink`.

### 2026-09-02, later still — what the green means, settled

Innes, on the past continuous: "maybe was & were should be a brighter yellow
instead of green". Done, and it closes the rule he had already half-made on
Present Continuous 2 ("why are we making is green? lets make them pink").

**The rule, in one line: the be that MAKES the tense wears the tense. Green is
the helper that carries no meaning of its own.**

- `was` / `were` + -ing → `--t-past-continuous` #F1D779 (59 spans across the
  two past continuous decks). Deliberately the published tense yellow, not the
  deck accent: the accent is the same yellow pulled down at hue 52 for body
  text, so the be now comes out a shade brighter than the -ing verb it helps —
  which is right, since the be is the half that inverts for a question and
  takes the negative.
- `is` / `are` / `am` + -ing → the present continuous pink (done earlier).
- The be that IS the verb → its own tense (brown in past simple, slate in
  present simple).
- **Green `--mark-aux` #46d98a is now: `do`/`does`/`did` do-support, and
  `have`/`has`/`had` in the perfects.** That second group is the one still
  unruled — if a perfect's `have` is half of the tense the way a continuous's
  `be` is, it should go turquoise, and the same argument applies. Worth
  putting to Innes as one question rather than one deck at a time.

**`going to` is a different green** — `--t-going-to` lime #70A43A, 111 spans.
Except on **future-simple-2**, which had never been given the going-to rule at
all: 18 chains wore the auxiliary mint as one lump, so `is going to` read as a
single helper. Split per the standing ruling (be blue, `going to` lime,
infinitive gold), and the two cue rows on slide 7 that stand in for "going to"
went lime with them so the ladder and its pill agree. That deck needed
`--t-going-to-ink: #7BAF44` (published lime measured 4.0:1 on its warm cards)
— the third deck-local lift this session, same Lab method.

**Three decks now carry a lifted ink token** (`--t-past-ink` ×3,
`--t-going-to-ink` ×1) because a published tense colour failed against that
particular camp's surfaces. The pattern is now clear enough to name: **a tense
colour is a system value, but the ink a deck paints with is a per-deck
measurement.** Keep the published token as-is so the TOKENS gate holds the
line together, and add `--<tense>-ink` beside it when the render says so.

### 2026-09-02, last — the perfect's have goes turquoise, and green is now do-support alone

Innes: "Present perfect have go turquoise - I concur." 110 spans across five
camp decks, plus the eight descent stations via the builder. `--mark-aux`
green fell from 255 spans to 74, and every one of those 74 is now do-support
or a commentary copula. The system's three sentences are in
`docs/COLOUR-RULES.md`; the reference page is `docs/colour-rules.html`.

Four things came out of it that a future session needs:

- **`build_descent.py`'s auxiliary pass was not quote-aware.** `AUX_SPAN`
  matched `<em class="aux">` and nothing else, so 37 auxiliaries inside the
  JS dictionary strings — written `class=\"aux\"` — came through green while
  the English slide was correct. The German and Spanish versions of eight
  stations had been wrong since the pass was written. It is also now
  case-blind: a sentence-initial `Have` was missed for the same reason
  (`AUX_LOOKUP` is all lower case). **This is the third time this session
  that the escaped-dictionary quoting trap has bitten** — CLAUDE.md warns
  about it for hand edits, but the builder had the same bug inside it.
- **A role colour on a solid accent plate is a blind spot.** Present
  perfect's dictum had the participle violet on the turquoise fill at
  **1.18:1** — invisible, on the takeaway line of the slide that teaches the
  participle. Every other measurement this week was ink on a dark
  translucent card; nothing looks at the one place the ground is light and
  opaque. Fixed by keeping the hue and dropping the lightness
  (`#B39BF5` → `#4B3B8A`). It is the only dictum in 24 decks carrying a role
  span, so this is one rule, not a class — but a gate for "role colour
  inside `.dictum`" would be four lines and would have caught it.
- **The AUXJOB gate earned its keep again**: it found `We have had the flat`
  with `had` — the participle of the main verb — wearing the auxiliary green,
  the moment the `have` beside it changed colour.
- **Turquoise on a turquoise camp.** `#70E0E0` sits 41–58 in RGB from the
  four perfect decks' own `--accent-bright` — the closest pair in the system,
  closer than the brown/yellow one flagged earlier. Not a legibility problem
  (8.4:1) but in a formula pill the marked `HAVE / HAS` and the generic
  `VERB-ING` slot now look alike. Lifting the turquoise does not help: it
  goes white before it separates. If it needs fixing, quieten the pill's
  generic slot, not the tense. Raised with Innes; not acted on.

Also: `borrowing` / `leaving` on present-continuous-2 slide 7 are pink, and
the `WAS / WERE + -ING` label on past-continuous-2 is yellow, both for the
same reason — the form the slide names should wear the colour the slide
teaches.

### 2026-09-02 — `tools/seo.py` deletes lessons it has never heard of

Merging Innes's `long-way-home-rpg` push and then running `seo.py`, as the
pipeline says to, **removed the new lesson from `library.html`, `llms.txt`,
`lesson-meta.json` and `sitemap.xml`**. Caught in the diff before it was
committed; nothing shipped.

The cause: in a cloud session the Supabase fetch fails on the proxy and
`seo.py` falls back to `tools/lessons.json`, a cache that predates the new
lesson. It then regenerates the crawlable index from that cache and deletes
every entry the cache does not contain. The run reports success. It prints
`! supabase unreachable (…) — using tools/lessons.json`, and that line is
the only warning you get.

This is the same shape as the `library.html` clobber already documented, but
worse, because the pipeline says to run `seo.py` after **every** build
without exception — so it will happen again to whoever pulls a lesson added
from Innes's machine. Recorded in CLAUDE.md next to the pipeline.

**The fix worth making**: `seo.py` should refuse to REMOVE an entry when it
is running off the cache — additive-only in fallback mode. Deleting on the
strength of a stale cache is never right.

### 2026-09-02 — the hub hardcodes the Free/Pro tag

Making Past Simple 1a free changed the database row and everything that
reads it: `library.html`'s grid (which pulls `access` live from Supabase via
`sb-client.js`), the crawlable index, the gate page, and the deck's
`isAccessibleForFree`. **`block-camp.html` did not**, because its Free/Pro
tag is typed in by hand, once per thumbnail, with nothing linking it to the
column it reports. The front page of the line contradicted the paywall, and
it surfaces as "it still says pro", not as an error.

`lesson-template/checker/check-access.py` now compares all 24 hardcoded tags
against `tools/lessons.json`. Verified firing on a broken copy, both ways it
can fail — a wrong tag, and a card with no tag. **Run it whenever an access
flag moves.**

Three separate "a hardcoded duplicate of a fact drifts from the fact" bugs
turned up in one session: the hub's access tags, the `.aux` markup inside the
descent's JS dictionaries, and `tools/lessons.json` versus Supabase. The
pattern is worth naming: **anything typed twice will disagree eventually, and
the second copy is always the one nobody looks at.** Where the duplicate
cannot be removed, gate it.

Also: the hub's Camp I note said "Part 1 free", which claims all eight Part 1
decks are free. Five are not, and that predates this change. Now "Part 1 free
on units 1–3", matching the descent's "station 9 free". It is sales copy —
Innes may reword it.

**How to change an access flag** (the full list, in order):
1. `update lessons set access = '<free|pro>' where file = '<deck>.html'` in
   Supabase — the Worker enforces this one and nothing else does.
2. The same field in `tools/lessons.json`, or the next cloud `seo.py` run
   reverts the indexes off the stale cache.
3. `python3 tools/seo.py`, then **read the diff** on `library.html`,
   `llms.txt`, `lesson-meta.json` and the deck itself.
4. The hand-typed tag in `block-camp.html`.
5. `python3 lesson-template/checker/check-access.py` — must pass.

### 2026-09-02 — adding a language is translation volume, not engineering

The decks were already built for this and nobody had noticed. Every deck
declares all ten languages in `LANGS`, `RTL_LANGS = ['ar']` is in place, and
`initLang()` only offers a language whose `UI_I18N` block is as long as
English:

    LANGS.filter(l => l.code === 'en' ||
                      Object.keys(UI_I18N[l.code] || {}).length >= enKeys)

So a language appears the moment its block is complete and never before. No
engine edit, no CSS, no build change. The Sherpa Tensing pages already run
the full nine (`de es fr it pt ru ar zh ja`) on a different mechanism
(`EX_TR` + `TR_ORDER`), which is where the target set comes from.

**The size of the job, measured across the 24 decks:**

| surface | strings per language |
|---|---|
| `UI_I18N` keys | 1,461 |
| always-on `.sup` glosses (ES/DE inline) | 643 |
| `BW_TR` word-bank entries | 1,735 |
| **total** | **3,839** |

Seven languages to reach the Sherpa set is **26,873 strings**. The eight
passive stations carry only 3 `UI_I18N` keys each because their content is
generated — those go through `build_descent.py`, whose `CHASSIS_LANGS` is
still `('en', 'de', 'es')`.

**`lesson-template/i18n_tool.py`** does the mechanical half:

    i18n_tool.py extract <deck> [lang] > out.json   # HTML unescaped for a translator
    i18n_tool.py merge   <deck> <lang> <in.json>    # re-escapes, refuses a short block
    i18n_tool.py status  [decks...]                 # which languages are complete

Two traps it now handles, both found by using it:

- **The empty stubs shadow you.** Each deck ships the eight unwritten
  languages as one-line stubs at the foot of `UI_I18N` (`fr: {},`). A block
  written above one of those is silently overridden — a later key in an
  object literal wins — so the language stays empty, the switcher goes on
  hiding it, and the merge *looks* like it worked. The tool writes into the
  last block, deletes any earlier duplicate, and refuses to leave more than
  one behind.
- **`slideOf` and `wordCount` are functions**, not strings. Omit them and the
  block is two keys short of English, so the language never appears. They are
  carried across and reported, because the plural rule needs a human.

**Ten keys stay in English by convention** — checked against the ES and DE
blocks, which agree: `beA`, `beB` (the paradigm cells `was`/`were`),
`beNote`, `didNote`, `edNote`, `irNote` (the formula plates show English
grammar), `coverTitle`, `chipFocus`, `ledDp`, and `actPlaceholder` (the
learner writes in English).

**French is done on `blockcamp-past-simple.html`** — the free flagship, 108
keys. Verified: the switcher offers Français, `documentElement.lang` follows,
and every slide was measured for overflow in French. Slide 22 reports 22px
past the deck bar, but so do English, German and Spanish — it is the
`.slide-body` container's own box, pre-existing, and nothing visible crosses.

**Still to decide, and it is not a coding question:** `ru`, `ar`, `zh` and
`ja` are learner-facing pedagogical glosses. A wrong one teaches a wrong
thing, and the completeness guard means a *wrong* language is worse than a
missing one, because it ships. Those four want a native-speaker pass before
they go live.

### 2026-09-02 — all sixteen camp decks in nine languages

`UI_I18N` is done: every Block Camp I deck now offers **en de es fr it pt ru
ar zh ja**. 113 language blocks, ~12,100 strings, produced by a Workflow
fan-out and merged with `lesson-template/i18n_tool.py`.

**Run `i18n_tool.py status` rather than trusting your own notes.** I merged
six languages into `future-simple`, merged only Arabic into
`future-simple-2`, and then wrote a commit message saying both were done.
Only the status command caught it.

**The verification that actually mattered was not the one I designed.** The
workflow's adversarial verify stage died almost entirely on a session limit
(97 agents done, 111 errored). What validated the blocks was a structural
gate (keys, function keys, `keep_english`, HTML class lists) plus rendering,
and rendering found every defect that mattered:

- **The Arabic slide counter read backwards.** `"5 / 22"` is three bidi runs,
  so RTL reorders them to `22 / 5`. The string is correct; only the render is
  wrong. Fixed with U+2066/U+2069 isolates, applied inside `i18n_tool.py` so
  it holds for every Arabic block — see `rtl_isolate()`.
- **Wrapping titles.** A title that fits one line in English wraps in most
  other languages and pushes the body 4–8px through the deck bar. Hit
  past-simple 6, present-continuous-2 8, past-continuous-2 5. Japanese
  overflowed *most* on past-simple despite being the shortest text — the
  quoted English terms give break opportunities English prose does not.
- **present-simple slide 4 was already broken in German and Spanish**, by
  10px, shipped, since the slide was written. The two formula pills fit one
  line in English and two in every other language, and the spacing was built
  for the one-line case. Nobody measures a language they cannot read. Fixed
  by tightening `.freq .freq-rule` — all ten languages now clear.

**Structural equality with English is a prompt to look, not a defect.** 12 of
3,400 comparisons differ in the SHIPPED de/es — a language with no copula has
no word to carry `<em class="aux">`. Russian and Chinese were flagged for the
same thing and were right. Do not "fix" these.

**Known gap in `checker/overflow` (scratch, not committed):** it did not flag
de/es on present-simple slide 4 even though direct measurement puts both at
+10px. Cause not established. Treat a clean run as suggestive, not proof, and
measure a specific slide directly when it matters.

**Still untranslated, per language:** 643 always-on `.sup` glosses and 1,735
`BW_TR` word-bank entries. The gloss CSS is also hardcoded to `es`/`de`
(`:root[lang="es"] .sup[data-lang="es"]`), so glosses the translators DID
write for the new languages — present-simple's `parNote` carries one in every
language — are inert until those rules are generalised. Deliberate: a gloss
on one slide and nothing elsewhere is worse than none.

**Not native-checked.** fr/it/pt read well. ru/ar/zh/ja are plausible and
handle the hard parts correctly (Russian's `n%10===1&&n%100!==11` plural,
Arabic's dual, Japanese's no-plural 語) but no native speaker has read them,
and the completeness guard means a wrong language ships the moment it is
complete.

## 2026-09-03 — The fuzzy pill: found, fixed, and it was never color-mix

`docs/HANDOVER-fuzzy-pill.md` carried this as unresolved with a live
hypothesis (his browser predates `color-mix()`). That hypothesis is dead: the
reporting machine runs Chrome 152 as its default browser, on a 3840x2160
panel at 200% Windows scaling, so DPR 2 and a 1920x~960 CSS viewport. The
`efca4c2` fallbacks are harmless and stay; the other 23 decks do **not** need
the sweep.

**The cause is a class-name collision in `blockcamp-present-simple.html`.**
`.freq` names the frequency-scale card (plate at 52% surface, 16px side
padding, `backdrop-filter: blur(8px)`) *and* the role colour on
`<b class="freq">ADVERB OF FREQUENCY</b>` inside the formula pill. The inline
marker therefore carried the card's plate, padding and blur. On one line that
is invisible. The second pill on slide 4 wraps in every language, which splits
the marker across two lines, and Chrome applies an inline element's
backdrop-filter to the bounding box of all its fragments — the whole first
line. "SUBJECT + am / are / is +" was painted, then blurred by the marker
painted after it. The blue sat on top of its own blur and stayed crisp, which
is exactly the screenshot: grey words soft and washed, blue beside them sharp.

Reproduced and isolated on the reporting machine, live site, Chrome 148 in
the desktop-app pane, stage at 1.333:
- pill 2 forced to one line → first line crisp and bright;
- `backdrop-filter: none` on `.formula` only → no change (matches the earlier
  ruling-out, which had tested the pill and not the marker);
- `backdrop-filter: none` on `b.freq` only, pill still wrapping → fixed.

**Fix:** one rule after the `.freq` card plate, `b.freq, em.freq { padding: 0;
background: none; backdrop-filter: none; }`, with the reasoning in the CSS
comment beside it. Dropping the 32px of accidental padding also narrows both
pills. Only present-simple has inline `freq` markers, so the other decks are
not affected today — but every one of the 24 has the same `.freq` card rule,
so a marker added to any of them will hit this again. The line-wide fix, if
anyone touches the card CSS, is to scope it to `.card.freq`.

Why three earlier passes missed it: they measured the *pill* — its computed
colours, its edge steepness at three scales — and the pill was innocent. The
defect lives on a child element and only on the wrapped line. Any time the
complaint is "this one looks different from that one" and the computed styles
match, diff the *children* and the *line count*, not the box.

**How to inspect a live deck at true pixels from the desktop app:** the pane
downsamples a 1920-wide viewport to 800, which hides exactly this class of
defect. Set the viewport to 800x400, then from the console
`stage.style.transform = 'translate(-100px,-690px) scale(1.33333)'` to put the
region of interest on screen at 1:1. `fitStage()` restores it, and any resize
event resets it, so apply it after the resize settles.

**`check-lesson.js` now runs on Windows.** It pinned the sandbox's
`/opt/pw-browsers/chromium`; it now uses that path only if it exists and
otherwise Playwright's own install. On this machine playwright is global, so
`export NODE_PATH="$(npm root -g)"` before running it.

**Still open from the handover, unchanged:** German and Spanish overflow
present-simple slide 7 by 22px; the scratch overflow checker is unreliable.

## 2026-09-03 — Present Simple: word bank and glosses in all ten languages

`blockcamp-present-simple.html` now carries `BW_TR` (80 entries) and the 25
always-on `.sup` glosses in fr, it, pt, ru, ar, zh and ja as well as es and de,
and the gloss CSS is generalised: every `:root[lang="es"] … .sup[data-lang="es"]`
rule is now written out for all nine gloss languages (the `data-boxw` width
knob is deliberately still de/es only). That also switches on the per-language
`parNote` glosses the translators had already written into `UI_I18N`, which
were inert until now.

Conventions carried over from es/de and applied in every language: gap
sentences are glossed with the gap filled; "(no existe)"-style markers for
non-existent forms; auxiliary notes keep the English pronouns; Steve, Alex,
Warden and Enderman stay in Latin script; skeletons keep the English function
word ("every + période"). Portuguese is European, matching the deck's `pt` UI
block (tu forms, pequeno-almoço). Chinese and Japanese mark person on
uninflected verbs with "(he/she/it 用)" / "(he/she/it の形)". **Not
native-checked**, same as the UI strings.

**Layout was measured in every language, not just English.**
`lesson-template/checker/overflow-langs.js` (new, committed) repeats
`check-lesson.js`'s LAYOUT measurement with each offered language switched on.
First run: es/fr/it/pt over on slide 2 by 9px (the he/she/it paradigm gloss
wrapped to two lines — es had been shipping that way), pt over on slide 7 by
52px (the "every + period" gloss wrapped, and the weekday gloss fell under the
chips instead of beside them). Fixed by shortening five glosses, one of them
Spanish: the he/she/it line is now "él / ella / ello construye" and its
equivalents — three pronouns, one verb, which is the teaching point anyway.
All ten languages now fit on all 22 slides. Run this tool after any gloss or
`UI_I18N` change; the English-only checker cannot see these.

**Still open across the line:** the other 15 Block Camp I decks and the eight
passive decks still have es/de-only glosses and word banks, and their gloss
CSS is still hardcoded to es/de. The merge is mechanical —
`lesson-template/bank_merge.py <deck> <dir>` does it, asserting every count: bank JSON per language keyed by the exact English, 25-string
gloss array in document order, CSS regenerated from the es template.

## 2026-09-03 — Entities in text-only UI strings, all sixteen Block Camp I decks

Seen in the Portuguese screenshot while checking the gloss work: the score
chip read `PONTUA&CCEDIL;&ATILDE;O 0/29`. `updateScoreChip()` writes
`t('scoreLabel')` with `textContent`, so an entity in that string prints
literally. The `pt` block had `"Pontua&ccedil;&atilde;o"` and the `fr` block
had `btnCopied: "Copi&eacute;"` — the copy button's confirmation, also
`textContent` — on every one of the sixteen Block Camp I decks, since
`1f072ae` rolled the same blocks out to all of them. Both decoded to the plain
characters in all sixteen. The passive decks were clean.

`check-lesson.js` now has an ENTITIES gate: the four keys that are consumed
with `textContent` (`scoreLabel`, `glossHide`, `glossShow`, `btnCopied`) fail
the check if any language's value carries `&…;`. Verified failing against the
pre-fix `blockcamp-past-simple.html` before it was trusted. If a future key is
written with `textContent`, add it to `textKeys` in the gate.

Found by the same sixteen-deck run, untouched: **`blockcamp-present-continuous.html`
slide 17 overflows by 3px in English** on the committed version too (`git
show HEAD:` copy fails the same way). Not caused by anything in this session;
it is the only Block Camp I deck that does not pass `check-lesson.js` today.
