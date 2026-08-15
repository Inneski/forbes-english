# -*- coding: utf-8 -*-
"""Out of This World — 5-Hour English Test Prep, PART II (Hours 4-5).

Second half of the rebuild. Hours 4 and 5: some/any, one/ones, reading
technique, guided writing, and the mock test.

Defects carried over from the old file and fixed here.

**The some/any rule was taught with no boundary, then tested on the
boundary.** The table said *any* for questions, and two items then asked
for "Have you got ___ apple juice?" — a request, where "Have you got
some apple juice?" is idiomatic native English. The rule as taught made
the natural answer wrong. There is now a slide on exactly this case, and
both answers are accepted where both are genuinely correct.

**One reading item was defensibly False and marked True.** "There was no
chicken at the restaurant" against a text saying there wasn't any chicken
*left* — a restaurant that has run out did have chicken. Restated so the
text supports one answer only.

**Mock Section 1 was a verbatim replay of Hour 1.** mt1 and mt2 were
word-for-word repeats of items whose answers the learner had already been
shown, with no word bank this time. Roughly eight of the twenty-seven
mock items were re-runs. Section 1 is rewritten on the same vocabulary
but new sentences, so it measures retention instead of recall of a
specific screen.

**Six mock items' entire feedback was the answer word.** `mt1: '<b>alien
</b>'` rendered as "✗ Not quite. **alien**" — an answer key printed in
the section meant to diagnose what the learner still cannot do.

**One explanation leaked an internal option key** — "The answer is (a)" —
on buttons that are never labelled (a) or (b) on screen, and quoted the
passage inaccurately while doing it.

**Thirteen of the twenty-seven mock items rendered outside their card**,
directly on the background, because a `<div class="card">` closed early.
The instruction line for the error-correction section was mid-grey on
dark navy and effectively unreadable. Structural, and gone with the
format.

**The model story did not meet its own brief.** Headed "~110 words", it
ran to 99 — below the 100-word minimum the same page sets as the target
— and never demonstrated *one/ones*, which its own checklist asks the
learner to verify. The model here is 112 words and is annotated: each
checklist item is marked where it happens.

**The grammar section could be answered without reading.** Two of its six
items paired a short present-simple form against a longer progressive
one, so the answer was the long option whenever the answer was
progressive. Gaps instead — the learner produces the form.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'exam-prep-5hour-course-part2.html'
F = 'ExamPrep'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #d8d6ac;
  --surface       : #e1e0c4;
  --surface2      : #dcdbb8;
  --border        : #964a64;
  --text          : #2a1119;
  --text-dim      : #5e2e3f;
  --accent        : #c0134e;
  --accent-bright : #9a0639;
  --accent-dim    : #e36b94;
  --secondary     : #255c5a;
  --contrast      : #075515;

  /* Same hero as Part I, same reason: a flat colour chart has no quiet
     area, so the pattern runs well below the house floor. */
  --bg-opacity    : 0.15;''' % F

COVER_CSS = (
    '.bg-layer::before { filter: saturate(0.28); }\n'
    '.slide[data-type="cover"] .cover-inner { position: relative; }\n'
    '.slide[data-type="cover"] .cover-inner > * { position: relative; z-index: 1; }\n'
    '.slide[data-type="cover"] .cover-inner::before {\n'
    '  content: ""; position: absolute; z-index: 0;\n'
    '  left: 50%; top: 50%; transform: translate(-50%, -50%);\n'
    '  width: 1010px; height: 500px; border-radius: 26px;\n'
    '  background: rgba(241,239,214,0.90);\n'
    '  box-shadow: 0 10px 60px rgba(0,0,0,0.28);\n'
    '}\n'
    '.slide[data-type="cover"] .cover-title,\n'
    '.slide[data-type="cover"] .cover-sub { text-shadow: none; }\n'
    '.slide[data-type="cover"] .chip {\n'
    '  background: #ffffff; border-color: var(--border); color: var(--text);\n'
    '}\n'
    '.stage.on-cover .deck-bar {\n'
    '  background: linear-gradient(180deg, transparent, rgba(241,239,214,0.92));\n'
    '}\n'
    '.deck-count, .deck-score { color: var(--text); }\n'
    '.eyebrow { color: var(--accent-bright); font-weight: 700; }\n'
    '.slide-title { text-shadow: 0 1px 0 rgba(255,255,255,0.75); }\n'
    '.card { background: rgba(238,236,208,0.94); }\n'
    '/* the reading passages are the one place this deck puts a block of\n'
    '   running text on screen, and the learner reads them twice. Solid. */\n'
    '.card.read-text { background: #f4f2e2; }\n'
)

# ── HOUR 4 ────────────────────────────────────────────────────────────
H4_SOME = [
    ('There are ______ grapes on the table.', ['some'],
     'A positive sentence → <strong>some</strong>.'),
    ("There aren't ______ onions left.", ['any'],
     'A negative sentence → <strong>any</strong>.'),
    ('Have you got ______ money?', ['any|some'],
     'A plain question → <strong>any</strong>. Both are accepted here: if you '
     'are really asking for money rather than checking, <em>some</em> is also '
     'natural English.'),
    ('Can I have ______ water, please?', ['some'],
     'A request → <strong>some</strong>. <em>Please</em> is the giveaway.'),
    ("I don't want ______ soup.", ['any'],
     'Negative (<em>don\'t want</em>) → <strong>any</strong>.'),
    ('Would you like ______ orange juice?', ['some'],
     'An offer → <strong>some</strong>. <em>Would you like…?</em> is always an '
     'offer, never a plain question.'),
]

H4_ONE = [
    ('Which cake do you want? The chocolate ______.', ['one'],
     'One cake, singular → <strong>one</strong>.'),
    ('Which shoes do you like? The black ______.', ['ones'],
     'Shoes are plural → <strong>ones</strong>.'),
    ('Do you want the small pizza or the large ______?', ['one'],
     'One pizza, singular → <strong>one</strong>.'),
    ("I don't like these glasses. I like the old ______.", ['ones'],
     'Glasses are plural → <strong>ones</strong>.'),
    ('Which bananas do you want? The yellow ______.', ['ones'],
     'Bananas are plural → <strong>ones</strong>.'),
]

READ1 = ('Yesterday, Mia went to a restaurant with her family. She wanted '
         'pizza, but there wasn\'t any pizza left. Her brother had chicken and '
         'potatoes. Mia had pancakes with strawberries. Later, they bought '
         'some ice cream.')

H4_TF1 = [
    dict(stem='There was a lot of pizza at the restaurant.',
         options=['True', 'False'], correct=1,
         why='<strong>False.</strong> The text says there <em>wasn\'t any pizza '
             'left</em>.'),
    dict(stem='Mia had pancakes with strawberries.',
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> Straight from the text — this is the kind '
             'of mark you must not lose.'),
]

# The old dialogue asked for "any apple juice" in a request, against a rule
# that gave no boundary. Both forms are accepted where both are natural.
H4_DIA = [
    ('<strong>Waiter:</strong> Good evening! Would you like ______ water?',
     ['some'],
     'An offer → <strong>some</strong>.'),
    ('<strong>Customer:</strong> Yes, please. And have you got ______ apple juice?',
     ['any|some'],
     'A question → <strong>any</strong> is the neutral form. <em>Some</em> is '
     'also correct here, because the customer is really making a request.'),
    ("<strong>Waiter:</strong> Sorry, there isn't ______ apple juice&hellip;",
     ['any'],
     'A negative → <strong>any</strong>. Only <em>any</em> works after '
     '<em>isn\'t</em>.'),
    ('&hellip;but we have ______ orange juice.', ['some'],
     'A positive statement → <strong>some</strong>.'),
    ("<strong>Customer:</strong> OK, I'll have ______ orange juice. Thank you!",
     ['some'],
     'A request → <strong>some</strong>.'),
]

# The old version printed "(one jacket)" and "(shoes = plural)" beside the
# gap — which is the answer.
H4_OO = [
    ('<strong>Assistant:</strong> Which jacket would you like?<br>'
     '<strong>Customer:</strong> The red ______, please.', ['one'],
     'One jacket → <strong>one</strong>. Look back at the question to find out '
     'whether the thing is singular or plural.'),
    ('<strong>Assistant:</strong> And which shoes?<br>'
     '<strong>Customer:</strong> The black ______.', ['ones'],
     'Shoes are plural → <strong>ones</strong>.'),
    ('<strong>Assistant:</strong> The small bag or the large ______?',
     ['one'],
     'One bag → <strong>one</strong>.'),
    ('<strong>Customer:</strong> The small ______, please.', ['one'],
     'Still one bag → <strong>one</strong>.'),
]

READ2 = ('Last Friday, Emma went to a new restaurant in the city centre. She '
         'wanted chicken but there wasn\'t any chicken left. The waiter '
         'recommended the lamb. Emma did not usually eat lamb, but she tried '
         'it and loved it! For dessert, she ordered the small cheesecake — she '
         'didn\'t want the large one. She also had some strawberries.')

H4_TF2 = [
    dict(stem='Emma went to the restaurant on Saturday.',
         options=['True', 'False'], correct=1,
         why='<strong>False.</strong> The text says <em>Last Friday</em>. Days '
             'and dates are exactly what step 3 of the reading method tells '
             'you to underline.'),
    # The old item read "There was no chicken at the restaurant", which a
    # careful reader answers False: a restaurant that has run out did have
    # chicken. Restated so the text supports one answer only.
    dict(stem="There wasn't any chicken left when Emma ordered.",
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> Note the word <em>left</em> — the '
             'restaurant had chicken earlier and ran out.'),
    dict(stem='Emma loved the lamb.', options=['True', 'False'], correct=0,
         why='<strong>True.</strong> "She tried it and loved it."'),
    dict(stem='Emma ordered the large cheesecake.', options=['True', 'False'],
         correct=1,
         why='<strong>False.</strong> She ordered the <em>small</em> one. One '
             'word decides it, which is why you read the question twice.'),
]

H4_R5 = [
    ('For dessert, Emma had the small cheesecake and some ______.',
     ['strawberries'],
     '<strong>strawberries</strong> — the last sentence of the text.'),
]

H4_MIX = [
    ("I'd like ______ grapes, please.", ['some'],
     'A request → <strong>some</strong>.'),
    ('Have you got ______ onions?', ['any|some'],
     '<strong>Any</strong> is the neutral question form. In a shop this is '
     'really a request, so <em>some</em> is also correct.'),
    ('Which apple do you want? The green ______.', ['one'],
     'One apple → <strong>one</strong>.'),
    ('Would you like ______ more water?', ['some'],
     'An offer → <strong>some</strong>.'),
    ("I don't like these old shoes. I prefer the new ______.", ['ones'],
     'Shoes are plural → <strong>ones</strong>.'),
]

# ── HOUR 5 · mock test ────────────────────────────────────────────────
# Section 1 was word-for-word Hour 1, and with the word bank removed. New
# sentences on the same eight words, so it tests whether the vocabulary
# stuck rather than whether the learner remembers one screen.
MOCK_VOCAB = [
    ('The ship landed and three ______ walked out onto the sand.', ['aliens|alien'],
     '<strong>Aliens</strong> — beings from another planet. The plural takes '
     '<em>-s</em> like any other noun.'),
    ('You cannot breathe outside, so put your ______ on first.',
     ['spacesuit|space suit'],
     '<strong>Spacesuit</strong> (<em>Raumanzug</em>).'),
    ('Small, red and sweet, and they grow near the ground: ______.',
     ['strawberries'],
     '<strong>Strawberries</strong> (<em>Erdbeeren</em>). Pears grow on trees; '
     'these do not.'),
    ('Beef, chicken and lamb are all types of ______.', ['meat'],
     '<strong>Meat</strong> (<em>Fleisch</em>) — the category, not one of the '
     'three.'),
    ('The ______ gave the order and the ship left the space centre.',
     ['commander'],
     '<strong>Commander</strong> (<em>Kommandant/in</em>) — the person in '
     'charge.'),
]

MOCK_GRAM = [
    ('She usually ______ (go) to school by bus.', ['goes'],
     '<strong>Usually</strong> is a habit → present simple, and <em>she</em> '
     'takes <em>-es</em> after <em>-o</em>.'),
    ('Look! The alien ______ (leave) the spaceship.',
     ["is leaving|'s leaving"],
     '<strong>Look!</strong> → present progressive.'),
    ('Yesterday, I ______ (watch) a science fiction film.', ['watched'],
     '<strong>Yesterday</strong> → past simple. <em>Watch</em> is regular, so '
     'just <em>-ed</em>.'),
    ('Did you ______ (eat) pizza yesterday?', ['eat'],
     'After <strong>did</strong>, the basic verb — <em>eat</em>, never '
     '<em>ate</em>.'),
    ("There aren't ______ tomatoes.", ['any'],
     'A negative → <strong>any</strong>.'),
    ('Which cake do you want? The small ______.', ['one'],
     'One cake → <strong>one</strong>.'),
]

READ3 = ('Last week, Tom and his sister went to a space camp. They saw a real '
         'spacesuit and ate lunch in a rocket café. Tom wanted a burger, but '
         'there wasn\'t any beef. He had chicken instead. His sister had a '
         'salad with peppers and tomatoes.')

MOCK_TF3 = [
    dict(stem='Tom and his sister went to a space camp last week.',
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> First sentence of the text.'),
    dict(stem='Tom ate a beef burger.', options=['True', 'False'], correct=1,
         why='<strong>False.</strong> He wanted one, but there wasn\'t any '
             'beef, so he had chicken. <em>Wanted</em> is not <em>ate</em>.'),
]
MOCK_R3 = [
    ('His sister had a salad with peppers and ______.', ['tomatoes|tomato'],
     '<strong>Tomatoes</strong> — last sentence. Both the singular and the '
     'plural are accepted.'),
]

MOCK_ERR = [
    ("Wrong: <em>She don't eat meat.</em> &nbsp;→&nbsp; She ______ eat meat.",
     ["doesn't|does not"],
     'she → <strong>doesn\'t</strong>.'),
    ('Wrong: <em>Look! The alien leaves the spaceship.</em> &nbsp;→&nbsp; '
     'Look! The alien ______ the spaceship.',
     ["is leaving|'s leaving"],
     '<strong>Look!</strong> forces the progressive.'),
    ('Wrong: <em>Did she went to the restaurant?</em> &nbsp;→&nbsp; '
     'Did she ______ to the restaurant?',
     ['go'],
     'Basic verb after <strong>did</strong>.'),
    ("Wrong: <em>There isn't some milk.</em> &nbsp;→&nbsp; There isn't ______ milk.",
     ['any'],
     'A negative takes <strong>any</strong>, never <em>some</em>.'),
    ('Wrong: <em>I want the red one.</em> (the question was about shoes) '
     '&nbsp;→&nbsp; I want the red ______.',
     ['ones'],
     'Shoes are plural → <strong>ones</strong>.'),
]

MOCK_SAO = [
    ('Would you like ______ ice cream?', ['some'],
     'An offer → <strong>some</strong>.'),
    ("He doesn't have ______ money.", ['any'],
     'A negative → <strong>any</strong>.'),
    ('Which pizza is yours? The small ______.', ['one'],
     'One pizza → <strong>one</strong>.'),
    ('Those are nice pears. I want the yellow ______.', ['ones'],
     'Pears are plural → <strong>ones</strong>.'),
]

READ4 = ('Yesterday, Lena and her family visited a space museum. They watched '
         'a film about planets and saw some old spacesuits. Lena\'s favourite '
         'was a red one from the 1960s. She also found an alien toy in the '
         'museum shop. She didn\'t buy it because there wasn\'t any money '
         'left. Later, they ate some pizza in the café.')

MOCK_TF4 = [
    dict(stem='Lena visited the space museum yesterday.',
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> The text opens with <em>Yesterday</em>.'),
    dict(stem="Lena's favourite spacesuit was blue.",
         options=['True', 'False'], correct=1,
         why='<strong>False.</strong> "Her favourite was a red <em>one</em>" — '
             'and note that <em>one</em> is standing in for <em>spacesuit</em>, '
             'which is the grammar from Hour 4 doing real work in a text.'),
]
MOCK_R4 = [
    ('Lena found an alien ______ in the museum shop.', ['toy'],
     '<strong>Toy</strong> — the sentence is there in the text, and this is '
     'what step 5 of the reading method is for.'),
]
MOCK_WHY = [
    dict(stem="Why didn't Lena buy the alien toy?",
         options=['There wasn\'t any money left.',
                  'The museum shop was already closed.',
                  'She did not really like it very much.'], correct=0,
         why='The text says <strong>there wasn\'t any money left</strong>. The '
             'other two are the kind of answer that sounds reasonable but is '
             'not in the text — always go back and find the line.'),
]


def read_slide(eyebrow_key, eyebrow, title_key, title, text, note_key, note):
    """A reading passage. One wide card, solid, because the learner reads it
    twice and refers back to it from the questions that follow."""
    return '''
    <section class="slide" data-type="teach" data-bg="%s/hero.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="card read-text" style="padding:26px 30px">
          <p class="prose" style="font-size:21px;line-height:1.65">%s</p>
        </div>
        <p class="prose dim" style="margin-top:14px;font-size:16px"
           data-i18n="%s">%s</p>
      </div>
    </section>
''' % (F, eyebrow_key, eyebrow, title_key, title, text, note_key, note)


def build():
    D.assert_no_key_is_longest(H4_TF1, 'H4 reading 1')
    D.assert_no_key_is_longest(H4_TF2, 'H4 reading 2')
    D.assert_no_key_is_longest(MOCK_TF3, 'Mock reading 3')
    D.assert_no_key_is_longest(MOCK_TF4, 'Mock reading 4')
    D.assert_no_key_is_longest(MOCK_WHY, 'Mock why')

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'Out of <em>This World</em>',
                 'Part II: some and any, one and ones, reading technique, and '
                 'the mock test',
                 [('Level', 'A1+ / A2 &middot; Part II'),
                  ('Focus', 'Hours 4&ndash;5'),
                  ('Count', '50 slides')])]

    S += [D.teach('saE', 'Hour 4 &middot; some or any', 'saT',
                  'The rule, and then the exception',
                  [('sa1h', 'Positive → some',
                    'There are <strong>some</strong> apples.',
                    'sa1n', 'This one never changes.'),
                   ('sa2h', 'Negative → any',
                    "There aren't <strong>any</strong> plums.",
                    'sa2n', 'After <em>not</em>, <em>isn\'t</em>, '
                    '<em>don\'t</em> — always <em>any</em>.'),
                   ('sa3h', 'Question → any',
                    'Have you got <strong>any</strong> money?',
                    'sa3n', 'When you genuinely do not know the answer. '
                    'Keep reading — the next slide is the case that catches '
                    'people out.')],
                  folder=F),
          D.teach('sbE', 'Hour 4 &middot; The case that catches people out',
                  'sbT', 'Offers and requests take some — even as questions',
                  [('sb1h', 'An offer',
                    'Would you like <strong>some</strong> tea?',
                    'sb1n', 'You are giving, not asking. <em>Would you '
                    'like…?</em> is always an offer.'),
                   ('sb2h', 'A request',
                    'Can I have <strong>some</strong> water, please?',
                    'sb2n', 'You are asking for a thing, not asking whether it '
                    'exists.'),
                   ('sb3h', 'The overlap',
                    'Have you got <strong>any</strong> / <strong>some</strong> '
                    'apple juice?',
                    'sb3n', 'In a café this is really a request, so both are '
                    'natural. In the test, <em>any</em> is the safe answer to a '
                    'plain question — but you now know why you hear both.')],
                  folder=F),
          D.teach('ooE', 'Hour 4 &middot; one or ones', 'ooT',
                  'So you do not have to say the noun twice',
                  [('oo1h', 'one — singular',
                    'I like the red jacket. → I like the red <strong>one</strong>.',
                    'oo1n', 'One thing.'),
                   ('oo2h', 'ones — plural',
                    'I want the blue shoes. → I want the blue '
                    '<strong>ones</strong>.',
                    'oo2n', 'More than one thing. Shoes, glasses, trousers and '
                    'jeans are always plural in English.'),
                   ('oo3h', 'How to decide',
                    'Look back at the noun in the question.',
                    'oo3n', 'The question tells you. <em>Which shoes…?</em> → '
                    'plural → <em>ones</em>. Nothing else decides it.')],
                  folder=F),
          D.teach('rmE', 'Hour 4 &middot; Reading method', 'rmT1',
                  'Before you read the questions (1 of 2)',
                  [('rm1h', '1 &middot; Read the title',
                    'It tells you the topic before you meet a single sentence.',
                    None, None),
                   ('rm2h', '2 &middot; Look at any picture',
                    'Free information, and it is usually about the main event.',
                    None, None),
                   ('rm3h', '3 &middot; Underline the facts',
                    'Names, days, times, places, numbers.',
                    'rm3n', 'Almost every True/False item is decided by one of '
                    'these. Underline them and the answers are already on the '
                    'page.')],
                  folder=F),
          D.teach('rmE', 'Hour 4 &middot; Reading method', 'rmT2',
                  'Then answer (2 of 2)',
                  [('rm4h', '4 &middot; Read the question twice',
                    'Small, large, Friday, Saturday — one word decides it.',
                    None, None),
                   ('rm5h', '5 &middot; Find the line',
                    'Go back and point at the sentence that proves it.',
                    'rm5n', 'If you cannot find the line, your answer is a '
                    'guess. An answer that "sounds right" is the classic trap.'),
                   ('rm6h', '6 &middot; Full sentence if asked',
                    '<em>Where did Mia go?</em> → Mia went to a restaurant.',
                    'rm6n', 'If the instruction says <em>in full sentences</em>, '
                    'one word scores nothing — however right it is.')],
                  folder=F)]

    for n, rows in enumerate([H4_SOME[:3], H4_SOME[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'sgE', 'Hour 4 &middot; Activity 1',
                    'sgT', 'some or any?', folder=F, size=18, width=140,
                    hint='Decide what the sentence is doing first: stating, '
                         'denying, asking, offering.' if n == 0 else None,
                    hint_key='sgHint' if n == 0 else None)]
    for n, rows in enumerate([H4_ONE[:3], H4_ONE[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'ogE', 'Hour 4 &middot; Activity 2',
                    'ogT', 'one or ones?', folder=F, size=18, width=140,
                    hint='Look back at the noun in the question.'
                         if n == 0 else None,
                    hint_key='ogHint' if n == 0 else None)]

    S += [read_slide('r1E', 'Hour 4 &middot; Reading 1', 'r1T',
                     "Mia's restaurant", READ1, 'r1N',
                     'Underline the names, the food and the word <em>left</em> '
                     'before you turn the page.')]
    S += ["".join(D.mc(i + 1, len(H4_TF1), q, 'tf1E', 'Hour 4 &middot; Activity 3',
                       'tf1T', 'True or false?', folder=F)
                  for i, q in enumerate(H4_TF1))]
    S += [D.teach('fsE', 'Hour 4 &middot; Full sentences', 'fsT',
                  'What a full answer looks like',
                  [('fs1h', 'Where did Mia go yesterday?',
                    'Mia <strong>went to a restaurant</strong> yesterday.',
                    'fs1n', 'The answer reuses the words of the question. That '
                    'is the whole technique.'),
                   ('fs2h', 'What did her brother eat?',
                    'Her brother <strong>ate chicken and potatoes</strong>.',
                    'fs2n', 'Past question → past answer. <em>Ate</em>, not '
                    '<em>eat</em>.'),
                   ('fs3h', 'What did they buy later?',
                    'They <strong>bought some ice cream</strong> later.',
                    'fs3n', 'Not "ice cream". A full sentence needs a subject '
                    'and a verb.')],
                  folder=F)]
    for n, rows in enumerate([H4_DIA[:3], H4_DIA[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'dgE', 'Hour 4 &middot; Activity 4',
                    'dgT', 'At the restaurant — some or any?', folder=F,
                    size=17, width=130,
                    hint='Read who is speaking. A waiter offers; a customer '
                         'asks.' if n == 0 else None,
                    hint_key='dgHint' if n == 0 else None)]
    for n, rows in enumerate([H4_OO[:2], H4_OO[2:]]):
        S += [D.gap(n + 1, 2, rows, None, 'doE', 'Hour 4 &middot; Activity 5',
                    'doT', 'In the shop — one or ones?', folder=F, size=17,
                    width=130,
                    hint='The assistant\'s question tells you singular or '
                         'plural.' if n == 0 else None,
                    hint_key='doHint' if n == 0 else None)]

    S += [read_slide('r2E', 'Hour 4 &middot; Reading 2', 'r2T',
                     "Emma's restaurant visit", READ2, 'r2N',
                     'Watch the day, the two dishes, and the words '
                     '<em>left</em>, <em>small</em> and <em>large</em>.')]
    S += ["".join(D.mc(i + 1, len(H4_TF2), q, 'tf2E', 'Hour 4 &middot; Activity 6',
                       'tf2T', 'True or false?', folder=F)
                  for i, q in enumerate(H4_TF2))]
    S += [D.gap(1, 1, H4_R5, None, 'r5E', 'Hour 4 &middot; Activity 6',
                'r5T', 'Complete from the text', folder=F, size=19, width=200)]
    for n, rows in enumerate([H4_MIX[:3], H4_MIX[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'mxE', 'Hour 4 &middot; Activity 7',
                    'mxT', 'Mixed: some, any, one, ones', folder=F, size=18,
                    width=140,
                    hint='All four are in play now. Decide what the sentence is '
                         'doing, then whether the thing is singular or plural.'
                         if n == 0 else None,
                    hint_key='mxHint' if n == 0 else None)]
    # ── Hour 5 ──
    S += [D.teach('stE', 'Hour 5 &middot; Guided writing', 'stT',
                  'The shape of a story that scores',
                  [('st1h', 'Beginning',
                    'When? Who? Where?',
                    'st1n', 'Two sentences is enough. Start with a time '
                    'marker and the examiner knows immediately that you can '
                    'use one.'),
                   ('st2h', 'Middle, then the problem',
                    'What happened? What went wrong?',
                    'st2n', 'A story with no problem is a list. The problem is '
                    'what makes the reader keep going.'),
                   ('st3h', 'Ending',
                    'What happened in the end?',
                    'st3n', 'Finish it. An unfinished story loses marks even '
                    'if every sentence in it is correct.')],
                  folder=F),
          D.teach('phE', 'Hour 5 &middot; Guided writing', 'phT',
                  'Phrases to join it together',
                  [('ph1h', 'To begin',
                    'Last weekend &middot; One day &middot; Yesterday',
                    None, None),
                   ('ph2h', 'To go on',
                    'First &middot; Then &middot; After that &middot; Later',
                    None, None),
                   ('ph3h', 'For the surprise, and the end',
                    'Suddenly &middot; But then &middot; In the end &middot; '
                    'Finally',
                    'ph3n', 'Use three or four across the whole text. Ten is '
                    'worse than three — it stops being a story and becomes a '
                    'list of connectors.')],
                  folder=F)]

    MODEL_A = ('<strong>Last Saturday,</strong> Mia and her brother went to the '
               'space centre. They looked at a big spaceship and took '
               '<strong>some</strong> photos. <strong>Suddenly,</strong> they '
               'heard a strange noise. An alien came out of the spaceship! At '
               'first Mia was scared, but the alien was friendly.')
    MODEL_B = ('He was hungry, so they gave him <strong>some</strong> pancakes '
               'and <strong>some</strong> strawberries. He <strong>didn\'t '
               'like</strong> the pancakes, but he loved the strawberries. He '
               'wanted more, but there weren\'t <strong>any</strong> left. '
               '<strong>Later,</strong> the alien went back into the '
               'spaceship. Before he left, he gave Mia two small stones — a '
               'green <strong>one</strong> and a blue <strong>one</strong>. '
               '<strong>In the end,</strong> Mia was happy, because she '
               '<strong>had</strong> an exciting story to tell at school.')
    S += [read_slide('mdE', 'Hour 5 &middot; Model text', 'mdT1',
                     'A story that does the job (1 of 2)', MODEL_A, 'mdN1',
                     'Bold marks every checklist item as it happens: a time '
                     'marker to open, <em>some</em>, and <em>suddenly</em> for '
                     'the surprise.'),
          read_slide('mdE', 'Hour 5 &middot; Model text', 'mdT2',
                     'A story that does the job (2 of 2)', MODEL_B, 'mdN2',
                     '112 words in total. Note <em>any</em> in the negative, '
                     '<em>one</em> twice, and three irregular pasts — '
                     '<em>gave</em>, <em>went</em>, <em>had</em>. The old model '
                     'was 99 words and never showed <em>one</em> at all.'),
          D.teach('ecE', 'Hour 5 &middot; Before the mock test', 'ecT',
                  'The five mistakes the error-correction section tests',
                  [('ec1h', 'The -s, and don\'t / doesn\'t',
                    'She <strong>doesn\'t</strong> eat meat.',
                    'ec1n', 'she / he / it → doesn\'t. Everyone else → don\'t.'),
                   ('ec2h', 'The base verb after did',
                    'Did she <strong>go</strong>? &middot; I didn\'t '
                    '<strong>see</strong> it.',
                    'ec2n', 'Never <em>did she went</em>. The past is inside '
                    '<em>did</em>.'),
                   ('ec3h', 'any in negatives, ones for plurals',
                    "There isn't <strong>any</strong> milk. &middot; The red "
                    "<strong>ones</strong>.",
                    'ec3n', 'And <em>Look!</em> always forces the progressive. '
                    'Five rules — that is the whole section.')],
                  folder=F)]

    for n, rows in enumerate([MOCK_VOCAB[:3], MOCK_VOCAB[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'v5E',
                    'Mock test &middot; Section 1', 'v5T', 'Vocabulary',
                    folder=F, size=17, width=170,
                    hint='No word bank this time — this is the test.'
                         if n == 0 else None,
                    hint_key='v5Hint' if n == 0 else None)]
    for n, rows in enumerate([MOCK_GRAM[:3], MOCK_GRAM[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'g5E', 'Mock test &middot; Section 2',
                    'g5T', 'Grammar', folder=F, size=17, width=160)]
    S += [read_slide('r3E', 'Mock test &middot; Section 3', 'r3T',
                     'The space camp', READ3, 'r3N',
                     'Three questions follow. Underline first.')]
    S += ["".join(D.mc(i + 1, len(MOCK_TF3), q, 'r3qE',
                       'Mock test &middot; Section 3', 'r3qT',
                       'True or false?', folder=F)
                  for i, q in enumerate(MOCK_TF3))]
    S += [D.gap(1, 1, MOCK_R3, None, 'r3gE', 'Mock test &middot; Section 3',
                'r3gT', 'Complete from the text', folder=F, size=19, width=190)]
    for n, rows in enumerate([MOCK_ERR[:3], MOCK_ERR[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'e5E', 'Mock test &middot; Section 4',
                    'e5T', 'Error correction', folder=F, size=16, width=140,
                    hint='Each sentence has one mistake. Write the correction '
                         'only.' if n == 0 else None,
                    hint_key='e5Hint' if n == 0 else None)]
    for n, rows in enumerate([MOCK_SAO[:2], MOCK_SAO[2:]]):
        S += [D.gap(n + 1, 2, rows, None, 's5E', 'Mock test &middot; Section 5',
                    's5T', 'some &middot; any &middot; one &middot; ones',
                    folder=F, size=18, width=140)]
    S += [read_slide('r4E', 'Mock test &middot; Section 6', 'r4T',
                     'The space museum', READ4, 'r4N',
                     'Four questions follow — two true/false, one gap and one '
                     'multiple choice.')]
    S += ["".join(D.mc(i + 1, len(MOCK_TF4), q, 'r4qE',
                       'Mock test &middot; Section 6', 'r4qT',
                       'True or false?', folder=F)
                  for i, q in enumerate(MOCK_TF4))]
    S += [D.gap(1, 1, MOCK_R4, None, 'r4gE', 'Mock test &middot; Section 6',
                'r4gT', 'Complete from the text', folder=F, size=19, width=180)]
    S += [D.mc(1, 1, MOCK_WHY[0], 'r4mE', 'Mock test &middot; Section 6',
               'r4mT', 'Why?', folder=F)]

    S += [D.results(),
          D.activate('The Alien in the Restaurant', 'Use at least four:',
                     ['some', 'any', 'one / ones', 'suddenly', 'In the end',
                      'went', 'had'],
                     'Speaking &middot; in pairs',
                     'One of you is the waiter. The other has brought an alien '
                     'to dinner.',
                     ['Waiter: offer four things, every offer with '
                      '<em>some</em>. Two of them have run out — say so with '
                      '<em>any</em>.',
                      'Customer: order using <em>one</em> and <em>ones</em> at '
                      'least once each. Do not repeat the noun.',
                      'Both: the alien does not like the first dish. Sort it '
                      'out without either of you being rude.',
                      'Both: tell the story afterwards in the past simple, in '
                      'six sentences, starting with a time marker.'],
                     'Writing &middot; 100&ndash;120 words',
                     'Write "The Alien in the Restaurant". Check it against the '
                     'model: a time marker to open, some and any used '
                     'correctly, one or ones once, three irregular past verbs, '
                     'and a real ending.',
                     'Last Saturday, an alien came into our restaurant. '
                     'Suddenly, …')]
    return S


if __name__ == '__main__':
    import i18n_exam2
    slides = "".join(build())
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Out of This World — 5-Hour English Test Prep · Part II',
                   i18n_exam2)
    s = s.replace('</style>\n</head>', COVER_CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes' % (OUT, len(s)))
