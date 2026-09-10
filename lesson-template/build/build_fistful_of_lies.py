#!/usr/bin/env python3
"""A Fistful of Lies — Past Simple voxel-western RPG (A1-A2).

    python3 lesson-template/build/build_fistful_of_lies.py

Rebuilds block-camp/fistful-of-lies-rpg.html from
lesson-template/build/rpg/fistful-of-lies-rpg/data.json — the text of the
standalone export Innes sent on 2026-09-10, pulled out by
rpg/extract_standalone.py.

**The ChatGPT kind of export** (docs/CHATGPT-RPG-BRIEF.md), and the first one
to arrive with everything that brief asks for: `meta`, a `briefing`, a
per-scene `hotspot` and `explanation`, and all nine of HOUSE-STYLE §8's
languages on every learner-facing string. So unlike the four RPGs before it,
this builder writes almost no new lesson text — the glosses come from the
export's own `local` blocks, flattened into rpg/<slug>/translations/ by that
directory's make-translations.py, and the feedback line under every answer is
the export's `explanation`. What is still this file's job:

  * **The panel side on every scene**, which no export carries. The art puts
    its lit object on the right of the frame in nineteen of twenty-one
    scenes, so the panel goes left almost everywhere; `fork` is the exception
    and says why.
  * **Pictures for the four endings and the briefing.** The export shipped 22
    plates — a cover, nineteen questions and two forks — and pointed all five
    of those screens at the cover. Four endings on one picture reads as one
    ending with four captions, so each now takes the plate its own text
    describes (ENDINGS below), and the briefing takes the office, the only
    room in the lesson with a desk in it.
  * **Two hotspots the export put where they could not be seen** — `tunnel`,
    whose lantern ran off the right edge of the plate, and `map`, whose box
    spanned 40% of the frame and reached under a translated panel. Everything
    else was placed accurately enough to keep; every one was read off a
    gridded contact sheet and then checked again on a closed-scene screenshot
    (rpg/README.md §3-4).

The answer key came distributed — 7/6/6 across the three slots, and no key is
the longest option in its scene — so `_check_answer_key` passes on the
export's own indices and nothing is re-dealt here. That is a first: the
Frankenstein export put the key in slot 0 on all 44 questions.

**The one engine addition this export needed:** `routeStory`. Its two success
endings carry a `routeTexts` block — a different closing paragraph depending
on whether you went back for Tito or after Andreas. The engine already tracks
`state.route` (it prints it under the final score), so an ending scene now
takes an optional `routeStory` of `{ROUTE: text}` and renders the first entry
the player's route list matches. Generic, in rpg.py, validated in nine
languages like every other learner string — README §9's rule for a mechanic an
export has and the engine does not.

Pictures: block-camp/fistful-of-lies-rpg/NN_name.webp, 1536x1024, as exported.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'fistful-of-lies-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. These are the export's own
# `hotspot` boxes, verified one at a time on a gridded contact sheet; the two
# that were changed say why.
#
# A left panel is 46% of the frame and grows to 54% the moment a gloss
# language is on (`tr-on` in the engine), so it reaches x=56. Every object
# below sits clear of that line.
HOT = {
    'cover':    ([82, 45, 24, 58], 'left',   'center'),       # Blane in the saloon doorway
    'rules':    ([82, 46, 20, 31], 'left',   'center', 56),   # the open safe; wide, five cards
    'entry':    ([81, 51,  5, 15], 'left',   'center'),       # the door handle
    'piano':    ([87, 62, 15, 17], 'left',   'center'),       # the piano keys
    'contract': ([73, 47, 14, 18], 'left',   'center'),       # the contract in Andreas's hand
    # The only scene whose object is dead centre. Route choices are centred
    # (README §3), but a centre panel is 64% wide and covers x=16-84, so it
    # sits on this signpost whichever end it is anchored to — measured at 61%
    # of the object hidden anchored `bottom` and 100% anchored `top`. The
    # choice scene's copy is short enough for a 34% panel on the picture's
    # empty left third, which clears the signpost completely and still does
    # not scroll in any of the nine languages.
    'fork':     ([50, 41, 12, 12], 'left',   'center', 34),   # the signpost
    'tito':     ([73, 69,  7,  5], 'left',   'center'),       # the silver coin on the bar
    'boot':     ([80, 62, 19, 24], 'left',   'center'),       # the muddy boot
    'office':   ([82, 46, 20, 31], 'left',   'center'),       # the safe, open and empty
    'receipt':  ([77, 63, 16, 20], 'left',   'center'),       # the receipt on the desk
    'hatch':    ([86, 66,  9, 12], 'left',   'center'),       # the hatch ring
    # Export box was [95, 48, 10, 21], which ran off the right edge of the
    # plate and took the marker with it. Same lantern, pulled inside the
    # frame — the glow further down the tunnel at x=72 is a digger, not a lamp,
    # and a marker there rendered on empty haze.
    'tunnel':   ([93, 48,  8, 16], 'left',   'center'),       # the lantern
    # Export box was [60, 70, 40, 19]: 40% of the frame, and its left edge ran
    # under a translated panel. Narrowed to the bank end of the map, which is
    # the half the clue is about.
    'map':      ([70, 70, 20, 15], 'left',   'center'),       # the map on the table
    'ledger':   ([72, 66, 26, 15], 'left',   'center'),       # the open ledger
    'sack':     ([90, 65, 13,  7], 'left',   'center'),       # the emptied gold tray
    'decision': ([86, 54, 18, 14], 'left',   'center'),       # the signpost, this one off to the right
    'rescue':   ([81, 57,  8, 18], 'left',   'center'),       # the padlock on the gate
    'key':      ([64, 52,  8,  8], 'left',   'center'),       # the bank key changing hands
    'chase':    ([84, 67, 26, 21], 'left',   'center'),       # the wheel tracks
    'brake':    ([92, 42, 10, 20], 'left',   'center'),       # the brake lever
    'bell':     ([88, 19, 13, 20], 'left',   'center'),       # the bell
    'showdown': ([76, 75, 28, 11], 'left',   'center'),       # the evidence papers on the table
    'dawn':     ([89, 57,  7,  5], 'left',   'center'),       # the gold coin on the piano
    'end_master':   ([89, 57,  7,  5], 'left', 'center'),
    'end_complete': ([76, 75, 28, 11], 'left', 'center'),
    'end_missing':  ([72, 66, 26, 15], 'left', 'center'),
    'end_failed':   ([84, 67, 26, 21], 'left', 'center'),
}

# ── a picture for each ending. The export sent none and pointed all four at
# the cover; each of these is the plate its own closing text describes.
ENDINGS = {
    'master':   ('22_dawn.webp',     True),    # the piano at dawn, and the coin that bought silence
    'complete': ('21_showdown.webp', True),    # the four papers that closed the case
    'missing':  ('13_ledger.webp',   False),   # the wages ledger, with the case still full of holes
    'failed':   ('18_chase.webp',    False),   # the wheel tracks of a wagon that got away
}


def T(en, **rest):
    return dict(en=en, **rest)


# ── the kicker over the rules briefing: the only learner-facing string in the
# lesson the export did not write, so its nine glosses live here rather than
# in translations/, which is generated from the export and nothing else.
BRIEFING_KICKER = T(
    'BEFORE THE FIRST NOTE',
    es='ANTES DE LA PRIMERA NOTA', de='VOR DEM ERSTEN TON',
    fr='AVANT LA PREMIÈRE NOTE', it='PRIMA DELLA PRIMA NOTA',
    pt='ANTES DA PRIMEIRA NOTA', ru='ПЕРЕД ПЕРВОЙ НОТОЙ',
    ar='قبل النغمة الأولى', zh='在第一个音符之前', ja='最初の一音の前に')

# ── HUD and button words. The English is this lesson's; the glosses are the
# export's own `ui` block, which already carries the nine.
LABELS = {
    'tiles': T('CLUE TILES',
               es='FICHAS', de='HINWEISSTEINE', fr='TUILES', it='TESSERE', pt='PEÇAS',
               ru='ФИШКИ', ar='القطع', zh='线索牌', ja='タイル'),
    'relic': T('CLUE TILE COLLECTED · +{p} POINTS',
               es='FICHA CONSEGUIDA · +{p} PUNTOS', de='HINWEISSTEIN GESAMMELT · +{p} PUNKTE',
               fr='TUILE OBTENUE · +{p} POINTS', it='TESSERA RACCOLTA · +{p} PUNTI',
               pt='PEÇA RECOLHIDA · +{p} PONTOS', ru='ФИШКА ПОЛУЧЕНА · +{p} ОЧКОВ',
               ar='جُمعت قطعة الدليل · +{p} نقاط', zh='获得线索牌 · +{p} 分',
               ja='タイル獲得 · +{p} ポイント'),
    'restart': T('RIDE AGAIN',
                 es='JUGAR DE NUEVO', de='ERNEUT REITEN', fr='REJOUER', it='GIOCA ANCORA',
                 pt='JOGAR NOVAMENTE', ru='ИГРАТЬ СНОВА', ar='العب مجددًا',
                 zh='再玩一次', ja='もう一度遊ぶ'),
}


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    c, b = DATA['cover'], DATA['briefing']
    scenes = {
        'cover': place('cover', {
            'kind': 'intro', 'img': c['image'],
            'k': T(c['eyebrow']), 'title': T(c['title']), 'story': T(c['lead']),
            'rules': [T(r) for r in c['rules']],
            'start': T(c['start']), 'small': T(c['small']),
            'next': 'rules'}),
        # The export pointed the briefing at the cover, which would have shown
        # the same plate twice running. The office is the lesson's one desk.
        'rules': place('rules', {
            'kind': 'rules', 'img': '08_office.webp',
            'k': BRIEFING_KICKER, 'title': T(b['title']),
            'rules': [{'name': T(card['head']), 'form': T(card['text'])} for card in b['cards']],
            'note': T(b['note']), 'button': T(b['button']),
            'next': DATA['first']}),
    }

    for sid, s in DATA['scenes'].items():
        base = {'img': s['image'], 'k': T(s['act']), 'title': T(s['title']),
                'story': T(s['story'])}
        if 'choices' in s:
            base['kind'] = 'choice'
            base['routes'] = [{'name': T(ch['label']), 'desc': T(ch['note']),
                               'route': ch['route'], 'target': ch['next']}
                              for ch in s['choices']]
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['clue'])
            base['prompt'] = T(s['prompt'])
            base['opts'] = [T(a['text']) for a in s['answers']]
            base['answer'] = next(i for i, a in enumerate(s['answers']) if a.get('correct'))
            base['points'] = s.get('points', 5)
            if s.get('relic'):
                base['relic'] = True
            base['fb'] = T(s['explanation'])
            # the export sends right and wrong answers down the same road; the
            # chance counter is the penalty, not a detour (README §9)
            assert s['correctNext'] == s['wrongNext'], sid
            base['next'] = s['correctNext']
        scenes[sid] = place(sid, base)

    # the last question decides whether a flawless run reaches the master ending
    scenes['dawn']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        img, success = ENDINGS[key]
        end = {'kind': 'ending', 'img': img, 'success': success,
               'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])}
        if e.get('routeTexts'):
            # keyed by the route name the choice scene pushes onto state.route
            end['routeStory'] = {r.upper(): T(t) for r, t in e['routeTexts'].items()}
        scenes[sid] = place(sid, end)

    sc = DATA['meta']['scoring']
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'A Fistful of Lies — Past Simple Voxel Western RPG (A1-A2)',
        'description': 'An interactive A1-A2 English lesson from Forbes English: '
                       'A Fistful of Lies — Past Simple Voxel Western RPG (A1-A2).',
        'langs': LANGS,
        # camp 3, Past Simple, on the Block Camp route map. The export asked
        # for #ffd58a; README §2 says the camp colour wins when they differ.
        'accent': '#B08968',
        'accent_ink': '#0b1a12', 'deep': '#1a1008', 'panel': 'rgba(18,12,6,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete',
                    'missing': 'end_missing', 'failed': 'end_failed'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
