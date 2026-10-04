# Artwork: two more sea charts, and the ship's rooms, for Sailing the Seas of Grammar

Innes, 2026-09-30: *"make extra maps with nautical theme like gerundia
infinitivia but for countable and uncountable nouns although perhaps that can
also be two pictures of rooms full of one or the other with a interim space
where they share stuff, also possible for regular and irregular verbs"*.
Then: *"both in one lesson"*, *"the rooms can be in a ship"*, and *"I will
make the images on request using midjourney … I planned to upgrade whatever
you made anyway but I was specially talking about the countable noun
images"*, *"make it for chat gpt"*, and of a coded cross-section of the ship:
*"not what I had in mind, I imagined real rooms"* (2026-10-04).

So the work is split:

- **The two maps are painted in code** by `lesson-template/build/sea_charts.py`
  and `sea_paint.py`. They have parchment, a ruled border with a degree band,
  water lines along every coast, hatched cliffs, terrain and a compass rose.
  They are finished art and can be upgraded later.
- **The countable-noun pictures are Innes's**, made in ChatGPT from
  `docs/CHATGPT-SEA-CHARTS-BRIEF.md`. They are three real rooms in one ship,
  painted as scenes you could stand in, not a diagram. Nothing stands in for
  them: the coded cross-section was dropped.

Everything is written by a separate label layer, never by the painting. That
keeps the words translatable and lets the map switch between place names and
bare nouns. It also means any map upgrade that keeps the coastlines keeps
every label.

## The builder, and its check

```bash
py lesson-template/build/sea_charts.py
```

This writes each chart to `docs/sea-charts/` as `<name>.svg` / `.png`
(labelled) and `<name>-plain.svg` / `.png` (paint only). It exits non-zero if
any of these happen:

- a harbour name leaves its coast
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
- **Each irregular island** has its own landmark: I·A·U Island a bell tower,
  -EW Island a windmill, -T Island a castle keep, -EN Island a wreck.

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

## The ship's rooms: countable and uncountable as places you can stand in

Three pictures, three rooms of one ship. They are made in ChatGPT
(`CHATGPT-SEA-CHARTS-BRIEF.md`, part 1) and labelled by the page afterwards.

- **The store cabin, `room-count`** (HOW MANY?). Everything is separate and
  countable: chairs in a row, suitcases, coins laid out on the table, loaves,
  tools on hooks, letters, bottles, books, apples.
- **The cargo hold, `room-bulk`** (HOW MUCH?). Everything is in heaps you
  could only measure: grain from a chute, sand, coffee beans, rice, water
  across the floor. It also holds the same kinds of cargo as the cabin, piled
  up: furniture, luggage, money, mail. **The same cargo, a different word.**
- **The galley between them, `room-galley`** (BOTH). The single thing sits
  next to the stuff it is made of: *a coffee / coffee*, *a chicken / chicken*,
  *a paper / paper*, *a glass / glass*, *a cake / cake*, *a light / light*
  (the lantern, and the sunlight through the porthole).

In the lesson, the rooms come first because they give the idea. Each one
opens its own part: the cabin opens Countania, the hold opens Uncountania,
and the galley opens Double Isle. Then comes the map, which is clickable and
carries the nouns and the traps.

## 2. `verbs-chart`: Regularia and the irregular archipelago

![verbs chart](sea-charts/verbs-chart.png)

| On the chart | What it teaches |
|---|---|
| **Regularia** (green, west) | The biggest land and the smoothest coast on the chart, with one rule: *verb + -ed, and almost every other verb*. Three provinces by sound, six harbours each. **/t/**: Stop Harbour, Walk Ridge, Watch Head, Cook Cove, Like Mere, Laugh Rock. **/d/**: Play Bay, Study Sands, Travel Tarn, Call Crag, Live Ness, Open Sound. **/ɪd/**: Start Point, Wait Moor, Visit Fell, Need Haven, Decide Head, Land's End. The spelling rules are in the names: *stopped* (double), *liked, lived, decided* (just -d), *studied* (y → i), *travelled* (British double l), *opened* (no double, because the stress is on *op-*). |
| **The archipelago** (Irregularia: no one rule, but families) | Each family is an island named after the sound it shares. **I·A·U Island** *ring · rang · rung* (sing, drink, swim, begin). **Ought Island** *buy · bought* (bring, think, catch, teach). **-EW Island** *blow · blew · blown* (grow, know, throw, fly). **-T Island** *keep · kept* (sleep, feel, leave, build). **-EN Island** *speak · spoke · spoken*, where the third form ends in -en (break, take, give, write). |
| **The Still Rocks / the Lone Stacks** | *cut · put · hit · let · cost*, which never change. *go · be · do · see*, which belong to no family. |
| **Forked Isle** (lilac) | One verb, two meanings, two past forms: *lie (lied / lay), hang (hanged / hung), shine (shined / shone)*. |
| **Currents west** | New verbs arrive regular (*texted, emailed, googled*). Some old ones are drifting west too, into the Shallows (*learnt / learned, dreamt / dreamed, burnt / burned, spelt / spelled*). |

*Didn't went* belongs in the lesson, not on the map. It is a rule about
sentences, not a place.

## The pictures: ChatGPT, from `docs/CHATGPT-SEA-CHARTS-BRIEF.md`

The prompts Innes pastes are in **`docs/CHATGPT-SEA-CHARTS-BRIEF.md`**,
written to ChatGPT.

- **Part 1, the three rooms.** One conversation, so they come out as one
  ship in one light. No words in the pictures. The objects are asked for large
  and well spaced, so labels can be pinned to them.
- **Part 2, map upgrades (optional)**, done the Gerundia way: the labelled
  repaint first, then a clean copy with the harbour dots kept
  (`countable-chart-clean.png`, `verbs-chart-clean.png`). Blob-detect the
  dots on the clean copy and move the place coordinates in `sea_charts.py`
  to match, as `eb491249` did for `sailing_map.py`.

Everything lands in **`incoming/sea-charts/`**. The folder exists on Innes's
machine (created 2026-10-04). `incoming/` is gitignored, so a cloud session
has to ask for it to be made.

## After the rooms arrive (for the session that picks this up)

1. `tools/prep-artwork.py` on each file.
2. Pin a label to each object in the three rooms (*a chair · three chairs*
   in the cabin, FURNITURE and SAND in the hold, *a coffee / coffee* in the
   galley). Place them by measuring the picture, and check them at phone width.
3. `extract-palette.py` on the lesson's hero, then `build_hubs.py`,
   `seo.py`, and the catalogue row.
