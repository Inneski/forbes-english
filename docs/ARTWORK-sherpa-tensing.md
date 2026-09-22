# Artwork brief — Sherpa Tensing, the 26-deck tense course

The shopping list Innes asked for on 2026-09-22: **heroes and background
textures** for the whole family. Forty files. Slot names are the filenames,
`build_sherpa.py` reads them by name, and the interim set that ships today
already sits under those names in `SherpaTensing/` — so a delivered file
overwrites its interim twin and the next build picks it up with no code
change. That is the same arrangement Holding the Line was delivered under.

Read `ARTWORK-holding-the-line.md` for the general mechanics of a
commission (batches, `prep-artwork.py`, the four-up duplicates). This brief
differs from the two editorial ones in every number, because these decks are
built on the **default** style, not the editorial one: the hero is washed
across every slide at 0.72 opacity and the text sits on plates on top of it
(HOUSE-STYLE §5), and the palette is **derived from the hero** by
`extract-palette.py` (§4). Both facts shape what to ask for.

---

## What is shipped now, and why it needs replacing

| | shipped now (interim) | what the deck wants |
|---|---|---|
| hero, 26 of them | the camp's own timeline diagram over a procedural contour field, in the camp's colour | a mountain scene, one per page, in the camp's colour |
| textures, 14 of them | procedural: contours, brick, hatch, stipple, graph paper, scree, cloud | photographed or painted material: canvas, rope, rock, snow, cloud |
| ratio | 16:9, 1600 × 900 | 16:9, **2000 × 1125** |
| library cards | still the old diagram renders in `SherpaCamps/` | cut from the new heroes |

The interim set is honest — the palette tool reads the tense colour out of
each diagram, so every deck already wears its route-map colour — but it is
a diagram, not a picture. The cover of a course whose entire metaphor is a
mountain currently shows no mountain.

---

## Three constraints that are not taste

1. **The hero drives the palette, so the hero must be the tense's colour.**
   `extract-palette.py` picks the accent as "the most colourful thing with
   enough presence" in the image. The route map has taught learners for
   months that past simple is brown, present perfect teal, future simple
   orange (§5a). Each hero therefore has to carry its tense colour as the
   dominant hue — not as a detail, as the sky or the ground. Get that wrong
   and camp three ships in the wrong colour with nobody having chosen it.

2. **The centre of the cover is covered.** This template's cover lockup —
   logo, a 62px title, the subtitle, three chips and the Begin button — is
   **centred**, under a radial scrim. Put the subject low, or to one side,
   and keep a quiet field through the middle. The hero also repeats behind
   every interior slide, under text plates, so a busy hero costs legibility
   on twenty-six slides, not one.

3. **Camps and clouds are light decks; descents are dark decks.** The
   thirteen camps and three clouds are built with `--light`: they want a
   bright, airy picture (day, open sky, pale ground). The nine descents are
   built dark: the same camp **by night**, moonlit, the tense colour glowing
   out of a near-black field. The route map already says it: *"the same
   tenses, lit from the other side."*

Deliver at 2000 × 1125, JPEG or PNG, no text, no logos, no faces.
`prep-artwork.py` resizes and converts; it refuses anything under 1400 wide.

---

## The palette — what each hero must be built around

These are the route map's colours, the ones the camp pages were themed from.
Name the colour in the prompt; the tool will find it.

| camp | tense | colour | zone |
|---|---|---|---|
| 1 | present continuous | `#E66085` rose pink | foundation |
| 2 | present simple | `#7A93B5` slate blue | foundation |
| 3 | past simple | `#B08968` earth brown | foundation |
| 4 | present perfect | `#36797E` deep teal | foundation |
| 5 | going to | `#70A43A` moss green | foundation |
| 6 | past continuous | `#F1D779` straw yellow | ridge |
| 7 | future simple | `#F0723F` sunset orange | ridge |
| 8 | present perfect continuous | `#46B0AB` glacier turquoise | ridge |
| 9 | future continuous | `#F0A500` amber | ridge |
| 10 | past perfect | `#6E0B24` maroon | summit push |
| 11 | past perfect continuous | `#4B1A7A` violet | summit push |
| 12 | future perfect | `#454545` charcoal | summit push |
| 13 | future perfect continuous | `#B0B0B0` pale grey | summit push |
| clouds | used to · be used to · causative | `#4A6E80` slate, `#7FA6B6` pale slate | off the route |

