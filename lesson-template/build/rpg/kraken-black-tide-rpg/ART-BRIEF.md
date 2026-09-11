# KRAKEN: THE BLACK TIDE — art brief

Thirty-two plates. **WebP, 1536 × 1024 (3:2), each under 200 KB**, named in
play order, dropped into `block-camp/kraken-black-tide-rpg/`. The briefing
screen reuses `07_q6_shed.webp`; nothing else is reused.

`prep-plates.py` in this folder does the resize, the crop to 3:2 and the WebP
squeeze, and refuses a batch that is short a plate:

```bash
py lesson-template/build/rpg/kraken-black-tide-rpg/prep-plates.py incoming/kraken
```

## The style contract — paste this sentence verbatim into every prompt

> Painted digital illustration, west coast of Scotland, late August, low grey
> Atlantic light with one warm amber lamp in frame, slate-blue sea, wet black
> granite, kelp green and rust red, soft brush edges, no hard outlines,
> eye-level three-quarter camera.

This is `meta.style`. It does not vary between plates. Two plates that were
lit differently read as two games (CHATGPT-RPG-BRIEF §4a).

**No lettering anywhere.** No shop names, no boat names on hulls, no chart
labels, no signposts with writing, no open books, no newspapers. An image
model's English comes out garbled at 1536 px, and a broken word on a language
lesson reads as a mistake in the lesson. Every clue in this script was written
so that it names a physical object and never a written one.

**Dark, but never black.** Half of this game happens at dusk, at night or
inside a cave. Every one of those plates needs a light source in frame — the
harbour lamp, a storm lantern, a wheelhouse window, moonlight on wet rock —
because the glow marker takes its colour from the object underneath it and a
dark object on a dark ground produces a marker nobody can see.

## The character sheet — paste the line for anyone who appears

- **Isla Brodie:** mid-thirties, dark red hair tied back, navy police
  waterproof with the collar up, pale, no hat.
- **Dr. Maren Hoy:** late twenties, black curly hair, round wire glasses,
  mustard-yellow fleece under an orange flotation vest.
- **Angus Quinn:** seventies, white beard, weathered brown face, oiled green
  wool jumper, flat cap, a long pale scar on the right forearm.
- **Provost Baird:** sixties, heavy grey overcoat, thin grey hair, a red
  rosette on the lapel.
- **The Selkie:** a small wooden creel boat, dark green hull, white
  wheelhouse, tyres along the gunwale, four yellow marker barrels lashed to
  the rail.
- **The kraken:** never shown whole. A black arm, a rim of wet light along it,
  a pale mantle under green water, a wake with nothing in front of it. No eye
  before plate 22, and no full body on any plate.

## The composition contract

**The lit object sits right of centre on every plate — between x = 60% and
x = 95% — and the left half of the frame stays quiet:** open water, fog, a
wall, sky, an empty pier. The dark glass panel sits left all game and grows
to 54% of the frame the moment a learner turns a gloss language on, so it
reaches x = 56. Nothing that has to be seen may live left of that line.

Sherlock: The Blue Hour composed all twenty-two of its plates this way and is
the only export that has ever needed no hotspot adjustment at all.

## The plates

Each row is the file, the scene, the object the glow sits on, and the draft
hotspot box `[cx, cy, w, h]` in percent of the picture. **The boxes are a
first draft written from these prompts, not measurements.** Read every one off
a gridded contact sheet once the plates exist, then screenshot every scene
closed and fix what missed (`README.md` §3–4).

---

### 01_cover.webp — the cover
**Object:** the four yellow barrels on the Selkie's rail · **hot** `[74, 62, 20, 16]`

> [STYLE] Dawn at the mouth of a Scottish sea loch. A small wooden creel boat
> with a dark green hull and a white wheelhouse motors out past the harbour
> wall, right of centre, four yellow marker barrels lashed along its rail and
> catching the first light. Under the water behind it, a vast pale shape the
> length of three boats, barely readable, no detail. Empty grey water and low
> cloud fill the left of the frame. --ar 3:2

