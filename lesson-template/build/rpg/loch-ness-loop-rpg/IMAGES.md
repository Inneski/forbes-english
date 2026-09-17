# THE LOCH NESS LOOP — the image list

These are the rules every one of the thirty-two prompts obeys. The prompts
themselves are generated from the final script and appended below; if a
prompt and this contract disagree, the contract wins and the prompt is wrong.

Thirty-two plates, numbered in play order to match the **Picture** field in
`STORY.md` and the `image` keys in `data.json`. One picture per scene plus a
cover; the briefing reuses `04_q3_shop3.webp`; the four endings have their
own plate. Nothing else is reused, and no two filenames may hold the same
picture.

## 16:9, and how to get it from a 3:2 model

**Deliver 16:9.** The plates are 1536 × 864 WebP under 200 KB; `prep-plates.py`
in this folder does the crop, the resize and the squeeze. Midjourney takes
`--ar 16:9` and gives it to you directly. ChatGPT's image model renders 3:2
(1536 × 1024) only; a 3:2 render is centre-cropped to 16:9, which takes 80 px
off the top and 80 px off the bottom. So on a 3:2 render **keep the object,
the light source and any face inside the middle 84% of the height** — nothing
that matters in the top or bottom eighth — and the crop costs nothing.

## The style contract — paste this sentence verbatim at the start of every prompt

> Flat vector illustration, cel-shaded, solid flat colours and clean
> geometric shapes, no outlines, soft long shadows, a faint paper grain;
> Highland light after rain in mid-September: loch-slate blue, bracken
> orange, heather purple, moss green and wet grey stone, with one warm amber
> light source in every frame; eye-level camera; characters with simple,
> expressive faces.

Written below as **[STYLE]**. It never varies, and it is `meta.style` in
`data.json`. Two plates lit differently read as two games; a plate with black
outlines among plates without them reads as a different artist.

## Four rules that cannot bend

1. **No lettering anywhere.** No shop name, no price card, no hire form, no
   road sign with words, no map labels, no bus destination, no writing on
   the phone screen, no logo on a jersey, no bunting with letters. Image
   models garble English and a broken word on a language lesson reads as a
   mistake in the lesson. Every clue in the script names a physical object,
   never a written one. End every prompt with
   `--no text, letters, writing, signage, logo, watermark`.
2. **The glowing object sits right of centre — between 60% and 94% of the
   width — and the left half of the frame stays quiet:** open water, sky,
   a bare wall, an empty road, a plain counter. The dark glass text panel
   sits on the left and reaches 56% of the width when a gloss language is
   on. Nothing that must be seen lives left of the middle. Sherlock: The
   Blue Hour composed every plate this way and is the only export that has
   ever needed no hotspot adjustment.
3. **Light enough to glow.** The marker takes its colour from the object
   under it. The pub at dusk, the pier at six in the morning, the loch at
   first light, the phone on the counter — each needs its amber light *on
   or beside the object*: the bar lamp, the launch's brass lamp, the
   sunrise behind her, the screen itself. No crushed blacks, no heavy
   grain, no lens flare, no fog over the object.
4. **One look per character, every plate.** Vector art drifts less than
   paint, but a red-haired woman drawn from twenty prompts is three women
   unless the line below is pasted into every prompt she appears in. Paste
   it. Do not paraphrase it.

## The character sheet — paste the line for anyone in the frame

- **Alex Marin (you):** thirties, short dark curly hair, olive skin, a bright
  blue waterproof jacket, dark leggings, a plain white hire helmet, a small
  black backpack. Seen from behind or three-quarter whenever possible — the
  player is Alex.
- **Shona Nicolson:** tall, early thirties, very long straight copper-red
  hair worn loose, pale skin with freckles, wide grey-green eyes, a dark
  green work apron over a grey T-shirt, black jeans, a pencil behind one ear.
- **Moira Fraser:** sixties, round, short silver-grey curls, red-framed
  glasses, a purple fleece, a pint of ale in her hand.
- **Jean Cameron:** fifties, lean, cropped grey hair, a navy cycling gilet
  with no writing over a checked shirt, reading glasses on a cord, a half
  pint of lager.
- **Archie MacRae:** seventies, small and broad, white stubble, a flat tweed
  cap, a yellow oilskin jacket over a navy jumper, a chipped enamel mug.
