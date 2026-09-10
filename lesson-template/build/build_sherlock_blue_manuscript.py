#!/usr/bin/env python3
"""Sherlock: The Blue Manuscript — Present Simple Questions RPG (A1-A2).

    python3 lesson-template/build/build_sherlock_blue_manuscript.py

Rebuilds block-camp/sherlock-blue-manuscript-rpg.html from
lesson-template/build/rpg/sherlock-blue-manuscript-rpg/data.json — the text of
the standalone export Innes sent on 2026-09-09, pulled out by
rpg/extract_standalone.py. Glosses come from the export's own `local` blocks,
flattened by rpg/make_translations.py.

The ChatGPT kind of export (docs/CHATGPT-RPG-BRIEF.md), but a much weaker one
than A Fistful of Lies, and three of its defects would have shipped a broken
lesson rather than an untidy one:

  * **The answer was in slot 0 on all fifteen questions.** This engine renders
    `opts` in spec order, so the first option really is the first button. KEY
    below deals it 5/5/5 across the three slots; rpg.py refuses the build if it
    drifts back.
  * **The last question hard-coded the master ending** (`next: 'end:master'`
    rather than `'resolve'`), so every player reached "THE CASE IS SOLVED"
    whatever they scored and two of the three endings were unreachable. It
    resolves from the score now, which is what the scoring block in `meta` is
    for.
  * **Every one of the seventeen hotspots was the same box**, `[78, 58, 20, 26]`
    — a placeholder, not a placement. All seventeen are read off gridded
    contact sheets here (rpg/README.md §3) and checked again on closed-scene
    screenshots.

Also the export's own: three endings and the briefing all pointed at the
cover, so each takes a plate of its own below.

**THIS LESSON IS NOT PUBLISHED, AND MUST NOT BE UNTIL THE ARTWORK IS
REPLACED.** The export shipped eighteen picture filenames holding **ten
distinct images**. Seven names are duplicates of another:

    05_ledger = 11_telegram = 14_libcard      08_dockpass = 15_key
    01_cover  = 12_cipher                     06_token    = 16_timetable
    03_watch  = 18_plate                      04_boot     = 17_rope
    07_choice1 = 13_choice2

Every one of those pairs is on the main spine, so a single thirteen-question
run shows the same picture two or three times, and the cover comes back as a
mid-game question. "One full-bleed picture per scene" is the first line of
rpg/README.md §1 and no builder can supply what the export did not draw. The
missing plates have to be re-requested — see docs/HANDOFF.md for the list.

Two of the ten were also simply on the wrong scenes, which SWAP below fixes:
`06_token.webp` holds a gas lamp and no token, `10_lamp.webp` holds the cab
token and no lamp. Three more name an object no plate contains at all
(`rope`, `plate`, `libcard`/`key`); their glow sits on the brightest real
object in the frame, which is honest but is not the standard.

Everything else here is finished and correct, so this builder is a re-run away
from shipping once the pictures arrive — the hotspots are the only part that
has to be read again.

Pictures: block-camp/sherlock-blue-manuscript-rpg/NN_name.webp, 1536x1024.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'sherlock-blue-manuscript-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. A left panel is 46% of the frame and
# grows to 54% with a gloss language on, so it reaches x=56; every object below
# clears that line, or the panel is moved instead.
#
# A trailing "no such object in the plate" comment marks the five scenes whose
# artwork does not hold the thing their clue names.
HOT = {
    'cover':     ([21, 51,  9, 12], 'right',  'center'),      # Holmes's magnifying lens
    'rules':     ([78, 66, 26, 18], 'left',   'center', 56),  # the open ledger; wide, four cards
    'envelope':  ([84, 62, 12, 13], 'left',   'center'),      # the blue envelope
    'watch':     ([76, 47, 15, 22], 'left',   'center'),      # the silver watch
    'boot':      ([80, 76, 16, 14], 'left',   'center'),      # the muddy print
    'ledger':    ([78, 66, 26, 18], 'left',   'center'),      # the night ledger
    'token':     ([66, 66, 14, 14], 'left',   'center'),      # the cab token (see SWAP)
    'choice1':   ([74, 29, 26, 16], 'center', 'bottom'),      # the signpost at the fork
    'dockpass':  ([89, 75, 14, 12], 'left',   'center'),      # the dock pass
    'ticket':    ([81, 66, 18, 13], 'left',   'center'),      # the museum ticket
    'lamp':      ([84, 20, 16, 26], 'left',   'center'),      # the gas lamp (see SWAP)
    'telegram':  ([66, 70, 14, 12], 'left',   'center'),      # the telegram on the desk
    # the disc sits at x=37, in front of Holmes, so the panel goes right
    'cipher':    ([37, 73, 11, 13], 'right',  'center'),      # the cipher disc
    'choice2':   ([74, 29, 26, 16], 'center', 'bottom'),      # the signpost at the fork
    'libcard':   ([88, 65, 18, 14], 'left',   'center'),      # the lit book — no card in the plate
    'key':       ([82, 73, 16, 13], 'left',   'center'),      # the lit crate — no key in the plate
    'timetable': ([84, 20, 16, 26], 'left',   'center'),      # the gas lamp — no timetable in the plate
    'rope':      ([70, 75, 16, 14], 'left',   'center'),      # the lit ironwork — no rope in the plate
    'plate':     ([76, 47, 15, 22], 'left',   'center'),      # the watch — no printing plate in the plate
    'end_master':    ([76, 47, 15, 22], 'left',  'center'),
    'end_assistant': ([37, 73, 11, 13], 'right', 'center'),
    'end_lost':      ([84, 20, 16, 26], 'left',  'center'),
}

# ── the answer key, dealt 5/5/5 in the order the scenes are played. Written
# out rather than generated so it is reviewable and stable across runs.
KEY = {
    'envelope': 0, 'watch': 1, 'boot': 2, 'ledger': 0, 'token': 1,
    'dockpass': 2, 'ticket': 0, 'lamp': 1, 'telegram': 2, 'cipher': 0,
    'libcard': 1, 'key': 2, 'timetable': 0, 'rope': 1, 'plate': 2,
}

# ── a picture for each ending and for the briefing. The export pointed all
# four screens at the cover.
END_IMG = {
    'master':    '18_plate.webp',      # the printer's own plate, and the thief with it
    'assistant': '12_cipher.webp',     # the disc half-read
    'lost':      '16_timetable.webp',  # the fog, and the trail gone cold
}
RULES_IMG = '05_ledger.webp'           # Holmes over an open book: a field guide

# ── SWAP. The export put these two plates on the wrong scenes: 06_token.webp
# holds a tall lit gas lamp and no token, and 10_lamp.webp holds the gold cab
# token and no lamp. Exchanging them gives both scenes the object their clue
# names, at no cost.
SWAP = {'token': '10_lamp.webp', 'lamp': '06_token.webp'}


def T(en, **rest):
    return dict(en=en, **rest)


# ── the two strings the export did not write, so their nine glosses live here.
BRIEFING_KICKER = T(
    'BEFORE BAKER STREET',
    es='ANTES DE BAKER STREET', de='VOR DER BAKER STREET',
    fr='AVANT BAKER STREET', it='PRIMA DI BAKER STREET',
    pt='ANTES DE BAKER STREET', ru='ПЕРЕД БЕЙКЕР-СТРИТ',
    ar='قبل شارع بيكر', zh='走进贝克街之前', ja='ベイカー街へ行く前に')

LABELS = {
    'tiles': T('EVIDENCE',
               es='PRUEBAS', de='BEWEISE', fr='PREUVES', it='PROVE', pt='PROVAS',
               ru='УЛИКИ', ar='الأدلة', zh='证据', ja='証拠'),
    'relic': T('EVIDENCE BLOCK RECOVERED · +{p} POINTS',
               es='PRUEBA CONSEGUIDA · +{p} PUNTOS', de='BEWEISSTÜCK GESICHERT · +{p} PUNKTE',
               fr='PREUVE OBTENUE · +{p} POINTS', it='PROVA RECUPERATA · +{p} PUNTI',
               pt='PROVA RECOLHIDA · +{p} PONTOS', ru='УЛИКА НАЙДЕНА · +{p} ОЧКОВ',
               ar='عُثر على دليل · +{p} نقاط', zh='取得证据 · +{p} 分',
               ja='証拠を入手 · +{p} ポイント'),
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
        'rules': place('rules', {
            'kind': 'rules', 'img': RULES_IMG,
            'k': BRIEFING_KICKER, 'title': T(b['title']),
            'rules': [{'name': T(card['head']), 'form': T(card['text'])} for card in b['cards']],
            'note': T(b['note']), 'button': T(b['button']),
            'next': DATA['first']}),
    }

    for sid, s in DATA['scenes'].items():
        base = {'img': SWAP.get(sid, s['image']), 'k': T(s['act']) if s.get('act') else None,
                'title': T(s['title']), 'story': T(s['story'])}
        base = {k: v for k, v in base.items() if v is not None}
        if 'choices' in s:
            base['kind'] = 'choice'
            base['routes'] = [{'name': T(ch['label']), 'desc': T(ch['note']),
                               'route': ch['route'], 'target': ch['next']}
                              for ch in s['choices']]
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['clue'])
            base['prompt'] = T(s['prompt'])
            texts = [a['text'] for a in s['answers']]
            correct = texts[next(i for i, a in enumerate(s['answers']) if a.get('correct'))]
            # deal the key to its slot without disturbing the distractors' order
            rest = [t for t in texts if t != correct]
            slot = KEY[sid]
            base['opts'] = [T(t) for t in rest[:slot] + [correct] + rest[slot:]]
            base['answer'] = slot
            base['points'] = s.get('points', 5)
            if s.get('relic'):
                base['relic'] = True
            base['fb'] = T(s['explanation'])
            assert s['correctNext'] == s['wrongNext'], sid
            nxt = s['correctNext']
            # the export ended the last question on `end:master`, so the score
            # never chose anything. 'resolve' hands it back to resolve().
            base['next'] = 'resolve' if nxt.startswith('end:') else nxt
        scenes[sid] = place(sid, base)

    scenes['plate']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': END_IMG[key], 'success': e.get('success', False),
            'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])})

    sc = DATA['meta']['scoring']
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Sherlock: The Blue Manuscript — Present Simple Questions Voxel RPG (A1-A2)',
        'description': 'An interactive A1-A2 English lesson from Forbes English: '
                       'Sherlock: The Blue Manuscript — Present Simple Questions Voxel RPG (A1-A2).',
        'langs': LANGS,
        # camp 1, Present Simple, on the Block Camp route map. The export asked
        # for #4BA3FF; README §2 says the camp colour wins when they differ.
        'accent': '#7A93B5',
        'accent_ink': '#0b1a12', 'deep': '#0b1420', 'panel': 'rgba(9,15,26,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        # the export shipped three endings, not four. "Almost solved" covers
        # both of the engine's middle outcomes — a good score short of perfect,
        # and a right final answer with an evidence block missing.
        'endings': {'master': 'end_master', 'complete': 'end_assistant',
                    'missing': 'end_assistant', 'failed': 'end_lost'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
