# -*- coding: utf-8 -*-
"""Saving Fawns from the Mower (B1-B2) — rebuilt as a 16:9 deck.

Sibling of `build_saving_fawns_b1.py`, same Animal Welfare art family, same
two defects found and fixed before this rebuild (every key authored at
index 0; the correct option written noticeably longer than the distractors
on several items) — see `saving_fawns_b1b2_data.py`.

The original scrolling page used the two hero images the other way round
from the B1 page: `deer-mountain-hero.png` as ITS cover, `deer-sunset-hero`
as a secondary. Kept that split here rather than defaulting both lessons
to the same cover — it's a free distinction the source content already
made, and it means the family's two lessons don't look identical at the
top of the library.

Same lesson-specific style as the B1 sibling, applied identically per
Innes's "in both": centred slide-body text, and the Forbes glyph + word
recoloured to a muted green via the palette's own --contrast token.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from saving_fawns_b1b2_data import READING, VOCAB, GRAMMAR, SORT_PAIRS, CATEGORY_LABEL

TPL = 'lesson-template/lesson-template.html'
OUT = 'saving-fawns-mower-b1-b2.html'
F = 'Animal Welfare'

# python3 lesson-template/extract-palette.py "Animal Welfare/mountain-dusk.jpg"
PALETTE = '''  --hero: url('%s/mountain-dusk.jpg');

  --void          : #0a100c;
  --surface       : #131e17;
  --surface2      : #1b2b20;
  --border        : #dc8668;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #fcc2ae;
  --accent-bright : #ffbda6;
  --accent-dim    : #f4815a;
  --secondary     : #9ab5c9;
  --contrast      : #1dedbe;''' % F

CHIPS = ['fawn', 'doe', 'combine harvester', 'thermal imaging camera',
         'drone pilot', 'volunteer', 'relocate', 'deterrent device']

# Innes, 2026-09-13: same lesson-specific style as the B1 sibling, applied
# identically ("in both") — centred slide-body text, and the Forbes glyph +
# word recoloured to a muted green via the palette's own counterpoint token
# rather than a hand-picked hex.
CSS = """
<style>
:root {
  --logo-mark: color-mix(in srgb, var(--contrast) 45%, var(--text-dim));
  --logo-word: var(--logo-mark);
}
.slide-body { align-items: center; text-align: center; }
.slide-body > .prose, .q-stem, .q-ctx, .order-hint {
  margin-left: auto; margin-right: auto;
}
.opts { justify-items: center; }
.opt { text-align: center; }
.cols { justify-items: center; }
.card { text-align: center; }
.act-list { list-style-position: inside; }
.act-target { justify-content: center; }
</style>
"""

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
        ('t1h', 'fawn', 't1b', 'a young deer, especially with its mother', None, ''),
        ('t2h', 'doe', 't2b', 'a female deer, the mother of a fawn', None, ''),
        ('t3h', 'instinct', 't3b', 'natural, unlearned behaviour', None, ''),
        ('t4h', 'combine harvester', 't4b', 'a large machine that cuts and processes crops', None, ''),
        ('t5h', 'thermal imaging camera', 't5b', 'a camera that detects heat instead of light', None, ''),
        ('t6h', 'to relocate', 't6b', 'to move something to a different place, often temporarily', None, ''),
    ]
    voc_slides = ''.join(
        D.teach('vocEyebrow', 'Before you read',
                'vocTitle%d' % (n + 1), 'Key vocabulary (%d/2)' % (n + 1),
                vocab_terms[n * 3:n * 3 + 3],
                folder=F, bg='mountain-dusk.jpg')
        for n in range(2)
    )

    passage = [
        ('read1Title', 'Why the freezing instinct fails', 'p1h',
         'An instinct with no answer for machines', 'p1b',
         'Every spring, deer give birth in the tall grass and meadows of the countryside. '
         'A newborn fawn has almost no scent and cannot run fast, so its main defence '
         'against danger is a simple instinct: freeze completely still and stay hidden in '
         'the grass. This instinct works well against foxes and wild boar &mdash; but it '
         'fails completely against something a fawn has never evolved to recognise: a '
         '<strong>combine harvester</strong>. A farmer cutting a field in early summer '
         'often cannot see a fawn lying motionless in the grass until it is far too late.'),
        ('read2Title', 'Reading the field from above', 'p2h',
         'Eyes in the cool morning air', 'p2b',
         'This is why a growing network of volunteers now flies drones fitted with '
         '<strong>thermal imaging cameras</strong> over fields in the very early morning, '
         'just before the mowing season begins. At dawn, the ground is still cool, and a '
         "fawn's body heat stands out clearly on camera as a bright shape against a cool, "
         'dark background &mdash; a difference that disappears by mid-morning, once the '
         'sun has warmed the whole field.'),
        ('read3Title', 'A careful, temporary rescue', 'p3h',
         'Minimal contact, minimal disturbance', 'p3b',
         'When a drone pilot spots a fawn, they alert a small ground team, who approach '
         'the animal carefully &mdash; usually wearing gloves and avoiding leaving their '
         'scent behind, since a doe may reject a fawn that smells of humans. The fawn '
         "isn't carried away. Instead, it's temporarily placed under a box or behind a "
         "barrier of cut branches, safely out of the mower's path. Once the field has "
         'been cut, the fawn is released again close to where it was found, so the doe '
         'can find it.'),
        ('read4Title', 'A network that depends on cooperation', 'p4h',
         'Farmers, hunters, pilots and volunteers', 'p4b',
         "This work depends on close cooperation between people who don't always see the "
         'countryside the same way: farmers, hunters, drone pilots, and volunteer '
         'conservationists. Farmers announce their mowing dates in advance; hunters and '
         'local rescue groups organise teams; drone pilots donate their time and their '
         'expensive thermal equipment. In German, conservationists sometimes call an '
         'unnecessary fawn death the &ldquo;M&auml;htod&rdquo; &mdash; literally, '
         '&ldquo;mowing death.&rdquo; In a single season, a well-organised regional '
         'network can locate and relocate several thousand fawns before the blades ever '
         'reach them.'),
    ]
    read_slides = ''.join(
        D.teach('readEyebrow', 'The article', title_key, title,
                [(head_key, head, body_key, body, None, '')],
                cols='1fr', folder=F, bg='mountain-dusk.jpg')
        for title_key, title, head_key, head, body_key, body in passage
    )

    grammar_intro = D.teach(
        'grammarEyebrow', 'Before the questions',
        'grammarTitle', 'Three patterns from the article',
        [('gc1h', 'Passive present simple', 'gc1b',
          'Use <strong>am/is/are + past participle</strong> when the action matters '
          'more than who does it: &ldquo;Thousands of fawns <em>are found</em> hidden '
          'in fields across the countryside.&rdquo;', None, ''),
         ('gc2h', 'First conditional', 'gc2b',
          '<strong>If + present simple, &hellip; will + infinitive</strong>, for a '
          'real, likely situation: &ldquo;If a pilot <em>spots</em> a fawn early, the '
          'team <em>will have</em> time to act.&rdquo;', None, ''),
         ('gc3h', 'Must, don&rsquo;t have to, should', 'gc3b',
          '<strong>Must</strong> = an essential rule. <strong>Don&rsquo;t have '
          'to</strong> = not legally necessary. <strong>Should</strong> = sensible '
          'advice, not a rule: &ldquo;You <em>must</em> wear gloves, farmers '
          '<em>don&rsquo;t have to</em> report mowing dates by law, and you '
          '<em>should</em> approach a fawn calmly.&rdquo;', None, '')],
        folder=F, bg='harvester-signal.jpg')

    slides = (
        D.cover(logo, 'Saving Fawns from the <em>Mower</em>',
                'Every spring, drone pilots fly thermal cameras over fields at dawn to '
                'find fawns hidden in the grass &mdash; before the combine harvesters '
                'arrive',
                [('Level', 'B1&ndash;B2 &middot; Upper intermediate'),
                 ('Focus', 'Reading, vocabulary and grammar'),
                 ('Count', '40 questions')])

        + voc_slides
        + read_slides

        + "".join(D.mc(i + 1, len(READING), q, 'rEyebrow', 'Reading comprehension',
                       'rTitle', 'Answer based on the article above',
                       folder=F, bg='mountain-dusk.jpg', stem_key=q['stem_key'])
                  for i, q in enumerate(READING))

        + "".join(D.mc(i + 1, len(VOCAB), q, 'vEyebrow', 'Vocabulary in context',
                       'vTitle', 'Choose the word that fits',
                       folder=F, bg='drone-pastel-sky.jpg')
                  for i, q in enumerate(VOCAB))

        + D.sort_slide(BINS, SORT_ITEMS,
                       'sortEyebrow', 'Word sorting',
                       'sortTitle', 'Sort each word into its category',
                       'sortHint', 'Match each word to the category it belongs to.',
                       'sortWhy',
                       folder=F, bg='harvester-daylight.jpg', bin_keys=CAT_KEYS)

        + grammar_intro
        + "".join(D.mc(i + 1, len(GRAMMAR), q, 'gEyebrow', 'Grammar focus',
                       'gTitle', 'Choose the correct form',
                       folder=F, bg='harvester-signal.jpg')
                  for i, q in enumerate(GRAMMAR))

        + D.results('resNext', 'You can read the article and use the grammar &rarr;',
                    folder=F, bg='fawn-meadow.jpg')

        + D.activate('Talk and write about fawn rescue', 'Use at least four:', CHIPS,
                     'Discussion &middot; in pairs or small groups',
                     'Discuss in pairs or small groups, then compare answers with '
                     'another group.',
                     ['You are a volunteer drone pilot. Explain to a farmer, in clear '
                      'terms, why he must tell your team his mowing dates in advance.',
                      'A neighbour says the rescue network is a waste of time and '
                      'money. Defend it &mdash; use at least one figure from the '
                      'article.',
                      'Your team has just found a fawn, and the farmer wants to start '
                      'mowing in ten minutes. Decide together, fast, what you do next.'],
                     'Writing &middot; 150&ndash;250 words',
                     'Write a short public notice for local farmers, explaining the '
                     'fawn rescue network and exactly what you need from them before '
                     'they mow.',
                     'Every spring, our network asks farmers to&hellip;',
                     folder=F, bg='fawn-meadow.jpg')
    )

    import i18n_saving_fawns_b1b2 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Saving Fawns from the Mower (B1-B2) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    s = s.replace('</head>', CSS + '</head>', 1)
    open(OUT, 'w', encoding='utf-8', newline='').write(s)
    total_mc = len(READING) + len(VOCAB) + len(GRAMMAR)
    print('wrote %s — %d slides, %d MC + %d sort items, %d bytes'
          % (OUT, s.count('<section class="slide'), total_mc, len(SORT_ITEMS), len(s)))


if __name__ == '__main__':
    build()