- **The club rider (shore road only):** forties, an orange club jersey with
  no writing, black shorts, a white road bike, sunglasses pushed up.
- **The farmer (high road only):** fifties, a green boiler suit, a wax cap,
  a black-and-white collie on the back of a red quad bike.
- **The bike:** a yellow hybrid hire bike — flat handlebars, a black rear
  pannier rack, silver mudguards, a black saddlebag under the saddle, a
  silver bell, no lettering on the frame.
- **The e-bike (shop only):** a grey step-through e-bike with a black
  battery pack on the down tube and a small green charge light.
- **Archie's launch:** an old wooden launch, dark green hull, varnished
  timber cabin, a brass lamp on the cabin roof, an orange fender on the
  side, an outboard-free stern with a tiller.
- **Her:** never shown whole. A long wet dark-green back with a rim of pink
  dawn light along it; a white wake with nothing in front of it; a neck
  like a curve of kelp against the sunrise. No face detail, no eye, no full
  body on any plate, and never on the cover as more than a shadow under the
  water.

## The plate list

| file | scene | glowing object |
|---|---|---|
| `01_cover.webp` | cover | the yellow hybrid bike on the shingle at Dores |
| `02_q1_shop1.webp` | `shop1` | the yellow hybrid at the counter |
| `03_q2_shop2.webp` | `shop2` | the e-bike's battery, green charge light on |
| `04_q3_shop3.webp` | `shop3` (and the briefing) | the saddle on the workstand |
| `05_q4_shop4.webp` | `shop4` | the right-hand brake lever on the handlebars |
| `06_q5_shop5.webp` | `shop5` | the rear derailleur on the back wheel |
| `07_q6_shop6.webp` | `shop6` | the loaded bike at the railing over the river |
| `08_choice1_dores.webp` | `dores` | the fork in the road above the beach, a bare signpost |
| `09_q7_shore1.webp` | `shore1` | the flat back tyre |
| `10_q8_shore2.webp` | `shore2` | the tyre lever hooked under the tyre |
| `11_q9_shore3.webp` | `shore3` | the club rider's orange jersey |
| `12_q10_shore4.webp` | `shore4` | the chain hanging off the chainring |
| `13_q7_hill1.webp` | `hill1` | the front wheel at the cattle grid |
| `14_q8_hill2.webp` | `hill2` | the mini pump on the valve |
| `15_q9_hill3.webp` | `hill3` | the farmer's red quad bike at the gate |
| `16_q10_hill4.webp` | `hill4` | the cassette on the back wheel |
| `17_q11_pub1.webp` | `pub1` | Moira's pint glass under the bar lamp |
| `18_q12_pub2.webp` | `pub2` | the pub window with the loch at dusk |
| `19_q13_pub3.webp` | `pub3` | the rear brake on the bike by the pub door |
| `20_choice2_pier.webp` | `pier` | the brass lamp on Archie's launch at the pier |
| `21_q14_deep1.webp` | `deep1` | Archie's hand on the tiller |
| `22_q15_deep2.webp` | `deep2` | the orange strap over the pannier rack |
| `23_q16_deep3.webp` | `deep3` | the wet back and white wake, the castle behind |
| `24_q14_bay1.webp` | `bay1` | the gulls on the flat water |
| `25_q15_bay2.webp` | `bay2` | the front wheel off, leaning on the thwart |
| `26_q16_bay3.webp` | `bay3` | the neck against the sunrise |
| `27_q17_back1.webp` | `back1` | the bent rear mudguard |
| `28_q18_back2.webp` | `back2` | the notes on the shop counter |
| `29_ending_master.webp` | `end_master` | the photo pinned on the shop wall |
| `30_ending_complete.webp` | `end_complete` | the phone on the counter, a wake on the screen |
| `31_ending_missing.webp` | `end_missing` | the phone in the open pannier on the counter |
| `32_ending_failed.webp` | `end_failed` | the bike on the rack of the bus at Fort Augustus |

## Checklist before the plates are handed over

- 32 files, named as above, no alternates, no superseded versions.
- The object is right of centre in every one and the left half is quiet.
- Every dusk, dawn and indoor plate has its amber light on or beside the
  object.
- Not one letter anywhere: check the shop, the jersey, the signpost, the
  phone, the bus, the bank notes (plain paper, no numerals).
