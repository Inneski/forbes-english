# Artwork brief: The Mystery of Marilyn Monroe — Prepositions (B1)

Innes, 2026-10-04: *"make marilyn house style 2"*. The deck is rebuilt as a
panel deck (`lesson-template/build/build_marilyn.py`) and is **live now**,
on crops of the two portraits already in `Marilyn/`. HOUSE-STYLE §5c wants a
picture per section plus one for the activation stage; the two portraits
cover the cover + stage 1 (`marilyn-hero.jpg`) and stage 2
(`marilyn-detail.jpg`). **Three plates are missing.** Each one is picked up
by the builder as soon as its file exists in `Marilyn/`; nothing else
changes.

**Drop folder: `incoming/marilyn/`** — the builder creates it whenever a
plate is missing, so it exists on this machine now. Then `/publish`.

## What the set matches

The two portraits are the reference: flat screen-print vector, coral, salmon
pink and cream on a dusty slate blue, solid black shadow shapes, a fine
speckle over the flat colour. The plates are objects, not people — **no
faces, no Marilyn** — so the portraits stay the only two pictures of her.

## Format: house style 2, the panel

Every plate is used full bleed on its stage divider and, for `plate-reel`,
also as a 548×720 portrait slice beside the text (`pos=` set by the
builder). So `--ar 16:9`, at least 2000 px wide, and the subject inside the
named third with flat ground either side.

Stem (the shopping list's, with this family's colours):

```text
flat vector illustration, cel-shaded, solid flat colour, minimalist, Noma Bar style, one idea in negative space, wide landscape, coral and salmon pink and cream with slate-blue and black silhouettes, subtle screen-print speckle, no text, no letters, no logos, no signage, no faces, subject contained in the <THIRD> of the frame with empty flat ground either side --ar 16:9 --style raw --no photorealistic, gradient, depth of field, perspective
```

## The three slots

| File | Used on | Third | Subject |
|---|---|---|---|
| `plate-grate.jpg` | stage 2 divider, the "Which way does it go?" cards, the subway-grate question | centre | a subway grate seen from above, with one white skirt-shaped gust of air rising out of it — the dress implied by the shape of the air, no figure |
| `plate-reel.jpg` | stage 3 divider and panel, the partner cards, the sort | left third | a single film reel, with a ribbon of film unspooling from it in a loop |
| `plate-seats.jpg` | the activation stage | centre | two cinema seats side by side, one folded down, facing the same way — the pair-speaking motif |

Until they arrive the builder uses: grate → `marilyn-detail.jpg`, reel →
`marilyn-hero.jpg` cropped to the earring (`pos='82% 50%'`), seats →
`marilyn-detail.jpg`.
