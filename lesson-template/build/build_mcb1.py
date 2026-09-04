# -*- coding: utf-8 -*-
"""Minecraft B1 — rebuilt as a 16:9 deck.

`forbes-english-minecraft-b1.html`, third of the six Minecraft lessons off the
scrolling format. All the scored items survive: six multiple choice, six gaps,
six collocation gaps from a bank, seven glossary pairs and the seven-step first
night. EN + DE + ES.

What changed, beyond the format:

- **Question three's key was in the wrong tense.** The stem asked which sentence
  was grammatically correct and its own feedback called the answer a present
  perfect; the key read *I just built*. It is *I have just built* now, and the
  distractors were lengthened to stop the repair making the key the longest
  option.
- **Gap six taught the present perfect and then asked for a past simple.**
  *I ______ found a village* had no auxiliary, so *just* could not sit where the
  lesson had just explained it sits. The auxiliary is supplied: *I have ______
  found*.
- **Two collocation items had a second correct answer the page itself named** in
  its own feedback, and marked it wrong. *Uncommon* and *consume* are accepted
  now; two others whose alternatives were fully correct English were replaced
  with real B1 errors instead.
- **The keys alternated C, B, C, B, C, B.** Dealt across all four positions in
  `mcb1_data.py`, and the template shuffles them again on every load.
- **The seven-step sequence was seven full sentences in a chunk pool**, 60 to 97
  characters each. Seven of those will not fit the stage without shrinking the
  type, which §6 forbids. They are short labels now and the sentences moved into
  the explanation &mdash; the same repair the DinoFacts timeline needed.
- **It now teaches.** The original had no pre-question content: five activities
  and every rule in the post-answer feedback. Three slides now cover the three
  tenses the questions actually test and what each is for, the fixed pairings
  the collocation activity is built on, and the game vocabulary as ordinary
  English words with a gaming sense &mdash; which is the part a learner can take
  away from the lesson and use somewhere else.

**Artwork is a stopgap and wants replacing.** Every flat-vector Minecraft
illustration in `minecraft/` is already the hero or a background of Past Modals
or Tense Review, and the rest of what is in Innes's Downloads under that name is
a voxel character line-up with weapons and blood — not for a B1 class. So this
deck uses the three rendered Minecraft scenes that were already on disk and
unspoken for: the sunrise world for the cover, the underwater temple, and the
voxel dinosaur. They are a consistent family and they suit the subject, but
three backgrounds across twenty-three slides is thin. Four or five flat-vector
scenes in the house family &mdash; a shelter at dusk, a crafting table, a mine,
a village &mdash; would replace them by editing the filenames below.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. Every other token is `extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from mcb1_data import MC, FIB, DD, DD_BANK, MATCH, ORDER

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-minecraft-b1.html'
F = 'MinecraftB1'

# python3 lesson-template/extract-palette.py MinecraftB1/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2c2c26;
  --surface       : #1f1d13;
  --surface2      : #2b291b;
  --border        : #d6a52a;
  --text          : #f5f4f2;
  --text-dim      : #bfb7a3;
  --accent        : #fdd369;
  --accent-bright : #ffc42f;
  --accent-dim    : #f6b615;
  --secondary     : #12589a;
  --contrast      : #1dbbed;''' % F

CHIPS = ['you have to', 'otherwise', 'I have just', 'for two hours',
         'when I find', 'take damage', 'spawn point', 'first, then, after that']

MC_BG = ['temple.jpg', 'rex.jpg', 'hero.jpg', 'temple.jpg', 'rex.jpg', 'hero.jpg']
FIB_BG = ['rex.jpg', 'temple.jpg', 'hero.jpg']
DD_BG = ['temple.jpg', 'hero.jpg', 'rex.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'MinecraftB1')
    D.assert_bank_is_not_a_key(DD_BANK, [a[0] for _, a, _ in DD])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Surviving the <em>First Night</em>',
                'The tenses a player needs to tell the story, and the words the game '
                'gives them',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Tense choice &amp; game vocabulary'),
                 ('Count', '20 slides')])

        + D.teach('tnEyebrow', 'Before the questions',
                  'tnTitle', 'Three tenses, three jobs',
                  [('tn1h', 'What you always do', 'tn1b',
                    'The present simple carries habits and rules: <em>when I find '
                    'diamonds, I <strong>always make</strong> armour</em>. It is the '
                    'tense for what is true every time, not what is happening now.',
                    'tn1n', '<em>Every morning I am checking my chest</em> is the '
                            'classic B1 slip. A routine is not in progress.'),
                   ('tn2h', 'What has just happened', 'tn2b',
                    'The present perfect links a finished action to now: <em>I '
                    '<strong>have just</strong> found a village</em>. <em>Just</em> '
                    'means a moment ago, <em>already</em> means sooner than expected, '
                    '<em>yet</em> means still not.',
                    'tn2n', 'Add <em>yesterday</em> and it breaks &mdash; a finished '
                            'time needs the past simple.'),
                   ('tn3h', 'How long it has been going on', 'tn3b',
                    '<em>I <strong>have been playing for</strong> two hours</em>. The '
                    'activity is still running and the sentence measures it. '
                    '<strong>For</strong> takes a length of time; <strong>since</strong> '
                    'takes a starting point.',
                    'tn3n', '<em>For two hours</em>, <em>since Tuesday</em>. Ask whether '
                            'the word names a stretch or a moment.')],
                  folder=F, bg='hero.jpg')

        + D.teach('coEyebrow', 'The pairings',
                  'coTitle', 'The word the game actually uses',
                  [('co1h', 'Verbs that only take one noun', 'co1b',
                    'You <strong>sleep in</strong> a bed, not rest in one. You '
                    '<strong>take damage</strong>, never make it. You '
                    '<strong>carry</strong> a torch, you do not wear it. Each pairing is '
                    'fixed and has to be learned whole.',
                    'co1n', '<em>Make damage</em> is the commonest of these errors, and '
                            'it is not English.'),
                   ('co2h', 'Words that describe how often', 'co2b',
                    'Diamonds are <strong>rare</strong>, or <em>uncommon</em> &mdash; '
                    'that is about how seldom they appear. <em>Difficult</em> and '
                    '<em>hard</em> are about the effort of getting them, which is a '
                    'different claim.',
                    'co2n', 'Rare things can be easy to get once found. The two words '
                            'are not interchangeable.'),
                   ('co3h', 'The connector that warns', 'co3b',
                    '<strong>Otherwise</strong> introduces what happens if you do not: '
                    '<em>build a shelter, <strong>otherwise</strong> mobs will '
                    'attack</em>. <em>Or</em> and <em>or else</em> do the same job in a '
                    'lower register.',
                    'co3n', 'It always points forward to a consequence, and the '
                            'consequence is always the bad one.')],
                  folder=F, bg='temple.jpg')

        + D.teach('vcEyebrow', 'The vocabulary',
                  'vcTitle', 'Game words that are ordinary English underneath',
                  [('vc1h', '<em>Spawn</em> and <em>respawn</em>', 'vc1b',
                    'To <strong>spawn</strong> is to appear in the world &mdash; the '
                    'first time, or after dying. The <em>re-</em> in '
                    '<strong>respawn</strong> means again, exactly as it does in '
                    '<em>rebuild</em> and <em>retry</em>.',
                    'vc1n', 'Your <em>spawn point</em> is where you reappear: your bed, '
                            'or where the world started you.'),
                   ('vc2h', '<em>Craft</em>, <em>mine</em>, <em>smelt</em>', 'vc2b',
                    'To <strong>craft</strong> is to make something with skill from '
                    'materials. To <strong>mine</strong> is to dig for stone, coal or '
                    'iron. To <strong>smelt</strong> is to heat raw ore in a furnace '
                    'until it becomes usable metal.',
                    'vc2n', 'All three are real English outside the game, and all three '
                            'mean the same thing there.'),
                   ('vc3h', '<em>Mob</em>, <em>biome</em>, <em>inventory</em>', 'vc3b',
                    'A <strong>mob</strong> is any moving creature, friendly or not. A '
                    '<strong>biome</strong> is a region with its own weather, plants and '
                    'landscape. Your <strong>inventory</strong> is everything you are '
                    'carrying.',
                    'vc3n', '<em>Biome</em> and <em>inventory</em> are used unchanged in '
                            'geography and in business.')],
                  folder=F, bg='rex.jpg')

        + "".join(D.mc(i + 1, len(MC), q, 'mcEyebrow',
                       'Activity 1 &middot; Multiple choice',
                       'mcTitle', 'What do you know, and how do you say it?',
                       folder=F, bg=MC_BG[i])
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, 3, part, None,
                        'fibEyebrow', 'Activity 2 &middot; The exact word',
                        'fibTitle', 'Complete the sentence',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='The clue in brackets tells you what kind of word you need.',
                        width=175, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + "".join(D.gap(n + 1, 3, part, DD_BANK if n == 0 else None,
                        'dndEyebrow', 'Activity 3 &middot; The right pairing',
                        'dndTitle', 'Which phrase belongs?',
                        folder=F, bg=DD_BG[n], hint_key='dndHint',
                        hint='Twenty-four phrases, six gaps. Most of them belong to no '
                             'gap here.',
                        width=185, size=17)
                  for n, part in enumerate([DD[:2], DD[2:4], DD[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; The glossary',
                  'matchTitle', 'Match the term to its meaning',
                  'matchHint', 'Click a term, then click what it means.',
                  'matchWhy', folder=F, bg='temple.jpg')

        + "".join(D.order(chunks, 'ordEyebrow',
                          'Activity 5 &middot; The first night',
                          'ordTitle', 'Put the seven steps in order',
                          'ordHint', 'Click a step to place it, click a placed step to '
                                     'take it back.',
                          why, folder=F, bg='rex.jpg')
                  for chunks, why in ORDER)

        + D.results('resNext', 'You survived the night. Now explain it &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Tell someone how to survive', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you has played for years, the other has never opened the '
                     'game. Three minutes each, then swap.',
                     ['Explain the first ten minutes of a new world to someone who has '
                      'never played anything.',
                      'Say what you have been doing in a game recently and what you have '
                      'just finished.',
                      'Describe your routine in a game you play &mdash; what you always '
                      'do, and in what order.',
                      'Warn your partner about three dangers, using <em>otherwise</em> '
                      'each time.'],
                     'Writing &middot; 120&ndash;150 words',
                     'Write the survival guide you would give a friend on their first '
                     'night. Say what they must do and in what order, what happens '
                     'otherwise, and what you have learned from playing. Use the present '
                     'simple for the rules and the present perfect for your own '
                     'experience.',
                     'The first thing you have to do is…',
                     folder=F, bg='temple.jpg')
    )

    import i18n_mcb1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Minecraft B1 Lesson | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairings, %d glossary, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(DD),
             len(MATCH), len(s)))


if __name__ == '__main__':
    build()
