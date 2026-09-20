# Artwork: Holding the Line (C1) — and the spec for any editorial deck

> **Delivered 2026-09-19.** All eight slots are in `HoldingTheLine/` and the
> deck is built on them. One thing did not survive the brief: every candidate
> came back **16:9**, so the seven framed plates were cut to 7:6 here before
> prep, at the centres recorded in `docs/HANDOFF.md`. If you are re-rendering
> any of them, `--ar 7:6` is still what you want — a native 7:6 keeps 35% more
> of the picture than a crop does.

Eight pictures. Everything above the slot table applies to **every** deck
built on the editorial style (HOUSE-STYLE §15), so commission the next one
from the same spec.

---

## Why this list is not shaped like the others

Every previous artwork brief in this repo said *16:9, at least 1400px wide,
the hero drives the palette*. On the editorial template none of those three
sentences is true, and the reasons are structural rather than taste.

1. **The palette is fixed and the art matches it** — not the other way round.
   `extract-palette.py` is not run for an editorial deck; the colours are
   authored once in the template and guarded by
   `tools/check-editorial-palette.py`. So the hexes below are a constraint on
   the pictures, not an output of them.
2. **The frame is 7:6, not 16:9.** The picture renders in a framed block
   473 × 410 css px — `.editorial-art` is 37% × 57% of the 1280 × 720 stage —
   centre-cropped to fill. Only the cover is full-bleed 16:9.
3. **Nearly every slide wants one.** A slide with no picture takes the full
   width and shows nothing; on a flat field that reads as an empty page. This
   deck gives 13 of its 23 slides a picture and the four widest none.
4. **Large near-white areas are fine here.** That is what the style exists
   for: there is no text over the picture, so nothing has to survive being
   read across it. The old warning about bright flat vector art does not
   apply.
5. **But the plate needs its own ground.** Cream-on-cream makes the frame
   disappear. Give each picture a ground one step off the page cream
   (`#f3ede0`, a pale slate or a sage wall) so the framed block reads as an
   object with an edge. The delivered set does this and it is the single
   biggest reason it sits well.

---

## The spec

> **Revised 2026-09-20, after two batches.** `--ar 7:6` did not take either
> time: every candidate in both came back 16:9. Twice is a default, not a
> slip, so this table now asks for what that pipeline actually produces and
> puts the burden on COMPOSITION instead of on the flag. Ask for 7:6 by all
> means — it keeps about a third more of the picture — but compose as if you
> will not get it.

| | **hero** (1 file) | **the framed plates** |
|---|---|---|
| ratio you will get | 16:9 | 16:9 |
| ratio the frame wants | 16:9 | **7:6** (473 × 410 css px) |
| Midjourney | `--ar 16:9` | `--ar 7:6`, and expect 16:9 |
| deliver at | 2000 × 1125 | 2944 × 1648 is fine |
| where it shows | full bleed behind the cover | framed block, right or left |
| composition | **subject on the RIGHT** | **subject inside the middle 65%** |
| keep clear | the left 58%, top to bottom | the outer sixth each side, and the top corners |

**The middle 65% is the whole instruction.** A 16:9 plate centre-cropped to
7:6 keeps the central 65% of its width and throws away a sixth off each side.
A subject composed inside that band survives untouched; one that spans the
full width comes back cut in half. Both batches lost pictures this way — a
clock bisected, two chairs sliced at the arms — and both were salvaged only by
choosing the crop centre by hand, plate by plate.

**The cover's quiet half.** The lockup — logo, an 88px title, the subtitle,
three chips and the Begin button — is left-aligned and capped at 58% of the
width, with a scrim behind it. Anything in that band is covered.

**The top corners.** Three slides render the picture as a 190px arch
(`data-art="arch"`). On the interim `remit` plate the arch clipped the top of
the drawing. Keep the subject out of the top ~15% at either corner and the
same file works in both frames.

**Upscale before you send.** A base Midjourney render at 7:6 comes out around
1232 × 1056, which is under the 1400px house minimum and `prep-artwork.py`
will skip it. Run the 2× upscale.

**One warning to ignore.** `prep-artwork.py` prints
`aspect 1.17, not 16:9 — it will crop on the deck` for every 7:6 plate,
because it was written when every picture was a background wash. Under this
style the warning is inverted: **7:6 is the correct shape and a 16:9 plate is
the one that gets cropped.** It is a note, not a rejection — the file still
processes. Do not "fix" it by re-rendering at 16:9.

