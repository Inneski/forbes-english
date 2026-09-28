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
  4 "more subtly and more of a sheen like the reflection of oil" -> this.
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
FILM = (0.78, 0.13)      # OKLCh lightness and chroma of the film's colours: a touch lighter than the grey
# the two films: (angle deg, em per colour, opacity). Different angles and band widths, so where
# they cross the colours interfere, as a film of oil does, instead of lying in one set of stripes
FILMS = [(118, 0.15, 0.20), (32, 0.21, 0.16)]
DRIFT = 22               # seconds for one drift, there and back again as one breath (alternate)
GLINT = 0.45             # the reflection's strength at its middle, as opacity of the paper's colour


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
    """a repeating run through the spectrum, back to where it began, faint: mixed in OKLab so
    hue melts into hue, as interference colours do"""
    stops = ['color-mix(in srgb,var(--shimmer-%d) %d%%,transparent) %.2fem'
             % (i % n + 1, round(alpha * 100), i * step) for i in range(n + 1)]
    return 'repeating-linear-gradient(%ddeg in oklab,%s)' % (angle, ','.join(stops))


def block(src):
    colours = film_colours(src)
    n = len(colours)
    ink = 'color-mix(in srgb,var(--ink) %d%%,transparent)'
    films = [film(n, *f) for f in FILMS]
    grey = 'linear-gradient(var(--tensing),var(--tensing))'
    # the reflection: a wide soft band of the paper's own light gliding over the film, which is
    # what makes a film read as a sheen rather than as paint
    glint = ('linear-gradient(105deg,transparent 30%%,color-mix(in srgb,var(--paper) %d%%,transparent) 50%%,'
             'transparent 70%%)' % round(GLINT * 100))
    css = [
        '/* "Tensing": its grey under a thin film of the camps\' colours, as oil on a wet road,',
        '   two films at different angles drifting slowly over each other (tools/sherpa_wash.py) */',
        ':root{%s}' % ' '.join('--shimmer-%d:%s;' % (i + 1, c) for i, c in enumerate(colours)),
        '.wordmark .brand .wash{font-style:normal;}',
        '@supports ((-webkit-background-clip:text) or (background-clip:text)){',
        '  .wordmark .brand .wash{display:inline-block;padding:0 .04em .1em;margin:0 -.04em -.1em;color:transparent;',
        '    text-shadow:none;-webkit-background-clip:text;background-clip:text;',
        '    background-image:%s,%s,%s;' % (glint, ','.join(films), grey),
        # three times the word each way and never repeated: the films can drift anywhere in
        # 0-100% and the word never meets an edge, so there is no seam to see
        '    background-size:300%% 100%%,300%% 300%%,300%% 300%%,100%% 100%%;background-repeat:no-repeat;',
        '    filter:drop-shadow(0 0 1px var(--paper)) drop-shadow(0 2px 1.5px %s) drop-shadow(0 8px 10px %s);'
        % (ink % 42, ink % 34),
        '    animation:st-oil %ds ease-in-out infinite alternate;}' % DRIFT,
        '}',
        # the two films take different paths, so their crossing never settles
        # (the reflection crosses the word once each way: 100% is off its left, 0% off its right)
        '@keyframes st-oil{0%{background-position:100% 0,0% 10%,100% 0%,0 0}'
        '50%{background-position:50% 0,55% 90%,35% 70%,0 0}100%{background-position:0% 0,100% 35%,0% 100%,0 0}}',
        '@media (prefers-reduced-motion:reduce){.wordmark .brand .wash{animation:none;}}',
    ]
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
