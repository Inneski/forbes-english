#!/usr/bin/env python3
"""An oil-film sheen on the route map's "Tensing", in the camps' colours.

    python tools/sherpa_wash.py            # write the block and the markup into the route map
    python tools/sherpa_wash.py --check    # exit 1 if either is missing or stale

Innes, 2026-09-28, four tries in one afternoon, each answer the brief for
the next:
  1 "some kind of multicolored ... random pixel color wash or waves of color
    that's constantly changing just on the word tensing" -> the whole word in
    two drifting runs of camp colour;
  2 "more of a thinner wave sheen that floats across" -> a narrow streak of
    thirteen dark slivers: "a hard edged band";
  3 "something ethereal magical tasteful - a bright multicoloured sheen
    wash" -> a wide pastel light, feathered, passing every ten seconds;
  4 "more subtly and more of a sheen like the reflection of oil" -> two
    faint films always on the grey, a pale reflection gliding over them;
  5 "Make the gliding band carry all the color" -> this.
The word keeps its grey (--tensing). On it lie two faint films of the camps'
colours, at different angles and band widths, so where they cross the
colours interfere as a film of oil does; both drift slowly, on different
paths, there and back, so the pattern never settles. Over them a wide, soft
band of the paper's own light glides once each way: the reflection, which
is what makes a film read as a sheen and not as paint.

THE COLOURS are the camps' own, read from the map's camp markers
(<g class="camp-dot" data-color=... data-href="sherpa-tensing-camp-N-...">),
so a camp recoloured on the map is recoloured in the film on the next run:
the chromatic ones, sorted by hue so they run as a spectrum rather than
stripe, each at one lightness and chroma (FILM), mixed in OKLab. The films
are faint (FILMS' opacities), so the word stays grey with colour in it. The
resting grey is what tools/check_route_map.py measures at 3:1; the sheen is
a tint on a logotype, which WCAG 1.4.3 leaves out of its contrast rule.

THE MOTION: every layer is three times the word each way and never
repeated, so moving anywhere within 0-100% the word never meets an edge.
One animation moves all of them, DRIFT seconds each way (alternate), eased.
Only background-position animates, over a word-sized box.
prefers-reduced-motion holds it still: a still film on the grey.

THE SHADOW is a filter: a text-shadow is painted over a background clipped
to the text and would darken it; a drop-shadow is cast by the painted
letters. Same halo and ink shadow as "Sherpa".

The markup: the word is wrapped once, <span><i class="wash">Tensing</i></span>,
because the outer span carries the arrival animation, whose filter (blur to
none) would otherwise overwrite the shadow's.
"""
import io
import math
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
NUM = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen']
WORD = 'Tensing'
FILM = (0.76, 0.14)      # OKLCh lightness and chroma of the film's colours
# the two films: (angle deg, em per colour, opacity). Different angles and band widths, so where
# they cross the colours interfere, as a film of oil does, instead of lying in one set of stripes.
# Seen only through the band, so they can be strong
FILMS = [(118, 0.13, 0.85), (32, 0.18, 0.55)]
LIGHT = 0.22             # the paper's own light in the band, over the film: the reflection
# the band's window, a mask (only its alpha counts): (position %, opacity) across it, soft all through
WINDOW = [(33, 0), (41, 0.3), (47, 0.85), (50, 1), (53, 0.85), (59, 0.3), (67, 0)]
ANGLE = 105              # deg: the band's slant, as light falls
LOOP = 14                # seconds for the films to go once round their paths
PASSES = [(0.0, 0.3), (0.5, 0.8)]   # when in the loop the band crosses, left to right
GRID = 0.025             # keyframe spacing through the loop


def paths(t):
    """at loop time t (0-1): where the band's window sits (100% is off the word's left, 0% off
    its right), and where the two films sit, on closed Lissajous curves (they end where they
    began, so the loop has no seam and no stop-and-turn)"""
    band = 100
    for s, e in PASSES:
        if s <= t <= e:
            u = (t - s) / (e - s)
            band = 100 - 100 * (3 * u * u - 2 * u ** 3)    # eased: floats in, floats out
    w = 2 * math.pi * t
    a = (50 + 50 * math.sin(w), 50 + 50 * math.sin(2 * w + 0.6))
    b = (50 + 50 * math.cos(w), 50 - 50 * math.sin(w + 1.1))
    return band, '0 0,%.1f%% %.1f%%,%.1f%% %.1f%%' % (a + b)


def keyframes():
    ts = {round(i * GRID, 4) for i in range(int(round(1 / GRID)) + 1)}
    for s, e in PASSES:
        ts |= {s, e, round(e + 0.001, 4)}           # the band leaves off the right, reappears off the left
    out = []
    for t in sorted(ts):
        band, films = paths(t)
        out.append('%.1f%%{background-position:%s;-webkit-mask-position:%.1f%% 0;mask-position:%.1f%% 0}'
                   % (t * 100, films, band, band))
    return '@keyframes st-oil{%s}' % ''.join(out)


def camp_colours(src):
    got = {}
    for colour, n in re.findall(r'<g class="camp-dot[^"]*" data-color="(#[0-9A-Fa-f]{6})" '
                                r'data-href="sherpa-tensing-camp-([a-z]+)-', src):
        got.setdefault(n, colour.upper())
    missing = [n for n in NUM if n not in got]
    if missing:
        raise SystemExit('FAIL: no camp marker colour for camp %s' % ', '.join(missing))
    return [got[n] for n in NUM]



