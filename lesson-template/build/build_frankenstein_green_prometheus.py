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
    item at `40_creature_lament`, where the correct option was the only one
    written out in full. OPTS below levels the three.

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

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. Read off gridded contact sheets
# (rpg/README.md §3); the object is the one the clue talks about, and the
# panel goes on the picture's empty side so it never covers that object.
HOT = {
    'cover':                  ([72, 30, 16, 24], 'left', 'center'),
    'rules':                  ([14, 64, 12, 14], 'right',  'center', 60),   # the skull on the study table
    '03_arctic_rescue':       ([22, 78, 16, 14], 'right', 'center'),       # the broken ice under the sled
    '04_warning':             ([35, 19, 15, 16], 'right', 'center'),   # the cabin window, the Arctic he wants
    '05_lightning_oak':       ([64, 25, 14, 26], 'left',   'center'),       # the struck tree
    '06_ingolstadt':          ([64, 24, 18, 24], 'left', 'center'),       # the university towers
    '07_research_choice':     ([52, 86, 12, 12], 'center', 'top'),          # Victor where the road divides
    '08_cemetery':            ([57, 62,  8, 12], 'left', 'center'),       # the lantern at the grave
    '09_waldman':             ([72, 45, 12, 20], 'left', 'center'),   # the demonstration apparatus
    '10_build':               ([24, 30, 12, 20], 'right', 'center'),       # Victor, who will not stop
    '11_life':                ([72, 32, 16, 26], 'left', 'center'),       # the body taking the spark
    '12_awakening_choice':    ([45, 86, 12, 12], 'center', 'top'),          # the hand between them
    '13_flee':                ([62, 48, 14, 26], 'left', 'center'),       # Victor running
    '14_speak':               ([38, 45, 16, 28], 'right', 'center'),       # the Creature he might address
    '15_henry':               ([60, 30, 14, 26], 'left', 'center'),       # Henry at the bedside
    '16_william':             ([30, 62, 10, 14], 'right', 'center'),   # the letter
    '17_justine':             ([78, 45, 16, 22], 'left',   'center', 56),   # the judges
    '18_alps':                ([78, 26, 14, 28], 'left', 'center'),       # the Creature on the glacier
    '19_cottage':             ([66, 60, 14, 14], 'left', 'center'),       # the lit cottage window
    '20_language':            ([21, 56, 10, 12], 'right', 'center'),       # the book
    '21_approach_choice':     ([52, 86, 14, 12], 'center', 'top'),          # the Creature deciding
    '22_knock':               ([60, 38, 14, 22], 'left', 'center'),       # blind De Lacey
    '23_firewood':            ([80, 46, 12, 16], 'left',   'center'),       # the door he leaves the wood by
    '24_rejection_fire':      ([78, 48, 14, 12], 'left', 'center'),       # the dark cottage
    '25_demand':              ([66, 28, 14, 18], 'left',   'center', 42),   # the vision of the companion
    '26_companion_choice':    ([60, 86, 12, 12], 'center', 'top'),          # Victor weighing it
    '27_orkney':              ([35, 58, 16, 12], 'right', 'center'),       # the shrouded second creature
    '28_refuse':              ([18, 30, 12, 24], 'right', 'center'),   # Victor refusing
    '29_destroy':             ([70, 60, 14, 16], 'left', 'center'),       # the torn shroud
    '30_clerval_prison':      ([40, 42, 16, 18], 'right', 'center'),       # the officers on the shore
    '31_wedding_choice':      ([55, 86, 10, 12], 'center', 'top'),          # the lantern
    '32_confess':             ([68, 80, 14, 14], 'left',   'center'),       # the open book between them
    '33_guard':               ([57, 52,  8, 12], 'left', 'center'),       # the lantern on his lone watch
    '34_elizabeth':           ([72, 58, 18, 16], 'left', 'center'),   # Elizabeth on the bed
    '35_arctic_chase':        ([28, 62, 18, 14], 'right', 'center'),   # the dogs and the sled — the longest story in the lesson
    '36_walton_choice':       ([28, 24, 18, 18], 'right', 'center'),       # the ice through the cabin window
    '37_turn_south':          ([33, 72, 14, 16], 'right',  'center'),       # the ship's wheel
    '38_pursue':              ([72, 38, 12, 22], 'left', 'center'),       # the figure still ahead
    '39_victor_death':        ([72, 45, 14, 20], 'left', 'center'),       # Victor
    '40_creature_lament':     ([58, 36, 10, 14], 'left', 'center'),   # the lamp at the cabin window
    '24_creature_to_geneva':  ([18, 38, 14, 30], 'right', 'center'),       # the Creature on the road
    '24_rescue_child':        ([72, 28, 12, 16], 'left', 'center'),   # the man raising his gun
    '24_william_frankenstein':([60, 60, 12, 18], 'left', 'center'),       # William
    '24_portrait_justine':    ([78, 25, 14, 22], 'left',   'center', 52),   # the Creature at the window
    '29_storm_at_sea':        ([23, 28, 12, 16], 'right', 'center'),       # the storm at the window
    '30_return_home':         ([25, 45, 12, 24], 'right', 'center'),       # Elizabeth, told too little
    '09b_obsession':          ([32, 62, 12, 14], 'right', 'center'),   # the skull on the books
    '18a_pursuit':            ([17, 60,  8, 12], 'right',  'center', 54),   # his lantern in the pass
    '22b_return':             ([85, 45, 12, 20], 'left', 'center'),   # the doorway Felix comes through
    '35b_ship_rescue':        ([65, 28, 16, 14], 'left', 'center'),   # the trapped ship
    'end_mercy':              ([18, 45, 14, 30], 'right', 'center'),
    'end_warning':            ([25, 45, 20, 30], 'right', 'center'),
    'end_ice':                ([72, 45, 18, 26], 'left', 'center'),
    'end_fail':               ([30, 40, 16, 26], 'right', 'center'),
}