- Shona's hair is long, straight and copper-red in every plate she is in;
  Jean has the glasses on a cord; Archie has the cap; the bike is yellow.
- Her: back, wake, neck. Never a face, never the whole animal.

# The plates

Each entry is the file, the scene, the object the glow sits on, and a draft
hotspot box `[cx, cy, w, h]` in percent of the 16:9 frame (centre, then
size). **The boxes are written from the prompts, not measured.** Read every
one off a gridded contact sheet once the plates exist, then screenshot every
scene closed and fix what missed. `[STYLE]` is the sentence in the contract
above, pasted verbatim.

---

### 01_cover.webp — the cover
**Object:** the yellow hybrid bike on the shingle at Dores · **hot** `[76, 60, 20, 24]`

> [STYLE] Late morning on the shingle beach at Dores, the loch flat and grey to the horizon. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — stands on its kickstand at the water's edge, warm sun through a gap in the cloud on its frame. Beside it, back to us, Alex Marin: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack. Under the flat water beyond the bike, a dark shadow the length of three boats, a shadow only, no detail. Open water and low cloud fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 02_q1_shop1.webp — `shop1`, CHAPTER 1 · THE SHOP
**Object:** the yellow hybrid at the counter · **hot** `[74, 58, 24, 30]`

> [STYLE] Inside a small bike shop at nine on a grey morning, a plain wooden counter running across the frame. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — has just been wheeled up to the counter, an amber work lamp on the counter lighting its frame. Behind it, one hand on the saddle, Shona Nicolson: tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear. The left of the frame is the bare counter top and a plain painted wall. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 03_q2_shop2.webp — `shop2`, CHAPTER 1 · THE SHOP
**Object:** the e-bike's battery, green charge light on · **hot** `[72, 62, 14, 18]`

> [STYLE] The same small bike shop, grey morning light from a window. On the right, a grey step-through e-bike with a black battery pack on the down tube and a small green charge light, the light lit and the battery under an amber work lamp clamped to a shelf above. Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — taps one finger on the battery, three-quarter to us, unconvinced. No yellow bike in this frame. The left of the frame is a bare whitewashed wall and empty floor. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 04_q3_shop3.webp — `shop3`, CHAPTER 1 · THE SHOP (and the briefing)
**Object:** the saddle on the workstand · **hot** `[70, 46, 12, 16]`

> [STYLE] The bike shop workshop, an amber lamp hanging low over a black workstand. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — is clamped in the stand, and its black saddle sits high in the lamplight, the small quick-release lever under it catching the light. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands astride it from behind, one foot on the floor. Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — holds a phone up, its back to us. A bare brick wall fills the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 05_q4_shop4.webp — `shop4`, CHAPTER 1 · THE SHOP
**Object:** the right-hand brake lever on the handlebars · **hot** `[78, 50, 14, 14]`

> [STYLE] A close view over the flat handlebars of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — inside the shop, the right-hand brake lever on the right of the frame lit by an amber lamp above the bench. Two pairs of hands: Alex Marin's, seen from behind — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — on the grips, and over them the freckled hands of Shona Nicolson: tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear, her hair falling into the right edge of the frame. The left of the frame is a plain grey shop wall. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 06_q5_shop5.webp — `shop5`, CHAPTER 1 · THE SHOP
**Object:** the rear derailleur on the back wheel · **hot** `[76, 62, 12, 16]`

> [STYLE] Low in the bike shop workshop, the back wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — held up in a workstand on the right. The rear derailleur, a sprung silver arm with two tiny jockey wheels under the stack of cogs, sits in a pool of amber light from a lamp clamped to the bench. Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — crouches beyond the wheel, one hand turning the pedal, watching the chain move. The left of the frame is bare concrete floor and a plain wall. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 07_q6_shop6.webp — `shop6`, CHAPTER 1 · THE SHOP
**Object:** the loaded bike at the railing over the river · **hot** `[74, 58, 22, 30]`

> [STYLE] Outside the shop on a wet pavement by a wide grey river in Inverness, mid-morning after rain. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — leans loaded against an iron railing, a black pannier on the rack, a break in the cloud putting warm low sun on its frame. Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — points away downriver. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands beside her, back to us, following her arm. The river and a pale sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 08_choice1_dores.webp — `dores`, ROUTE CHOICE 1
**Object:** the fork in the road above the beach, a bare signpost · **hot** `[72, 48, 10, 30]`

