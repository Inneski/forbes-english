# Brief for ChatGPT: seven painted worlds for the Forbes English front page

*Give this whole file to ChatGPT, with the reference pictures listed under
"Attach these". Ask for one world at a time.*

---

## What this is for

forbesenglish.com is an English-teaching site. Its front page is a live 3D
scene. A flat illustrated woman (bob haircut, dark round glasses, red lips,
arms folded on an open book) sits waist-deep in still water at the centre.
The site's sections are big titles on a ring around her. When a visitor
drags, she turns, and the whole world around her changes to suit that
section.

Right now each world's sky and distance are built from simple 3D shapes,
and they look basic. **I want you to paint the backdrop for each world as
one 360° panorama.** The site wraps it around the scene like the inside of
a globe, so it turns with her and the visitor can look all the way round.

You are painting **only the backdrop**: sky, horizon, distant scenery and
middle distance. The woman, the water she sits in and the titles are added
by the site on top. Do not paint them.

## Format (please follow exactly; the site depends on it)

- **Equirectangular 360° panorama, 2:1, at least 4096 × 2048 px, PNG.**
  The left and right edges must join seamlessly, because they meet behind
  the viewer.
- **The horizon sits exactly halfway down** (y = 1024 on a 2048-high
  image). The camera is at her eye level, a little above the water.
- **The bottom half is water and near ground, seen from just above it**:
  calm, plain, a little darker than the sky. No objects close to the
  bottom edge. The site draws its own water and reflections over the
  bottom quarter.
- **Keep the centre clear.** The middle of the image (x 1536–2560) is
  directly behind her head. Keep it to sky and low, distant horizon, with
  nothing taller than about 8% of the image height there. The big shapes
  of each world go to the left and right of centre, and behind the viewer
  (the left and right quarters of the image).
- **The top 30% is sky only.** The site's heading and menu sit over it, so
  keep it calm, with no busy detail or strong contrast there.
- **No text, letters, logos, signatures, people or animals** (except where
  a world below asks for birds). No frame, border or vignette.
- **One light direction per world**, given below, so the site's own 3D
  light matches it.

## House style (applies to every world)

- **Flat, screen-printed illustration**, in the manner of mid-century travel
  posters and modern vector editorial art: large clean shapes, limited
  colour, soft gradients in the sky, and a visible print grain or halftone
  texture over everything. Not photographic, not glossy 3D, not
  painterly-loose.
- **Calm, classy, uncluttered.** It is the background to text, so it must
  never fight the words over it.
- **Limited palette**: each world's colours are given below as hex codes.
  Stay within them, plus tints and shades of them.
- Depth comes from **layers fading into haze** (aerial perspective), not
  from detail.

## Attach these as references

From the repo, or ask Innes for them:

- The woman: `HOUSE STYLE/blackisler_cool_female_student_studying_at_home_with_books_No_f252909d-c97d-494b-b5b6-596be1e11502_2.png` (style and palette anchor)
- IELTS: `ielts-essay/hero.jpg` and `ielts-hub/route-*.jpg` (salmon clouds, duck-egg sky)
- Sherpa Tensing: `Sherpa Tensing/hero-route-map.jpg` and `Sherpa Tensing/cloud-1.webp`
- Block Camp: `BlockCamp/hub-hero.jpg`
- Grammar: `sailing-the-seas-of-grammar/hero.jpg`
- A screenshot of each world as it is now, from forbesenglish.com

---

## The seven worlds

Paint them in this order. Deliver each as the filename shown.

### 1. The Lesson Library — `library.png`

A vast circular **library rotunda** at night, as if she sits in a flooded
reading room. Walls of book-lined shelves in dark walnut curve all the way
round, rising in tiers with brass rails and ladders. Tall pillars stand
between the bays. A dome overhead has a glowing oculus. Warm lamplight
glows from brass lamps.
- **Light:** warm, from behind her and above (the oculus), with lamp pools on the shelves.
- **Palette:** `#0f0805` `#2e1a0e` `#4a2c18` `#6b4226` `#c9a14a` `#ffcf8a` `#f3ead8`
- **Centre clear:** a soft golden glow behind her, with shelves only to the sides.

