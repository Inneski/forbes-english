# Artwork: three more sea charts for Sailing the Seas of Grammar

Innes, 2026-09-30: *"make extra maps with nautical theme like gerundia
infinitivia but for countable and uncountable nouns although perhaps that can
also be two pictures of rooms full of one or the other with a interim space
where they share stuff, also possible for regular and irregular verbs"*.
Then: *"both in one lesson"*, *"the rooms can be in a ship"*, and *"I will
make the images on request using midjourney … I planned to upgrade whatever
you made anyway but I was specially talking about the countable noun
images"*.

So the work is split:

- **The two maps are painted in code** by `lesson-template/build/sea_charts.py`
  and `sea_paint.py`. They have parchment, a ruled border with a degree band,
  water lines along every coast, hatched cliffs, terrain and a compass rose.
  They are finished art and can be upgraded later.
- **The countable-noun pictures, the ship's rooms, are Innes's**, made in
  Midjourney from the requests below. The coded hold stands in until they
  arrive.

Everything is written by a separate label layer, never by the painting. That
keeps the words translatable and lets the page switch between place names
and bare nouns. It also means any upgrade that keeps the coastlines keeps
every label.

## The builder, and its check

```bash
py lesson-template/build/sea_charts.py
```

This writes each chart to `docs/sea-charts/` as `<name>.svg` / `.png`
(labelled) and `<name>-plain.svg` / `.png` (paint only). It exits non-zero if
any of these happen:

- a harbour name leaves its coast, or a caption on the hold leaves the hull
- a caption meant for open water touches a beach
- two labels touch
- anything runs under the ruled border

The measurements are taken in headless Chromium against the real glyphs and
coastlines. The check was run against deliberately broken copies and failed
on each of them.

The terrain is part of the grammar:

- **Countania** is planted in square orchards of exactly nine trees, with
  separate farmhouses. Everything there can be counted.
- **Uncountania** is wheat and dunes, stuff you can only measure.
- **Regularia** is a tidy grid of fields.
- **Each irregular island** has its own landmark: Bell Island a bell tower,
  Windward Isle a windmill, Keep Island a castle keep, Broken Reef a wreck.

`terrain()` never plants anything inside a label's box.

## 1. `countable-chart`: Countania and Uncountania

![countable chart](sea-charts/countable-chart.png)

| On the chart | What it teaches |
|---|---|
| **Countania** (brick, west) | *a / an · many · a few · -s* |
| **Uncountania** (wheat, east) | *much · a little · no a / an · no -s* |
| **Paired harbours** | Each uncountable harbour faces its countable partner at the same latitude, with the same surname: *Furniture Crag ↔ Chair Crag, Information Point ↔ Fact Point, Advice Head ↔ Tip Head, Luggage Sands ↔ Suitcase Sands*. Twelve pairs: work/job, information/fact, advice/tip, luggage/suitcase, furniture/chair, travel/trip, money/coin, music/song, equipment/tool, weather/storm, homework/task, progress/step. The trap is on the east shore. The way out is directly across the water. |
| **Double Isle** (lilac) | Both shores, two meanings: coffee, chicken, paper, room, glass, hair, time. Lilac, like Twofold Isle, so "the lilac island is both" holds across the series. |
| **The False Cape** | A spur of Uncountania flying **-S**. *News, maths and physics* look plural but are singular: *the news is*. |
| **The piece-of ferry** | The one way across, west only: *a piece of advice · a bottle of water · a slice of bread*. |
| **The Shallows** | Quantifiers that work on either shore: *some, any, a lot of, plenty of, no, enough, more, most*. |

## 2. `countable-hold`: the rooms, in a ship

