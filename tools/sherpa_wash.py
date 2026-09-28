#!/usr/bin/env python3
"""A living wash of the thirteen camps' colours on the route map's "Tensing".

    python tools/sherpa_wash.py            # write the block and the markup into the route map
    python tools/sherpa_wash.py --check    # exit 1 if either is missing or stale

Innes, 2026-09-28: "some kind of multicolored ... random pixel color wash or
waves of color that's constantly changing just on the word tensing".

THE COLOURS are the camps' own, read from the map's camp markers
(<g class="camp-dot" data-color=... data-href="sherpa-tensing-camp-N-...">),
so a camp recoloured on the map is recoloured in the wash on the next run.
Each is darkened in OKLCh, same hue and chroma, only as far as FLOOR on the
paper: "Tensing" is display type and must be seen, as its grey had to be.
That floor holds for the whole wash, not just the stops: the gradients and
the layer blend mix in sRGB, and a mix of two colours in gamma space is never
lighter than the lighter of them (each channel's x^2.2 is convex), so nothing
in between the stops falls under it. tools/check_route_map.py measures the
tokens.

THE MOTION is two layers clipped to the letters: the camps in route order,
sliding right; over them, the same colours in another order, spaced wider,
half transparent, sliding left. Each travels exactly one of its own periods
per loop, so neither has a seam, and they cross at different speeds, so the
mix keeps changing. Only background-position animates, over a word-sized box.
prefers-reduced-motion holds it still (still multicoloured).

THE SHADOW moves from text-shadow to filter: a text-shadow is painted over a
background clipped to the text and would darken the colours, a drop-shadow
is cast by the painted letters. Same halo and ink shadow as "Sherpa".

The markup: the word is wrapped once, <span><i class="wash">Tensing</i></span>,
because the outer span carries the arrival animation, whose filter (blur to
none) would otherwise overwrite the shadow's.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'lesson-template'))
import soften as S                                     # noqa: E402

MAP = os.path.join(ROOT, 'sherpa-tensing-route-map.html')
START, END = '<!-- SHERPA-WASH:start -->', '<!-- SHERPA-WASH:end -->'
FENCE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
MARK_OLD = '<div class="brand">Sherpa <span>Tensing</span></div>'
MARK_NEW = '<div class="brand">Sherpa <span><i class="wash">Tensing</i></span></div>'
FLOOR = 3.0
NUM = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen']
STEP = 1.1          # em per colour, the camps in route order (back layer)
STEP_FRONT = 1.7    # em per colour, shuffled, half transparent (front layer)
LOOP = 26           # seconds for each layer to travel one of its periods
SHUFFLE = [6, 1, 9, 4, 12, 7, 2, 10, 5, 0, 8, 3, 11]   # the second layer's order: no neighbours from the first


def camp_colours(src):
    got = {}
    for colour, n in re.findall(r'<g class="camp-dot[^"]*" data-color="(#[0-9A-Fa-f]{6})" '
                                r'data-href="sherpa-tensing-camp-([a-z]+)-', src):
        got.setdefault(n, colour.upper())
    missing = [n for n in NUM if n not in got]
    if missing:
        raise SystemExit('FAIL: no camp marker colour for camp %s' % ', '.join(missing))
    return [got[n] for n in NUM]


def paper(src):
    m = re.search(r'--paper:\s*(#[0-9A-Fa-f]{6})', src)
    return m.group(1).upper()


def hold(h, ground):
    L, C, H = S.to_lch(h)
    while S.contrast(S.from_lch(L, C, H), ground) < FLOOR:
        L -= 0.004
    return S.from_lch(L, C, H)


def layer(order, step, alpha):
    """one horizontal run through the colours, ending where it began: tiled at its own
    period, it repeats without a seam"""
    stops = []
    for i, k in enumerate(order + order[:1]):
        c = 'var(--wash-%d)' % (k + 1)
        if alpha < 1:
            c = 'color-mix(in srgb,%s %d%%,transparent)' % (c, round(alpha * 100))
        stops.append('%s %.2fem' % (c, i * step))
    return 'linear-gradient(90deg,%s)' % ','.join(stops), len(order) * step


def block(src):
    ground = paper(src)
    wash = [hold(c, ground) for c in camp_colours(src)]
    front, pf = layer(SHUFFLE, STEP_FRONT, .55)
    back, pb = layer(list(range(len(wash))), STEP, 1)
    ink = 'color-mix(in srgb,var(--ink) %d%%,transparent)'
    css = [
        '/* "Tensing" in a living wash of the thirteen camps\' colours (tools/sherpa_wash.py):',
        '   each darkened to %.1f:1 on the paper, two layers drifting against each other */' % FLOOR,
        ':root{%s}' % ' '.join('--wash-%d:%s;' % (i + 1, c) for i, c in enumerate(wash)),
        '.wordmark .brand .wash{font-style:normal;}',
        '@supports ((-webkit-background-clip:text) or (background-clip:text)){',
        '  .wordmark .brand .wash{display:inline-block;padding:0 .04em .1em;margin:0 -.04em -.1em;color:transparent;',
        '    text-shadow:none;-webkit-background-clip:text;background-clip:text;',
        '    background-image:%s,%s;' % (front, back),
        '    background-size:%.2fem 100%%,%.2fem 100%%;background-repeat:repeat-x;' % (pf, pb),
        '    filter:drop-shadow(0 0 1px var(--paper)) drop-shadow(0 2px 1.5px %s) drop-shadow(0 8px 10px %s);'
        % (ink % 42, ink % 34),
        '    animation:st-wash %ds linear infinite;}' % LOOP,
        '}',
        # each layer slides exactly one of its own periods per loop, the camps in route order
        # to the right, the shuffled ones to the left: no seam, and never the same mix twice
        '@keyframes st-wash{from{background-position:0 0,0 0}to{background-position:-%.2fem 0,%.2fem 0}}' % (pf, pb),
        '@media (prefers-reduced-motion:reduce){.wordmark .brand .wash{animation:none;}}',
    ]
    return START + '\n<style id="sherpa-wash">\n' + '\n'.join(css) + '\n</style>\n' + END + '\n', wash


def main():
    check = '--check' in sys.argv
    src = io.open(MAP, encoding='utf-8').read()
    blk, wash = block(src)
    new = src.replace(MARK_OLD, MARK_NEW, 1)
    new = FENCE.sub(lambda m: blk, new, count=1) if FENCE.search(new) else new.replace('</head>', blk + '</head>', 1)
    bad = [] if MARK_NEW in new else ['wordmark not in the expected form']
    if check:
        if new != src:
            bad.append('wash block or markup missing or stale')
        print('PASS: "Tensing" washes in %d camp colours, each >= %.1f:1' % (len(wash), FLOOR) if not bad
              else 'FAIL: ' + '; '.join(bad))
        sys.exit(1 if bad else 0)
    if bad:
        raise SystemExit('FAIL: ' + bad[0])
    if new != src:
        io.open(MAP, 'w', encoding='utf-8', newline='\n').write(new)
    for i, c in enumerate(wash):
        print('  camp %-2d %s  %.2f:1' % (i + 1, c, S.contrast(c, paper(src))))


if __name__ == '__main__':
    main()