# ── the answer key. The export put it in slot 0 on all 44 questions; this
# deals it across the three, in the order the scenes are played. Written out
# rather than generated so it is reviewable and stable across runs — a hash
# of the scene id would reshuffle the whole lesson on any rename.
KEY = {
    '03_arctic_rescue': 1, '04_warning': 0, '05_lightning_oak': 2, '06_ingolstadt': 1,
    '08_cemetery': 0, '09_waldman': 2, '10_build': 1, '11_life': 0, '13_flee': 2,
    '14_speak': 1, '15_henry': 0, '16_william': 2, '17_justine': 1, '18_alps': 0,
    '19_cottage': 2, '20_language': 1, '22_knock': 0, '23_firewood': 2,
    '24_rejection_fire': 1, '25_demand': 0, '27_orkney': 2, '28_refuse': 1,
    '29_destroy': 0, '30_clerval_prison': 2, '32_confess': 1, '33_guard': 0,
    '34_elizabeth': 2, '35_arctic_chase': 1, '37_turn_south': 0, '38_pursue': 2,
    '39_victor_death': 1, '40_creature_lament': 0, '24_creature_to_geneva': 2,
    '24_rescue_child': 1, '24_william_frankenstein': 0, '24_portrait_justine': 2,
    '29_storm_at_sea': 1, '30_return_home': 0, '09b_obsession': 2,
    '18a_pursuit': 1, '22b_return': 0, '35b_ship_rescue': 2,
}