### 02_q1_drift.webp — `drift`, CHAPTER 1
**Object:** the yellow barrel in the stern · **hot** `[76, 66, 13, 14]`

> [STYLE] First light in a small Highland harbour. An empty wooden creel boat
> has drifted in against the pier on the right, mooring rope trailing in the
> water, nobody aboard. One yellow marker barrel lies on its side in the
> stern, chewed and split, lit by a lamp on the pier. Flat grey water and mist
> across the left half of the frame. --ar 3:2

### 03_q2_bell.webp — `bell`, CHAPTER 1
**Object:** the brass harbour bell · **hot** `[80, 38, 12, 18]`

> [STYLE] A brass bell on a wet stone post at the head of a Highland pier,
> right of frame, catching amber light from a harbour lamp. Isla Brodie
> [character line] stands below it with her hand on the rope, looking out.
> Villagers in oilskins are small and out of focus behind her. The left of the
> frame is open water and pale morning fog. --ar 3:2

### 04_q3_provost.webp — `provost`, CHAPTER 1
**Object:** the red regatta buoy · **hot** `[78, 60, 16, 20]`

> [STYLE] A Highland harbour on a regatta morning, bunting strung along the
> quay with no writing on it. Provost Baird [character line] stands on the
> right beside a big red mooring buoy on the stones, arms folded, facing Isla
> Brodie [character line] who is turned away from us. Sunlight through cloud
> on the buoy. Open harbour water fills the left. --ar 3:2

### 05_q4_hoy.webp — `hoy`, CHAPTER 1
**Object:** the sonar case · **hot** `[75, 63, 17, 17]`

> [STYLE] A single-track road above a Scottish sea loch. Dr. Maren Hoy
> [character line] has set a large silver instrument case on the tailgate of a
> mud-spattered estate car on the right, catching the light, its lid open on
> foam and coiled cable. She is looking down at the water. Loch, hills and low
> cloud fill the left of the frame. --ar 3:2

### 06_q5_jar.webp — `jar`, CHAPTER 1
**Object:** the glass jar · **hot** `[77, 55, 12, 18]`

> [STYLE] Inside a village hall kitchen at midday, cold light from a window.
> On a scrubbed wooden table on the right stands a wide glass jar of clear
> fluid holding a single black curved beak-ring the size of a fist, lit from
> behind so the glass glows. Dr. Maren Hoy [character line] leans over it in
> the background. The left of the frame is bare wall. --ar 3:2

### 07_q6_shed.webp — `shed`, CHAPTER 1 · also the rules briefing
**Object:** the yellow barrel on the wall · **hot** `[79, 45, 14, 22]`

> [STYLE] The inside of a fisherman's shed, warm bulb overhead, creels and
> coiled rope. Four yellow marker barrels hang on the right-hand wall in a
> row; the nearest one is bitten clean through, its edge splintered, lit by
> the bulb. Angus Quinn [character line] stands at the bench with his back
> half turned. A wide empty workbench fills the left of the frame. --ar 3:2

### 08_choice1_sound.webp — `sound`, ROUTE CHOICE 1
**Object:** the channel marker where the water splits · **hot** `[72, 52, 11, 26]`

> [STYLE] A Scottish sea loch seen from a boat's bow, the water dividing
> around a black rocky headland. A tall green iron channel marker stands right
> of centre on a skerry, catching the light. Beyond it to the right the water
> runs out to a low broken reef; to the far right, dark cave mouths under a
> cliff. The left of the frame is open water and sky. --ar 3:2

### 09_q7_reef1.webp — `reef1`, CHAPTER 2 · THE REEF
**Object:** the orange sonar float · **hot** `[79, 62, 13, 15]`

