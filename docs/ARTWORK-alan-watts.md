# Artwork brief — Alan Watts, The Art of Being Present (B1)

Companion to `ARTWORK-holding-the-line.md`, which is the general spec for the
editorial style (HOUSE-STYLE §15). Read that first: the frame geometry, the
"middle 65%" rule and the `prep-artwork.py` warning to ignore are all there and
are not repeated here.

**Revised 2026-09-22, Innes's call: no Alan Watts, no bearded man.** The first
version of this brief asked for nine posterised portraits, because the lesson is
about a specific person and the supplied batch was already portraits. He asked
for the list again without them, and he is right to. Three reasons it is the
better set:

1. **It puts this deck back on the house stem.** `ARTWORK-holding-the-line.md`
   says *no people, no faces* and means it. A deck that opts out is a deck that
   has to justify itself every time someone re-renders it.
2. **Generated likenesses of a real named person get worse the more you make.**
   Nine was already a lot of near-misses of a man who died in 1973. Twenty is a
   set where some of them are visibly not him, on a page with his name at the
   top.
3. **Objects age better.** A chair or a stone does not go out of date, does not
   drift off-model between batches, and can be re-rendered in two years to match
   whatever the set already looks like.

The nine portraits currently shipped stay live until a replacement set exists.
Nothing here is urgent — see the note at the end.

---

## What is shipped now, and why it needs replacing

The deck is live on nine plates salvaged from a 2:1 batch. They work — every
subject is in frame — but they are a rescue, not the intended set:

| | shipped now | what the frame wants |
|---|---|---|
| plate ratio as rendered | **2:1** | **7:6** |
| what survived | central 58% of the width | the whole picture |
| `plate-a` … `plate-d` | 1166 × 1000 | ≥ 1400 wide |
| `plate-e` … `plate-i` | **952 × 816** | ≥ 1400 wide |
| hero | 2000 × 1091, subject **centred** | 16:9, subject on the **right** |

Two concrete costs:

1. **Roughly 42% of every plate was thrown away**, and the crop centre had to
   be chosen per plate by finding the darkest region — the commit that did it
   is `614a7b0`. A native 7:6 render keeps all of it.
2. **`plate-e` … `plate-i` are 952px wide.** The framed block is 473 × 410 css
   px, so at 2× device pixel ratio it needs 946 × 820. They are one pixel
   clear of soft. There is no retina headroom and no room to re-crop again.

Neither is visible at 1× on a laptop. Both are visible on a projector and on a
phone, which is where these decks actually get used.

---

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

The nine shipped portraits run hotter than this — coral and salmon rather than
blush. A replacement set does **not** need to match them, because it replaces
them wholesale; match the table instead. The editorial palette is fixed at the
CSS level either way, so the deck's type and cards stay on-key regardless. Keep
the **object** dark and the **ground** warm and you are inside the set.

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
