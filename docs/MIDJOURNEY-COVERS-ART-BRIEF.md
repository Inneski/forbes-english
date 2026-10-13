# Midjourney brief: two covers that are currently duplicates

Paste each prompt into Midjourney as it is. The `--sref` link pulls in the
Part I cover from the live site as the style reference, so nothing needs
attaching. Pick the best of the four results, upscale it, and save it into
the folder named. Then tell a local Claude session "covers are in".

## 1. The Parisian Conquest II: The Long Winter

Save to [C:\Users\black\Documents\FORBES\incoming\parisian-conquest-2](../incoming/parisian-conquest-2)

```
flat mid-century screen-print illustration, Paris office interior at winter dusk, tall windows with dark slate-blue pillars, snow on Paris rooftops outside, cold pale blue-grey sky, a few falling snowflakes, three pendant lamps switched on casting small warm coral pools of light on a long desk, a woman in black silhouette with big hair tied back and a dark suit standing at the desk on the left, one hand on a stack of papers, looking at a monitor showing a falling bar chart, two coffee cups and a phone on the desk, a winter coat draped over an empty coral chair, right half calm with window and snow, quiet tense late-evening mood, limited palette, fine grain and speckle, hard silhouettes, no text --ar 16:9 --sref https://forbesenglish.com/dnd-rpg/parisian-office-scene.jpg --no text, letters, numbers, logo, watermark
```

## 2. Out of This World: 5-Hour Test Prep, Part II (A2)

Save to [C:\Users\black\Documents\FORBES\incoming\exam-prep-2](../incoming/exam-prep-2)

```
full-frame grid of flat hand-printed colour squares on a dark teal border, the squares form a hidden pixel picture: top two-thirds dark navy and near-black squares as a night sky with scattered pale yellow and white star squares, a small ringed planet made of orange and coral squares in the right third, bottom rows bright warm teal coral pink orange and yellow squares like a horizon, reads as a colour chart first and a space scene second, flat matte, subtle paper texture --ar 16:9 --sref https://forbesenglish.com/ExamPrep/hero.jpg --no text, letters, numbers, logo, watermark, gradients
```

## For the Claude session that puts them in

- Parisian II: `tools/prep-artwork.py` → `dnd-rpg/long-winter.jpg`; point
  the `<img>` in `forbes-dnd-rpg-part2.html` and its `LESSON_IMAGES` row in
  `library.html` at it (`check-library.js --vs-origin --expect
  forbes-dnd-rpg-part2.html`).
- Exam Prep II: same, to `ExamPrep/hero-part2.jpg`, row
  `exam-prep-5hour-course-part2.html`; that deck is generated, so change
  its builder, not the HTML.
- Then `tools/build_hubs.py`, `tools/seo.py`, commit by name, push.
