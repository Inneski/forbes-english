# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 1.

English, German and Spanish, teach cards in the six-item form.

The usual split (HOUSE-STYLE §8) with one addition that matters on a Listening
deck: the answers themselves — NOVAKOVA, Thursday, the phone number — are what
the learner writes into the form, and they are never translated anywhere,
because the task is transcribing English from English speech. What translates
is the rule around it, and the reason each trap works.
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
    coverTitle='Section 1 &mdash; <em>the everyday conversation</em>',
    coverSub='Two speakers, one form to fill in, and a recording that plays '
             'exactly once',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 questions',

    t1Eyebrow='Before you listen',
    t1Title='The easiest section, and the one people throw marks away on',
    t1ah='What Section 1 always is',
    t1ab='Two speakers, an everyday situation, and a form or a set of notes to '
         'complete. Enrolling, booking, reporting something lost. It is the '
         'gentlest English on the paper.',
    t1an='Which is why a lost mark here costs the same as a lost mark in the '
         'lecture, and hurts more.',
    t1bh='It tests writing, not understanding',
    t1bb='You will understand nearly every word. The marks go on whether you '
         'can write a spelled surname, a phone number and a price down '
         'accurately while someone keeps talking.',
    t1bn='Spelling counts. A correctly heard word spelt wrong scores nothing.',
    t1ch='Read the form first',
    t1cb='You get time before the recording starts. Use it to see what KIND of '
         'answer each gap wants &mdash; a day, a number, a name &mdash; so you '
         'are waiting for the right thing instead of listening to everything.',
    t1cn='A gap after "£" wants a number. You can know that before you hear a '
         'word.',

    audEyebrow='The recording',
    audTitle='You will hear it once',
    audNote='A telephone conversation between a woman and the manager of a '
            'community sports centre. Read the questions on the next slides '
            'first, then press play &mdash; here, or in the bar at the foot of '
            'any question slide. The recording keeps playing while you answer, '
            'and you hear it once.',

    gapEyebrow='Questions 1&ndash;7 &middot; Complete the form',
    gapTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    gapHint='Spelling is marked. Write what you actually heard, not what you '
            'expected to hear.',

    t2Eyebrow='After the recording',
    t2Title='The four places this section takes its marks',
    t2ah='The correction',
    t2ab='A speaker says one thing and immediately changes it &mdash; '
         '<em>Tuesday&hellip; sorry, that&rsquo;s the children, the adult class is '
         'Thursday</em>. The answer is always the second one. This is the '
         'commonest mistake on the whole section.',
    t2an='Listen for <em>sorry</em>, <em>actually</em>, <em>I mean</em>, <em>I '
         'beg your pardon</em>. Every one of them is a warning that the answer '
         'is about to change.',
    t2bh='The spelled word',
    t2bb='When a speaker starts giving letters, an answer is being dictated. '
         'In Section 1 it usually happens once, and it is never repeated more '
         'than the speakers would naturally repeat it.',
    t2bn='Know the letters that sound alike in English: A, E and I; G and J; '
         'M and N.',
    t2ch='The number and the distractor',
    t2cb='British speakers say <em>double oh</em> for two noughts and '
         '<em>oh</em> for one. And there are nearly always two prices or two '
         'times &mdash; one of them labelled as the wrong one, quickly.',
    t2cn='Thirty-five was the monthly rate for non-members. She was joining, '
         'so the answer was forty-two.',

    mcEyebrow='Questions 8&ndash;10 &middot; Detail',
    mcTitle='What exactly did they say?',

    l1why='The small pool, side entrance. He gives both in one breath &mdash; '
          '"the classes are in the small pool, not the main one, so come '
          'through the side entrance" &mdash; and the two halves get swapped '
          'by anyone answering from memory rather than from the line.',
    l2why='The street behind the library is free after five. The car park is '
          'real, but he says it fills up by six; "free after five" attaches to '
          'the street, not the car park.',
    l4why='The building was refurbished. The friend and the local paper are '
          'both mentioned in her last question, one line earlier, which is '
          'exactly why they are there.',

    actTitle='Take the call',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with a form each. One of you is the receptionist '
                  'at a centre, a hotel or a garage; the other is enquiring. '
                  'The receptionist must spell one name, give one phone '
                  'number, and correct themselves once. The caller fills in '
                  'the form and then reads it back.',
    actSpeak1='Speller: give the surname once, at speaking speed. Do not slow '
              'down and do not repeat it unless you are asked.',
    actSpeak2='Caller: read the whole form back at the end. Every wrong letter '
              'is a mark, so say the letters, not the word.',
    actSpeak3='Somewhere in the call, change one detail after you have already '
              'given it. See whether your partner catches it.',
    actWriteKind='Writing · 100–150 words',
    actWriteBrief='Write the six lines of a form for a booking of your own '
                  'choosing &mdash; a course, a delivery, a repair &mdash; and '
                  'beside each one write what KIND of answer it needs: a name, '
                  'a day, a number, a price. That is the thirty seconds of '
                  'preparation the test gives you, done in advance.',
    actPlaceholder='Surname: … (a name, spelled)',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 1 &mdash; <em>das Alltagsgespräch</em>',
    coverSub='Zwei Sprecher, ein Formular und eine Aufnahme, die genau einmal '
             'läuft',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 Fragen',

    t1Eyebrow='Bevor du hörst',
    t1Title='Der leichteste Teil &mdash; und der, in dem Punkte verschenkt werden',
    t1ah='Was Section 1 immer ist',
    t1ab='Zwei Sprecher, eine Alltagssituation und ein Formular oder Notizen '
         'zum Ausfüllen. Anmelden, buchen, etwas als verloren melden. Das '
         'einfachste Englisch der ganzen Prüfung.',
    t1an='Genau deshalb kostet ein Fehler hier so viel wie einer in der '
         'Vorlesung &mdash; und ärgert mehr.',
    t1bh='Geprüft wird Schreiben, nicht Verstehen',
    t1bb='Du wirst fast jedes Wort verstehen. Die Punkte hängen daran, ob du '
         'einen buchstabierten Nachnamen, eine Telefonnummer und einen Preis '
         'korrekt mitschreibst, während weitergesprochen wird.',
    t1bn='Rechtschreibung zählt. Ein richtig gehörtes, falsch geschriebenes '
         'Wort bringt null.',
    t1ch='Lies zuerst das Formular',
    t1cb='Vor der Aufnahme bekommst du Zeit. Nutze sie, um zu sehen, welche '
         'ART von Antwort jede Lücke will &mdash; ein Tag, eine Zahl, ein Name '
         '&mdash; damit du auf das Richtige wartest, statt auf alles zu hören.',
    t1cn='Eine Lücke nach „£“ will eine Zahl. Das weißt du, bevor ein Wort '
         'gefallen ist.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal',
    audNote='Ein Telefongespräch zwischen einer Frau und dem Leiter eines '
            'Gemeindesportzentrums. Lies zuerst die Fragen auf den nächsten '
            'Folien, dann drücke Play &mdash; hier oder in der Leiste unten auf '
            'jeder Fragenfolie. Die Aufnahme läuft weiter, während du '
            'antwortest, und du hörst sie einmal.',

    gapEyebrow='Fragen 1&ndash;7 &middot; Formular ausfüllen',
    gapTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    gapHint='Rechtschreibung wird bewertet. Schreib, was du gehört hast, nicht '
            'was du erwartet hast.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Die vier Stellen, an denen dieser Teil die Punkte holt',
    t2ah='Die Korrektur',
    t2ab='Jemand sagt etwas und ändert es sofort &mdash; <em>Tuesday&hellip; '
         'sorry, that&rsquo;s the children, the adult class is Thursday</em>. Die '
         'Antwort ist immer die zweite. Der häufigste Fehler im ganzen Teil.',
    t2an='Achte auf <em>sorry</em>, <em>actually</em>, <em>I mean</em>, <em>I '
         'beg your pardon</em>. Jedes davon kündigt an, dass die Antwort sich '
         'gleich ändert.',
    t2bh='Das buchstabierte Wort',
    t2bb='Sobald jemand Buchstaben nennt, wird eine Antwort diktiert. In '
         'Section 1 passiert das meist einmal, und es wird nicht öfter '
         'wiederholt, als zwei Menschen es natürlich täten.',
    t2bn='Kenne die Buchstaben, die im Englischen ähnlich klingen: A, E und I; '
         'G und J; M und N.',
    t2ch='Die Zahl und der Ablenker',
    t2cb='Briten sagen <em>double oh</em> für zwei Nullen und <em>oh</em> für '
         'eine. Und fast immer gibt es zwei Preise oder zwei Uhrzeiten &mdash; '
         'einer davon wird kurz als der falsche markiert.',
    t2cn='Fünfunddreißig war der Monatspreis für Nichtmitglieder. Sie tritt '
         'bei, also lautet die Antwort zweiundvierzig.',

    mcEyebrow='Fragen 8&ndash;10 &middot; Detail',
    mcTitle='Was genau wurde gesagt?',

    l1why='Der kleine Pool, Seiteneingang. Er nennt beides in einem Atemzug '
          '&mdash; „the classes are in the small pool, not the main one, so '
          'come through the side entrance“ &mdash; und wer aus dem Gedächtnis '
          'antwortet, vertauscht die beiden Hälften.',
    l2why='Die Straße hinter der Bibliothek ist ab fünf frei. Den Parkplatz '
          'gibt es, aber er ist ab sechs voll; „free after five“ gehört zur '
          'Straße, nicht zum Parkplatz.',
    l4why='Das Gebäude wurde saniert. Die Empfehlung und die Lokalzeitung '
          'kommen beide in ihrer letzten Frage vor, eine Zeile davor, und genau '
          'deshalb stehen sie dort.',

    actTitle='Nimm den Anruf an',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, jeder mit einem Formular. Einer ist an der '
                  'Rezeption eines Zentrums, Hotels oder einer Werkstatt, der '
                  'andere fragt an. Die Rezeption muss einen Namen '
                  'buchstabieren, eine Telefonnummer nennen und sich einmal '
                  'korrigieren. Der Anrufer füllt aus und liest zurück.',
    actSpeak1='Buchstabierer: nenne den Nachnamen einmal, in normalem Tempo. '
              'Nicht langsamer werden und nicht wiederholen, außer man fragt.',
    actSpeak2='Anrufer: lies am Ende das ganze Formular zurück. Jeder falsche '
              'Buchstabe ist ein Punkt &mdash; also nenne die Buchstaben, '
              'nicht das Wort.',
    actSpeak3='Ändere irgendwo im Gespräch ein Detail, das du schon genannt '
              'hast. Schau, ob dein Partner es mitbekommt.',
    actWriteKind='Schreiben · 100–150 Wörter',
    actWriteBrief='Schreib die sechs Zeilen eines Formulars für eine Buchung '
                  'deiner Wahl &mdash; Kurs, Lieferung, Reparatur &mdash; und '
                  'daneben, welche ART von Antwort jede Zeile braucht: Name, '
                  'Tag, Zahl, Preis. Das sind die dreißig Sekunden Vorbereitung '
                  'der Prüfung, vorab erledigt.',
    actPlaceholder='Surname: … (a name, spelled)',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 1 &mdash; <em>la conversación cotidiana</em>',
    coverSub='Dos hablantes, un formulario que rellenar y una grabación que '
             'suena exactamente una vez',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 preguntas',

    t1Eyebrow='Antes de escuchar',
    t1Title='La parte más fácil, y en la que se regalan puntos',
    t1ah='Qué es siempre la Section 1',
    t1ab='Dos hablantes, una situación cotidiana y un formulario o unas notas '
         'que completar. Matricularse, reservar, denunciar una pérdida. El '
         'inglés más sencillo de todo el examen.',
    t1an='Justo por eso un punto perdido aquí cuesta lo mismo que uno perdido '
         'en la conferencia, y duele más.',
    t1bh='Examina escribir, no entender',
    t1bb='Vas a entender casi todas las palabras. Los puntos dependen de si '
         'sabes anotar con exactitud un apellido deletreado, un número de '
         'teléfono y un precio mientras el otro sigue hablando.',
    t1bn='La ortografía cuenta. Una palabra bien oída y mal escrita no puntúa.',
    t1ch='Lee primero el formulario',
    t1cb='Te dan tiempo antes de la grabación. Úsalo para ver qué TIPO de '
         'respuesta pide cada hueco &mdash; un día, un número, un nombre '
         '&mdash; y así esperar lo correcto en vez de escucharlo todo.',
    t1cn='Un hueco detrás de «£» pide un número. Eso lo sabes antes de oír una '
         'sola palabra.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez',
    audNote='Una conversación telefónica entre una mujer y el responsable de '
            'un centro deportivo municipal. Lee primero las preguntas de las '
            'diapositivas siguientes y luego dale a reproducir, aquí o en la '
            'barra de abajo de cualquier pregunta. La grabación sigue sonando '
            'mientras respondes, y la oyes una sola vez.',

    gapEyebrow='Preguntas 1&ndash;7 &middot; Completa el formulario',
    gapTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    gapHint='Se corrige la ortografía. Escribe lo que has oído, no lo que '
            'esperabas oír.',

    t2Eyebrow='Después de la grabación',
    t2Title='Los cuatro sitios donde esta parte se lleva los puntos',
    t2ah='La corrección',
    t2ab='Alguien dice una cosa y la cambia enseguida: <em>Tuesday&hellip; '
         'sorry, that&rsquo;s the children, the adult class is Thursday</em>. La '
         'respuesta es siempre la segunda. Es el fallo más común de toda la '
         'sección.',
    t2an='Escucha <em>sorry</em>, <em>actually</em>, <em>I mean</em>, <em>I beg '
         'your pardon</em>. Cada uno avisa de que la respuesta va a cambiar.',
    t2bh='La palabra deletreada',
    t2bb='En cuanto alguien empieza a dar letras, se está dictando una '
         'respuesta. En la Section 1 suele pasar una vez, y no se repite más de '
         'lo que dos personas lo repetirían de forma natural.',
    t2bn='Aprende las letras que suenan parecido en inglés: A, E e I; G y J; M '
         'y N.',
    t2ch='El número y el distractor',
    t2cb='Los británicos dicen <em>double oh</em> para dos ceros y <em>oh</em> '
         'para uno. Y casi siempre hay dos precios o dos horas, con uno '
         'marcado de pasada como el que no vale.',
    t2cn='Treinta y cinco era la tarifa mensual de no socios. Ella se hace '
         'socia, así que la respuesta es cuarenta y dos.',

    mcEyebrow='Preguntas 8&ndash;10 &middot; Detalle',
    mcTitle='¿Qué dijeron exactamente?',

    l1why='La piscina pequeña, entrada lateral. Lo dice todo de una vez '
          '&mdash; «the classes are in the small pool, not the main one, so '
          'come through the side entrance» &mdash; y quien responde de memoria '
          'intercambia las dos mitades.',
    l2why='La calle de detrás de la biblioteca es gratis a partir de las '
          'cinco. El aparcamiento existe, pero dice que se llena a las seis; '
          '«free after five» va con la calle, no con el aparcamiento.',
    l4why='El edificio se reformó. La amiga y el periódico local aparecen los '
          'dos en su última pregunta, una línea antes, y por eso están ahí.',

    actTitle='Atiende la llamada',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con un formulario cada uno. Uno atiende la '
                  'recepción de un centro, un hotel o un taller; el otro '
                  'pregunta. Recepción tiene que deletrear un nombre, dar un '
                  'número de teléfono y corregirse una vez. Quien llama '
                  'rellena el formulario y luego lo lee en voz alta.',
    actSpeak1='Quien deletrea: da el apellido una sola vez, a velocidad '
              'normal. Sin frenar y sin repetirlo salvo que te lo pidan.',
    actSpeak2='Quien llama: lee al final el formulario entero. Cada letra mal '
              'es un punto, así que di las letras, no la palabra.',
    actSpeak3='En algún momento de la llamada, cambia un dato que ya habías '
              'dado. A ver si tu compañero lo pilla.',
    actWriteKind='Escritura · 100–150 palabras',
    actWriteBrief='Escribe las seis líneas de un formulario para una reserva '
                  'que elijas &mdash; un curso, un envío, una reparación '
                  '&mdash; y al lado de cada una, qué TIPO de respuesta pide: '
                  'un nombre, un día, un número, un precio. Son los treinta '
                  'segundos de preparación del examen, hechos por adelantado.',
    actPlaceholder='Surname: … (a name, spelled)',
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
