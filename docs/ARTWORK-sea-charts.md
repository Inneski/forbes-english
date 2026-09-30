# Artwork brief: three more sea charts for Sailing the Seas of Grammar

Innes, 2026-09-30: *"make extra maps with nautical theme like gerundia
infinitivia but for countable and uncountable nouns although perhaps that can
also be two pictures of rooms full of one or the other with a interim space
where they share stuff, also possible for regular and irregular verbs"*

This brief covers three charts: the nouns as a map, the nouns as your "two
rooms" idea, and the verbs. All three are drawn and checked. What they need
now is the ChatGPT repaint.

## How the Gerundia chart was made, and why these follow it

1. `sailing_map.py` drew a flat coded chart (it is still in history: `git show
   f4dbfa0e^:sailing-the-seas-of-grammar/hero.jpg`).
2. ChatGPT repainted it as the illustrated chart, with every label. That
   became `sailing-the-seas-of-grammar/hero.jpg`.
3. ChatGPT then made the same picture with no words, only the harbour dots.
   That became `chart-clean.jpg`, and the page's clickable layer sits on top
   of it. The label coordinates were calibrated by blob-detecting the painted
   dots (`eb491249`).

The three layouts below are step 1. They are built by
`lesson-template/build/sea_charts.py`, and they come out in the same
1000×660 space as the first chart, so steps 2 and 3 work the same way. The
builder also measures the layout in headless Chromium. It fails if a harbour
name spills off its coast, a sea caption lands on a beach, or two labels
touch, so the painter is copying a layout that is known to be clean. That
check was run against deliberately broken copies and caught all three kinds
of fault.

## The three layouts: `docs/sea-charts/`

### 1. `countable-chart.png`: Countania and Uncountania

![countable chart](sea-charts/countable-chart.png)

| On the chart | What it teaches |
|---|---|
| **Countania** (brick, west) | *a / an · many · a few · -s* |
| **Uncountania** (wheat, east) | *much · a little · no a / an · no -s* |
| **Paired harbours** | Each uncountable harbour faces its countable partner at the same latitude, with the same surname: *Furniture Crag ↔ Chair Crag, Information Point ↔ Fact Point, Advice Head ↔ Tip Head, Luggage Sands ↔ Suitcase Sands*. Twelve pairs: work/job, information/fact, advice/tip, luggage/suitcase, furniture/chair, travel/trip, money/coin, music/song, equipment/tool, weather/storm, homework/task, progress/step. The traps are on the east side. The way out of each trap is directly across the water. |
| **Double Isle** (lilac) | Both shores, two meanings: coffee, chicken, paper, room, glass, hair, time. Lilac, like Twofold Isle, so "the lilac island is both" holds across the series. |
| **The False Cape** | A spur of Uncountania flying a flag marked **-S**. *News, maths and physics* look plural but are singular: *the news is*. It is the same device as the first chart's False Cape (a flag that lies). |
| **The piece-of ferry** | The one way across, west only: *a piece of advice · a bottle of water · a slice of bread*. |
| **The Shallows** | Quantifiers that work on either shore: *some, any, a lot of, plenty of, no, enough, more, most*. |
| **Compass** | *◀ HOW MANY? · HOW MUCH? ▶* |

### 2. `countable-hold.png`: the two rooms, as a ship's hold

