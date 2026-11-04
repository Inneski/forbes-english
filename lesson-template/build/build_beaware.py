# -*- coding: utf-8 -*-
"""Be Aware of This Cleaner (B1) — a new deck from a local Facebook advert.

Source: a post on a Highland community notice board, sent by Innes as two
phone screenshots on 2026-11-04. A cleaning business wrote its advert as a
mock "BE AWARE OF THIS LADY!!!" warning — the "crimes" are going behind
toilets and rescuing shower screens — and ended on the reveal of her name and
how to book. It is a neat, very shareable piece of real English: news-report
passives (HAS BEEN SPOTTED), the present perfect of a state that is still true
(HAS BEEN THERE FOR AGES), KEEP + VERB-ING, a past perfect, and a tight set of
cleaning vocabulary.

Two decisions:

1. **The post is retold, not copied, and the business is invented.** The
   real advert names a real person and carried a doorbell-camera photo of
   her face. A lesson on a public site is not the place for either, so the
   cleaner is "Morag" of "Glen Sparkle Cleaning", and the reading slides are
   a rewrite in the same shape and the same grammar. Nothing pedagogical is
   lost: every structure the original used is still in the text.

2. **The hero is a placeholder.** No landscape picture came with the
   request (HOUSE-STYLE §14), so `BeAwareOfThisCleaner/hero.jpg` is a
   procedurally drawn field of soap bubbles and sparkles, and the palette is
   the tool's dark output for it, unedited. Swap the file and re-run
   extract-palette.py when real artwork arrives.
"""
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'be-aware-of-this-cleaner.html'
F = 'BeAwareOfThisCleaner'

# py lesson-template/extract-palette.py BeAwareOfThisCleaner/hero.jpg
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0f1217;
  --surface       : #181d26;
  --surface2      : #1f2732;
  --border        : #555556;
  --text          : #f2f4f5;
  --text-dim      : #a3b1bf;
  --accent        : #6588ac;
  --accent-bright : #8eacca;
  --accent-dim    : #445b71;
  --secondary     : #d7c386;
  --contrast      : #e27674;''' % F

POST1 = ('🚨 <strong>BE AWARE OF THIS LADY!!!</strong> 🚨 PLEASE SHARE &mdash; she&rsquo;s '
         'causing chaos across the Highlands! She <strong>has been spotted</strong>:<br>'
         '▶ attacking grease that <strong>has been</strong> behind cookers for years<br>'
         '▶ making taps so shiny you can see your face in them<br>'
         '▶ going BEHIND toilets. Yes, BEHIND them!<br>'
         '▶ rescuing shower screens that everyone else <strong>had given up on</strong>')
POST2 = ('And the worst part? <strong>SHE KEEPS COMING BACK.</strong> Weekly, fortnightly '
         '&mdash; whenever you need her. She never minds the mess, and she has heard '
         'every excuse going.<br><br>'
         'After a long investigation&hellip; her name is <strong>Morag</strong>, and she runs '
         'Glen Sparkle Cleaning ✨ Drop me a message to book!<br><br>'
         'PLEASE SHARE&hellip; there&rsquo;s a shower screen out there that still thinks it&rsquo;s safe.')

# (stem, options, correct index, why). Keys spread over the four positions.
MC = [
    dict(stem='Why does the post begin &ldquo;BE AWARE OF THIS LADY!!!&rdquo;?',
         options=['because she has damaged people&rsquo;s homes',
                  'to sound like a real warning, as a joke',
                  'because the police are looking for her',
                  'to tell people that she has stopped work'],
         correct=1,
         why='It copies the style of a real warning post. Then the &ldquo;crimes&rdquo; turn out '
             'to be very good cleaning &mdash; that surprise is the joke, and it is why people share it.'),
    dict(stem='The hard white layer that water leaves on taps and shower screens is ______.',
         options=['sawdust', 'condensation', 'cobwebs', 'limescale'],
         correct=3,
         why='<strong>Limescale</strong> is the chalky white build-up left by hard water. '
             '<strong>Condensation</strong> is water drops on a cold window or mirror &mdash; it wipes off.'),
    dict(stem='The sticky, oily dirt that builds up behind a cooker is ______.',
         options=['grease', 'pollen', 'gravel', 'varnish'],
         correct=0,
         why='<strong>Grease</strong> is oily dirt from cooking. It is why the post calls the '
             'cleaner&rsquo;s attack on it a &ldquo;crime&rdquo; &mdash; nobody else will touch it.'),
    dict(stem='Morag cleans some houses fortnightly. She visits them ______.',
         options=['twice every week', 'once each month', 'every two weeks', 'on alternate days'],
         correct=2,
         why='A <strong>fortnight</strong> is two weeks, so <strong>fortnightly</strong> means '
             'once every two weeks. It is common in British English and rare in American English.'),
    dict(stem='&ldquo;She has been spotted going behind toilets.&rdquo; This means ______.',
         options=['she has got dirty marks', 'people have seen her',
                  'she has been arrested', 'she has hidden somewhere'],
         correct=1,
         why='To <strong>spot</strong> someone is to see or notice them. HAS BEEN + PAST PARTICIPLE '
             'is the passive: it does not say WHO saw her, just like a news report.'),
    dict(stem='Shower screens &ldquo;that everyone else had given up on&rdquo;: the other cleaners had ______.',
         options=['cleaned them every single week', 'replaced them with new ones',
                  'stopped trying to clean them', 'given them away to a friend'],
         correct=2,
         why='To <strong>give up on</strong> something is to stop trying to fix it because it '
             'seems hopeless. HAD + PAST PARTICIPLE puts it before Morag arrived.'),
    dict(stem='&ldquo;SHE KEEPS COMING BACK!&rdquo; This tells us she ______.',
         options=['returns again and again', 'comes back only once',
                  'wants to come back later', 'never wants to come back'],
         correct=0,
         why='KEEP + VERB-ING means again and again. In a warning it sounds terrible; in an '
             'advert it means regular visits &mdash; weekly or fortnightly.'),
    dict(stem='&ldquo;She has heard every excuse going.&rdquo; This means ______.',
         options=['she makes a lot of excuses herself', 'she leaves when you make excuses',
                  'she only cleans for people who go out', 'she has heard all the usual excuses'],
         correct=3,
         why='<strong>Every excuse going</strong> = every excuse that exists. Whatever you say '
             'about the mess, she has heard it before &mdash; so there is no need to feel embarrassed.'),
]

