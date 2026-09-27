# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 2.

Ten languages, teach cards in the six-item form: English, German and Spanish
from the start; French, Italian, Portuguese, Russian, Arabic, Chinese and
Japanese added on 2026-09-25 (conventions in `ielts_langs.py`). Example
sentences a learner is meant to SAY in the activation stay English in every
language, like the answers.

Same split as Section 1: the answers are what the learner writes from English
speech, so they stay English everywhere. What translates is the rule, and on
this deck the rule is mostly about orientation — the words that tell you where
something is relative to something else, which is the whole map task.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
from ielts_langs import TAIL_MORE

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'audioPlay', 'audioOnce', 'audioPlaying', 'audioDone', 'audioReplay',
        'audioMissing']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

TAIL.update(TAIL_MORE)

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Section 2 &mdash; <em>the monologue and the map</em>',
    coverSub='One speaker, nobody to ask, and a plan you have to hold in your '
             'head',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 questions',

    t1Eyebrow='Before you listen',
    t1Title='One voice, and almost nothing said twice',
    t1ah='Nobody asks a question',
    t1ab='In Section 1 the other speaker keeps checking &mdash; <em>sorry, '
         'forty-two?</em> &mdash; and every check is a free repeat. In a '
         'monologue nobody does that, so a detail you miss is usually gone.',
    t1an='That is why the preparation time matters so much here.',
    t1bh='The map task is about orientation as much as English',
    t1bb='Labelling a plan tests whether you can hold an orientation while '
         'somebody walks you through a space in words. The vocabulary is '
         'small; the difficulty is that everything is relative to something '
         'else.',
    t1bn='In the real paper you get a drawn plan with letters on it. Here the '
         'places and positions are matched instead &mdash; the same work, one '
         'step before the letters.',
    t1ch='Fix your starting point first',
    t1cb='<em>On your left as you come through the gate</em> means nothing '
         'until you know where the gate is and which way you are facing. Find '
         'the entrance on the plan before the recording starts, and mark which '
         'way is "ahead".',
    t1cn='Many map-task marks are lost by candidates who never worked out '
         'where they were standing.',

    audEyebrow='The recording',
    audTitle='You will hear it once',
    audNote='A guide talking to a group of visitors at a public garden. Read '
            'the questions on the next slides first, then press play &mdash; '
            'here, or in the bar at the foot of any question slide. The '
            'recording keeps playing while you answer, and you hear it once.',

    matchEyebrow='Questions 1&ndash;5 &middot; The layout',
    matchTitle='Put each place where the guide put it',
    matchHint='Click a place, then its position. Everything is given relative '
              'to something else.',

    notesEyebrow='Questions 6&ndash;8 &middot; Complete the notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='Twice, a sentence contains two numbers. Write the one the gap '
              'asks for.',

    t2Eyebrow='After the recording',
    t2Title='How a map task hides its answers',
    t2ah='The shared landmark',
    t2ab='Two things are put beside the same feature &mdash; the play area '
         '<em>and</em> the bicycle racks are both next to the car park. '
         'Naming the landmark does not identify either of them, so the '
         'sentence has to be held whole.',
    t2an='<em>Two things</em> or <em>in fact</em> can signal that a second '
         'item is about to share a position.',
    t2bh='The thing that moved',
    t2bb='Something is described in its old place and then corrected to its '
         'new one. The plant stall "used to stand by the lake". Anyone '
         'answering from the first mention puts it in the wrong place.',
    t2bn='The guide repeats the new position deliberately. In a monologue, a '
         'repeat is usually a signal.',
    t2ch='The direction that depends on you',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Every one of these is relative to the speaker&rsquo;s position, not '
         'to the page.',
    t2cn='<em>Behind</em> and <em>beyond</em> are the two that catch people: '
         'behind the lake is on its far side, beyond the greenhouse is past '
         'it.',

    mcEyebrow='Questions 9&ndash;12 &middot; Detail',
    mcTitle='What exactly did the guide say?',

    m2why='The bank of the stream is being repaired. The birds are mentioned, '
          'and so is the spring, but neither is the reason: the spring is when '
          'it reopens.',
    m3why='Do not feed the birds. The guide gives a reason &mdash; bread is '
          'bad for them &mdash; and a reason attached to an instruction often '
          'marks what a speaker wants you to remember.',
    m4why='The ticket lasts all day, so visitors may stay. "We finish back at '
          'the café" is the line before, and it is about where the tour ends, '
          'not when you have to leave.',
    m5why='Anticlockwise, from the glasshouse &mdash; the last thing the guide '
          'says. Both halves come in one sentence, which is exactly where a '
          'distractor swaps one of them.',

    actTitle='Give the tour',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with a simple plan each &mdash; draw the room you '
                  'are in, or a building you both know. One of you describes '
                  'where five things are, without pointing and without naming '
                  'a compass direction. The other marks them on their own copy '
                  'and then compares.',
    actSpeak1='Describer: fix the starting point out loud first. "You come in '
              'through the door by the lifts." Then everything is relative to '
              'that.',
    actSpeak2='Put two of your five things beside the same landmark, and see '
              'whether your partner separates them.',
    actSpeak3='Move one thing halfway through: "the printer used to be by the '
              'window &mdash; it is now&hellip;" Say the new place twice, as '
              'the guide in the recording does.',
    actWriteKind='Writing · 100–150 words',
    actWriteBrief='Write the opening ninety seconds of a tour of somewhere you '
                  'know well, describing where five things are. Use no '
                  'compass directions at all &mdash; only positions relative '
                  'to the entrance and to each other &mdash; and put two of '
                  'them beside the same landmark.',
    actPlaceholder='As you come through the main door, on your left…',
)

