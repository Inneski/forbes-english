#!/usr/bin/env python3
"""Contour areas on every Sherpa page, in the margins beside the lesson: a band
down the top of the page that fades out, and one up from the foot that fades in.

    python tools/sherpa_topo.py            # add or refresh the block on every page
    python tools/sherpa_topo.py --check    # exit 1 if a page is missing it or it is stale
    node   tools/sherpa_topo_clear.js      # measure: no bare text under a line

Innes, 2026-09-26, after the hub got its contour background: "some parts
could have topology background areas ... parts of each background".

HOW. The hub's tile (`Sherpa Tensing/topo-tile.svg`, from tools/topo_tile.py)
is used as a MASK, not a picture, so each page draws the lines in its own
--accent-dark: plum on camp one, teal on camp four, pale green on descent
nine's dark page. Two pseudo-elements on <body>, behind everything, each
masked three ways at once: by the tile, by a vertical fade, and by a
horizontal carve that keeps the lesson's 1000px column clear.

WHY THE MARGINS. The first version laid the bands behind the hero, and
measured every text token against a line crossing it. Eight of the
thirteen camps refused at any visible opacity: the recolours leave --accent
at 3.0:1 and --accent-dark just over 4.5:1 on the paper, so a line under the
wordmark or a kicker breaks a floor. The carve takes text out of the
question instead of trading contrast page by page, so every page carries
the same line. Below about 1080px there is no margin and the page is plain,
as it was.

The one piece of text that lives in the margin, the "Show me anyway" link
beside the passive gate, gets a paper halo, as the hub's kicker does.
tools/sherpa_topo_clear.js renders every page at four widths and fails on
any text sitting straight on the paper inside a band without one.

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
COLUMN = 500      # half of main's max-width
CLEAR = 16        # px of plain paper between the last line and main's edge
FADE = 56         # px over which the lines fade in beyond that
OPACITY = 1      # the hub draws the tile at full strength; the carve, not opacity, protects the text


def block():
    tile = 'url("%s") 0 0/640px 640px repeat' % TILE.replace(' ', '%20')
    inner, outer = COLUMN + CLEAR, COLUMN + CLEAR + FADE
    carve = ('linear-gradient(to right,#000 0,#000 calc(50%% - %dpx),transparent calc(50%% - %dpx),'
             'transparent calc(50%% + %dpx),#000 calc(50%% + %dpx),#000 100%%)' % (outer, inner, inner, outer))
    top = 'linear-gradient(to bottom,#000 0,#000 35%,transparent 100%)'
    foot = 'linear-gradient(to top,#000 0,#000 30%,transparent 100%)'
    css = ['/* contour areas (tools/sherpa_topo.py): the hub\'s tile as a mask, drawn in this',
           '   page\'s --accent-dark, in the margins only: the lesson column stays clear */',
           'body{position:relative;}',
           'body::before,body::after{content:"";position:absolute;left:0;right:0;z-index:-1;pointer-events:none;',
           '  background:var(--accent-dark);opacity:%s;}' % OPACITY,
           '/* the mask shorthand resets mask-composite, so the composite comes after it, */',
           '/* in the same rule: without it the three layers add up to a solid block   */',
           'body::before{top:0;height:min(820px,100vh);',
           '  -webkit-mask:%s,%s,%s;' % (tile, top, carve),
           '  mask:%s,%s,%s;' % (tile, top, carve),
           '  -webkit-mask-composite:source-in;mask-composite:intersect;}',
           'body::after{bottom:0;height:min(560px,70vh);',
           '  -webkit-mask:%s,%s,%s;' % (tile, foot, carve),
           '  mask:%s,%s,%s;' % (tile, foot, carve),
           '  -webkit-mask-composite:source-in;mask-composite:intersect;}',
           '/* the one text in the margin, the gate\'s dashed "Show me anyway": a paper halo */',
           '.voice-bar a.ghost{text-shadow:0 0 2px var(--paper),0 0 4px var(--paper),0 0 6px var(--paper),0 0 8px var(--paper);}',
           '@media print{body::before,body::after{display:none;}}']
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
            bad.append('%s: no <main>, so no column to keep clear' % name)
            continue
        new = FENCE.sub('', src).replace('</head>', block() + '</head>', 1)
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
