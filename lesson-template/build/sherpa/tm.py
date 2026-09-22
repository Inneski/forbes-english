# -*- coding: utf-8 -*-
"""Translation memory across the Sherpa i18n files.

    py lesson-template/build/sherpa/tm.py todo <slug>     # strings with no memory hit
    py lesson-template/build/sherpa/tm.py fill <slug> <draft.json>
        merge a draft {de:{key:..}, es:{key:..}, en:{..}, chips, quiz} with
        memory hits and write sherpa/i18n/<slug>.json

The family repeats itself: the nine descents share four fifths of their
prose, every camp says "When to use it", "Conjugation chart" and "Three
mistakes worth naming". An English string that already has a German and a
Spanish in a finished file is reused verbatim; only the rest is written.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build_sherpa as B   # noqa: E402

AUTHORED = ['coverSub', 'actTitle', 'actUse', 'actSpeakBrief', 'actSpeak1', 'actSpeak2',
            'actSpeak3', 'actWriteKind', 'actWriteBrief', 'actPlaceholder']


def memory():
    mem = {'de': {}, 'es': {}}
    for slug in B.slugs():
        p = os.path.join(B.I18N, slug + '.json')
        if not os.path.exists(p):
            continue
        A = json.load(open(p, encoding='utf-8'))
        c = json.load(open(os.path.join(B.CONTENT, slug + '.json'), encoding='utf-8'))
        EN = B.en_strings(c)
        EN.update(A.get('en', {}))
        for lang in ('de', 'es'):
            for k, v in A.get(lang, {}).items():
                if k in EN and EN[k] and k not in AUTHORED and k != 'chipCount':
                    mem[lang].setdefault(EN[k], v)
    return mem


def strings(slug):
    c = json.load(open(os.path.join(B.CONTENT, slug + '.json'), encoding='utf-8'))
    EN = B.en_strings(c)
    return {k: v for k, v in EN.items() if k not in AUTHORED and k != 'chipCount'}


def todo(slug):
    mem = memory()
    EN = strings(slug)
    out = {k: v for k, v in EN.items() if (v not in mem['de'] or v not in mem['es'])
           and not (re.search(r'_ch\d+t\d+c\d+$', k) and (v.strip().startswith('"') or not re.search(r'[a-z]{3,} [a-z]{3,} [a-z]{3,}', re.sub(r'<[^>]+>', '', v))))}
    print('%s: %d of %d strings need writing' % (slug, len(out), len(EN)))
    for k, v in out.items():
        print('%s\t%s' % (k, v))


def fill(slug, draft_path):
    mem = memory()
    EN = strings(slug)
    D = json.load(open(draft_path, encoding='utf-8'))
    out = {'chips': D['chips'], 'quiz': D.get('quiz', {}), 'en': D['en']}
    for lang in ('de', 'es'):
        blk = {}
        for k, v in EN.items():
            if k in D.get(lang, {}):
                blk[k] = D[lang][k]
            elif v in mem[lang]:
                blk[k] = mem[lang][v]
            elif re.search(r'_ch\d+t\d+c\d+$', k) or v.strip().startswith('"'):
                blk[k] = v          # an English form or example cell stays English
            else:
                raise SystemExit('%s.%s has no draft and no memory: %s' % (lang, k, v[:60]))
        for k in AUTHORED:
            blk[k] = D[lang][k]
        out[lang] = blk
    p = os.path.join(B.I18N, slug + '.json')
    json.dump(out, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print('wrote', p)


if __name__ == '__main__':
    if sys.argv[1] == 'todo':
        todo(sys.argv[2])
    else:
        fill(sys.argv[2], sys.argv[3])
