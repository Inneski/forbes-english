# -*- coding: utf-8 -*-
"""The Language of Flow (B2) — rebuilt as a deck.

The source was a four-part scrolling page: watch a TED-Ed talk, click eight
vocabulary cards to reveal their definitions, answer five questions, read four
discussion prompts. Everything survives. What changed:

  * **The five keys sat at positions [1, 2, 2, 1, 2].** Never A, never D. A
    learner who knows nothing and always picks B or C scores well above chance
    on every single question, and at B2 they are quite capable of noticing.
    Rebalanced to [2, 3, 0, 1, 3] — all four positions used, none starved.

  * **Two keys were the longest option by a wide margin.** Q2's key ran 23
    characters against a 14-character field (the other three psychologists had
    short names), and Q5's 57 against 49. Both are answerable on shape alone.
    Q2's distractors are now three real psychologists with names of comparable
    length; Q5's were lengthened. House rule: lengthen the distractors, never
    shorten the key.

  * **The vocabulary was click-to-reveal, which scores nothing.** Eight terms
    that the learner could flip over and feel they had learned. They are now
    taught on two slides, matched against plain-English glosses, and then used
    in eight gap-fill sentences that are marked.

  * **The discussion prompts were the end of the page.** They are now the
    activation stage proper — four speaking prompts with a term bank, plus the
    writing task, so the terms have to be produced rather than recognised.

Dark palette. The hero is a retro-terminal desert with a bright teal sky and
a pink brain cloud; the light palette derives a dusty pink surface that fights
it, while the dark one picks up the black frame and the gold HUD. Backgrounds
measured after building rather than assumed.
"""
import re, sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck
import i18n_flow as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson (flow).html'
F = 'FlowState'
VIDEO = 'https://www.youtube.com/watch?v=0rIjFCNay2Q'

# Derived by lesson-template/extract-palette.py FlowState/flow-hero.jpg.
# Every row of the contrast report passes; text on surface is 15.61:1.
PALETTE = '''  --hero: url('%s/flow-hero.jpg');

  --void          : #0e0e09;
  --surface       : #1c1c12;
  --surface2      : #29291a;
  --border        : #ad8c36;
  --text          : #f5f4f2;
  --text-dim      : #bfb8a3;
  --accent        : #efc65a;
  --accent-bright : #ffbe12;
  --accent-dim    : #d2a01b;
  --secondary     : #8cc4c6;
  --contrast      : #1dbaed;''' % F


# ── the eight terms ────────────────────────────────────────────────────
TERMS_STATE = [
    ('flow state', 'noun phrase',
     'Complete absorption in an activity, with energised focus and effort that stops feeling like effort.'),
    ('immersion', 'noun',
     'Being so far inside a task that nothing outside it registers.'),
    ('temporal distortion', 'noun phrase',
     'Losing your sense of how much time has passed — the most reported sign of flow.'),
    ('neurological', 'adjective',
     'Relating to the brain and nervous system. Flow has a measurable neurological signature, not just a felt one.'),
]
TERMS_COND = [
    ('optimal challenge', 'noun phrase',
     'Hard enough to hold your whole skill, not so hard it tips into anxiety.'),
    ('intrinsic motivation', 'noun phrase',
     'Doing it because the doing is the reward, rather than for money or praise.'),
    ('cognitive load', 'noun phrase',
     'How much your working memory is carrying at this moment.'),
    ('productivity', 'noun',
     'How much meaningful work gets finished in a given stretch of time.'),
]

MATCH = [
    ('flow state', 'Absorbed to the point where effort stops feeling like effort'),
    ('cognitive load', 'How much your working memory is carrying right now'),
    ('optimal challenge', 'Hard enough to hold you, not hard enough to panic you'),
    ('temporal distortion', 'Losing your sense of how much time has passed'),
    ('intrinsic motivation', 'Doing it because the doing is the reward'),
    ('immersion', 'So far inside something that nothing outside registers'),
]

