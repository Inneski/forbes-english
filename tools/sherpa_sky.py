#!/usr/bin/env python3
"""Clouds drifting across every Sherpa page, seen from above.

    python tools/sherpa_sky.py            # make the clouds and add or refresh the layer on all 26 pages
    python tools/sherpa_sky.py --check    # exit 1 if a page's layer is missing or stale
    node   tools/sherpa_sheen_perf.js     # the frame measurement, with and without the effects

Innes, 2026-09-26: "get aerial shot of clouds moving in the background like
in the https://mythsmap.english-heritage.org.uk/", then "put the clouds on tense
pages too but lose the visible hard edge around the clouds". The clouds come
from tools/make_clouds.py, drawn from noise; nothing of English Heritage's is used.

HOW THEIRS WORKS (read from their saved page, in incoming/): ~90 cloud images,
600x400, three variants, scattered over a layer the size of the map, which
drifts along the live wind direction over 300s and fades out at each loop.

HOW THIS WORKS: six cloud images, each with a soft shadow on the ground beneath
it (what makes a cloud read as seen from above), baked on a canvas padded well
past the blur so no edge is cut; the tool refuses a cloud whose border is not
clear. Nine of them drift across a FIXED, screen-sized layer, each on its own
loop, near clouds larger and quicker, far ones smaller, fainter and slower,
staggered by negative delays so the sky is never empty. The page scrolls
beneath them, as the ground does under an aircraft.

WHY SCREEN-SIZED. The first version slid two page-sized tiles; on a long tense
page at phone density those were layers of hundreds of millions of pixels,
and with the sheen the page fell to 17 fps whenever anything else animated
(tools/sherpa_sheen_perf.js, 4x-throttled phone). Nine cloud-sized layers
cost a small fraction of that and do not grow with the page.

Only `transform` animates. The layer sits behind the content, above the paper,
the contours and the sheen; text on the paper wears a paper halo, so no cloud
crosses a glyph. On a night page (the descents) the sky is fainter. For
prefers-reduced-motion the clouds stand still where they are; print hides them.
"""
import glob
import io
import os
import re
import sys

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_clouds                                         # noqa: E402

DIR = 'Sherpa Tensing'
IMAGES = 6                  # cloud-1 .. cloud-6.webp, seeds 3100 + i
SHADOW = 0.16               # the shadow's strength
# each cloud on the page: (image, width px, top % of the screen, seconds to cross, delay fraction, opacity)
CLOUDS = [
    (1, 560, 8, 95, 0.10, 0.95), (2, 480, 38, 110, 0.55, 0.95), (3, 620, 64, 85, 0.30, 0.95), (4, 430, 84, 120, 0.80, 0.9),
    (5, 300, 20, 170, 0.20, 0.6), (6, 260, 50, 190, 0.65, 0.55), (1, 280, 74, 180, 0.45, 0.6), (2, 240, 2, 200, 0.90, 0.5),
    (3, 270, 92, 175, 0.05, 0.55)]
DARK_OPACITY = 0.38         # on a night page white clouds glare: fainter, as clouds seen at night
CSS_START, CSS_END = '<!-- SHERPA-SKY:start -->', '<!-- SHERPA-SKY:end -->'
EL_START, EL_END = '<!-- SHERPA-SKY-EL:start -->', '<!-- SHERPA-SKY-EL:end -->'
CSS_FENCE = re.compile(re.escape(CSS_START) + r'.*?' + re.escape(CSS_END) + r'\n?', re.S)
EL_FENCE = re.compile(re.escape(EL_START) + r'.*?' + re.escape(EL_END) + r'\n?', re.S)
ELEMENT = (EL_START + '\n<div class="sherpa-sky" aria-hidden="true">' + '<i></i>' * len(CLOUDS) + '</div>\n' + EL_END + '\n')