> [STYLE] A road above the beach at Dores, late morning, the tarmac still dark from rain. On the right the road splits at a plain wooden signpost with two blank, weathered arms and no writing, one arm pointing along the shore, the other up towards moorland; the low sun through cloud lights the post warm. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands astride a yellow hybrid hire bike, flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame, seen from behind at the post, looking at the two roads. The flat grey loch and the shingle beach fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 09_q7_shore1.webp — `shore1`, CHAPTER 2 · THE SHORE ROAD
**Object:** the flat back tyre · **hot** `[76, 64, 16, 20]`

> [STYLE] Early afternoon on the shore road, the loch flat and slate-grey at the edge of the tarmac. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — leans against a mossy drystone wall, its back tyre squashed flat against the road and a single thorn standing out of the rubber. A patch of warm sun through the cloud lights the flat tyre. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — crouches by the wheel, three-quarter from behind. The empty loch and a low sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 10_q8_shore2.webp — `shore2`, CHAPTER 2 · THE SHORE ROAD
**Object:** the tyre lever hooked under the tyre · **hot** `[78, 56, 12, 14]`

> [STYLE] Close on the grass verge of the shore road, afternoon. On the right, the back wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — is off the bike and held upright in two hands, a blue plastic tyre lever hooked under the edge of the tyre and clipped to a spoke, a second lever on the grass beside a folded spare tube and a mini pump, warm afternoon sun on the lever. The hands belong to Alex Marin, seen from behind and above: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack. Flat grey water and a stony shore fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 11_q9_shore3.webp — `shore3`, CHAPTER 2 · THE SHORE ROAD
**Object:** the club rider's orange jersey · **hot** `[76, 44, 14, 30]`

> [STYLE] The shore road in the afternoon, wet tarmac, bracken orange on the bank. On the right, a club rider — forties, an orange club jersey with no writing, black shorts, a white road bike, sunglasses pushed up — has stopped astride his bike and leans down to press a thumb into the back tyre of a yellow hybrid hire bike, flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame, the tyre now round again. The low sun makes his jersey the brightest thing in the frame. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — holds the bike, back to us. The loch, flat and empty, fills the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 12_q10_shore4.webp — `shore4`, CHAPTER 2 · THE SHORE ROAD
**Object:** the chain hanging off the chainring · **hot** `[76, 62, 14, 18]`

> [STYLE] A steep road climbing out of a wooded village on the shore, late afternoon, birch and pine on the bank. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — is stopped on the slope, and the chain hangs slack below the big chainring at the pedals, its teeth bare, a shaft of warm sun between the trees lighting the dangling chain. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands over it from behind, looking down at the pedals. The road drops away to the loch far below and a pale sky on the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 13_q7_hill1.webp — `hill1`, CHAPTER 2 · THE HIGH ROAD
**Object:** the front wheel at the cattle grid · **hot** `[76, 62, 14, 20]`

> [STYLE] The high road over the moor, early afternoon, heather purple and wet grey stone, a few sheep in the distance. On the right, the front wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — rests on the iron bars of a cattle grid, one spoke visibly slack and bowed away from the others, warm sun through cloud on the rim. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — kneels at the wheel, three-quarter from behind, one finger on the loose spoke. An empty single-track road runs away across the moor on the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 14_q8_hill2.webp — `hill2`, CHAPTER 2 · THE HIGH ROAD
**Object:** the mini pump on the valve · **hot** `[78, 58, 12, 16]`

> [STYLE] A gravel lay-by on the moor road near a small stone bridge, mid-afternoon. On the right, the back wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — with a small black mini pump screwed onto the valve, the tyre visibly soft and squashed at the bottom, warm afternoon sun on the pump and the rim. The pumping hands of Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — enter from the right edge, the rest of Alex out of frame. A small dark lochan and a wide moorland sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 15_q9_hill3.webp — `hill3`, CHAPTER 2 · THE HIGH ROAD
**Object:** the farmer's red quad bike at the gate · **hot** `[78, 58, 22, 26]`

