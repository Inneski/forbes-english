#!/usr/bin/env python3
"""The Last Bounty — Past Simple voxel-western RPG (A2).

    python3 lesson-template/build/build_last_bounty.py

Rebuilds block-camp/last-bounty-rpg.html from
lesson-template/build/rpg/last-bounty-rpg/data.json — the text of the
standalone export Innes sent on 2026-09-09, pulled out by
rpg/extract_standalone.py. Glosses come from the export's own `local` blocks,
flattened by rpg/make_translations.py.

The best ChatGPT-kind export received so far (docs/CHATGPT-RPG-BRIEF.md), and
the first that needed no correcting at all in three places the others all got
wrong: twenty-three filenames holding twenty-three *distinct* pictures, a
different nameable object on every scene, and an answer key already dealt
6/6/5 across the slots. Compare the Sherlock: The Blue Manuscript export of the
same week, which shipped ten pictures under eighteen filenames and could not be
published at all (docs/HANDOFF.md, 2026-09-10).

**Its scoring is repair-until-correct, and the export says so in prose rather
than in a flag.** `meta.scoring` is `tiles: 0, chances: 0, pass: 50` and the
briefing note reads "You always finish the story; score 50 out of 75 for a
reward ending." Chances at zero with no repair flag would mean the opposite —
this engine sends a player with no chances left to the failed ending on their
first wrong answer — so `repair: True` is what the export actually describes:
a wrong answer explains itself and lets the learner try again, points on the
first try only, and the run always reaches an ending. Same mode as Wonderland.

**`endingRoutes` is the mechanic this one added to the engine.** The export
maps the second story choice to an ending — RESCUE to "more than a reward",
PURSUE to "a coward found courage" — but the reward is meant to be earned:
50 of 75. The engine could already let a route name an ending; it could not
put a floor under it, so a player scoring 20 still collected the reward. Each
route now carries `endingMin`, and below it the ending falls through to the
normal ladder. Frankenstein sets none, so its two route endings are unchanged.

Fixed here, both the export's:

  * **The last question hard-coded an ending** (`next: 'end:rescue'`), so the
    route and the score decided nothing. It resolves now.
  * **`fire`'s hotspot was 62% of the picture tall**, which `validate()`
    rejects; it is the bank window, and the window is not that big.

Pictures: block-camp/last-bounty-rpg/*.webp, 1536x1024.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
SLUG = 'last-bounty-rpg'
BASE = os.path.join(HERE, 'rpg', SLUG)
DATA = json.load(open(os.path.join(BASE, 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE
PASS = DATA['meta']['scoring']['pass']

# ── hotspots: [cx, cy, w, h] in % of the 1536x1024 picture, then panel side,
# vertical anchor, optional panel width %. The export's own boxes, checked one
# at a time on a gridded contact sheet and again on a closed-scene screenshot.
# Where a box is trimmed the comment says why.
#
# A left panel is 46% of the frame and 54% with a gloss language on, so it
# reaches x=56. The width on each line below is the narrowest that holds that
# scene's copy without scrolling in German, Russian and Japanese, measured
# rather than guessed — this lesson's stories are longer than A Fistful of
# Lies's and the default 46 scrolled on seventeen of twenty-four screens.
#
# The export shipped its own panelWidth of 34-38 everywhere, which is the
# opposite move and the one rpg/README.md §1 rules out: never shrink to fit.
#
# Four objects — `door`, `brother`, `chase`, `cuffs` — sit within a few percent
# of the centre line, where no panel both holds the copy and clears the object.
# A centre panel is no help: with a gloss under every line it runs nearly the
# full height of the frame, so `top` and `bottom` anchoring change nothing.
# These four take the middle setting, measured: the object stays 70-100%
# visible and the panel scrolls 50-90px before the question is answered —
# about one line, and answering scrolls the panel to the feedback regardless.
HOT = {
    'cover':    ([86, 43, 17, 49], 'left',   'center'),       # the lantern over the doors
    'rules':    ([92, 64,  7, 11], 'left',   'center', 64),   # the glass on the bar; wide, five cards
    'door':     ([50, 52,  6, 35], 'right',  'center', 40),   # the saloon door, dead centre
    'mirror':   ([92, 64,  7, 11], 'left',   'center', 50),   # the glass
    'table':    ([67, 67, 14, 26], 'left',   'center'),       # the overturned table (trimmed from w31 h45)
    'stable':   ([85, 15, 10, 26], 'left',   'center', 50),   # the hanging rope
    'poster':   ([84, 55, 18, 52], 'left',   'center', 58),   # the wanted poster (trimmed from w34 h60)
    'approach': ([74, 20, 16, 36], 'center', 'bottom'),       # the ladder to the roof, high in the frame
    'roof':     ([89, 48, 20, 40], 'left',   'center', 50),   # the oil can
    'letter':   ([77, 54, 16, 16], 'left',   'center', 54),   # Tito's note
    'confess':  ([77, 78, 30, 20], 'left',   'center', 50),   # Tito's letter
    'brother':  ([56, 83,  8, 13], 'left',   'center', 46),   # the sheriff's badge
    'ambush':   ([89, 24, 20, 46], 'left',   'center', 62),   # the broken window
    # the export asked for h62, which validate() rejects — a hotspot may not be
    # more than 60% of the plate, and the bank window is not.
    'fire':     ([79, 36, 30, 52], 'left',   'center', 50),   # the bank window
    'priority': ([92, 54, 10, 24], 'center', 'bottom'),       # the bank padlock, far right
    'rescue':   ([93, 46,  8, 40], 'left',   'center'),       # the broken chain (pulled off the edge)
    'chase':    ([58, 74, 20, 24], 'left',   'center', 46),   # the fallen timber
    'return':   ([89, 75, 11, 25], 'left',   'center', 50),   # the teddy bear
    'duel':     ([92, 43, 10, 27], 'left',   'center', 62),   # the pocket watch
    'shot':     ([78, 86, 26, 16], 'left',   'center'),       # the dropped revolver (trimmed from w44)
    'cuffs':    ([54, 46,  9, 25], 'left',   'center', 42),   # the handcuffs
    'end_rescue':  ([59, 57, 12, 22], 'left', 'center', 42),  # the witness statement
    'end_pursuit': ([92, 20, 16, 29], 'left', 'center'),      # the sheriff's star
    'end_lost':    ([73, 77, 25, 16], 'left', 'center'),      # the pencil
}


def T(en, **rest):
    return dict(en=en, **rest)


# ── the kicker over the rules briefing: the one learner-facing string the
# export did not write, so its nine glosses live here.
BRIEFING_KICKER = T(
    'BEFORE YOU RIDE',
    es='ANTES DE CABALGAR', de='BEVOR DU LOSREITEST',
    fr='AVANT DE PARTIR', it='PRIMA DI CAVALCARE',
    pt='ANTES DE CAVALGAR', ru='ПЕРЕД ДОРОГОЙ',
    ar='قبل أن تنطلق', zh='上路之前', ja='旅立つ前に')

# ── repair mode's chrome is written for Wonderland's spells. All of it is
# reworded here; the engine's defaults would put "SPELL REPAIRED" on a western.
LABELS = {
    'progress': T('QUESTIONS',
                  es='PREGUNTAS', de='FRAGEN', fr='QUESTIONS', it='DOMANDE', pt='PERGUNTAS',
                  ru='ВОПРОСЫ', ar='الأسئلة', zh='题目', ja='問題'),
    'correct': T('RIGHT FIRST TIME · +{p} POINTS',
                 es='BIEN A LA PRIMERA · +{p} PUNTOS', de='GLEICH RICHTIG · +{p} PUNKTE',
                 fr='JUSTE DU PREMIER COUP · +{p} POINTS', it='GIUSTO AL PRIMO COLPO · +{p} PUNTI',
                 pt='CERTO À PRIMEIRA · +{p} PONTOS', ru='ВЕРНО С ПЕРВОГО РАЗА · +{p} ОЧКОВ',
                 ar='صحيح من أول مرة · +{p} نقاط', zh='一次答对 · +{p} 分',
                 ja='一発正解 · +{p} ポイント'),
    'repaired': T('PUT RIGHT',
                  es='CORREGIDO', de='BERICHTIGT', fr='CORRIGÉ', it='CORRETTO', pt='CORRIGIDO',
                  ru='ИСПРАВЛЕНО', ar='صُحّح', zh='已改正', ja='なおした'),
    'tryAgain': T('NOT QUITE · TRY ANOTHER',
                  es='CASI · PRUEBA OTRA', de='FAST · VERSUCH EINE ANDERE',
                  fr='PRESQUE · ESSAIE UNE AUTRE', it='QUASI · PROVA UN\'ALTRA',
                  pt='QUASE · TENTA OUTRA', ru='ПОЧТИ · ПОПРОБУЙ ДРУГОЙ',
                  ar='تقريبًا · جرّب إجابة أخرى', zh='差一点 · 再试一个',
                  ja='おしい · 別の答えを試そう'),
    'review': T('REVIEW WHAT YOU PUT RIGHT',
                es='REPASA LO QUE CORREGISTE', de='SIEH DIR AN, WAS DU BERICHTIGT HAST',
                fr='REVOIS CE QUE TU AS CORRIGÉ', it='RIVEDI CIÒ CHE HAI CORRETTO',
                pt='REVÊ O QUE CORRIGISTE', ru='ПОВТОРИ ТО, ЧТО ИСПРАВИЛ',
                ar='راجع ما صحّحته', zh='复习你改正的题', ja='なおした問題を復習'),
    'perfect': T('Every answer right the first time. A clean ride.',
                 es='Todas las respuestas bien a la primera. Un viaje limpio.',
                 de='Jede Antwort gleich richtig. Ein sauberer Ritt.',
                 fr='Chaque réponse juste du premier coup. Un sans-faute.',
                 it='Ogni risposta giusta al primo colpo. Una cavalcata pulita.',
                 pt='Todas as respostas certas à primeira. Uma cavalgada limpa.',
                 ru='Каждый ответ верен с первого раза. Чистый путь.',
                 ar='كل إجابة صحيحة من أول مرة. رحلة نظيفة.',
                 zh='每题都一次答对。一趟干净的路。',
                 ja='すべて一発正解。完璧な旅だった。'),
    'firstTry': T('right first time',
                  es='a la primera', de='beim ersten Versuch', fr='du premier coup',
                  it='al primo colpo', pt='à primeira', ru='с первого раза',
                  ar='من أول مرة', zh='一次答对', ja='一発正解'),
    'restart': T('RIDE ANOTHER ROUTE',
                 es='CABALGA OTRA RUTA', de='EINE ANDERE ROUTE REITEN',
                 fr='PRENDRE UNE AUTRE ROUTE', it='CAVALCA UN\'ALTRA ROTTA',
                 pt='CAVALGAR OUTRA ROTA', ru='ПРОЕХАТЬ ДРУГИМ ПУТЁМ',
                 ar='اسلك طريقًا آخر', zh='走另一条路', ja='別の道を行く'),
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
            'kind': 'rules', 'img': b['image'],
            'k': BRIEFING_KICKER, 'title': T(b['title']),
            'rules': [{'name': T(card['head']), 'form': T(card['text'])} for card in b['cards']],
            'note': T(b['note']), 'button': T(b['button']),
            'next': DATA['first']}),
    }

    # the second story choice decides which reward ending the run reaches
    ending_of = DATA['meta'].get('endingRoutes', {})

    for sid, s in DATA['scenes'].items():
        base = {'img': s['image'], 'k': T(s['act']), 'title': T(s['title']),
                'story': T(s['story'])}
        if 'choices' in s:
            base['kind'] = 'choice'
            base['routes'] = []
            for ch in s['choices']:
                r = {'name': T(ch['label']), 'desc': T(ch['note']),
                     'route': ch['route'], 'target': ch['next']}
                if ch['route'] in ending_of:
                    # the route picks the reward ending; the floor decides
                    # whether one was earned. Both are success endings, so
                    # neither is upgraded by a flawless run.
                    r['ending'] = ending_of[ch['route']]
                    r['endingMin'] = PASS
                base['routes'].append(r)
        else:
            base['kind'] = 'question'
            base['clue'] = T(s['clue'])
            base['prompt'] = T(s['prompt'])
            base['opts'] = [T(a['text']) for a in s['answers']]
            base['answer'] = next(i for i, a in enumerate(s['answers']) if a.get('correct'))
            base['points'] = s.get('points', 5)
            base['fb'] = T(s['explanation'])
            assert s['correctNext'] == s['wrongNext'], sid
            nxt = s['correctNext']
            # the export ended the last question on `end:rescue`, so neither the
            # route nor the score chose anything. 'resolve' hands it back.
            base['next'] = 'resolve' if nxt.startswith('end:') else nxt
        scenes[sid] = place(sid, base)

    scenes['cuffs']['final'] = True

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': e['image'], 'success': e.get('success', False),
            'k': T(e['label']), 'title': T(e['title']), 'story': T(e['text'])})

    sc = DATA['meta']['scoring']
    total = 15   # questions on any one path: 5 + 1 + 4 + 1 + 4
    return {
        'file': 'block-camp/%s.html' % SLUG,
        'img_dir': 'block-camp/%s' % SLUG,
        'title': 'The Last Bounty — Past Simple Voxel Western RPG (A2)',
        'description': 'An interactive A2 English lesson from Forbes English: '
                       'The Last Bounty — Past Simple Voxel Western RPG (A2).',
        'langs': LANGS,
        # camp 3, Past Simple, on the Block Camp route map — the same camp as
        # A Fistful of Lies, and the same colour. The export asked for the
        # hub's gold #e8c04a; README §2 says the camp colour wins.
        'accent': '#B08968',
        'accent_ink': '#0b1a12', 'deep': '#1a1008', 'panel': 'rgba(18,12,6,.88)',
        'labels': LABELS,
        'start': 'cover', 'scenes': scenes,
        # three endings, two of them rewards chosen by the second story choice.
        # `master` and `complete` are never reached: every player passes that
        # choice, so `endingPick` is always set and answers first.
        'endings': {'master': 'end_rescue', 'complete': 'end_rescue',
                    'missing': 'end_lost', 'failed': 'end_lost',
                    'rescue': 'end_rescue', 'pursuit': 'end_pursuit'},
        'max': sc['max'], 'points': sc['points'], 'tiles': sc['tiles'],
        'chances': sc['chances'], 'complete_score': sc['pass'],
        'repair': True, 'total': total,
    }


if __name__ == '__main__':
    rpg.assemble(rpg.apply_translations(build(), os.path.join(BASE, 'translations')))
