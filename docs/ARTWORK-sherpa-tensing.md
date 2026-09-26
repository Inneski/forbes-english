# Artwork brief — Sherpa Tensing, the 25-deck tense course

The shopping list Innes asked for on 2026-09-22, **revised 2026-09-24**
after the colour redesign: **25 heroes and 7 background textures**, plus
one optional banner. Slot names are the filenames, `build_sherpa.py` reads
them by name, and the interim set already sits under those names in
`SherpaTensing/`, so a delivered file overwrites its interim twin and the
next build picks it up with no code change.

Read `ARTWORK-holding-the-line.md` for the general mechanics of a
commission (batches, `prep-artwork.py`, the four-up duplicates).

---

## What changed on 2026-09-24, and why it makes the pictures easier

The first version of this brief asked every hero to *be* its tense colour,
because the deck palette was derived from the hero. Midjourney ignored the
colour on almost every render, and the derived palettes were muddy. So the
colour no longer comes from the picture:

- **The colour comes from the route map.** `build_sherpa.py` reads each
  tense's colour and its ink straight from `sherpa-tensing-route-map.html`
  (`colour_key()`), so every deck wears exactly the map's colour whatever
  the picture looks like.
- **The cover card carries the colour, the picture does not have to.** A
  camp's cover is a white card with the tense name in its colour; a
  descent's is a card *of* the colour with the map's ink on it. The picture
  is shown untinted, as painted.
- **The card sits on the quieter half of the picture.** The builder
  measures which half is calmer (`quiet_side()`) and puts the card there.
  So the subject can sit on either side; what matters is that one half is
  quiet.
- **Descents are not night scenes any more.** Innes: "the hero doesn't have
  to be a negative thing." A descent's picture is a sister shot of its
  camp: the same place, another angle or another hour (the moonlit tarn,
  the moonlit campsite). Where no sister shot exists, the camp's own
  picture mirrored left to right works: the passive is the sentence turned
  around.
- **One texture set serves both faces.** Each deck dyes it in its own
  colour (multiplied in greyscale), so the seven textures appear pale on a
  camp and full-strength on a descent. The night set is gone.

---

## Two constraints that are not taste

1. **One half of every hero must be quiet.** The cover card covers about
   half the frame, on whichever side is calmer. Put the subject low and to
   one side, and keep the other half open sky, water, snow or haze. A
   subject dead centre gets covered either way.
2. **Keep to the zone.** The route map groups the camps: **foundation**
   (camps 1–5) is forest, meadow and river gravel; the **ridge** (6–9) is
   rock, scree and the snowline; the **summit push** (10–13) is ice, snow
   and thin air. A cover in the wrong zone looks fine alone and wrong in
   the sequence.

Deliver at 2000 × 1125, PNG or JPEG, no text, no logos, no faces.
`prep-artwork.py` resizes and converts; it refuses anything under 1400 wide.

---

## The colour key (for reference, not for the prompt)

The deck takes these from the route map. A hero that leans towards its
colour looks deliberate next to the card, but it is no longer required.

| camp | tense | colour | ink on it | zone |
|---|---|---|---|---|
| 1 | present continuous | `#F2ADBF` baby pink | dark | foundation |
| 2 | present simple | `#7A93B5` slate blue | dark | foundation |
| 3 | past simple | `#B08968` earth brown | dark | foundation |
| 4 | present perfect | `#36797E` deep teal | white | foundation |
| 5 | going to | `#99BA7D` soft sage | dark | foundation |
| 6 | past continuous | `#F1D779` yellow | dark | ridge |
| 7 | future simple | `#DB815F` muted terracotta | dark | ridge |
| 8 | present perfect continuous | `#97D0E5` baby-blue turquoise | dark | ridge |
| 9 | future continuous | `#E1AB5A` soft ochre | dark | ridge |
| 10 | past perfect | `#6E0B24` maroon | white | summit push |
| 11 | past perfect continuous | `#4B1A7A` violet | white | summit push |
| 12 | future perfect | `#454545` charcoal | white | summit push |
| 13 | future perfect continuous | `#B0B0B0` silver | dark | summit push |

