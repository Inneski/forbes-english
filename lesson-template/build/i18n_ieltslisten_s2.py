# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 2.

English, German and Spanish, teach cards in the six-item form.

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
    actSpeak1='Beschreiber: leg zuerst laut den Ausgangspunkt fest. „Du kommst '
              'durch die Tür bei den Aufzügen herein.“ Danach ist alles '
              'relativ dazu.',
    actSpeak2='Setz zwei deiner fünf Dinge neben denselben Orientierungspunkt '
              'und schau, ob dein Partner sie auseinanderhält.',
    actSpeak3='Verschieb auf halber Strecke ein Ding: „der Drucker stand '
              'früher am Fenster &mdash; jetzt ist er&hellip;“ Sag den neuen '
              'Ort zweimal, wie die Führerin in der Aufnahme.',
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
    actSpeak1='Quien describe: fija en voz alta el punto de partida. «Entras '
              'por la puerta que está junto a los ascensores.» A partir de ahí '
              'todo es relativo a eso.',
    actSpeak2='Pon dos de tus cinco cosas junto a la misma referencia y mira '
              'si tu compañero las separa.',
    actSpeak3='A mitad de camino, mueve una cosa: «la impresora estaba junto a '
              'la ventana… ahora está…». Di el sitio nuevo dos veces, como '
              'hace la guía de la grabación.',
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