The three zones are the route map's own groupings and they give the climb
its scenery: **foundation** camps sit in forest, meadow and river gravel;
the **ridge** is rock, scree and the snowline; the **summit push** is ice,
snow and thin air. A hero that puts camp two in snow and camp twelve in a
meadow will look fine on its own and wrong in the sequence.

---

## The style stem

Every hero prompt is `<subject>, <stem>`.

```text
flat matte gouache mountain landscape, soft grain, muted natural tones with <colour> as the dominant hue of the sky and ground, wide empty sky, the subject low in the frame and off centre, quiet uncluttered middle, no people, no faces, no text, no logos, no brand marks, --ar 16:9 --style raw
```

For a descent, swap the opening to `flat matte gouache mountain landscape at
night, moonlit,` and add `near-black field with <colour> glowing in the
snow and the tents`. Keep everything else.

Two things in that stem are load-bearing:

- **`<colour> as the dominant hue of the sky and ground`** is constraint 1
  above, said in a way the model acts on. A rose-pink *tent* on a blue
  mountain gives you a blue deck.
- **`quiet uncluttered middle`** is constraint 2. The two batches for the
  editorial decks both came back with the subject dead centre; the cover
  lockup then sat on top of it.

**Upscale before you send.** A base 16:9 render is under the 1400px floor.

---

## The shopping list

### The heroes — 26 files, `--ar 16:9`

The subject of each is the camp's own metaphor: the page's title, which is
now the cover title, is in the second column. Paint the title.

| slot | cover title | prompt subject |
|---|---|---|
| `hero-camp-01` | The ripple | a still tarn at a base camp at dawn, rings spreading from one dropped stone, rose-pink light on the water |
| `hero-camp-02` | The bedrock | the granite foot of the mountain rising straight out of a meadow, slate-blue stone, morning haze |
| `hero-camp-03` | The camp behind you | a struck campsite seen from the path above it: flattened grass, a ring of stones, the trail leading on, earth-brown ground |
| `hero-camp-04` | The rope still attached | one rope running from a lower camp up out of frame to the climber, deep-teal shadowed slope |
| `hero-camp-05` | The route already chosen | a marked trail with route flags winding ahead through moss-green meadow towards the ridge |
| `hero-camp-06` | The weather you were already in | a ridge path inside a sudden squall, straw-yellow storm light, one small tent holding |
| `hero-camp-07` | The weather you can't see yet | a ridge with a bank of weather building behind it, sunset-orange sky, nothing decided |
| `hero-camp-08` | The tracks you leave behind | muddy boot tracks along a wet path beside glacier-turquoise meltwater, the walker just out of frame |
| `hero-camp-09` | This time tomorrow | a tent pitched on a ledge with tomorrow's route visible beyond it, amber late light |
| `hero-camp-10` | The camp you had already struck | an empty ledge where a camp stood, pole marks still in the snow, maroon dusk |
| `hero-camp-11` | The hours before the hut | a mountain hut with a long trail of footprints leading to it across violet twilight snow |
| `hero-camp-12` | Done before you get there | a summit cairn seen from below, already built, charcoal rock against a pale sky |
| `hero-camp-13` | The hours you'll have put in | the long final snowfield to the summit, one line of steps up it, pale-grey light |
| `hero-descent-01` | Being done right now | camp one's tarn by night, the rings still spreading, rose-pink moonlight |
| `hero-descent-02` | The way things are done | camp two's granite foot by night, slate-blue moonlit stone |
| `hero-descent-03` | When nobody did it | camp three's struck campsite by night, the trail lit by a low moon, earth brown |
| `hero-descent-04` | It has been done | camp four's rope by night, teal glow along its length |
| `hero-descent-07` | It will be done | camp seven's ridge by night with the weather now arrived, orange lightning in cloud |
| `hero-descent-08` | It was being done | camp six's squall by night, straw-yellow light inside the one tent |
| `hero-descent-09` | It is going to be done | camp five's flagged trail by night, moss-green flags catching torchlight |
| `hero-descent-10` | It had been done | camp ten's empty ledge by night, maroon sky, the pole marks in moonlit snow |
| `hero-descent-12` | It will have been done | camp twelve's cairn by night, charcoal against stars |
| `hero-cloud-used-to` | The thing you don't do any more | a valley seen from above through a gap in cloud, a village where a village used to be, slate and pale slate |
| `hero-cloud-be-used-to` | The thing that stopped being strange | a climber's boots at rest on a rock above a sea of cloud, thin air, ease, pale slate |
| `hero-cloud-causative` | Somebody else did it, and you arranged it | a full moon over the mountain, a laden porter's silhouette on the trail far below, slate and pale slate |

