#!/usr/bin/env python3
"""Block Camp flags: an achievement record of the flags a learner has planted
on every camp of the climb and every station of the descent - and, since
2026-10-02, the Lookout those flags raise (docs/LOOKOUT-DESIGN.md).

    py lesson-template/build/block-camp-flags/build.py            # write both
    py lesson-template/build/block-camp-flags/build.py --check    # exit 1 if stale
                                                                  # or a caption,
                                                                  # contrast pair or
                                                                  # plate check fails
    py lesson-template/build/block-camp-flags/build.py --self-test  # the caption gate
                                                                  # refuses wrong-tense
                                                                  # probes and broken
                                                                  # copies

Innes, 2026-10-02: "Users need some kind of achievement record of flags
obtained from all the camps." Then: "think of a way to make this more fun
like you are building or trying to reach something" - Raise the Lookout.

Writes two files:

  block-camp/camp-flags.js   from template.js - window.CampFlags: the flag
                             table, the rule, the record, the pixel sprite,
                             the route-map decorations and the Lookout
                             (lookout(), meter(), lampSprite()). Loaded by
                             camp-end.js on every deck, by both route maps
                             and by flags.html.
  block-camp/flags.html      from template.html - "Your Lookout": the code
                             tower on a canvas stage with its HUD, sheets and
                             build-in, then "the parts list" (the eighteen
                             flags in two rows, as storeys and lamps).

and keeps one cache beside this file:

  plate-tokens.json          the colours sampled from the two plates, with
                             each plate's sha1. Rebuilt (PIL) only when a
                             plate or a sample box changes; --check fails if a
                             plate changed and the cache was not re-sampled.

THE TABLE IS THE HUB'S. Camps, stations, names and colours are
block-camp-hub/build.py's CLIMB, DESCENT, CAMP and INK, imported the way the
quest and camp-nav builders import them, so the flags cannot disagree with the
hub cards, the quest or the deck buttons. (The two hand-kept route maps paint
camp 9 #6E0B24 and the Trial #46B0AB; the flags follow the hub, #d66d77 and
gold, like everything generated.) A camp or station appears only once its
deck exists, as on the hub. Each part is stamped free or pro by the hub's
access() - lesson-meta.json, what the Worker gates on - never by a list here.

THE RULE (template.js, PASS and GOLD):
  - a flag is planted when the camp's Part 1 (or the station's deck) reaches
    its Results slide with a score of 50% or more;
  - it carries a star when Part 2 does the same (camps with a Part 2 only:
    the flags with no Part 2 have no star slot at all);
  - it goes gold when Part 1 (or the station) scores 75% or more.
  Recorded at the Results slide, kept as the best score per deck, and latched:
  a later lower score, a deck rebuilt with more slides, or a Part 2 that lands
  later never takes a flag back. This is deliberately not the quest's "Camp
  pitched" badge (every part paged to the last slide, score-blind).

THE SAVE: the record lives in the learner's CampSave file under a new
top-level key, 'flags' = { pageId: {best, max, pct, plays, firstAt, lastAt,
pass, gold} }, written with CampSave.get/put. camp-save.js is not changed:
format v1 and MAGIC stay as they are, because twelve RPGs inline a copy of it
and a bump would wipe every save; the old copies keep unknown keys. So the
flags travel with the quest page's save code like the village's rangers do.

THE LOOKOUT (Phase A of docs/LOOKOUT-DESIGN.md; no art, all code):
  - STOREYS: climb flag N raises storey N. Each storey has its own object
    (from the climb map's scene N), a gold effect, a caption in the camp's
    own tense with a FORM line, and the goal the Next chip names.
  - LAMPS: descent station S lights the lamp on storey S-8; the Trial (16)
    hangs the gold lamp on storey 8, because camp 8 has no passive station.
  - TIERS (3, 9, 18): the trim goes oak, iron, brass, then gold at 18 golds.
  - MILESTONES: true counts only (9/18 is "Halfway"; storey 4 is "Four
    storeys up").
  - ADVENTURES: the hub's list, each hung off the camp whose tense it teaches
    (the quest builder's rule), as pennants on the bunting. They never count
    toward the 18.
  - TOKENS: every colour the tower uses that is not CAMP/INK or the sprite
    palette in template.js is sampled here from the plates (PIL box means),
    or is a sample with its HLS lightness set. None is picked by hand.
  - GO PRO: the target of the site nav's Go Pro button, read from the hub's
    nav.html, so a padlocked Next chip goes where the nav goes.

  The captions stay English in every language on purpose: they are the
  English being practised. --check holds each one to the house rules: one
  verb group in CAPS, that verb group matching its tense's shape, and a FORM
  line of the tense name in CAPS + the same verb group.
"""
import colorsys, hashlib, importlib.util, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
HUB = os.path.join(REPO, 'lesson-template', 'build', 'block-camp-hub')
OUT_JS = os.path.join(REPO, 'block-camp', 'camp-flags.js')
OUT_HTML = os.path.join(REPO, 'block-camp', 'flags.html')
TOKENS_JSON = os.path.join(HERE, 'plate-tokens.json')

