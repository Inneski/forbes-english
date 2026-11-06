# -*- coding: utf-8 -*-
"""Build a house style 2 deck from a content spec. 2026-11-06.

Written after the third HS2 conversion repeated the same forty lines (cover,
bubbles, art per block, key dealing, recap, results, activation, palette).
A lesson builder now holds only what the lesson IS — its items, its rules,
its translations — and calls build(SPEC, T, GLOSS). HOUSE-STYLE.md §16 is
the look; deck.py is still where every slide shape lives.

SPEC
  out, title, folder, scheme      the page, its <title>, its picture folder,
                                  the stand-in colour scheme
  art   {slot: (motif, brief)}    every picture the deck needs; real plates
                                  in <folder>/<slot>.jpg win over stand-ins
  hero  'hero'                    which slot is the cover (default 'hero')
  flow  [step, ...]               the slides between cover and results:
     ('talk', eyebrow_key, title_key, [prompt_html, ...], slot|None, cols)
     ('rules', eyebrow_key, title_key, [(pill, [bullet_key, ...] | [(None, html)], example_html|None)], slot|None)
     ('mc', eyebrow_key, title_key, [item, ...], slot|None, side)
          item: dict(stem, options, correct, why=<key>, ctx=<key>?, gl=<gloss key>?)
     ('gap', eyebrow_key, title_key, hint_key, [(sentence, [answers], why_key), ...], [bank]?)
     ('order', eyebrow_key, title_key, hint_key, [(pieces, decoys, why_key), ...], slot|None, side)
     ('survey', eyebrow_key, title_key, hint_key, question_html, [(text, n), ...], slot|None, side)
     ('raw', html)
  chips [str]                     the activation's target-language strip
  act   slot                      the activation's picture (default 'act')
  langs                           default ('en', 'de', 'es')

T      {lang: {key: str}}         every UI_I18N string; the chrome is added
GLOSS  {lang: {key: html}}        optional: click-to-reveal translations of
                                  English stems (the template's .gloss), for
                                  the pages that were written with L1 support

Required keys in T: coverTitle coverSub chipLevel chipFocus chipCount
actTitle actUse actSpeakBrief actSpeak1-3 actWriteKind actWriteBrief
actPlaceholder, plus every key the flow names.
"""
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..', '..', 'tools'))
import deck as D  # noqa: E402
import make_standin  # noqa: E402
from chrome_i18n import CHROME  # noqa: E402

TPL = 'lesson-template/lesson-template.html'

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'actSpeakWord', 'actWriteWord']

GLOSS_UI = {'en': dict(glossShow='Translate', glossHide='Hide translation'),
            'de': dict(glossShow='Übersetzen', glossHide='Übersetzung ausblenden'),
            'es': dict(glossShow='Traducir', glossHide='Ocultar traducción')}

# Where the key sits in the SOURCE. The engine shuffles on screen, but the
# KEYS gate reads the source, and question banks are written with the key
# at B far more often than chance. A swap, nothing else moves.
DEAL = [2, 0, 3, 1, 0, 2, 1, 3, 2, 0, 1, 3, 0, 2, 3, 1]


def _deal(it, n):
    o = list(it['options'])
    t = DEAL[n % len(DEAL)] % len(o)
    c = it['correct']
    o[c], o[t] = o[t], o[c]
    return dict(it, options=o, correct=t)


# The label in front of a gap slide's word bank. Supplied here so a lesson
# that uses a bank cannot ship without it (check-lesson's I18N gate).
BANK_UI = {'en': 'Word bank:', 'de': 'Wortliste:', 'es': 'Banco de palabras:',
           'it': 'Parole:', 'ja': '語群：', 'fr': 'Banque de mots :', 'pt': 'Banco de palavras:'}


class _I18n:
    def __init__(self, T, langs, gloss):
        self.T = {c: dict(T[c], **(GLOSS_UI[c] if gloss else {})) for c in langs}
        for c in langs:
            self.T[c].setdefault('bankLabel', BANK_UI[c])

    def render(self, code):
        d = dict(self.T[code])
        for k in LIFT:
            d[k] = CHROME[code][k]
        rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
                for k in sorted(d)]
        return '{\n' + ',\n'.join(rows) + '\n  }'


def _palette(path):
    """extract-palette.py --paper on the hero, in-process. Fails the build
    on any contrast row that does not pass — §4, mechanically."""
    spec = importlib.util.spec_from_file_location(
        'xpal', os.path.join(HERE, '..', 'extract-palette.py'))
    X = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(X)
    p = X.build_palette(path, dark=False, paper=True)
    rows = [('text', 'surface', 4.5), ('text', 'void', 4.5), ('text-dim', 'surface', 4.5),
            ('accent', 'surface', 4.5), ('accent-bright', 'surface', 4.5),
            ('contrast', 'surface', 4.5), ('border', 'surface', 1.25),
            ('accent-bright', 'text', 1.45)]
    bad = ['%s on %s %.2f' % (a, b, X.contrast_ratio(p[a], p[b])) for a, b, m in rows
           if X.contrast_ratio(p[a], p[b]) < m]
    assert not bad, 'palette from %s fails: %s' % (path, '; '.join(bad))
    order = ['void', 'surface', 'surface2', 'border', 'text', 'text-dim', 'accent',
             'accent-bright', 'accent-dim', 'secondary', 'contrast']
    return '\n'.join('  --%-14s: %s;' % (k, X.hex_of(p[k])) for k in order)


