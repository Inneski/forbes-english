# -*- coding: utf-8 -*-
"""Station 12 — Past Continuous Passive.  Mirrors camp 4, and wears its gold.

THE FOUR CORNERS ARE NOW COMPLETE, and this deck is the one that closes them.
By here a learner has met:

    is / are  + participle          station 9   a process, now
    is / are  + being + participle  station 10  happening now
    was / were + participle         station 11  finished, dated
    was / were + being + participle station 12  happening THEN

So this deck teaches almost no new form - `being` is station 10's, `was/were`
is station 11's - and instead spends its weight on the one thing only it can
do: an unfinished action in the past with something CUTTING ACROSS IT. That is
camp 4's whole subject in the active, and the passive of it is the same
sentence with the doer removed.

    the wall was being built when the creeper arrived

WHY THIS DECK IS B1 WHERE 10 AND 11 ARE A2. Not the form. The form is easier
than station 15's. It is that the sentence needs TWO clauses to mean anything -
the long one and the one that interrupts it - and a learner has to hold a
tense in each. Camp 4 is where that starts in the active, and it is one step
harder in the passive because neither clause names anybody.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'past-continuous-time-signals/%s'   # camp 4's own plates

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'It was being done, and nobody is named') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> were building <em class="obj">the wall</em>.',
       ['<em class="agent">Alex</em> was drawing <em class="obj">the map</em>',
        '<em class="agent">they</em> were lighting <em class="obj">the torches</em>'],
       gloss('Los aldeanos estaban construyendo el muro.',
             'Dorfbewohner bauten gerade die Mauer.')),
      ('Passive', '<em class="obj">The wall</em> <em class="aux">was being</em> <em class="pp">built</em>.',
       ['<em class="obj">the map</em> <em class="aux">was being</em> <em class="pp">drawn</em>',
        '<em class="obj">the torches</em> <em class="aux">were being</em> <em class="pp">lit</em>'],
       gloss('El muro estaba siendo construido.',
             'Die Mauer wurde gerade gebaut.')),
    ])),

# The four corners on one slide. Nothing here is new; the point is that the
# learner can see the grid is now closed, and where this deck sits in it.
sec('teach', B % 'bg23.jpg', 'left', 'top',
    head('The form', 'Two words you already have') + '\n' +
    para([
      ('Now, in general', [('station 9', '<em class="t-ps">is</em> <em class="pp">built</em>')],
       gloss('Ahora, en general', 'Jetzt, allgemein')),
      ('Now, as you watch', [('station 10', '<em class="t-pc">is being</em> <em class="pp">built</em>')],
       gloss('Ahora, mientras miras', 'Jetzt, w&auml;hrend du zusiehst')),
      ('Then, finished', [('station 11', '<em class="t-past">was</em> <em class="pp">built</em>')],
       gloss('Entonces, terminado', 'Damals, abgeschlossen')),
      ('Then, still going', [('station 12', '<em class="t-pastc">was being</em> <em class="pp">built</em>')],
       gloss('Entonces, todav&iacute;a en marcha', 'Damals, noch im Gange')),
    ], '<em class="obj">THING</em> + <em class="aux">was</em> / <em class="aux">were</em> '
       '+ <em class="aux">being</em> + <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg09.jpg', 'left', 'top',
    head('The form', 'Only the first word changes') + '\n' +
    para([
      ('One thing', [('the wall', '<em class="aux">was being</em> <em class="pp">built</em>'),
                     ('no', '<em class="aux">wasn&rsquo;t being</em> <em class="pp">built</em>')],
       gloss('estaba siendo construido', 'wurde gerade gebaut')),
      ('More than one', [('the walls', '<em class="aux">were being</em> <em class="pp">built</em>'),
                         ('no', '<em class="aux">weren&rsquo;t being</em> <em class="pp">built</em>')],
       gloss('estaban siendo construidos', 'wurden gerade gebaut')),
      ('Asking', [('one', '<em class="aux">Was</em> it <em class="aux">being</em> <em class="pp">built</em>?'),
                  ('more', '<em class="aux">Were</em> they <em class="aux">being</em> <em class="pp">built</em>?')],
       gloss('&iquest;Se estaba construyendo?', 'Wurde sie gerade gebaut?')),
    ], 'only <em class="aux">&lsquo;was&rsquo;</em> / <em class="aux">&lsquo;were&rsquo;</em> changes')),

# THE SLIDE THIS DECK OWNS, and camp 4's whole subject. The long action is
# passive; the thing that cuts across it is a plain past simple, and both
# clauses are on screen at once so the shape can be seen rather than described.
sec('teach', B % 'bg13.jpg', 'left', 'top',
    head('The shape', 'The long one, and the one that cuts in') + '\n' +
    para([
      ('The long action &mdash; passive',
       [('', '<em class="obj">The wall</em> <em class="aux">was being</em> <em class="pp">built</em> &hellip;')],
       gloss('La acci&oacute;n larga', 'Die lange Handlung')),
      ('The interruption &mdash; past simple',
       [('', '&hellip; when a creeper <em class="t-past">arrived</em>.')],
       gloss('La interrupci&oacute;n', 'Die Unterbrechung')),
      ('Together',
       [('', '<em class="obj">The wall</em> <em class="aux">was being</em> <em class="pp">built</em> '
             'when a creeper <em class="t-past">arrived</em>.')],
       gloss('El muro estaba siendo construido cuando lleg&oacute; un creeper.',
             'Die Mauer wurde gerade gebaut, als ein Creeper kam.')),
    ], 'long one <em class="aux">was being</em> &hellip; short one '
       '<em class="t-past">cut across it</em>')),

sec('teach', B % 'bg17.jpg', 'left', 'top',
    head('Why choose it', 'The work was under way, and nobody is blamed') + '\n' +
    para([
      ('Something was in progress',
       [('', '<em class="obj">The bridge</em> <em class="aux">was being</em> <em class="pp">repaired</em> all week.')],
       gloss('Algo estaba en marcha', 'Etwas war im Gange')),
      ('And then it was interrupted',
       [('', '<em class="obj">The map</em> <em class="aux">was being</em> <em class="pp">drawn</em> '
             'when the lamp <em class="t-past">went</em> out.')],
       gloss('Y entonces se interrumpi&oacute;', 'Und dann wurde es unterbrochen')),
      ('Background to a story',
       [('', '<em class="obj">Torches</em> <em class="aux">were being</em> <em class="pp">lit</em> '
             'all along the road.')],
       gloss('El fondo de una historia', 'Der Hintergrund einer Geschichte')),
    ], 'this is the voice of a scene, not of a fact')),

sec('teach', B % 'bg30.jpg', 'right', 'top',
    head('Time signals', 'Words that hold the door open') + '\n' +
    cards([
      ('A stretch of time', 'The action filled it, start to end.',
       ['all morning', 'all week', 'at that moment'],
       gloss('toda la ma&ntilde;ana &middot; toda la semana &middot; en aquel momento',
             'den ganzen Morgen &middot; die ganze Woche &middot; in jenem Moment')),
      ('The cut across it', 'A short past simple lands inside the long one.',
       ['when', 'as', 'while'],
       gloss('cuando &middot; mientras &middot; mientras que',
             'als &middot; w&auml;hrend &middot; w&auml;hrend')),
    ])),

sec('teach', B % 'bg36.jpg', 'right', 'top',
    head('The doer', 'Still optional, still usually gone') + '\n' +
    para([
      ('Worth saying',
       [('yes', '<em class="obj">The map</em> <em class="aux">was being</em> <em class="pp">drawn</em> '
                '<em class="agent">by Alex</em>.')],
       gloss('Vale la pena decirlo', 'Der T&auml;ter ist eine Neuigkeit')),
      ('Not worth saying',
       [('no', '<em class="obj">The bread</em> <em class="aux">was being</em> <em class="pp">baked</em>. '
              '<span class="dim">(by the baker &mdash; obviously)</span>')],
       gloss('No hace falta decirlo', 'Muss man nicht sagen')),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

mc(1, 6, B % 'bg05.jpg', 'left', 'top', 'Choose the passive',
   'The wall ______ when the creeper arrived.', 'was being built',
   [('was built', 'That is finished. The sentence needs an action still going on.'),
    ('was being build', 'Third form: built.'),
    ('were being built', 'One wall, so &lsquo;was&rsquo;.')],
   'El muro ______ cuando lleg&oacute; el creeper.',
   'Die Mauer ______, als der Creeper kam.',
   why='The building had not finished when the creeper arrived, so &lsquo;was being built&rsquo;.'),

mc(2, 6, B % 'bg21.jpg', 'left', 'top', 'Choose the passive',
   'The torches ______ all along the road.', 'were being lit',
   [('was being lit', '&lsquo;Torches&rsquo; is plural, so &lsquo;were&rsquo;.'),
    ('were being light', 'Third form: lit.'),
    ('were lighting', 'Active &mdash; that says the torches lit something.')],
   'Las antorchas ______ por todo el camino.',
   'Die Fackeln ______ die ganze Stra&szlig;e entlang.',
   why='More than one torch, so &lsquo;were being&rsquo; &mdash; then the third form.'),

# The two halves, and which tense each takes. This is the deck in one question.
mc(3, 6, B % 'bg14.jpg', 'right', 'top', 'Which half is which?',
   'The map was being drawn when the lamp ______ out.', 'went',
   [('was going', 'Both halves long, and then nothing interrupts anything.'),
    ('was gone', 'That is not a past simple; it reads as a state.'),
    ('has gone', 'The sentence is finished and dated, so it cannot take a present perfect.')],
   'El mapa estaba siendo dibujado cuando la l&aacute;mpara se ______.',
   'Die Karte wurde gerade gezeichnet, als die Lampe ______.',
   why='The long action is passive continuous; the thing that cuts across it is a plain past simple.'),

mc(4, 6, B % 'bg28.jpg', 'right', 'bottom', 'Say no',
   'The bridge ______ that week.', "wasn't being repaired",
   [("didn't being repaired", 'A passive never uses &lsquo;did&rsquo;.'),
    ("weren't being repaired", 'One bridge, so &lsquo;was&rsquo;.'),
    ("wasn't been repaired", '&lsquo;been&rsquo; goes with has or have, not with was.')],
   'El puente ______ esa semana.', 'Die Br&uuml;cke ______ in jener Woche.',
   why='The &lsquo;not&rsquo; goes on the first auxiliary: <em class="aux">wasn&rsquo;t</em> + being + the third form.'),

mc(5, 6, B % 'bg33.jpg', 'right', 'top', 'Ask the question',
   '______ the torches being lit when you arrived?', 'Were',
   [('Was', '&lsquo;Torches&rsquo; is plural.'),
    ('Did', 'A passive question never starts with &lsquo;did&rsquo;.'),
    ('Have', 'That would need &lsquo;been&rsquo;, and a time that is still open.')],
   '&iquest;______ encendiendo las antorchas cuando llegaste?',
   '______ die Fackeln gerade angez&uuml;ndet, als du ankamst?',
   why='To ask, the first auxiliary moves to the front. Torches is plural, so &lsquo;Were&rsquo;.'),

mc(6, 6, B % 'bg39.jpg', 'left', 'top', 'Finished, or still going?',
   'Which one says the work had NOT finished?',
   'The wall was being built.',
   [('The wall was built.', 'Finished, and dated. That is station 11.'),
    ('The wall has been built.', 'Finished, and it still counts. That is station 15.'),
    ('The wall is being built.', 'Still going, but now &mdash; not then.')],
   '&iquest;Cu&aacute;l dice que no hab&iacute;a terminado?',
   'Welcher Satz sagt, dass es NICHT fertig war?',
   why='&lsquo;was being&rsquo; is the only one that puts an unfinished action in the past.'),

sort(B % 'bg25.jpg', 'left', 'top', 'Which half takes which tense?',
     'Click a half, then click the tense it takes.',
     ['was / were being &mdash; the long one', 'past simple &mdash; the cut'],
     [(0, 'the wall ___ built'), (0, 'the map ___ drawn'),
      (0, 'the torches ___ lit'), (0, 'the bridge ___ repaired'),
      (1, 'when a creeper arrived'), (1, 'when the lamp went out'),
      (1, 'when we got there'), (1, 'as the sun set')],
     'The long action takes was / were being. The thing that cuts across it '
     'is always a plain past simple.'),

match(B % 'bg31.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('They were building the wall', 'the wall was being built',
        'Estaban construyendo el muro', 'Sie bauten gerade die Mauer',
        'el muro estaba siendo construido', 'die Mauer wurde gerade gebaut'),
       ('Alex was drawing the map', 'the map was being drawn',
        'Alex estaba dibujando el mapa', 'Alex zeichnete gerade die Karte',
        'el mapa estaba siendo dibujado', 'die Karte wurde gerade gezeichnet'),
       ('They were lighting the torches', 'the torches were being lit',
        'Estaban encendiendo las antorchas', 'Sie z&uuml;ndeten gerade die Fackeln an',
        'las antorchas estaban siendo encendidas', 'die Fackeln wurden gerade angez&uuml;ndet'),
       ('Somebody was repairing the bridge', 'the bridge was being repaired',
        'Alguien estaba reparando el puente', 'Jemand reparierte gerade die Br&uuml;cke',
        'el puente estaba siendo reparado', 'die Br&uuml;cke wurde gerade repariert'),
       ('A creeper was watching us', 'we were being watched',
        'Un creeper nos observaba', 'Ein Creeper beobachtete uns',
        'nos estaban observando', 'wir wurden beobachtet'),
       ('They were baking the bread', 'the bread was being baked',
        'Estaban horneando el pan', 'Sie backten gerade das Brot',
        'el pan estaba siendo horneado', 'das Brot wurde gerade gebacken')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg23.jpg', 'left', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The map was being ', 'drawn', '. <span class="dim">(draw)</span>',
      'draw &rarr; drew &rarr; drawn. Not &lsquo;drew&rsquo;.', 170,
      'El mapa estaba siendo ______. (dibujar)',
      'Die Karte wurde gerade ______. (zeichnen)'),
     ('The torches were being ', 'lit', '. <span class="dim">(light)</span>',
      'light &rarr; lit &rarr; lit.', 170,
      'Las antorchas estaban siendo ______. (encender)',
      'Die Fackeln wurden gerade ______. (anz&uuml;nden)'),
     ('The bridge was being ', 'repaired', '. <span class="dim">(repair)</span>',
      'Regular verb, so the third form is just -ed.', 170,
      'El puente estaba siendo ______. (reparar)',
      'Die Br&uuml;cke wurde gerade ______. (reparieren)')]),

gap(2, 2, B % 'bg38.jpg', 'right', 'top', 'Which tense in each half?',
    'The long half is passive; the short one that cuts in is past simple.',
    [('The wall was being built when a creeper ', 'arrived', '.',
      'The interruption is a plain past simple.', 150,
      'El muro estaba siendo construido cuando ______ un creeper.',
      'Die Mauer wurde gerade gebaut, als ein Creeper ______.'),
     ('The map ', 'was', ' being drawn all evening.',
      'One map, so &lsquo;was&rsquo;.', 130,
      'El mapa ______ siendo dibujado toda la tarde.',
      'Die Karte ______ den ganzen Abend gezeichnet.'),
     ('The torches ', 'were', ' being lit as we walked.',
      'Torches is plural.', 130,
      'Las antorchas ______ siendo encendidas mientras and&aacute;bamos.',
      'Die Fackeln ______ angez&uuml;ndet, w&auml;hrend wir gingen.')]),

order(B % 'bg27.jpg', 'left', 'top', 'the wall | was | being | built .',
      'The thing, then was, then being, then the third form.',
      'El muro estaba siendo construido.', 'Die Mauer wurde gerade gebaut.'),

order(B % 'bg34.jpg', 'left', 'top',
      'the map | was | being | drawn | when the lamp | went out .',
      'The long half first, then the short one that cuts across it.',
      'El mapa estaba siendo dibujado cuando se apag&oacute; la l&aacute;mpara.',
      'Die Karte wurde gerade gezeichnet, als die Lampe ausging.'),

results(B % 'bg41.jpg', 'left', 'top'),

activate(B % 'bg19.jpg', 'Now set a scene',
         ['was being built', 'were being made', 'was being repaired',
          'were being watched', 'when', 'while', 'all morning', 'by'],
         ['Describe a place you walked past. What was being done there?',
          'Tell a story with two halves: something long, and the thing that cut across it.',
          'Something was being done and you interrupted it. Say what &mdash; and name nobody.'],
         ['Write six lines of a scene where work was under way, naming nobody.',
          'Then add one line saying what interrupted it. Which tense did that line need?']),
]

STATION = dict(
    file='blockcamp-passive-past-continuous.html',
    chassis='blockcamp-past-continuous.html',   # camp 4: brings its gold with it
    title='Past Continuous Passive',
    sub='Station 12: it was being done, and something cut across it',
    # Not the form - the form is easier than station 15's. It is that the
    # sentence needs two clauses to mean anything, and neither names anybody.
    level='B1',
    doctitle='Block Camp II — Passive 12: Past Continuous Passive (B1) | Forbes English',
    hero=B % 'bg13.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to the two halves. The long one takes was / were being; the cut takes a past simple.',
        resMid='Check &lsquo;was being&rsquo; against &lsquo;was&rsquo;. One had not finished; the other had.',
        resStrong='Strong. Look again at the ones with two clauses in them.',
        resPerfect='Full marks. Now set a scene where work was under way, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zu den zwei H&auml;lften. Die lange nimmt was / were being, der Einschnitt das Past Simple.',
        resMid='Vergleiche &lsquo;was being&rsquo; mit &lsquo;was&rsquo;. Eines war nicht fertig, das andere schon.',
        resStrong='Stark. Sieh dir die S&auml;tze mit zwei Teils&auml;tzen noch einmal an.',
        resPerfect='Volle Punktzahl. Beschreib jetzt eine Szene mit laufender Arbeit - ohne Namen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve a las dos mitades. La larga lleva was / were being; el corte lleva past simple.',
        resMid='Compara &lsquo;was being&rsquo; con &lsquo;was&rsquo;. Uno no hab&iacute;a terminado; el otro s&iacute;.',
        resStrong='Muy bien. Revisa las frases que ten&iacute;an dos mitades.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora monta una escena con trabajo en marcha, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
