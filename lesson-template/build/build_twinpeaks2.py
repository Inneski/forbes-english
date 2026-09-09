# -*- coding: utf-8 -*-
"""Between Two Worlds — Advanced Prepositions (C1), rebuilt as a 16:9 deck.

`twin_peaks_prepositions_v5.html` was a 145 KB scrolling page, English only,
with no hero — which is why it has been sitting in the library as a disabled
"Coming soon" card since `38d2ac5`. Every scored item survives: 10 multiple
choice, 11 gap-fill blanks, 8 error-correction, 8 matching pairs.

Two things about this build are new to the repo.

**The panel layout.** The artwork here is six flat-vector illustrations, not
atmosphere, and §5's washed hero at 0.72 under a plated card is the wrong
treatment for a picture that is worth looking at. `deck.panel()` gives the
image a 548px column at full opacity and the text the rest of the stage, on
flat --void. Nothing is plated, because nothing overlaps. `deck.divider()`
opens each stage with the picture alone. Both live in the template, so any
deck can use them.

**What was cut, and why.** The old page listed 36 collocations across three
tables. At ~55 words a slide that is nine slides of list, which is reference
material rather than teaching, so this deck carries the 24 that the exercises
actually test and drops the rest. Nothing that is tested was cut.

The activation stage did not exist on the old page — HOUSE-STYLE §0 rule 6
requires one, so it is written here rather than ported.

Artwork is `TwinPeaks2/`, six images prepped from the Midjourney PNGs with
tools/prep-artwork.py (34.7 MB -> 2.0 MB). The palette is derived from
hero.jpg; every contrast row PASSes.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_twinpeaks2 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'twin_peaks_prepositions_v5.html'
F = 'TwinPeaks2'

E = I.T['en']          # one source for the English; see the i18n docstring

# py lesson-template/extract-palette.py TwinPeaks2/hero.jpg
PALETTE = """  --hero: url('%s/hero.jpg');

  --void          : #0b0e10;
  --surface       : #131a1f;
  --surface2      : #1b252b;
  --border        : #c87664;
  --text          : #f5f2f2;
  --text-dim      : #bfa8a3;
  --accent        : #f3ae9f;
  --accent-bright : #fbbaac;
  --accent-dim    : #e46c52;
  --secondary     : #131d23;
  --contrast      : #1dedae;""" % F


# ── helpers so the slide list below reads as a deck, not as plumbing ───
def panel(n, stage, pic, side='left', pos=None):
    """A two-paragraph panel slide. Keys follow s<n>t / s<n>a / s<n>b."""
    return D.panel('e%d' % stage, E['e%d' % stage], 's%dt' % n, E['s%dt' % n],
                   [('s%da' % n, E['s%da' % n]),
                    ('s%db' % n, E['s%db' % n], 'dim')],
                   folder=F, pic=pic, side=side, pos=pos)


def cards(n, stage, letters, bg=None, cols=None):
    """A teach slide of 3-4 six-item cards. Keys are s<n><letter>{h,b,n}."""
    return D.teach('e%d' % stage, E['e%d' % stage], 's%dt' % n, E['s%dt' % n],
                   [('s%d%sh' % (n, L), E['s%d%sh' % (n, L)],
                     's%d%sb' % (n, L), E['s%d%sb' % (n, L)],
                     's%d%sn' % (n, L), E['s%d%sn' % (n, L)]) for L in letters],
                   cols=cols, folder=F, bg=bg)


def divider(n, pic, pos=None):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic, pos=pos)