![ship's hold](sea-charts/countable-hold.png)

The same point shown as rooms. There are two holds, and between them is the
galley, where both kinds of noun sit together.

- **The counting hold** (HOW MANY?): chairs, suitcases, coins, loaves, tools
  and letters. Each one sits apart and carries a tag: *a chair · 3 chairs*.
- **The bulk hold** (HOW MUCH?): the same cargo in heaps, with one word on
  each heap: FURNITURE, LUGGAGE, MONEY, BREAD, EQUIPMENT, MAIL.
- **The galley** (BOTH): one of each thing beside the stuff it is made of:
  *a coffee / coffee*, *a chicken / chicken*, *a paper / paper*,
  *a glass / glass*, *a cake / cake*, *a chocolate / chocolate*. Hair stays
  on the map as Hair Head. A single hair can't be painted recognisably.

In the lesson, the hold comes first because it gives the idea: **the same
cargo, a different word**. Then the map, which is clickable and carries the
nouns and the traps.

## 3. `verbs-chart`: Regularia and the irregular archipelago

![verbs chart](sea-charts/verbs-chart.png)

| On the chart | What it teaches |
|---|---|
| **Regularia** (green, west) | One continent, one rule (*verb + -ed*), and the smoothest coast on the chart. Three provinces by sound: **/t/** (Stop Harbour, Walk Ridge, Watch Head, Cook Cove), **/d/** (Play Bay, Study Sands, Travel Tarn, Call Crag), **/ɪd/** (Start Point, Wait Moor, Visit Fell, Land's End). The spelling rules are in the names: *stopped, studied, travelled, played*. |
| **The archipelago** (Irregularia: no one rule, but families) | Each family is an island. **Bell Island** *ring · rang · rung* (sing, drink, swim, begin). **Ought Island** *buy · bought* (bring, think, catch, teach). **Windward Isle** *blow · blew · blown* (grow, know, throw, fly). **Keep Island** *keep · kept*, the -t endings (sleep, feel, leave, build). **Broken Reef** *break · broke · broken* (speak, steal, wake, choose). |
| **The Still Rocks / the Lone Stacks** | *cut · put · hit · let · cost*, which never change. *go · be · do · see*, which belong to no family. |
| **Forked Isle** (lilac) | One verb, two meanings, two past forms: *lie (lied / lay), hang (hanged / hung), shine (shined / shone)*. |
| **Currents west** | New verbs arrive regular (*texted, emailed, googled*). Some old ones are drifting west too, into the Shallows (*learnt / learned, dreamt / dreamed, burnt / burned, spelt / spelled*). |

*Didn't went* belongs in the lesson, not on the map. It is a rule about
sentences, not a place.

## Midjourney requests: the countable-noun rooms

There are three pictures, and they sit side by side on the page as three
rooms of one ship. Each one is its own image, so none of them has to line up
with a layout. The labels are fitted to what you paint afterwards.

Every prompt ends with the same **style stem**:

```text
antique hand-painted illustration, watercolour and fine ink hatching on aged parchment, warm lantern light, cutaway view of a wooden ship's interior, no text, no lettering, no labels, no numbers --ar 3:4 --sref https://forbesenglish.com/sailing-the-seas-of-grammar/chart-clean.jpg --no text, letters, words, writing, numbers
```

Paste each subject below in front of the stem.

| file | subject |
|---|---|
| `hold-count` | `the counting hold of a wooden sailing ship, cargo set out one by one in neat separate rows on plank shelves: three wooden chairs, four leather suitcases, six gold coins in a line, four loaves of bread, five tools, six sealed letters, every item apart from the others with a small blank paper tag, orderly and tidy,` |
| `hold-bulk` | `the bulk hold of the same wooden sailing ship, the same cargo piled into heaps with nothing separate: a jumbled heap of furniture, a mound of luggage, a spilled heap of coins and banknotes, a pile of bread, a heap of tools and equipment, a burst sack of mail spilling letters, untidy and overflowing,` |
| `hold-galley` | `the ship's galley between the two holds, a long wooden table with pairs set side by side: one cup of coffee beside an open sack of coffee beans, a live hen beside a roast chicken on a plate, a folded newspaper beside a ream of blank paper, a drinking glass beside a leaning pane of glass, a whole iced cake beside a single slice, one wrapped chocolate beside a broken bar of chocolate,` |

Notes:

- **The tags are blank on purpose.** The page writes *a chair · 3 chairs* on
  top of them. Midjourney lettering comes out as pseudo-writing.
- **The three have to read as one ship.** Use the same `--sref` and the same
  seed for all three if you can, and pick renders with similar light.
- **The bulk hold must be the same cargo as the counting hold.** That is the
  whole point. If a render swaps chairs for barrels, reroll it.

Drop them in **`incoming/sea-charts/`** as `hold-count`, `hold-bulk` and
`hold-galley` (PNG or JPG).

## Upgrading the maps (optional)

The painted charts are finished art, but they can be upgraded. The safe
route is the Midjourney editor's **Retexture**. Upload the `-plain.png` for
the chart, use a prompt like
`antique hand-painted sea chart, watercolour and ink on parchment --sref <the chart-clean URL above>`,
and it repaints while keeping the coastlines, which is what keeps every label
on its land. Name the result `countable-chart-upgrade` or
`verbs-chart-upgrade` and drop it in `incoming/sea-charts/`. The label check
runs against it before it goes on a page.

A fresh composition from a plain prompt would not keep the coastlines, and
the labels would need re-fitting.

## After the rooms arrive (for the session that picks this up)

1. `tools/prep-artwork.py` on each file.
2. Fit the hold's label layer (item tags, heap names, galley pairs) to the
   painted objects, then re-run the page builder.
3. `extract-palette.py` on the lesson's hero, then `build_hubs.py`,
   `seo.py`, and the catalogue row.
