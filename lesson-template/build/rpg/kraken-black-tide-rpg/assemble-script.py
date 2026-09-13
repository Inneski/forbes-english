#!/usr/bin/env python3
"""Turn the written script into data.json — dealing the answer key as it goes.

    py lesson-template/build/rpg/kraken-black-tide-rpg/assemble-script.py script.json

`script.json` is what the writing pass produced: a flat list of question
scenes, each carrying `correct`, `wrong1` and `wrong2` as three separate
fields, plus the frame (cover, briefing, the two route choices, four endings).
Writing them as named fields rather than as an ordered list is deliberate —
it makes the slot the key lands in this program's decision rather than a
writer's habit, and the habit is the defect: the Frankenstein export arrived
with the answer in slot 0 on all forty-four questions, which is invisible in a
diff and obvious to the third student who notices.

So this does three things the writing cannot do for itself:

  1. **Deals the key** from the explicit SLOT map below, balanced 6/6/6 over
     each of the two PLAY orders rather than over this file. A rotation over
     the file order looks right and is not: the file interleaves the branches,
     so a cycle correlates the slot with the branch.
  2. **Runs every item gate** — check-items.py, which measures the budgets, the
     option lengths, the blend tell, the CAPS convention and the error-family
     balance. Much cheaper to hear about here than after thirty-two plates
     exist.
  3. **Wires the graph**: the fixed next/correctNext/wrongNext edges, the four
     marker barrels, the plate filenames, and the scoring block.

Writes data.json beside this file. Idempotent; run it again after any rewrite.
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# scene id -> the plate it plays on. Play order, and the same list
# prep-plates.py writes. The briefing has no plate of its own (the builder
# gives it the shed) and the four endings are named in the builder.
IMG = {
    'drift': '02_q1_drift.webp', 'bell': '03_q2_bell.webp',
    'provost': '04_q3_provost.webp', 'hoy': '05_q4_hoy.webp',
    'jar': '06_q5_jar.webp', 'shed': '07_q6_shed.webp',
    'sound': '08_choice1_sound.webp',
    'reef1': '09_q7_reef1.webp', 'reef2': '10_q8_reef2.webp',
    'reef3': '11_q9_reef3.webp', 'reef4': '12_q10_reef4.webp',
    'cave1': '13_q7_cave1.webp', 'cave2': '14_q8_cave2.webp',
    'cave3': '15_q9_cave3.webp', 'cave4': '16_q10_cave4.webp',
    'wreck1': '17_q11_wreck1.webp', 'wreck2': '18_q12_wreck2.webp',
    'wreck3': '19_q13_wreck3.webp',
    'decision': '20_choice2_decision.webp',
    'corry1': '21_q14_corry1.webp', 'corry2': '22_q15_corry2.webp',
    'corry3': '23_q16_corry3.webp',
    'night1': '24_q14_night1.webp', 'night2': '25_q15_night2.webp',
    'night3': '26_q16_night3.webp',
    'barrels': '27_q17_barrels.webp', 'last': '28_q18_last.webp',
}

# play order of the twenty-five question scenes. Both branches are listed
# where they actually occur, so the key rotation walks them alternately.
ORDER = ['drift', 'bell', 'provost', 'hoy', 'jar', 'shed',
         'reef1', 'cave1', 'reef2', 'cave2', 'reef3', 'cave3', 'reef4', 'cave4',
         'wreck1', 'wreck2', 'wreck3',
         'corry1', 'night1', 'corry2', 'night2', 'corry3', 'night3',
         'barrels', 'last']

# where each question scene goes next. 'last' resolves to an ending by score.
NEXT = {
    'drift': 'bell', 'bell': 'provost', 'provost': 'hoy', 'hoy': 'jar',
    'jar': 'shed', 'shed': 'sound',
    'reef1': 'reef2', 'reef2': 'reef3', 'reef3': 'reef4', 'reef4': 'wreck1',
    'cave1': 'cave2', 'cave2': 'cave3', 'cave3': 'cave4', 'cave4': 'wreck1',
    'wreck1': 'wreck2', 'wreck2': 'wreck3', 'wreck3': 'decision',
    'corry1': 'corry2', 'corry2': 'corry3', 'corry3': 'barrels',
    'night1': 'night2', 'night2': 'night3', 'night3': 'barrels',
    'barrels': 'last', 'last': 'resolve',
}

CHOICE_NEXT = {
    'sound':    {'REEF': 'reef1', 'CAVES': 'cave1'},
    'decision': {'CORRY': 'corry1', 'WATCH': 'night1'},
}

# the four marker barrels, spread one to a chapter
RELICS = {'drift', 'shed', 'wreck1', 'last'}

# Which button the key sits on, per scene. A rotation over the file order was
# the obvious thing and it was wrong: the file interleaves the two branches, so
# a repeating cycle correlates the slot with the branch. It dealt 8/8/9 overall
# and still gave one of the two PLAY orders a 8/2/8 split — on that path the
# middle button was right twice in eighteen questions, which is a stronger tell
# than the one the dealing exists to remove.
#
# So the map is explicit and balanced over both paths instead of over the file:
# each path gets 6/6/6, no slot runs three deep, and no two parallel branch
# scenes (reef1/cave1, corry2/night2, …) share a slot bar one, so replaying to
# take the other road hands over nothing.
SLOT = {
    # shared trunk, 4/4/3
    'drift': 0, 'bell': 1, 'provost': 2, 'hoy': 0, 'jar': 1, 'shed': 2,
    'wreck1': 0, 'wreck2': 1, 'wreck3': 2, 'barrels': 0, 'last': 1,
    # branch A, 2/2/3
    'reef1': 2, 'reef2': 0, 'reef3': 1, 'reef4': 2,
    'corry1': 0, 'corry2': 1, 'corry3': 2,
    # branch B, 2/2/3
    'cave1': 0, 'cave2': 2, 'cave3': 0, 'cave4': 1,
    'night1': 2, 'night2': 1, 'night3': 2,
}

META = {
    'title': 'KRAKEN: THE BLACK TIDE',
    'grammar': 'Present Perfect / Present Perfect Continuous',
    'world': 'The west coast of Scotland',
    'style': ('Painted digital illustration, west coast of Scotland, late August, low grey '
              'Atlantic light with one warm amber lamp in frame, slate-blue sea, wet black '
              'granite, kelp green and rust red, soft brush edges, no hard outlines, '
              'eye-level three-quarter camera'),
    'level': 'B1',
    'accent': '#e8c04a',
    'protagonist': 'Isla Brodie',
    'cast': {'sergeant': 'Isla Brodie', 'scientist': 'Dr. Maren Hoy',
             'skipper': 'Angus Quinn', 'provost': 'Provost Baird'},
    'inspiration': {'title': 'Jaws', 'author': 'Steven Spielberg',
                    'adaptation': 'Original west-coast-of-Scotland adaptation of the '
                                  'closed-beach premise, with a kraken.'},
    'scoring': {'points': 5, 'tiles': 4, 'chances': 3, 'max': 90, 'pass': 75},
    'questionsPerPath': 18,
}


def deal(scene, slot):
    """Put the key in `slot` and the two distractors either side of it."""
    wrong = [scene['wrong1'], scene['wrong2']]
    opts = []
    for i in range(3):
        if i == slot:
            opts.append({'text': scene['correct'], 'correct': True})
        else:
            opts.append({'text': wrong.pop(0)})
    return opts


# The budget, length, blend, CAPS and family gates all live in check-items.py
# and are run from here, so there is one implementation and one place to fix.
#
# rpg.py's own length gate stays where it is but cannot be relied on: it wants
# the key 10% AND 4 characters longer than its longest distractor before it
# fires, which no real three-option item reaches. Measured against this
# lesson's first draft it passed all twenty-five while seven of them had a
# strict length ordering a learner could read. check-items.py uses a flat
# two-character margin in both directions instead.
import importlib.util

_spec = importlib.util.spec_from_file_location(
    'check_items', os.path.join(HERE, 'check-items.py'))
check_items = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_items)


def main(argv):
    if not argv:
        sys.exit('usage: assemble-script.py script.json')
    src = json.load(open(argv[0], encoding='utf-8'))
    by_id = {s['id']: s for s in src['scenes']}
    frame = src['frame']

    missing = [sid for sid in ORDER if sid not in by_id]
    if missing:
        sys.exit('script.json is short %d scenes: %s' % (len(missing), ', '.join(missing)))
    extra = [sid for sid in by_id if sid not in ORDER]
    if extra:
        sys.exit('script.json has scenes the graph does not: %s' % ', '.join(extra))

    check_items.FAMILIES.update(
        json.load(open(os.path.join(HERE, 'families.json'), encoding='utf-8')))
    problems = check_items.check(src['scenes'])

    scenes, tally = {}, {0: 0, 1: 0, 2: 0}
    for n, sid in enumerate(ORDER):
        s = by_id[sid]
        slot = SLOT[sid]
        opts = deal(s, slot)
        tally[slot] += 1
        scene = {
            'image': IMG[sid],
            'hotspot': {'object': s['object']},
            'act': s['act'], 'title': s['title'], 'story': s['story'],
            'clue': s['clue'], 'prompt': s['prompt'],
            'answers': opts,
            'explanation': s['explanation'],
            'points': 5,
            'relic': sid in RELICS,
            'correctNext': NEXT[sid], 'wrongNext': NEXT[sid],
        }
        scenes[sid] = scene

    for ch in frame['choices']:
        sid = ch['id']
        scenes[sid] = {
            'image': IMG[sid],
            'hotspot': {'object': ch['object']},
            'act': ch['act'], 'title': ch['title'], 'story': ch['story'],
            'choices': [{'route': r['route'], 'next': CHOICE_NEXT[sid][r['route']],
                         'label': r['label'], 'note': r['note']} for r in ch['routes']],
        }

    # the graph has to be walkable in both directions: nothing dangling, and
    # nothing nobody can reach
    ids = set(scenes)
    for sid, s in scenes.items():
        for nxt in ([c['next'] for c in s['choices']] if 'choices' in s
                    else [s['correctNext'], s['wrongNext']]):
            if nxt != 'resolve' and nxt not in ids:
                problems.append('%s points at %r, which does not exist' % (sid, nxt))
    reached, stack = set(), ['drift']
    while stack:
        sid = stack.pop()
        if sid in reached or sid == 'resolve':
            continue
        reached.add(sid)
        s = scenes[sid]
        stack += ([c['next'] for c in s['choices']] if 'choices' in s
                  else [s['correctNext']])
    for sid in ids - reached:
        problems.append('%s is an orphan: nothing reaches it' % sid)

    n_rel = sum(1 for s in scenes.values() if s.get('relic'))
    if n_rel != META['scoring']['tiles']:
        problems.append('%d marker barrels, scoring says %d' % (n_rel, META['scoring']['tiles']))

    # measured over each PLAY order, not the file: the file interleaves the
    # branches and a file-order tally hides a per-path skew completely.
    for pname, order in check_items.PATHS.items():
        t = {0: 0, 1: 0, 2: 0}
        for sid in order:
            t[SLOT[sid]] += 1
        if max(t.values()) / len(order) > 0.40:
            problems.append('%s: the key sits in one slot on %d of %d questions (%d/%d/%d)'
                            % (pname, max(t.values()), len(order), t[0], t[1], t[2]))

    if problems:
        print('\n'.join(problems))
        sys.exit('\n%d problems — fix the script, not this file' % len(problems))

    cov = frame['cover']
    out = {
        'meta': META,
        'cover': {'image': '01_cover.webp', 'eyebrow': cov['eyebrow'], 'title': cov['title'],
                  'lead': cov['lead'], 'rules': cov['rules'], 'start': cov['start'],
                  'small': cov['small']},
        'briefing': {'image': '07_q6_shed.webp', 'title': frame['briefing']['title'],
                     'cards': frame['briefing']['cards'], 'note': frame['briefing']['note'],
                     'button': frame['briefing']['button']},
        'first': 'drift',
        'scenes': scenes,
        'endings': {e['key']: {'label': e['label'], 'title': e['title'], 'text': e['text']}
                    for e in frame['endings']},
    }
    dest = os.path.join(HERE, 'data.json')
    with open(dest, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote data.json — %d scenes (%d questions), key %d/%d/%d, %d barrels'
          % (len(scenes), len(ORDER), tally[0], tally[1], tally[2], n_rel))


if __name__ == '__main__':
    main(sys.argv[1:])