Camps 1, 5, 7, 8 and 9 were recoloured on 2026-09-26 at Innes's request
(`lesson-template/recolour_family.py`), and camps 3, 5 and 7 now carry dark
ink; the stopped deck builder's `sherpa/content/*.json` palettes still hold
the old values. A descent takes its twin camp's colour (descent eight is
camp six's yellow). The clouds are off the key and keep their own page colours
(`#3F6577` slate for used to and the causative, `#6A5E8C` dusty violet for
be used to).

---

## The style stem

Every hero prompt is `<subject>, <stem>`.

```text
flat matte gouache mountain landscape, soft paper grain, muted natural tones, wide empty sky, the subject low in the frame and to one side, the other half quiet and open, no people, no faces, no text, no logos, no brand marks, --ar 16:9 --style raw
```

**Upscale before you send.** A base 16:9 render is under the 1400px floor.

---

## The shopping list

### The heroes — 25 files, `--ar 16:9`

The subject of each is the page's own metaphor, its evocative title (now
the line under the tense name on the cover). Paint the title.

As of 2026-09-24 Innes has renders for **all thirteen camps** and sister
shots for **descents one, two and three** (`incoming/sherpa/`, and the
first batch in `incoming/`). Still wanted: the other six descents (or
accept the mirrored camp picture) and the three clouds.

| slot | cover title | prompt subject |
|---|---|---|
| `hero-camp-01` | The ripple | a still tarn at a base camp at dawn, rings spreading from one dropped stone |
| `hero-camp-02` | The bedrock | the granite foot of the mountain rising straight out of a meadow, morning haze |
| `hero-camp-03` | The camp behind you | a struck campsite seen from the path above it: flattened grass, a ring of stones, the trail leading on |
| `hero-camp-04` | The rope still attached | one rope running from a lower camp up out of frame |
| `hero-camp-05` | The route already chosen | a marked trail with route flags winding ahead through meadow towards the ridge |
| `hero-camp-06` | The weather you were already in | a ridge path inside a sudden squall, one small tent holding |
| `hero-camp-07` | The weather you can't see yet | a ridge with a bank of weather building behind it, nothing decided |
| `hero-camp-08` | The tracks you leave behind | muddy boot tracks along a wet path beside glacier meltwater, the walker out of frame |
| `hero-camp-09` | This time tomorrow | a tent pitched on a ledge with tomorrow's route visible beyond it, late light |
| `hero-camp-10` | The camp you had already struck | an empty ledge where a camp stood, pole marks still in the snow, dusk |
| `hero-camp-11` | The hours before the hut | a mountain hut with a long trail of footprints leading to it across twilight snow |
| `hero-camp-12` | Done before you get there | a summit cairn seen from below, already built, against a pale sky |
| `hero-camp-13` | The hours you'll have put in | the long final snowfield to the summit, one line of steps up it |
| `hero-descent-01` | Being done right now | camp one's tarn from another angle, the rings still spreading (a moon is welcome) |
| `hero-descent-02` | The way things are done | camp two's granite foot, a later hour |
| `hero-descent-03` | When nobody did it | camp three's struck campsite, the trail under a low moon |
| `hero-descent-04` | It has been done | camp four's rope, seen from above |
| `hero-descent-07` | It will be done | camp seven's ridge with the weather now arrived |
| `hero-descent-08` | It was being done | camp six's squall, light inside the one tent |
| `hero-descent-09` | It is going to be done | camp five's flagged trail from further along it |
| `hero-descent-10` | It had been done | camp ten's empty ledge, the pole marks in the snow |
| `hero-descent-12` | It will have been done | camp twelve's cairn under an evening sky |
| `hero-cloud-used-to` | The thing you don't do any more | a valley seen from above through a gap in cloud, a small old village far below |
| `hero-cloud-be-used-to` | The thing that stopped being strange | a climber's boots at rest on a rock above a sea of cloud, thin air, ease |
| `hero-cloud-causative` | Somebody else did it, and you arranged it | a full moon over the mountain, a laden porter's silhouette on the trail far below |

