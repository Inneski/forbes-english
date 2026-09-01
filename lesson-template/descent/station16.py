# -*- coding: utf-8 -*-
"""Station 16 — The Trial.  Mirrors camp 8, and wears its cyan.

THE LAST STATION, AND IT TEACHES NOTHING NEW. Every other deck on the descent
introduces one auxiliary. This one introduces none: it puts all seven passives
back on the table together, mixed with the actives they came from, and asks a
learner to choose.

WHY THAT IS A DIFFERENT SKILL. Inside station 11 every answer is a past simple
passive, so a learner can score well by pattern rather than by meaning - the
deck itself gives the game away. Take the label off and the question becomes
the real one: which tense, and which voice? That is the only question a
learner is ever asked outside a grammar lesson.

THE TWO DECISIONS, KEPT SEPARATE. The deck is built around them in order,
because a learner who muddles them cannot be helped by being told to try
harder:

    WHICH VOICE   is the doer worth naming? If not, passive.
    WHICH TENSE   when did it happen, and is it finished?

Voice first. A learner who picks the tense first and then tries to bend it
into a passive writes 'the wall was been built', and that sentence is the
reason this deck exists.

CAMP 8 HAS NO PASSIVE OF ITS OWN - nobody says 'has been being built' - so its
plates carry the trial instead. That is why the line has seven tense passives
and a trial rather than eight passives.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'present-perfect-continuous-time-signals/%s'   # camp 8's plates, no passive of its own

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('The trial', 'Two decisions, and they are not the same one') + '\n' +
    cards([
      ('First: which voice?', 'Is the doer worth naming?',
       ['somebody worth naming &rarr; <em class="agent">active</em>',
        'nobody, or obvious &rarr; <em class="obj">passive</em>'],
       gloss('&iquest;Merece la pena nombrar al autor?',
             'Lohnt es sich, den T&auml;ter zu nennen?')),
      ('Then: which tense?', 'When was it, and is it finished?',
       ['now &middot; then &middot; later',
        'finished &middot; still going'],
       gloss('&iquest;Cu&aacute;ndo fue, y ha terminado?',
             'Wann war es, und ist es fertig?')),
    ])),

# THE WHOLE DESCENT ON ONE PAGE. Nothing here is new; the value is that seven
# chains a learner met one at a time are finally side by side - each in its
# own camp's colour, so the grid reads as the trail rather than as a list.
# The third form stays purple down the right-hand edge, which is the point.
sec('teach', B % 'bg22.jpg', 'left', 'top',
    head('The seven', 'Every passive you have met') + '\n' +
    para([
      ('now, in general',
       [('9', '<em class="t-ps">is</em> / <em class="t-ps">are</em> <em class="pp">built</em>')],
       gloss('ahora, en general', 'jetzt, allgemein')),
      ('now, as you watch',
       [('10', '<em class="t-pc">is being</em> <em class="pp">built</em>')],
       gloss('ahora, mientras miras', 'jetzt, w&auml;hrend du zusiehst')),
      ('then, finished',
       [('11', '<em class="t-past">was</em> / <em class="t-past">were</em> <em class="pp">built</em>')],
       gloss('entonces, terminado', 'damals, abgeschlossen')),
      ('then, still going',
       [('12', '<em class="t-pastc">was being</em> <em class="pp">built</em>')],
       gloss('entonces, en marcha', 'damals, im Gange')),
      ('later, planned',
       [('13', '<em class="t-gt">is going to be</em> <em class="pp">built</em>')],
       gloss('luego, planeado', 'sp&auml;ter, geplant')),
      ('later, promised',
       [('14', '<em class="t-fs">will be</em> <em class="pp">built</em>')],
       gloss('luego, prometido', 'sp&auml;ter, versprochen')),
      ('finished, still counts',
       [('15', '<em class="t-pperf">has been</em> <em class="pp">built</em>')],
       gloss('terminado, y a&uacute;n cuenta', 'fertig, und z&auml;hlt noch')),
    ], 'seven chains, one <em class="pp">third form</em> at the end of every one'),
    # Three columns, not four. At four the grid ran 74% of the canvas and the
    # last card of the top row landed on the runner's head - which the
    # negative-space gate cannot see, because it measures the 52% column a
    # normal side-pinned slide occupies and this slide opted out of that.
    'data-w="wide" style="--wcols:3;--col-w:58%"'),

# THE SLIDE THIS DECK OWNS. Voice first, tense second, and the sentence that
# happens when a learner does it the other way round.
sec('teach', B % 'bg16.jpg', 'left', 'top',
    head('The order', 'Voice first, then tense') + '\n' +
    para([
      ('Do it this way',
       [('1', 'nobody worth naming &rarr; <em class="obj">passive</em>'),
        ('2', 'finished, and dated &rarr; <em class="aux">was</em> + <em class="pp">built</em>')],
       gloss('Primero la voz, luego el tiempo', 'Erst das Genus, dann die Zeit')),
      ('Do it the other way and this happens',
       [('', '<s>the wall <em class="aux">was been</em> built</s>')],
       gloss('Al rev&eacute;s sale esto', 'Andersherum kommt das heraus')),
      ('Because the auxiliary belongs to the TENSE',
       [('', 'pick the voice, and the chain writes itself')],
       gloss('El auxiliar pertenece al tiempo', 'Das Hilfsverb geh&ouml;rt zur Zeit')),
    ], 'choose the <b>voice</b>, then the <b>tense</b> &mdash; '
       'never the other way round')),

sec('teach', B % 'bg09.jpg', 'right', 'top',
    head('When NOT to use it', 'The passive is not always the better sentence') + '\n' +
    para([
      ('The doer is the news',
       [('', '<em class="agent">A creeper</em> <em class="t-past">broke</em> the wall. '
             '<span class="dim">(that is the story)</span>')],
       gloss('Si el autor es la noticia', 'Wenn der T&auml;ter die Nachricht ist')),
      ('Nobody is hiding anything',
       [('', '<em class="agent">I</em> <em class="t-past">made</em> this. '
             '<span class="dim">(not: this was made by me)</span>')],
       gloss('Si no se oculta nada', 'Wenn nichts verborgen wird')),
      ('A chain of passives is hard to read',
       [('', 'Two in a row is usually one too many.')],
       gloss('Demasiadas pasivas seguidas cansan',
             'Zu viele Passive hintereinander erm&uuml;den')),
    ], 'the passive is a <b>choice</b>, and sometimes the wrong one')),

sec('teach', B % 'bg28.jpg', 'left', 'top',
    head('The three forms', '<em class="inf">&lsquo;be&rsquo;</em> &middot; '
                            '<em class="aux">&lsquo;being&rsquo;</em> &middot; '
                            '<em class="aux">&lsquo;been&rsquo;</em>') + '\n' +
    para([
      ('after a modal or <em class="aux">&lsquo;going to&rsquo;</em>',
       [('', '<em class="inf">be</em> <em class="pp">built</em>')],
       gloss('tras un modal o &lsquo;going to&rsquo;', 'nach Modalverb oder &lsquo;going to&rsquo;')),
      ('after <em class="aux">&lsquo;is&rsquo;</em>, <em class="aux">&lsquo;are&rsquo;</em>, '
       '<em class="aux">&lsquo;was&rsquo;</em>, <em class="aux">&lsquo;were&rsquo;</em>',
       [('', '<em class="aux">being</em> <em class="pp">built</em>')],
       gloss('tras is, are, was, were', 'nach is, are, was, were')),
      ('after <em class="aux">&lsquo;has&rsquo;</em> or <em class="aux">&lsquo;have&rsquo;</em>',
       [('', '<em class="aux">been</em> <em class="pp">built</em>')],
       gloss('tras has o have', 'nach has oder have')),
    ], 'the word in FRONT decides &mdash; it has decided every time on this descent')),

sec('teach', B % 'bg30.jpg', 'left', 'top',
    head('The doer', 'Everything you have learned about &lsquo;by&rsquo;') + '\n' +
    para([
      ('Keep it &mdash; the doer is a surprise',
       [('', 'The wall was broken <em class="agent">by a creeper</em>.')],
       gloss('Mant&eacute;nlo si sorprende', 'Behalte es, wenn es &uuml;berrascht')),
      ('Drop it &mdash; everybody could guess',
       [('', 'The bread is baked every morning.')],
       gloss('Qu&iacute;talo si es obvio', 'Weg damit, wenn es klar ist')),
      ('Drop it &mdash; you would rather not say',
       [('', 'The window was broken. <span class="dim">(not by me!)</span>')],
       gloss('Qu&iacute;talo si prefieres callarlo', 'Weg damit, wenn du schweigen willst')),
    ], 'most passives, on every station, carry <b>NO</b> &lsquo;by&rsquo; at all')),

sec('teach', B % 'bg36.jpg', 'left', 'top',
    head('Time signals', 'The word that picks the tense for you') + '\n' +
    cards([
      ('Closed time', 'A finished window: past.',
       ['yesterday', 'in 1990', 'last week'],
       gloss('ayer &middot; en 1990 &middot; la semana pasada',
             'gestern &middot; im Jahr 1990 &middot; letzte Woche')),
      ('Open time', 'Still running: present perfect.',
       ['ever', 'never', 'so far', 'already'],
       gloss('alguna vez &middot; nunca &middot; hasta ahora &middot; ya',
             'jemals &middot; nie &middot; bisher &middot; schon')),
    ]),
    'data-w="wide" style="--wcols:2"'),

mc(1, 6, B % 'bg04.jpg', 'left', 'top', 'Which tense?',
   'The wall ______ in 1990.', 'was built',
   [('is built', '&lsquo;In 1990&rsquo; is a closed window, so it cannot be a present.'),
    ('has been built', 'A dated year closes the door; the present perfect needs it open.'),
    ('is being built', 'That would mean the work is happening as you read this.')],
   'El muro ______ en 1990.', 'Die Mauer ______ 1990.',
   why='A named year is a closed window, and a closed window takes the past simple.'),

mc(2, 6, B % 'bg13.jpg', 'left', 'top', 'Which tense?',
   'Listen &mdash; the bell ______ right now.', 'is being rung',
   [('is rung', 'True in general, but the sentence says right now.'),
    ('has been rung', 'That is finished, and you would not be listening to it.'),
    ('was being rung', 'That puts it in the past, and &lsquo;right now&rsquo; does not.')],
   'Escucha: la campana ______ ahora mismo.',
   'H&ouml;r mal - die Glocke ______ gerade.',
   why='&lsquo;Right now&rsquo; plus an unfinished action is the present continuous passive.'),

mc(3, 6, B % 'bg20.jpg', 'left', 'bottom', 'Which voice?',
   'Which is the better sentence to put in a notice?',
   'The gate will be locked at sunset.',
   [('Somebody will lock the gate at sunset.', 'A notice does not need a vague somebody in it.'),
    ('The gate, somebody will lock it at sunset.', 'Two subjects, and neither of them clear.'),
    ('At sunset, a person locks the gate.', 'A present simple, and it names a person nobody asked about.')],
   '&iquest;Cu&aacute;l va mejor en un aviso?',
   'Welcher Satz passt besser auf ein Schild?',
   why='Nobody needs telling who locks a gate, so the passive removes the noise.'),

mc(4, 6, B % 'bg07.jpg', 'right', 'top', 'Which word?',
   'The bridge has ______ repaired at last.', 'been',
   [('being', '&lsquo;being&rsquo; follows is, are, was or were &mdash; never has.'),
    ('be', '&lsquo;be&rsquo; follows a modal or &lsquo;going to&rsquo;.'),
    ('was', 'Two auxiliaries in a row, and neither is a participle.')],
   'El puente ha ______ reparado por fin.',
   'Die Br&uuml;cke ist endlich repariert ______.',
   why='&lsquo;has&rsquo; in front means &lsquo;been&rsquo;, every time, on every station.'),

mc(5, 6, B % 'bg32.jpg', 'left', 'top', 'Active, or passive?',
   'Your friend asks who smashed the window. Which do you say?',
   'A creeper broke it.',
   [('It was broken by a creeper.', 'Correct English, but they asked WHO, so name the creeper first.'),
    ('It was broken.', 'That is the sentence you use to avoid the question.'),
    ('It is being broken.', 'That says it is happening now, and the window is already smashed.')],
   'Te preguntan qui&eacute;n rompi&oacute; la ventana. &iquest;Qu&eacute; dices?',
   'Man fragt dich, wer das Fenster eingeworfen hat. Was sagst du?',
   why='When the doer IS the answer to the question, the active is the better sentence.'),

mc(6, 6, B % 'bg34.jpg', 'left', 'top', 'Which tense?',
   'The village ______ down twice, and it is still standing.',
   'has been knocked',
   [('was knocked', 'That closes the window, and the sentence keeps it open with &lsquo;still&rsquo;.'),
    ('is knocked', 'A present simple would make it a routine, twice a day.'),
    ('will be knocked', 'That has not happened yet, and this has happened twice.')],
   'El pueblo ______ dos veces, y sigue en pie.',
   'Das Dorf ______ zweimal, und es steht noch.',
   why='A count so far, in a window that is still open, is the present perfect passive.'),

sort(B % 'bg26.jpg', 'left', 'top', 'Which station does it come from?',
     'Click a chain, then click when it happens.',
     ['now', 'then', 'later'],
     [(0, 'is mined'), (0, 'is being mined'),
      (1, 'was mined'), (1, 'was being mined'), (1, 'has been mined'),
      (2, 'is going to be mined'), (2, 'will be mined')],
     'Present perfect looks back from now, so it sits with THEN &mdash; but the '
     'window it looks through is still open, which is why it can say &lsquo;so far&rsquo;.'),

match(B % 'bg23.jpg', 'right', 'top', 'Match the sentence to its job',
      'Click a sentence, then click what it is doing.',
      [('The gate is locked at sunset.', 'a rule, every day',
        'La puerta se cierra al anochecer.', 'Das Tor wird bei Sonnenuntergang verschlossen.',
        'una norma, cada d&iacute;a', 'eine Regel, jeden Tag'),
       ('The gate is being locked.', 'happening as you watch',
        'Est&aacute;n cerrando la puerta.', 'Das Tor wird gerade verschlossen.',
        'pasa mientras miras', 'passiert, w&auml;hrend du zusiehst'),
       ('The gate was locked at sunset.', 'finished, and dated',
        'La puerta fue cerrada al anochecer.', 'Das Tor wurde bei Sonnenuntergang verschlossen.',
        'terminado, con fecha', 'abgeschlossen, mit Datum'),
       ('The gate has been locked.', 'finished, and it still counts',
        'La puerta ha sido cerrada.', 'Das Tor ist verschlossen worden.',
        'terminado, y a&uacute;n cuenta', 'fertig, und z&auml;hlt noch'),
       ('The gate is going to be locked.', 'a plan already made',
        'La puerta va a ser cerrada.', 'Das Tor wird geschlossen werden.',
        'un plan ya hecho', 'ein fertiger Plan'),
       ('The gate will be locked.', 'a promise, or a guess',
        'La puerta ser&aacute; cerrada.', 'Das Tor wird verschlossen werden.',
        'una promesa o una suposici&oacute;n', 'ein Versprechen oder eine Vermutung')],
      'Same gate, same passive, six different jobs. The chain in the middle is what changes.'),

gap(1, 2, B % 'bg19.jpg', 'right', 'top', 'Fill the chain',
    'The time signal tells you which tense; the missing word tells you which chain.',
    [('The wall was ', 'built', ' in 1990. <span class="dim">(build)</span>',
      'A closed window, so the past simple passive: was + the third form.', 150,
      'El muro fue ______ en 1990. (construir)',
      'Die Mauer wurde 1990 ______. (bauen)'),
     ('The bridge has ', 'been', ' repaired at last.',
      '&lsquo;has&rsquo; always takes &lsquo;been&rsquo;.', 140,
      'El puente ha ______ reparado por fin.',
      'Die Br&uuml;cke ist endlich repariert ______.'),
     ('The gate will ', 'be', ' locked from Monday.',
      'A modal always takes the bare verb &lsquo;be&rsquo;.', 120,
      'La puerta ______ cerrada desde el lunes.',
      'Das Tor wird ab Montag verschlossen ______.')]),

gap(2, 2, B % 'bg31.jpg', 'right', 'top', 'Which voice does it want?',
    'Type &lsquo;active&rsquo; or &lsquo;passive&rsquo; for each situation.',
    [('A notice on a wall about closing time: ', 'passive', '.',
      'A notice names nobody, so the passive is the better sentence.', 150,
      'Un aviso sobre la hora de cierre: ______.',
      'Ein Schild &uuml;ber die Schlie&szlig;zeit: ______.'),
     ('Somebody asks who broke the window: ', 'active', '.',
      'The doer IS the answer, so name them.', 150,
      'Te preguntan qui&eacute;n rompi&oacute; la ventana: ______.',
      'Jemand fragt, wer das Fenster zerbrochen hat: ______.'),
     ('Explaining how iron is smelted: ', 'passive', '.',
      'A process is about the steps, not about who takes them.', 150,
      'Explicar c&oacute;mo se funde el hierro: ______.',
      'Erkl&auml;ren, wie Eisen geschmolzen wird: ______.')]),

order(B % 'bg38.jpg', 'left', 'top',
      'the village | has | been | rebuilt | twice .',
      'The thing, then has, then been, then the third form, then the count.',
      'El pueblo ha sido reconstruido dos veces.',
      'Das Dorf ist zweimal wieder aufgebaut worden.'),

order(B % 'bg40.jpg', 'right', 'top',
      'the gate | will | be | locked | at sunset .',
      'The thing, then will, then be, then the third form, then the time.',
      'La puerta ser&aacute; cerrada al anochecer.',
      'Das Tor wird bei Sonnenuntergang verschlossen werden.'),

results(B % 'bg41.jpg', 'left', 'top'),

activate(B % 'bg35.jpg', 'Now choose for yourself',
         ['is done', 'is being done', 'was done', 'has been done',
          'is going to be done', 'will be done', 'by', 'nobody'],
         ['Describe how something is made where you live. Then say who makes it '
          'in ONE sentence, and explain why that sentence needed the active.',
          'Tell a story with three tenses in it. Use the passive whenever the '
          'doer is not the point.',
          'Read a notice out loud, then say the same thing to a friend. What changed?'],
         ['Write eight lines about a place that has changed, mixing both voices.',
          'Then mark every passive. Could any of them be active without getting worse?']),
]

STATION = dict(
    file='blockcamp-passive-trial.html',
    chassis='blockcamp-present-perfect-continuous.html',   # camp 8's cyan
    title='The Trial',
    sub='Station 16: every tense, both voices, no labels',
    # The chains are all revision, but nothing here is labelled - a learner has
    # to choose the voice and then the tense with no deck telling them which.
    # That is the hardest thing on the descent, and the only thing they will
    # ever be asked outside a grammar lesson.
    level='B1',
    doctitle='Block Camp II — Passive 16: The Trial (B1) | Forbes English',
    hero=B % 'bg22.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to the order: voice first, then tense. Picking the tense first is what makes &lsquo;was been built&rsquo;.',
        resMid='Check the time signals. A closed window takes the past; an open one takes the present perfect.',
        resStrong='Strong. Look again at the two where the ACTIVE was the better sentence.',
        resPerfect='Full marks, and that is the descent finished. Both voices, seven tenses, your choice.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zur Reihenfolge: erst Genus, dann Zeit. Andersherum entsteht &lsquo;was been built&rsquo;.',
        resMid='Sieh dir die Zeitsignale an. Geschlossenes Fenster: Past. Offenes: Present Perfect.',
        resStrong='Stark. Sieh dir die zwei an, wo das AKTIV der bessere Satz war.',
        resPerfect='Volle Punktzahl - und damit ist der Abstieg geschafft. Beide Genera, sieben Zeiten, deine Wahl.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve al orden: primero la voz, luego el tiempo. Al rev&eacute;s sale &lsquo;was been built&rsquo;.',
        resMid='Mira las se&ntilde;ales de tiempo. Ventana cerrada: pasado. Abierta: present perfect.',
        resStrong='Muy bien. Revisa las dos donde la ACTIVA era la mejor frase.',
        resPerfect='Puntuaci&oacute;n perfecta, y con eso acaba el descenso. Dos voces, siete tiempos, t&uacute; eliges.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
