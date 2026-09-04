# -*- coding: utf-8 -*-
"""Minecraft C1 — rebuilt as a 16:9 deck.

`forbes-english-minecraft-c1.html`, fourth of the six Minecraft lessons off the
scrolling format. All thirty-one scored items survive: twelve multiple choice
(six on register, six on collocation), six gaps from a bank, seven terms to
match and the six-sentence paragraph. EN + DE + ES.

The old activity three called itself drag-and-drop, but each gap carried its
own four candidate phrases with three errors written for that sentence alone
&mdash; <em>comply to</em>, <em>capitalised at</em>. Pooling those into one bank
would destroy the contrast that makes each item work, so they are multiple
choice here, which is what they always were.

What changed, beyond the format:

- **Eleven of twelve keys sat at position one or two.** Activity three keyed
  element zero of every pool, and activity one ran 1, 1, 2, 1, 2, 0. Dealt
  across all four positions in `mcc1_data.py`, and shuffled again at runtime.
- **Five keys were the only longest option**, one of them by 43 characters
  &mdash; and on a lesson where the register *is* the answer, length is exactly
  the wrong signal, because the formal option is naturally the longer one.
  Every distractor was lengthened; no key was shortened; each stays the error it
  was.
- **Question five's option B did not contain the phrase the stem asks about.**
  The stem asks where *resource acquisition* is used well and one option never
  used it. It uses it now and fails on register instead, which is the point.
- **Four typed gaps accepted one word** where the frame admitted several. The
  near-synonyms the page's own feedback conceded are accepted, and a six-word
  bank keeps the target lexis in view.
- **It now teaches.** The original was five activities and every rule in the
  feedback. Three slides now cover what the lesson is actually about: that
  formality is a property of the whole clause rather than of a word dropped
  into it, the six fixed pairings and the two that turn on connotation, and the
  lexis that only works in one grammar &mdash; <em>spawn</em> intransitive,
  <em>venture forth</em> without an object, <em>iterative</em> against
  <em>repetitive</em>.

Two items are left as found and worth a look: question three has a defensible
second answer, which its own explanation concedes, and question twelve's
<em>seized upon</em> collocates perfectly well with <em>potential</em>. Both
would need a rewrite rather than a re-key.

**Artwork.** The flat-vector Minecraft set is spoken for by Past Modals and
Tense Review, so this deck uses three voxel studies from Innes's Downloads,
photographed with a shallow depth of field: a voxel Odysseus for the cover, a
warrior, and a group of creatures. They read as objects made of blocks rather
than as screenshots, which suits a lesson about Minecraft as something a
scholar writes about rather than something a player is inside. Three
backgrounds over twenty-one slides is thin and a fourth would help.

`--void` is lifted off the derived near-black to a grey, per Innes's standing
preference. Every other token is `extract-palette.py` output unedited.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
from mcc1_data import MC, FIB, FIB_BANK, MATCH, ORDER

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-minecraft-c1.html'
F = 'MinecraftC1'

# python3 lesson-template/extract-palette.py MinecraftC1/hero.jpg \
#            --accent-hue=190 --accent-sat=0.7
#
# The honest derivation returns a terracotta accent, which is the hero itself:
# the Forbes wordmark on the cover sat in the same colour as the figure behind
# it and all but vanished. Rotating to the teal that is already in the shield
# and the sky separates them without hand-picking anything. Every contrast row
# still passes.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #2d2d26;
  --surface       : #232216;
  --surface2      : #2f2e1e;
  --border        : #1e4047;
  --text          : #f2f5f5;
  --text-dim      : #a3bbbf;
  --accent        : #1e95ad;
  --accent-bright : #30c5e3;
  --accent-dim    : #13505c;
  --secondary     : #9a5531;
  --contrast      : #f26390;''' % F

CHIPS = ['constitutes', 'characterised by', 'underpins', 'serves as',
         'is regarded as', 'adhere to', 'procedurally generated',
         'is perhaps best evidenced by']

REG_BG = ['warrior.jpg', 'creatures.jpg', 'hero.jpg',
          'warrior.jpg', 'creatures.jpg', 'hero.jpg']
COL_BG = ['creatures.jpg', 'hero.jpg', 'warrior.jpg',
          'creatures.jpg', 'hero.jpg', 'warrior.jpg']
FIB_BG = ['hero.jpg', 'warrior.jpg', 'creatures.jpg']


def build():
    D.assert_no_key_is_longest(MC, 'MinecraftC1')
    D.assert_bank_is_not_a_key(FIB_BANK, [a[0] for _, a, _ in FIB])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'Writing About <em>Minecraft</em>',
                'The same game, described by a player and described by a scholar',
                [('Level', 'C1 &middot; Advanced'),
                 ('Focus', 'Academic register &amp; collocation'),
                 ('Count', '23 slides')])

        + D.teach('reEyebrow', 'Before the questions',
                  'reTitle', 'Formality is a whole clause, not a word',
                  [('re1h', 'The verbs that carry it', 're1b',
                    'A thing <strong>constitutes</strong> something rather than <em>is</em> '
                    'it. A region is <strong>characterised by</strong> its features. A '
                    'behaviour <strong>underpins</strong> what follows. A system '
                    '<strong>serves as</strong> a channel for something.',
                    're1n', 'Four verbs, and between them they carry most academic '
                            'description.'),
                   ('re2h', 'What disqualifies an option', 're2b',
                    'Vague quantifiers (<em>wood and stone and stuff</em>), discourse '
                    'markers (<em>basically</em>, <em>honestly</em>), and the defining '
                    'relative opened with <em>is when</em>. Each one is fine in speech '
                    'and none survives in an essay.',
                    're2n', '<em>A biome is when the land is different</em> &mdash; the '
                            'giveaway construction.'),
                   ('re3h', 'The trap', 're3b',
                    'A formal word inside a casual frame is still casual: <em>we do '
                    'resource acquisition</em> uses the phrase and gets it wrong, because '
                    'the phrase needs no verb at all.',
                    're3n', 'The whole clause has to change. That is what makes this '
                            'hard.')],
                  folder=F, bg='hero.jpg')

        + D.teach('coEyebrow', 'The fixed pairings',
                  'coTitle', 'Six collocations and their near-misses',
                  [('co1h', 'Prepositions the verb fixes', 'co1b',
                    'You <strong>adhere to</strong> guidelines, and you <em>comply '
                    'with</em> them &mdash; never <em>comply to</em>. Something is '
                    '<strong>regarded as</strong> a thing or <em>considered to be</em> '
                    'one, never <em>viewed for</em> it.',
                    'co1n', '<em>Capitalise on</em>, not <em>at</em>. There is no rule; '
                            'the verb simply takes one.'),
                   ('co2h', 'Connotation decides two of them', 'co2b',
                    'To <strong>exploit</strong> a mechanic is neutral and technical; '
                    '<em>misuse</em> and <em>abuse</em> import a judgement the sentence '
                    'is not making. To <strong>harness</strong> potential is positive, '
                    'where <em>exploit</em> would insult the people described.',
                    'co2n', 'The same act, three attitudes. At C1 the attitude is the '
                            'answer.'),
                   ('co3h', 'Terms a field has fixed', 'co3b',
                    'Content built to rules is <strong>procedurally generated</strong>. '
                    'That is the industry&rsquo;s own term; <em>randomly constructed</em> '
                    'and <em>computationally rendered</em> describe nothing in particular '
                    'and would not be understood.',
                    'co3n', 'When a field has a term, the near-synonym is not a stylistic '
                            'choice.')],
                  folder=F, bg='warrior.jpg')

        + D.teach('lxEyebrow', 'The lexis',
                  'lxTitle', 'Words that only work in one grammar',
                  [('lx1h', '<em>Spawn</em> is intransitive here', 'lx1b',
                    'Mobs <strong>spawn</strong>; nobody spawns them. The word describes '
                    'appearing under conditions, so a transitive use &mdash; <em>the game '
                    'spawns mobs</em> in the sense of <em>creates</em> &mdash; misses what '
                    'it means.',
                    'lx1n', '<em>Venture forth</em> is the same shape: intransitive, and '
                            'it takes no object.'),
                   ('lx2h', '<em>Iterative</em> is not <em>repetitive</em>', 'lx2b',
                    'An <strong>iterative</strong> process repeats in order to refine: '
                    'each cycle improves on the last. <em>Repetitive</em> means the same '
                    'thing again with no gain, which is the opposite claim about the '
                    'work.',
                    'lx2n', 'It comes from software, and it is now standard in any '
                            'writing about design.'),
                   ('lx3h', 'The abstract nouns', 'lx3b',
                    '<strong>Vigilance</strong> is watchfulness maintained against a '
                    'hazard. A <strong>conduit</strong> is a channel, usually '
                    'metaphorical. Cultural <strong>resonance</strong> is reach and '
                    'significance beyond the original field.',
                    'lx3n', 'All three are formal, all three have plain equivalents, and '
                            'the register is the point.')],
                  folder=F, bg='creatures.jpg')

        + "".join(D.mc(i + 1, 6, MC[i], 'mcEyebrow', 'Activity 1 &middot; Register',
                       'mcTitle', 'Which sentence would survive in an essay?',
                       folder=F, bg=REG_BG[i])
                  for i in range(6))

        + "".join(D.mc(i + 1, 6, MC[6 + i], 'dndEyebrow',
                       'Activity 2 &middot; Collocation',
                       'dndTitle', 'Which phrase does the sentence take?',
                       folder=F, bg=COL_BG[i])
                  for i in range(6))

        + "".join(D.gap(n + 1, 3, part, FIB_BANK,
                        'fibEyebrow', 'Activity 3 &middot; The formal word',
                        'fibTitle', 'One word completes the sentence',
                        folder=F, bg=FIB_BG[n], hint_key='fibHint',
                        hint='Six words in the bank, six gaps. Several near-synonyms are '
                             'also accepted.',
                        width=190, size=17)
                  for n, part in enumerate([FIB[:2], FIB[2:4], FIB[4:]]))

        + D.match(MATCH, 'matchEyebrow', 'Activity 4 &middot; The terminology',
                  'matchTitle', 'Match the term to its definition',
                  'matchHint', 'Click a term, then click what it means.',
                  'matchWhy', folder=F, bg='hero.jpg')

        + "".join(D.order(chunks, 'ordEyebrow', 'Activity 5 &middot; The paragraph',
                          'ordTitle', 'Build the argued paragraph',
                          'ordHint', 'Click a sentence to place it, click a placed '
                                     'sentence to take it back.',
                          why, folder=F, bg='warrior.jpg')
                  for chunks, why in ORDER)

        + D.results('resNext', 'You can read the register. Now write in it &rarr;',
                    folder=F, bg='hero.jpg')

        + D.activate('Present the case', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in pairs',
                     'One of you is arguing that games belong in a curriculum; the other '
                     'chairs the committee and is not persuaded. Four minutes each, then '
                     'swap.',
                     ['Define something from a game you know, in a sentence that would '
                      'survive in an essay.',
                      'Make a claim, then hedge it, then evidence it &mdash; in that '
                      'order and in three sentences.',
                      'Concede your opponent&rsquo;s strongest point and then turn it, '
                      'starting with <em>despite</em>.',
                      'Describe what a system does without once saying that it '
                      '<em>is</em> anything.'],
                     'Writing &middot; 200&ndash;250 words',
                     'Write the opening of a paper arguing that a game deserves academic '
                     'attention. Define your object, concede the obvious objection, make '
                     'one claim and evidence it, and close by saying what the field '
                     'currently holds. Hedge what deserves hedging and let no clause slip '
                     'into speech.',
                     'Minecraft constitutes an unusually productive object of study because…',
                     folder=F, bg='creatures.jpg')
    )

    import i18n_mcc1 as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Minecraft C1 Lesson | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d slides, %d MC, %d gaps, %d terms, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(FIB), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
