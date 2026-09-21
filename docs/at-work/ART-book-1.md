# Artwork shopping list — Book 1, Day One

Every picture the Book 1 layout has a slot for, one line per slot, in the
form the site's other briefs use: append the stem to the subject. The spec
for ratios, sizes and composition is README §7; what is new here is the
five smaller spots a unit, which the layout added and the level file did
not name. Seven pictures a unit, 105 for the book, plus the cover and the
team page.

**Accent: gold.** Lena's gold shoulder bag is in every picture she is in.
The other props: Tom's flat cap, Ana's headset (usually on a screen), Sam's
round glasses, Priya's laptop under one arm. Figures are faceless silhouettes.

## The stem

```text
<subject>, flat vector illustration, cel-shaded, solid flat colour,
minimalist, Noma Bar style, warm cream ground, black and slate-blue
silhouettes, gold accent, bright and airy, figures as simple faceless
silhouettes, subject off-centre, no text, no numbers, no logos --style raw
```

## The slots and their shapes

| slot | where on the page | frame | ask for | compose |
|---|---|---|---|---|
| `opener` | across the top of the unit opener, 210 × 118 mm | 16:9 | `--ar 16:9` | subject in the middle 75%; nothing that matters in the bottom-left quarter |
| `scene` | beside the dialogue, arched, 80 × 130 mm | 3:5 portrait | `--ar 2:3`, expect 16:9 | subject inside the middle 40% of a wide frame, or ask for portrait and hope |
| `label` | beside the vocabulary matching, arched, 70 × 70 mm | square | `--ar 1:1`, expect 16:9 | the whole word set visible in one scene; centre it |
| `grammar` | beside the rule, narrow, 55 × 96 mm | 4:7 portrait | `--ar 2:3`, expect 16:9 | one figure, one action, centred |
| `roleplay` | beside the practice items, narrow, 55 × 100 mm | portrait | `--ar 2:3` | two figures facing, centred |
| `phrase` | beside the phrase box, arched, 70 × 80 mm | near square | `--ar 1:1` | a small scene, centred |
| `case` | beside the case, 70 × 104 mm | portrait | `--ar 2:3` | the situation, centred |

**Deliver as** PNG, un-split four-ups are fine; `tools/prep-artwork.py` picks
and hashes. **Filenames** `art/book-1/u05-scene.png` etc. Print wants the
2× upscale on everything and the 4× on the openers.

## Cover and front matter

| file | subject |
|---|---|
| `cover` | the Unit 1 opener recomposed for a portrait board: the video-call wall on the right, Lena with her gold bag small at the bottom-left, wide quiet cream at the left and bottom for the lockup |
| `team` | the whole Greenline team in one wide office scene: Sam in round glasses at a standing desk, Tom in a flat cap in the doorway with a box, Priya crossing with a laptop, Lena with her gold bag arriving, Ana in a headset on a big screen on the wall |
| `portrait-lena` … `portrait-priya` | five head-and-shoulders portraits for the Meet the Team page, one per character, each with its prop, on plain cream, matching scale |

## The units

### Unit 1 · People & Places

| slot | subject |
|---|---|
| opener | a video call as a wall of four big windows on a screen in a small bright office; Lena with her gold bag standing in front of it, Tom in his flat cap beside her, Ana in a headset on the screen, a pale-wood desk in the foreground |
| scene | Priya with a laptop under one arm leaning over Lena's desk, Lena writing her name on a card in big letters |
| label | a desk with a name card, a laptop showing a map with four countries marked, a lanyard, a mug, a headset and an office plant, each thing clear and separate |
| grammar | Lena alone at a laptop, one hand raised in a wave at the screen |
| roleplay | two silhouettes at two laptops back to back, each waving at its own screen |
| phrase | a hand writing a long name on a card, one letter picked out gold |
| case | a new-starter form on a clipboard, a pen, Lena's gold bag on the chair |

### Unit 2 · Work Days

| slot | subject |
|---|---|
| opener | two rooms side by side: a Bristol office on the left with Lena at a desk and rain on the window, a bright Valencia flat on the right with Ana in a headset and a sea horizon; one large clock face on each wall, hands only, one hour apart |
| scene | Lena at a laptop with a mug, the screen showing Ana waving, morning light in stripes across the desk |
| label | a daily timeline as a strip: alarm clock, bus, desk, sandwich, a video call, a front door at dusk |
| grammar | Lena walking into the office with a coffee, a wall clock behind her |
| roleplay | two silhouettes on a split screen, one with a sun behind, one with a moon |
| phrase | a headset lying beside a laptop whose screen shows a green dot |
| case | a weekly planner grid on a wall with a gold pin in one square |

### Unit 3 · The Digital Office

