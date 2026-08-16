# -*- coding: utf-8 -*-
"""Conservation Travel (C1/C2) — rebuilt as a deck.

A scrolling page with a genuinely good 1,500-word feature on it — five real
conservation projects, reported with specifics — and three activities that
could all be passed without reading it.

## The word bank was the answer key

Not correlated with the answers. The identical list, in the identical order:

    bank    : rare  retraining  traditional  millennia  Cultural  extinction
    answers : rare  retraining  traditional  millennia  Cultural  extinction

Read the bank top to bottom, fill the gaps top to bottom, six out of six,
having read neither the bank nor the sentences. Every other instance of this
defect in the catalogue was a bank that leaked the order; this one *was* the
key. The bank is sorted here, which is what `assert_bank_is_not_a_key` wants,
and the gaps within each slide are ordered so the sorted bank is not itself a
sequence.

`Cultural` was also capitalised in the bank, which separately announced which
gap began a sentence. Sorting alone would not fix that — the gap has been moved
off the sentence boundary so the word can sit in the bank lower-case with
everything else.

## The other two gave themselves away as well

**The MC keys ran 1 1 1 2 1 1** — five of six on the same index — and the key
was the longest option in three of the six. Keys are deranged to 2 0 3 1 3 0
and the three short distractors were lengthened. No key was shortened: on
inference items the key is long *because* it states the inference precisely,
and trimming it to satisfy the ratio would remove the thing being tested.

**Every `correctOrder` was `[0,1,2,3,4]`.** The runtime shuffles the steps, so
this was never learner-visible — the same situation as Nature Agency's all-zero
keys, and it is hygiene rather than a fix. The source order is scrambled anyway,
for printed hand-outs and for the day someone drops the shuffle.

## What the deck teaches that the page did not

Nothing on the page taught anything. It presented a feature, then tested
comprehension of it.

Two threads are worth teaching and both are in the text already. The first is
**reading for inference** — five of the six MC items ask what the article
*implies*, not what it says, and the distractors are mostly true statements
that simply are not the point. That distinction is the whole C1/C2 skill and it
now has a slide and a worked example.

The second is **naming by comparison**. The article calls the Carpathians
"Europe's Yellowstone", and one MC item turns on reading that correctly. A
comparison imports some properties and not others; deciding which is a skill
that transfers well beyond this lesson.

## Artwork

Nine images in `Conservation/`, commissioned to the lesson's own five projects
rather than to "nature" in general, and each is placed on the material it
depicts: `frog.jpg` behind the Mashpi glass frog, `turtles.jpg` behind Costa
Rica, `reef-canyon.jpg` and `reef-lagoon.jpg` behind Coral Gardeners,
`ama-boat.jpg` and `ama-dusk.jpg` behind the ama divers, and `plantation.jpg`
behind the item about Sevilla buying out the logging company and retraining its
workers — a picture of exactly that transition.

`reef-lagoon.jpg` is the cover: the lesson is subtitled "From Cloud Forests to
Coral Reefs" and it is the one frame holding forest, reef and open water
together. Its centre is open water and sky, which is what a centred cover title
needs.

`wildfire.jpg` and `island.jpg` back slides whose content they do not depict.
That is a compromise worth naming rather than hiding: there is no fire project
in this lesson. If either ever looks like it is claiming to illustrate
something, drop it and repeat one of the others instead.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-conservation-c1.html'
F = 'Conservation'

# Derived: python3 lesson-template/extract-palette.py Conservation/reef-lagoon.jpg
# Every row PASS.
PALETTE = '''  --hero: url('%s/reef-lagoon.jpg');

  --void          : #0d0f10;
  --surface       : #191d1f;
  --surface2      : #252a2d;
  --border        : #7c8c93;
  --text          : #f2f4f5;
  --text-dim      : #a8b4b9;
  --accent        : #7fb2c4;
  --accent-bright : #a8cfdc;
  --accent-dim    : #4d8598;
  --secondary     : #e8836f;
  --contrast      : #1eeb9a;''' % F

# ── Activity 1 · inference, rebuilt ───────────────────────────────────
# Keys deranged to 2 0 3 1 3 0. Distractors lengthened at Q1, Q3 and Q6;
# no key shortened.
MC = [
    dict(stem='What is the article actually for, judged by its opening rather than its subject?',
         ctx='The distinction the whole activity turns on: what a text does, not what it is about.',
         options=[
             'To rank wildlife-protection schemes across six continents by how much measurable '
             'recovery each one has achieved for the species it targets',
             'To argue that conservation science belongs to scientists, and that visitors on site '
             'are at best a distraction and at worst an active hindrance to the work',
             'To show that travel can support conservation, and that a traveller can contribute '
             'rather than only observe',
             'To promote high-end eco-resorts and wilderness retreats to readers who can afford '
             'to pay a premium for access to protected landscapes'],
         correct=2,
         why='The opening offers <em>the opportunity to meet the individuals leading such efforts '
             'and contribute your time</em>. Contribution is the claim. The other three are all '
             'things the article could plausibly have been, which is what makes them useful here.'),
    dict(stem='Why is the Mashpi glass frog scientifically significant?',
         ctx='Ecuador, Chocó cloud forest.',
         options=[
             'Because it took five years to document a species that could have vanished before '
             'science knew it existed',
             'Because it is the largest transparent amphibian ever recorded anywhere in South '
             'America, and the only one found above two thousand metres',
             'Because it was the first amphibian species anywhere to be discovered using '
             'eco-acoustic monitoring devices rather than by direct field observation',
             'Because it demonstrated that cloud forests hold more species per hectare than any '
             'other terrestrial ecosystem yet surveyed on Earth'],
         correct=0,
         why='The significance is the near-miss, not the record. <em>Could have vanished before '
             'science knew it existed</em> — the point is how close the species came to being '
             'lost unrecorded, which is an argument for the reserve, not a fact about frogs.'),
    dict(stem='The Carpathians are called &ldquo;Europe&rsquo;s Yellowstone&rdquo;. What does the '
              'comparison import?',
         ctx='Romania. One MC item in the source turned entirely on reading this correctly.',
         options=[
             'That Romania is marketing its wilderness primarily to American visitors, and has '
             'chosen a reference point they will recognise immediately',
             'That the mountains are as commercially developed as Yellowstone, with the same '
             'density of roads, lodges and visitor infrastructure across the protected area',
             'That the project depends on American funding and American expertise, and would not '
             'be viable on European resources alone',
             'The scale and ambition of the wildlife recovery — not the commerce, the visitor '
             'numbers or the funding'],
         correct=3,
         why='A comparison imports some properties and not others, and you have to decide which. '
             'Yellowstone here means <em>continental-scale rewilding</em>. It does not import the '
             'car parks. Deciding what an analogy carries is the transferable skill in this item.'),
    dict(stem='Why are sea turtle nests moved to protected hatcheries in Costa Rica?',
         ctx='The one item on this activity that is straight recall rather than inference.',
         options=[
             'Because the open beach has become too hot for natural incubation to succeed '
             'reliably, following several unusually warm nesting seasons',
             'To protect the eggs from poaching and allow round-the-clock monitoring',
             'To allow the eggs to be studied with scientific equipment that cannot practicably '
             'be transported to or operated on an open beach at night',
             'Because the turtles increasingly lay their eggs below the high-water line, where '
             'tidal inundation destroys a large proportion of each clutch'],
         correct=1,
         why='Poaching and monitoring. Worth noticing that three plausible-sounding alternatives '
             'here are <em>real problems that turtle projects elsewhere do face</em> — they are '
             'simply not this article&rsquo;s reason.'),
    dict(stem='What makes Coral Gardeners in French Polynesia innovative, on the article&rsquo;s '
              'account?',
         ctx='The project the ordering activity also covers.',
         options=[
             'It replants coral at depths that bleaching events cannot reach, using the thermal '
             'stability of deeper water as a refuge for vulnerable species',
             'It works exclusively from traditional Polynesian reef knowledge and deliberately '
             'rejects modern scientific instrumentation as inappropriate to the setting',
             'It concentrates on relocating endangered fish populations to healthier reef '
             'sections rather than on restoring the damaged reef structure itself',
             'It selects corals that already survived bleaching, then tracks the regrowth with AI'],
         correct=3,
         why='Two halves, and you need both: <em>selection for demonstrated resilience</em> plus '
             '<em>instrumented monitoring</em>. Option 1 describes a real technique that is not '
             'this project&rsquo;s, which is the commonest way to get this item wrong.'),
    dict(stem='Why would losing the ama divers be more than the end of a profession?',
         ctx='Japan. The article calls the tradition an Important Intangible Folk Cultural Property.',
         options=[
             'Because generations of sustainable fishing knowledge and ecological understanding '
             'would go with it',
             'Because the ama hold the only legal right to fish certain Japanese coastal waters, '
             'and those grounds would fall out of any management regime if the right lapsed',
             'Because their disappearance would cause the immediate collapse of the local seafood '
             'industry and the coastal economies that depend on it for employment',
             'Because the tradition is the only surviving evidence that Japanese women worked in '
             'coastal industries before the modern period, and the record would be lost'],
         correct=0,
         why='The loss is <em>epistemic</em> — knowledge about the sea, accumulated over two '
             'millennia and held nowhere else. Option 3 is close enough to be tempting: heritage '
             'value is real, but the article&rsquo;s claim is about ecological knowledge.'),
]

# ── Activity 2 · the vocabulary ───────────────────────────────────────
# The bank is sorted, and within each slide the gaps are ordered so the sorted
# bank is not a sequence. `cultural` is lower-case now: the gap was moved off
# the start of its sentence so the capital could stop announcing itself.
ITEMS = {
    'rare':        ('Cloud forests are ______ high-altitude ecosystems, uncommon by comparison '
                    'with almost any other habitat type.', 'rare',
                    'Sits directly before the noun phrase it limits. Not <em>scarce</em>, which '
                    'is about supply against demand.'),
    'retraining':  ('Sevilla bought the land from a logging company and turned it into a reserve, '
                    '______ its loggers and poachers as researchers.', 'retraining',
                    'A participle carrying the second action. The prefix does the work: the skills '
                    'were already there and were redirected, not replaced.'),
    'traditional': ('Coral Gardeners blends ______ Polynesian knowledge with modern marine '
                    'science.', 'traditional',
                    'Neutral here, and deliberately so. In other contexts it can imply outdated; '
                    'paired with <em>modern science</em> as an equal, it does not.'),
    'millennia':   ('The ama have dived for over two ______, on breath control alone.', 'millennia',
                    'Plural of <em>millennium</em>. A Latin plural that survives intact in formal '
                    'English — <em>two millenniums</em> is not wrong but reads oddly.'),
    'cultural':    ('Japan lists the practice as an Important Intangible Folk ______ Property, a '
                    'formal designation of heritage value.', 'cultural',
                    'Part of a fixed official title, which is why the whole phrase capitalises in '
                    'the source. The word itself is ordinary.'),
    'extinction':  ('Scientists warn that without urgent action all coral reefs could face ______ '
                    'by 2050.', 'extinction',
                    'Of a species or a whole system. <em>Face extinction</em> is the collocation; '
                    '<em>face extinguishing</em> is not English.'),
}
GROUPS = [
    ['retraining', 'extinction'],   # sorted bank: extinction, retraining -> positions 1 0
    ['traditional', 'cultural'],    # sorted bank: cultural, traditional -> positions 1 0
    ['rare', 'millennia'],          # sorted bank: millennia, rare       -> positions 1 0
]
GAPS = [[(ITEMS[k][0], [ITEMS[k][1]], ITEMS[k][2]) for k in g] for g in GROUPS]
BANKS = [sorted(g) for g in GROUPS]

# ── Activity 3 · sequence ─────────────────────────────────────────────
# Source stored every one of these as correctOrder [0,1,2,3,4] — the steps were
# already in order. Scrambled here; the engine shuffles too.
ORDER1 = [
    'Divers pick out corals that came through earlier bleaching events',
    'Fragments are grown on in underwater nurseries',
    'Healthy coral is transplanted onto the damaged reef',
    'AI tracks how much of it takes and regrows',
    'Visitors join the daily boat missions',
]
ORDER2 = [
    'A logging company holds 1,500 acres of Chocó cloud forest',
    'Sevilla buys the land and founds the Mashpi Reserve',
    'Its loggers and poachers are retrained as researchers',
    'A team finds the glass frog on the Amagusa River',
    'The reserve has 24 new species to its name',
]

# ── the five projects, sorted by what each one is protecting ──────────
BINS = ['A species', 'A habitat', 'A human practice']
SORT1 = [
    ('The Mashpi glass frog', 0),
    ('Carpathian bison and lynx', 0),
    ('Leatherback nests at Tortuguero', 0),
    ('1,500 acres of Chocó cloud forest', 1),
    ('Bleached reef sections off Mo&rsquo;orea', 1),
    ('Old-growth forest in Romania', 1),
    ('Ama breath-hold diving', 2),
    ('Polynesian reef knowledge', 2),
]

CHIPS = ['rare', 'retraining', 'traditional', 'millennia', 'cultural', 'extinction',
         'face extinction', 'imply', 'the article suggests']


def build():
    D.assert_no_key_is_longest(MC, 'Conservation')
    for n, (rows, bank) in enumerate(zip(GAPS, BANKS), 1):
        D.assert_bank_is_not_a_key(bank, [r[1][0] for r in rows])

    logo = D.logo_from(TPL)

    teach = (
        D.teach('t1e', 'Before the first question',
                't1t', 'Five of the six questions ask what the article <em>implies</em>',
                [('t1ah', 'Not what it says',
                  'Recall questions have one findable answer. These do not.',
                  't1an', 'You are being asked what follows from the text &mdash; which is why '
                          'you can locate a sentence and still choose wrong.'),
                 ('t1bh', 'The distractors are usually true',
                  'They are just not the article&rsquo;s point.',
                  't1bn', 'Several name real problems that conservation projects elsewhere do '
                          'face. Truth is not the test; relevance is.'),
                 ('t1ch', 'The habit that helps',
                  'Ask what the sentence is <em>doing</em>, not only what it reports.',
                  't1cn', 'A detail can be there to prove a point, to concede one, or to set a '
                          'scene. Which it is decides the answer.')],
                cols='1fr 1fr 1fr', folder=F, bg='island.jpg'),
        D.teach('t2e', 'Worked example',
                't2t', 'Two readings of the same sentence',
                [('t2ah', 'The sentence',
                  '<em>It could have vanished before science knew it existed.</em>',
                  't2an', 'About the Mashpi glass frog, documented after five years of survey '
                          'work in the Chocó cloud forest.'),
                 ('t2bh', 'The shallow reading',
                  '&ldquo;A rare frog was found.&rdquo;',
                  't2bn', 'True, and it answers nothing. It treats the clause as a fact about an '
                          'animal.'),
                 ('t2ch', 'The reading being tested',
                  '&ldquo;Undocumented species are being lost, so the reserve is urgent.&rdquo;',
                  't2cn', 'The clause is an <em>argument for the reserve</em>. That is what it is '
                          'doing in the paragraph, and that is the answer.')],
                cols='1fr 1fr 1fr', folder=F, bg='frog.jpg'),
        D.teach('t3e', 'The transferable one',
                't3t', 'Naming by comparison &mdash; &ldquo;Europe&rsquo;s Yellowstone&rdquo;',
                [('t3ah', 'What it imports',
                  'Scale, ambition, continental-scale rewilding, restored large mammals.',
                  't3an', 'This is the load the phrase is meant to carry, and the article says so '
                          'in the sentences around it.'),
                 ('t3bh', 'What it does not',
                  'The car parks, the visitor numbers, the funding, the nationality.',
                  't3bn', 'A comparison never imports everything. If it did, it would be an '
                          'identity claim rather than a comparison.'),
                 ('t3ch', 'Deciding which',
                  'Read what the writer does with the phrase immediately afterwards.',
                  't3cn', 'The next sentences here are about reintroduced species and old-growth '
                          'forest. So: ecology, not commerce. The context selects the load.')],
                cols='1fr 1fr 1fr', folder=F, bg='wildfire.jpg'),
        D.teach('t4e', 'The vocabulary, one',
                't4t', 'Scarcity and loss',
                [('t4ah', 'rare',
                  'Uncommon in itself. <em>Rare high-altitude ecosystems.</em>',
                  't4an', 'Not <em>scarce</em>, which is about supply against demand, and not '
                          '<em>endangered</em>, which is about trajectory.'),
                 ('t4bh', 'face extinction',
                  'The collocation. <em>All coral reefs could face extinction by 2050.</em>',
                  't4bn', 'Of a species or a whole system. <em>Face</em> is doing work: it frames '
                          'the outcome as still ahead and still avoidable.'),
                 ('t4ch', 'millennia',
                  'Plural of <em>millennium</em>. <em>Over two millennia.</em>',
                  't4cn', 'A Latin plural that survived intact into formal English. Reach for it '
                          'when the span itself is the point.')],
                cols='1fr 1fr 1fr', folder=F, bg='reef-canyon.jpg'),
        D.teach('t5e', 'The vocabulary, two',
                't5t', 'Transformation and heritage',
                [('t5ah', 'retraining',
                  '<em>Retraining its loggers and poachers as researchers.</em>',
                  't5an', 'The prefix carries the argument: the skills were already there &mdash; '
                          'the forest knowledge, the tracking &mdash; and were redirected, not '
                          'replaced.'),
                 ('t5bh', 'traditional',
                  '<em>Traditional Polynesian knowledge</em>, blended with marine science.',
                  't5bn', 'Neutral here, deliberately. Elsewhere it can imply outdated; set '
                          'alongside modern science as an equal partner, it does not.'),
                 ('t5ch', 'cultural',
                  '<em>Important Intangible Folk Cultural Property</em> &mdash; Japan&rsquo;s '
                  'formal designation for the ama.',
                  't5cn', 'An ordinary word inside a fixed official title. The capitals belong to '
                          'the title, not to the word.')],
                cols='1fr 1fr 1fr', folder=F, bg='plantation.jpg'),
        D.teach('t6e', 'The five projects',
                't6t', 'What each one is actually protecting',
                [('t6ah', 'Ecuador &middot; Mashpi',
                  'A logging concession bought out and turned into cloud forest reserve.',
                  't6an', '24 new species recorded, the glass frog among them.'),
                 ('t6bh', 'Romania &middot; the Carpathians',
                  'Rewilding at scale &mdash; bison, lynx, old-growth forest.',
                  't6bn', 'The one the Yellowstone comparison is about.'),
                 ('t6ch', 'Costa Rica &middot; the turtles',
                  'Night patrols, nests relocated to guarded hatcheries.',
                  't6cn', 'Against poaching, with round-the-clock monitoring.'),
                 ('t6dh', 'Polynesia &amp; Japan',
                  'Coral Gardeners replant resilient coral; the ama dive on held breath.',
                  't6dn', 'One protects a habitat, the other a practice. The last activity asks '
                          'you to tell those apart.')],
                cols='1fr 1fr 1fr 1fr', folder=F, bg='ama-dusk.jpg'),
    )

    slides = (
        D.cover(logo, 'Conservation <em>Travel</em>',
                'From cloud forests to coral reefs &mdash; five projects, and the difference '
                'between what a text says and what it means',
                [('Level', 'C1 &middot; C2'),
                 ('Focus', 'Inference &amp; the vocabulary of loss'),
                 ('Count', '21 slides')])
        + "".join(teach)
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'What does it imply?',
                       'qTitle', 'Choose the reading the article supports', folder=F,
                       ctx=q.get('ctx'),
                       bg=('turtles.jpg' if i % 3 == 1 else 'reef-lagoon.jpg' if i % 3 == 2 else None))
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, len(GAPS), rows, BANKS[n], 'gapEyebrow', 'The article&rsquo;s own words',
                        'gapTitle', 'Complete the sentence', folder=F,
                        hint_key='gapHint',
                        hint='Every word in the bank is used exactly once on this slide.',
                        bg='ama-boat.jpg' if n % 2 else None,
                        width=210, size=18)
                  for n, rows in enumerate(GAPS))
        + D.order(ORDER1, 'ordEyebrow', 'Sequence',
                  'ordTitle', 'The Coral Gardeners restoration process',
                  'ordHint', 'Drag the steps into order &mdash; or click one, then the position '
                             'you want it in.',
                  'Selection, then cultivation, then transplant, then monitoring, then visitors. '
                  'The visitors come last for a reason: the project is a restoration programme '
                  'that accepts help, not a tourist activity with a conservation theme.',
                  folder=F, bg='reef-canyon.jpg')
        + D.order(ORDER2, 'ordEyebrow', 'Sequence',
                  'ordTitle2', 'How the Mashpi Reserve came about',
                  'ordHint', 'Drag the steps into order &mdash; or click one, then the position '
                             'you want it in.',
                  'The order carries the argument. The retraining comes <em>before</em> the '
                  'discovery, so the people who found the frog are the same people who had been '
                  'logging the forest. That is the article&rsquo;s point, and it is lost if you '
                  'read the steps as a list rather than a sequence.',
                  folder=F, bg='frog.jpg')
        + D.sort_slide(BINS, SORT1, 'sortEyebrow', 'The five projects',
                       'sortTitle', 'What is each one protecting?',
                       'sortHint', 'Drag each into a box &mdash; or click it, then the box. A '
                                   'wrong first placement costs that item&rsquo;s point.',
                       'Species, habitat, practice. The three need different arguments and '
                       'different laws: you can list a species, you can designate a habitat, and '
                       'for a practice Japan had to invent a category &mdash; Important '
                       'Intangible Folk Cultural Property.',
                       folder=F, bg='island.jpg')
        + D.results('resNext', 'You can read the argument. Now make one →')
        + D.activate('Make the case for one project', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'One of you has funding for exactly one of the five projects. The other '
                     'wants it spent somewhere else.',
                     ['Argue for a project that protects a <em>practice</em> rather than a '
                      'species. Notice that it is harder, and say why.',
                      'Use <em>face extinction</em> once, accurately &mdash; about something that '
                      'can actually become extinct.',
                      'Make one claim your partner has to infer rather than one you state '
                      'outright. Then ask them what they took from it.',
                      'Compare your project to a famous one. Then say which properties the '
                      'comparison carries and which it does not.'],
                     'Writing &middot; 250&ndash;300 words',
                     'A funding case for one project: what it protects, what is lost without it, '
                     'and what a visitor actually contributes. Do not overstate — the strongest '
                     'version concedes the weakest part of the case.',
                     'This project protects…')
    )

    import i18n_conservation as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Conservation Travel — Inference &amp; Vocabulary (C1) | Forbes English', I)
    # Same call as the other pale-artwork decks, and measured rather than
    # assumed. `lesson-template/bgmeasure.py` over the background slides gives
    # text_vs_brightest_bg of 7.50-8.08 at 0.42 and 3.81-4.19 at the template's
    # default 0.72 -- below the 4.5 floor, so the default fails here.
    #
    # Measure the variant INSIDE the repo directory. Writing the 0.72 copy to
    # /tmp makes the relative image paths unresolvable, the backgrounds render
    # as nothing, and the tool then reports 17.5:1 -- a spectacular pass that
    # means the images never loaded. That happened on the first attempt here.
    s = s.replace('  --bg-opacity: 0.72;', '  --bg-opacity: 0.42;', 1)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d <section class="slide" (checker header is authoritative), '
          '%d MC, %d gap slides, 2 orders, 1 sort, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(s)))


if __name__ == '__main__':
    build()
