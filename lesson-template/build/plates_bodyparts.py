# -*- coding: utf-8 -*-
"""Artwork pipeline for the two body-parts decks.

The four hand-built SVG plates in BodyParts/ predate the decks — they were
drawn for the old scrolling lesson (HOUSE-STYLE §10: bespoke diagrams are the
best thing in an old file, keep them). Two mechanical steps turn them into
deck artwork, and both are here rather than done by hand because they have to
be repeatable when a plate is edited:

  1. **Halo the leader lines.** A leader drawn in one dark stroke disappears
     wherever it crosses the navy figure, which on a profile is most of its
     length — the shipped face plate read as though the eyebrow and eyelash
     labels pointed at the hairline. Every leader is drawn twice: a cream
     underlay, then the dark line. Same principle as the text-shadow §5 puts
     on copy over artwork. face-neck.svg carries its halos in the source (it
     was re-laid-out by hand for the three words the coursebook has and the
     plate did not); the rest get them here.

  2. **A wordless variant of every plate.** A labelled chart behind a
     matching round is an answer key: the learner reads the word off the
     background instead of recalling it. So each plate ships twice — labelled
     for the section divider, where the chart IS the teaching, and stripped
     for the question slides behind it. Stripping is text, leaders and dots;
     the drawing is untouched.

The wordless whole-body chart is the hero of Part 1, which is also why the
hero carries no labels: --hero is the background of every slide that does not
name its own, including all eighteen scored ones.

    py lesson-template/build/plates_bodyparts.py

Rasterising goes through headless Chromium (playwright, already in
node_modules) rather than cairosvg, which is not installed on Innes's machine:
the plates use DM Sans / Playfair / DM Mono by name and a renderer without
them silently substitutes a fallback of a different width.
"""
import json
import os
import re
import subprocess
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ART = os.path.join(ROOT, 'BodyParts')

# (source, plain-variant name or None, width, height)
PLATES = [
    ('anatomy-chart.svg', 'chart-plain.svg', 1600, 1000),
    ('face-neck.svg', 'face-plain.svg', 1280, 720),
    ('torso-organs.svg', 'torso-plain.svg', 1280, 720),
    ('limbs-extremities.svg', 'limbs-plain.svg', 1280, 720),
    ('idioms.svg', None, 1280, 720),
    ('idioms-soft.svg', None, 1280, 720),
    ('gestures.svg', None, 1600, 900),
    ('speaking.svg', None, 1280, 720),
]

# chart-plain is the hero of Part 1; gestures is the hero of Part 2.
JPEG = {
    'chart-plain.svg': 'hero.jpg',
    'face-neck.svg': 'face-neck.jpg',
    'face-plain.svg': 'face-plain.jpg',
    'torso-organs.svg': 'torso-organs.jpg',
    'torso-plain.svg': 'torso-plain.jpg',
    'limbs-extremities.svg': 'limbs-extremities.jpg',
    'limbs-plain.svg': 'limbs-plain.jpg',
    'idioms.svg': 'idioms.jpg',
    'idioms-soft.svg': 'idioms-soft.jpg',
    'gestures.svg': 'hero-idioms.jpg',
    'speaking.svg': 'speaking.jpg',
}

HALO_RULE = ('  .halo { fill: none; stroke: #f4eee2; stroke-width: 4.5; '
             'opacity: .92; }\n')


def halo(src):
    """Give every leader a cream underlay. Idempotent.

    The de-dup pass is not paranoia: the first version of _dup renamed the
    class by literal string, so on the two plates whose leaders are class
    "lead" rather than "ld" it emitted the dark line twice and no halo at
    all. Collapsing an identical adjacent pair makes a re-run repair that
    rather than double it again."""
    src = re.sub(r'(<polyline class="(?:ld|lead)"[^/]*/>)\1', r'\1', src)
    if 'class="halo"' in src:
        return src
    src = src.replace('  .ld {', HALO_RULE + '  .ld {')
    src = src.replace('  .lead ', HALO_RULE + '  .lead ')

    def _dup(m):
        return re.sub(r'class="(?:ld|lead)"', 'class="halo"', m.group(0)) + m.group(0)
    return re.sub(r'<polyline class="(?:ld|lead)"[^/]*/>', _dup, src)


