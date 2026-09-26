#!/usr/bin/env python3
"""Clouds drifting across the Sherpa route map, seen from above.

    python tools/sherpa_sky.py            # make the tiles and add or refresh the layer
    python tools/sherpa_sky.py --check    # exit 1 if the layer is missing or stale
    node   tools/sherpa_sheen_perf.js     # the same frame measurement applies

Innes, 2026-09-26: "get aerial shot of clouds moving in the background like
in the https://mythsmap.english-heritage.org.uk/", and on whether we could
make the clouds ourselves: yes. The clouds come from tools/make_clouds.py,
drawn from noise; nothing of English Heritage's is used.

HOW THEIRS WORKS (read from their saved page): ~90 cloud images, 600x400,
three variants, scattered at random over a layer the size of the map; the
whole layer drifts along the live wind direction over 300s and fades out at
the end of each loop; half the clouds sit at another "altitude" and move
faster when the map is dragged.

HOW THIS WORKS: the clouds are baked into two repeating tiles, a far one
(small, faint, slow) and a near one (larger, brighter, faster), each cloud
with a soft shadow on the ground beneath it, which is what makes a cloud
read as seen from above. Each tile is drawn with its clouds wrapped across
its edges, so it repeats without a seam, and each layer slides exactly one
tile per loop, so the loop has no seam either: no fade needed. Only
`transform` animates. The layer sits behind the page's content, above the
paper, the contours and the sheen; the text on the paper already wears a
paper halo (tools/sherpa_sheen.py), so no cloud crosses a glyph.
prefers-reduced-motion holds the clouds still; print hides them.
"""
import io
import os
import re
import sys

import numpy as np
from PIL import Image, ImageFilter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import make_clouds                                         # noqa: E402

PAGE = 'sherpa-tensing-route-map.html'
DIR = 'Sherpa Tensing'
# name: (tile w, tile h, clouds, scale range, opacity, shadow alpha, seconds per tile, seed)
LAYERS = {
    'far':  (1800, 1400, 7, (0.30, 0.46), 0.62, 0.10, 240, 11),
    'near': (2300, 1800, 6, (0.55, 0.80), 0.95, 0.18, 150, 23),
}
CSS_START, CSS_END = '<!-- SHERPA-SKY:start -->', '<!-- SHERPA-SKY:end -->'
EL_START, EL_END = '<!-- SHERPA-SKY-EL:start -->', '<!-- SHERPA-SKY-EL:end -->'
CSS_FENCE = re.compile(re.escape(CSS_START) + r'.*?' + re.escape(CSS_END) + r'\n?', re.S)
EL_FENCE = re.compile(re.escape(EL_START) + r'.*?' + re.escape(EL_END) + r'\n?', re.S)
ELEMENT = EL_START + '\n<div class="sherpa-sky" aria-hidden="true"><i></i><i></i></div>\n' + EL_END + '\n'


def tile(name):
    tw, th, n, (s0, s1), opacity, shadow_a, _, seed = LAYERS[name]
    rng = np.random.default_rng(seed)
    canvas = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    shadows = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    # spread the clouds: one per horizontal band, jittered, so they never pile up
    for i in range(n):
        c = make_clouds.cloud(seed * 100 + i)
        s = rng.uniform(s0, s1)
        c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
        a = np.asarray(c, np.float32)
        a[..., 3] *= opacity
        c = Image.fromarray(a.clip(0, 255).astype(np.uint8), 'RGBA')
        x = int(rng.uniform(0, tw))
        y = int(th * (i + rng.uniform(0.1, 0.9)) / n)
        # its shadow on the ground: the same shape, dark, blurred, off to the lower right
        sh = np.zeros((c.height, c.width, 4), np.float32)
        sh[..., 3] = np.asarray(c, np.float32)[..., 3] * shadow_a / max(opacity, 1e-3)
        sh[..., :3] = (40, 34, 38)
        sh = Image.fromarray(sh.clip(0, 255).astype(np.uint8), 'RGBA').filter(ImageFilter.GaussianBlur(18 * s + 6))
        off = (int(60 * s + 20), int(90 * s + 30))
        # wrap across every edge, so the tile repeats without a seam
        for dx in (-tw, 0, tw):
            for dy in (-th, 0, th):
                shadows.alpha_composite(sh, (x + dx + off[0], y + dy + off[1])) if -sh.width < x + dx + off[0] < tw and -sh.height < y + dy + off[1] < th else None
                canvas.alpha_composite(c, (x + dx, y + dy)) if -c.width < x + dx < tw and -c.height < y + dy < th else None
    out = Image.alpha_composite(shadows, canvas)
    path = os.path.join(ROOT, DIR, 'sky-%s.webp' % name)
    out.save(path, 'WEBP', quality=82, method=6)
    return path


def block():
    css = ['/* clouds drifting across the map, seen from above (tools/sherpa_sky.py): two tiles,',
           '   each sliding exactly one tile per loop, by transform only */',
           'body{position:relative;}',
           '.sherpa-sky{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden;}',
           '.sherpa-sky i{position:absolute;top:0;left:0;will-change:transform;}']
    for k, name in enumerate(('far', 'near'), 1):
        tw, th, _, _, _, _, secs, _ = LAYERS[name]
        url = '%s/sky-%s.webp' % (DIR.replace(' ', '%20'), name)
        css += ['.sherpa-sky i:nth-child(%d){width:calc(100%% + %dpx);height:calc(100%% + %dpx);'
                'background:url("%s") 0 0/%dpx %dpx repeat;animation:sherpa-sky-%s %ds linear infinite;}'
                % (k, tw, th, url, tw, th, name, secs),
                '@keyframes sherpa-sky-%s{from{transform:translate(-%dpx,-%dpx)}to{transform:translate(0,0)}}'
                % (name, tw, th)]
    css += ['@media (prefers-reduced-motion:reduce){.sherpa-sky i{animation:none;transform:translate(-40%,-30%);}}',
            '@media print{.sherpa-sky{display:none;}}']
    return CSS_START + '\n<style id="sherpa-sky">\n' + '\n'.join(css) + '\n</style>\n' + CSS_END + '\n'


def apply(src):
    b = block()
    src = CSS_FENCE.sub(lambda m: b, src, count=1) if CSS_FENCE.search(src) else src.replace('</head>', b + '</head>', 1)
    if EL_FENCE.search(src):
        return EL_FENCE.sub(lambda m: ELEMENT, src, count=1)
    # after the sheen, so the clouds pass over the lit contours
    anchor = '<!-- SHERPA-SHEEN-EL:end -->\n'
    if anchor in src:
        return src.replace(anchor, anchor + ELEMENT, 1)
    return re.sub(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + ELEMENT, src, count=1)


def main():
    check = '--check' in sys.argv
    bad = []
    if not check:
        for name in LAYERS:
            p = tile(name)
            print('  %s  %d KB' % (os.path.relpath(p, ROOT), os.path.getsize(p) // 1024))
    for name in LAYERS:
        if not os.path.exists(os.path.join(ROOT, DIR, 'sky-%s.webp' % name)):
            bad.append('sky-%s.webp missing' % name)
    p = os.path.join(ROOT, PAGE)
    src = io.open(p, encoding='utf-8').read()
    new = apply(src)
    if check:
        if new != src:
            bad.append('%s: sky layer missing or stale' % PAGE)
    elif new != src:
        io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
        print('  ' + PAGE)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS' if not bad else 'FAIL: %d' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