# ── the ten investigation questions ────────────────────────────────────
# Options are never translated: they ARE the English being tested. The key
# is placed at a different index each time and is never the longest option
# — check-lesson.js measures both.
MC = [
    dict(stem='The agent was determined to solve the case, ____ the risk to his own life.',
         options=['although', 'despite', 'because of', 'in spite'],
         correct=1,
         why='q1w'),
    dict(stem='The outcome of the investigation depended entirely ____ one witness.',
         options=['from', 'of', 'on', 'at'],
         correct=2,
         why='q2w'),
    dict(stem='She had not spoken a word ____ the night of the murder.',
         options=['since', 'after', 'from', 'during'],
         correct=0,
         why='q3w'),
    dict(stem='Cooper was well aware ____ the dangers that waited beyond the curtain.',
         options=['about', 'for', 'with', 'of'],
         correct=3,
         why='q4w'),
    dict(stem='____ the evidence gathered, a pattern began to emerge.',
         options=['Despite of', 'On the basis of', 'In the event of', 'Due to'],
         correct=1,
         why='q5w'),
    dict(stem='The man ____ the black jacket had been standing there all night.',
         options=['on', 'in', 'with', 'wearing'],
         correct=1,
         why='q6w'),
    dict(stem='The trauma resulted ____ years of repressed memory.',
         options=['in', 'of', 'by', 'from'],
         correct=3,
         why='q7w'),
    dict(stem='Which is the better choice for formal academic writing?',
         # The key must not be the longest option — a learner can score on
         # length alone, and check-lesson.js measures it. The informal
         # distractor is correct English too; that is the point of the
         # question, so padding it costs nothing.
         options=['The lodge that he had originally come from was now sealed.',
                  'The lodge from which he had come was now sealed.',
                  'The lodge what he had come from was now sealed.',
                  'The lodge he had came from was now sealed.'],
         correct=1,
         # Options are shuffled at runtime, so an explanation may never say
         # "the first two" — by the time a learner reads it, the order has
         # changed. Name the forms instead.
         why='q8w'),
    dict(stem='The sheriff was found guilty ____ withholding evidence.',
         options=['for', 'about', 'of', 'in'],
         correct=2,
         why='q9w'),
    dict(stem='____ Cooper, every agent who entered the Lodge lost their mind.',
         options=['Besides from', 'Except to', 'Outside of', 'Apart from'],
         correct=3,
         why='q10w'),
]

# ── the Black Lodge: 11 blanks over four slides ────────────────────────
# Every row carries its own explanation. A gap-fill that explains only some
# of its blanks tells a learner they were wrong and not why — and the EXPLAIN
# gate fails the build for it.
GAP = [
    [('The discovery of the body resulted ______ a full federal investigation. '
      '(event &rarr; consequence)', ['in'],
      'g1w1'),
     ('______ ______ ______ the fog, Cooper pressed on toward the cabin. '
      '(three words, = despite)', ['in', 'spite', 'of'],
      'g1w2')],
    [('She had been obsessed ______ the case ever ______ the first victim was found.',
      ['with', 'since'],
      'g2w1'),
     ('He was aware ______ being watched, and he responded ______ this by leaving '
      'a false trail.', ['of', 'to'],
      'g2w2')],
    [('The log lady spoke ______ ______ ______ those who could not speak for '
      'themselves. (three words, = representing)', ['on', 'behalf', 'of'],
      'g3w1'),
     ('______ ______ ______ a series of coded messages, the killer revealed their '
      'location. (three words, = using)', ['by', 'means', 'of'],
      'g3w2')],
    [('The effect ______ the town was devastating.', ['on'],
      'g4w1'),
     ('Nobody was capable ______ trust anymore.', ['of'],
      'g4w2')],
]

# ── crime scene: four right, four wrong ────────────────────────────────
SORT_ITEMS = [
    ('She was very interested about the investigation.', 1),
    ('The detective apologised for the delay in filing his report.', 0),
    ('Despite of the warnings, he entered the mill alone.', 1),
    ('The increase in strange phenomena was documented.', 0),
    ('She had been living in Twin Peaks since twenty years.', 1),
    ('On behalf of the department, I extend our condolences.', 0),
    ('The crime resulted of a long sequence of events.', 1),
    ('He was found guilty of first-degree murder.', 0),
]

# Eight pairs on one slide measured 504px into a 500px body — four over.
# HOUSE-STYLE §6 is explicit that the answer is more slides, never smaller
# type, so the eight are split four and four along their part of speech.
MATCH_A = [
    ('She was afraid ___', 'of what was inside'),
    ('He specialises ___', 'in forensic linguistics'),
    ('The suspect suffers ___', 'from anxiety'),
    ('She was capable ___', 'of anything'),
]
MATCH_B = [
    ('Her attitude ___', 'towards the case'),
    ('This resulted ___', 'in a trial'),
    ("He's responsible ___", 'for the crime'),
    ('There was no solution ___', 'to the mystery'),
]


