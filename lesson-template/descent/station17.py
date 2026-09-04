# -*- coding: utf-8 -*-
"""Station 17 - Past Perfect Passive.  Mirrors camp 9, and wears its maroon.

Camp 9 (Past Perfect, the earlier past) was appended to the climb after the
eight tenses, so its station is appended to the descent after the Trial:
station N still mirrors camp N-8. The chassis is blockcamp-past-perfect.html -
which brings the Memory Vault plates, the maroon ink for 'had' and the purple
participle with it, so this deck needs no colour of its own.

The one thing this station teaches that station 15 does not: the passive
keeps the ORDER. 'By the time we arrived, the gate had been locked' - the
'had been' half is still the earlier action, the past simple half is still the
later one. Everything else is the swap, the form, the third form, why choose
it, and the small words - the same syllabus as every other station.
"""
from slidekit import head, sec, gloss, para, cards, mc, sort, match, gap, order, results, activate

B = 'past-perfect-time-signals/%s'   # camp 9's own plates - same place, other side

# A BARE 'been' IS WRITTEN WITH ITS CLASS, NOT AS class="aux". build_descent's
# tense_in_situ() gives a lone 'been' the present perfect's turquoise, because
# until this station every lone 'been' on the descent belonged to 'has been'.
# Here it belongs to 'had been' - 'Had it been locked?', 'had already been
# locked' - so it takes the past perfect's maroon by hand, and the chain reads
# as one colour whether a question or an adverb has split it.


def g(es, de):
    return gloss(es, de)