spec = importlib.util.spec_from_file_location('hub', os.path.join(HUB, 'build.py'))
hub = importlib.util.module_from_spec(spec)
spec.loader.exec_module(hub)

# The Trial has no camp of its own: gold, as on the hub card (build.py
# descent_cards), the quest and the deck buttons (block-camp-nav TRIAL).
TRIAL = ('#e8c04a', '#0b1a12')


def table():
    rows = []
    for n, name, slug, _l1, _l2 in hub.CLIMB:
        p1, p2 = 'blockcamp-%s' % slug, 'blockcamp-%s-2' % slug
        if not hub.present(p1 + '.html'):
            continue
        parts = [p1] + ([p2] if hub.present(p2 + '.html') else [])
        acc = [hub.access(p1 + '.html', 'free' if (n, 1) in hub.FREE_CLIMB else 'pro')]
        if len(parts) > 1:
            acc.append(hub.access(p2 + '.html', 'pro'))
        rows.append({'key': 'climb-%d' % n, 'line': 'climb', 'n': n, 'label': name,
                     'colour': hub.CAMP[n], 'ink': hub.INK[n], 'parts': parts, 'access': acc,
                     'href': p1 + '.html', 'href2': (p2 + '.html') if len(parts) > 1 else None})
    for st, camp, name, slug, _lvl, acc in hub.DESCENT:
        p = 'blockcamp-passive-%s' % slug
        if not hub.present(p + '.html'):
            continue
        colour, ink = (hub.CAMP[camp], hub.INK[camp]) if camp else TRIAL
        rows.append({'key': 'descent-%d' % st, 'line': 'descent', 'n': st, 'label': name,
                     'colour': colour, 'ink': ink, 'parts': [p], 'access': [hub.access(p + '.html', acc)],
                     'href': p + '.html', 'href2': None, 'trial': not camp})
    return rows


# ── THE LOOKOUT ─────────────────────────────────────────────────────────
# docs/LOOKOUT-DESIGN.md section 4. The captions are the design's drafts after
# the house tense check (memories "Stative is not the test" and "Grammar
# tokens in CAPS"); three were tightened so the tense is forced, not merely
# likely:
#   2  "The hoist IS LIFTING the canvas."   + "Look!": now-ness made explicit
#   3  "...the logs this morning."          -> "yesterday": "this morning"
#                                              takes HAVE STACKED while it is
#                                              still morning
#   St 10 "Storey 2's lamp IS BEING LIT."   + "Look!", as storey 2
#   3  "...yesterday."                      -> "a minute ago": the caption shows the
#                                              moment the storey goes up, and "ago"
#                                              still forces the past simple
#   7  "You HAVE BUILT the deck."           + "So far": with no time frame BUILT
#                                              fitted as well. Not "seven storeys
#                                              so far": the Lookout is order-free,
#                                              so a count could be false
#   St 15 "...HAS BEEN LIT."                + "since sunset" (WAS LIT fitted too)
#   St 17 "...HAD BEEN HUNG before dark."   -> "By the time it got dark, ...": a
#                                              second past event, so WAS HUNG no
#                                              longer fits
# `goal` finishes the Next chip's "50% ..." line.
#
# `object` and `effect` are the design's notes for whoever draws the storey.
# The learner reads `desc` and `goldDesc` (the storey sheet on flags.html):
# plain English about what the pixels actually show, with no frame counts or
# timings - --check refuses those (LEARNER_JARGON).
STOREYS = [
    {'n': 1, 'object': 'Cobblestone footings, arched door, cream canvas awning, iron lantern',
     'effect': 'The lantern lights: a warm pool and a 2-frame flicker',
     'desc': 'Stone footings, an arched door and an iron lantern', 'goldDesc': 'the lantern lights up the door',
     'caption': 'The lantern LIGHTS the door every evening.', 'verb': 'LIGHTS',
     'goal': 'lays the footings'},
    {'n': 2, 'object': 'Rope-and-pulley hoist lifting a canvas bundle',
     'effect': 'The pulley wheel turns gold (2-frame turn)',
     'desc': 'A pulley hoist lifting a canvas bundle', 'goldDesc': 'the pulley wheel turns gold and lifts the bundle higher',
     'caption': 'Look! The hoist IS LIFTING the canvas.', 'verb': 'IS LIFTING',
     'goal': 'raises storey 2'},
    {'n': 3, 'object': 'Stacked logs and an empty iron fire basket',
     'effect': 'The basket catches: a 3-frame pixel flame',
     'desc': 'Stacked logs and an empty iron fire basket', 'goldDesc': 'a fire burns in the basket',
     'caption': 'You STACKED the logs a minute ago.', 'verb': 'STACKED',
     'goal': 'raises storey 3'},
    {'n': 4, 'object': 'Small stone hearth with a chimney pipe',
     'effect': 'The hearth mouth glows and 3 smoke puffs rise',
     'desc': 'A small stone hearth with a chimney pipe', 'goldDesc': 'the hearth glows and smoke rises',
     'caption': 'The fire WAS BURNING when you finished the hearth.', 'verb': 'WAS BURNING',
     'goal': 'raises storey 4'},
    {'n': 5, 'object': 'Signpost with two arrows pointing up, a rolled map on a crate',
     'effect': 'The signpost\'s big arrow turns gold',
     'desc': 'Two signposts pointing up, and a rolled map on a crate', 'goldDesc': 'the big arrow turns gold',
     'caption': 'Look at the sign: you ARE GOING TO REACH the top!', 'verb': 'ARE GOING TO REACH',
     'goal': 'raises storey 5'},
    {'n': 6, 'object': 'Brass telescope on a tripod',
     'effect': 'A glint at the lens every 6 s',
     'desc': 'A brass telescope on a tripod', 'goldDesc': 'the telescope turns gold and its lens glints',
     'caption': 'One day you WILL SEE the far side from here.', 'verb': 'WILL SEE',
     'goal': 'raises storey 6'},
    {'n': 7, 'object': 'Wrap-around deck and railing, a small cairn and a pair of boots',
     'effect': 'A gold capstone on the cairn, and the boots glint',
     'desc': 'A deck with a railing, a small cairn of stones and a pair of boots', 'goldDesc': 'a gold stone tops the cairn and the boots shine',
     'caption': 'So far, you HAVE BUILT the deck and its railing.', 'verb': 'HAVE BUILT',
     'goal': 'raises storey 7'},
    {'n': 8, 'object': 'Cabin with glass windows and a hanging lantern',
     'effect': 'The windows glow warm',
     'desc': 'A cabin with glass windows and a lantern inside', 'goldDesc': 'the windows glow warm',
     'caption': 'You HAVE BEEN BUILDING since breakfast.', 'verb': 'HAVE BEEN BUILDING',
     'goal': 'raises storey 8'},
    {'n': 9, 'object': 'Stepped green roof with a stone beacon cradle',
     'effect': 'The cradle stones turn gold',
     'desc': 'A stepped green roof with a stone cradle for the beacon', 'goldDesc': 'the cradle stones turn gold',
     'caption': 'The sun HAD SET by the time the roof went on.', 'verb': 'HAD SET',
     'goal': 'puts the roof on'},
]
# what a learner-facing line may not say: the design's production notes
LEARNER_JARGON = re.compile(r'\d+-frame|\bframes?\b|every \d+ ?s\b|\bsampled\b|\bsub-?pixels?\b|\bpx\b', re.I)

