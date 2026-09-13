# -*- coding: utf-8 -*-
"""Saving Fawns from the Mower (B1) — rebuilt as a 16:9 deck.

Replaces the hand-authored scrolling quiz page. Two defects were found and
fixed on the source page this session, before the rebuild started, and are
carried over rather than redone:

1. Every one of the 28 MC keys was authored at index 0. Shuffling position
   alone did not fix it — the correct option was also written with visibly
   more detail than the distractors in 6 of 8 reading items, so length gave
   the answer away regardless of where it sat. Both the position and the
   distractor lengths were fixed on the source page; `deck.assert_no_key_is_longest`
   re-verifies it here.

Artwork: two flat-vector dusk/dawn scenes already existed
(`deer-sunset-hero.png`, `deer-mountain-hero.png`); three more were
commissioned in the same style per HOUSE-STYLE §5c, one per remaining
section (vocabulary, word-sort, activation), since a hero plus one swap is
not enough background variety for a five-section lesson.

Word Sorting has a dedicated `sort` slide type in the engine (bins + items),
not a generic `match` — used here instead of forcing it into a term/definition
shape.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from saving_fawns_b1_data import READING, VOCAB, GRAMMAR, SORT_PAIRS, CATEGORY_LABEL

TPL = 'lesson-template/lesson-template.html'
OUT = 'saving-fawns-mower-b1.html'
F = 'Animal Welfare'

# python3 lesson-template/extract-palette.py "Animal Welfare/hero.jpg"
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #090d0e;
  --surface       : #121a1c;
  --surface2      : #1a2629;
  --border        : #aa4e47;
  --text          : #f5f2f2;
  --text-dim      : #bfa5a3;
  --accent        : #e77970;
  --accent-bright : #f4b0aa;
  --accent-dim    : #d1372a;
  --secondary     : #0c171a;
  --contrast      : #1ded98;''' % F

CHIPS = ['fawn', 'doe', 'drone', 'thermal imaging camera', 'combine harvester',
         'drone pilot', 'volunteer', 'relocate', 'gloves']

CATS = ['people', 'equipment', 'animals', 'actions']
CAT_KEYS = ['catPeople', 'catEquipment', 'catAnimals', 'catActions']
BINS = [CATEGORY_LABEL[c] for c in CATS]
SORT_ITEMS = [(word, CATS.index(cat)) for word, cat in SORT_PAIRS]


def build():
    D.assert_no_key_is_longest(READING, 'Reading')
    D.assert_no_key_is_longest(VOCAB, 'Vocab')
    D.assert_no_key_is_longest(GRAMMAR, 'Grammar')
    logo = D.logo_from(TPL)

    vocab_terms = [
        ('t1h', 'fawn', 't1b', 'a baby deer', None, ''),
        ('t2h', 'doe', 't2b', 'a mother deer', None, ''),
        ('t3h', 'instinct', 't3b', 'natural behaviour, not learned', None, ''),
        ('t4h', 'drone', 't4b', 'a small flying machine, no pilot inside', None, ''),
        ('t5h', 'drone pilot', 't5b', 'the person flying the drone', None, ''),
        ('t6h', 'thermal imaging camera', 't6b', 'a camera that sees heat', None, ''),
        ('t7h', 'combine harvester', 't7b', 'a big machine that cuts fields', None, ''),
        ('t8h', 'volunteer', 't8b', 'a person who helps for free', None, ''),
        ('t9h', 'to mow', 't9b', 'to cut grass or crops with a machine', None, ''),
        ('t10h', 'to spot', 't10b', 'to see or notice something', None, ''),
        ('t11h', 'to relocate', 't11b', 'to move something a short distance', None, ''),
        ('t12h', 'gloves', 't12b', 'you wear these on your hands', None, ''),
    ]
    voc_slides = ''.join(
        D.teach('vocEyebrow', 'Before you read',
                'vocTitle%d' % (n + 1), 'Key vocabulary (%d/3)' % (n + 1),
                vocab_terms[n * 4:n * 4 + 4],
                folder=F, bg='hero.jpg')
        for n in range(3)
    )

    passage = [
        ('read1Title', 'Why fawns are at risk', 'p1h', 'A simple instinct', 'p1b',
         'Every spring, deer have babies in the tall grass and fields. A baby deer is '
         'called a <strong>fawn</strong>. A fawn has almost no smell, so foxes cannot '
         'find it easily. When a fawn feels danger, it does something simple: it stays '
         'completely still. This works well against foxes. But it does not work against '
         'a big farm machine called a <strong>combine harvester</strong>. The machine '
         'cannot see a small fawn hiding in the grass.'),
        ('read2Title', 'How drones find them', 'p2h', 'Eyes in the sky', 'p2b',
         'This is why many volunteers now use drones to help. A <strong>drone</strong> '
         'is a small flying machine with a camera. Early in the morning, the drone flies '
         'over the field. The camera can see body heat. In the cool morning air, a '
         "fawn&rsquo;s warm body is easy to see on the camera. Later in the day, the "
         'whole field gets warm from the sun, so this does not work anymore. That is why '
         'the drone teams fly at dawn.'),
        ('read3Title', 'What the rescue team does', 'p3h', 'The rescue', 'p3b',
         'When the drone pilot finds a fawn, a small team walks to it. They wear gloves. '
         'Why? Because the mother deer might not want her baby anymore if it smells like '
         'a human. The team does not carry the fawn far away. They put a box or some '
         'branches over it, near the same spot. This keeps the fawn safe while the '
         'farmer cuts the field. After the work is finished, the team lets the fawn go '
         'again, close to where they found it.'),
        ('read4Title', 'Who makes it work', 'p4h', 'Teamwork, and the numbers', 'p4b',
         'This project needs many different people working together: farmers, hunters, '
         'drone pilots, and volunteers. Farmers tell the team when they plan to cut a '
         'field. Then the team can check it first. In German, people call an accident '
         'like this a &ldquo;M&auml;htod&rdquo; &mdash; it means &ldquo;mowing '
         'death&rdquo;. With good teamwork, one region can save many thousands of fawns '
         'every year.'),
    ]
    read_slides = ''.join(
        D.teach('readEyebrow', 'The article', title_key, title,
                [(head_key, head, body_key, body, None, '')],
                cols='1fr', folder=F, bg='hero.jpg')
        for title_key, title, head_key, head, body_key, body in passage
    )

    grammar_intro = D.teach(
        'grammarEyebrow', 'Before the questions',
        'grammarTitle', 'Three patterns from the text',
        [('gc1h', 'Passive present simple', 'gc1b',
          'Use <strong>am/is/are + past participle</strong> when the action matters '
          'more than who does it: &ldquo;Fawns <em>are found</em> early in the '
          'morning.&rdquo;', None, ''),
         ('gc2h', 'First conditional', 'gc2b',
          '<strong>If + present simple, &hellip; will + infinitive</strong>, for a '
          'real, likely situation: &ldquo;If a pilot <em>spots</em> a fawn early, the '
          'team <em>will have</em> time to help.&rdquo;', None, ''),
         ('gc3h', 'Must, don&rsquo;t have to, should', 'gc3b',
          '<strong>Must</strong> = a strong rule. <strong>Don&rsquo;t have to</strong> '
          '= not necessary. <strong>Should</strong> = friendly advice, not a rule: '
          '&ldquo;You <em>must</em> wear gloves, but you <em>don&rsquo;t have to</em> '
          'carry the fawn far, and you <em>should</em> stay calm.&rdquo;', None, '')],
        folder=F, bg='mountain-dusk.jpg')

    slides = (
        D.cover(logo, 'Saving Fawns from the <em>Mower</em>',
                'Drones, thermal cameras and a rescue network that saves thousands '
                'of fawns every spring',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Reading, vocabulary and grammar'),
                 ('Count', '40 questions')])

        + voc_slides
        + read_slides

        + "".join(D.mc(i + 1, len(READING), q, 'rEyebrow', 'Reading comprehension',
                       'rTitle', 'Answer using the text above',
                       folder=F, bg='hero.jpg', stem_key=q['stem_key'])
                  for i, q in enumerate(READING))

        + "".join(D.mc(i + 1, len(VOCAB), q, 'vEyebrow', 'Vocabulary in context',
                       'vTitle', 'Choose the word that fits',
                       folder=F, bg='drone-thermal.jpg')
                  for i, q in enumerate(VOCAB))

        + D.sort_slide(BINS, SORT_ITEMS,
                       'sortEyebrow', 'Word sorting',
                       'sortTitle', 'Sort each word into its category',
                       'sortHint', 'Match each word to the category it belongs to.',
                       'sortWhy',
                       folder=F, bg='harvester-flag.jpg', bin_keys=CAT_KEYS)

        + grammar_intro
        + "".join(D.mc(i + 1, len(GRAMMAR), q, 'gEyebrow', 'Grammar focus',
                       'gTitle', 'Choose the correct form',
                       folder=F, bg='mountain-dusk.jpg')
                  for i, q in enumerate(GRAMMAR))

        + D.results('resNext', 'You can read the article and use the grammar &rarr;',
                    folder=F, bg='fawn-release.jpg')

        + D.activate('Talk and write about fawn rescue', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs or small groups',
                     'Discuss in pairs or small groups, then compare answers with '
                     'another group.',
                     ['You are a volunteer drone pilot. Explain to a farmer, in simple '
                      'terms, why he must tell your team his mowing dates in advance.',
                      'A neighbour says the rescue project is a waste of time and '
                      'money. Defend it &mdash; use at least one number from the text.',
                      'Your team has just found a fawn, and the farmer wants to start '
                      'mowing in ten minutes. Decide together, fast, what you do next.'],
                     'Writing &middot; 150&ndash;250 words',
                     'Write a short public notice for local farmers, explaining the '
                     'fawn rescue project and exactly what you need from them before '
                     'they mow.',
                     'Every spring, our team asks farmers to&hellip;',
                     folder=F, bg='fawn-release.jpg')
    )

    import i18n_saving_fawns_b1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Saving Fawns from the Mower (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    total_mc = len(READING) + len(VOCAB) + len(GRAMMAR)
    print('wrote %s — %d slides, %d MC + %d sort items, %d bytes'
          % (OUT, s.count('<section class="slide'), total_mc, len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