SOFT = 0.42


def soft(src):
    """The same plate at SOFT strength over its own cream field.

    The idiom plate is three big saturated coral ribbons, and unlike the
    anatomy plates it does not go quiet behind a slide: at full strength the
    word-bank chips on the gap slides land on a ribbon and lose their edge.
    So it ships twice as well — full strength on the divider, where it is the
    thing being looked at, and soft behind the questions."""
    i = src.index('/>', src.index('<rect class="bg"')) + 2
    j = src.rindex('</svg>')
    return (src[:i] + '\n<g opacity="%s">' % SOFT + src[i:j] + '</g>\n'
            + src[j:]).replace('<title>', '<title>Soft: ')


def plain(src):
    """The same drawing with nothing written on it."""
    src = re.sub(r'<text\b.*?</text>', '', src, flags=re.S)
    src = re.sub(r'<polyline class="(?:ld|lead|halo)"[^/]*/>', '', src)
    src = re.sub(r'<circle class="(?:dt|dot)"[^/]*/>', '', src)
    src = re.sub(r'\n[ \t]*\n+', '\n', src)
    return src.replace('<title>', '<title>Unlabelled: ')


def rasterise(jobs):
    """jobs: [(svg_path, png_path, w, h)] — one headless Chromium for all."""
    script = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          '_raster_plates.js')
    open(script, 'w', encoding='utf-8', newline='').write(RASTER_JS)
    env = dict(os.environ, NODE_PATH=os.path.join(ROOT, 'node_modules'))
    subprocess.run(['node', script, json.dumps(jobs)], check=True, cwd=ROOT,
                   env=env)
    os.remove(script)


RASTER_JS = """const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const jobs = JSON.parse(process.argv[2]);
  const b = await chromium.launch();
  for (const [src, out, w, h] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h },
                                deviceScaleFactor: 1 });
    await p.goto(new URL('file://' + path.resolve(src)).href);
    await p.evaluate(() => document.fonts.ready);
    await p.waitForTimeout(250);
    await p.screenshot({ path: out });
    await p.close();
  }
  await b.close();
})();
"""


def main():
    jobs, made = [], []
    open(os.path.join(ART, 'idioms-soft.svg'), 'w', encoding='utf-8',
         newline='').write(soft(open(os.path.join(ART, 'idioms.svg'),
                                    encoding='utf-8').read()))
    for name, plain_name, w, h in PLATES:
        path = os.path.join(ART, name)
        if not os.path.exists(path):
            sys.exit('missing plate: %s' % path)
        src = open(path, encoding='utf-8').read()
        haloed = halo(src)
        if haloed != src:
            open(path, 'w', encoding='utf-8', newline='').write(haloed)
            made.append('haloed  %s' % name)
            src = haloed
        if plain_name:
            out = os.path.join(ART, plain_name)
            open(out, 'w', encoding='utf-8', newline='').write(plain(src))
            made.append('stripped %s' % plain_name)

    for svg, jpg in sorted(JPEG.items()):
        w, h = next((p[2], p[3]) for p in PLATES
                    if p[0] == svg or p[1] == svg)
        png = os.path.join(ART, '_%s.png' % jpg[:-4])
        jobs.append([os.path.join(ART, svg), png, w, h])

    rasterise(jobs)

    for (_, png, _, _), (svg, jpg) in zip(jobs, sorted(JPEG.items())):
        im = Image.open(png).convert('RGB')
        im.save(os.path.join(ART, jpg), 'JPEG', quality=86, optimize=True)
        os.remove(png)
        made.append('%s  %dx%d  %.0f KB'
                    % (jpg, im.width, im.height,
                       os.path.getsize(os.path.join(ART, jpg)) / 1024))

    print("\n".join(made))


if __name__ == '__main__':
    main()
