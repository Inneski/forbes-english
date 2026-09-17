# -*- coding: utf-8 -*-
"""Check the fixed editorial palette still clears AA.

    python3 tools/check-editorial-palette.py

Every other deck derives its palette from its hero and `extract-palette.py`
prints a contrast report as it does so, which is what stops a bad palette
shipping. `data-style="editorial"` deliberately does not derive — it is one
hand-authored set shared by every deck that opts in (see the EDITORIAL STYLE
block in lesson-template.html for why that is the safe direction).

That trade only holds while something still measures it. This is that
something: it reads the constants out of the template and out of deck.py,
checks they agree, and runs the same rows extract-palette.py would.

Exit code is non-zero if any row fails, so it can go in front of a build.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, 'lesson-template', 'lesson-template.html')
DECK = os.path.join(ROOT, 'lesson-template', 'build', 'deck.py')

# name, foreground, background, minimum, what it is for.
# The background is --surface (the card) rather than --void (the field),
# because the card is the tighter of the two: #ffffff against text is a
# smaller gap than the cream field is.
ROWS = [
    ('text on surface',         'text',          'surface', 4.5, 'body copy'),
    ('text on void',            'text',          'void',    4.5, 'body copy on the field'),
    ('text-dim on surface',     'text-dim',      'surface', 4.5, 'card notes, hints'),
    ('accent on surface',       'accent',        'surface', 4.5, 'buttons, rules'),
    ('accent-bright on surface', 'accent-bright', 'surface', 4.5, 'headings'),
    ('contrast on surface',     'contrast',      'surface', 4.5, 'counterpoint'),
    ('border on surface',       'border',        'surface', 1.25, 'hairlines must show'),
    ('text on stamp',           'text',          'stamp',   4.5, 'the rotated badge'),
]


def lum(hexcode):
    c = hexcode.lstrip('#')
    out = []
    for i in (0, 2, 4):
        v = int(c[i:i + 2], 16) / 255.0
        out.append(v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * out[0] + 0.7152 * out[1] + 0.0722 * out[2]


def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def tokens_from_template():
    s = open(TPL, encoding='utf-8').read()
    m = re.search(r'html\[data-style="editorial"\]\s*\{(.*?)\n\}', s, re.S)
    assert m, 'no html[data-style="editorial"] block in the template'
    return dict(re.findall(r'--([a-z-]+)\s*:\s*(#[0-9a-fA-F]{6})', m.group(1)))


def tokens_from_deck():
    s = open(DECK, encoding='utf-8').read()
    m = re.search(r"EDITORIAL_PALETTE = '''(.*?)'''", s, re.S)
    assert m, 'no EDITORIAL_PALETTE in deck.py'
    return dict(re.findall(r'--([a-z-]+)\s*:\s*(#[0-9a-fA-F]{6})', m.group(1)))


def main():
    tpl, deck = tokens_from_template(), tokens_from_deck()

    # The two copies exist because the template styles the page and the
    # builder writes the :root block. They must not drift.
    shared = set(tpl) & set(deck)
    drift = sorted(k for k in shared if tpl[k].lower() != deck[k].lower())
    print('\n  editorial palette — %d token(s) in the template, %d in deck.py\n'
          % (len(tpl), len(deck)))
    if drift:
        for k in drift:
            print('    DRIFT  --%-14s template %s  vs  deck.py %s'
                  % (k, tpl[k], deck[k]))
        print('\n  the template and deck.py disagree; fix before building\n')
        return 1
    print('    OK     the template and deck.py agree on all %d shared token(s)'
          % len(shared))

    missing = [k for _, f, b, _, _ in ROWS for k in (f, b) if k not in tpl]
    if missing:
        print('    MISSING tokens: %s' % sorted(set(missing)))
        return 1

    print()
    bad = 0
    for name, fg, bg, floor, why in ROWS:
        r = ratio(tpl[fg], tpl[bg])
        ok = r >= floor
        bad += not ok
        print('    %-26s %6.2f:1  (min %.2f)  %s   %s'
              % (name, r, floor, 'PASS' if ok else 'FAIL', why))

    print('\n  %s\n' % ('all rows pass' if not bad else '%d row(s) FAILED' % bad))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