### 2. IELTS Academic — `ielts.png`

An **old university at golden hour**, in the colours of the site's IELTS
pages. A long tree-lined avenue runs straight back from the viewer to a
sandstone college with a columned portico and a green-copper dome, small
in the distance at the centre. The trees either side are clipped
deciduous trees in light turquoise. Salmon cumulus clouds sit low on the
horizon under a duck-egg sky.
- **Light:** low sun from the left.
- **Palette:** `#8fb3bd` `#b8e6dc` `#86c4bd` `#e8826c` `#f6b49c` `#efe2cf` `#1c2228`
- **Centre:** the portico can sit at the centre, but **small** (under 8% of the height).

### 3. Sherpa Tensing — `sherpa.png`

**High Himalayan peaks**, in the style of the Sherpa Tensing route map: one
great snow-capped massif off to the right, ranges behind fading in layers
into a dusty blue sky, and soft cloud banks lying low across the
mid-ground. Slate rock, white snow, alpenglow salmon where the sun catches
the ridges.
- **Light:** high sun from the right.
- **Palette:** `#eef3f6` `#dfe8ea` `#b4c6d4` `#4a545c` `#26313a` `#f2b8a2` `#ffffff`

### 4. Block Camp — `blockcamp.png`

A **sunny voxel world**, like a tasteful Minecraft landscape: blocky hills
and terraces, blocky trees with square green canopies, sand blocks, a
distant blocky mountain, and a soft light-blue sky with blocky clouds. It
should be the one world that is openly cubic, but still clean and limited
in colour, not busy.
- **Light:** bright midday, from the upper left.
- **Palette:** `#7fb8ff` `#d4ecff` `#6aa84f` `#3d7a2a` `#d8c48a` `#6b4a2b` `#1d3550`

### 5. Role-Playing Games — `rpg.png`

A **moor at dusk, where stories begin**. A wide heather moor under a plum
and amber sky with the first stars, with low mist lying in the hollows. At
the far end of several roads, each story shows as a small lit thing on
the horizon:
- far left: a stone **railway viaduct** with a lit train crossing it
- right: a **lighthouse** on a dark headland, its beam sweeping
- far right: **frosted mountain peaks**
- low in the sky just right of centre: one **red star**
- **Light:** the last glow of sunset behind her, low and amber.
- **Palette:** `#2a1d3c` `#5e4a66` `#7a4f86` `#d9886a` `#ffb27a` `#e5443c` `#1c1620`

### 6. Grammar — `grammar.png`

A **sculpture plaza** in a calm, modern style: curved pale walls, arches,
tall slim columns, floating discs and ribbons of colour, under a clear
deep-blue sky. Faint grammar words (no real text) suggested only as
abstract shapes drifting in the sky.
- **Light:** strong sun from the upper right, crisp shadows.
- **Palette:** `#16263e` `#c8dcef` `#fff6e8` `#a8282a` `#24443d` `#e8b04a` `#f0ece4`

### 7. Level Check — `levelcheck.png`

**Open sea at evening.** Flat still water to the horizon, a long bank of
salmon cumulus all along the horizon, a dusty blue sky, and a white sun
high on the left. To her right a tall **tide gauge** post stands in the
water by a dark jetty, with plain bands and no numbers. The site adds the
A1–C2 markings itself. A small sailboat sits far off on the left horizon,
with a few gulls.
- **Light:** sun high on the left.
- **Palette:** `#7d9db0` `#c4d0d0` `#f29a84` `#f6b8a2` `#fbf6ee` `#1c2228` `#16232b`

---

## Delivering

Save each panorama with the filename above and send them to Innes. He
drops them in `incoming/home-worlds/` on his machine, and Claude wires them
into the page.

If a world does not work at 360°, a **wide 3:1 backdrop** (6144 × 2048)
is the fallback: same horizon at half height, same clear centre. Say which
you made.
