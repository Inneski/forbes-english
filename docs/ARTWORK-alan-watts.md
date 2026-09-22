# Artwork brief — Alan Watts, The Art of Being Present (B1)

Companion to `ARTWORK-holding-the-line.md`, which is the general spec for the
editorial style (HOUSE-STYLE §15). Read that first: the frame geometry, the
"middle 65%" rule and the `prep-artwork.py` warning to ignore are all there and
are not repeated here.

**What this brief is for, corrected 2026-09-23.** Innes asked for a shopping
list "with non Alan Watts bearded man requests" — meaning *stop putting more
pictures of the man on the list*, not *get rid of the ones we have*. A previous
pass read it the second way and cut all nine portraits. They are restored from
`614a7b0` and the deck now carries **both** sets.

So this list exists to add subjects that are **not** another portrait. The nine
portraits are finished work and are not to be replaced.

**The deck uses the two sets for different jobs, and the split is the lesson's
own: a portrait where the slide is about the man, an object where it is about
the idea.** The illusion of the separate self is a coat sharing an edge with its
own shadow; *wu wei* is water parting round a stone. Watts's face on those slides
would say "here is Watts again" where the slide is trying to say something
specific. His face belongs on who he was, on the line he is remembered for, and
on the comprehension run, which is about what *he* said.

---

## Status — 18 pictures, one slot still open

**Delivered 2026-09-22/23.** Nine object plates (`plate-a` … `plate-i`) were
rendered to this brief and are live **alongside** the nine restored Watts
portraits (`watts-a` … `watts-i`). Eighteen pictures across twenty-two
art-bearing slides, so only three repeat — all three late in the sentence-building
run, far enough from their first showing not to read as one.

**Seven objects came back native 7:6** (2368 × 2032) — the first time `--ar 7:6`
has actually taken in this repo, and worth knowing it *can*. Two came back 16:9
and needed different handling:

| plate | what happened |
|---|---|
| `plate-e` microphone | Right-aligned **by hand**. The subject-centroid routine put the crop at x=0, because the dark wall panel on the left outweighs the microphone, and that sliced the microphone off the right edge. A dark *background* beats a dark *subject*; do not trust a centroid on a plate with a large dark field in it. |
| `plate-d` river stone | The stone fills its frame edge to edge, so cropping to 7:6 zoomed further in and the arch cut it into an abstract stripe. **Padded instead** — the whole 16:9 inside a 7:6 canvas with its own edge colours extended. When a subject fills its frame, add ground rather than taking picture away. |

**The arch follows the picture, not the deck.** `build_watts.py` has an
`arched(bg)` helper that returns true only for `plate-*`. The still lifes have
sky above them and take the 190px arch well; the portraits are
head-and-shoulders that fill the frame and come back with the hair cut off. One
flag for the whole deck cannot express that, which is why it is a function.

### Still outstanding: the hero

Every framed slot is filled. **The cover is not**, and it is the one thing a
learner sees go wrong: the hero is still the centred ZEN/TAO/NOW/BEING diagram,
so the 88px title lands on the word ZEN.

Two ways to close it, and the cheap one is probably right:

1. **No new art.** Shift the existing diagram right so the left 58% is clear.
   Crop-and-pad on a file already on disk.
2. **Render the hero below**, and move the diagram onto the "Who was Alan
   Watts?" slide as a `data-bg`, where nothing is set over it and it is allowed
   to be centred.

## The style stem

Every prompt below is `<subject>, <stem>`. This is the house editorial stem,
unchanged — which is the point of dropping the portraits.

```text
flat editorial illustration, posterised into four flat tones, two-tone slate blue and pale blush on a warm cream ground, one brick-red accent, heavy grain and halftone stipple, hard single light source, long soft shadow, no people, no faces, no hands, no text, no logos, no brand marks, generous negative space, centred subject, --ar 7:6 --style raw
```

Four things in it are load-bearing:

- **`no people, no faces, no hands`** — `no hands` is added here. Half the
  subjects below are things a person would be holding or sitting on, and that
  is exactly the prompt that grows an arm in the corner.
- **`posterised into four flat tones`** — what holds a batch together as one
  set. Drop it and you get airbrushed digital painting.
- **`centred subject`** — this is the "middle 65%" rule said in a way the model
  acts on. It is the instruction that failed on the portrait batch, where the
  subject sat hard left and the 7:6 crop took his head off.
- **`--ar 7:6`** — ask even though Midjourney often returns 16:9 anyway. Asking
  is free; the composition instruction is the actual defence.

**Upscale before you send.** A base 7:6 render is about 1232 × 1056, under the
1400px house minimum. Run the 2× upscale.

## The palette

Same tokens as the general spec, with the two this deck leans on:

| role | hex | how to say it |
|---|---|---|
| the field | `#fff9ed` | warm cream |
| plate ground | `#f3ede0` | one step darker than the field |
| ink / the object | `#123a3e` | near-black teal |
| primary | `#1c5789` | slate blue |
| secondary | `#f8dcd1` | pale blush |
| the one accent | `#a33b12` | brick red — **one object per picture** |

The delivered set sits on these tokens closely — slate blue, blush, warm cream
— which is why it reads as one thing with the deck's own type and cards. Any
later addition should match this table rather than eyeballing the existing
plates. Keep the **object** dark and the **ground** warm and you are inside the
set.

---

## The shopping list

Ten files. Slot names are the filenames; `build_watts.py` names each one in its
`READ`, `MC_BG` and `ORDER_BG` lists, so swapping a real set in is one line per
slot.