> [STYLE] A farm gate on the high road at the top of a long descent, late afternoon light warm and low. On the right, the farmer — fifties, a green boiler suit, a wax cap, a black-and-white collie on the back of a red quad bike — sits on the idling red quad at the open gate, one hand holding it, the sun on the quad's red bodywork. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands astride a yellow hybrid hire bike, flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame, back to us, at the edge of the gate. The road drops away to a distant green glen and a pale sky on the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 16_q10_hill4.webp — `hill4`, CHAPTER 2 · THE HIGH ROAD
**Object:** the cassette on the back wheel · **hot** `[78, 60, 12, 16]`

> [STYLE] A long straight drag of road across open moor, afternoon, bracken and heather either side. On the right, close and low, the back wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — with the stack of silver cogs, the cassette, catching a warm shaft of sun, the chain sitting on the largest cog. Above it the leg and black leggings of Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — pushing the bike from behind, the upper body cut by the right edge. The empty road climbs away into a wide moorland sky on the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 17_q11_pub1.webp — `pub1`, CHAPTER 3 · FORT AUGUSTUS
**Object:** Moira's pint glass under the bar lamp · **hot** `[72, 56, 10, 16]`

> [STYLE] Inside a small pub by the canal locks on a Wednesday evening, dark wood and a long bar. On the right, under a single amber brass bar lamp, a full pint of ale glows on the bar in front of Moira Fraser: sixties, round, short silver-grey curls, red-framed glasses, a purple fleece, a pint of ale in her hand, laughing towards us. Between her and the right edge, seen from behind on a stool, Alex Marin: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack, the helmet on the bar. At the far right, not looking up from her glass, Jean Cameron: fifties, lean, cropped grey hair, a navy cycling gilet with no writing over a checked shirt, reading glasses on a cord, a half pint of lager. The left of the frame is the empty end of the bar and a plain dark panelled wall. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 18_q12_pub2.webp — `pub2`, CHAPTER 3 · FORT AUGUSTUS
**Object:** the pub window with the loch at dusk · **hot** `[76, 44, 24, 34]`

> [STYLE] The corner of a pub at dusk, dark panelled wall. On the right, a small-paned sash window looks out on the loch lying flat as a plate under a violet and slate sky, the last light on the water, a brass oil-style lamp burning amber on the windowsill so the glass and the sill glow. In front of the window, backs to us and small, Moira Fraser — sixties, round, short silver-grey curls, red-framed glasses, a purple fleece, a pint of ale in her hand — and Jean Cameron — fifties, lean, cropped grey hair, a navy cycling gilet with no writing over a checked shirt, reading glasses on a cord, a half pint of lager — look out at it together. Nobody else in the frame. The left of the frame is bare dark panelling. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 19_q13_pub3.webp — `pub3`, CHAPTER 3 · FORT AUGUSTUS
**Object:** the rear brake on the bike by the pub door · **hot** `[76, 62, 14, 16]`

> [STYLE] Outside the pub door at dusk, a warm amber porch lamp over the step. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — is turned upside down on its saddle and handlebars, the back wheel up, and the rear brake, two rubber pads either side of the rim, sits directly under the porch lamp. Jean Cameron — fifties, lean, cropped grey hair, a navy cycling gilet with no writing over a checked shirt, reading glasses on a cord, a half pint of lager — kneels at the wheel with a small multi-tool, spinning it with one hand, her half set on the step. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — stands behind her, back to us. The dark canal basin and its lock gates under a dusk sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 20_choice2_pier.webp — `pier`, ROUTE CHOICE 2
**Object:** the brass lamp on Archie's launch at the pier · **hot** `[78, 42, 10, 14]`

> [STYLE] Six in the morning at a wooden pier at Fort Augustus, the sky deep blue before dawn and the loch a black mirror. On the right, moored to the pier, an old wooden launch, dark green hull, varnished timber cabin, a brass lamp on the cabin roof, an orange fender on the side, an outboard-free stern with a tiller — the brass lamp lit and throwing amber light over the cabin roof and the water. In the stern, Archie MacRae: seventies, small and broad, white stubble, a flat tweed cap, a yellow oilskin jacket over a navy jumper, a chipped enamel mug, waiting. On the pier planks, back to us, Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — holding a yellow hybrid hire bike, flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame. Dark, still water and hills fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 21_q14_deep1.webp — `deep1`, CHAPTER 4 · THE CASTLE
**Object:** Archie's hand on the tiller · **hot** `[78, 60, 14, 16]`

