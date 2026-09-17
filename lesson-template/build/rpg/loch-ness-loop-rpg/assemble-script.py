#!/usr/bin/env python3
"""Turn the written script into data.json — dealing the answer key as it goes.

    py lesson-template/build/rpg/loch-ness-loop-rpg/assemble-script.py [script.json]

`script.json` is what the writing pass produced: a flat list of question
scenes, each carrying `correct`, `wrong1` and `wrong2` as three separate
fields, plus the frame (cover, briefing, the two route choices, four
endings). Named fields rather than an ordered list, so the slot the key
lands in is this program's decision and never a writer's habit — the
Frankenstein export arrived with the answer in slot 0 on all forty-four
questions (rpg/kraken-black-tide-rpg/assemble-script.py has the history).

This does three things the writing cannot do for itself:

  1. **Deals the key** from the explicit SLOT map below, balanced 6/6/6 over
     each of the FOUR play orders (two forks, so 2 x 2 paths). A rotation
     over the file order correlates the slot with the branch.
  2. **Runs every item gate** — check-items.py — before writing anything.
  3. **Wires the graph**: next edges, the four photos, the 16:9 plate names,
     the scoring block, and the builder's chrome strings under meta.chrome.

Writes data.json beside this file, in the shape docs/CHATGPT-RPG-BRIEF.md §7
asks ChatGPT for, minus `images` and the hotspot boxes (ChatGPT's job) and
minus `local` (the glosses live in translations/<lang>.json in this
directory, and the builder applies them). Idempotent; run it after any rewrite.
"""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# scene id -> the plate it plays on. Play order; the same list prep-plates.py
# writes. The briefing reuses shop3's plate; the endings have their own.
IMG = {
    'shop1': '02_q1_shop1.webp', 'shop2': '03_q2_shop2.webp', 'shop3': '04_q3_shop3.webp',
    'shop4': '05_q4_shop4.webp', 'shop5': '06_q5_shop5.webp', 'shop6': '07_q6_shop6.webp',
    'dores': '08_choice1_dores.webp',
    'shore1': '09_q7_shore1.webp', 'shore2': '10_q8_shore2.webp',
    'shore3': '11_q9_shore3.webp', 'shore4': '12_q10_shore4.webp',
    'hill1': '13_q7_hill1.webp', 'hill2': '14_q8_hill2.webp',
    'hill3': '15_q9_hill3.webp', 'hill4': '16_q10_hill4.webp',
    'pub1': '17_q11_pub1.webp', 'pub2': '18_q12_pub2.webp', 'pub3': '19_q13_pub3.webp',
    'pier': '20_choice2_pier.webp',
    'deep1': '21_q14_deep1.webp', 'deep2': '22_q15_deep2.webp', 'deep3': '23_q16_deep3.webp',
    'bay1': '24_q14_bay1.webp', 'bay2': '25_q15_bay2.webp', 'bay3': '26_q16_bay3.webp',
    'back1': '27_q17_back1.webp', 'back2': '28_q18_back2.webp',
}
COVER_IMG = '01_cover.webp'
RULES_IMG = '04_q3_shop3.webp'
ENDING_IMG = {'master': '29_ending_master.webp', 'complete': '30_ending_complete.webp',
              'missing': '31_ending_missing.webp', 'failed': '32_ending_failed.webp'}

# file order of the twenty-five question scenes, branches interleaved where
# they occur so a reader of data.json meets them in play order
ORDER = ['shop1', 'shop2', 'shop3', 'shop4', 'shop5', 'shop6',
         'shore1', 'hill1', 'shore2', 'hill2', 'shore3', 'hill3', 'shore4', 'hill4',
         'pub1', 'pub2', 'pub3',
         'deep1', 'bay1', 'deep2', 'bay2', 'deep3', 'bay3',
         'back1', 'back2']