![ship's hold](sea-charts/countable-hold.png)

Your two-rooms idea, done as a ship's hold to keep the nautical theme. It is
a wooden ship cut open lengthways:

- **The counting hold** (HOW MANY?): chairs, suitcases, coins, loaves, tools,
  letters. Each one sits apart with a numbered tag: *a chair · 3 chairs*.
- **The bulk hold** (HOW MUCH?): *the same cargo in the same rows*, piled into
  heaps with one word on each heap: FURNITURE, LUGGAGE, MONEY, BREAD,
  EQUIPMENT, MAIL.
- **The galley**, the space they share (BOTH): one of each thing beside the
  stuff it is made of. *A coffee* (a cup) sits beside *coffee* (a sack of
  beans), *a chicken* (a hen) beside *chicken* (the meat), *a paper* beside
  *paper*, *a glass* beside *glass*, *a cake* beside *cake*, *a hair* beside
  *hair*.
- Caption: **THE SAME CARGO · A DIFFERENT WORD**.

The hold explains *why* furniture is uncountable: the word names the heap,
not the pieces. The map can't show that. What the map gives you is the list
of nouns and the traps.

### 3. `verbs-chart.png`: Regularia and the irregular archipelago

![verbs chart](sea-charts/verbs-chart.png)

| On the chart | What it teaches |
|---|---|
| **Regularia** (green, west) | One continent with one rule, *verb + -ed*. Its coast is deliberately smoother than any other on the chart. Dotted county lines split it into three provinces by sound: **-ED SAYS /t/** (Stop Harbour, Walk Ridge, Watch Head, Cook Cove), **/d/** (Play Bay, Study Sands, Travel Tarn, Call Crag), **/ɪd/** (Start Point, Wait Moor, Visit Fell, Land's End). The spelling rules are in the names too: *stopped, studied, travelled, played*. |
| **The archipelago** ("Irregularia: no one rule · but families") | There's no single rule, but there are families, and each family is an island. **Bell Island** *ring · rang · rung* (sing, drink, swim, begin). **Ought Island** *buy · bought* (bring, think, catch, teach). **Windward Isle** *blow · blew · blown* (grow, know, throw, fly). **Keep Island** *keep · kept*, the -t endings (sleep, feel, leave, build). **Broken Reef** *break · broke · broken* (speak, steal, wake, choose). |
| **The Still Rocks** | *cut · put · hit · let · cost*: no change at all. |
| **The Lone Stacks** | *go · be · do · see*: no family at all. |
| **Forked Isle** (lilac) | One verb, two meanings, two past forms: *lie (lied / lay), hang (hanged / hung), shine (shined / shone)*. |
| **Currents, both running west** | **NEW VERBS SAIL WEST**: *texted · emailed · googled* (every new verb is regular). **SOME OLD ONES ARE DRIFTING WEST**, into **the Shallows**: *learnt / learned, dreamt / dreamed, burnt / burned, spelt / spelled*. |
| **Compass** | *◀ WALKED · WENT ▶* |

The *did* rule (*Did you go? I didn't go*, never *didn't went*) is not on the
chart. It is a rule about sentences, not a place, so it belongs in the
lesson.

## The ChatGPT recipe: two turns per chart

Attach **two images** to each first turn:

1. `sailing-the-seas-of-grammar/hero.jpg`, the finished Gerundia chart, as
   the style reference.
2. The layout from `docs/sea-charts/`.

### Turn 1: the labelled chart (the two maps)

```text
Image 1 is a finished illustrated sea chart. Image 2 is a flat layout for a new chart in the same series. Paint image 2 in exactly the style of image 1: an antique hand-painted sea chart on parchment with a thin ruled border, watercolour terrain with fine ink hatching, cliffs along the coasts, forests, hills and lakes, a compass rose, a sailing ship and small waves on a pale blue sea. Landscape, 3:2.

Keep the layout of image 2 exactly: the same coastlines, islands, sandbank, dashed currents and flag in the same places, and every harbour dot exactly where it is. Copy every word in image 2 exactly as it is spelled, in the same place, with serif capitals for the titles and plain lettering for the place names, as in image 1. Add no other words. British spelling.

<CHART NOTES>
```

**`<CHART NOTES>` for `countable-chart.png`:**

```text
Countania, the brick-red western shore, is a land of things you can count: orchards planted in rows, separate farmhouses, stacked crates and barrels on its quays, boats moored one by one. Uncountania, the golden eastern shore, is a land of stuff you can only measure: wheat fields, sand dunes, marshes, lakes and rivers, a mill with grain pouring from it. Double Isle is lilac like the island in image 1, with a small lighthouse. The False Cape is a golden spur of Uncountania flying a red pennant marked -S. A small ferry boat sits on the northern dashed current, heading west.
```

**`<CHART NOTES>` for `verbs-chart.png`:**

```text
Regularia, the green western continent, is orderly: a neat grid of fields, straight roads and hedgerows, identical villages, a smooth coastline, with two faint dotted county lines dividing it into three provinces. The eastern sea is an archipelago, every island a different colour and character: Bell Island (orange) with a bell tower, Ought Island (gold), Windward Isle (blue-grey) windswept with bent trees and a windmill, Keep Island (rose) with a castle keep, Broken Reef (sand) with jagged broken rocks and a small wreck. The Still Rocks are four low flat rocks; the Lone Stacks are four tall sea stacks standing apart. Forked Isle is lilac like the island in image 1, with a river that splits in two.
```

### Turn 1 for the hold, `countable-hold.png`

```text
Image 1 is a finished illustrated sea chart. Image 2 is a flat layout for a cutaway picture in the same series. Paint image 2 in exactly the style of image 1 (parchment, watercolour, fine ink hatching) as a cutaway of a wooden sailing ship's hull, opened lengthways to show three compartments, the sea behind it and three masts with pennants. Landscape, 3:2.

Keep the layout of image 2 exactly, and copy every word in image 2 exactly as it is spelled, in the same place. Add no other words.

Left, the counting hold: in each row the real objects are set out one by one, each with a small numbered tag: 3 wooden chairs, 4 suitcases, 6 coins, 4 loaves, 5 tools, 6 letters.
Right, the bulk hold: the same things in the same rows, but heaped up with no tags: a jumbled heap of furniture, a pile of luggage, a heap of loose coins and banknotes, a heap of bread, a pile of tools and equipment, a sack spilling mail.
Middle, the galley: in each row one single thing with a tag beside the stuff it is made of: one cup of coffee beside a sack of coffee beans; a live hen beside cooked chicken meat on a plate; a newspaper beside a ream of blank paper; a drinking glass beside a pane of glass; a whole cake beside a slice on a plate; a single hair on a comb beside a long braid of hair.
```

### Turn 2: the clean copy (all three)

In the same conversation:

```text
Now the same picture with every word, letter and number removed: no names, no titles, no captions, blank pennants and blank tags. Keep every harbour dot exactly where it is. Change nothing else.
```

If a label comes back misspelt in turn 1, ask for that one word to be fixed
before you ask for turn 2. The clean copy inherits whatever turn 1 got
wrong.

## Where the files go

Drop them in **`incoming/sea-charts/`** under these names (PNG or JPG is
fine):

| file | what it is |
|---|---|
| `countable-chart` / `countable-chart-clean` | the map, labelled and clean |
| `countable-hold` / `countable-hold-clean` | the hold, labelled and clean |
| `verbs-chart` / `verbs-chart-clean` | the verbs map, labelled and clean |

## What happens after that (for the session that picks this up)

1. `tools/prep-artwork.py` on each file. The two charts become the heroes of
   two new pages in the Sailing family. Suggested slugs:
   `sailing-countable-uncountable.html` and `sailing-regular-irregular.html`.
2. Blob-detect the painted dots on each `-clean` file and move the place
   coordinates in `sea_charts.py` to match, as `eb491249` did for
   `sailing_map.py`. Then the clickable label layer lands on the painted dots.
3. Write the builders on the Sailing machinery (`build_sailing.py` is the
   model; do not edit it while another session holds it). Give each page its
   own clickable chart, rule cards and checkpoints, with EN + DE + ES as the
   minimum. Nouns level A2–B1. Verbs level A2–B1, with Forked Isle and the
   Shallows as the stretch.
4. `extract-palette.py` on each painted hero, then `build_hubs.py`, `seo.py`
   and the catalogue rows.

**Still open for Innes:** for countable and uncountable, which picture leads:
the map, the hold, or both? My recommendation is both in one lesson. The hold
opens the lesson because it gives the idea (same cargo, different word), and
the map is the clickable hero because it holds the list of nouns and the
traps.