> [STYLE] The Selkie [boat line] working over a shallow reef in grey chop. An
> orange sonar float trails astern on the right, half out of the water,
> bright against the slate sea. Dr. Maren Hoy [character line] kneels at the
> stern paying out cable. Broken water over the reef fills the middle
> distance; the left is open sea and cloud. --ar 3:2

### 10_q8_reef2.webp — `reef2`, CHAPTER 2 · THE REEF
**Object:** the torn net · **hot** `[77, 58, 18, 20]`

> [STYLE] A creel net hauled over a boat's gunwale on the right, hanging in
> two pieces, the cut edge clean and bright with wet. Angus Quinn [character
> line] holds the severed end in both fists. Grey water streams off it. The
> left of the frame is empty sea and a low horizon. --ar 3:2

### 11_q9_reef3.webp — `reef3`, CHAPTER 2 · THE REEF
**Object:** the last seal on the skerry · **hot** `[78, 60, 12, 12]`

> [STYLE] A low black skerry at the edge of a reef, wet and empty, dozens of
> shallow dents in the weed where animals lay. One grey seal remains, right of
> centre, lit and looking straight out to sea. The left of the frame is flat
> grey water with nothing on it. --ar 3:2

### 12_q10_reef4.webp — `reef4`, CHAPTER 2 · THE REEF
**Object:** the scarred hull plate · **hot** `[76, 66, 20, 16]`

> [STYLE] Close on the dark green hull of a small wooden boat, seen from the
> water line, right of frame. Four long pale scores have been dragged through
> the paint in parallel, each the width of a wrist, raw wood showing bright.
> Spray and grey sea. The left of the frame is open water. --ar 3:2

### 13_q7_cave1.webp — `cave1`, CHAPTER 2 · THE SEA CAVES
**Object:** the storm lantern · **hot** `[75, 50, 11, 18]`

> [STYLE] The mouth of a sea cave under a black granite headland at low water,
> seen from an inflatable boat. A brass storm lantern hangs on a pole at the
> bow on the right, lit, throwing amber on the wet rock. Kelp hangs in torn
> ribbons above the entrance. The left of the frame is dark open water and
> pale sky. --ar 3:2

### 14_q8_cave2.webp — `cave2`, CHAPTER 2 · THE SEA CAVES
**Object:** the dinghy lamp · **hot** `[78, 57, 12, 14]`

> [STYLE] Inside a flooded sea cave, wet black walls. A small swamped dinghy
> lies wedged against the right-hand wall, half under water, its little deck
> lamp still burning yellow and reflecting off the surface. Isla Brodie
> [character line] stands knee-deep beside it. The left of the frame is dark
> water and the pale arch of the cave mouth behind. --ar 3:2

### 15_q9_cave3.webp — `cave3`, CHAPTER 2 · THE SEA CAVES
**Object:** the broken creel · **hot** `[77, 62, 17, 16]`

> [STYLE] A rock ledge inside a sea cave, lit warm by a lantern out of frame.
> On the right, a smashed wooden creel lies among heaped white shells and
> crab shell fragments, its slats snapped outward. Wet black rock above. The
> left of the frame is deep shadow and still water. --ar 3:2

### 16_q10_cave4.webp — `cave4`, CHAPTER 2 · THE SEA CAVES
**Object:** the wet tide line on the rock · **hot** `[74, 44, 20, 12]`

> [STYLE] Inside a sea cave with the tide making. On the right-hand wall a
> dark wet band runs level across the black granite well above head height,
> catching the lantern light, with dry rock and white barnacles above it.
> Water is climbing the wall. The left of the frame is rising dark water.
> --ar 3:2

### 17_q11_wreck1.webp — `wreck1`, CHAPTER 3 · THE WRECK
**Object:** the yellow barrel rising in the water · **hot** `[76, 58, 13, 15]`

> [STYLE] Looking down into clear green shallow water from a boat's rail. The
> rusted hull of a small trawler lies on its side on the sand below. A yellow
> marker barrel is rising out of the wreck on the right, trailing weed, bright
> under the surface. The left of the frame is open green water and the shadow
> of the boat. --ar 3:2

