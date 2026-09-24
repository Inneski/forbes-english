# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 1.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

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

# The form explanations sit beside their answers in the data module, which
# keeps the only copy of the English; they were plain strings there until
# 2026-09-23, so German and Spanish learners read them in English.
from ieltslisten_s1_data import FORM
T['en'].update(('f%dwhy' % (i + 1), r[2]) for i, r in enumerate(FORM))

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

    # Questions 1-7: the English is registered from the data module, below.
    f1why='Einmal buchstabiert, Buchstabe für Buchstabe. Sobald jemand '
          'anfängt, Buchstaben zu nennen, wird dir eine Antwort diktiert.',
    f2why='„Double oh“ sind zwei Nullen, „oh“ ist eine: 07700 900 642. Wer '
          'auf elf einzelne Ziffern wartet, hört nie elf.',
    f3why='Er sagt Tuesday und korrigiert sich sofort: „sorry, I beg your '
          'pardon, that’s the children.“ Die Antwort ist immer die Korrektur.',
    f4why='Halb sieben. Zwanzig nach ist die Zeit, zu der man am Becken sein '
          'soll &mdash; genau so eine Zahl in der Nähe, die dasteht, damit man '
          'sie aus Versehen aufschreibt.',
    f5why='Zehn, einmal gesagt, direkt vor den Preisen. Der Mitgliederpreis '
          'danach gilt für dieselben zehn Wochen &mdash; „the whole term“.',
    f6why='Fünfunddreißig kommt zuerst, und das ist der Monatspreis für '
          'Nichtmitglieder. Sie wird Mitglied, also zahlt sie zweiundvierzig '
          'für den ganzen Kurs.',
    f7why='Badesachen und Handtuch sind „the usual“. Die Badekappe hebt er '
          'als das hervor, was die Leute vergessen, und eine Antwort in '
          'Section 1 ist fast immer das, was betont wird.',
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

    # Questions 1-7: the English is registered from the data module, below.
    f1why='Se deletrea una sola vez, letra a letra. En cuanto alguien empieza '
          'a dar letras, te están dictando una respuesta.',
    f2why='«Double oh» son dos ceros y «oh» es uno: 07700 900 642. Quien espera '
          'once cifras sueltas no las oye nunca.',
    f3why='Dice Tuesday y se corrige enseguida: «sorry, I beg your pardon, '
          'that’s the children». La respuesta es siempre la corrección.',
    f4why='Las seis y media. Y veinte es la hora de estar ya junto a la '
          'piscina: justo el tipo de número cercano que se pone ahí para que '
          'lo apuntes por error.',
    f5why='Diez, dicho una vez, justo antes de los precios. El precio para '
          'socios que viene después cubre las mismas diez semanas: «the whole '
          'term».',
    f6why='Treinta y cinco se dice primero, y es la tarifa mensual para quien '
          'no es socio. Ella se hace socia, así que paga cuarenta y dos por el '
          'curso entero.',
    f7why='El bañador y la toalla son «the usual». El gorro es lo que él '
          'destaca como lo que la gente olvida, y una respuesta de la Section 1 '
          'casi siempre es lo que se subraya.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Section 1 &mdash; <em>la conversation du quotidien</em>',
    coverSub='Deux interlocuteurs, un formulaire à remplir et un enregistrement '
             'diffusé une seule fois',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 questions',

    t1Eyebrow='Avant l’écoute',
    t1Title='La partie la plus facile, et celle où l’on jette des points',
    t1ah='Ce qu’est toujours la Section 1',
    t1ab='Deux interlocuteurs, une situation du quotidien, et un formulaire ou '
         'des notes à compléter. S’inscrire, réserver, signaler un objet perdu. '
         'C’est l’anglais le plus simple de toute l’épreuve.',
    t1an='C’est pourquoi un point perdu ici coûte autant qu’un point perdu dans '
         'la conférence, et fait plus mal.',
    t1bh='On teste l’écrit, pas la compréhension',
    t1bb='Vous comprendrez presque chaque mot. Les points dépendent de votre '
         'capacité à noter exactement un nom épelé, un numéro de téléphone et un '
         'prix pendant que l’on continue de parler.',
    t1bn='L’orthographe compte. Un mot bien entendu mais mal écrit ne rapporte '
         'rien.',
    t1ch='Lisez d’abord le formulaire',
    t1cb='Vous avez du temps avant le début de l’enregistrement. Servez-vous-en '
         'pour voir quel TYPE de réponse attend chaque blanc &mdash; un jour, un '
         'nombre, un nom &mdash; afin d’attendre la bonne chose au lieu de tout '
         'écouter.',
    t1cn='Un blanc après « £ » attend un nombre. Vous pouvez le savoir avant '
         'd’entendre un seul mot.',

    audEyebrow='L’enregistrement',
    audTitle='Vous l’entendrez une fois',
    audNote='Une conversation téléphonique entre une femme et le responsable '
            'd’un centre sportif municipal. Lisez d’abord les questions des '
            'diapositives suivantes, puis lancez la lecture &mdash; ici, ou dans '
            'la barre en bas de n’importe quelle question. L’enregistrement '
            'continue pendant que vous répondez, et vous ne l’entendez qu’une '
            'fois.',

    gapEyebrow='Questions 1&ndash;7 &middot; Complétez le formulaire',
    gapTitle='Écrivez UN MOT ET/OU UN NOMBRE dans chaque blanc',
    gapHint='L’orthographe est notée. Écrivez ce que vous avez réellement '
            'entendu, pas ce que vous vous attendiez à entendre.',

    t2Eyebrow='Après l’enregistrement',
    t2Title='Les quatre endroits où cette partie vous prend des points',
    t2ah='La correction',
    t2ab='Quelqu’un dit une chose et la change aussitôt &mdash; '
         '<em>Tuesday&hellip; sorry, that&rsquo;s the children, the adult class '
         'is Thursday</em>. La réponse est toujours la seconde. C’est l’erreur la '
         'plus fréquente de toute la partie.',
    t2an='Guettez <em>sorry</em>, <em>actually</em>, <em>I mean</em>, <em>I beg '
         'your pardon</em>. Chacun annonce que la réponse va changer.',
    t2bh='Le mot épelé',
    t2bb='Dès que quelqu’un commence à donner des lettres, on vous dicte une '
         'réponse. En Section 1, cela arrive en général une fois, et ce n’est '
         'jamais répété plus que deux personnes ne le feraient naturellement.',
    t2bn='Connaissez les lettres qui se ressemblent en anglais : A, E et I ; G '
         'et J ; M et N.',
    t2ch='Le nombre et le distracteur',
    t2cb='Les Britanniques disent <em>double oh</em> pour deux zéros et '
         '<em>oh</em> pour un seul. Et il y a presque toujours deux prix ou deux '
         'heures &mdash; l’un des deux présenté, très vite, comme le mauvais.',
    t2cn='Trente-cinq était le tarif mensuel des non-membres. Elle '
         's’inscrivait, donc la réponse était quarante-deux.',

    mcEyebrow='Questions 8&ndash;10 &middot; Détails',
    mcTitle='Qu’ont-ils dit exactement ?',

    l1why='Le petit bassin, entrée latérale. Il donne les deux d’une traite '
          '&mdash; « the classes are in the small pool, not the main one, so '
          'come through the side entrance » &mdash; et qui répond de mémoire '
          'plutôt qu’à partir de la phrase intervertit les deux moitiés.',
    l2why='La rue derrière la bibliothèque est gratuite après cinq heures. Le '
          'parking existe bien, mais il dit qu’il est plein vers six heures ; '
          '« free after five » se rapporte à la rue, pas au parking.',
    l4why='Le bâtiment a été rénové. La recommandation d’un proche et le journal '
          'local sont tous deux mentionnés dans sa dernière question, une ligne '
          'plus tôt, et c’est précisément pour cela qu’ils sont là.',

    actTitle='Prenez l’appel',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, chacun avec un formulaire. L’un tient l’accueil d’un '
                  'centre, d’un hôtel ou d’un garage ; l’autre se renseigne. '
                  'L’accueil doit épeler un nom, donner un numéro de téléphone '
                  'et se corriger une fois. Celui qui appelle remplit le '
                  'formulaire, puis le relit à voix haute.',
    actSpeak1='Qui épelle : donnez le nom de famille une seule fois, au débit '
              'normal. Ne ralentissez pas et ne le répétez pas, sauf si on vous '
              'le demande.',
    actSpeak2='Qui appelle : relisez tout le formulaire à la fin. Chaque lettre '
              'fausse est un point perdu, alors dites les lettres, pas le mot.',
    actSpeak3='À un moment de l’appel, changez un détail que vous avez déjà '
              'donné. Voyez si votre partenaire le remarque.',
    actWriteKind='Écriture · 100–150 mots',
    actWriteBrief='Écrivez les six lignes d’un formulaire pour une réservation '
                  'de votre choix &mdash; un cours, une livraison, une '
                  'réparation &mdash; et, à côté de chacune, le TYPE de réponse '
                  'qu’elle demande : un nom, un jour, un nombre, un prix. Ce '
                  'sont les trente secondes de préparation de l’épreuve, faites '
                  'd’avance.',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='Épelé une seule fois, lettre par lettre. Dès que quelqu’un commence à '
          'donner des lettres, on vous dicte une réponse.',
    f2why='« Double oh » veut dire deux zéros, et « oh » un seul : 07700 900 '
          '642. Qui attend onze chiffres séparés n’en entend jamais onze.',
    f3why='Il dit Tuesday et se corrige aussitôt : « sorry, I beg your pardon, '
          'that’s the children. » La réponse est toujours la correction.',
    f4why='Six heures et demie. Six heures vingt, c’est l’heure d’arriver au '
          'bord du bassin : exactement le genre de nombre voisin placé là pour '
          'être noté par erreur.',
    f5why='Dix, dit une seule fois, juste avant les prix. Le tarif membre qui '
          'suit couvre les mêmes dix semaines &mdash; « the whole term ».',
    f6why='Trente-cinq est dit en premier, et c’est le tarif mensuel des '
          'non-membres. Elle devient membre, donc elle paie quarante-deux pour '
          'tout le trimestre.',
    f7why='Le maillot et la serviette, c’est « the usual ». Le bonnet est ce '
          'qu’il signale comme la chose que les gens oublient, et une réponse de '
          'Section 1 est presque toujours l’élément sur lequel on insiste.',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Section 1 &mdash; <em>la conversazione quotidiana</em>',
    coverSub='Due persone che parlano, un modulo da compilare e una '
             'registrazione che si sente una volta sola',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 domande',

    t1Eyebrow='Prima dell’ascolto',
    t1Title='La parte più facile, e quella in cui si buttano via punti',
    t1ah='Che cos’è sempre la Section 1',
    t1ab='Due persone, una situazione quotidiana e un modulo o degli appunti da '
         'completare. Iscriversi, prenotare, denunciare uno smarrimento. È '
         'l’inglese più semplice di tutta la prova.',
    t1an='Proprio per questo un punto perso qui costa quanto uno perso nella '
         'lezione, e brucia di più.',
    t1bh='Si valuta la scrittura, non la comprensione',
    t1bb='Capirai quasi ogni parola. I punti dipendono dal saper annotare con '
         'precisione un cognome compitato, un numero di telefono e un prezzo '
         'mentre l’altro continua a parlare.',
    t1bn='L’ortografia conta. Una parola sentita bene ma scritta male non vale '
         'niente.',
    t1ch='Leggi prima il modulo',
    t1cb='Hai del tempo prima che parta la registrazione. Usalo per capire che '
         'TIPO di risposta vuole ogni spazio &mdash; un giorno, un numero, un '
         'nome &mdash; così aspetti la cosa giusta invece di ascoltare tutto.',
    t1cn='Uno spazio dopo «£» vuole un numero. Puoi saperlo prima di sentire una '
         'sola parola.',

    audEyebrow='La registrazione',
    audTitle='La sentirai una volta',
    audNote='Una telefonata tra una donna e il responsabile di un centro '
            'sportivo comunale. Leggi prima le domande delle slide successive, '
            'poi premi play &mdash; qui o nella barra in fondo a qualsiasi slide '
            'di domande. La registrazione continua mentre rispondi, e la senti '
            'una volta sola.',

    gapEyebrow='Domande 1&ndash;7 &middot; Completa il modulo',
    gapTitle='Scrivi UNA PAROLA E/O UN NUMERO in ogni spazio',
    gapHint='L’ortografia viene valutata. Scrivi quello che hai sentito davvero, '
            'non quello che ti aspettavi di sentire.',

    t2Eyebrow='Dopo la registrazione',
    t2Title='I quattro momenti in cui questa parte ti toglie punti',
    t2ah='La correzione',
    t2ab='Qualcuno dice una cosa e la cambia subito &mdash; <em>Tuesday&hellip; '
         'sorry, that&rsquo;s the children, the adult class is Thursday</em>. La '
         'risposta è sempre la seconda. È l’errore più comune di tutta la '
         'sezione.',
    t2an='Fai attenzione a <em>sorry</em>, <em>actually</em>, <em>I mean</em>, '
         '<em>I beg your pardon</em>. Ognuno avverte che la risposta sta per '
         'cambiare.',
    t2bh='La parola compitata',
    t2bb='Appena qualcuno comincia a dire delle lettere, ti stanno dettando una '
         'risposta. Nella Section 1 di solito succede una volta, e non viene mai '
         'ripetuta più di quanto due persone farebbero naturalmente.',
    t2bn='Impara le lettere che in inglese si somigliano: A, E e I; G e J; M e '
         'N.',
    t2ch='Il numero e il distrattore',
    t2cb='I britannici dicono <em>double oh</em> per due zeri e <em>oh</em> per '
         'uno. E quasi sempre ci sono due prezzi o due orari &mdash; uno dei due '
         'indicato, in fretta, come quello sbagliato.',
    t2cn='Trentacinque era la tariffa mensile per i non soci. Lei si stava '
         'iscrivendo, quindi la risposta era quarantadue.',

    mcEyebrow='Domande 8&ndash;10 &middot; Dettagli',
    mcTitle='Che cosa hanno detto esattamente?',

    l1why='La piscina piccola, ingresso laterale. Lui dice le due cose d’un '
          'fiato &mdash; «the classes are in the small pool, not the main one, '
          'so come through the side entrance» &mdash; e chi risponde a memoria '
          'invece che dalla frase scambia le due metà.',
    l2why='La strada dietro la biblioteca è gratuita dopo le cinque. Il '
          'parcheggio esiste, ma lui dice che si riempie entro le sei; «free '
          'after five» si riferisce alla strada, non al parcheggio.',
    l4why='L’edificio è stato ristrutturato. Il consiglio di un amico e il '
          'giornale locale compaiono entrambi nella sua ultima domanda, una riga '
          'prima, ed è proprio per questo che sono lì.',

    actTitle='Rispondi alla chiamata',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, ognuno con un modulo. Uno fa il receptionist di un '
                  'centro, di un hotel o di un’officina; l’altro chiede '
                  'informazioni. Il receptionist deve compitare un nome, dare un '
                  'numero di telefono e correggersi una volta. Chi chiama '
                  'compila il modulo e poi lo rilegge ad alta voce.',
    actSpeak1='Chi compita: di’ il cognome una volta sola, a velocità normale. '
              'Non rallentare e non ripeterlo, a meno che non te lo chiedano.',
    actSpeak2='Chi chiama: alla fine rileggi tutto il modulo. Ogni lettera '
              'sbagliata è un punto, quindi di’ le lettere, non la parola.',
    actSpeak3='A un certo punto della chiamata, cambia un dettaglio che hai già '
              'dato. Vedi se il tuo compagno se ne accorge.',
    actWriteKind='Scrittura · 100–150 parole',
    actWriteBrief='Scrivi le sei righe di un modulo per una prenotazione a tua '
                  'scelta &mdash; un corso, una consegna, una riparazione '
                  '&mdash; e accanto a ciascuna scrivi che TIPO di risposta '
                  'richiede: un nome, un giorno, un numero, un prezzo. Sono i '
                  'trenta secondi di preparazione che ti dà la prova, fatti in '
                  'anticipo.',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='Compitato una volta sola, lettera per lettera. Nel momento in cui '
          'qualcuno comincia a dire delle lettere, ti stanno dettando una '
          'risposta.',
    f2why='«Double oh» sono due zeri e «oh» è uno: 07700 900 642. Chi aspetta '
          'undici cifre separate non ne sente mai undici.',
    f3why='Dice Tuesday e si corregge subito: «sorry, I beg your pardon, '
          'that’s the children.» La risposta è sempre la correzione.',
    f4why='Le sei e mezza. Le sei e venti sono l’ora in cui presentarsi a bordo '
          'vasca: proprio il tipo di numero vicino messo lì per essere scritto '
          'per sbaglio.',
    f5why='Dieci, detto una volta, subito prima dei prezzi. Il prezzo per i soci '
          'che segue copre le stesse dieci settimane &mdash; «the whole term».',
    f6why='Trentacinque viene detto per primo, ed è la tariffa mensile per i non '
          'soci. Lei si iscrive, quindi paga quarantadue per tutto il '
          'trimestre.',
    f7why='Costume e asciugamano sono «the usual». La cuffia è quella che lui '
          'indica come la cosa che la gente dimentica, e una risposta della '
          'Section 1 è quasi sempre l’elemento su cui si insiste.',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Section 1 &mdash; <em>a conversa do dia a dia</em>',
    coverSub='Duas pessoas, um formulário para preencher e uma gravação que '
             'passa exatamente uma vez',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 perguntas',

    t1Eyebrow='Antes de ouvir',
    t1Title='A parte mais fácil, e aquela onde se deitam pontos fora',
    t1ah='O que a Section 1 é sempre',
    t1ab='Duas pessoas, uma situação do dia a dia e um formulário ou umas notas '
         'para completar. Inscrever-se, reservar, participar a perda de alguma '
         'coisa. É o inglês mais simples de toda a prova.',
    t1an='É precisamente por isso que um ponto perdido aqui custa o mesmo que um '
         'ponto perdido na palestra, e dói mais.',
    t1bh='Avalia a escrita, não a compreensão',
    t1bb='Vais perceber quase todas as palavras. Os pontos dependem de '
         'conseguires anotar com exatidão um apelido soletrado, um número de '
         'telefone e um preço enquanto a outra pessoa continua a falar.',
    t1bn='A ortografia conta. Uma palavra bem ouvida mas mal escrita não vale '
         'nada.',
    t1ch='Lê primeiro o formulário',
    t1cb='Tens tempo antes de a gravação começar. Usa-o para ver que TIPO de '
         'resposta pede cada espaço &mdash; um dia, um número, um nome &mdash; '
         'para esperares a coisa certa em vez de ouvires tudo.',
    t1cn='Um espaço depois de «£» pede um número. Podes sabê-lo antes de ouvires '
         'uma única palavra.',

    audEyebrow='A gravação',
    audTitle='Vais ouvi-la uma vez',
    audNote='Uma conversa telefónica entre uma mulher e o responsável de um '
            'centro desportivo municipal. Lê primeiro as perguntas dos '
            'diapositivos seguintes e depois carrega em reproduzir &mdash; aqui '
            'ou na barra no fundo de qualquer diapositivo de perguntas. A '
            'gravação continua enquanto respondes, e só a ouves uma vez.',

    gapEyebrow='Perguntas 1&ndash;7 &middot; Completa o formulário',
    gapTitle='Escreve UMA PALAVRA E/OU UM NÚMERO em cada espaço',
    gapHint='A ortografia é avaliada. Escreve o que ouviste de facto, não o que '
            'esperavas ouvir.',

    t2Eyebrow='Depois da gravação',
    t2Title='Os quatro sítios onde esta parte te tira pontos',
    t2ah='A correção',
    t2ab='Alguém diz uma coisa e muda-a logo a seguir &mdash; '
         '<em>Tuesday&hellip; sorry, that&rsquo;s the children, the adult class '
         'is Thursday</em>. A resposta é sempre a segunda. É o erro mais comum '
         'de toda a secção.',
    t2an='Está atento a <em>sorry</em>, <em>actually</em>, <em>I mean</em>, '
         '<em>I beg your pardon</em>. Cada uma avisa que a resposta está '
         'prestes a mudar.',
    t2bh='A palavra soletrada',
    t2bb='Quando alguém começa a dizer letras, está a ser ditada uma resposta. '
         'Na Section 1 isto costuma acontecer uma vez, e nunca é repetido mais '
         'do que duas pessoas o repetiriam naturalmente.',
    t2bn='Conhece as letras que soam parecidas em inglês: A, E e I; G e J; M e '
         'N.',
    t2ch='O número e o distrator',
    t2cb='Os britânicos dizem <em>double oh</em> para dois zeros e <em>oh</em> '
         'para um. E há quase sempre dois preços ou duas horas &mdash; um deles '
         'apontado, de passagem, como o errado.',
    t2cn='Trinta e cinco era a mensalidade para não sócios. Ela ia '
         'inscrever-se, por isso a resposta era quarenta e dois.',

    mcEyebrow='Perguntas 8&ndash;10 &middot; Pormenor',
    mcTitle='O que disseram exatamente?',

    l1why='A piscina pequena, entrada lateral. Ele diz as duas coisas de uma vez '
          '&mdash; «the classes are in the small pool, not the main one, so '
          'come through the side entrance» &mdash; e quem responde de memória, '
          'e não a partir da frase, troca as duas metades.',
    l2why='A rua atrás da biblioteca é gratuita depois das cinco. O parque de '
          'estacionamento existe, mas ele diz que enche por volta das seis; '
          '«free after five» refere-se à rua, não ao parque.',
    l4why='O edifício foi remodelado. A recomendação de uma pessoa amiga e o '
          'jornal local aparecem ambos na última pergunta dela, uma linha antes, '
          'e é exatamente por isso que lá estão.',

    actTitle='Atende a chamada',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, cada um com um formulário. Um está na receção de um '
                  'centro, de um hotel ou de uma oficina; o outro pede '
                  'informações. A receção tem de soletrar um nome, dar um número '
                  'de telefone e corrigir-se uma vez. Quem liga preenche o '
                  'formulário e depois lê-o em voz alta.',
    actSpeak1='Quem soletra: diz o apelido uma só vez, à velocidade normal. Não '
              'abrandes e não repitas, a não ser que te peçam.',
    actSpeak2='Quem liga: no fim, lê o formulário todo em voz alta. Cada letra '
              'errada é um ponto, por isso diz as letras, não a palavra.',
    actSpeak3='A certa altura da chamada, muda um pormenor que já tinhas dado. '
              'Vê se o teu colega dá por isso.',
    actWriteKind='Escrita · 100–150 palavras',
    actWriteBrief='Escreve as seis linhas de um formulário para uma reserva à '
                  'tua escolha &mdash; um curso, uma entrega, uma reparação '
                  '&mdash; e ao lado de cada uma escreve que TIPO de resposta '
                  'pede: um nome, um dia, um número, um preço. São os trinta '
                  'segundos de preparação que a prova te dá, feitos com '
                  'antecedência.',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='Soletrado uma só vez, letra a letra. Assim que alguém começa a dizer '
          'letras, estão a ditar-te uma resposta.',
    f2why='«Double oh» são dois zeros e «oh» é um: 07700 900 642. Quem espera '
          'onze algarismos soltos nunca ouve onze.',
    f3why='Ele diz Tuesday e corrige-se logo: «sorry, I beg your pardon, '
          'that’s the children.» A resposta é sempre a correção.',
    f4why='Seis e meia. Seis e vinte é a hora de estar à beira da piscina: '
          'exatamente o tipo de número próximo que está ali para ser escrito por '
          'engano.',
    f5why='Dez, dito uma vez, mesmo antes dos preços. O preço para sócios que '
          'vem a seguir cobre as mesmas dez semanas &mdash; «the whole term».',
    f6why='Trinta e cinco é dito primeiro, e é a mensalidade para não sócios. '
          'Ela vai inscrever-se, por isso paga quarenta e dois pelo período '
          'inteiro.',
    f7why='O fato de banho e a toalha são «the usual». A touca é o que ele '
          'destaca como aquilo de que as pessoas se esquecem, e uma resposta da '
          'Section 1 é quase sempre o elemento que é sublinhado.',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Section 1 &mdash; <em>бытовой разговор</em>',
    coverSub='Два собеседника, одна анкета и запись, которая звучит ровно один '
             'раз',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 вопросов',

    t1Eyebrow='Перед прослушиванием',
    t1Title='Самая лёгкая часть &mdash; и та, где баллы теряют зря',
    t1ah='Чем всегда бывает Section 1',
    t1ab='Два собеседника, бытовая ситуация и анкета или заметки, которые нужно '
         'заполнить. Записаться, забронировать, сообщить о потере. Это самый '
         'простой английский во всём экзамене.',
    t1an='Именно поэтому балл, потерянный здесь, стоит столько же, сколько '
         'балл, потерянный в лекции, и обиднее.',
    t1bh='Проверяется письмо, а не понимание',
    t1bb='Вы поймёте почти каждое слово. Баллы зависят от того, сможете ли вы '
         'точно записать продиктованную по буквам фамилию, номер телефона и '
         'цену, пока собеседник продолжает говорить.',
    t1bn='Орфография учитывается. Слово, услышанное верно, но записанное с '
         'ошибкой, не приносит ничего.',
    t1ch='Сначала прочитайте анкету',
    t1cb='Перед началом записи у вас есть время. Используйте его, чтобы понять, '
         'какого ТИПА ответ нужен в каждом пропуске &mdash; день, число, имя '
         '&mdash; и ждать нужного, а не слушать всё подряд.',
    t1cn='Пропуск после «£» требует числа. Это можно знать ещё до того, как '
         'прозвучит первое слово.',

    audEyebrow='Запись',
    audTitle='Вы услышите её один раз',
    audNote='Телефонный разговор женщины с управляющим муниципального '
            'спортивного центра. Сначала прочитайте вопросы на следующих '
            'слайдах, затем нажмите воспроизведение &mdash; здесь или на панели '
            'внизу любого слайда с вопросами. Запись продолжает звучать, пока вы '
            'отвечаете, и вы слышите её один раз.',

    gapEyebrow='Вопросы 1&ndash;7 &middot; Заполните анкету',
    gapTitle='Впишите ОДНО СЛОВО И/ИЛИ ЧИСЛО в каждый пропуск',
    gapHint='Орфография оценивается. Пишите то, что действительно услышали, а '
            'не то, что ожидали услышать.',

    t2Eyebrow='После записи',
    t2Title='Четыре места, где эта часть отнимает баллы',
    t2ah='Поправка',
    t2ab='Говорящий называет одно и тут же меняет &mdash; <em>Tuesday&hellip; '
         'sorry, that&rsquo;s the children, the adult class is Thursday</em>. '
         'Ответ всегда второй. Это самая частая ошибка во всей части.',
    t2an='Ловите <em>sorry</em>, <em>actually</em>, <em>I mean</em>, <em>I beg '
         'your pardon</em>. Каждое из них предупреждает, что ответ сейчас '
         'изменится.',
    t2bh='Слово по буквам',
    t2bb='Как только говорящий начинает называть буквы, вам диктуют ответ. В '
         'Section 1 это обычно бывает один раз и повторяется не больше, чем '
         'повторили бы два человека в обычном разговоре.',
    t2bn='Знайте буквы, которые в английском звучат похоже: A, E и I; G и J; M '
         'и N.',
    t2ch='Число и отвлекающий вариант',
    t2cb='Британцы говорят <em>double oh</em> о двух нулях и <em>oh</em> об '
         'одном. И почти всегда звучат две цены или два времени &mdash; одно из '
         'них мимоходом обозначено как неверное.',
    t2cn='Тридцать пять &mdash; месячный тариф для тех, кто не состоит в клубе. '
         'Она вступала, поэтому ответ &mdash; сорок два.',

    mcEyebrow='Вопросы 8&ndash;10 &middot; Детали',
    mcTitle='Что именно они сказали?',

    l1why='Малый бассейн, боковой вход. Он называет оба на одном дыхании '
          '&mdash; «the classes are in the small pool, not the main one, so come '
          'through the side entrance» &mdash; и тот, кто отвечает по памяти, а '
          'не по фразе, меняет половины местами.',
    l2why='Улица за библиотекой бесплатна после пяти. Парковка есть, но он '
          'говорит, что к шести она заполняется; «free after five» относится к '
          'улице, а не к парковке.',
    l4why='Здание отремонтировали. Совет знакомого и местная газета упоминаются '
          'в её последнем вопросе, строкой раньше, и именно поэтому они там.',

    actTitle='Примите звонок',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, у каждого анкета. Один работает на ресепшене центра, '
                  'отеля или автосервиса, другой наводит справки. Ресепшен '
                  'должен продиктовать по буквам одно имя, назвать один номер '
                  'телефона и один раз поправиться. Звонящий заполняет анкету и '
                  'в конце зачитывает её.',
    actSpeak1='Тот, кто диктует: назовите фамилию один раз, в обычном темпе. Не '
              'замедляйтесь и не повторяйте, если не просят.',
    actSpeak2='Звонящий: в конце зачитайте всю анкету. Каждая неверная буква '
              '&mdash; потерянный балл, поэтому называйте буквы, а не слово.',
    actSpeak3='Где-нибудь в разговоре измените деталь, которую уже назвали. '
              'Посмотрите, заметит ли партнёр.',
    actWriteKind='Письмо · 100–150 слов',
    actWriteBrief='Напишите шесть строк анкеты для бронирования на ваш выбор '
                  '&mdash; курс, доставка, ремонт &mdash; и рядом с каждой '
                  'укажите, какого ТИПА ответ она требует: имя, день, число, '
                  'цена. Это те тридцать секунд подготовки, которые даёт '
                  'экзамен, сделанные заранее.',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='Продиктовано по буквам один раз. Как только говорящий начинает '
          'называть буквы, вам диктуют ответ.',
    f2why='«Double oh» &mdash; это два нуля, а «oh» &mdash; один: 07700 900 642. '
          'Кто ждёт одиннадцать отдельных цифр, никогда не услышит '
          'одиннадцать.',
    f3why='Он говорит Tuesday и сразу поправляется: «sorry, I beg your pardon, '
          'that’s the children». Ответ &mdash; всегда поправка.',
    f4why='Половина седьмого. Двадцать минут седьмого &mdash; это когда нужно '
          'быть у бассейна: как раз такое соседнее число, которое стоит там, '
          'чтобы его записали по ошибке.',
    f5why='Десять, сказано один раз, прямо перед ценами. Цена для членов клуба, '
          'которая идёт следом, покрывает те же десять недель &mdash; «the whole '
          'term».',
    f6why='Тридцать пять звучит первым, и это месячный тариф для тех, кто не '
          'состоит в клубе. Она вступает, поэтому платит сорок два за весь '
          'курс.',
    f7why='Купальник и полотенце &mdash; это «the usual». Шапочку он выделяет '
          'как то, что люди забывают, а ответ в Section 1 почти всегда &mdash; '
          'то, на чём делают упор.',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Section 1 &mdash; <em>المحادثة اليومية</em>',
    coverSub='متحدثان، واستمارة واحدة تملؤها، وتسجيل يُذاع مرة واحدة فقط',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 أسئلة',

    t1Eyebrow='قبل أن تستمع',
    t1Title='أسهل الأقسام، والقسم الذي تُهدر فيه الدرجات',
    t1ah='ما الذي يأتي في Section 1 دائمًا',
    t1ab='متحدثان، وموقف من الحياة اليومية، واستمارة أو ملاحظات عليك إكمالها: '
         'التسجيل في دورة، أو الحجز، أو الإبلاغ عن شيء مفقود. إنها أسهل '
         'إنجليزية في الاختبار كله.',
    t1an='ولهذا بالذات تكلّفك الدرجة الضائعة هنا ما تكلّفه الدرجة الضائعة في '
         'المحاضرة، وتؤلم أكثر.',
    t1bh='يختبر الكتابة، لا الفهم',
    t1bb='ستفهم كل كلمة تقريبًا. أما الدرجات فتتوقف على قدرتك على أن تكتب بدقة '
         'اسم عائلة مُتهجّى، ورقم هاتف، وسعرًا، بينما يواصل المتحدث كلامه.',
    t1bn='الإملاء يُحتسب. الكلمة التي تسمعها صحيحة وتكتبها خطأً لا تنال شيئًا.',
    t1ch='اقرأ الاستمارة أولًا',
    t1cb='يُعطى لك وقت قبل أن يبدأ التسجيل. استخدمه لترى نوع الإجابة التي '
         'يريدها كل فراغ &mdash; يومًا، أو رقمًا، أو اسمًا &mdash; فتنتظر الشيء '
         'الصحيح بدل أن تستمع إلى كل شيء.',
    t1cn='الفراغ الذي يأتي بعد «£» يريد رقمًا. يمكنك أن تعرف ذلك قبل أن تسمع '
         'كلمة واحدة.',

    audEyebrow='التسجيل',
    audTitle='ستسمعه مرة واحدة',
    audNote='مكالمة هاتفية بين امرأة ومدير مركز رياضي محلي. اقرأ أولًا الأسئلة '
            'في الشرائح التالية، ثم اضغط زر التشغيل &mdash; هنا، أو في الشريط '
            'أسفل أي شريحة أسئلة. يستمر التسجيل وأنت تجيب، ولن تسمعه إلا مرة '
            'واحدة.',

    gapEyebrow='الأسئلة 1&ndash;7 &middot; أكمل الاستمارة',
    gapTitle='اكتب كلمة واحدة و/أو رقمًا واحدًا في كل فراغ',
    gapHint='الإملاء يُقيَّم. اكتب ما سمعته فعلًا، لا ما توقعت أن تسمعه.',

    t2Eyebrow='بعد التسجيل',
    t2Title='المواضع الأربعة التي يأخذ منها هذا القسم درجاتك',
    t2ah='التصحيح',
    t2ab='يقول المتحدث شيئًا ثم يغيّره فورًا &mdash; <em>Tuesday&hellip; sorry, '
         'that&rsquo;s the children, the adult class is Thursday</em>. والإجابة '
         'هي الثانية دائمًا. هذا أشيع خطأ في القسم كله.',
    t2an='انتبه إلى <em>sorry</em> و<em>actually</em> و<em>I mean</em> و<em>I '
         'beg your pardon</em>. كل واحدة منها إنذار بأن الإجابة على وشك أن '
         'تتغيّر.',
    t2bh='الكلمة المتهجّاة',
    t2bb='حين يبدأ المتحدث بذكر الحروف، فهناك إجابة تُملى عليك. في Section 1 '
         'يحدث ذلك عادةً مرة واحدة، ولا يتكرر أكثر مما يكرره متحدثان بشكل '
         'طبيعي.',
    t2bn='اعرف الحروف المتشابهة في النطق بالإنجليزية: A وE وI؛ وG وJ؛ وM وN.',
    t2ch='الرقم والمشتِّت',
    t2cb='يقول البريطانيون <em>double oh</em> لصفرين و<em>oh</em> لصفر واحد. '
         'وهناك دائمًا تقريبًا سعران أو وقتان &mdash; يُشار إلى أحدهما بسرعة '
         'على أنه الخطأ.',
    t2cn='خمسة وثلاثون كان الاشتراك الشهري لغير الأعضاء. وهي كانت تنضم إلى '
         'المركز، فكانت الإجابة اثنين وأربعين.',

    mcEyebrow='الأسئلة 8&ndash;10 &middot; التفاصيل',
    mcTitle='ماذا قالوا بالضبط؟',

    l1why='المسبح الصغير، والمدخل الجانبي. يذكر الاثنين في نَفَس واحد &mdash; '
          '<bdi>&ldquo;the classes are in the small pool, not the main one, so '
          'come through the side entrance&rdquo;</bdi> &mdash; ومن يجيب من '
          'الذاكرة لا من الجملة يبدّل النصفين.',
    l2why='الشارع خلف المكتبة مجاني بعد الخامسة. موقف السيارات موجود، لكنه يقول '
          'إنه يمتلئ بحلول السادسة؛ وعبارة <bdi>&ldquo;free after '
          'five&rdquo;</bdi> تعود إلى الشارع لا إلى الموقف.',
    l4why='جُدِّد المبنى. أما الصديق والصحيفة المحلية فكلاهما مذكور في سؤالها '
          'الأخير، قبل ذلك بسطر، ولهذا بالضبط هما هناك.',

    actTitle='أجب عن المكالمة',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='في أزواج، مع استمارة لكل منكما. أحدكما موظف استقبال في مركز '
                  'أو فندق أو ورشة تصليح، والآخر يستفسر. على موظف الاستقبال أن '
                  'يتهجّى اسمًا واحدًا، ويذكر رقم هاتف واحدًا، ويصحّح نفسه مرة '
                  'واحدة. ويملأ المتصل الاستمارة ثم يقرؤها بصوت عالٍ.',
    actSpeak1='من يتهجّى: اذكر اسم العائلة مرة واحدة، بسرعة الكلام العادية. لا '
              'تبطئ ولا تكرّره إلا إذا طُلب منك.',
    actSpeak2='المتصل: اقرأ الاستمارة كلها في النهاية. كل حرف خطأ درجة ضائعة، '
              'فاذكر الحروف لا الكلمة.',
    actSpeak3='في مكان ما من المكالمة، غيّر تفصيلًا سبق أن ذكرته، وانظر هل ينتبه '
              'زميلك.',
    actWriteKind='الكتابة · 100–150 كلمة',
    actWriteBrief='اكتب الأسطر الستة لاستمارة حجز من اختيارك &mdash; دورة، أو '
                  'توصيل، أو تصليح &mdash; واكتب بجانب كل سطر نوع الإجابة التي '
                  'يحتاجها: اسم، يوم، رقم، سعر. هذه هي الثلاثون ثانية من '
                  'التحضير التي يمنحك إياها الاختبار، منجزة مسبقًا.',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='يُتهجّى مرة واحدة، حرفًا حرفًا. في اللحظة التي يبدأ فيها المتحدث '
          'بذكر الحروف، تكون هناك إجابة تُملى عليك.',
    f2why='عبارة <bdi>&ldquo;double oh&rdquo;</bdi> تعني صفرين، '
          'و<bdi>&ldquo;oh&rdquo;</bdi> تعني صفرًا واحدًا: <bdi>07700 900 '
          '642</bdi>. ومن ينتظر أحد عشر رقمًا منفصلًا لا يسمع أحد عشر أبدًا.',
    f3why='يقول Tuesday ثم يصحّح نفسه فورًا: <bdi>&ldquo;sorry, I beg your '
          'pardon, that&rsquo;s the children.&rdquo;</bdi> والإجابة هي التصحيح '
          'دائمًا.',
    f4why='السادسة والنصف. أما السادسة وعشرون دقيقة فهي موعد الوصول إلى حافة '
          'المسبح، وهذا بالضبط نوع الرقم القريب الذي يوضع هناك لكي يُكتب '
          'خطأً.',
    f5why='عشرة، تُقال مرة واحدة، قبل الأسعار مباشرة. وسعر الأعضاء الذي يليها '
          'يغطي الأسابيع العشرة نفسها &mdash; <bdi>&ldquo;the whole '
          'term&rdquo;</bdi>.',
    f6why='خمسة وثلاثون تُقال أولًا، وهي الاشتراك الشهري لغير الأعضاء. وهي '
          'تنضم إلى المركز، فتدفع اثنين وأربعين عن الفصل كله.',
    f7why='ملابس السباحة والمنشفة هي <bdi>&ldquo;the usual&rdquo;</bdi>. أما '
          'قبعة السباحة فهي ما يخصّه بالذكر على أنه الشيء الذي ينساه الناس، '
          'وإجابة Section 1 تكون في الغالب العنصر الذي يُشدَّد عليه.',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Section 1 &mdash; <em>日常对话</em>',
    coverSub='两位说话人，一张要填的表格，一段只播放一次的录音',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 题',

    t1Eyebrow='听之前',
    t1Title='最简单的部分，也是最容易白白丢分的部分',
    t1ah='Section 1 总是什么样',
    t1ab='两位说话人，一个日常场景，一张要填的表格或一份笔记。报名、预订、报失物'
         '品。这是整张试卷里最简单的英语。',
    t1an='正因为如此，在这里丢的一分和在讲座部分丢的一分一样多，却更让人心疼。',
    t1bh='考的是书写，不是理解',
    t1bb='你几乎每个词都能听懂。分数取决于你能否在对方不停说话的同时，准确写下一'
         '个拼读出来的姓、一个电话号码和一个价格。',
    t1bn='拼写要计分。听对了却拼错的词，一分不得。',
    t1ch='先读表格',
    t1cb='录音开始前有一段时间。用它看清每个空要的是什么类型的答案——日期、数字'
         '还是名字——这样你是在等对的东西，而不是什么都听。',
    t1cn='“£” 后面的空要填数字。你在听到一个词之前就能知道这一点。',

    audEyebrow='录音',
    audTitle='你只能听一次',
    audNote='一段电话对话，一位女士和一家社区体育中心的经理。先读后面几页的问题，'
            '再按播放——在这里，或在任何一页问题底部的播放条上。你作答时录音会'
            '继续播放，而且只播放一次。',

    gapEyebrow='问题 1&ndash;7 &middot; 完成表格',
    gapTitle='每个空填写一个单词和/或一个数字',
    gapHint='拼写要计分。写你真正听到的，而不是你以为会听到的。',

    t2Eyebrow='录音之后',
    t2Title='这一部分扣分的四个地方',
    t2ah='更正',
    t2ab='说话人说了一样东西，马上又改口——<em>Tuesday&hellip; sorry, '
         'that&rsquo;s the children, the adult class is Thursday</em>。答案永远'
         '是第二个。这是整个部分最常见的错误。',
    t2an='注意听 <em>sorry</em>、<em>actually</em>、<em>I mean</em>、<em>I beg '
         'your pardon</em>。每一个都在提醒你：答案马上要变了。',
    t2bh='拼读的单词',
    t2bb='说话人一开始报字母，就是在给你口述答案。Section 1 里这种情况通常只出现'
         '一次，而且重复的次数不会超过两个人自然对话时的重复。',
    t2bn='记住英语里发音相近的字母：A、E 和 I；G 和 J；M 和 N。',
    t2ch='数字和干扰项',
    t2cb='英国人把两个零说成 <em>double oh</em>，一个零说成 <em>oh</em>。而且几'
         '乎总会出现两个价格或两个时间——其中一个会被很快地点明是错的。',
    t2cn='三十五是非会员的月费。她是要入会的，所以答案是四十二。',

    mcEyebrow='问题 8&ndash;10 &middot; 细节',
    mcTitle='他们到底说了什么？',

    l1why='小泳池，侧门。他一口气说了两件事——&ldquo;the classes are in the '
          'small pool, not the main one, so come through the side '
          'entrance&rdquo;——凭记忆而不是根据原句作答的人，会把两半弄反。',
    l2why='图书馆后面的街道五点以后免费。停车场确实有，但他说六点前就满了；'
          '&ldquo;free after five&rdquo; 说的是那条街，不是停车场。',
    l4why='大楼翻修过。朋友和当地报纸都出现在她的最后一个问题里，就在前一行，这'
          '正是它们出现在那里的原因。',

    actTitle='接这个电话',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，每人一张表格。一人在某个中心、酒店或修车行做前台，'
                  '另一人来咨询。前台必须拼读一个名字、报一个电话号码，并且自我'
                  '更正一次。来电者填好表格，最后把它读一遍。',
    actSpeak1='拼读的人：用正常语速把姓说一遍。不要放慢；除非对方要求，否则不要'
              '重复。',
    actSpeak2='来电者：最后把整张表格读回去。每错一个字母就丢一分，所以要报字母，'
              '而不是读单词。',
    actSpeak3='在通话中的某个地方，改掉一个你已经说过的细节。看看同伴能不能发现。',
    actWriteKind='写作 · 100–150 词',
    actWriteBrief='为你自选的一项预订写出一张表格的六行——一门课程、一次送货、一'
                  '次维修——并在每一行旁边写上它需要哪种答案：名字、日期、数字、'
                  '价格。这就是考试给你的那三十秒准备时间，提前完成。',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='只拼读一次，一个字母一个字母地说。说话人一开始报字母，就是在给你口述'
          '答案。',
    f2why='&ldquo;Double oh&rdquo; 是两个零，&ldquo;oh&rdquo; 是一个零：07700 '
          '900 642。等着听十一个单独数字的考生，永远听不到十一个。',
    f3why='他说了 Tuesday，马上改口：&ldquo;sorry, I beg your pardon, '
          'that&rsquo;s the children.&rdquo; 答案永远是更正后的那个。',
    f4why='六点半。六点二十是到泳池边的时间，正是那种放在旁边、让人一不小心就写'
          '下来的相近数字。',
    f5why='十，只说了一次，就在报价之前。后面的会员价涵盖的是同样的十周——'
          '&ldquo;the whole term&rdquo;。',
    f6why='三十五先说出来，那是非会员的月费。她要入会，所以整个学期付四十二。',
    f7why='泳衣和毛巾是 &ldquo;the usual&rdquo;。泳帽是他特别点出来、说大家常忘'
          '带的东西，而 Section 1 的答案几乎总是被强调的那一项。',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Section 1 &mdash; <em>日常の会話</em>',
    coverSub='話し手は二人、埋める用紙は一枚、そして録音は一度きり',
    chipLevel='B2&ndash;C1', chipFocus='Listening &middot; Section 1',
    chipCount='10 問',

    t1Eyebrow='聞く前に',
    t1Title='いちばん易しいセクション、そして点を捨ててしまうセクション',
    t1ah='Section 1 はいつもこういうもの',
    t1ab='話し手は二人、日常の場面、そして埋める用紙かメモ。入会の手続き、予約、'
         '落とし物の届け出。試験全体でいちばん易しい英語です。',
    t1an='だからこそ、ここで失う1点は講義で失う1点と同じ重さで、しかもより悔しい'
         'のです。',
    t1bh='試されるのは理解ではなく、書くこと',
    t1bb='ほぼすべての語が聞き取れるはずです。点数を分けるのは、相手が話し続けて'
         'いる間に、つづりを言われた名字、電話番号、値段を正確に書き取れるかどう'
         'かです。',
    t1bn='つづりも採点されます。正しく聞き取れても、つづりを間違えれば0点です。',
    t1ch='まず用紙を読む',
    t1cb='録音が始まる前に時間があります。それを使って、各空欄がどんな種類の答え'
         'を求めているか――曜日か、数字か、名前か――を確かめましょう。そうすれば、'
         'すべてを聞くのではなく、必要なものを待ち構えられます。',
    t1cn='「£」の後の空欄には数字が入ります。一語も聞く前にわかることです。',

    audEyebrow='録音',
    audTitle='聞けるのは一度だけ',
    audNote='女性と地域のスポーツセンターの責任者との電話での会話です。まず次の'
            'スライドの問題を読み、それから再生を押しましょう――ここでも、どの問'
            '題スライドの下のバーでもかまいません。答えている間も録音は流れ続け、'
            '聞けるのは一度だけです。',

    gapEyebrow='問題 1&ndash;7 &middot; 用紙を完成させる',
    gapTitle='各空欄に「1語および／または数字1つ」を書きましょう',
    gapHint='つづりも採点されます。聞こえると思っていたものではなく、実際に聞こえ'
            'たものを書きましょう。',

    t2Eyebrow='録音の後で',
    t2Title='このセクションが点を奪う四つの場所',
    t2ah='言い直し',
    t2ab='話し手が何かを言って、すぐに変えます――<em>Tuesday&hellip; sorry, '
         'that&rsquo;s the children, the adult class is Thursday</em>。答えは必'
         'ず二つ目です。このセクション全体でいちばん多い間違いです。',
    t2an='<em>sorry</em>、<em>actually</em>、<em>I mean</em>、<em>I beg your '
         'pardon</em> に耳を澄ましましょう。どれも、答えがこれから変わるという'
         '合図です。',
    t2bh='つづりを言われる語',
    t2bb='話し手がアルファベットを言い始めたら、答えを書き取らされているのです。'
         'Section 1 ではたいてい一度だけで、二人の人が自然に繰り返す以上に繰り返'
         'されることはありません。',
    t2bn='英語で似て聞こえる文字を覚えておきましょう：A、E と I、G と J、M と '
         'N。',
    t2ch='数字と引っかけ',
    t2cb='イギリス人はゼロ二つを <em>double oh</em>、ゼロ一つを <em>oh</em> と'
         '言います。そして値段や時刻はほぼ必ず二つ出てきて――そのうち一つは、さっ'
         'と違うものだと示されます。',
    t2cn='35は非会員の月額料金でした。彼女は入会するところだったので、答えは42で'
         'した。',

    mcEyebrow='問題 8&ndash;10 &middot; 詳細',
    mcTitle='正確には何と言ったか？',

    l1why='小さいプール、横の入口。彼は一息に両方を言います――&ldquo;the classes '
          'are in the small pool, not the main one, so come through the side '
          'entrance&rdquo;――そのため、元の文ではなく記憶から答える人は、二つを入'
          'れ替えてしまいます。',
    l2why='図書館の裏の通りは5時以降無料です。駐車場はありますが、6時には満車に'
          'なると彼は言っています。&ldquo;free after five&rdquo; は通りの話で、'
          '駐車場の話ではありません。',
    l4why='建物が改装されたからです。友人と地元の新聞は、どちらも一行前の彼女の'
          '最後の質問に出てきます。まさにそのために置かれているのです。',

    actTitle='電話を受ける',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、それぞれ用紙を一枚持ちます。一人はセンターかホテルか整'
                  '備工場の受付、もう一人は問い合わせる人です。受付は名前を一つつ'
                  'づりで伝え、電話番号を一つ言い、一度言い直さなければなりません。'
                  '電話をかけた人は用紙を埋め、最後に読み上げます。',
    actSpeak1='つづりを言う人：名字は普通の速さで一度だけ言いましょう。ゆっくりに'
              'せず、頼まれない限り繰り返さないこと。',
    actSpeak2='電話をかけた人：最後に用紙全体を読み上げましょう。間違った文字一つ'
              'が1点なので、単語ではなく文字を言うこと。',
    actSpeak3='通話のどこかで、すでに伝えた情報を一つ変えましょう。パートナーが気'
              'づくかどうか見てみます。',
    actWriteKind='ライティング · 100–150 語',
    actWriteBrief='自分で選んだ予約――講座、配達、修理――のための用紙の6行を書き、'
                  'それぞれの横に、どんな種類の答えが必要かを書きましょう：名前、'
                  '曜日、数字、値段。試験がくれる30秒の準備を、前もって済ませて'
                  'おくのです。',
    actPlaceholder='Surname: … (a name, spelled)',

    f1why='一文字ずつ、一度だけつづりが言われます。話し手が文字を言い始めた瞬間、'
          '答えを書き取らされているのです。',
    f2why='&ldquo;Double oh&rdquo; はゼロ二つ、&ldquo;oh&rdquo; はゼロ一つで'
          'す：07700 900 642。11個のばらばらの数字を待っている受験者には、11個は'
          '決して聞こえません。',
    f3why='彼は Tuesday と言って、すぐに言い直します：&ldquo;sorry, I beg your '
          'pardon, that&rsquo;s the children.&rdquo; 答えは必ず言い直した方です。',
    f4why='6時半。6時20分はプールサイドに着いているべき時刻で、まさに間違えて書か'
          'せるために置かれた、近くの数字です。',
    f5why='10。値段の直前に一度だけ言われます。その後の会員料金は同じ10週間分で'
          'す――&ldquo;the whole term&rdquo;。',
    f6why='35が先に言われますが、それは非会員の月額料金です。彼女は入会するので、'
          '学期全体で42を払います。',
    f7why='水着とタオルは &ldquo;the usual&rdquo; です。キャップは人が忘れるもの'
          'として彼がわざわざ取り上げていて、Section 1 の答えはほとんどいつも、強'
          '調される品物です。',
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
