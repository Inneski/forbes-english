#!/usr/bin/env python3
"""A thin sheen of the thirteen camps' colours floating across the route map's "Tensing".

    python tools/sherpa_wash.py            # write the block and the markup into the route map
    python tools/sherpa_wash.py --check    # exit 1 if either is missing or stale

Innes, 2026-09-28: "some kind of multicolored ... random pixel color wash or
waves of color that's constantly changing just on the word tensing"; the
first try filled the whole word with two drifting runs of colour. Then: "try
something like that but more of a thinner wave sheen that floats across";
that was a narrow streak of the camps' colours held dark, thirteen slivers
side by side, and read as "a hard edged band, I meant something ethereal
magical tasteful - a bright multicoloured sheen wash". So now: the word
keeps its grey (--tensing), and a soft light washes across it, as over
mother-of-pearl, with a faint bloom round the word while it passes.

THE COLOURS are the camps' own, read from the map's camp markers
(<g class="camp-dot" data-color=... data-href="sherpa-tensing-camp-N-...">),
so a camp recoloured on the map is recoloured in the light on the next run:
the chromatic ones, sorted by hue so they flow as a spectrum rather than
stripe, each lifted to one pastel lightness and chroma (PASTEL). They are
light, and are meant to be: the word's resting grey is what must be read
(tools/check_route_map.py measures --tensing at 3:1), and the light is a
passing highlight on a logotype, which WCAG 1.4.3 leaves out of its
contrast rule. The ink shadow keeps the letters' shape under it.

NO EDGES: each colour's opacity swells from nothing to PEAK and back along
the band (sin^2), and the gradient mixes in OKLab, so hue melts into hue and
the light into the grey.

THE MOTION: the light sits in the middle of a background WIDE words wide,
not repeated, and background-position carries it from off the word's left
to off its right, eased, in SWEEP of every LOOP seconds; the rest of the loop
it waits outside the word. The bloom (a drop-shadow in the middle colour)
rises and falls with it. Only background-position and the word's filter
animate, over a word-sized box. prefers-reduced-motion leaves the light
outside: plain grey.

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
WIDE = 4            # the background is this many words wide; the light sits in its middle
BAND = (30, 70)     # the light's extent, in % of that background (1.6 words, most of it faint)
PEAK = 0.82         # the light's opacity at its heart; it falls away as sin^2 either side
PASTEL = (0.87, 0.105)   # OKLCh lightness and chroma of the light's colours
ANGLE = 110         # deg: a slant, as light falls
LOOP = 10           # seconds from one pass to the next
SWEEP = 0.68        # the part of the loop spent crossing
GLOW = 0.55         # the bloom round the word at the light's height, as opacity


def camp_colours(src):
    got = {}
    for colour, n in re.findall(r'<g class="camp-dot[^"]*" data-color="(#[0-9A-Fa-f]{6})" '
                                r'data-href="sherpa-tensing-camp-([a-z]+)-', src):
        got.setdefault(n, colour.upper())
    missing = [n for n in NUM if n not in got]
    if missing:
        raise SystemExit('FAIL: no camp marker colour for camp %s' % ', '.join(missing))
    return [got[n] for n in NUM]



def shimmer(src):
    """the camps' colours as light: the chromatic ones, in order of hue so they flow as a
    spectrum does, each lifted to one pastel lightness and chroma"""
    lch = [S.to_lch(c) for c in camp_colours(src)]
    hues = sorted(h for L, C, h in lch if C > 0.03)     # the greys (camps 12, 13) have no hue to give
    return [S.from_lch(PASTEL[0], PASTEL[1], h) for h in hues]


def light(n):
    """the band: each colour at an opacity that swells from nothing to PEAK and back (sin^2),
    mixed in OKLab so neighbouring hues melt into each other"""
    a, b = BAND
    stops = ['transparent %.1f%%' % a]
    for i in range(n):
        t = (i + 1) / (n + 1)
        alpha = PEAK * math.sin(math.pi * t) ** 2
        stops.append('color-mix(in srgb,var(--shimmer-%d) %d%%,transparent) %.2f%%'
                     % (i + 1, round(alpha * 100), a + (b - a) * t))
    stops.append('transparent %.1f%%' % b)
    return 'linear-gradient(%ddeg in oklab,%s)' % (ANGLE, ','.join(stops))


def block(src):
    colours = shimmer(src)
    ink = 'color-mix(in srgb,var(--ink) %d%%,transparent)'
    shadow = 'drop-shadow(0 0 1px var(--paper)) drop-shadow(0 2px 1.5px %s) drop-shadow(0 8px 10px %s)' % (ink % 42, ink % 34)
    mid = 'var(--shimmer-%d)' % (len(colours) // 2 + 1)
    glow = lambda a: 'drop-shadow(0 0 9px color-mix(in srgb,%s %d%%,transparent))' % (mid, round(a * 100))
    s = round(SWEEP * 100)
    css = [
        '/* "Tensing": a soft light of the camps\' colours washes across its grey, as over',
        '   mother-of-pearl, and the word blooms faintly as it passes (tools/sherpa_wash.py) */',
        ':root{%s}' % ' '.join('--shimmer-%d:%s;' % (i + 1, c) for i, c in enumerate(colours)),
        '.wordmark .brand .wash{font-style:normal;}',
        '@supports ((-webkit-background-clip:text) or (background-clip:text)){',
        '  .wordmark .brand .wash{display:inline-block;padding:0 .04em .1em;margin:0 -.04em -.1em;color:transparent;',
        '    text-shadow:none;-webkit-background-clip:text;background-clip:text;',
        '    background-image:%s,linear-gradient(var(--tensing),var(--tensing));' % light(len(colours)),
        '    background-size:%d00%% 100%%,100%% 100%%;background-repeat:no-repeat;' % WIDE,
        '    filter:%s %s;' % (shadow, glow(0)),
        '    animation:st-sheen %ds cubic-bezier(.45,.05,.55,.95) infinite;}' % LOOP,
        '}',
        # 100%: the light is off the word's left; 0%: off its right. Then it waits.
        # The bloom rises and falls with it, at its height when the light is mid-word
        '@keyframes st-sheen{0%%{background-position:100%% 0,0 0;filter:%s %s}' % (shadow, glow(0)),
        '  %d%%{filter:%s %s}' % (s // 2, shadow, glow(GLOW)),
        '  %d%%,100%%{background-position:0%% 0,0 0;filter:%s %s}}' % (s, shadow, glow(0)),
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
        print('PASS: a light of %d camp colours washes across "Tensing"' % len(wash) if not bad
              else 'FAIL: ' + '; '.join(bad))
        sys.exit(1 if bad else 0)
    if bad:
        raise SystemExit('FAIL: ' + bad[0])
    if new != src:
        io.open(MAP, 'w', encoding='utf-8', newline='\n').write(new)
    print('  light: ' + ' '.join(wash))


if __name__ == '__main__':
    main()