### 18_q12_wreck2.webp — `wreck2`, CHAPTER 3 · THE WRECK
**Object:** the old harpoon head · **hot** `[78, 61, 14, 13]`

> [STYLE] Angus Quinn [character line] sits on the engine box of a small boat,
> sleeve rolled back, a long pale scar down his right forearm. In his hands on
> the right he turns an old iron harpoon head, pitted and bent, catching the
> light from the wheelhouse. Isla Brodie [character line] listens in the
> background. The left of the frame is open sea through the doorway. --ar 3:2

### 19_q13_wreck3.webp — `wreck3`, CHAPTER 3 · THE WRECK
**Object:** the brass porthole · **hot** `[79, 55, 13, 19]`

> [STYLE] Underwater, close on the side of a rusted trawler hull lying on
> sand, right of frame. A heavy brass porthole is still in place, polished
> bright where the weed has been scoured away, its glass gone. Green light
> from above. The left of the frame is open water and drifting silt. --ar 3:2

### 20_choice2_decision.webp — `decision`, ROUTE CHOICE 2
**Object:** the Selkie's compass · **hot** `[74, 57, 12, 15]`

> [STYLE] Inside the wheelhouse of a small fishing boat at dusk, lit by the
> instrument glow. A big brass binnacle compass stands right of centre on the
> console, lit amber from within, its card unreadable. Through the windscreen
> beyond, the sea splits two ways around a dark island. Angus Quinn and Isla
> Brodie [character lines] stand either side. The left of the frame is the
> dark side window and open water. --ar 3:2

### 21_q14_corry1.webp — `corry1`, CHAPTER 4 · THE CORRY
**Object:** the rope on the capstan · **hot** `[77, 63, 15, 15]`

> [STYLE] The deck of a small fishing boat at the edge of a great whirlpool
> between two black islands, the water turning in slow smooth rings. On the
> right, a thick wet rope is wound three times round an iron capstan, drawn
> hard and shining. The left of the frame is the turning water, wide and
> empty. --ar 3:2

### 22_q15_corry2.webp — `corry2`, CHAPTER 4 · THE CORRY
**Object:** the arm over the gunwale · **hot** `[78, 55, 17, 24]`

> [STYLE] A single vast black tentacle has come up out of the sea and laid
> itself over the gunwale of a small wooden boat on the right, a rim of cold
> light along its wet length, the pale suckers catching the lamp. No body, no
> eye, no face. The rail bends under it. The left of the frame is churning
> dark water and spray. --ar 3:2

### 23_q16_corry3.webp — `corry3`, CHAPTER 4 · THE CORRY
**Object:** the engine lamp · **hot** `[76, 52, 11, 15]`

> [STYLE] Down in the cramped engine space of a small fishing boat, oily and
> close. A caged inspection lamp hangs on the right above a hot diesel engine,
> burning hard yellow, water sliding across the plates below it. Angus Quinn
> [character line] crouches with a spanner. The left of the frame is dark
> bulkhead. --ar 3:2

### 24_q14_night1.webp — `night1`, CHAPTER 4 · THE NIGHT WATCH
**Object:** the harbour lamp · **hot** `[79, 36, 11, 20]`

> [STYLE] A Highland harbour at night during a regatta, strings of small
> lights over the moored boats. On the right, a single iron lamp on the quay
> wall burns amber and lays a long line across the black water. Isla Brodie
> [character line] stands beneath it looking out. The left of the frame is
> dark water and the shapes of hills. --ar 3:2

### 25_q15_night2.webp — `night2`, CHAPTER 4 · THE NIGHT WATCH
**Object:** the last lit lamp on the water · **hot** `[75, 57, 10, 11]`