SLIDES = [

sec('teach', B % 'bg30.jpg', 'right', 'top',
    head('What it means', 'The same event, the other way round') + '\n' +
    cards([
      ('Active', '<em class="agent">The guards</em> had locked <em class="obj">the gate</em>.',
       ['<em class="agent">the water</em> had cracked <em class="obj">the wall</em>',
        '<em class="agent">somebody</em> had opened <em class="obj">the vault</em>'],
       g('Los guardias hab&iacute;an cerrado la puerta.', 'Die Wachen hatten das Tor verschlossen.')),
      ('Passive', '<em class="obj">The gate</em> <em class="aux">had been</em> <em class="pp">locked</em>.',
       ['<em class="obj">the wall</em> <em class="aux">had been</em> <em class="pp">cracked</em>',
        '<em class="obj">the vault</em> <em class="aux">had been</em> <em class="pp">opened</em>'],
       g('La puerta hab&iacute;a sido cerrada.', 'Das Tor war verschlossen worden.')),
    ])),

sec('teach', B % 'bg02.jpg', 'right', 'top',
    head('The swap', '<em class="obj">The object</em> becomes the subject') + '\n' +
    para([
      ('Active &mdash; the doer goes first',
       [('', '<em class="agent">The guards</em> had locked <em class="obj">the gate</em>')],
       g('Activa: primero quien lo hace', 'Aktiv: der T&auml;ter zuerst')),
      ('Passive &mdash; the same gate, now in front',
       [('', '<em class="obj">The gate</em> <em class="aux">had been</em> <em class="pp">locked</em> '
             '<em class="agent">by the guards</em>')],
       g('La puerta hab&iacute;a sido cerrada por los guardias', 'Das Tor war von den Wachen verschlossen worden')),
      ('And the doer can go',
       [('', '<em class="obj">The gate</em> <em class="aux">had been</em> <em class="pp">locked</em>.')],
       g('Y quien lo hace puede desaparecer', 'Und der T&auml;ter kann wegfallen')),
    ], '<em class="obj">THING</em> + <em class="aux">had been</em> + <em class="pp">PAST PARTICIPLE</em>')),

sec('teach', B % 'bg06.jpg', 'right', 'top',
    head('The form', 'One &lsquo;had been&rsquo; for everything') + '\n' +
    para([
      ('One thing, or many', [('the gate', '<em class="aux">had been</em> <em class="pp">locked</em>'),
                              ('the gates', '<em class="aux">had been</em> <em class="pp">locked</em>')],
       g('hab&iacute;a sido cerrada &middot; hab&iacute;an sido cerradas', 'war verschlossen worden &middot; waren verschlossen worden')),
      ('Say no', [('long', '<em class="aux">had</em> <em class="neg">not</em> <em class="t-ppf">been</em> <em class="pp">locked</em>'),
                  ('short', '<em class="aux">hadn&rsquo;t been</em> <em class="pp">locked</em>')],
       g('no hab&iacute;a sido cerrada', 'war nicht verschlossen worden')),
      ('Ask', [('one', '<em class="aux">Had</em> it <em class="t-ppf">been</em> <em class="pp">locked</em>?'),
               ('many', '<em class="aux">Had</em> they <em class="t-ppf">been</em> <em class="pp">locked</em>?')],
       g('&iquest;Hab&iacute;a sido cerrada? &middot; &iquest;Hab&iacute;an sido cerradas?', 'War es verschlossen worden? &middot; Waren sie verschlossen worden?')),
    ], '<em class="aux">&lsquo;had been&rsquo;</em> &mdash; the same for every subject'),
    'data-w="wide" style="--wcols:3"'),

sec('teach', B % 'bg08.jpg', 'right', '',
    head('The form', 'The participle is the THIRD form') + '\n' +
    para([
      ('Regular &mdash; add -ed', [('VERB', 'lock &rarr; locked &rarr; <em class="pp">locked</em>'),
                                   ('VERB', 'repair &rarr; repaired &rarr; <em class="pp">repaired</em>')],
       g('Regulares: se a&ntilde;ade -ed', 'Regelm&auml;&szlig;ig: -ed anh&auml;ngen')),
      ('Irregular &mdash; learn the third one',
       [('VERB', 'take &rarr; took &rarr; <em class="pp">taken</em>'),
        ('VERB', 'break &rarr; broke &rarr; <em class="pp">broken</em>'),
        ('VERB', 'find &rarr; found &rarr; <em class="pp">found</em>')],
       g('Irregulares: apr&eacute;ndete la tercera', 'Unregelm&auml;&szlig;ig: die dritte Form lernen')),
    ], 'the passive ALWAYS uses the <em class="pp">THIRD</em> form'),
    'data-w="wide"'),

sec('teach', B % 'bg04.jpg', 'right', 'top',
    head('Earlier and later', 'The passive keeps the order') + '\n' +
    para([
      ('Earlier &mdash; past perfect passive',
       [('', 'The cart <em class="aux">had been</em> <em class="pp">wrecked</em>')],
       g('Antes: el carro hab&iacute;a sido destrozado', 'Fr&uuml;her: der Wagen war zerst&ouml;rt worden')),
      ('Later &mdash; past simple',
       [('', '&hellip; by the time we <em class="t-past">arrived</em>.')],
       g('Despu&eacute;s: para cuando llegamos', 'Sp&auml;ter: als wir ankamen')),
      ('Swap the halves, swap the story',
       [('', 'When we <em class="t-past">arrived</em>, it <em class="aux">had been</em> <em class="pp">wrecked</em>.')],
       g('Cuando llegamos, ya hab&iacute;a sido destrozado', 'Als wir ankamen, war er schon zerst&ouml;rt worden')),
    ], 'the earlier action still takes <em class="aux">&lsquo;had&rsquo;</em>')),

sec('teach', B % 'bg24.jpg', 'right', 'top',   # measured: x6.71 quieter than the left
    head('Why choose it', 'When the doer is not the point') + '\n' +
    para([
      ('You did not know who', [('', 'The lock <em class="aux">had been</em> <em class="pp">broken</em>.')],
       g('No sab&iacute;as qui&eacute;n', 'Man wusste nicht, wer')),
      ('Everyone already knew who', [('', 'The bridge <em class="aux">had been</em> <em class="pp">repaired</em>.')],
       g('Todos sab&iacute;an ya qui&eacute;n', 'Alle wussten es ohnehin')),
      ('The thing mattered more', [('', 'Three shards <em class="aux">had been</em> <em class="pp">taken</em>.')],
       g('La cosa importaba m&aacute;s', 'Die Sache war wichtiger')),
    ], 'most passives carry <b>NO</b> &lsquo;by&rsquo; at all')),

sec('teach', B % 'bg21.jpg', 'left', 'top',
    head('Time signals', 'Small words, same places') + '\n' +
    para([
      ('already &middot; just', [('', 'The gate <em class="aux">had</em> already <em class="t-ppf">been</em> <em class="pp">locked</em>.')],
       g('ya &middot; acabar de', 'schon &middot; gerade')),
      ('never &middot; ever', [('', 'The vault <em class="aux">had</em> never <em class="t-ppf">been</em> <em class="pp">opened</em>.')],
       g('nunca &middot; alguna vez', 'nie &middot; jemals')),
      ('yet &mdash; at the end', [('', 'The wall <em class="aux">hadn&rsquo;t been</em> <em class="pp">repaired</em> yet.')],
       g('todav&iacute;a no &mdash; al final', 'noch nicht &mdash; am Ende')),
    ], 'the signal sits between <em class="aux">&lsquo;had&rsquo;</em> and <em class="t-ppf">&lsquo;been&rsquo;</em>')),

mc(1, 6, B % 'bg14.jpg', 'right', 'top', 'Choose the passive',
   'By the time we arrived, the beacon ______.', 'had been repaired',
   [('had repaired', 'That is active &mdash; it says the beacon did the repairing.' + g('Eso es activa.', 'Das ist Aktiv.')),
    ('had been repair', 'The passive needs the third form: repaired.' + g('Falta la tercera forma.', 'Es fehlt die dritte Form.')),
    ('has been repaired', '&lsquo;has&rsquo; is now. We arrived in the past, and this came before that.' + g('&rsquo;has&rsquo; es ahora.', '&rsquo;has&rsquo; ist jetzt.'))],
   'Para cuando llegamos, el faro ______.', 'Als wir ankamen, ______ das Leuchtfeuer ______.',
   why='Earlier than our arrival, so &lsquo;had been&rsquo; &mdash; then the third form, &lsquo;repaired&rsquo;.' + g('antes de que llegáramos: had been + tercera forma', 'vor unserer Ankunft: had been + dritte Form')),

mc(2, 6, B % 'bg12.jpg', 'left', 'top', 'Choose the passive',
   'The torches ______ before dark.', 'had been lit',
   [('had been light', '&lsquo;light&rsquo; is the first form. The third is &lsquo;lit&rsquo;.' + g('&rsquo;light&rsquo; es la forma base.', '&rsquo;light&rsquo; ist die Grundform.')),
    ('had lit', 'Active &mdash; torches cannot light themselves.' + g('Activa: las antorchas no se encienden solas.', 'Aktiv: Fackeln z&uuml;nden sich nicht selbst an.')),
    ('were been lit', '&lsquo;were&rsquo; and &lsquo;been&rsquo; never go together. It is &lsquo;had been&rsquo;.' + g('&rsquo;were been&rsquo; no existe.', '&rsquo;were been&rsquo; gibt es nicht.'))],
   'Las antorchas ______ antes de anochecer.', 'Die Fackeln ______ vor Einbruch der Dunkelheit ______.',
   why='&lsquo;had been&rsquo; for one or many, and the third form of &lsquo;light&rsquo; is &lsquo;lit&rsquo;.' + g('had been + lit', 'had been + lit')),

mc(3, 6, B % 'bg17.jpg', 'left', 'top', 'Say no',
   'The map ______ when they set off.', 'hadn&rsquo;t been read',
   [('hadn&rsquo;t read', 'Active. The map is not doing the reading.' + g('Activa.', 'Aktiv.')),
    ('hadn&rsquo;t been readed', '&lsquo;read&rsquo; is irregular. Its third form is &lsquo;read&rsquo;.' + g('La tercera forma es &rsquo;read&rsquo;.', 'Die dritte Form ist &rsquo;read&rsquo;.')),
    ('hadn&rsquo;t be read', 'After &lsquo;had&rsquo; comes &lsquo;been&rsquo;, not &lsquo;be&rsquo;.' + g('Tras &rsquo;had&rsquo; va &rsquo;been&rsquo;.', 'Nach &rsquo;had&rsquo; kommt &rsquo;been&rsquo;.'))],
   'El mapa ______ cuando partieron.', 'Die Karte ______ noch nicht ______, als sie aufbrachen.',
   why='The &lsquo;not&rsquo; goes on &lsquo;had&rsquo;: hadn&rsquo;t been read.' + g('el &rsquo;not&rsquo; va con &rsquo;had&rsquo;', 'das &rsquo;not&rsquo; h&auml;ngt an &rsquo;had&rsquo;')),

mc(4, 6, B % 'bg26.jpg', 'right', 'top', 'Ask the question',
   '______ the wall been repaired before the flood?', 'Had',
   [('Has', '&lsquo;Has&rsquo; is now. The flood was in the past.' + g('&rsquo;Has&rsquo; es ahora.', '&rsquo;Has&rsquo; ist jetzt.')),
    ('Was', 'There is a &lsquo;been&rsquo; here, so the first word is &lsquo;Had&rsquo;.' + g('Con &rsquo;been&rsquo;, primero va &rsquo;Had&rsquo;.', 'Mit &rsquo;been&rsquo; steht zuerst &rsquo;Had&rsquo;.')),
    ('Did', 'A past simple question does not take &lsquo;been&rsquo;.' + g('Una pregunta con &rsquo;Did&rsquo; no lleva &rsquo;been&rsquo;.', 'Eine Frage mit &rsquo;Did&rsquo; nimmt kein &rsquo;been&rsquo;.'))],
   '&iquest;______ sido reparado el muro antes de la inundaci&oacute;n?', '______ die Mauer vor der Flut repariert worden?',
   why='To ask, &lsquo;Had&rsquo; moves to the front and &lsquo;been&rsquo; stays where it was.' + g('&rsquo;Had&rsquo; va al principio', '&rsquo;Had&rsquo; r&uuml;ckt nach vorn')),

mc(5, 6, B % 'bg36.jpg', 'right', 'top', 'Active, or passive?',
   'Which means the same as &lsquo;The water had cracked the wall&rsquo;?',
   'The wall had been cracked by the water.',
   [('The wall had cracked the water.', 'That swaps who did what.' + g('Eso cambia qui&eacute;n hizo qu&eacute;.', 'Das vertauscht, wer was tat.')),
    ('The wall had been crack by the water.', 'Third form: cracked.' + g('Tercera forma: cracked.', 'Dritte Form: cracked.')),
    ('The water had been cracked by the wall.', 'Both halves the wrong way round.' + g('Las dos mitades al rev&eacute;s.', 'Beide H&auml;lften verkehrt herum.'))],
   '&iquest;Cu&aacute;l significa lo mismo?', 'Welcher Satz bedeutet dasselbe?',
   why='The wall was the object, so it goes to the front; the water follows &lsquo;by&rsquo;.' + g('el objeto pasa al principio', 'das Objekt r&uuml;ckt nach vorn')),

mc(6, 6, B % 'bg23.jpg', 'left', 'top', 'Which came first?',
   'When Audrey looked, the shard had been taken.', 'the shard was taken',
   [('Audrey looked', 'That is the later action &mdash; it is in the past simple.' + g('Esa es la posterior.', 'Das ist die sp&auml;tere Handlung.')),
    ('both at the same moment', '&lsquo;had been taken&rsquo; puts the taking earlier.' + g('&rsquo;had been taken&rsquo; es lo anterior.', '&rsquo;had been taken&rsquo; ist das Fr&uuml;here.')),
    ('the sentence does not say', 'It does: the past perfect is always the earlier one, passive or not.' + g('S&iacute; lo dice.', 'Doch, er sagt es.'))],
   'Cuando Audrey mir&oacute;, el fragmento hab&iacute;a sido robado.', 'Als Audrey hinsah, war die Scherbe schon genommen worden.',
   why='&lsquo;had been taken&rsquo; is the past perfect, so it happened before she looked.' + g('&rsquo;had been taken&rsquo; pas&oacute; antes', '&rsquo;had been taken&rsquo; geschah vorher')),

sort(B % 'bg25.jpg', 'left', 'top', 'Active, or passive?',
     'Click a sentence, then click its group.',
     ['active', 'passive'],
     [(0, 'they had locked it'), (0, 'we had found it'), (0, 'she had read it'), (0, 'they had lit it'),
      (1, 'it had been locked'), (1, 'it had been found'), (1, 'it had been read'), (1, 'it had been lit')],
     'Active: somebody had done it. Passive: it had been done &mdash; the doer is gone and &lsquo;been&rsquo; has appeared.'),

match(B % 'bg09.jpg', 'left', 'top', 'Match the active to its passive',
      'Click an active sentence, then click the passive that means the same.',
      [('The guards had locked the gate', 'the gate had been locked',
        'Los guardias hab&iacute;an cerrado la puerta', 'Die Wachen hatten das Tor verschlossen',
        'la puerta hab&iacute;a sido cerrada', 'das Tor war verschlossen worden'),
       ('Somebody had taken the shard', 'the shard had been taken',
        'Alguien hab&iacute;a robado el fragmento', 'Jemand hatte die Scherbe genommen',
        'el fragmento hab&iacute;a sido robado', 'die Scherbe war genommen worden'),
       ('The water had cracked the wall', 'the wall had been cracked',
        'El agua hab&iacute;a agrietado el muro', 'Das Wasser hatte die Mauer gespalten',
        'el muro hab&iacute;a sido agrietado', 'die Mauer war gespalten worden'),
       ('Dale had repaired the beacon', 'the beacon had been repaired',
        'Dale hab&iacute;a reparado el faro', 'Dale hatte das Leuchtfeuer repariert',
        'el faro hab&iacute;a sido reparado', 'das Leuchtfeuer war repariert worden'),
       ('They had opened the vault', 'the vault had been opened',
        'Hab&iacute;an abierto la c&aacute;mara', 'Sie hatten die Kammer ge&ouml;ffnet',
        'la c&aacute;mara hab&iacute;a sido abierta', 'die Kammer war ge&ouml;ffnet worden')],
      'The object of the active is always the subject of the passive.'),

gap(1, 2, B % 'bg33.jpg', 'left', 'top', 'Write the participle',
    'Type the verb in brackets in its third form.',
    [('The lock had been ', 'broken', '. <span class="dim">(break)</span>',
      'Not &lsquo;broke&rsquo; &mdash; that is the second form.', 170,
      'La cerradura hab&iacute;a sido ______. (romper)', 'Das Schloss war ______ worden. (aufbrechen)'),
     ('The shards had been ', 'taken', '. <span class="dim">(take)</span>',
      'take &rarr; took &rarr; taken. The passive takes the third.', 170,
      'Los fragmentos hab&iacute;an sido ______. (robar)', 'Die Scherben waren ______ worden. (nehmen)'),
     ('The bridge had been ', 'repaired', '. <span class="dim">(repair)</span>',
      'Regular verb, so the third form is just -ed.', 170,
      'El puente hab&iacute;a sido ______. (reparar)', 'Die Br&uuml;cke war ______ worden. (reparieren)')]),

gap(2, 2, B % 'bg16.jpg', 'right', 'top', '&lsquo;had&rsquo;, or &lsquo;had been&rsquo;?',   # measured: x5.00
    'Is the thing in front doing it, or having it done?',
    [('The guards ', 'had', ' locked the gate.', 'The guards did the locking: active.', 150,
      'Los guardias ______ cerrado la puerta.', 'Die Wachen ______ das Tor verschlossen.'),
     ('The gate ', 'had been', ' locked by the guards.', 'The gate had it done to it: passive.', 150,
      'La puerta ______ cerrada por los guardias.', 'Das Tor ______ von den Wachen verschlossen worden.'),
     ('The key ', 'had been', ' found before dark.', 'A key cannot find. Passive.', 150,
      'La llave ______ encontrada antes de anochecer.', 'Der Schl&uuml;ssel ______ vor Einbruch der Dunkelheit gefunden worden.')]),

order(B % 'bg38.jpg', 'right', 'top', 'the gate | had | been | locked .',
      'The thing, then had, then been, then the third form.',
      'La puerta hab&iacute;a sido cerrada.', 'Das Tor war verschlossen worden.'),

order(B % 'bg39.jpg', 'left', 'bottom', 'the wall | had | been | cracked | by the water .',
      '&lsquo;by&rsquo; and the doer come last, after the participle.',
      'El muro hab&iacute;a sido agrietado por el agua.', 'Die Mauer war vom Wasser gespalten worden.'),

results(B % 'bg41.jpg', 'left', 'top'),

activate(B % 'bg40.jpg', 'Now say what had been done',
         ['had been locked', 'had been taken', 'had been broken',
          'had been repaired', 'by the time', 'already', 'yet', 'by'],
         ['Describe a room you came back to. What had been moved before you got there?',
          'Tell your partner about a place where everything had already been decided before you arrived.',
          'Say what had been taken, and do not say who took it.'],
         ['Write a report on the vault after the raid, using only past perfect passives.',
          'Then rewrite one line as active. Which one had to name somebody?']),
]