NEXT = {
    'shop1': 'shop2', 'shop2': 'shop3', 'shop3': 'shop4', 'shop4': 'shop5',
    'shop5': 'shop6', 'shop6': 'dores',
    'shore1': 'shore2', 'shore2': 'shore3', 'shore3': 'shore4', 'shore4': 'pub1',
    'hill1': 'hill2', 'hill2': 'hill3', 'hill3': 'hill4', 'hill4': 'pub1',
    'pub1': 'pub2', 'pub2': 'pub3', 'pub3': 'pier',
    'deep1': 'deep2', 'deep2': 'deep3', 'deep3': 'back1',
    'bay1': 'bay2', 'bay2': 'bay3', 'bay3': 'back1',
    'back1': 'back2', 'back2': 'resolve',
}

CHOICE_NEXT = {
    'dores': {'SHORE ROAD': 'shore1', 'HIGH ROAD': 'hill1'},
    'pier':  {'THE CASTLE': 'deep1', 'THE BAY': 'bay1'},
}

# the four photos. deep3 and bay3 are parallel, so every path collects four.
RELICS = {'shop3', 'pub2', 'deep3', 'bay3', 'back1'}
TILES = 4

# Which button the key sits on, per scene. Balanced over every PLAY order:
# the trunk (11 scenes) deals 4/4/3, each branch-1 arm deals 1/1/2 and each
# branch-2 arm 1/1/1, so every one of the four paths comes out 6/6/6. No slot
# runs three deep on any path, and parallel scenes share a slot only once
# (shore4/hill4), so replaying the other road hands over nothing.
SLOT = {
    'shop1': 0, 'shop2': 1, 'shop3': 2, 'shop4': 0, 'shop5': 1, 'shop6': 2,
    'pub1': 0, 'pub2': 1, 'pub3': 2, 'back1': 0, 'back2': 1,
    'shore1': 2, 'shore2': 0, 'shore3': 1, 'shore4': 2,
    'hill1': 1, 'hill2': 2, 'hill3': 0, 'hill4': 2,
    'deep1': 1, 'deep2': 2, 'deep3': 0,
    'bay1': 0, 'bay2': 1, 'bay3': 2,
}

META = {
    'title': 'THE LOCH NESS LOOP',
    'grammar': 'Bike-parts vocabulary (British English)',
    'world': 'Loch Ness and the Great Glen',
    'style': ('Flat vector illustration, cel-shaded, solid flat colours and clean shapes, '
              'no outlines, soft long shadows; Highland light after rain, mid-September: '
              'loch-slate blue, heather and bracken orange, moss green, wet grey stone, '
              'one warm amber light in every frame; eye-level camera; 16:9'),
    'level': 'B2',
    'accent': '#e8c04a',
    'aspect': '16:9',
    'plate': {'w': 1536, 'h': 864},
    'protagonist': 'Alex Marin',
    'cast': {'you': 'Alex Marin', 'shop': 'Shona Nicolson', 'pub': ['Moira Fraser', 'Jean Cameron'],
             'boat': 'Archie MacRae'},
    'scoring': {'points': 5, 'tiles': TILES, 'chances': 3, 'max': 90, 'pass': 75},
    'questionsPerPath': 18,
    # the builder's own strings, glossed in translations/ like everything else
    'chrome': {
        'briefingKicker': 'BEFORE YOU SET OFF',
        'tiles': 'PHOTOS',
        'relic': 'PHOTO TAKEN · +{p} POINTS',
        'restart': 'RIDE AGAIN',
    },
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


_spec = importlib.util.spec_from_file_location('check_items', os.path.join(HERE, 'check-items.py'))
check_items = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_items)