def build():
    logo = D.logo_from(TPL)
    n_mc, n_gap = len(MC), len(GAP)

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        # ── stage 1 · advanced theory ──────────────────────────────────
        divider(1, 'among-trees.jpg'),
        panel(1, 1, 'hero.jpg'),
        cards(2, 1, 'abc', bg='among-trees.jpg'),
        panel(3, 1, 'profile.jpg', side='right'),
        cards(4, 1, 'abc', bg='window.jpg'),
        cards(5, 1, 'abc', bg='window.jpg'),
        panel(6, 1, 'coffee.jpg', pos='60% 50%'),

        # ── stage 2 · multi-word forms ─────────────────────────────────
        divider(2, 'coffee.jpg', pos='60% 50%'),
        cards(7, 2, 'abcd', bg='coffee.jpg', cols='1fr 1fr'),
        cards(8, 2, 'abcd', bg='among-trees.jpg', cols='1fr 1fr'),
        cards(9, 2, 'abcd', bg='among-trees.jpg', cols='1fr 1fr'),
        panel(10, 2, 'window.jpg', side='right', pos='38% 50%'),
        cards(11, 2, 'abc', bg='hero.jpg'),

        # ── stage 3 · lexical patterns ─────────────────────────────────
        divider(3, 'window.jpg', pos='38% 50%'),
        cards(12, 3, 'abcd', bg='window.jpg', cols='1fr 1fr'),
        panel(13, 3, 'hero.jpg', side='right'),
        cards(14, 3, 'abcd', bg='hero.jpg', cols='1fr 1fr'),
        cards(15, 3, 'abcd', bg='profile.jpg', cols='1fr 1fr'),
        cards(16, 3, 'abcd', bg='profile.jpg', cols='1fr 1fr'),
        cards(17, 3, 'abcd', bg='coffee.jpg', cols='1fr 1fr'),

        # ── stage 4 · the double agents ────────────────────────────────
        divider(4, 'profile.jpg'),
        panel(18, 4, 'among-trees.jpg'),
        cards(19, 4, 'abc', bg='profile.jpg'),
        cards(20, 4, 'ab', bg='profile.jpg', cols='1fr 1fr'),
        panel(21, 4, 'window.jpg', side='right', pos='38% 50%'),
        panel(22, 4, 'coffee.jpg', pos='60% 50%'),

        # ── stage 5 · the investigation ────────────────────────────────
        divider(5, 'among-trees.jpg'),
    ] + [
        D.mc(i + 1, n_mc, q, 'e5', E['e5'], 'q%dt' % (i + 1), E['q%dt' % (i + 1)],
             folder=F, bg=['hero.jpg', 'among-trees.jpg', 'coffee.jpg',
                           'window.jpg', 'profile.jpg'][i % 5])
        for i, q in enumerate(MC)
    ] + [
        # ── stage 6 · the black lodge ──────────────────────────────────
        divider(6, 'red-room.jpg'),
    ] + [
        D.gap(i + 1, n_gap, rows, None, 'e6', E['e6'],
              'g%dt' % (i + 1), E['g%dt' % (i + 1)],
              folder=F, bg='red-room.jpg',
              hint=E['gapHint'], hint_key='gapHint', width=130)
        for i, rows in enumerate(GAP)
    ] + [
        # ── stage 7 · crime scene analysis ─────────────────────────────
        divider(7, 'hero.jpg'),
        D.sort_slide([E['binOk'], E['binBad']], SORT_ITEMS,
                     'e7', E['e7'], 'sortT', E['sortT'],
                     'sortHint', E['sortHint'], 'sortWhy',
                     bin_keys=['binOk', 'binBad'],
                     folder=F, bg='hero.jpg'),

        # ── stage 8 · red room connections ─────────────────────────────
        divider(8, 'red-room.jpg'),
        D.match(MATCH_A, 'e8', E['e8'], 'matchT', E['matchT'],
                'matchHint', E['matchHint'], 'matchWhy',
                folder=F, bg='red-room.jpg'),
        D.match(MATCH_B, 'e8', E['e8'], 'matchT2', E['matchT2'],
                'matchHint', E['matchHint'], 'matchWhy',
                folder=F, bg='red-room.jpg'),

        # ── results, then activation ───────────────────────────────────
        # §10b: the activation stage comes AFTER the results and is the last
        # thing the learner sees. This deck had them the other way round, so
        # the lesson ended on a score instead of on the learner producing
        # something. The ACTIVATION gate only asserts the slide exists, so
        # nothing caught it — found by the session building The Square.
        D.results(folder=F, bg='hero.jpg'),
        D.activate(E['actTitle'], E['actUse'],
                   ['in spite of', 'aware of', 'result in', 'on behalf of',
                    'capable of'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg='profile.jpg'),
    ])

    D.assemble(TPL, OUT, slides, PALETTE,
               'Between Two Worlds — Advanced Prepositions (C1)',
               I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides' % (OUT, slides.count('<section class="slide')))


if __name__ == '__main__':
    build()