**Every subject below is an object or an empty place.** Where the lesson needs
a person, the picture shows what the person left behind — the chair, the
microphone, the coat on the hook. That is the same move `ARTWORK-holding-the-line.md`
makes when it draws the activation stage as two chairs, and it reads as
deliberate rather than as an absence.

### The cover — 1 file, `--ar 16:9`

| slot | prompt subject |
|---|---|
| `hero` | `a single empty wooden chair on the right-hand third, facing away towards a low sun over layered hills, the left two-thirds open cream sky with nothing in it` — **`--ar 16:9`**, deliver 2000 × 1125 |

**The left 58% must be empty.** The cover lockup — logo, an 88px title, the
subtitle, three chips and the Begin button — is left-aligned and capped there,
with a scrim behind it. The current hero is a centred ZEN/TAO/NOW/BEING diagram,
so the title lands on the word ZEN.

Keep that diagram. It is a good concept map and it is what the library card is
cut from — it just wants to be a *teaching* plate rather than the cover.
`data-bg` on the "Who was Alan Watts?" slide would use it properly, and it is
the one picture in the set that is allowed to be centred, because nothing is
set over it there.

### The framed plates — 9 files, `--ar 7:6`

| slot | where it appears | prompt subject |
|---|---|---|
| `plate-a` | Idea one — the separate self | `a single empty overcoat hanging on a wall hook, its shadow dissolving into the wall so coat and wall share one edge` |
| `plate-b` | Idea three — impermanence | `one open flower past its best in a narrow vase, three fallen petals on the table below it` |
| `plate-c` | The man — who he was | `an empty wooden chair facing a low sun sinking behind layered hills, seen from behind` |
| `plate-d` | Idea two — wu wei | `a smooth river stone with water parting around it, the current unbroken on both sides, seen from directly above` |
| `plate-e` | In his own words | `a vintage ribbon microphone alone on a bare stage, one warm spotlight pooling under it` |
| `plate-f` | Comprehension questions | `an open book lying face-down and spine-up on a plain table, a single bookmark ribbon trailing off the edge` |
| `plate-g` | Afterwards / activation | `two simple chairs turned slightly towards each other across a low table, nobody in either` |
| `plate-h` | Vocabulary | `seven smooth pebbles in a row on flat sand, one of them turned over to show its pale underside` |
| `plate-i` | Results / closing | `a narrow path running out across open ground under a wide sky of flat stylised clouds` |

Five notes on the list:

- **`plate-g` is the activation plate**, the last thing a learner sees, and the
  two chairs are doing a job: the slide is a speaking task for pairs. Do not
  swap it for another still life.
- **`plate-d` is the one that will fight you.** Water parting round a stone at
  four flat tones is hard, and the first batch will come back either as a
  photograph or as a logo. If it will not resolve, the fallback subject is
  `a paper boat riding a current, seen from above, the water drawn as flat
  contour lines` — same idea, easier to posterise.
- **`plate-h` must show exactly seven pebbles.** The slide is a seven-word gap
  fill. Nobody will count them, but if it is wrong it is wrong in a way that
  cannot be unseen once someone does.
- **Nine plates cover twenty-two art-bearing slides**, so several repeat. That
  is inside HOUSE-STYLE §5c, which asks for one background per *section* plus
  activation, not one per slide. To kill the repeats, the slots worth doubling
  first are `plate-f` and `plate-i`, which carry four each.
- **An object set brings the arch back.** `build_watts.py` currently passes no
  `data-art`, because head-and-shoulders portraits fill the frame and the 190px
  arch was clipping hair. A still life with air above it has the top 15% to
  spare, so the arch becomes available again — set `shape='arch'` in `art()`
  and `arch=True` in `reading()`, rebuild, and look at it before deciding.

## Dropping a new set in

```bash
python3 tools/prep-artwork.py "incoming/Alan Watts/<files>" --into alan-watts \
        --names hero,plate-a,plate-b,plate-c,plate-d,plate-e,plate-f,plate-g,plate-h,plate-i
python3 lesson-template/build/build_watts.py
node   lesson-template/check-lesson.js forbes-alan-watts-b1.html   # must exit clean
python3 tools/seo.py
```

`prep-artwork.py` will print `aspect 1.17, not 16:9 — it will crop on the
deck` for every 7:6 plate. **Ignore it** — under this style 7:6 is the correct
shape and a 16:9 plate is the one that gets cropped. It is a note, not a
rejection, and the file still processes.

It will also refuse near-identical files, which is what you want: the supplied
batch contained two exact duplicates and they were caught on hash.

**Run `--dry-run` first.** Midjourney's four-up variants are near-identical by
design and the dry run tells you which of the four to keep before anything is
written.

---

## How urgent is this

Not very, and it is worth being honest about that rather than letting a tidy
document imply otherwise.

The deck is live and working. All nine portraits have their subject in frame
after `614a7b0`, every checker passes, and nothing on the page is broken. The
two costs listed at the top are real but small: five plates are 952px against a
framed block that needs 946 at 2× DPR, which is six pixels of headroom, and a
crop that threw away width it has already finished throwing away.

**The one thing a learner actually sees is the cover**, where the title sits on
the word ZEN. That does not need new artwork at all — the existing diagram just
needs shifting right so the left 58% is clear, which is a crop-and-pad job on a
file already on disk.

So: commission this set when there is a reason to open Midjourney anyway. Do
not commission it *because* of this document.
