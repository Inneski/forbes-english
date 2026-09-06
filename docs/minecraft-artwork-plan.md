# Minecraft artwork: the incoming set, and where each picture goes

Innes generated roughly **95 flat-vector Minecraft scenes** on 2026-09-06 and
showed them to a cloud session as chat attachments. A cloud session sees an
attachment as an image, **not as a file on disk** — `/mnt/attach` was empty and
a filesystem sweep found nothing — so that session could audit them and could
not place them. This document is the audit, written down so the placement is
mechanical once the files exist somewhere a session can read.

**To make them usable, the files must reach the repo.** Either route works:

- Upload to `incoming/` at
  <https://github.com/Inneski/forbes-english/upload/main/incoming> (five at a
  time; the uploader wedges on large batches — see CLAUDE.md).
- Or, on Innes's own machine, run the prep tool directly on the download folder:
  `py tools\prep-artwork.py "%USERPROFILE%\Downloads" --into incoming --keep-names --dry-run`
  then drop `--dry-run`, commit and push.

Either way, **run `tools/prep-artwork.py` before committing.** Raw Midjourney
PNGs are 3–7 MB each; `.git` is already ~700 MB with no LFS and never forgets a
blob. Ninety-five raw files add ~500 MB permanently; the same ninety-five at
house spec add ~25 MB.

## What arrived

All 16:9, all in the coral / slate-blue / cream / dusty-pink family that
matches the existing artwork. The register is more architectural and graphic
than the current Noma-Bar-ish character silhouettes — a deliberate style shift,
and a welcome one given the old set is exhausted and repeating (see the
2026-09-06 audit entry in HANDOFF.md).

Roughly **95 images resolving to ~45 distinct pictures.** The gap between those
numbers is the point: Midjourney returns variants, and several exact repeats
came through in separate batches.

### Families

| Family | Approx. count | Usable |
|---|---|---|
| Redstone / circuit diagrams | 6 | 3 |
| Blue silhouette landscapes (castle, fort, cliffside) | 5 | 4 |
| Archive / storage corridors | 4 | 3 |
| Isometric towns and crowds | 4 | 2 |
| Terrain, strata, canyons | 8 | 4 |
| Underwater / light shafts | 6 | 3 |
| Red caves and tunnels | 6 | 3 |
| Specimen drawers, field tents (DinoCraft) | 7 | 4 |
| Mobs: creeper, wolf, pig, villager, Steve | 10 | 6 |
| Chests, furnaces, ore/tool icon rows | 12 | 6 |
| Trees, saplings, bread, water-meets-lava | 10 | 5 |

### Known exact repeats

Sent twice or more across batches — the hash pass will confirm, but these were
visible by eye:

- the plateau cutaway with the waterline (batch 1 and batch 5)
- the green hill with the dark cliff opening
- the orange-sun blocky pyramid
- the six-panel ore/gem icon grid
- the blue-canopy tree with the sapling
- the split blue/red mountain with lava meeting water
- Steve standing in front of the sun, on the cracked path

### Do not use

- **The labelled-boxes archive** — the labels carry fake lettering, which reads
  as sloppy at full-screen.
- **The saturated "head full of a colourful town"** — far more saturated than
  everything else; will not sit in a deck with the rest.
- **The moonlit archive, the night pyramid with the fire, the deepest red
  caves** — too dark for a light-theme deck. Usable only if a deck goes dark.

## Allocation

Every one of the six decks is `data-theme="light"`, so the picture chosen for
each slot must be bright. Names below are the target filenames; the builder's
`MC_BG` / `FIB_BG` / `EC_BG` lists in `lesson-template/build/` reference them.

### `tense-review-minecraft.html` — TenseReview/ (8, currently 3 distinct, 0 unique)

*Twelve tenses, and the three decisions that pick between them.* Scenes that
carry time:

| File | Picture |
|---|---|
| `hero.jpg` | Steve walking toward the low sun over water |
| `rails.jpg` | the minecart rail bridge across the chasm under the big sun |
| `sapling.jpg` | the sapling beside the full-grown blocky tree |
| `lake.jpg` | the blocky lake with the heron and the reflection |
| `ravine.jpg` | the ravine with the tiny figure on the near edge |
| `tracks.jpg` | footprints in snow leading away behind a walking figure |
| `bed.jpg` | the bed on open ground under a rising moon |
| `dusk.jpg` | the fort on the hill under the great white sun |

`tracks.jpg` and `bed.jpg` arrived late and are the two briefs the first pass
wrote out longhand — *snow with footprints leading away behind a figure*, and
*a bed and a rising moon*. Nothing else in the set carries "before" and "after"
as plainly: the footprints are the past visible in the present, the bed is the
full stop. They displace the red canyon and the strata cliff, which go to
DinoCraft Pt II where geology is the subject rather than the metaphor.

### `minecraft-lesson.html` — MustHaveTo/ (8, currently 4 distinct, 0 unique, all low-res copies)

*Two ways to say you have no choice.* Obligation and prohibition:

| File | Picture |
|---|---|
| `hero.jpg` | the lit furnace with fire and coal |
| `ravine.jpg` | the ravine, figure on the edge (a hazard you must avoid) |
| `chest.jpg` | the open chest against blue mountains and clouds |
| `stall.jpg` | the villager market stall with barrels and crates |
| `bread.jpg` | the loaf with the wheat stalk |
| `wolf.jpg` | the wolf close-up |
| `pig.jpg` | the new pig close-up (**not** the pig already in `minecraft/`) |
| `night.jpg` | the blocky treeline at dusk |

### `forbes-english-minecraft-editorial.html` — MinecraftEd/ (7, keeps `city.jpg`)

*How anything turns into anything else.* Transformation, literally:

| File | Picture |
|---|---|
| `hero.jpg` | the hexagonal cutaway cube, water above and lava below |
| `smelt.jpg` | the furnace cube with the glowing ore inside |
| `meet.jpg` | the split mountain where lava meets water |
| `grow.jpg` | the sapling and the full tree |
| `bake.jpg` | the loaf and the wheat |
| `ore.jpg` | the ore / block / pickaxe icon row |
| `block.jpg` | the classic grass block, isometric |
| `city.jpg` | *(unchanged — the one picture this deck already owns)* |

### `forbes-english-minecraft-b1.html` — MinecraftB1/ (7, keeps `village.jpg`)

*The tenses a player needs to tell the story.* A story arc, in order:

| File | Picture |
|---|---|
| `hero.jpg` | Steve in front of the rising sun on the cracked path |
| `wake.jpg` | the minimal mountain with the small fort |
| `tree.jpg` | the big blocky tree over the plaza |
| `cave.jpg` | the red cave mouth with the glowing spire |
| `stall.jpg` | the second villager stall, against the grey peak |
| `rails.jpg` | the rail bridge *(if not taken by Tense Review — do not share)* |
| `home.jpg` | the castle silhouette against blocky clouds |
| `village.jpg` | *(unchanged)* |

### `forbes-english-minecraft-c1.html` — MinecraftC1/ (4 replacements)

*The same game, described by a player and described by a scholar.* Replaces the
two photoreal renders (`creatures`, `structure`) that break the deck's style:

| File | Picture |
|---|---|
| `hero.jpg` | the fort on the hill under the great white sun |
| `redstone.jpg` | the hexagonal redstone cube read as a technical diagram |
| `crowd.jpg` | the isometric village square with many small figures |
| `archive.jpg` | the archive corridor of stacked chests |

### DinoCraft (Pt I 5, Pt II 6) — `minecraft/`

Covered outright by this batch: the field lab tent, the specimen drawers with
fossils, the storm over the nesting ground with the parasaurolophus silhouette,
the submerged cave, the strata cliffs, the excavation trench.

## After the files land

1. `python3 tools/prep-artwork.py incoming --into <LessonFolder> --names ...`
   — it refuses anything matching an image already in the repo or another file
   in the same batch, and flags anything too dark or the wrong shape.
2. Re-derive each palette: `python3 lesson-template/extract-palette.py <folder>/hero.jpg --light`.
   Every row must PASS. Never hand-pick a colour.
3. Update the `MC_BG` / `FIB_BG` / `EC_BG` lists in the six builders under
   `lesson-template/build/`, re-run each builder.
4. `node lesson-template/check-lesson.js <lesson>.html` — must exit clean.
5. `python3 tools/seo.py`, then **read `git diff` on `library.html`, `llms.txt`,
   `lesson-meta.json` and `sitemap.xml`** before committing (see CLAUDE.md — a
   cloud run silently drops anything newer than `tools/lessons.json`).
6. Delete `incoming/` in the same commit that files the artwork.

## Every brief is covered

Nothing on the shopping list is missing. Later batches closed all four of the
briefs the first pass could not fill:

- **A player leaning over a lit campfire** — the "figure at a furnace" brief
  with a character in it rather than just the object. Use it as
  `MustHaveTo/hero.jpg` ahead of the empty furnace: an obligation lesson
  wants somebody under the obligation.
- **A locked door**, twice — one padlocked iron door, one plain dark door
  with a keyhole against a pale green ground. The plain one is the stronger
  slide (more air around the subject, nothing competing with the card) and
  takes `MustHaveTo/locked.jpg`. It is the deck's prohibition picture:
  *you mustn't go in* rather than *you don't have to*.
- **Rain** — a figure sheltering under a blocky tree in driving rain, pale
  blue-grey, the only weather picture in the whole set. `MustHaveTo/rain.jpg`.
  It is also the one image that shows a consequence of *not* acting, which is
  what an obligation lesson is for.
- **A boat on open water**, four ways — an empty rowing boat, one under sail,
  one with a player at the oars, one with a figure lying in it. Take the
  player at the oars: `MustHaveTo/boat.jpg`. Water to the horizon on every
  side is the picture of having no choice but to keep going, and the three
  empty boats say the same thing with nobody in them to say it about.

**Stop generating.** Roughly 145 images arrived, resolving to about 55 distinct
pictures against a shopping list of 34. Every deck can now have artwork that
nothing else on the site uses, which was the whole point of the audit.