# The explanations for Questions 1-8 sit beside their answers in the data
# module, which keeps the only copy of the English; they were plain strings
# there until 2026-09-23, so German and Spanish learners read them in English.
from ieltslisten_s2_data import PLACES_WHY, NOTES
T['en']['placesWhy'] = PLACES_WHY
T['en'].update(('n%dwhy' % (i + 1), r[2]) for i, r in enumerate(NOTES))

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 2 &mdash; <em>der Monolog und der Plan</em>',
    coverSub='Eine Stimme, niemand zum Nachfragen, und ein Plan, den du im '
             'Kopf behalten musst',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 Fragen',

    t1Eyebrow='Bevor du hörst',
    t1Title='Eine Stimme, und fast nichts wird zweimal gesagt',
    t1ah='Niemand stellt eine Rückfrage',
    t1ab='In Section 1 hakt die zweite Person ständig nach &mdash; <em>sorry, '
         'forty-two?</em> &mdash; und jede Rückfrage ist eine geschenkte '
         'Wiederholung. Im Monolog fragt niemand nach, also ist ein verpasstes '
         'Detail meist weg.',
    t1an='Deshalb zählt die Vorbereitungszeit hier so viel.',
    t1bh='Die Kartenaufgabe prüft Orientierung ebenso wie Englisch',
    t1bb='Einen Plan zu beschriften prüft, ob du eine Orientierung behältst, '
         'während dich jemand mit Worten durch einen Raum führt. Der '
         'Wortschatz ist klein; schwierig ist, dass alles relativ zu etwas '
         'anderem angegeben wird.',
    t1bn='In der echten Prüfung bekommst du einen gezeichneten Plan mit '
         'Buchstaben. Hier werden stattdessen Orte und Positionen zugeordnet '
         '&mdash; dieselbe Arbeit, einen Schritt vor den Buchstaben.',
    t1ch='Leg zuerst deinen Standpunkt fest',
    t1cb='<em>On your left as you come through the gate</em> heißt gar nichts, '
         'solange du nicht weißt, wo das Tor ist und wohin du schaust. Finde '
         'den Eingang auf dem Plan, bevor die Aufnahme startet, und markiere, '
         'wo „geradeaus“ ist.',
    t1cn='Viele Punkte einer Kartenaufgabe verlieren Kandidaten, die nie '
         'geklärt haben, wo sie stehen.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal',
    audNote='Eine Führerin spricht zu einer Besuchergruppe in einem '
            'öffentlichen Garten. Lies zuerst die Fragen auf den nächsten '
            'Folien, dann drücke Play &mdash; hier oder in der Leiste unten auf '
            'jeder Fragenfolie. Die Aufnahme läuft weiter, während du '
            'antwortest, und du hörst sie einmal.',

    matchEyebrow='Fragen 1&ndash;5 &middot; Die Anlage',
    matchTitle='Ordne jeden Ort dorthin, wo die Führerin ihn hingesetzt hat',
    matchHint='Klicke einen Ort an, dann seine Position. Alles ist relativ zu '
              'etwas anderem angegeben.',

    notesEyebrow='Fragen 6&ndash;8 &middot; Notizen vervollständigen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Zweimal stehen zwei Zahlen im selben Satz. Schreib die, nach '
              'der die Lücke fragt.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Wie eine Kartenaufgabe ihre Antworten versteckt',
    t2ah='Der geteilte Orientierungspunkt',
    t2ab='Zwei Dinge werden neben dasselbe Merkmal gesetzt &mdash; der '
         'Spielplatz <em>und</em> die Fahrradständer stehen beide neben dem '
         'Parkplatz. Den Orientierungspunkt zu nennen identifiziert keines '
         'von beiden; der Satz muss ganz behalten werden.',
    t2an='<em>Two things</em> oder <em>in fact</em> kann ankündigen, dass '
         'gleich ein zweites Ding dieselbe Position teilt.',
    t2bh='Das, was umgezogen ist',
    t2bb='Etwas wird an seinem alten Ort beschrieben und dann an den neuen '
         'korrigiert. Der Pflanzenstand „used to stand by the lake“. Wer nach '
         'der ersten Nennung antwortet, setzt ihn falsch.',
    t2bn='Sie wiederholt die neue Position absichtlich. Im Monolog ist eine '
         'Wiederholung meist ein Signal.',
    t2ch='Die Richtung, die von dir abhängt',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Alles davon ist relativ zur Position der Sprecherin, nicht zum '
         'Blatt.',
    t2cn='<em>Behind</em> und <em>beyond</em> erwischen die meisten: behind '
         'the lake heißt jenseits davon, beyond the greenhouse heißt daran '
         'vorbei.',

    mcEyebrow='Fragen 9&ndash;12 &middot; Detail',
    mcTitle='Was genau hat die Führerin gesagt?',

    m2why='Das Ufer des Bachs wird repariert. Die Vögel kommen vor und der '
          'Frühling auch, aber keins ist der Grund: im Frühling wird wieder '
          'geöffnet.',
    m3why='Die Vögel nicht füttern. Sie nennt einen Grund &mdash; Brot ist '
          'schlecht für sie &mdash; und ein Grund an einer Anweisung markiert '
          'oft, was man sich merken soll.',
    m4why='Das Ticket gilt den ganzen Tag, also darf man bleiben. „We finish '
          'back at the café“ steht davor und sagt, wo die Führung endet, nicht '
          'wann man gehen muss.',
    m5why='Gegen den Uhrzeigersinn, ab dem Glashaus &mdash; das Letzte, was die '
          'Führerin sagt. Beide Hälften stehen in einem Satz, und genau dort '
          'tauscht ein Ablenker eine davon aus.',

    actTitle='Führt eine Gruppe',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, jeder mit einem einfachen Plan &mdash; zeichne '
                  'den Raum, in dem ihr seid, oder ein Gebäude, das ihr beide '
                  'kennt. Einer beschreibt, wo fünf Dinge sind, ohne zu zeigen '
                  'und ohne Himmelsrichtungen. Der andere trägt sie ein und '
                  'vergleicht.',
    actSpeak1='Beschreiber: leg zuerst laut den Ausgangspunkt fest: „You come '
              'in through the door by the lifts.“ Danach ist alles relativ '
              'dazu.',
    actSpeak2='Setz zwei deiner fünf Dinge neben denselben Orientierungspunkt '
              'und schau, ob dein Partner sie auseinanderhält.',
    actSpeak3='Verschieb auf halber Strecke ein Ding: „the printer used to be '
              'by the window &mdash; it is now&hellip;“ Sag den neuen Ort '
              'zweimal, wie die Führerin in der Aufnahme.',
    actWriteKind='Schreiben · 100–150 Wörter',
    actWriteBrief='Schreib die ersten neunzig Sekunden einer Führung durch '
                  'einen Ort, den du gut kennst, und beschreibe, wo fünf Dinge '
                  'sind. Ohne jede Himmelsrichtung &mdash; nur relativ zum '
                  'Eingang und zueinander &mdash; und setz zwei davon neben '
                  'denselben Orientierungspunkt.',
    actPlaceholder='As you come through the main door, on your left…',

    # Questions 1-8: the English is registered from the data module, below.
    placesWhy='Jeder dieser Orte wird relativ zu etwas anderem angegeben '
              '&mdash; genau das ist eine Kartenaufgabe. Der Spielplatz teilt '
              'sich seinen Orientierungspunkt mit den Fahrradständern &mdash; '
              'beide liegen am Parkplatz &mdash;, also würde auf einem echten '
              'Plan, auf dem auch die Fahrradständer einen Buchstaben hätten, '
              '„next to the car park“ allein ihn nicht bestimmen. Der '
              'Pflanzenstand wird zweimal beschrieben, eben weil er umgezogen '
              'ist.',
    n1why='Zehn bis halb sechs. Gefragt ist die Schließzeit, und sie kommt '
          'als zweite im selben kurzen Satz wie die Öffnungszeit.',
    n2why='Acht Pfund. Derselbe Satz geht weiter mit „no charge at all for '
          'anyone under sixteen“, und das steht da, um jeden zu erwischen, '
          'der 0 schreibt.',
    n3why='Neunzig Minuten. Nicht die Öffnungszeiten und nicht „all day“ '
          '&mdash; so lange gilt das Ticket, eine Zeile später gesagt.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 2 &mdash; <em>el monólogo y el plano</em>',
    coverSub='Una sola voz, nadie a quien preguntar y un plano que tienes que '
             'sostener en la cabeza',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 preguntas',

    t1Eyebrow='Antes de escuchar',
    t1Title='Una voz, y casi nada se dice dos veces',
    t1ah='Nadie pregunta nada',
    t1ab='En la Section 1 la otra persona va comprobando &mdash; <em>sorry, '
         'forty-two?</em> &mdash; y cada comprobación es una repetición '
         'gratis. En un monólogo nadie lo hace, así que lo que se te escapa '
         'suele perderse.',
    t1an='Por eso el tiempo de preparación cuenta tanto aquí.',
    t1bh='La tarea del plano mide la orientación tanto como el inglés',
    t1bb='Etiquetar un plano mide si puedes mantener una orientación mientras '
         'alguien te lleva por un espacio con palabras. El vocabulario es '
         'poco; lo difícil es que todo se da en relación con otra cosa.',
    t1bn='En el examen real te dan un plano dibujado con letras. Aquí se '
         'emparejan lugares y posiciones: el mismo trabajo, un paso antes de '
         'las letras.',
    t1ch='Fija primero tu punto de partida',
    t1cb='<em>On your left as you come through the gate</em> no significa nada '
         'hasta que sabes dónde está la puerta y hacia dónde miras. Localiza '
         'la entrada en el plano antes de que empiece la grabación y marca '
         'qué dirección es «de frente».',
    t1cn='Muchos puntos de un plano los pierde quien nunca averiguó dónde '
         'estaba.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez',
    audNote='Una guía hablando a un grupo de visitantes en un jardín público. '
            'Lee primero las preguntas de las diapositivas siguientes y luego '
            'dale a reproducir, aquí o en la barra de abajo de cualquier '
            'pregunta. La grabación sigue sonando mientras respondes, y la oyes '
            'una sola vez.',

    matchEyebrow='Preguntas 1&ndash;5 &middot; La distribución',
    matchTitle='Coloca cada sitio donde lo colocó la guía',
    matchHint='Haz clic en un sitio y luego en su posición. Todo se da en '
              'relación con otra cosa.',

    notesEyebrow='Preguntas 6&ndash;8 &middot; Completa las notas',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Dos veces hay dos números en la misma frase. Escribe el que '
              'pide el hueco.',

    t2Eyebrow='Después de la grabación',
    t2Title='Cómo esconde sus respuestas una tarea de plano',
    t2ah='La referencia compartida',
    t2ab='Dos cosas se colocan junto al mismo elemento: la zona de juegos '
         '<em>y</em> el aparcabicis están las dos al lado del aparcamiento. '
         'Nombrar la referencia no identifica ninguna, así que hay que '
         'quedarse con la frase entera.',
    t2an='<em>Two things</em> o <em>in fact</em> pueden anunciar que un '
         'segundo elemento va a compartir posición.',
    t2bh='Lo que se ha movido',
    t2bb='Algo se describe en su sitio antiguo y luego se corrige al nuevo. El '
         'puesto de plantas «used to stand by the lake». Quien responde por la '
         'primera mención lo coloca mal.',
    t2bn='Repite la posición nueva a propósito. En un monólogo, una repetición '
         'suele ser una señal.',
    t2ch='La dirección que depende de ti',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. Todo '
         'eso es relativo a dónde está la persona que habla, no al papel.',
    t2cn='<em>Behind</em> y <em>beyond</em> son las dos que pillan a la gente: '
         'behind the lake es al otro lado, beyond the greenhouse es pasado el '
         'invernadero.',

    mcEyebrow='Preguntas 9&ndash;12 &middot; Detalle',
    mcTitle='¿Qué dijo exactamente la guía?',

    m2why='Están reparando la orilla del arroyo. Los pájaros salen, y la '
          'primavera también, pero ninguno es el motivo: en primavera se '
          'vuelve a abrir.',
    m3why='No dar de comer a los pájaros. Da un motivo &mdash; el pan les '
          'sienta mal &mdash; y un motivo pegado a una instrucción suele '
          'marcar lo que quien habla quiere que recuerdes.',
    m4why='La entrada vale todo el día, así que pueden quedarse. «We finish '
          'back at the café» es la línea anterior y dice dónde acaba la '
          'visita, no cuándo hay que irse.',
    m5why='En sentido contrario a las agujas del reloj, desde el invernadero: '
          'es lo último que dice la guía. Las dos mitades van en una frase, y '
          'ahí es justo donde un distractor cambia una.',

    actTitle='Haz de guía',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con un plano sencillo cada uno: dibujad la sala '
                  'en la que estáis, o un edificio que conozcáis los dos. Uno '
                  'describe dónde están cinco cosas, sin señalar y sin usar '
                  'puntos cardinales. El otro las marca en su copia y luego '
                  'comparáis.',
    actSpeak1='Quien describe: fija en voz alta el punto de partida: «You come '
              'in through the door by the lifts.» A partir de ahí todo es '
              'relativo a eso.',
    actSpeak2='Pon dos de tus cinco cosas junto a la misma referencia y mira '
              'si tu compañero las separa.',
    actSpeak3='A mitad de camino, mueve una cosa: «the printer used to be by '
              'the window &mdash; it is now&hellip;». Di el sitio nuevo dos '
              'veces, como hace la guía de la grabación.',
    actWriteKind='Escritura · 100–150 palabras',
    actWriteBrief='Escribe los primeros noventa segundos de una visita guiada '
                  'a un sitio que conozcas bien, diciendo dónde están cinco '
                  'cosas. Sin ningún punto cardinal &mdash; solo posiciones '
                  'relativas a la entrada y entre sí &mdash; y pon dos de '
                  'ellas junto a la misma referencia.',
    actPlaceholder='As you come through the main door, on your left…',

    # Questions 1-8: the English is registered from the data module, below.
    placesWhy='Cada uno de estos sitios se da en relación con otra cosa, que '
              'es justo en lo que consiste una tarea de plano. La zona de '
              'juegos comparte referencia con el aparcabicis &mdash; los dos '
              'están junto al aparcamiento &mdash;, así que en un plano de '
              'verdad, donde el aparcabicis también tendría letra, «next to '
              'the car park» por sí solo no la identificaría. Y el puesto de '
              'plantas se describe dos veces precisamente porque ha cambiado '
              'de sitio.',
    n1why='De diez a cinco y media. Lo que se pide es la hora de cierre, y '
          'llega en segundo lugar, en la misma frase corta que la de apertura.',
    n2why='Ocho libras. La misma frase sigue con «no charge at all for anyone '
          'under sixteen», que está ahí para pillar a quien escriba 0.',
    n3why='Noventa minutos. Ni el horario de apertura ni «all day», que es lo '
          'que dura la entrada y se dice una línea después.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Section 2 &mdash; <em>le monologue et le plan</em>',
    coverSub='Une seule voix, personne à qui demander, et un plan à garder en '
             'tête',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 questions',

    t1Eyebrow='Avant l’écoute',
    t1Title='Une seule voix, et presque rien n’est dit deux fois',
    t1ah='Personne ne pose de question',
    t1ab='En Section 1, l’autre interlocuteur vérifie sans cesse &mdash; '
         '<em>sorry, forty-two?</em> &mdash; et chaque vérification est une '
         'répétition gratuite. Dans un monologue, personne ne le fait : un '
         'détail manqué est le plus souvent perdu.',
    t1an='C’est pourquoi le temps de préparation compte tant ici.',
    t1bh='La tâche du plan teste l’orientation autant que l’anglais',
    t1bb='Compléter un plan teste votre capacité à garder votre orientation '
         'pendant que quelqu’un vous fait traverser un lieu avec des mots. Le '
         'vocabulaire est réduit ; la difficulté, c’est que tout est situé '
         'par rapport à autre chose.',
    t1bn='À l’examen, vous recevez un plan dessiné avec des lettres. Ici, on '
         'associe plutôt les lieux et les positions &mdash; le même travail, '
         'une étape avant les lettres.',
    t1ch='Fixez d’abord votre point de départ',
    t1cb='<em>On your left as you come through the gate</em> ne veut rien dire '
         'tant que vous ne savez pas où est l’entrée et dans quelle direction '
         'vous regardez. Repérez l’entrée sur le plan avant le début de '
         'l’enregistrement, et notez quelle direction est « tout droit ».',
    t1cn='Beaucoup de points se perdent sur un plan parce que le candidat n’a '
         'jamais établi où il se trouvait.',

    audEyebrow='L’enregistrement',
    audTitle='Vous l’entendrez une fois',
    audNote='Une guide s’adresse à un groupe de visiteurs dans un jardin '
            'public. Lisez d’abord les questions des diapositives suivantes, '
            'puis lancez la lecture &mdash; ici, ou dans la barre en bas de '
            'n’importe quelle question. L’enregistrement continue pendant que '
            'vous répondez, et vous ne l’entendez qu’une fois.',

    matchEyebrow='Questions 1&ndash;5 &middot; La disposition',
    matchTitle='Placez chaque lieu là où la guide l’a placé',
    matchHint='Cliquez sur un lieu, puis sur sa position. Tout est situé par '
              'rapport à autre chose.',

    notesEyebrow='Questions 6&ndash;8 &middot; Complétez les notes',
    notesTitle='Écrivez UN MOT ET/OU UN NOMBRE dans chaque blanc',
    notesHint='À deux reprises, une phrase contient deux nombres. Écrivez celui '
              'que demande le blanc.',

    t2Eyebrow='Après l’enregistrement',
    t2Title='Comment une tâche de plan cache ses réponses',
    t2ah='Le repère partagé',
    t2ab='Deux choses sont placées à côté du même élément &mdash; l’aire de '
         'jeux <em>et</em> les râteliers à vélos sont tous deux à côté du '
         'parking. Nommer le repère n’identifie ni l’un ni l’autre : il faut '
         'retenir la phrase entière.',
    t2an='<em>Two things</em> ou <em>in fact</em> peuvent annoncer qu’un second '
         'élément va partager la même position.',
    t2bh='Ce qui a déménagé',
    t2bb='Un élément est décrit à son ancien emplacement, puis corrigé vers le '
         'nouveau. Le stand de plantes « used to stand by the lake ». Qui '
         'répond d’après la première mention le place au mauvais endroit.',
    t2bn='La guide répète la nouvelle position exprès. Dans un monologue, une '
         'répétition est généralement un signal.',
    t2ch='La direction qui dépend de vous',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Toutes ces indications dépendent de la position de la personne qui '
         'parle, pas de la page.',
    t2cn='<em>Behind</em> et <em>beyond</em> sont les deux pièges : behind the '
         'lake, c’est de l’autre côté du lac ; beyond the greenhouse, c’est '
         'après la serre.',

    mcEyebrow='Questions 9&ndash;12 &middot; Détails',
    mcTitle='Qu’a dit exactement la guide ?',

    m2why='On répare la berge du ruisseau. Les oiseaux sont mentionnés, le '
          'printemps aussi, mais ni l’un ni l’autre n’est la raison : le '
          'printemps, c’est la réouverture.',
    m3why='Ne pas nourrir les oiseaux. La guide donne une raison &mdash; le pain '
          'leur fait du mal &mdash; et une raison attachée à une consigne '
          'signale souvent ce que la personne qui parle veut que vous '
          'reteniez.',
    m4why='Le billet est valable toute la journée, donc les visiteurs peuvent '
          'rester. « We finish back at the café » est la phrase d’avant : elle '
          'dit où finit la visite, pas quand il faut partir.',
    m5why='Dans le sens inverse des aiguilles d’une montre, en partant de '
          'l’ancienne serre du café &mdash; la dernière chose que dit la guide. '
          'Les deux moitiés tiennent dans une seule phrase, et c’est '
          'exactement là qu’un distracteur en échange une.',

    actTitle='Faites la visite',
    actUse='Au moins trois :',
    actSpeakBrief='À deux, chacun avec un plan simple &mdash; dessinez la pièce '
                  'où vous êtes, ou un bâtiment que vous connaissez tous les '
                  'deux. L’un décrit où se trouvent cinq choses, sans montrer '
                  'du doigt et sans nommer de point cardinal. L’autre les place '
                  'sur sa propre copie, puis vous comparez.',
    actSpeak1='Qui décrit : fixez d’abord le point de départ à voix haute : '
              '« You come in through the door by the lifts. » Ensuite, tout se '
              'situe par rapport à ce point.',
    actSpeak2='Placez deux de vos cinq choses à côté du même repère, et voyez '
              'si votre partenaire les distingue.',
    actSpeak3='En cours de route, déplacez une chose : « the printer used to be '
              'by the window &mdash; it is now&hellip; » Dites le nouvel '
              'emplacement deux fois, comme la guide de l’enregistrement.',
    actWriteKind='Écriture · 100–150 mots',
    actWriteBrief='Écrivez les quatre-vingt-dix premières secondes d’une visite '
                  'd’un lieu que vous connaissez bien, en disant où se trouvent '
                  'cinq choses. Aucun point cardinal &mdash; seulement des '
                  'positions par rapport à l’entrée et les unes aux autres '
                  '&mdash; et placez-en deux à côté du même repère.',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='Chacun de ces lieux est situé par rapport à autre chose : c’est '
              'cela, une tâche de plan. L’aire de jeux partage son repère avec '
              'les râteliers à vélos &mdash; tous deux à côté du parking '
              '&mdash; donc sur un vrai plan, où les râteliers auraient aussi '
              'une lettre, « next to the car park » ne suffirait pas à '
              'l’identifier. Le stand de plantes est décrit deux fois justement '
              'parce qu’il a déménagé.',
    n1why='De dix heures à dix-sept heures trente. On demande l’heure de '
          'fermeture, et elle arrive en second, dans la même phrase courte que '
          'l’heure d’ouverture.',
    n2why='Huit livres. La même phrase continue avec « no charge at all for '
          'anyone under sixteen », qui est là pour piéger quiconque écrit 0.',
    n3why='Quatre-vingt-dix minutes. Ni les horaires d’ouverture, ni « all '
          'day » &mdash; c’est la durée de validité du billet, dite une ligne '
          'plus loin.',
)

# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Section 2 &mdash; <em>il monologo e la mappa</em>',
    coverSub='Una sola voce, nessuno a cui chiedere e una pianta da tenere a '
             'mente',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 domande',

    t1Eyebrow='Prima dell’ascolto',
    t1Title='Una sola voce, e quasi niente detto due volte',
    t1ah='Nessuno fa domande',
    t1ab='Nella Section 1 l’altra persona continua a verificare &mdash; '
         '<em>sorry, forty-two?</em> &mdash; e ogni verifica è una ripetizione '
         'gratuita. In un monologo nessuno lo fa, quindi un dettaglio perso di '
         'solito è perso per sempre.',
    t1an='Per questo il tempo di preparazione conta così tanto qui.',
    t1bh='Il compito della mappa misura l’orientamento quanto l’inglese',
    t1bb='Completare una pianta verifica se riesci a mantenere l’orientamento '
         'mentre qualcuno ti accompagna a parole attraverso uno spazio. Il '
         'lessico è poco; la difficoltà è che tutto è dato in relazione a '
         'qualcos’altro.',
    t1bn='Nell’esame vero ricevi una pianta disegnata con delle lettere. Qui '
         'invece si abbinano luoghi e posizioni &mdash; lo stesso lavoro, un '
         'passo prima delle lettere.',
    t1ch='Fissa prima il punto di partenza',
    t1cb='<em>On your left as you come through the gate</em> non significa '
         'niente finché non sai dov’è il cancello e da che parte stai '
         'guardando. Trova l’ingresso sulla pianta prima che parta la '
         'registrazione, e segna qual è la direzione «avanti».',
    t1cn='Molti punti del compito della mappa li perde chi non ha mai '
         'stabilito dove si trovava.',

    audEyebrow='La registrazione',
    audTitle='La sentirai una volta',
    audNote='Una guida parla a un gruppo di visitatori in un giardino pubblico. '
            'Leggi prima le domande delle slide successive, poi premi play '
            '&mdash; qui o nella barra in fondo a qualsiasi slide di domande. '
            'La registrazione continua mentre rispondi, e la senti una volta '
            'sola.',

    matchEyebrow='Domande 1&ndash;5 &middot; La disposizione',
    matchTitle='Metti ogni luogo dove l’ha messo la guida',
    matchHint='Clicca su un luogo, poi sulla sua posizione. Tutto è dato in '
              'relazione a qualcos’altro.',

    notesEyebrow='Domande 6&ndash;8 &middot; Completa gli appunti',
    notesTitle='Scrivi UNA PAROLA E/O UN NUMERO in ogni spazio',
    notesHint='Due volte una frase contiene due numeri. Scrivi quello che '
              'chiede lo spazio.',

    t2Eyebrow='Dopo la registrazione',
    t2Title='Come il compito della mappa nasconde le risposte',
    t2ah='Il punto di riferimento condiviso',
    t2ab='Due cose vengono messe accanto allo stesso elemento &mdash; l’area '
         'giochi <em>e</em> le rastrelliere per le bici sono entrambe accanto '
         'al parcheggio. Nominare il punto di riferimento non identifica '
         'nessuna delle due, quindi bisogna tenere a mente la frase intera.',
    t2an='<em>Two things</em> o <em>in fact</em> possono segnalare che un '
         'secondo elemento sta per condividere la stessa posizione.',
    t2bh='La cosa che si è spostata',
    t2bb='Qualcosa viene descritto al suo vecchio posto e poi corretto con '
         'quello nuovo. Il banco delle piante «used to stand by the lake». Chi '
         'risponde in base alla prima menzione lo mette nel posto sbagliato.',
    t2bn='La guida ripete apposta la nuova posizione. In un monologo, una '
         'ripetizione di solito è un segnale.',
    t2ch='La direzione che dipende da te',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Ognuna di queste indicazioni dipende dalla posizione di chi parla, '
         'non dalla pagina.',
    t2cn='<em>Behind</em> e <em>beyond</em> sono le due che ingannano: behind '
         'the lake è dall’altra parte del lago, beyond the greenhouse è oltre '
         'la serra.',

    mcEyebrow='Domande 9&ndash;12 &middot; Dettagli',
    mcTitle='Che cosa ha detto esattamente la guida?',

    m2why='Stanno riparando l’argine del ruscello. Gli uccelli vengono '
          'nominati, e anche la primavera, ma nessuno dei due è il motivo: la '
          'primavera è quando riapre.',
    m3why='Non dare da mangiare agli uccelli. La guida dà un motivo &mdash; il '
          'pane fa loro male &mdash; e un motivo legato a un’istruzione spesso '
          'segnala ciò che chi parla vuole che tu ricordi.',
    m4why='Il biglietto vale tutto il giorno, quindi i visitatori possono '
          'restare. «We finish back at the café» è la frase precedente, e dice '
          'dove finisce la visita, non quando bisogna andarsene.',
    m5why='In senso antiorario, partendo dalla vecchia serra del caffè &mdash; '
          'l’ultima cosa che dice la guida. Le due metà stanno in una sola '
          'frase, ed è proprio lì che un distrattore ne scambia una.',

    actTitle='Fai da guida',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, ognuno con una pianta semplice &mdash; disegnate '
                  'la stanza in cui siete, o un edificio che conoscete '
                  'entrambi. Uno descrive dove si trovano cinque cose, senza '
                  'indicare e senza nominare i punti cardinali. L’altro le '
                  'segna sulla sua copia e poi confrontate.',
    actSpeak1='Chi descrive: fissa prima ad alta voce il punto di partenza: '
              '«You come in through the door by the lifts.» Poi tutto è '
              'relativo a quel punto.',
    actSpeak2='Metti due delle tue cinque cose accanto allo stesso punto di '
              'riferimento, e vedi se il tuo compagno le distingue.',
    actSpeak3='A metà, sposta una cosa: «the printer used to be by the window '
              '&mdash; it is now&hellip;» Di’ il nuovo posto due volte, come fa '
              'la guida nella registrazione.',
    actWriteKind='Scrittura · 100–150 parole',
    actWriteBrief='Scrivi i primi novanta secondi di una visita guidata a un '
                  'posto che conosci bene, dicendo dove si trovano cinque '
                  'cose. Nessun punto cardinale &mdash; solo posizioni rispetto '
                  'all’ingresso e tra loro &mdash; e metti due di queste accanto '
                  'allo stesso punto di riferimento.',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='Ognuno di questi luoghi è dato in relazione a qualcos’altro, ed '
              'è proprio questo il compito della mappa. L’area giochi condivide '
              'il punto di riferimento con le rastrelliere per le bici &mdash; '
              'entrambe accanto al parcheggio &mdash; quindi su una pianta '
              'vera, dove anche le rastrelliere avrebbero una lettera, «next to '
              'the car park» da solo non la identificherebbe. Il banco delle '
              'piante è descritto due volte proprio perché si è spostato.',
    n1why='Dalle dieci alle cinque e mezza. Si chiede l’orario di chiusura, che '
          'arriva per secondo nella stessa frase breve dell’orario di '
          'apertura.',
    n2why='Otto sterline. La stessa frase continua con «no charge at all for '
          'anyone under sixteen», che è lì per ingannare chi scrive 0.',
    n3why='Novanta minuti. Non l’orario di apertura, e non «all day» &mdash; che '
          'è quanto dura il biglietto, detto una riga dopo.',
)

