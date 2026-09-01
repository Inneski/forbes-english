# -*- coding: utf-8 -*-
"""Station 13 — Going To Passive.  Mirrors camp 5, and wears its lime.

THE FIRST FUTURE ON THE WAY DOWN, and the first deck where the object and a
bare verb stand on one page - which is why --mark-obj was moved off the gold
before this station was written. See the ruling in build_descent.py.

    the wall is going to be built

FOUR WORDS OF AUXILIARY, and that is the whole difficulty. A learner who has
stations 9 to 12 can build every one of them; what they cannot do yet is keep
`be` in the middle. It is the one word with no meaning of its own here - it is
not the `be` of `is`, it is the bare verb that `going to` demands - and it is
the word they drop:

    <s>the wall is going to built</s>     the bare verb is missing
    <s>the wall is going to being built</s>  station 10's word, in the wrong slot

So `be` gets the gold of every bare verb after a modal or `going to`, because
that is exactly what it is, and the deck says so out loud rather than asking a
learner to notice.

WHAT THIS TENSE MEANS, and it is camp 5's meaning unchanged: a plan already
made, or evidence you can point at. The passive removes the planner - which is
what makes it the voice of an announcement.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'going-to-infinitive/%s'   # camp 5's own plates

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'It is going to be done, and nobody is named') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> are going to build <em class="obj">the wall</em>.',
       ['<em class="agent">Alex</em> is going to draw <em class="obj">the map</em>',
        '<em class="agent">they</em> are going to plant <em class="obj">the wheat</em>'],
       gloss('Los aldeanos van a construir el muro.',
             'Dorfbewohner werden die Mauer bauen.')),
      ('Passive', '<em class="obj">The wall</em> <em class="aux">is going to</em> '
       '<em class="inf">be</em> <em class="pp">built</em>.',
       ['<em class="obj">the map</em> <em class="aux">is going to</em> <em class="inf">be</em> <em class="pp">drawn</em>',
        '<em class="obj">the wheat</em> <em class="aux">is going to</em> <em class="inf">be</em> <em class="pp">planted</em>'],
       gloss('El muro va a ser construido.',
             'Die Mauer wird gebaut werden.')),
    ])),

# THE WORD THEY DROP, NAMED. 'be' is gold here because it IS the bare verb
# after 'going to' - the same job it does in the active, on the same deck.
sec('teach', B % 'bg21.jpg', 'right', 'top',
    head('The form', 'The word in the middle is <em class="inf">&lsquo;be&rsquo;</em>') + '\n' +
    para([
      ('Active &mdash; a bare verb after &lsquo;going to&rsquo;',
       [('', 'they <em class="aux">are going to</em> <em class="inf">build</em> it')],
       gloss('Activa: verbo en infinitivo', 'Aktiv: Grundform nach &lsquo;going to&rsquo;')),
      ('Passive &mdash; the bare verb is <em class="inf">be</em>',
       [('', 'it <em class="aux">is going to</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('Pasiva: el infinitivo es &lsquo;be&rsquo;',
             'Passiv: die Grundform ist &lsquo;be&rsquo;')),
      ('Drop it and the sentence breaks',
       [('', '<s>it is going to <em class="pp">built</em></s>')],
       gloss('Si lo quitas, la frase se rompe',
             'L&auml;sst man es weg, bricht der Satz')),
    ], '<em class="obj">THING</em> + <em class="aux">is</em> / <em class="aux">are going to</em> '
       '+ <em class="inf">be</em> + <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg06.jpg', 'left', 'top',
    head('The form', 'Only the first word changes') + '\n' +
    para([
      ('One thing', [('the wall', '<em class="aux">is going to</em> <em class="inf">be</em> <em class="pp">built</em>'),
                     ('no', '<em class="aux">isn&rsquo;t going to</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('va a ser construido', 'wird gebaut werden')),
      ('More than one', [('the walls', '<em class="aux">are going to</em> <em class="inf">be</em> <em class="pp">built</em>'),
                         ('no', '<em class="aux">aren&rsquo;t going to</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('van a ser construidos', 'werden gebaut werden')),
      ('Asking', [('one', '<em class="aux">Is</em> it <em class="aux">going to</em> <em class="inf">be</em> <em class="pp">built</em>?'),
                  ('more', '<em class="aux">Are</em> they <em class="aux">going to</em> <em class="inf">be</em> <em class="pp">built</em>?')],
       gloss('&iquest;Va a ser construido?', 'Wird sie gebaut werden?')),
    ], 'only <em class="aux">&lsquo;is&rsquo;</em> / <em class="aux">&lsquo;are&rsquo;</em> changes &mdash; '
       '<em class="inf">&lsquo;be&rsquo;</em> and the <em class="pp">participle</em> never do')),

# THE TRAP: two words that both follow an auxiliary and both come from 'be'.
# Station 10 taught 'being'; this deck's word is 'be', and they are one slot
# apart in the same sentence shape.
sec('teach', B % 'bg28.jpg', 'right', 'top',
    head('The trap', '<em class="inf">&lsquo;be&rsquo;</em>, '
                     '<em class="aux">&lsquo;being&rsquo;</em>, '
                     '<em class="aux">&lsquo;been&rsquo;</em>') + '\n' +
    para([
      ('after <em class="aux">&lsquo;going to&rsquo;</em>',
       [('', 'it is going to <em class="inf">be</em> <em class="pp">built</em> '
             '<span class="dim">(a plan)</span>')],
       gloss('tras &lsquo;going to&rsquo;', 'nach &lsquo;going to&rsquo;')),
      ('after <em class="aux">&lsquo;is&rsquo;</em> / <em class="aux">&lsquo;are&rsquo;</em>',
       [('', 'it is <em class="aux">being</em> <em class="pp">built</em> '
             '<span class="dim">(right now)</span>')],
       gloss('tras &lsquo;is&rsquo; / &lsquo;are&rsquo;', 'nach &lsquo;is&rsquo; / &lsquo;are&rsquo;')),
      ('after <em class="aux">&lsquo;has&rsquo;</em> / <em class="aux">&lsquo;have&rsquo;</em>',
       [('', 'it has <em class="aux">been</em> <em class="pp">built</em> '
             '<span class="dim">(finished)</span>')],
       gloss('tras &lsquo;has&rsquo; / &lsquo;have&rsquo;', 'nach &lsquo;has&rsquo; / &lsquo;have&rsquo;')),
    ], 'the word in FRONT decides which one &mdash; every time')),

sec('teach', B % 'bg04.jpg', 'left', 'top',
    head('Why choose it', 'A plan made, and a planner removed') + '\n' +
    para([
      ('The decision is already taken',
       [('', '<em class="obj">The bridge</em> <em class="aux">is going to</em> <em class="inf">be</em> '
             '<em class="pp">repaired</em> next week.')],
       gloss('La decisi&oacute;n ya est&aacute; tomada', 'Die Entscheidung ist gefallen')),
      ('You can see it coming',
       [('', '<em class="obj">That wall</em> <em class="aux">is going to</em> <em class="inf">be</em> '
             '<em class="pp">knocked</em> down &mdash; look at it.')],
       gloss('Se ve venir', 'Man sieht es kommen')),
      ('An announcement names nobody',
       [('', '<em class="obj">The gate</em> <em class="aux">is going to</em> <em class="inf">be</em> '
             '<em class="pp">closed</em> at sunset.')],
       gloss('Un aviso no nombra a nadie', 'Eine Ansage nennt niemanden')),
    ], 'this is the voice of a notice on a wall')),

sec('teach', B % 'bg19.jpg', 'right', 'top',
    head('Time signals', 'How far ahead the plan reaches') + '\n' +
    cards([
      ('Soon', 'Close enough to point at.',
       ['tonight', 'tomorrow', 'any minute now'],
       gloss('esta noche &middot; ma&ntilde;ana &middot; en cualquier momento',
             'heute Abend &middot; morgen &middot; jeden Moment')),
      ('Further out', 'Still decided, just not yet.',
       ['next week', 'next month', 'next year'],
       gloss('la semana que viene &middot; el mes que viene &middot; el a&ntilde;o que viene',
             'n&auml;chste Woche &middot; n&auml;chsten Monat &middot; n&auml;chstes Jahr')),
    ]),
    'data-w="wide" style="--wcols:2"'),

sec('teach', B % 'bg16.jpg', 'left', 'top',
    head('The doer', 'The planner is the first thing to go') + '\n' +
    para([
      ('Worth saying',
       [('yes', '<em class="obj">The map</em> <em class="aux">is going to</em> <em class="inf">be</em> '
                '<em class="pp">drawn</em> <em class="agent">by Alex</em>.')],
       gloss('Vale la pena decirlo', 'Der T&auml;ter ist eine Neuigkeit')),
      ('Not worth saying',
       [('no', '<em class="obj">The wheat</em> <em class="aux">is going to</em> <em class="inf">be</em> '
              '<em class="pp">planted</em> tomorrow.')],
       gloss('No hace falta decirlo', 'Muss man nicht sagen')),
    ], 'an announcement that names its author is not an announcement')),

mc(1, 6, B % 'bg02.jpg', 'right', 'top', 'Choose the passive',
   'The wall ______ next week.', 'is going to be built',
   [('is going to built', 'The bare verb &lsquo;be&rsquo; is missing.'),
    ('is going to being built', '&lsquo;being&rsquo; follows is or are, not &lsquo;going to&rsquo;.'),
    ('are going to be built', 'One wall, so &lsquo;is&rsquo;.')],
   'El muro ______ la semana que viene.',
   'Die Mauer ______ n&auml;chste Woche.',
   why='&lsquo;going to&rsquo; takes a bare verb, and in the passive that bare verb is &lsquo;be&rsquo;.'),

mc(2, 6, B % 'bg15.jpg', 'right', 'top', 'Choose the passive',
   'The torches ______ tonight.', 'are going to be lit',
   [('is going to be lit', '&lsquo;Torches&rsquo; is plural, so &lsquo;are&rsquo;.'),
    ('are going to be light', 'Third form: lit.'),
    ('are going to lighting', 'Neither a bare verb nor a participle.')],
   'Las antorchas ______ esta noche.', 'Die Fackeln ______ heute Abend.',
   why='More than one torch, so &lsquo;are going to&rsquo; &mdash; then be, then the third form.'),

# The be / being / been question, which is the deck's own trap.
mc(3, 6, B % 'bg39.jpg', 'right', 'bottom', 'Which word goes in?',
   'The bridge is going to ______ repaired.', 'be',
   [('being', '&lsquo;being&rsquo; follows is or are. After &lsquo;going to&rsquo; it is &lsquo;be&rsquo;.'),
    ('been', '&lsquo;been&rsquo; follows has or have.'),
    ('is', 'Two auxiliaries in a row, and none of them a bare verb.')],
   'El puente va a ______ reparado.', 'Die Br&uuml;cke wird repariert ______.',
   why='&lsquo;going to&rsquo; always takes a bare verb, and the bare verb of the passive is &lsquo;be&rsquo;.'),

mc(4, 6, B % 'bg30.jpg', 'left', 'bottom', 'Say no',
   'The wheat ______ this year.', "isn't going to be planted",
   [("isn't going to plant", 'Active &mdash; that says the wheat plants something.'),
    ("doesn't going to be planted", 'A passive never uses &lsquo;does&rsquo;.'),
    ("aren't going to be planted", 'Wheat is uncountable, so &lsquo;is&rsquo;.')],
   'El trigo ______ este a&ntilde;o.', 'Der Weizen ______ dieses Jahr.',
   why='The &lsquo;not&rsquo; goes on the first auxiliary, and the rest of the chain does not move.'),

mc(5, 6, B % 'bg09.jpg', 'right', 'top', 'Ask the question',
   '______ the gate going to be closed at sunset?', 'Is',
   [('Are', '&lsquo;Gate&rsquo; is one thing.'),
    ('Does', 'A passive question never starts with &lsquo;does&rsquo;.'),
    ('Will', 'That is station 14, and it would need &lsquo;will be&rsquo; without &lsquo;going to&rsquo;.')],
   '&iquest;______ a cerrarse la puerta al anochecer?',
   '______ das Tor bei Sonnenuntergang geschlossen?',
   why='To ask, the first auxiliary moves to the front. One gate, so &lsquo;Is&rsquo;.'),

mc(6, 6, B % 'bg11.jpg', 'left', 'top', 'Plan, or evidence?',
   'Look at those cracks. The wall ______ down.', 'is going to be knocked',
   [('was going to be knocked', 'A plan somebody had in the past. The cracks are here NOW.'),
    ('is currently being knocked', 'That says the work is happening as you speak.'),
    ('has already been knocked', 'Finished, and the wall would already be gone.')],
   'Mira esas grietas. El muro ______.',
   'Sieh dir die Risse an. Die Mauer ______.',
   why='Evidence you can point at is exactly what &lsquo;going to&rsquo; is for.'),

sort(B % 'bg26.jpg', 'left', 'top',
     '<em class="inf">be</em>, <em class="aux">being</em>, or <em class="aux">been</em>?',
     'Click a beginning, then click the word that follows it.',
     ['be', 'being', 'been'],
     [(0, 'it is going to ___ built'), (0, 'they are going to ___ made'),
      (1, 'the wall is ___ built'), (1, 'we are ___ watched'),
      (2, 'the wall has ___ built'), (2, 'they have ___ found')],
     '&lsquo;going to&rsquo; takes the bare verb &lsquo;be&rsquo;. '
     '&lsquo;is&rsquo; and &lsquo;are&rsquo; take &lsquo;being&rsquo;. '
     '&lsquo;has&rsquo; and &lsquo;have&rsquo; take &lsquo;been&rsquo;.'),

match(B % 'bg13.jpg', 'right', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('They are going to build the wall', 'the wall is going to be built',
        'Van a construir el muro', 'Sie werden die Mauer bauen',
        'el muro va a ser construido', 'die Mauer wird gebaut werden'),
       ('Alex is going to draw the map', 'the map is going to be drawn',
        'Alex va a dibujar el mapa', 'Alex wird die Karte zeichnen',
        'el mapa va a ser dibujado', 'die Karte wird gezeichnet werden'),
       ('They are going to plant the wheat', 'the wheat is going to be planted',
        'Van a plantar el trigo', 'Sie werden den Weizen pflanzen',
        'el trigo va a ser plantado', 'der Weizen wird gepflanzt werden'),
       ('Somebody is going to repair the bridge', 'the bridge is going to be repaired',
        'Alguien va a reparar el puente', 'Jemand wird die Br&uuml;cke reparieren',
        'el puente va a ser reparado', 'die Br&uuml;cke wird repariert werden'),
       ('They are going to light the torches', 'the torches are going to be lit',
        'Van a encender las antorchas', 'Sie werden die Fackeln anz&uuml;nden',
        'las antorchas van a ser encendidas', 'die Fackeln werden angez&uuml;ndet werden'),
       ('They are going to close the gate', 'the gate is going to be closed',
        'Van a cerrar la puerta', 'Sie werden das Tor schlie&szlig;en',
        'la puerta va a ser cerrada', 'das Tor wird geschlossen werden')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg17.jpg', 'left', 'top', 'Write the missing word',
    'One word is missing from every chain, and it is the same word.',
    [('The wall is going to ', 'be', ' built.',
      '&lsquo;going to&rsquo; takes a bare verb; in the passive it is &lsquo;be&rsquo;.', 120,
      'El muro va a ______ construido.', 'Die Mauer wird gebaut ______.'),
     ('The torches are going to ', 'be', ' lit.',
      'The chain does not change when the subject is plural.', 120,
      'Las antorchas van a ______ encendidas.',
      'Die Fackeln werden angez&uuml;ndet ______.'),
     ('Is the gate going to ', 'be', ' closed?',
      'In a question the auxiliary moves, but &lsquo;be&rsquo; stays put.', 120,
      '&iquest;La puerta va a ______ cerrada?',
      'Wird das Tor geschlossen ______?')]),

gap(2, 2, B % 'bg31.jpg', 'left', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The map is going to be ', 'drawn', '. <span class="dim">(draw)</span>',
      'draw &rarr; drew &rarr; drawn.', 170,
      'El mapa va a ser ______. (dibujar)',
      'Die Karte wird ______ werden. (zeichnen)'),
     ('The wheat is going to be ', 'planted', '. <span class="dim">(plant)</span>',
      'Regular verb, so the third form is just -ed.', 170,
      'El trigo va a ser ______. (plantar)',
      'Der Weizen wird ______ werden. (pflanzen)'),
     ('The torches are going to be ', 'lit', '. <span class="dim">(light)</span>',
      'light &rarr; lit &rarr; lit.', 170,
      'Las antorchas van a ser ______. (encender)',
      'Die Fackeln werden ______ werden. (anz&uuml;nden)')]),

order(B % 'bg38.jpg', 'right', 'top',
      'the wall | is | going to | be | built .',
      'The thing, then is going to, then be, then the third form.',
      'El muro va a ser construido.', 'Die Mauer wird gebaut werden.'),

order(B % 'bg40.jpg', 'left', 'top',
      'the map | is | going to | be | drawn | by Alex .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.',
      'El mapa va a ser dibujado por Alex.',
      'Die Karte wird von Alex gezeichnet werden.'),

results(B % 'bg25.jpg', 'right', 'top'),

activate(B % 'bg35.jpg', 'Now announce something',
         ['is going to be built', 'are going to be made', 'is going to be closed',
          'is going to be repaired', 'tomorrow', 'next week', 'any minute now', 'by'],
         ['Announce three changes coming to your town. Name nobody who decided them.',
          'Point at something and say what is going to be done to it, and when.',
          'Read out a notice: what is going to be closed, and from when?'],
         ['Write a notice for a village wall in six lines, naming nobody.',
          'Then rewrite one line as active. Did the notice get better or worse?']),
]

STATION = dict(
    file='blockcamp-passive-going-to.html',
    chassis='blockcamp-going-to.html',   # camp 5: brings its lime with it
    title='Going To Passive',
    sub='Station 13: it is going to be done, and nobody is named',
    # Camp 5 part 1 is A1, but this chain is four auxiliary words long and the
    # deck has to hold be / being / been apart. B1, like station 12.
    level='B1',
    doctitle='Block Camp II — Passive 13: Going To Passive (B1) | Forbes English',
    hero=B % 'bg21.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to the word in the middle. &lsquo;going to&rsquo; always takes the bare verb &lsquo;be&rsquo;.',
        resMid='Check be against being and been. The word in FRONT decides which one.',
        resStrong='Strong. Look again at the ones where the chain was four words long.',
        resPerfect='Full marks. Now announce something, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zum Wort in der Mitte. Nach &lsquo;going to&rsquo; steht immer die Grundform &lsquo;be&rsquo;.',
        resMid='Vergleiche be, being und been. Das Wort DAVOR entscheidet.',
        resStrong='Stark. Sieh dir die S&auml;tze mit der vierteiligen Kette noch einmal an.',
        resPerfect='Volle Punktzahl. Verk&uuml;nde jetzt etwas - ohne jemanden zu nennen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve a la palabra del medio. Tras &lsquo;going to&rsquo; siempre va el infinitivo &lsquo;be&rsquo;.',
        resMid='Compara be, being y been. Lo decide la palabra de DELANTE.',
        resStrong='Muy bien. Revisa las frases con la cadena de cuatro palabras.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora anuncia algo, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
