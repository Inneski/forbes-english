# -*- coding: utf-8 -*-
"""Minecraft Trivia (B1) — rebuilt as a 16:9 deck.

`forbes-english-minecraft-editorial.html`, last of the six Minecraft lessons
that this session could take off the scrolling format. All thirty-two scored
items survive: twelve multiple choice (six trivia, six sentence-completions),
six typed numbers, seven strange facts to match and the seven-step run.
EN + DE + ES.

The old activity three called itself drag-and-drop, but it authored four
candidate answers per sentence and then poured six private pools into one
twenty-four-chip tray. Whatever the chips looked like, each item is four
options against one stem, so they are multiple choice here.

What changed, beyond the format:

- **The keys were at C, C, B, C, B, B and then index zero six times.** Never A,
  never D, and the drag pools always keyed their first element. Dealt across all
  four positions in `mced_data.py`, and shuffled again at runtime.
- **Two items had two right answers.** Redstone dust *is* a non-solid block, and
  a Notch Apple *does* cure a zombie villager &mdash; the stems certified both.
  Re-pointed at a stone slab and a bottle of honey, where the key is
  unambiguous.
- **Question six's key was the only long option**, and two typed gaps accepted
  one spelling where the frame admitted several.
- **The seven-step sequence was seven full sentences** in a chunk pool, 60 to
  108 characters. Short labels now, with the sentences in the explanation.
- **It now teaches.** The original was five activities and every rule in the
  feedback, which on a trivia lesson means it taught nothing at all. Three
  slides now name the language the items are actually built out of: the
  change-of-state verbs and the passive that game rules are written in, the
  reading skill the multiple choice trains (four long options that differ by one
  clause), and the numbers and hyphenated premodifiers the detail lives in.

Three things in the content are left as found. The matching activity restates
the keys of questions one, three and five almost verbatim, so a learner who did
activity one gets three of the seven free. The cats explanation is circular. And
the sand explanation invents a floor-check mechanic the game does not have.
None is a defect the format can fix; each wants a rewrite.

**This deck borrows Minecraft B1's artwork, and that is the thing to fix
first.** Every flat-vector Minecraft illustration in `minecraft/` is already
the hero or a background of Past Modals or Tense Review. The three rendered
night scenes that were left are a Twin Peaks homage &mdash; recognisable
characters in the Red Room, and a "Welcome to Twin Peaks" sign legible in the
corner of the widest one. That is somebody else's work on a published lesson
cover, so it is not going out, and cropping the sign out does not fix what the
rest of the frame still is. So this deck points at `MinecraftB1/` and rotates
its accent to keep the two apart on screen.

Four flat-vector Minecraft scenes in the house family would replace this
properly: something at night with mobs, a piston or redstone contraption, a
Nether portal, and the End. Change `F` and the three filenames below and rerun.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. The accent is rotated because two decks cannot share one palette
and one artwork set and still read as two decks; everything else is
`extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from mced_data import MC, FIB, MATCH, ORDER

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-minecraft-editorial.html'
F = 'MinecraftB1'

# python3 lesson-template/extract-palette.py MinecraftB1/hero.jpg \
#            --accent-hue=330 --accent-sat=0.6
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2c2727;
  --surface       : #1f1d13;
  --surface2      : #2b291b;
  --border        : #a65a80;
  --text          : #f5f2f4;
  --text-dim      : #bfa3b1;
  --accent        : #e185b3;
  --accent-bright : #f1bcd7;
  --accent-dim    : #c84285;
  --secondary     : #fdd369;
  --contrast      : #1ded21;''' % F

CHIPS = ['turns into', 'is created when', 'can only be obtained by',
         'despite having', 'even though', 'up to', 'exactly', 'only then']

TRIV_BG = ['temple.jpg', 'rex.jpg', 'hero.jpg', 'temple.jpg', 'rex.jpg', 'hero.jpg']
COMP_BG = ['rex.jpg', 'hero.jpg', 'temple.jpg', 'rex.jpg', 'hero.jpg', 'temple.jpg']
FIB_BG = ['hero.jpg', 'temple.jpg', 'rex.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'MinecraftEd')
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Things Only <em>Players</em> Know',
                'Minecraft trivia, and the English that explains how anything turns into '
                'anything else',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Change-of-state verbs &amp; long options'),
                 ('Count', '23 slides')])

        + D.teach('chEyebrow', 'Before the questions',
                  'chTitle', 'How English says a thing became another thing',
                  [('ch1h', 'The change verbs', 'ch1b',
                    'Lightning <strong>transforms</strong> a pig <strong>into</strong> a '
                    'zombie piglin. It <strong>turns into</strong> one; it '
                    '<strong>becomes</strong> one. <em>Transform</em> and <em>turn</em> '
                    'both take <em>into</em>, and neither takes <em>to</em>.',
                    'ch1n', '<em>Revert back into</em> is common in game English, though '
                            '<em>back</em> is doing no work.'),
                   ('ch2h', 'Rules prefer the passive', 'ch2b',
                    'A Charged Creeper <strong>is created when</strong> lightning '
                    'strikes. A sponge <strong>can only be obtained by</strong> defeating '
                    'an Elder Guardian. The doer is the game, so nobody names it.',
                    'ch2n', '<em>By</em> + <em>-ing</em> after a passive: <em>obtained by '
                            'defeating</em>, never <em>by defeat</em>.'),
                   ('ch3h', 'Two conditionals for two kinds of rule', 'ch3b',
                    'Zero for what is always so: <em>if you add a thirteenth block, it '
                    '<strong>doesn&rsquo;t</strong> move</em>. First for what will happen '
                    'to you: <em>if you attack one, nearby piglins <strong>will</strong> '
                    'become hostile</em>.',
                    'ch3n', 'Present in the <em>if</em>-clause either way. Only the '
                            'result half changes.')],
                  folder=F, bg='hero.jpg')

        + D.teach('opEyebrow', 'The reading skill',
                  'opTitle', 'Four options that differ by one clause',
                  [('op1h', 'The noun is never the answer', 'op1b',
                    'Every option here names the same kind of thing. What separates them '
                    'is the clause hung off it: <em>the Gold Pickaxe, <strong>despite '
                    'having</strong> the lowest durability</em>. Scan for the clause, not '
                    'the noun.',
                    'op1n', 'If two options start identically, the difference is '
                            'somewhere after the comma.'),
                   ('op2h', 'Which, who, whose', 'op2b',
                    '<em>Which</em> for items and events, <em>who</em> for mobs treated '
                    'as animate, <em>whose</em> for a property they own: <em>a Charged '
                    'Creeper, <strong>whose</strong> explosion radius is doubled</em>.',
                    'op2n', '<em>Whose</em> is not only for people. It is the possessive '
                            'of <em>which</em> too.'),
                   ('op3h', 'Concession is the giveaway', 'op3b',
                    '<em>Despite</em>, <em>even though</em>, <em>although</em>, '
                    '<em>but</em> mark the surprising fact, and a trivia question is '
                    'usually asking for exactly that. <em>Despite</em> takes a noun or an '
                    '<em>-ing</em>; <em>even though</em> takes a clause.',
                    'op3n', '<em>Despite having</em> the lowest durability &mdash; not '
                            '<em>despite it has</em>.')],
                  folder=F, bg='temple.jpg')

        + D.teach('nuEyebrow', 'The detail',
                  'nuTitle', 'Numbers, and the words hung in front of nouns',
                  [('nu1h', 'Say the number exactly', 'nu1b',
                    'Coordinates go negative: diamonds sit at <strong>Y = -58</strong>, '
                    'read <em>minus fifty-eight</em>. Limits are exact: <em>up to '
                    '<strong>12</strong> blocks</em>, <em>exactly <strong>15</strong> '
                    'bookshelves</em>.',
                    'nu1n', '<em>Up to</em> is a maximum; <em>exactly</em> admits nothing '
                            'either side.'),
                   ('nu2h', 'Compound premodifiers', 'nu2b',
                    'English packs a whole description in front of the noun and '
                    'hyphenates it: a <strong>gravity-affected</strong> block, an '
                    '<strong>iron-tier</strong> tool, a <strong>10-block</strong> radius, '
                    'a <strong>day/night</strong> cycle.',
                    'nu2n', 'The hyphen shows the words are working as one adjective. No '
                            'plural inside it: <em>10-block</em>, not <em>10-blocks</em>.'),
                   ('nu3h', '<em>Re-</em> means again', 'nu3b',
                    'You <strong>respawn</strong> where you last slept, a curable '
                    'villager <strong>reverts</strong> to a villager, and a thrown Eye of '
                    'Ender may be <strong>retrieved</strong>. The prefix is productive '
                    'and predictable.',
                    'nu3n', 'It is the same <em>re-</em> as in <em>rebuild</em>, '
                            '<em>retry</em> and <em>reload</em>.')],
                  folder=F, bg='rex.jpg')

        + "".join(D.mc(i + 1, 6, MC[i], 'mcEyebrow', 'Activity 1 &middot; Trivia',
                       'mcTitle', 'What does a player actually know?',
                       folder=F, bg=TRIV_BG[i])
                  for i in range(6))

        + "".join(D.mc(i + 1, 6, MC[6 + i], 'dndEyebrow',
                       'Activity 2 &middot; Complete the fact',
                       'dndTitle', 'Which word finishes the sentence?',
                       folder=F, bg=COMP_BG[i])
                  for i in range(6))

        + "".join(D.gap(n + 1, 3, part, None,
                        'fibEyebrow', 'Activity 3 &middot; The exact number',
                        'fibTitle', 'Type what the sentence needs',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='Numbers may be written in digits or in words.',
                        width=175, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; The strange facts',
                  'matchTitle', 'Match the thing to what is odd about it',
                  'matchHint', 'Click a name, then click the fact.',
                  'matchWhy', folder=F, bg='hero.jpg')

        + "".join(D.order(chunks, 'ordEyebrow', 'Activity 5 &middot; The run',
                          'ordTitle', 'Put the seven steps in order',
                          'ordHint', 'Click a step to place it, click a placed step to '
                                     'take it back.',
                          why, folder=F, bg='temple.jpg')
                  for chunks, why in ORDER)

        + D.results('resNext', 'You know the facts. Now tell them &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Tell them the thing they do not know', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you knows a game inside out; the other has played it for an '
                     'hour. Three minutes each, then swap.',
                     ['Explain a trick in a game you know, and say why it works.',
                      'Describe something that turns into something else, and what '
                      'triggers it.',
                      'State a rule twice: once as a general truth, once as a warning to '
                      'your partner.',
                      'Tell your partner a fact that surprised you, starting with '
                      '<em>despite</em> or <em>even though</em>.'],
                     'Writing &middot; 150&ndash;180 words',
                     'Write six facts about a game, a sport or a hobby that a beginner '
                     'would not know. State each one as a rule rather than a story, use a '
                     'passive or a change verb in at least three of them, and make at '
                     'least one turn on a concession &mdash; the surprising part is what '
                     'makes a fact worth telling.',
                     'Despite being the weakest tool in the game, the gold pickaxe…',
                     folder=F, bg='rex.jpg')
    )

    import i18n_mced as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Minecraft Trivia Lesson (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d facts, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
