# -*- coding: utf-8 -*-
"""Interface strings for the two B1 Mixed Grammar Tests.

The text lives one language per file (`mixed_b1_<lang>.py`), each defining
AREA, COMMON, P1 and P2, so a language can be written, checked and committed
on its own. This module merges them per part and renders the UI_I18N block.

What translates (HOUSE-STYLE §8): the chrome, the true/false statements (they
are rules ABOUT English, the same as a teach card), the word glosses and every
explanation. What does not: stems, options, story sentences, chunks and the
sentences to correct — the English under test. English examples quoted inside
an explanation stay English in every language.

Each explanation is printed with its grammar area in bold in front of it,
which is where the old page put the badge it showed after answering. Tense
areas also get their route-map colour (§5a) as a dot.

`python i18n_mixed_b1.py` reports key parity for every language on disk.
"""
import importlib
import json
import os
import sys
import types

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
import mixed_b1_data as DATA

LANGS = ('en', 'de', 'es', 'fr', 'it', 'pt')

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'actSpeakKind',
        'btnCopy', 'btnCopied', 'wordCount', 'ledDp', 'ledTime',
        'ledClues', 'actSpeakWord', 'actWriteWord', 'resNext']


def available():
    here = os.path.dirname(os.path.abspath(__file__))
    return tuple(c for c in LANGS
                 if os.path.exists(os.path.join(here, 'mixed_b1_%s.py' % c)))


def _mod(code):
    return importlib.import_module('mixed_b1_%s' % code)


def _areas(part):
    """Which explanation key belongs to which grammar area, for this part."""
    P = DATA.PARTS[part]
    out = {}
    for n, q in enumerate(P['MC'], 1):
        out['x_mc%d' % n] = q['area']
    STORY_AREA = {1: ['presSimple', 'presPerf', 'pastCont', 'presCont', 'cond',
                      'quant'],
                  2: ['presSimple', 'pastSimple', 'presPerf', 'pastCont',
                      'presCont', 'cond']}[part]
    for n, a in enumerate(STORY_AREA, 1):
        out['x_st%d' % n] = a
    for n, q in enumerate(P['TF'], 1):
        out['x_tf%d' % n] = q['area']
    for n, (_, a) in enumerate(P['ORDER'], 1):
        out['x_or%d' % n] = a
    for n, q in enumerate(P['FIX'], 1):
        out['x_fx%d' % n] = q['area']
    return out


def table(code, part):
    m = _mod(code)
    d = dict(m.COMMON)
    d.update(getattr(m, 'P%d' % part))
    for k, area in _areas(part).items():
        dot = ''
        if area in DATA.TENSE_COLOUR:
            dot = '<span class="tdot" style="--tdot:%s"></span>' % DATA.TENSE_COLOUR[area]
        d[k] = '%s<strong>%s.</strong> %s' % (dot, m.AREA[area], d[k])
    return d


def module(part):
    """An object with render(code), which is all deck.assemble() asks for."""
    def render(code):
        d = table(code, part)
        for k in LIFT:
            d[k] = CHROME[code][k]
        return '{\n' + ',\n'.join(
            '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)) + '\n  }'
    return types.SimpleNamespace(render=render, EN=table('en', part))


def check():
    """Every language defines exactly the English keys. Returns problems."""
    en = _mod('en')
    bad = []
    for c in available():
        m = _mod(c)
        for name in ('AREA', 'COMMON', 'P1', 'P2'):
            a, b = set(getattr(en, name)), set(getattr(m, name))
            if a != b:
                bad.append('%s.%s missing %s extra %s'
                           % (c, name, sorted(a - b), sorted(b - a)))
    return bad


if __name__ == '__main__':
    probs = check()
    print('languages on disk:', ', '.join(available()))
    print('\n'.join(probs) or 'key parity OK')