def image(k):
    """Cloud k with its ground shadow, on a canvas padded past the blur."""
    c = make_clouds.cloud(3100 + k)
    a = np.asarray(c, np.float32)[..., 3]
    radius = 22
    pad = int(3 * radius) + 4
    off = (40, 60)                                       # the sun is to the upper left
    w, h = c.width + 2 * pad + off[0], c.height + 2 * pad + off[1]
    sh = np.zeros((h, w, 4), np.float32)
    sh[pad + off[1]:pad + off[1] + c.height, pad + off[0]:pad + off[0] + c.width, 3] = a * SHADOW
    sh[..., :3] = (40, 34, 38)
    shadow = Image.fromarray(sh.clip(0, 255).astype(np.uint8), 'RGBA').filter(ImageFilter.GaussianBlur(radius))
    out = shadow.copy()
    out.alpha_composite(c, (pad, pad))
    al = np.asarray(out)[..., 3]
    edge = max(al[0].max(), al[-1].max(), al[:, 0].max(), al[:, -1].max())
    if edge > 0:                                          # the measurement: a cut shows as a hard edge
        sys.exit('! cloud-%d has alpha %d on its border: it would show a hard edge' % (k, edge))
    path = os.path.join(ROOT, DIR, 'cloud-%d.webp' % k)
    out.save(path, 'WEBP', quality=84, method=6)
    return path, out.size


def dark(src):
    m = re.search(r'--paper\s*:\s*#([0-9A-Fa-f]{6})', src)
    if not m:
        return False
    r, g, b = (int(m.group(1)[i:i + 2], 16) for i in (0, 2, 4))
    return (0.2126 * r + 0.7152 * g + 0.0722 * b) < 110


def block(sizes, is_dark=False):
    css = ['/* clouds drifting across the screen, seen from above (tools/sherpa_sky.py): nine clouds,',
           '   each on its own loop, in a fixed screen-sized layer, by transform only */',
           '.sherpa-sky{position:fixed;inset:0;z-index:-1;pointer-events:none;overflow:hidden;%s}'
           % ('opacity:%s;' % DARK_OPACITY if is_dark else ''),
           '.sherpa-sky i{position:absolute;left:0;background:0 0/100% 100% no-repeat;will-change:transform;'
           'animation:sherpa-sky-drift linear infinite;}',
           '@keyframes sherpa-sky-drift{from{transform:translateX(-100%)}to{transform:translateX(100vw)}}']
    for n, (k, w, top, secs, delay, op) in enumerate(CLOUDS, 1):
        iw, ih = sizes[k]
        css.append('.sherpa-sky i:nth-child(%d){top:%d%%;width:%dpx;height:%dpx;background-image:url("%s/cloud-%d.webp");'
                   'animation-duration:%ds;animation-delay:-%ds;opacity:%s;}'
                   % (n, top, w, round(w * ih / iw), DIR.replace(' ', '%20'), k, secs, round(secs * delay), op))
    css += ['/* the smallest phones: the far clouds only would crowd, so the near ones shrink */',
            '@media (max-width:560px){.sherpa-sky i{transform-origin:0 0;}.sherpa-sky i:nth-child(-n+4){scale:.7;}}',
            '@media (prefers-reduced-motion:reduce){.sherpa-sky i{animation-play-state:paused;}}',
            '@media print{.sherpa-sky{display:none;}}']
    return CSS_START + '\n<style id="sherpa-sky">\n' + '\n'.join(css) + '\n</style>\n' + CSS_END + '\n'


def apply(src, sizes):
    b = block(sizes, dark(src))
    src = CSS_FENCE.sub(lambda m: b, src, count=1) if CSS_FENCE.search(src) else src.replace('</head>', b + '</head>', 1)
    if EL_FENCE.search(src):
        return EL_FENCE.sub(lambda m: ELEMENT, src, count=1)
    anchor = '<!-- SHERPA-SHEEN-EL:end -->\n'               # after the sheen: clouds over the lit contours
    if anchor in src:
        return src.replace(anchor, anchor + ELEMENT, 1)
    return re.sub(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + ELEMENT, src, count=1)


def main():
    check = '--check' in sys.argv
    bad = []
    sizes = {}
    for k in range(1, IMAGES + 1):
        p = os.path.join(ROOT, DIR, 'cloud-%d.webp' % k)
        if check:
            if not os.path.exists(p):
                bad.append('cloud-%d.webp missing' % k)
                continue
            sizes[k] = Image.open(p).size
        else:
            p, sizes[k] = image(k)
            print('  %s  %dx%d  %d KB' % (os.path.relpath(p, ROOT), sizes[k][0], sizes[k][1], os.path.getsize(p) // 1024))
    if bad:
        for b in bad:
            print('FAIL ' + b)
        sys.exit(1)
    for p in sorted(glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))):
        name = os.path.basename(p)
        src = io.open(p, encoding='utf-8').read()
        new = apply(src, sizes)
        if check:
            if new != src:
                bad.append('%s: sky layer missing or stale' % name)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: 26 pages' if not bad else 'FAIL: %d' % len(bad))
    else:
        print('  26 pages')
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
