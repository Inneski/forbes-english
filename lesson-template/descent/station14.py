# -*- coding: utf-8 -*-
"""Station 14 — Future Simple Passive.  Mirrors camp 6, and wears its orange.

THE SHORTEST FUTURE PASSIVE, AND THE EASIEST CHAIN ON THE DESCENT.

    the wall will be built

`will` never changes - not for one thing, not for many, not for I - so this
deck has no is/are, no was/were, no has/have. It is the only station where
the auxiliary does not have to agree with anything, and that is worth saying
out loud, because a learner who has just come through stations 9 to 13 has
spent five decks counting the thing in front.

WHAT IT COSTS INSTEAD is the choice against station 13. `will be built` and
`is going to be built` are both futures, both passive, both correct English,
and camp 6's whole second half is about which one a speaker picks. The passive
does not change that choice, it only removes the person making it - so this
deck's last teaching slide is the contrast, and its hardest question is a
learner deciding between two right-looking sentences.

    will be     -> a prediction, or a decision made as you speak
    is going to be -> a plan already made, or evidence in front of you
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'future-simple-will/%s'   # camp 6's own plates

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'It will be done, and nobody is named') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> <em class="modal">will</em> '
       '<em class="inf">build</em> <em class="obj">the wall</em>.',
       ['<em class="agent">Alex</em> <em class="modal">will</em> <em class="inf">draw</em> <em class="obj">the map</em>',
        '<em class="agent">they</em> <em class="modal">will</em> <em class="inf">light</em> <em class="obj">the torches</em>'],
       gloss('Los aldeanos construir&aacute;n el muro.', 'Dorfbewohner werden die Mauer bauen.')),
      ('Passive', '<em class="obj">The wall</em> <em class="modal">will</em> '
       '<em class="inf">be</em> <em class="pp">built</em>.',
       ['<em class="obj">the map</em> <em class="modal">will</em> <em class="inf">be</em> <em class="pp">drawn</em>',
        '<em class="obj">the torches</em> <em class="modal">will</em> <em class="inf">be</em> <em class="pp">lit</em>'],
       gloss('El muro ser&aacute; construido.', 'Die Mauer wird gebaut werden.')),
    ])),

# THE ONE THING THIS DECK MAKES EASIER, and after five decks of counting the
# subject it deserves its own slide rather than a footnote.
sec('teach', B % 'bg13.jpg', 'right', 'top',
    head('The form', 'Nothing agrees with anything') + '\n' +
    para([
      ('One thing', [('the wall', '<em class="modal">will</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('una cosa', 'eine Sache')),
      ('More than one', [('the walls', '<em class="modal">will</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('varias cosas', 'mehrere Sachen')),
      ('Me, you, anybody', [('I / you / they', '<em class="modal">will</em> <em class="inf">be</em> <em class="pp">told</em>')],
       gloss('yo, t&uacute;, cualquiera', 'ich, du, alle')),
    ], '<em class="obj">THING</em> + <em class="modal">will</em> + <em class="inf">be</em> '
       '+ <em class="pp">PAST PARTICIPLE</em> &mdash; the same four words every time')),

sec('teach', B % 'bg29.jpg', 'left', 'top',
    head('The form', 'Saying no, and asking') + '\n' +
    para([
      ('No', [('long', '<em class="modal">will not</em> <em class="inf">be</em> <em class="pp">built</em>'),
              ('short', '<em class="modal">won&rsquo;t</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('no ser&aacute; construido', 'wird nicht gebaut werden')),
      ('Asking', [('', '<em class="modal">Will</em> it <em class="inf">be</em> <em class="pp">built</em>?')],
       gloss('&iquest;Ser&aacute; construido?', 'Wird sie gebaut werden?')),
      ('Short answers', [('yes', 'Yes, it <em class="modal">will</em>.'),
                         ('no', 'No, it <em class="modal">won&rsquo;t</em>.')],
       gloss('S&iacute;. / No.', 'Ja. / Nein.')),
    ], 'the <em class="modal">&lsquo;not&rsquo;</em> goes on '
       '<em class="modal">&lsquo;will&rsquo;</em>, and nothing else moves')),

sec('teach', B % 'bg22.jpg', 'right', 'top',
    head('The trap', 'The bare verb is still <em class="inf">&lsquo;be&rsquo;</em>') + '\n' +
    para([
      ('Active &mdash; a bare verb after will',
       [('', 'they <em class="modal">will</em> <em class="inf">build</em> it')],
       gloss('Activa: infinitivo tras &lsquo;will&rsquo;', 'Aktiv: Grundform nach &lsquo;will&rsquo;')),
      ('Passive &mdash; that bare verb is <em class="inf">be</em>',
       [('', 'it <em class="modal">will</em> <em class="inf">be</em> <em class="pp">built</em>')],
       gloss('Pasiva: el infinitivo es &lsquo;be&rsquo;', 'Passiv: die Grundform ist &lsquo;be&rsquo;')),
      ('Never <em class="aux">&lsquo;being&rsquo;</em> or <em class="aux">&lsquo;been&rsquo;</em> here',
       [('', '<s>it will being built</s> &nbsp;&middot;&nbsp; <s>it will been built</s>')],
       gloss('Nunca &lsquo;being&rsquo; ni &lsquo;been&rsquo;', 'Nie &lsquo;being&rsquo; oder &lsquo;been&rsquo;')),
    ], 'a modal always takes a bare verb &mdash; and here it is '
       '<em class="inf">&lsquo;be&rsquo;</em>')),

sec('teach', B % 'bg17.jpg', 'right', 'top',
    head('Why choose it', 'A promise, a prediction, a rule for later') + '\n' +
    para([
      ('A prediction',
       [('', '<em class="obj">The bridge</em> <em class="modal">will</em> <em class="inf">be</em> '
             '<em class="pp">finished</em> by winter.')],
       gloss('Una predicci&oacute;n', 'Eine Vorhersage')),
      ('A promise, with the promiser removed',
       [('', '<em class="obj">Your map</em> <em class="modal">will</em> <em class="inf">be</em> '
             '<em class="pp">returned</em>.')],
       gloss('Una promesa, sin quien la hace', 'Ein Versprechen, ohne den Versprechenden')),
      ('A rule that starts later',
       [('', '<em class="obj">The gate</em> <em class="modal">will</em> <em class="inf">be</em> '
             '<em class="pp">locked</em> from Monday.')],
       gloss('Una norma futura', 'Eine k&uuml;nftige Regel')),
    ], 'this is the voice of a promise you cannot pin on anybody')),

# THE CHOICE. Camp 6's second half in one slide, with the doer already gone
# from both sides so only the meaning is left to choose between.
sec('teach', B % 'bg25.jpg', 'left', 'top',
    head('The choice', '<em class="modal">will be</em>, or '
                       '<em class="aux">is going to be</em>?') + '\n' +
    para([
      ('<em class="modal">will be</em> &mdash; you decide as you speak',
       [('', 'Fine &mdash; <em class="obj">it</em> <em class="modal">will</em> '
             '<em class="inf">be</em> <em class="pp">rebuilt</em>.')],
       gloss('Lo decides al hablar', 'Du entscheidest im Sprechen')),
      ('<em class="modal">will be</em> &mdash; or you are guessing',
       [('', '<em class="obj">It</em> <em class="modal">will</em> <em class="inf">be</em> '
             '<em class="pp">finished</em> by Friday, I think.')],
       gloss('O est&aacute;s adivinando', 'Oder du vermutest')),
      ('<em class="aux">is going to be</em> &mdash; already decided, or in front of you',
       [('', '<em class="obj">It</em> <em class="aux">is going to</em> <em class="inf">be</em> '
             '<em class="pp">rebuilt</em> &mdash; look at the plans.')],
       gloss('Ya decidido, o a la vista', 'Schon entschieden, oder sichtbar')),
    ], 'the passive changes neither one &mdash; it only removes who decided')),

sec('teach', B % 'bg09.jpg', 'left', 'top',
    head('The doer', 'A promise rarely names its keeper') + '\n' +
    para([
      ('Worth saying',
       [('yes', '<em class="obj">The map</em> <em class="modal">will</em> <em class="inf">be</em> '
                '<em class="pp">drawn</em> <em class="agent">by Alex</em>.')],
       gloss('Vale la pena decirlo', 'Der T&auml;ter ist eine Neuigkeit')),
      ('Not worth saying',
       [('no', '<em class="obj">You</em> <em class="modal">will</em> <em class="inf">be</em> '
              '<em class="pp">told</em> tomorrow.')],
       gloss('No hace falta decirlo', 'Muss man nicht sagen')),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

mc(1, 6, B % 'bg05.jpg', 'left', 'top', 'Choose the passive',
   'The wall ______ by winter.', 'will be built',
   [('will built', 'The bare verb &lsquo;be&rsquo; is missing.'),
    ('will being built', '&lsquo;being&rsquo; follows is or are, never a modal.'),
    ('will be build', 'Third form: built.')],
   'El muro ______ para el invierno.', 'Die Mauer ______ bis zum Winter.',
   why='A modal takes a bare verb, and in the passive that bare verb is &lsquo;be&rsquo;.'),

mc(2, 6, B % 'bg12.jpg', 'right', 'top', 'One, or many?',
   'The torches ______ at sunset.', 'will be lit',
   [('will are be lit', 'Two auxiliaries in a row. &lsquo;will&rsquo; needs nothing else.'),
    ('are will be lit', 'The modal comes first, and it never doubles up.'),
    ('will be light', 'Third form: lit.')],
   'Las antorchas ______ al anochecer.', 'Die Fackeln ______ bei Sonnenuntergang.',
   why='&lsquo;will&rsquo; never changes. Plural or singular, the chain is the same four words.'),

mc(3, 6, B % 'bg32.jpg', 'right', 'top', 'Say no',
   'The bridge ______ this year.', "won't be repaired",
   [("doesn't be repaired", 'A passive never uses &lsquo;does&rsquo;.'),
    ("won't being repaired", '&lsquo;being&rsquo; never follows a modal.'),
    ("isn't will be repaired", 'Two auxiliaries, and the modal in the wrong place.')],
   'El puente ______ este a&ntilde;o.', 'Die Br&uuml;cke ______ dieses Jahr.',
   why='The &lsquo;not&rsquo; goes on &lsquo;will&rsquo;, and the rest of the chain does not move.'),

mc(4, 6, B % 'bg35.jpg', 'left', 'top', 'Ask the question',
   '______ the gate be locked from Monday?', 'Will',
   [('Is', 'That would need &lsquo;going to&rsquo; after it.'),
    ('Does', 'A passive question never starts with &lsquo;does&rsquo;.'),
    ('Has', 'That would need &lsquo;been&rsquo;, and a time that is still open.')],
   '&iquest;______ cerrada la puerta desde el lunes?',
   '______ das Tor ab Montag verschlossen?',
   why='To ask, the modal moves to the front. It is still &lsquo;will&rsquo;, unchanged.'),

# The hardest question on the deck, and the one camp 6 built toward: two
# sentences that are both correct English, decided by the situation.
mc(5, 6, B % 'bg37.jpg', 'left', 'top', 'Which future?',
   'Look at those plans on the table. The village ______ rebuilt.',
   'is going to be',
   [('will be', 'A prediction or an on-the-spot decision &mdash; but the plans are already drawn.'),
    ('was going to be', 'A past plan. The plans are on the table now.'),
    ('has been', 'Finished, and the village would already be standing.')],
   'Mira esos planos. El pueblo ______ reconstruido.',
   'Sieh dir die Pl&auml;ne an. Das Dorf ______ wieder aufgebaut.',
   why='Plans on the table are evidence you can point at, which is what &lsquo;going to&rsquo; is for.'),

mc(6, 6, B % 'bg40.jpg', 'left', 'top', 'Which future?',
   '&lsquo;The bridge is broken.&rsquo; &lsquo;Fine &mdash; it ______ tomorrow.&rsquo;',
   'will be repaired',
   [('is going to be repaired', 'That would mean the plan existed before you spoke.'),
    ('is being repaired', 'That says the work is happening as you speak.'),
    ('was repaired', 'Finished and dated, and the bridge is broken now.')],
   '&mdash;El puente est&aacute; roto. &mdash;Vale, ______ ma&ntilde;ana.',
   '&bdquo;Die Br&uuml;cke ist kaputt.&ldquo; &bdquo;Gut &mdash; sie ______ morgen.&ldquo;',
   why='The decision is being taken as the speaker speaks, and that is exactly &lsquo;will&rsquo;.'),

sort(B % 'bg26.jpg', 'right', 'top', 'Which future does it need?',
     'Click a situation, then click the future it takes.',
     ['will be &mdash; decided now, or a guess',
      'is going to be &mdash; already decided, or evidence'],
     [(0, 'Fine, it ___ done tomorrow.'), (0, 'It ___ finished by winter, I think.'),
      (0, 'Don’t worry, you ___ told.'), (0, 'I promise it ___ returned.'),
      (1, 'Look at the plans — it ___ rebuilt.'),
      (1, 'The cracks are huge — it ___ knocked down.'),
      (1, 'The date is set — the gate ___ closed.'),
      (1, 'The seed is bought — the wheat ___ planted.')],
     'A guess or an on-the-spot decision takes &lsquo;will be&rsquo;. '
     'A plan already made, or evidence in front of you, takes &lsquo;is going to be&rsquo;.'),

match(B % 'bg19.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('They will build the wall', 'the wall will be built',
        'Construir&aacute;n el muro', 'Sie werden die Mauer bauen',
        'el muro ser&aacute; construido', 'die Mauer wird gebaut werden'),
       ('Alex will draw the map', 'the map will be drawn',
        'Alex dibujar&aacute; el mapa', 'Alex wird die Karte zeichnen',
        'el mapa ser&aacute; dibujado', 'die Karte wird gezeichnet werden'),
       ('They will light the torches', 'the torches will be lit',
        'Encender&aacute;n las antorchas', 'Sie werden die Fackeln anz&uuml;nden',
        'las antorchas ser&aacute;n encendidas', 'die Fackeln werden angez&uuml;ndet werden'),
       ('Somebody will tell you', 'you will be told',
        'Alguien te lo dir&aacute;', 'Jemand wird es dir sagen',
        'te lo dir&aacute;n', 'dir wird es gesagt werden'),
       ('They will lock the gate', 'the gate will be locked',
        'Cerrar&aacute;n la puerta', 'Sie werden das Tor schlie&szlig;en',
        'la puerta ser&aacute; cerrada', 'das Tor wird geschlossen werden'),
       ('We will finish the bridge', 'the bridge will be finished',
        'Terminaremos el puente', 'Wir werden die Br&uuml;cke fertigstellen',
        'el puente ser&aacute; terminado', 'die Br&uuml;cke wird fertiggestellt werden')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg18.jpg', 'left', 'top', 'Write the missing word',
    'The same word is missing from every chain.',
    [('The wall will ', 'be', ' built.',
      'A modal takes a bare verb; in the passive it is &lsquo;be&rsquo;.', 120,
      'El muro ______ construido.', 'Die Mauer wird gebaut ______.'),
     ('The torches will ', 'be', ' lit.',
      'Plural changes nothing after &lsquo;will&rsquo;.', 120,
      'Las antorchas ______ encendidas.', 'Die Fackeln werden angez&uuml;ndet ______.'),
     ('Will the gate ', 'be', ' locked?',
      'In a question the modal moves, but the bare verb stays.', 120,
      '&iquest;La puerta ______ cerrada?', 'Wird das Tor verschlossen ______?')]),

gap(2, 2, B % 'bg31.jpg', 'left', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The map will be ', 'drawn', '. <span class="dim">(draw)</span>',
      'draw &rarr; drew &rarr; drawn.', 170,
      'El mapa ser&aacute; ______. (dibujar)', 'Die Karte wird ______ werden. (zeichnen)'),
     ('You will be ', 'told', '. <span class="dim">(tell)</span>',
      'tell &rarr; told &rarr; told.', 170,
      'Te lo ______. (decir)', 'Es wird dir ______ werden. (sagen)'),
     ('The bridge will be ', 'finished', '. <span class="dim">(finish)</span>',
      'Regular verb, so the third form is just -ed.', 170,
      'El puente ser&aacute; ______. (terminar)',
      'Die Br&uuml;cke wird ______ werden. (fertigstellen)')]),

order(B % 'bg38.jpg', 'left', 'top', 'the wall | will | be | built .',
      'The thing, then will, then be, then the third form.',
      'El muro ser&aacute; construido.', 'Die Mauer wird gebaut werden.'),

order(B % 'bg41.jpg', 'left', 'top',
      'the map | will | be | drawn | by Alex .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.',
      'El mapa ser&aacute; dibujado por Alex.',
      'Die Karte wird von Alex gezeichnet werden.'),

results(B % 'bg25.jpg', 'left', 'top'),

activate(B % 'bg07.jpg', 'Now make a promise',
         ['will be built', 'will be told', 'will be finished', "won't be closed",
          'by winter', 'tomorrow', 'from Monday', 'by'],
         ['Promise your partner three things, and never say who will do them.',
          'Predict what will be built in your town in ten years.',
          'One of you is worried. Reassure them: what will be done, and when?'],
         ['Write a notice about what will be done next month, naming nobody.',
          'Then change one line to &lsquo;is going to be&rsquo;. What changed about the meaning?']),
]

STATION = dict(
    file='blockcamp-passive-future-simple.html',
    chassis='blockcamp-future-simple.html',   # camp 6: brings its orange with it
    title='Future Simple Passive',
    sub='Station 14: it will be done, and nobody is named',
    # Camp 6 part 1 is A2. The chain here is the easiest on the descent - will
    # never agrees with anything - but the will / going to choice is B1 work,
    # and this deck asks a learner to make it with the doer already gone.
    level='B1',
    doctitle='Block Camp II — Passive 14: Future Simple Passive (B1) | Forbes English',
    hero=B % 'bg13.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to the chain: will + be + the third form. It is the same four words every time.',
        resMid='Check &lsquo;be&rsquo; against being and been. A modal only ever takes the bare verb.',
        resStrong='Strong. Look again at the two questions asking which future the situation needs.',
        resPerfect='Full marks. Now promise somebody something, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zur Kette: will + be + dritte Form. Immer dieselben vier W&ouml;rter.',
        resMid='Vergleiche &lsquo;be&rsquo; mit being und been. Nach einem Modalverb steht nur die Grundform.',
        resStrong='Stark. Sieh dir die zwei Fragen an, wo die Situation die Zukunft w&auml;hlt.',
        resPerfect='Volle Punktzahl. Versprich jetzt jemandem etwas - ohne jemanden zu nennen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve a la cadena: will + be + tercera forma. Siempre las mismas cuatro palabras.',
        resMid='Compara &lsquo;be&rsquo; con being y been. Un modal solo lleva el infinitivo.',
        resStrong='Muy bien. Revisa las dos preguntas donde la situaci&oacute;n elige el futuro.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora prom&eacute;tele algo a alguien, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