# ── the terms in use ──────────────────────────────────────────────────
# The explanation sits on the slide, not on each row. Four rows each carrying
# their own feedback paragraph reserve 46px apiece whether or not anyone has
# pressed Check, which pushed both of these slides 51px past the canvas. One
# pooled note per screen is also how build_food_a1 does it, and it reads
# better: the four traps here are variations on one point about form.
GAP_A = [
    ('Three hours vanished while she was editing. That ______ is the most '
     'commonly reported sign of flow.', ['temporal distortion'], None),
    ('He keeps at the problem long after the bonus stops mattering — that is '
     '______.', ['intrinsic motivation'], None),
    ('A task at the very edge of what you can do, but not past it, is an '
     '______.', ['optimal challenge'], None),
    ('Twelve open tabs raise your ______ until nothing gets full attention.',
     ['cognitive load'], None),
]
WHY_A = ('<strong>Temporal distortion</strong> is fixed as a phrase — not <em>time '
         'distortion</em> in academic writing. <strong>Intrinsic</strong> means coming '
         'from inside; its opposite, <em>extrinsic motivation</em>, is the money and the '
         'praise. Note the article in <strong>an optimal challenge</strong>, and note '
         'that <em>optimal</em> means best for the purpose, not simply <em>maximum</em>. '
         '<strong>Cognitive load</strong> is uncountable — <em>a high cognitive load</em>, '
         'never <em>cognitive loads</em>.')
GAP_B = [
    ('Flow has a ______ basis: real changes in the brain&rsquo;s chemistry and networks.',
     ['neurological'], None),
    ('Total ______ in the task leaves no attention spare for anything else.',
     ['immersion'], None),
    ('Athletes tend to call the ______ &ldquo;being in the zone&rdquo;.',
     ['flow state'], None),
    ('Four uninterrupted hours can beat a whole fragmented day for ______.',
     ['productivity'], None),
]
WHY_B = ('The adjective is <strong>neurological</strong>; the field is <em>neurology</em> '
         'and the specialist a <em>neurologist</em>. You are <strong>immersed in</strong> '
         'something — the preposition is always <em>in</em>. <strong>Flow state</strong> is '
         'two words as a noun; hyphenate only in front of another noun, as in '
         '<em>flow-state research</em>. <strong>Productivity</strong> is uncountable, and '
         'it measures output against time rather than effort or hours worked.')
ANSWERS = [a for _, aa, _ in GAP_A + GAP_B for a in aa]
BANK = sorted(ANSWERS)

# ── comprehension ─────────────────────────────────────────────────────
MC = [
    dict(
        stem='What has to be true of the relationship between challenge and skill for flow to occur?',
        options=[
            'Skill must comfortably exceed the challenge',
            'The challenge must greatly exceed the skill',
            'Challenge and skill must be roughly equal',
            'Skill level is largely irrelevant to flow',
        ],
        correct=2,
        why='Flow sits at the balance point. Below it the task bores you, above it the task frightens you; the band where the two are matched is narrow, which is why flow is hard to schedule.',
    ),
    dict(
        stem='Which psychologist named the concept and spent a career researching it?',
        options=[
            'Wilhelm Maximilian Wundt',
            'Urie Bronfenbrenner',
            'Elizabeth K&uuml;bler-Ross',
            'Mihaly Csikszentmihalyi',
        ],
        correct=3,
        why='<strong>Csikszentmihalyi</strong> coined <em>flow</em> and built the research programme behind it. The other three are real figures from other fields — development, perception and grief.',
    ),
    dict(
        stem='What typically happens to your sense of time in a flow state?',
        options=[
            'It distorts, and we lose track of it',
            'It slows down quite considerably',
            'It stays exactly as it always was',
            'We become aware of every second',
        ],
        correct=0,
        why='This is <strong>temporal distortion</strong>. Note that it is not simply <em>slowing</em> — people report both directions, and the reliable part is the loss of track, not which way it runs.',
    ),
    dict(
        stem='Which condition is most consistently found to help someone enter flow?',
        options=[
            'Multitasking across several projects at once',
            'Having clear goals and immediate feedback',
            'Working in a noisy, stimulating environment',
            'Setting very easy, quickly achievable targets',
        ],
        correct=1,
        why='Clear goals and immediate feedback are the two conditions the research keeps returning to. Both remove ambiguity, and ambiguity is what pulls attention back out of the task.',
    ),
    dict(
        stem='Which of these best describes <em>intrinsic motivation</em>?',
        options=[
            'Being paid well for finishing the task on time',
            'Being motivated by external praise or recognition',
            'Being told by others that you are talented at it',
            'Being driven by enjoyment of the activity itself',
        ],
        correct=3,
        why='The activity is the reward. Curiosity and the pleasure of getting better carry the person — which is why intrinsic motivation survives the removal of the bonus and extrinsic motivation does not.',
    ),
]


