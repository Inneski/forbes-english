# -*- coding: utf-8 -*-
"""Station 9 — Present Simple Passive.  Mirrors camp 1, and wears its slate.

THE TOP OF THE DESCENT. The descent runs in the same order as the climb, so the
first tense a learner met going up is the first one they meet coming down.

That makes this deck carry TWO jobs where every station below it carries one:
the SWAP itself - object to the front, verb to BE + participle, doer optional -
and then its own auxiliary. Stations 10 to 15 teach only their own auxiliary
and assume the swap is already known, so if the swap is not learned here it is
not taught anywhere.

WHY THE PRESENT SIMPLE PASSIVE IS THE RIGHT ONE TO CARRY IT. Its auxiliary is
the smallest in the line - is and are, no second auxiliary, no participle of
'be' to hold in your head - so the swap is the only new thing on the screen.
Station 15's 'has been taken' could not have done this job first.

The last teaching slide is the one this tense earns on its own: processes,
rules and signs are where the present simple passive actually lives, and it is
the answer to a learner asking why anyone would choose it.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'present-simple-time-signals/%s'   # camp 1's own plates - same place, other side

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'The same event, told the other way round') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> mine <em class="obj">the stone</em>.',
       ['<em class="agent">Alex</em> locks <em class="obj">the gate</em>',
        '<em class="agent">a creeper</em> breaks <em class="obj">the wall</em>'],
       gloss('Los aldeanos extraen la piedra.', 'Dorfbewohner bauen den Stein ab.')),
      ('Passive', '<em class="obj">The stone</em> <em class="aux">is</em> <em class="pp">mined</em>.',
       ['<em class="obj">the gate</em> <em class="aux">is</em> <em class="pp">locked</em>',
        '<em class="obj">the wall</em> <em class="aux">is</em> <em class="pp">broken</em>'],
       gloss('La piedra es extra&iacute;da.', 'Der Stein wird abgebaut.')),
    ])),

# THE SWAP, AND THIS DECK IS WHERE IT IS TAUGHT. Three STATES of one sentence,
# not three instructions: the object's gold can be followed from the back of
# the active to the front of the passive without reading a word.
sec('teach', B % 'bg22.jpg', 'right', 'top',
    head('The swap', '<em class="obj">The object</em> becomes the subject') + '\n' +
    para([
      ('Active &mdash; the doer goes first',
       [('', '<em class="agent">Villagers</em> mine <em class="obj">the stone</em>')], ''),
      ('Passive &mdash; the same stone, now in front',
       [('', '<em class="obj">The stone</em> <em class="aux">is</em> <em class="pp">mined</em> '
             '<em class="agent">by villagers</em>')], ''),
      ('And the doer can go',
       [('', '<em class="obj">The stone</em> <em class="aux">is</em> <em class="pp">mined</em>.')], ''),
    ], '<em class="obj">THING</em> + <em class="aux">is</em> / <em class="aux">are</em> '
       '+ <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg31.jpg', 'left', 'top',
    head('The form', 'One auxiliary, then the third form') + '\n' +
    para([
      ('One thing', [('the stone', '<em class="aux">is</em> <em class="pp">mined</em>'),
                     ('no', '<em class="aux">isn&rsquo;t</em> <em class="pp">mined</em>')],
       gloss('es extra&iacute;da', 'wird abgebaut')),
      ('More than one', [('the stones', '<em class="aux">are</em> <em class="pp">mined</em>'),
                         ('no', '<em class="aux">aren&rsquo;t</em> <em class="pp">mined</em>')],
       gloss('son extra&iacute;das', 'werden abgebaut')),
      ('Asking', [('one', '<em class="aux">Is</em> it <em class="pp">mined</em>?'),
                  ('more', '<em class="aux">Are</em> they <em class="pp">mined</em>?')], ''),
    ], 'only <em class="aux">is</em> / <em class="aux">are</em> changes &mdash; '
       'the <em class="pp">participle</em> never does')),

sec('teach', B % 'bg02.jpg', 'right', 'top',
    head('The form', 'The participle is the THIRD form') + '\n' +
    para([
      ('Regular &mdash; add -ed', [('VERB', 'mine &rarr; mined &rarr; <em class="pp">mined</em>'),
                                   ('VERB', 'lock &rarr; locked &rarr; <em class="pp">locked</em>')], ''),
      ('Irregular &mdash; learn the third one',
       [('VERB', 'build &rarr; built &rarr; <em class="pp">built</em>'),
        ('VERB', 'break &rarr; broke &rarr; <em class="pp">broken</em>'),
        ('VERB', 'find &rarr; found &rarr; <em class="pp">found</em>')], ''),
    ], 'the passive ALWAYS uses the <em class="pp">THIRD</em> form')),

sec('teach', B % 'bg04.jpg', 'left', 'top',
    head('Why choose it', 'When the doer is not the point') + '\n' +
    para([
      ('You do not know who',
       [('', '<em class="obj">The gate</em> <em class="aux">is</em> <em class="pp">locked</em> every night.')], ''),
      ('Everyone already knows who',
       [('', '<em class="obj">Bread</em> <em class="aux">is</em> <em class="pp">baked</em> in the village.')], ''),
      ('The thing matters more',
       [('', '<em class="obj">Diamonds</em> <em class="aux">are</em> <em class="pp">found</em> deep underground.')], ''),
    ])),

sec('teach', B % 'bg06.jpg', 'right', 'top',
    head('The doer', '&lsquo;by&rsquo; is optional, and usually left out') + '\n' +
    para([
      ('Keep &lsquo;by&rsquo; when the doer is news',
       [('yes', '<em class="obj">The map</em> <em class="aux">is</em> <em class="pp">drawn</em> '
                '<em class="agent">by a villager</em>.')], ''),
      ('Drop it when it is not',
       [('no', '<em class="obj">The stone</em> <em class="aux">is</em> <em class="pp">mined</em>. '
              '<span class="dim">(by somebody &mdash; who cares?!)</span>')], ''),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

# The slide this tense earns on its own. Present perfect passive is about a
# result that still counts; present simple passive is about how things are
# done - which is why it is the voice of every process, rule and sign.
sec('teach', B % 'bg07.jpg', 'left', 'top',
    head('Where you meet it', 'Processes, rules and signs') + '\n' +
    para([
      ('A process &mdash; step after step',
       [('', '<em class="obj">Iron</em> <em class="aux">is</em> <em class="pp">smelted</em>, then '
             '<em class="obj">tools</em> <em class="aux">are</em> <em class="pp">made</em>.')], ''),
      ('A rule &mdash; who does it does not matter',
       [('', '<em class="obj">The gate</em> <em class="aux">is</em> <em class="pp">closed</em> at sunset.')], ''),
      ('A sign &mdash; short, and nobody named',
       [('', '<em class="obj">Torches</em> <em class="aux">are</em> <em class="pp">placed</em> every ten blocks.')], ''),
    ], 'this is where the present simple passive lives')),

mc(1, 6, B % 'bg05.jpg', 'right', 'top', 'Choose the passive',
   'The stone ______ by villagers.', 'is mined',
   [('mines', 'That is active &mdash; it says the stone does the mining.'),
    ('is mine', '&lsquo;Mine&rsquo; is the first form. The third is &lsquo;mined&rsquo;.'),
    ('are mined', 'One stone, so the auxiliary is &lsquo;is&rsquo;.')],
   'La piedra ______ por los aldeanos.', 'Der Stein ______ von Dorfbewohnern.',
   why='One stone, so &lsquo;is&rsquo;, and the third form of &lsquo;mine&rsquo; is &lsquo;mined&rsquo;.'),

mc(2, 6, B % 'bg12.jpg', 'left', 'top', 'Choose the passive',
   'The torches ______ every ten blocks.', 'are placed',
   [('is placed', '&lsquo;Torches&rsquo; is plural, so &lsquo;are&rsquo;.'),
    ('are place', '&lsquo;Place&rsquo; is the first form. The third is &lsquo;placed&rsquo;.'),
    ('are placing', 'Active &mdash; that says the torches place something.')],
   'Las antorchas ______ cada diez bloques.', 'Die Fackeln ______ alle zehn Bl&ouml;cke.',
   why='More than one torch, so &lsquo;are&rsquo; &mdash; then the third form, &lsquo;placed&rsquo;.'),

mc(3, 6, B % 'bg14.jpg', 'right', 'top', 'Say no',
   'The gate ______ during the day.', "isn't locked",
   [("doesn't lock", 'Active. The gate is not doing the locking.'),
    ("aren't locked", 'One gate, so &lsquo;is&rsquo;.'),
    ("isn't lock", 'Third form: locked.')],
   'La puerta ______ durante el d&iacute;a.', 'Das Tor ______ tags&uuml;ber.',
   why='To say no, the &lsquo;not&rsquo; goes on the auxiliary: <em class="aux">isn&rsquo;t</em> + <em class="pp">locked</em>.'),

mc(4, 6, B % 'bg33.jpg', 'left', 'top', 'Ask the question',
   '______ the diamonds found deep underground?', 'Are',
   [('Is', '&lsquo;Diamonds&rsquo; is plural.'),
    ('Have', 'That is a present perfect question, and there is no &lsquo;been&rsquo; here.'),
    ('Do', 'A present simple active question does not take a participle.')],
   '&iquest;______ los diamantes en las profundidades?', '______ die Diamanten tief unten gefunden?',
   why='To ask, the auxiliary moves to the front. Diamonds is plural, so it is &lsquo;Are&rsquo;.'),

mc(5, 6, B % 'bg38.jpg', 'right', 'top', 'Active, or passive?',
   'Which means the same as &lsquo;A creeper breaks the wall&rsquo;?',
   'The wall is broken by a creeper.',
   [('The wall breaks a creeper.', 'That swaps who did what.'),
    ('The wall is break by a creeper.', 'Third form: broken.'),
    ('A creeper is broken by the wall.', 'Both halves the wrong way round.')],
   '&iquest;Cu&aacute;l significa lo mismo?', 'Welcher Satz bedeutet dasselbe?',
   why='The wall was the object, so it goes to the front; the creeper follows &lsquo;by&rsquo;.'),

mc(6, 6, B % 'bg40.jpg', 'left', 'top', 'Leave it, or keep it?',
   'Which is better English?', 'The gate is locked at sunset.',
   [('The gate is locked by somebody at sunset.', '&lsquo;By somebody&rsquo; adds nothing. Drop it.'),
    ('The gate is locked by a person at sunset.', 'Same problem &mdash; the doer is not news.'),
    ('The gate locks at sunset.', 'That says the gate locks itself.')],
   '&iquest;Cu&aacute;l suena mejor?', 'Welcher Satz klingt besser?',
   why='Nobody needs telling that somebody locks a gate. Drop the doer and the sentence improves.'),

# 'bread' is in the singular bin on purpose: it is uncountable, so it takes
# 'is' although it names more than one loaf. A learner who is counting shapes
# rather than counting things gets it wrong here, which is the point.
sort(B % 'bg26.jpg', 'right', 'top', '&lsquo;is&rsquo;, or &lsquo;are&rsquo;?',
     'Click a subject, then click the words that go with it.',
     ['is', 'are'],
     [(0, 'the stone'), (0, 'the gate'), (0, 'bread'), (0, 'the map'),
      (1, 'the stones'), (1, 'the torches'), (1, 'diamonds'), (1, 'the walls')],
     'One thing takes &lsquo;is&rsquo;. More than one takes &lsquo;are&rsquo;. '
     '&lsquo;Bread&rsquo; is uncountable, so it takes &lsquo;is&rsquo; too. The doer changes nothing.'),

match(B % 'bg34.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('Villagers mine the stone', 'the stone is mined'),
       ('Alex locks the gate', 'the gate is locked'),
       ('A creeper breaks the wall', 'the wall is broken'),
       ('They place the torches', 'the torches are placed'),
       ('Steve bakes the bread', 'the bread is baked'),
       ('Miners find the diamonds', 'the diamonds are found')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg27.jpg', 'right', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The wall is ', 'broken', '. <span class="dim">(break)</span>',
      'Not &lsquo;broke&rsquo; &mdash; that is the second form.', 170),
     ('The bread is ', 'baked', '. <span class="dim">(bake)</span>',
      'Regular verb, so the third form is just -ed.', 170),
     ('The diamonds are ', 'found', '. <span class="dim">(find)</span>',
      'find &rarr; found &rarr; found. Here the second and third are the same word.', 170)]),

gap(2, 2, B % 'bg12.jpg', 'left', 'top', '&lsquo;is&rsquo;, or &lsquo;are&rsquo;?',
    'Look at the thing in front, not at the doer.',
    [('The torches ', 'are', ' placed by villagers.', 'Torches is plural.', 130),
     ('The gate ', 'is', ' locked by Alex.',
      'One gate. Alex is the doer and changes nothing.', 130),
     ('The diamonds ', 'are', ' found underground.', 'Diamonds is plural.', 130)]),

order(B % 'bg20.jpg', 'right', 'top', 'the stone | is | mined .',
      'The thing, then is, then the third form.'),

order(B % 'bg40.jpg', 'left', 'top', 'the map | is | drawn | by a villager .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.'),

results(B % 'bg25.jpg', 'left', 'top'),

activate(B % 'bg39.jpg', 'Now say how it is done',
         ['is mined', 'are placed', 'is locked', 'are found',
          'is made', 'by', 'every day', 'never'],
         ['Describe how something in your town is made. Do not say who makes it.',
          'Tell your partner three rules where you live, using is or are and the third form.',
          'Explain a process: what is done first, and what is done after that?'],
         ['Write the rules of a village in six lines, naming nobody.',
          'Then rewrite one line as active. Which one had to name somebody?']),
]

STATION = dict(
    file='blockcamp-passive-present-simple.html',
    chassis='blockcamp-present-simple.html',   # camp 1: brings its slate with it
    title='Present Simple Passive',
    sub='Station 9: it is done, and nobody is named',
    # GRADED, NOT FLAT. The descent climbs like the ascent: camp 1 is A1, and
    # the passive of it is one step harder, not four. Station 15 stays B1.
    level='A2',
    doctitle='Block Camp II — Passive 9: Present Simple Passive (A2) | Forbes English',
    hero=B % 'bg31.jpg',
    slides=SLIDES,
    # The chassis brought camp 1's scoring messages with it - "go back to the
    # paradigm", about the third-person -s, on a deck that does not teach it.
    # Every station overrides its own, IN EVERY LANGUAGE THE CHASSIS FILLS:
    # de and es are not decoration here, they are the same wrong advice in
    # another language for anyone who changes the picker.
    messages={
      'en': dict(
        resLow='Go back to the swap. The object of the active is the subject of the passive.',
        resMid='Look again at &lsquo;is&rsquo; and &lsquo;are&rsquo;. Count the thing in front, not the doer.',
        resStrong='Strong. Check the ones where you had to choose the third form.',
        resPerfect='Full marks. Now say how something is done, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zum Tausch. Das Objekt des Aktivsatzes ist das Subjekt des Passivsatzes.',
        resMid='Sieh dir &lsquo;is&rsquo; und &lsquo;are&rsquo; noch einmal an. Z&auml;hle das Ding davor, nicht den T&auml;ter.',
        resStrong='Stark. Sieh dir die an, bei denen du die dritte Form w&auml;hlen musstest.',
        resPerfect='Volle Punktzahl. Sag jetzt, wie etwas gemacht wird, ohne jemanden zu nennen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve al cambio. El objeto de la activa es el sujeto de la pasiva.',
        resMid='Mira otra vez &lsquo;is&rsquo; y &lsquo;are&rsquo;. Cuenta la cosa de delante, no quien la hace.',
        resStrong='Muy bien. Revisa las que te obligaron a elegir la tercera forma.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora di c&oacute;mo se hace algo, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
