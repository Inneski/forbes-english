# -*- coding: utf-8 -*-
"""Out of This World — 5-Hour English Test Prep, PART I (Hours 1-3).

Rebuild of exam-prep-5hour-courseEXP.html, which was a tabbed scrolling
course carrying 151 scored items. At house-style density the whole course
is ~143 slides, so it ships as two parts; this is Hours 1-3 and keeps the
original filename, so the live URL does not change.

What the audit found, and what this build does about it.

**Two word banks were answer keys.** Both listed their answers in gap
order — read the bank downwards and you have five marks without reading a
single sentence. Both are alphabetised here, and the guard in deck.py
asserts the positions are not ascending.

**Answer positions were patterned.** All four odd-one-out keys were option
(c); all five time-marker keys were (a); the eight tense items ran a
perfect a-b-a-b, so a learner who noticed the rhythm scored 8/8 without
reading. The engine shuffles options at runtime, so the patterns cannot
survive — but two distractors were also eliminable on word order alone
("The alien last week appeared in the garden" is not a sentence), and
those never tested anything. They are rewritten.

**Five placeholders printed the answer.** `placeholder="e.g. She is
reading."` on the item whose answer is "She is reading"; `"Did she
see...?"` on the item testing the base verb after *did*. Gone.

**Substring matching accepted the mistake it was correcting.** The old
grader tested `answer.indexOf(key) !== -1`, and the key for "❌ She didn't
liked the soup" was "didn't like" — which is a substring of the faulty
sentence, so retyping the error verbatim scored the point and printed
"✓ Correct!". These are gaps now: the learner supplies the form, and the
engine matches the whole field against an explicit alternatives list.

**The negatives rejected correct English.** Every item in Activity 2.6
accepted "does not like pizza" but not "She does not like pizza", against
an instruction that explicitly invited free-form answers. Every
alternative a learner might reasonably type is listed here — contractions
and full forms both.

**Three of five "write the question" items were malformed.** "He went to
school → Did he go to school?" — the question is not answered by the
answer given. The prompts now supply yes/no answers, so asking a yes/no
question is coherent.

**The story-ordering task had a defensible alternative order** (the noise
came *after* the egg hatched) and introduced "the dinosaur" with a
definite article and no antecedent. Resequenced so the noise comes from
inside the box, and the hatching sentence introduces the dinosaur.

**Six scored items had no feedback at all** (the food-sorting task wrote
no string on any outcome), and 107 of 151 items showed the same words
whether the learner was right or wrong. Every scored item here carries an
explanation, and the engine branches.

**Teaching lived in the feedback.** Regular past simple was never taught —
only the irregular table existed, and then the learner was scored on
*looked* and asked to know why *goed* is wrong. The -s and -ing spelling
rules existed only inside answer strings. Three verbs (run, give, know)
were tested but never listed. All of that is now on teaching slides,
before the practice.

**Vocabulary tested but never given:** tomato, pancakes, grapes,
potatoes, peaches, cream. Added, with German glosses, on their own slide.
"suddenly — quickly / a surprise" was simply wrong (it means
unexpectedly, German *plötzlich*) and the next activity tested that word.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'exam-prep-5hour-courseEXP.html'
F = 'ExamPrep'

# Light theme: the hero is a saturated colour grid, bright edge to edge.
# The dark derivation failed its accent row (3.48:1); the light one passes
# every row. Derived mechanically, not chosen.
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

  /* This hero is a colour chart, not a picture: sixty flat, fully
     saturated blocks with hard edges and no quiet area anywhere. At the
     house default of 0.62 the light theme's interior slides had the
     eyebrow and the slide title fighting a magenta square directly
     behind them. Dropped well below the floor and desaturated hard,
     because text suffered and nothing is lost — a colour chart has no
     composition to preserve. Both departures are deliberate. */
  --bg-opacity    : 0.15;''' % F

# The template's own note says never to brighten a light cover to rescue
# text — if the title will not read, the hero is wrong for a light lesson.
# The hero here was chosen by the user, so instead of brightening the
# image the cover text gets a plate of its own and the artwork stays at
# full strength around it. Same move as the locker-corridor lesson.
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
    '/* the cover shadow is a white glow, which does nothing on a cream\n'
    '   plate and softens the display face. Off here. */\n'
    '.slide[data-type="cover"] .cover-title,\n'
    '.slide[data-type="cover"] .cover-sub { text-shadow: none; }\n'
    '.slide[data-type="cover"] .chip {\n'
    '  background: #ffffff; border-color: var(--border); color: var(--text);\n'
    '}\n'
    '/* the bar sits on the raw grid on the cover, where the template\n'
    '   removes its gradient. Give it one back. */\n'
    '.stage.on-cover .deck-bar {\n'
    '  background: linear-gradient(180deg, transparent, rgba(241,239,214,0.92));\n'
    '}\n'
    '.deck-count, .deck-score { color: var(--text); }\n'
    '/* the eyebrow and slide title sit directly on the pattern, with no\n'
    '   card under them; at 19px mono the eyebrow needs the extra weight. */\n'
    '.eyebrow { color: var(--accent-bright); font-weight: 700; }\n'
    '.slide-title { text-shadow: 0 1px 0 rgba(255,255,255,0.75); }\n'
    '.card { background: rgba(238,236,208,0.94); }\n'
)

# ── HOUR 1 ────────────────────────────────────────────────────────────
H1_VERBS = [
    dict(stem='Complete the sentences with the past simple.',
         options=['complete', 'sentences', 'past', 'simple'], correct=0,
         why='<strong>Complete</strong> is the command verb — it tells you what to '
             'do. <em>Past simple</em> is the target: it tells you what to use.'),
    dict(stem='Choose True or False.',
         options=['Choose', 'True', 'False', 'or'], correct=0,
         why='<strong>Choose</strong> is the command verb. You are not writing '
             'anything here — you are picking one of two.'),
    dict(stem='Write a dialogue using one or ones.',
         options=['Write', 'dialogue', 'using', 'ones'], correct=0,
         why='<strong>Write</strong> is the command verb. <em>One or ones</em> is '
             'the target — the thing the examiner is looking for.'),
    dict(stem='Answer in full sentences.',
         options=['Answer', 'full', 'sentences', 'in'], correct=0,
         why='<strong>Answer</strong> is the command verb, and <em>in full '
             'sentences</em> is the condition. One word will not score here.'),
    dict(stem='Match the words to the pictures.',
         options=['Match', 'words', 'pictures', 'the'], correct=0,
         why='<strong>Match</strong> is the command verb. Nothing has to be '
             'written — you are joining two lists.'),
]

H1_FILL = [
    ('A person from another planet is an ______.', ['alien'],
     'An <strong>alien</strong> comes from another planet. German: '
     '<em>Außerirdische/r</em>.'),
    ('Astronauts wear a ______ so they can breathe in space.',
     ['spacesuit|space suit'],
     'A <strong>spacesuit</strong> (<em>Raumanzug</em>) carries its own air.'),
    ('Mars is a ______, not a star.', ['planet'],
     'Mars is a <strong>planet</strong>. A star makes its own light; a planet '
     'does not.'),
    ('The astronauts flew to Mars in a ______.', ['spaceship|space ship'],
     'They travel in a <strong>spaceship</strong> (<em>Raumschiff</em>).'),
    ('The ______ is the person in charge of the spaceship.', ['commander'],
     'The <strong>commander</strong> (<em>Kommandant/in</em>) gives the orders.'),
]
H1_BANK = sorted(['alien', 'spacesuit', 'planet', 'spaceship', 'commander'])

H1_CAT = [
    ('Beef is ______.', ['meat'],
     '<strong>Meat</strong> (<em>Fleisch</em>). Beef comes from a cow.'),
    ('Strawberries are ______.', ['fruit'],
     '<strong>Fruit</strong> (<em>Obst</em>). Strawberries are sweet and grow '
     'on a small plant.'),
    ('Cabbage is a ______.', ['vegetable|veg'],
     '<strong>Vegetable</strong> (<em>Gemüse</em>). Cabbage is the big green '
     'leaves you cook.'),
    ('Chicken is ______.', ['meat'],
     '<strong>Meat</strong> (<em>Fleisch</em>). Chicken comes from a bird.'),
    ('Pears are ______.', ['fruit'],
     '<strong>Fruit</strong> (<em>Obst</em>). Pears grow on a tree, like '
     'apples.'),
    ('Onions are a ______.', ['vegetable|veg'],
     '<strong>Vegetable</strong> (<em>Gemüse</em>). You cook with onions; you '
     'do not eat them as a dessert.'),
]

H1_ODD = [
    dict(stem='Which word is different from the others?',
         options=['spaceship', 'planet', 'chicken'], correct=2,
         why='<strong>Chicken</strong> is food. <em>Spaceship</em> and '
             '<em>planet</em> are both space words.'),
    # Written the other way round on purpose. With beef / chicken /
    # strawberries the key was the only long word on the slide and could be
    # picked on shape alone; asking for the meat among the fruit puts the
    # short word in the answer position instead.
    dict(stem='Which word is different from the others?',
         options=['strawberries', 'pears', 'chicken'], correct=2,
         why='<strong>Chicken</strong> is meat. <em>Strawberries</em> and '
             '<em>pears</em> are both fruit.'),
    dict(stem='Which word is different from the others?',
         options=['peppers', 'onions', 'plums'], correct=2,
         why='<strong>Plums</strong> are fruit. <em>Peppers</em> and '
             '<em>onions</em> are vegetables.'),
    dict(stem='Which word is different from the others?',
         options=['commander', 'spacesuit', 'tomato'], correct=2,
         why='<strong>Tomato</strong> is food. <em>Commander</em> and '
             '<em>spacesuit</em> are both space words.'),
]

H1_TF = [
    dict(stem='A plum is a type of vegetable.', options=['True', 'False'],
         correct=1,
         why='<strong>False.</strong> A plum (<em>Pflaume</em>) is fruit. You '
             'eat it raw and sweet.'),
    dict(stem='Beef comes from a cow.', options=['True', 'False'], correct=0,
         why='<strong>True.</strong> Beef (<em>Rindfleisch</em>) is the meat of '
             'a cow. Lamb comes from a sheep.'),
    dict(stem='Astronauts wear a spacesuit in space.',
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> There is no air in space, so the suit '
             'carries its own.'),
    dict(stem='UFO means Unidentified Flying Object — nobody knows what it is.',
         options=['True', 'False'], correct=0,
         why='<strong>True.</strong> <em>Unidentified</em> means we cannot say '
             'what it is. That is the whole meaning of the word.'),
    dict(stem='Pancakes are a type of meat.', options=['True', 'False'],
         correct=1,
         why='<strong>False.</strong> Pancakes (<em>Pfannkuchen</em>) are made '
             'from flour, milk and eggs.'),
]

H1_MENU = [
    ('Main course: grilled ______ — the meat that comes from a bird.',
     ['chicken'],
     '<strong>Chicken</strong>. Beef comes from a cow and lamb from a sheep, '
     'so only chicken fits "a bird".'),
    ('Dessert: fresh red ______ with cream.', ['strawberries'],
     '<strong>Strawberries</strong> are the red ones. Pears are green or '
     'yellow, so the colour decides it.'),
    ('Fruit salad: apples, ______ and peaches — the green fruit from a tree.',
     ['pears'],
     '<strong>Pears</strong> (<em>Birnen</em>) grow on trees, like apples. '
     'Strawberries grow on a small plant near the ground.'),
    ('Vegetarian dish: ______ and pepper stir-fry — the big green leaves.',
     ['cabbage'],
     '<strong>Cabbage</strong> (<em>Kohl</em>) is the leaf vegetable. Read the '
     'clue after the dash: it tells you which word fits.'),
    ('Starter: hot red ______ soup.', ['tomato|tomatoes'],
     '<strong>Tomato</strong> soup. Both <em>tomato soup</em> and '
     '<em>tomatoes</em> are accepted here.'),
]
H1_MENU_BANK = sorted(['chicken', 'strawberries', 'pears', 'cabbage', 'tomato'])

# ── HOUR 2 ────────────────────────────────────────────────────────────
# The old "correct the mistake" items were graded by substring match, so
# retyping the faulty sentence scored the point. As gaps the learner has
# to produce the form, and the whole field is matched.
H2_ERR = [
    ('Wrong: <em>She play football.</em> &nbsp;→&nbsp; She ______ football.',
     ['plays'],
     'She / he / it takes <strong>-s</strong> in the present simple: '
     '<em>she plays</em>.'),
    ('Wrong: <em>He don\'t like onions.</em> &nbsp;→&nbsp; He ______ like onions.',
     ["doesn't|does not"],
     'He / she / it uses <strong>doesn\'t</strong>, never <em>don\'t</em>. And '
     'the verb after it stays basic: <em>like</em>, not <em>likes</em>.'),
    ('Wrong: <em>Does she likes pizza?</em> &nbsp;→&nbsp; Does she ______ pizza?',
     ['like'],
     'After <strong>does</strong>, use the basic verb. The <em>-s</em> is '
     'already in <em>does</em> — you never write it twice.'),
    ('Wrong: <em>I goes to school.</em> &nbsp;→&nbsp; I ______ to school.',
     ['go'],
     '<strong>I</strong> never takes <em>-s</em>. Only he, she and it do.'),
    ('Wrong: <em>They doesn\'t watch TV.</em> &nbsp;→&nbsp; They ______ watch TV.',
     ["don't|do not"],
     'I, you, we and they use <strong>don\'t</strong>. Only he, she and it use '
     '<em>doesn\'t</em>.'),
]

# These were two-option MCQs: plays / is playing. The progressive form is
# always the longer string, so on every item with a progressive key the
# answer was the long one — a tell the learner can use without reading the
# sentence, and one that cannot be fixed by lengthening a distractor,
# because "comes" cannot be made longer without ceasing to be the word.
# As gaps the learner produces the form, and the time word is the only
# thing that can tell them which.
H2_TENSE = [
    ('She usually ______ (play) tennis on Fridays.', ['plays'],
     '<strong>usually</strong> means it happens again and again — a habit, so '
     'present simple. She takes <em>-s</em>.'),
    ('Look! The alien ______ (come) out of the spaceship.',
     ['is coming|\'s coming'],
     '<strong>Look!</strong> means it is happening in front of you right now, '
     'so present progressive: <em>is coming</em>.'),
    ('I ______ (eat) breakfast every morning.', ['eat'],
     '<strong>Every morning</strong> is a habit. After <em>I</em> there is no '
     '<em>-s</em>.'),
    ('We ______ (learn) English now.', ["are learning|'re learning"],
     '<strong>Now</strong> means at this moment — present progressive.'),
    ('We ______ (play) football every Saturday.', ['play'],
     '<strong>Every Saturday</strong> is a repeated habit, so present simple. '
     '<em>We</em> takes no <em>-s</em>.'),
    ('Sssh! The baby ______ (sleep) at the moment.',
     ["is sleeping|'s sleeping"],
     '<strong>At the moment</strong> means right now — present progressive.'),
    ('I ______ (speak) three languages: English, German and French.', ['speak'],
     'Knowing a language is always true, not something happening this second. '
     'Always true → present simple.'),
    ('Listen! They ______ (eat) a pizza in the space café.',
     ["are eating|'re eating"],
     '<strong>Listen!</strong> works like <em>Look!</em> — it points at this '
     'moment, so present progressive.'),
]

# The metalanguage the old version put inside the sentence itself
# ("She (third person singular) _____ to the space centre") is gone; the
# subject is doing that work on its own.
H2_PARA = [
    ('Every Saturday, Mia ______ (go) to the space centre.', ['goes'],
     '<strong>goes</strong> — <em>Mia</em> is she, so add <em>-s</em>. After '
     '<em>-o</em> the spelling is <em>-es</em>: go → goes.'),
    ('She ______ (meet) her friend Lena there.', ['meets'],
     '<strong>meets</strong> — she, so <em>-s</em>.'),
    ('They ______ (look) at the big spaceship.', ['look'],
     '<strong>look</strong> — <em>they</em> takes no <em>-s</em>. Only he, she '
     'and it do.'),
    ('They ______ (take) lots of photos.', ['take'],
     '<strong>take</strong> — they, so no <em>-s</em>.'),
    ('After the visit, they always ______ (eat) pancakes together.', ['eat'],
     '<strong>eat</strong> — <em>always</em> tells you it is a habit, and '
     '<em>they</em> keeps the verb basic.'),
]

# Contractions are correct English, so they are accepted. The old version
# marked "She's reading" wrong.
H2_PROG = [
    ('Now: she / read &nbsp;→&nbsp; She ______ .',
     ["is reading|'s reading"],
     'she + <strong>is</strong> + verb<strong>-ing</strong>. '
     '<em>She\'s reading</em> is the same thing, and also correct.'),
    ('Now: he / play football &nbsp;→&nbsp; He ______ football.',
     ["is playing|'s playing"],
     'he + <strong>is</strong> + play<strong>ing</strong>.'),
    ('Now: they / eat &nbsp;→&nbsp; They ______ .',
     ["are eating|'re eating"],
     'they + <strong>are</strong> + eat<strong>ing</strong>.'),
    ('Look! I / watch the alien &nbsp;→&nbsp; I ______ the alien.',
     ["am watching|'m watching"],
     'I + <strong>am</strong> + watch<strong>ing</strong>. Only <em>I</em> '
     'takes <em>am</em>.'),
    ('Listen! it / make a noise &nbsp;→&nbsp; It ______ a noise.',
     ["is making|'s making"],
     'it + <strong>is</strong> + mak<strong>ing</strong>. <em>Make</em> ends in '
     '<em>-e</em>, so drop the <em>-e</em>: making, not <em>makeing</em>.'),
]

H2_NEG = [
    ('She likes pizza. &nbsp;→&nbsp; She ______ pizza.',
     ["doesn't like|does not like"],
     'she → <strong>doesn\'t</strong> + basic verb. Not <em>doesn\'t likes</em> '
     '— the <em>-s</em> is already inside <em>doesn\'t</em>.'),
    ('He plays tennis. &nbsp;→&nbsp; He ______ tennis.',
     ["doesn't play|does not play"],
     'he → <strong>doesn\'t play</strong>. The <em>-s</em> moves off the verb '
     'and into <em>doesn\'t</em>.'),
    ('I watch TV every evening. &nbsp;→&nbsp; I ______ TV every evening.',
     ["don't watch|do not watch"],
     'I → <strong>don\'t</strong>, never <em>doesn\'t</em>.'),
    ('They eat breakfast at 7am. &nbsp;→&nbsp; They ______ breakfast at 7am.',
     ["don't eat|do not eat"],
     'they → <strong>don\'t eat</strong>.'),
    ('The commander speaks English. &nbsp;→&nbsp; The commander ______ English.',
     ["doesn't speak|does not speak"],
     '<em>The commander</em> is one person — he or she — so '
     '<strong>doesn\'t speak</strong>.'),
]

H2_MATCH = [
    ('go', 'goes'), ('watch', 'watches'), ('fly', 'flies'),
    ('do', 'does'), ('eat', 'eats'), ('finish', 'finishes'),
]

# ── HOUR 3 ────────────────────────────────────────────────────────────
H3_PAST_A = [
    ('go &nbsp;→&nbsp; ______', ['went'],
     '<strong>went</strong>. Irregular — there is no rule, you learn it.'),
    ('see &nbsp;→&nbsp; ______', ['saw'],
     '<strong>saw</strong>. Irregular.'),
    ('eat &nbsp;→&nbsp; ______', ['ate'],
     '<strong>ate</strong>. Irregular.'),
]
H3_PAST_B = [
    ('buy &nbsp;→&nbsp; ______', ['bought'],
     '<strong>bought</strong>. Irregular — and the spelling is worth a second '
     'look: <em>-ought</em>.'),
    ('write &nbsp;→&nbsp; ______', ['wrote'],
     '<strong>wrote</strong>. Irregular.'),
    ('watch &nbsp;→&nbsp; ______', ['watched'],
     '<strong>watched</strong>. Regular, so just add <em>-ed</em>. Not every '
     'verb in this activity is irregular — check before you guess.'),
]
H3_MATCH = [
    ('come', 'came'), ('take', 'took'), ('have', 'had'),
    ('run', 'ran'), ('give', 'gave'), ('know', 'knew'),
]

H3_ERR = [
    ('Wrong: <em>Did you went home?</em> &nbsp;→&nbsp; Did you ______ home?',
     ['go'],
     'After <strong>did</strong>, use the basic verb. <em>Did</em> is already '
     'the past, so <em>went</em> would say it twice.'),
    ('Wrong: <em>I didn\'t saw the alien.</em> &nbsp;→&nbsp; I didn\'t ______ the alien.',
     ['see'],
     'Same rule after <strong>didn\'t</strong>: basic verb. <em>See</em>, not '
     '<em>saw</em>.'),
    ('Wrong: <em>She didn\'t liked the soup.</em> &nbsp;→&nbsp; She didn\'t ______ the soup.',
     ['like'],
     'Basic verb after <em>didn\'t</em> — and that is true for regular verbs '
     'too, so <strong>like</strong>, not <em>liked</em>.'),
    ('Wrong: <em>Did he found the spaceship?</em> &nbsp;→&nbsp; Did he ______ the spaceship?',
     ['find'],
     '<strong>find</strong>. The past is inside <em>did</em>.'),
    ('Wrong: <em>We goed to the space centre.</em> &nbsp;→&nbsp; We ______ to the space centre.',
     ['went'],
     '<strong>went</strong>. <em>Go</em> is irregular, so <em>-ed</em> does not '
     'work on it. There is no such word as <em>goed</em>.'),
]

H3_ORDER = [
    'Five years ago, Tom found an egg in the garden.',
    'He put the egg in a box.',
    'Suddenly, he heard a strange noise inside the box.',
    'The next morning, he heard the noise again.',
    'A week later, the egg opened and a small dinosaur came out.',
    'Five years later, the dinosaur was as big as a house.',
]

H3_STORY = [
    ('Last night, Tom ______ (go) into the garden.', ['went'],
     '<strong>went</strong> — go is irregular.'),
    ('He ______ (see) a bright light in the sky.', ['saw'],
     '<strong>saw</strong> — see is irregular.'),
    ('He ______ (run) inside.', ['ran'],
     '<strong>ran</strong> — run is irregular.'),
    ('He ______ (find) his sister.', ['found'],
     '<strong>found</strong> — find is irregular.'),
    ('They ______ (look) out of the window together.', ['looked'],
     '<strong>looked</strong> — look is <em>regular</em>, so it just takes '
     '<em>-ed</em>. Not every verb in a past story is irregular.'),
    ('The light ______ (come) closer and closer.', ['came'],
     '<strong>came</strong> — come is irregular.'),
]

# Every prompt now gives a yes/no answer, so a yes/no question is the
# coherent thing to ask. Three of the old five were not.
H3_Q = [
    ('Yes, she saw an alien. &nbsp;→&nbsp; ______ she ______ an alien?',
     ['Did|did', 'see'],
     '<strong>Did she see…?</strong> — Did + person + basic verb. Never '
     '<em>Did she saw</em>.'),
    ('Yes, he went to school. &nbsp;→&nbsp; ______ he ______ to school?',
     ['Did|did', 'go'],
     '<strong>Did he go…?</strong> — <em>go</em>, not <em>went</em>.'),
    ('No, they didn\'t eat pizza. &nbsp;→&nbsp; ______ they ______ pizza?',
     ['Did|did', 'eat'],
     '<strong>Did they eat…?</strong> — <em>eat</em>, not <em>ate</em>.'),
    ('Yes, Tom found the egg. &nbsp;→&nbsp; ______ Tom ______ the egg?',
     ['Did|did', 'find'],
     '<strong>Did Tom find…?</strong> — <em>find</em>, not <em>found</em>.'),
    ('Yes, she bought a new spacesuit. &nbsp;→&nbsp; ______ she ______ a new spacesuit?',
     ['Did|did', 'buy'],
     '<strong>Did she buy…?</strong> — <em>buy</em>, not <em>bought</em>.'),
]

H3_TM = [
    dict(stem='I went to bed early. ______ I got up and had breakfast.',
         options=['The next morning', 'Two minutes ago', 'Every Saturday'],
         correct=0,
         why='<strong>The next morning</strong> — you get up the morning after '
             'you go to bed. <em>Two minutes ago</em> would put breakfast '
             'before bed.'),
    dict(stem='The alien ______ appeared in the garden — nobody expected it.',
         options=['suddenly', 'every day', 'slowly'], correct=0,
         why='<strong>Suddenly</strong> means <em>unexpectedly</em> — German '
             '<em>plötzlich</em>. It is not about speed, and the clue is '
             '"nobody expected it".'),
    dict(stem='She started the project ______ and finished it yesterday.',
         options=['two weeks ago', 'next Wednesday', 'in two days'], correct=0,
         why='<strong>Two weeks ago</strong> points backwards from now. The '
             'other two point forwards, and the sentence has already finished.'),
    dict(stem='They found the spaceship on Monday. A week ______, it opened.',
         options=['later', 'before', 'ago'], correct=0,
         why='<strong>Later</strong> means after the event you just named. '
             '<em>Ago</em> counts back from now, not from an earlier event.'),
    dict(stem='Tom met the alien yesterday. ______, they became good friends.',
         options=['Later', 'Suddenly', 'Two years ago'], correct=0,
         why='<strong>Later</strong> — time passes and then the next thing '
             'happens. <em>Suddenly</em> would mean it was a surprise.'),
]

# ── slides ────────────────────────────────────────────────────────────
def build():
    D.assert_no_key_is_longest(H1_VERBS, 'H1 command verbs')
    D.assert_no_key_is_longest(H1_ODD, 'H1 odd one out')
    D.assert_no_key_is_longest(H1_TF, 'H1 true/false')
    D.assert_no_key_is_longest(H3_TM, 'H3 time markers')
    D.assert_bank_is_not_a_key(H1_BANK, [a.split('|')[0] for _, aa, _ in H1_FILL
                                         for a in aa])
    D.assert_bank_is_not_a_key(H1_MENU_BANK,
                               [a.split('|')[0] for _, aa, _ in H1_MENU for a in aa])

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'Out of <em>This World</em>',
                 'Five hours to your English test — Part I: strategy, vocabulary '
                 'and the two present tenses',
                 [('Level', 'A1+ / A2 &middot; Part I'),
                  ('Focus', 'Hours 1&ndash;3'),
                  ('Count', '69 slides')])]

    # front matter
    S += [D.teach('mapE', 'Before you start', 'mapT', 'What is in the test?',
                  [(None, 'Structure &amp; Reading',
                    'Find the keywords in the instruction. Then True/False, '
                    'completing sentences, and answering in full sentences.',
                    'mapN1', 'Getting this wrong costs marks you already knew '
                    'how to earn.'),
                   (None, 'Words &amp; Grammar',
                    'Unit 8 space words and Unit 9 food words, used correctly '
                    'in a sentence. Present simple, present progressive, past '
                    'simple, some/any, one/ones.',
                    'mapN2', 'This is the largest part of the paper.'),
                   (None, 'Writing',
                    'One text of 100&ndash;120 words, with a beginning, a '
                    'middle and an end, joined with linking words.',
                    'mapN3', 'Part II covers this in full.')],
                  folder=F),
          D.teach('planE', 'Your flight plan', 'planT',
                  'Three hours in this part',
                  [(None, 'Hour 1',
                    'Test strategy and vocabulary.',
                    'planN1', 'You will understand what an instruction is '
                    'asking for, and know the space and food words by heart.'),
                   (None, 'Hour 2',
                    'Present simple and present progressive.',
                    'planN2', 'You will make statements, negatives and '
                    'questions, and choose between the two tenses on purpose.'),
                   (None, 'Hour 3',
                    'Past simple and time markers.',
                    'planN3', 'You will tell a finished story in the right '
                    'order, and ask questions about it.')],
                  folder=F)]

    # ── Hour 1 ──
    S += [D.teach('goldE', 'Hour 1 &middot; Test strategy', 'goldT',
                  'Read the instruction like a sat-nav',
                  [('gold1h', 'Step 1 &mdash; find the verb',
                    'complete &middot; choose &middot; write &middot; answer '
                    '&middot; match',
                    'gold1n', 'The verb tells you what to <em>do</em>. Nothing '
                    'else in the instruction does.'),
                   ('gold2h', 'Step 2 &mdash; find the target',
                    'past simple &middot; some/any &middot; one/ones',
                    'gold2n', 'The target tells you what the examiner is '
                    'looking for. Miss it and a correct sentence still scores '
                    'nothing.'),
                   ('gold3h', 'Worked example',
                    '&ldquo;<em>Complete</em> the sentences with the '
                    '<em>past simple</em>.&rdquo;',
                    'gold3n', 'Verb: complete. Target: past simple. Now you '
                    'know both what to do and what to use.')],
                  folder=F)]

    U8 = [('spaceship', 'Raumschiff'), ('commander', 'Kommandant/in'),
          ('alien', 'Außerirdische/r'), ('spacesuit', 'Raumanzug'),
          ('planet', 'Planet'), ('space centre', 'Raumfahrtzentrum'),
          ('time traveller', 'Zeitreisende/r'), ('UFO', 'UFO')]
    for n, group in enumerate([U8[:4], U8[4:]]):
        S += [D.teach('u8E', 'Hour 1 &middot; Unit 8 words', 'u8T%d' % (n + 1),
                      'Science fiction (%d of 2)' % (n + 1),
                      [(None, e, g, None, None) for e, g in group],
                      folder=F)]

    S += [D.teach('catE', 'Hour 1 &middot; Food groups', 'catT',
                  'Meat, fruit, vegetable',
                  [('cat1h', 'Meat &mdash; Fleisch',
                    'beef &middot; chicken &middot; lamb',
                    'cat1n', 'Beef is from a cow, chicken from a bird, lamb '
                    'from a young sheep.'),
                   ('cat2h', 'Fruit &mdash; Obst',
                    'strawberries &middot; pears &middot; plums',
                    'cat2n', 'Sweet, and usually eaten raw.'),
                   ('cat3h', 'Vegetable &mdash; Gemüse',
                    'cabbage &middot; onions &middot; peppers',
                    'cat3n', 'Usually cooked, and not sweet. This is the group '
                    'German learners lose marks on.')],
                  folder=F)]

    U9 = [('beef', 'Rindfleisch'), ('chicken', 'Hähnchen'), ('lamb', 'Lamm'),
          ('cabbage', 'Kohl'), ('onions', 'Zwiebeln'), ('peppers', 'Paprika'),
          ('strawberries', 'Erdbeeren'), ('pears', 'Birnen'),
          ('plums', 'Pflaumen'), ('cheesecake', 'Käsekuchen')]
    for n, group in enumerate([U9[:6], U9[6:]]):
        cards = [(None, '%s &middot; %s' % (group[i][0], group[i + 1][0]),
                  '%s &middot; %s' % (group[i][1], group[i + 1][1]), None, None)
                 for i in range(0, len(group), 2)]
        S += [D.teach('u9E', 'Hour 1 &middot; Unit 9 words', 'u9T%d' % (n + 1),
                      'Food (%d of 2)' % (n + 1), cards, folder=F)]

    S += [D.teach('exE', 'Hour 1 &middot; Also on the menu', 'exT',
                  'Words the test uses that the word list forgot',
                  [(None, 'tomato &middot; potatoes', 'Tomate &middot; Kartoffeln',
                    None, None),
                   (None, 'pancakes &middot; cream', 'Pfannkuchen &middot; Sahne',
                    None, None),
                   (None, 'grapes &middot; peaches', 'Trauben &middot; Pfirsiche',
                    None, None),
                   (None, 'salad &middot; ice cream', 'Salat &middot; Eis',
                    None, None)],
                  folder=F)]

    S += ["".join(D.mc(i + 1, len(H1_VERBS), q, 'vE',
                       'Hour 1 &middot; Activity 1', 'vT',
                       'Click the word that tells you what to do', folder=F)
                  for i, q in enumerate(H1_VERBS))]
    for n, rows in enumerate([H1_FILL[:3], H1_FILL[3:]]):
        S += [D.gap(n + 1, 2, rows, H1_BANK if n == 0 else None, 'fE',
                    'Hour 1 &middot; Activity 2', 'fT',
                    'Complete the sentence', folder=F, size=18, width=200,
                    hint='Five words in the bank, five gaps. Each is used once.'
                         if n == 0 else None,
                    hint_key='fHint' if n == 0 else None)]
    for n, rows in enumerate([H1_CAT[:3], H1_CAT[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'cE', 'Hour 1 &middot; Activity 3',
                    'cT', 'Meat, fruit or vegetable?', folder=F, size=18,
                    width=170,
                    hint='Type one word: meat, fruit or vegetable.',
                    hint_key='cHint')]
    S += ["".join(D.mc(i + 1, len(H1_ODD), q, 'oE', 'Hour 1 &middot; Activity 4',
                       'oT', 'Odd one out', folder=F)
                  for i, q in enumerate(H1_ODD))]
    S += ["".join(D.mc(i + 1, len(H1_TF), q, 'tfE', 'Hour 1 &middot; Activity 5',
                       'tfT', 'True or false?', folder=F)
                  for i, q in enumerate(H1_TF))]
    for n, rows in enumerate([H1_MENU[:3], H1_MENU[3:]]):
        S += [D.gap(n + 1, 2, rows, H1_MENU_BANK if n == 0 else None, 'mE',
                    'Hour 1 &middot; Activity 6', 'mT',
                    'Complete the restaurant menu', folder=F, size=17,
                    width=190,
                    hint='Each word is used once. The clue after the dash tells '
                         'you which one.' if n == 0 else None,
                    hint_key='mHint' if n == 0 else None)]
    # ── Hour 2 ──
    S += [D.teach('psE', 'Hour 2 &middot; Present simple', 'psT',
                  'Habits, and things that are always true',
                  [('ps1h', 'Positive',
                    'I play tennis. &middot; She play<strong>s</strong> tennis.',
                    'ps1n', 'She, he and it add <em>-s</em>. Nothing else does.'),
                   ('ps2h', 'Negative',
                    "I <strong>don't</strong> play. &middot; "
                    "She <strong>doesn't</strong> play.",
                    'ps2n', 'The verb after don\'t / doesn\'t is always basic.'),
                   ('ps3h', 'Question',
                    '<strong>Do</strong> you play? &middot; '
                    '<strong>Does</strong> she play?',
                    'ps3n', 'Signal words: usually, often, sometimes, never, '
                    'every day, on Mondays.')],
                  folder=F),
          D.teach('ppE', 'Hour 2 &middot; Present progressive', 'ppT',
                  'Happening right now',
                  [('pp1h', 'Positive',
                    'I <strong>am</strong> eat<strong>ing</strong>. &middot; '
                    'She <strong>is</strong> watching.',
                    'pp1n', 'am / is / are, then the verb with <em>-ing</em>.'),
                   ('pp2h', 'Negative',
                    "I'm not eating. &middot; They aren't playing.",
                    'pp2n', 'Only <em>am / is / are</em> changes. The '
                    '<em>-ing</em> word never does.'),
                   ('pp3h', 'Question',
                    'Am I eating? &middot; Is she watching TV?',
                    'pp3n', 'Signal words: now, at the moment, today, right '
                    'now, Look!, Listen!')],
                  folder=F),
          D.teach('chE', 'Hour 2 &middot; The decision', 'chT',
                  'Which tense, and how you know',
                  [('ch1h', 'Again and again → simple',
                    'She play<strong>s</strong> tennis on Fridays.',
                    'ch1n', 'A habit, a routine, or something always true. It '
                    'does not matter what is happening as you read.'),
                   ('ch2h', 'At this moment → progressive',
                    'Look! She <strong>is playing</strong> tennis.',
                    'ch2n', 'It is happening as you speak. Look! and Listen! '
                    'are the clearest signals in the exam.'),
                   ('ch3h', 'Find the signal first',
                    'usually, every day → simple &nbsp;|&nbsp; now, Look! → '
                    'progressive',
                    'ch3n', 'Read the sentence for a time word before you look '
                    'at the verb. The time word decides, every time.')],
                  folder=F),
          D.teach('ssE', 'Hour 2 &middot; Spelling', 'ssT',
                  'How she / he / it gets its -s',
                  [('ss1h', 'Most verbs: add -s',
                    'play → plays &middot; eat → eats &middot; meet → meets',
                    None, None),
                   ('ss2h', 'After -o, -ch, -sh, -ss: add -es',
                    'go → goes &middot; watch → watches &middot; finish → '
                    'finishes',
                    None, None),
                   ('ss3h', 'Consonant + y: -y becomes -ies',
                    'fly → flies &middot; study → studies',
                    'ss3n', 'But <em>play → plays</em>: there is a vowel before '
                    'the y, so nothing changes.')],
                  folder=F),
          D.teach('igE', 'Hour 2 &middot; Spelling', 'igT',
                  'Making the -ing form',
                  [('ig1h', 'Most verbs: add -ing',
                    'watch → watching &middot; play → playing',
                    None, None),
                   ('ig2h', 'Ends in -e: drop the -e',
                    'make → making &middot; write → writing',
                    'ig2n', 'Never <em>makeing</em>. This one is tested.'),
                   ('ig3h', 'Short word, one consonant: double it',
                    'sit → sitting &middot; run → running',
                    None, None)],
                  folder=F)]

    for n, rows in enumerate([H2_ERR[:3], H2_ERR[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'e2E', 'Hour 2 &middot; Activity 1',
                    'e2T', 'Fix the mistake', folder=F, size=17, width=150,
                    hint='Each sentence has one mistake. Write only the missing '
                         'part.' if n == 0 else None,
                    hint_key='e2Hint' if n == 0 else None)]
    for n, rows in enumerate([H2_TENSE[:3], H2_TENSE[3:6], H2_TENSE[6:]]):
        S += [D.gap(n + 1, 3, rows, None, 'tnE', 'Hour 2 &middot; Activity 2',
                    'tnT', 'Simple or progressive?', folder=F, size=17,
                    width=170,
                    hint='Find the time word first — it decides the tense.'
                         if n == 0 else None,
                    hint_key='tnHint' if n == 0 else None)]
    for n, rows in enumerate([H2_PARA[:3], H2_PARA[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'paE', 'Hour 2 &middot; Activity 3',
                    'paT', "Mia's Saturday — present simple", folder=F,
                    size=18, width=150,
                    hint='Use the present simple form of the verb in brackets.'
                         if n == 0 else None,
                    hint_key='paHint' if n == 0 else None)]
    for n, rows in enumerate([H2_PROG[:3], H2_PROG[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'pgE', 'Hour 2 &middot; Activity 4',
                    'pgT', 'Write the progressive form', folder=F, size=17,
                    width=180,
                    hint='am / is / are, then the verb with -ing. Short forms '
                         'are fine.' if n == 0 else None,
                    hint_key='pgHint' if n == 0 else None)]
    for n, rows in enumerate([H2_NEG[:3], H2_NEG[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'ngE', 'Hour 2 &middot; Activity 5',
                    'ngT', 'Make it negative', folder=F, size=17, width=200,
                    hint="don't or doesn't, then the basic verb. Full forms are "
                         'accepted too.' if n == 0 else None,
                    hint_key='ngHint' if n == 0 else None)]
    S += [D.match(H2_MATCH, 'mtE', 'Hour 2 &middot; Activity 6', 'mtT',
                  'Match the verb to its she / he / it form', 'mtHint',
                  'Click a verb, then click the form that goes with she, he or '
                  'it.',
                  'Watch the spelling group: <strong>-o, -ch, -sh</strong> take '
                  '<em>-es</em>, and a consonant before <em>-y</em> gives '
                  '<em>-ies</em>.', folder=F)]

    # ── Hour 3 ──
    S += [D.teach('reE', 'Hour 3 &middot; Past simple', 'reT',
                  'Most verbs simply take -ed',
                  [('re1h', 'The rule',
                    'watch → watch<strong>ed</strong> &middot; look → '
                    'look<strong>ed</strong>',
                    're1n', 'This covers most verbs in the language. Learn it '
                    'first, then learn the exceptions.'),
                   ('re2h', 'Small spelling changes',
                    'like → liked &middot; stop → stopped &middot; study → '
                    'studied',
                    're2n', 'Ends in -e: add only -d. Short word with one '
                    'consonant: double it.'),
                   ('re3h', 'Some verbs change completely',
                    'go → went, not <em>goed</em>',
                    're3n', 'These are the irregular verbs. There is no rule '
                    'for them — the next two slides are the ones to learn.')],
                  folder=F)]
    IRR = [('go', 'went'), ('eat', 'ate'), ('see', 'saw'), ('buy', 'bought'),
           ('find', 'found'), ('write', 'wrote'), ('come', 'came'),
           ('make', 'made'), ('take', 'took'), ('have', 'had'), ('run', 'ran'),
           ('give', 'gave'), ('know', 'knew')]
    for n, group in enumerate([IRR[:7], IRR[7:]]):
        cards, i = [], 0
        while i < len(group):
            pair = group[i:i + 3]
            cards.append((None,
                          ' &middot; '.join(a for a, _ in pair),
                          ' &middot; '.join(b for _, b in pair), None, None))
            i += 3
        S += [D.teach('irE', 'Hour 3 &middot; Irregular verbs', 'irT%d' % (n + 1),
                      'The thirteen you must know (%d of 2)' % (n + 1), cards,
                      folder=F)]
    S += [D.teach('ddE', 'Hour 3 &middot; Negatives and questions', 'ddT',
                  "After did and didn't, the verb goes basic",
                  [('dd1h', 'Positive',
                    'I watch<strong>ed</strong> a film.',
                    None, None),
                   ('dd2h', 'Negative',
                    "I <strong>didn't watch</strong> a film.",
                    'dd2n', 'Not <em>didn\'t watched</em>. The past is already '
                    'inside <em>didn\'t</em>.'),
                   ('dd3h', 'Question',
                    '<strong>Did</strong> you <strong>watch</strong> a film?',
                    'dd3n', 'Not <em>Did you watched?</em> — same reason. This '
                    'is the single most tested rule in Hour 3.')],
                  folder=F),
          D.teach('tkE', 'Hour 3 &middot; Time markers', 'tkT',
                  'The words that put a sentence in the past',
                  [('tk1h', 'Pointing back from now',
                    'yesterday &middot; last week &middot; two days ago',
                    'tk1n', 'German: gestern, letzte Woche, vor zwei Tagen.'),
                   ('tk2h', 'Moving the story on',
                    'later &middot; the next morning &middot; a week later',
                    'tk2n', 'These count from the last event, not from now.'),
                   ('tk3h', 'suddenly = unexpectedly',
                    'Suddenly, he heard a noise.',
                    'tk3n', 'German <em>plötzlich</em>. It does <em>not</em> '
                    'mean quickly — it means nobody saw it coming.')],
                  folder=F)]

    for n, rows in enumerate([H3_PAST_A, H3_PAST_B]):
        S += [D.gap(n + 1, 2, rows, None, 'pvE', 'Hour 3 &middot; Activity 1',
                    'pvT', 'Write the past form', folder=F, size=19, width=170,
                    hint='Careful — not every verb here is irregular.',
                    hint_key='pvHint')]
    S += [D.match(H3_MATCH, 'm3E', 'Hour 3 &middot; Activity 2', 'm3T',
                  'Match the verb to its past form', 'm3Hint',
                  'Click a verb, then click its past form.',
                  'All six are irregular, and three of them (run, give, know) '
                  'are the ones learners most often miss.', folder=F)]
    for n, rows in enumerate([H3_ERR[:3], H3_ERR[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'e3E', 'Hour 3 &middot; Activity 3',
                    'e3T', 'Fix the mistake', folder=F, size=16, width=130,
                    hint='Write only the missing verb.' if n == 0 else None,
                    hint_key='e3Hint' if n == 0 else None)]
    S += [D.order(H3_ORDER, 'orE', 'Hour 3 &middot; Activity 4', 'orT',
                  "Put Tom's story in order", 'orHint',
                  'Click the sentences in the order they happened.',
                  'Follow the time markers: <em>five years ago</em> starts it, '
                  '<em>suddenly</em> and <em>the next morning</em> come while '
                  'the egg is still closed, and <em>five years later</em> ends '
                  'it.', folder=F)]
    for n, rows in enumerate([H3_STORY[:3], H3_STORY[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'stE', 'Hour 3 &middot; Activity 5',
                    'stT', 'The bright light — past simple', folder=F,
                    size=18, width=150,
                    hint='Use the past simple of the verb in brackets.'
                         if n == 0 else None,
                    hint_key='stHint' if n == 0 else None)]
    for n, rows in enumerate([H3_Q[:3], H3_Q[3:]]):
        S += [D.gap(n + 1, 2, rows, None, 'qE', 'Hour 3 &middot; Activity 6',
                    'qT', 'Write the question', folder=F, size=16, width=110,
                    hint='Two gaps each: the question word, then the verb.'
                         if n == 0 else None,
                    hint_key='qHint' if n == 0 else None)]
    S += ["".join(D.mc(i + 1, len(H3_TM), q, 'tmE', 'Hour 3 &middot; Activity 7',
                       'tmT', 'Choose the time marker', folder=F)
                  for i, q in enumerate(H3_TM))]

    S += [D.results(),
          D.activate('Tell it, then write it', 'Use at least four:',
                     ['went', 'saw', 'suddenly', 'the next morning',
                      "didn't", 'Did you…?', 'is happening now'],
                     'Speaking &middot; in pairs',
                     'One of you saw something strange last night. The other is '
                     'the reporter.',
                     ['Reporter: ask four questions with <em>Did you…?</em> '
                      'Every verb after <em>did</em> stays basic.',
                      'Witness: tell what happened, in order. Use '
                      '<em>suddenly</em> once and <em>the next morning</em> '
                      'once.',
                      'Witness: say one thing you do <em>every day</em>, and '
                      'one thing that is happening <em>right now</em>.',
                      'Both: agree on one sentence for the newspaper, in the '
                      'past simple, under twelve words.'],
                     'Writing &middot; 100&ndash;120 words',
                     'Write the story of a strange night. Start with a time '
                     'marker, keep it in the past simple, and use at least '
                     'three irregular verbs.',
                     'Last night, I went into the garden. Suddenly, …')]
    return S


if __name__ == '__main__':
    import i18n_exam1
    slides = "".join(build())
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Out of This World — 5-Hour English Test Prep · Part I',
                   i18n_exam1)
    s = s.replace('</style>\n</head>', COVER_CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes' % (OUT, len(s)))
