# Artwork brief: Contingency Plans & Trade-offs (C1)

Innes, 2026-09-27: *"u will need artwork"*. **Six plates, one per slot.** The
deck is built and passes every gate against placeholders;
`build_contingencytradeoffs.py` writes the gitignored preview
`_contingency-trade-offs-vocab.html` until all six files below exist in
`Construction3/`, then writes the live `contingency-trade-offs-vocab.html`.
The live page is untouched until then (the Mixed Grammar precedent).

## Format: house style 2, the panel

Every plate is used twice, so it has to survive both crops:

1. **Full bleed** on its stage divider: the whole 16:9 frame.
2. **Panel**: a 548×720 slice (aspect 0.76, portrait) out of the same file,
   chosen by `pos=` in the builder, at full opacity beside the text column.

So: **`--ar 16:9`, upscaled to at least 2400 px wide** (the staged plates are
2944×1648), and **the one subject inside a vertical band about a third of the
frame wide**, with flat ground either side. The slot table says which third;
the builder's `pos=` is already set to that third. A wide composition with
the idea spread across the frame will not survive the panel.

## What the set matches

The four site pictures already in `Construction3/` (`hero.jpg`, `a.jpg`,
`b.jpg`, `c.jpg`) are the style reference: flat editorial vector, dusty
slate-blue sky, cream and pale concrete, one brick-red / coral accent, black
silhouettes, light grain. Give Midjourney `a.jpg` as `--sref`. They stay on
disk as placeholders and are not used by the finished deck.

**Found and considered:** three tower-crane renders already in `incoming/`
(`blackisler_a_single_tower_crane_against_a_flat_sky_above_an_u_4cf0f5fc…_0/_2/_3.png`,
2944×1648). Right palette, but they are textured concrete rather than flat
vector, and the crane is spread across the frame. `_2` could stand in for
`plate-site` if Innes likes it (subject centred, crop `pos='50% 50%'`);
nothing in `Downloads/` fits.

## The style stem

Every prompt is `<subject>, <stem>`:

```text
flat editorial vector illustration in the style of Noma Bar, one idea in negative space, dusty slate blue sky, cream and pale concrete, a single brick-red accent, solid black silhouettes, light grain, construction site, calm, no text, no letters, no logos, no signage, no faces, subject contained in the <THIRD> of the frame with empty flat ground either side --ar 16:9 --style raw --sref <url of Construction3/a.jpg>
```

- **`no text, no signage`**: sites are full of signs and blueprints invite
  lettering. Midjourney lettering is garbage.
- **`no faces`**: silhouettes of workers are fine and on-style; faces are not.
- Replace `<THIRD>` with the slot's third.

## The shopping list — into `Construction3/`

| slot | where it appears | third / `pos=` | prompt subject |
|---|---|---|---|
| `plate-cover` | cover (washed under the title) and the default wash behind card and question slides | centre, calm in the middle | `a half-built concrete tower with one tower crane beside it at dusk, a low red sun, wide empty sky above` |
| `plate-plans` | Part 1 divider + panel (contingency plan, ad hoc, trade-off, shortfall) | right third / `88% 50%` | `a crane hook holding two loads on a balance beam, one heavy block and one light, the beam tilted — a trade-off` |
| `plate-site` | Part 2 divider + panel (moisture, firmness, retrofit, fire-retardant) | centre-left / `40% 50%` | `a cutaway section of a wall showing layers: brick, insulation, a membrane, one drop of water beading on the surface` |
| `plate-people` | Part 3 divider + panel (arduous, exhaustion, persuasive, take for granted) | right third / `82% 50%` | `a lone worker silhouette sitting on a steel beam high above the site at the end of the day, hard hat in hand` |
| `plate-test` | Part 4 divider + all three quiz-section panels (crops at 15%, 50%, 85%) | three uprights, one per third / `15%`, `50%`, `85%` | `three identical scaffold towers standing apart in a row, each a different height, one red` |
| `plate-act` | activation stage background | centre, calm | `two folding chairs facing each other beside a site cabin, a rolled plan on a crate between them, nobody in either` |

Notes:

- **`plate-test` is cropped three ways.** The three towers must sit roughly at
  15%, 50% and 85% across so each quiz panel gets one. If they drift, move the
  percentages in `quiz_intro(...)` rather than re-rendering.
- **`plate-plans` is the lesson's idea** (plan A against plan B, what you give
  up). If the balance beam will not resolve flat, the fallback is
  `two cranes lifting the same beam from opposite ends`.
- **`plate-act` is a pair-speaking slide**, so two empty seats, as in the
  Mixed Grammar brief. Do not swap it for a still life.

## Dropping the set in

```bash
py tools/prep-artwork.py incoming/ --into Construction3 --dry-run
py tools/prep-artwork.py "incoming/<six files>" --into Construction3 \
   --names plate-cover,plate-plans,plate-site,plate-people,plate-test,plate-act
py lesson-template/build/build_contingencytradeoffs.py     # writes the LIVE page once all 6 exist
py tools/seo.py                                              # restores the SEO block; read its diff
node lesson-template/check-lesson.js contingency-trade-offs-vocab.html
node lesson-template/checker/answered-overflow.js contingency-trade-offs-vocab.html en de
```

Then look at every divider and panel once and tune `pos=` by eye: the checker
cannot see a subject cut in half. Re-run `extract-palette.py` on
`plate-cover.jpg` and paste the result into `PALETTE` if the cover changes
the colours. Then set `deck = true` (SQL in HANDOFF).