GAPS = [
    [('That grease ______ behind the cooker since 2019.', ['has been'],
      'HAS BEEN + since / for: it started in 2019 and it is still there now.'),
     ('Our cleaner ______ coming back every Friday, and we love it.', ['keeps'],
      'KEEP + VERB-ING = again and again. "She" takes KEEPS.')],
    [('A woman has been ______ going behind toilets in Inverness!', ['spotted|seen'],
      'HAS BEEN + PAST PARTICIPLE: the passive. "Spotted" and "seen" both work.'),
     ('By the time Morag arrived, we ______ given up on that shower screen.', ['had'],
      'HAD + PAST PARTICIPLE: we gave up first, and then Morag arrived.')],
]
BANK = ['had', 'has been', 'is being', 'keep', 'keeps', 'spotted', 'spotting', 'was']

MATCH = [
    ('spotless', 'completely clean, with no marks at all'),
    ('a deep clean', 'a very thorough clean, top to bottom'),
    ('give up on something', 'stop trying to fix it because it seems hopeless'),
    ('drop me a message', 'send me a quick, informal message'),
    ('no judgement', 'nobody will think badly of you'),
]

CHIPS = ['has been spotted', 'keeps coming back', 'has been there for ages',
         'had given up on', 'every excuse going', 'spotless', 'a deep clean',
         'drop me a message']

# English explanations, read by i18n_beaware.py before build() swaps in keys.
EN_WHY = [q['why'] for q in MC]


