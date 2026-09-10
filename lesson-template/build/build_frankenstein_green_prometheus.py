#!/usr/bin/env python3
"""Frankenstein: The Green Prometheus — GOING TO voxel RPG (A2), in two parts.

    python3 lesson-template/build/build_frankenstein_green_prometheus.py

Writes TWO pages from one data.json, one translation set and one picture
directory:

    block-camp/frankenstein-green-prometheus-rpg.html   Part I: Ambitions
    block-camp/frankenstein-consequences-rpg.html       Part II: Consequences

The story breaks where Innes's two title lockups say it breaks — at the
Creature's awakening. Part I is the rise: the Arctic frame, the oak,
Ingolstadt, the workshop, the spark. Part II is everything that costs.

`img_dir` becomes `G.dir` as its last path segment, so both pages point at
block-camp/frankenstein-green-prometheus-rpg/ and every plate resolves from
either. No artwork is moved or duplicated.

Rebuilds those pages from
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
import copy, json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'frankenstein-green-prometheus-rpg'          # the picture directory, shared
PAGE = {1: 'frankenstein-green-prometheus-rpg',     # Part I keeps the published URL
        2: 'frankenstein-consequences-rpg'}
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

# ── where the story breaks in two. Everything not listed here (minus SKIP)
# is Part II, which opens on the choice Part I ends one beat before.
PART1 = ('03_arctic_rescue', '04_warning', '05_lightning_oak', '05b_oak_burning',
         '06_ingolstadt', '07_research_choice', '08_cemetery', '09_waldman',
         '09b_obsession', '10_build', '11_life')

# The last question of each part: resolve() gates the master ending on the
# final answer being right, so each page needs its own.
FINAL = {1: '11_life', 2: '39_victor_death'}

# Part I carried one relic, and one spark makes `state.tiles >= G.tiles`
# true for anyone who finds it — no tension at all. The strike itself is
# the obvious second.
RELIC_ADD = ('05_lightning_oak',)

# Part I's endings. There is no spare artwork — all 56 plates are already
# spoken for — so two of these borrow a plate from inside Part I's own run
# and the third reuses Part II's purpose-built fail plate, which a Part I
# player never sees. `master` and `complete` share a scene, which is what
# Part II already does with `mercy`. If Innes commissions three more plates,
# only the `img` values here change.
P1_ENDINGS = {
    'p1_end_alive': ('12_awakening_choice', True,
                     'END OF PART I · THE SPARK TAKES', 'The Eyes Open',
                     'The body breathes. Victor is going to spend the rest of his life '
                     'answering for this. Part II begins here.'),
    'p1_end_sparks': ('10_build', True,
                      'END OF PART I · A SPARK LEFT BEHIND', 'The Bench Is Not Clear',
                      'The Creature lives, but you walked past a spark on the way. '
                      'Run Part I again and take them both.'),
    # word for word Part II's fail screen, so it costs no new gloss
    'p1_end_fail': ('44_ending_fail', False,
                    'FAILED EXPERIMENT', 'TRY THE FORM AGAIN',
                    'Too many answers went wrong. Build the pattern again: '
                    'AM / IS / ARE + GOING TO + base verb.'),
}

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. Read off gridded contact sheets
# (rpg/README.md §3); the object is the one the clue talks about, and the
# panel goes on the picture's empty side so it never covers that object.
HOT = {
    # The cover is the original hero again, so the lantern of the Round 2
    # arctic plate is gone: the glow is the green column of the apparatus.
    # The panel is anchored BOTTOM, not centre, because the painted lockup
    # now occupies the sky — see make_cover.py for how the band is measured.
    'cover':                  ([69, 66, 10, 20], 'left',   'bottom', 46),  # the lit column of the apparatus, low enough to clear the lockup
    'rules':                  ([14, 64, 12, 14], 'right',  'center', 60),   # the skull on the study table
    '03_arctic_rescue':       ([22, 78, 16, 14], 'right', 'center'),       # the broken ice under the sled
    '04_warning':             ([35, 19, 15, 16], 'right', 'center'),   # the cabin window, the Arctic he wants
    '05_lightning_oak':       ([57, 33, 15, 26], 'left',   'center', 38),       # the oak, with the bolt above it
    '05b_oak_burning':       ([58, 50, 14, 20], 'left',   'center'),       # the burning split trunk
    '06_ingolstadt':          ([30, 52, 13, 22], 'right',  'center'),       # Victor and his books on the university steps
    '07_research_choice':     ([79, 33, 12, 18], 'center', 'bottom'),        # the lit laboratory door, one of the two roads
    '08_cemetery':            ([57, 62,  8, 12], 'left', 'center'),       # the lantern at the grave
    '09_waldman':             ([72, 45, 12, 20], 'left', 'center'),   # the demonstration apparatus
    '10_build':               ([24, 30, 12, 20], 'right', 'center'),       # Victor, who will not stop
    '11_life':                ([86, 60, 14, 20], 'left', 'center'),       # the body taking the spark
    '12_awakening_choice':    ([44, 33, 10, 14], 'center', 'bottom'),        # Victor, deciding whether to speak
    '13_flee':                ([62, 48, 14, 26], 'left', 'center'),       # Victor running
    '14_speak':               ([48, 42, 12, 26], 'right',  'center', 34),   # the Creature he tries to address
    '15_henry':               ([60, 30, 14, 26], 'left', 'center'),       # Henry at the bedside
    '16_william':             ([30, 62, 10, 14], 'right', 'center'),   # the letter
    '17_justine':             ([78, 45, 16, 22], 'left',   'center', 56),   # the judges
    '18_alps':                ([82, 49, 18, 38], 'left', 'center'),       # the Creature on the glacier
    '19_cottage':             ([71, 65, 20, 18], 'left', 'center'),       # the lit cottage window
    '20_language':            ([38, 49, 13, 11], 'right',  'center'),       # the open book he found
    '21_approach_choice':     ([50, 38, 12, 14], 'center', 'bottom'),        # the Creature deciding how to approach
    '22_knock':               ([60, 38, 14, 22], 'left', 'center'),       # blind De Lacey
    '23_firewood':            ([58, 69, 16, 22], 'left',   'center', 38),       # the door he leaves the wood by
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
    '29_storm_at_sea':        ([39, 67, 32, 24], 'right',  'center', 34),       # the storm at the window
    '30_return_home':         ([16, 46, 18, 36], 'right', 'center'),       # Elizabeth, told too little
    '09b_obsession':          ([32, 62, 12, 14], 'right', 'center'),   # the skull on the books
    '18a_pursuit':            ([88, 15,  9, 14], 'left',   'center'),       # the Creature on the ridge ahead
    '22b_return':             ([85, 43, 16, 40], 'left', 'center'),   # the doorway Felix comes through
    '35b_ship_rescue':        ([63, 28, 16, 14], 'left',   'center'),       # the trapped ship
    'end_mercy':              ([18, 45, 14, 30], 'right', 'center'),
    'end_warning':            ([42, 49, 20, 34], 'right', 'center'),
    'end_ice':                ([72, 45, 18, 26], 'left', 'center'),
    'end_fail':               ([30, 40, 16, 26], 'right', 'center'),
    # Part II's cover. The marker is Walton's bearded stranger, low enough on
    # his coat to leave his face clear, and at cy 58 the picture is bottom-
    # aligned exactly as Part I's is — which is why one pair of make_cover.py
    # constants serves both plates. Panel right, because he is on the left.
    'cover2':                 ([15, 58, 10, 18], 'right',  'bottom', 54),
    'p1_end_alive':           ([44, 33, 10, 14], 'center', 'bottom'),
    'p1_end_sparks':          ([24, 30, 12, 20], 'right',  'center'),
    'p1_end_fail':            ([30, 40, 16, 26], 'right',  'center'),
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
        {'name': T('FORM · AM / IS / ARE + GOING TO'), 'form': T('I AM going to leave · she IS going to leave · they ARE going to leave')},
        {'name': T("NEGATIVE · AM NOT / ISN'T / AREN'T"), 'form': T("He ISN'T going to wait. · They AREN'T going to follow.")},
        {'name': T('QUESTION · AM / IS / ARE + SUBJECT'), 'form': T("IS he going to speak? · Yes, he IS. / No, he ISN'T.")},
        {'name': T('USE 1 · A PLAN'), 'form': T('He has decided. He IS GOING TO study science.')},
        {'name': T('USE 2 · EVIDENCE'), 'form': T('Look at the sky. The storm IS GOING TO break.')},
    ],
    # Innes, 2026-09-10: "we dont need to talk about future simple or pres
    # cont in this legend, just make it neater and focus on going to
    # infinitive". The distractors are form errors, so the note names the one
    # rule they all break instead of contrasting three tenses.
    'note': T('Never lose the BE and never lose the TO. The verb after TO never changes: he is going to LEAVE, never LEAVES and never LEAVING.'),
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


def build(part):
    first = 'cover' if part == 1 else 'cover2'
    # the scenes this part owns; a `next` that points outside it resolves
    keep = {sid for sid in DATA['scenes']
            if sid not in SKIP and (sid in PART1) == (part == 1)}
    scenes = {
        first: place(first, {
            'kind': 'intro', 'img': '01_cover' if part == 1 else '01_cover_part2',
            # No `title`. The plate carries Innes's painted lockup, which
            # already reads FRANKENSTEIN: THE GREEN PROMETHEUS — a typeset h1
            # under it only says the same thing a second time, and it was
            # eating the height the lockup needs. The engine now skips the h1
            # when a scene has no title, and takes the image's alt text from
            # `alt` instead. The kicker stays: it names the grammar, which the
            # lockup does not, and it is the line that actually translates.
            'k': T('BLOCK CAMP · GOING TO'),
            'alt': ('Frankenstein: The Green Prometheus — Victor at the lightning apparatus'
                    if part == 1 else
                    'Frankenstein: The Green Prometheus, Part II — Walton\'s ship in the Arctic ice'),
            # One sentence, not two. The painted lockup owns the top of the
            # plate now, so every line the panel does not need is height the
            # title treatment gets back.
            'story': T('Lightning, secrets, and a body built from many different parts.'
                       if part == 1 else
                       'The Creature is awake and Victor is running. '
                       'Everything from here is what that night cost.'),
            'start': T('BEGIN'),
            # The lantern belonged to the Round 2 Arctic plate, and the
            # line repeated the corner help besides. Wonderland's shape
            # instead: what the player is about to get.
            'small': T('One player · A2 · one choice · three endings' if part == 1 else
                       'One player · A2 · five choices · four endings'),
            'next': 'rules'}),
        # Both parts open on the same briefing. It is the same grammar and the
        # same spellbook; a player who arrives at Part II without Part I still
        # needs it, and one who played both is not told anything new.
        'rules': place('rules', dict(copy.deepcopy(RULES),
                                     next='03_arctic_rescue' if part == 1
                                     else '12_awakening_choice')),
    }

    for sid, s in DATA['scenes'].items():
        if sid in SKIP or ((sid in PART1) != (part == 1)):
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
            if s.get('relic') or sid in RELIC_ADD:
                base['relic'] = True
            base['fb'] = T(s['explanation']['en'])
            nxt = s.get('next')
            base['next'] = nxt if nxt and nxt not in SKIP and nxt in keep else 'resolve'
        scenes[sid] = place(sid, base)

    # the last question decides whether a flawless run reaches the master ending
    scenes[FINAL[part]]['final'] = True

    if part == 1:
        for sid, (img, ok, k, title, story) in P1_ENDINGS.items():
            e = {'kind': 'ending', 'img': img, 'success': ok,
                 'k': T(k), 'title': T(title), 'story': T(story)}
            # "Part II begins here" is a promise the page has to keep. Only the
            # ending that actually reaches the awakening carries the link — the
            # other two want the player to run Part I again, not skip it.
            if sid == 'p1_end_alive':
                e['link'] = '/block-camp/%s.html' % PAGE[2]
                e['linkLabel'] = T('PLAY PART II')
            scenes[sid] = place(sid, e)
    else:
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

    max_score, max_relics = best(first)
    n_q = sum(1 for s in scenes.values() if s['kind'] == 'question')
    print('  part %d: %d questions authored; the longest single run scores %d '
          'and collects %d spark(s)' % (part, n_q, max_score, max_relics))
    title = ('Frankenstein Part I: Ambitions — Going To Voxel RPG (A2)' if part == 1 else
             'Frankenstein Part II: Consequences — Going To Voxel RPG (A2)')
    spec = {
        'file': 'block-camp/%s.html' % PAGE[part],
        # Both pages read the same folder: G.dir is img_dir's last segment,
        # and both pages sit in block-camp/, so the relative path resolves.
        'img_dir': 'block-camp/%s' % SLUG,
        'title': title,
        'description': 'An interactive A2 English lesson from Forbes English: %s.' % title,
        'langs': LANGS,
        'accent': '#70A43A',        # camp 5, Going To, on the Block Camp route map
        'accent_ink': '#0b1a12', 'deep': '#0d1a0c', 'panel': 'rgba(10,18,9,.88)',
        'labels': {
            'tiles':  T('SPARKS'),
            'relic':  T('SPARK RECOVERED · +{p} POINTS'),
            'begin':  T('BEGIN'),
        },
        'start': first, 'scenes': scenes,
        'endings': ({'master': 'p1_end_alive', 'complete': 'p1_end_alive',
                     'missing': 'p1_end_sparks', 'failed': 'p1_end_fail'} if part == 1 else
                    {'master': 'end_warning', 'complete': 'end_mercy',
                     'missing': 'end_ice', 'failed': 'end_fail',
                     'mercy': 'end_mercy', 'ice': 'end_ice'}),
        'max': max_score, 'points': 5, 'tiles': max_relics, 'chances': 3,
        'complete_score': round(max_score * 0.8),
    }
    return spec


if __name__ == '__main__':
    for part in (1, 2):
        rpg.assemble(rpg.apply_translations(build(part),
                                            os.path.join(BASE, 'translations')))