# station -> its lamp's caption. The storey is station - 8 (the Trial, 16,
# lands on storey 8). The Trial teaches every tense, so its caption carries
# its own: `tense` overrides the station's name for the FORM line.
LAMP_CAPTIONS = {
    9:  {'caption': 'The lamps ARE LIT every evening.', 'verb': 'ARE LIT'},
    10: {'caption': 'Look! Storey 2’s lamp IS BEING LIT.', 'verb': 'IS BEING LIT'},
    11: {'caption': 'Storey 3’s lamp WAS LIT at sunset.', 'verb': 'WAS LIT'},
    12: {'caption': 'Storey 4’s lamp WAS BEING LIT when the wind dropped.', 'verb': 'WAS BEING LIT'},
    13: {'caption': 'Look at the lamps: the beacon IS GOING TO BE LIT!', 'verb': 'IS GOING TO BE LIT'},
    14: {'caption': 'The beacon WILL BE SEEN from the valley.', 'verb': 'WILL BE SEEN'},
    15: {'caption': 'Storey 7’s lamp HAS BEEN LIT since sunset.', 'verb': 'HAS BEEN LIT'},
    16: {'caption': 'The Trial HAS BEEN PASSED: the gold lamp is yours.', 'verb': 'HAS BEEN PASSED',
         'tense': 'Present Perfect Passive'},
    17: {'caption': 'By the time it got dark, the roof lamp HAD BEEN HUNG.', 'verb': 'HAD BEEN HUNG'},
}

# The shape a verb group must have in each tense. A caption whose CAPS group
# does not fit its storey's tense fails --check. The slots are strict: an
# -ING form only where the tense has one, BEING / BEEN only where they
# belong, a past form (-ED or an irregular past) for the past simple and the
# participles, and never a past form for the present simple. --self-test
# proves each shape refuses the other tenses' groups.
IRREGULAR = ('BUILT LIT HUNG SET SEEN SAW WENT GONE MADE PUT CUT HIT LET SHUT KEPT LEFT SLEPT FELT MET SENT SPENT '
             'HELD TOLD SOLD FOUND BOUGHT BROUGHT CAUGHT TAUGHT THOUGHT STOOD WON RAN BEGAN BEGUN SANG SUNG CAME '
             'BECAME GAVE GIVEN TOOK TAKEN SHOOK SHAKEN WROTE WRITTEN ROSE RISEN DROVE DRIVEN RODE RIDDEN ATE EATEN '
             'FELL FALLEN FLEW FLOWN GREW GROWN KNEW KNOWN THREW THROWN DREW DRAWN BLEW BLOWN WORE WORN TORE TORN '
             'BROKE BROKEN SPOKE SPOKEN STOLE STOLEN CHOSE CHOSEN FROZE FROZEN WOKE WOKEN GOT FORGOT FORGOTTEN '
             'HID HIDDEN SAT LAY LAIN LED FED READ HEARD PAID SAID LAID MEANT BURNT DONE DID DUG STUCK STRUCK '
             'SWUNG SPUN WOUND SHONE SHOT LOST COST BURST CAST SPREAD HURT').split()
