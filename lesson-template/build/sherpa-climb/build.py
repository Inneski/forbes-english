#!/usr/bin/env python3
"""The Climb and The Descent: Sherpa Tensing's two tense games, built into
sherpa-tensing-the-climb.html (the active tenses, up the route map's ascent) and
sherpa-tensing-the-descent.html (the passives, down its descent, in a night-and-storm look).

    py lesson-template/build/sherpa-climb/build.py            # build The Climb (and i18n/strings.json)
    py lesson-template/build/sherpa-climb/build.py --game descent   # build The Descent (and i18n-descent/strings.json)
    py lesson-template/build/sherpa-climb/build.py --game all --check   # prove both pages are fresh builds
    py lesson-template/build/sherpa-climb/build.py --check    # exit 1 if the page on disk is not a fresh build
    py lesson-template/build/sherpa-climb/build.py --strict   # also fail on any language not fully translated
    py lesson-template/build/sherpa-climb/build.py --dump     # print the validated content as JSON (for the test)
    py lesson-template/build/sherpa-climb/build.py --content <file.py>   # build from another content file
                                                              # (a draft, or a test copy with a SUMMIT)
    py lesson-template/build/sherpa-climb/build.py --i18n <dir>          # build with another translations folder
    py lesson-template/build/sherpa-climb/build.py --out <file.html>     # write (or --check) another file: a test
                                                              # variant, which test_climb.js --page serves

Innes, 2026-10-02: "an interactive game for sherpa tensing to practice the
tenses and scale the mountain, it will have a continuity of characters and
narrative but not very much narrative, mainly question to question".

WHAT COMES FROM WHERE
    content.py                    every English word the learner reads (camps, items, cast)
    sherpa-tensing-route-map.html the camp colours, inks, levels, tense names and camp pages
                                  (its colour key rows), the ascent mountain (its sprite and its
                                  13 markers and route segments), its :root tokens, and the
                                  language names in its picker. Read here with regexes, never
                                  copied: the map has been recoloured several times.
    template.html/.css/.js        the page; this file fills its {{SLOTS}}
    i18n/<lang>.json              flat {"English": "translation"} per language; empty = not
                                  offered. A language is offered only when complete
                                  (HOUSE-STYLE section 8: complete or empty, never partial)
    tools/sherpa_*.py             the family look (Faktum, contours, sheen, clouds, arrival),
                                  applied here with the tools' own functions, so each tool's
                                  --check passes on the page as built

The page is written only when it changes, and the build is deterministic: the
same inputs give the same bytes. An SEO block that tools/seo.py has written into
the page on disk is carried over, so seo.py and --check do not fight.

TWO GAMES, ONE ENGINE (GAMES below; --game picks one, default climb)
    The Descent is the same page, the same template and the same rules, with:
    content_descent.py            its stops IN PLAY ORDER (12, 10, 7, 6, 5, 4, 3, 2, 1; a stop is its
                                  twin camp number), the finale (SUMMIT, "home to base camp") and
                                  CHROME, which overrides the climb's English interface strings
    the route map's descent       its nine desc rows (passive names, levels, lesson pages), its
                                  13 diamond markers (4 of them "no camp") and desc-seg-2..13,
                                  and #epic-night-v2
    i18n-descent/<lang>.json      merged OVER i18n/<lang>.json: a string whose English the climb
                                  already has inherits its translation
    descent.css                   appended after template.css: night around the paper card, the
                                  diamonds, the storm layer (one --storm-k knob)
    template.js                   /*@game:climb*/A/*@game:descent*/B/*@game:end*/ fences, resolved
                                  here; the climb's A is its original text, byte for byte
    Altitudes come from content.py by twin camp, so the two games cannot drift. A scene
    SherpaDescent/camp-NN.jpg that does not exist yet falls back to SherpaClimb/camp-NN.jpg.
"""
import html as _html
import importlib.util
import io
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))

# ── the two games. Everything that differs between them is here or in a @game fence ──
GAMES = {
    'climb': dict(
        content='content.py', out='sherpa-tensing-the-climb.html', i18n='i18n', inherit=None,
        face='ascent', sprite='epic-day-v2', shape='circle', mini_vb='150 50 500 540', dir=+1,
        scenes='SherpaClimb', scene_fallback=None, final_scene='summit', final_fallback=None,
        hero=['SherpaClimb/tensing-hero', 'SherpaClimb/base-camp', 'SherpaClimb/camp-02'],
        top=['SherpaClimb/summit-top.jpg', 'Sherpa Tensing/sherpa-day.jpg'],
        save='sherpa.climb.v1', id='c', final_id='s', css=None, page_title='Sherpa Tensing — The Climb',
        final_note='the summit push', end_note='the end, at the summit'),
    'descent': dict(
        content='content_descent.py', out='sherpa-tensing-the-descent.html', i18n='i18n-descent', inherit='i18n',
        face='descent', sprite='epic-night-v2', shape='diamond', mini_vb='150 70 500 540', dir=-1,
        scenes='SherpaDescent', scene_fallback='SherpaClimb', final_scene='finale', final_fallback='SherpaClimb/camp-01',
        hero=['SherpaDescent/summit-night', 'SherpaClimb/summit-top'],
        top=['SherpaDescent/base-camp.jpg', 'SherpaClimb/base-camp.jpg'],
        save='sherpa.descent.v1', id='d', final_id='r', css='descent.css', page_title='Sherpa Tensing — The Descent',
        final_note='the finale, home to base camp', end_note='the end, at base camp'),
}
G = GAMES['climb']
OUT_NAME = G['out']
OUT = os.path.join(ROOT, OUT_NAME)
MAP = os.path.join(ROOT, 'sherpa-tensing-route-map.html')
CAMP_ONE = os.path.join(ROOT, 'sherpa-tensing-camp-one-present-continuous.html')
I18N_DIR = os.path.join(HERE, G['i18n'])
INHERIT_DIR = None
STRINGS = os.path.join(I18N_DIR, 'strings.json')
LANGS = ['de', 'es', 'fr', 'it', 'pt', 'ru', 'ar', 'zh', 'ja']
RTL = ['ar']

sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'lesson-template'))
import sherpa_type        # noqa: E402
import sherpa_topo        # noqa: E402
import sherpa_sheen       # noqa: E402
import sherpa_sky         # noqa: E402
import sherpa_arrive      # noqa: E402
import sherpa_links       # noqa: E402
from soften import to_lch, from_lch, contrast   # noqa: E402

# a grammar token: a word of two or more capitals (IS, VERB-ING, DON'T, -ING)
CAPS = re.compile(r"\b[A-Z][A-Z]+(?:['’-][A-Z]+)*\b")
PLACE = re.compile(r'\{\w+\}')
GAP = re.compile(r'_{3,}')
CUE = re.compile(r'\s*\(([^()]*)\)\s*$')
SPOT = re.compile(r'\[([^\[\]]+)\]')
SINGLE_QUOTED = re.compile(r"(?<![\w])'[^'\s][^']*'(?![\w])|‘[^’]+’")
GREY = '#C9C6C2'          # the route map's colour for a marker that is not open (sherpaPaintDots)
GOLD = '#D2A53B'          # the gold flag (a medal colour, like --good/--bad: not a tense colour)

