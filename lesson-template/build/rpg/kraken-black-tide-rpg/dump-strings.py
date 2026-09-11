#!/usr/bin/env python3
"""Every English string this lesson has to gloss, in one list.

    py lesson-template/build/rpg/kraken-black-tide-rpg/dump-strings.py

Prints them one per line and writes strings.json beside this file.

HANDOFF-rpg.md §5 step 2: build the spec and collect every dict with an `en`
key. That is the only list that matches what `validate()` will refuse on — a
briefing card's head, a route button, a cover chip and the HUD labels are all
learner-facing and none of them is in `check_translations.py`'s TEXT_KEYS,
which reads an extracted data.json rather than an assembled spec.

Answer options are collected too but marked, because they are the English
being taught and this lesson does not gloss them (rpg/README.md §1, and
HOUSE-STYLE §8: never translate the target language).
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, BUILD)

import build_kraken_black_tide as B  # noqa: E402


def main():
    spec = B.build()
    opts = set()
    for s in spec['scenes'].values():
        for o in s.get('opts', []):
            if 'en' in o:
                opts.add(o['en'])

    found = []
    seen = set()

    def walk(o):
        if isinstance(o, dict):
            if isinstance(o.get('en'), str):
                v = o['en'].strip()
                if v and v not in seen:
                    seen.add(v)
                    found.append(v)
                return
            for v in o.values():
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    walk(spec['scenes'])
    walk(spec.get('labels', {}))
    walk(spec.get('tags', {}))

    need = [s for s in found if s not in opts]
    dest = os.path.join(HERE, 'strings.json')
    with open(dest, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(need, f, ensure_ascii=False, indent=1)
        f.write('\n')
    for s in need:
        print(s)
    print('\n%d strings to gloss (%d answer options skipped) -> strings.json'
          % (len(need), len(opts)), file=sys.stderr)


if __name__ == '__main__':
    main()
