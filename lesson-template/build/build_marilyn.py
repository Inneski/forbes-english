# -*- coding: utf-8 -*-
"""The Mystery of Marilyn Monroe — Prepositions (B1), rebuilt as a 16:9 panel
deck ("house style 2").

`marilyn_prepositions.html` was a scrolling page with three activities (five
multiple choice, five dropdowns, five drag-and-drops) and a free-writing box.
Innes found two wrong keys in it while teaching on 2026-10-04 (`fe343f65`);
the audit that followed (`9484fd83`) replaced every distractor that was also
correct and two false biographical claims. This rebuild keeps all fifteen
items and regroups them by what they teach rather than by widget:

  1 Time            — AT / ON / IN cards, MC ×4
  2 Place, movement — the model paragraph from the old free-writing box
                      (rewritten: the old one described film reels the
                      picture does not contain), cards ×2, gap ×3 (7 blanks),
                      MC ×1 (the subway grate)
  3 Fixed partners  — cards ×2, MC ×3, sort ×8 (four L1 slips)
then results and the activation stage, which carries the old "write what
you see" task with a reader and a purpose.

**Art.** Two flat screen-print portraits, which is the panel layout's case
exactly. HOUSE-STYLE §5c wants a picture per section plus one for the
activation; two pictures cover the cover and stage 1 (the hero) and stage 2
(the close-up). Until the three plates in docs/ARTWORK-marilyn.md exist this
builds the live page on different crops of the two portraits — face, eye,
earring — and swaps each plate in as soon as its file is in `Marilyn/`.

Card examples deliberately avoid the tested sentences: a card that prints
"ON 1 June 1926" before a question about 1 June 1926 tests reading, not
prepositions.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_marilyn as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'marilyn_prepositions.html'
F = 'Marilyn'

HERO = 'marilyn-hero.jpg'
DETAIL = 'marilyn-detail.jpg'


def plate(name, fallback):
    return name if os.path.exists(os.path.join(F, name)) else fallback


GRATE = plate('plate-grate.jpg', DETAIL)     # stage 2 divider
REEL = plate('plate-reel.jpg', HERO)         # stage 3 divider + panel
SEATS = plate('plate-seats.jpg', DETAIL)     # activation
MISSING = [p for p in ('plate-grate.jpg', 'plate-reel.jpg', 'plate-seats.jpg')
           if not os.path.exists(os.path.join(F, p))]

# The drop folder the brief names. Innes, 2026-09-30: "make sure the folder
# exists or you tell me to make it in future, hard wire that".
DROP = os.path.join('incoming', 'marilyn')
if MISSING:
    os.makedirs(DROP, exist_ok=True)

E = I.T['en']

# py lesson-template/extract-palette.py Marilyn/marilyn-hero.jpg
# (2026-10-04; every row PASS)
PALETTE = """  --hero: url('%s/%s');

  --void          : #111614;
  --surface       : #1a2320;
  --surface2      : #232f2a;
  --border        : #b56960;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #e99b92;
  --accent-bright : #f5bbb4;
  --accent-dim    : #d4594b;
  --secondary     : #4c718e;
  --contrast      : #1ded9e;""" % (F, HERO)

# English example line under each card: no key, never translated.
NOTES = {
    2: {'a': 'AT eight o’clock · AT the age of twenty · AT night',
        'b': 'ON 14 January · ON Monday · ON the night of the premiere',
        'c': 'IN August · IN 1962 · IN the 1950s · IN the morning'},
    4: {'a': 'IN the kitchen · IN Brentwood · IN Los Angeles',
        'b': 'ON the screen · ON page 5 · ON Fifth Helena Drive',
        'c': 'AT the cinema · AT the premiere · AT the top of the company'},
    5: {'a': 'The lamp hangs OVER the table.',
        'b': 'We drove THROUGH the tunnel. · She went THROUGH a divorce.',
        'c': 'The cat is asleep UNDER the bed.'},
    7: {'a': 'Hollywood is famous FOR its films.',
        'b': 'Do you know anything ABOUT jazz?',
        'c': 'He died FROM his injuries.'},
    8: {'a': 'She signed a contract WITH a record company.',
        'b': 'Keep the children OUT OF the kitchen.',
        'c': 'The police have a file ON him.',
        'd': 'She married a doctor. · She is married TO a doctor.'},
}

