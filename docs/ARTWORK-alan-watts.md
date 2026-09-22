# Artwork brief — Alan Watts, The Art of Being Present (B1)

Companion to `ARTWORK-holding-the-line.md`, which is the general spec for the
editorial style (HOUSE-STYLE §15). Read that first: the frame geometry, the
"middle 65%" rule and the `prep-artwork.py` warning to ignore are all there and
are not repeated here.

**This deck differs from Holding the Line in one deliberate way: it is a deck
of faces.** That stem says *no people, no faces*, because its subjects are
objects and a generated face in a lesson about being criticised by your manager
is a liability. Here the lesson is *about a specific person*, his portrait is
the whole visual idea, and Watts died in 1973. So the portrait is the subject,
and the stem below says so.

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

Every prompt below is `<subject>, <stem>`.

```text
flat editorial portrait illustration, posterised into four flat tones, slate blue and near-black teal figure against a warm cream and coral ground, one burnt-orange accent shape, heavy grain and halftone stipple, hard single light source, no text, no logos, no brand marks, generous negative space, subject centred and complete within the frame, --ar 7:6 --style raw
```

Three things in that stem are load-bearing and should not be edited out:

- **`posterised into four flat tones`** — what makes the existing nine read as
  one set. Drop it and you get airbrushed digital painting that will not sit
  beside them.
- **`subject centred and complete within the frame`** — this is the "middle
  65%" rule said in a way the model acts on. It is what failed last time.
- **`--ar 7:6`** — ask for it even though, per the general spec, Midjourney
  frequently ignores it and returns 16:9 anyway. Asking costs nothing and
  sometimes works; the composition instruction is the actual defence.

**Upscale before you send.** A base 7:6 render is about 1232 × 1056, under the
1400px house minimum. Run the 2× upscale.

---

## The palette

Same tokens as the general spec, with the two this deck leans on:

| role | hex | how to say it |
|---|---|---|
| the field | `#fff9ed` | warm cream |
| plate ground | `#f3ede0` | one step darker than the field |
| ink / figure | `#123a3e` | near-black teal |
| primary | `#1c5789` | slate blue |
| secondary | `#f8dcd1` | pale blush |
| the one accent | `#a33b12` | brick red — **one object per picture** |

The shipped plates run hotter than this — coral and salmon rather than blush.
That is fine and does not need matching exactly; the editorial palette is
fixed at the CSS level, so the deck's type and cards stay on-key regardless.
Keep the **figure** dark and the **ground** warm and you are inside the set.

---

## The shopping list

Ten files. Slot names are the filenames; `build_watts.py` names each one in
its `READ`, `MC_BG` and `ORDER_BG` lists, so swapping a real set in is one
line per slot.

### The cover — 1 file, `--ar 16:9`

| slot | prompt subject |
|---|---|
| `hero` | `Alan Watts seated in profile on the right-hand third, looking out over an empty horizon, the left two-thirds an open cream sky with nothing in it` — **`--ar 16:9`**, deliver 2000 × 1125 |

**The left 58% must be empty.** The cover lockup — logo, an 88px title, the
subtitle, three chips and the Begin button — is left-aligned and capped there.
The current hero is a centred ZEN/TAO/NOW/BEING diagram, so the title sits on
top of the word ZEN. It is legible and it is not right.

Keep the existing diagram — it is a genuinely good concept map and it is what
the library card is cut from. It just wants to be a *teaching* plate rather
than the cover: `data-bg` on the "Who was Alan Watts?" slide would use it well.

### The framed plates — 9 files, `--ar 7:6`

| slot | where it appears | prompt subject |
|---|---|---|
| `plate-a` | Idea one — the separate self | `a man's face in close-up, one hand resting against his chin, mid-thought, concentric rings radiating behind his head` |
| `plate-b` | Idea three — impermanence | `a bearded man half-turned away, a single flower going over in the foreground, petals falling` |
| `plate-c` | The man — who he was | `a bearded man in profile watching a low sun sink behind layered hills, seen from behind and slightly below` |
| `plate-d` | Idea two — wu wei | `a man mid-gesture, one open palm raised, explaining something, loose concentric arcs behind him` |
| `plate-e` | In his own words | `a man standing at a microphone on a bare stage, three-quarter view, one warm spotlight` |
| `plate-f` | Comprehension questions | `a man's face split by hard light and shadow, half in slate blue and half in cream, looking directly out` |
| `plate-g` | Afterwards / activation | `a man walking away down a path between two hills, small in the frame, reel-to-reel tape spooling in the sky above him` |
| `plate-h` | Vocabulary | `a seated man with an open book face-down on his knee, looking up and away from it` |
| `plate-i` | Results / closing | `a man standing under a wide sky of flat stylised clouds, hands in coat pockets, calm` |

Four notes on the list:

- **Nine plates cover twenty-two art-bearing slides**, so several repeat. That
  is within HOUSE-STYLE §5c, which asks for one background per *section* plus
  activation, not one per slide. If you want to kill the repeats, the slots
  worth doubling first are `plate-f` and `plate-i`, which each carry four.
- **`plate-g` is the activation plate.** It is the last thing a learner sees,
  so the walking-away composition is doing a job; do not swap it for another
  head-and-shoulders.
- **Head-and-shoulders fills the frame, which is why the deck no longer uses
  the arch.** If you want `data-art="arch"` back, these need the subject clear
  of the top ~15% at both corners — that means half-body or wider, not
  close-ups. It is a real trade and the plain 22px corner is fine.
- **No text in the pictures.** Two of the supplied renders carried a stray
  Midjourney glyph near an outer edge. The 7:6 re-crop happened to remove
  both, which is luck rather than process — a native 7:6 render has no outer
  sixth to lose them in, so `no text, no logos, no brand marks` has to do the
  work in the prompt. Checked on the shipped files: all nine corners are
  clean.

---

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
