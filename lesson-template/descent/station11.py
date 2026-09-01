# -*- coding: utf-8 -*-
"""Station 11 — Past Simple Passive.  Mirrors camp 3, and wears its amber.

THE SAME SHAPE AS STATION 9, ONE TENSE BACK. `is / are` becomes `was / were`
and nothing else moves. A learner who has station 9 already has this deck's
form; what they do not have is the SECOND-versus-THIRD problem, and that is
what this one is really about.

    they built the wall        <- second form, active
    the wall was built         <- third form, passive

In `build`, `send`, `find` and `put` those two forms are the same word, so the
passive looks identical to the active past and a learner can go a whole lesson
without noticing which one they are using. In `break`, `take`, `write` and
`eat` they are different, and the mistake becomes audible: "the wall was
broke". That is the sentence this deck exists to stop.

So the third-form slide here is not a repeat of station 9's. Station 9 asked
"what is the third form?". This one asks "which of these two is it?", because
here there is a second form sitting right next to it, wearing camp 3's brown.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'past-simple-time-signals/%s'   # camp 3's own plates

SLIDES = [

sec('teach', B % 'bg17.jpg', 'left', 'top',
    head('What it means', 'It was done, and nobody is named') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> <em class="t-past">built</em> <em class="obj">the wall</em>.',
       ['<em class="agent">Alex</em> <em class="t-past">locked</em> <em class="obj">the gate</em>',
        '<em class="agent">a creeper</em> <em class="t-past">broke</em> <em class="obj">the bridge</em>'],
       gloss('Los aldeanos construyeron el muro.', 'Dorfbewohner bauten die Mauer.')),
      ('Passive', '<em class="obj">The wall</em> <em class="aux">was</em> <em class="pp">built</em>.',
       ['<em class="obj">the gate</em> <em class="aux">was</em> <em class="pp">locked</em>',
        '<em class="obj">the bridge</em> <em class="aux">was</em> <em class="pp">broken</em>'],
       gloss('El muro fue construido.', 'Die Mauer wurde gebaut.')),
    ])),

sec('teach', B % 'bg38.jpg', 'right', 'top',
    head('The form', 'Station 9, one tense back') + '\n' +
    para([
      ('Station 9 &mdash; now',
       [('', '<em class="obj">The wall</em> <em class="aux">is</em> <em class="pp">built</em>.')],
       gloss('Ahora', 'Jetzt')),
      ('Station 11 &mdash; finished, and dated',
       [('', '<em class="obj">The wall</em> <em class="aux">was</em> <em class="pp">built</em> in 1990.')],
       gloss('Terminado, con fecha', 'Abgeschlossen, mit Datum')),
      ('Only the auxiliary moved',
       [('', '&lsquo;is&rsquo; &rarr; <em class="aux">&lsquo;was&rsquo;</em> &nbsp;&middot;&nbsp; &lsquo;are&rsquo; &rarr; <em class="aux">&lsquo;were&rsquo;</em>')],
       gloss('Solo cambia el auxiliar', 'Nur das Hilfsverb &auml;ndert sich')),
    ], '<em class="obj">THING</em> + <em class="aux">was</em> / <em class="aux">were</em> '
       '+ <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg10.jpg', 'left', 'top',
    head('The form', 'Only &lsquo;was&rsquo; and &lsquo;were&rsquo; change') + '\n' +
    para([
      ('One thing', [('the wall', '<em class="aux">was</em> <em class="pp">built</em>'),
                     ('no', '<em class="aux">wasn&rsquo;t</em> <em class="pp">built</em>')],
       gloss('fue construido', 'wurde gebaut')),
      ('More than one', [('the walls', '<em class="aux">were</em> <em class="pp">built</em>'),
                         ('no', '<em class="aux">weren&rsquo;t</em> <em class="pp">built</em>')],
       gloss('fueron construidos', 'wurden gebaut')),
      ('Asking', [('one', '<em class="aux">Was</em> it <em class="pp">built</em>?'),
                  ('more', '<em class="aux">Were</em> they <em class="pp">built</em>?')],
       gloss('&iquest;Fue construido?', 'Wurde sie gebaut?')),
    ], 'no <em class="aux">&lsquo;did&rsquo;</em> anywhere &mdash; the passive already has its auxiliary')),

# THE SLIDE THIS DECK OWNS. Station 9 asked what the third form IS. Here the
# second form is standing next to it in camp 3's brown, and the question is
# which of the two the sentence needs.
sec('teach', B % 'bg08.jpg', 'right', 'top',
    head('The trap', 'Second form, or third?') + '\n' +
    para([
      ('Same word &mdash; no way to slip',
       [('build', '<em class="t-past">built</em> &rarr; <em class="pp">built</em>'),
        ('find', '<em class="t-past">found</em> &rarr; <em class="pp">found</em>')],
       gloss('La misma palabra', 'Dasselbe Wort')),
      ('Different words &mdash; here is the mistake',
       [('break', '<em class="t-past">broke</em> &rarr; <em class="pp">broken</em>'),
        ('take', '<em class="t-past">took</em> &rarr; <em class="pp">taken</em>'),
        ('write', '<em class="t-past">wrote</em> &rarr; <em class="pp">written</em>')],
       gloss('Palabras distintas: aqu&iacute; est&aacute; el fallo',
             'Verschiedene W&ouml;rter: hier passiert der Fehler')),
      ('So this is wrong',
       [('', '<s>the wall was <em class="t-past">broke</em></s> &rarr; '
             'the wall was <em class="pp">broken</em>')],
       gloss('Esto est&aacute; mal', 'Das ist falsch')),
    ], 'the passive ALWAYS takes the <em class="pp">THIRD</em> form, never the '
       '<em class="t-past">second</em>')),

sec('teach', B % 'bg37.jpg', 'left', 'top',
    head('Why choose it', 'History, and nobody to blame') + '\n' +
    para([
      ('Nobody knows who',
       [('', '<em class="obj">The village</em> <em class="aux">was</em> <em class="pp">built</em> long ago.')],
       gloss('Nadie sabe qui&eacute;n', 'Niemand wei&szlig;, wer')),
      ('Everyone knows who, so why say it',
       [('', '<em class="obj">The bread</em> <em class="aux">was</em> <em class="pp">baked</em> that morning.')],
       gloss('Todos lo saben ya', 'Alle wissen es ohnehin')),
      ('You would rather not say who',
       [('', '<em class="obj">The window</em> <em class="aux">was</em> <em class="pp">broken</em>. '
             '<span class="dim">(not by me!)</span>')],
       gloss('Prefieres no decir qui&eacute;n', 'Man will nicht sagen, wer')),
    ], 'this is the voice of history, and of an excuse')),

sec('teach', B % 'bg25.jpg', 'right', 'top',
    head('Time signals', 'Words that close the door') + '\n' +
    cards([
      ('A named time', 'The sentence says exactly when.',
       ['yesterday', 'last night', 'in 1990', 'that morning'],
       gloss('ayer &middot; anoche &middot; en 1990 &middot; aquella ma&ntilde;ana',
             'gestern &middot; gestern Abend &middot; im Jahr 1990 &middot; an jenem Morgen')),
      ('Counting back', 'How far back from today.',
       ['two days ago', 'a year ago', 'long ago'],
       gloss('hace dos d&iacute;as &middot; hace un a&ntilde;o &middot; hace mucho',
             'vor zwei Tagen &middot; vor einem Jahr &middot; vor langer Zeit')),
    ]),
    'data-w="wide" style="--wcols:2"'),

sec('teach', B % 'bg28.jpg', 'left', 'top',
    head('The doer', '&lsquo;by&rsquo; is optional here too') + '\n' +
    para([
      ('Keep it when the doer is the news',
       [('yes', '<em class="obj">The map</em> <em class="aux">was</em> <em class="pp">drawn</em> '
                '<em class="agent">by a villager</em>.')],
       gloss('Mant&eacute;nlo si el autor es noticia',
             'Behalte es, wenn der T&auml;ter neu ist')),
      ('Drop it when it is not',
       [('no', '<em class="obj">The gate</em> <em class="aux">was</em> <em class="pp">locked</em> at sunset.')],
       gloss('Qu&iacute;talo si no lo es', 'Sonst f&auml;llt es weg')),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

mc(1, 6, B % 'bg05.jpg', 'right', 'top', 'Choose the passive',
   'The wall ______ in 1990.', 'was built',
   [('built', 'That is active &mdash; it needs somebody in front doing the building.'),
    ('was build', '&lsquo;Build&rsquo; is the first form. The third is &lsquo;built&rsquo;.'),
    ('were built', 'One wall, so the auxiliary is &lsquo;was&rsquo;.')],
   'El muro ______ en 1990.', 'Die Mauer ______ 1990.',
   why='One wall, so &lsquo;was&rsquo;, and the third form of &lsquo;build&rsquo; is &lsquo;built&rsquo;.'),

# The mistake this deck exists to stop, put straight to the learner.
mc(2, 6, B % 'bg12.jpg', 'left', 'top', 'Second form, or third?',
   'The window ______ during the storm.', 'was broken',
   [('was broke', '&lsquo;Broke&rsquo; is the second form. The passive takes the third: broken.'),
    ('were broken', 'One window, so &lsquo;was&rsquo;.'),
    ('broke', 'Active &mdash; that says the window broke something.')],
   'La ventana ______ durante la tormenta.', 'Das Fenster ______ w&auml;hrend des Sturms.',
   why='break &rarr; broke &rarr; broken. The passive never takes the second form.'),

mc(3, 6, B % 'bg21.jpg', 'right', 'top', 'Choose the passive',
   'The torches ______ every night.', 'were lit',
   [('was lit', '&lsquo;Torches&rsquo; is plural, so &lsquo;were&rsquo;.'),
    ('were light', 'Third form: lit.'),
    ('were lighting', 'Active &mdash; that says the torches lit something.')],
   'Las antorchas ______ cada noche.', 'Die Fackeln ______ jede Nacht.',
   why='More than one torch, so &lsquo;were&rsquo; &mdash; then the third form, &lsquo;lit&rsquo;.'),

mc(4, 6, B % 'bg31.jpg', 'left', 'top', 'Say no',
   'The bridge ______ that year.', "wasn't repaired",
   [("didn't repaired", 'A passive never uses &lsquo;did&rsquo;. It already has an auxiliary.'),
    ("weren't repaired", 'One bridge, so &lsquo;was&rsquo;.'),
    ("wasn't repair", 'Third form: repaired.')],
   'El puente ______ ese a&ntilde;o.', 'Die Br&uuml;cke ______ in jenem Jahr.',
   why='The &lsquo;not&rsquo; goes on the auxiliary: <em class="aux">wasn&rsquo;t</em> + the third form.'),

mc(5, 6, B % 'bg33.jpg', 'right', 'top', 'Ask the question',
   '______ the diamonds found last week?', 'Were',
   [('Was', '&lsquo;Diamonds&rsquo; is plural.'),
    ('Did', 'A passive question never starts with &lsquo;did&rsquo;.'),
    ('Have', 'That would need &lsquo;been&rsquo;, and a time that is still open.')],
   '&iquest;______ encontrados los diamantes la semana pasada?',
   '______ die Diamanten letzte Woche gefunden?',
   why='To ask, the auxiliary moves to the front. Diamonds is plural, so &lsquo;Were&rsquo;.'),

mc(6, 6, B % 'bg19.jpg', 'left', 'top', 'Active, or passive?',
   'Which means the same as &lsquo;A creeper broke the bridge&rsquo;?',
   'The bridge was broken by a creeper.',
   [('The bridge broke a creeper.', 'That swaps who did what.'),
    ('The bridge was broke by a creeper.', 'Second form. The passive takes &lsquo;broken&rsquo;.'),
    ('A creeper was broken by the bridge.', 'Both halves the wrong way round.')],
   '&iquest;Cu&aacute;l significa lo mismo?', 'Welcher Satz bedeutet dasselbe?',
   why='The bridge was the object, so it goes to the front; the creeper follows &lsquo;by&rsquo;.'),

sort(B % 'bg27.jpg', 'right', 'top', 'Second form, or third?',
     'Click a word, then click which form it is.',
     ['second &mdash; active', 'third &mdash; passive'],
     [(0, 'broke'), (0, 'took'), (0, 'wrote'), (0, 'ate'),
      (1, 'broken'), (1, 'taken'), (1, 'written'), (1, 'eaten')],
     'The passive always takes the third. If a word can follow &lsquo;was&rsquo; '
     'or &lsquo;were&rsquo;, it is the third form.'),

match(B % 'bg29.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('Villagers built the wall', 'the wall was built',
        'Los aldeanos construyeron el muro', 'Dorfbewohner bauten die Mauer',
        'el muro fue construido', 'die Mauer wurde gebaut'),
       ('Alex locked the gate', 'the gate was locked',
        'Alex cerr&oacute; la puerta', 'Alex schloss das Tor',
        'la puerta fue cerrada', 'das Tor wurde geschlossen'),
       ('A creeper broke the bridge', 'the bridge was broken',
        'Un creeper rompi&oacute; el puente', 'Ein Creeper zerst&ouml;rte die Br&uuml;cke',
        'el puente fue roto', 'die Br&uuml;cke wurde zerst&ouml;rt'),
       ('They lit the torches', 'the torches were lit',
        'Encendieron las antorchas', 'Sie z&uuml;ndeten die Fackeln an',
        'las antorchas fueron encendidas', 'die Fackeln wurden angez&uuml;ndet'),
       ('Steve wrote the sign', 'the sign was written',
        'Steve escribi&oacute; el cartel', 'Steve schrieb das Schild',
        'el cartel fue escrito', 'das Schild wurde geschrieben'),
       ('Miners found the diamonds', 'the diamonds were found',
        'Los mineros encontraron los diamantes', 'Bergleute fanden die Diamanten',
        'los diamantes fueron encontrados', 'die Diamanten wurden gefunden')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg23.jpg', 'right', 'top', 'Write the third form',
    'Type the verb in brackets in its third form, not its second.',
    [('The bridge was ', 'broken', '. <span class="dim">(break)</span>',
      'Not &lsquo;broke&rsquo; &mdash; that is the second form.', 170,
      'El puente fue ______. (romper)', 'Die Br&uuml;cke wurde ______. (zerst&ouml;ren)'),
     ('The sign was ', 'written', '. <span class="dim">(write)</span>',
      'write &rarr; wrote &rarr; written. Not &lsquo;wrote&rsquo;.', 170,
      'El cartel fue ______. (escribir)', 'Das Schild wurde ______. (schreiben)'),
     ('The bread was ', 'eaten', '. <span class="dim">(eat)</span>',
      'eat &rarr; ate &rarr; eaten. Not &lsquo;ate&rsquo;.', 170,
      'El pan fue ______. (comer)', 'Das Brot wurde ______. (essen)')]),

gap(2, 2, B % 'bg36.jpg', 'left', 'top', '&lsquo;was&rsquo;, or &lsquo;were&rsquo;?',
    'Look at the thing in front, not at the doer.',
    [('The torches ', 'were', ' lit by Alex.', 'Torches is plural.', 130,
      'Las antorchas ______ encendidas por Alex.',
      'Die Fackeln ______ von Alex angez&uuml;ndet.'),
     ('The gate ', 'was', ' locked at sunset.', 'One gate.', 130,
      'La puerta ______ cerrada al anochecer.',
      'Das Tor ______ bei Sonnenuntergang verschlossen.'),
     ('The diamonds ', 'were', ' found in 1990.', 'Diamonds is plural.', 130,
      'Los diamantes ______ encontrados en 1990.',
      'Die Diamanten ______ 1990 gefunden.')]),

order(B % 'bg30.jpg', 'right', 'top', 'the wall | was | built | in 1990 .',
      'The thing, then was, then the third form, then the time.',
      'El muro fue construido en 1990.', 'Die Mauer wurde 1990 gebaut.'),

order(B % 'bg34.jpg', 'left', 'top',
      'the bridge | was | broken | by a creeper .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.',
      'El puente fue roto por un creeper.',
      'Die Br&uuml;cke wurde von einem Creeper zerst&ouml;rt.'),

results(B % 'bg41.jpg', 'left', 'top'),

activate(B % 'bg19.jpg', 'Now say what was done',
         ['was built', 'were found', 'was broken', 'were made',
          'in 1990', 'long ago', 'by', 'never'],
         ['Describe an old building where you live. When was it built? Do not say who built it.',
          'Tell your partner three things that were made in your country, and never name a maker.',
          'Something was broken. Say what was broken and when &mdash; and avoid saying who did it.'],
         ['Write six lines of village history, naming nobody.',
          'Then rewrite one line as active. Which one had to name somebody?']),
]

STATION = dict(
    file='blockcamp-passive-past-simple.html',
    chassis='blockcamp-past-simple.html',   # camp 3: brings its amber with it
    title='Past Simple Passive',
    sub='Station 11: it was done, and nobody is named',
    level='A2',
    doctitle='Block Camp II — Passive 11: Past Simple Passive (A2) | Forbes English',
    hero=B % 'bg17.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to the second and third forms. The passive never takes the second.',
        resMid='Check &lsquo;was&rsquo; against &lsquo;were&rsquo;. Count the thing in front, not the doer.',
        resStrong='Strong. Look again at the verbs whose second and third forms differ.',
        resPerfect='Full marks. Now tell some history, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zu zweiter und dritter Form. Das Passiv nimmt nie die zweite.',
        resMid='Vergleiche &lsquo;was&rsquo; und &lsquo;were&rsquo;. Z&auml;hle das Ding davor, nicht den T&auml;ter.',
        resStrong='Stark. Sieh dir die Verben an, deren zweite und dritte Form verschieden sind.',
        resPerfect='Volle Punktzahl. Erz&auml;hl jetzt Geschichte - ohne jemanden zu nennen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve a la segunda y la tercera forma. La pasiva nunca lleva la segunda.',
        resMid='Compara &lsquo;was&rsquo; y &lsquo;were&rsquo;. Cuenta la cosa de delante, no quien la hace.',
        resStrong='Muy bien. Revisa los verbos cuya segunda y tercera forma son distintas.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora cuenta algo de historia, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