Three notes:

- **A descent is a sister shot of its camp,** so a learner who has done
  camp three recognises the place on the way down. Nine of them, because
  four tenses have no passive worth teaching (the route map says why). If
  one never arrives, mirror the camp's picture left to right.
- **`hero-cloud-causative` gets the moon.** The page calls the causative
  "the moon", not a cloud.
- **No faces.** Boots, a silhouette far away, a porter from behind.

The route map hub is not rebuilt and keeps its interactive SVG mountains.
An optional 26th file, `hero-route-map`, would give it and its library
card a banner: *the whole mountain, one face in daylight and the other at
dusk, both routes faintly visible.*

**Filled 2026-09-25**, with one of Innes's own renders from `incoming/sherpa/`
(the long final snowfield, a stair of steps up the ridge to the summit): it
is the hub's hero at `Sherpa Tensing/hero-route-map.jpg`, 1200px, not in
`SherpaTensing/`. A commissioned replacement goes to that path, or the
page's `<img src>` moves with it. The library card is still the SVG render.

### The textures — 7 files, `--ar 16:9`

One per **section role**, one set for both faces. They sit under text
boxes on every inside slide, dyed in the deck's colour, so they are
material, not scenery: no horizon, no subject, no focal point, even light,
low contrast, and **light**: the builder multiplies them onto the colour,
so a dark texture turns a descent muddy and gets measured into more opaque
boxes.

```text
seamless flat texture of <material>, soft even light, no subject, no horizon, no focal point, low contrast, fine natural grain, pale off-white and light grey, no text, --ar 16:9 --style raw
```

| slot | where it shows | material |
|---|---|---|
| `bg-day-briefing` | the briefing slide and "When to use it" | a topographic map sheet, contour lines on paper |
| `bg-day-building` | "How it's built", the conjugation charts | dry-stone wall, blocks stacked |
| `bg-day-fork` | "The fork in the path" | a trail junction from above: two worn paths dividing through scree |
| `bg-day-markers` | "Signal words" | a field of small cairn stones |
| `bg-day-stage` | the interactive diagram slides | squared expedition notebook paper |
| `bg-day-climb` | the fourteen practice questions and the results | scree and packed snow underfoot |
| `bg-day-view` | the activation stage | high cloud from above, the calm one |

The climb texture is under fourteen slides in a row. It is the one to get
quietest.

---

## Dropping a set in

Move the batch out of `incoming/` into a folder of its own, numbered so the
sorted order matches `--names`, then:

```bash
py tools/prep-artwork.py <batch-folder> --into SherpaTensing --dry-run
py tools/prep-artwork.py <batch-folder> --into SherpaTensing --names hero-camp-01,hero-camp-02,…
py lesson-template/build/build_sherpa.py
for f in sherpa-tensing-*.html; do node lesson-template/check-lesson.js "$f"; done
py tools/seo.py
```

The build stops if any contrast row fails, and it measures the textures'
darkest tile, so a texture that is too dark shows up as more opaque boxes
(a `--plate` line in the palette block) rather than as unreadable text.

**Look at every cover once it is built.** The builder picks the card's
side by measuring the picture, and it can be fooled: a busy sky on the
quiet side of the subject. If a card sits on the subject, crop or mirror
the picture rather than moving the card by hand.

Then the library cards: `LESSON_IMAGES` in `library.html` still points the
26 rows at the old diagram renders in `SherpaCamps/`. Cut a 1200 × 512
card from each new hero and repoint the rows.
