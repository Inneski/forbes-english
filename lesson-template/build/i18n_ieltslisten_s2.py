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
    t1Title='One voice, and no second chance at anything',
    t1ah='Nobody asks a question',
    t1ab='In Section 1 the other speaker keeps checking &mdash; <em>sorry, '
         'forty-two?</em> &mdash; and every check is a free repeat. A '
         'monologue never does that. A detail you miss is simply gone.',
    t1an='Which is why the preparation time matters more here than anywhere '
         'else on the paper.',
    t1bh='The map task is not about English',
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
    t1cn='Half the marks on a map task are lost by candidates who never '
         'established where they were standing.',

    audEyebrow='The recording',
    audTitle='You will hear it once',
    audNote='A guide talking to a group of visitors at a public garden. Press '
            'play when you are ready. There is no pause and no rewind, exactly '
            'as in the test.',

    matchEyebrow='Questions 1&ndash;5 &middot; The layout',
    matchTitle='Put each place where the guide put it',
    matchHint='Click a place, then its position. Everything is given relative '
              'to something else.',

    notesEyebrow='Questions 6&ndash;8 &middot; Complete the notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='Two numbers arrive in the same sentence more than once. Write '
              'the one the gap asks for.',

    t2Eyebrow='After the recording',
    t2Title='How a map task hides its answers',
    t2ah='The shared landmark',
    t2ab='Two things are put beside the same feature &mdash; the play area '
         '<em>and</em> the bicycle racks are both next to the car park. '
         'Naming the landmark does not identify either of them, so the '
         'sentence has to be held whole.',
    t2an='Whenever a speaker says <em>two things</em> or <em>in fact</em>, a '
         'second item is about to share a position.',
    t2bh='The thing that moved',
    t2bb='Something is described in its old place and then corrected to its '
         'new one. The plant stall "used to stand by the lake". Anyone '
         'answering from the first mention puts it in the wrong place.',
    t2bn='He repeats the new position deliberately. A repeat in a monologue is '
         'never decoration.',
    t2ch='The direction that depends on you',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. '
         'Every one of these is relative to the speaker&rsquo;s position, not '
         'to the page.',
    t2cn='<em>Behind</em> and <em>beyond</em> are the two that catch people: '
         'behind the lake is across it, beyond the greenhouse is past it.',

    mcEyebrow='Questions 9&ndash;12 &middot; Detail',
    mcTitle='What exactly did the guide say?',

    m1why='The glasshouse was the ticket office and is now the café. Both '
          'facts are in one sentence and the order is what decides the '
          'answer &mdash; which is the sentence the distractor simply '
          'reverses.',
    m2why='The bank of the stream is being repaired. The birds are mentioned, '
          'and so is the spring, but neither is the reason: the spring is when '
          'it reopens.',
    m3why='Do not feed the birds. He gives a reason &mdash; bread is bad for '
          'them &mdash; and a reason attached to an instruction is how a '
          'monologue marks the thing it wants you to remember.',
    m4why='The ticket lasts all day, so visitors may stay. "We finish back at '
          'the café" is the line before, and it is about where the tour ends, '
          'not when you have to leave.',

    actTitle='Give the tour',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with a simple plan each &mdash; draw the room you '
                  'are in, or a building you both know. One of you describes '
                  'where five things are, without pointing and without naming '
                  'a compass direction. The other marks them on their own copy '
                  'and then compares.',
    actSpeak1='Describer: fix the starting point out loud first. "You come in '
              'through the door on the north side." Then everything is '
              'relative to that.',
    actSpeak2='Put two of your five things beside the same landmark, and see '
              'whether your partner separates them.',
    actSpeak3='Move one thing halfway through: "the printer used to be by the '
              'window &mdash; it is now&hellip;" Say the new place twice, as a '
              'real guide does.',
    actWriteKind='Writing · 100–150 words',
    actWriteBrief='Write the opening ninety seconds of a tour of somewhere you '
                  'know well, describing where five things are. Use no '
                  'compass directions at all &mdash; only positions relative '
                  'to the entrance and to each other &mdash; and put two of '
                  'them beside the same landmark.',
    actPlaceholder='As you come through the main door, on your left…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 2 &mdash; <em>der Monolog und der Plan</em>',
    coverSub='Eine Stimme, niemand zum Nachfragen, und ein Plan, den du im '
             'Kopf behalten musst',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 Fragen',

    t1Eyebrow='Bevor du hörst',
    t1Title='Eine Stimme &mdash; und nirgends eine zweite Chance',
    t1ah='Niemand stellt eine Rückfrage',
    t1ab='In Section 1 hakt die zweite Person ständig nach &mdash; <em>sorry, '
         'forty-two?</em> &mdash; und jede Rückfrage ist eine geschenkte '
         'Wiederholung. Ein Monolog tut das nie. Was du verpasst, ist weg.',
    t1an='Genau deshalb zählt die Vorbereitungszeit hier mehr als sonst wo in '
         'der Prüfung.',
    t1bh='Die Kartenaufgabe prüft kein Englisch',
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
    t1cn='Die Hälfte der Punkte einer Kartenaufgabe verlieren Kandidaten, die '
         'nie festgelegt haben, wo sie stehen.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal',
    audNote='Eine Führerin spricht zu einer Besuchergruppe in einem '
            'öffentlichen Garten. Drücke Play, wenn du bereit bist. Kein '
            'Pausieren, kein Zurückspulen &mdash; genau wie in der Prüfung.',

    matchEyebrow='Fragen 1&ndash;5 &middot; Die Anlage',
    matchTitle='Ordne jeden Ort dorthin, wo die Führerin ihn hingesetzt hat',
    matchHint='Klicke einen Ort an, dann seine Position. Alles ist relativ zu '
              'etwas anderem angegeben.',

    notesEyebrow='Fragen 6&ndash;8 &middot; Notizen vervollständigen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Mehrfach stehen zwei Zahlen im selben Satz. Schreib die, nach '
              'der die Lücke fragt.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Wie eine Kartenaufgabe ihre Antworten versteckt',
    t2ah='Der geteilte Orientierungspunkt',
    t2ab='Zwei Dinge werden neben dasselbe Merkmal gesetzt &mdash; der '
         'Spielplatz <em>und</em> die Fahrradständer stehen beide neben dem '
         'Parkplatz. Den Orientierungspunkt zu nennen identifiziert keines '
         'von beiden; der Satz muss ganz behalten werden.',
    t2an='Wenn jemand <em>two things</em> oder <em>in fact</em> sagt, teilt '
         'gleich ein zweites Ding dieselbe Position.',
    t2bh='Das, was umgezogen ist',
    t2bb='Etwas wird an seinem alten Ort beschrieben und dann an den neuen '
         'korrigiert. Der Pflanzenstand „used to stand by the lake“. Wer nach '
         'der ersten Nennung antwortet, setzt ihn falsch.',
    t2bn='Sie wiederholt die neue Position absichtlich. Eine Wiederholung im '
         'Monolog ist nie Dekoration.',
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

    m1why='Das Glashaus war das Kartenhäuschen und ist jetzt das Café. Beides '
          'steht in einem Satz, und die Reihenfolge entscheidet &mdash; genau '
          'den Satz dreht der Ablenker um.',
    m2why='Das Ufer des Bachs wird repariert. Die Vögel kommen vor und der '
          'Frühling auch, aber keins ist der Grund: im Frühling wird wieder '
          'geöffnet.',
    m3why='Die Vögel nicht füttern. Sie nennt einen Grund &mdash; Brot ist '
          'schlecht für sie &mdash; und ein Grund an einer Anweisung ist im '
          'Monolog die Markierung für das, was man behalten soll.',
    m4why='Das Ticket gilt den ganzen Tag, also darf man bleiben. „We finish '
          'back at the café“ steht davor und sagt, wo die Führung endet, nicht '
          'wann man gehen muss.',

    actTitle='Führt eine Gruppe',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, jeder mit einem einfachen Plan &mdash; zeichne '
                  'den Raum, in dem ihr seid, oder ein Gebäude, das ihr beide '
                  'kennt. Einer beschreibt, wo fünf Dinge sind, ohne zu zeigen '
                  'und ohne Himmelsrichtungen. Der andere trägt sie ein und '
                  'vergleicht.',
    actSpeak1='Beschreiber: leg zuerst laut den Ausgangspunkt fest. „Du kommst '
              'durch die Tür an der Nordseite herein.“ Danach ist alles '
              'relativ dazu.',
    actSpeak2='Setz zwei deiner fünf Dinge neben denselben Orientierungspunkt '
              'und schau, ob dein Partner sie auseinanderhält.',
    actSpeak3='Verschieb auf halber Strecke ein Ding: „der Drucker stand '
              'früher am Fenster &mdash; jetzt ist er&hellip;“ Sag den neuen '
              'Ort zweimal, wie eine echte Führung es tut.',
    actWriteKind='Schreiben · 100–150 Wörter',
    actWriteBrief='Schreib die ersten neunzig Sekunden einer Führung durch '
                  'einen Ort, den du gut kennst, und beschreibe, wo fünf Dinge '
                  'sind. Ohne jede Himmelsrichtung &mdash; nur relativ zum '
                  'Eingang und zueinander &mdash; und setz zwei davon neben '
                  'denselben Orientierungspunkt.',
    actPlaceholder='As you come through the main door, on your left…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 2 &mdash; <em>el monólogo y el plano</em>',
    coverSub='Una sola voz, nadie a quien preguntar y un plano que tienes que '
             'sostener en la cabeza',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 2',
    chipCount='12 preguntas',

    t1Eyebrow='Antes de escuchar',
    t1Title='Una voz, y ninguna segunda oportunidad',
    t1ah='Nadie pregunta nada',
    t1ab='En la Section 1 la otra persona va comprobando &mdash; <em>sorry, '
         'forty-two?</em> &mdash; y cada comprobación es una repetición '
         'gratis. Un monólogo no hace eso. Lo que se te escapa, se fue.',
    t1an='Por eso el tiempo de preparación cuenta aquí más que en ninguna otra '
         'parte del examen.',
    t1bh='La tarea del plano no va de inglés',
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
    t1cn='La mitad de los puntos de un plano los pierde quien nunca fijó dónde '
         'estaba de pie.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez',
    audNote='Una guía hablando a un grupo de visitantes en un jardín público. '
            'Dale a reproducir cuando estés listo. Sin pausa y sin rebobinar, '
            'igual que en el examen.',

    matchEyebrow='Preguntas 1&ndash;5 &middot; La distribución',
    matchTitle='Coloca cada sitio donde lo colocó la guía',
    matchHint='Haz clic en un sitio y luego en su posición. Todo se da en '
              'relación con otra cosa.',

    notesEyebrow='Preguntas 6&ndash;8 &middot; Completa las notas',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Más de una vez hay dos números en la misma frase. Escribe el '
              'que pide el hueco.',

    t2Eyebrow='Después de la grabación',
    t2Title='Cómo esconde sus respuestas una tarea de plano',
    t2ah='La referencia compartida',
    t2ab='Dos cosas se colocan junto al mismo elemento: la zona de juegos '
         '<em>y</em> el aparcabicis están las dos al lado del aparcamiento. '
         'Nombrar la referencia no identifica ninguna, así que hay que '
         'quedarse con la frase entera.',
    t2an='Cuando alguien dice <em>two things</em> o <em>in fact</em>, un '
         'segundo elemento va a compartir posición.',
    t2bh='Lo que se ha movido',
    t2bb='Algo se describe en su sitio antiguo y luego se corrige al nuevo. El '
         'puesto de plantas «used to stand by the lake». Quien responde por la '
         'primera mención lo coloca mal.',
    t2bn='Repite la posición nueva a propósito. Una repetición en un monólogo '
         'nunca es decoración.',
    t2ch='La dirección que depende de ti',
    t2cb='<em>On your left</em>, <em>directly ahead</em>, <em>behind the '
         'lake</em>, <em>on the far side from where we are standing</em>. Todo '
         'eso es relativo a dónde está la persona que habla, no al papel.',
    t2cn='<em>Behind</em> y <em>beyond</em> son las dos que pillan a la gente: '
         'behind the lake es al otro lado, beyond the greenhouse es pasado el '
         'invernadero.',

    mcEyebrow='Preguntas 9&ndash;12 &middot; Detalle',
    mcTitle='¿Qué dijo exactamente la guía?',

    m1why='El invernadero era la taquilla y ahora es la cafetería. Los dos '
          'datos van en una frase y el orden es lo que decide: justo la frase '
          'que el distractor da la vuelta.',
    m2why='Están reparando la orilla del arroyo. Los pájaros salen, y la '
          'primavera también, pero ninguno es el motivo: en primavera se '
          'vuelve a abrir.',
    m3why='No dar de comer a los pájaros. Da un motivo &mdash; el pan les '
          'sienta mal &mdash; y un motivo pegado a una instrucción es como un '
          'monólogo marca lo que quiere que recuerdes.',
    m4why='La entrada vale todo el día, así que pueden quedarse. «We finish '
          'back at the café» es la línea anterior y dice dónde acaba la '
          'visita, no cuándo hay que irse.',

    actTitle='Haz de guía',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con un plano sencillo cada uno: dibujad la sala '
                  'en la que estáis, o un edificio que conozcáis los dos. Uno '
                  'describe dónde están cinco cosas, sin señalar y sin usar '
                  'puntos cardinales. El otro las marca en su copia y luego '
                  'comparáis.',
    actSpeak1='Quien describe: fija en voz alta el punto de partida. «Entras '
              'por la puerta del lado norte.» A partir de ahí todo es relativo '
              'a eso.',
    actSpeak2='Pon dos de tus cinco cosas junto a la misma referencia y mira '
              'si tu compañero las separa.',
    actSpeak3='A mitad de camino, mueve una cosa: «la impresora estaba junto a '
              'la ventana… ahora está…». Di el sitio nuevo dos veces, como '
              'hace una guía de verdad.',
    actWriteKind='Escritura · 100–150 palabras',
    actWriteBrief='Escribe los primeros noventa segundos de una visita guiada '
                  'a un sitio que conozcas bien, diciendo dónde están cinco '
                  'cosas. Sin ningún punto cardinal &mdash; solo posiciones '
                  'relativas a la entrada y entre sí &mdash; y pon dos de '
                  'ellas junto a la misma referencia.',
    actPlaceholder='As you come through the main door, on your left…',
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