Four notes:

- **Descents are the camp by night.** Same composition as the day file, or
  near it, so a learner who has done camp three sees the same ledge on the
  other face. Nine of them, because four tenses have no passive worth
  teaching (the route map says why).
- **`hero-cloud-causative` gets the moon.** The page calls the causative
  "the moon", not a cloud, and its diagram is drawn as three boxes on a
  line; the moon is the one figurative element the family's own copy asks
  for.
- **No faces.** Boots, a silhouette far away, a porter from behind. This is
  a grammar course; a generated face on a cover is a liability and adds
  nothing.
- **The route map hub is not rebuilt** and keeps its two interactive SVG
  mountains. If a banner hero is wanted for it and for the library card,
  `hero-route-map`: *the whole mountain, the sunlit face on the left and
  the night face on the right, both routes faintly visible* — an optional
  27th file.

### The textures — 14 files, `--ar 16:9`

One per **section role**, in a day set (camps, clouds) and a night set
(descents). They sit under text plates on every interior slide, so they
are material, not scenery: no horizon, no subject, no focal point, even
light, low contrast. The interim set is procedural; these are the real
thing.

```text
seamless flat texture of <material>, soft even light, no subject, no horizon, no focal point, low contrast, fine natural grain, <day: warm off-white and pale stone / night: near-black slate with pale cool marks>, no text, --ar 16:9 --style raw
```

| slot (day / night) | where it shows | material |
|---|---|---|
| `bg-day-briefing` / `bg-night-briefing` | the briefing slide and "When to use it" | a topographic map sheet, contour lines on paper |
| `bg-day-building` / `bg-night-building` | "How it's built", the conjugation charts | dry-stone wall, blocks stacked |
| `bg-day-fork` / `bg-night-fork` | "The fork in the path" | a trail junction from above: two worn paths dividing through scree |
| `bg-day-markers` / `bg-night-markers` | "Signal words" | a field of small cairn stones |
| `bg-day-stage` / `bg-night-stage` | the interactive diagram slides | squared expedition notebook paper |
| `bg-day-climb` / `bg-night-climb` | the fourteen practice questions and the results | scree and packed snow underfoot |
| `bg-day-view` / `bg-night-view` | the activation stage | high cloud from above, the calm one |

Two notes:

- **The climb texture is under fourteen slides in a row.** It is the one to
  get quietest. The interim scree had to be turned down twice before the
  question stems read cleanly.
- **Optional upgrade, +14 files:** a texture set per zone (foundation ·
  ridge · summit push) instead of one day set — meadow-and-gravel for camps
  one to five, rock-and-snowline for six to nine, ice for ten to thirteen —
  makes the climb feel like a climb slide by slide. Name them
  `bg-foundation-<role>`, `bg-ridge-<role>`, `bg-summit-<role>`; the
  builder's `ROLE` map gains a zone lookup. Not needed for the decks to be
  right; needed for them to be beautiful.

---

## Dropping a set in

Move the batch out of `incoming/` into a folder of its own, numbered so the
sorted order matches `--names`, then:

```bash
py tools\prep-artwork.py <batch-folder> --into SherpaTensing --dry-run
py tools\prep-artwork.py <batch-folder> --into SherpaTensing --names hero-camp-01,hero-camp-02,…
py lesson-template\build\build_sherpa.py            # derives every palette again from the new heroes
for f in sherpa-tensing-*.html; node lesson-template\check-lesson.js $f   # every deck must exit clean
py tools\seo.py
```

Then the library cards: `LESSON_IMAGES` in `library.html` still points the
26 rows at the old diagram renders in `SherpaCamps/`. Cut a 1200 × 512
card from each new hero (fit by height, pad from the hero's own field
colour if the subject sits low — see the Watts card note in `HANDOFF.md`)
and repoint the rows.

`build_sherpa.py` re-derives the palette from whatever `hero-<slug>.jpg`
is on disk and stops the build if any contrast row fails, so a hero that
does not carry its tense colour is caught at build time, not on the live
site. Camps and clouds are derived `--light`; a dark delivery for a camp
will fail the "text on void" row — that is the tool refusing a night
picture for a day deck, not a bug.
