#!/usr/bin/env python3
"""Turn the written script into data.json, STORY.md and IMAGES.md.

    py lesson-template/build/rpg/anatomy-of-a-verdict-rpg/assemble-script.py

Anatomy of a Verdict is a script-first Block Camp RPG (the Loch Ness Loop
pattern, docs/CHATGPT-RPG-BRIEF.md "When Claude has written the script
first"): C1, concession (although / despite / even so / adjective + as …),
a jury room in an English Crown Court. Loosely after the courtroom-drama
shape of a juror holding out against eleven; every name, the case and the
evidence are invented.

`script.json` holds every word, with each question's key and distractors as
named fields (`correct`, `wrong1`, `wrong2`) so the slot is dealt here, from
SLOT, never by a writer's habit. This program:

  1. runs the gates — word budgets (brief §2), key never the longest option,
     straight quotes only, the blank kept in gap prompts, the graph complete
     with no orphans, four votes on every path, the key balanced on every
     PLAY order (no slot over 40%, never three running);
  2. writes data.json in the brief §7 shape, minus `images`, hotspot boxes
     (ChatGPT's job) and `local` (glosses go in translations/<lang>.json);
  3. renders STORY.md (the words in play order, key marked) and IMAGES.md
     (the style contract and one paste-ready prompt per plate).

Edit script.json, never the three outputs. Idempotent.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

ORDER = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6',
         'rec1', 'stair1', 'rec2', 'stair2', 'rec3', 'stair3', 'rec4', 'stair4',
         'after1', 'after2', 'after3',
         'wit1', 'clock1', 'wit2', 'clock2', 'wit3', 'clock3',
         'vote1', 'vote2']

NEXT = {
    'room1': 'room2', 'room2': 'room3', 'room3': 'room4', 'room4': 'room5',
    'room5': 'room6', 'room6': 'evidence',
    'rec1': 'rec2', 'rec2': 'rec3', 'rec3': 'rec4', 'rec4': 'after1',
    'stair1': 'stair2', 'stair2': 'stair3', 'stair3': 'stair4', 'stair4': 'after1',
    'after1': 'after2', 'after2': 'after3', 'after3': 'doubt',
    'wit1': 'wit2', 'wit2': 'wit3', 'wit3': 'vote1',
    'clock1': 'clock2', 'clock2': 'clock3', 'clock3': 'vote1',
    'vote1': 'vote2', 'vote2': 'resolve',
}
CHOICE_NEXT = {
    'evidence': {'THE RECORDING': 'rec1', 'THE STAIRWELL': 'stair1'},
    'doubt': {'THE WITNESS': 'wit1', 'THE CLOCK': 'clock1'},
}

TRUNK_A = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6']
MID = ['after1', 'after2', 'after3']
END = ['vote1', 'vote2']
ARM1 = {'REC': ['rec1', 'rec2', 'rec3', 'rec4'], 'STAIR': ['stair1', 'stair2', 'stair3', 'stair4']}
ARM2 = {'WIT': ['wit1', 'wit2', 'wit3'], 'CLOCK': ['clock1', 'clock2', 'clock3']}
PATHS = {'%s/%s' % (a, b): TRUNK_A + ARM1[a] + MID + ARM2[b] + END
         for a in ARM1 for b in ARM2}

# a vote turns at each: Agnes, the second vote, Gerald (either arm), Victor
RELICS = {'room3', 'after2', 'wit3', 'clock3', 'vote1'}
TILES = 4

# key slot per scene: trunk 4/4/3, arm-1 arms 1/1/2, arm-2 arms 1/1/1 →
# every one of the four paths deals 6/6/6
SLOT = {
    'room1': 0, 'room2': 1, 'room3': 2, 'room4': 0, 'room5': 1, 'room6': 2,
    'after1': 0, 'after2': 1, 'after3': 2, 'vote1': 0, 'vote2': 1,
    'rec1': 2, 'rec2': 0, 'rec3': 1, 'rec4': 2,
    'stair1': 1, 'stair2': 2, 'stair3': 0, 'stair4': 2,
    'wit1': 1, 'wit2': 2, 'wit3': 0,
    'clock1': 0, 'clock2': 1, 'clock3': 2,
}

# plates in play order; the briefing reuses room1's, the endings have their own
_plates = ['room1', 'room2', 'room3', 'room4', 'room5', 'room6', 'evidence',
           'rec1', 'rec2', 'rec3', 'rec4', 'stair1', 'stair2', 'stair3', 'stair4',
           'after1', 'after2', 'after3', 'doubt',
           'wit1', 'wit2', 'wit3', 'clock1', 'clock2', 'clock3', 'vote1', 'vote2']
IMG = {}
for _i, _sid in enumerate(_plates, start=2):
    if _sid in CHOICE_NEXT:
        tag = 'choice%d' % (list(CHOICE_NEXT).index(_sid) + 1)
    else:
        tag = 'q%d' % (PATHS['REC/WIT'].index(_sid) + 1 if _sid in PATHS['REC/WIT']
                       else PATHS['STAIR/CLOCK'].index(_sid) + 1)
    IMG[_sid] = '%02d_%s_%s.webp' % (_i, tag, _sid)
COVER_IMG = '01_cover.webp'
RULES_IMG = IMG['room1']
ENDING_IMG = {k: '%02d_ending_%s.webp' % (len(_plates) + 2 + i, k)
              for i, k in enumerate(['master', 'complete', 'missing', 'failed'])}

STYLE = ('Painted digital illustration in muted oil tones, soft brush edges, no hard '
         'outlines; an English Crown Court jury room and a converted stone mill on a '
         'rainy October afternoon: slate blue, oatmeal, faded oxblood and brass, with one '
         'warm lamp glow on the key object in every frame; eye-level camera, '
         'three-quarter view; 3:2')

CAST = [
    ('Mira Castell (you, juror twelve)', 'forties, short black bob streaked grey, brown skin, '
     'round tortoiseshell glasses, a mustard cardigan over a black polo neck. Seen from behind '
     'or three-quarter whenever possible: the player is Mira.'),
    ('Gerald Pryce (foreman)', 'sixties, tall, bald with a white fringe, navy blazer, '
     'plain dark red tie, a steel wristwatch.'),
    ('Agnes Bell', 'seventies, small, white hair in a bun, lilac twinset, reading glasses '
     'on a chain, a yellow pencil.'),
    ('Danny Rourke', 'fifties, stocky, shaved head, grey stubble, black bomber jacket, '
     'a white mug of tea.'),
    ('Priya Sandhu', 'thirties, long black plait, hospital-blue fleece, tired dark eyes, '
     'a lanyard with a blank card.'),
    ('Victor Lane', 'sixties, heavy, ruddy face, thinning sandy hair, brown tweed jacket, '
     'a gold signet ring.'),
    ('Ruth Adair (the accused)', 'early fifties, cropped grey hair, strong hands; in court '
     'a plain dark suit, in the mill a clay-stained linen smock.'),
    ('Kit Marlow (the apprentice)', 'nineteen, thin, dark hair over his eyes, a clay-dusted '
     'canvas apron, big white headphones.'),
]
NO_TEXT = '--no text, letters, writing, numbers, signage, logo, watermark'

META = {
    'title': 'ANATOMY OF A VERDICT',
    'grammar': 'Concession (although, despite, even so, adjective + as)',
    'world': 'An English Crown Court',
    'style': STYLE,
    'level': 'C1',
    'accent': '#c9a45c',
    'protagonist': 'Mira Castell',
    'cast': {'you': 'Mira Castell', 'foreman': 'Gerald Pryce',
             'jurors': ['Agnes Bell', 'Danny Rourke', 'Priya Sandhu', 'Victor Lane'],
             'accused': 'Ruth Adair', 'dead': 'Simon Hale', 'witness': 'Kit Marlow'},
    'scoring': {'points': 5, 'tiles': TILES, 'chances': 3, 'max': 90, 'pass': 75},
    'questionsPerPath': 18,
    'chrome': {
        'briefingKicker': 'BEFORE YOU DELIBERATE',
        'tiles': 'VOTES',
        'relic': 'VOTE TURNED · +{p} POINTS',
        'restart': 'SIT AGAIN',
    },
}

BUDGET = {'title': 5, 'act': 6, 'story': 28, 'clue': 16, 'prompt': 13, 'explanation': 25}
OPT_MAX, LEAD_MAX, CARD_MAX = 45, 35, 12


def words(s):
    return len(s.split())


def deal(s, slot):
    wrong = [s['wrong1'], s['wrong2']]
    return [{'text': s['correct'], 'correct': True} if i == slot else {'text': wrong.pop(0)}
            for i in range(3)]


def check(src, by_id):
    p = []
    frame = src['frame']
    blob = json.dumps(src, ensure_ascii=False)
    for ch in '‘’“”':
        if ch in blob:
            p.append('curly quote %r in script.json: straight quotes only' % ch)
    if words(frame['cover']['lead']) > LEAD_MAX:
        p.append('cover lead is %d words (max %d)' % (words(frame['cover']['lead']), LEAD_MAX))
    for c in frame['briefing']['cards']:
        if words(c['text']) > CARD_MAX:
            p.append('briefing card %r is %d words (max %d)' % (c['head'], words(c['text']), CARD_MAX))
    for ch in frame['choices']:
        for f in ('title', 'act', 'story'):
            if words(ch[f]) > BUDGET[f]:
                p.append('%s.%s is %d words (max %d)' % (ch['id'], f, words(ch[f]), BUDGET[f]))
    for sid in ORDER:
        s = by_id[sid]
        for f, mx in BUDGET.items():
            if words(s[f]) > mx:
                p.append('%s.%s is %d words (max %d)' % (sid, f, words(s[f]), mx))
        opts = [s['correct'], s['wrong1'], s['wrong2']]
        for o in opts:
            if len(o) > OPT_MAX:
                p.append('%s option %r is %d characters (max %d)' % (sid, o, len(o), OPT_MAX))
        if len(s['correct']) > max(len(s['wrong1']), len(s['wrong2'])):
            p.append('%s: the key is the longest option' % sid)
        if len(set(o.lower() for o in opts)) < 3:
            p.append('%s: two options are the same' % sid)
        if '___' in s['prompt'] and len(s['correct'].split()) > 4:
            p.append('%s: a gap prompt with a long key, check it is a gap' % sid)
        if s['correct'].lower() in s['clue'].lower():
            p.append('%s: the clue gives the key away' % sid)
    return p


def graph(scenes):
    p = []
    for sid, s in scenes.items():
        nxts = [c['next'] for c in s['choices']] if 'choices' in s else [s['correctNext'], s['wrongNext']]
        for n in nxts:
            if n != 'resolve' and n not in scenes:
                p.append('%s points at %r, which does not exist' % (sid, n))
    reached, stack = set(), ['room1']
    while stack:
        sid = stack.pop()
        if sid in reached or sid == 'resolve':
            continue
        reached.add(sid)
        s = scenes[sid]
        stack += [c['next'] for c in s['choices']] if 'choices' in s else [s['correctNext']]
    for sid in set(scenes) - reached:
        p.append('%s is an orphan: nothing reaches it' % sid)
    for name, order in PATHS.items():
        n = sum(1 for sid in order if sid in RELICS)
        if n != TILES:
            p.append('%s: %d votes on the path, scoring says %d' % (name, n, TILES))
        t = [0, 0, 0]
        for sid in order:
            t[SLOT[sid]] += 1
        if max(t) / len(order) > 0.40:
            p.append('%s: key slots %d/%d/%d, one slot over 40%%' % (name, t[0], t[1], t[2]))
        run = 1
        for a, b in zip(order, order[1:]):
            run = run + 1 if SLOT[a] == SLOT[b] else 1
            if run >= 3:
                p.append('%s: slot %d three running at %s' % (name, SLOT[b], b))
    return p


def prompt_for(picture):
    who = [line for name, line in CAST if name.split(' (')[0].split()[0] in picture]
    sheet = ' '.join('%s: %s' % (n.split(' (')[0], l) for n, l in CAST
                     if n.split(' (')[0].split()[0] in picture)
    return '%s. %s%s Glowing object on the right, between 60%% and 94%% of the width; the left half quiet. --ar 3:2 %s' % (
        STYLE, picture, (' ' + sheet) if who else '', NO_TEXT)


def render_story(data, src):
    by_id = {s['id']: s for s in src['scenes']}
    fr = src['frame']
    L = ['# ANATOMY OF A VERDICT — the script', '',
         '<!-- GENERATED by assemble-script.py from script.json. Do not edit this file. -->', '',
         'A Block Camp RPG for **C1** learners: **%s**, in **%s**. The pictures are in `IMAGES.md`; '
         'this file is the words, in play order, with the key marked ✔ in the slot it sits in.'
         % (META['grammar'], META['world']), '',
         '## How this file is used', '',
         '- **ChatGPT** gets this file, `IMAGES.md`, `data.json` and the standing brief '
         '`docs/CHATGPT-RPG-BRIEF.md`. Its job is the pictures, the hotspot boxes and the export: '
         'paste `data.json` in as `window.VERDICT_GAME_DATA` **unchanged**, add `images` and each '
         'scene\'s `hotspot` box, change no text, and write **no `local` blocks**.',
         '- **The Claude session that builds it** follows `docs/HANDOFF-rpg.md` (script-first kind). '
         'Plates are 3:2, 1536 × 1024.', '',
         '## Scoring', '',
         '| | |', '|---|---|',
         '| Points | +5 a correct answer |',
         '| Chances | 3. A wrong answer costs one; at 0 the game ends in `failed` |',
         '| Votes | 4 turned, at four named scenes. Miss one and the best ending is `missing` |',
         '| Per path | 18 questions, max 90, pass 75 |', '',
         'Chrome strings: HUD **%s**, relic line **%s**, play again **%s**, briefing kicker **%s**.'
         % (META['chrome']['tiles'], META['chrome']['relic'], META['chrome']['restart'],
            META['chrome']['briefingKicker']), '', '---', '',
         '# COVER', '',
         '**Picture:** `%s` · **Object:** %s' % (COVER_IMG, fr['cover']['object']), '',
         '**Eyebrow:** %s  ' % fr['cover']['eyebrow'],
         '**Title:** %s  ' % fr['cover']['title'],
         '**Lead (%d words):** %s  ' % (words(fr['cover']['lead']), fr['cover']['lead']),
         '**Chips:** %s  ' % ' · '.join('`%s`' % r for r in fr['cover']['rules']),
         '**Start button:** %s  ' % fr['cover']['start'],
         '**Small line:** %s' % fr['cover']['small'], '',
         '# BRIEFING', '',
         '**Picture:** `%s` (reused) · **Title:** %s' % (RULES_IMG, fr['briefing']['title']), '']
    for i, c in enumerate(fr['briefing']['cards'], 1):
        L.append('%d. **%s** — %s' % (i, c['head'], c['text']))
    L += ['', '**Note:** %s  ' % fr['briefing']['note'], '**Button:** %s' % fr['briefing']['button'], '']

    play = (TRUNK_A + ['evidence'] + ARM1['REC'] + ARM1['STAIR'] + MID + ['doubt']
            + ARM2['WIT'] + ARM2['CLOCK'] + END)
    act = None
    n = 0
    for sid in play:
        s = data['scenes'][sid]
        if s['act'] != act:
            act = s['act']
            L += ['---', '', '# %s' % act, '']
        if 'choices' in s:
            L += ['**Picture:** `%s` · **Object:** %s' % (s['image'], s['hotspot']['object']), '',
                  '### %s' % s['title'], '', s['story'], '']
            for c in s['choices']:
                L.append('- **%s** → `%s` — button *%s*. %s' % (c['route'], c['next'], c['label'], c['note']))
            L.append('')
            continue
        n += 1
        L += ['### %s · %s%s' % (sid, s['title'], '  ★ VOTE TURNED' if s['relic'] else ''),
              '**Picture:** `%s` · **Object:** %s' % (s['image'], s['hotspot']['object']), '',
              '**Story.** %s' % s['story'], '', '**Clue.** %s' % s['clue'], '',
              '**%s**' % s['prompt'], '']
        for i, a in enumerate(s['answers'], 1):
            L.append('%d. %s%s' % (i, a['text'], '  ✔' if a.get('correct') else ''))
        L += ['', '*%s*' % s['explanation'], '', '→ `%s`' % s['correctNext'], '']
    L += ['---', '', '# ENDINGS', '']
    for k, e in data['endings'].items():
        L += ['### %s · %s — %s' % (k, e['label'], e['title']),
              '**Picture:** `%s` · **Object:** %s' % (e['image'], e['hotspot']['object']), '',
              e['text'], '']
    return '\n'.join(L)


def render_images(data, src):
    fr = src['frame']
    by_id = {s['id']: s for s in src['scenes']}
    pics = {c['id']: c['picture'] for c in fr['choices']}
    pics.update({s['id']: s['picture'] for s in src['scenes']})
    L = ['# ANATOMY OF A VERDICT — the image list', '',
         '<!-- GENERATED by assemble-script.py from script.json. Do not edit this file. -->', '',
         '%d plates, numbered in play order to match `image` in `data.json`. The briefing reuses '
         '`%s`; nothing else is reused, and no two filenames may hold the same picture.'
         % (len(IMG) + 1 + len(ENDING_IMG), RULES_IMG), '',
         '**Deliver WebP, 1536 × 1024 (3:2), each under 200 KB.**', '',
         '## The style contract — the start of every prompt, verbatim', '',
         '> %s' % STYLE, '',
         '## Four rules that cannot bend', '',
         '1. **No lettering anywhere.** No writing on evidence bags, folders, screens, photos, '
         'watches, signs, vans or lanyards; no numbers, no timestamps. Every prompt ends with '
         '`%s`.' % NO_TEXT,
         '2. **The glowing object sits right, between 60% and 94% of the width; the left half '
         'stays quiet** — wall, window, empty chairs, dark table. The text panel sits left all game.',
         '3. **Light enough to glow.** A warm lamp on or beside the object in every frame. No '
         'crushed blacks, no heavy grain, no lens flare.',
         '4. **One look per character.** Paste their line from the sheet below, unchanged, into '
         'every prompt they appear in (the prompts below already do).', '',
         '**No violence shown.** Simon Hale never appears; the stairwell is shown only in '
         'empty police photographs. No blood.', '',
         '## The character sheet', '']
    for name, line in CAST:
        L.append('- **%s:** %s' % (name, line))
    L += ['', '## The prompts', '',
          '### `%s` — cover · object: %s' % (COVER_IMG, fr['cover']['object']), '',
          '```', prompt_for(fr['cover']['picture']), '```', '']
    for sid in sorted(IMG, key=lambda k: IMG[k]):
        obj = data['scenes'][sid]['hotspot']['object']
        L += ['### `%s` · object: %s' % (IMG[sid], obj), '',
              '```', prompt_for(pics[sid]), '```', '']
    for e in fr['endings']:
        L += ['### `%s` — ending %s · object: %s' % (ENDING_IMG[e['key']], e['key'], e['object']), '',
              '```', prompt_for(e['picture']), '```', '']
    return '\n'.join(L)


def main():
    src = json.load(open(os.path.join(HERE, 'script.json'), encoding='utf-8'))
    by_id = {s['id']: s for s in src['scenes']}
    missing = [sid for sid in ORDER if sid not in by_id]
    extra = [sid for sid in by_id if sid not in ORDER]
    if missing or extra:
        sys.exit('script.json scenes differ from ORDER: missing %s, extra %s' % (missing, extra))

    problems = check(src, by_id)
    frame = src['frame']
    scenes = {}
    for sid in ORDER:
        s = by_id[sid]
        scenes[sid] = {
            'image': IMG[sid], 'kind': 'GRAMMAR',
            'hotspot': {'object': s['object']},
            'act': s['act'], 'title': s['title'], 'story': s['story'],
            'clue': s['clue'], 'prompt': s['prompt'],
            'answers': deal(s, SLOT[sid]),
            'explanation': s['explanation'], 'points': 5,
            'relic': sid in RELICS,
            'correctNext': NEXT[sid], 'wrongNext': NEXT[sid],
        }
    for ch in frame['choices']:
        sid = ch['id']
        scenes[sid] = {
            'image': IMG[sid], 'kind': 'choice',
            'hotspot': {'object': ch['object']},
            'act': ch['act'], 'title': ch['title'], 'story': ch['story'],
            'choices': [{'route': r['route'], 'next': CHOICE_NEXT[sid][r['route']],
                         'label': r['label'], 'note': r['note']} for r in ch['routes']],
        }
    problems += graph(scenes)
    endings = {e['key']: e for e in frame['endings']}
    for key in ENDING_IMG:
        if key not in endings:
            problems.append('no %s ending' % key)
    if problems:
        print('\n'.join(problems))
        sys.exit('\n%d problems — fix script.json, not this file' % len(problems))

    cov, br = frame['cover'], frame['briefing']
    out = {
        'meta': META,
        'cover': {'image': COVER_IMG, 'eyebrow': cov['eyebrow'], 'title': cov['title'],
                  'lead': cov['lead'], 'rules': cov['rules'], 'start': cov['start'],
                  'small': cov['small'], 'hotspot': {'object': cov['object']}},
        'briefing': {'image': RULES_IMG, 'title': br['title'], 'cards': br['cards'],
                     'note': br['note'], 'button': br['button']},
        'first': 'room1',
        'scenes': scenes,
        'endings': {k: {'image': ENDING_IMG[k], 'label': e['label'], 'title': e['title'],
                        'text': e['text'], 'hotspot': {'object': e['object']}}
                    for k, e in endings.items()},
    }
    for name, text in (('data.json', json.dumps(out, ensure_ascii=False, indent=1) + '\n'),
                       ('STORY.md', render_story(out, src) + '\n'),
                       ('IMAGES.md', render_images(out, src) + '\n')):
        with open(os.path.join(HERE, name), 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
    tally = [sum(1 for sid in ORDER if SLOT[sid] == i) for i in range(3)]
    print('wrote data.json, STORY.md, IMAGES.md — %d scenes (%d questions), key %d/%d/%d over '
          'the file, 6/6/6 and 4 votes on each of %d paths, %d plates'
          % (len(scenes), len(ORDER), tally[0], tally[1], tally[2], len(PATHS),
             len(IMG) + 1 + len(ENDING_IMG)))


if __name__ == '__main__':
    main()
