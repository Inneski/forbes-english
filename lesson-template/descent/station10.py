# -*- coding: utf-8 -*-
"""Station 10 — Present Continuous Passive.  Mirrors camp 2, and wears its pink.

ONE WORD LONGER THAN STATION 9, AND THAT WORD IS THE WHOLE LESSON. Station 9
taught the swap and `is / are` + participle. This deck changes exactly one
thing: `being` slides in between them.

    the stone is mined          <- station 9, a process
    the stone is being mined    <- station 10, happening as you watch

So the deck does NOT re-teach the swap. It teaches where `being` goes, why it
is easy to drop, and what the sentence means without it - because "the stone
is mined" is not wrong, it is a different sentence, and a learner who drops
`being` has not made a spelling mistake, they have changed the meaning.

THE TRAP THIS TENSE OWNS is the one every learner meets: `being` and `been`.
They are one letter apart, they both follow an auxiliary, and they belong to
different tenses. Camp 8 is the only other place a learner meets `being` at
all, so this is where it gets its slide.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'present-continuous-time-signals/%s'   # camp 2's own plates

SLIDES = [

sec('teach', B % 'bg01.jpg', 'left', 'top',
    head('What it means', 'Happening now, and nobody is named') + '\n' +
    cards([
      ('Active', '<em class="agent">Villagers</em> are mining <em class="obj">the stone</em>.',
       ['<em class="agent">Alex</em> is building <em class="obj">the wall</em>',
        '<em class="agent">they</em> are lighting <em class="obj">the torches</em>'],
       gloss('Los aldeanos est&aacute;n extrayendo la piedra.',
             'Dorfbewohner bauen gerade den Stein ab.')),
      ('Passive', '<em class="obj">The stone</em> <em class="aux">is being</em> <em class="pp">mined</em>.',
       ['<em class="obj">the wall</em> <em class="aux">is being</em> <em class="pp">built</em>',
        '<em class="obj">the torches</em> <em class="aux">are being</em> <em class="pp">lit</em>'],
       gloss('La piedra est&aacute; siendo extra&iacute;da.',
             'Der Stein wird gerade abgebaut.')),
    ])),

# THE ONE NEW WORD, AND IT IS SHOWN AS A GAP BEING FILLED. Station 9's
# sentence is on the top row with a hole in it; this deck's word drops in.
sec('teach', B % 'bg22.jpg', 'right', 'top',
    head('The form', 'One word slides in: <em class="aux">&lsquo;being&rsquo;</em>') + '\n' +
    para([
      ('Station 9 &mdash; a process',
       [('', '<em class="obj">The stone</em> <em class="aux">is</em> <em class="pp">mined</em>.')],
       gloss('La piedra se extrae (en general)', 'Der Stein wird abgebaut (allgemein)')),
      ('Station 10 &mdash; right now, as you watch',
       [('', '<em class="obj">The stone</em> <em class="aux">is being</em> <em class="pp">mined</em>.')],
       gloss('La piedra est&aacute; siendo extra&iacute;da ahora',
             'Der Stein wird gerade abgebaut')),
      ('Nothing else moved',
       [('', 'same thing in front, same third form at the end')],
       gloss('Lo dem&aacute;s no cambia', 'Sonst &auml;ndert sich nichts')),
    ], '<em class="obj">THING</em> + <em class="aux">am</em> / <em class="aux">is</em> / '
       '<em class="aux">are</em> + <em class="aux">being</em> + <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg34.jpg', 'left', 'top',
    head('The form', 'Only the first word changes') + '\n' +
    para([
      ('One thing', [('the wall', '<em class="aux">is being</em> <em class="pp">built</em>'),
                     ('no', '<em class="aux">isn&rsquo;t being</em> <em class="pp">built</em>')],
       gloss('est&aacute; siendo construido', 'wird gerade gebaut')),
      ('More than one', [('the walls', '<em class="aux">are being</em> <em class="pp">built</em>'),
                         ('no', '<em class="aux">aren&rsquo;t being</em> <em class="pp">built</em>')],
       gloss('est&aacute;n siendo construidos', 'werden gerade gebaut')),
      ('Asking', [('one', '<em class="aux">Is</em> it <em class="aux">being</em> <em class="pp">built</em>?'),
                  ('more', '<em class="aux">Are</em> they <em class="aux">being</em> <em class="pp">built</em>?')],
       gloss('&iquest;Se est&aacute; construyendo?', 'Wird es gerade gebaut?')),
    ], 'only <em class="aux">&lsquo;is&rsquo;</em> / <em class="aux">&lsquo;are&rsquo;</em> changes &mdash; '
       '<em class="aux">&lsquo;being&rsquo;</em> and the <em class="pp">participle</em> never do')),

# THE TRAP THIS DECK OWNS. One letter, two tenses, and both sit in the same
# slot behind an auxiliary. Nowhere else in the line are they side by side.
sec('teach', B % 'bg28.jpg', 'right', 'top',
    head('The trap', '&lsquo;being&rsquo; or &lsquo;been&rsquo;?') + '\n' +
    para([
      ('<em class="aux">&lsquo;being&rsquo;</em> &mdash; happening now',
       [('', '<em class="obj">The wall</em> <em class="aux">is being</em> <em class="pp">built</em>. '
             '<span class="dim">(they are working on it)</span>')],
       gloss('se est&aacute; construyendo ahora', 'wird gerade gebaut')),
      ('<em class="aux">&lsquo;been&rsquo;</em> &mdash; already finished',
       [('', '<em class="obj">The wall</em> <em class="aux">has been</em> <em class="pp">built</em>. '
             '<span class="dim">(it is standing)</span>')],
       gloss('ya se ha construido', 'ist schon gebaut worden')),
      ('The giveaway is the word in front',
       [('', '<em class="aux">&lsquo;is&rsquo;</em> / <em class="aux">&lsquo;are&rsquo;</em> &rarr; being &nbsp;&middot;&nbsp; '
             '<em class="aux">&lsquo;has&rsquo;</em> / <em class="aux">&lsquo;have&rsquo;</em> &rarr; been')],
       gloss('M&iacute;rate la palabra de delante', 'Achte auf das Wort davor')),
    ], 'one letter, two tenses &mdash; check what comes BEFORE it')),

sec('teach', B % 'bg05.jpg', 'left', 'top',
    head('Why choose it', 'The work matters, the workers do not') + '\n' +
    para([
      ('A job in progress',
       [('', '<em class="obj">The bridge</em> <em class="aux">is being</em> <em class="pp">repaired</em>.')],
       gloss('Un trabajo en marcha', 'Eine Arbeit im Gange')),
      ('A change you can see happening',
       [('', '<em class="obj">The village</em> <em class="aux">is being</em> <em class="pp">rebuilt</em>.')],
       gloss('Un cambio que se ve', 'Eine sichtbare Ver&auml;nderung')),
      ('Something being done to you',
       [('', '<em class="obj">We</em> <em class="aux">are being</em> <em class="pp">watched</em>.')],
       gloss('Algo que te hacen a ti', 'Etwas, das mit dir geschieht')),
    ], 'this is the voice of a building site and a warning')),

sec('teach', B % 'bg16.jpg', 'right', 'top',
    head('Time signals', 'The words that put it in this second') + '\n' +
    cards([
      ('Right now', 'The work is happening as you speak.',
       ['now', 'right now', 'at the moment', 'currently'],
       gloss('ahora &middot; ahora mismo &middot; en este momento &middot; actualmente',
             'jetzt &middot; gerade jetzt &middot; im Moment &middot; zurzeit')),
      ('Look and listen', 'Tell someone to notice it happening.',
       ['Look!', 'Listen!', 'still'],
       gloss('&iexcl;Mira! &middot; &iexcl;Escucha! &middot; todav&iacute;a',
             'Schau! &middot; H&ouml;r mal! &middot; noch immer')),
    ]),
    'data-w="wide" style="--wcols:2"'),

sec('teach', B % 'bg09.jpg', 'left', 'top',
    head('The doer', 'Keep &lsquo;by&rsquo; only when it is news') + '\n' +
    para([
      ('Worth saying',
       [('yes', '<em class="obj">The gate</em> <em class="aux">is being</em> <em class="pp">guarded</em> '
                '<em class="agent">by a creeper</em>.')],
       gloss('Vale la pena decirlo', 'Der T&auml;ter ist eine Neuigkeit')),
      ('Not worth saying',
       [('no', '<em class="obj">The bread</em> <em class="aux">is being</em> <em class="pp">baked</em>. '
              '<span class="dim">(by the baker &mdash; obviously)</span>')],
       gloss('No hace falta decirlo', 'Muss man nicht sagen')),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

mc(1, 6, B % 'bg04.jpg', 'right', 'top', 'Choose the passive',
   'The wall ______ right now.', 'is being built',
   [('is building', 'Active &mdash; that says the wall is doing the building.'),
    ('is been built', '&lsquo;been&rsquo; belongs to has / have. After &lsquo;is&rsquo; it is &lsquo;being&rsquo;.'),
    ('are being built', 'One wall, so the auxiliary is &lsquo;is&rsquo;.')],
   'El muro ______ ahora mismo.', 'Die Mauer ______ gerade.',
   why='One wall, so &lsquo;is&rsquo; &mdash; then &lsquo;being&rsquo;, then the third form.'),

mc(2, 6, B % 'bg06.jpg', 'left', 'top', 'Choose the passive',
   'The torches ______ as we speak.', 'are being lit',
   [('is being lit', '&lsquo;Torches&rsquo; is plural, so &lsquo;are&rsquo;.'),
    ('are being light', 'Third form: lit.'),
    ('are lighting', 'Active &mdash; that says the torches light something.')],
   'Las antorchas ______ mientras hablamos.', 'Die Fackeln ______ gerade.',
   why='More than one torch, so &lsquo;are being&rsquo; &mdash; then the third form, &lsquo;lit&rsquo;.'),

# The being/been question, asked rather than told. Its distractor is the exact
# confusion the teach slide names, so a wrong click lands on the explanation.
mc(3, 6, B % 'bg20.jpg', 'right', 'bottom', '&lsquo;being&rsquo;, or &lsquo;been&rsquo;?',
   'The bridge is ______ repaired at the moment.', 'being',
   [('been', '&lsquo;been&rsquo; needs has or have in front, not &lsquo;is&rsquo;.'),
    ('be', 'That would need &lsquo;will&rsquo; in front of it.'),
    ('was', 'Two auxiliaries in a row, and the sentence says &lsquo;at the moment&rsquo;.')],
   'El puente est&aacute; ______ reparado en este momento.',
   'Die Br&uuml;cke wird ______ repariert.',
   why='&lsquo;is&rsquo; in front means &lsquo;being&rsquo;. &lsquo;been&rsquo; would need &lsquo;has&rsquo;.'),

mc(4, 6, B % 'bg29.jpg', 'left', 'bottom', 'Say no',
   'The village ______ rebuilt this week.', "isn't being",
   [("isn't been", '&lsquo;been&rsquo; goes with has, not with is.'),
    ("doesn't being", 'A passive never uses &lsquo;does&rsquo;.'),
    ("aren't being", 'One village, so &lsquo;is&rsquo;.')],
   'El pueblo ______ reconstruido esta semana.',
   'Das Dorf ______ diese Woche wieder aufgebaut.',
   why='The &lsquo;not&rsquo; goes on the first auxiliary: <em class="aux">isn&rsquo;t</em> + being + the third form.'),

mc(5, 6, B % 'bg17.jpg', 'right', 'top', 'Ask the question',
   '______ the diamonds being counted?', 'Are',
   [('Is', '&lsquo;Diamonds&rsquo; is plural.'),
    ('Have', 'That would need &lsquo;been&rsquo;, not &lsquo;being&rsquo;.'),
    ('Do', 'A passive question never starts with &lsquo;do&rsquo;.')],
   '&iquest;______ contando los diamantes?', '______ die Diamanten gerade gez&auml;hlt?',
   why='To ask, the first auxiliary moves to the front. Diamonds is plural, so &lsquo;Are&rsquo;.'),

mc(6, 6, B % 'bg30.jpg', 'left', 'top', 'Now, or in general?',
   'Which one means the work is happening as you watch?',
   'The stone is being mined.',
   [('The stone is mined.', 'True in general &mdash; that is station 9, a process.'),
    ('The stone has been mined.', 'Finished. The result is there and the work is over.'),
    ('The stone mines.', 'That says the stone does the mining.')],
   '&iquest;Cu&aacute;l pasa ahora mismo?', 'Welcher Satz passiert gerade jetzt?',
   why='&lsquo;being&rsquo; is what puts the work in this second. Without it the sentence is a general rule.'),

sort(B % 'bg26.jpg', 'right', 'top', '&lsquo;being&rsquo;, or &lsquo;been&rsquo;?',
     'Click a beginning, then click the word that follows it.',
     ['being', 'been'],
     [(0, 'the wall is ___ built'), (0, 'the torches are ___ lit'),
      (0, 'we are ___ watched'), (0, 'is it ___ repaired?'),
      (1, 'the wall has ___ built'), (1, 'the torches have ___ lit'),
      (1, 'it has ___ opened'), (1, 'they have ___ found')],
     '&lsquo;is&rsquo; and &lsquo;are&rsquo; take &lsquo;being&rsquo;. '
     '&lsquo;has&rsquo; and &lsquo;have&rsquo; take &lsquo;been&rsquo;. '
     'The word in FRONT decides it, every time.'),

match(B % 'bg13.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('They are mining the stone', 'the stone is being mined',
        'Est&aacute;n extrayendo la piedra', 'Sie bauen gerade den Stein ab',
        'la piedra est&aacute; siendo extra&iacute;da', 'der Stein wird gerade abgebaut'),
       ('Alex is building the wall', 'the wall is being built',
        'Alex est&aacute; construyendo el muro', 'Alex baut gerade die Mauer',
        'el muro est&aacute; siendo construido', 'die Mauer wird gerade gebaut'),
       ('They are lighting the torches', 'the torches are being lit',
        'Est&aacute;n encendiendo las antorchas', 'Sie z&uuml;nden gerade die Fackeln an',
        'las antorchas est&aacute;n siendo encendidas', 'die Fackeln werden gerade angez&uuml;ndet'),
       ('A creeper is watching us', 'we are being watched',
        'Un creeper nos observa', 'Ein Creeper beobachtet uns',
        'nos est&aacute;n observando', 'wir werden beobachtet'),
       ('Somebody is repairing the bridge', 'the bridge is being repaired',
        'Alguien est&aacute; reparando el puente', 'Jemand repariert gerade die Br&uuml;cke',
        'el puente est&aacute; siendo reparado', 'die Br&uuml;cke wird gerade repariert'),
       ('They are rebuilding the village', 'the village is being rebuilt',
        'Est&aacute;n reconstruyendo el pueblo', 'Sie bauen gerade das Dorf wieder auf',
        'el pueblo est&aacute; siendo reconstruido', 'das Dorf wird gerade wieder aufgebaut')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg36.jpg', 'right', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The wall is being ', 'built', '. <span class="dim">(build)</span>',
      'build &rarr; built &rarr; built. The second and third are the same word.', 170,
      'El muro est&aacute; siendo ______. (construir)',
      'Die Mauer wird gerade ______. (bauen)'),
     ('The torches are being ', 'lit', '. <span class="dim">(light)</span>',
      'light &rarr; lit &rarr; lit. Not &lsquo;lighted&rsquo; here.', 170,
      'Las antorchas est&aacute;n siendo ______. (encender)',
      'Die Fackeln werden gerade ______. (anz&uuml;nden)'),
     ('The bridge is being ', 'repaired', '. <span class="dim">(repair)</span>',
      'Regular verb, so the third form is just -ed.', 170,
      'El puente est&aacute; siendo ______. (reparar)',
      'Die Br&uuml;cke wird gerade ______. (reparieren)')]),

gap(2, 2, B % 'bg31.jpg', 'left', 'top', '&lsquo;being&rsquo;, or &lsquo;been&rsquo;?',
    'Look at the auxiliary in front of the gap.',
    [('The village is ', 'being', ' rebuilt.', '&lsquo;is&rsquo; takes &lsquo;being&rsquo;.', 140,
      'El pueblo est&aacute; ______ reconstruido.',
      'Das Dorf wird gerade ______ aufgebaut.'),
     ('The gate has ', 'been', ' locked.', '&lsquo;has&rsquo; takes &lsquo;been&rsquo;.', 140,
      'La puerta ha ______ cerrada.', 'Das Tor ist ______ verschlossen worden.'),
     ('We are ', 'being', ' watched.', '&lsquo;are&rsquo; takes &lsquo;being&rsquo;.', 140,
      'Nos est&aacute;n ______ observando.', 'Wir werden gerade ______ beobachtet.')]),

order(B % 'bg21.jpg', 'right', 'top', 'the wall | is | being | built .',
      'The thing, then is, then being, then the third form.',
      'El muro est&aacute; siendo construido.', 'Die Mauer wird gerade gebaut.'),

order(B % 'bg40.jpg', 'left', 'top',
      'the bridge | is | being | repaired | by the villagers .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.',
      'El puente est&aacute; siendo reparado por los aldeanos.',
      'Die Br&uuml;cke wird gerade von den Dorfbewohnern repariert.'),

results(B % 'bg41.jpg', 'left', 'top'),

activate(B % 'bg35.jpg', 'Now say what is happening',
         ['is being built', 'are being made', 'is being repaired',
          'are being watched', 'right now', 'at the moment', 'still', 'by'],
         ['Describe a building site you have seen. What is being done there?',
          'Look out of the window. Say three things that are being done outside.',
          'One of you is being watched. Say what is being done, and never say who does it.'],
         ['Write six lines about a place that is changing, naming nobody.',
          'Then rewrite one line with &lsquo;by&rsquo;. Was it worth adding?']),
]

STATION = dict(
    file='blockcamp-passive-present-continuous.html',
    chassis='blockcamp-present-continuous.html',   # camp 2: brings its pink with it
    title='Present Continuous Passive',
    sub='Station 10: it is being done, and nobody is named',
    # Camp 2 part 1 is A1; its passive is one step harder, matching the way
    # station 9 sits one step above camp 1.
    level='A2',
    doctitle='Block Camp II — Passive 10: Present Continuous Passive (A2) | Forbes English',
    hero=B % 'bg16.jpg',
    slides=SLIDES,
    messages={
      'en': dict(
        resLow='Go back to &lsquo;being&rsquo;. It slides in between the auxiliary and the third form.',
        resMid='Check &lsquo;being&rsquo; against &lsquo;been&rsquo;. The word in FRONT decides which one.',
        resStrong='Strong. Look again at the ones where you had to choose is or are.',
        resPerfect='Full marks. Now say what is being done around you, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zu &lsquo;being&rsquo;. Es schiebt sich zwischen Hilfsverb und dritte Form.',
        resMid='Vergleiche &lsquo;being&rsquo; mit &lsquo;been&rsquo;. Das Wort DAVOR entscheidet.',
        resStrong='Stark. Sieh dir die an, bei denen du zwischen is und are w&auml;hlen musstest.',
        resPerfect='Volle Punktzahl. Sag jetzt, was gerade um dich herum gemacht wird - ohne Namen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve a &lsquo;being&rsquo;. Se mete entre el auxiliar y la tercera forma.',
        resMid='Compara &lsquo;being&rsquo; con &lsquo;been&rsquo;. Lo decide la palabra de DELANTE.',
        resStrong='Muy bien. Revisa las que te obligaron a elegir entre is y are.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora di qu&eacute; se est&aacute; haciendo a tu alrededor, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