> [STYLE] Aboard the launch on the open loch at first light, the water flat and slate blue, pale pink at the horizon. On the right, in the stern of an old wooden launch, dark green hull, varnished timber cabin, a brass lamp on the cabin roof, an orange fender on the side, an outboard-free stern with a tiller, sits Archie MacRae: seventies, small and broad, white stubble, a flat tweed cap, a yellow oilskin jacket over a navy jumper, a chipped enamel mug, his weathered hand resting on the varnished tiller, the brass lamp still lit and casting amber light down onto that hand. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — sits low on the thwart in the middle distance, back to us, camera held below the wooden rail. Empty water and the wake behind the boat fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 22_q15_deep2.webp — `deep2`, CHAPTER 4 · THE CASTLE
**Object:** the orange strap over the pannier rack · **hot** `[76, 58, 16, 16]`

> [STYLE] The bow of the launch at first light, looking down into the boat, the loch a pale mirror beyond the gunwale. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — lies on its side in the bow of an old wooden launch, dark green hull, varnished timber cabin, a brass lamp on the cabin roof, an orange fender on the side, an outboard-free stern with a tiller, and a bright orange ratchet strap is cinched over the black pannier rack above the back wheel, the amber brass lamp and the pink dawn lighting the strap. The hands of Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — pull the strap tight, the rest of Alex out of frame at the right. Flat empty water and a pale sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 23_q16_deep3.webp — `deep3`, CHAPTER 4 · THE CASTLE
**Object:** the wet back and white wake, the castle behind · **hot** `[74, 54, 26, 16]`

> [STYLE] Open water off Urquhart Castle at sunrise, the loch flat and slate blue. On the right, fifty yards off, a long wet dark-green back breaks the surface with a rim of pink dawn light along it and a white wake trailing away from us, no head, no face, nothing more of the animal shown. Behind it on the far shore the ruined castle on its rock, the sun rising warm and amber beside the tower and lighting the wet back. In the lower right corner only the varnished rail of the launch; the camera is aboard, nobody in shot. Empty, still water and a pale pink sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 24_q14_bay1.webp — `bay1`, CHAPTER 4 · THE BAY
**Object:** the gulls on the flat water · **hot** `[74, 56, 26, 14]`

> [STYLE] A shallow weedy bay at first light where the river meets the loch, reeds along the shore, the water dead flat, mist lifting. On the right, a raft of thirty white gulls sits on the water off the reeds, the sunrise low and amber behind them so each bird is rimmed with light. In the lower right, the bow of an old wooden launch, dark green hull, varnished timber cabin, a brass lamp on the cabin roof, an orange fender on the side, an outboard-free stern with a tiller, drifts with no wake, Archie MacRae — seventies, small and broad, white stubble, a flat tweed cap, a yellow oilskin jacket over a navy jumper, a chipped enamel mug — a small still figure at the tiller, cap down. Empty grey-blue water and a bank of reeds in mist fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 25_q15_bay2.webp — `bay2`, CHAPTER 4 · THE BAY
**Object:** the front wheel off, leaning on the thwart · **hot** `[76, 58, 16, 22]`

> [STYLE] Inside the launch in the bay at first light, looking down the boat, the wooden thwart across the middle. On the right, the front wheel of a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — has been taken off and leans against the thwart, its silver quick-release lever flipped open, the bike's empty fork resting beside it; the brass lamp of an old wooden launch, dark green hull, varnished timber cabin, a brass lamp on the cabin roof, an orange fender on the side, an outboard-free stern with a tiller, burns amber on the cabin roof above the wheel. Archie MacRae — seventies, small and broad, white stubble, a flat tweed cap, a yellow oilskin jacket over a navy jumper, a chipped enamel mug — nods at it from the right edge. Still water past the gunwale and a pale dawn sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 26_q16_bay3.webp — `bay3`, CHAPTER 4 · THE BAY
**Object:** the neck against the sunrise · **hot** `[76, 46, 12, 30]`

