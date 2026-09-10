#!/usr/bin/env python3
"""Sherlock Holmes: The Blue Hour — Present Simple RPG (A2).

    python3 lesson-template/build/build_sherlock_blue_hour.py

Rebuilds block-camp/sherlock-blue-hour-rpg.html from
lesson-template/build/rpg/sherlock-blue-hour-rpg/data.json — the text of the
standalone export Innes sent on 2026-09-10, pulled out by
rpg/extract_standalone.py. Glosses come from the export's own `local` blocks,
flattened by rpg/make_translations.py.

**This replaces Sherlock: The Blue Manuscript**, which was built and then never
published: that export shipped eighteen picture filenames holding ten distinct
images, so a single run showed the same picture two or three times. Innes sent
this one instead — "I wasn't happy with the blue manuscript" — and it is a
different class of export. 22 filenames, 22 distinct pictures, no scene sharing
a plate with another, a specific nameable object on every one, an answer key
already dealt 7/6/6, an explanation on every question, and all nine of
HOUSE-STYLE §8's languages throughout. The Blue Manuscript's builder, data and
artwork are deleted in the same commit.

Four things this builder does that the export did not:

  * **A picture for each of the four endings and for the briefing.** The export
    pointed all five at the cover. 22 plates cover a cover, nineteen questions
    and two forks exactly, so every one of these five reuses a question's plate;
    they are chosen to be as far from their twin as the graph allows, and the
    endings are terminal, where a repeat does not read as one.
  * **Trims two hotspots that `validate()` rejects** — `wheel` at 74% of the
    plate tall and `cable` at 65%. The limit is 60, and neither object is that
    big.
  * **Drops the export's `resolve` pseudo-scene.** It is a scene-shaped object
    with `type: "resolve"` listing the four endings, which is this generator's
    way of saying "the last question resolves from the score". This engine says
    that with `next: 'resolve'` on the question itself, which `arrest` already
    carries, so the pseudo-scene is skipped rather than translated.
  * **Writes the briefing kicker and the HUD words**, the only learner-facing
    strings the export does not carry.

Pictures: block-camp/sherlock-blue-hour-rpg/NN_name.webp, 1536x1024. Note the
style: this one is painted Victorian London, not the voxel look the other five
adventures share, so its catalogue title says "London RPG" and not "Voxel RPG".
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'sherlock-blue-hour-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

# the generator's "the score picks the ending" marker, not a scene
SKIP = ('resolve',)

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. These are the export's own boxes,
# rounded, and checked one at a time on closed-scene screenshots.
#
# A left panel is 46% of the frame and 54% with a gloss language on, so it
# reaches x=56. Every object here sits right of x=60, which is why this lesson
# needs almost no panel juggling: the art was composed for it.
HOT = {
    'cover':    ([76, 59, 14, 14], 'left',   'center'),       # the Blue Star
    'rules':    ([92, 34,  9, 52], 'left',   'center', 56),   # the window; wide, four cards
    'letter':   ([83, 67, 19, 13], 'left',   'center'),       # the envelope
    'clock':    ([79, 26, 21, 34], 'left',   'center'),       # the clock
    'street':   ([64, 20, 22, 13], 'left',   'center', 40),   # the signpost, high and left of centre
    'pawn':     ([70, 60, 13, 15], 'left',   'center'),       # the watch
    'seal':     ([71, 51, 13, 15], 'left',   'center'),       # the seal
    'stable':   ([73, 37,  9, 20], 'left',   'center'),       # the horseshoe
    # export asked for h74; validate() caps a hotspot at 60% of the plate
    'wheel':    ([88, 41, 20, 56], 'left',   'center'),       # the wheel
    'window':   ([92, 34,  9, 58], 'left',   'center'),       # the window
    'guard':    ([76, 60,  8,  8], 'left',   'center'),       # the cup
    'mud':      ([78, 78, 20, 24], 'left',   'center'),       # the bootprint
    'routes':   ([74, 30, 15,  8], 'left',   'center', 46),   # the signpost
    'owl':      ([69, 48, 16, 33], 'left',   'center'),       # the owl
    'feather':  ([79, 65, 25, 23], 'left',   'center'),       # the feather
    'boat':     ([64, 62, 20, 30], 'left',   'center', 44),   # the boat
    'cargo':    ([86, 65, 24, 45], 'left',   'center'),       # the crate
    'ledger':   ([79, 65, 33, 24], 'left',   'center'),       # the ledger
    # export asked for h65; same cap as `wheel`
    'cable':    ([94, 64, 11, 58], 'left',   'center'),       # the cable
    'portrait': ([83, 30, 24, 57], 'left',   'center'),       # the portrait
    'bell':     ([87, 46, 27, 55], 'left',   'center'),       # the bell
    'weight':   ([67, 48, 18, 56], 'left',   'center', 44),   # the weight
    'arrest':   ([74, 53,  5, 19], 'left',   'center'),       # the handcuffs
    'end_master':   ([74, 53,  5, 19], 'left', 'center'),
    'end_complete': ([79, 65, 33, 24], 'left', 'center'),
    'end_missing':  ([94, 64, 11, 58], 'left', 'center'),
    'end_failed':   ([64, 62, 20, 30], 'left', 'center', 44),
}

# ── a plate for each ending, and for the briefing. The export pointed all five
# at the cover.
END_IMG = {
    'master':   '22_arrest.webp',   # the case closed, and the cuffs that closed it
    'complete': '17_ledger.webp',   # the four pieces of evidence, written down
    'missing':  '18_cable.webp',    # "one link is missing"
    'failed':   '15_boat.webp',     # "the boat disappears into blue fog"
}
RULES_IMG = '09_window.webp'        # mid-lesson, and the furthest plate from its own scene


def T(en, **rest):
    return dict(en=en, **rest)


# ── the strings the export does not carry, so their nine glosses live here.
BRIEFING_KICKER = T(
    'BEFORE THE BELL',
    es='ANTES DE LA CAMPANA', de='VOR DEM GLOCKENSCHLAG',
    fr='AVANT LA CLOCHE', it='PRIMA DELLA CAMPANA',
    pt='ANTES DO SINO', ru='ДО УДАРА КОЛОКОЛА',
    ar='قبل دقّة الجرس', zh='钟声之前', ja='鐘が鳴る前に')

LABELS = {
    'tiles': T('EVIDENCE',
               es='PRUEBAS', de='BEWEISE', fr='PREUVES', it='PROVE', pt='PROVAS',
               ru='УЛИКИ', ar='الأدلة', zh='证据', ja='証拠'),
    'relic': T('EVIDENCE TILE FOUND · +{p} POINTS',
               es='PRUEBA ENCONTRADA · +{p} PUNTOS', de='BEWEISSTÜCK GEFUNDEN · +{p} PUNKTE',
               fr='PREUVE TROUVÉE · +{p} POINTS', it='PROVA TROVATA · +{p} PUNTI',
               pt='PROVA ENCONTRADA · +{p} PONTOS', ru='УЛИКА НАЙДЕНА · +{p} ОЧКОВ',
               ar='عُثر على دليل · +{p} نقاط', zh='找到证据 · +{p} 分',
               ja='証拠を発見 · +{p} ポイント'),
    'restart': T('REOPEN THE CASE',
                 es='REABRE EL CASO', de='DEN FALL NEU ÖFFNEN', fr='ROUVRIR L\'ENQUÊTE',
                 it='RIAPRI IL CASO', pt='REABRIR O CASO', ru='ОТКРЫТЬ ДЕЛО СНОВА',
                 ar='أعد فتح القضية', zh='重启这桩案子', ja='事件を再開する'),
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
        if sid in SKIP:
            continue
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
            nxt = s['correctNext']
            base['next'] = 'resolve' if nxt in SKIP or nxt.startswith('end:') else nxt
        scenes[sid] = place(sid, base)

    # the last question decides whether a flawless run reaches the master ending
    scenes['arrest']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': END_IMG[key], 'success': key in ('master', 'complete'),
            'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])})

    sc = DATA['meta']['scoring']
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Sherlock Holmes: The Blue Hour — Present Simple London RPG (A2)',
        'description': 'An interactive A2 English lesson from Forbes English: '
                       'Sherlock Holmes: The Blue Hour — Present Simple London RPG (A2).',
        'langs': LANGS,
        # camp 1, Present Simple, on the Block Camp route map. The export asked
        # for #62caff; README §2 says the camp colour wins when they differ.
        'accent': '#7A93B5',
        'accent_ink': '#0b1420', 'deep': '#0a1422', 'panel': 'rgba(8,14,24,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete',
                    'missing': 'end_missing', 'failed': 'end_failed'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
