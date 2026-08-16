# -*- coding: utf-8 -*-
"""Ordering Food & Drink (A1, Part 1) — built as a deck.

The source was a single scrolling page with three stacked activity blocks and
no teaching in front of them: six multiple-choice situations, an eight-blank
café dialogue, five sentences to reorder, then a score. Everything scored
survives. What changed:

  * **The answer key was in the HTML.** Every blank in the fill-in exercise
    carried its own answer as a literal argument on the element —
    `onclick="fillBlank('fib-1','table')"` — and the argument was not even
    used by the handler. View source, or hover a chip, and the exercise is
    over. The deck stores answers the way the template does, in `data-answer`,
    which the engine reads and compares; it is no more hidden, but it is not
    sitting on the element the learner is about to click either.

  * **Question 6 failed the length rule and taught bad grammar.** The key ran
    48 characters against a 33-character field — a learner who knows nothing
    can score it on shape alone — and it read *"I'm allergic to nuts. Is there
    any in this dish?"* `Nuts` is plural, so it is *are there any*. A grammar
    error inside the key of an A1 lesson is the worst place to have one: it is
    the sentence the learner is being told to copy. The key is rewritten to
    *"Does this dish have any?"*, which is correct, shorter, and what people
    actually say; the distractors were lengthened to close the gap. House
    rule, unchanged: lengthen the distractors, never shorten the key.

  * **No activation.** The page ended on a score. There is now a roleplay and
    a writing task, because a beginner who has recognised the right phrase
    four times out of six still cannot say any of them out loud.

  * **No teaching.** Two slides now state the three polite openings and the
    four words before anything is asked. At A1 the rules go on the wall first.

Light theme, on the standing instruction to keep backgrounds from going murky.
The artwork is a flat-illustration bar set: bright coral and mid blue, which
the light palette reads cleanly and a dark one would have muddied.
"""
import re, sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck
import i18n_food_a1 as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-food-ordering-a1-part1.html'
F = 'FoodA1P1'

# Derived by lesson-template/extract-palette.py FoodA1P1/two-at-bar.jpg --light.
# Every row of the contrast report passes; text on surface is 12.28:1.
PALETTE = '''  --hero: url('%s/two-at-bar.jpg');

  --void          : #d8cbac;
  --surface       : #e1d9c4;
  --surface2      : #dcd1b8;
  --border        : #96574a;
  --text          : #2a1511;
  --text-dim      : #5e362e;
  --accent        : #ab1d00;
  --accent-bright : #781400;
  --accent-dim    : #f05536;
  --secondary     : #446a86;
  --contrast      : #07553c;''' % F


# Three of the six pictures carry a dark band across the top — a chalkboard
# menu in one, a row of pendant lamps in two others. Measured behind the slide
# title with the text hidden, dark ink on that band came out at 2.57:1 against
# a 4.5 floor, on ten of the eighteen slides. Dropping --bg-opacity would have
# fixed it by bleaching all six pictures, which is the failure the light theme
# exists to avoid. Instead the template's top wash stop is raised for this
# lesson only, from 26% of --void to 88%, and the ramp is pulled down from 20%
# of the slide height to 26% so that it clears the title. The middle 54% is
# untouched: the artwork is still artwork where the artwork is.
HEAD_CSS = '''
/* see the builder docstring: top-band wash, this lesson only */
html[data-theme="light"] .stage:not(.on-cover) .bg-layer::after {
  background:
    linear-gradient(180deg,
      color-mix(in srgb, var(--void) 88%, transparent) 0%,
      color-mix(in srgb, var(--void) 80%, transparent) 11%,
      var(--wash-mid) 26%,
      var(--wash-mid) 80%,
      var(--wash-edge) 100%);
}

/* The blocks that sit on the bare illustration rather than inside a card —
   the question stems, the order hint and its drop zone, the word banks and
   the three lines of the results slide — measured 2.5 to 3.0:1 against dark
   ink, on a 4.5 floor. This artwork has hard black silhouettes in it, so a
   halo alone does not carry them. Same remedy as the Geoscience and Nature
   Agency light decks: give those blocks the card treatment, a translucent
   surface with a blur behind it, rather than washing the whole slide harder
   and losing the picture. HOUSE-STYLE §5. */
[data-type="mc"] .q-stem,
[data-type="order"] .order-hint,
[data-type="gap"] .act-target,
[data-type="activate"] .act-target,
[data-type="results"] .score-big,
[data-type="results"] #scoreMsg:not(:empty),
[data-type="results"] .prose.dim {
  background: color-mix(in srgb, var(--surface) 95%, transparent);
  backdrop-filter: blur(4px);
  border: 1px solid color-mix(in srgb, var(--border) 82%, transparent);
  border-radius: 14px;
  padding: 10px 18px;
}
[data-type="order"] .order-target {
  background: color-mix(in srgb, var(--surface) 82%, transparent);
  backdrop-filter: blur(3px);
}
/* A plate has to shrink to its text or it becomes a band across the slide —
   and an EMPTY plate is worse than none: #scoreMsg carries nothing until the
   results slide is reached, and an empty one rendered as a stray lozenge
   floating under the score. */
[data-type="results"] .score-big,
[data-type="results"] #scoreMsg,
[data-type="results"] .prose.dim { align-self: center; max-width: 74ch; }
[data-type="order"] .order-hint { align-self: flex-start; width: fit-content; }
'''

