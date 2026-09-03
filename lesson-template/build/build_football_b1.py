# -*- coding: utf-8 -*-
"""Football Vocabulary (B1) — rebuilt as a 16:9 deck.

Replaces the scrolling page that survived the merge with the Argentina
edition. All fourteen scored items survive verbatim, and three defects in
the original did not:

1. **Every key was authored at index 0** — fourteen out of fourteen. The
   runtime shuffle hid it on screen and printed it straight through to PDF.
   Spread across the four positions in `football_b1_data.py`.

2. **The lesson taught nothing.** It was fourteen questions and a score;
   every rule appeared only in the feedback after you had already answered,
   so the vocabulary could only be learned by getting it wrong. Three
   teaching slides now open the deck — the people on the pitch, what stops
   and restarts play, and the words for how the match went — and between
   them they cover every term the questions test.

3. **The Spanish gloss had nowhere to live.** Each item carried one
   (`es: "Referee = arbitro"`) and a deck's `data-explain` takes a single
   string. Explanations are now UI_I18N keys, so the gloss reaches Spanish
   learners in the Spanish build and English learners see English.

Artwork was already in the repo: four flat-vector match scenes at
3376×1440, brought over from the Argentina edition, resized and re-encoded
into `FootballB1/`. The palette is the tool's `--light` output for
`FootballB1/hero.jpg`, unedited — the hero is bright and airy, which is
what §4a says the light theme is for, and every contrast row passes with
margin where the dark derivation left headings barely separated from body
text.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from football_b1_data import MC

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-football-b1.html'
F = 'FootballB1'

# python3 lesson-template/extract-palette.py FootballB1/hero.jpg --light
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8c8ac;
  --surface       : #e1d7c4;
  --surface2      : #dccfb8;
  --border        : #967a4a;
  --text          : #2a2111;
  --text-dim      : #5e4c2e;
  --accent        : #845300;
  --accent-bright : #644107;
  --accent-dim    : #ec9b12;
  --secondary     : #b4c2c3;
  --contrast      : #095e6d;''' % F

CHIPS = ['referee', 'offside', 'foul', 'throw-in', 'goal kick', 'corner',
         'clean sheet', 'substitution', 'extra time', 'own goal']

# the three interior backgrounds, cycled so no two neighbouring slides match
BGS = ['kickoff.jpg', 'run.jpg', 'sunset.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'FootballB1')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Football <em>English</em>',
                'Positions, fouls, set pieces and the words commentators actually use',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Match-day vocabulary'),
                 ('Count', '20 slides')])

        + D.teach('whoEyebrow', 'Before the questions',
                  'whoTitle', 'Who is who on the pitch',
                  [('who1h', 'The officials',
                    'who1b',
                    'The <strong>referee</strong> runs the match and blows the whistle. '
                    'The <strong>linesman</strong> (or assistant referee) watches the '
                    'lines and raises a flag for offside.',
                    'who1n', 'One referee, two linesmen. Only the referee can stop play.'),
                   ('who2h', 'The outfield',
                    'who2b',
                    'A <strong>defender</strong> stops attacks, a <strong>midfielder</strong> '
                    'links defence and attack, a <strong>winger</strong> plays wide, and a '
                    '<strong>striker</strong> plays furthest forward.',
                    'who2n', '<em>Forward</em> and <em>striker</em> overlap; the striker is '
                             'the one nearest goal.'),
                   ('who3h', 'The goal, and the bench',
                    'who3b',
                    'The <strong>goalkeeper</strong> is the only player allowed to use their '
                    'hands. The <strong>coach</strong> (or manager) picks the team and makes '
                    'the changes from the bench.',
                    'who3n', 'British commentary usually says <em>manager</em>; '
                             '<em>coach</em> is understood everywhere.')],
                  folder=F, bg='kickoff.jpg')

        + D.teach('stopEyebrow', 'The whistle',
                  'stopTitle', 'What stops play, and what restarts it',
                  [('st1h', 'Stopped for an offence',
                    'st1b',
                    'A <strong>foul</strong> is an illegal action on an opponent. A '
                    '<strong>yellow card</strong> is a warning; a <strong>red card</strong> '
                    'sends the player off for good.',
                    'st1n', 'Two yellows in one match make a red. The team plays on with ten.'),
                   ('st2h', 'Stopped for offside',
                    'st2b',
                    'A player is <strong>offside</strong> if they are nearer the '
                    'opponents&rsquo; goal line than both the ball and the second-last '
                    'defender when the ball is played to them.',
                    'st2n', 'Offside is a position, not an action &mdash; you are '
                            '<em>in</em> an offside position.'),
                   ('st3h', 'Restarting play',
                    'st3b',
                    'Over the touchline &rarr; <strong>throw-in</strong>. Over the goal line '
                    'off an attacker &rarr; <strong>goal kick</strong>. Off a defender &rarr; '
                    '<strong>corner</strong>. A foul in the box &rarr; <strong>penalty</strong>.',
                    'st3n', 'Which restart you get depends on who touched it last, not on '
                            'who was fouled.')],
                  folder=F, bg='run.jpg')

        + D.teach('matchEyebrow', 'After the whistle',
                  'matchTitle', 'Words for how the match went',
                  [('mt1h', 'Nothing conceded',
                    'mt1b',
                    'A <strong>clean sheet</strong> is a match in which your team let in no '
                    'goals. It is credit to the goalkeeper and the defence together.',
                    'mt1n', 'You <em>keep</em> a clean sheet. You do not <em>make</em> or '
                            '<em>do</em> one.'),
                   ('mt2h', 'Still level',
                    'mt2b',
                    'If the score is <strong>level</strong> after ninety minutes, a knockout '
                    'match goes to <strong>extra time</strong> &mdash; two halves of fifteen '
                    'minutes.',
                    'mt2n', '<em>Injury time</em> is different: minutes added to the end of '
                            'a normal half.'),
                   ('mt3h', 'Changes and mistakes',
                    'mt3b',
                    'A <strong>substitution</strong> replaces a player from the bench. An '
                    '<strong>own goal</strong> is one you accidentally put into your own net.',
                    'mt3n', 'An own goal still counts &mdash; for the other team.')],
                  folder=F, bg='sunset.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Match report',
                       'qTitle', 'Choose the word that fits',
                       folder=F, bg=BGS[i % len(BGS)])
                  for i, q in enumerate(MC))

        + D.results('resNext', 'You can follow the match. Now call it &rarr;',
                    folder=F, bg='sunset.jpg')

        + D.activate('Commentate on the match', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you commentates, the other is the pundit who disagrees. '
                     'Ninety seconds each, then swap.',
                     ['Describe the goal that opened the scoring &mdash; who had the ball, '
                      'what they did, where it went in.',
                      'The referee has given a penalty. Argue that it was the right '
                      'decision; your partner argues it was not.',
                      'Your team is 1&ndash;0 up with ten minutes left. Tell the coach which '
                      'substitution to make, and why.',
                      'Sum the match up in thirty seconds without naming the score.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write a short match report for a club website. Say how the goals came, '
                     'name one player who changed the game, and end with what the result '
                     'means for the table.',
                     'It finished 2&ndash;1 at a wet Estadio Municipal, and&hellip;',
                     folder=F, bg='kickoff.jpg')
    )

    import i18n_football_b1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Football Vocabulary (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(s)))


if __name__ == '__main__':
    build()