# irregular pasts spelt like their base form: SET is present and past
SAME_AS_BASE = {'SET', 'PUT', 'CUT', 'HIT', 'LET', 'SHUT', 'READ', 'COST', 'BURST', 'CAST', 'SPREAD', 'HURT'}
AUX = r'(?:AM|IS|ARE|WAS|WERE|BE|BEING|BEEN|HAVE|HAS|HAD|WILL|DO|DOES|DID|GOING|TO)'
_IRR = '|'.join(IRREGULAR)
_NOT_BASE = '|'.join(w for w in IRREGULAR if w not in SAME_AS_BASE)
PAST = r'(?:[A-Z]+ED|%s)' % _IRR                         # STACKED, LIT, SET
BASE = r'(?!%s\b)(?!(?:%s)\b)(?![A-Z]+ED\b)[A-Z]+(?<!ING)' % (AUX, _NOT_BASE)   # REACH, SEE; never SAW
PRESENT = BASE                                            # LIGHTS; never STACKED or LIT
ING = r'(?!BEING\b)[A-Z]+ING'
VERB_SHAPE = {
    'Present Simple': PRESENT,
    'Present Continuous': r'(AM|IS|ARE) ' + ING,
    'Past Simple': r'(?!%s\b)' % AUX + PAST,
    'Past Continuous': r'(WAS|WERE) ' + ING,
    'Going To': r'(AM|IS|ARE) GOING TO ' + BASE,
    'Future Simple': r'WILL ' + BASE,
    'Present Perfect': r'(HAVE|HAS) ' + PAST,
    'Present Perfect Continuous': r'(HAVE|HAS) BEEN ' + ING,
    'Past Perfect': r'HAD ' + PAST,
    'Present Simple Passive': r'(AM|IS|ARE) ' + PAST,
    'Present Continuous Passive': r'(AM|IS|ARE) BEING ' + PAST,
    'Past Simple Passive': r'(WAS|WERE) ' + PAST,
    'Past Continuous Passive': r'(WAS|WERE) BEING ' + PAST,
    'Going To Passive': r'(AM|IS|ARE) GOING TO BE ' + PAST,
    'Future Simple Passive': r'WILL BE ' + PAST,
    'Present Perfect Passive': r'(HAVE|HAS) BEEN ' + PAST,
    'Past Perfect Passive': r'HAD BEEN ' + PAST,
}
# a wrong-tense group per tense that its shape must refuse (--self-test): the
# probes the 2026-10-02 language review found passing, and their kin
SHAPE_PROBES = {
    'Present Simple': ['STACKED', 'LIT', 'IS LIGHTING', 'LIGHTING'],
    'Present Continuous': ['IS LIFTED', 'IS BEING', 'WAS LIFTING'],
    'Past Simple': ['LIGHTS', 'WAS', 'LIGHTING', 'HAS'],
    'Past Continuous': ['WAS BURNT', 'WAS BEING', 'IS BURNING'],
    'Going To': ['ARE GOING TO REACHING', 'ARE GOING TO REACHED', 'IS GOING TO BE'],
    'Future Simple': ['WILL BEING', 'WILL SEEING', 'WILL SAW', 'WILL BE'],
    'Present Perfect': ['HAVE BUILDING', 'HAVE BEEN', 'HAVE BUILD'],
    'Present Perfect Continuous': ['HAVE BEEN BUILT', 'HAVE BEEN BEING'],
    'Past Perfect': ['HAD SETTING', 'HAD BEEN', 'HAD SETS'],
    'Present Simple Passive': ['IS LIFTING', 'ARE LIGHTING', 'IS BEING', 'IS LIGHT'],
    'Present Continuous Passive': ['IS BEING LIGHTING', 'IS BEING LIGHT'],
    'Past Simple Passive': ['WAS BURNING', 'WAS BEING', 'WAS BEEN'],
    'Past Continuous Passive': ['WAS BEING LIGHTING', 'WAS BEING BEEN'],
    'Going To Passive': ['IS GOING TO BE LIGHTING', 'IS GOING TO BE BEING'],
    'Future Simple Passive': ['WILL BE SEEING', 'WILL BE BEING'],
    'Present Perfect Passive': ['HAVE BEEN BUILDING', 'HAS BEEN BEING'],
    'Past Perfect Passive': ['HAD BEEN SETTING', 'HAD BEEN BEING'],
}
# words that are not a verb group however they are written
NOT_VERBS = {'I', 'A'}

TIERS = (3, 9, 18)
TIER_NAMES = ('oak', 'iron', 'brass', 'gold')
FLAME = (1, 4, 7)          # lamps lit: embers, small flame, big flame
DUSK_STEP = 0.04           # the dusk layer deepens this much per lamp


def form(tense, verb):
    return '%s · %s' % (tense.upper(), verb)


def storeys():
    names = {n: name for n, name, *_ in hub.CLIMB}
    out = []
    for s in STOREYS:
        tense = names[s['n']]
        f = form(tense, s['verb'])
        out.append(dict(s, tense=tense, form=f, formShort=f.replace('CONTINUOUS', 'CONT.')))
    return out