def term_cards(terms):
    """No data-i18n on any of it. The term, its part of speech and its gloss
    are the lesson — they stay in English on every setting, so giving them
    translation keys would only create eight keys no language will ever fill."""
    return [(None, t, '<span class="dim" style="font-size:14px;letter-spacing:.06em;'
             'text-transform:uppercase">%s</span>' % pos, None, d)
            for t, pos, d in terms]


def video_slide():
    """The TED-Ed talk. No video slide type exists in the template and this
    lesson is the only one that needs one, so it is a teach slide with a real
    link rather than a ninth builder in deck.py."""
    return '''
    <section class="slide" data-type="teach" data-bg="%s/flow-bg-pattern.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="vidEyebrow">Part one</div>
        <h2 class="slide-title" data-i18n="vidTitle">Watch this first</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols" style="grid-template-columns:1.15fr 1fr">
          <div class="card">
            <p class="prose"><strong>TED-Ed &middot; How to Enter a Flow State</strong></p>
            <p class="prose" style="margin-top:10px;font-size:18px" data-i18n="vidBody">
              Four and a half minutes on what flow is and how the brain enters it. Watch it
              through before the vocabulary — the terms below all appear in it.
            </p>
            <div style="margin-top:18px">
              <a class="btn btn-solid" href="%s" target="_blank" rel="noopener"
                 data-i18n="btnOpen">Open ↗</a>
            </div>
            <p class="prose dim" style="margin-top:12px;font-size:14px" data-i18n="vidNote">
              Opens YouTube in a new tab.
            </p>
          </div>
          <div class="card" style="padding:0;overflow:hidden">
            <img src="https://img.youtube.com/vi/0rIjFCNay2Q/hqdefault.jpg"
                 alt="TED-Ed: How to Enter a Flow State"
                 style="width:100%%;height:100%%;object-fit:cover;display:block">
          </div>
        </div>
      </div>
    </section>
''' % (F, VIDEO)


def assert_keys_deranged(mc):
    """The defect this rebuild exists to fix, asserted so it cannot come back.

    The source used positions [1, 2, 2, 1, 2] — never A, never D. Guess B or C
    and you beat chance on every item. Require every position to appear."""
    pos = [q['correct'] for q in mc]
    missing = sorted(set(range(4)) - set(pos))
    assert not missing, ('the key never lands at position(s) %s: %s. A learner '
                         'who always guesses the used positions beats chance.'
                         % (missing, pos))
    return pos


