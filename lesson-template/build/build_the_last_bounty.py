#!/usr/bin/env python3
"""The Last Bounty — Past Simple voxel-Western RPG (A2).

    python3 lesson-template/build/build_the_last_bounty.py

Rebuilds block-camp/the-last-bounty-rpg.html from
lesson-template/build/rpg/the-last-bounty-rpg/data.json, the text of the
standalone export Innes sent on 2026-09-09 (incoming/The-Last-Bounty.html,
window.BOUNTY_GAME_DATA), pulled out by rpg/extract_standalone.py.

This is the "ChatGPT kind" export (HANDOFF-rpg.md §3): built from
docs/CHATGPT-RPG-BRIEF.md, it already carries `meta`, a `briefing` object
(cards + note + button), a per-scene `hotspot` and `panelWidth`, a per-scene
`explanation`, and all nine languages (es de fr it pt ru ar zh ja) in every
scene's `local` block — so unlike Lost Yellow Road (es/de only) or Wonderland
(no gloss at all), this builder needs no `translations/` directory: every
learner-facing field is read straight out of the export in all nine
languages. Hotspots were eyeballed against every picture (rpg/README.md §3)
and are the export's own numbers except `door` and `chase`, where the named
object sits close to the frame's centre and the export's left/right math
(mirrored below) put the panel over the busier half of the picture — both
were flipped to the empty side by eye.

Pictures: block-camp/the-last-bounty-rpg/<name>.webp, 1536×1024, as exported.

The story: two branching narrative choices (a stakeout route and a bank
crisis) and three endings. The export's own game rules stay as sent —
5 points a correct answer, no tiles, no chances/hearts (`meta.scoring`) — but
that "no chances" design needed a small, generic fix in rpg.py: the engine's
resolve()/advance() previously treated `chances:0` as "zero lives", which
made ANY wrong answer end the game immediately, contradicting the export's
own briefing note ("You always finish the story"). Both functions now treat
the score threshold as the good-standing test when a game has no chances
mechanic at all — see the comment on resolve() in rpg.py. The two story
choices route to the two reward endings via chooseRoute()'s existing
`ending` field (keyed off meta.endingRoutes); scoring below the pass
threshold (50/75) sends either route to the one consolation ending
instead. The HUD's TILES badge is now hidden when a game has none, the way
CHANCES already was — this is the first RPG shipped with tiles:0.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'rpg'))
import rpg

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = json.load(open(os.path.join(HERE, 'rpg', 'the-last-bounty-rpg', 'data.json'), encoding='utf-8'))
LANGS = rpg.NINE   # all nine ship straight from the export — see docstring


def L(en, local, field):
    """Every language present in `local` for one field, English on top."""
    d = {'en': en}
    for lang in LANGS:
        v = (local.get(lang) or {}).get(field)
        if v is not None:
            d[lang] = v
    return d


def Li(en, local, field, i):
    """Same as L() for the i-th item of a list field (cover 'rules' chips)."""
    d = {'en': en}
    for lang in LANGS:
        arr = (local.get(lang) or {}).get(field)
        if arr is not None and i < len(arr):
            d[lang] = arr[i]
    return d


def Lsub(en, local, field, i, subfield):
    """Every language for one sub-field of the i-th item of a list of dicts
    (the briefing's 'cards' [{head,text}], a choice scene's 'choices'
    [{label,note}])."""
    d = {'en': en}
    for lang in LANGS:
        arr = (local.get(lang) or {}).get(field)
        if arr is not None and i < len(arr) and subfield in arr[i]:
            d[lang] = arr[i][subfield]
    return d


# ── hotspots: [cx, cy, w, h] in % of the 1536×1024 picture (the export's own
# numbers), then panel side, vertical anchor, optional panel width %.
# Checked against every picture with rpg/README.md §3's contact-sheet method
# (scratch_hotcheck/*.jpg, not committed) — every glow sits on the named
# object. `door` and `chase` are overridden: both objects sit within a few
# percent of centre, and simple left/right-of-centre math put the panel over
# the busy half of the frame (the gunman and Tito; the horse and riders) —
# eyeballing put the panel on the genuinely empty half instead.
def _hot():
    def side_for(x):
        return 'left' if x > 50 else 'right'
    hot = {}
    c = DATA['cover']['hotspot']
    hot['cover'] = ([c['x'], c['y'], c['w'], c['h']], side_for(c['x']), 'center', DATA['cover'].get('panelWidth'))
    b = DATA['briefing']['hotspot']
    hot['rules'] = ([b['x'], b['y'], b['w'], b['h']], side_for(b['x']), 'center', 56)  # widened: 5 rule cards
    for sid, s in DATA['scenes'].items():
        h = s['hotspot']
        if 'choices' in s:
            hot[sid] = ([h['x'], h['y'], h['w'], h['h']], 'center', 'top', s.get('panelWidth'))
        else:
            hot[sid] = ([h['x'], h['y'], h['w'], h['h']], side_for(h['x']), 'center', s.get('panelWidth'))
    for key, e in DATA['endings'].items():
        h = e['hotspot']
        hot['end_' + key] = ([h['x'], h['y'], h['w'], h['h']], side_for(h['x']), 'center')
    hot['door'] = (hot['door'][0], 'left', 'center', hot['door'][3])
    hot['chase'] = (hot['chase'][0], 'left', 'center', hot['chase'][3])
    # the engine caps a hotspot at 60% of the picture on a side; the export's
    # bank window box (a 3x2 window, most of the picture's right third) is
    # 62% tall — clipped to fit, still squarely on the window.
    fw, fh = hot['fire'][0][2], min(hot['fire'][0][3], 60)
    hot['fire'] = ([hot['fire'][0][0], hot['fire'][0][1], fw, fh],) + hot['fire'][1:]
    return hot


HOT = _hot()


def place(sid, scene):
    hot, pos, v = HOT[sid][:3]
    scene.update({'hot': hot, 'pos': pos, 'v': v})
    if len(HOT[sid]) > 3 and HOT[sid][3]:
        scene['width'] = HOT[sid][3]
    return scene


def build():
    c, cl = DATA['cover'], DATA['cover']['local']
    br, brl = DATA['briefing'], DATA['briefing']['local']
    scenes = {
        'cover': place('cover', {
            'kind': 'intro', 'img': c['image'],
            'k': L(c['eyebrow'], cl, 'eyebrow'),
            'title': L(c['title'], cl, 'title'),
            'story': L(c['lead'], cl, 'lead'),
            'rules': [Li(r, cl, 'rules', i) for i, r in enumerate(c['rules'])],
            'start': L(c['start'], cl, 'start'),
            'small': L(c['small'], cl, 'small'),
            'next': 'rules'}),
        'rules': place('rules', {
            # 'k' left unset: the export gives the briefing no separate kicker
            # line (RULES.md's rules-intro layout doesn't need one either).
            'kind': 'rules', 'img': br['image'],
            'title': L(br['title'], brl, 'title'),
            # the briefing's cards are {head, text} — the engine's rule cards
            # want {name, form}; head -> name, text -> form.
            'rules': [{'name': Lsub(card['head'], brl, 'cards', i, 'head'),
                       'form': Lsub(card['text'], brl, 'cards', i, 'text')}
                      for i, card in enumerate(br['cards'])],
            'note': L(br['note'], brl, 'note'),
            'button': L(br['button'], brl, 'button'),
            'next': DATA['first'],
        }),
    }

    for sid, s in DATA['scenes'].items():
        l = s['local']
        base = {'img': s['image'],
                'k': L(s['act'], l, 'act'),
                'title': L(s['title'], l, 'title'),
                'story': L(s['story'], l, 'story')}
        if 'choices' in s:
            base['kind'] = 'choice'
            routes = []
            for i, ch in enumerate(s['choices']):
                route = {'name': Lsub(ch['label'], l, 'choices', i, 'label'),
                         'desc': Lsub(ch['note'], l, 'choices', i, 'note'),
                         'route': ch['route'], 'target': ch['next']}
                if sid == 'priority':
                    route['ending'] = DATA['meta']['endingRoutes'][ch['route']]
                routes.append(route)
            base['routes'] = routes
        else:
            base['kind'] = 'question'
            base['clue'] = L(s['clue'], l, 'clue')
            base['prompt'] = L(s['prompt'], l, 'prompt')
            base['opts'] = [{'en': a['text']} for a in s['answers']]   # not glossed in this export
            base['answer'] = next(i for i, a in enumerate(s['answers']) if a.get('correct'))
            base['points'] = s.get('points', 5)
            base['fb'] = L(s['explanation'], l, 'explanation')
            # the export sent wrong answers down the same road as right ones;
            # the score threshold is the penalty, not a detour (see docstring)
            assert s['correctNext'] == s['wrongNext'], sid
            if sid == 'cuffs':
                base['final'] = True
                base['next'] = 'resolve'
            else:
                base['next'] = s['correctNext']
        scenes[sid] = place(sid, base)

    for key, e in DATA['endings'].items():
        sid = 'end_' + key
        el = e['local']
        scenes[sid] = place(sid, {
            'kind': 'ending', 'img': e['image'], 'success': e['success'],
            'k': L(e['label'], el, 'label'),
            'title': L(e['title'], el, 'title'),
            'story': L(e['text'], el, 'text')})

    spec = {
        'file': 'block-camp/the-last-bounty-rpg.html',
        'img_dir': 'block-camp/the-last-bounty-rpg',
        'title': 'The Last Bounty — Past Simple Voxel Western RPG (A2)',
        'description': 'An interactive A2 English lesson from Forbes English: The Last Bounty — Past Simple Voxel Western RPG (A2).',
        'langs': LANGS,
        'accent': '#B08968',        # camp 3, Past Simple, on the Block Camp route map
        'accent_ink': '#0b1a12', 'deep': '#241a10', 'panel': 'rgba(22,15,3,.88)',
        'start': 'cover', 'scenes': scenes,
        'endings': {'rescue': 'end_rescue', 'pursuit': 'end_pursuit', 'failed': 'end_lost'},
        'max': DATA['meta']['scoring']['max'], 'points': DATA['meta']['scoring']['points'],
        'tiles': DATA['meta']['scoring']['tiles'], 'chances': DATA['meta']['scoring']['chances'],
        'complete_score': DATA['meta']['scoring']['pass'],
    }
    return spec


if __name__ == '__main__':
    rpg.assemble(build())
