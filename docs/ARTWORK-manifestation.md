# Artwork brief: Manifestation — Can You Think It Into Being? (B2)

> **DONE 2026-10-13.** The two-chairs render came afterwards and is `plate-act`.
>
> **First delivery, five of six.** Innes rendered eleven files (two or
> three variants of five slots); picks: dandelion `_0` (cover), cork board
> `_0`, megaphone `_0`, magnifying glass `_0` (`_2` has a hand in it),
> balance `_2` (the only one with feather against stone). **No two-chairs
> render came**, so `plate-act` is the second dandelion (`_2`) for now; drop
> a two-chairs render into `incoming/manifestation/`, prep it as
> `plate-act`, and rebuild. The balance fills its frame, so its panel uses
> `plate-view-panel.jpg`, padded with its own sky and table rather than
> cropped (see the builder). The palette came out of the dandelion with
> `--light`; every row PASS.

Innes, 2026-10-13: *"make forbes lesson on manifestation - give me artwork
shopping list"*. **Six plates, one per slot.** The deck is built and passes
every gate except HEAD (which `seo.py` writes on the live page) against
stand-ins. `build_manifestation.py` writes the gitignored preview
`_forbes-manifestation-b2.html` until all six files below exist in
`manifestation/`, then stops once and asks for the palette (see the end),
then writes the live `forbes-manifestation-b2.html`. The builder creates the
drop folder `incoming/manifestation/` whenever it runs in preview mode, so
the folder exists.

## Format: house style 2, the panel

Every plate is used twice, so it has to survive both crops:

1. **Full bleed** on its part divider: the whole 16:9 frame.
2. **Panel**: a portrait slice (about 0.76) out of the same file, chosen by
   `pos=` in the builder, at full opacity beside the text column.

So: **`--ar 16:9`, upscaled to at least 2400 px wide**, and **the one
subject inside a vertical band about a third of the frame wide**, with flat
ground either side. The slot table says which third, and the builder's
`pos=` is already set to it.

## What the set matches

**The Alan Watts object plates** (`alan-watts/plate-a.jpg` … `plate-l.jpg`).
Manifestation is the same shelf (self-help, the mind, the present), and
those plates already prove the look: four flat tones, slate blue and blush
on cream, one brick-red accent, grain, one object with a long shadow. The
preview runs on copies of them (`manifestation/_ph-*.jpg`, gitignored), so
the deck you see now is close to the finished look. Give Midjourney
**`alan-watts/plate-a.jpg`** (the coat and its shadow) as `--sref`, because
it is the idea-in-negative-space plate, and that is what this set needs.

## The style stem

Every prompt is `<subject>, <stem>`:

```text
flat editorial illustration, posterised into four flat tones, two-tone slate blue and pale blush on a warm cream ground, one brick-red accent, heavy grain and halftone stipple, hard single light source, long soft shadow, no people, no faces, no hands, no text, no letters, no logos, generous negative space, subject contained in the <THIRD> of the frame with empty flat ground either side --ar 16:9 --style raw --sref <url of alan-watts/plate-a.jpg>
```

- **`no text, no letters`**: a vision board, a megaphone and a journal all
  invite lettering, and Midjourney lettering is garbage. Blank cards and
  shapes stand in for words.
- **`no hands`**: half these subjects are things a person holds.
- Replace `<THIRD>` with the slot's third.

## The shopping list — into `incoming/manifestation/`

| slot | where it appears | third / `pos=` | prompt subject |
|---|---|---|---|
| `plate-cover` | cover, and the default wash behind card and question slides | centre, calm in the middle | `a dandelion seed head on a plain table, its seeds lifting off and turning into small stars as they rise into an empty sky` |
| `plate-trend` | Part 1 divider + panel (the vocabulary: vision board, affirmation, the law of attraction) | left third / `20% 50%` | `a cork board on a bare wall with blank pinned cards and cut-out paper shapes of a house, a palm tree and a key, red string linking them` |
| `plate-claims` | Part 2 divider + panel (reporting a claim: *is said to*, *supposedly*) | right third / `80% 50%` | `a vintage megaphone lying on its side on a plain shelf, a drift of blank paper speech bubbles floating out of it` |
| `plate-evidence` | Part 3 divider + panel (the research, confirmation bias) | centre / `50% 50%` | `a magnifying glass resting on a field of clover, the one four-leaf clover under the lens shown huge, the ordinary clover outside it small` |
| `plate-view` | Part 4 divider + panel (the balanced view) | right-of-centre / `70% 50%` | `an old brass balance scale hanging perfectly level, a feather in one pan and a small stone in the other` |
| `plate-act` | activation stage background | centre, calm | `two simple chairs turned towards each other across a low table, a wishbone on the table between them, nobody in either` |

