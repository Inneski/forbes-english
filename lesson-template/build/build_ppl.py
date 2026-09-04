# -*- coding: utf-8 -*-
"""Present Perfect with Lego (B1) — rebuilt as a 16:9 deck.

`forbes-english-present-perfect-lego-b1.html`, mechanically the soundest of the
nine Lego pages and the first of them off the scrolling format. All twenty-six
scored items survive: seven multiple choice, seven gaps, six sentences to
rebuild and six signal words to sort.

What changed, beyond the format:

- **Multiple-choice question one was ungrammatical.** The stem read "My nephew
  ____ this Lego castle three times this week" and the key was `has built it`,
  which produces *has built it this Lego castle*. Two of the three distractors
  carried the same duplicated object, so the item could not be answered
  correctly whichever way a learner read it. Rewritten around the same stem and
  the same teaching point.
- **The gaps accepted one spelling each.** The original compared with `===`, so
  `'ve finished` and `havent found` were marked wrong. Every gap now takes its
  contraction and its apostrophe-less form, and gap seven takes both
  `has completed` and `have completed`, since British English lets `team` be
  singular or plural.
- **Activity 4 was not a matching activity.** Six cues mapped onto two
  right-hand cells — Simple or Continuous — which is a sort, and `match()`
  cannot pair six terms to two definitions. It is a sort slide now, which is
  what it always was.
- **The Polish glosses are gone from the cues.** They read "just / właśnie".
  Polish is not one of the site's nine languages and the switcher does not
  offer it, so it was the one L1 a learner could not turn off. The cues stand
  in English and the switcher does the L1 work — German and Spanish here.
- **It now teaches.** The original had a two-line legend contrasting the two
  forms and nothing else. Three slides now cover the two shapes, the single
  question that chooses between them (result or activity), and the state verbs
  that have no continuous at all. Every one of the twenty-six items lands
  inside one of the three.

Artwork is the existing `lego/` family — six flat-vector brick studies in
coral, pink, navy and cream, already on disk. `lego-b2-cube-0.jpg` was this
page's own image and stays the cover, so `library.html` needs no edit.

The palette is `extract-palette.py --light`. The artwork is cream and pink
throughout and a dark chrome sat on it as mud; on a light theme the derived
canvas is already a warm sand, so there is no near-black to lift and every
token is tool output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from ppl_data import MC, FIB, ORDER, SORT, SORT_BINS

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-present-perfect-lego-b1.html'
F = 'lego'

# python3 lesson-template/extract-palette.py lego/lego-b2-cube-0.jpg --light
PALETTE = '''  --hero: url('%s/lego-b2-cube-0.jpg');

  --void          : #d8cdac;
  --surface       : #e1dac4;
  --surface2      : #dcd3b8;
  --border        : #96544a;
  --text          : #2a1411;
  --text-dim      : #5e342e;
  --accent        : #ae230e;
  --accent-bright : #861404;
  --accent-dim    : #e26755;
  --secondary     : #0a3a5d;
  --contrast      : #07553a;''' % F

CHIPS = ['have you ever', 'so far', 'for two days', 'I have just',
         'all morning', 'not yet', 'since I was', 'three times']

MC_BG = ['lego-b2-cube-1.jpg', 'lego-b2-scene-a.jpg', 'lego-b2-cube-2.jpg',
         'lego-b2-scene-b.jpg', 'lego-b2-cube-1.jpg', 'lego-b2-scene-c.jpg',
         'lego-b2-cube-2.jpg']
FIB_BG = ['lego-b2-scene-a.jpg', 'lego-b2-cube-1.jpg', 'lego-b2-scene-c.jpg',
          'lego-b2-cube-2.jpg']
ORD_BG = ['lego-b2-cube-1.jpg', 'lego-b2-scene-b.jpg', 'lego-b2-cube-2.jpg',
          'lego-b2-scene-a.jpg', 'lego-b2-cube-1.jpg', 'lego-b2-scene-c.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'PresentPerfectLego')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Present Perfect, <em>Brick by Brick</em>',
                'Two tenses that look the same, and the one question that separates '
                'them',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Present perfect simple &amp; continuous'),
                 ('Count', '24 slides')])

        + D.teach('shEyebrow', 'Before the questions',
                  'shTitle', 'One tense, two shapes',
                  [('sh1h', 'The simple form', 'sh1b',
                    '<strong>Have</strong> or <strong>has</strong> + past participle: '
                    '<em>she <strong>has built</strong> the castle</em>. It reports a '
                    'finished action whose result is still here now.',
                    'sh1n', 'The castle exists. That is the point of the sentence.'),
                   ('sh2h', 'The continuous form', 'sh2b',
                    '<strong>Have</strong> or <strong>has been</strong> + <em>-ing</em>: '
                    '<em>she <strong>has been building</strong> the castle</em>. It '
                    'reports the activity itself, running up to now.',
                    'sh2n', 'It may be finished, it may not. The sentence is not '
                            'saying.'),
                   ('sh3h', 'Both connect past to present', 'sh3b',
                    'Neither one is a past tense. Both say something about <em>now</em>: '
                    'the result of the action, or the activity that produced it. Past '
                    'simple cuts that link.',
                    'sh3n', '<em>I built it yesterday</em> is over. <em>I have built '
                            'it</em> reaches into now.')],
                  folder=F, bg='lego-b2-cube-1.jpg')

        + D.teach('chEyebrow', 'The one question',
                  'chTitle', 'Result, or activity?',
                  [('ch1h', 'Ask what the sentence is about', 'ch1b',
                    'If it is about the <strong>outcome</strong> &mdash; what now '
                    'exists, how many times, whether it is done &mdash; use the simple. '
                    'If it is about the <strong>doing</strong> &mdash; how long, why '
                    'you are tired, the mess on the table &mdash; use the continuous.',
                    'ch1n', 'One question, asked every time. Everything below follows '
                            'from it.'),
                   ('ch2h', 'Counting means simple', 'ch2b',
                    '<em>Three times</em>, <em>twice</em>, <em>the third time</em> count '
                    'finished events, and you cannot count an activity that is still '
                    'running. <em>He <strong>has dropped</strong> it three times</em>.',
                    'ch2n', '<em>Has been dropping</em> would describe a habit, not '
                            'three events.'),
                   ('ch3h', 'Duration means continuous', 'ch3b',
                    '<em>For two days</em>, <em>all morning</em>, <em>since 2019</em> '
                    'measure how long. <em>She <strong>has been working</strong> on it '
                    'for two days</em> &mdash; the length is the news.',
                    'ch3n', '<em>For</em> and <em>since</em> both take the continuous '
                            'when duration is the point.')],
                  folder=F, bg='lego-b2-scene-a.jpg')

        + D.teach('stEyebrow', 'The exception',
                  'stTitle', 'Some verbs have no continuous',
                  [('st1h', 'State verbs', 'st1b',
                    '<em>Be</em>, <em>have</em> (own), <em>know</em>, <em>like</em>, '
                    '<em>believe</em>, <em>seem</em> describe states, not activities. A '
                    'state has no <em>-ing</em> form here, however long it lasts.',
                    'st1n', '<em>I have known her for years</em>, never <em>have been '
                            'knowing</em>.'),
                   ('st2h', '<em>Have</em> is two verbs', 'st2b',
                    'Owning is a state: <em>How many minifigures <strong>have you '
                    'got</strong>?</em> Doing something is not: <em>we <strong>have been '
                    'having</strong> trouble with step 12</em> is fine.',
                    'st2n', 'If <em>have</em> means <em>own</em>, no continuous. If it '
                            'means <em>experience</em>, it is allowed.'),
                   ('st3h', 'The tired-hands test', 'st3b',
                    'When a present state is explained by a recent activity, the state '
                    'takes the simple and the activity takes the continuous: <em>my '
                    'hands hurt because I <strong>have been sorting</strong> '
                    'pieces</em>.',
                    'st3n', 'Two clauses, two tenses, and each one is doing a different '
                            'job.')],
                  folder=F, bg='lego-b2-cube-2.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Simple or continuous?', folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 4, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The exact form',
                        'fibTitle', 'Complete the sentence',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='The verb is given in brackets. Contractions are accepted.',
                        width=180, size=18)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:6], FIB[6:]]))

        + "".join(D.order(chunks, 'ordEyebrow',
                          'Activity 3 &middot; Sentence building',
                          'ordTitle', 'Put the sentence back together',
                          'ordHint', 'Click a chunk to place it, click a placed chunk '
                                     'to take it back.',
                          why, folder=F, bg=ORD_BG[n])
                  for n, (chunks, why) in enumerate(ORDER))

        + D.sort_slide(SORT_BINS, SORT, 'sortEyebrow',
                       'Activity 4 &middot; The signal words',
                       'sortTitle', 'Which form does each one call for?',
                       'sortHint', 'Click a word to place it, click a placed word to '
                                   'take it back.',
                       'sortWhy', folder=F, bg='lego-b2-scene-b.jpg')

        + D.results('resNext', 'You can pick the form. Now report the weekend &rarr;',
                    folder=F, bg='lego-b2-cube-0.jpg')

        + D.activate('Report on the build', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you has been building all weekend; the other has just '
                     'walked in and wants to know what happened. Three minutes each, '
                     'then swap.',
                     ['Say what you have finished today and what you have been working '
                      'on but not finished.',
                      'Explain why the room looks like this. Use the activity, not the '
                      'result.',
                      'Ask your partner three questions with <em>ever</em>, and follow '
                      'each answer up.',
                      'Describe something you have been doing since you were a child.'],
                     'Writing &middot; 120&ndash;150 words',
                     'Write the message you would send a friend after a weekend of '
                     'building. Say what you have finished, what you have been working '
                     'on, how long it has taken, and what you still have not managed. '
                     'Use both forms and make each one earn its place.',
                     'I have finally finished the…',
                     folder=F, bg='lego-b2-scene-c.jpg')
    )

    import i18n_ppl as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Present Perfect with Lego (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d order, %d sort, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(ORDER),
             len(SORT), len(s)))


if __name__ == '__main__':
    build()