def lamps():
    out = []
    for st, camp, name, slug, _lvl, _acc in hub.DESCENT:
        c = LAMP_CAPTIONS[st]
        tense = c.get('tense', name)
        f = form(tense, c['verb'])
        out.append({'n': st - 8, 'station': st, 'tense': tense, 'caption': c['caption'], 'verb': c['verb'],
                    'form': f, 'formShort': f.replace('CONTINUOUS', 'CONT.'),
                    'goal': 'lights the gold lamp' if not camp else 'lights lamp %d' % (st - 8)})
    return out


def unescape(s):
    return (s.replace('&rsquo;', '’').replace('&mdash;', '—').replace('&ndash;', '–')
             .replace('&amp;', '&'))


def adventures():
    """The hub's adventures in the hub's (= the Quest's) order. Each hangs off
    the camp whose tense it teaches - its first grammar chip - exactly as
    block-camp-quest/build.py does; one with no camp (conditionals, narrative
    tenses) flies gold, as the Quest's badge does."""
    by_name = {name: n for n, name, *_ in hub.CLIMB}
    by_name['Future Simple: Will'] = by_name['Future Simple']
    out = []
    for href, _img, title, _desc, gram, _lvl, acc, _tag in hub.ADVENTURES:
        if not hub.present(href):
            continue
        camp = by_name.get(gram[0])
        t = unescape(title)
        out.append({'id': re.sub(r'\.html$', '', href.split('/')[-1]), 'href': href,
                    'title': t, 'short': t.split(':')[0], 'camp': camp or 0,
                    'colour': hub.CAMP[camp] if camp else TRIAL[0], 'ink': hub.INK[camp] if camp else TRIAL[1],
                    'access': hub.access(href, acc)})
    return out


def milestones(rows, advs):
    n_star = sum(1 for r in rows if len(r['parts']) > 1)
    return [
        {'id': 'begun', 'test': 'k', 'at': 1, 'toast': 'Your Lookout has begun'},
        {'id': 'four', 'test': 'built', 'at': 4, 'toast': 'Four storeys up'},
        {'id': 'halfway', 'test': 'k', 'at': 9, 'toast': 'Halfway'},
        {'id': 'stands', 'test': 'built', 'at': 9, 'toast': 'THE LOOKOUT STANDS'},
        {'id': 'beacon', 'test': 'k', 'at': 18, 'toast': 'Every lamp is lit · BEACON LIT'},
        {'id': 'iron', 'test': 'golds', 'at': TIERS[0], 'toast': 'Iron trim'},
        {'id': 'brass', 'test': 'golds', 'at': TIERS[1], 'toast': 'Brass trim'},
        {'id': 'golden', 'test': 'golds', 'at': TIERS[2], 'toast': 'GOLDEN LOOKOUT'},
        {'id': 'summitFlag', 'test': 'stars', 'at': n_star, 'toast': 'The Summit Flag'},
        {'id': 'fullSummit', 'test': 'adventures', 'at': len(advs), 'toast': 'A full summit'},
    ]


def go_pro():
    """Where the site nav's Go Pro button points (hub nav.html, the band every
    Block Camp page carries)."""
    nav = open(os.path.join(HUB, 'nav.html'), encoding='utf-8').read()
    m = re.search(r'<a href="([^"]+)" class="tb-cta-gold"', nav)
    if not m:
        raise SystemExit('nav.html has no tb-cta-gold link: the Go Pro target cannot be read')
    return m.group(1)


# ── plate-sampled tokens ────────────────────────────────────────────────
# The mockup's palette.py, moved here. Box means on the two plates; the boxes
# are the mockup's (reviewed in its contact sheet), plus ROOF, which the
# mockup typed in as "sampled from hub-hero's roof" and is now measured: the
# lit right half of the painted lookout's roof on hub-hero.jpg.
FAR = 'BlockCampDescent/watchtower-far-side.jpg'
HERO = 'BlockCamp/hub-hero.jpg'
SAMPLES = {
    'SKY_TOP': (FAR, (400, 0, 1200, 10)),
    'SKY_HOR': (FAR, (400, 160, 1200, 170)),
    'CLOUD':   (FAR, (400, 120, 1200, 130)),
    'GRASS':   (HERO, (360, 820, 420, 850)),
    'PAD':     (HERO, (560, 820, 600, 840)),
    'CANVAS':  (HERO, (300, 720, 340, 740)),
    'ROOF':    (HERO, (1150, 420, 1176, 428)),
}
# a sample with its HLS lightness set (design 8: "dusk = sky top at HLS L 0.12")
DERIVED = {
    'TWI': ('SKY_TOP', 0.30),
    'DUSK': ('SKY_TOP', 0.12),
    'BLUEPRINT': ('SKY_TOP', 0.82),
    'HUD': ('SKY_TOP', 0.10),
    'SHEET': ('SKY_TOP', 0.06),
    'GRASS_DK': ('GRASS', 0.18),
    'ROOF_DK': ('ROOF', 0.28),
}


