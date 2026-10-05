#!/usr/bin/env python3
"""Check one translation file without building the page.

    py lesson-template/build/sherpa-climb/check_lang.py de                  # The Climb: i18n/de.json
    py lesson-template/build/sherpa-climb/check_lang.py --game descent de   # The Descent: i18n-descent/de.json
                                                                             # over the climb's i18n/de.json

Reads the game's strings.json (written by build.py: every English string and a
note on where it is used) and the game's <lang>.json, and prints what build.py
would refuse: missing strings, stale keys, and the problems() it checks (a CAPS
token lost, a {placeholder} changed, an odd number of ** marks). Exit 1 on any.

The Descent inherits: a string whose English is the same as one of the climb's
takes the climb's translation (i18n/<lang>.json), and i18n-descent/<lang>.json
holds only the rest (and wins where both have it). Stale keys are counted in
the descent's own file only.

It writes nothing, so several translators can run it at once; build.py itself
rewrites the page, and two of those at once would race.
"""
import io
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build  # noqa: E402  (build.py runs nothing on import)

DIRS = {'climb': ('i18n', None), 'descent': ('i18n-descent', 'i18n')}


def load(rel, lang):
    p = os.path.join(HERE, rel, lang + '.json')
    if not os.path.exists(p):
        return {}
    return json.load(io.open(p, encoding='utf-8'))


def main():
    args = sys.argv[1:]
    game = 'climb'
    if '--game' in args:
        i = args.index('--game')
        game = args[i + 1]
        del args[i:i + 2]
    if game not in DIRS or len(args) != 1 or args[0] not in build.LANGS:
        raise SystemExit('usage: check_lang.py [--game climb|descent] <%s>' % '|'.join(build.LANGS))
    lang = args[0]
    own_dir, parent_dir = DIRS[game]
    en = json.load(io.open(os.path.join(HERE, own_dir, 'strings.json'), encoding='utf-8'))
    own = load(own_dir, lang)
    merged = dict(load(parent_dir, lang)) if parent_dir else {}
    merged.update(own)
    have = {k: v for k, v in merged.items() if isinstance(v, str) and v.strip()}
    missing = [s for s in en if s not in have]
    stale = [k for k in own if k not in en]
    inherited = [s for s in en if s not in own and s in have]
    bad = []
    for s in en:
        if s in have:
            bad += ['%r: %s' % (s[:70], b) for b in build.problems(s, have[s])]
    out = sys.stdout
    for s in missing:
        out.write('missing: %s\n' % s[:90].encode('ascii', 'backslashreplace').decode())
    for k in stale:
        out.write('stale key (not an English string the page uses): %s\n' % k[:90].encode('ascii', 'backslashreplace').decode())
    for b in bad:
        out.write('problem: %s\n' % b.encode('ascii', 'backslashreplace').decode())
    ok = not (missing or stale or bad)
    out.write('%s: %s %s %d/%d translated (%d inherited from %s), %d stale, %d problem(s)\n' % (
        'PASS' if ok else 'FAIL', game, lang, len(en) - len(missing), len(en), len(inherited),
        parent_dir or '-', len(stale), len(bad)))
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
