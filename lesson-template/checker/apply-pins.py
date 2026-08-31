#!/usr/bin/env python3
"""Write Innes's own placement calls into the decks.

pins.json is the record of every slide he has placed by eye. The measurement
in check-placement.py is a default and nothing more: it scores detail, and it
cannot see a SUBJECT - it does not know that a villager outranks a wall. A pin
outranks the measurement, permanently.

Usage: python3 apply-pins.py [deck.html ...]     (default: every blockcamp deck)
"""
import glob, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
PINS = json.load(open(os.path.join(HERE, 'pins.json')))


def sections(text):
    return [m for m in re.finditer(r'<section class="slide[^>]*>', text)
            if 'data-type=' in m.group(0)]


def set_attr(tag, name, value):
    tag = re.sub(r' %s="[^"]*"' % name, '', tag)
    return tag + (f' {name}="{value}"' if value else '')


def main(decks):
    for deck in decks:
        pins = PINS.get(os.path.basename(deck))
        if not pins:
            continue
        src = open(deck, encoding='utf-8').read()
        spans = sections(src)
        edits, done = [], []
        for k, pin in pins.items():
            i = int(k)
            if i > len(spans):
                print(f'  {deck} slide {i}: no such slide'); continue
            m = spans[i - 1]
            tag = m.group(0)[:-1]
            before = tag
            tag = set_attr(tag, 'data-side', pin['side'])
            tag = set_attr(tag, 'data-vpos', '' if pin.get('vpos', 'center') == 'center' else pin['vpos'])
            # An exact offset beats a named step. solve-nudge.py scans every
            # offset the canvas allows and reports the one that puts the block
            # in the negative space; a pin carrying nx/ny uses that number
            # directly instead of rounding to one or two nudges.
            if pin.get('nx') is not None or pin.get('ny') is not None:
                tag = set_attr(tag, 'data-nudge', 'fine')
                bits = []
                if pin.get('nx') is not None: bits.append(f"--nx:{pin['nx']}px")
                if pin.get('ny') is not None: bits.append(f"--ny:{pin['ny']}px")
                tag = set_attr(tag, 'style', ';'.join(bits))
            else:
                tag = set_attr(tag, 'data-nudge', pin.get('nudge', ''))
                tag = re.sub(r' style="--n[xy]:[^"]*"', '', tag)
            if tag != before:
                edits.append((m.start(), m.end(), tag + '>'))
                done.append((i, pin))
        for a, b, new in sorted(edits, reverse=True):
            src = src[:a] + new + src[b:]
        if edits:
            open(deck, 'w', encoding='utf-8').write(src)
        print(f'{os.path.basename(deck)}: {len(done)} pinned')
        for i, pin in sorted(done):
            if pin.get('nx') is not None or pin.get('ny') is not None:
                n = f" {pin.get('nx', 0):+d}px,{pin.get('ny', 0):+d}px"
            else:
                n = f" +{pin['nudge']}" if pin.get('nudge') else ''
            print(f"   slide {i:<3} {pin['side']}/{pin.get('vpos','center')}{n:<12} {pin['why']}")


if __name__ == '__main__':
    main(sys.argv[1:] or sorted(glob.glob('blockcamp-*.html')))