def _hx(c):
    c = c.lstrip('#')
    return tuple(int(c[i:i + 2], 16) for i in (0, 2, 4))


def _setl(c, L):
    r, g, b = [v / 255 for v in _hx(c)]
    h, _l, s = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(h, L, s)
    return '#%02x%02x%02x' % (round(r * 255), round(g * 255), round(b * 255))


def _sha1(rel):
    return hashlib.sha1(open(os.path.join(REPO, rel), 'rb').read()).hexdigest()


def tokens(write=True):
    """The sampled colours. Read from plate-tokens.json while both plates and
    every box are unchanged, so a build needs no PIL and two machines cannot
    disagree by a JPEG decoder's rounding; re-sampled (and the cache
    rewritten) only when something it depends on moved. With write=False
    (--check) a stale cache is an error, not a rebuild."""
    key = {'plates': {p: _sha1(p) for p in sorted({FAR, HERO})},
           'samples': {k: [v[0], list(v[1])] for k, v in sorted(SAMPLES.items())},
           'derived': {k: [v[0], v[1]] for k, v in sorted(DERIVED.items())}}
    try:
        cache = json.load(open(TOKENS_JSON, encoding='utf-8'))
    except (OSError, ValueError):
        cache = None
    if cache and cache.get('key') == key:
        return cache['tokens'], False
    if not write:
        moved = [p for p in key['plates'] if not cache or cache.get('key', {}).get('plates', {}).get(p) != key['plates'][p]]
        raise ValueError('plate-tokens.json is stale (%s) - run build.py to re-sample'
                         % (', '.join(moved) + ' changed' if moved else 'a sample box changed'))
    from PIL import Image
    ims = {p: Image.open(os.path.join(REPO, p)).convert('RGB') for p in (FAR, HERO)}
    t = {}
    for k, (p, box) in SAMPLES.items():
        t[k] = '#%02x%02x%02x' % ims[p].crop(box).resize((1, 1), Image.BOX).getpixel((0, 0))
    for k, (src, L) in DERIVED.items():
        t[k] = _setl(t[src], L)
    t = dict(sorted(t.items()))
    open(TOKENS_JSON, 'w', encoding='utf-8', newline='\n').write(
        json.dumps({'note': 'GENERATED by build.py: box means on the plates. Delete to re-sample.',
                    'key': key, 'tokens': t}, indent=1, ensure_ascii=False) + '\n')
    return t, True


def ink_dark():
    """The dark ink of the hub's INK table (every camp but 7, and the Trial).
    It is the lamps' iron frame and the gold caps' outline: design 9 measured
    GOLD_DK at only 1.2-1.6:1 on the cloths, so gold never touches a glass."""
    inks = list(hub.INK.values()) + [TRIAL[1]]
    return min(inks, key=_lum)


def lookout(rows, toks):
    advs = adventures()
    return {
        'tiers': list(TIERS), 'tierNames': list(TIER_NAMES), 'flame': list(FLAME), 'duskStep': DUSK_STEP,
        'storeys': storeys(), 'lamps': lamps(), 'milestones': milestones(rows, advs),
        'adventures': advs, 'tokens': toks, 'inkDk': ink_dark(), 'goPro': go_pro(),
    }


# ── checks ──────────────────────────────────────────────────────────────
CAPS_RUN = re.compile(r"\b[A-Z][A-Z’']*[A-Z]\b(?:\s+\b[A-Z][A-Z’']*[A-Z]\b)*")


def check_captions(sts, lps):
    """Every caption: exactly one verb group in CAPS, of its tense's shape,
    and a FORM line that is the tense in CAPS + that same group."""
    bad = []
    for p in [('storey %d' % s['n'], s) for s in sts] + [('lamp, station %d' % l['station'], l) for l in lps]:
        what, d = p
        runs = [r for r in CAPS_RUN.findall(d['caption']) if r not in NOT_VERBS]
        shape = VERB_SHAPE.get(d['tense'])
        if shape is None:
            bad.append('%s: no verb shape for tense %r' % (what, d['tense']))
            continue
        if runs != [d['verb']]:
            bad.append('%s: CAPS groups %r in %r, expected exactly [%r]' % (what, runs, d['caption'], d['verb']))
        if not re.fullmatch(shape, d['verb']):
            bad.append('%s: %r is not a %s verb group (%s)' % (what, d['verb'], d['tense'], shape))
        if d['form'] != '%s · %s' % (d['tense'].upper(), d['verb']):
            bad.append('%s: FORM %r is not "%s · %s"' % (what, d['form'], d['tense'].upper(), d['verb']))
        if not re.search(r'[.!?]$', d['caption']):
            bad.append('%s: caption does not end a sentence: %r' % (what, d['caption']))
        if re.search(r"'", d['caption']):
            bad.append('%s: straight apostrophe in %r (house style is ’)' % (what, d['caption']))
    # what the storey sheet tells the learner: no production notes
    for s in sts:
        for k in ('desc', 'goldDesc'):
            v = s.get(k) or ''
            if not v.strip():
                bad.append('storey %d: no learner-facing %s' % (s['n'], k))
            elif LEARNER_JARGON.search(v):
                bad.append('storey %d: %s %r reads like a production note (%s)' % (s['n'], k, v, LEARNER_JARGON.pattern))
    return bad