TR_PAIRS = [
 ('Past Perfect Passive', 'Pluscuamperfecto pasivo', 'Plusquamperfekt Passiv'),
 ('By the time we arrived, the beacon ______.', 'Para cuando llegamos, el faro ______.', 'Als wir ankamen, ______ das Leuchtfeuer ______.'),
 ('had been repaired', 'había sido reparado', 'war repariert worden'),
 ('had repaired', 'había reparado (activa)', 'hatte repariert (Aktiv)'),
 ('had been repair', '(forma base: no existe)', '(Grundform: gibt es nicht)'),
 ('has been repaired', 'ha sido reparado (presente)', 'ist repariert worden (Gegenwart)'),
 ('The torches ______ before dark.', 'Las antorchas ______ antes de anochecer.', 'Die Fackeln ______ vor Einbruch der Dunkelheit ______.'),
 ('had been lit', 'habían sido encendidas', 'waren angezündet worden'),
 ('had been light', '(forma base: no existe)', '(Grundform: gibt es nicht)'),
 ('were been lit', '(no existe)', '(gibt es nicht)'),
 ('had lit', 'habían encendido (activa)', 'hatten angezündet (Aktiv)'),
 ('The map ______ when they set off.', 'El mapa ______ cuando partieron.', 'Die Karte ______ noch nicht ______, als sie aufbrachen.'),
 (u"hadn’t been read", 'no había sido leído', 'war nicht gelesen worden'),
 (u"hadn’t read", 'no había leído (activa)', 'hatte nicht gelesen (Aktiv)'),
 (u"hadn’t been readed", '(no existe)', '(gibt es nicht)'),
 (u"hadn’t be read", '(no existe)', '(gibt es nicht)'),
 ('______ the wall been repaired before the flood?', '¿______ sido reparado el muro antes de la inundación?', '______ die Mauer vor der Flut repariert worden?'),
 ('Had', '(past perfect)', '(Past Perfect)'), ('Has', '(presente perfecto)', '(Present Perfect)'),
 ('Was', '(pasado de ‘be’)', '(Vergangenheit von ‘be’)'), ('Did', '(pasado simple)', '(Past Simple)'),
 ('Which means the same as ‘The water had cracked the wall’?', '¿Cuál significa lo mismo que ‘The water had cracked the wall’?', 'Welcher Satz bedeutet dasselbe wie ‘The water had cracked the wall’?'),
 ('The wall had been cracked by the water.', 'El muro había sido agrietado por el agua.', 'Die Mauer war vom Wasser gespalten worden.'),
 ('The wall had cracked the water.', 'El muro había agrietado el agua.', 'Die Mauer hatte das Wasser gespalten.'),
 ('The wall had been crack by the water.', '(falta la tercera forma)', '(dritte Form fehlt)'),
 ('The water had been cracked by the wall.', 'El agua había sido agrietada por el muro.', 'Das Wasser war von der Mauer gespalten worden.'),
 ('When Audrey looked, the shard had been taken.', 'Cuando Audrey miró, el fragmento había sido robado.', 'Als Audrey hinsah, war die Scherbe schon genommen worden.'),
 ('the shard was taken', 'robaron el fragmento', 'die Scherbe wurde genommen'),
 ('Audrey looked', 'Audrey miró', 'Audrey sah hin'),
 ('both at the same moment', 'ambas en el mismo momento', 'beide im selben Moment'),
 ('the sentence does not say', 'la frase no lo dice', 'der Satz sagt es nicht'),
 ('they had locked it', 'lo habían cerrado', 'sie hatten es verschlossen'),
 ('we had found it', 'lo habíamos encontrado', 'wir hatten es gefunden'),
 ('she had read it', 'ella lo había leído', 'sie hatte es gelesen'),
 ('they had lit it', 'la habían encendido', 'sie hatten es angezündet'),
 ('it had been locked', 'había sido cerrado', 'es war verschlossen worden'),
 ('it had been found', 'había sido encontrado', 'es war gefunden worden'),
 ('it had been read', 'había sido leído', 'es war gelesen worden'),
 ('it had been lit', 'había sido encendida', 'es war angezündet worden'),
 ('active', 'activa', 'Aktiv'), ('passive', 'pasiva', 'Passiv'),
 ('(break)', '(romper)', '(aufbrechen)'), ('(take)', '(robar)', '(nehmen)'), ('(repair)', '(reparar)', '(reparieren)'),
 ('The lock had been . (break)', 'La cerradura había sido ______. (romper)', 'Das Schloss war ______ worden. (aufbrechen)'),
 ('The shards had been . (take)', 'Los fragmentos habían sido ______. (robar)', 'Die Scherben waren ______ worden. (nehmen)'),
 ('The bridge had been . (repair)', 'El puente había sido ______. (reparar)', 'Die Brücke war ______ worden. (reparieren)'),
 ('The guards locked the gate.', 'Los guardias ______ cerrado la puerta.', 'Die Wachen ______ das Tor verschlossen.'),
 ('The gate locked by the guards.', 'La puerta ______ cerrada por los guardias.', 'Das Tor ______ von den Wachen verschlossen worden.'),
 ('The key found before dark.', 'La llave ______ encontrada antes de anochecer.', 'Der Schlüssel ______ vor Einbruch der Dunkelheit gefunden worden.'),
 ('the gate', 'la puerta', 'das Tor'), ('had', 'había', 'war'), ('been', 'sido', '… worden'), ('locked .', 'cerrada .', 'verschlossen .'),
 ('the wall', 'el muro', 'die Mauer'), ('cracked', 'agrietado', 'gespalten'), ('by the water .', 'por el agua .', 'vom Wasser .'),
 ('had been locked', 'había sido cerrado', 'war verschlossen worden'), ('had been taken', 'había sido robado', 'war genommen worden'),
 ('had been broken', 'había sido roto', 'war zerbrochen worden'), ('had been repaired', 'había sido reparado', 'war repariert worden'),
 ('by the time', 'para cuando', 'als … schon'), ('already', 'ya', 'schon'), ('yet', 'todavía, aún', 'noch (nicht)'), ('by', 'por', 'von'),
 # teach chips
 ('the water had cracked the wall', 'el agua había agrietado el muro', 'das Wasser hatte die Mauer gespalten'),
 ('somebody had opened the vault', 'alguien había abierto la cámara', 'jemand hatte die Kammer geöffnet'),
 ('the wall had been cracked', 'el muro había sido agrietado', 'die Mauer war gespalten worden'),
 ('the vault had been opened', 'la cámara había sido abierta', 'die Kammer war geöffnet worden'),
]
TR = {'es': {k: v for k, v, _ in TR_PAIRS}, 'de': {k: v for k, _, v in TR_PAIRS}}