# ── the six situations ─────────────────────────────────────────────────
MC = [
    dict(
        stem='You have just sat down and you want something to read the dishes from. You say:',
        options=[
            'Where is the toilet, please?',
            'Can I see the menu, please?',
            'I don&rsquo;t want anything today.',
            'We are ready to pay now.',
        ],
        correct=1,
        why='<strong>Can I&hellip;?</strong> is the everyday polite request for one thing. The other three are all real sentences — they are simply about something else, which is the commonest way to be misunderstood at A1.',
    ),
    dict(
        stem='The waiter is at your table and you want to order a coffee. You say:',
        options=[
            'I am going to coffee now.',
            'Coffee is very good here.',
            'Do you drink coffee every day?',
            'I&rsquo;d like a coffee, please.',
        ],
        correct=3,
        why='<strong>I&rsquo;d like&hellip;</strong> is how you order. It is short for <em>I would like</em>, and it is softer than <em>I want</em> — which is correct English and still sounds like a demand in a café.',
    ),
    dict(
        stem='The waiter asks &ldquo;Are you ready to order?&rdquo; You have not chosen yet. You say:',
        options=[
            'Yes, I want a pizza now.',
            'Not yet, thank you. One moment.',
            'The food is very expensive here.',
            'My friend doesn&rsquo;t want any food.',
        ],
        correct=1,
        why='<strong>Not yet</strong> means &ldquo;no, but soon&rdquo;. With <em>thank you</em> after it, it buys you a minute and nobody is offended. Saying nothing at all is what makes the waiter stand there.',
    ),
    dict(
        stem='You have finished eating and you want to pay. You say:',
        options=[
            'I didn&rsquo;t like the food at all.',
            'Where can I find a taxi near here?',
            'Could we have the bill, please?',
            'Can you open a window for us, please?',
        ],
        correct=2,
        why='<strong>Could we have&hellip;?</strong> is the polite request for a table of two or more. In American English the bill is the <em>check</em> — <em>could we have the check, please?</em> — but the frame is identical.',
    ),
    dict(
        stem='The food is very good and you want to say so. You say:',
        options=[
            'It&rsquo;s delicious, thank you!',
            'I want a different table now.',
            'We are not here for dinner.',
            'This dish is cold and late too.',
        ],
        correct=0,
        why='<strong>Delicious</strong> means very tasty. It is one word and it does the whole job — you do not need a sentence about the food to compliment it.',
    ),
    dict(
        stem='You are allergic to nuts and you want to check a dish before you order it. You say:',
        options=[
            'I never eat anything at all in restaurants.',
            'Please bring me a large glass of cold milk.',
            'I&rsquo;m allergic to nuts. Does this dish have any?',
            'Can you recommend a dish made with nuts for me?',
        ],
        correct=2,
        why='<strong>I&rsquo;m allergic to&hellip;</strong> then a question about the dish. Say the allergy first: it is the part the kitchen needs. The preposition is fixed — allergic <em>to</em>, never <em>of</em> or <em>at</em>.',
    ),
]

# ── the café dialogue ──────────────────────────────────────────────────
# Answers in gap order. The bank is sorted, so it cannot be read straight
# down as a key — assert_bank_is_not_a_key checks that below.
GAP_A = [
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">Waiter</span>Good afternoon! Would you like a ______ for two?', ['table'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">You</span>Yes, please. Can we sit ______?', ['outside'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">Waiter</span>Of course. Here is your ______.', ['menu'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">You</span>Thank you. We&rsquo;d ______ a few minutes to choose.', ['like'], None),
]
WHY_A = ('A table is what you ask for at the door, and a table for two is the fixed phrase — not '
         'a table for two people. Sit outside takes nothing in front of outside. And we\'d like '
         'is simply I\'d like for more than one person: the same polite frame, all the way through.')

GAP_B = [
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">Waiter</span>Are you ______ to order?', ['ready'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">You</span>Yes! I&rsquo;d like the pasta and a glass of ______, please.', ['water'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">Waiter</span><em>(brings the food)</em> ______ your meal!', ['enjoy'], None),
    ('<span class="dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-right:10px">You</span>Thank you. Could we have the ______, please?', ['bill'], None),
]
WHY_B = ('Ready to order is fixed — the waiter will use those exact words. It is a glass of '
         'water, never a glass water. Enjoy your meal is what the waiter says as the food '
         'lands, and thank you is the whole reply. The bill is the paper you pay; in America '
         'it is the check.')

