#!/usr/bin/env python3
"""Frankenstein: The Green Prometheus — GOING TO voxel RPG (A2).

    python3 lesson-template/build/build_frankenstein_green_prometheus.py

Rebuilds block-camp/frankenstein-green-prometheus-rpg.html from
lesson-template/build/rpg/frankenstein-green-prometheus-rpg/data.json — the
text of the V32 standalone export, pulled out by rpg/extract_patched.py —
plus everything below that the export did not have: the hotspot on each
picture, a rules briefing before the first question, and a distributed
answer key.

Every gloss comes from rpg/frankenstein-green-prometheus-rpg/translations/,
nine languages keyed by the English string. The export's own de/es were not
carried over: 71 of them gloss a pre-patch English that later blocks rewrote,
so they described scenes no longer on the page (docs/HANDOFF.md, 2026-09-07).

Three things this builder fixes that the export shipped wrong:

  * **The answer was in slot 0 on all 44 questions.** A deck shuffles its
    options in the browser; this engine renders `opts` in spec order, so the
    first option really is the first button. KEY below deals the key across
    the three slots. rpg.py refuses the build if it drifts back.
  * **Two scenes were unreachable** — `17b_search` and `36a_icebound_rescue`,
    each a near-twin of the scene that superseded it. Dropped, which is what
    takes the lesson to 42 questions.
  * **One item keyed the longest option by 9 characters** — the short-answer
    item at `40_creature_lament`. That scene is now cut outright (CUT below),
    so the levelled option set went with it.

Pictures: block-camp/frankenstein-green-prometheus-rpg/*.webp, 1536x1024.
The export mixed 3:2 and 16:9 plates; the 16:9 ones were centre-cropped to
3:2 before the hotspots were read off them.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'frankenstein-green-prometheus-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

# Nothing points at these: each is a superseded draft of the scene after it.
DEAD = ('17b_search', '36a_icebound_rescue')

# Cut on purpose, 2026-09-09. The lament put the Creature at Victor's bedside
# at human scale one scene after the crew flee a figure the height of an ice
# cliff, and the jump read as two different characters. Innes cut the scene
# rather than the artwork: "the creature's remorse at this point nobody
# cares". 39_victor_death becomes the last question and its `next` resolves
# to the ending.
CUT = ('40_creature_lament',)

SKIP = DEAD + CUT

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. Read off gridded contact sheets
# (rpg/README.md §3); the object is the one the clue talks about, and the
# panel goes on the picture's empty side so it never covers that object.
HOT = {
    'cover':                  ([7, 53, 10, 15], 'center', 'center'),   # the ship's lantern at Victor's rail
    'rules':                  ([14, 64, 12, 14], 'right',  'center', 60),   # the skull on the study table
    '03_arctic_rescue':       ([22, 78, 16, 14], 'right', 'center'),       # the broken ice under the sled
    '04_warning':             ([35, 19, 15, 16], 'right', 'center'),   # the cabin window, the Arctic he wants
    '05_lightning_oak':       ([57, 33, 15, 26], 'left',   'center'),       # the oak, with the bolt above it
    '05b_oak_burning':       ([58, 50, 14, 20], 'left',   'center'),       # the burning split trunk
    '06_ingolstadt':          ([30, 52, 13, 22], 'right',  'center'),       # Victor and his books on the university steps
    '07_research_choice':     ([79, 33, 12, 18], 'center', 'bottom'),        # the lit laboratory door, one of the two roads
    '08_cemetery':            ([57, 62,  8, 12], 'left', 'center'),       # the lantern at the grave
    '09_waldman':             ([72, 45, 12, 20], 'left', 'center'),   # the demonstration apparatus
    '10_build':               ([24, 30, 12, 20], 'right', 'center'),       # Victor, who will not stop
    '11_life':                ([86, 60, 14, 20], 'left', 'center'),       # the body taking the spark
    '12_awakening_choice':    ([44, 33, 10, 14], 'center', 'bottom'),        # Victor, deciding whether to speak
    '13_flee':                ([62, 48, 14, 26], 'left', 'center'),       # Victor running
    '14_speak':               ([48, 42, 12, 26], 'right',  'center', 42),   # the Creature he tries to address
    '15_henry':               ([60, 30, 14, 26], 'left', 'center'),       # Henry at the bedside
    '16_william':             ([30, 62, 10, 14], 'right', 'center'),   # the letter
    '17_justine':             ([78, 45, 16, 22], 'left',   'center', 56),   # the judges
    '18_alps':                ([82, 49, 18, 38], 'left', 'center'),       # the Creature on the glacier
    '19_cottage':             ([71, 65, 20, 18], 'left', 'center'),       # the lit cottage window
    '20_language':            ([38, 49, 13, 11], 'right',  'center'),       # the open book he found
    '21_approach_choice':     ([50, 38, 12, 14], 'center', 'bottom'),        # the Creature deciding how to approach
    '22_knock':               ([60, 38, 14, 22], 'left', 'center'),       # blind De Lacey
    '23_firewood':            ([58, 69, 16, 22], 'left', 'center'),       # the door he leaves the wood by
    '24_rejection_fire':      ([89, 47, 10, 13], 'left',   'center'),       # the dark, empty cottage
    '25_demand':              ([66, 28, 14, 18], 'left',   'center', 42),   # the vision of the companion
    '26_companion_choice':    ([21, 45, 10, 12], 'center', 'bottom', 44),   # the book Victor weighs it over
    '27_orkney':              ([85, 61, 16, 26], 'left', 'center'),       # the shrouded second creature
    '28_refuse':              ([18, 30, 12, 24], 'right', 'center'),   # Victor refusing
    '29_destroy':             ([70, 60, 14, 16], 'left', 'center'),       # the torn shroud
    '30_clerval_prison':      ([71, 42, 24, 28], 'left', 'center'),       # the officers on the shore
    '31_wedding_choice':      ([39, 32, 10, 13], 'center', 'bottom'),        # Elizabeth, who may or may not be told
    '32_confess':             ([68, 80, 14, 14], 'left',   'center'),       # the open book between them
    '33_guard':               ([76, 61, 10, 16], 'left', 'center'),       # the lantern on his lone watch
    '34_elizabeth':           ([63, 44, 18, 28], 'left', 'center'),   # Elizabeth on the bed
    '35_arctic_chase':        ([27, 75, 22, 18], 'right', 'center'),   # the dogs and the sled — the longest story in the lesson
    '36_walton_choice':       ([28, 24, 18, 18], 'right', 'center'),       # the ice through the cabin window
    '37_turn_south':          ([33, 72, 14, 16], 'right',  'center'),       # the ship's wheel
    # Re-read 2026-09-09 against the replacement plate. The old box was the
    # oversized Creature, who filled [72, 38, 12, 22]; at honest scale he is a
    # small figure further down the channel, so the old box now lands on empty
    # mist. Padded past his silhouette so the marker is a comfortable target.
    '38_pursue':              ([75, 61,  6, 10], 'left', 'center'),       # the figure still ahead
    '39_victor_death':        ([86, 54, 18, 24], 'left', 'center'),       # Victor
    '24_creature_to_geneva':  ([31, 25, 14, 20], 'right', 'center'),       # the Creature on the road
    '24_rescue_child':        ([72, 28, 12, 16], 'left', 'center'),   # the man raising his gun
    '24_william_frankenstein':([83, 69, 20, 28], 'left', 'center'),       # William
    # Was [78, 25] on the window: the marker landed on flat moonlight and
    # rendered as a pale blank blob. The clue names the locket, so the
    # locket is the object. Panel right and narrow — this plate is busy on
    # both sides, and 40% clears the locket and Justine's face.
    '24_portrait_justine':    ([46, 62,  7, 12], 'right',  'center', 40),   # the locket he is about to leave
    '29_storm_at_sea':        ([39, 67, 32, 24], 'right', 'center'),       # the storm at the window
    '30_return_home':         ([16, 46, 18, 36], 'right', 'center'),       # Elizabeth, told too little
    '09b_obsession':          ([32, 62, 12, 14], 'right', 'center'),   # the skull on the books
    '18a_pursuit':            ([88, 15,  9, 14], 'left',   'center'),       # the Creature on the ridge ahead
    '22b_return':             ([85, 43, 16, 40], 'left', 'center'),   # the doorway Felix comes through
    '35b_ship_rescue':        ([63, 28, 16, 14], 'left',   'center'),       # the trapped ship
    'end_mercy':              ([18, 45, 14, 30], 'right', 'center'),
    'end_warning':            ([42, 49, 20, 34], 'right', 'center'),
    'end_ice':                ([72, 45, 18, 26], 'left', 'center'),
    'end_fail':               ([30, 40, 16, 26], 'right', 'center'),
}

# ── the answer key. The export put it in slot 0 on all 44 questions; this
# deals it across the three, in the order the scenes are played. Written out
# rather than generated so it is reviewable and stable across runs — a hash
# of the scene id would reshuffle the whole lesson on any rename.
KEY = {
    '03_arctic_rescue': 1, '04_warning': 0, '05_lightning_oak': 2, '05b_oak_burning': 0, '06_ingolstadt': 1,
    '08_cemetery': 0, '09_waldman': 2, '10_build': 1, '11_life': 0, '13_flee': 2,
    '14_speak': 1, '15_henry': 0, '16_william': 2, '17_justine': 1, '18_alps': 0,
    '19_cottage': 2, '20_language': 1, '22_knock': 0, '23_firewood': 2,
    '24_rejection_fire': 1, '25_demand': 0, '27_orkney': 2, '28_refuse': 1,
    '29_destroy': 0, '30_clerval_prison': 2, '32_confess': 1, '33_guard': 0,
    '34_elizabeth': 2, '35_arctic_chase': 1, '37_turn_south': 0, '38_pursue': 2,
    '39_victor_death': 1, '24_creature_to_geneva': 2,
    '24_rescue_child': 1, '24_william_frankenstein': 0, '24_portrait_justine': 2,
    '29_storm_at_sea': 1, '30_return_home': 0, '09b_obsession': 2,
    '18a_pursuit': 1, '22b_return': 0, '35b_ship_rescue': 2,
}

# ── story rewrites. Only where the panel could not hold the copy.
# Emptied 2026-09-10. The Round 2 batch rewrote the story on all 47
# rendered scenes and capped every one at 22 English words, which is what
# these trims existed to do; and it replaced every option set, which is
# what the 35b entry existed to do. An override left here would silently
# beat the new text — data.json is the one source now.
STORY = {}

# ── option rewrites. Only where the export's own set broke a house gate.
OPTS = {}

# ── the rules briefing (kind `rules`), which the export had as one HTML blob.
# The five form cards and two use cards, glossed in the translations file.
def T(en):
    return {'en': en}


RULES = {
    'kind': 'rules', 'img': 'final_obsession',
    'k': T('BEFORE YOU BEGIN'),
    'title': T('Going To'),
    # No story line: the four cards and the note say all of it, and with a
    # gloss under every one of them the panel had nowhere to put a paragraph
    # that only repeated them.
    # Five cards, not four. `.rules-intro` is a two-column grid whose LAST
    # card spans both columns, so an even count leaves one card stranded
    # half-width on its own row and pushes the note out on its own — which is
    # how "USE 2 — STRONG EVIDENCE" ended up looking like an afterthought
    # rather than the partner of USE 1. Odd counts lay out 2+2+1.
    'rules': [
        {'name': T('FORM'), 'form': T('I am / he is / they are + going to + base verb.')},
        {'name': T('NEGATIVE'), 'form': T("am not / isn't / aren't + going to + base verb.")},
        {'name': T('QUESTION'), 'form': T('Am / Is / Are + subject + going to + base verb?')},
        {'name': T('USE 1 · A PLAN'), 'form': T('something you have already decided')},
        {'name': T('USE 2 · EVIDENCE'), 'form': T('something you can see is about to happen')},
    ],
    # Innes, 2026-09-10: "we dont need to talk about future simple or pres
    # cont in this legend, just make it neater and focus on going to
    # infinitive". The distractors are form errors, so the note names the one
    # rule they all break instead of contrasting three tenses.
    'note': T('The verb after to never changes: he is going to leave, not leaves and not leaving.'),
    'next': '03_arctic_rescue',
}


def place(sid, scene):
    # the export names its pictures without an extension; ours are all webp
    scene['img'] = scene['img'] + '.webp'
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    scenes = {
        'cover': place('cover', {
            'kind': 'intro', 'img': '01_cover',
            # The plate carries a painted FRANKENSTEIN wordmark again
            # (rpg/<slug>/make_cover.py), so the kicker no longer repeats it —
            # and the glossed title underneath is the subtitle, which is the
            # half that actually translates.
            'k': T('BLOCK CAMP · GOING TO'),
            'title': T('The Green Prometheus'),
            'story': T('Lightning. Secrets. A body built from many different parts. '
                       'Enter Frankenstein and guide the story with your choices.'),
            'start': T('BEGIN'),
            'small': T('Tap the glowing lantern to open each scene.'),
            'next': 'rules'}),
        'rules': place('rules', dict(RULES)),
    }

    for sid, s in DATA['scenes'].items():
        if sid in SKIP:
            continue
        base = {'img': s['image'], 'k': T(s['act']),
                'title': T(s['title']['en']),
                'story': T(STORY.get(sid) or s['story']['en'])}
        if s['kind'] == 'choice':
            base['kind'] = 'choice'
            base['routes'] = []
            for ch in s['choices']:
                r = {'name': T(ch['label']['en']), 'desc': T(ch['note']['en']),
                     'route': ch['route'], 'target': ch['next']}
                # 36_walton_choice is the one that decides the Arctic ending —
                # its own clue says so, in nine languages.
                # Turning for home is the branch the master ending describes
                # ("helped Walton choose people over glory"), so only that one
                # can be upgraded by a flawless run. Chasing north ends in the
                # ice however well you answered.
                if ch.get('final') == 'south':
                    r['ending'], r['master'] = 'mercy', True
                elif ch.get('final') == 'north':
                    r['ending'] = 'ice'
                base['routes'].append(r)
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['mission']['en'])
            base['prompt'] = T(s['prompt']['en'])
            texts = OPTS.get(sid) or [a['en'] for a in s['answers']]
            correct = texts[s['correct']]
            # deal the key to its slot without disturbing the distractors' order
            rest = [t for i, t in enumerate(texts) if i != s['correct']]
            slot = KEY[sid]
            order = rest[:slot] + [correct] + rest[slot:]
            base['opts'] = [T(t) for t in order]
            base['answer'] = slot
            base['points'] = 5
            if s.get('relic'):
                base['relic'] = True
            base['fb'] = T(s['explanation']['en'])
            nxt = s.get('next')
            base['next'] = nxt if nxt and nxt not in SKIP else 'resolve'
        scenes[sid] = place(sid, base)

    # the last question decides whether a flawless run reaches the master ending
    scenes['39_victor_death']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': e['image'], 'success': key in ('mercy', 'warning'),
            'k': T(e['eyebrow']['en']), 'title': T(e['title']['en']),
            'story': T(e['story']['en'])})

    # The most a player can actually score is not 5 x every question: the six
    # forks mean roughly a third of them are never seen on any one run. Taking
    # the total instead put 210 on the HUD when 180 is the ceiling, and made
    # the master ending — which resolve() gates on score >= max — unreachable.
    # Both are read off the longest path through the graph instead.
    def best(sid, seen=()):
        """(points, relics) still reachable from this scene."""
        if sid in seen or sid not in scenes:
            return (0, 0)
        s, seen = scenes[sid], seen + (sid,)
        if s['kind'] == 'ending':
            return (0, 0)
        if s['kind'] == 'choice':
            return max((best(r['target'], seen) for r in s['routes']), default=(0, 0))
        p, r = best(s['next'], seen) if s.get('next') != 'resolve' else (0, 0)
        if s['kind'] == 'question':
            return (p + s.get('points', 5), r + (1 if s.get('relic') else 0))
        return (p, r)

    max_score, max_relics = best('cover')
    n_q = sum(1 for s in scenes.values() if s['kind'] == 'question')
    print('  %d questions authored; the longest single run scores %d and collects %d spark(s)'
          % (n_q, max_score, max_relics))
    spec = {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Frankenstein: The Green Prometheus — Going To Voxel RPG (A2)',
        'description': 'An interactive A2 English lesson from Forbes English: '
                       'Frankenstein: The Green Prometheus — Going To Voxel RPG (A2).',
        'langs': LANGS,
        'accent': '#70A43A',        # camp 5, Going To, on the Block Camp route map
        'accent_ink': '#0b1a12', 'deep': '#0d1a0c', 'panel': 'rgba(10,18,9,.88)',
        'labels': {
            'tiles':  T('SPARKS'),
            'relic':  T('SPARK RECOVERED · +{p} POINTS'),
            'begin':  T('BEGIN'),
        },
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_warning', 'complete': 'end_mercy',
                    'missing': 'end_ice', 'failed': 'end_fail',
                    'mercy': 'end_mercy', 'ice': 'end_ice'},
        'max': max_score, 'points': 5, 'tiles': max_relics, 'chances': 3,
        'complete_score': round(max_score * 0.8),
    }
    return spec


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