Notes:

- **`plate-cover` is the lesson's idea**: a wish turning into something.
  If the seeds-into-stars will not resolve in four flat tones, the
  fallback is `a single lit candle on a bare table, its shadow on the wall
  behind it shaped like an open door`.
- **`plate-evidence` is the one that will fight you.** The scale contrast
  (one clover huge under the lens) is the joke, and it is confirmation bias
  in one picture. If it comes back as a plain magnifying glass, keep the
  best one and say so; the deck still works.
- **`plate-act` is a pair-speaking slide**, so two empty seats, as in every
  activation brief in this family (Watts `plate-g` is the same idea). Do
  not swap it for a still life.

## Dropping the set in

```bash
py tools/prep-artwork.py incoming/manifestation --into manifestation --dry-run
py tools/prep-artwork.py "incoming/manifestation/<six files>" --into manifestation \
   --names plate-cover,plate-trend,plate-claims,plate-evidence,plate-view,plate-act
py lesson-template/extract-palette.py manifestation/plate-cover.jpg --light   # paste into PALETTE_LIVE
py lesson-template/build/build_manifestation.py      # writes the LIVE page
py tools/build_hubs.py
py tools/seo.py                                      # restores the SEO block; read its diff
node lesson-template/check-lesson.js forbes-manifestation-b2.html
node lesson-template/checker/answered-overflow.js forbes-manifestation-b2.html en de es
```

`--light` assumes the plates come back cream like the Watts set; if they
come back dark, drop it. Then look at every divider and panel once and tune
`pos=` by eye, because the checker cannot see a subject cut in half. Delete
`manifestation/_ph-*.jpg`. Add the row to `library.html`'s `LESSON_IMAGES`
(`"forbes-manifestation-b2.html": "manifestation/plate-cover.jpg"`), and the
catalogue row (title `Manifestation: Can You Think It Into Being?`, level
B2). `tools/topics.py` already files it under `passive-voice`.

## Round 2 — four quiet plates for the question slides (2026-10-13)

Innes, on the live deck: *"dandelion too repetitive - ask for more
artwork"*. Every card and question slide had no picture of its own and fell
back to the cover, so the dandelion sat behind 25 of 35 slides. **Fixed in
the builder at once with the art already in:** each part's slides now wear
that part's plate, and the dandelion is on the cover and results only.

These four finish the job: a **second plate per part for the question
slides**, so a part's teaching and its questions do not share a picture.
`build_manifestation.py` picks each one up the moment it exists in
`manifestation/` (`qbg()`); nothing else to edit.

**They sit BEHIND text**, washed, under cards, which is a different job from
the panels. So: **quiet, low detail, the subject small and low in the frame,
a wide empty field above it.** Same stem as round 1, `--ar 16:9`, same
`--sref`, with `<THIRD>` as `lower third, small`.

| slot | behind | prompt subject |
|---|---|---|
| `plate-trend-2` | Part 1 questions + match | `a small notebook lying open on a desk, a pencil across it, one folded paper star resting on the blank page` |
| `plate-claims-2` | Part 2 gap fills, sentence builders, questions | `two paper-cup telephones joined by a long taut string running across an empty wall` |
| `plate-evidence-2` | Part 3 sort + questions | `a glass laboratory flask on a plain shelf with one small white cloud floating inside it` |
| `plate-view-2` | Part 4 gap fills + questions | `a wooden signpost on an empty hilltop, two blank arms pointing in opposite directions` |

Drop them in [incoming/manifestation](../incoming/manifestation) (it exists), then:

```bash
py tools/prep-artwork.py "incoming/manifestation/<four files>" --into manifestation \
   --names plate-trend-2,plate-claims-2,plate-evidence-2,plate-view-2
py lesson-template/build/build_manifestation.py
py tools/seo.py
node lesson-template/check-lesson.js forbes-manifestation-b2.html
```