def self_test():
    """Prove the caption gate refuses what it should: every SHAPE_PROBES group
    against its tense, broken copies of real captions, and jargon in a sheet
    line. Returns a list of probes that wrongly passed."""
    missed = []
    for tense, probes in SHAPE_PROBES.items():
        for v in probes:
            if re.fullmatch(VERB_SHAPE[tense], v):
                missed.append('%s accepted %r' % (tense, v))
    sts, lps = storeys(), lamps()
    if check_captions(sts, lps):
        missed.append('the real captions do not pass: %s' % check_captions(sts, lps))
    def broken(i, **kw):
        c = [dict(s) for s in sts]
        c[i].update(kw)
        return check_captions(c, lps)
    cases = [
        ('lowercase verb', broken(2, caption='You stacked the logs a minute ago.')),
        ('second CAPS group', broken(2, caption='You STACKED the logs a minute AGO.')),
        ('wrong FORM tense', broken(2, form='PAST CONTINUOUS · STACKED')),
        ('no sentence end', broken(2, caption='You STACKED the logs a minute ago')),
        ('straight apostrophe', broken(2, caption="You STACKED the logs, didn't you?")),
        ('wrong-tense verb', broken(0, caption='The lantern LIT the door every evening.', verb='LIT',
                                    form='PRESENT SIMPLE · LIT')),
        ('jargon in goldDesc', broken(2, goldDesc='a 3-frame pixel flame')),
        ('timing in goldDesc', broken(5, goldDesc='a glint at the lens every 6 s')),
        ('empty desc', broken(4, desc='')),
    ]
    for name, problems in cases:
        if not problems:
            missed.append('a broken copy passed: ' + name)
    return missed


