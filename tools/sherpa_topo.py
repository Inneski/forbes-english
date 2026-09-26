#!/usr/bin/env python3
"""Contour areas on every Sherpa page: a band down from the top, one up from
the foot, and four large areas alternating sides down the page, reaching
into the lesson column and across a phone screen.

    python tools/sherpa_topo.py            # add or refresh the block on every page
    python tools/sherpa_topo.py --check    # exit 1 if a page is missing it or it is stale
    node   tools/sherpa_topo_clear.js      # measure: every text on the paper has its halo

Innes, 2026-09-26: "some parts could have topology background areas ...
parts of each background", then "add more topology to all the tenses".

HOW. The hub's tile (`Sherpa Tensing/topo-tile.svg`, from tools/topo_tile.py)
is used as a MASK, not a picture, so each page draws the lines in its own
--accent-dark: plum on camp one, teal on camp four, pale green on descent
nine's dark page. One pseudo-element covers <body>, behind everything; its
mask is the tile intersected with the union of the six areas.

TEXT. The first version put lines behind the hero and measured each text
token against a line crossing it: eight camps failed at any visible
opacity (the recolours leave --accent at 3.0:1 and --accent-dark just over
4.5:1 on the paper). The second kept to the margins, which left a laptop
with thin strips and a phone with nothing. This one does what the hub
does: every text that sits straight on the paper wears a paper-coloured
halo (a survey-map label), so no line ever touches a glyph and every token
is measured on the paper as before. Cards, buttons and chips have their
own grounds and hide the lines anyway. The hero diagrams paint a paper
rectangle; a feathered paper shadow turns its hard edge into a clearing.

tools/sherpa_topo_clear.js renders every page at four widths and fails on
any text straight on the paper without the halo, and on any halo that
lands on something other than the paper (a glow round a button's text).

The route map is not touched: its whole background is the tile.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TILE = 'Sherpa Tensing/topo-tile.svg'
START, END = '<!-- SHERPA-TOPO:start -->', '<!-- SHERPA-TOPO:end -->'
FENCE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
OPACITY = 1       # the hub draws the tile at full strength

# the text that sits straight on the paper on every Sherpa page (measured
# 2026-09-26 over all 25 pages at 1280 and 390): wordmark, title, lead,
# section labels and headings, loose examples and notes, route links, the
# translation bar's label, the passive gate's dashed link
HALO_ON = ['.wordmark', 'h1', 'h1 ~ p', '.camp > .camp-label', '.camp > h2', '.camp > p.example',
           '.camp > p.chart-note', '.btnrow > a.route-link', '.tr-bar > .tr-label', '.voice-bar a.ghost']
HALO = '0 0 2px var(--paper),0 0 4px var(--paper),0 0 6px var(--paper),0 0 8px var(--paper)'

# (x, y%, w, h): each area is a soft ellipse; x 'L' centres it on the left edge, 'R' on the right
AREAS = [('L', 24, 1240, 1100), ('R', 46, 1240, 1100), ('L', 68, 1240, 1100), ('R', 88, 1240, 1000)]


def area_mask(tile_path):
    """The mask declarations: the tile intersected with the union of the areas.
    tools/sherpa_sheen.py draws its glint through the same areas with its own tile."""
    tile = 'url("%s") 0 0/640px 640px repeat' % tile_path.replace(' ', '%20')
    layers = [tile,
              'linear-gradient(#000 0,#000 40%,transparent 100%) 0 0/100% 900px no-repeat',
              'linear-gradient(to top,#000 0,#000 30%,transparent 100%) 0 100%/100% 700px no-repeat']
    for side, y, w, h in AREAS:
        x = '%dpx' % (-w // 2) if side == 'L' else 'calc(100%% + %dpx)' % (w // 2)
        layers.append('radial-gradient(closest-side,#000 35%%,transparent 100%%) %s %d%%/%dpx %dpx no-repeat'
                      % (x, y, w, h))
    n = len(layers) - 1
    return ['  -webkit-mask:%s;' % ','.join(layers),
            '  mask:%s;' % ','.join(layers),
            '  /* after the shorthand, which resets it: the tile intersects the union of the areas */',
            '  -webkit-mask-composite:%s;' % ','.join(['source-in'] + ['source-over'] * n),
            '  mask-composite:%s;' % ','.join(['intersect'] + ['add'] * n)]


def block():
    css = ['/* contour areas (tools/sherpa_topo.py): the hub\'s tile as a mask, drawn in this',
           '   page\'s --accent-dark, in six areas; text on the paper wears a paper halo */',
           'body{position:relative;}',
           'body::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;',
           '  background:var(--accent-dark);opacity:%s;' % OPACITY] + area_mask(TILE)
    css[-1] += '}'
    css += [
           '%s{text-shadow:%s;}' % (','.join(HALO_ON), HALO),
           '/* these two take a background on hover, where a halo would be a glow */',
           '.btnrow > a.route-link:hover,.voice-bar a.ghost:hover{text-shadow:none;}',
           '/* a hero diagram paints a paper rectangle: feather its edge into a clearing */',
           'svg.hero-diagram{background:var(--paper);box-shadow:0 0 18px 14px var(--paper);}',
           '.ring-hero-svg{border-radius:50%;box-shadow:0 0 16px 10px var(--paper);}',
           '@media print{body::before{display:none;}}']
    return START + '\n<style id="sherpa-topo">\n' + '\n'.join(css) + '\n</style>\n' + END + '\n'


def pages():
    return sorted(p for p in glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))
                  if not p.endswith('sherpa-tensing-route-map.html'))


def main():
    check = '--check' in sys.argv
    if not os.path.exists(os.path.join(ROOT, TILE)):
        sys.exit('! %s is missing (tools/topo_tile.py makes it)' % TILE)
    bad = []
    for p in pages():
        src = io.open(p, encoding='utf-8').read()
        name = os.path.basename(p)
        if not re.search(r'--accent-dark\s*:', src):
            bad.append('%s: no --accent-dark to draw the lines in' % name)
            continue
        if not re.search(r'<main\b', src):
            bad.append('%s: no <main>: not a lesson page' % name)
            continue
        # rewrite the block where it stands (tools/sherpa_type.py keeps one beside it,
        # and moving either would make the other look stale); insert only when absent
        new = (FENCE.sub(lambda m: block(), src, count=1) if FENCE.search(src)
               else src.replace('</head>', block() + '</head>', 1))
        if check:
            if new != src:
                bad.append('%s: contour block missing or stale' % name)
        elif new != src:
            io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
            print('  ' + name)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: %d pages' % len(pages()) if not bad else 'FAIL: %d problem(s)' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
