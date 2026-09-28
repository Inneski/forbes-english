#!/usr/bin/env python3
"""The Sherpa lesson pages' text arrives, as the route map's does.

    python tools/sherpa_arrive.py            # write the block into every lesson page
    python tools/sherpa_arrive.py --check    # exit 1 if a page lacks it or has a stale copy

Innes, 2026-09-28, on the route map: "some kind of effect for the text to
arrive/fly onto the page", then "ok do it" to the same on the lesson pages.
On load "Sherpa" glides in from the left out of a blur, "Tensing" follows
from the right, the hero's lines (eyebrow, title, paragraph, globe) rise in
one after another, and the hero diagram fades up last. Transform, opacity
and filter only, once. Off under prefers-reduced-motion.

The route map carries its own copy in its hand-kept CSS; this is the lesson
pages' fenced block (SHERPA-ARRIVE), rewritten in place, inserted before
</head> only when absent.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = '<!-- SHERPA-ARRIVE:start -->', '<!-- SHERPA-ARRIVE:end -->'
FENCE = re.compile(re.escape(START) + r'.*?' + re.escape(END) + r'\n?', re.S)
EASE = 'cubic-bezier(.2,.8,.2,1)'
CSS = '\n'.join([
    '/* arrival (tools/sherpa_arrive.py): the name flies in, the hero rises, once */',
    '@keyframes st-in-left{from{opacity:0;transform:translateX(-48px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}',
    '@keyframes st-in-right{from{opacity:0;transform:translateX(64px);filter:blur(6px)}to{opacity:1;transform:none;filter:none}}',
    '@keyframes st-rise{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}',
    '@keyframes st-fade{from{opacity:0;transform:scale(.97)}to{opacity:1;transform:none}}',
    '.wordmark .brand{animation:st-in-left .9s %s both;}' % EASE,
    '.wordmark .brand span{display:inline-block;animation:st-in-right .9s %s .28s both;}' % EASE,
    '.hero > div:first-child > *{animation:st-rise .8s %s both;}' % EASE,
    '.hero > div:first-child > :nth-child(1){animation-delay:.45s}'
    '.hero > div:first-child > :nth-child(2){animation-delay:.55s}'
    '.hero > div:first-child > :nth-child(3){animation-delay:.68s}'
    '.hero > div:first-child > :nth-child(n+4){animation-delay:.8s}',
    '.hero > :not(:first-child){animation:st-fade 1s %s .75s both;}' % EASE,
    '@media (prefers-reduced-motion:reduce){.wordmark .brand,.wordmark .brand span,'
    '.hero > div:first-child > *,.hero > :not(:first-child){animation:none;}}',
])
BLOCK = START + '\n<style id="sherpa-arrive">\n' + CSS + '\n</style>\n' + END + '\n'


def pages():
    return sorted(p for p in glob.glob(os.path.join(ROOT, 'sherpa-tensing-*.html'))
                  if not p.endswith('sherpa-tensing-route-map.html'))


def main():
    check = '--check' in sys.argv
    bad = []
    for p in pages():
        name = os.path.basename(p)
        src = io.open(p, encoding='utf-8').read()
        if '<section class="hero"' not in src or '<div class="brand">' not in src:
            bad.append('%s: no hero or wordmark in the expected form' % name)
            continue
        new = FENCE.sub(lambda m: BLOCK, src, count=1) if FENCE.search(src) else src.replace('</head>', BLOCK + '</head>', 1)
        if new != src:
            if check:
                bad.append('%s: arrival block missing or stale' % name)
            else:
                io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
                print('  ' + name)
    for b in bad:
        print('FAIL ' + b)
    if check:
        print('PASS: %d pages arrive' % len(pages()) if not bad else 'FAIL: %d' % len(bad))
    sys.exit(1 if bad else 0)


if __name__ == '__main__':
    main()