def build():
    pos = assert_keys_deranged(MC)
    deck.assert_no_key_is_longest(MC, 'Flow')
    bankpos = deck.assert_bank_is_not_a_key(BANK, ANSWERS)
    logo = deck.logo_from(TPL)

    slides = deck.cover(
        logo, 'The Language of <em>Flow</em>',
        'Peak performance, deep focus, and the vocabulary to discuss both',
        [('Level', 'B2 · Psychology &amp; productivity'),
         ('Focus', 'Academic vocabulary'),
         ('Count', '15 slides')])

    slides += deck.teach(
        'shapeEyebrow', 'Before the vocabulary',
        'shapeTitle', 'Four conditions, and flow is the result',
        [(None, 'A matched challenge', '&ldquo;Hard, but not too hard.&rdquo;', 's1',
          'Not too easy, not too hard. Boredom sits on one side of that line and anxiety on '
          'the other; flow is the narrow band between them.'),
         (None, 'Clear goals, fast feedback', '&ldquo;Am I getting it right? Yes — keep going.&rdquo;', 's2',
          'You know what you are aiming at and you can see, moment to moment, whether it is '
          'working. Ambiguity is what breaks concentration.'),
         (None, 'The reward is the doing', '&ldquo;I would do this unpaid.&rdquo;', 's3',
          'The activity is its own reward. Anything you would still do with the payment '
          'removed is a candidate.'),
         (None, 'One thing at a time', '&ldquo;No notifications for two hours.&rdquo;', 's4',
          'One thing, uninterrupted. Every switch of attention costs more than the seconds it '
          'appears to take.')],
        cols='1fr 1fr 1fr 1fr', folder=F, bg='flow-bg-pattern.jpg')

    slides += video_slide()

    slides += deck.teach('termEyebrow', 'The eight terms',
                         'termTitleA', 'Four to describe the state',
                         term_cards(TERMS_STATE), cols='1fr 1fr 1fr 1fr', folder=F)
    slides += deck.teach('termEyebrow', 'The eight terms',
                         'termTitleB', 'Four to describe the conditions',
                         term_cards(TERMS_COND), cols='1fr 1fr 1fr 1fr',
                         folder=F, bg='flow-bg-pattern.jpg')

    slides += deck.match(
        MATCH, 'matchEyebrow', 'Say it in plain English',
        'matchTitle', 'Six terms and what they actually mean',
        'matchHint', 'Click a term, then click its meaning.',
        'Two of these are worth memorising whole. Optimal challenge is the condition you can '
        'actually engineer, and cognitive load is the one you can actually reduce — the other '
        'four describe what happens once you have.',
        folder=F)

    for n, rows, why in ((1, GAP_A, WHY_A), (2, GAP_B, WHY_B)):
        slides += deck.gap(n, 2, rows, BANK, 'gapEyebrow', 'The terms in use',
                           'gapTitle', 'Complete the sentence', folder=F,
                           bg='flow-bg-pattern.jpg' if n == 2 else None,
                           hint='One term per gap. Every term in the bank is used exactly '
                                'once across the two screens.',
                           hint_key='gapHint', why=why, width=210, size=19)

    mc_bg = [None, 'flow-bg-pattern.jpg', None, 'flow-bg-pattern.jpg', None]
    for n, q in enumerate(MC, 1):
        slides += deck.mc(n, len(MC), q, 'qEyebrow', 'Comprehension',
                          'qTitle', 'What does the research say?', folder=F, bg=mc_bg[n - 1])

    slides += deck.results('resNext', 'Now produce it. That is the part that transfers →')

    slides += deck.activate(
        'Now argue about it', 'Use at least four:',
        ['flow state', 'immersion', 'temporal distortion', 'neurological',
         'optimal challenge', 'intrinsic motivation', 'cognitive load', 'productivity'],
        'Discussion · in pairs',
        'In pairs or small groups. Take a position and defend it — one prompt each, three minutes apiece.',
        ['Describe a time you entered flow. What were the conditions? Use three of the terms.',
         'Notifications are said to be the enemy of flow. Redesign a working day to protect two uninterrupted hours.',
         '<em>Lost in the moment</em> is the informal version. Give three more English expressions for intense concentration.',
         'Struggle and discomfort have value too. To what extent should work feel like flow?'],
        'Writing · 150–200 words',
        'Take the prompt you did not speak on and answer it in writing. Use at least four of the eight terms.',
        'The clearest flow state I can remember was…')

    s = deck.assemble(TPL, OUT, slides, PALETTE,
                      'The Language of Flow — B2', I, langs=('en', 'de'))

    # The template ships --bg-opacity at 0.72, which suits a photographic hero.
    # This one is a flat illustration with large areas of saturated teal and
    # sand; at 0.72 the interior slides read as the picture with text on top
    # rather than a slide. Walked down with lesson-template/bgmeasure.py against
    # the brightest patterned slide (index 5, the video slide) until the body
    # copy cleared 7:1, then stopped at the highest value that does:
    #   0.46 -> 6.97  (fails)   0.44 -> 7.32   0.42 -> 7.68   0.40 -> 8.06
    # 0.44 keeps the most of the illustration that AAA-for-body-text allows.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.44;', 1)
    open(OUT, 'w', encoding='utf-8').write(s)

    print('wrote %s — %d sections, %d MC (keys at %s), %d gaps, %d pairs, '
          'bank positions %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), pos, len(ANSWERS),
             len(MATCH), bankpos, len(s)))


if __name__ == '__main__':
    build()
