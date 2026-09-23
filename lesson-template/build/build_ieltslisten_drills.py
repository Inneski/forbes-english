# -*- coding: utf-8 -*-
"""IELTS Listening: numbers, spelling and accents — the drills.

The last lesson on the Listening route and the odd one out. The four section
lessons each teach a section; this one takes the three things that lose marks
in **all** of them and drills each on its own.

**Two short recordings rather than one long one, and that is the whole
difference.** Every other deck on this route plays a section once, because
that is the test. A drill is the opposite: a few seconds, repeated until the
distinction is automatic — and the engine's replay control, which on the
section decks says plainly that the real test will not let you, is here the
point rather than a concession.

Each clip is built from short takes in **different accents**, so the accent
drill is not a section at the end: it is the structure of the other two. A
learner meets British, American, Australian, Canadian, Irish and New Zealand
English while doing nothing but writing down numbers and letters.

Five number gaps across two slides, two spelled names, a sort that groups the
letter pairs which actually collide, and four questions on the conventions
themselves.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltslisten_drills_data import (CLIPS, NUMBERS_A, NUMBERS_B, NUMBERS_BANK,
                                     SPELLING, SPELLING_BANK,
                                     PAIRS_BINS, PAIRS_ITEMS, PAIRS_WHY, MC)

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-listening-drills.html'
F = 'ielts-listen-drills'

# python3 lesson-template/extract-palette.py ielts-listen-drills/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0c0e0c;
  --surface       : #171b16;
  --surface2      : #21271f;
  --border        : #b38066;
  --text          : #f5f3f2;
  --text-dim      : #bfada3;
  --accent        : #e8b297;
  --accent-bright : #f2bca1;
  --accent-dim    : #d27c51;
  --secondary     : #335159;
  --contrast      : #1dedce;''' % F

CHIPS = ['double oh = 00', 'eight eighty', 'thirteen &ne; thirty',
         'A and E collide', 'E and I are swapped', 'double F = FF']

BG_BRIEF, BG_NUM, BG_SPELL, BG_PAIRS = ('bg02.jpg', 'bg03.jpg',
                                        'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build(make_audio=False):
    D.assert_no_key_is_longest(MC, 'IELTSDRILLS')
    logo = D.logo_from(TPL)

    if make_audio:
        import tts
        for fn, takes, _label in CLIPS:
            tts.render(takes, os.path.join(F, fn))

    import tts
    labels = {}
    for fn, _takes, label in CLIPS:
        p = os.path.join(F, fn)
        assert os.path.exists(p), (
            '%s is missing. Run this builder once with --audio; a drill whose '
            'clip is absent ships a player that never starts.' % p)
        secs = tts.duration(p)
        labels[fn] = '%s &middot; 0:%02d' % (label, int(secs))

    slides = (
        D.cover(logo, 'Numbers, spelling <em>and accents</em>',
                'The three things that lose marks in every section, drilled on '
                'their own',
                [('Level', 'B2&ndash;C1'),
                 ('Focus', 'Listening &middot; all four sections'),
                 ('Count', '17 points')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title',
                  'These are not listening problems. They are convention '
                  'problems.',
                  [('t1ah', 'English says numbers its own way', 't1ab',
                    '<em>Double oh</em> is two noughts. <em>Oh</em> is one. A '
                    'room is <em>eight eighty</em>, not eight hundred and '
                    'eighty. None of this is hard to hear &mdash; it is hard '
                    'to <strong>expect</strong>.', 't1an',
                    'Thirteen and thirty are the costliest pair in the '
                    'language. The stress moves; the vowel barely does.'),
                   ('t1bh', 'Letter names collide', 't1bb',
                    '<strong>A</strong> and <strong>E</strong>, '
                    '<strong>E</strong> and <strong>I</strong>, '
                    '<strong>G</strong> and <strong>J</strong>, '
                    '<strong>M</strong> and <strong>N</strong>. Four pairs, '
                    'and between them they account for most of the misspelled '
                    'answers on the paper.', 't1bn',
                    'E and I are the worst, because they are swapped between '
                    'English and most European languages. What you were taught '
                    'at school is actively against you here.'),
                   ('t1ch', 'Six accents, one test', 't1cb',
                    'British, American, Australian, Canadian, Irish and New '
                    'Zealand English all appear in real papers. The two '
                    'recordings here are built from takes in different '
                    'accents, so you are drilling all three things at once.',
                    't1cn',
                    'You cannot learn an accent in a lesson. You can stop '
                    'being surprised by one, and that is most of the '
                    'benefit.')],
                  folder=F, bg=BG_BRIEF)

        + D.audio('numAudEyebrow', 'Drill 1 &middot; The recording',
                  'numAudTitle', 'Five speakers, five numbers',
                  'numAudNote',
                  'Short takes in five accents. Look at the gaps on the next '
                  'slides, then press play &mdash; here or in the bar at the '
                  'foot of those slides. When it ends you can play it again '
                  'from here: this is a drill, not the test.',
                  'numbers.mp3', labels['numbers.mp3'], folder=F, bg=BG_NUM)

        + "".join(D.gap(n + 1, 2, rows, NUMBERS_BANK,
                        'numEyebrow', 'Drill 1 &middot; Numbers',
                        'numTitle', 'Write ONE NUMBER in each gap',
                        folder=F, bg=BG_NUM,
                        hint_key='numHint',
                        hint='Write figures, not words. Two of these are said '
                             'in a way English learners are rarely taught.',
                        width=210, size=19)
                  for n, rows in enumerate([NUMBERS_A, NUMBERS_B]))

        + D.audio('spellAudEyebrow', 'Drill 2 &middot; The recording',
                  'spellAudTitle', 'Two names, spelled once each',
                  'spellAudNote',
                  'Two takes, two accents. Each name is given letter by letter '
                  'exactly once, at speaking speed, as in the real test. Look '
                  'at the gaps on the next slide, then press play.',
                  'spelling.mp3', labels['spelling.mp3'], folder=F,
                  bg=BG_SPELL)

        + D.gap(1, 1, SPELLING, SPELLING_BANK,
                'spellEyebrow', 'Drill 2 &middot; Spelling',
                'spellTitle', 'Write the name exactly as it was spelled',
                folder=F, bg=BG_SPELL,
                hint_key='spellHint',
                hint='Spelling is marked. One of these uses the same "double" '
                     'convention as the numbers drill.',
                width=240, size=19)

        + D.sort_slide(PAIRS_BINS, PAIRS_ITEMS,
                       'sortEyebrow', 'Drill 3 &middot; The pairs that collide',
                       'sortTitle',
                       'Which letter names actually get confused?',
                       'sortHint',
                       'Drag each pair into a column &mdash; or click one, '
                       'then the column you want it in.',
                       PAIRS_WHY, folder=F, bg=BG_PAIRS,
                       bin_keys=['sortBin1', 'sortBin2'])

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Drill 4 &middot; The conventions', 'mcTitle',
                       'What does English actually do here?',
                       folder=F, bg=BG_PAIRS, ctx=q.get('ctx'))
                  for i, q in enumerate(MC))

        + D.results('resNext', 'You can hear it. Now dictate it &rarr;',
                    folder=F)

        + D.activate('Dictate and check', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'In pairs, taking turns. Dictate five things to your '
                     'partner: a surname, a phone number, a price, a date and '
                     'a room number. Say each one once, at normal speed. Then '
                     'swap papers and mark them &mdash; every wrong character '
                     'is a lost mark, exactly as in the test.',
                     ['Use <em>double</em> at least once, in a number and in a '
                      'name.',
                      'Put one number in your set that contains a thirteen or '
                      'a thirty, and do not help.',
                      'Spell one name containing two of the colliding pairs '
                      '&mdash; an A and an E, or an M and an N.'],
                     'Writing &middot; 80&ndash;120 words',
                     'Write out the five items you dictated, in figures and '
                     'letters, then write beside each one the mistake you '
                     'expected your partner to make. Naming the trap in '
                     'advance is what stops you walking into it yourself.',
                     'Surname: … (expected mistake: A heard as R)',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltslisten_drills as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Listening: Numbers, Spelling and Accents | Forbes English',
                   I, langs=('en', 'de', 'es'))
    pts = (sum(r[0].count('______') for r in NUMBERS_A + NUMBERS_B + SPELLING)
           + len(PAIRS_ITEMS) + len(MC))
    print('wrote %s — %d slides, %d scored points, %d clips, %d bytes'
          % (OUT, s.count('<section class="slide'), pts, len(CLIPS), len(s)))


if __name__ == '__main__':
    build(make_audio='--audio' in sys.argv)