def _hero_card(folder, slot):
    """The picture the palette is derived from: the real hero if it is on
    disk, else the stand-in's card."""
    for ext in ('.jpg', '.jpeg', '.png', '.webp'):
        if os.path.exists(os.path.join(folder, slot + ext)):
            return os.path.join(folder, slot + ext)
    return os.path.join(folder, 'standin-%s.jpg' % slot)


def build(SPEC, T, GLOSS=None):
    F = SPEC['folder']
    langs = SPEC.get('langs', ('en', 'de', 'es'))
    hero = SPEC.get('hero', 'hero')
    act = SPEC.get('act', 'act')
    E = T['en']
    # Stand-ins only for slots with no real plate on disk; a real plate needs
    # no brief and no placeholder beside it.
    missing = {k: v for k, v in SPEC['art'].items()
               if not any(os.path.exists(os.path.join(F, k + e)) for e in ('.jpg', '.jpeg', '.png', '.webp'))}
    if missing:
        make_standin.ensure(F, missing, scheme=SPEC.get('scheme', 'warm'), deck=SPEC['out'])

    cover, hero_ref = D.hs2_cover(D.logo_from(TPL), E['coverTitle'], E['coverSub'],
                                  [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                                   ('Count', E['chipCount'])], F, slot=hero)
    s = [cover]
    dealt = 0

    def put(html, slot, side=None, shape=None):
        return D.art(html, F, slot, side=side, shape=shape) if slot else html

    for step in SPEC['flow']:
        kind = step[0]
        if kind == 'talk':
            _, ek, tk, prompts, slot, cols = step
            s.append(put(D.bubbles(ek, E[ek], tk, E[tk], [(None, p) for p in prompts], cols=cols), slot))
        elif kind == 'rules':
            _, ek, tk, cards, slot = step
            built = []
            for pill, bullets, ex in cards:
                bl = [b if isinstance(b, tuple) else (b, E[b]) for b in bullets]
                pl = (pill, E[pill]) if isinstance(pill, str) and pill in E else pill
                built.append((pl, bl, ex))
            s.append(put(D.rules(ek, E[ek], tk, E[tk], built), slot))
        elif kind == 'mc':
            _, ek, tk, items, slot, side = step
            items = [_deal(it, dealt + i) for i, it in enumerate(items)]
            dealt += len(items)
            D.assert_no_key_is_longest(items, SPEC['out'])
            for i, it in enumerate(items, 1):
                sl = D.mc(i, len(items), it, ek, E[ek], tk, E[tk],
                          ctx=E[it['ctx']] if it.get('ctx') else None, ctx_key=it.get('ctx'))
                if it.get('gl'):
                    sl = sl.replace('<p class="q-stem"', '<p class="q-stem gloss" data-tr="%s"' % it['gl'], 1)
                # A long stem takes the full width: beside a picture it wraps
                # and the answered explanation runs off the canvas.
                long_ = (len(re.sub(r'<[^>]+>', '', it['stem'])) > 92
                         or max(len(re.sub(r'<[^>]+>', '', o)) for o in it['options']) > 58)
                s.append(sl if long_ or it.get('wide') else put(sl, slot, side))
        elif kind == 'gap':
            # An optional sixth element is a word bank; deck.gap() refuses
            # one that lists the answers in gap order.
            _, ek, tk, hk, rows = step[:5]
            bank = step[5] if len(step) > 5 else None
            if bank:
                D.assert_bank_is_not_a_key(bank, [a for _, ans, _ in rows for a in ans])
            s.append(D.gap(1, 1, rows, bank, ek, E[ek], tk, E[tk], hint=E[hk], hint_key=hk, size=21))
        elif kind == 'order':
            _, ek, tk, hk, rows, slot, side = step
            for pieces, decoys, why in rows:
                s.append(put(D.order(pieces, ek, E[ek], tk, E[tk], hk, E[hk], why, decoys=decoys),
                             slot, side))
        elif kind == 'survey':
            _, ek, tk, hk, q, answers, slot, side = step
            s.append(put(D.survey(ek, E[ek], tk, E[tk], None, q, answers, hint=(hk, E[hk])), slot, side))
        elif kind == 'raw':
            s.append(step[1])
        else:
            raise AssertionError('unknown step %r' % kind)

    s.append(D.results())
    s.append(put(D.activate(E['actTitle'], E['actUse'], SPEC['chips'], 'Speaking', E['actSpeakBrief'],
                            [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                            E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder']), act))
    body = ''.join(s)
    n = body.count('<section class="slide')
    for c in langs:
        assert str(n) in T[c]['chipCount'], '%s chipCount says %r; the deck has %d slides' % (
            c, T[c]['chipCount'], n)

    pal = "  --hero: url('%s');\n%s" % (hero_ref, _palette(_hero_card(F, hero)))
    mod = _I18n(T, langs, bool(GLOSS))
    out = D.assemble(TPL, SPEC['out'], body, pal, SPEC['title'], mod, langs=langs, style='hs2')
    if GLOSS:
        tr = 'const NARRATIVE_TR = ' + json.dumps({c: GLOSS[c] for c in langs if c in GLOSS},
                                                  ensure_ascii=False, indent=1) + ';\n'
        out = out.replace('const UI_I18N = {', tr + 'const UI_I18N = {', 1)
        open(SPEC['out'], 'w', encoding='utf-8', newline='').write(out)
    print('wrote %s — %d slides' % (SPEC['out'], n))
    return out


def check_keys(T, langs=('en', 'de', 'es')):
    base = set(T['en'])
    for c in langs:
        m, x = base - set(T[c]), set(T[c]) - base
        assert not m and not x, '%s: missing %s extra %s' % (c, sorted(m), sorted(x))