S1_EXAMPLES = ('<em>a star IN the 1950s · famous AT twenty-seven · '
               'married ON 29 June 1956</em>')

# The old free-writing model described "pale lines … echoing old film reels",
# which are not in the picture. This one describes what is there.
MODEL = ('Her pale hair falls <strong>across</strong> her forehead and hangs '
         '<strong>down</strong> the right side of the picture. The left side is '
         '<strong>in</strong> deep shadow, so only one eye looks out '
         '<strong>at</strong> us. A streak of orange runs <strong>down</strong> '
         'her cheek, <strong>below</strong> that eye, and a small beauty mark sits '
         'just <strong>above</strong> her lip.')


def cards(n, stage, letters, bg, cols=None):
    return D.teach('e%d' % stage, E['e%d' % stage], 's%dt' % n, E['s%dt' % n],
                   [('s%d%sh' % (n, L), E['s%d%sh' % (n, L)],
                     's%d%sb' % (n, L), E['s%d%sb' % (n, L)],
                     None, NOTES[n][L]) for L in letters],
                   cols=cols, folder=F, bg=bg)


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


# ── multiple choice ────────────────────────────────────────────────────
# Every distractor is wrong in the sentence, not merely less likely: the
# old page lost points to "during the early hours" and "inside her bedroom".
MC_TIME = [
    dict(stem='Marilyn Monroe was born ____ 1 June 1926, in Los Angeles.',
         options=['at', 'on', 'in', 'during'], correct=1, why='q1w'),
    dict(stem='Her body was discovered ____ the early hours of 5 August 1962.',
         options=['in', 'at', 'on', 'to'], correct=0, why='q2w'),
    dict(stem='She married the baseball player Joe DiMaggio ____ January 1954.',
         options=['at', 'in', 'on', 'for'], correct=1, why='q3w'),
    dict(stem='She died ____ the age of thirty-six.',
         options=['in', 'on', 'at', 'with'], correct=2, why='q4w'),
]
# "on" is left out on purpose: she stood ON the grate as well as OVER it.
MC_GRATE = [
    dict(stem='Her white dress blew up as she stood ____ a subway grate.',
         options=['along', 'over', 'into', 'towards'], correct=1, why='q8w'),
]
# "away from public life" is correct English, so it is not an option.
MC_PARTNERS = [
    dict(stem='In 1946 she signed her first film contract ____ 20th Century Fox.',
         options=['by', 'of', 'with', 'under'], correct=2, why='q5w'),
    dict(stem='Some say powerful people wanted to keep her ____ public life.',
         options=['out of', 'out at', 'aside of', 'apart of'], correct=0, why='q6w'),
    dict(stem='The FBI kept a file ____ Monroe because of her political friends.',
         options=['at', 'of', 'over', 'on'], correct=3, why='q7w'),
]
for group in (MC_TIME, MC_GRATE, MC_PARTNERS):
    D.assert_no_key_is_longest(group)

# ── gap fill: (rows, bank) ─────────────────────────────────────────────
GAPS = [
    ([('Monroe was found dead ______ her bedroom.', ['in'], 'g1w1'),
      ('She appeared ______ the cover of the first issue of Playboy.', ['on'], 'g1w2')],
     ['on', 'at', 'in']),
    ([('The scene was filmed ______ Lexington Avenue, ______ New York.',
       ['on', 'in'], 'g2w1'),
      ('A train passed ______ the street, and the air rushed up ______ the grate.',
       ['under|beneath|underneath|below', 'through|from'], 'g2w2')],
     ['through', 'in', 'over', 'under', 'on']),
    ([('Many believe there was a conspiracy ______ the highest levels of government.',
       ['at|within'], 'g3w1'),
      ('She lived ______ a difficult childhood, moving between foster homes.',
       ['through'], 'g3w2')],
     ['through', 'by', 'at', 'across']),
]
for rows, bank in GAPS:
    D.assert_bank_is_not_a_key(bank, [a for _, ans, _ in rows for a in ans])

