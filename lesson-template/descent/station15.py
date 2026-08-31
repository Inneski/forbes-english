# -*- coding: utf-8 -*-
"""Station 15 — Present Perfect Passive.  Mirrors camp 7, and wears its green.

THE DESCENT RUNS IN THE SAME ORDER AS THE CLIMB. Innes: "present simple should
start the descent (same as the ascent order)". So Present Simple Passive is
station 9 and this one is second from the bottom - you meet the tenses in the
order you learned them, not in reverse.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'present-perfect-time-signals/%s'   # camp 7's own plates - same place, other side

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'The same event, told the other way round') + '\n' +
    cards([
      ('Active', '<em class="agent">Alex</em> has taken <em class="obj">the map</em>.',
       ['<em class="agent">the villagers</em> have mined <em class="obj">the stone</em>',
        '<em class="agent">a creeper</em> has broken <em class="obj">the wall</em>'],
       gloss('Alex ha tomado el mapa.', 'Alex hat die Karte genommen.')),
      ('Passive', '<em class="obj">The map</em> <em class="aux">has been</em> <em class="pp">taken</em>.',
       ['<em class="obj">the stone</em> <em class="aux">has been</em> <em class="pp">mined</em>',
        '<em class="obj">the wall</em> <em class="aux">has been</em> <em class="pp">broken</em>'],
       gloss('El mapa ha sido tomado.', 'Die Karte wurde genommen.')),
    ])),

sec('teach', B % 'bg22.jpg', 'right', 'top',
    head('The swap', '<em class="obj">The object</em> becomes the subject') + '\n' +
    para([
      ('Active &mdash; the doer goes first',
       [('', '<em class="agent">Alex</em> has taken <em class="obj">the map</em>')], ''),
      ('Passive &mdash; the same map, now in front',
       [('', '<em class="obj">The map</em> <em class="aux">has been</em> <em class="pp">taken</em> '
             '<em class="agent">by Alex</em>')], ''),
      ('And the doer can go',
       [('', '<em class="obj">The map</em> <em class="aux">has been</em> <em class="pp">taken</em>.')], ''),
    ], '<em class="obj">THING</em> + <em class="aux">has</em> / <em class="aux">have been</em> '
       '+ <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg31.jpg', 'left', 'top',
    head('The form', 'Two auxiliaries, then the third form') + '\n' +
    para([
      ('One thing', [('the map', '<em class="aux">has been</em> <em class="pp">taken</em>'),
                     ('no', '<em class="aux">hasn&rsquo;t been</em> <em class="pp">taken</em>')],
       gloss('ha sido tomado', 'wurde genommen')),
      ('More than one', [('the maps', '<em class="aux">have been</em> <em class="pp">taken</em>'),
                         ('no', '<em class="aux">haven&rsquo;t been</em> <em class="pp">taken</em>')],
       gloss('han sido tomados', 'wurden genommen')),
      ('Asking', [('one', '<em class="aux">Has</em> it <em class="aux">been</em> <em class="pp">taken</em>?'),
                  ('more', '<em class="aux">Have</em> they <em class="aux">been</em> <em class="pp">taken</em>?')], ''),
    ], '<em class="aux">BEEN</em> never changes &mdash; only <em class="aux">has</em> / <em class="aux">have</em> does')),

sec('teach', B % 'bg02.jpg', 'right', 'top',
    head('The form', 'The participle is the THIRD form') + '\n' +
    para([
      ('Regular &mdash; add -ed', [('VERB', 'mine &rarr; mined &rarr; <em class="pp">mined</em>'),
                                   ('VERB', 'place &rarr; placed &rarr; <em class="pp">placed</em>')], ''),
      ('Irregular &mdash; learn the third one',
       [('VERB', 'build &rarr; built &rarr; <em class="pp">built</em>'),
        ('VERB', 'break &rarr; broke &rarr; <em class="pp">broken</em>'),
        ('VERB', 'take &rarr; took &rarr; <em class="pp">taken</em>')], ''),
    ], 'the passive ALWAYS uses the <em class="pp">THIRD</em> form')),

sec('teach', B % 'bg04.jpg', 'left', 'top',
    head('Why choose it', 'When the doer is not the point') + '\n' +
    para([
      ('You do not know who', [('', 'My chest <em class="aux">has been</em> <em class="pp">opened</em>.')], ''),
      ('Everyone already knows who', [('', 'The village <em class="aux">has been</em> <em class="pp">rebuilt</em>.')], ''),
      ('The thing matters more', [('', 'Three diamonds <em class="aux">have been</em> <em class="pp">found</em>.')], ''),
    ])),

sec('teach', B % 'bg06.jpg', 'right', 'top',
    head('The doer', '&lsquo;by&rsquo; is optional, and usually left out') + '\n' +
    para([
      ('Keep &lsquo;by&rsquo; when the doer is news',
       [('yes', 'The map <em class="aux">has been</em> <em class="pp">drawn</em> <em class="agent">by a villager</em>.')], ''),
      ('Drop it when it is not',
       [('no', 'The door <em class="aux">has been</em> <em class="pp">locked</em>. '
              '<span class="dim">(by somebody &mdash; who cares?!)</span>')], ''),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

sec('teach', B % 'bg07.jpg', 'left', 'top',
    head('Time signals', 'The same small words, on the other side') + '\n' +
    para([
      ('already &middot; just', [('', 'The bridge <em class="aux">has</em> already <em class="aux">been</em> <em class="pp">built</em>.')], ''),
      ('never &middot; ever', [('', 'It <em class="aux">has</em> never <em class="aux">been</em> <em class="pp">opened</em>.')], ''),
      ('yet &mdash; at the end', [('', 'The wall <em class="aux">hasn&rsquo;t been</em> <em class="pp">repaired</em> yet.')], ''),
    ], 'the signal sits between <em class="aux">has</em> and <em class="aux">been</em>')),

mc(1, 6, B % 'bg05.jpg', 'right', 'top', 'Choose the passive',
   'The bridge ______ already.', 'has been built',
   [('has built', 'That is active &mdash; it says the bridge did the building.'),
    ('has been build', 'The passive needs the third form: built.'),
    ('have been built', 'One bridge, so the auxiliary is &lsquo;has&rsquo;.')],
   'El puente ______ ya.', 'Die Br&uuml;cke ______ schon.'),

mc(2, 6, B % 'bg12.jpg', 'left', 'top', 'Choose the passive',
   'Three chests ______ this week.', 'have been opened',
   [('has been opened', 'Three chests is plural, so &lsquo;have&rsquo;.'),
    ('have been open', '&lsquo;open&rsquo; is the first form. The third is &lsquo;opened&rsquo;.'),
    ('have opened', 'Active &mdash; chests cannot open themselves.')],
   'Tres cofres ______ esta semana.', 'Drei Kisten ______ diese Woche.'),

mc(3, 6, B % 'bg14.jpg', 'right', 'top', 'Say no',
   'The wall ______ yet.', "hasn't been repaired",
   [("hasn't repaired", 'Active. The wall is not doing the repairing.'),
    ("haven't been repaired", 'One wall, so &lsquo;has&rsquo;.'),
    ("hasn't been repair", 'Third form: repaired.')],
   'El muro ______ todav&iacute;a.', 'Die Mauer ______ noch nicht.'),

mc(4, 6, B % 'bg33.jpg', 'left', 'top', 'Ask the question',
   '______ the diamonds been found?', 'Have',
   [('Has', '&lsquo;Diamonds&rsquo; is plural.'),
    ('Are', 'That is a present passive, and there is a &lsquo;been&rsquo; here.'),
    ('Did', 'A past simple question does not take &lsquo;been&rsquo;.')],
   '&iquest;______ encontrado los diamantes?', '______ die Diamanten gefunden?'),

mc(5, 6, B % 'bg38.jpg', 'right', 'top', 'Active, or passive?',
   'Which means the same as &lsquo;A creeper has broken the wall&rsquo;?',
   'The wall has been broken by a creeper.',
   [('The wall has broken a creeper.', 'That swaps who did what.'),
    ('The wall has been break by a creeper.', 'Third form: broken.'),
    ('A creeper has been broken by the wall.', 'Both halves the wrong way round.')],
   '&iquest;Cu&aacute;l significa lo mismo?', 'Welcher Satz bedeutet dasselbe?'),

mc(6, 6, B % 'bg40.jpg', 'left', 'top', 'Leave it, or keep it?',
   'Which is better English?', 'My chest has been opened.',
   [('My chest has been opened by somebody.', '&lsquo;By somebody&rsquo; adds nothing. Drop it.'),
    ('My chest has been opened by a person.', 'Same problem &mdash; the doer is not news.'),
    ('My chest has opened.', 'That says it opened itself.')],
   '&iquest;Cu&aacute;l suena mejor?', 'Welcher Satz klingt besser?'),

sort(B % 'bg26.jpg', 'right', 'top', '&lsquo;has been&rsquo;, or &lsquo;have been&rsquo;?',
     'Click a subject, then click the words that go with it.',
     ['has been', 'have been'],
     [(0, 'the map'), (0, 'the wall'), (0, 'it'), (0, 'the bridge'),
      (1, 'the maps'), (1, 'three chests'), (1, 'they'), (1, 'the diamonds')],
     'One thing takes &lsquo;has been&rsquo;. More than one takes &lsquo;have been&rsquo;. The doer changes nothing.'),

match(B % 'bg34.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('They have lit the torches', 'the torches have been lit'),
       ('Alex has taken the map', 'the map has been taken'),
       ('A creeper has broken it', 'it has been broken'),
       ('Somebody has opened the door', 'the door has been opened'),
       ('They have found the diamonds', 'the diamonds have been found'),
       ('Steve has eaten the bread', 'the bread has been eaten')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg27.jpg', 'right', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The wall has been ', 'broken', '. <span class="dim">(break)</span>',
      'Not &lsquo;broke&rsquo; &mdash; that is the second form.', 170),
     ('The bread has been ', 'eaten', '. <span class="dim">(eat)</span>',
      'eat &rarr; ate &rarr; eaten. The passive takes the third.', 170),
     ('The stone has been ', 'mined', '. <span class="dim">(mine)</span>',
      'Regular verb, so the third form is just -ed.', 170)]),

gap(2, 2, B % 'bg12.jpg', 'left', 'top', '&lsquo;has&rsquo;, or &lsquo;have&rsquo;?',
    'Look at the thing in front, not at the doer.',
    [('The torches ', 'have', ' been lit.', 'Torches is plural.', 130),
     ('The door ', 'has', ' been locked by the villagers.',
      'One door. The villagers are the doer and change nothing.', 130),
     ('The chests ', 'have', ' been opened.', 'Chests is plural.', 130)]),

order(B % 'bg20.jpg', 'right', 'top', 'the bridge | has | been | built .',
      'The thing, then has, then been, then the third form.'),

order(B % 'bg40.jpg', 'left', 'top', 'the map | has | been | drawn | by a villager .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.'),

results(B % 'bg25.jpg', 'left', 'top'),

activate(B % 'bg39.jpg', 'Now say what has been done',
         ['has been built', 'have been found', 'has been broken',
          'have been taken', 'already', 'yet', 'never', 'by'],
         ['Describe a room you came back to. What has been moved?',
          'Tell your partner three things in your town that have been built since you were born.',
          'Say what has been taken, and do not say who took it.'],
         ['Write a report on a village after a raid, using only passives.',
          'Then rewrite one line as active. Which one had to name somebody?']),
]

STATION = dict(
    file='blockcamp-passive-present-perfect.html',
    chassis='blockcamp-present-perfect.html',   # camp 7: brings its green with it
    title='Present Perfect Passive',
    sub='Station 15: it has been done, and it still counts',
    level='B1',
    doctitle='Block Camp II — Passive 15: Present Perfect Passive (B1) | Forbes English',
    hero=B % 'bg31.jpg',
    slides=SLIDES,
    # The chassis brought camp 7's scoring messages with it, so a learner who
    # scored nothing was told "Go back to the dictum" - about a slide this
    # deck has not got. Every station overrides its own.
    messages=dict(
        resLow='Go back to the swap. The object of the active is the subject of the passive.',
        resMid='Look again at the third form. &lsquo;Broke&rsquo; and &lsquo;broken&rsquo; are not the same word.',
        resStrong='Strong. Check the ones where you had to choose &lsquo;has&rsquo; or &lsquo;have&rsquo;.',
        resPerfect='Full marks. Now say what has been done, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;',
    ),
)