| slot | subject |
|---|---|
| opener | an office desk seen straight on: a laptop with a blank screen, a second monitor still in its box, a gold cable in a tangle, a printer on a shelf; Priya's silhouette with a laptop under her arm arriving from the right |
| scene | Lena holding her laptop up to a phone propped on the desk so Priya on the phone screen can see it; a small light glowing on the laptop's side |
| label | a flat-lay of desk kit: laptop, mouse, keyboard, charger, headphones, printer, a cupboard door ajar, a password sticky note left blank |
| grammar | a supply cupboard open with shelves of boxed screens and one empty shelf |
| roleplay | Lena holding up a frozen laptop, Priya's silhouette pointing at a button |
| phrase | a finger holding down a power button, a ring of light around it gold |
| case | a chat window on a screen drawn as three empty bubbles, a laptop with a red dot |

### Unit 4 · On the Move

| slot | subject |
|---|---|
| opener | a railway station concourse with a blank departure board, Lena with her gold bag walking towards a platform, a long train beyond the barrier; through the glass wall on the far left, Tom's van at the kerb |
| scene | a simple street map drawn as a picture: a station, a café on a corner, a dotted line of footprints turning left and going straight, one gold office door on the right |
| label | a row of transport in one street: a bus, a tram, a taxi, a bike, a van, a figure on foot, a ticket machine |
| grammar | a train pulling out of a platform, a clock on a pole |
| roleplay | Tom in his flat cap pointing down a street, Lena following his arm with her eyes |
| phrase | a corner with a café awning and an arrow of footprints turning left, the arrow gold |
| case | a phone with a map route drawn as a line from a station to a gold pin |

### Unit 5 · Well-being

| slot | subject |
|---|---|
| opener | one picture, two weathers: a seafront promenade in Valencia at sunrise on the right with Ana's silhouette walking, a rainy Bristol park on the left with Lena running under trees, one gold sun over the middle |
| scene | two laptops facing each other across a table, each screen showing a silhouette in a headset, a mug beside each |
| label | a weekend in objects: running shoes, a yoga mat, a cooking pot, a book, a football, a film ticket, a beach towel |
| grammar | a calendar week with small icons in the days, some days empty |
| roleplay | two silhouettes on a call leaning towards each other, one laughing |
| phrase | a raised eyebrow and a smile drawn as two curves on a cream circle, gold |
| case | a well-being board on a wall with sticky notes, one gold |

### Unit 6 · Company History

| slot | subject |
|---|---|
| opener | a garage with its door up, one wooden desk inside under a bare bulb, a younger Sam in round glasses in the doorway, a small van in the drive, a gold sunset behind the roofs |
| scene | a timeline drawn as a road with three small buildings along it — a garage, a small unit, a warehouse — and one van driving from the first towards the last |
| label | a company history in objects: a garage key, a first desk, a price tag, a calendar page, a photo frame, a milestone marker stone |
| grammar | an old photo of two silhouettes beside a single desk, the frame gold |
| roleplay | Sam at his desk telling a story with both hands, Lena with a notebook |
| phrase | a big number drawn as four blank blocks on a wall, a hand pointing at two of them |
| case | a website page mock-up as a picture: a headline bar, an old photo block, three short lines |

### Unit 7 · Recent Events

| slot | subject |
|---|---|
| opener | four small scenes in a row like a film strip: a train, a street with a café, a meeting room with one chair, a station at dusk; Lena's gold bag in every one |
| scene | Lena at the Monday call pointing at a screen that shows a photo of a chair, Tom and Sam listening on the other windows |
| label | a trip in objects: a train ticket, a coffee cup, a catalogue, a handshake, a sandwich, a house key |
| grammar | a diary page with four short entries drawn as lines, the first ticked gold |
| roleplay | Lena telling a story counting on her fingers, Tom listening with his cap pushed back |
| phrase | four stepping stones in a row across water, numbered by size |
| case | a report on a desk: a sheet with a title bar and six lines, a chair in the corner |

### Unit 8 · Current Projects

| slot | subject |
|---|---|
| opener | the warehouse floor from above: Tom in a flat cap loading flat boxes into an open van, Lena at a desk by the door with a laptop, Priya crossing the floor with hers, a gold forklift parked in the corner |
| scene | Lena and Priya side by side at one screen, Priya pointing at a column of cells |
| label | a busy desk: a laptop with a page half written, a spreadsheet printout, a stack of boxes, a phone mid-call, a van key, a clock |
| grammar | Tom mid-lift with a box, motion lines behind him |
| roleplay | Lena with a hand half raised at Priya's desk, Priya turning from her screen |
| phrase | a spreadsheet drawn as a grid with one column glowing gold |
| case | a team chat board with three cards: a tick, a spinner, an hourglass |

### Unit 9 · Making Choices

| slot | subject |
|---|---|
| opener | two cardboard boxes on a warehouse table, one plain and small, one large with a recycling mark; Tom and Lena on either side, each with a hand on one box; a gold price tag hanging from each |
| scene | two vans side by side in a yard, one small and one big, Tom in his flat cap between them scratching his head |
| label | pairs of things to compare: a big and a small box, a fast and a slow van, a cheap and a dear price tag, a strong and a thin cardboard sheet |
| grammar | a set of scales with a box on each pan, one pan lower |
| roleplay | Tom and Lena across a table, each holding up a different box |
| phrase | a thought bubble with a tick and a question mark, the tick gold |
| case | two app icons on a phone screen, one with a price tag |

