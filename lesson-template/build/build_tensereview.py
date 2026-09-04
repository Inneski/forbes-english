# -*- coding: utf-8 -*-
"""Tense Review — Minecraft Edition (B2) — rebuilt as a 16:9 deck.

`tense-review-minecraft.html`, second of the six Minecraft lessons on the old
scrolling format. All thirty scored items survive: six multiple choice, seven
gaps in a streamer's commentary, five grammar claims to judge, six collocations
and six sentences to repair.

What changed, beyond the format:

- **It now teaches.** The original opened with a rail of twelve tense names —
  Pres. Simple, Pres. Cont., Pres. Perf. Sim. and so on — and explained none of
  them. Three slides do that work now: the three questions that pick a tense
  (when / finished or running / finished before what), the perfect continuous
  family, and the two traps that account for most of the losses here (a closed
  time reference next to a present perfect, and `will` inside a time clause).
  Every one of the thirty items lands inside one of the three.
- **Four of six multiple-choice keys were the longest option**, because the
  answer was always the longest tense name. Each question gains a fourth option
  at least as long as the key, and each of those is a real error: `would have
  been exploring` is the mixed-conditional slip, `has been building` the
  present-for-past slip. See `tensereview_data.py`.
- **One error-correction item had no error in it** while the rubric promised
  one. Replaced with a genuine Past Perfect Continuous failure.
- **The true/false section is a sort.** Five claims into two bins, which is what
  a true/false question is, and it stops five items from being worth a coin
  flip each.

Artwork: `TenseReview/`, five flat-vector scenes from Innes's Downloads in one
family — cream skies, dusty pink mesas, a blocky figure and a bicycle. The
palette is `extract-palette.py --light`, because the artwork is pale and a dark
chrome sat on it badly; it also keeps this deck visibly apart from Past Modals,
which is the other Minecraft deck and is dark. Every token is tool output
unedited, `--void` included: on a light theme the derived canvas is already a
warm sand rather than the near-black that Innes asked to have lifted.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from tensereview_data import MC, FIB, SORT, SORT_BINS, MATCH, EC

TPL = 'lesson-template/lesson-template.html'
OUT = 'tense-review-minecraft.html'
F = 'TenseReview'

# python3 lesson-template/extract-palette.py TenseReview/hero.jpg --light
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8c6ac;
  --surface       : #e1d5c4;
  --surface2      : #dccdb8;
  --border        : #96594a;
  --text          : #2a1611;
  --text-dim      : #5e372e;
  --accent        : #b22909;
  --accent-bright : #881a00;
  --accent-dim    : #e76b4e;
  --secondary     : #bdd7df;
  --contrast      : #08543e;''' % F

CHIPS = ['had already', 'have been -ing', 'by the time', 'while I was',
         'since then', 'will have been', 'as soon as', 'it turned out that']

MC_BG = ['mesa.jpg', 'deep.jpg', 'coast.jpg', 'pig.jpg', 'mesa.jpg', 'coast.jpg']
FIB_BG = ['coast.jpg', 'pig.jpg', 'mesa.jpg', 'deep.jpg']
EC_BG = ['pig.jpg', 'mesa.jpg', 'coast.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'TenseReview')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Tenses in the <em>Overworld</em>',
                'Twelve tenses, thirty questions, and the three decisions that pick '
                'between them',
                [('Level', 'B2 &middot; Upper-intermediate'),
                 ('Focus', 'The twelve tenses'),
                 ('Count', '21 slides')])

        + D.teach('axEyebrow', 'Before the questions',
                  'axTitle', 'Three questions choose the tense',
                  [('ax1h', 'When?', 'ax1b',
                    'Past, present or future. This picks the auxiliary and nothing '
                    'else: <em>was</em>, <em>is</em>, <em>will be</em>. Every one of '
                    'the twelve tenses answers this first.',
                    'ax1n', 'Get this wrong and no amount of aspect will rescue the '
                            'sentence.'),
                   ('ax2h', 'Finished, or still running?', 'ax2b',
                    'The simple form reports a whole event: <em>he built the '
                    'portal</em>. The continuous shows it in progress and unfinished '
                    'at that moment: <em>he was building the portal</em>.',
                    'ax2n', 'This is why an interruption takes the continuous and the '
                            'interruption itself takes the simple.'),
                   ('ax3h', 'Finished before what?', 'ax3b',
                    'The perfect ties one time to another. <em>Had built</em> is '
                    'finished before a past point; <em>has built</em> before now; '
                    '<em>will have built</em> before a future point.',
                    'ax3n', 'Twelve tenses is three times two times two. Nothing else '
                            'is going on.')],
                  folder=F, bg='mesa.jpg')

        + D.teach('pcEyebrow', 'The family learners avoid',
                  'pcTitle', 'Perfect continuous: how long, up to when',
                  [('pc1h', 'What it adds', 'pc1b',
                    '<strong>Have been + -ing</strong> takes the perfect&rsquo;s link '
                    'between two times and asks how long the activity ran up to the '
                    'later one. <em>I have been mining all morning</em> counts the '
                    'morning.',
                    'pc1n', 'The simple perfect counts results; the continuous counts '
                            'duration.'),
                   ('pc2h', 'All three times', 'pc2b',
                    '<em>She <strong>has been</strong> crafting</em> (up to now), '
                    '<em>he <strong>had been</strong> carrying it</em> (up to a past '
                    'moment), <em>I <strong>will have been</strong> working nine '
                    'hours</em> (up to a future moment).',
                    'pc2n', 'The auxiliary changes; <em>been + -ing</em> never does.'),
                   ('pc3h', 'The tell in the sentence', 'pc3b',
                    'A stretch of time (<em>for three days</em>, <em>all morning</em>, '
                    '<em>for nine hours</em>) next to a boundary (<em>by the '
                    'time&hellip;</em>, <em>since&hellip;</em>) is asking for a perfect '
                    'continuous.',
                    'pc3n', 'No duration in the sentence? Then the simple perfect is '
                            'almost always right.')],
                  folder=F, bg='coast.jpg')

        + D.teach('trEyebrow', 'The two traps',
                  'trTitle', 'Where B2 loses the marks',
                  [('tr1h', 'Finished time blocks the present perfect', 'tr1b',
                    '<em>Last year</em>, <em>in 2011</em>, <em>yesterday</em> close the '
                    'time off, and the present perfect needs it open. <em>I have '
                    'visited the End last year</em> is not English &mdash; it is <em>I '
                    'visited</em>.',
                    'tr1n', '<em>At the time of writing</em> and <em>since 1.16</em> '
                            'keep it open, so those take the perfect.'),
                   ('tr2h', 'Time clauses do not take <em>will</em>', 'tr2b',
                    'After <em>when</em>, <em>by the time</em>, <em>as soon as</em>, '
                    '<em>until</em>, English uses a present form for future meaning: '
                    '<em>when the player <strong>enters</strong> the Deep '
                    'Dark&hellip;</em>',
                    'tr2n', 'The main clause still takes <em>will</em>. Only the time '
                            'clause drops it.'),
                   ('tr3h', '<em>While</em> wants something in progress', 'tr3b',
                    '<em>While</em> and <em>as</em> set up a background action, so they '
                    'take a continuous form. The thing that cuts across it &mdash; the '
                    'Creeper, the Ghast &mdash; is a single event and takes the simple.',
                    'tr3n', '<em>While the Wither has destroyed</em> fails on this; it '
                            'wants <em>was destroying</em>.')],
                  folder=F, bg='pig.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'Choose the form that fits',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 4, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The live commentary',
                        'fibTitle', 'Complete the streamer&rsquo;s sentence',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='The tense and the verb are given. Contractions are '
                             'accepted.',
                        width=185, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:6], FIB[6:]]))

        + D.sort_slide(SORT_BINS, SORT, 'sortEyebrow', 'Activity 3 &middot; Judgement',
                       'sortTitle', 'Is the sentence sound, or is the tense wrong?',
                       'sortHint', 'Click a sentence to place it, click a placed '
                                   'sentence to take it back.',
                       'sortWhy', folder=F, bg='deep.jpg')

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; The register',
                  'matchTitle', 'Match the term to what it means',
                  'matchHint', 'Click a term, then click its meaning.',
                  'matchWhy', folder=F, bg='mesa.jpg')

        + "".join(D.gap(n + 1, 3, part, None,
                        'ecEyebrow', 'Activity 5 &middot; Repair the sentence',
                        'ecTitle', 'One wrong form in each',
                        folder=F, bg=EC_BG[n], hint_key='ecHint',
                        hint='Type the corrected verb only, exactly as it should '
                             'appear.',
                        width=185, size=17)
                  for n, part in enumerate([EC[:2], EC[2:4], EC[4:]]))

        + D.results('resNext', 'You can pick the tense. Now tell the story &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Narrate the run', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is the streamer recapping the session, the other is a '
                     'viewer who joined late and needs the story in order. Four minutes '
                     'each, then swap.',
                     ['Recap the last hour of a game to someone who missed it. Say what '
                      'had already happened before they arrived.',
                      'Describe something you have been doing for weeks and still have '
                      'not finished.',
                      'Predict where your build will be by the end of the month, and '
                      'say how long you will have been working on it.',
                      'Tell the story of something that went wrong while you were doing '
                      'something else.'],
                     'Writing &middot; 180&ndash;220 words',
                     'Write the day-47 update post for a hardcore survival series. '
                     'Cover what you had done before the session, what you have been '
                     'working on since, what went wrong while you were away from base, '
                     'and what you will have finished by day 50. Use at least six '
                     'different tenses and make each one earn its place.',
                     'Day 47. Before I logged off last night I had already&hellip;',
                     folder=F, bg='coast.jpg')
    )

    import i18n_tensereview as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Tense Review — Minecraft Edition (B2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d sort, %d pairs, %d repairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(SORT),
             len(MATCH), len(EC), len(s)))


if __name__ == '__main__':
    build()
