#!/usr/bin/env python3
"""Kraken: The Black Tide — Present Perfect West Highland RPG (B1).

    py lesson-template/build/build_kraken_black_tide.py

Builds block-camp/kraken-black-tide-rpg.html from
lesson-template/build/rpg/kraken-black-tide-rpg/data.json.

**A fourth kind of source: no export at all.** The five RPGs before this one
were rebuilds of a standalone HTML file somebody else generated
(rpg/README.md §2 names the three kinds). This one was written here, to
docs/CHATGPT-RPG-BRIEF.md, from a one-line commission: Jaws, on the west coast
of Scotland, with a kraken. So `data.json` is not extracted from anything —
it is the script, in the export's own shape, and BIBLE.md beside it is the
document the writing was checked against. ART-BRIEF.md carries the style
contract, the character sheet and the thirty-two image prompts, because the
pictures were commissioned after the words for once, which is why every
plate's object sits right of frame and every panel in this game sits left.

Grammar: Present Perfect, so the accent is Block Camp camp 7's #2E7D65 — the
only colour in the page (rpg/README.md §1). Eighteen questions on either path,
two forks, four marker barrels, three chances: max 90, pass 75, which is the
score you still reach after spending all three chances.

The answer key was dealt across the three slots by assemble-script.py in the
data directory rather than left where the writing put it — the script was
written with `correct`/`wrong1`/`wrong2` as named fields precisely so the slot
could never become a habit. `_check_answer_key` in rpg.py is what proves it
held: no slot over 40%, and no key the longest option in its scene.

Pictures: block-camp/kraken-black-tide-rpg/NN_name.webp, 1536x1024 WebP,
prepared by rpg/kraken-black-tide-rpg/prep-plates.py.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'kraken-black-tide-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 plate, then panel side,
# vertical anchor, optional panel width %.
#
# ART-BRIEF.md §"The composition contract" put the lit object right of x=60 on
# every plate on purpose, so the panel sits LEFT in all thirty-three scenes and
# not one of them needs a centre panel — including the two route choices, which
# README §3 would otherwise centre. A left panel is 46% of the frame and grows
# to 54% the moment a gloss language is on, so it reaches x=56; every box below
# starts to the right of that.
#
# These are the brief's own draft boxes. Verify each one on a gridded contact
# sheet and then on a closed-scene screenshot before shipping (README §3-4) —
# a hotspot that missed is obvious in a thumbnail and invisible in this table.
HOT = {
    'cover':    ([74, 62, 20, 16], 'left', 'center'),        # the four barrels on the rail
    'rules':    ([79, 45, 14, 22], 'left', 'center', 56),    # the bitten barrel; wide, five cards
    'drift':    ([76, 66, 13, 14], 'left', 'center'),        # the yellow barrel in the stern
    'bell':     ([80, 38, 12, 18], 'left', 'center'),        # the brass harbour bell
    'provost':  ([78, 60, 16, 20], 'left', 'center'),        # the red regatta buoy
    'hoy':      ([75, 63, 17, 17], 'left', 'center'),        # the sonar case
    'jar':      ([77, 55, 12, 18], 'left', 'center'),        # the glass jar
    'shed':     ([79, 45, 14, 22], 'left', 'center'),        # the yellow barrel on the wall
    'sound':    ([72, 52, 11, 26], 'left', 'center', 40),    # the channel marker
    'reef1':    ([79, 62, 13, 15], 'left', 'center'),        # the orange sonar float
    'reef2':    ([77, 58, 18, 20], 'left', 'center'),        # the torn net
    'reef3':    ([78, 60, 12, 12], 'left', 'center'),        # the last seal on the skerry
    'reef4':    ([76, 66, 20, 16], 'left', 'center'),        # the scarred hull plate
    'cave1':    ([75, 50, 11, 18], 'left', 'center'),        # the storm lantern
    'cave2':    ([78, 57, 12, 14], 'left', 'center'),        # the dinghy lamp
    'cave3':    ([77, 62, 17, 16], 'left', 'center'),        # the broken creel
    'cave4':    ([74, 44, 20, 12], 'left', 'center'),        # the wet tide line
    'wreck1':   ([76, 58, 13, 15], 'left', 'center'),        # the barrel rising off the wreck
    'wreck2':   ([78, 61, 14, 13], 'left', 'center'),        # the old harpoon head
    'wreck3':   ([79, 55, 13, 19], 'left', 'center'),        # the brass porthole
    'decision': ([74, 57, 12, 15], 'left', 'center', 40),    # the Selkie's compass
    'corry1':   ([77, 63, 15, 15], 'left', 'center'),        # the rope on the capstan
    'corry2':   ([78, 55, 17, 24], 'left', 'center'),        # the arm over the gunwale
    'corry3':   ([76, 52, 11, 15], 'left', 'center'),        # the engine lamp
    'night1':   ([79, 36, 11, 20], 'left', 'center'),        # the harbour lamp
    'night2':   ([75, 57, 10, 11], 'left', 'center'),        # the last lit lamp on the water
    'night3':   ([77, 64, 16, 17], 'left', 'center'),        # the strained mooring rope
    'barrels':  ([76, 58, 15, 18], 'left', 'center'),        # the barrel going over the rail
    'last':     ([78, 60, 16, 20], 'left', 'center'),        # the harpoon line running out
    'end_master':   ([74, 55, 18, 18], 'left', 'center'),    # the open harbour mouth
    'end_complete': ([77, 62, 18, 16], 'left', 'center'),    # the green hull on the slip
    'end_missing':  ([75, 58, 20, 20], 'left', 'center'),    # the turning water of the Corry
    'end_failed':   ([78, 52, 14, 22], 'left', 'center'),    # the empty berth and its lamp
}

# ── a plate for each ending. Four endings sharing the cover reads as one
# ending with four captions (the Fistful rebuild, 2026-09-10), so each takes
# the picture its own closing text describes. `success` drives the engine's
# win chrome.
ENDINGS = {
    'master':   ('29_ending_master.webp',   True),
    'complete': ('30_ending_complete.webp', True),
    'missing':  ('31_ending_missing.webp',  False),
    'failed':   ('32_ending_failed.webp',   False),
}

# The rules briefing has no plate of its own: it takes the shed, which is the
# one room in the lesson with the four barrels on the wall — the thing the
# whole scoring system is about.
RULES_IMAGE = '07_q6_shed.webp'


def T(en, **rest):
    return dict(en=en, **rest)


# ── the kicker over the rules briefing. Every other learner-facing string in
# this lesson is glossed from translations/; this one is written here because
# it belongs to the engine's briefing screen rather than to the script.
BRIEFING_KICKER = T(
    'BEFORE YOU GO OUT',
    es='ANTES DE SALIR AL MAR', de='BEVOR DU HINAUSFÄHRST',
    fr='AVANT DE PRENDRE LA MER', it='PRIMA DI USCIRE IN MARE',
    pt='ANTES DE SAIR PARA O MAR', ru='ПЕРЕД ВЫХОДОМ В МОРЕ',
    ar='قبل أن تبحر', zh='出海之前', ja='海に出る前に')

# ── HUD and button words. The tiles are Quinn's marker barrels, so they are
# not "tiles" anywhere a learner can see.
LABELS = {
    'tiles': T('MARKER BARRELS',
               es='BOYAS', de='MARKIERTONNEN', fr='BOUÉES', it='BOE', pt='BOIAS',
               ru='БУИ', ar='البراميل', zh='浮标桶', ja='マーカー樽'),
    'relic': T('MARKER BARREL SECURED · +{p} POINTS',
               es='BOYA ASEGURADA · +{p} PUNTOS', de='MARKIERTONNE GESICHERT · +{p} PUNKTE',
               fr='BOUÉE FIXÉE · +{p} POINTS', it='BOA ASSICURATA · +{p} PUNTI',
               pt='BOIA PRESA · +{p} PONTOS', ru='БУЙ ЗАКРЕПЛЁН · +{p} ОЧКОВ',
               ar='تم تثبيت البرميل · +{p} نقاط', zh='浮标桶已固定 · +{p} 分',
               ja='マーカー樽を確保 · +{p} ポイント'),
    'restart': T('SAIL AGAIN',
                 es='ZARPAR DE NUEVO', de='NOCH EINMAL AUSLAUFEN', fr='REPRENDRE LA MER',
                 it='SALPARE DI NUOVO', pt='ZARPAR DE NOVO', ru='ВЫЙТИ В МОРЕ СНОВА',
                 ar='أبحر مجددًا', zh='再次启航', ja='もう一度出航する'),
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
            'kind': 'rules', 'img': RULES_IMAGE,
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
            # a wrong answer costs a chance, not a detour: both roads out of a
            # question scene are the same road (README §9)
            assert s['correctNext'] == s['wrongNext'], sid
            base['next'] = s['correctNext']
        scenes[sid] = place(sid, base)

    # the eighteenth question is the one that decides whether a flawless run
    # reaches the master ending
    scenes['last']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        img, success = ENDINGS[key]
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': img, 'success': success,
            'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])})

    sc = DATA['meta']['scoring']
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'Kraken: The Black Tide — Present Perfect West Highland RPG (B1)',
        'description': 'An interactive B1 English lesson from Forbes English: '
                       'Kraken: The Black Tide — Present Perfect West Highland RPG (B1).',
        'langs': LANGS,
        # camp 7, Present Perfect, on the Block Camp route map
        'accent': '#2E7D65',
        'accent_ink': '#f2f7f3', 'deep': '#08161a', 'panel': 'rgba(6,18,22,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        'endings': {'master': 'end_master', 'complete': 'end_complete',
                    'missing': 'end_missing', 'failed': 'end_failed'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
