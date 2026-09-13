#!/usr/bin/env python3
"""Measure the twenty-five items for the defects a reader cannot see.

    py lesson-template/build/rpg/kraken-black-tide-rpg/check-items.py [script.json]

A multi-agent audit of the first draft filed 165 findings, and the three that
mattered were all quantities rather than opinions:

  1. **The blend tell.** "Pick the option every one of whose words appears in
     one of the other two" scored 9 of 25 outright. In a three-option minimal
     pair the key is usually the intersection of its distractors' good halves,
     so this is the default state of a carelessly written item, not bad luck.
     An item is clean when the key owns at least one token that appears in
     neither distractor, OR when all three options carry the same multiset of
     words and only the order differs - then the rule names all three and
     discriminates nothing.
  2. **The length tell.** The key was shortest or tied-shortest 15 of 25
     times. `rpg.py`'s own gate never fired on any of it: its thresholds want
     the key 10% AND 4 characters longer than the longest distractor, which no
     real item reaches. The gate here is a flat two characters, in both
     directions, and it is the one HOUSE-STYLE actually describes - ties are
     the target.
  3. **The one-sub-skill tell.** 19 of 25 distractors died to "the word after
     HAVE/HAS is a past participle". A learner who knows only that scores most
     of the game. So every distractor is tagged with the error family it
     belongs to, no family may carry more than 55% of the items on either path
     (the audit asked for a cap of 10 of 18), and no two consecutive items on
     a path may share a family pair.

Exit 0 clean, 1 with findings.
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# the two orders a player can actually meet, which is what the adjacency and
# the family balance have to be measured over - not the file order
PATHS = {
    'REEF+CORRY': ['drift', 'bell', 'provost', 'hoy', 'jar', 'shed',
                   'reef1', 'reef2', 'reef3', 'reef4',
                   'wreck1', 'wreck2', 'wreck3',
                   'corry1', 'corry2', 'corry3', 'barrels', 'last'],
    'CAVES+WATCH': ['drift', 'bell', 'provost', 'hoy', 'jar', 'shed',
                    'cave1', 'cave2', 'cave3', 'cave4',
                    'wreck1', 'wreck2', 'wreck3',
                    'night1', 'night2', 'night3', 'barrels', 'last'],
}

# The error family each distractor belongs to. Kept here rather than in the
# script so the script stays the shape the builder reads.
#   PART  wrong participle form after HAVE/HAS    has took, has taked
#   AUX   wrong auxiliary                         they are not come, do you have called
#   DROP  auxiliary left out                      Quinn just shown me one
#   AGR   subject agreement                       the rope have gone
#   ADV   adverb in the wrong place               has shown me one just
#   PREP  wrong time preposition                  since two weeks, from Tuesday
#   TENSE Past Simple chosen over Present Perfect, or the reverse
#   CONT  continuous chosen over perfect          is fishing for forty years
FAMILIES = {}   # filled from families.json beside this file

WORD_CAPS = {'title': 5, 'act': 6, 'story': 28, 'clue': 16, 'prompt': 13, 'explanation': 25}
OPT_CHARS = 45
CAPS_TOKEN = re.compile(r'\b(HAVE|HAS|HASN|HAVEN|NOT|BEEN|GONE|EVER|NEVER|JUST|ALREADY|YET|SINCE|FOR|AGO|STILL|PAST|SIMPLE|PRESENT|PERFECT|[A-Z]{3,})\b')


def words(s):
    return [w for w in re.findall(r"[A-Za-z']+", s.lower()) if w]


def blend(opts):
    """Which options have every word covered by the union of the others?"""
    sets = [set(words(o)) for o in opts]
    out = []
    for i, s in enumerate(sets):
        others = set().union(*[t for j, t in enumerate(sets) if j != i])
        if s <= others:
            out.append(i)
    return out


def check(scenes):
    bad = []
    S = {s['id']: s for s in scenes}

    for sid, s in S.items():
        opts = [s['correct'], s['wrong1'], s['wrong2']]

        # ── budgets
        for field, cap in WORD_CAPS.items():
            v = s.get(field, '')
            if len(v.split()) > cap:
                bad.append('%-8s %s is %d words, wall %d' % (sid, field, len(v.split()), cap))
        for o in opts:
            if len(o) > OPT_CHARS:
                bad.append('%-8s option %d chars, wall %d: %r' % (sid, len(o), OPT_CHARS, o))
        for k, v in s.items():
            if isinstance(v, str) and re.search(r'[‘’“”]', v):
                bad.append('%-8s %s has a curly quote' % (sid, k))

        # ── length tell: flat two characters, both directions
        kl, o1, o2 = len(opts[0]), len(opts[1]), len(opts[2])
        hi, lo = max(o1, o2), min(o1, o2)
        if kl > hi + 2:
            bad.append('%-8s key is longest by %d chars (%d vs %d/%d)' % (sid, kl - hi, kl, o1, o2))
        if kl < lo - 2:
            bad.append('%-8s key is shortest by %d chars (%d vs %d/%d)' % (sid, lo - kl, kl, o1, o2))

        # ── blend tell
        b = blend(opts)
        if b == [0]:
            bad.append('%-8s BLEND: the key is the only option whose every word is in another' % sid)

        # ── the explanation must name the rule in CAPS (addendum A)
        if not CAPS_TOKEN.search(s.get('explanation', '')):
            bad.append('%-8s explanation has no CAPS grammar token' % sid)

        # ── the clue must not carry the form the prompt asks the learner for
        key_l = ' ' + s['correct'].lower().rstrip('.?') + ' '
        if key_l.strip() and key_l.strip() in (' ' + s.get('clue', '').lower() + ' '):
            bad.append('%-8s the clue contains the key verbatim' % sid)

        # ── families
        fam = FAMILIES.get(sid)
        if not fam or len(fam) != 2:
            bad.append('%-8s no error families declared' % sid)

    # ── per-path balance and adjacency
    for pname, order in PATHS.items():
        tally = collections.Counter()
        for sid in order:
            for f in set(FAMILIES.get(sid, [])):
                tally[f] += 1
        n = len(order)
        for fam, c in tally.most_common():
            # counted in ITEMS, not distractors: an item is "a PART item" if
            # either of its two wrong options is a participle-form error. The
            # audit measured 19 of 25 and asked for a cap of 10 of 18.
            if c > n * 0.55:
                bad.append('%-11s family %s carries %d of %d items (over 55%%)' % (pname, fam, c, n))
        for a, b2 in zip(order, order[1:]):
            fa, fb = set(FAMILIES.get(a, [])), set(FAMILIES.get(b2, []))
            if fa and fa == fb:
                bad.append('%-11s %s and %s are the same family pair back to back (%s)'
                           % (pname, a, b2, '+'.join(sorted(fa))))

    # ── nothing said twice: sentences repeated across scenes
    seen = {}
    for sid, s in S.items():
        for field in ('story', 'clue', 'prompt', 'explanation'):
            for sent in re.split(r'(?<=[.?!])\s+', s.get(field, '')):
                k = re.sub(r'[^a-z ]', '', sent.lower()).strip()
                if len(k.split()) < 5:
                    continue
                if k in seen and seen[k] != sid:
                    bad.append('%-8s repeats %s: %r' % (sid, seen[k], sent[:60]))
                seen[k] = sid
    return bad


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, 'script.json')
    scenes = json.load(open(path, encoding='utf-8'))['scenes']
    fam_path = os.path.join(HERE, 'families.json')
    if os.path.exists(fam_path):
        FAMILIES.update(json.load(open(fam_path, encoding='utf-8')))
    bad = check(scenes)
    tally = collections.Counter(f for v in FAMILIES.values() for f in v)
    print('families: ' + ', '.join('%s %d' % kv for kv in tally.most_common()))
    if bad:
        print('\n'.join(bad))
        print('\n%d findings' % len(bad))
        return 1
    print('%d items clean' % len(scenes))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
