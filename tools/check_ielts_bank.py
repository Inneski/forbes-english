#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A prompt's declared type has to match how it actually ends.

Mis-tagging is invisible on the page — the chip just says the wrong thing —
and it breaks the one filter a candidate uses most: 'show me the type I am
practising'. One mis-tag got in on the first pass of the second expansion.
"""
import re, sys
ENDINGS = {
 'opinion':    [r'to what extent do you agree', r'do you agree or disagree'],
 'discussion': [r'discuss both views and give your own opinion'],
 'outweigh':   [r'outweigh the (dis)?advantages\?', r'outweigh the case against it\?'],
 'measure':    [r'what measures', r'what could be done', r'what problems does this cause'],
 'direct':     [r'why is this', r'why has this', r'why do you think', r'what are the reasons'],
}
def check(topics):
    bad = []
    for t in topics:
        for p, ty in t['prompts']:
            low = p.lower()
            if not any(re.search(pat, low) for pat in ENDINGS[ty]):
                bad.append((t['id'], ty, p))
    return bad


if __name__ == '__main__':
    import os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from ielts_bank_data import TOPICS

    fails = 0
    bad = check(TOPICS)
    print(f"  {len(TOPICS)} topics · {sum(len(t['prompts']) for t in TOPICS)} prompts")
    print(f"  {'PASS' if not bad else 'FAIL'}  every prompt ends in the shape its type claims")
    for tid, ty, p in bad:
        print(f"        [{tid}] tagged {ty}: {p[:90]}")
    fails += bool(bad)

    seen = {}
    for t in TOPICS:
        for p, _ in t['prompts']:
            seen.setdefault(p.strip().lower(), []).append(t['id'])
    dupes = {k: v for k, v in seen.items() if len(v) > 1}
    print(f"  {'PASS' if not dupes else 'FAIL'}  no prompt appears under two topics")
    for k, v in dupes.items():
        print(f"        {v}: {k[:80]}")
    fails += bool(dupes)

    thin = [t['id'] for t in TOPICS if len(t['for']) < 3 or len(t['against']) < 3]
    print(f"  {'PASS' if not thin else 'FAIL'}  every topic argues both ways, three each")
    for tid in thin:
        print(f"        {tid}")
    fails += bool(thin)

    # A topic offering only one or two essay types is a topic a candidate
    # cannot use to practise the type they are weakest at.
    narrow = [(t['id'], len({ty for _, ty in t['prompts']})) for t in TOPICS]
    narrow = [(i, n) for i, n in narrow if n < 4]
    print(f"  {'PASS' if not narrow else 'WARN'}  every topic covers at least four of the five types")
    for i, n in narrow:
        print(f"        {i}: {n} type(s)")

    sys.exit(1 if fails else 0)
