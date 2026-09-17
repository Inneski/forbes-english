#!/usr/bin/env python3
"""Measure the twenty-five items for the defects a reader cannot see.

    py lesson-template/build/rpg/loch-ness-loop-rpg/check-items.py [script.json]

Adapted from rpg/kraken-black-tide-rpg/check-items.py, whose three gates came
out of a 165-finding audit and were each verified failing against a
deliberately broken copy before they were trusted:

  1. **The blend tell.** "Pick the option every one of whose words appears in
     one of the other two" scored 9 of 25 on the Kraken draft. The key must
     own at least one word that appears in neither distractor.
  2. **The length tell.** A flat two-character margin in both directions;
     rpg.py's own gate (10% AND 4 chars) never fires on a real item.
  3. **The one-sub-skill tell.** Every distractor carries an error family;
     no family may carry more than 55% of the items on any path, and no two
     consecutive items on a path may share a family pair.

Two gates are this lesson's own, because it has two kinds of question:

  4. **VOCAB items must not print the key on the panel.** A part name that
     appears in the story, clue or prompt makes the question free — so the
     tokens the key owns (the ones in neither distractor, stopwords aside)
     may not appear anywhere on the panel.
  5. **The convention is kind-specific.** A VOCAB explanation names its
     target in CAPS; a CCQ explanation cites the speech in double quotes.
     A lowercase VOCAB explanation or an uncited CCQ is refused.

Plus the frame: cover lead, briefing cards, route notes and ending text
against their walls, and no briefing card printing a correct option.

Exit 0 clean, 1 with findings.
"""
import collections, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# the four orders a player can actually meet — family balance, adjacency and
# the answer-key deal are all measured over these, never over the file
TRUNK_A = ['shop1', 'shop2', 'shop3', 'shop4', 'shop5', 'shop6']
TRUNK_B = ['pub1', 'pub2', 'pub3']
TRUNK_C = ['back1', 'back2']
BRANCH1 = {'SHORE': ['shore1', 'shore2', 'shore3', 'shore4'],
           'HILL':  ['hill1', 'hill2', 'hill3', 'hill4']}
BRANCH2 = {'CASTLE': ['deep1', 'deep2', 'deep3'],
           'BAY':    ['bay1', 'bay2', 'bay3']}
PATHS = {}
for b1, s1 in BRANCH1.items():
    for b2, s2 in BRANCH2.items():
        PATHS['%s+%s' % (b1, b2)] = TRUNK_A + s1 + TRUNK_B + s2 + TRUNK_C

# parallel scenes: the same slot on the two branches of a fork
PARALLEL = list(zip(BRANCH1['SHORE'], BRANCH1['HILL'])) + list(zip(BRANCH2['CASTLE'], BRANCH2['BAY']))

KINDS = {'VOCAB', 'CCQ'}
FAMILIES_FOR = {'VOCAB': {'PART', 'TRANSFER', 'COLLOC'},
                'CCQ': {'NUMBER', 'PARTIAL', 'OPPOSITE', 'INFER'}}
FAMILIES = {}   # filled from families.json beside this file

WORD_CAPS = {'title': 5, 'act': 6, 'story': 28, 'clue': 16, 'prompt': 13, 'explanation': 25}
OPT_CHARS = 45
FRAME_CAPS = {'lead': 35, 'card_text': 12, 'card_head': 6, 'note': 25, 'route_note': 14,
              'route_label': 5, 'ending_text': 45, 'choice_story': 28, 'small': 12}
CAPS_TOKEN = re.compile(r'\b[A-Z][A-Z-]{2,}\b')
CITATION = re.compile(r'"[^"]{3,}"')
STOP = set('a an the to of in on at for by with and or is are it its this that you your be '
           'not no up down off out into over under one two three from as if so than then'.split())


def words(s):
    return [w for w in re.findall(r"[A-Za-z'-]+", s.lower()) if w]


def blend(opts):
    """Which options have every word covered by the union of the others?"""
    sets = [set(words(o)) for o in opts]
    out = []
    for i, s in enumerate(sets):
        others = set().union(*[t for j, t in enumerate(sets) if j != i])
        if s <= others:
            out.append(i)
    return out


def norm(s):
    return re.sub(r'[^a-z ]', '', s.lower()).strip()


