#!/usr/bin/env python3
"""A living sheen across the contour lines on every Sherpa page.

    python tools/sherpa_sheen.py            # add or refresh it on all 26 pages
    python tools/sherpa_sheen.py --check    # exit 1 if a page is missing it or it is stale
    node   tools/sherpa_topo_clear.js       # measure: every text on the paper keeps its halo
    node   tools/sherpa_sheen_perf.js       # measure: what it costs in frames

Innes, 2026-09-26: "can you put a magic animated living shiny sheen wave
effect across the topology?"

HOW. Two slanted bands of light drift across the page, one each way, at
different angles and speeds, and light up the contour lines where they
cross them. The light is a gradient on two <i> elements inside a
<div class="topo-sheen">, and that div is masked by `Sherpa
Tensing/topo-sheen.svg`: the same contours as the tile, at full opacity and
a little wider, so a lit line glints rather than tints. On a lesson page
the mask is also cut to the contour areas (tools/sherpa_topo.py's
area_mask), so the glint appears only where there are lines; on the route
map, whose whole background is the tile, it is the tile alone.

Each band is a repeating gradient that slides exactly one period per
cycle, so the loop has no seam and every stretch of a long page sees a
band go by. Only `transform` animates, so the browser moves the light on
the compositor instead of repainting the page; tools/sherpa_sheen_perf.js
measures the frame rate with and without it on a throttled phone.

COLOUR, per page, from its own tokens in OKLCh: on a light page the light
is the accent pushed vivid (L 0.62) with a brighter, warmer centre; on a
dark descent it is the accent near white. Text is untouched: every text on
the paper already wears the paper halo (tools/sherpa_topo.py), which the
light passes behind. prefers-reduced-motion switches it off, as does print.
"""
import glob
import io
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'lesson-template'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from soften import to_lch, from_lch                   # noqa: E402
import sherpa_topo                                     # noqa: E402

TILE = 'Sherpa Tensing/topo-tile.svg'
SHEEN_TILE = 'Sherpa Tensing/topo-sheen.svg'
MAP = 'sherpa-tensing-route-map.html'
CSS_START, CSS_END = '<!-- SHERPA-SHEEN:start -->', '<!-- SHERPA-SHEEN:end -->'
EL_START, EL_END = '<!-- SHERPA-SHEEN-EL:start -->', '<!-- SHERPA-SHEEN-EL:end -->'
CSS_FENCE = re.compile(re.escape(CSS_START) + r'.*?' + re.escape(CSS_END) + r'\n?', re.S)
EL_FENCE = re.compile(re.escape(EL_START) + r'.*?' + re.escape(EL_END) + r'\n?', re.S)
ELEMENT = EL_START + '\n<div class="topo-sheen" aria-hidden="true"><i></i><i></i></div>\n' + EL_END + '\n'

# the route map's text straight on the paper (measured by tools/sherpa_topo_clear.js,
# 2026-09-26): the lesson pages carry theirs in tools/sherpa_topo.py; the map needs its
# own, because the sheen lights the tile behind its whole page, not just the areas
HUB_HALO = ['.wordmark .sub', '.counts', '.intro h1', '.intro .lead', '.section-title', '.map-how',
            '.legend', '.teach-row > span', '.btn-ghost']
HALO = sherpa_topo.HALO

# (angle deg, period px along the gradient, band px, seconds, direction, opacity)
BANDS = [(100, 1600, 300, 11, 1, 0.95), (72, 2300, 200, 19, -1, 0.6)]


def sheen_tile():
    """The contours at full opacity and 1.5x the width: a lit line glints."""
    svg = io.open(os.path.join(ROOT, TILE), encoding='utf-8').read()
    svg = re.sub(r'stroke-opacity="[0-9.]+"', 'stroke-opacity="1"', svg)
    svg = re.sub(r'stroke-width="([0-9.]+)"', lambda m: 'stroke-width="%.2f"' % (float(m.group(1)) * 1.5), svg)
    return svg


def tokens(src):
    return {k: v.upper() for k, v in re.findall(r'(--[a-z-]+)\s*:\s*(#[0-9A-Fa-f]{6})', src)}


def colours(t):
    acc = t['--accent']
    L, C, H = to_lch(acc)
    dark = to_lch(t['--paper'])[0] < 0.5
    warm = H + math.radians(28)
    if dark:
        return from_lch(0.88, max(C, 0.11), H), from_lch(0.97, 0.06, warm)
    return from_lch(0.62, max(C * 1.15, 0.15), H), from_lch(0.76, max(C, 0.13), warm)