# ── sort: the four slips a B1 learner actually makes ──────────────────
SORT_ITEMS = [
    ('She was famous for her breathy voice.', 0),
    ('She was famous by her breathy voice.', 1),
    ('Some believe she knew too much about the Kennedys.', 0),
    ('The FBI kept a file at her for years.', 1),
    ('The coroner said she had died from an overdose.', 0),
    ('The coroner said she had died for an overdose.', 1),
    ('In 1956 she married Arthur Miller.', 0),
    ('In 1956 she got married with Arthur Miller.', 1),
]


def build():
    logo = D.logo_from(TPL)
    mc_bg = [HERO, DETAIL, HERO, DETAIL]

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        # ── stage 1 · time ─────────────────────────────────────────────
        divider(1, HERO),
        D.panel('e1', E['e1'], 's1t', E['s1t'],
                [('s1a', E['s1a']), (None, S1_EXAMPLES, 'dim')],
                folder=F, pic=HERO, pos='55% 50%'),
        cards(2, 1, 'abc', HERO),
    ] + [
        D.mc(i + 1, len(MC_TIME), q, 'e1', E['e1'], 'mcT', E['mcT'],
             folder=F, bg=mc_bg[i])
        for i, q in enumerate(MC_TIME)
    ] + [
        # ── stage 2 · place and movement ───────────────────────────────
        divider(2, GRATE),
        D.panel('e2', E['e2'], 's3t', E['s3t'],
                [('s3a', E['s3a'], 'dim'), (None, MODEL)],
                folder=F, pic=DETAIL, side='right', pos='58% 50%'),
        cards(4, 2, 'abc', DETAIL),
        cards(5, 2, 'abc', GRATE),
    ] + [
        D.gap(i + 1, len(GAPS), rows, bank, 'e2', E['e2'], 'gapT', E['gapT'],
              folder=F, bg=DETAIL, hint=E['gapHint'], hint_key='gapHint',
              width=130)
        for i, (rows, bank) in enumerate(GAPS)
    ] + [
        D.mc(1, 1, MC_GRATE[0], 'e2', E['e2'], 'mcT', E['mcT'],
             folder=F, bg=GRATE),

        # ── stage 3 · fixed partners ───────────────────────────────────
        divider(3, REEL),
        D.panel('e3', E['e3'], 's6t', E['s6t'],
                [('s6a', E['s6a']), ('s6b', E['s6b'], 'dim')],
                folder=F, pic=REEL, pos='82% 50%' if REEL == HERO else '20% 50%'),
        cards(7, 3, 'abc', HERO),
        cards(8, 3, 'abcd', REEL, cols='1fr 1fr'),
    ] + [
        D.mc(i + 1, len(MC_PARTNERS), q, 'e3', E['e3'], 'mcT', E['mcT'],
             folder=F, bg=[HERO, DETAIL, HERO][i])
        for i, q in enumerate(MC_PARTNERS)
    ] + [
        D.sort_slide([E['binOk'], E['binBad']], SORT_ITEMS,
                     'e3', E['e3'], 'sortT', E['sortT'],
                     'sortHint', E['sortHint'], 'sortWhy',
                     bin_keys=['binOk', 'binBad'], folder=F, bg=REEL),

        # ── results, then activation (§10b: activation is last) ────────
        D.results(folder=F, bg=HERO),
        D.activate(E['actTitle'], E['actUse'],
                   ['on 14 January', 'in the early hours', 'at the age of',
                    'famous for', 'know about', 'keep … out of'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=SEATS),
    ])

    D.assemble(TPL, OUT, slides, PALETTE,
               'The Mystery of Marilyn Monroe — Prepositions (B1)',
               I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides%s' % (
        OUT, slides.count('<section class="slide'),
        ('; plates still missing: %s (drop them in %s/)' % (', '.join(MISSING), DROP))
        if MISSING else ''))


if __name__ == '__main__':
    build()
