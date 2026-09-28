#!/usr/bin/env python3
"""A thin sheen of the thirteen camps' colours floating across the route map's "Tensing".

    python tools/sherpa_wash.py            # write the block and the markup into the route map
    python tools/sherpa_wash.py --check    # exit 1 if either is missing or stale

Innes, 2026-09-28: "some kind of multicolored ... random pixel color wash or
waves of color that's constantly changing just on the word tensing"; the
first try filled the whole word with two drifting runs of colour. Then: "try
something like that but more of a thinner wave sheen that floats across".
So the word keeps its grey (--tensing), and a narrow, soft-edged, slanted
streak of the camps' colours, packed tight like light through a prism,
floats across it, rests off the word, and comes round again.

THE COLOURS are the camps' own, read from the map's camp markers
(<g class="camp-dot" data-color=... data-href="sherpa-tensing-camp-N-...">),
so a camp recoloured on the map is recoloured in the sheen on the next run.
Each is darkened in OKLCh, same hue and chroma, only as far as FLOOR on the
paper: "Tensing" is display type and must be seen while the streak crosses
it, as its grey must. The floor holds between the stops too: gradients and
the soft edges over the grey mix in sRGB, and a mix of two colours in gamma
space is never lighter than the lighter of them (each channel's x^2.2 is
convex). tools/check_route_map.py measures every token.

THE MOTION: the streak sits in the middle of a background three words wide,
not repeated, and background-position carries it from off the word's left
to off its right, eased, in SWEEP of every LOOP seconds; the rest of the loop
it waits outside the word. Only background-position animates, over a
word-sized box. prefers-reduced-motion leaves it outside: plain grey.

THE SHADOW is a filter: a text-shadow is painted over a background clipped
to the text and would darken it; a drop-shadow is cast by the painted
letters. Same halo and ink shadow as "Sherpa".

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
WIDE = 3            # the background is this many words wide; the streak sits in its middle
BAND = (44, 56)     # the streak's colours, in % of that background (~2/5 of the word)
FEATHER = 2.5       # % of soft edge either side
ANGLE = 105         # deg: a slant, as light falls
LOOP = 8            # seconds from one pass to the next
SWEEP = 0.62        # the part of the loop spent crossing


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


def streak(n):
    a, b = BAND
    stops = ['transparent %.1f%%' % (a - FEATHER)]
    stops += ['var(--wash-%d) %.2f%%' % (i + 1, a + (b - a) * i / (n - 1)) for i in range(n)]
    stops += ['transparent %.1f%%' % (b + FEATHER)]
    return 'linear-gradient(%ddeg,%s)' % (ANGLE, ','.join(stops))


def block(src):
    ground = paper(src)
    wash = [hold(c, ground) for c in camp_colours(src)]
    ink = 'color-mix(in srgb,var(--ink) %d%%,transparent)'
    css = [
        '/* "Tensing": a thin sheen of the thirteen camps\' colours floats across its grey',
        '   (tools/sherpa_wash.py); each colour darkened to %.1f:1 on the paper */' % FLOOR,
        ':root{%s}' % ' '.join('--wash-%d:%s;' % (i + 1, c) for i, c in enumerate(wash)),
        '.wordmark .brand .wash{font-style:normal;}',
        '@supports ((-webkit-background-clip:text) or (background-clip:text)){',
        '  .wordmark .brand .wash{display:inline-block;padding:0 .04em .1em;margin:0 -.04em -.1em;color:transparent;',
        '    text-shadow:none;-webkit-background-clip:text;background-clip:text;',
        '    background-image:%s,linear-gradient(var(--tensing),var(--tensing));' % streak(len(wash)),
        '    background-size:%d00%% 100%%,100%% 100%%;background-repeat:no-repeat;' % WIDE,
        '    filter:drop-shadow(0 0 1px var(--paper)) drop-shadow(0 2px 1.5px %s) drop-shadow(0 8px 10px %s);'
        % (ink % 42, ink % 34),
        '    animation:st-sheen %ds cubic-bezier(.45,.05,.55,.95) infinite;}' % LOOP,
        '}',
        # 100%: the streak is off the word's left; 0%: off its right. Then it waits.
        '@keyframes st-sheen{0%%{background-position:100%% 0,0 0}%d%%,100%%{background-position:0%% 0,0 0}}'
        % round(SWEEP * 100),
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
            bad.append('sheen block or markup missing or stale')
        print('PASS: "Tensing" carries a sheen of %d camp colours, each >= %.1f:1' % (len(wash), FLOOR) if not bad
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
