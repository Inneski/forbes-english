# Forbes English — lesson template

Start every new or revamped lesson here.

| File | What it is |
|---|---|
| `HOUSE-STYLE.md` | **Read this first.** The binding house-style specification. |
| `lesson-template.html` | Working 16:9 slide lesson. Copy it; fill in two marked regions. |
| `extract-palette.py` | Derives a lesson's colour palette from its hero image. |
| `check-lesson.js` | Pre-ship checker. Must exit clean before you push. |
| `forbes-logo.svgfrag` | The stacked Forbes / ENGLISH lockup. Copy verbatim. |
| `forbes-glyph.svgfrag` | The Forbes wordmark path on its own. |
| `sample-hero.jpg` | Placeholder hero so the template runs out of the box. |

## Quick start

```bash
cp lesson-template/lesson-template.html my-lesson.html
mkdir -p my-lesson && cp <your image> my-lesson/hero.jpg
python3 lesson-template/extract-palette.py my-lesson/hero.jpg
```

Then in `my-lesson.html`: set `--hero`, paste the palette, write the slides.
Then check it:

```bash
node lesson-template/check-lesson.js my-lesson.html
```

It must exit clean. Then work through the eye-checks in `HOUSE-STYLE.md` §12.