def build():
    D.assert_no_key_is_longest(MC, 'BeAware')
    flat = [a for part in GAPS for _, aa, _ in part for a in aa]
    pos = D.assert_bank_is_not_a_key(BANK, flat)
    logo = D.logo_from(TPL)
    for n, q in enumerate(MC):
        q['why'] = 'q%dwhy' % (n + 1)

    slides = (
        D.cover(logo, 'Be Aware of This <em>Cleaner</em>',
                'A fake warning, a real advert &mdash; the English of a Facebook post that went round the Highlands',
                [('Level', 'B1 &middot; Intermediate'),
                 ('Focus', 'Reading &middot; cleaning words &middot; present perfect'),
                 ('Count', '19 slides')])

        + D.teach('postEyebrow', 'Read the post &middot; 1 of 2',
                  'postTitle', 'Seen on a community notice board',
                  [(None, '', POST1, 'post1n',
                    'Read it once for the joke. What do you think is going on?')])

        + D.teach('postEyebrow2', 'Read the post &middot; 2 of 2',
                  'postTitle2', '&hellip; and the reveal',
                  [(None, '', POST2, 'post2n',
                    'Were you right? Who wrote the post, and what do they want?')])

        + D.teach('jokeEyebrow', 'How it works',
                  'jokeTitle', 'A warning that is really an advert',
                  [('j1h', '1 &middot; The set-up', 'j1b',
                    'Capital letters, alarm emojis and <strong>PLEASE SHARE</strong>: it looks '
                    'exactly like a warning about a criminal.',
                    'j1n', 'People share warnings, so the post travels.'),
                   ('j2h', '2 &middot; The twist', 'j2b',
                    'Every &ldquo;crime&rdquo; is something a customer wants: grease gone, shiny '
                    'taps, the place behind the toilet clean.',
                    'j2n', 'The joke is the gap between the tone and the facts.'),
                   ('j3h', '3 &middot; The reveal', 'j3b',
                    'Only at the end: her name, the business, the services, and '
                    '<strong>drop me a message</strong>.',
                    'j3n', 'Advert first, then the call to action.')])

        + D.teach('wordsEyebrow', 'Vocabulary',
                  'wordsTitle', 'Cleaning words from the post',
                  [('w1h', 'The dirt', 'w1b',
                    '<strong>grease</strong> &mdash; oily dirt from cooking<br>'
                    '<strong>limescale</strong> &mdash; white build-up from water<br>'
                    '<strong>grime</strong> &mdash; dirt that has been there a long time',
                    'w1n', 'All three are uncountable: some grease, NOT a grease.'),
                   ('w2h', 'The result', 'w2b',
                    '<strong>spotless</strong> &mdash; no marks at all<br>'
                    '<strong>sparkling</strong> &mdash; clean and bright<br>'
                    '<strong>shiny</strong> &mdash; reflects the light',
                    'w2n', '&ldquo;So shiny you can see your face in them.&rdquo;'),
                   ('w3h', 'The service', 'w3b',
                    '<strong>a regular clean</strong> &mdash; the normal visit<br>'
                    '<strong>a deep clean</strong> &mdash; everything, top to bottom<br>'
                    '<strong>weekly / fortnightly</strong> &mdash; every week / two weeks',
                    'w3n', 'A fortnight = two weeks. Very British.')])

        + D.teach('gramEyebrow', 'Grammar',
                  'gramTitle', 'Three structures doing the work',
                  [('g1h', 'HAS BEEN + PAST PARTICIPLE', 'g1b',
                    '&ldquo;She <strong>has been spotted</strong>.&rdquo; The passive: we do not '
                    'say WHO saw her. It sounds like a news report.',
                    'g1n', 'spot &rarr; spotted · see &rarr; seen'),
                   ('g2h', 'HAS BEEN + for / since', 'g2b',
                    '&ldquo;Grease that <strong>has been</strong> there for years.&rdquo; It started '
                    'in the past and it is still there now.',
                    'g2n', 'for years · since 2019 · for ages'),
                   ('g3h', 'KEEP + VERB-ING', 'g3b',
                    '&ldquo;She <strong>keeps coming</strong> back.&rdquo; Again and again. '
                    '&ldquo;She&rdquo; takes KEEPS.',
                    'g3n', 'Also in the post: HAD + PAST PARTICIPLE &mdash; &ldquo;had given up on&rdquo;.')])

        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Check your reading',
                       'qTitle', 'Choose the best answer')
                  for i, q in enumerate(MC))

        + "".join(D.gap(n + 1, len(GAPS), part, BANK, 'gapEyebrow', 'Grammar',
                        'gapTitle', 'Complete the sentences',
                        hint_key='gapHint',
                        hint='Type one item from the word bank. Some are not used.')
                  for n, part in enumerate(GAPS))

        + D.match(MATCH, 'matchEyebrow', 'Phrases', 'matchTitle', 'What do they mean?',
                  'matchHint', 'Click a phrase, then click its meaning.',
                  'All five are everyday phrases from adverts and messages. '
                  '&ldquo;Drop me a message&rdquo; is friendlier than &ldquo;contact me&rdquo;.')

        + D.results('resNext', 'Now write your own fake warning &rarr;')

        + D.activate('Write your own fake warning', 'Use at least three:', CHIPS,
                     'Speaking &middot; in pairs',
                     'Choose a local business &mdash; a dog walker, a plumber, a baker, a '
                     'hairdresser. Turn its best quality into a &ldquo;crime&rdquo;.',
                     ['Say your opening warning as dramatically as you can. Your partner guesses the business.',
                      'Give three &ldquo;crimes&rdquo; it has been spotted committing. Use HAS BEEN + PAST PARTICIPLE.',
                      'Say what the worst part is &mdash; something customers keep getting. Use KEEP + VERB-ING.',
                      'Is this kind of advert clever or annoying? Would you share it? Say why.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write a &ldquo;BE AWARE&rdquo; post for a community Facebook page, advertising a '
                     'real or invented local business. Warning first, then the twist, then the '
                     'reveal and how to book.',
                     '🚨 BE AWARE OF THIS MAN!!! 🚨 He has been spotted&hellip;')
    )

    import i18n_beaware as I
    s = D.assemble(TPL, OUT, slides, PALETTE,
                   'Be Aware of This Cleaner (B1) | Forbes English', I,
                   langs=('en', 'de', 'es'))
    print('wrote %s — %d MC, bank positions %s, %d bytes' % (OUT, len(MC), pos, len(s)))


if __name__ == '__main__':
    build()