def film_colours(src):
    """the camps' colours as a thin film: the chromatic ones, in order of hue so they run as
    a spectrum does, each at one lightness and chroma"""
    lch = [S.to_lch(c) for c in camp_colours(src)]
    hues = sorted(h for L, C, h in lch if C > 0.03)     # the greys (camps 12, 13) have no hue to give
    return [S.from_lch(FILM[0], FILM[1], h) for h in hues]


def film(n, angle, step, alpha):
    """a repeating run through the spectrum, back to where it began: mixed in OKLab so hue
    melts into hue, as interference colours do"""
    stops = ['color-mix(in srgb,var(--shimmer-%d) %d%%,transparent) %.2fem'
             % (i % n + 1, round(alpha * 100), i * step) for i in range(n + 1)]
    return 'repeating-linear-gradient(%ddeg in oklab,%s)' % (angle, ','.join(stops))


def block(src):
    colours = film_colours(src)
    n = len(colours)
    ink = 'color-mix(in srgb,var(--ink) %d%%,transparent)'
    films = [film(n, *f) for f in FILMS]
    light = 'linear-gradient({0},{0})'.format('color-mix(in srgb,var(--paper) %d%%,transparent)' % round(LIGHT * 100))
    window = 'linear-gradient(%ddeg,%s)' % (ANGLE, ','.join(
        ('color-mix(in srgb,#000 %d%%,transparent) %d%%' % (round(o * 100), at)) if 0 < o < 1
        else ('#000 %d%%' % at if o else 'transparent %d%%' % at) for at, o in WINDOW))
    css = [
        '/* "Tensing": grey at rest; a soft band of light glides across it carrying all the colour,',
        '   a film of the camps\' colours as oil on a wet road, seen only where the light is.',
        '   The film is on a copy of the word laid over it, masked by the moving band (tools/sherpa_wash.py) */',
        ':root{%s}' % ' '.join('--shimmer-%d:%s;' % (i + 1, c) for i, c in enumerate(colours)),
        '.wordmark .brand .wash{font-style:normal;position:relative;display:inline-block;padding:0 .04em .1em;margin:0 -.04em -.1em;',
        '  text-shadow:none;filter:drop-shadow(0 0 1px var(--paper)) drop-shadow(0 2px 1.5px %s) drop-shadow(0 8px 10px %s);}'
        % (ink % 42, ink % 34),
        '@supports ((-webkit-background-clip:text) or (background-clip:text)) and ((-webkit-mask-image:none) or (mask-image:none)){',
        # alt text "": the copy is decoration, a screen reader has already read the word
        '  .wordmark .brand .wash::after{content:"%s"/"";position:absolute;left:0;top:0;padding:inherit;white-space:nowrap;' % WORD,
        '    pointer-events:none;color:transparent;-webkit-background-clip:text;background-clip:text;',
        '    background-image:%s,%s;' % (light, ','.join(films)),
        # three times the word each way and never repeated: the films can drift anywhere in
        # 0-100% and the word never meets an edge, so there is no seam to see
        '    background-size:100% 100%,300% 300%,300% 300%;background-repeat:no-repeat;',
        '    -webkit-mask-image:%s;mask-image:%s;' % (window, window),
        '    -webkit-mask-size:300% 100%;mask-size:300% 100%;-webkit-mask-repeat:no-repeat;mask-repeat:no-repeat;',
        '    -webkit-mask-position:100% 0;mask-position:100% 0;',
        '    animation:st-oil %ds linear infinite;}' % LOOP,
        '}',
        # the films circle on different curves inside the band, so the colour it carries never
        # settles; the band crosses left to right twice a loop
        keyframes(),
        '@media (prefers-reduced-motion:reduce){.wordmark .brand .wash::after{animation:none;}}',
    ]
    # a line written with %% but never %-formatted reaches the page as "300%%", which the browser
    # drops without a word: the layers fell back to the word's own size, so moving them moved
    # nothing, and the first oil sheen shipped standing still (2026-09-28)
    bad = [l for l in css if '%%' in l]
    if bad:
        raise SystemExit('FAIL: unformatted %%%% in the CSS: ' + bad[0].strip()[:80])
    return START + '\n<style id="sherpa-wash">\n' + '\n'.join(css) + '\n</style>\n' + END + '\n', colours


def main():
    check = '--check' in sys.argv
    src = io.open(MAP, encoding='utf-8').read()
    blk, wash = block(src)
    new = src.replace(MARK_OLD, MARK_NEW, 1)
    new = FENCE.sub(lambda m: blk, new, count=1) if FENCE.search(new) else new.replace('</head>', blk + '</head>', 1)
    bad = [] if MARK_NEW in new else ['wordmark not in the expected form']
    if check:
        if new != src:
            bad.append('sheen block or markup missing or stale')
        print('PASS: a film of %d camp colours lies on "Tensing"' % len(wash) if not bad
              else 'FAIL: ' + '; '.join(bad))
        sys.exit(1 if bad else 0)
    if bad:
        raise SystemExit('FAIL: ' + bad[0])
    if new != src:
        io.open(MAP, 'w', encoding='utf-8', newline='\n').write(new)
    print('  film: ' + ' '.join(wash))


if __name__ == '__main__':
    main()