STATION = dict(
    file='blockcamp-passive-past-perfect.html',
    chassis='blockcamp-past-perfect.html',   # camp 9: brings its maroon with it
    title='Past Perfect Passive',
    sub='Station 17: it had been done before we got there',
    level='B1',
    doctitle='Block Camp II — Passive 17: Past Perfect Passive (B1) | Forbes English',
    hero=B % 'bg31.jpg',
    slides=SLIDES,
    tr=TR,
    row=dict(file='blockcamp-passive-past-perfect.html',
             title='Block Camp II — Passive 17: Past Perfect Passive',
             level='B1', access='pro', deck=True, video=False,
             created_at='2026-09-04T00:00:00+00:00', sort_order=None),
    card='BlockCamp/passive-17-past-perfect.jpg',
    messages={
      'en': dict(
        resLow='Go back to the swap. The object of the active is the subject of the passive.',
        resMid='Look again at the third form. &lsquo;Broke&rsquo; and &lsquo;broken&rsquo; are not the same word.',
        resStrong='Strong. Check the ones where you had to choose &lsquo;had&rsquo; or &lsquo;had been&rsquo;.',
        resPerfect='Full marks. Now say what had been done, and name nobody.',
        resNext='Recognising it is half of it. Now produce it &rarr;'),
      'de': dict(
        resLow='Geh zur&uuml;ck zum Tausch. Das Objekt des Aktivsatzes ist das Subjekt des Passivsatzes.',
        resMid='Sieh dir die dritte Form noch einmal an. &lsquo;Broke&rsquo; und &lsquo;broken&rsquo; sind nicht dasselbe Wort.',
        resStrong='Stark. Sieh dir die an, bei denen du zwischen &lsquo;had&rsquo; und &lsquo;had been&rsquo; w&auml;hlen musstest.',
        resPerfect='Volle Punktzahl. Sag jetzt, was gemacht worden war, ohne jemanden zu nennen.',
        resNext='Erkennen ist die halbe Miete. Jetzt anwenden &rarr;'),
      'es': dict(
        resLow='Vuelve al cambio. El objeto de la activa es el sujeto de la pasiva.',
        resMid='Mira otra vez la tercera forma. &lsquo;Broke&rsquo; y &lsquo;broken&rsquo; no son la misma palabra.',
        resStrong='Muy bien. Revisa las que te obligaron a elegir entre &lsquo;had&rsquo; y &lsquo;had been&rsquo;.',
        resPerfect='Puntuaci&oacute;n perfecta. Ahora di lo que se hab&iacute;a hecho, sin nombrar a nadie.',
        resNext='Reconocerlo es la mitad. Ahora prod&uacute;celo &rarr;'),
    },
)