# ── the chrome, in English. key -> (English, note for the translator) ─────────────
EN = {
    'upLink':      ('Route map', 'pinned link back to the course\'s route map'),
    'tagline':     ('a guide to English tenses', 'the line beside the "Sherpa Tensing" wordmark (as on the route map)'),
    'langLabel':   ('Language', 'aria-label of the language menu'),
    'kicker':      ('Tense game', 'small label above the title'),
    'title':       ('The Climb', 'the game\'s name, the page title'),
    'lead':        ('Climb the mountain with Tensing and the team. Each camp is one tense, and every right answer takes you higher.',
                    'the line under the title. Tensing is a name'),
    'startOne':    ('Start at camp one', 'main button when nothing has been played yet'),
    'continue':    ('Continue: camp {n}', 'main button once there is progress; {n} is a camp number'),
    'continueTop': ('Continue: the summit push', 'main button when the next stop is the summit push'),
    'chooseBtn':   ('Choose a camp', 'second button: scrolls down to the list of camps'),
    'teamH':       ('The team', 'section heading over the characters'),
    'briefWho':    ('Tensing, the guide', 'label over the guide\'s welcome lines'),
    'howItWorks':  ('How it works', 'phones: opens the rest of the guide\'s welcome lines'),
    'momo':        ('And Momo, the yak at base camp.', 'footnote under the team. Momo is a name'),
    'chooseH':     ('Choose a camp', 'section heading over the mountain and the list of camps'),
    'chooseHow':   ('The way up has no locks: start at whichever camp you need.', 'note under that heading (same words as the route map)'),
    'mapAria':     ('The mountain, with a marker for each camp on the way up. Every camp is also listed here.',
                    'screen-reader description of the mountain picture'),
    'summitRow':   ('Summit push · all thirteen tenses', 'the last row of the camp list: one line for every tense'),
    'srBest':      ('Best first try: {k} of {m}', 'screen-reader text after a camp\'s best score, e.g. 7/8'),
    'flagGold':    ('Gold flag', 'tooltip and screen-reader text of the gold flag icon'),
    'flagPlain':   ('Flag', 'tooltip and screen-reader text of the plain flag icon'),
    'camps':       ('Camps', 'button back to the list of camps (top bar, end screens)'),
    'backAria':    ('Back to the camps', 'aria-label of the back button in the top bar'),
    'campN':       ('Camp {n}', 'the camp chip in the top bar, before the tense name'),
    'summitPush':  ('Summit push', 'the chip and heading of the last stage, every tense at once'),
    'altitude':    ('Altitude', 'screen-reader label before the height in metres'),
    'progress':    ('Progress: {k} of {m}', 'screen-reader label of the progress dots'),
    'soundOn':     ('Sound on', 'sound effects button, when on'),
    'soundOff':    ('Sound off', 'sound effects button, when off'),
    'nightMode':   ('Night mode', 'button that turns the page dark (pressed) or back to day'),
    'chooseFree':  ('The first two camps are free; the camps with a padlock are for Pro members.', 'replaces the note under "Choose a camp" for a visitor who is not a Pro member'),
    'proOnly':     ('Pro members only', 'tooltip and screen-reader text of the padlock on a locked camp'),
    'proHead':     ('The first two camps are free', 'heading of the box that opens on a locked camp'),
    'proNote':     ('The other camps are for Pro members. Already a member? Sign in.', 'text of that box'),
    'proPlans':    ('See plans', 'button in that box: the prices page'),
    'proSignIn':   ('Sign in', 'button in that box: the account page'),
    'campAlt':     ('Camp {n} · {alt} m', 'small line over the tense name on arrival; {alt} is a height in metres'),
    'summitAlt':   ('Summit push · {alt} m', 'the same line for the summit push'),
    'start':       ('Start', 'button on the arrival card'),
    'readFirst':   ('Read camp {n} first', 'link to the camp\'s lesson page, on the arrival card'),
    'askChoose':   ('Choose the words for the gap.', 'instruction over a multiple-choice line'),
    'askChoose2':  ('Choose the words for the gaps.', 'the same, when the line has two gaps'),
    'askType':     ('Type the words for the gap.', 'instruction over a typed line'),
    'askSpot':     ('Which tense is the marked form?', 'instruction over a "which tense" line'),
    'gap':         ('gap', 'screen-reader word for the empty space in a sentence'),
    'typeAria':    ('Your answer', 'aria-label of the text box'),
    'typeHint':    ('Type here', 'placeholder in the text box'),
    'check':       ('Check', 'button that checks a typed answer'),
    'again':       ('Again', 'tag on a line that has come back after a mistake'),
    'right':       ('Right. Up you go.', 'after a right answer'),
    'wrong':       ('Not quite. The rope holds.', 'after a wrong answer: nobody falls'),
    'wrongMore':   ('This line comes back before you leave the camp.', 'after a wrong answer'),
    'next':        ('Next', 'button to the next line'),
    'translation': ('Translation', 'small toggle on a card too full for the translations beneath the English: it shows '
                                   'the translation in place of the English, and pressed again, the English'),
    'keys':        ('Keys: 1–3 choose · Enter next · S sound · Esc camps', 'keyboard help under the card (computers only)'),
    'keysType':    ('Keys: Enter checks, then Enter next · Esc camps', 'the same, under a line you type into'),
    'keysMove':    ('Keys: Enter goes on · S sound · Esc camps', 'the same, on the arrival and end cards'),
    'reached':     ('Camp {n} reached', 'heading when a camp is finished'),
    'firstTry':    ('First try: {k} of {m}', 'score when a camp is finished: right the first time'),
    'goldYes':     ('A gold flag: 75% or more right first time.', 'under the score, when it is 75% or more'),
    'goldNo':      ('A flag. Gold is 75% right first time.', 'under the score, when it is under 75%'),
    'onTo':        ('On to camp {n}', 'button to the next camp'),
    'onTop':       ('On to the summit', 'button after the last camp'),
    'summitH':     ('The summit', 'heading of the end screen'),
    'seeClimb':    ('See your climb', 'end screen, first step (the last lines of the story): button to the second step, '
                                      'the scores and the lines to look at again'),
    'yourClimb':   ('Your climb', 'end screen, second step: heading over the scores'),
    'goldCount':   ('Gold flags: {x} of {m}', 'end screen: camps with a gold flag'),
    'overall':     ('First try overall: {p}%', 'end screen: right first time, across the camps played'),
    'review':      ('Worth another look', 'end screen: the lines missed first time'),
    'reviewNone':  ('Nothing to look at again: every line right first time.', 'end screen, when nothing was missed'),
    'rvChip':      ('Camp {n} · {k}', 'end screen: a camp, and how many of its lines to look at again'),
    'rvOpen':      ('Read them again', 'end screen button: opens the lines missed first time, in full'),
    'close':       ('Close', 'button that closes that list'),
    'climbAgain':  ('Climb again', 'end screen button: start again from camp one'),
    'wayDown':     ('The way down is in the passive', 'end screen link to the passive half of the route map'),
}

def chrome(c):
    """The interface English for this game: EN, with the content module's CHROME over it
    (The Descent's "Right. Down you go."). The keys stay EN's, in EN's order."""
    over = getattr(c, 'CHROME', None) or {}
    bad = sorted(k for k in over if k not in EN)
    if bad:
        raise SystemExit('CHROME keys not in EN (an override needs a string to override): %s' % ', '.join(bad))
    for k, v in over.items():
        if not (isinstance(v, tuple) and len(v) == 2 and all(isinstance(x, str) and x for x in v)):
            raise SystemExit('CHROME %s: (English, note for the translator), got %r' % (k, v))
        if sorted(PLACE.findall(v[0])) != sorted(PLACE.findall(EN[k][0])) and k != 'readFirst':
            # readFirst may drop {n}: a stop's own lesson page is not named by its camp number
            raise SystemExit('CHROME %s: placeholders %s, the page fills %s' % (k, PLACE.findall(v[0]), PLACE.findall(EN[k][0])))
    return {k: over.get(k, v) for k, v in EN.items()}


SLUG = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8,
        'nine': 9, 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13}


def read(p):
    return io.open(p, encoding='utf-8').read()


def esc(s):
    return _html.escape(s, quote=False)


def attr(s):
    return _html.escape(s, quote=True)


def bold(s):
    """English with **bold** marks, escaped, as HTML."""
    return re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', esc(s))


# ── content ─────────────────────────────────────────────────────────────────────
CONTENT = os.path.join(HERE, G['content'])