def main(argv):
    path = argv[0] if argv else os.path.join(HERE, 'script.json')
    src = json.load(open(path, encoding='utf-8'))
    by_id = {s['id']: s for s in src['scenes']}
    frame = src['frame']

    missing = [sid for sid in ORDER if sid not in by_id]
    if missing:
        sys.exit('script.json is short %d scenes: %s' % (len(missing), ', '.join(missing)))
    extra = [sid for sid in by_id if sid not in ORDER]
    if extra:
        sys.exit('script.json has scenes the graph does not: %s' % ', '.join(extra))

    fam_path = os.path.join(HERE, 'families.json')
    if os.path.exists(fam_path):
        check_items.FAMILIES.update(json.load(open(fam_path, encoding='utf-8')))
    problems = check_items.check(src)

    scenes, tally = {}, {0: 0, 1: 0, 2: 0}
    for sid in ORDER:
        s = by_id[sid]
        slot = SLOT[sid]
        tally[slot] += 1
        scenes[sid] = {
            'image': IMG[sid],
            'kind': s['kind'],
            'hotspot': {'object': s['object']},
            'act': s['act'], 'title': s['title'], 'story': s['story'],
            'clue': s['clue'], 'prompt': s['prompt'],
            'answers': deal(s, slot),
            'explanation': s['explanation'],
            'points': 5,
            'relic': sid in RELICS,
            'correctNext': NEXT[sid], 'wrongNext': NEXT[sid],
        }

    for ch in frame['choices']:
        sid = ch['id']
        scenes[sid] = {
            'image': IMG[sid],
            'kind': 'choice',
            'hotspot': {'object': ch['object']},
            'act': ch['act'], 'title': ch['title'], 'story': ch['story'],
            'choices': [{'route': r['route'], 'next': CHOICE_NEXT[sid][r['route']],
                         'label': r['label'], 'note': r['note']} for r in ch['routes']],
        }

    ids = set(scenes)
    for sid, s in scenes.items():
        for nxt in ([c['next'] for c in s['choices']] if 'choices' in s
                    else [s['correctNext'], s['wrongNext']]):
            if nxt != 'resolve' and nxt not in ids:
                problems.append('%s points at %r, which does not exist' % (sid, nxt))
    reached, stack = set(), ['shop1']
    while stack:
        sid = stack.pop()
        if sid in reached or sid == 'resolve':
            continue
        reached.add(sid)
        s = scenes[sid]
        stack += ([c['next'] for c in s['choices']] if 'choices' in s else [s['correctNext']])
    for sid in ids - reached:
        problems.append('%s is an orphan: nothing reaches it' % sid)

    # photos and the key deal are both measured per PLAY order
    for pname, order in check_items.PATHS.items():
        n_rel = sum(1 for sid in order if sid in RELICS)
        if n_rel != TILES:
            problems.append('%s: %d photos on the path, scoring says %d' % (pname, n_rel, TILES))
        t = {0: 0, 1: 0, 2: 0}
        for sid in order:
            t[SLOT[sid]] += 1
        if max(t.values()) / len(order) > 0.40:
            problems.append('%s: the key sits in one slot on %d of %d questions (%d/%d/%d)'
                            % (pname, max(t.values()), len(order), t[0], t[1], t[2]))
        run = 1
        for a, b in zip(order, order[1:]):
            run = run + 1 if SLOT[a] == SLOT[b] else 1
            if run >= 3:
                problems.append('%s: the key sits in slot %d three questions running at %s'
                                % (pname, SLOT[b], b))

    endings = {e['key']: e for e in frame['endings']}
    for key in ('master', 'complete', 'missing', 'failed'):
        if key not in endings:
            problems.append('no %s ending' % key)

    if problems:
        print('\n'.join(problems))
        sys.exit('\n%d problems — fix the script, not this file' % len(problems))

    cov, br = frame['cover'], frame['briefing']
    out = {
        'meta': META,
        'cover': {'image': COVER_IMG, 'eyebrow': cov['eyebrow'], 'title': cov['title'],
                  'lead': cov['lead'], 'rules': cov['rules'], 'start': cov['start'],
                  'small': cov['small'], 'hotspot': {'object': cov['object']}},
        'briefing': {'image': RULES_IMG, 'title': br['title'], 'cards': br['cards'],
                     'note': br['note'], 'button': br['button']},
        'first': 'shop1',
        'scenes': scenes,
        'endings': {k: {'image': ENDING_IMG[k], 'label': e['label'], 'title': e['title'],
                        'text': e['text'], 'hotspot': {'object': e['object']}}
                    for k, e in endings.items()},
    }
    dest = os.path.join(HERE, 'data.json')
    with open(dest, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
        f.write('\n')
    print('wrote data.json — %d scenes (%d questions), key %d/%d/%d over the file, 4 photos a path'
          % (len(scenes), len(ORDER), tally[0], tally[1], tally[2]))


if __name__ == '__main__':
    main(sys.argv[1:])