> [STYLE] Black night water seen from a harbour wall, a scatter of moored
> yachts gone completely dark. One masthead lamp on the right is still
> burning, small and white, doubled in the water below it. The left of the
> frame is empty black sea and sky with no horizon. --ar 3:2

### 26_q16_night3.webp — `night3`, CHAPTER 4 · THE NIGHT WATCH
**Object:** the strained mooring rope · **hot** `[77, 64, 16, 17]`

> [STYLE] Close on a floating pontoon at night under harbour light. On the
> right a mooring rope is drawn bar-tight from a bent steel cleat down into
> black water, the fibres lifting, the pontoon deck tilted and streaming. The
> left of the frame is the flat dark pontoon running away into the night.
> --ar 3:2

### 27_q17_barrels.webp — `barrels`, CHAPTER 5 · THE LAST RUN
**Object:** the yellow barrel going over the rail · **hot** `[76, 58, 15, 18]`

> [STYLE] A yellow marker barrel is halfway over the rail of a small fishing
> boat on the right, rope whipping off the deck behind it, spray coming up,
> bright against the grey sea. Dr. Maren Hoy [character line] has both arms
> braced against the transom. The left of the frame is heaving open water.
> --ar 3:2

### 28_q18_last.webp — `last`, CHAPTER 5 · THE LAST RUN
**Object:** the harpoon line running out · **hot** `[78, 60, 16, 20]`

> [STYLE] The stern of a small fishing boat, low and close to the water. A
> harpoon line is tearing off a wooden drum on the right, smoking with spray,
> running taut into the sea. Isla Brodie [character line] has one hand on the
> rail and is watching the line go. The left of the frame is white wake and
> grey sea. --ar 3:2

### 29_ending_master.webp — `master`
**Object:** the open harbour mouth · **hot** `[74, 55, 18, 18]`

> [STYLE] A Highland harbour in clear morning light, the water calm and green,
> small boats out beyond the wall. On the right, the harbour mouth stands open
> between two stone arms with sunlight on the water running through it.
> Children on the pier in the middle distance. The left of the frame is bright
> empty quay. --ar 3:2

### 30_ending_complete.webp — `complete`
**Object:** the green hull on the slip · **hot** `[77, 62, 18, 16]`

> [STYLE] Late afternoon on a Highland slipway. The broken dark green hull of
> a small fishing boat lies canted on the concrete on the right, planks
> stove, water draining out of it, the low sun on the wet timber. Angus Quinn
> [character line] sits wrapped in a blanket at the top of the slip. The left
> of the frame is the empty harbour. --ar 3:2

### 31_ending_missing.webp — `missing`
**Object:** the turning water of the Corry · **hot** `[75, 58, 20, 20]`

> [STYLE] The great whirlpool between two black islands at dusk, seen from
> above the water. On the right the surface is drawn down into a wide smooth
> turning ring, catching the last cold light, with nothing floating on it. The
> left of the frame is flat dark sea and low cloud. --ar 3:2

### 32_ending_failed.webp — `failed`
**Object:** the empty berth and its lamp · **hot** `[78, 52, 14, 22]`

> [STYLE] A Highland harbour before dawn in rain. On the right, one empty
> berth between two moored boats, its mooring lines hanging slack into black
> water, a single amber quay lamp above it in the wet air. Villagers stand
> small and still at the end of the pier. The left of the frame is dark
> water. --ar 3:2

---

## Before handing the plates over

1. Thirty-two files, thirty-two different pictures. Two filenames holding the
   same image has cost this repo a whole export.
2. Every plate WebP, 1536 × 1024, under 200 KB.
3. No lettering anywhere, on anything.
4. The lit object right of x = 60 on every plate, left half quiet.
5. Every dark plate has a light source in frame.
6. Quinn, Brodie, Hoy and the Selkie look the same in every plate they appear
   in. Check plate 07 against plate 30, and plate 03 against plate 28.
7. No plate shows the kraken whole, and none before plate 22 shows any part
   of it at all.