def load_content(path=None):
    spec = importlib.util.spec_from_file_location('climb_content', path or CONTENT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return prepare(mod)


def prepare(c):
    """A stop with no 'alt' takes its twin camp's from the climb's content.py: The Descent
    sleeps at the same camps on the way down, so the heights are written once. (The
    climb's camps all carry their own, so for it this does nothing.)"""
    need = [s for s in (getattr(c, 'CAMPS', None) or []) if isinstance(s, dict) and 'alt' not in s]
    if need:
        spec = importlib.util.spec_from_file_location('climb_alts', os.path.join(HERE, 'content.py'))
        climb = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(climb)
        alts = {camp['n']: camp['alt'] for camp in climb.CAMPS}
        for s in need:
            if s.get('n') in alts:
                s['alt'] = alts[s['n']]
    return c


def gaps(text):
    return len(GAP.findall(text))


def parts(answer):
    return [p.strip() for p in answer.split('...')] if '...' in answer else [answer]


def check_key(iid, opts, key):
    """rpg.py _check_answer_key, per item: the key may not be the longest option by
    more than 10% and 4 characters, nor the shortest by 1.5x and 10 characters."""
    bad = []
    kl = len(key)
    others = [len(o) for o in opts if o != key]
    hi, lo = max(others), min(others)
    if kl > hi * 1.10 and kl - hi >= 4:
        bad.append('%s: the key is the longest option, %d chars against %d (%.2fx): %r' % (iid, kl, hi, kl / hi, key))
    if lo > kl * 1.50 and lo - kl >= 10:
        bad.append('%s: the key is the shortest option, %d chars against %d (%.2fx): %r' % (iid, kl, lo, lo / kl, key))
    return bad


def validate(c, route):
    """Refuse to build on any content defect, naming the item."""
    bad = []
    cast, via = c.CAST, c.VIA
    seen = set()
    route_ns = set(route['tenses'])

    def line(where, ln):
        if ln.get('who') not in cast:
            bad.append('%s: who %r is not in CAST' % (where, ln.get('who')))
        if ln.get('via') is not None and ln['via'] not in via:
            bad.append('%s: via %r is not in VIA' % (where, ln['via']))
        if not ln.get('en'):
            bad.append('%s: no English' % where)
        elif ln['en'].count('**') % 2:
            bad.append('%s: unbalanced ** in %r' % (where, ln['en']))

    def item(it, home):
        iid = it.get('id', '?')
        if iid in seen:
            bad.append('%s: duplicate id' % iid)
        seen.add(iid)
        want = ('%s%s-' % (G['id'], home)) if home != 'summit' else G['final_id'] + '-'
        if not str(iid).startswith(want):
            bad.append('%s: id should start %r' % (iid, want))
        if it.get('who') not in cast:
            bad.append('%s: who %r is not in CAST' % (iid, it.get('who')))
        if it.get('via') is not None and it['via'] not in via:
            bad.append('%s: via %r is not in VIA' % (iid, it['via']))
        text, kind = it.get('text', ''), it.get('kind')
        for k in ('text', 'fb'):
            if it.get(k, '').count('**') % 2:
                bad.append('%s: unbalanced ** in %s' % (iid, k))
        fb = it.get('fb', '')
        if not CAPS.search(fb):
            bad.append('%s: fb has no CAPS grammar token: %r' % (iid, fb))
        if SINGLE_QUOTED.search(fb):
            bad.append('%s: fb cites a form in single quotes (use "double"): %r' % (iid, fb))
        if home == 'summit':
            if it.get('camp') not in route_ns:
                bad.append('%s: summit item needs camp: <%s> (the tense it tests), got %r'
                           % (iid, ', '.join(map(str, route['order'])), it.get('camp')))
        if kind == 'choose':
            opts = it.get('options') or []
            ans = it.get('answer')
            if len(opts) != 3 or len(set(opts)) != 3 or not all(isinstance(o, str) and o for o in opts):
                bad.append('%s: choose needs exactly 3 distinct options, got %r' % (iid, opts))
            elif opts[0] != ans:
                bad.append('%s: options[0] must be the answer (%r), got %r' % (iid, ans, opts[0]))
            else:
                bad.extend(check_key(iid, opts, ans))
                for o in opts:
                    if o.count('...') > 1:
                        bad.append('%s: option %r has more than one "...": a line has at most two gaps' % (iid, o))
                    elif len(parts(o)) != len(parts(ans)):
                        bad.append('%s: option %r and the answer disagree on "..." (two gaps)' % (iid, o))
                    elif not all(parts(o)):
                        bad.append('%s: option %r leaves a gap empty' % (iid, o))
            want_gaps = len(parts(ans)) if isinstance(ans, str) and ans else 1
            if gaps(text) != want_gaps:
                bad.append('%s: %d gap(s) in the text, the answer fills %d' % (iid, gaps(text), want_gaps))
            if SPOT.search(text):
                bad.append('%s: a choose line has a [bracketed] form' % iid)
        elif kind == 'type':
            acc = it.get('accept') or []
            if not acc:
                bad.append('%s: type needs a non-empty accept list' % iid)
            if it.get('answer') not in acc:
                bad.append('%s: the answer %r is not in accept' % (iid, it.get('answer')))
            if gaps(text) != 1:
                bad.append('%s: a typed line has exactly one gap, found %d' % (iid, gaps(text)))
            if '...' in (it.get('answer') or ''):
                bad.append('%s: a typed answer fills one gap; no "..."' % iid)
            if SPOT.search(text):
                bad.append('%s: a typed line has a [bracketed] form' % iid)
        elif kind == 'spot':
            opts = it.get('options') or []
            if len(SPOT.findall(text)) != 1 or text.count('[') != 1 or text.count(']') != 1:
                bad.append('%s: spot needs exactly one [bracketed] form' % iid)
            if gaps(text):
                bad.append('%s: spot has no gap' % iid)
            if len(opts) != 3 or len(set(opts)) != 3 or not all(isinstance(o, int) for o in opts):
                bad.append('%s: spot needs 3 distinct camp numbers, got %r' % (iid, opts))
            elif opts[0] != it.get('answer'):
                bad.append('%s: options[0] must be the answer (%r), got %r' % (iid, it.get('answer'), opts[0]))
            for o in opts:
                if isinstance(o, int) and o not in route_ns:
                    bad.append('%s: camp %r is not on the route map' % (iid, o))
            # a camp's spot line may mark another camp's tense: a contrast the learner has to
            # see, where a line that always marks the camp's own tense would be answered by
            # the camp chip on the card
        else:
            bad.append('%s: kind %r is not choose / type / spot' % (iid, kind))

    def stage(s, where, home):
        for i, ln in enumerate(s.get('arrive') or []):
            line('%s arrive[%d]' % (where, i), ln)
        if s.get('done'):
            line('%s done' % where, s['done'])
        tip = s.get('tip') or ''
        if not tip:
            bad.append('%s: no tip' % where)
        elif not CAPS.search(tip):
            bad.append('%s: the tip has no CAPS form: %r' % (where, tip))
        elif SINGLE_QUOTED.search(tip):
            bad.append('%s: the tip cites a form in single quotes: %r' % (where, tip))
        if tip.count('**') % 2:
            bad.append('%s: unbalanced ** in the tip' % where)
        if s.get('side') not in (None, 'left', 'right'):
            bad.append("%s: side is 'left' or 'right' (where the card goes on a computer), got %r" % (where, s['side']))
        if not s.get('items'):
            bad.append('%s: no items' % where)
        for it in s.get('items') or []:
            item(it, home)

    for i, ln in enumerate(getattr(c, 'INTRO', None) or []):
        line('INTRO[%d]' % i, ln)
    last = None
    up = G['dir'] > 0       # the climb goes up, the descent down: numbers and heights move together
    for camp in c.CAMPS:
        n = camp.get('n')
        if n not in route_ns:
            bad.append('camp %r is not on the route map' % n)
            continue
        if last is not None and ((n <= last[0] or camp.get('alt', 0) <= last[1]) if up
                                 else (n >= last[0] or camp.get('alt', 0) >= last[1])):
            bad.append('camp %d: camps go %s in order, numbers and altitudes %s'
                       % (n, 'up' if up else 'down', 'rising' if up else 'falling'))
        last = (n, camp.get('alt', 0))
        if camp.get('storm') is not None and camp['storm'] not in (0, 1, 2, 3):
            bad.append('camp %d: storm is 0-3, got %r' % (n, camp['storm']))
        if not isinstance(camp.get('alt'), int):
            bad.append('camp %d: alt must be whole metres' % n)
        stage(camp, 'camp %d' % n, n)
    if c.SUMMIT is not None:
        s = c.SUMMIT
        if s.get('n') != 'summit':
            bad.append("SUMMIT: n must be 'summit'")
        if not isinstance(s.get('alt'), int) or not isinstance(s.get('top'), int) or (s['top'] <= s['alt'] if up else s['top'] >= s['alt']):
            bad.append('SUMMIT: alt and top are whole metres, top %s alt' % ('above' if up else 'below'))
        if last and isinstance(s.get('alt'), int) and (s['alt'] <= last[1] if up else s['alt'] >= last[1]):
            bad.append('SUMMIT: alt must be %s the last camp' % ('above' if up else 'below'))
        if s.get('storm') is not None and s['storm'] not in (0, 1, 2, 3):
            bad.append('SUMMIT: storm is 0-3, got %r' % s['storm'])
        stage(s, 'SUMMIT', 'summit')
    for i, ln in enumerate(getattr(c, 'OUTRO', None) or []):
        line('OUTRO[%d]' % i, ln)
    for k, v in cast.items():
        if not v.get('name') or not v.get('role'):
            bad.append('CAST %s: name and role' % k)
    if bad:
        raise SystemExit('%s refused (%d):\n  %s' % (os.path.basename(CONTENT), len(bad), '\n  '.join(bad)))


# ── the route map ───────────────────────────────────────────────────────────────
def read_route():
    src = read(MAP)
    # its own tokens: every custom property of every :root in its own <style>, before the
    # generated blocks (colours, and --radius, --lift: the look is more than its hexes)
    own = src.split('<!-- SHERPA-TYPE:start -->')[0]
    tok = {}
    for body in re.findall(r':root\s*\{([^}]*)\}', own):
        for k, v in re.findall(r'(--[a-z0-9-]+)\s*:\s*([^;]+?)\s*;', body):
            v = v.strip()
            tok.setdefault(k, v.upper() if re.fullmatch(r'#[0-9A-Fa-f]{6}', v) else v)
    for k, v in re.findall(r'(--(?:good|good-bg|bad|bad-bg))\s*:\s*(#[0-9A-Fa-f]{6})', read(CAMP_ONE)):
        tok.setdefault(k, v.upper())
    need = ['--ink', '--ink-soft', '--paper', '--card', '--tensing', '--accent', '--accent-dark', '--accent-light',
            '--accent-lighter', '--accent-text', '--paper-deep', '--good', '--good-bg', '--bad', '--bad-bg', '--radius']
    miss = [k for k in need if k not in tok]
    if miss:
        raise SystemExit('route map: no %s token' % ', '.join(miss))
    for k in need:
        if k != '--radius' and not re.fullmatch(r'#[0-9A-F]{6}', tok[k]):
            raise SystemExit('route map: %s is %r, not a hex colour' % (k, tok[k]))

    # the colour key: one row per camp
    tenses = {}
    for href, bg, ink, num, name, inner in re.findall(
            r'<a class="camp-row" href="(sherpa-tensing-camp-[a-z-]+\.html)" style="background:(#[0-9A-Fa-f]{6});'
            r'color:(#[0-9A-Fa-f]{6});"><span class="camp-num">(\d+)</span><span class="camp-name">([^<]+)</span>(.*?)</a>',
            src, re.S):
        lvl = re.search(r'<span class="lvl"[^>]*>([^<]+)</span>', inner)
        tenses[int(num)] = {'href': href, 'fill': bg.upper(), 'ink': ink.upper(), 'name': _html.unescape(name),
                            'level': lvl.group(1) if lvl else ''}
    if sorted(tenses) != list(range(1, 14)):
        raise SystemExit('route map: read camps %s off the colour key, not 1-13' % sorted(tenses))

    # the ascent: its markers and route segments
    asc = src.split('class="descent-map"')[0]
    dots = {}
    for tag, href, cx, cy, glyph, lx, ly, anchor, label in re.findall(
            r'(<g class="camp-dot live" data-color="#[0-9A-Fa-f]{6}" data-href="(sherpa-tensing-camp-[a-z-]+\.html)"[^>]*>)\s*'
            r'<circle class="dot-fill" cx="(\d+)" cy="(\d+)"[^>]*/>\s*(<g transform=.*?)\s*'
            r'<text class="dot-label" x="(\d+)" y="(\d+)" text-anchor="(start|end)"[^>]*>([^<]+)</text>\s*</g>', asc, re.S):
        n = SLUG[re.match(r'sherpa-tensing-camp-([a-z]+)-', href).group(1)]
        colour = re.search(r'data-color="(#[0-9A-Fa-f]{6})"', tag).group(1).upper()
        if colour != tenses[n]['fill']:
            raise SystemExit('route map: camp %d marker %s, key row %s' % (n, colour, tenses[n]['fill']))
        if href != tenses[n]['href']:
            raise SystemExit('route map: camp %d marker links %s, key row %s' % (n, href, tenses[n]['href']))
        dots[n] = {'x': int(cx), 'y': int(cy), 'glyph': glyph.strip(), 'lx': int(lx), 'ly': int(ly), 'anchor': anchor}
    if sorted(dots) != list(range(1, 14)):
        raise SystemExit('route map: read ascent markers %s, not 1-13' % sorted(dots))
    segs = {}
    for n, colour, x1, y1, x2, y2 in re.findall(
            r'<path id="asc-seg-(\d+)" class="route-seg" data-color="(#[0-9A-Fa-f]{6})"[^>]*d="M(\d+),(\d+) L(\d+),(\d+)"', asc):
        segs[int(n)] = {'colour': colour.upper(), 'd': 'M%s,%s L%s,%s' % (x1, y1, x2, y2)}
    if sorted(segs) != list(range(1, 13)):
        raise SystemExit('route map: read ascent segments %s, not 1-12' % sorted(segs))

    # the mountain's art: #epic-day-v2 and every def it reaches for
    sprite = src[src.index('<svg width="0" height="0"'):]
    sprite = sprite[:sprite.index('</svg>')]

    def by_id(i):
        m = re.search(r'<(\w+)\b[^>]*\bid="%s"[^>]*>.*?</\1>' % re.escape(i), sprite, re.S)
        if not m:
            raise SystemExit('route map: no #%s in the sprite' % i)
        return m.group(0)
    order, todo = [], [G['sprite']]
    while todo:
        i = todo.pop(0)
        if i in order:
            continue
        order.append(i)
        for ref in re.findall(r'url\(#([\w-]+)\)|href="#([\w-]+)"', by_id(i)):
            todo.append(ref[0] or ref[1])
    defs = [by_id(i) for i in reversed(order)]
    clip = re.search(r'<clipPath id="day-v2-clip">\s*<path d="([^"]+)"', sprite).group(1)
    pts = [(int(x), int(y)) for x, y in re.findall(r'(\d+) (\d+)', clip)]
    peak = min(pts, key=lambda p: p[1])

    names = re.findall(r'<option value="([a-z]{2})" lang="[a-z]{2}"(?: dir="rtl")?>([^<]+)</option>',
                       src[src.index('class="lang-select"'):])
    route = {'tok': tok, 'tenses': tenses, 'dots': dots, 'segs': segs, 'defs': defs, 'peak': peak,
             'names': dict(names), 'rows': tenses, 'order': sorted(tenses)}
    if G['face'] == 'descent':
        route.update(read_descent(src, tenses))
    return route


def read_descent(src, rows):
    """The route map's descent, keyed by TWIN camp (a stop is the camp the team sleeps at
    again on the way down; "Descent Eight" is the past continuous passive, from camp 6, and
    its own number is never shown). Returns what replaces the ascent's tenses, dots, segs
    and peak, plus the play order, the legs the climber walks and the four no-camp markers."""
    stops = {}
    for href, twin, c, name, lvl in re.findall(
            r'<a class="desc-row" href="(sherpa-tensing-descent-[a-z-]+\.html)" data-camp="(\d+)" style="--c:(#[0-9A-Fa-f]{6});">'
            r'<span class="diamond"[^>]*></span><span class="off-text"><span class="camp-name">([^<]+)</span>'
            r'.*?<span class="lvl"[^>]*>([^<]+)</span>', src, re.S):
        n = int(twin)
        if n not in rows or c.upper() != rows[n]['fill']:
            raise SystemExit('route map: desc row %s is camp %d in %s, the camp row says %s'
                             % (href, n, c, rows.get(n, {}).get('fill')))
        stops[n] = {'href': href, 'fill': c.upper(), 'ink': rows[n]['ink'], 'name': _html.unescape(name), 'level': lvl}
    if len(stops) != 9:
        raise SystemExit('route map: read %d desc rows, not 9' % len(stops))
    by_href = {v['href']: n for n, v in stops.items()}
    by_fill = {v['fill']: n for n, v in rows.items()}

    part = src[src.index('class="descent-map"'):]
    part = part[:part.index('</svg>')]
    marks = {}
    for cls, colour, href, points, glyph, lx, ly, anchor in re.findall(
            r'<g class="camp-dot (live|no-camp)" data-color="(#[0-9A-Fa-f]{6})"(?: data-href="([^"]+)")?'
            r'(?: data-seg="desc-seg-\d+")?\s*>\s*<polygon class="dot-fill" points="([^"]+)"[^>]*/>\s*(<g transform=.*?</g>)\s*'
            r'<text class="dot-label" x="(\d+)" y="(\d+)" text-anchor="(start|end)"[^>]*>[^<]+</text>', part, re.S):
        p = [tuple(int(v) for v in xy.split(',')) for xy in points.split()]
        x, y = p[0][0], p[1][1]
        if cls == 'live':
            if href not in by_href:
                raise SystemExit('route map: descent marker %s has no desc row' % href)
            n = by_href[href]
            if colour.upper() != stops[n]['fill']:
                raise SystemExit('route map: descent marker %s is %s, its row %s' % (href, colour, stops[n]['fill']))
        else:
            n = by_fill.get(colour.upper())
            if n is None or n in stops:
                raise SystemExit('route map: no-camp marker %s is not a camp without a passive' % colour)
        marks[n] = {'x': x, 'y': y, 'glyph': glyph.strip(), 'lx': int(lx), 'ly': int(ly), 'anchor': anchor,
                    'live': cls == 'live', 'colour': colour.upper()}
    if sorted(marks) != list(range(1, 14)) or sum(m['live'] for m in marks.values()) != 9:
        raise SystemExit('route map: read descent markers %s, not 13 with 9 live' % sorted(marks))

    raw = {}
    for k, x1, y1, x2, y2 in re.findall(
            r'<path id="desc-seg-(\d+)" class="route-seg" data-color="#[0-9A-Fa-f]{6}"[^>]*d="M(\d+),(\d+) L(\d+),(\d+)"', part):
        raw[int(k)] = ((int(x1), int(y1)), (int(x2), int(y2)))
    if sorted(raw) != list(range(2, 14)):
        raise SystemExit('route map: read descent segments %s, not 2-13' % sorted(raw))
    # the path, summit down: desc-seg-k runs from point k-2 to point k-1, each point a marker
    at = {(m['x'], m['y']): n for n, m in marks.items()}
    pts = [raw[2][0]] + [raw[k][1] for k in range(2, 14)]
    for k in range(3, 14):
        if raw[k][0] != raw[k - 1][1]:
            raise SystemExit('route map: desc-seg-%d does not start where desc-seg-%d ends' % (k, k - 1))
    if any(p not in at for p in pts):
        raise SystemExit('route map: a descent segment ends off a marker')
    path = [at[p] for p in pts]
    order = [n for n in path if marks[n]['live']]
    one, two = marks[order[-1]], marks[order[-2]]
    foot = (one['x'], one['y'] + (one['y'] - two['y']))     # one step below the last stop: base camp

    legs, segs, owner = {}, {}, {}
    live_at = [i for i, n in enumerate(path) if marks[n]['live']]
    for a, i in enumerate(live_at):
        j = live_at[a + 1] if a + 1 < len(live_at) else None
        legs[str(path[i])] = ([list(pts[q]) for q in range(i, j + 1)] if j is not None
                              else [list(pts[i]), list(foot)])
    for k in range(2, 14):
        start = k - 2
        before = [i for i in live_at if i <= start]
        owner[k] = path[before[-1]] if before else order[0]     # the opening leg lights with the first stop
        segs[k] = {'colour': stops[owner[k]]['fill'], 'd': 'M%d,%d L%d,%d' % (raw[k][0] + raw[k][1]), 'owner': owner[k]}
    legs['summit'] = [list(pts[live_at[-1]]), list(foot)]
    dots = {n: m for n, m in marks.items() if m['live']}
    nocamp = [marks[n] for n in path if not marks[n]['live']]
    return {'tenses': stops, 'dots': dots, 'segs': segs, 'peak': foot, 'order': order, 'legs': legs,
            'nocamp': nocamp}


# ── colours derived from the route map's (never picked) ────────────────────────
def deep(fill, paper):
    """The camp colour, darkened along its own hue until it reads as text on the paper (4.5:1)."""
    L, C, H = to_lch(fill)
    c = fill
    while contrast(c, paper) < 4.5 and L > 0.05:
        L -= 0.01
        c = from_lch(L, C, H)
    return c.upper()


def marker(fill):
    """A highlighter in the camp colour: the same hue, light enough to read ink over."""
    L, C, H = to_lch(fill)
    return from_lch(max(L, 0.86), min(C, 0.09), H).upper()


def pack(fill):
    """A muted pack colour for a team member, off one camp colour."""
    L, C, H = to_lch(fill)
    return from_lch(0.62, C * 0.55, H).upper()


# ── the team, seen from behind (the art rule: no faces) ─────────────────────────
PACK_FROM = {'ana': 2, 'otto': 3, 'sam': 7, 'doris': 11}
HAT = {'ana': 'beanie', 'otto': 'brim', 'sam': 'hood', 'doris': 'radio'}


def _size(rel):
    from PIL import Image
    return Image.open(os.path.join(ROOT, rel)).size


def hero_img():
    """The start screen's picture: base camp (Navya and Momo, where the story starts) once
    SherpaClimb/base-camp.jpg exists; camp two's scene until then. The Descent's: the summit at
    night (SherpaDescent/summit-night.jpg) once it exists; the team on top until then. The
    first of the game's `hero` pictures that exists."""
    hero = G['hero']
    base = next((b for b in hero if os.path.exists(os.path.join(ROOT, b + '.jpg'))), hero[-1])
    w, h = _size('%s.jpg' % base)
    sm = '%s-sm.jpg' % base
    if os.path.exists(os.path.join(ROOT, sm)):
        return ('<img src="%s" srcset="%s 960w, %s.jpg %dw" sizes="(max-width:860px) 100vw, 560px" '
                'width="%d" height="%d" alt="" fetchpriority="high">' % (sm, sm, base, w, w, h))
    return '<img src="%s.jpg" width="%d" height="%d" alt="" fetchpriority="high">' % (base, w, h)


def momo_img():
    """Momo never speaks, so he is not a team card; his portrait, once it exists, sits
    beside his line under the team (SherpaClimb/cast-momo.jpg)."""
    rel = 'SherpaClimb/cast-momo.jpg'
    if not os.path.exists(os.path.join(ROOT, rel)):
        return ''
    w, h = _size(rel)
    return '<img src="%s" width="%d" height="%d" alt="" loading="lazy" decoding="async">' % (rel, w, h)


def figure(who, route):
    # Innes's own character art, when it arrives, wins over the drawn figure with no code
    # change: SherpaClimb/cast-<who>.jpg (portrait, ~4:5; prep it with tools/prep-artwork.py
    # and docs/ARTWORK-sherpa-climb.md). Until then: Tensing is the course's sherpa render,
    # the others the SVG figures below.
    art = os.path.join(ROOT, 'SherpaClimb', 'cast-%s.jpg' % who)
    if os.path.exists(art):
        from PIL import Image
        w, h = Image.open(art).size
        return ('<img src="SherpaClimb/cast-%s.jpg" width="%d" height="%d" alt="" '
                'loading="lazy" decoding="async">' % (who, w, h))
    if who == 'tensing':
        return ('<img src="Sherpa%20Tensing/sherpa-guide.jpg" width="360" height="450" alt="" '
                'loading="lazy" decoding="async">')
    fill = route['rows'][PACK_FROM.get(who, 5)]['fill']
    p = pack(fill)
    L, C, H = to_lch(p)
    p_dark = from_lch(L - 0.12, C, H).upper()
    jacket = from_lch(0.84, C * 0.5, H).upper()
    hair = '#3A2A30'
    legs = '#4E4248'
    hat = HAT.get(who, 'beanie')
    out = ['<svg viewBox="0 0 64 80" aria-hidden="true" focusable="false">']
    # legs and boots
    out.append('<rect x="23" y="54" width="8" height="20" rx="3" fill="%s"/><rect x="33" y="54" width="8" height="20" rx="3" fill="%s"/>' % (legs, legs))
    out.append('<rect x="21" y="72" width="11" height="5" rx="2" fill="%s"/><rect x="32" y="72" width="11" height="5" rx="2" fill="%s"/>' % (hair, hair))
    # jacket: shoulders and arms
    out.append('<path d="M17 30 Q18 24 26 23 L38 23 Q46 24 47 30 L49 52 Q49 56 45 56 L19 56 Q15 56 15 52 Z" fill="%s"/>' % jacket)
    # head (from behind: hair)
    if hat == 'hood':
        # a hood up, seen from behind: one solid shape with a seam down the middle and a
        # drawstring hem. No opening, no hair showing: from the front a hood is a face
        out.append('<path d="M22 23 Q21 6 32 5 Q43 6 42 23 Q32 26 22 23 Z" fill="%s"/>' % jacket)
        out.append('<path d="M32 6 Q33 15 32 24" stroke="%s" stroke-width="1.2" fill="none" stroke-linecap="round"/>' % p_dark)
        out.append('<path d="M23 21 Q32 24 41 21" stroke="%s" stroke-width="1.6" fill="none" stroke-linecap="round"/>' % p_dark)
    else:
        out.append('<circle cx="32" cy="15" r="8" fill="%s"/>' % hair)
    if hat == 'beanie':
        out.append('<path d="M24 14 Q24 5 32 5 Q40 5 40 14 Z" fill="%s"/><circle cx="32" cy="4" r="2.6" fill="%s"/>' % (p_dark, jacket))
    elif hat == 'brim':
        out.append('<ellipse cx="32" cy="12" rx="14" ry="3.2" fill="%s"/><path d="M25 12 Q25 4 32 4 Q39 4 39 12 Z" fill="%s"/>' % (p_dark, p_dark))
    # the pack: a top roll, the body, two straps
    out.append('<rect x="20" y="26" width="24" height="28" rx="6" fill="%s"/>' % p)
    out.append('<rect x="19" y="21" width="26" height="7" rx="3.5" fill="%s"/>' % p_dark)
    out.append('<rect x="24" y="36" width="16" height="10" rx="3" fill="%s"/>' % p_dark)
    if hat == 'radio':
        out.append('<path d="M41 22 L47 4" stroke="%s" stroke-width="2" stroke-linecap="round"/><circle cx="47" cy="4" r="2" fill="%s"/>' % (hair, p_dark))
    out.append('</svg>')
    return ''.join(out)


# ── the mountain ────────────────────────────────────────────────────────────────
def mountain(route, content_ns, mini):
    """Two stacked SVGs: the art (never repainted) and the markers over it."""
    if G['shape'] == 'diamond':
        return mountain_night(route, content_ns, mini)
    tok = route['tok']
    if mini:
        vb = '150 50 500 540'
        r, hit, scale, sw = 15, 0, 1.35, 9
    else:
        vb = '0 0 800 620'
        r, hit, scale, sw = 11, 24, 1, 6
    art = ('<svg class="mtn-art" viewBox="%s" aria-hidden="true" focusable="false">'
           '<use href="#epic-day-v2" x="0" y="0" width="800" height="620"/></svg>' % vb)
    o = ['<svg class="mtn-over" viewBox="%s" aria-hidden="true" focusable="false">' % vb]
    for n in sorted(route['segs']):
        s = route['segs'][n]
        o.append('<path class="seg" data-seg="%d" data-color="%s" d="%s" stroke="%s" stroke-width="%d" '
                 'stroke-linecap="round" fill="none"/>' % (n, s['colour'], s['d'], GREY, sw))
    if mini:
        # wide enough to ring the marker and the climber beside it
        o.append('<circle class="pulse" cx="0" cy="0" r="%d" fill="none" stroke="%s" stroke-width="4"/>' % (r + 16, tok['--ink']))
    for n in sorted(route['dots']):
        d = route['dots'][n]
        t = route['tenses'][n]
        live = n in content_ns
        cls = 'dot' + ('' if live else ' soon')
        o.append('<g class="%s" data-camp="%d" data-color="%s">' % (cls, n, t['fill'] if live else GREY))
        if hit and live:
            o.append('<circle class="hit" cx="%d" cy="%d" r="%d"/>' % (d['x'], d['y'], hit))
        o.append('<circle class="dot-fill" cx="%d" cy="%d" r="%d" fill="%s" stroke="#FFFFFF" stroke-width="2"/>'
                 % (d['x'], d['y'], r, t['fill'] if live else GREY))
        glyph = d['glyph']
        if scale != 1:
            glyph = glyph.replace('transform="translate(%d,%d)"' % (d['x'], d['y']),
                                  'transform="translate(%d,%d) scale(%s)"' % (d['x'], d['y'], scale), 1)
        o.append(glyph)
        if not mini:
            o.append('<text class="dot-label" x="%d" y="%d" text-anchor="%s" dominant-baseline="central" font-size="18" '
                     'font-weight="600" font-family="Inter, sans-serif" fill="%s">%s</text>'
                     % (d['lx'], d['ly'], d['anchor'], tok['--ink'], esc(t['name'])))
        # a flag planted beside the marker once the camp is reached (painted by the page)
        fh, fw, ft = (30, 19, 12) if mini else (26, 16, 10)
        o.append('<g class="dflag" transform="translate(%d,%d)"><path d="M0,0 V-%d" stroke="%s" stroke-width="2.4" '
                 'stroke-linecap="round"/><path class="pennant" d="M0,-%d L%d,-%g L0,-%d Z" stroke="%s" stroke-width="1.4" '
                 'stroke-linejoin="round"/></g>'
                 % (d['x'] + round(r * 0.7), d['y'] - round(r * 0.5), fh, tok['--ink'],
                    fh, fw, fh - ft / 2, fh - ft, tok['--ink']))
        o.append('</g>')
    if mini:
        # the climber walks beside the route, not on it: standing on a marker it hid the
        # camp's colour and its pulse
        o.append('<g class="climber" id="climber"><g transform="translate(%d,-6) scale(1.7) translate(0,-6)">'
                 '<rect x="-7" y="-2" width="14" height="17" rx="4" fill="%s" stroke="#FFFFFF" stroke-width="2"/>'
                 '<rect x="-8" y="-7" width="16" height="6" rx="3" fill="%s" stroke="#FFFFFF" stroke-width="1.5"/>'
                 '<circle cx="0" cy="-12" r="5.5" fill="%s" stroke="#FFFFFF" stroke-width="2"/></g></g>'
                 % (r + 12, tok['--ink'], tok['--accent-dark'], tok['--ink']))
    o.append('</svg>')
    return '<div class="mtn%s">%s%s</div>' % (' mtn-mini' if mini else '', art, ''.join(o))


def diamond(x, y, h):
    return '%d,%d %d,%d %d,%d %d,%d' % (x, y - h, x + h, y, x, y + h, x - h, y)


def mountain_night(route, content_ns, mini):
    """The Descent's mountain: the route map's night art, its diamonds (half-diagonal 12 as
    on the map, 16 on the mini-map), the four passives nobody uses drawn faint and dashed
    with no number and no label (the page never selects them), and each segment over a
    pale casing so the darkest camp colours still read on night. The marker colours stay
    in the SVG attributes; descent.css turns the inks (labels, flags, pulse) to night-ink."""
    tok = route['tok']
    if mini:
        vb = G['mini_vb']
        h, hit, scale, sw = round(12 * 1.35), 0, 1.35, 9
    else:
        vb = '0 0 800 620'
        h, hit, scale, sw = 12, 24, 1, 6
    art = ('<svg class="mtn-art" viewBox="%s" aria-hidden="true" focusable="false">'
           '<use href="#%s" x="0" y="0" width="800" height="620"/></svg>' % (vb, G['sprite']))
    o = ['<svg class="mtn-over" viewBox="%s" aria-hidden="true" focusable="false">' % vb]
    for k in sorted(route['segs']):
        s = route['segs'][k]
        o.append('<path class="seg-case" d="%s" stroke-width="%d" stroke-linecap="round" fill="none"/>' % (s['d'], sw + 3))
        o.append('<path class="seg" data-seg="%d" data-color="%s" d="%s" stroke="%s" stroke-width="%d" '
                 'stroke-linecap="round" fill="none"/>' % (s['owner'], s['colour'], s['d'], GREY, sw))
    if mini:
        o.append('<circle class="pulse" cx="0" cy="0" r="%d" fill="none" stroke="%s" stroke-width="4"/>' % (h + 16, tok['--ink']))

    def glyph_at(m):
        g = m['glyph']
        if scale != 1:
            g = g.replace('transform="translate(%d,%d)"' % (m['x'], m['y']),
                          'transform="translate(%d,%d) scale(%s)"' % (m['x'], m['y'], scale), 1)
        return g
    for m in route['nocamp']:
        o.append('<g class="no-camp"><polygon class="dot-fill" points="%s" fill="%s" stroke="#FFFFFF" stroke-width="2"/>%s</g>'
                 % (diamond(m['x'], m['y'], h), GREY, glyph_at(m)))
    for n in route['order']:
        d = route['dots'][n]
        t = route['tenses'][n]
        live = n in content_ns
        o.append('<g class="%s" data-camp="%d" data-color="%s">' % ('dot' + ('' if live else ' soon'), n, t['fill'] if live else GREY))
        if hit and live:
            o.append('<circle class="hit" cx="%d" cy="%d" r="%d"/>' % (d['x'], d['y'], hit))
        o.append('<polygon class="dot-fill" points="%s" fill="%s" stroke="#FFFFFF" stroke-width="2"/>'
                 % (diamond(d['x'], d['y'], h), t['fill'] if live else GREY))
        o.append(glyph_at(d))
        if not mini:
            o.append('<text class="dot-label" x="%d" y="%d" text-anchor="%s" dominant-baseline="central" font-size="18" '
                     'font-weight="600" font-family="Inter, sans-serif" fill="%s">%s</text>'
                     % (d['lx'], d['ly'], d['anchor'], tok['--ink'], esc(t['name'])))
        fh, fw, ft = (30, 19, 12) if mini else (26, 16, 10)
        o.append('<g class="dflag" transform="translate(%d,%d)"><path d="M0,0 V-%d" stroke="%s" stroke-width="2.4" '
                 'stroke-linecap="round"/><path class="pennant" d="M0,-%d L%d,-%g L0,-%d Z" stroke="%s" stroke-width="1.4" '
                 'stroke-linejoin="round"/></g>'
                 % (d['x'] + round(h * 0.7), d['y'] - round(h * 0.5), fh, tok['--ink'],
                    fh, fw, fh - ft / 2, fh - ft, tok['--ink']))
        o.append('</g>')
    if mini:
        o.append('<g class="climber" id="climber"><g transform="translate(%d,-6) scale(1.7) translate(0,-6)">'
                 '<rect x="-7" y="-2" width="14" height="17" rx="4" fill="%s" stroke="#FFFFFF" stroke-width="2"/>'
                 '<rect x="-8" y="-7" width="16" height="6" rx="3" fill="%s" stroke="#FFFFFF" stroke-width="1.5"/>'
                 '<circle cx="0" cy="-12" r="5.5" fill="%s" stroke="#FFFFFF" stroke-width="2"/></g></g>'
                 % (h + 12, tok['--ink'], tok['--accent-dark'], tok['--ink']))
    o.append('</svg>')
    return '<div class="mtn%s">%s%s</div>' % (' mtn-mini' if mini else '', art, ''.join(o))


# ── the question line, and the line put right ──────────────────────────────────
def lines_of(it):
    """(question html, corrected html). The corrected line fills the gap(s) with the
    answer in <b>, takes the [brackets] off a spot form, and drops the cue."""
    text, kind = it['text'], it['kind']
    cue = None
    form = None
    if kind in ('choose', 'type'):
        m = CUE.search(text)
        if m:
            cue, text = m.group(1), text[:m.start()]
    if kind == 'spot':
        m = SPOT.search(text)
        form = m.group(1)
        text = text[:m.start()] + '\x01' + text[m.end():]
    text = GAP.sub('\x00', text)
    text = re.sub(r'\s+([.,!?;:])', r'\1', text).strip()
    e = esc(text)
    q = e.replace('\x00', '<span class="gap"></span>').replace('\x01', '<mark class="spot">%s</mark>' % esc(form or ''))
    if cue:
        q += ' <span class="cue">(%s)</span>' % esc(cue)
    fixed = e
    if kind == 'spot':
        fixed = fixed.replace('\x01', '<b>%s</b>' % esc(form))
    else:
        for p in parts(it['answer']):
            # "'ll carry" belongs to the word before it: "I<b>'ll carry</b>", not "I <b>'ll carry</b>"
            hole = ' \x00' if p.startswith("'") and ' \x00' in fixed else '\x00'
            fixed = fixed.replace(hole, '<b>%s</b>' % esc(p), 1)
    if '\x00' in fixed or '\x01' in fixed or '_' in fixed or '[' in fixed:
        raise SystemExit('%s: the corrected line did not come out clean: %r' % (it['id'], fixed))
    return q, fixed


# ── i18n ────────────────────────────────────────────────────────────────────────
def strings(c, route, en=None):
    """Every English string a translator sees: {English: note}, in page order."""
    out = {}

    def add(s, note):
        if s and s not in out:
            out[s] = note
    for key, (en_s, note) in (en or EN).items():
        add(en_s, note)
    for k, v in c.CAST.items():
        add(v['role'], 'what %s does in the team (team card, speaker rows)' % v['name'])
    for k, v in c.VIA.items():
        add(v, 'how a line reaches the team, shown after the speaker\'s name')
    for ln in getattr(c, 'INTRO', None) or []:
        add(ln['en'], 'the guide\'s welcome, on the start screen')

    def stage(s, where):
        for ln in s.get('arrive') or []:
            add(ln['en'], '%s, on arrival, said by %s. **bold** marks the tense: keep the marks round the same form' % (where, c.CAST[ln['who']]['name']))
        add(s['tip'], '%s, the tip. CAPS words are grammar and stay in English' % where)
        for it in s['items']:
            add(it['fb'], 'explanation after %s (%s). CAPS words stay in English; "quoted" words are the English' % (it['id'], it['text']))
        if s.get('done'):
            add(s['done']['en'], '%s, when it is finished, said by %s' % (where, c.CAST[s['done']['who']]['name']))
    for camp in c.CAMPS:
        stage(camp, 'camp %d (%s)' % (camp['n'], route['tenses'][camp['n']]['name']))
    if c.SUMMIT is not None:
        stage(c.SUMMIT, G['final_note'])
    for ln in getattr(c, 'OUTRO', None) or []:
        add(ln['en'], '%s, said by %s' % (G['end_note'], c.CAST[ln['who']]['name']))
    return out


def mark_inherited(out):
    """The Descent's list for translators: a string The Climb already has is marked, because
    its translation is inherited from i18n/<lang>.json (the tables merge, the descent's own
    file on top), so a translator need only do the rest."""
    if not INHERIT_DIR:
        return out
    p = os.path.join(INHERIT_DIR, 'strings.json')
    have = json.loads(read(p)) if os.path.exists(p) else {}
    tag = ' [inherited: The Climb has this English, so its translation comes from %s/<lang>.json]' % os.path.basename(INHERIT_DIR)
    return {k: (v + tag if k in have else v) for k, v in out.items()}


def problems(en, tr):
    """What a translation must keep: every CAPS token, every {placeholder}, ** pairs."""
    bad = []
    for tok in sorted(set(CAPS.findall(en))):
        if not re.search(r'(?<![A-Za-z])%s(?![A-Za-z])' % re.escape(tok), tr):
            bad.append('lost the CAPS token %s' % tok)
    if sorted(PLACE.findall(en)) != sorted(PLACE.findall(tr)):
        bad.append('placeholders %s became %s' % (sorted(PLACE.findall(en)), sorted(PLACE.findall(tr))))
    if tr.count('**') % 2:
        bad.append('unbalanced **')
    return bad


def _table(p, lang):
    try:
        d = json.loads(read(p) or '{}')
    except ValueError as e:
        raise SystemExit('%s/%s.json is not JSON: %s' % (os.path.basename(os.path.dirname(p)), lang, e))
    return {k: v for k, v in d.items() if isinstance(v, str) and v.strip()}


def load_i18n(all_strings, strict):
    """Each language's table: I18N_DIR/<lang>.json, merged OVER INHERIT_DIR/<lang>.json when the
    game inherits (The Descent over The Climb: a string whose English is the same takes the
    climb's translation unless the descent's own file says it differently). "Complete or
    empty" applies to the merged table; stale keys are counted in the game's own file only."""
    os.makedirs(I18N_DIR, exist_ok=True)
    complete, report, errors = [], [], []
    tables = {}
    where = os.path.basename(I18N_DIR)
    for lang in LANGS:
        p = os.path.join(I18N_DIR, lang + '.json')
        if not os.path.exists(p):
            io.open(p, 'w', encoding='utf-8', newline='\n').write('{}\n')
        own = _table(p, lang)
        base = {}
        if INHERIT_DIR and os.path.exists(os.path.join(INHERIT_DIR, lang + '.json')):
            base = _table(os.path.join(INHERIT_DIR, lang + '.json'), lang)
        have = dict(base)
        have.update(own)
        missing = [s for s in all_strings if s not in have]
        stale = [k for k in own if k not in all_strings]
        inherited = sum(1 for s in all_strings if s in base and s not in own)
        bad = []
        for s in all_strings:
            if s in have:
                bad += ['%s: %r %s' % (lang, s[:60], b) for b in problems(s, have[s])]
        errors += bad
        empty = len(missing) == len(all_strings)
        unstarted = bool(INHERIT_DIR) and not own and not empty
        if not missing and not bad:
            complete.append(lang)
            tables[lang] = {s: have[s] for s in all_strings}
            state = 'complete'
        elif empty:
            state = 'empty (not offered)'
        elif unstarted:
            state = 'not started, %d to translate (not offered)' % len(missing)
        else:
            state = 'PARTIAL, %d missing (not offered):' % len(missing)
        report.append('  %s: %d/%d %s%s%s' % (lang, len(all_strings) - len(missing), len(all_strings), state,
                                               (', %d inherited from %s' % (inherited, os.path.basename(INHERIT_DIR)))
                                               if INHERIT_DIR else '',
                                               (' %d stale key(s) ignored' % len(stale)) if stale else ''))
        # which strings: by name, so a translator can finish the file. An empty file is
        # missing all of them, and that list is i18n/strings.json itself (for a game that
        # inherits, an own file not yet started is the same: the list is its strings.json)
        if missing and not empty and not unstarted:
            report.extend('      missing: %s' % short(s) for s in missing)
        if strict and missing:
            errors.append('%s: %s (--strict)' % (lang, 'empty: all %d strings missing, listed in %s/strings.json'
                                                 % (len(missing), where) if empty or unstarted else '%d string(s) missing: %s'
                                                 % (len(missing), '; '.join(short(s) for s in missing))))
    return complete, tables, report, errors


def short(s, n=72):
    s = s.replace('\n', ' ')
    return repr(s if len(s) <= n else s[:n - 1] + '…')


# ── the page ────────────────────────────────────────────────────────────────────
def scene(n):
    """A stage's picture, without .jpg (the page adds -sm.jpg on a narrow screen). The
    Descent's own art, SherpaDescent/camp-NN (twin numbers) and storm, once both sizes
    exist; until then the climb's picture of the same camp (and camp one for the storm), so
    nothing 404s."""
    if n == 'summit':
        own, fallback = '%s/%s' % (G['scenes'], G['final_scene']), G['final_fallback']
    else:
        own = '%s/camp-%02d' % (G['scenes'], n)
        fallback = '%s/camp-%02d' % (G['scene_fallback'], n) if G['scene_fallback'] else None
    if fallback is None or all(os.path.exists(os.path.join(ROOT, own + x)) for x in ('.jpg', '-sm.jpg')):
        return own
    return fallback


def top_scene():
    """The end screen's picture. The Climb: the team on top (docs/ARTWORK-sherpa-climb.md)
    once it exists, the course's sherpa render until then. The Descent: base camp at last
    (SherpaDescent/base-camp.jpg), the climb's base camp until then."""
    top = G['top']
    return next((p for p in top if os.path.exists(os.path.join(ROOT, p))), top[-1])


def quiet_side(path):
    """Which side of a scene the card covers on a computer: the quieter one, so the camp
    itself stays in view (the cairn at twelve, the hut at eleven, the tent at nine). The
    measure is edge density at structure scale (the picture at 200px wide, so film grain
    does not count), left 5-45% against right 57-97% of the frame, below the top 10%.
    The right is the default; the card moves left only when the right is clearly busier."""
    from PIL import Image, ImageFilter, ImageStat
    im = Image.open(path).convert('L')
    w, h = im.size
    im = im.resize((200, round(h * 200 / w)), Image.LANCZOS)
    w, h = im.size
    e = im.filter(ImageFilter.FIND_EDGES)
    left = ImageStat.Stat(e.crop((int(w * .05), int(h * .1), int(w * .45), h - 1))).mean[0]
    right = ImageStat.Stat(e.crop((int(w * .57), int(h * .1), int(w * .97), h - 1))).mean[0]
    return 'left' if right > left * 1.08 else 'right'


def side_of(stage, img):
    if stage.get('side'):
        return stage['side']
    p = os.path.join(ROOT, img)
    return quiet_side(p) if os.path.exists(p) else 'right'


def sheen_grey(tok):
    """The climb wears the route map's greyed chrome, so its light is greyed as the map's
    is: tools/sherpa_sheen.py's own colours, at its MAP_CHROMA (Innes, 2026-09-28: "reduce
    the pink saturation on the topology too"). The tool gives every page but the map the
    vivid light, which on this page's greyed pink read as coral; this overrides only the
    two custom properties, one class stronger, and leaves the tool's block as it writes it,
    so its --check still passes."""
    sheen, hot = sherpa_sheen.colours(tok)
    sheen, hot = (from_lch(L, C * sherpa_sheen.MAP_CHROMA, H).upper() for L, C, H in (to_lch(sheen), to_lch(hot)))
    return 'html:root{--sheen:%s;--sheen-hot:%s;}' % (sheen, hot)


RUNTIME_VARS = {'--c', '--k', '--d', '--m'}    # set inline per camp by the page's script


def undefined_vars(css, defined):
    """var(--x) with no fallback that nothing defines: an empty value fails silently (the
    team cards lost their corners to a missing --radius)."""
    defined = set(defined) | set(re.findall(r'(--[a-z0-9-]+)\s*:', css)) | RUNTIME_VARS
    return sorted({v for v in re.findall(r'var\((--[a-z0-9-]+)\s*\)', css) if v not in defined})


def fence(js, game):
    """template.js's few game-specific lines: /*@game:climb*/A/*@game:descent*/B/*@game:end*/
    keeps A or B, and /*@game:descent*/B/*@game:end*/ alone is the descent's only. A marker
    alone on its line takes the line with it, so the climb's A is its original text, byte for
    byte (build.py --check proves it)."""
    js = re.sub(r'^[ \t]*(/\*@game:(?:climb|descent|end)\*/)[ \t]*\n', r'\1', js, flags=re.M)
    js = re.sub(r'/\*@game:climb\*/(.*?)/\*@game:descent\*/(.*?)/\*@game:end\*/',
                lambda m: m.group(1) if game == 'climb' else m.group(2), js, flags=re.S)
    js = re.sub(r'/\*@game:descent\*/(.*?)/\*@game:end\*/',
                lambda m: m.group(1) if game == 'descent' else '', js, flags=re.S)
    if '@game:' in js:
        raise SystemExit('template.js: a @game fence is not closed (%s)' % js[js.index('@game:') - 10:][:60])
    return js


SCENE_DIV = '<div class="scene"><img id="scene" alt="" decoding="async"></div>'


def page_template(tpl, en):
    """The template, fitted to the game: its <title>, every data-t text and data-t-aria label
    refilled from this game's English (for The Climb these are the template's own words, so
    nothing changes), and for The Descent the storm layer between the scene and the veil."""
    tpl, k = re.subn(r'<title>[^<]*</title>', lambda m: '<title>%s</title>' % esc(G['page_title']), tpl, count=1)
    if k != 1:
        raise SystemExit('template.html: no <title>')
    tpl, k1 = re.subn(r'(<[^<>]*\bdata-t="(\w+)"[^<>]*>)([^<]*)<',
                      lambda m: '%s%s<' % (m.group(1), esc(en[m.group(2)][0])), tpl)
    tpl, k2 = re.subn(r'aria-label="[^"]*" data-t-aria="(\w+)"',
                      lambda m: 'aria-label="%s" data-t-aria="%s"' % (attr(en[m.group(1)][0]), m.group(1)), tpl)
    if k1 < 10 or k2 < 3:
        raise SystemExit('template.html: refilled %d data-t text(s) and %d label(s); its literals have moved' % (k1, k2))
    if G['face'] == 'descent':
        if tpl.count(SCENE_DIV) != 1:
            raise SystemExit('template.html: the scene div is not there exactly once, so the storm has nowhere to go')
        tpl = tpl.replace(SCENE_DIV, SCENE_DIV + '\n  <div class="storm" aria-hidden="true"></div>')
    return tpl


SNOWFLAKE = ('<svg viewBox="0 0 20 20"><g stroke="currentColor" stroke-width="1.7" stroke-linecap="round" fill="none">'
             '<path d="M10 1.8v16.4M2.9 5.9l14.2 8.2M2.9 14.1l14.2-8.2"/>'
             '<path d="M7.8 3.2L10 5l2.2-1.8M7.8 16.8L10 15l2.2 1.8"/></g></svg>')


def build(strict=False):
    c = load_content()
    route = read_route()
    validate(c, route)
    en = chrome(c)
    tok = route['tok']
    paper = tok['--paper']
    content_ns = [camp['n'] for camp in c.CAMPS]
    order = route['order']
    last_route = order[-1]        # the climb: camp 13; the descent: camp 1, the last stop down

    def route_next(n):
        i = order.index(n)
        return order[i + 1] if i + 1 < len(order) else None

    tenses = {}
    for n, t in sorted(route['tenses'].items()):
        tenses[str(n)] = {'name': t['name'], 'level': t['level'], 'href': t['href'], 'fill': t['fill'],
                          'ink': t['ink'], 'deep': deep(t['fill'], paper), 'mark': marker(t['fill'])}

    def items_of(stage, home):
        out = []
        for it in stage['items']:
            q, fixed = lines_of(it)
            d = {'id': it['id'], 'kind': it['kind'], 'who': it['who'], 'q': q, 'fixed': fixed, 'fb': it['fb'],
                 'answer': it['answer']}
            if it.get('via'):
                d['via'] = it['via']
            if it['kind'] in ('choose', 'spot'):
                d['options'] = list(it['options'])
            if it['kind'] == 'choose':
                d['gaps'] = len(parts(it['answer']))
            if it['kind'] == 'type':
                d['accept'] = list(it['accept'])
            d['camp'] = it.get('camp', home)
            out.append(d)
        return out

    def lines(ls):
        return [{k: ln[k] for k in ('who', 'via', 'en') if ln.get(k)} for ln in (ls or [])]

    camps = []
    alts = [camp['alt'] for camp in c.CAMPS]
    for i, camp in enumerate(c.CAMPS):
        n = camp['n']
        nxt = c.CAMPS[i + 1] if i + 1 < len(c.CAMPS) else None
        if nxt and nxt['n'] == route_next(n):
            next_alt = nxt['alt']
        elif n == last_route and c.SUMMIT is not None:
            next_alt = c.SUMMIT['alt']
        elif nxt:
            next_alt = nxt['alt']
        else:   # not written yet: go on at the last step's rate (up for the climb, down for the descent)
            next_alt = camp['alt'] + ((camp['alt'] - alts[i - 1]) if i else 400 * G['dir'])
        st = {'n': n, 'alt': camp['alt'], 'nextAlt': next_alt, 'scene': scene(n),
              'side': side_of(camp, scene(n) + '.jpg'),
              'arrive': lines(camp.get('arrive')), 'tip': camp['tip'], 'items': items_of(camp, n),
              'done': lines([camp['done']])[0] if camp.get('done') else None}
        if 'storm' in camp:
            st['storm'] = camp['storm']
        camps.append(st)
    summit = None
    if c.SUMMIT is not None:
        s = c.SUMMIT
        summit = {'n': 'summit', 'alt': s['alt'], 'nextAlt': s['top'], 'scene': scene('summit'),
                  'side': side_of(s, scene('summit') + '.jpg'),
                  'arrive': lines(s.get('arrive')), 'tip': s['tip'], 'items': items_of(s, 'summit'),
                  'done': lines([s['done']])[0] if s.get('done') else None}
        if 'storm' in s:
            summit['storm'] = s['storm']
    figs = {who: figure(who, route) for who in c.CAST}
    top = top_scene()
    data = {
        'camps': camps, 'summit': summit, 'outro': lines(getattr(c, 'OUTRO', None)),
        'cast': {k: {'name': v['name'], 'role': v['role']} for k, v in c.CAST.items()},
        'via': dict(c.VIA), 'figs': figs, 'tenses': tenses, 'lastRoute': last_route,
        'dots': {str(n): [d['x'], d['y']] for n, d in sorted(route['dots'].items())},
        'peak': list(route['peak']), 'grey': GREY, 'gold': GOLD,
        'top': {'scene': top.replace(' ', '%20'), 'side': side_of({}, top)},
    }
    if G['face'] == 'descent':
        data['legs'] = route['legs']       # the polylines the climber walks, through the no-camp markers
        data['top']['storm'] = 0           # calm at base camp

    all_strings = strings(c, route, en)
    complete, tables, report, errors = load_i18n(all_strings, strict)
    if errors:
        raise SystemExit('translations refused (%d):\n  %s' % (len(errors), '\n  '.join(errors)))
    langs = ['en'] + complete
    i18n = {'en': {k: v[0] for k, v in en.items()}, 'langs': langs, 'rtl': RTL,
            'names': {l: route['names'].get(l, l) for l in langs}, 't': tables}

    def js_json(obj):
        return json.dumps(obj, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')

    # static markup
    tok_css = ':root{%s}' % ''.join('%s:%s;' % (k, v) for k, v in tok.items())
    tok_css += ':root{--gold:%s;--grey:%s;}' % (GOLD, GREY)
    tok_css += sheen_grey(tok)
    sprite = ('<svg class="sprite" width="0" height="0" aria-hidden="true" focusable="false" '
              'style="position:absolute;overflow:hidden"><defs>\n%s\n</defs></svg>' % '\n'.join(route['defs']))
    intro = ''
    if getattr(c, 'INTRO', None):
        # the box is the guide's; a line someone else says (Navya's storm warning in The
        # Descent) carries its speaker's name
        li = ''.join('<li>%s<span class="en">%s</span><span class="gl" data-gl="%s"></span></li>'
                     % ('' if ln['who'] == 'tensing' else '<span class="brief-by">%s:</span> ' % esc(c.CAST[ln['who']]['name']),
                        bold(ln['en']), attr(ln['en'])) for ln in c.INTRO)
        # on a phone the guide's first line shows, and "How it works" opens the others
        more = ('<button class="brief-more" type="button" aria-expanded="false" aria-controls="brief-lines">'
                '<span data-t="howItWorks">%s</span> <span aria-hidden="true">&darr;</span></button>'
                % esc(en['howItWorks'][0])) if len(c.INTRO) > 1 else ''
        intro = ('<div class="brief" id="brief"><p class="brief-who"><span data-t="briefWho">%s</span></p>'
                 '<ul id="brief-lines">%s</ul>%s</div>' % (esc(en['briefWho'][0]), li, more))
    team = ''.join('<li class="member"><span class="fig">%s</span><span class="mtext"><b>%s</b>'
                   '<span class="role">%s</span><span class="gl" data-gl="%s"></span></span></li>'
                   % (figs[k], esc(v['name']), esc(v['role']), attr(v['role'])) for k, v in c.CAST.items())
    picks = []
    night = G['shape'] == 'diamond'
    for camp in c.CAMPS:
        t = tenses[str(camp['n'])]
        # the descent's number sits in a diamond, turned back upright (descent.css)
        num = ('<span>%d</span>' if night else '%d') % camp['n']
        picks.append('<li><button class="pick" type="button" data-camp="%d" style="--c:%s;--k:%s">'
                     '<span class="pick-num">%s</span><span class="pick-name">%s</span>'
                     '<span class="pick-meta"><span class="pick-lvl">%s</span><span class="pick-best"></span>'
                     '<span class="pick-flag"></span></span></button></li>'
                     % (camp['n'], t['fill'], t['ink'], num, esc(t['name']), esc(t['level'])))
    if c.SUMMIT is not None:
        icon = (SNOWFLAKE if night else '<svg viewBox="0 0 20 20"><path d="M2 17 L8 6 L11 11 L13 8 L18 17 Z" '
                'fill="currentColor"/></svg>')
        picks.append('<li><button class="pick pick-summit" type="button" data-camp="summit">'
                     '<span class="pick-num" aria-hidden="true">%s</span><span class="pick-name" data-t="summitRow">%s</span>'
                     '<span class="pick-meta"><span class="pick-best"></span><span class="pick-flag"></span></span></button></li>'
                     % (icon, esc(en['summitRow'][0])))
    options = ''.join('<option value="%s" lang="%s"%s>%s</option>' % (l, l, ' dir="rtl"' if l in RTL else '',
                                                                      esc(i18n['names'][l])) for l in langs)

    tpl = page_template(read(os.path.join(HERE, 'template.html')), en)
    css = read(os.path.join(HERE, 'template.css'))
    if G['css']:
        css = css.strip('\n') + '\n' + read(os.path.join(HERE, G['css']))
    js = fence(read(os.path.join(HERE, 'template.js')), 'descent' if G['face'] == 'descent' else 'climb')
    undef = undefined_vars(css, list(tok) + ['--gold', '--grey'])
    if undef:
        raise SystemExit('template.css uses %s, which nothing defines (add a fallback, or the token)' % ', '.join(undef))
    slots = {
        'CSS': tok_css + '\n' + css.strip('\n'),
        'JS': js.strip('\n'),
        'DATA': js_json(data),
        'I18N': js_json(i18n),
        'SPRITE': sprite,
        'INTRO': intro,
        'TEAM': team,
        'HERO_IMG': hero_img(),
        'MOMO_IMG': momo_img(),
        'PICKS': ''.join(picks),
        'MAP_START': mountain(route, content_ns, False),
        'MAP_MINI': mountain(route, content_ns, True),
        'LANG_OPTIONS': options,
        'LANG_SOLO': ' solo' if len(langs) == 1 else '',
        'BRAND': sherpa_links.BRAND_NEW,
        'SUB': sherpa_links.SUB_NEW,
    }
    for k, v in slots.items():
        tpl = tpl.replace('{{%s}}' % k, v)
    left = re.findall(r'\{\{[A-Z_]+\}\}', tpl)
    if left:
        raise SystemExit('template slots left unfilled: %s' % left)
    page = family(tpl)
    return page, all_strings, report


# ── the family look, with the tools' own functions ─────────────────────────────
def cloud_sizes():
    from PIL import Image
    return {k: Image.open(os.path.join(ROOT, sherpa_sky.DIR, 'cloud-%d.webp' % k)).size
            for k in range(1, sherpa_sky.IMAGES + 1)}


def family(src):
    """Each block exactly as its tool writes it, so every tool's --check passes."""
    # SHERPA-TYPE (tools/sherpa_type.py main())
    base = sherpa_type.FENCE.sub('', src)
    b = sherpa_type.block(base)
    src = sherpa_type.keep_fraunces(sherpa_type.FENCE.sub(lambda m: b, src, count=1) if sherpa_type.FENCE.search(src)
                                    else src.replace('</head>', b + '</head>', 1))
    # SHERPA-TOPO (tools/sherpa_topo.py main())
    src = (sherpa_topo.FENCE.sub(lambda m: sherpa_topo.block(), src, count=1) if sherpa_topo.FENCE.search(src)
           else src.replace('</head>', sherpa_topo.block() + '</head>', 1))
    # SHERPA-SHEEN, SHERPA-SKY (their apply())
    src = sherpa_sheen.apply(src, False)
    src = sherpa_sky.apply(src, cloud_sizes())
    # SHERPA-ARRIVE (tools/sherpa_arrive.py main())
    f = sherpa_arrive.FENCE
    src = f.sub(lambda m: sherpa_arrive.BLOCK, src, count=1) if f.search(src) else src.replace('</head>', sherpa_arrive.BLOCK + '</head>', 1)
    return src


def family_problems(src):
    """Run each tool's own test on the page as built: what its --check would say."""
    bad = []
    again = family(src)
    if again != src:
        bad.append('the family blocks are not stable (a second pass changes the page)')
    if sherpa_links.BRAND_NEW not in src or sherpa_links.SUB_NEW not in src:
        bad.append('the wordmark is not sherpa_links.BRAND_NEW + SUB_NEW')
    if '<section class="hero"' not in src or '<div class="brand">' not in src:
        bad.append('no <section class="hero"> or <div class="brand"> (sherpa_arrive)')
    if not re.search(r'--accent-dark\s*:', src) or not re.search(r'<main\b', src):
        bad.append('no --accent-dark or <main> (sherpa_topo)')
    if '--accent' not in sherpa_sheen.tokens(src) or '--paper' not in sherpa_sheen.tokens(src):
        bad.append('no hex --accent / --paper (sherpa_sheen)')
    return bad


# ── SEO block: tools/seo.py writes one into the page; carry it over ────────────
SEO = re.compile(r'<!-- SEO:start -->.*?<!-- SEO:end -->\n?', re.S)


def carry_seo(page, old):
    if not old:
        return page
    m = SEO.search(old)
    if not m:
        return page
    title = re.search(r'<title>.*?</title>', old, re.S)
    if title:
        page = re.sub(r'<title>.*?</title>', lambda _: title.group(0), page, count=1, flags=re.S)
    anchor = re.search(r'<meta name="viewport"[^>]*>\n', page)
    return page[:anchor.end()] + m.group(0) + page[anchor.end():]


def real_strings():
    """The translators' list always comes from the game's real content file (content.py,
    content_descent.py), whatever the page was built from, and whether or not its gates
    pass: a draft must not rewrite it, and a refused item still has words to translate.
    Until the real file exists (or while it cannot even be read for strings) the list
    comes from the content the page is built from, and says so."""
    global CONTENT
    real = os.path.join(HERE, G['content'])
    keep = CONTENT
    for path in ([real] if os.path.exists(real) else []) + ([keep] if keep != real else []):
        CONTENT = path
        try:
            c = load_content()
            return mark_inherited(strings(c, read_route(), chrome(c)))
        except Exception as e:      # an unfinished real file: say so, and use the build's own content
            print('  strings.json: %s could not be read for strings (%s: %s)' % (os.path.basename(path), type(e).__name__, e))
        finally:
            CONTENT = keep
        if path == real:
            print('  strings.json: from %s until %s reads' % (os.path.basename(keep), G['content']))
    if not os.path.exists(real):
        print('  strings.json: %s does not exist yet' % G['content'])
    raise SystemExit('no content to list strings from')


def set_game(name):
    """Point every path at one game's files (before --content/--out/--i18n, which still win)."""
    global G, CONTENT, I18N_DIR, INHERIT_DIR, STRINGS, OUT, OUT_NAME
    G = GAMES[name]
    CONTENT = os.path.join(HERE, G['content'])
    I18N_DIR = os.path.join(HERE, G['i18n'])
    INHERIT_DIR = os.path.join(HERE, G['inherit']) if G['inherit'] else None
    STRINGS = os.path.join(I18N_DIR, 'strings.json')
    OUT_NAME = G['out']
    OUT = os.path.join(ROOT, OUT_NAME)


def run(name, args):
    global CONTENT, I18N_DIR, OUT, OUT_NAME
    set_game(name)
    if '--content' in args:
        CONTENT = os.path.abspath(args[args.index('--content') + 1])
        print('content from %s' % CONTENT)
    if '--out' in args:           # a variant for a test: never the page's own path
        OUT = os.path.abspath(args[args.index('--out') + 1])
        OUT_NAME = os.path.basename(OUT)
        print('page to %s' % OUT)
    if '--i18n' in args:          # another translations folder (a draft, or a test)
        I18N_DIR = os.path.abspath(args[args.index('--i18n') + 1])
        print('translations from %s' % I18N_DIR)
    if '--dump' in args:
        c = load_content()
        route = read_route()
        validate(c, route)
        print(json.dumps({'game': name, 'page': G['out'], 'save': G['save'], 'dir': G['dir'], 'finalId': G['final_id'],
                          'miniVb': [int(v) for v in G['mini_vb'].split()], 'order': route['order'],
                          'lastRoute': route['order'][-1],
                          'camps': c.CAMPS, 'summit': c.SUMMIT, 'outro': getattr(c, 'OUTRO', None),
                          'cast': c.CAST, 'tenses': {str(n): t['name'] for n, t in route['tenses'].items()},
                          'hrefs': {str(n): t['href'] for n, t in route['tenses'].items()},
                          'en': {k: v[0] for k, v in chrome(c).items()}},
                         ensure_ascii=True))  # a Windows console is cp1252: "→" in an fb would crash the print
        return 0
    check, strict = '--check' in args, '--strict' in args
    strings_json = json.dumps(real_strings(), ensure_ascii=False, indent=1) + '\n'
    page, all_strings, report = build(strict)
    old = read(OUT) if os.path.exists(OUT) else None
    page = carry_seo(page, old)
    bad = family_problems(page)
    if bad:
        raise SystemExit('family look:\n  ' + '\n  '.join(bad))
    old_strings = read(STRINGS) if os.path.exists(STRINGS) else None
    rel = '%s/strings.json' % G['i18n']
    print('translations (%d strings):' % len(all_strings))
    for line in report:
        print(line)
    if check:
        fails = []
        if old != page:
            fails.append('%s is not a fresh build: run build.py%s' % (OUT_NAME, '' if name == 'climb' else ' --game ' + name))
        if old_strings != strings_json:
            fails.append('%s is stale: run build.py%s' % (rel, '' if name == 'climb' else ' --game ' + name))
        for f in fails:
            print('FAIL ' + f)
        print('PASS: %s is a fresh build' % OUT_NAME if not fails else 'FAIL: %d' % len(fails))
        return 1 if fails else 0
    if old_strings != strings_json:
        io.open(STRINGS, 'w', encoding='utf-8', newline='\n').write(strings_json)
        print('  wrote %s' % rel)
    if old != page:
        io.open(OUT, 'w', encoding='utf-8', newline='\n').write(page)
        print('  wrote %s (%d KB)' % (OUT_NAME, len(page.encode('utf-8')) // 1024))
    else:
        print('  %s unchanged' % OUT_NAME)
    return 0


def main():
    args = sys.argv[1:]
    game = args[args.index('--game') + 1] if '--game' in args else 'climb'
    if game == 'all':
        if any(a in args for a in ('--content', '--out', '--i18n', '--dump')):
            raise SystemExit('--game all builds or checks the real pages only (no --content, --out, --i18n or --dump)')
        codes = []
        for name in GAMES:
            print('== %s ==' % name)
            codes.append(run(name, args))
        sys.exit(max(codes))
    if game not in GAMES:
        raise SystemExit('--game is %s or all, not %r' % (' | '.join(GAMES), game))
    sys.exit(run(game, args))


if __name__ == '__main__':
    main()
