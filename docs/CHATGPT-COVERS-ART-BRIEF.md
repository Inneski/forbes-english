# Brief for ChatGPT: two covers that are currently duplicates

**How to use this file.** Each section below is one picture. Start a new
ChatGPT chat for each one, attach the reference picture it names, and paste
everything between that section's two rules as your first message. Save
the result into the folder it names. Then tell a local Claude session:
*"The covers are in incoming — put them in."*

Both folders already exist:
- [C:\Users\black\Documents\FORBES\incoming\parisian-conquest-2](../incoming/parisian-conquest-2)
- [C:\Users\black\Documents\FORBES\incoming\exam-prep-2](../incoming/exam-prep-2)

Size for both: **landscape, 16:9** (1792 × 1024 in ChatGPT is fine; the
originals are 2944 × 1648).

---

## 1. The Parisian Conquest II: The Long Winter

**Attach:** [C:\Users\black\Documents\FORBES\dnd-rpg\parisian-office-scene.jpg](../dnd-rpg/parisian-office-scene.jpg)
(the Part I cover). **Save as:** `incoming/parisian-conquest-2/cover.png`

---

This is the cover of Part I of a business-English course called *The
Parisian Conquest*. Please make the cover of **Part II: The Long Winter**,
a sequel picture that sits next to it as a matching pair.

**Keep exactly the same style as the attached picture.** Flat mid-century
screen-print illustration, a limited palette, fine grain and speckle, hard
silhouettes, no gradients, no photographic detail. Same kind of office:
tall windows with dark pillars between them, a long desk, pendant lamps,
a Paris skyline through the glass.

**What changes: it is a year later, in deep winter.**
- Keep the slate blue and black. Swap the warm coral sky for a **cold
  pale blue-grey winter dusk**, with snow on the rooftops and a few
  falling flakes in the windows.
- The pendant lamps are **switched on**, giving small warm pools of
  coral-orange light on the desk: the only warm colour in the picture.
- Same woman in silhouette (big hair tied back, dark suit), now
  **standing** at the desk, one hand on a stack of papers, looking at a
  screen showing a falling bar chart. Steady and determined, not
  defeated.
- Detail on the desk: two coffee cups, a phone, a closed laptop.
  A winter coat over one of the empty chairs.
- The mood is "we kept the client, but this year was hard": quiet,
  late, tense, calm.

Put her and the desk in the **left half**. Keep the right half simpler
(window, sky, snow), because text sits there in the lesson. Keep faces
and anything important out of the top and bottom tenth.

No text, no letters, no numbers, no logos, no watermark anywhere.

---

## 2. Out of This World: 5-Hour Test Prep, Part II (A2)

**Attach:** [C:\Users\black\Documents\FORBES\ExamPrep\hero.jpg](../ExamPrep/hero.jpg)
(the Part I cover, a grid of colour squares). **Save as:** `incoming/exam-prep-2/cover.png`

---

This is the cover of Part I of an English test-prep course called *Out of
This World*. Please make the cover of **Part II**, a matching picture.

**Keep the same idea and style:** a full-frame grid of flat colour
squares, slightly hand-printed, on a dark teal frame, with the same
palette (teals, corals, pinks, oranges, yellows, deep blues).

**What changes:** the squares should form a picture you only see from a
distance. Some squares go dark navy and near-black to make a **night sky**
across the top two-thirds, with a few pale-yellow and white squares as
stars. A **small planet with a ring**, made of orange and coral squares,
sits in the right third. The bottom rows keep the bright warm colours of
Part I, like a horizon. It should still read as a colour grid first and
a space scene second.

Keep the important shapes out of the top and bottom tenth.

No text, no letters, no numbers, no logos, no watermark anywhere.

---

## For the Claude session that puts them in

- Parisian II: `tools/prep-artwork.py` → `dnd-rpg/long-winter.jpg`; point
  the `<img>` in `forbes-dnd-rpg-part2.html` and its `LESSON_IMAGES` row in
  `library.html` at it (`check-library.js --vs-origin --expect
  forbes-dnd-rpg-part2.html`).
- Exam Prep II: same, to `ExamPrep/hero-part2.jpg`, row
  `exam-prep-5hour-course-part2.html`. That deck is generated, so change
  its builder, not the HTML.
- Then `tools/build_hubs.py`, `tools/seo.py`, commit by name, push.
