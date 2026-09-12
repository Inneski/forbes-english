# -*- coding: utf-8 -*-
"""IELTS Speaking Part 3 — the discussion (C1), built as a 16:9 deck.

The second of the two lessons `ielts-speaking.html` had been promising from a
disabled card. There was no source page to rebuild: the hero copy on the route
said "Part 3 is the abstract discussion and it needs the other two working
before it is worth attempting. It is next in the route," and behind that
sentence was nothing at all. This is the lesson it was promising.

It teaches the three moves that make Part 3 a different test from Part 1,
rather than the same test with harder topics:

  1. **The person changes.** Part 1 asks about your kitchen; Part 3 asks why
     fewer people cook. An answer that is still about you has answered the
     wrong question, however fluent it is.
  2. **The examiner is trained to disagree**, whatever you say — so pushback
     is the task rather than a verdict, and the skill is conceding what is
     fair while keeping the rest.
  3. **Certainty is graded once, on purpose.** Hedging is Lexical Resource,
     not filler; hedging every clause reads as evasion and leaves no position
     on the table at all.

Six pictures, one per section, none shared with Part 1 &amp; 2: the room from a
wider angle for the cover, a window onto a skyline for the move from the
personal to the general, two chairs set at an angle for the pushback, an
unmarked dial for degrees of certainty, five doors for the question run, and
the room with a clock for the activation stage. The palette derives from the
hero and lands close to the route's existing one, which is what keeps the two
decks reading as one course while sharing no image.

Spanish and German both ship complete. Note for whoever picks up the route:
`forbes-english-ielts-speaking-part1-2.html` is hand-written HTML with no
builder anywhere in the repo, and it still carries `es:{}` — English and German
only, against the standing minimum. It is recorded in docs/HANDOFF.md.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
from ieltsp3_data import GENERAL, PUSHBACK, HEDGE, ALL, ORDER, ORDER_WHY

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-ielts-speaking-part3.html'
F = 'ielts-speaking-part3'

# python3 lesson-template/extract-palette.py ielts-speaking-part3/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0a0f0e;
  --surface       : #141d1a;
  --surface2      : #1c2925;
  --border        : #a06851;
  --text          : #f5f3f2;
  --text-dim      : #bfaba3;
  --accent        : #e09677;
  --accent-bright : #f0c2ae;
  --accent-dim    : #c66035;
  --secondary     : #151e1b;
  --contrast      : #1dedc6;''' % F

# The target language, and the chips on the activation stage. English in every
# gloss: these are the phrases the learner has to produce in the room.
CHIPS = ['tend to', 'on the whole', 'by and large', 'a case in point',
         'true up to a point', 'it is often argued', 'broadly speaking',
         'on reflection']

# One picture per section (HOUSE-STYLE §5b), and its own for the activation
# stage. bg05 — five closed doors with one ajar — sits behind the ordering
# task because that slide is the one where the learner picks the way in.
BG_GENERAL, BG_PUSH, BG_HEDGE, BG_ORDER = ('bg02.jpg', 'bg03.jpg',
                                           'bg04.jpg', 'bg05.jpg')
BG_ACT = 'bg06.jpg'


def build():
    D.assert_no_key_is_longest(ALL, 'IELTSP3')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'IELTS Speaking <em>Part 3</em>',
                'The discussion: answering for people in general, and holding '
                'the line when the examiner disagrees',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Speaking Part 3'),
                 ('Count', '13 questions')])

        + D.teach('t1Eyebrow', 'Before you start',
                  't1Title', 'Part 1 asked about you. Part 3 asks about people.',
                  [('t1ah', 'The person changes', 't1ab',
                    'Part 1: &ldquo;Do you enjoy cooking?&rdquo; Part 3: '
                    '&ldquo;Why do fewer people cook at home now?&rdquo; The '
                    'second question is not about your kitchen. Answer for the '
                    'group.', 't1an',
                    'If the answer would still stand with you removed from it, '
                    'it is a Part 3 answer.'),
                   ('t1bh', 'Three phrases that generalise', 't1bb',
                    '<em>Tend to</em>, <em>on the whole</em>, <em>by and '
                    'large</em>. Each says &ldquo;this is what is usually '
                    'true&rdquo;, and each leaves room for the exceptions the '
                    'examiner is about to raise.', 't1bn',
                    '<em>Tend to</em> takes a plain verb: people <em>tend to '
                    'arrive</em> late, never <em>tend to arriving</em> late.'),
                   ('t1ch', 'Your own life still counts', 't1cb',
                    'One example, placed after the general claim, shows you '
                    'mean it. <em>A case in point is&hellip;</em> marks it as '
                    'an illustration rather than as the whole answer.', 't1cn',
                    'One example is support. Three examples is a Part 1 answer '
                    'that has run long.')],
                  folder=F, bg=BG_GENERAL)

        + "".join(D.mc(i + 1, len(GENERAL), q, 'mcaEyebrow',
                       'Activity 1 &middot; The general case', 'mcaTitle',
                       'Which answer is about people, not about you?',
                       folder=F, bg=BG_GENERAL, ctx=q.get('ctx'))
                  for i, q in enumerate(GENERAL))

        + D.teach('t2Eyebrow', 'Before you start',
                  't2Title',
                  'The examiner disagrees. That is the task, not a verdict.',
                  [('t2ah', 'Pushback is scripted', 't2ab',
                    'Examiners are trained to challenge in Part 3, whatever '
                    'you say. It is not a signal that the answer was weak '
                    '&mdash; it is the part of the test that finds out what '
                    'you can do under pressure.', 't2an',
                    'A well-made point often attracts more pushback, not less, '
                    'precisely because it is worth pushing.'),
                   ('t2bh', 'Concede, then qualify', 't2bb',
                    'Give the other side something true, then keep your '
                    'ground: <em>That is true up to a point, though&hellip;</em> '
                    'or <em>I would accept that for smaller towns, '
                    'but&hellip;</em>', 't2bn',
                    'The clause after the concession carries your position. '
                    'Stopping at the concession is how a point gets lost.'),
                   ('t2ch', 'Changing your mind is allowed', 't2cb',
                    'Say it aloud and it reads as thinking: <em>Actually, now '
                    'that I say it&hellip;</em> or <em>On reflection, I would '
                    'put that differently.</em>', 't2cn',
                    'A silent reversal confuses the listener. A signalled one '
                    'is coherence, and coherence is a quarter of the mark.')],
                  folder=F, bg=BG_PUSH)

        + "".join(D.mc(i + 1, len(PUSHBACK), q, 'mcbEyebrow',
                       'Activity 2 &middot; Under pressure', 'mcbTitle',
                       'The examiner has just disagreed', folder=F, bg=BG_PUSH,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(PUSHBACK))

        + D.teach('t3Eyebrow', 'Before you start',
                  't3Title', 'How sure are you? Say so once, and mean it.',
                  [('t3ah', 'Hedging is vocabulary', 't3ab',
                    '<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
                    'cases</em>. These are precise words doing a precise job, '
                    'and precision is what Lexical Resource measures.', 't3an',
                    'A hedge is not a filler. <em>Sort of</em> and <em>kind '
                    'of</em> are fillers &mdash; they grade nothing.'),
                   ('t3bh', 'Move the claim off yourself', 't3bb',
                    '<em>It is often argued that&hellip;</em> and <em>There is '
                    'a case for saying&hellip;</em> report a position without '
                    'signing your name to it, which leaves you free to take it '
                    'apart a sentence later.', 't3bn',
                    'Useful on a topic you know little about: you can run the '
                    'argument without claiming it.'),
                   ('t3ch', 'Hedge once, not everywhere', 't3cb',
                    'One graded claim reads as judgement. Four in a row reads '
                    'as evasion, and an answer carrying a hedge on every '
                    'clause has stopped saying anything at all.', 't3cn',
                    'Commit in the main clause, limit in the clause after it. '
                    'That is the shape.')],
                  folder=F, bg=BG_HEDGE)

        + "".join(D.mc(i + 1, len(HEDGE), q, 'mccEyebrow',
                       'Activity 3 &middot; Degrees of certainty', 'mccTitle',
                       'How sure, and how do you say it?', folder=F, bg=BG_HEDGE,
                       ctx=q.get('ctx'))
                  for i, q in enumerate(HEDGE))

        + D.order(ORDER, 'ordEyebrow', 'Activity 4 &middot; The shape of an answer',
                  'ordTitle', 'Put the four moves in order',
                  'ordHint', 'Drag them into order &mdash; or click one, then '
                             'the position you want it in.',
                  ORDER_WHY, folder=F, bg=BG_ORDER)

        + D.results('resNext', 'You can spot it. Now use it &rarr;', folder=F)

        + D.activate('Run a Part 3', 'Use at least three:', CHIPS,
                     'Discussion &middot; in pairs',
                     'One of you examines, one answers, and a phone holds '
                     'the clock. The examiner asks four questions on a '
                     'single topic and must disagree at least twice. Five '
                     'minutes, then swap.',
                     ['Candidate: answer for people in general first, and only '
                      'then give one example of your own.',
                      'Examiner: push back on the strongest thing you hear, '
                      'not the weakest. Ask whether it holds everywhere.',
                      'Candidate: concede what is fair, keep the rest, and '
                      'grade how sure you are exactly once.'],
                     'Writing &middot; 180&ndash;250 words',
                     'Write out your best answer to one of the four questions '
                     'you were asked, as you would want to have said it: '
                     'position, reason, one example, and the concession that '
                     'answers the pushback before it arrives.',
                     'On the whole, people…',
                     folder=F, bg=BG_ACT)
    )

    import i18n_ieltsp3 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'IELTS Speaking Part 3: The Discussion (C1) | Forbes English',
                   I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d questions, %d bytes'
          % (OUT, s.count('<section class="slide'), len(ALL) + 1, len(s)))


if __name__ == '__main__':
    build()
