# -*- coding: utf-8 -*-
"""Add (or replace) translated blocks in a builder's i18n module from JSON.

    py -X utf8 lesson-template/build/i18n_from_json.py <module> <json-dir>
                                                        [--builder <file>]

    <module>    the i18n module's stem, e.g. i18n_ieltslisten_s3
    <json-dir>  holds fr.json, it.json, pt.json, ru.json, ar.json, zh.json,
                ja.json — one flat {key: string} object each, the same keys
                as T['en'] (data-derived keys included)
    --builder   the matching build_*.py; its langs=('en', 'de', 'es') is
                switched to langs=LANGS and the import added

Each JSON file becomes a `T['xx'] = dict(...)` block in the shape Section 2
(`i18n_ieltslisten_s2.py`) uses — adjacent string literals wrapped at ~66
columns — inserted before `def render`. `ielts_langs.TAIL_MORE` is wired in
if the module lacks it, and the docstring's "English, German and Spanish"
line is brought up to date. A re-run replaces the generated blocks (from the
French marker to `def render`), so a wording fix is: edit the JSON, re-run,
rebuild. A module with a hand-written block for one of these seven refuses.

Why JSON and not the Python by hand: a translator (human or model) writes
plain strings with no quote-escaping to get wrong, and the key check against
English runs before anything is written. Used for the three Listening decks
(Section 3, Section 4, the drills) on 2026-10-05; the JSON sources were
scratch files, the module is the source of truth.
"""
import importlib
import io
import json
import os
import re
import sys

BUILD = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BUILD)

NAMES = {'fr': 'French', 'it': 'Italian', 'pt': 'Portuguese', 'ru': 'Russian',
         'ar': 'Arabic', 'zh': 'Chinese', 'ja': 'Japanese'}
ORDER = ('fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja')
SAME_OK = ('chipLevel', 'chipFocus', 'actPlaceholder')   # legitimately English


def chunks(s, width=66):
    words = s.split(' ')
    out, cur = [], ''
    for w in words:
        cand = (cur + ' ' + w) if cur else w
        if len(cand) > width and cur:
            out.append(cur + ' ')
            cur = w
        else:
            cur = cand
    out.append(cur)
    return out


def block(code, d, order):
    bar = '─' * (70 - len(NAMES[code]) - 6)
    lines = ['# ── %s %s' % (NAMES[code], bar), "T['%s'] = dict(" % code]
    for k in order:
        parts = chunks(d[k])
        lines.append('    %s=%s%s' % (k, repr(parts[0]), ',' if len(parts) == 1 else ''))
        pad = ' ' * (4 + len(k) + 1)
        for i, p in enumerate(parts[1:], 1):
            lines.append('%s%s%s' % (pad, repr(p), ',' if i == len(parts) - 1 else ''))
    lines.append(')')
    return '\n'.join(lines)


def main(argv):
    if len(argv) < 3:
        sys.exit(__doc__)
    modname, jdir = argv[1], argv[2]
    builder = argv[argv.index('--builder') + 1] if '--builder' in argv else None

    mod = importlib.import_module(modname)
    en = mod.T['en']
    order = list(en)
    path = os.path.join(BUILD, modname + '.py')
    src = io.open(path, encoding='utf-8').read()

    first = src.find('\n# ── French ')
    if first != -1:
        end = src.find('\n\ndef render(code):')
        assert end > first, 'generated blocks are not followed by def render'
        # keep PEP 8's two blank lines before `def render`, so a re-run with
        # the same JSON reproduces the module byte for byte
        src = src[:first].rstrip('\n') + '\n' + src[end:]
        print('  replacing the generated fr..ja blocks')
    else:
        for code in ORDER:
            if "T['%s'] = dict(" % code in src:
                sys.exit('%s has a hand-written T[%r]; refusing' % (modname, code))

    blocks = []
    for code in ORDER:
        with io.open(os.path.join(jdir, code + '.json'), encoding='utf-8') as f:
            d = json.load(f)
        missing, extra = set(en) - set(d), set(d) - set(en)
        if missing or extra:
            sys.exit('%s: MISSING %s EXTRA %s' % (code, sorted(missing), sorted(extra)))
        same = [k for k in order if d[k] == en[k] and k not in SAME_OK]
        if same:
            print('  note %s identical to English: %s' % (code, same))
        blocks.append(block(code, d, order))

    marker = '\n\ndef render(code):'
    assert src.count(marker) == 1, 'def render anchor'
    src = src.replace(marker, '\n\n' + '\n\n'.join(blocks) + marker)

    if 'TAIL_MORE' not in src:
        anchor = 'from chrome_i18n import CHROME\n'
        assert anchor in src, 'CHROME import anchor'
        src = src.replace(anchor, anchor + 'from ielts_langs import TAIL_MORE\n', 1)
        src, n = re.subn(r'(\nTAIL = \{.*?\n\}\n)', r'\1TAIL.update(TAIL_MORE)\n', src,
                         count=1, flags=re.S)
        assert n == 1, 'TAIL dict anchor'

    old_doc = 'English, German and Spanish, teach cards in the six-item form.'
    if old_doc in src:
        src = src.replace(old_doc, (
            'All ten IELTS languages (`ielts_langs.LANGS`), teach cards in the\n'
            'six-item form. English, German and Spanish from the start; French,\n'
            'Italian, Portuguese, Russian, Arabic, Chinese and Japanese added by\n'
            '`i18n_from_json.py` (conventions in `ielts_langs.py`).'), 1)

    with io.open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(src)
    print('wrote', os.path.relpath(path))

    if builder:
        bpath = builder if os.path.isabs(builder) else os.path.join(BUILD, os.path.basename(builder))
        b = io.open(bpath, encoding='utf-8').read()
        if "langs=('en', 'de', 'es')" in b:
            b = b.replace("langs=('en', 'de', 'es')", 'langs=LANGS', 1)
            if 'from ielts_langs import LANGS' not in b:
                b = b.replace('import deck as D\n', 'import deck as D\nfrom ielts_langs import LANGS\n', 1)
            with io.open(bpath, 'w', encoding='utf-8', newline='\n') as f:
                f.write(b)
            print('wrote', os.path.relpath(bpath), '(langs=LANGS)')
        else:
            print('builder untouched (already on LANGS, or no langs=(en, de, es) to switch)')


if __name__ == '__main__':
    main(sys.argv)