ANSWERS = [a for _, aa, _ in GAP_A + GAP_B for a in aa]
BANK = sorted(ANSWERS)

# ── the five sentences ─────────────────────────────────────────────────
ORDER = [
    (["I'd", 'like', 'the', 'soup,', 'please.'],
     'The order never moves: who wants it, then <em>like</em>, then the dish, then <em>please</em>. '
     'Fill the middle with anything on the menu and the sentence still works.'),
    (['Can', 'we', 'have', 'the', 'bill,', 'please?'],
     'A question with <em>can</em> puts <em>can</em> first: <strong>Can we have&hellip;?</strong>, not '
     '<em>We can have&hellip;?</em>. Everything after it stays in the order it would be in a statement.'),
    (['Is', 'there', 'a', 'table', 'for', 'two?'],
     '<em>There is a table</em> becomes <strong>Is there a table?</strong> — those two words swap places '
     'and nothing else moves. It is the question you ask at the door.'),
    (["I'm", 'allergic', 'to', 'dairy', 'products.'],
     'Allergic is always followed by <strong>to</strong>. Learn the two words as one: <em>allergic to</em>. '
     'This is the sentence worth being able to say without thinking.'),
    (['Does', 'this', 'dish', 'have', 'any', 'meat?'],
     'After <strong>does</strong> the verb goes back to its plain form: <em>does this dish have</em>, '
     'not <em>does this dish has</em>. <em>Any</em> is what you use in a question.'),
]


def numbered(html, n, total, key):
    """Give an order slide the same '3 / 5' counter the MC slides carry.

    deck.order() takes a plain eyebrow because most lessons use it once.
    Rather than change nine signatures for one lesson, the counter is
    spliced in after the fact — the translated span keeps its key and the
    digits sit outside it, exactly as deck.mc() builds them."""
    old = '<div class="eyebrow" data-i18n="%s">' % key
    new = '<div class="eyebrow"><span data-i18n="%s">' % key
    assert old in html, 'order eyebrow not found'
    head, tail = html.split(old, 1)
    text, rest = tail.split('</div>', 1)
    return '%s%s%s</span> &middot; %d / %d</div>%s' % (head, new, text, n, total, rest)


