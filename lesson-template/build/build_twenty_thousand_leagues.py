#!/usr/bin/env python3
"""Twenty Thousand Leagues: The Sealed Log — Past Perfect Simple + Continuous RPG (B1-B2).

    py lesson-template/build/build_twenty_thousand_leagues.py
    RPG_EN_ONLY=1 py lesson-template/build/build_twenty_thousand_leagues.py   # structure check, no glosses

Builds block-camp/twenty-thousand-leagues-rpg.html from
lesson-template/build/rpg/twenty-thousand-leagues-rpg/data.json.

**The second skin of the Nautilus adventure, made into a second lesson.**
`Nautilus_20000_Leagues_RPG_Revamped.html` arrived beside the voxel export
that became `nautilus-black-archive-rpg` (Present Perfect, B1): same 41 scene
ids, same 27 questions, only the art differs — painted and cinematic where the
other is voxel. Publishing it as it stood would have put an identical lesson
in the catalogue under a second cover, so on 2026-09-13 Innes asked for the
text to change. The pictures are the export's, in the same scene order; every
word is new, and the grammar moves one camp along the route map:

  * **Past perfect simple against past perfect continuous.** The voyage is
    told from the ship's log, written afterwards, so every entry looks back
    from a later past moment — "by the time they turned back", "when the lamp
    failed" — and asks what was already finished then (a result, a number:
    had collected six pearls) and what was still going on (a duration: had
    been descending for six hours). The voxel lesson asks the same question
    from NOW; this one asks it from THEN, which is the step from B1 to B2.
  * **Two distractors carry the contrast, one carries the trap.** Every item
    has the other past-perfect form (the contrast being taught), the past
    simple (right in a plain narrative, wrong once the sentence anchors on a
    later moment), and the present perfect in the same aspect as the key
    (the voxel lesson's answer, wrong here — the log looks back from the
    past, not from now). That last one is also the same length as the key,
    which keeps the key off the top of the length gate on every continuous
    item; a past-perfect-continuous key is the longest form there is.
  * **The consequence scenes are on the path.** The export routed a wrong
    answer through them and a right answer past them; this engine sends every
    answer down one road (README section 9), and the voxel builder left the
    five "consequence" plates unreachable as a result. Here they are log
    entries in their own right — a seam opened, the gate closed — so all
    forty pictures are seen on a full run.
  * **Four endings, written for the log.** The export chose its ending words
    in JavaScript; nothing survived extraction. Each ending here is a last
    entry, past perfect and all.
  * **Nine languages** in translations/, with the strings the voxel lesson
    shares (route names, HUD words) carried over from its files so the two
    lessons gloss the same English the same way.

Pictures: block-camp/twenty-thousand-leagues-rpg/NN_name.webp, 1536x864 (16:9),
so the spec passes img_w and img_h. Scene 41, the export's expedition map, is a
nav screen for its own hash routing and is not copied.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'twenty-thousand-leagues-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = [] if os.environ.get('RPG_EN_ONLY') else rpg.NINE

# ── hotspots: [cx, cy, w, h] in % of the 1536x864 picture, then panel side,
# vertical anchor, optional panel width %. Read off gridded contact sheets
# (README section 3) — the painted plates put their subject mid-frame more
# often than the voxel ones did, so several panels are narrowed rather than
# moved: a gloss language widens the panel by 8 points and a 46% left panel
# reaches x=54. check-rpg-panels.js measures the result.
HOT = {
    'intro':     ([63, 18, 36, 22], 'left',   'center'),       # the Nautilus, lamps on, above the drowned city
    'brief':     ([88, 68, 14, 18], 'left',   'center', 70),   # the chart orb under Nemo's hand; four cards, and French needs the width
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
    'tstatue':   ([90, 50, 18, 50], 'left',   'center'),       # the metal door
    't4':        ([60, 64, 24, 34], 'left',   'center', 38),   # the black plate with the etched chart; a gloss panel reaches x=46
    'log':       ([66, 76, 20, 16], 'left',   'center'),       # the journal under Aronnax's hand
    'engine':    ([22, 35, 34, 34], 'right',  'center'),       # the pressure drive
    'ballast':   ([57, 32, 12, 40], 'left',   'center'),       # the valve lever Lia is hauling on
    'repairdec': ([57, 47, 30, 40], 'left',   'center', 38),   # the airlock wheel, mid-frame
    'i1':        ([33, 54, 26, 28], 'right',  'center'),       # the regulator in Lia's hands, sparking
    'i2':        ([12, 28, 10, 14], 'right',  'center'),       # the coolant tap
    'i3':        ([24, 26, 40, 44], 'right',  'center'),       # the power cells
    'o1':        ([12, 33, 14, 16], 'right',  'center'),       # Nadia's helmet lamp
    'o2':        ([38, 66, 12, 14], 'right',  'center'),       # the repair tool's light on the fracture
    'o3':        ([75, 12, 16, 18], 'left',   'center'),       # the eye above Nadia
    'squidq':    ([92, 12, 14, 16], 'left',   'center'),       # the squid's eye
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
    'end_missing':  ([90, 50, 18, 50], 'left', 'center'),      # the metal door, still shut
    'end_failed':   ([76, 68, 26, 30], 'left', 'center'),      # the rail the squid tore away
}

# ── a plate for each ending. Endings are terminal, where a repeated plate does
# not read as one; the surfacing plate is kept for the run that earns it.
END_IMG = {
    'master':   '40_end.webp',
    'complete': '39_archive.webp',
    'missing':  '18_tstatue.webp',
    'failed':   '31_tentacle.webp',
}


def T(en, **rest):
    return dict(en=en, **rest)


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def deal(opts, order):
    """Rotate one question's options by its ordinal so the key is spread over
    all four slots. The options are four forms of one verb; their order carries
    no information, so nothing is lost by turning them."""
    k = order % len(opts)
    return opts[k:] + opts[:k]


# ── the four endings, each a last log entry.
ENDINGS = {
    'master': dict(
        k=T('LOG COMPLETE'), title=T('THE NAUTILUS SURFACED'),
        story=T('The last page was written in daylight. By the time the Nautilus broke '
                'the surface, every entry had been checked twice, and the archive case '
                'had not left Nemo’s side for a day.'),
        success=True),
    'complete': dict(
        k=T('ARCHIVE READ'), title=T('THE RECORD STOOD'),
        story=T('They had read the core and copied what it held before they turned for '
                'home. The city kept the original; the Nautilus carried the copy, and '
                'the surface finally knew what had been waking down there.'),
        success=True),
    'missing': dict(
        k=T('ONE DOOR UNOPENED'), title=T('WHAT THE DEEP KEPT'),
        story=T('The Nautilus rose with most of the record and one metal door still '
                'shut behind her. Mara had been marking the chart all the way up. '
                'Somebody would go back for it.'),
        success=False),
    'failed': dict(
        k=T('LOG UNFINISHED'), title=T('THE DARK CLOSED'),
        story=T('The rail went, then the light. The Nautilus had been running on '
                'ballast alone for an hour when the trench finally took her. The last '
                'entry stops in the middle of a sentence.'),
        success=False),
}

# ── route notes: the second line under each choice, so a fork states a
# consequence rather than offering a coin toss.
DESC = {
    'c1':       T('Straight at the signal, through the crystal.'),
    't1':       T('The long way, past a gate that carried the same mark.'),
    'crescue':  T('A diver first. The signal would keep.'),
    'csignal':  T('The signal first. The diver had air.'),
    'tarchive': T('The hall above, where the records were shelved.'),
    'tstatue':  T('The tunnel below, where the water ran cold.'),
    'i1':       T('Lia worked the drive from inside the hull.'),
    'o1':       T('Nadia went out to the plating herself.'),
    'ft1':      T('Into the trench, to let the crystal hold it.'),
    'fc1':      T('Through the streets of the coral city, at full speed.'),
}

LABELS = {
    # the engine's default progress word is Blocula's SPELLS
    'progress': T('ENTRIES',
                  es='ENTRADAS', de='EINTRÄGE', fr='ENTRÉES', it='VOCI', pt='ENTRADAS',
                  ru='ЗАПИСИ', ar='مدخلات', zh='条目', ja='記録'),
    'tiles': T('PAGES',
               es='PÁGINAS', de='SEITEN', fr='PAGES', it='PAGINE', pt='PÁGINAS',
               ru='СТРАНИЦЫ', ar='صفحات', zh='页', ja='ページ'),
    'relic': T('LOG PAGE RECOVERED · +{p} POINTS'),
    'restart': T('OPEN THE LOG AGAIN'),
}

RELIC = ('q0', 'log', 'engine', 'archive')   # on the spine, so reachable on every route
FINAL = 'archive'


def build():
    scenes = {}
    order = 0
    for sid, s in DATA['scenes'].items():
        base = {'img': s['img'], 'k': T(s['kicker']), 'story': T(s['story'])}
        if s.get('title'):
            base['title'] = T(s['title'])
        if s.get('big'):
            base['title'] = T(s['big'])

        if 'opts' in s:
            base['kind'] = 'question'
            base['prompt'] = T(s['prompt'])
            opts = deal(s['opts'], order)
            order += 1
            base['opts'] = [T(o['text']) for o in opts]
            base['answer'] = next(i for i, o in enumerate(opts) if o['correct'])
            base['fb'] = T(s['fb'])
            base['points'] = 5
            if sid in RELIC:
                base['relic'] = True
            if sid == FINAL:
                base['final'] = True
            base['next'] = s['next']
        elif 'routes' in s:
            base['kind'] = 'choice'
            base['prompt'] = T(s['prompt'])
            base['routes'] = [{'name': T(r['text']), 'desc': DESC[r['next']],
                               'route': r['route'], 'target': r['next']} for r in s['routes']]
        elif sid == 'intro':
            base['kind'] = 'intro'
            base['rules'] = [T(s['badge'])]
            base['start'] = T('OPEN THE LOG')
            base['small'] = T('Past perfect simple and continuous, B1–B2')
            base['next'] = s['next']
        elif sid == 'brief':
            base['kind'] = 'rules'
            base['rules'] = [{'name': T(c['head']), 'form': T(c['body'])} for c in s['rules']]
            base['note'] = T('Finished by then: the simple. Still going on then: the continuous.')
            base['button'] = T('READ THE FIRST ENTRY')
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
        'title': 'Twenty Thousand Leagues: The Sealed Log — Past Perfect Deep-Sea RPG (B1-B2)',
        'description': 'An interactive B1-B2 English lesson from Forbes English: '
                       'Twenty Thousand Leagues: The Sealed Log — Past Perfect Deep-Sea RPG (B1-B2).',
        'langs': LANGS,
        # camp 9 on the Block Camp route map, Past Perfect — the rose that
        # sits against the teal of the plates. One accent (README section 1).
        'accent': '#d66d77',
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
    spec = build()
    if LANGS:
        spec = rpg.apply_translations(spec, os.path.join(BASE, 'translations'))
    rpg.assemble(spec)