def band_css(i, angle, period, band, secs, direction, opacity):
    lead = period - band
    grad = ('repeating-linear-gradient(%ddeg,transparent 0,transparent %dpx,var(--sheen) %dpx,'
            'var(--sheen-hot) %dpx,var(--sheen) %dpx,transparent %dpx)'
            % (angle, lead, lead + band * 0.4, lead + band * 0.5, lead + band * 0.6, period))
    hp = period / math.sin(math.radians(angle))          # the pattern's horizontal period
    frm, to = ('-%.1fpx' % hp, '0') if direction > 0 else ('0', '-%.1fpx' % hp)
    return ['.topo-sheen i:nth-child(%d){left:-%dpx;right:-%dpx;background:%s;opacity:%s;' % (i, math.ceil(hp), math.ceil(hp), grad, opacity),
            '  animation:topo-sheen-%d %ss linear infinite;}' % (i, secs),
            '@keyframes topo-sheen-%d{from{transform:translateX(%s)}to{transform:translateX(%s)}}' % (i, frm, to)]


def block(src, is_map):
    t = tokens(src)
    sheen, hot = colours(t)
    if is_map:
        tile = 'url("%s") 0 0/640px 640px repeat' % SHEEN_TILE.replace(' ', '%20')
        mask = ['  -webkit-mask:%s;' % tile, '  mask:%s;' % tile]
    else:
        mask = sherpa_topo.area_mask(SHEEN_TILE)
    css = ['/* a living sheen across the contours (tools/sherpa_sheen.py): two bands of light,',
           '   moved by transform only, seen through the contour lines */',
           ':root{--sheen:%s;--sheen-hot:%s;}' % (sheen, hot),
           'body{position:relative;}',
           '.topo-sheen{position:absolute;inset:0;z-index:-1;pointer-events:none;overflow:hidden;'] + mask
    css[-1] += '}'
    css += ['.topo-sheen i{position:absolute;top:0;bottom:0;will-change:transform;}']
    for i, b in enumerate(BANDS, 1):
        css += band_css(i, *b)
    if is_map:
        css += ['/* the light crosses the whole map page: its text on the paper wears the paper halo */',
                '%s{text-shadow:%s;}' % (','.join(HUB_HALO), HALO),
                '.btn-ghost:hover{text-shadow:none;}',
                '/* the clouds\' labels ("used to", "to be used to doing"): SVG\'s halo is a paper outline */',
                'g[filter="url(#cloud-shadow)"] text{paint-order:stroke;stroke:var(--paper);stroke-width:4px;stroke-linejoin:round;}']
    css += ['@media (prefers-reduced-motion:reduce){.topo-sheen{display:none;}}',
            '@media print{.topo-sheen{display:none;}}']
    return CSS_START + '\n<style id="sherpa-sheen">\n' + '\n'.join(css) + '\n</style>\n' + CSS_END + '\n'


def apply(src, is_map):
    b = block(CSS_FENCE.sub('', src), is_map)
    src = CSS_FENCE.sub(lambda m: b, src, count=1) if CSS_FENCE.search(src) else src.replace('</head>', b + '</head>', 1)
    if EL_FENCE.search(src):
        src = EL_FENCE.sub(lambda m: ELEMENT, src, count=1)
    else:
        src = re.sub(r'(<body\b[^>]*>\n?)', lambda m: m.group(1) + ELEMENT, src, count=1)
    return src


def main():
    check = '--check' in sys.argv
    bad = []
    tile_path = os.path.join(ROOT, SHEEN_TILE)
    want = sheen_tile()
    have = io.open(tile_path, encoding='utf-8').read() if os.path.exists(tile_path) else None
    if have != want:
        if check:
            bad.append('%s missing or stale' % SHEEN_TILE)
        else:
            io.open(tile_path, 'w', encoding='utf-8', newline='\n').write(want)
            print('  ' + SHEEN_TILE)
    for p in sorted(glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))):
        name = os.path.basename(p)
        src = io.open(p, encoding='utf-8').read()
        if '--accent' not in tokens(src) or '--paper' not in tokens(src):
            bad.append('%s: no --accent/--paper to colour the light' % name)
            continue
        new = apply(src, name == MAP)
        if check:
            if new != src:
                bad.append('%s: sheen missing or stale' % name)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  ' + name)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: 26 pages' if not bad else 'FAIL: %d problem(s)' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
