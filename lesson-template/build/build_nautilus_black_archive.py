#!/usr/bin/env python3
"""Nautilus: The Black Archive — Present Perfect Simple + Continuous RPG (B1).

    py lesson-template/build/build_nautilus_black_archive.py

Rebuilds block-camp/nautilus-black-archive-rpg.html from
lesson-template/build/rpg/nautilus-black-archive-rpg/data.json — the text of
the "Minecraft Edition" export, pulled out by rpg/extract_static.py.

**The fourth kind of export, and the first to carry no game object at all.**
README §2 named three kinds and said a fourth means "read its script first".
This one's script holds nothing but the engine: scoring, hash routing and the
feedback box. Every learner-facing string is already rendered markup, so
extract_static.py parses rather than executes. Its docstring has the detail.

**Two skins, one adventure.** Innes sent this alongside
`Nautilus_20000_Leagues_RPG_Revamped.html`, a painted version of the same
game: same 41 scene ids, all 27 questions with byte-identical prompts and
byte-identical options, only the art and a few flavour words differ ("a city
built from forgotten blocks" against "a city beneath the seabed"). Publishing
both would put two indistinguishable lessons in the catalogue, so only the
voxel one ships — it is the look the other Block Camp adventures share.

Six things this builder does that the export did not:

  * **Deals the answer key.** The export puts the key in slot 0 on fifteen
    questions and slot 1 on the other twelve — never slot 2 or 3. A student
    who has learned no grammar scores by guessing from the top two. This
    engine renders `opts` in spec order, so the builder rotates each
    question's options by a fixed offset from its index in the scene list.
    `_check_answer_key`'s gate is 80% in one slot and would have passed this
    at 56%, which is why the rotation is here and not left to the validator.
  * **Writes four endings.** The export has one `#end` screen whose title and
    paragraph were chosen in JavaScript from the score, so the text for
    master / complete / missing / failed did not survive extraction and is
    written here. Each gets its own plate.
  * **An explanation under every answer.** The export carries `why` per
    option, but the same sentence on all four — it explains the rule, not the
    choice. Taken as `fb`.
  * **Nine languages.** The export has no `local` block and no lang attribute
    anywhere: English only. The glosses live in translations/.
  * **Drops `map`.** Scene 41 is a teacher's expedition index — a nav screen
    for the export's own hash routing. This engine has its own HUD and scene
    graph, so it is skipped, the way Sherlock's builder skips `resolve`.
  * **Drops hull and oxygen.** The export tracked two damage bars; this engine
    scores on points, tiles and chances (README §9 keeps an export's rules,
    but only where the engine has them). The five consequence scenes stay as
    story beats and the chance counter carries the penalty.

Pictures: block-camp/nautilus-black-archive-rpg/NN_name.webp, **1536x864** —
16:9, like Wonderland and unlike the 3:2 default, so the spec passes img_w
and img_h.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'nautilus-black-archive-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

BULLET, DASH = '·', '—'
SKIP = ('map',)          # the teacher's expedition index, not a scene of the game

# ── hotspots: [cx, cy, w, h] in % of the 1536x864 picture, then panel side,
# vertical anchor, optional panel width %. Read off gridded contact sheets
# (README §3) and named by the object the export's own alt text names — every
# plate says "Minecraft-style <id> scene: the <object>", which is the thing
# the clue talks about and so the thing that glows.
#
# The art is composed with the subject off-centre on nearly every plate, so
# most panels sit on the opposite side at the default 46%. Where the object
# creeps toward the middle the panel is narrowed instead of moved — a gloss
# language widens the panel by 8 points and a 46% left panel reaches x=58.
HOT = {
    'intro':     ([37, 18, 34, 20], 'right',  'center'),       # the Nautilus, running above the drowned city
    'brief':     ([75, 72, 12, 18], 'left',   'center', 60),   # the chart orb in Nemo's hands; wide, two cards
    'q0':        ([57, 45,  9, 13], 'left',   'center', 40),   # the headlamp
    'leak':      ([13, 46, 12, 22], 'right',  'center'),       # the valve
    'route':     ([80, 48, 13, 40], 'left',   'center'),       # the branching crystal
    'c1':        ([22, 58, 16, 28], 'right',  'center'),       # the crystal shard
    'cbad':      ([87, 62, 13, 20], 'left',   'center'),       # the oxygen gauge
    'c2':        ([62, 72, 12, 16], 'left',   'center'),       # the pearl pouch
    'cdec':      ([60, 83,  7, 10], 'left',   'center'),       # the flashing lamp
    'crescue':   ([37, 60, 10, 15], 'right',  'center'),       # the trapped helmet
    'csignal':   ([61, 40, 20, 34], 'left',   'center', 38),   # the aperture
    'c4':        ([80, 45, 28, 42], 'left',   'center'),       # the dome
    't1':        ([63, 22, 16, 26], 'left',   'center', 42),   # the threshold
    'tbad':      ([27, 30, 14, 20], 'right',  'center'),       # the damaged plate
    't2':        ([60, 38, 16, 22], 'left',   'center', 44),   # the carved eye
    'tdec':      ([70, 40, 10, 16], 'left',   'center'),       # the spiral crest
    'tarchive':  ([62, 45, 14, 26], 'left',   'center', 42),   # the tablet Aronnax holds, not the diver;
                                                           # it starts at x=55, so 42% + gloss stops clear
    'tstatue':   ([88, 45, 15, 34], 'left',   'center'),       # the bronze door
    't4':        ([62, 55, 14, 28], 'left',   'center', 42),   # the obsidian map
    'log':       ([70, 68, 14, 16], 'left',   'center'),       # the journal
    'engine':    ([28, 55, 18, 28], 'right',  'center'),       # the pressure drive
    'ballast':   ([24, 62, 16, 24], 'right',  'center'),       # the valve handle
    'repairdec': ([62, 55, 18, 34], 'left',   'center', 42),   # the airlock wheel
    'i1':        ([72, 45, 20, 28], 'left',   'center'),       # the regulator
    'i2':        ([15, 46,  9, 15], 'right',  'center'),       # the coolant tap
    'i3':        ([38, 62, 20, 18], 'right',  'center', 38),       # the power cells
    'o1':        ([20, 35, 13, 18], 'right',  'center'),       # the helmet lamp
    'o2':        ([72, 55, 10, 15], 'left',   'center'),       # the repair tool
    'o3':        ([29, 14, 10, 13], 'right',  'center'),       # the approaching eye
    'squidq':    ([88, 14, 11, 14], 'left',   'center'),       # the squid eye
    'tentacle':  ([58, 55, 16, 24], 'left',   'center', 42),   # the torn rail
    'finaldec':  ([85, 68, 15, 24], 'left',   'center'),       # the helm
    'ft1':       ([22, 70, 24, 24], 'right',  'center'),       # the pearl trail
    'ft2':       ([30, 72, 22, 20], 'right',  'center'),       # the crystal wall
    'ft3':       ([57, 63, 18, 18], 'left',   'center', 34),   # the Nautilus bow
    'fc1':       ([92, 42, 13, 38], 'left',   'center'),       # the next arch
    'fc2':       ([72, 35, 20, 38], 'left',   'center'),       # the falling tower
    'fc3':       ([90, 50, 13, 34], 'left',   'center'),       # the narrow arch
    'archive':   ([62, 45, 24, 42], 'left',   'center', 40),   # the archive core
    # the four endings, on their own plates
    'end_master':   ([80, 62, 10, 14], 'left', 'center'),      # the archive case, home
    'end_complete': ([62, 45, 24, 42], 'left', 'center', 40),  # the archive core
    'end_missing':  ([88, 45, 15, 34], 'left', 'center'),      # the bronze door, still shut
    'end_failed':   ([58, 55, 16, 24], 'left', 'center', 42),  # the torn rail
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
        'title': 'Nautilus: The Black Archive — Present Perfect Voxel RPG (B1)',
        'description': 'An interactive B1 English lesson from Forbes English: '
                       'Nautilus: The Black Archive — Present Perfect Voxel RPG (B1).',
        'langs': LANGS,
        # camp 8 on the Block Camp route map, Present Perfect Continuous - the
        # half of the contrast this lesson is pitched at, and a teal that sits
        # in the plates rather than on top of them. One accent (README section 1).
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