### Unit 10 · The Green Office

| slot | subject |
|---|---|
| opener | a kitchen corner with three big bins in a row, blue, green and black; a shelf of ceramic mugs, a plant, a window with a bicycle outside; Lena pinning a blank poster to the wall, her gold bag on a chair |
| scene | Tom on the phone with one hand raised in a polite stop, a heap of plastic bags on the desk in front of him, one of them gold |
| label | the green kitchen in objects: three bins, a ceramic mug, a paper cup crossed out, a light switch, a window latch, a refill bottle |
| grammar | a poster on a wall with six lines, three ticks and three crosses |
| roleplay | Tom showing Lena the bins, pointing at the blue one |
| phrase | a hand raised palm out, friendly, a small gold heart above it |
| case | a plastic pen in a box with a bow, a hand pushing it gently back |

### Unit 11 · Simple Problems

| slot | subject |
|---|---|
| opener | a delivered desk in a customer's office with a crack across its top, one chair beside it and an empty outline where a second chair should be; Tom in his flat cap on the phone in the doorway |
| scene | Lena photographing the cracked desktop with her phone, the crack picked out in gold |
| label | things that go wrong: a cracked top, an empty chair outline, a late clock, a wrong-colour lamp, an order number on a label, a camera |
| grammar | a phone held out with a photo of a crack on its screen |
| roleplay | Tom on the phone with a hand on his chest, a customer silhouette on the other side of a split frame |
| phrase | two hands meeting over a broken desk, a gold sticking plaster on the crack |
| case | an email on a screen drawn as a subject bar and five lines, a gold envelope |

### Unit 12 · Arrangements

| slot | subject |
|---|---|
| opener | a wall calendar of blank squares with one square filled gold, Lena on the phone in front of it, a camera on a tripod and two light stands leaning in the corner |
| scene | a photographer's silhouette with a camera bag crossing the warehouse floor, Sam in his round glasses waving from a doorway |
| label | a photo shoot in objects: a calendar page, an invite card, a camera, two lights, a van key, a parking sign |
| grammar | a diary page with a time crossed out and a new time written beside it, gold |
| roleplay | Lena on the phone with a calendar in the other hand, a photographer silhouette on a split frame |
| phrase | two clock faces, one with its hands moved, an arrow between them |
| case | a calendar invite drawn as a card: what, when, where, who, one line each |

### Unit 13 · Orders & Prices

| slot | subject |
|---|---|
| opener | a hotel lobby with a long empty meeting room seen through open doors; the hotel manager holding a tablet that shows Ana in her headset; forty small chair silhouettes stacked in a corner |
| scene | an invoice as a picture: a sheet on a desk with rows of blank lines and one gold total box, a hand with a pen checking a row |
| label | an order in objects: stacked chairs, a desk, an invoice, a coin stack, a euro and a pound sign, a delivery van |
| grammar | a pile of chairs beside a pile of coins, both the same height |
| roleplay | Ana in a headset with a form, the hotel manager silhouette with a tablet |
| phrase | two digits drawn large as blocks with a question mark between them |
| case | an order confirmation drawn as a receipt with four lines and a gold total |

### Unit 14 · Visitors

| slot | subject |
|---|---|
| opener | the Greenline showroom, three pale-wood desks and chairs on display; Lena at the door with a tray of two cups, Mr Shaw's silhouette with a briefcase stepping in; a gold cushion on one chair |
| scene | a laptop screen showing six small video windows, one of them outlined in gold with a hand raised, a plate of biscuits beside the keyboard |
| label | a welcome in objects: a coat on a hook, a tray with two cups, a plate of biscuits, a visitor badge, a showroom chair, a water jug |
| grammar | a tray with a coffee and a tea, a hand hovering over one |
| roleplay | Lena holding a door open, a visitor silhouette with a briefcase |
| phrase | an armchair with a cushion and a cup on the arm, the cushion gold |
| case | a reception desk with a visitor book open, a pen, a plant |

### Unit 15 · Next Steps

| slot | subject |
|---|---|
| opener | a taxi at the kerb outside the Greenline office at golden hour; Ana with a suitcase turning to wave; Lena, Tom and Sam in the doorway; a gold sky over the roofs |
| scene | a notebook open on a desk with three ticks drawn down a list, a gold pen, a train ticket tucked into the corner |
| label | a future in objects: a course certificate, a camera on a tripod, a shop front outline, a ladder, a suitcase, a phone with a heart |
| grammar | Lena at a crossroads sign with three blank arrows, her gold bag on her shoulder |
| roleplay | Sam and Lena across a desk, a sheet with three lines between them |
| phrase | two silhouettes waving, one with a suitcase, a taxi's rear light gold |
| case | a goodbye card standing on a desk, one gold line drawn on it |