# ── Portuguese (European) ──────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Section 2 &mdash; <em>o monólogo e o mapa</em>',
    coverSub='Uma só voz, ninguém a quem perguntar e uma planta que tens de '
             'guardar na cabeça',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 perguntas',

    t1Eyebrow='Antes de ouvir',
    t1Title='Uma só voz, e quase nada dito duas vezes',
    t1ah='Ninguém faz perguntas',
    t1ab='Na Section 1 a outra pessoa está sempre a confirmar &mdash; '
         '<em>sorry, forty-two?</em> &mdash; e cada confirmação é uma '
         'repetição grátis. Num monólogo ninguém faz isso, por isso um '
         'pormenor que te escape costuma perder-se.',
    t1an='É por isso que o tempo de preparação conta tanto aqui.',
    t1bh='A tarefa do mapa testa a orientação tanto como o inglês',
    t1bb='Legendar uma planta testa se consegues manter a orientação enquanto '
         'alguém te conduz por um espaço com palavras. O vocabulário é pouco; '
         'a dificuldade é que tudo é dado em relação a outra coisa.',
    t1bn='No exame real recebes uma planta desenhada com letras. Aqui, em vez '
         'disso, fazem-se corresponder lugares e posições &mdash; o mesmo '
         'trabalho, um passo antes das letras.',
    t1ch='Fixa primeiro o teu ponto de partida',
    t1cb='<em>On your left as you come through the gate</em> não quer dizer '
         'nada enquanto não souberes onde fica o portão e para onde estás '
         'virado. Encontra a entrada na planta antes de a gravação começar e '
         'marca qual é a direção «em frente».',
    t1cn='Muitos pontos da tarefa do mapa perdem-nos os candidatos que nunca '
         'perceberam onde estavam.',

    audEyebrow='A gravação',
    audTitle='Vais ouvi-la uma vez',
    audNote='Uma guia a falar para um grupo de visitantes num jardim público. '
            'Lê primeiro as perguntas dos diapositivos seguintes e depois '
            'carrega em reproduzir &mdash; aqui ou na barra no fundo de '
            'qualquer diapositivo de perguntas. A gravação continua enquanto '
            'respondes, e só a ouves uma vez.',

    matchEyebrow='Perguntas 1&ndash;5 &middot; A disposição',
    matchTitle='Põe cada lugar onde a guia o pôs',
    matchHint='Clica num lugar e depois na sua posição. Tudo é dado em relação '
              'a outra coisa.',

    notesEyebrow='Perguntas 6&ndash;8 &middot; Completa as notas',
    notesTitle='Escreve UMA PALAVRA E/OU UM NÚMERO em cada espaço',
    notesHint='Duas vezes, uma frase tem dois números. Escreve o que o espaço '
              'pede.',

    t2Eyebrow='Depois da gravação',
    t2Title='Como a tarefa do mapa esconde as respostas',
    t2ah='A referência partilhada',
    t2ab='Duas coisas ficam ao lado do mesmo elemento &mdash; o parque '
         'infantil <em>e</em> os suportes para bicicletas estão ambos ao lado '
         'do parque de estacionamento. Nomear a referência não identifica '
         'nenhum deles, por isso é preciso reter a frase inteira.',
    t2an='<em>Two things</em> ou <em>in fact</em> podem assinalar que um '
         'segundo elemento vai partilhar a mesma posição.',
    t2bh='O que mudou de sítio',
    t2bb='Algo é descrito no sítio antigo e depois corrigido para o novo. A '
         'banca das plantas «used to stand by the lake». Quem responde pela '
         'primeira menção põe-na no sítio errado.',
    t2bn='A guia repete a nova posição de propósito. Num monólogo, uma '
         'repetição costuma ser um sinal.',
    t2ch='A direção que depende de ti',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Todas estas indicações dependem da posição de quem fala, não da '
         'página.',
    t2cn='<em>Behind</em> e <em>beyond</em> são as duas que apanham as pessoas: '
         'behind the lake é do outro lado do lago, beyond the greenhouse é '
         'depois da estufa.',

    mcEyebrow='Perguntas 9&ndash;12 &middot; Pormenor',
    mcTitle='O que disse exatamente a guia?',

    m2why='Estão a reparar a margem do riacho. As aves são referidas, e a '
          'primavera também, mas nenhuma delas é a razão: a primavera é quando '
          'reabre.',
    m3why='Não dar comida às aves. A guia dá uma razão &mdash; o pão faz-lhes '
          'mal &mdash; e uma razão ligada a uma instrução costuma marcar o que '
          'quem fala quer que retenhas.',
    m4why='O bilhete é válido todo o dia, por isso os visitantes podem ficar. '
          '«We finish back at the café» é a frase anterior e diz onde acaba a '
          'visita, não quando é preciso sair.',
    m5why='No sentido contrário ao dos ponteiros do relógio, a partir da '
          'antiga estufa do café &mdash; a última coisa que a guia diz. As '
          'duas metades vêm na mesma frase, e é exatamente aí que um distrator '
          'troca uma delas.',

    actTitle='Faz de guia',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, cada um com uma planta simples &mdash; desenhem a '
                  'sala onde estão, ou um edifício que ambos conheçam. Um '
                  'descreve onde estão cinco coisas, sem apontar e sem usar '
                  'pontos cardeais. O outro marca-as na sua cópia e depois '
                  'comparam.',
    actSpeak1='Quem descreve: fixa primeiro, em voz alta, o ponto de partida: '
              '«You come in through the door by the lifts.» A partir daí, tudo '
              'é relativo a isso.',
    actSpeak2='Põe duas das tuas cinco coisas ao lado da mesma referência e vê '
              'se o teu colega as distingue.',
    actSpeak3='A meio, muda uma coisa de sítio: «the printer used to be by the '
              'window &mdash; it is now&hellip;» Diz o sítio novo duas vezes, '
              'como faz a guia na gravação.',
    actWriteKind='Escrita · 100–150 palavras',
    actWriteBrief='Escreve os primeiros noventa segundos de uma visita guiada a '
                  'um sítio que conheces bem, dizendo onde estão cinco coisas. '
                  'Nenhum ponto cardeal &mdash; só posições em relação à entrada '
                  'e umas às outras &mdash; e põe duas delas ao lado da mesma '
                  'referência.',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='Cada um destes lugares é dado em relação a outra coisa, e é isso '
              'mesmo uma tarefa de mapa. O parque infantil partilha a '
              'referência com os suportes para bicicletas &mdash; ambos ao lado '
              'do parque de estacionamento &mdash; por isso numa planta a '
              'sério, onde os suportes também teriam uma letra, «next to the '
              'car park» sozinho não o identificaria. A banca das plantas é '
              'descrita duas vezes precisamente porque mudou de sítio.',
    n1why='Das dez às cinco e meia. Pede-se a hora de fecho, que chega em '
          'segundo lugar, na mesma frase curta que a hora de abertura.',
    n2why='Oito libras. A mesma frase continua com «no charge at all for anyone '
          'under sixteen», que está lá para apanhar quem escreve 0.',
    n3why='Noventa minutos. Nem o horário de abertura, nem «all day» &mdash; que '
          'é quanto tempo dura o bilhete, dito uma linha depois.',
)

# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Section 2 &mdash; <em>монолог и план</em>',
    coverSub='Один голос, спросить некого, и план, который нужно держать в '
             'голове',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 вопросов',

    t1Eyebrow='Перед прослушиванием',
    t1Title='Один голос, и почти ничего не звучит дважды',
    t1ah='Никто не переспрашивает',
    t1ab='В Section 1 второй собеседник всё время уточняет &mdash; <em>sorry, '
         'forty-two?</em> &mdash; и каждое уточнение даёт бесплатный повтор. '
         'В монологе этого никто не делает, поэтому пропущенная деталь обычно '
         'потеряна.',
    t1an='Вот почему время на подготовку здесь так важно.',
    t1bh='Задание с планом проверяет ориентацию не меньше, чем английский',
    t1bb='Подписать план значит удержать ориентацию, пока вас словами ведут по '
         'пространству. Слов немного; трудность в том, что всё описано '
         'относительно чего-то другого.',
    t1bn='На настоящем экзамене вам дают нарисованный план с буквами. Здесь '
         'вместо этого сопоставляются места и позиции &mdash; та же работа, на '
         'шаг раньше букв.',
    t1ch='Сначала определите точку отсчёта',
    t1cb='<em>On your left as you come through the gate</em> ничего не '
         'значит, пока вы не знаете, где ворота и куда вы смотрите. Найдите '
         'вход на плане до начала записи и отметьте, какое направление '
         'означает «прямо».',
    t1cn='Многие баллы в задании с планом теряют те, кто так и не понял, где '
         'стоит.',

    audEyebrow='Запись',
    audTitle='Вы услышите её один раз',
    audNote='Экскурсовод обращается к группе посетителей в городском саду. '
            'Сначала прочитайте вопросы на следующих слайдах, затем нажмите '
            'воспроизведение &mdash; здесь или на панели внизу любого слайда с '
            'вопросами. Запись продолжает звучать, пока вы отвечаете, и вы '
            'слышите её один раз.',

    matchEyebrow='Вопросы 1&ndash;5 &middot; Расположение',
    matchTitle='Расставьте места так, как их расставила экскурсовод',
    matchHint='Нажмите на место, затем на его позицию. Всё описано '
              'относительно чего-то другого.',

    notesEyebrow='Вопросы 6&ndash;8 &middot; Заполните заметки',
    notesTitle='Впишите ОДНО СЛОВО И/ИЛИ ЧИСЛО в каждый пропуск',
    notesHint='Дважды в одном предложении звучат два числа. Впишите то, о '
              'котором спрашивает пропуск.',

    t2Eyebrow='После записи',
    t2Title='Как задание с планом прячет ответы',
    t2ah='Общий ориентир',
    t2ab='Две вещи помещены рядом с одним и тем же объектом &mdash; детская '
         'площадка <em>и</em> велопарковка обе находятся рядом с автостоянкой. '
         'Назвав ориентир, вы не определите ни одну из них, поэтому фразу '
         'нужно удержать целиком.',
    t2an='<em>Two things</em> или <em>in fact</em> могут сигнализировать, что '
         'сейчас второй объект окажется в той же позиции.',
    t2bh='То, что переехало',
    t2bb='Что-то описывают на старом месте, а потом исправляют на новое. '
         'Прилавок с растениями «used to stand by the lake». Кто отвечает по '
         'первому упоминанию, ставит его не туда.',
    t2bn='Экскурсовод нарочно повторяет новое место. В монологе повтор обычно '
         'служит сигналом.',
    t2ch='Направление, которое зависит от вас',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. Всё '
         'это указано относительно того, где стоит говорящий, а не '
         'относительно страницы.',
    t2cn='<em>Behind</em> и <em>beyond</em> &mdash; две ловушки: behind the '
         'lake значит на другом берегу озера, beyond the greenhouse значит '
         'дальше теплицы.',

    mcEyebrow='Вопросы 9&ndash;12 &middot; Детали',
    mcTitle='Что именно сказала экскурсовод?',

    m2why='Ремонтируют берег ручья. Птицы упоминаются, и весна тоже, но ни то '
          'ни другое не причина: весной дорожку снова откроют.',
    m3why='Не кормить птиц. Экскурсовод называет причину &mdash; хлеб им вреден '
          '&mdash; а причина, привязанная к указанию, часто отмечает то, что '
          'говорящий хочет, чтобы вы запомнили.',
    m4why='Билет действует весь день, поэтому посетители могут остаться. «We '
          'finish back at the café» звучит строкой раньше, и это о том, где '
          'заканчивается экскурсия, а не о том, когда нужно уходить.',
    m5why='Против часовой стрелки, начиная со старой оранжереи с кафе &mdash; '
          'это последнее, что говорит экскурсовод. Обе половины звучат в одном '
          'предложении, и именно там отвлекающий вариант подменяет одну из '
          'них.',

    actTitle='Проведите экскурсию',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, у каждого простой план &mdash; нарисуйте комнату, в '
                  'которой вы находитесь, или здание, которое вы оба знаете. '
                  'Один описывает, где находятся пять предметов, не показывая '
                  'рукой и не называя сторон света. Другой отмечает их на своей '
                  'копии, а затем вы сравниваете.',
    actSpeak1='Тот, кто описывает: сначала вслух задайте точку отсчёта: «You '
              'come in through the door by the lifts.» Дальше всё описывается '
              'относительно неё.',
    actSpeak2='Поставьте два из пяти предметов рядом с одним ориентиром и '
              'посмотрите, различит ли их партнёр.',
    actSpeak3='На полпути переместите один предмет: «the printer used to be by '
              'the window &mdash; it is now&hellip;» Назовите новое место '
              'дважды, как это делает экскурсовод в записи.',
    actWriteKind='Письмо · 100–150 слов',
    actWriteBrief='Напишите первые девяносто секунд экскурсии по месту, которое '
                  'вы хорошо знаете, и скажите, где находятся пять вещей. '
                  'Никаких сторон света &mdash; только положение относительно '
                  'входа и друг друга &mdash; и поставьте две из них рядом с '
                  'одним ориентиром.',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='Каждое из этих мест описано относительно чего-то другого '
              '&mdash; в этом и состоит задание с планом. Детская площадка '
              'делит ориентир с велопарковкой &mdash; обе рядом с автостоянкой '
              '&mdash; поэтому на настоящем плане, где у велопарковки тоже была '
              'бы буква, «next to the car park» само по себе не определило бы '
              'её. Прилавок с растениями описан дважды именно потому, что он '
              'переехал.',
    n1why='С десяти до половины шестого. Спрашивают время закрытия, и оно '
          'звучит вторым в том же коротком предложении, что и время открытия.',
    n2why='Восемь фунтов. То же предложение продолжается словами «no charge at '
          'all for anyone under sixteen», и они там, чтобы поймать того, кто '
          'напишет 0.',
    n3why='Девяносто минут. Не часы работы и не «all day» &mdash; столько '
          'действует билет, это сказано строкой ниже.',
)