def build():
    deck.assert_no_key_is_longest(MC, 'FoodA1P1')
    pos = deck.assert_bank_is_not_a_key(BANK, ANSWERS)
    logo = deck.logo_from(TPL)

    slides = deck.cover(
        logo,
        'Ordering Food &amp; <em>Drink</em>',
        'Part one: getting a table, ordering it, and asking for the bill',
        [('Level', 'A1 · Part 1 of 2'),
         ('Focus', 'Café &amp; restaurant English'),
         ('Count', '18 slides')])

    slides += deck.teach(
        'askEyebrow', 'Before the questions',
        'askTitle', 'Three openings do almost all of the work',
        [(None, 'Can I&hellip;?', '&ldquo;Can I see the menu, please?&rdquo;', 'ask1',
          'For one thing, for yourself. <em>Please</em> is not optional in English — without it '
          'the same words sound like an order.'),
         (None, 'Could we&hellip;?', '&ldquo;Could we have the bill, please?&rdquo;', 'ask2',
          'The same request from two people or more. <em>Could</em> is a step politer than '
          '<em>can</em>, and works everywhere <em>can</em> does.'),
         (None, 'I&rsquo;d like&hellip;', '&ldquo;I&rsquo;d like a coffee, please.&rdquo;', 'ask3',
          'This is how you order. Short for <em>I would like</em>. <em>I want</em> is correct '
          'English and still sounds rude here.')],
        cols='1fr 1fr 1fr', folder=F, bg='bar-shaker.jpg')

    slides += deck.teach(
        'wordEyebrow', 'The words themselves',
        'wordTitle', 'Four you cannot get through a meal without',
        [(None, 'table &middot; menu &middot; bill',
          '&ldquo;A table for two.&rdquo; &ldquo;Here is your menu.&rdquo; &ldquo;Could we have the bill?&rdquo;',
          'word1',
          'A <em>table</em> is what you ask for at the door, the <em>menu</em> is what you read, '
          'the <em>bill</em> is what you pay. American menus say <em>check</em> for the bill.'),
         (None, 'ready to order', '&ldquo;Are you ready to order?&rdquo; &mdash; &ldquo;Not yet, thank you.&rdquo;',
          'word2',
          'The waiter&rsquo;s most common question. <em>Not yet</em> is the polite way to buy '
          'yourself another minute.'),
         (None, 'allergic to&hellip;', '&ldquo;I&rsquo;m allergic to nuts.&rdquo;', 'word3',
          'The preposition never changes: allergic <strong>to</strong>. Not <em>of</em>, not '
          '<em>at</em>. This is the one phrase on the slide worth learning perfectly.')],
        cols='1.3fr 1fr 1fr', folder=F, bg='drink-sign.jpg')

    mc_bg = [None, 'counter-till.jpg', None, 'wine-bar.jpg', None, 'tray.jpg']
    for n, q in enumerate(MC, 1):
        slides += deck.mc(n, len(MC), q, 'qEyebrow', 'In the café',
                          'qTitle', 'What do you say?', folder=F, bg=mc_bg[n - 1])

    slides += deck.gap(1, 2, GAP_A, BANK, 'gapEyebrow', 'A whole visit, in order',
                       'gapTitle', 'Complete the conversation', folder=F, bg='wine-bar.jpg',
                       hint='One word per gap. Every word in the bank is used exactly once '
                            'across the two screens.',
                       hint_key='gapHint', why=WHY_A, width=170, size=20)
    slides += deck.gap(2, 2, GAP_B, BANK, 'gapEyebrow', 'A whole visit, in order',
                       'gapTitle', 'Complete the conversation', folder=F, bg='counter-till.jpg',
                       hint='One word per gap. Every word in the bank is used exactly once '
                            'across the two screens.',
                       hint_key='gapHint', why=WHY_B, width=170, size=20)

    ord_bg = ['tray.jpg', None, 'drink-sign.jpg', None, 'bar-shaker.jpg']
    for n, (words, why) in enumerate(ORDER, 1):
        slides += numbered(
            deck.order(words, 'ordEyebrow', 'Say it in the right order',
                       'ordTitle', 'Build the sentence',
                       'ordHint', 'Click the words in order. Click a word you have placed '
                                  'to take it back.',
                       why, folder=F, bg=ord_bg[n - 1]),
            n, len(ORDER), 'ordEyebrow')

    slides += deck.results('resNext', 'Now say it out loud. That is the part that transfers →')

    slides += deck.activate(
        'Now order something', 'Use at least four:',
        ['Can I&hellip;?', 'Could we&hellip;?', 'I&rsquo;d like&hellip;',
         'a table for two', 'Not yet, thank you', 'It&rsquo;s delicious',
         'I&rsquo;m allergic to&hellip;'],
        'Roleplay · in pairs',
        'One waiter, one customer. Then swap over, and change the order the second time.',
        ['Arrive at the door. Ask for a table for two, and ask to sit outside.',
         'Ask for the menu. The waiter asks if you are ready — you are not. Buy a minute.',
         'Order one thing to eat and one thing to drink. Say <em>please</em> every time.',
         'Tell the waiter about an allergy, then ask for the bill.'],
        'Writing · 40–60 words',
        'Write out your conversation as a dialogue. The waiter speaks first.',
        'Waiter: Good afternoon! Do you have a reservation?')

    s = deck.assemble(TPL, OUT, slides, PALETTE,
                      'Ordering Food &amp; Drink — A1 Part 1', I,
                      langs=('en', 'de', 'es'))

    # Light theme: the palette alone gives light colours on a dark structure.
    # Both have to be set or the deck comes out with pale text on pale cards.
    s = s.replace('<html lang="en">', '<html lang="en" data-theme="light">', 1)
    assert 'data-theme="light"' in s, 'the light theme flag did not attach'
    s = s.replace('</style>\n</head>', HEAD_CSS + '</style>\n</head>', 1)
    assert 'top-band wash' in s, 'the head CSS did not attach'
    open(OUT, 'w', encoding='utf-8').write(s)

    print('wrote %s — %d sections, %d MC, %d gaps, %d sentences, bank positions %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(ANSWERS),
             len(ORDER), pos, len(s)))


if __name__ == '__main__':
    build()