# ── story rewrites. Only where the panel could not hold the copy.
STORY = {
    # The export's median story is 21 words, the Lost Yellow Road range. The
    # scenes its late patches rewrote run 38-68 words, and those are exactly
    # the panels that scroll once a gloss sits under every line. README §1
    # offers two levers, and widening past ~56% only moves the problem (a
    # 64% panel then covers the object it grew out of), so these are cut to
    # the length the rest of the lesson already uses. The nine glosses were
    # cut to match by sentence index, never by chopping the tail: 16_william
    # keeps its first and last sentence because the missing locket is what
    # 17_justine and 24_portrait_justine both turn on.
    '04_warning': 'Walton speaks eagerly about the glory he hopes to win in the Arctic.',
    '09_waldman': (
        'At Ingolstadt, Victor attends Professor Waldman\'s anatomy lecture in a '
        'grand theatre of science. He watches controlled experiments with '
        'chemistry and electricity, and the display awakens his ambition.'
    ),
    '09b_obsession': (
        'Waldman\'s lecture stays in Victor\'s mind. He begins spending long '
        'nights alone with anatomy books, chemical notes and studies of decay.'
    ),
    '16_william': (
        'Victor learns that his young brother William has been murdered outside '
        'Geneva. Victor realizes the terrible truth — and the locket is missing.'
    ),
    '17_justine': (
        'The missing locket is suddenly found in the pocket of Justine Moritz, a '
        'kind young woman who lives with Victor\'s family. Justine says she never '
        'took it.'
    ),
    '18_alps': (
        'Victor finally tracks the Creature down on the glacier. He expects a '
        'fight, but the Creature turns to face him and demands to be heard.'
    ),
    '22b_return': (
        'For one brief moment, blind De Lacey listens without fear. Felix '
        'returns, sees the Creature beside his father and attacks before hearing '
        'an explanation.'
    ),
    '24_creature_to_geneva': (
        'After losing the De Laceys, the Creature leaves the valley and travels '
        'toward Geneva. He is wounded by rejection but still remembers every '
        'small kindness he has witnessed.'
    ),
    '24_rejection_fire': (
        'Felix attacks the Creature before listening, and the De Lacey family '
        'abandons the cottage. The Creature returns and stares at the dark, empty '
        'home.'
    ),
    '24_rescue_child': (
        'Near a rushing river, a little girl falls into the water. The Creature '
        'jumps in and saves her.'
    ),
    '24_william_frankenstein': (
        'Near Geneva, the Creature meets a young boy named William. William '
        'recoils in fear and reveals that he is a Frankenstein, turning the '
        'Creature\'s anger back toward Victor\'s family.'
    ),
    '28_refuse': (
        'The Creature wants Victor to make him a companion so he will not be '
        'alone. Victor refuses at first.'
    ),
    '34_elizabeth': (
        'On the wedding night, the Creature keeps his promise and kills '
        'Elizabeth. With no one able to stop the Creature, Victor swears to hunt '
        'him himself.'
    ),
    '35_arctic_chase': (
        'The chase lasts for months. Farther north, he buys dogs and a sled and '
        'follows the Creature onto the frozen sea.'
    ),
    '35b_ship_rescue': (
        'His dogs are gone, his sled is breaking, and he collapses on the frozen '
        'sea. Through the ice and green light, Walton\'s trapped ship appears.'
    ),
    '36_walton_choice': (
        'Days later, the trapped crew begs Walton to turn south if the ice opens. '
        'Walton must decide whether to protect the people around him or continue '
        'chasing glory.'
    ),
}

# ── option rewrites. Only where the export's own set broke a house gate.
OPTS = {
    # The key was the only option written out in full — 56 characters against
    # 38 and 47, which is scoreable without reading the grammar. All three now
    # carry the same tail, and the apostrophes are straight (the export mixed
    # curly and straight across the three).
    '40_creature_lament': ["No, he isn't. He's going to disappear into the darkness.",
                           "No, he doesn't. He going to disappear into the darkness.",
                           "No, he isn't going disappear into the darkness."],
    # "are going to" was the longest by a character. The third option now
    # carries a real learner error — be + going to + be — and is the longest.
    '35b_ship_rescue': ['are going to', 'is going to', 'are going to be'],
}

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
    'rules': [
        {'name': T('FORM'), 'form': T('I am / he is / they are + going to + base verb.')},
        {'name': T('NEGATIVE'), 'form': T("am not / isn't / aren't + going to + base verb.")},
        {'name': T('QUESTION'), 'form': T('Am / Is / Are + subject + going to + base verb?')},
        {'name': T('INTENTIONS'), 'form': T('a plan already decided')},
    ],
    'note': T('USE 2 — STRONG EVIDENCE: a prediction based on what you can see now.'),
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
            # "Frankenstein:" alone is 86px wider than the 46% panel at cover
            # size and does not break, so the name rides the kicker and the
            # subtitle carries the title. The full name is still the <title>.
            'k': T('FRANKENSTEIN · GOING TO'),
            'title': T('The Green Prometheus'),
            'story': T('Lightning. Secrets. A body built from many different parts. '
                       'Enter Frankenstein and guide the story with your choices.'),
            'start': T('BEGIN'),
            'small': T('Tap the glowing lantern to open each scene.'),
            'next': 'rules'}),
        'rules': place('rules', dict(RULES)),
    }

    for sid, s in DATA['scenes'].items():
        if sid in DEAD:
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
            base['next'] = nxt if nxt and nxt not in DEAD else 'resolve'
        scenes[sid] = place(sid, base)

    # the last question decides whether a flawless run reaches the master ending
    scenes['40_creature_lament']['final'] = True

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
