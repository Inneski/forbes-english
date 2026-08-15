# -*- coding: utf-8 -*-
"""The Alchemist — B2. Rebuild as a 16:9 deck. Same filename, same URL.

**The comprehension section could be answered without the passage.** All
four keys were the longest or joint-longest option; COMP-2's key ran 69
characters against distractors of 23, 24 and 43.

**The grammar section could be answered without reading the stem.** All
four keys began with *had*, and all four sat at index 1. Pick the option
starting with *had*, four times, score 4/4 — and the learner never has to
decide whether the past perfect is needed, which is the only thing the
section is for.

**GRAM-4 marked correct English wrong.** *The Englishman read many books
about alchemy before he met Santiago* is a perfectly good sentence:
*before* already orders the events, so the past perfect is optional. The
feedback said it "is needed". That item is rewritten, and the case it got
wrong — when you do **not** need the past perfect — is now taught on its
own slide, because it is the half of the rule the lesson never had.

**COMP-1 could not be answered from the text at all.** "Why does
Santiago originally become a shepherd?" — the passage never says, and the
item's own feedback conceded it: *"The novel explains that…"*. The other
three were verbatim lifts, so not one of the four required inference.

**The word bank was the answer key.** The glossary listed omen, flock,
caravan, oasis, pursue…; the four gap answers in gap order were omen →
caravan → oasis → pursue — a straight walk down a list that stayed
on screen while the questions were answered.

**There was no wrong-answer feedback in the file.** Not "some items were
missing it": the code rendered one `explain` string with either
*Correct!* or *Not quite.* in front of it, for all twelve items. Every
wrong-answer explanation here is new.

**The novel, corrected.** The reading said Santiago "abandons his flock";
he sells it — and the grammar box two sections later said "sold his
sheep", contradicting it inside the same lesson. GRAM-2 invented a detail
(the alchemist "had already heard about him" before the oasis). And the
ending was never stated anywhere, while COMP-4 offered "the ending is
left open" as a distractor: he does dig up the treasure, at the ruined
church in Spain where the dream started.

**Alchemy is never explained.** The warm-up asks "What do you know about
alchemy? What was it trying to achieve?" and the lesson never answers,
though the novel's title, its central character and four vocabulary items
depend on it.

Three illustrations: the shepherd on the hill as the hero, the
alchemist's laboratory and the pyramids as per-slide backgrounds.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'alchemist_b2_lesson.html'
F = 'Alchemist'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e1214;
  --surface       : #171f21;
  --surface2      : #202b2d;
  --border        : #90766a;
  --text          : #f5f3f2;
  --text-dim      : #bfaca3;
  --accent        : #d4a38c;
  --accent-bright : #e8bba6;
  --accent-dim    : #b5704f;
  --secondary     : #1c2527;
  --contrast      : #2edbbf;''' % F

CSS = '.card.read-text { background: #141b1d; }\n'

PARAS = [
    ('Santiago is a young shepherd from Andalusia, content with a simple '
     'life and the freedom to travel with his flock. Then a dream repeats '
     'itself: there is treasure waiting for him near the Egyptian pyramids. '
     'He consults a fortune-teller, and later meets an old man who claims to '
     'be a king in disguise.',
     'p1n', 'Note <em>content with</em> — satisfied, not eager for more. '
     'It is the state the rest of the story disturbs.'),
    ('The old man persuades him to <strong>sell his flock</strong> and go in '
     'search of his &ldquo;Personal Legend&rdquo; &mdash; the particular '
     'purpose the novel says each person is here to fulfil. Santiago sells '
     'the sheep, crosses to North Africa, and is robbed of everything within '
     'a day of arriving.',
     'p2n', 'He <em>sells</em> the flock &mdash; he does not abandon it. '
     'The difference matters: this is a deliberate trade, not a walking '
     'away.'),
    ('Starting again from nothing, he works for a crystal merchant and '
     'learns patience. He joins a caravan crossing the desert to an oasis. '
     'On the way he meets an Englishman obsessed with alchemy, falls in love '
     'with a woman named Fatima, and is tested by hardship, by war between '
     'rival tribes, and by his own doubts.',
     'p3n', 'Four of the vocabulary words are in this paragraph: '
     '<em>merchant</em>, <em>caravan</em>, <em>oasis</em>, '
     '<em>hardship</em>.'),
    ('At the oasis he meets an alchemist, who teaches him to read the '
     'desert, the wind and the sun, and to trust what the novel calls the '
     '&ldquo;Soul of the World&rdquo;. Through a series of trials Santiago '
     'learns that the treasure he has been chasing was never only a thing '
     'buried in the ground.',
     'p4n', '<em>Trial</em> here is not a courtroom. It is a test of what '
     'someone can bear — the older sense of the word.'),
    ('And the ending, because it changes how you read everything before '
     'it. Santiago reaches the pyramids and digs, and finds nothing. '
     'Robbers beat him, and one of them mentions his own recurring dream: '
     'treasure buried under a tree at a ruined church in Spain. It is the '
     'exact place Santiago set out from. He goes back, digs, and the gold '
     'is there.',
     'p5n', 'So the treasure is real <em>and</em> the journey was the point. '
     'A reading that keeps only one of those two is thinner than the book.'),
]

COMP = [
    # COMP-1 was unanswerable from the passage. This asks about something
    # paragraph 1 actually establishes.
    dict(stem='What does paragraph 1 tell you about Santiago before the '
              'dream?',
         options=['He was satisfied with the life he already had',
                  'He was restless and looking for a way out',
                  'He was poor and could not afford to travel',
                  'He was searching for treasure near the pyramids'],
         correct=0,
         why='<em>Content with a simple life</em>. This matters: the story is '
             'not about escaping something bad. He gives up something he '
             'liked, which is what makes the choice cost anything.'),
    dict(stem='What persuades Santiago to leave?',
         options=['A repeated dream, and an old man who calls it his purpose',
                  'A business offer made to him by the crystal merchant in Tangier',
                  'His parents, who had wanted a different life for him',
                  'A letter that arrived from a stranger living in Cairo'],
         correct=0,
         why='Two things together, and the item is testing whether you '
             'noticed both. The dream alone had already repeated without '
             'moving him; it takes the old man naming it a Personal Legend.'),
    dict(stem='What happens to Santiago within a day of reaching Africa?',
         options=['He is robbed of everything he has',
                  'He meets the alchemist at the oasis',
                  'He is offered work by an Englishman',
                  'He decides to go straight back home'],
         correct=0,
         why='Robbed, immediately. The crystal merchant comes after that, and '
             'the alchemist much later, at the oasis.'),
    dict(stem='How does the novel actually end?',
         options=['He finds the treasure buried back where he started',
                  'He finds the treasure buried near the pyramids',
                  'He never finds it, and the ending is left open',
                  'The alchemist gives him the treasure as a reward'],
         correct=0,
         why='Under the tree at the ruined church in Spain. He had to go to '
             'Egypt to be told where it was — that is the joke the whole book '
             'is built on, and it only works if you know he does find it.'),
    dict(stem='So what does the treasure represent?',
         options=['Both the gold and what the journey taught him',
                  'Only the wisdom he gained along the journey',
                  'Only the gold that he digs up at the end',
                  'Nothing &mdash; it is a symbol with no referent'],
         correct=0,
         why='Careful with this one. It is tempting to say <em>only the '
             'wisdom</em>, because that sounds like the moral — but he really '
             'does dig up real gold. The book insists on both, and a reading '
             'that drops either half is thinner than the book.'),
]

VOCAB = [
    ('omen', 'a sign believed to predict what is coming',
     'v1', 'A dark cloud on the morning of a wedding is a <em>bad omen</em>. '
     'The adjective almost always comes with it: good, bad, ill.'),
    ('flock', 'a group of sheep or goats',
     'v2', 'Birds come in a <em>flock</em> too. Cattle come in a herd, fish '
     'in a shoal.'),
    ('caravan', 'a group of travellers crossing a desert together',
     'v3', 'In British English a caravan is also the thing you tow behind a '
     'car. Context separates them completely.'),
    ('oasis', 'a fertile place with water in a desert',
     'v4', 'Used figuratively as well: <em>an oasis of calm</em>. The plural '
     'is <em>oases</em>.'),
    ('pursue', 'to follow or chase something with determination',
     'v5', 'You <em>pursue a dream</em>, a career, a qualification. Formal; '
     'the everyday word is <em>chase</em> or <em>go after</em>.'),
    ('merchant', 'someone who buys and sells goods for profit',
     'v6', 'Slightly old-fashioned or specialised now: a wine merchant, a '
     'merchant ship.'),
    ('destined', 'certain to happen, as if it were already decided',
     'v7', '<em>Destined to</em> + verb, or <em>destined for</em> + noun. It '
     'is the adjective at the centre of this novel&rsquo;s argument.'),
    ('hardship', 'severe difficulty or suffering',
     'v8', 'Uncountable, usually: <em>years of hardship</em>. Not the same as '
     '<em>hardness</em>.'),
    ('trial', 'a difficult test of what somebody can bear',
     'v9', 'The courtroom sense is the commoner one today, so watch the '
     'context: <em>the trials of the journey</em> is this sense.'),
    ('wisdom', 'good judgement that comes from experience',
     'v10', 'Uncountable. Not the same as intelligence or knowledge — wisdom '
     'is what you do with them.'),
]

VOCAB_GAPS = [
    ('The old man&rsquo;s warning felt like a bad ______ for the journey '
     'ahead.', ['omen'],
     '<strong>Omen</strong> — a sign of what is coming. <em>Bad omen</em> is '
     'the standard collocation.'),
    ('They crossed the desert with a large ______ of traders.', ['caravan'],
     '<strong>Caravan</strong> — the group travelling together, not the '
     'vehicle.'),
    ('After weeks of walking they reached the ______ and drank.', ['oasis'],
     '<strong>Oasis</strong> — water in a desert. Plural <em>oases</em>.'),
    ('She decided to ______ her dream, however long it took.', ['pursue'],
     '<strong>Pursue</strong> a dream — determined, sustained chasing.'),
    ('Years of ______ had taught him patience.', ['hardship'],
     '<strong>Hardship</strong> — severe difficulty. Uncountable here.'),
    ('He was ______ to find it, or so the old man told him.', ['destined'],
     '<strong>Destined to</strong> + verb. The word the whole novel argues '
     'about.'),
]
VOCAB_BANK = sorted(['omen', 'caravan', 'oasis', 'pursue', 'hardship',
                     'destined', 'flock', 'trial'])

VOCAB_MATCH = [
    ('merchant', 'Somebody who buys and sells goods for profit'),
    ('trial', 'A difficult test of what somebody can bear'),
    ('wisdom', 'Good judgement that comes from experience'),
    ('flock', 'A group of sheep or goats'),
    ('omen', 'A sign believed to predict what is coming'),
    ('oasis', 'A fertile place with water in a desert'),
]

# ── grammar ───────────────────────────────────────────────────────────
# Every key in the old section began with "had" and sat at index 1. Two
# of these five are past simple, so "pick the one with had" now loses
# marks. The item that marked correct English wrong is gone.
GRAM = [
    dict(stem='Santiago sold his sheep because he ______ to look for the '
              'treasure.',
         options=['had decided', 'was deciding', 'has decided', 'decides'],
         correct=0,
         why='The deciding came first, the selling second, and the sentence '
             'gives them in the reverse order. That is exactly when the past '
             'perfect earns its place: <strong>had decided</strong>.'),
    dict(stem='By the time he reached the oasis, he ______ everything he '
              'owned.',
         options=['had already lost', 'already lost', 'was already losing',
                  'has already lost'],
         correct=0,
         why='<em>By the time</em> is a strong signal: the earlier event takes '
             '<strong>had</strong>. Note where <em>already</em> sits — between '
             '<em>had</em> and the participle, never before <em>had</em>.'),
    # Past simple is correct here. In the old lesson every key was a past
    # perfect, so a learner could never practise deciding.
    dict(stem='The Englishman ______ many books about alchemy before he met '
              'Santiago.',
         options=['read', 'had been reading', 'has read', 'reads'], correct=0,
         why='<strong>Read</strong> — past simple. <em>Before</em> has '
             'already put the events in order, so the past perfect is optional '
             'already put the events in order, so the past perfect is optional '
             'here, not required. <em>Had read</em> would also be fine; '
             '<em>has read</em> and <em>reads</em> would not.'),
    dict(stem='Santiago realised that he ______ everything he needed all '
              'along.',
         options=['had had', 'has had', 'was having', 'having had'], correct=0,
         why='Two past times: he <em>realised</em> at one moment (past '
             'simple), and what he realised was true before it (past perfect). '
             '<strong>Had had</strong> looks strange and is correct — the '
             'auxiliary and the participle of the same verb.'),
    # Also past simple: two events in the order they happened.
    dict(stem='He ______ the sheep, ______ to Africa, and ______ robbed.',
         options=['sold &middot; travelled &middot; was',
                  'had sold &middot; had travelled &middot; had been',
                  'has sold &middot; has travelled &middot; has been',
                  'was selling &middot; was travelling &middot; was being'],
         correct=0,
         why='Three events told <em>in the order they happened</em> — so plain '
             'past simple, three times. Stacking past perfects here would say '
             'that all of it happened before some other past moment, and there '
             'is no other moment.'),
]

GRAM_GAPS = [
    ('She ______ (already / leave) by the time I arrived.',
     ['had already left'],
     '<strong>had already left</strong>. <em>By the time</em> → past perfect, '
     'and <em>already</em> goes between the auxiliary and the participle.'),
    ('He ______ (sell) the sheep and ______ (set) off the next morning.',
     ['sold', 'set'],
     '<strong>sold … set</strong>. Two events in order, so past simple twice. '
     'No earlier reference point, no past perfect.'),
    ('When he finally reached Egypt, he ______ (walk) for months.',
     ['had walked|had been walking'],
     '<strong>had walked</strong> — or <em>had been walking</em>, which puts '
     'the emphasis on the duration. Both are accepted.'),
    ('He ______ (not / tell) anyone about the dream before he left.',
     ["hadn't told|had not told"],
     '<strong>hadn&rsquo;t told</strong>. The negative sits on the auxiliary: '
     '<em>had not</em> + participle.'),
]


def read_slide(ek, e, tk, t, text, nk, note, bg=None):
    return '''
    <section class="slide" data-type="teach" data-bg="%s/%s">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
        <div class="card read-text" style="padding:22px 28px">
          <p class="prose" style="font-size:19px;line-height:1.6">%s</p>
          <p class="prose dim" style="margin-top:14px;padding-top:12px;
             border-top:1px solid var(--border);font-size:15px"
             data-i18n="%s">%s</p>
        </div>
      </div>
    </section>
''' % (F, bg or 'hero.jpg', ek, e, tk, t, text, nk, note)


def build():
    D.assert_no_key_is_longest(COMP, 'Comprehension')
    D.assert_no_key_is_longest(GRAM, 'Grammar')
    D.assert_bank_is_not_a_key(VOCAB_BANK,
                               [a.split('|')[0] for _, aa, _ in VOCAB_GAPS
                                for a in aa])

    logo = D.logo_from(TPL)
    S = [D.cover(logo, 'The <em>Alchemist</em>',
                 'Santiago, the desert, and the past perfect — a B2 reading '
                 'and grammar lesson on Paulo Coelho&rsquo;s novel',
                 [('Level', 'B2 &middot; Literature'),
                  ('Focus', 'Narrative past tenses'),
                  ('Count', '31 slides')])]

    S += [D.teach('alE', 'Before you read', 'alT',
                  'What alchemy actually was',
                  [('al1h', 'The stated goal',
                    'Turn base metal into gold. Find the elixir of life.',
                    'al1n', 'Practised across the Islamic world, China, India '
                    'and Europe for well over a thousand years, by people who '
                    'were entirely serious.'),
                   ('al2h', 'What it really produced',
                    'Distillation, laboratory glassware, the first pure acids.',
                    'al2n', 'Newton wrote more on alchemy than on physics. '
                    'Modern chemistry grew directly out of it.'),
                   ('al3h', 'What the novel does with it',
                    'The transformation is the person, not the metal.',
                    'al3n', 'Santiago is not trying to make gold. He is '
                    'the material being worked on.')],
                  folder=F, bg='lab.jpg'),
          D.teach('whE', 'Before you read', 'whT', 'Who is who',
                  [('wh1h', 'Santiago',
                    'A shepherd from Andalusia, in southern Spain.',
                    'wh1n', 'He is never named in some translations — he is '
                    'simply &ldquo;the boy&rdquo;.'),
                   ('wh2h', 'The old man &middot; the crystal merchant',
                    'The one who sends him. The one who slows him down.',
                    'wh2n', 'The old man claims to be Melchizedek, a king. '
                    'The merchant is the counter-example: a man who has a '
                    'dream and will not go.'),
                   ('wh3h', 'The Englishman &middot; Fatima &middot; the alchemist',
                    'The scholar, the woman at the oasis, the teacher.',
                    'wh3n', 'The Englishman studies alchemy in books; the '
                    'alchemist practises it. The book has a view about which '
                    'of the two learns anything.')],
                  folder=F),
          D.teach('ktE', 'Before you read', 'ktT', 'Two terms the book invents',
                  [('kt1h', 'Personal Legend',
                    'The one thing a person is here to do.',
                    'kt1n', 'Capitalised throughout, as a proper noun. In the '
                    'Portuguese original it is <em>Lenda Pessoal</em>.'),
                   ('kt2h', 'The Soul of the World',
                    'The single thing everything is made of and speaks to.',
                    'kt2n', 'This is the book&rsquo;s metaphysics in one '
                    'phrase, and it is what the alchemist teaches Santiago to '
                    'listen to.'),
                   ('kt3h', 'Omens',
                    'Signs that point the way, if you are reading.',
                    'kt3n', 'The first vocabulary word in this lesson, and the '
                    'mechanism the entire plot runs on.')],
                  folder=F)]

    bgs = [None, None, None, 'pyramids.jpg', 'pyramids.jpg']
    for i, (text, nk, note) in enumerate(PARAS):
        S += [read_slide('rdE', 'The story', 'rdT%d' % (i + 1),
                         'The story so far &mdash; %d of 5' % (i + 1),
                         text, nk, note, bg=bgs[i])]

    S += ["".join(D.mc(i + 1, len(COMP), q, 'cE', 'Comprehension', 'cT',
                       'Check your understanding', folder=F)
                  for i, q in enumerate(COMP))]

    for n in range(3):
        group = VOCAB[n * 4:(n + 1) * 4] if n < 2 else VOCAB[8:]
        S += [D.teach('vE', 'Vocabulary', 'vT%d' % (n + 1),
                      'Ten words (%d of 3)' % (n + 1),
                      [(None, w, d, nk, note) for w, d, nk, note in group],
                      folder=F)]
    for n, rows in enumerate([VOCAB_GAPS[:3], VOCAB_GAPS[3:]]):
        S += [D.gap(n + 1, 2, rows, VOCAB_BANK if n == 0 else None, 'vgE',
                    'Vocabulary in use', 'vgT', 'Complete the sentence',
                    folder=F, size=17, width=160,
                    hint='Eight words in the bank, six gaps. Two are not '
                         'needed.' if n == 0 else None,
                    hint_key='vgHint' if n == 0 else None)]
    S += [D.match(VOCAB_MATCH, 'vmE', 'Vocabulary', 'vmT',
                  'Match the word to its meaning', 'vmHint',
                  'Click a word, then click its meaning.',
                  'Six of the ten words, and every one of them appears in the '
                  'story you have just read &mdash; which is the only way '
                  'vocabulary ever really sticks.', folder=F)]

    S += [D.teach('g1E', 'Grammar &middot; narrative past', 'g1T',
                  'The past perfect: had + past participle',
                  [('g1ah', 'What it does',
                    'Marks the <strong>earlier</strong> of two past events.',
                    'g1an', 'He sold the sheep because he <em>had decided</em> '
                    'to go. Deciding first, selling second.'),
                   ('g1bh', 'The form',
                    'had + past participle &mdash; for every person',
                    'g1bn', 'No <em>has</em>, no agreement, no exceptions. '
                    'Negative: <em>hadn&rsquo;t told</em>.'),
                   ('g1ch', 'Adverb placement',
                    'had <strong>already</strong> left &middot; had '
                    '<strong>never</strong> seen',
                    'g1cn', 'Between the auxiliary and the participle. '
                    '<em>Already had left</em> is the commonest slip.')],
                  folder=F),
          D.teach('g2E', 'Grammar &middot; narrative past', 'g2T',
                  'When you do NOT need it',
                  [('g2ah', 'When the order is already clear',
                    'He read the books <em>before</em> he met Santiago.',
                    'g2an', '<em>Before</em> and <em>after</em> do the ordering '
                    'themselves, so the past perfect becomes optional here. '
                    'Both versions of that sentence are correct English.'),
                   ('g2bh', 'When events are told in order',
                    'He sold the sheep, travelled to Africa and was robbed.',
                    'g2bn', 'Three past simples. Reaching for <em>had</em> '
                    'here says these happened before some other past moment — '
                    'and there isn&rsquo;t one.'),
                   ('g2ch', 'The test',
                    'Am I stepping <em>back</em> from where the story is?',
                    'g2cn', 'If yes, use it. If you are just moving forwards, '
                    'past simple. Overusing the past perfect is as wrong as '
                    'missing it, and much more common at B2.')],
                  folder=F)]
    S += ["".join(D.mc(i + 1, len(GRAM), q, 'gqE', 'Grammar &middot; practice',
                       'gqT', 'Past simple or past perfect?', folder=F)
                  for i, q in enumerate(GRAM))]
    for n, rows in enumerate([GRAM_GAPS[:2], GRAM_GAPS[2:]]):
        S += [D.gap(n + 1, 2, rows, None, 'ggE', 'Grammar &middot; practice',
                    'ggT', 'Write the correct form', folder=F, size=17,
                    width=190,
                    hint='Use the words in brackets. Decide first whether you '
                         'are stepping back.' if n == 0 else None,
                    hint_key='ggHint' if n == 0 else None)]

    S += [D.results(),
          D.activate('Personal Legends', 'Use at least four:',
                     ['had already', 'by the time', 'before he',
                      'destined to', 'pursue', 'omen', 'hardship'],
                     'Speaking &middot; in pairs',
                     'The crystal merchant has a dream and never goes. '
                     'Santiago goes. One of you defends each.',
                     ['Merchant&rsquo;s side: argue that the dream is worth '
                      'more unrealised. Use <em>by the time</em> once.',
                      'Santiago&rsquo;s side: argue the opposite, and use '
                      '<em>had already</em> at least twice.',
                      'Both: tell one true story about giving something up. '
                      'Two past perfects, no more &mdash; watch the '
                      'overuse.',
                      'Both: agree on what the novel is actually claiming, in '
                      'one sentence, and say whether you believe it.'],
                     'Writing &middot; 200&ndash;250 words',
                     'Is a Personal Legend a useful idea or a comforting one? '
                     'Use the novel as evidence, in narrative past tenses, and '
                     'step back with the past perfect at least twice.',
                     'Santiago had been content with his flock long before the '
                     'dream first came…')]
    return S


if __name__ == '__main__':
    import i18n_alchemist
    s = D.assemble(TPL, OUT, "".join(build()), PALETTE,
                   'The Alchemist — B2 English', i18n_alchemist)
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes' % (OUT, len(s)))
