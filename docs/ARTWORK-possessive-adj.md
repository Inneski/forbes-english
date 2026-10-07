# Artwork brief (Midjourney): My Cat, Your Dog — possessive adjectives (A1, young learners)

Innes, 2026-10-07: *"make a type 2 lesson and ask for artwork … should appeal
to young learners"*, then *"it is for midjourney"*. **Five plates.** The deck
is built and passes every gate on placeholders; `build_possessive_adj.py`
writes the gitignored preview `_forbes-english-possessive-adjectives-a1.html`
until all five files exist, and creates the drop folder whenever it runs
without them.

**Drop folder (it exists):**
[C:\Users\black\Documents\FORBES\incoming\possessive-adj](../incoming/possessive-adj)

Save as `hero.png`, `mia.png`, `leo.png`, `near-far.png`, `pet-show.png`,
then tell a local session: *"The possessive pictures are in
incoming/possessive-adj — put them in."*

## Format: house style 2, the panel

Each plate is used three ways: **whole** on its stage's opening slide;
as a **tall slice** (548×720, the band from about 45% to 85% across) beside
the reading text; and **faintly behind the questions**, whose answers sit on
the left. So: **`--ar 16:9`**, everyone **between the middle and the right
edge**, and the **left third plain**. A wide group spread across the frame
will not survive the slice.

## Characters stay the same: make the cover first

Midjourney does not remember people between prompts. Render **plate 1** first,
pick the best one, copy its image URL, and add it to plates 2–5 as an
omni-reference: `--oref <url> --ow 100` (V7; on V6 the same idea is
`--cref <url> --cw 100`). Lower `--ow` if it starts copying the garden too.

## The style stem

Every prompt is `<subject>, <stem>`:

```text
flat children's picture-book illustration, simple rounded shapes, clean flat colour, soft paper grain, warm cheerful pastels butter yellow peach mint sky blue with tomato red and deep teal accents, friendly cartoon characters with simple dot eyes and small smiles, sunny and sweet, characters on the right side of the frame, plain empty left third --ar 16:9 --style raw --no text, letters, numbers, signs, logos, watermark, realistic, photo, 3d render, gradient, scary
```

## The cast (repeat the bits each prompt needs)

- **Mia**, girl of nine: brown high ponytail, yellow T-shirt, denim dungarees.
  **Pepper**, her black-and-white cat with white paws.
- **Leo**, her little brother, seven: short sandy hair, red hoodie, green
  shorts. **Biscuit**, his golden-brown floppy-eared puppy; red ball, bright
  blue dog bed.
- **Snowy**, the family's white rabbit with pink ears.
- **Grandpa Joe**: grey beard, flat cap, green cardigan; **Rio**, a blue and
  yellow parrot.
- **Ella and Sam**, twin girl and boy, red-and-white striped jumpers;
  **Tank**, their tortoise.
- **Mr Brown**, teacher: round glasses, brown jacket; a goldfish in a round
  bowl.

## The five prompts

**1 · `hero.png` — the cover**
```text
a girl of nine with a brown high ponytail, yellow T-shirt and denim dungarees sitting on a garden lawn hugging a black-and-white cat, her little brother with sandy hair and a red hoodie kneeling beside her while a golden-brown floppy-eared puppy licks his face, a white rabbit sitting in front of them, low wooden fence and one round tree behind, sunny afternoon, <stem>
```

**2 · `mia.png` — Mia and her cat**
```text
the girl with the brown ponytail and yellow T-shirt sitting on her bed proudly holding up her black-and-white cat, soft cushions, a window with blue sky, a small cat bowl on the floor, plain pale wall on the left, <stem> --oref <cover url> --ow 100
```

**3 · `leo.png` — Leo and his puppy**
```text
the little boy with sandy hair and a red hoodie who has just thrown a red ball, the golden-brown floppy-eared puppy leaping after it with ears flying, a bright blue dog bed by the back door of the house, open lawn on the left, <stem> --oref <cover url> --ow 100
```

**4 · `near-far.png` — this and that**
```text
close to the viewer and large, the girl with the brown ponytail holding a white rabbit in her arms; behind her the boy in the red hoodie points far into the distance at a tiny brown horse standing on a faraway green hill, strong sense of near and far, open sky and grass on the left, <stem> --oref <cover url> --ow 100
```
The point of the picture is that the rabbit is **close** and the horse is
**far**. If the horse comes back big, add `tiny distant horse` again and
reroll; do not accept a horse at the children's scale.

**5 · `pet-show.png` — the school pet show**
```text
a sunny school playground pet show with plain coloured bunting, a grandpa with a grey beard, flat cap and green cardigan with a blue and yellow parrot on his shoulder, twin girl and boy in red-and-white striped jumpers holding up a tortoise, a teacher with round glasses and a brown jacket behind a small table with a goldfish in a round bowl, happy and busy but not crowded, plain playground and sky on the left, <stem> --oref <cover url> --ow 50
```
`--ow 50` here: only Mia and Leo's family style should carry over, and four
new characters need room.

## Checking a render before saving it

- Everyone between the middle and the right edge; the left third plain.
- No lettering anywhere — bunting and the cat bowl invite it.
- Flat colour, not a painterly 3D render. A filename is not evidence of
  style (HANDOFF, 2026-09-24): open the picture.
- Mia's yellow T-shirt and Leo's red hoodie are the same in all five.

## For the session that puts them in

```bash
py tools/prep-artwork.py incoming/possessive-adj/hero.png incoming/possessive-adj/mia.png incoming/possessive-adj/leo.png incoming/possessive-adj/near-far.png incoming/possessive-adj/pet-show.png --into PossessiveAdj --names hero,mia,leo,near-far,pet-show
py lesson-template/extract-palette.py PossessiveAdj/hero.jpg --light   # paste into PALETTE_LIVE
py lesson-template/build/build_possessive_adj.py                       # now writes the live page
node lesson-template/check-lesson.js forbes-english-possessive-adjectives-a1.html
```

then the catalogue row, `tools/build_hubs.py`, `tools/seo.py`, commit, push.
Panels use `pos='78% 50%'`; if a subject sits further left, pass a `pos=`
for that panel rather than recropping the file.