> [STYLE] The bay at sunrise, flat water, reeds dark along the far shore. On the right, a long dark neck like a curve of kelp rises out of the water in silhouette against the amber disc of the rising sun, wet, no face detail, no eye, no head shape, nothing else of the animal shown; a white wake with nothing in front of it crosses the water below the neck. The sun behind the neck is the light in the frame. A few gulls in the air above the reeds. No boat and nobody in the frame. Empty pale water and a quiet grey-pink sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 27_q17_back1.webp — `back1`, CHAPTER 5 · THE NORTH SIDE
**Object:** the bent rear mudguard · **hot** `[78, 60, 14, 18]`

> [STYLE] A gravel walkers' path high above the north shore of the loch, late morning, birch and bracken, the water far below. On the right, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — leans against a moss-covered boulder, and its silver rear mudguard is bent inwards so that its edge touches the back tyre, warm sun on the crumpled silver. Alex Marin — thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack — crouches beside it, three-quarter from behind, thumb on the bend. Beyond the bike, just right of the middle and far down, the ruined castle on its rock in the loch. Open water and a wide sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 28_q18_back2.webp — `back2`, CHAPTER 5 · THE NORTH SIDE
**Object:** the notes on the shop counter · **hot** `[76, 60, 16, 14]`

> [STYLE] The bike shop counter at midday, grey light from the window and an amber work lamp on the counter. On the right, a small fan of plain paper bank notes, blank, no numerals or printing, lies on the wooden counter in the lamplight, the freckled hand of Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — laying the last one down, her face three-quarter and dry. Opposite her, seen from behind at the right edge, the shoulder and helmet of Alex Marin: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack. The bare left half of the counter and a plain wall fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 29_ending_master.webp — `end_master`, the master ending
**Object:** the photo pinned on the shop wall · **hot** `[78, 46, 12, 16]`

> [STYLE] The wall behind the shop counter at midday, a corkboard covered with small pinned snapshots of cyclists, none readable. On the right, under an amber wall lamp, Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — presses a pin into a new print: a dark curved shape on pink dawn water, no detail. Next to it, a print of Alex Marin astride a yellow bike. Below, back to us, Alex Marin: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack. Bare painted wall fills the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 30_ending_complete.webp — `end_complete`, the complete ending
**Object:** the phone on the counter, a wake on the screen · **hot** `[76, 60, 12, 16]`

> [STYLE] The bike shop counter at midday, seen from above and across. On the right, a phone lies flat on the wooden counter, its screen lit and the light in the frame: a photo of grey water with a white wake and spots of rain on the lens, nothing else, no words on the screen. The freckled hand of Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — rests beside it, her copper hair falling into the top right. A white hire helmet sits at the right edge. The bare counter, an amber lamp switched off, and a plain wall fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 31_ending_missing.webp — `end_missing`, the missing ending
**Object:** the phone in the open pannier on the counter · **hot** `[76, 58, 16, 18]`

> [STYLE] The bike shop counter at midday, grey window light and an amber work lamp on the counter. On the right, an open black pannier bag sits on the wooden counter with a phone lying inside it, screen dark, the work lamp shining straight down into the open bag onto the phone. Beside the bag, Shona Nicolson — tall, early thirties, very long straight copper-red hair worn loose, pale skin with freckles, wide grey-green eyes, a dark green work apron over a grey T-shirt, black jeans, a pencil behind one ear — holds out a few plain blank paper notes, no numerals or printing, three-quarter to us, listening. Behind her at the right edge, a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — is back on its stand. A bare painted wall fills the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark

### 32_ending_failed.webp — `end_failed`, the failed ending
**Object:** the bike on the rack of the bus at Fort Augustus · **hot** `[76, 56, 20, 22]`

> [STYLE] A grey afternoon at a bus stop by the canal at Fort Augustus, drizzle, wet tarmac. On the right, a plain single-decker bus with blank white destination blinds and no livery stands with a yellow hybrid hire bike — flat handlebars, a black rear pannier rack, silver mudguards, a black saddlebag under the saddle, a silver bell, no lettering on the frame — clamped on the rack at its front, the bus's amber headlamps lit against the drizzle and lighting the bike. Through the window behind the driver, small and from behind, Alex Marin: thirties, short dark curly hair, olive skin, a bright blue waterproof jacket, dark leggings, a plain white hire helmet, a small black backpack. The flat grey loch keeping itself to itself and a low sky fill the left of the frame. --ar 16:9 --no text, letters, writing, signage, logo, watermark