# ── Arabic ─────────────────────────────────────────────────────────────
# Quoted English is wrapped in <bdi>, as in Section 1, so it keeps its own
# word order inside right-to-left text (check-lesson.js BIDI).
T['ar'] = dict(
    coverTitle='Section 2 &mdash; <em>المونولوج والخريطة</em>',
    coverSub='صوت واحد، ولا أحد تسأله، ومخطط عليك أن تحفظه في ذهنك',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 سؤالًا',

    t1Eyebrow='قبل أن تستمع',
    t1Title='صوت واحد، ولا يكاد يُقال شيء مرتين',
    t1ah='لا أحد يطرح سؤالًا',
    t1ab='في Section 1 يظل المتحدث الآخر يستوثق &mdash; <em>sorry, '
         'forty-two?</em> &mdash; وكل استيثاق تكرار مجاني. أما في المونولوج '
         'فلا أحد يفعل ذلك، ولذلك فالتفصيل الذي يفوتك يضيع في الغالب.',
    t1an='ولهذا يكتسب وقت التحضير هنا كل هذه الأهمية.',
    t1bh='مهمة الخريطة تختبر الاتجاهات بقدر ما تختبر الإنجليزية',
    t1bb='تعبئة المخطط تختبر قدرتك على الحفاظ على اتجاهك بينما يقودك أحدهم '
         'بالكلمات عبر مكان ما. المفردات قليلة؛ والصعوبة أن كل شيء يُحدَّد '
         'بالنسبة إلى شيء آخر.',
    t1bn='في الاختبار الحقيقي تحصل على مخطط مرسوم عليه حروف. أما هنا فتطابق '
         'الأماكن بالمواقع بدلًا من ذلك &mdash; العمل نفسه، قبل الحروف بخطوة.',
    t1ch='حدّد نقطة انطلاقك أولًا',
    t1cb='عبارة <em>On your left as you come through the gate</em> لا تعني '
         'شيئًا حتى تعرف أين البوابة وإلى أي اتجاه تنظر. حدّد المدخل على '
         'المخطط قبل أن يبدأ التسجيل، وضع علامة على الاتجاه «إلى الأمام».',
    t1cn='كثير من درجات مهمة الخريطة يخسرها مرشحون لم يحددوا قط أين كانوا '
         'يقفون.',

    audEyebrow='التسجيل',
    audTitle='ستسمعه مرة واحدة',
    audNote='مرشدة تتحدث إلى مجموعة من الزوار في حديقة عامة. اقرأ أولًا الأسئلة '
            'في الشرائح التالية، ثم اضغط زر التشغيل &mdash; هنا، أو في الشريط '
            'أسفل أي شريحة أسئلة. يستمر التسجيل وأنت تجيب، ولن تسمعه إلا مرة '
            'واحدة.',

    matchEyebrow='الأسئلة 1&ndash;5 &middot; تخطيط المكان',
    matchTitle='ضع كل مكان حيث وضعته المرشدة',
    matchHint='انقر على مكان، ثم على موقعه. كل شيء محدد بالنسبة إلى شيء آخر.',

    notesEyebrow='الأسئلة 6&ndash;8 &middot; أكمل الملاحظات',
    notesTitle='اكتب كلمة واحدة و/أو رقمًا واحدًا في كل فراغ',
    notesHint='مرتين تحتوي جملة واحدة على رقمين. اكتب الرقم الذي يسأل عنه '
              'الفراغ.',

    t2Eyebrow='بعد التسجيل',
    t2Title='كيف تخفي مهمة الخريطة إجاباتها',
    t2ah='المَعلَم المشترك',
    t2ab='يوضع شيئان بجانب المَعلَم نفسه &mdash; منطقة لعب الأطفال وحوامل '
         'الدراجات <em>كلاهما</em> بجانب موقف السيارات. ذكرُ المَعلَم لا يحدد '
         'أيًّا منهما، ولذلك يجب أن تحتفظ بالجملة كاملة.',
    t2an='قد تنبئ <em>two things</em> أو <em>in fact</em> بأن شيئًا ثانيًا على '
         'وشك أن يشارك الموقع نفسه.',
    t2bh='الشيء الذي انتقل',
    t2bb='يوصف شيء في مكانه القديم ثم يُصحَّح إلى مكانه الجديد. كشك النباتات '
         '<bdi>&ldquo;used to stand by the lake&rdquo;</bdi>. ومن يجيب من '
         'الذكر الأول يضعه في المكان الخطأ.',
    t2bn='تكرر المرشدة الموقع الجديد عمدًا. في المونولوج، التكرار إشارة في '
         'الغالب.',
    t2ch='الاتجاه الذي يتوقف عليك',
    t2cb='<em>On your left</em>، <em>directly ahead</em>، <em>behind the '
         'lake</em>، <em>on the far side from where we are standing</em>. كل '
         'هذه التعبيرات منسوبة إلى موقع المتحدث، لا إلى الصفحة.',
    t2cn='<em>Behind</em> و<em>beyond</em> هما الكلمتان اللتان توقعان الناس: '
         '<bdi>behind the lake</bdi> تعني على الضفة الأخرى من البحيرة، '
         'و<bdi>beyond the greenhouse</bdi> تعني بعد الدفيئة.',

    mcEyebrow='الأسئلة 9&ndash;12 &middot; التفاصيل',
    mcTitle='ماذا قالت المرشدة بالضبط؟',

    m2why='يجري إصلاح ضفة الجدول. الطيور مذكورة، والربيع كذلك، لكن أيًّا '
          'منهما ليس السبب: الربيع هو موعد إعادة الفتح.',
    m3why='لا تطعموا الطيور. تذكر المرشدة سببًا &mdash; الخبز مضر بها &mdash; '
          'والسبب المرتبط بتعليمات كثيرًا ما يشير إلى ما يريد المتحدث أن '
          'تتذكره.',
    m4why='التذكرة صالحة طوال اليوم، فيجوز للزوار البقاء. عبارة '
          '<bdi>&ldquo;We finish back at the café&rdquo;</bdi> هي السطر '
          'السابق، وهي عن مكان انتهاء الجولة، لا عن موعد المغادرة.',
    m5why='عكس اتجاه عقارب الساعة، بدءًا من البيت الزجاجي القديم &mdash; آخر '
          'ما تقوله المرشدة. النصفان يأتيان في جملة واحدة، وهناك بالضبط '
          'يستبدل المشتِّت أحدهما.',

    actTitle='قُد الجولة',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='في أزواج، مع مخطط بسيط لكل منكما &mdash; ارسما الغرفة التي '
                  'أنتما فيها، أو مبنى تعرفانه كلاكما. يصف أحدكما أين توجد '
                  'خمسة أشياء، دون أن يشير بيده ودون ذكر أي جهة من الجهات '
                  'الأربع. ويضع الآخر علامات عليها في نسخته ثم تقارنان.',
    actSpeak1='من يصف: حدّد نقطة الانطلاق بصوت عالٍ أولًا: <bdi>&ldquo;You '
              'come in through the door by the lifts.&rdquo;</bdi> ثم يصبح كل '
              'شيء منسوبًا إليها.',
    actSpeak2='ضع شيئين من أشيائك الخمسة بجانب المَعلَم نفسه، وانظر هل يميّز '
              'زميلك بينهما.',
    actSpeak3='في منتصف الطريق، انقل شيئًا واحدًا: <bdi>&ldquo;the printer '
              'used to be by the window &mdash; it is now&hellip;&rdquo;</bdi> '
              'وقل المكان الجديد مرتين، كما تفعل المرشدة في التسجيل.',
    actWriteKind='الكتابة · 100–150 كلمة',
    actWriteBrief='اكتب التسعين ثانية الأولى من جولة في مكان تعرفه جيدًا، وصف '
                  'فيها أين توجد خمسة أشياء. لا تذكر أي جهة من الجهات الأربع '
                  '&mdash; فقط مواقع منسوبة إلى المدخل وإلى بعضها &mdash; وضع '
                  'اثنين منها بجانب المَعلَم نفسه.',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='كل مكان من هذه الأماكن محدد بالنسبة إلى شيء آخر، وهذا هو جوهر '
              'مهمة الخريطة. منطقة لعب الأطفال تشترك في مَعلَمها مع حوامل '
              'الدراجات &mdash; كلاهما بجانب موقف السيارات &mdash; ولذلك على '
              'مخطط حقيقي، حيث يكون لحوامل الدراجات حرف أيضًا، لن تكفي عبارة '
              '<bdi>&ldquo;next to the car park&rdquo;</bdi> وحدها لتحديدها. '
              'ويوصف كشك النباتات مرتين لأنه انتقل تحديدًا.',
    n1why='من العاشرة حتى الخامسة والنصف. المطلوب هو موعد الإغلاق، ويأتي ثانيًا '
          'في الجملة القصيرة نفسها التي فيها موعد الفتح.',
    n2why='ثمانية جنيهات. الجملة نفسها تتابع بعبارة <bdi>&ldquo;no charge at '
          'all for anyone under sixteen&rdquo;</bdi>، وهي موجودة لتوقع من '
          'يكتب 0.',
    n3why='تسعون دقيقة. لا ساعات العمل، ولا <bdi>&ldquo;all day&rdquo;</bdi> '
          '&mdash; فهي مدة صلاحية التذكرة، وتُقال بعد سطر واحد.',
)

# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Section 2 &mdash; <em>独白与地图</em>',
    coverSub='一个声音，没人可问，还有一张要记在脑子里的平面图',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 题',

    t1Eyebrow='听之前',
    t1Title='只有一个声音，几乎什么都不会说第二遍',
    t1ah='没人提问',
    t1ab='在 Section 1 里，另一位说话人不停地确认——<em>sorry, forty-two?</em>'
         '——每一次确认都是一次免费的重复。独白里没人这样做，所以漏掉的细节通常'
         '就找不回来了。',
    t1an='所以这里的准备时间格外重要。',
    t1bh='地图题考方向感，也考英语',
    t1bb='给平面图标注，考的是有人用语言带你穿过一个地方时，你能不能保持方向'
         '感。词汇不多；难的是每样东西都是相对于别的东西来描述的。',
    t1bn='真实考试里你会拿到一张画好的、标着字母的平面图。这里改成把地点和位置'
         '配对——同样的工作，只是在字母之前一步。',
    t1ch='先确定你的起点',
    t1cb='在你知道大门在哪、自己面朝哪个方向之前，<em>On your left as you come '
         'through the gate</em> 毫无意义。录音开始前先在图上找到入口，并标出哪'
         '个方向是“正前方”。',
    t1cn='地图题上的很多分，都丢在从没弄清自己站在哪里的考生身上。',

    audEyebrow='录音',
    audTitle='你只能听一次',
    audNote='一位导游在一座公共花园里对一群游客讲话。先读后面几页的问题，再按播'
            '放——在这里，或在任何一页问题底部的播放条上。你作答时录音会继续播'
            '放，而且只播放一次。',

    matchEyebrow='问题 1&ndash;5 &middot; 布局',
    matchTitle='把每个地方放到导游说的位置',
    matchHint='先点一个地方，再点它的位置。一切都是相对于别的东西来描述的。',

    notesEyebrow='问题 6&ndash;8 &middot; 完成笔记',
    notesTitle='每个空填写一个单词和/或一个数字',
    notesHint='有两次，一句话里出现两个数字。填空里问的那一个。',

    t2Eyebrow='录音之后',
    t2Title='地图题怎样藏起答案',
    t2ah='共用的地标',
    t2ab='两样东西被放在同一个地标旁边——儿童游乐区<em>和</em>自行车停放架都在'
         '停车场旁边。说出地标并不能确定其中任何一个，所以必须把整句话记住。',
    t2an='<em>two things</em> 或 <em>in fact</em> 可能预示着第二样东西马上要共用'
         '同一个位置。',
    t2bh='挪了地方的东西',
    t2bb='某样东西先在旧位置被描述，然后被更正到新位置。植物摊 &ldquo;used to '
         'stand by the lake&rdquo;。按第一次提到的位置作答的人，会把它放错地'
         '方。',
    t2bn='导游是有意重复新位置的。在独白里，重复通常是一个信号。',
    t2ch='取决于你的方向',
    t2cb='<em>On your left</em>、<em>directly ahead</em>、<em>behind the '
         'lake</em>、<em>on the far side from where we are standing</em>。这些'
         '都是相对于说话人的位置，而不是相对于纸面。',
    t2cn='<em>Behind</em> 和 <em>beyond</em> 最容易让人上当：behind the lake '
         '是在湖的另一边，beyond the greenhouse 是过了温室再往前。',

    mcEyebrow='问题 9&ndash;12 &middot; 细节',
    mcTitle='导游到底说了什么？',

    m2why='溪岸正在维修。鸟提到了，春天也提到了，但都不是原因：春天是重新开放'
          '的时间。',
    m3why='不要喂鸟。导游给了理由——面包对鸟有害——而附在指令上的理由，常常标出'
          '说话人希望你记住的东西。',
    m4why='门票全天有效，所以游客可以留下。&ldquo;We finish back at the '
          'café&rdquo; 是前一句，说的是导览在哪里结束，不是什么时候必须离开。',
    m5why='逆时针，从旧玻璃房（现在的咖啡馆）出发——这是导游说的最后一句话。两'
          '半内容在同一句里，而干扰项正好在这里调换其中一半。',

    actTitle='带一次导览',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，每人一张简单的平面图——画出你们所在的房间，或你们'
                  '都熟悉的一栋楼。一人描述五样东西的位置，不能用手指，也不能'
                  '说东南西北。另一人在自己那份图上标出来，然后对照。',
    actSpeak1='描述的人：先大声确定起点：&ldquo;You come in through the door by '
              'the lifts.&rdquo; 之后一切都相对于这个起点。',
    actSpeak2='把你五样东西中的两样放在同一个地标旁边，看看同伴能不能把它们分'
              '开。',
    actSpeak3='说到一半，挪动一样东西：&ldquo;the printer used to be by the '
              'window &mdash; it is now&hellip;&rdquo; 新位置说两遍，就像录音'
              '里的导游那样。',
    actWriteKind='写作 · 100–150 词',
    actWriteBrief='写出带人参观一个你很熟悉的地方的头九十秒，说明五样东西在哪'
                  '里。完全不用东南西北——只用相对于入口和彼此的位置——并把其中'
                  '两样放在同一个地标旁边。',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='这些地方每一个都是相对于别的东西来描述的，这正是地图题的本质。儿'
              '童游乐区和自行车停放架共用一个地标——都在停车场旁边——所以在真实'
              '的平面图上，停放架也会有一个字母，光说 &ldquo;next to the car '
              'park&rdquo; 是确定不了它的。植物摊之所以被描述两次，正是因为它挪'
              '了地方。',
    n1why='十点到五点半。问的是关门时间，它在同一个短句里排在开门时间后面。',
    n2why='八英镑。同一句话接着说 &ldquo;no charge at all for anyone under '
          'sixteen&rdquo;，放在那里是为了让写 0 的人上当。',
    n3why='九十分钟。不是开放时间，也不是 &ldquo;all day&rdquo;——那是门票的有效'
          '时间，在下一句才说。',
)

# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Section 2 &mdash; <em>モノローグと地図</em>',
    coverSub='話し手は一人、質問できる相手はいない、そして頭の中に保たなければな'
             'らない見取り図',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 問',

    t1Eyebrow='聞く前に',
    t1Title='声は一つ、そしてほとんど何も二度は言われない',
    t1ah='誰も質問しない',
    t1ab='Section 1 では、もう一人の話し手が何度も確認します――<em>sorry, '
         'forty-two?</em>――そして確認のたびに、無料の繰り返しが手に入ります。モ'
         'ノローグではそれをする人がいないので、聞き逃した情報はたいてい戻ってき'
         'ません。',
    t1an='だからこそ、ここでは準備時間がとても大切です。',
    t1bh='地図問題は英語と同じくらい、方向感覚を試します',
    t1bb='見取り図に記入する問題は、誰かが言葉であなたをある場所の中へ案内する'
         '間、向きを保っていられるかを試します。語彙は少ないのですが、難しいの'
         'は、すべてが何か別のものを基準に説明されることです。',
    t1bn='本番では、文字が書き込まれた見取り図が配られます。ここでは代わりに場'
         '所と位置を組み合わせます――同じ作業を、文字の一歩手前で行うのです。',
    t1ch='まず自分の出発点を決める',
    t1cb='門がどこにあり、自分がどちらを向いているかがわかるまで、<em>On your '
         'left as you come through the gate</em> は何の意味もありません。録音が'
         '始まる前に見取り図で入口を見つけ、どちらが「正面」かに印をつけましょ'
         'う。',
    t1cn='地図問題の点の多くは、自分がどこに立っているかを確かめなかった受験者'
         'が失っています。',

    audEyebrow='録音',
    audTitle='聞けるのは一度だけ',
    audNote='公共の庭園で、ガイドが見学者のグループに話しています。まず次のスラ'
            'イドの問題を読み、それから再生を押しましょう――ここでも、どの問題ス'
            'ライドの下のバーでもかまいません。答えている間も録音は流れ続け、聞'
            'けるのは一度だけです。',

    matchEyebrow='問題 1&ndash;5 &middot; 配置',
    matchTitle='ガイドが言った位置に、それぞれの場所を置きましょう',
    matchHint='場所をクリックし、次にその位置をクリックします。すべてが何か別の'
              'ものを基準に説明されています。',

    notesEyebrow='問題 6&ndash;8 &middot; メモを完成させる',
    notesTitle='各空欄に「1語および／または数字1つ」を書きましょう',
    notesHint='一つの文に数字が二つ出てくることが二回あります。空欄が求めている'
              '方を書きましょう。',

    t2Eyebrow='録音の後で',
    t2Title='地図問題はどうやって答えを隠すか',
    t2ah='共有された目印',
    t2ab='二つのものが同じ目印の横に置かれます――子どもの遊び場<em>と</em>自転'
         '車置き場は、どちらも駐車場の隣です。目印を言っても、どちらなのかは決'
         'まりません。だから文全体を覚えておく必要があります。',
    t2an='<em>two things</em> や <em>in fact</em> は、二つ目のものが同じ位置を共'
         '有することの合図になりえます。',
    t2bh='移動したもの',
    t2bb='何かが古い場所で説明され、それから新しい場所に訂正されます。植物の売'
         '店は &ldquo;used to stand by the lake&rdquo;。最初に言われた場所で答え'
         'る人は、間違った場所に置いてしまいます。',
    t2bn='ガイドは新しい位置をわざと繰り返しています。モノローグでは、繰り返し'
         'はたいてい合図です。',
    t2ch='あなたの位置で決まる方向',
    t2cb='<em>On your left</em>、<em>directly ahead</em>、<em>behind the '
         'lake</em>、<em>on the far side from where we are standing</em>。これら'
         'はどれも、紙面ではなく、話し手の位置を基準にしています。',
    t2cn='<em>Behind</em> と <em>beyond</em> は、多くの人がつまずく二語です：'
         'behind the lake は湖の向こう側、beyond the greenhouse は温室を過ぎた先'
         'です。',

    mcEyebrow='問題 9&ndash;12 &middot; 詳細',
    mcTitle='ガイドは正確には何と言ったか？',

    m2why='小川の土手が修理中だからです。鳥も春も出てきますが、どちらも理由では'
          'ありません。春は再開する時期です。',
    m3why='鳥にえさをやらないこと。ガイドは理由を添えています――パンは鳥の体に悪'
          'い――そして指示に添えられた理由は、話し手が覚えておいてほしいことの目'
          '印になることがよくあります。',
    m4why='チケットは一日中有効なので、見学者は残ってかまいません。&ldquo;We '
          'finish back at the café&rdquo; はその前の一文で、ツアーが終わる場所'
          'の話であり、いつ帰らなければならないかの話ではありません。',
    m5why='反時計回りに、古いガラスハウス（今のカフェ）から――ガイドが最後に言う'
          'ことです。二つの要素が一つの文に入っているので、まさにそこで引っかけの'
          '選択肢が片方を入れ替えるのです。',

    actTitle='ツアーを案内する',
    actUse='三つ以上：',
    actSpeakBrief='ペアで、それぞれ簡単な見取り図を一枚持ちます――今いる部屋か、'
                  '二人とも知っている建物を描きましょう。一人が五つのものの位置'
                  'を、指さしをせず、東西南北も使わずに説明します。もう一人は自'
                  '分の図に印をつけ、最後に見比べます。',
    actSpeak1='説明する人：まず出発点を声に出して決めましょう。&ldquo;You come '
              'in through the door by the lifts.&rdquo; それ以降は、すべてそこ'
              'を基準にします。',
    actSpeak2='五つのうち二つを同じ目印の横に置き、パートナーが区別できるか見て'
              'みましょう。',
    actSpeak3='途中で一つを動かしましょう：&ldquo;the printer used to be by the '
              'window &mdash; it is now&hellip;&rdquo; 新しい場所は、録音のガイ'
              'ドのように二回言いましょう。',
    actWriteKind='ライティング · 100–150 語',
    actWriteBrief='よく知っている場所のツアーの最初の90秒を書き、五つのものの位'
                  '置を説明しましょう。東西南北は使わず、入口と互いの位置関係だ'
                  'けで。そのうち二つは同じ目印の横に。',
    actPlaceholder='As you come through the main door, on your left…',

    placesWhy='これらの場所はどれも、何か別のものを基準に説明されています。それ'
              'こそが地図問題です。子どもの遊び場は自転車置き場と目印を共有して'
              'います――どちらも駐車場の隣――ので、自転車置き場にも文字がつく本'
              '物の見取り図なら、&ldquo;next to the car park&rdquo; だけでは特定'
              'できません。植物の売店が二度説明されるのは、まさに移動したからで'
              'す。',
    n1why='10時から5時半まで。聞かれているのは閉園時刻で、開園時刻と同じ短い文'
          'の中で二番目に出てきます。',
    n2why='8ポンド。同じ文は &ldquo;no charge at all for anyone under '
          'sixteen&rdquo; と続き、それは0と書く人を引っかけるためにあります。',
    n3why='90分。開園時間でも &ldquo;all day&rdquo; でもありません――それはチケッ'
          'トの有効期間で、一行後に言われます。',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