def _lum(c):
    def ch(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b = [ch(v) for v in _hx(c)]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(a, b):
    x, y = _lum(a), _lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


# the sprite palette in template.js that the checks need; read from the
# template so a change there is measured, not copied
def sprite_palette():
    src = open(os.path.join(HERE, 'template.js'), encoding='utf-8').read()
    return dict(re.findall(r"\b([A-Z_]+) = '(#[0-9a-fA-F]{6})'", src))


def trim_tiers():
    """The trim colours, oak to gold, by sprite-palette name, read from
    template.js's P.TIER so the check measures what the tower draws."""
    src = open(os.path.join(HERE, 'template.js'), encoding='utf-8').read()
    m = re.search(r'p\.TIER = \[([^\]]+)\]', src)
    if not m:
        raise ValueError('template.js has no p.TIER = [...] line: the trim check cannot read the tiers')
    return re.findall(r'p\.([A-Z_]+)', m.group(1))


def check_contrast(rows, ink_dk, toks=None):
    """Adjacent code colours that must read apart at phone size (design 9):
    the tag digit on its tag, a star in ink on its cloth, a lamp's ink lid
    and foot on its glass (the Trial's gold glass included), a gold crown on
    that lid - and the trim against the flags.html sky: oak on its own, the
    metal tiers (iron, brass, gold) on the ink rim the stage draws round
    them, and that rim on the sky's top and horizon samples."""
    pal = sprite_palette()
    pairs = []
    for r in rows:
        pairs.append(('ink on %s' % r['key'], r['ink'], r['colour']))
        if r['line'] == 'descent':
            pairs.append(('lamp lid on %s glass' % r['key'], ink_dk, r['colour']))
    pairs.append(('gold crown on lamp lid', pal['GOLD_C'], ink_dk))
    pairs.append(('gold crown highlight on lamp lid', pal['GOLD_HI'], ink_dk))
    if toks:
        tiers = trim_tiers()
        for sky in ('SKY_TOP', 'SKY_HOR'):
            pairs.append(('oak trim (%s) on the sky (%s)' % (tiers[0], sky), pal[tiers[0]], toks[sky]))
            pairs.append(('metal trim rim on the sky (%s)' % sky, ink_dk, toks[sky]))
        for name, t in zip(TIER_NAMES[1:], tiers[1:]):
            pairs.append(('%s trim (%s) on its rim' % (name, t), pal[t], ink_dk))
    bad = ['%s: %s on %s is %.2f:1 (needs 3:1)' % (w, a, b, contrast(a, b)) for w, a, b in pairs if contrast(a, b) < 3]
    return bad, min(contrast(a, b) for _w, a, b in pairs)


# the hub's and the quest's padlock (block-camp-hub/build.py chips())
LOCK = ('<svg viewBox="0 0 10 12" aria-hidden="true"><path d="M2 5V3.5a3 3 0 0 1 6 0V5h1v7H1V5h1zm1.4 0h3.2V3.5'
        'a1.6 1.6 0 0 0-3.2 0V5z"/></svg><span class="sr"> (Pro)</span>')


def tiles(rows, line):
    """The static markup of one row of "the parts list" (the eighteen flags
    under Your Lookout). The sprite slot is filled at runtime (camp-flags.js
    draws it); the text and the links are here so the page reads without
    script. A climb flag is the storey it raises, a descent flag the lamp it
    hangs (station S on storey S-8); a Pro part's link carries the padlock,
    from the catalogue (table() stamps it through the hub's access())."""
    out = []
    for r in rows:
        if r['line'] != line:
            continue
        what = 'Storey %d' % r['n'] if line == 'climb' else ('Lamp %d' % (r['n'] - 8))
        lock = [LOCK if a == 'pro' else '' for a in r['access']]
        links = '<a class="pt" href="../%s">%s%s</a>' % (r['href'], 'Part 1' if r['href2'] else 'Open', lock[0])
        if r['href2']:
            links += '<a class="pt" href="../%s">Part 2%s</a>' % (r['href2'], lock[1])
        out.append(
            '<li class="fl locked" data-key="%s" style="--c:%s;--ci:%s">'
            '<span class="art" aria-hidden="true"></span>'
            '<span class="no mono">%s</span>'
            '<span class="nm">%s</span>'
            '<span class="st">Not planted yet</span>'
            '<span class="bs"></span>'
            '<span class="pts">%s</span></li>'
            % (r['key'], r['colour'], r['ink'], what.upper(), r['label'], links))
    return '\n      '.join(out)


def render(write_tokens=True):
    rd = lambda d, n: open(os.path.join(d, n), encoding='utf-8').read()
    rows = table()
    toks, _ = tokens(write_tokens)
    lk = lookout(rows, toks)
    data = json.dumps(rows, ensure_ascii=False, separators=(',', ':'))
    lkdata = json.dumps(lk, ensure_ascii=False, separators=(',', ':'))
    js = rd(HERE, 'template.js').replace('{{TABLE}}', data).replace('{{LOOKOUT}}', lkdata)

    nav = rd(HUB, 'nav.html')
    nav = re.sub(r'href="(?!https?:|mailto:|#|\.\./)([^"]+)"', r'href="../\1"', nav)
    nav = re.sub(r'src="(?!https?:|data:|\.\./)([^"]+)"', r'src="../\1"', nav)
    nav = nav.replace('href="../block-camp.html" aria-current="page"', 'href="../block-camp.html"')
    n_climb = sum(r['line'] == 'climb' for r in rows)
    n_desc = sum(r['line'] == 'descent' for r in rows)
    n_star = sum(1 for r in rows if len(r['parts']) > 1)
    html = (rd(HERE, 'template.html')
            .replace('{{MONOCRAFT}}', rd(HUB, 'monocraft.css'))
            .replace('{{NAV}}', nav)
            .replace('{{CLIMB}}', tiles(rows, 'climb'))
            .replace('{{DESCENT}}', tiles(rows, 'descent'))
            .replace('{{N_CLIMB}}', str(n_climb))
            .replace('{{N_DESCENT}}', str(n_desc))
            .replace('{{N_STAR}}', str(n_star))
            .replace('{{N_ALL}}', str(len(rows)))
            .replace('{{LOOKOUT}}', lkdata))
    return js, html, rows, lk


def main():
    check = '--check' in sys.argv
    if '--self-test' in sys.argv:
        missed = self_test()
        if missed:
            print('\n'.join('FAIL: ' + m for m in missed))
            sys.exit(1)
        print('OK: the caption gate refuses all %d wrong-tense probes and every broken copy'
              % sum(len(v) for v in SHAPE_PROBES.values()))
        return
    try:
        js, html, rows, lk = render(write_tokens=not check)
    except ValueError as e:
        print('FAIL: %s' % e)
        sys.exit(1)
    leftover = sorted(set(re.findall(r'\{\{[A-Z_]+\}\}', js + html)))
    problems = ['unfilled placeholder %s' % p for p in leftover]
    problems += check_captions(lk['storeys'], lk['lamps'])
    bad, low = check_contrast(rows, lk['inkDk'], lk['tokens'])
    problems += bad
    pairs = ((OUT_JS, js), (OUT_HTML, html))
    if check:
        stale = []
        for path, text in pairs:
            try:
                cur = open(path, encoding='utf-8', newline='').read()
            except OSError:
                cur = None
            if cur != text:
                stale.append(os.path.relpath(path, REPO))
        if stale:
            problems.insert(0, 'STALE: ' + ', '.join(stale) + ' - run lesson-template/build/block-camp-flags/build.py')
        if problems:
            print('\n'.join('FAIL: ' + p for p in problems))
            sys.exit(1)
        print('OK: camp-flags.js and flags.html match the hub tables (%d flags); %d captions pass; '
              'contrast pairs >= %.2f:1; plate tokens current'
              % (len(rows), len(lk['storeys']) + len(lk['lamps']), low))
        return
    if problems:
        print('\n'.join('FAIL: ' + p for p in problems))
        sys.exit(1)
    for path, text in pairs:
        open(path, 'w', encoding='utf-8', newline='\n').write(text)
    print('wrote block-camp/camp-flags.js and block-camp/flags.html - %d climb, %d descent flags; '
          'lookout: %d storeys, %d lamps, %d adventures'
          % (sum(r['line'] == 'climb' for r in rows), sum(r['line'] == 'descent' for r in rows),
             len(lk['storeys']), len(lk['lamps']), len(lk['adventures'])))


if __name__ == '__main__':
    main()
