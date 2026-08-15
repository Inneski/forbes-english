# -*- coding: utf-8 -*-
"""The Language of Self-Improvement (B1) — rebuilt as a deck.

Everything survives: the TED talk, the reading, the eight vocabulary items,
six comprehension questions, eight gaps and the four discussion prompts.

Five defects were fixed rather than carried over.

**The key was the longest option in five of the six questions.** At B1 that is
the whole test: a learner scores five out of six by picking the longest and
learns nothing. Every distractor was lengthened to match.

**Two questions could not be answered from the lesson.** Q4 quoted "months
flying by forgotten" and Q6 attributed the word *sustainable* to Matt Cutts,
but the page carried no transcript and the video opened in another tab. The
deck now summarises the talk's argument on its own slide, so those items are
answerable from what the learner has in front of them.

**One question was verbatim recall.** Q3 asked what a growth mindset is in
almost exactly the words the reading used, and the same sentence appeared
again in the gap fill. It now asks the learner to apply the idea instead.

**The gap fill gave no explanations** — unlike the quiz on the same page — and
revealed the answer only for gaps left empty, so a learner who filled one
wrongly was never told what it should have been. Every gap now explains
itself, and the engine reveals the answer either way.

**And the two activities never combined.** The quiz was out of six, the gap
fill out of eight, and nothing added them up. The deck counts every scored
element once.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson_self-improvement (self).html'
F = 'SelfImprovement'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0a0d0a;
  --surface       : #141914;
  --surface2      : #1e251e;
  --border        : #ae614f;
  --text          : #f5f2f2;
  --text-dim      : #bfa9a3;
  --accent        : #e6917d;
  --accent-bright : #f5ad9c;
  --accent-dim    : #d15436;
  --secondary     : #334759;
  --contrast      : #1dedb0;''' % F

MC = [
    dict(stem='In the TED Talk, what does Matt Cutts suggest that people should do?',
         options=['Try something new every day for thirty days',
                  'Work considerably harder at their job every day',
                  'Try something new every single hour of the day',
                  'Watch a good deal less television every week'],
         correct=0,
         why='Think of something you have always wanted to try, and do it for the next <strong>30 days</strong>. He argues that thirty days is long enough to build a habit and short enough to finish.'),
    dict(stem='According to the reading, what is the <em>1% rule</em>?',
         options=['Getting 1% better each day, which adds up over a year',
                  'Working about 1% harder than everyone else does',
                  'Spending only 1% of your free time on social media',
                  'Saving roughly 1% of your salary every single month'],
         correct=0,
         why='One per cent a day compounds: after a year you are almost <strong>38 times</strong> better. The point is not the number &mdash; it is that small and daily beats large and occasional.'),
    dict(stem='Your friend fails a driving test and says &ldquo;I am just not a driver.&rdquo; What would a growth mindset sound like?',
         options=['&ldquo;I failed the hill start. I will practise that this week.&rdquo;',
                  '&ldquo;I have never been very good at practical things at all.&rdquo;',
                  '&ldquo;The examiner was extremely strict with me this morning.&rdquo;',
                  '&ldquo;I should probably stop and try again in a few years.&rdquo;'],
         correct=0,
         why='A <strong>growth mindset</strong> treats the mistake as information, not as a verdict on the person. Notice that the right answer names the <em>specific</em> thing to work on &mdash; that is what makes it useful.'),
    dict(stem='Why does Matt Cutts say the 30-day challenges made his life more memorable?',
         options=['He remembered exactly what he did on each of the days',
                  'He travelled to a great many new and unusual countries',
                  'He met a large number of famous and interesting people',
                  'He wrote a very successful book during the challenges'],
         correct=0,
         why='His phrase is that months stop <em>flying by forgotten</em>. Doing something deliberately each day makes the time countable, and therefore memorable.'),
    dict(stem='According to the reading, why do small, consistent actions beat one big effort?',
         options=['They turn into habits, so progress needs less willpower',
                  'They need no effort or willpower from you whatsoever',
                  'They are the only possible way to achieve a goal in life',
                  'They make you feel pleasantly overwhelmed and excited'],
         correct=0,
         why='A <strong>habit</strong> is something you do without deciding to. Once the action is automatic, you stop spending willpower on it &mdash; and willpower is the thing that runs out.'),
    dict(stem='What does <em>sustainable</em> mean when we talk about self-improvement?',
         options=['Able to continue for a long time without stopping',
                  'Very exciting and motivating right from the start',
                  'Possible to do perfectly and without any mistakes',
                  'Extremely difficult and requiring maximum effort'],
         correct=0,
         why='<strong>Sustainable</strong> is about duration, not intensity. A change you can keep up for a year beats one you can keep up for a fortnight, however impressive the fortnight looks.'),
]

GAPS = [
    ('It is easy to feel ______ when you have too many things to do at the same time.',
     ['overwhelmed'],
     '<strong>Overwhelmed</strong> = it feels too big to manage. Note that we <em>feel</em> overwhelmed &mdash; it describes you, not the task.'),
    ('Going to bed at the same time every night is a good ______ that helps you sleep better.',
     ['habit'],
     'A <strong>habit</strong> is something you do automatically, without deciding to each time. That is exactly why it saves willpower.'),
    ('People with a ______ believe that they can always learn and improve.',
     ['growth mindset'],
     'A <strong>growth mindset</strong> treats ability as something you build rather than something you were issued with.'),
    ('Learning a new skill requires ______ &mdash; especially when it feels difficult and boring.',
     ['willpower'],
     '<strong>Willpower</strong> is a limited resource, which is the argument for building habits instead of relying on it.'),
    ('To improve your English, you must be ______ and practise every single day.',
     ['consistent'],
     '<strong>Consistent</strong> means regularly and without stopping. Fifteen minutes daily beats four hours on a Sunday.'),
    ('Working with children is very ______ because you can see how much they learn.',
     ['fulfilling'],
     '<strong>Fulfilling</strong> = satisfying because it has meaning. Not the same as <em>enjoyable</em>: hard work is often more fulfilling than easy work.'),
    ('Small daily changes are more ______ than extreme diets or sudden challenges.',
     ['sustainable'],
     '<strong>Sustainable</strong> = you can keep it up. This is the sentence the whole lesson is arguing for.'),
    ('Understanding your own strengths and values is part of ______ too, not just achieving goals.',
     ['self-improvement'],
     '<strong>Self-improvement</strong> is not only about getting better at things &mdash; the reading ends on knowing yourself, which is the harder half.'),
]
BANK = sorted(['overwhelmed', 'habit', 'growth mindset', 'willpower', 'consistent',
               'fulfilling', 'sustainable', 'self-improvement',
               'personal development', 'motivation'])

MATCH = [
    ('consistent', 'Doing something regularly, without stopping'),
    ('overwhelmed', 'Feeling that something is too big to manage'),
    ('willpower', 'The ability to do a hard thing you do not feel like doing'),
    ('fulfilling', 'Satisfying, because it has meaning or purpose'),
    ('sustainable', 'Able to continue for a long time without stopping'),
    ('a habit', 'Something you do automatically, without thinking'),
]

CHIPS = ['a habit', 'consistent', 'willpower', 'overwhelmed', 'a growth mindset',
         'sustainable', 'fulfilling', 'the 1% rule']


def build():
    D.assert_no_key_is_longest(MC, 'Self-improvement')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    video = '''
    <section class="slide" data-type="teach">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="vidEyebrow">Before anything else</div>
        <h2 class="slide-title" data-i18n="vidTitle">Three and a half minutes, and then the argument</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1.1fr 1fr 1fr">
          <div class="card">
            <p class="prose"><strong>Try Something New for 30 Days</strong></p>
            <p class="prose dim" style="margin-top:6px;font-size:16px">Matt Cutts &middot; TED &middot; 3 min 27 s</p>
            <p class="prose" style="margin-top:10px;font-size:17px">
              <a href="https://www.youtube.com/watch?v=UNP03fDSj1U" target="_blank" rel="noopener"
                 style="color:var(--accent-bright)">youtube.com/watch?v=UNP03fDSj1U</a>
            </p>
            <p class="prose dim" style="margin-top:10px;font-size:15px" data-i18n="vidNote">Watch it first. The next three cards are what he argues, so you can check whether you heard the same thing.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="v1h">Thirty days is the unit</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px" data-i18n="v1b">Long enough for a habit to form, short enough that you can see the end from the start.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="v2h">Small beats dramatic</strong></p>
            <p class="prose" style="margin-top:8px;font-size:18px" data-i18n="v2b">The changes that <em>stick</em> are the sustainable ones. The dramatic ones come back off.</p>
          </div>
        </div>
        <div class="card" style="margin-top:14px">
          <p class="prose" style="font-size:18px"><strong data-i18n="v3h">And the part people miss:</strong>
            <span data-i18n="v3b">the months stopped &ldquo;flying by forgotten&rdquo;. Doing something deliberately each day made the time countable &mdash; and therefore memorable.</span></p>
        </div>
      </div>
    </section>
'''

    slides = (
        D.cover(logo, 'The Language of <em>Self-Improvement</em>',
                'Habits, mindset and the case for small steps &mdash; the words for talking about getting better',
                [('Level', 'B1 &middot; Intermediate'), ('Focus', 'Personal development'),
                 ('Count', '17 slides')])
        + video
        + D.teach('readEyebrow', 'From the reading',
                  'readTitle', 'Why small steps lead to big changes',
                  [('r1h', 'Start smaller than feels serious',
                    'Fifteen minutes of reading. One short walk.',
                    'r1b', 'People stall because the change they picture is too big to begin. The size of the first step is the only thing that decides whether there is a second one.'),
                   ('r2h', 'The 1% rule',
                    '1% better each day &rarr; <strong>38&times;</strong> better in a year.',
                    'r2b', 'The arithmetic is the argument. Small and daily compounds; large and occasional does not.'),
                   ('r3h', 'Build the habit, not the willpower',
                    'A habit is something you do without deciding to.',
                    'r3b', 'Willpower runs out. A habit does not need any, which is why it outlasts motivation.')],
                  folder=F)
        + D.teach('mindEyebrow', 'The other half of it',
                  'mindTitle', 'Mindset, and knowing yourself',
                  [('m1h', 'A growth mindset',
                    'Your abilities are <em>not fixed</em>. You can always learn.',
                    'm1b', 'The practical test: after a failure, do you name a thing to practise, or a fact about yourself?'),
                   ('m2h', 'Mistakes are information',
                    'Not a verdict &mdash; an instruction about what to do next.',
                    'm2b', 'People with a growth mindset see a mistake as a reason to change the method, not a reason to stop.'),
                   ('m3h', 'It is not only about goals',
                    'Knowing your strengths, weaknesses and values.',
                    'm3b', 'The reading ends here, and it is the harder half: once you know who you are, the choices get easier to make.')],
                  folder=F)
        + D.match(MATCH, 'matchEyebrow', 'Eight words, six of them here',
                  'matchTitle', 'Match the word to what it means',
                  'matchHint', 'Click a word, then click its meaning.',
                  'Two of these are worth separating carefully: fulfilling is not the same as enjoyable — hard work is often more fulfilling than easy work — and sustainable is about how long you can keep something up, not how impressive it looks.',
                  folder=F)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Video and reading',
                       'qTitle', 'What did it actually say?', folder=F)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 3, part, BANK, 'gapEyebrow', 'The right word',
                        'gapTitle', 'Complete the sentence', folder=F,
                        hint_key='gapHint',
                        hint='Two of the ten words in the bank belong to no gap here.',
                        width=200, size=18)
                  for n, part in enumerate([GAPS[:3], GAPS[3:6], GAPS[6:]]))
        + D.results('resNext', 'You have the words. Now say something true with them →')
        + D.activate('Thirty days from now', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs',
                     'Speak for at least a minute on each. Short answers do not count.',
                     ['Name a good habit you already have. How did it start &mdash; deliberately, or by accident?',
                      'Describe a time you felt overwhelmed. What did you actually do about it?',
                      'Do you agree that small changes beat big ones? Give one example from your own life.',
                      'Some people say always try to improve; others say accept yourself. Can both be true?'],
                     'Writing &middot; 120&ndash;160 words',
                     'Choose your own 30-day challenge and write the plan: what, when, how you will know it worked.',
                     'For the next thirty days I am going to…')
    )

    import i18n_self as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'The Language of Self-Improvement — B1', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             pos, len(s)))


if __name__ == '__main__':
    build()
