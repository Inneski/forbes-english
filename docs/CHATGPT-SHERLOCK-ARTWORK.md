# Sherlock: The Blue Manuscript — the eight pictures the export is missing

**Paste the section below to ChatGPT.** It is the only thing standing between
that lesson and publication: the builder, the text, the nine languages, the
answer key and the scoring are all finished and committed
(`lesson-template/build/build_sherlock_blue_manuscript.py`). When the plates
arrive, drop them in `block-camp/sherlock-blue-manuscript-rpg/`, re-read the
hotspots (`rpg/README.md` §3) and re-run the builder.

## What went wrong

The export shipped **eighteen picture filenames holding ten distinct images**.
Seven names were byte-identical copies of another:

| these are all one picture |
|---|
| `05_ledger` = `11_telegram` = `14_libcard` |
| `08_dockpass` = `15_key` |
| `01_cover` = `12_cipher` |
| `06_token` = `16_timetable` |
| `03_watch` = `18_plate` |
| `04_boot` = `17_rope` |
| `07_choice1` = `13_choice2` |

Every duplicate pair sits on the main route, so a single thirteen-question run
shows the same picture two or three times, and the cover comes back as a
mid-game question. A Block Camp RPG is one full-bleed picture per scene with
one glowing object on it — that is the whole interaction, and it cannot be
built from ten pictures.

Two of the ten were also attached to the wrong scenes: `06_token.webp` holds a
gas lamp and no token, and `10_lamp.webp` holds the cab token and no lamp. The
builder swaps those two, so they do not need redrawing.

---

## The request (paste this)

Eight replacement pictures for the Sherlock: The Blue Manuscript RPG. Same
style as the ten you already sent — blue voxel Victorian London at night,
1536×1024 WebP, under 200 KB each, no text baked into the image.

**Every one must be a new, distinct image.** No reuse between these eight, and
none of them may repeat a picture already sent. Each needs **one bright,
clearly nameable object**, positioned on one side of the frame with the other
side quiet, so a glowing marker can sit on it and a text panel can open beside
it without covering it. Put the named object roughly two-thirds of the way
across the frame, not in the middle.

| file | scene | the object that must be in it, lit and unmistakable |
|---|---|---|
| `11_telegram.webp` | a telegram arrives at Baker Street | a telegram form on a desk |
| `12_cipher.webp` | Holmes reads the coded disc | a cipher disc — a circular brass code wheel |
| `13_choice2.webp` | the second route choice | a signpost with two arms, pointing to a library and to a river warehouse |
| `14_libcard.webp` | the reading room | a library card on a counter |
| `15_key.webp` | the river warehouse | a large iron key on a hook |
| `16_timetable.webp` | the station platform | a printed railway timetable board |
| `17_rope.webp` | the rooftop | a rope tied over a parapet |
| `18_plate.webp` | the printer's workshop | a metal printing plate on a press |

Deliver the eight files. Nothing else needs to change — do not re-emit the
game data.

---

## For the session that receives them

1. Drop the files in `block-camp/sherlock-blue-manuscript-rpg/`.
2. Confirm there are no duplicates left:
   `for f in block-camp/sherlock-blue-manuscript-rpg/*.webp; do git hash-object "$f"; done | sort | uniq -d`
   must print nothing.
3. Re-read `HOT` in the builder against gridded contact sheets — every box in
   it was placed for the old plates and none of the eight will still be right.
4. `python3 lesson-template/build/build_sherlock_blue_manuscript.py`
5. `NODE_PATH=$(npm root -g) node lesson-template/check-rpg-panels.js sherlock-blue-manuscript-rpg`
6. Then publish it the normal way: hub card, `LESSON_IMAGES`, catalogue row
   after the page is live, `seo.py` last (`docs/HANDOFF-rpg.md` §5-7).