---

## The palette — these are the deck's own tokens

Name them in the prompt. They are what the type, the cards and the field are
already set in, so a picture outside them will be the only thing on the slide
that is off-key.

| role | hex | how to say it |
|---|---|---|
| the field | `#fff9ed` | warm cream |
| plate ground | `#f3ede0` | one step darker than the field |
| primary | `#1c5789` | slate blue |
| primary, deep | `#16456b` | deep slate |
| ink | `#123a3e` | near-black teal |
| secondary | `#f8dcd1` | pale blush |
| the one accent | `#a33b12` | brick red — **one object per picture, no more** |

---

## The style stem

Every prompt below is `<subject>, <stem>`.

```text
flat editorial illustration, two-tone slate blue and pale blush on a warm cream ground, one brick-red accent, heavy grain and stipple texture, hard single light source, long soft shadow, no people, no faces, no text, no logos, no brand marks, generous negative space, centred subject, --ar 7:6 --style raw
```

**No people, deliberately.** The style treats the artwork as an object, the
subjects below are all objects, and a generated face in a lesson about being
criticised by your manager is a liability the deck does not need. The one
place two figures would be natural — the activation stage — is drawn as two
chairs instead, which says the same thing.

---

## The eight slots

Slot names are the filenames. `build_holdingline.py` has an `ART` map at the
top and that is the only place a filename appears, so swapping the real set
in is one line per slot.

| slot | where it appears | prompt subject |
|---|---|---|
| `hero` | the cover, full bleed | `a tall high-backed executive chair and a small plain chair at opposite ends of one long table, the tall chair on the right, wide empty floor to the left` — **`--ar 16:9`** |
| `remit` | the passive teaching card; two questions; the second gap screen | `a boundary taped out on an office floor, three folders stacked squarely inside it and one folder lying across the line` |
| `ledger` | the first gap screen; one question | `a clipboard with four rows, three of them ticked and the fourth an empty dotted box` |
| `facts` | two questions; the sentence-order round | `a large plain wall clock beside a stack of three dated paper dockets` |
| `door` | three questions | `a single closed office door with a small blank nameplate, long diagonal shadow across the floor` |
| `handover` | the ONCE teaching card; the second ask screen | `an archive box with its lid lifted off, a blank luggage tag hanging from the handle` |
| `keys` | the first ask screen | `an access card lying at an angle in front of a wall-mounted card reader` |
| `talk` | the activation stage | `two identical chairs turned to face each other across a small low table` |

Several variants per slot are welcome — `prep-artwork.py --dry-run` will say
which of a four-up are near-duplicates, and the building session picks one.

---

## When they land

**Copy this batch out of `incoming/` first.** That folder is shared with
every other session and holds hundreds of files from earlier drops; pointing
`prep-artwork.py` at it processes all of them and `--names` then fails on a
count mismatch, which is the friendly version of the mistake. Move the batch
to a folder of its own, numbered so that sorted order matches `--names`:

```bash
py tools\prep-artwork.py <batch-folder> --into HoldingTheLine --dry-run
```

then, once the keepers are chosen:

```bash
py tools\prep-artwork.py <batch-folder> --into HoldingTheLine --width 1600 --names remit,ledger,facts,door,handover,keys,talk
```

The hero goes in its own run without `--width`, because 16:9 at 2000px is
right for a full-bleed cover and lands near 220 KB anyway.

Then, in order:

1. **Do not run `extract-palette.py`.** This deck's colours are fixed. Run
   `py tools\check-editorial-palette.py` instead — every row must PASS.
2. Change the eight values in `ART` at the top of
   `lesson-template/build/build_holdingline.py` from `.svg` to `.jpg`.
3. `py lesson-template\build\build_holdingline.py`
4. `node lesson-template\check-lesson.js forbes-english-holding-the-line-c1.html`
5. Catalogue row, `LibraryCards/forbes-english-holding-the-line-c1.jpg`
   (1200 × 512, cut from the hero), `library.html` line,
   `py tools\build_hubs.py`, then `py tools\seo.py` last.

The interim SVG plates and their generator were deleted in the commit that
brought this set in. Two sets of plates in one folder is how a lesson ends up
built twice.
