# -*- coding: utf-8 -*-
"""Write the per-page work manifest an authoring agent translates from.

    py lesson-template/build/sherpa/manifest.py            # all
    py lesson-template/build/sherpa/manifest.py camp-03    # one

Output: sherpa/work/<slug>.manifest.json —
  strings   every translatable English string, keyed as the builder keys it
  authored  the keys the agent must WRITE in English as well (cover line,
            activation stage): their value here is a hint, not text
  quiz_fix  the multiple-choice items whose key is the longest option, with
            the lengths, so the agent can lengthen the distractors
  signals   the page's signal words, to pick activation chips from
  reference the old page's own translations where it had any (camps one and
            two carried eight languages), for terminology
"""
import html
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
import build_sherpa as B   # noqa: E402

WORK = os.path.join(HERE, 'work')
AUTHORED = ['coverSub', 'actTitle', 'actUse', 'actSpeakBrief', 'actSpeak1', 'actSpeak2',
            'actSpeak3', 'actWriteKind', 'actWriteBrief', 'actPlaceholder']


def manifest(slug):
    c = json.load(open(os.path.join(B.CONTENT, slug + '.json'), encoding='utf-8'))
    EN = B.en_strings(c)
    strings = {k: v for k, v in EN.items() if k not in AUTHORED and k != 'chipCount'}
    fixes = []
    for n, q in enumerate(c['quiz'], 1):
        L = [len(html.unescape(re.sub(r'<[^>]+>', '', o))) for o in q['options']]
        k = L[q['options'].index(q['correct'])]
        if k == max(L) and L.count(max(L)) == 1 and k - sorted(L)[-2] >= 4:
            fixes.append(dict(n=n, prompt=q['prompt'], hint=q.get('hint'), correct=q['correct'],
                              options=q['options'], lengths=L, explain=q['explain']))
    signals = []
    for s in c['sections']:
        for sg in s.get('signals', []):
            signals.extend(sg['items'])
    m = dict(slug=slug, file=c['file'], kind=c['kind'], level=B.LEVELS[slug],
             title=c['title'], lede=c['hero']['lede'], strings=strings,
             authored={k: EN[k] or '(write this)' for k in AUTHORED},
             quiz_fix=fixes, signals=signals,
             reference={k: v for k, v in (c.get('i18n') or {}).items() if k != 'en'})
    os.makedirs(WORK, exist_ok=True)
    p = os.path.join(WORK, slug + '.manifest.json')
    json.dump(m, open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
    print('%-16s %3d strings, %2d quiz fixes' % (slug, len(strings), len(fixes)))


if __name__ == '__main__':
    for slug in (sys.argv[1:] or B.slugs()):
        manifest(slug)
