#!/usr/bin/env python3
"""Nautilus: The Black Archive — Present Perfect RPG on the painted plates (B1).

    py lesson-template/build/build_nautilus_black_archive_deep.py

Builds block-camp/nautilus-black-archive-deep-rpg.html from
lesson-template/build/rpg/nautilus-black-archive-deep-rpg/data.json — the text
of `Nautilus_20000_Leagues_RPG_Revamped.html`, pulled out by
rpg/extract_static.py, which is the same static-markup export kind as the voxel
edition (that builder's docstring has the detail).

**The painted skin, published as it stands.** The voxel edition
(`build_nautilus_black_archive.py`) and this one are the same adventure in two
art styles, and on 2026-09-13 the painted one was first rewritten into a
different grammar point to avoid a duplicate — `build_twenty_thousand_leagues.py`,
Past Perfect, B1-B2. Innes asked on 2026-09-13 for the painted skin to be
published in its own right as well, with its own Present Perfect text: three
editions of one dive, and a student picks the art and the tense. The two
Present Perfect editions differ in exactly two strings, both of them scenery —
the export's own "a city beneath the seabed" for "a city built from forgotten
blocks", and an Aronnax line that matches the painted plate. Everything else,
all 27 questions included, is byte-identical, which is deliberate: the lesson
is the same lesson.

So this builder is the voxel one with three things changed and nothing else:

  * **The hotspot table**, read off the painted plates. Those are the same
    plates the Sealed Log uses, so its table is the base here — see below for
    the three entries the upgraded artwork moved.
  * **Turquoise, not rose.** Camp 8's `#46B0AB`, the voxel edition's accent
    and the export's own — Innes asked for turquoise rather than the Sealed
    Log's `#d66d77` when he asked for this edition.
  * **A narrower briefing panel.** Two rule cards here against the Sealed
    Log's four, so 60% rather than 70%.

**The artwork is the upgraded set** (`Revamped (3)`, 2026-09-13). Measured
against the plates the Sealed Log shipped with: 34 of the 40 are the same
picture at a higher bitrate (mean abs. difference ~0.3/255 on a 192x108
greyscale, i.e. encoder noise), and six are genuinely redrawn. Two of the six
are recomposed and move their hotspot — `brief`, where the chart table swings
from Nemo's hand at the right edge to the centre of the frame, and `log`, where
Aronnax stops closing the journal amid flying pages and sits writing it by
lamplight. Four are the same composition with the divers newly helmeted
(`tdec`, `tstatue`, `t4`, `finaldec`); of those only `t4` needed its hotspot
moved, and because it sat on the edge of the glowing plate rather than because
the picture changed.

Pictures: block-camp/nautilus-black-archive-deep-rpg/NN_name.webp, **1536x864** —
16:9, so the spec passes img_w and img_h.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'nautilus-black-archive-deep-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

BULLET, DASH = '·', '—'
SKIP = ('map',)          # the teacher's expedition index, not a scene of the game

# ── hotspots: [cx, cy, w, h] in % of the 1536x864 picture, then panel side,
# vertical anchor, optional panel width %. These are the painted plates, so the
# table starts from the one build_twenty_thousand_leagues.py read off the same
# pictures (README section 3) rather than from the voxel edition's, whose art is
# composed differently on every frame. Three entries differ from it, all three
# because the upgraded artwork moved the object:
#
#   brief  the chart table was under Nemo's hand at the right edge; it is now
#          the centre of the frame with Nemo pointing in from the right, so the
#          glow moves to the lit ruins on the chart and the panel takes the dark
#          bulkhead on the left. 60% here against the Sealed Log's 70% — two
#          rule cards, not four.
#   log    Aronnax was closing the journal with pages in the water; he is now
#          writing it by lamplight, and the open book sits three points lower.
#   t4     unchanged in composition, but the old entry sat on the lower-left
#          corner of the etched plate and caught the diver's glove. Centred on
#          the glowing chart, which the new helmet does not reach.
#
# The painted plates put their subject mid-frame more often than the voxel ones,
# so several panels are narrowed rather than moved: a gloss language widens the
# panel by 8 points and a 46% left panel reaches x=54. check-rpg-panels.js
# measures the result.
HOT = {
    'intro':     ([63, 18, 36, 22], 'left',   'center'),       # the Nautilus, lamps on, above the drowned city
    'brief':     ([74, 72, 18, 18], 'left',   'center', 60),   # the lit ruins on the chart table, under Nemo's finger
    'q0':        ([87, 24, 14, 14], 'left',   'center'),       # the headlamp on the bow
    'leak':      ([28, 55, 18, 22], 'right',  'center'),       # the valve wheel Lia is closing
    'route':     ([69, 47, 14, 18], 'left',   'center'),       # the crystal where the seabed splits
    'c1':        ([30, 52, 18, 40], 'right',  'center'),       # the diver on the line
    'cbad':      ([90, 57, 14, 20], 'left',   'center'),       # the gauge in the diver's hand
    'c2':        ([14, 70, 18, 20], 'right',  'center'),       # the net of black pearls
    'cdec':      ([93, 81, 10, 14], 'left',   'center'),       # the broken lamp by the trapped diver's hand
    'crescue':   ([16, 55, 20, 26], 'right',  'center'),       # the trapped diver's helmet
    'csignal':   ([80, 36, 26, 40], 'left',   'center'),       # the turquoise aperture
    'c4':        ([80, 42, 36, 55], 'left',   'center'),       # the dome under the reef
    't1':        ([70, 22, 18, 28], 'left',   'center'),       # the warm lights inside the ruins
    'tbad':      ([28, 42, 22, 24], 'right',  'center'),       # the starboard plates on the gate
    't2':        ([77, 61, 12, 14], 'left',   'center'),       # Mara's lamp on the carved wall
    'tdec':      ([80, 62, 18, 22], 'left',   'center'),       # the turquoise mark on the floor
    'tarchive':  ([54, 38, 18, 24], 'left',   'center', 38),   # the tablets in Aronnax's hands, mid-frame
    'tstatue':   ([90, 50, 18, 50], 'left',   'center'),       # the ringed door
    't4':        ([78, 50, 28, 44], 'left',   'center', 38),   # the etched chart, glowing; a gloss panel reaches x=46
    'log':       ([66, 79, 22, 16], 'left',   'center'),       # the open journal he is writing in
    'engine':    ([22, 35, 34, 34], 'right',  'center'),       # the pressure drive
    'ballast':   ([10, 63, 16, 20], 'right',  'center', 40),   # the ballast valve wheel, bottom left; the dark hull is the empty side
    'repairdec': ([57, 47, 30, 40], 'left',   'center', 38),   # the airlock wheel, mid-frame
    'i1':        ([33, 54, 26, 28], 'right',  'center'),       # the regulator in Lia's hands, sparking
    'i2':        ([12, 28, 10, 14], 'right',  'center'),       # the coolant tap
    'i3':        ([24, 26, 40, 44], 'right',  'center'),       # the power cells
    'o1':        ([12, 33, 14, 16], 'right',  'center'),       # Nadia's helmet lamp
    'o2':        ([38, 66, 12, 14], 'right',  'center'),       # the repair tool's light on the fracture
    'o3':        ([75, 12, 16, 18], 'left',   'center'),       # the eye above Nadia
    'squidq':    ([87, 20, 12, 16], 'left',   'center'),       # the squid's eye, clear of the HUD corner
    'tentacle':  ([76, 68, 26, 30], 'left',   'center'),       # the torn rail
    'finaldec':  ([88, 82, 22, 26], 'left',   'center'),       # the helm
    'ft1':       ([20, 50, 38, 55], 'right',  'center'),       # the pearl trail
    'ft2':       ([72, 55, 30, 45], 'left',   'center'),       # the squid in the crystals
    'ft3':       ([75, 58, 30, 22], 'left',   'center'),       # the Nautilus slipping past
    'fc1':       ([90, 25, 16, 30], 'left',   'center'),       # the arch Mara calls out
    'fc2':       ([78, 18, 28, 32], 'left',   'center'),       # the falling tower
    'fc3':       ([78, 45, 36, 40], 'left',   'center'),       # the Nautilus in the narrow arch
    'archive':   ([70, 35, 40, 45], 'left',   'center', 40),   # the archive core
    # the four endings, on their own plates
    'end_master':   ([81, 9, 12, 14], 'left', 'center'),       # the case held up in daylight
    'end_complete': ([70, 35, 40, 45], 'left', 'center', 40),  # the archive core
    'end_missing':  ([90, 50, 18, 50], 'left', 'center'),      # the ringed door, still shut
    'end_failed':   ([76, 68, 26, 30], 'left', 'center'),      # the rail the squid tore away
}

# ── a plate for each ending. The export had one #end screen and chose its
# words in JavaScript, so three of these reuse a plate from deep in the game;
# endings are terminal, where a repeat does not read as one.
END_IMG = {
    'master':   '40_end.webp',       # the crew surfaced, the case aboard
    'complete': '39_archive.webp',   # the core, read but not carried
    'missing':  '18_tstatue.webp',   # the bronze door that never opened
    'failed':   '31_tentacle.webp',  # the rail the kraken tore away
}


# ── distractors the export got wrong, replaced one string at a time.
#
# Two faults, and one fix for both. HOUSE-STYLE's hard gate says the key must
# never be the longest option, and on a present-perfect-continuous item it
# always is: "has been searching" is six characters longer than "has searched"
# because the form is longer. Four questions failed the gate. Separately, some
# distractors are not English at all — "is call", "is translate", "translated
# since" — and a B1 student strikes those out without reading the sentence,
# which turns a four-way item into a two-way one.
#
# Replacing the junk with a grammatical past-perfect-continuous distractor
# fixes both: it is wrong for a sentence anchored in the present, it is as
# plausible as the key to someone who has not learned the contrast, and it is
# the same length, so the key stops being the giveaway. The simple-form
# distractor stays on every item — it is the contrast being taught.
OPTS_FIX = {
    'q0':      {'searched': 'had been searching'},
    'c1':      {'descended': 'had been descending', 'are descended': 'are descending'},
    'crescue': {'called': 'had been calling', 'is call': 'is calling'},
    't2':      {'is translate': 'had been translating', 'translated since': 'translated'},
}


# ── the briefing, rewritten for this engine's HUD.
#
# The export tracked a hull bar and an oxygen bar, and its briefing says so:
# "Wrong answers cost hull and oxygen". README section 9 keeps an export's
# rules only where this engine has them, and it has neither — it counts
# points, shards and three chances — so the shipped sentence described a
# penalty a student could not see anywhere on the page. This one names what
# the HUD actually counts, and is a sentence shorter, which is also what
# takes the Spanish briefing panel back inside its frame.
BRIEF_STORY = ("Send the right commands to keep the Nautilus alive. Choose the best tense "
               "for the meaning: a completed result, or an activity continuing up to now. "
               "Every expedition has 15 challenges and three chances; your choices shape "
               "the route.")

def T(en, **rest):
    return dict(en=en, **rest)


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def deal(sid, opts, order):
    """Rotate one question's options so the key is not always in the top two.

    The export's key sits in slot 0 fifteen times and slot 1 twelve times,
    never lower. Rotating by the question's ordinal spreads it over all four
    slots without touching a single string: the options keep their wording,
    their explanations and their `next`, and only their order changes. The
    distractors are as plausible in any order — they are four tenses of one
    verb, not a list with a natural sequence.
    """
    n = len(opts)
    k = order % n
    return opts[k:] + opts[:k]


# ── the four endings. The export chose these words in JavaScript from the
# score, so nothing survived extraction; they are written here, in the voice
# of the game and without a word about any earlier version of it.
ENDINGS = {
    'master': dict(
        k=T('EXPEDITION COMPLETE'), title=T('THE NAUTILUS RETURNS'),
        story=T('The case comes up through the moon pool still cold from the deep. '
                'Every reading holds. Nemo signs the log, and for the first time in '
                'three days the crew has been sleeping instead of listening.'),
        success=True),
    'complete': dict(
        k=T('ARCHIVE READ'), title=T('THE RECORD STANDS'),
        story=T('You have read the core and copied what it holds. The city keeps the '
                'original; the Nautilus carries the copy. It is enough — the surface '
                'will know what has been waking down here.'),
        success=True),
    'missing': dict(
        k=T('ONE DOOR UNOPENED'), title=T('WHAT THE DEEP KEPT'),
        story=T('The Nautilus rises with most of the record and one bronze door still '
                'shut behind her. Mara has been marking the chart all the way up. '
                'Somebody will come back for it.'),
        success=False),
    'failed': dict(
        k=T('EXPEDITION LOST'), title=T('THE DARK CLOSES'),
        story=T('The rail goes, then the light. The Nautilus has been running on '
                'ballast alone for an hour when the trench finally takes her. '
                'The signal is still pulsing when the last lamp dies.'),
        success=False),
}

# ── route notes. The export gave each route a label and nothing else; the
# engine prints a second line under it, and a fork with no consequence stated
# is a coin toss rather than a decision.
DESC = {
    'c1':       T('Straight at the signal, through the crystal.'),
    't1':       T('The long way, past a gate that carries the same mark.'),
    'crescue':  T('A diver first. The signal will keep.'),
    'csignal':  T('The signal first. The diver has air.'),
    'tarchive': T('The hall above, where the records are shelved.'),
    'tstatue':  T('The tunnel below, where the water runs cold.'),
    'i1':       T('Lia works the drive from inside the hull.'),
    'o1':       T('Nadia goes out to the plating herself.'),
    'ft1':      T('Take it into the trench and let the crystal hold it.'),
    'fc1':      T('Outrun it through the streets of the coral city.'),
}

LABELS = {
    # the engine's default progress word is Blocula's SPELLS
    'progress': T('CHALLENGES',
                  es='RETOS', de='AUFGABEN', fr='DÉFIS', it='SFIDE', pt='DESAFIOS',
                  ru='ЗАДАНИЯ', ar='تحدّيات', zh='挑战', ja='課題'),
    'tiles': T('SHARDS',
               es='FRAGMENTOS', de='SPLITTER', fr='ÉCLATS', it='FRAMMENTI', pt='FRAGMENTOS',
               ru='ОСКОЛКИ', ar='شظايا', zh='碎片', ja='破片'),
    'relic': T('ARCHIVE SHARD RECOVERED · +{p} POINTS'),
    'restart': T('DIVE AGAIN'),
}

RELIC = ('q0', 'log', 'engine', 'archive')   # on the spine, so reachable on every route
FINAL = 'archive'


def build():
    scenes = {}
    order = 0
    for sid, s in DATA['scenes'].items():
        if sid in SKIP or sid == 'end':
            continue
        base = {'img': s['img'], 'k': T(s['kicker']), 'story': T(' '.join(s['story']))}
        if s.get('title'):
            base['title'] = T(s['title'])
        if s.get('big'):
            base['title'] = T(s['big'])

        if 'opts' in s:
            base['kind'] = 'question'
            base['prompt'] = T(s['prompt'])
            fix = OPTS_FIX.get(sid, {})
            opts = [dict(o, text=fix.get(o['text'], o['text'])) for o in s['opts']]
            opts = deal(sid, opts, order)
            order += 1
            base['opts'] = [T(o['text']) for o in opts]
            base['answer'] = next(i for i, o in enumerate(opts) if o['correct'])
            base['fb'] = T(opts[base['answer']]['why'])
            base['points'] = 5
            if sid in RELIC:
                base['relic'] = True
            if sid == FINAL:
                base['final'] = True
                base['next'] = 'resolve'
            else:
                # the export sends right and wrong down different roads only to
                # pass through a consequence scene that rejoins; the engine's
                # chance counter is the penalty (README section 9)
                base['next'] = opts[base['answer']]['next']
        elif 'routes' in s:
            base['kind'] = 'choice'
            base['prompt'] = T(s['prompt'])
            base['routes'] = [{'name': T(r['text'].split(BULLET)[-1].split(DASH)[-1].strip()),
                               'desc': DESC[r['next']], 'route': r['route'],
                               'target': r['next']} for r in s['routes']]
        elif sid == 'intro':
            base['kind'] = 'intro'
            base['rules'] = [T(s['badge'])]
            base['start'] = T('BOARD THE NAUTILUS')
            base['small'] = T('Present perfect simple and continuous, B1')
            base['next'] = s['next']
        elif sid == 'brief':
            base['kind'] = 'rules'
            base['story'] = T(BRIEF_STORY)
            base['rules'] = [{'name': T(c['head']), 'form': T(c['body'])} for c in s['rules']]
            base['note'] = T('Read the meaning, not the words. A finished result takes '
                             'the simple; an activity still running takes the continuous.')
            base['button'] = T('START THE DESCENT')
            base['next'] = s['next']
        else:
            base['kind'] = 'story'
            base['next'] = s['next']
        scenes[sid] = place(sid, base)

    for key, e in ENDINGS.items():
        sid = 'end_' + key
        scenes[sid] = place(sid, dict(kind='ending', img=END_IMG[key], **e))

    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Nautilus: The Black Archive — Present Perfect Deep-Sea RPG (B1)',
        'description': 'An interactive B1 English lesson from Forbes English: '
                       'Nautilus: The Black Archive — Present Perfect Deep-Sea RPG (B1).',
        'langs': LANGS,
        # camp 8 on the Block Camp route map, Present Perfect Continuous - the
        # half of the contrast this lesson is pitched at. The export's own
        # chrome is turquoise (--t: #48e4d4) and so is every glowing thing in
        # the plates, so the camp colour and the art agree for once; Innes
        # asked for turquoise here rather than the Sealed Log's rose. One
        # accent (README section 1).
        'accent': '#46B0AB',
        'accent_ink': '#0b1a12', 'deep': '#06181f', 'panel': 'rgba(6,20,27,.88)',
        'labels': LABELS,
        'start': 'intro', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete',
                    'missing': 'end_missing', 'failed': 'end_failed'},
        'max': 75, 'points': 5, 'tiles': 4, 'chances': 3, 'complete_score': 65,
        'total': 15,
        'img_w': 1536, 'img_h': 864,
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
