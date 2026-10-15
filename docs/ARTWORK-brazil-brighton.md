# Artwork brief (Midjourney): Cold, Colder, the Coldest — From Brazil to Brighton (A1)

Five plates. The deck is built and passes every gate on placeholders;
`lesson-template/build/build_brazil_brighton.py` writes the gitignored preview
`_forbes-english-brazil-to-brighton-a1.html` until all five exist, and creates
the drop folder whenever it runs without them.

**Drop folder (it exists on Innes's machine):**
[C:\Users\black\Documents\FORBES\incoming\brazil-brighton](../incoming/brazil-brighton)

Save as `hero.png`, `ana.png`, `cold.png`, `drivers.png`, `homework.png`, then
tell a local session: *"The Brazil to Brighton pictures are in
incoming/brazil-brighton — put them in."*

## Format: house style 2, the panel

Each plate is seen whole on its stage's opening slide, as a tall slice beside
the reading text, and faintly behind the questions, whose answers sit on the
left. So `--ar 16:9`, the subject **between the middle and the right edge**,
and the **left third plain**.

## Style

Flat screen-print editorial, matched to the live A1 food deck with
`--sref https://forbesenglish.com/FoodA1P2/hero.jpg`.

Ana is in two plates (ana, homework): render `ana` first and add its URL to
`homework` as `--oref <url> --ow 100`.

## Prompts

1. **hero** — cover and the accent stage
   `Brighton seafront on a bright breezy day, the Palace Pier stretching out into a blue-green sea, pebble beach, striped deckchairs, seagulls overhead, a young woman pushing a toddler in a buggy along the promenade, flat screen-print editorial illustration, bold flat shapes, limited palette of coral, navy, sea green and cream, fine grain, subject between the middle and the right edge of the frame, plain empty sky and sea in the left third --ar 16:9 --style raw --sref https://forbesenglish.com/FoodA1P2/hero.jpg --no text, letters, numbers, signs, logos, watermark`

2. **ana** — stage 1, I am / he is / they are
   `a young Brazilian mother with dark curly hair holding her sixteen-month-old son on her hip, both smiling, on a pebble beach in front of a row of colourful beach huts, warm afternoon light, flat screen-print editorial illustration, bold flat shapes, coral, navy, mustard and cream, fine grain, figures between the middle and the right edge of the frame, plain empty left third --ar 16:9 --style raw --sref https://forbesenglish.com/FoodA1P2/hero.jpg --no text, letters, numbers, signs, logos, watermark`

3. **cold** — stage 2, cold / colder / the coldest
   `the north of Scotland in winter, a frosty field running down to a grey firth, a small white cottage with smoke from the chimney, snowy hills far away, one figure in a thick coat and scarf walking a dog, cold pale light, flat screen-print editorial illustration, bold flat shapes, icy blue, slate, white and one coral accent, fine grain, cottage and figure between the middle and the right edge of the frame, plain empty left third --ar 16:9 --style raw --sref https://forbesenglish.com/FoodA1P2/hero.jpg --no text, letters, numbers, signs, logos, watermark`

4. **drivers** — stage 3, lorry / van / taxi driver / chauffeur
   `a British street with four vehicles in a row: a big lorry, a white delivery van with its driver carrying a parcel, a black taxi, and a shiny black car with a chauffeur in a cap holding the back door open, morning light, flat screen-print editorial illustration, bold flat shapes, navy, coral, white and black, fine grain, vehicles between the middle and the right edge of the frame, plain empty road and wall in the left third --ar 16:9 --style raw --sref https://forbesenglish.com/FoodA1P2/hero.jpg --no text, letters, numbers, signs, logos, watermark, number plates`

5. **homework** — translate, results, activation
   `a young mother studying English at a kitchen table late in the evening, laptop open, headphones on, a cup of tea and a notebook, through an open door a toddler asleep in a cot, warm lamp light against a blue night window, flat screen-print editorial illustration, bold flat shapes, navy, coral and warm cream, fine grain, woman between the middle and the right edge of the frame, plain empty wall in the left third --ar 16:9 --style raw --sref https://forbesenglish.com/FoodA1P2/hero.jpg --oref <url of ana> --ow 100 --no text, letters, numbers, screen text, logos, watermark`

## When they land

```bash
py tools/prep-artwork.py <the five files> --into BrazilBrighton --names hero,ana,cold,drivers,homework
py lesson-template/extract-palette.py BrazilBrighton/hero.jpg          # add --light if the hero is bright
```

Paste the block into `PALETTE_LIVE` in the builder (every row must PASS), re-run
it, then the catalogue row, `build_hubs.py` and `seo.py` (`/publish` does all of it).