def check(src):
    bad = []
    scenes = src['scenes']
    S = {s['id']: s for s in scenes}
    all_ids = sorted(set(sum(PATHS.values(), [])))
    for sid in all_ids:
        if sid not in S:
            bad.append('%-8s missing from script.json' % sid)
    for sid in S:
        if sid not in all_ids:
            bad.append('%-8s is not in the graph' % sid)

    for sid, s in S.items():
        kind = s.get('kind')
        if kind not in KINDS:
            bad.append('%-8s kind must be VOCAB or CCQ, not %r' % (sid, kind))
            continue
        opts = [s.get('correct', ''), s.get('wrong1', ''), s.get('wrong2', '')]
        if not all(opts):
            bad.append('%-8s needs correct, wrong1 and wrong2' % sid)
            continue

        # ── budgets
        for field, cap in WORD_CAPS.items():
            v = s.get(field, '')
            if not v:
                bad.append('%-8s has no %s' % (sid, field))
            elif len(v.split()) > cap:
                bad.append('%-8s %s is %d words, wall %d' % (sid, field, len(v.split()), cap))
        for o in opts:
            if len(o) > OPT_CHARS:
                bad.append('%-8s option %d chars, wall %d: %r' % (sid, len(o), OPT_CHARS, o))
        for k, v in s.items():
            if isinstance(v, str) and re.search(r'[‘’“”]', v):
                bad.append('%-8s %s has a curly quote' % (sid, k))
        if s.get('title') != s.get('title', '').upper():
            bad.append('%-8s title is not in CAPITALS' % sid)
        if s.get('act') != s.get('act', '').upper():
            bad.append('%-8s act kicker is not in CAPITALS' % sid)

        # ── length tell: flat two characters, both directions
        kl, o1, o2 = len(opts[0]), len(opts[1]), len(opts[2])
        hi, lo = max(o1, o2), min(o1, o2)
        if kl > hi + 2:
            bad.append('%-8s key is longest by %d chars (%d vs %d/%d)' % (sid, kl - hi, kl, o1, o2))
        if kl < lo - 2:
            bad.append('%-8s key is shortest by %d chars (%d vs %d/%d)' % (sid, lo - kl, kl, o1, o2))
        if len(set(o.strip().lower() for o in opts)) < 3:
            bad.append('%-8s two options are the same text' % sid)

        # ── blend tell
        if blend(opts) == [0]:
            bad.append('%-8s BLEND: the key is the only option whose every word is in another' % sid)

        # ── the convention, by kind
        expl = s.get('explanation', '')
        if kind == 'VOCAB' and not CAPS_TOKEN.search(expl):
            bad.append('%-8s VOCAB explanation has no CAPS target word' % sid)
        if kind == 'CCQ' and not CITATION.search(expl):
            bad.append('%-8s CCQ explanation cites nothing in double quotes' % sid)

        # ── the key must not be on the panel
        panel = ' '.join(s.get(f, '') for f in ('story', 'clue', 'prompt'))
        panel_words = set(words(panel))
        key_l = norm(opts[0])
        if key_l and key_l in norm(panel):
            bad.append('%-8s the panel contains the key verbatim' % sid)
        if kind == 'VOCAB':
            own = set(words(opts[0])) - set(words(opts[1])) - set(words(opts[2])) - STOP
            leaked = sorted(w for w in own if w in panel_words)
            if leaked:
                bad.append('%-8s VOCAB key word(s) %s appear on the panel' % (sid, ', '.join(leaked)))

        # ── families
        fam = FAMILIES.get(sid)
        if not fam or len(fam) != 2:
            bad.append('%-8s needs two error families in families.json' % sid)
        else:
            for f in fam:
                if f not in FAMILIES_FOR[kind]:
                    bad.append('%-8s family %s is not a %s family' % (sid, f, kind))

    # ── per-path: kind counts, family balance, adjacency
    for pname, order in PATHS.items():
        kinds = collections.Counter(S[sid]['kind'] for sid in order if sid in S)
        if kinds.get('VOCAB') != 9 or kinds.get('CCQ') != 9:
            bad.append('%-11s has %d VOCAB and %d CCQ; the slot table says 9 and 9'
                       % (pname, kinds.get('VOCAB', 0), kinds.get('CCQ', 0)))
        tally = collections.Counter()
        for sid in order:
            for f in set(FAMILIES.get(sid, [])):
                tally[f] += 1
        n = len(order)
        for fam, c in tally.most_common():
            if c > n * 0.55:
                bad.append('%-11s family %s carries %d of %d items (over 55%%)' % (pname, fam, c, n))
        for a, b2 in zip(order, order[1:]):
            fa, fb = set(FAMILIES.get(a, [])), set(FAMILIES.get(b2, []))
            if fa and fa == fb:
                bad.append('%-11s %s and %s are the same family pair back to back (%s)'
                           % (pname, a, b2, '+'.join(sorted(fa))))

    # ── parallel scenes must test the same kind
    for a, b2 in PARALLEL:
        if a in S and b2 in S and S[a]['kind'] != S[b2]['kind']:
            bad.append('%-8s and %s are parallel but %s / %s' % (a, b2, S[a]['kind'], S[b2]['kind']))

    # ── nothing said twice: sentences repeated across scenes
    seen = {}
    for sid, s in S.items():
        for field in ('story', 'clue', 'prompt', 'explanation'):
            for sent in re.split(r'(?<=[.?!])\s+', s.get(field, '')):
                k = norm(sent)
                if len(k.split()) < 5:
                    continue
                if k in seen and seen[k] != sid:
                    bad.append('%-8s repeats %s: %r' % (sid, seen[k], sent[:60]))
                seen[k] = sid

    # ── the frame
    fr = src.get('frame', {})
    cov = fr.get('cover', {})
    if len(cov.get('lead', '').split()) > FRAME_CAPS['lead']:
        bad.append('cover    lead is %d words, wall %d' % (len(cov['lead'].split()), FRAME_CAPS['lead']))
    if len(cov.get('small', '').split()) > FRAME_CAPS['small']:
        bad.append('cover    small line is %d words, wall %d' % (len(cov['small'].split()), FRAME_CAPS['small']))
    if len(cov.get('rules', [])) != 3:
        bad.append('cover    needs exactly three chips')
    br = fr.get('briefing', {})
    keys = {norm(s['correct']) for s in S.values() if s.get('correct')}
    for i, c in enumerate(br.get('cards', [])):
        if len(c.get('text', '').split()) > FRAME_CAPS['card_text']:
            bad.append('card %d   text is %d words, wall %d' % (i + 1, len(c['text'].split()), FRAME_CAPS['card_text']))
        if len(c.get('head', '').split()) > FRAME_CAPS['card_head']:
            bad.append('card %d   head is %d words, wall %d' % (i + 1, len(c['head'].split()), FRAME_CAPS['card_head']))
        for k in keys:
            if k and k in norm(c.get('text', '')):
                bad.append('card %d   prints a correct option: %r' % (i + 1, k))
    if not 2 <= len(br.get('cards', [])) <= 5:
        bad.append('briefing needs two to five cards')
    if len(br.get('note', '').split()) > FRAME_CAPS['note']:
        bad.append('briefing note is %d words, wall %d' % (len(br['note'].split()), FRAME_CAPS['note']))
    for ch in fr.get('choices', []):
        if len(ch.get('story', '').split()) > FRAME_CAPS['choice_story']:
            bad.append('%-8s story is %d words, wall %d' % (ch['id'], len(ch['story'].split()), FRAME_CAPS['choice_story']))
        for r in ch.get('routes', []):
            if len(r.get('note', '').split()) > FRAME_CAPS['route_note']:
                bad.append('%-8s route %s note is %d words, wall %d' % (ch['id'], r['route'], len(r['note'].split()), FRAME_CAPS['route_note']))
            if len(r.get('label', '').split()) > FRAME_CAPS['route_label']:
                bad.append('%-8s route %s label is %d words, wall %d' % (ch['id'], r['route'], len(r['label'].split()), FRAME_CAPS['route_label']))
            if r.get('route') != r.get('route', '').upper() or r.get('label') != r.get('label', '').upper():
                bad.append('%-8s route names and labels are CAPITALS' % ch['id'])
    for e in fr.get('endings', []):
        if len(e.get('text', '').split()) > FRAME_CAPS['ending_text']:
            bad.append('end_%-6s text is %d words, wall %d' % (e['key'], len(e['text'].split()), FRAME_CAPS['ending_text']))
        if e.get('title') != e.get('title', '').upper() or e.get('label') != e.get('label', '').upper():
            bad.append('end_%-6s label and title are CAPITALS' % e['key'])
    for blob in json.dumps(fr, ensure_ascii=False),:
        if re.search(r'[‘’“”]', blob):
            bad.append('frame    has a curly quote somewhere')
    return bad


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, 'script.json')
    src = json.load(open(path, encoding='utf-8'))
    # families.json lives beside the script being checked (a draft in its own
    # folder carries its own), falling back to the one beside this file
    fam_path = os.path.join(os.path.dirname(os.path.abspath(path)), 'families.json')
    if not os.path.exists(fam_path):
        fam_path = os.path.join(HERE, 'families.json')
    if os.path.exists(fam_path):
        FAMILIES.update(json.load(open(fam_path, encoding='utf-8')))
    bad = check(src)
    tally = collections.Counter(f for v in FAMILIES.values() for f in v)
    print('families: ' + ', '.join('%s %d' % kv for kv in tally.most_common()))
    if bad:
        print('\n'.join(bad))
        print('\n%d findings' % len(bad))
        return 1
    print('%d items clean' % len(src['scenes']))
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
