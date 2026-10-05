# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 4.

All ten IELTS languages (`ielts_langs.LANGS`), teach cards in the
six-item form. English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-10-05 (conventions in `ielts_langs.py`).

The answers on this deck come straight out of the recording — transpiration,
interception, twelve hundred — so they stay English in every gloss. What
translates is the rule: how a lecture signposts itself, and what a word limit
does to a right answer written too long.
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
    coverTitle='Section 4 &mdash; <em>the lecture</em>',
    coverSub='One speaker, one long run, and the only section with no break '
             'in the middle',
    chipLevel='C1', chipFocus='Listening &middot; Section 4',
    chipCount='10 questions',

    t1Eyebrow='Before you listen',
    t1Title='It is hard for one reason, and it is not the vocabulary',
    t1ah='There is no pause',
    t1ab='Sections 1 to 3 stop halfway so you can read the next questions. '
         'Section 4 runs straight through. One speaker, no second voice to '
         'interrupt and repeat &mdash; so if you lose your place there is '
         'nothing to grab hold of.',
    t1an='Read all the questions before you press play. There will be no '
         'moment later in which to do it.',
    t1bh='Follow the signposts, not the sentences',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; <em>the '
         'third function</em> &middot; <em>finally</em>. A lecturer tells you '
         'where you are roughly once a minute, and those words are the only '
         'handholds in a long run of continuous speech.',
    t1bn='If you have drifted, stop trying to catch up on meaning and wait for '
         'the next signpost. It is coming.',
    t1ch='The word limit is the marker',
    t1cb='Note completion takes the words from the recording, so the answer is '
         'rarely hard to hear. What loses the mark is writing three words '
         'where two were allowed, or adding a word the gap already has beside '
         'it.',
    t1cn='Read what is printed either side of the gap. Half the over-long '
         'answers repeat a word that was already there.',

    audEyebrow='The recording',
    audTitle='You will hear it once, straight through',
    audNote='Part of a lecture on the role of trees in cities, with no break '
            'in the middle. Read all ten questions on the next slides first, '
            'then press play &mdash; here, or in the bar at the foot of any '
            'question slide. It keeps playing while you answer.',

    notesEyebrow='Questions 1&ndash;10 &middot; Complete the notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='Every answer is said aloud, in order. Two come with a second '
              'number beside them, and only one of each pair counts.',

    t2Eyebrow='After the recording',
    t2Title='The four places a lecture takes its marks',
    t2ah='The term defined in passing',
    t2ab='<em>The technical term is interception loss</em> &mdash; and then an '
         'explanation. When a lecturer says <em>the technical term is</em> or '
         '<em>that is</em>, a markable word has just gone past.',
    t2an='The definition is help, not the answer. The answer is usually the '
         'term itself.',
    t2bh='The number that is corrected',
    t2bb='Eight hundred pounds, then <em>no, I should be accurate</em>, then '
         'twelve hundred. The Section 1 correction trap, arriving at Section 4 '
         'speed where there is no second speaker to confirm it.',
    t2bn='And two degrees is the answer while four is quoted and then called '
         '"an upper bound" &mdash; a figure that gets qualified is not the '
         'figure they want.',
    t2ch='The aside that still counts',
    t2cb='Twenty seconds about roots and pavements, which the lecturer flags as '
         'a digression. It is off the main argument &mdash; and it still holds '
         'an answer, Question 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. A digression is a change '
         'of subject, not a rest.',

    actTitle='Give the three-minute lecture',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. Take something you know well and talk for three '
                  'minutes without stopping, with three numbered points. Your '
                  'partner takes notes and is not allowed to ask anything. '
                  'Then compare their notes with what you meant to say.',
    actSpeak1='Speaker: signpost every point out loud &mdash; <em>first</em>, '
              '<em>the second reason</em>, <em>finally</em>. Count them as you '
              'go.',
    actSpeak2='Correct one number halfway through, the way a real lecturer '
              'does, and see whether it reaches the notes.',
    actSpeak3='Take one twenty-second digression and announce it as one. Your '
              'partner notes its one point, in three words or fewer.',
    actWriteKind='Writing · 120–180 words',
    actWriteBrief='Write the notes a listener should have ended up with: your '
                  'three points, the numbers, and the one term you defined. '
                  'Set a word limit at the top &mdash; ONE WORD AND/OR A '
                  'NUMBER is the strictest the test uses &mdash; and keep every '
                  'line inside it.',
    actPlaceholder='Point 1: … / cooled by: …',
)

# The note explanations sit beside their answers in the data module, which
# keeps the only copy of the English; they were plain strings there until
# 2026-09-23, so German and Spanish learners read them in English.
from ieltslisten_s4_data import NOTES
T['en'].update(('n%dwhy' % (i + 1), r[2]) for i, r in enumerate(NOTES))

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 4 &mdash; <em>die Vorlesung</em>',
    coverSub='Ein Sprecher, ein langer Block, und der einzige Teil ohne Pause '
             'in der Mitte',
    chipLevel='C1', chipFocus='Listening &middot; Section 4',
    chipCount='10 Fragen',

    t1Eyebrow='Bevor du hörst',
    t1Title='Schwer ist es aus einem Grund &mdash; und der ist nicht der Wortschatz',
    t1ah='Es gibt keine Pause',
    t1ab='Teil 1 bis 3 halten in der Mitte an, damit du die nächsten Fragen '
         'lesen kannst. Teil 4 läuft durch. Ein Sprecher, keine zweite Stimme, '
         'die unterbricht und wiederholt &mdash; wer den Faden verliert, hat '
         'nichts zum Festhalten.',
    t1an='Lies alle Fragen, bevor du Play drückst. Später gibt es dafür keinen '
         'Moment mehr.',
    t1bh='Folge den Wegweisern, nicht den Sätzen',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; <em>the '
         'third function</em> &middot; <em>finally</em>. Etwa einmal pro '
         'Minute sagt dir ein Vortragender, wo du bist, und das sind die '
         'einzigen Haltegriffe in einem langen Stück Dauerrede.',
    t1bn='Wenn du abgedriftet bist, hör auf, inhaltlich aufzuholen, und warte '
         'auf den nächsten Wegweiser. Er kommt.',
    t1ch='Das Wortlimit ist der Prüfstein',
    t1cb='Notizen-Ergänzen nimmt die Wörter aus der Aufnahme, die Antwort ist '
         'also selten schwer zu hören. Den Punkt kostet, wer drei Wörter '
         'schreibt, wo zwei erlaubt waren, oder ein Wort ergänzt, das neben '
         'der Lücke schon steht.',
    t1cn='Lies, was links und rechts der Lücke gedruckt ist. Die Hälfte der zu '
         'langen Antworten wiederholt ein Wort, das schon da war.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal, ohne Unterbrechung',
    audNote='Ein Ausschnitt aus einer Vorlesung über die Rolle von Bäumen in '
            'Städten, ohne Pause in der Mitte. Lies zuerst alle zehn Fragen auf '
            'den nächsten Folien, dann drücke Play &mdash; hier oder in der '
            'Leiste unten auf jeder Fragenfolie. Die Aufnahme läuft weiter, '
            'während du antwortest.',

    notesEyebrow='Fragen 1&ndash;10 &middot; Notizen vervollständigen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Jede Antwort wird laut gesagt, der Reihe nach. Zwei kommen mit '
              'einer zweiten Zahl daneben, und nur eine von beiden zählt.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Die vier Stellen, an denen eine Vorlesung Punkte holt',
    t2ah='Der nebenbei definierte Begriff',
    t2ab='<em>The technical term is interception loss</em> &mdash; und dann '
         'eine Erklärung. Wenn jemand <em>the technical term is</em> oder '
         '<em>that is</em> sagt, ist gerade ein punktewertes Wort vorbeigekommen.',
    t2an='Die Erklärung ist Hilfe, nicht die Antwort. Die Antwort ist meist '
         'der Begriff selbst.',
    t2bh='Die korrigierte Zahl',
    t2bb='Achthundert Pfund, dann <em>no, I should be accurate</em>, dann '
         'zwölfhundert. Die Korrekturfalle aus Teil 1, jetzt im Tempo von '
         'Teil 4 und ohne zweiten Sprecher, der sie bestätigt.',
    t2bn='Und zwei Grad ist die Antwort, während vier genannt und dann „an '
         'upper bound“ genannt wird &mdash; eine Zahl, die eingeschränkt wird, '
         'ist nicht die gesuchte.',
    t2ch='Der Einschub, der trotzdem zählt',
    t2cb='Zwanzig Sekunden über Wurzeln und Gehwege, die der Vortragende als '
         'Abschweifung ankündigt. Sie liegen neben dem Hauptargument &mdash; '
         'und enthalten trotzdem eine Antwort, Frage 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Eine Abschweifung ist ein '
         'Themenwechsel, keine Pause.',

    actTitle='Halte die Drei-Minuten-Vorlesung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Nimm etwas, das du gut kennst, und rede drei '
                  'Minuten ohne Pause, mit drei nummerierten Punkten. Dein '
                  'Partner macht Notizen und darf nichts fragen. Danach '
                  'vergleicht ihr die Notizen mit dem, was du sagen wolltest.',
    actSpeak1='Sprecher: kündige jeden Punkt laut an &mdash; <em>first</em>, '
              '<em>the second reason</em>, <em>finally</em>. Zähl sie mit.',
    actSpeak2='Korrigiere auf halber Strecke eine Zahl, wie es echte '
              'Vortragende tun, und schau, ob es in den Notizen ankommt.',
    actSpeak3='Mach eine Abschweifung von zwanzig Sekunden und kündige sie als '
              'solche an. Dein Partner notiert ihren einen Punkt, in höchstens '
              'drei Wörtern.',
    actWriteKind='Schreiben · 120–180 Wörter',
    actWriteBrief='Schreib die Notizen auf, mit denen ein Zuhörer hätte '
                  'enden sollen: deine drei Punkte, die Zahlen und der eine '
                  'Begriff, den du definiert hast. Setz oben ein Wortlimit '
                  '&mdash; ONE WORD AND/OR A NUMBER ist das strengste der '
                  'Prüfung &mdash; und halte jede Zeile darin.',
    actPlaceholder='Point 1: … / cooled by: …',

    # Questions 1-10: the English is registered from the data module, below.
    n1why='Infrastructure, im ersten Satz: die These, die der ganze Vortrag '
          'stützen soll.',
    n2why='Transpiration, im selben Atemzug erklärt als „releasing water '
          'vapour through the leaves“. Die Antwort ist der Fachbegriff, nicht '
          'die Erklärung.',
    n3why='Zwei, für Europa. Vier wird für Australien genannt und sofort ein '
          '„upper bound“ genannt &mdash; eine Zahl, die gleich eingeschränkt '
          'wird, ist nicht die Antwort.',
    n4why='„The technical term is interception loss“ &mdash; deutlicher kann '
          'nichts anzeigen, dass ein Wort einen Punkt wert ist.',
    n5why='Zwanzig bis dreißig. Was neben der Lücke gedruckt steht, zeigt, '
          'welche Hälfte der Spanne gefragt ist.',
    n6why='Pit, mitten in dem Einschub, den der Vortragende als Abschweifung '
          'ankündigt. Ein Einschub liegt neben dem Hauptargument, leer ist er '
          'nicht.',
    n7why='Air quality, und der Vortragende bewertet es selbst &mdash; „the '
          'weakest evidence of the three“. Wer seine eigenen Punkte ordnet, '
          'liefert dir die Struktur gleich mit.',
    n8why='Trap. Die Einschränkung folgt direkt auf die Behauptung, die sie '
          'begrenzt &mdash; Bäume fangen Feinstaub ein, und sie können auch die '
          'verschmutzte Luft einschließen. Dasselbe Verb, die umgekehrte '
          'Wirkung.',
    n9why='Zwölfhundert. Achthundert kommt zuerst und wird im selben Satz '
          'korrigiert &mdash; „no, I should be accurate“ &mdash; die '
          'Korrekturfalle aus Section 1 im Tempo von Section 4.',
    n10why='Watering &mdash; „the watering, not the planting“. In der letzten '
           'Zeile eines Vortrags sitzt seine Pointe, und der Gegensatz kommt im '
           'selben Atemzug.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 4 &mdash; <em>la conferencia</em>',
    coverSub='Una sola voz, un tramo largo, y la única parte sin pausa a '
             'mitad',
    chipLevel='C1', chipFocus='Listening &middot; Section 4',
    chipCount='10 preguntas',

    t1Eyebrow='Antes de escuchar',
    t1Title='Es difícil por un motivo, y no es el vocabulario',
    t1ah='No hay pausa',
    t1ab='Las secciones 1 a 3 paran a mitad para que leas las preguntas '
         'siguientes. La 4 va de seguido. Una sola voz, sin nadie que '
         'interrumpa y repita: si pierdes el hilo, no hay de dónde agarrarse.',
    t1an='Lee todas las preguntas antes de darle a reproducir. Luego no habrá '
         'ningún momento para hacerlo.',
    t1bh='Sigue las señales, no las frases',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; <em>the '
         'third function</em> &middot; <em>finally</em>. Más o menos una vez '
         'por minuto te dicen dónde estás, y esas palabras son los únicos '
         'asideros en un tramo largo de habla seguida.',
    t1bn='Si te has despistado, deja de intentar recuperar el sentido y espera '
         'a la siguiente señal. Va a llegar.',
    t1ch='El límite de palabras es lo que marca',
    t1cb='Completar notas toma las palabras de la grabación, así que la '
         'respuesta rara vez cuesta oírla. El punto se pierde al escribir tres '
         'palabras donde cabían dos, o al añadir una palabra que ya está junto '
         'al hueco.',
    t1cn='Lee lo que hay impreso a ambos lados del hueco. La mitad de las '
         'respuestas largas de más repiten una palabra que ya estaba.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez, de seguido',
    audNote='Parte de una conferencia sobre el papel de los árboles en las '
            'ciudades, sin pausa a mitad. Lee primero las diez preguntas de las '
            'diapositivas siguientes y luego dale a reproducir, aquí o en la '
            'barra de abajo de cualquier pregunta. Sigue sonando mientras '
            'respondes.',

    notesEyebrow='Preguntas 1&ndash;10 &middot; Completa las notas',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Todas las respuestas se dicen en voz alta, en orden. Dos llegan '
              'con un segundo número al lado, y solo uno de los dos vale.',

    t2Eyebrow='Después de la grabación',
    t2Title='Los cuatro sitios donde una conferencia se lleva los puntos',
    t2ah='El término definido de pasada',
    t2ab='<em>The technical term is interception loss</em>, y luego una '
         'explicación. Cuando alguien dice <em>the technical term is</em> o '
         '<em>that is</em>, acaba de pasar una palabra que puntúa.',
    t2an='La definición es ayuda, no la respuesta. La respuesta suele ser el '
         'término.',
    t2bh='El número que se corrige',
    t2bb='Ochocientas libras, luego <em>no, I should be accurate</em>, luego '
         'mil doscientas. La trampa de corrección de la Section 1, a la '
         'velocidad de la 4 y sin un segundo hablante que lo confirme.',
    t2bn='Y dos grados es la respuesta, mientras que cuatro se cita y se llama '
         '«an upper bound»: una cifra que se matiza no es la que piden.',
    t2ch='El inciso que también cuenta',
    t2cb='Veinte segundos sobre raíces y aceras, que el conferenciante anuncia '
         'como digresión. Se sale del argumento principal, y aun así contiene '
         'una respuesta, la pregunta 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Una digresión es un '
         'cambio de tema, no un descanso.',

    actTitle='Da la conferencia de tres minutos',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Coge algo que conozcas bien y habla tres '
                  'minutos sin parar, con tres puntos numerados. Tu compañero '
                  'toma notas y no puede preguntar nada. Luego comparad sus '
                  'notas con lo que querías decir.',
    actSpeak1='Quien habla: señaliza cada punto en voz alta &mdash; '
              '<em>first</em>, <em>the second reason</em>, <em>finally</em>. '
              'Ve contándolos.',
    actSpeak2='Corrige un número a mitad de camino, como hace un '
              'conferenciante de verdad, y mira si llega a las notas.',
    actSpeak3='Haz una digresión de veinte segundos y anúnciala como tal. Tu '
              'compañero apunta su única idea, en tres palabras como mucho.',
    actWriteKind='Escritura · 120–180 palabras',
    actWriteBrief='Escribe las notas con las que debería haber acabado quien '
                  'te escuchaba: tus tres puntos, las cifras y el término que '
                  'definiste. Pon arriba un límite de palabras &mdash; ONE '
                  'WORD AND/OR A NUMBER es el más estricto del examen &mdash; y '
                  'que cada línea lo respete.',
    actPlaceholder='Point 1: … / cooled by: …',

    # Questions 1-10: the English is registered from the data module, below.
    n1why='Infrastructure, en la primera frase: la tesis que toda la '
          'conferencia está construida para defender.',
    n2why='Transpiration, definida en la misma frase como «releasing water '
          'vapour through the leaves». La respuesta es el término, no la '
          'definición.',
    n3why='Dos, para Europa. Cuatro se cita para Australia y enseguida se '
          'llama «upper bound»: una cifra que se matiza al momento no es la '
          'respuesta.',
    n4why='«The technical term is interception loss»: no hay señal más clara '
          'de que una palabra vale un punto.',
    n5why='De veinte a treinta. Lo que está impreso junto al hueco muestra qué '
          'mitad del intervalo se pide.',
    n6why='Pit, dentro del inciso que el profesor anuncia como digresión. Un '
          'inciso se sale del argumento principal, pero no está vacío.',
    n7why='Air quality, y el propio profesor lo califica: «the weakest '
          'evidence of the three». Un profesor que ordena sus propios '
          'argumentos te está dando la estructura.',
    n8why='Trap. La complicación llega justo después de la afirmación que '
          'limita: los árboles atrapan partículas, y también pueden atrapar el '
          'aire contaminado. El mismo verbo, el efecto contrario.',
    n9why='Mil doscientas. Ochocientas se dice primero y se corrige en la '
          'misma frase («no, I should be accurate»): la trampa de la '
          'corrección de la Section 1, a la velocidad de la Section 4.',
    n10why='Watering: «the watering, not the planting». La última línea de una '
           'conferencia es donde remata su idea, y el contraste va en la misma '
           'frase.',
)


# ── French ──────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Section 4 — <em>le cours magistral</em>',
    coverSub='Un seul orateur, une longue séquence, et la seule section sans '
             'pause au milieu',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 questions',
    t1Eyebrow="Avant l'écoute",
    t1Title="C'est difficile pour une seule raison, et ce n'est pas le "
            'vocabulaire',
    t1ah="Il n'y a pas de pause",
    t1ab="Les sections 1 à 3 s'arrêtent à mi-parcours pour vous laisser lire "
         "les questions suivantes. La section 4 file d'une traite. Un seul "
         'orateur, aucune seconde voix pour interrompre et répéter — si vous '
         "perdez le fil, il n'y a rien à quoi vous raccrocher.",
    t1an="Lisez toutes les questions avant de lancer la lecture. Il n'y aura "
         'plus aucun moment pour le faire ensuite.',
    t1bh='Suivez les balises, pas les phrases',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; <em>finally</em>. Un '
         'conférencier vous dit où vous en êtes environ une fois par minute, '
         'et ces mots sont les seules prises dans une longue séquence de '
         'parole continue.',
    t1bn="Si vous avez décroché, cessez d'essayer de rattraper le sens et "
         'attendez la balise suivante. Elle arrive.',
    t1ch='La limite de mots est le correcteur',
    t1cb="Les notes à compléter reprennent les mots de l'enregistrement, la "
         'réponse est donc rarement difficile à entendre. Ce qui fait perdre '
         "le point, c'est écrire trois mots quand deux étaient permis, ou "
         "ajouter un mot que l'espace a déjà à côté de lui.",
    t1cn="Lisez ce qui est imprimé de chaque côté de l'espace. La moitié des "
         'réponses trop longues répètent un mot qui était déjà là.',
    audEyebrow="L'enregistrement",
    audTitle="Vous l'entendrez une fois, d'une traite",
    audNote='Un extrait de cours sur le rôle des arbres en ville, sans pause au '
            "milieu. Lisez d'abord les dix questions des diapositives "
            'suivantes, puis lancez la lecture — ici, ou dans la barre au bas '
            "de n'importe quelle diapositive de question. L'enregistrement "
            'continue pendant que vous répondez.',
    notesEyebrow='Questions 1–10 &middot; Complétez les notes',
    notesTitle='Écrivez UN MOT ET/OU UN NOMBRE dans chaque espace',
    notesHint="Chaque réponse est dite à voix haute, dans l'ordre. Deux arrivent "
              'avec un second nombre à côté, et un seul de chaque paire compte.',
    t2Eyebrow="Après l'enregistrement",
    t2Title='Les quatre endroits où un cours place ses points',
    t2ah='Le terme défini en passant',
    t2ab='<em>The technical term is interception loss</em> — puis une '
         'explication. Quand un conférencier dit <em>the technical term '
         'is</em> ou <em>that is</em>, un mot qui vaut un point vient de '
         'passer.',
    t2an='La définition est une aide, pas la réponse. La réponse est '
         'généralement le terme lui-même.',
    t2bh='Le nombre qui est corrigé',
    t2bb='Huit cents livres, puis <em>no, I should be accurate</em>, puis '
         'douze cents. Le piège de la correction de la section 1, qui arrive '
         'à la vitesse de la section 4, sans second orateur pour le '
         'confirmer.',
    t2bn='Et deux degrés est la réponse alors que quatre est cité puis '
         "qualifié d'« an upper bound » — un chiffre qu'on nuance n'est pas "
         "celui qu'on vous demande.",
    t2ch='La digression qui compte quand même',
    t2cb='Vingt secondes sur les racines et les trottoirs, que le '
         "conférencier signale comme une digression. C'est hors de "
         "l'argument principal — et cela contient quand même une réponse, la "
         'question 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Une digression est un '
         'changement de sujet, pas une pause.',
    actTitle='Donnez le cours de trois minutes',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='Par deux. Prenez un sujet que vous connaissez bien et parlez trois '
                  'minutes sans vous arrêter, avec trois points numérotés. Votre '
                  "partenaire prend des notes et n'a pas le droit de poser de "
                  'question. Comparez ensuite ses notes avec ce que vous vouliez '
                  'dire.',
    actSpeak1='Orateur : balisez chaque point à voix haute — <em>first</em>, '
              '<em>the second reason</em>, <em>finally</em>. Comptez-les au fur '
              'et à mesure.',
    actSpeak2='Corrigez un nombre à mi-parcours, comme le fait un vrai '
              "conférencier, et voyez s'il arrive jusqu'aux notes.",
    actSpeak3='Faites une digression de vingt secondes et annoncez-la comme '
              'telle. Votre partenaire note son unique idée, en trois mots ou '
              'moins.',
    actWriteKind='Writing · 120–180 mots',
    actWriteBrief="Rédigez les notes qu'un auditeur devrait avoir à la fin : vos "
                  'trois points, les nombres, et le terme que vous avez défini. Fixez '
                  'une limite de mots en haut — ONE WORD AND/OR A NUMBER est la plus '
                  'stricte que le test utilise — et tenez chaque ligne dedans.',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure, dans la première phrase : la thèse que tout le '
          'cours est construit pour soutenir.',
    n2why='Transpiration, défini dans le même souffle que « releasing water '
          'vapour through the leaves ». La réponse est le terme, pas la '
          'définition.',
    n3why="Deux, pour l'Europe. Quatre est cité pour l'Australie et aussitôt "
          "qualifié d'« upper bound » — un chiffre qu'on nuance n'est pas la "
          'réponse.',
    n4why='« The technical term is interception loss » — le signal le plus '
          "clair qui soit qu'un mot vaut un point.",
    n5why="Vingt à trente. Ce qui est imprimé à côté de l'espace indique "
          'quelle moitié de la fourchette il attend.',
    n6why="Pit, à l'intérieur de la digression que le conférencier signale "
          "comme telle. Une digression est hors de l'argument principal, pas "
          'vide.',
    n7why='Air quality, et le conférencier le classe lui-même — « the weakest '
          'evidence of the three ». Un conférencier qui hiérarchise ses '
          'propres points vous tend la structure.',
    n8why="Trap. La complication arrive juste après l'affirmation qu'elle "
          'limite — les arbres piègent les particules, et ils peuvent aussi '
          "piéger l'air pollué. Même verbe, effet opposé.",
    n9why="Douze cents. Huit cents est dit d'abord et corrigé dans la même "
          'phrase — « no, I should be accurate » — le piège de la correction '
          'de la section 1 à la vitesse de la section 4.',
    n10why='Watering — « the watering, not the planting ». La dernière phrase '
           "d'un cours est là où il porte son point, et le contraste est dit "
           'dans le même souffle.',
)

# ── Italian ─────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Section 4 — <em>la lezione</em>',
    coverSub="Un solo parlante, un unico lungo tratto, e l'unica sezione senza "
             'pausa a metà',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 domande',
    t1Eyebrow='Prima di ascoltare',
    t1Title='È difficile per un solo motivo, e non è il lessico',
    t1ah="Non c'è pausa",
    t1ab='Le sezioni da 1 a 3 si fermano a metà per farti leggere le domande '
         'successive. La sezione 4 fila dritta fino alla fine. Un solo '
         'parlante, nessuna seconda voce che interrompa e ripeta — se perdi '
         "il filo, non c'è nulla a cui aggrapparti.",
    t1an='Leggi tutte le domande prima di premere play. Dopo non ci sarà '
         'nessun momento per farlo.',
    t1bh='Segui i segnali, non le frasi',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; <em>finally</em>. Chi tiene '
         'la lezione ti dice dove sei circa una volta al minuto, e quelle '
         'parole sono gli unici appigli in un lungo tratto di parlato '
         'continuo.',
    t1bn='Se ti sei perso, smetti di cercare di recuperare il senso e '
         'aspetta il segnale successivo. Sta arrivando.',
    t1ch='Il limite di parole è il correttore',
    t1cb='Il completamento degli appunti prende le parole dalla '
         'registrazione, quindi la risposta è raramente difficile da '
         'sentire. Ciò che fa perdere il punto è scrivere tre parole dove ne '
         'erano permesse due, o aggiungere una parola che lo spazio ha già '
         'accanto.',
    t1cn='Leggi ciò che è stampato su entrambi i lati dello spazio. Metà '
         'delle risposte troppo lunghe ripete una parola che era già lì.',
    audEyebrow='La registrazione',
    audTitle='La sentirai una volta, tutta di seguito',
    audNote='Parte di una lezione sul ruolo degli alberi in città, senza pausa '
            'a metà. Leggi prima tutte e dieci le domande nelle slide '
            'successive, poi premi play — qui, o nella barra in fondo a '
            'qualsiasi slide con una domanda. Continua a suonare mentre '
            'rispondi.',
    notesEyebrow='Domande 1–10 &middot; Completa gli appunti',
    notesTitle='Scrivi UNA PAROLA E/O UN NUMERO in ogni spazio',
    notesHint='Ogni risposta viene detta ad alta voce, in ordine. Due arrivano '
              'con un secondo numero accanto, e di ogni coppia ne conta uno solo.',
    t2Eyebrow='Dopo la registrazione',
    t2Title='I quattro punti in cui una lezione piazza i suoi punteggi',
    t2ah='Il termine definito di passaggio',
    t2ab='<em>The technical term is interception loss</em> — e poi una '
         'spiegazione. Quando chi parla dice <em>the technical term is</em> '
         'o <em>that is</em>, una parola che vale un punto è appena passata.',
    t2an='La definizione è un aiuto, non la risposta. La risposta è di '
         'solito il termine stesso.',
    t2bh='Il numero che viene corretto',
    t2bb='Ottocento sterline, poi <em>no, I should be accurate</em>, poi '
         'milleduecento. La trappola della correzione della sezione 1, che '
         "arriva alla velocità della sezione 4, dove non c'è un secondo "
         'parlante a confermarla.',
    t2bn='E due gradi è la risposta mentre quattro viene citato e poi '
         'definito «an upper bound» — una cifra che viene ridimensionata non '
         'è quella che vogliono.',
    t2ch='La digressione che conta comunque',
    t2cb='Venti secondi su radici e marciapiedi, che chi parla segnala come '
         "una digressione. È fuori dall'argomento principale — e contiene "
         'comunque una risposta, la domanda 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Una digressione è un '
         'cambio di argomento, non una pausa.',
    actTitle='Tieni la lezione di tre minuti',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia. Prendi qualcosa che conosci bene e parlane per tre '
                  'minuti senza fermarti, con tre punti numerati. Il tuo compagno '
                  'prende appunti e non può chiedere nulla. Poi confrontate i suoi '
                  'appunti con ciò che volevi dire.',
    actSpeak1='Chi parla: segnala ogni punto ad alta voce — <em>first</em>, '
              '<em>the second reason</em>, <em>finally</em>. Contali man mano.',
    actSpeak2='Correggi un numero a metà strada, come fa un vero docente, e '
              'guarda se arriva negli appunti.',
    actSpeak3='Fai una digressione di venti secondi e annunciala come tale. Il '
              "tuo compagno ne annota l'unico punto, in tre parole o meno.",
    actWriteKind='Writing · 120–180 parole',
    actWriteBrief='Scrivi gli appunti con cui un ascoltatore dovrebbe essere uscito: '
                  "i tuoi tre punti, i numeri e l'unico termine che hai definito. "
                  'Metti un limite di parole in alto — ONE WORD AND/OR A NUMBER è il '
                  'più severo che il test usi — e tieni ogni riga dentro quel limite.',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure, nella prima frase: la tesi che tutta la lezione è '
          'costruita per sostenere.',
    n2why='Transpiration, definito nello stesso respiro di «releasing water '
          'vapour through the leaves». La risposta è il termine, non la '
          'definizione.',
    n3why="Due, per l'Europa. Quattro viene citato per l'Australia e definito "
          'subito «upper bound» — una cifra che viene ridimensionata non è la '
          'risposta.',
    n4why='«The technical term is interception loss» — il segnale più chiaro '
          'che esista che una parola vale un punto.',
    n5why='Da venti a trenta. Ciò che è stampato accanto allo spazio mostra '
          "quale metà dell'intervallo vuole.",
    n6why='Pit, dentro la digressione che chi parla segnala come tale. Una '
          "digressione è fuori dall'argomento principale, non vuota.",
    n7why='Air quality, e chi parla la classifica da sé — «the weakest '
          'evidence of the three». Un docente che mette in ordine i propri '
          'punti ti sta consegnando la struttura.',
    n8why="Trap. La complicazione arriva subito dopo l'affermazione che "
          'limita — gli alberi intrappolano il particolato, e possono '
          "intrappolare anche l'aria inquinata. Stesso verbo, effetto "
          'opposto.',
    n9why='Milleduecento. Ottocento viene detto prima e corretto nella stessa '
          'frase — «no, I should be accurate» — la trappola della correzione '
          'della sezione 1 alla velocità della sezione 4.',
    n10why="Watering — «the watering, not the planting». L'ultima riga di una "
           'lezione è dove piazza il suo punto, e il contrasto viene detto '
           'nello stesso respiro.',
)

# ── Portuguese ──────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Section 4 — <em>a palestra</em>',
    coverSub='Um só orador, um longo trecho contínuo, e a única secção sem pausa '
             'a meio',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 perguntas',
    t1Eyebrow='Antes de ouvir',
    t1Title='É difícil por uma só razão, e não é o vocabulário',
    t1ah='Não há pausa',
    t1ab='As secções 1 a 3 param a meio para leres as perguntas seguintes. A '
         'secção 4 segue de uma ponta à outra. Um só orador, nenhuma segunda '
         'voz para interromper e repetir — por isso, se perderes o fio, não '
         'há nada a que te agarrares.',
    t1an='Lê todas as perguntas antes de carregares em play. Mais tarde não '
         'haverá nenhum momento para o fazer.',
    t1bh='Segue os sinais, não as frases',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; <em>finally</em>. Quem dá a '
         'palestra diz-te onde estás mais ou menos uma vez por minuto, e '
         'essas palavras são os únicos pontos de apoio num longo trecho de '
         'fala contínua.',
    t1bn='Se te perdeste, deixa de tentar recuperar o sentido e espera pelo '
         'sinal seguinte. Ele vem aí.',
    t1ch='O limite de palavras é o corretor',
    t1cb='Completar as notas usa as palavras da gravação, por isso a '
         'resposta raramente é difícil de ouvir. O que perde o ponto é '
         'escrever três palavras onde eram permitidas duas, ou acrescentar '
         'uma palavra que o espaço já tem ao lado.',
    t1cn='Lê o que está impresso de cada lado do espaço. Metade das '
         'respostas demasiado longas repete uma palavra que já lá estava.',
    audEyebrow='A gravação',
    audTitle='Vais ouvi-la uma vez, de uma ponta à outra',
    audNote='Parte de uma palestra sobre o papel das árvores nas cidades, sem '
            'pausa a meio. Lê primeiro as dez perguntas nos diapositivos '
            'seguintes e depois carrega em play — aqui, ou na barra ao fundo de '
            'qualquer diapositivo de pergunta. Continua a tocar enquanto '
            'respondes.',
    notesEyebrow='Perguntas 1–10 &middot; Completa as notas',
    notesTitle='Escreve UMA PALAVRA E/OU UM NÚMERO em cada espaço',
    notesHint='Todas as respostas são ditas em voz alta, por ordem. Duas vêm com '
              'um segundo número ao lado, e só um de cada par conta.',
    t2Eyebrow='Depois da gravação',
    t2Title='Os quatro lugares onde uma palestra põe os seus pontos',
    t2ah='O termo definido de passagem',
    t2ab='<em>The technical term is interception loss</em> — e depois uma '
         'explicação. Quando quem fala diz <em>the technical term is</em> ou '
         '<em>that is</em>, acabou de passar uma palavra que vale um ponto.',
    t2an='A definição é uma ajuda, não a resposta. A resposta é normalmente '
         'o próprio termo.',
    t2bh='O número que é corrigido',
    t2bb='Oitocentas libras, depois <em>no, I should be accurate</em>, '
         'depois mil e duzentas. A armadilha da correção da secção 1, a '
         'chegar à velocidade da secção 4, onde não há um segundo orador '
         'para a confirmar.',
    t2bn='E dois graus é a resposta, enquanto quatro é citado e depois '
         'chamado «an upper bound» — um número que é relativizado não é o '
         'que eles querem.',
    t2ch='O aparte que conta na mesma',
    t2cb='Vinte segundos sobre raízes e passeios, que o orador assinala como '
         'uma digressão. Está fora do argumento principal — e mesmo assim '
         'contém uma resposta, a pergunta 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Uma digressão é uma '
         'mudança de assunto, não um descanso.',
    actTitle='Dá a palestra de três minutos',
    actUse='Usa pelo menos três:',
    actSpeakBrief='A pares. Pega em algo que conheças bem e fala três minutos sem '
                  'parar, com três pontos numerados. O teu colega toma notas e não '
                  'pode perguntar nada. Depois comparem as notas dele com o que '
                  'querias dizer.',
    actSpeak1='Orador: assinala cada ponto em voz alta — <em>first</em>, <em>the '
              'second reason</em>, <em>finally</em>. Conta-os à medida que '
              'avanças.',
    actSpeak2='Corrige um número a meio, como faz um verdadeiro professor, e vê '
              'se chega às notas.',
    actSpeak3='Faz uma digressão de vinte segundos e anuncia-a como tal. O teu '
              'colega anota o seu único ponto, em três palavras ou menos.',
    actWriteKind='Writing · 120–180 palavras',
    actWriteBrief='Escreve as notas com que um ouvinte devia ter ficado: os teus três '
                  'pontos, os números e o termo que definiste. Põe um limite de '
                  'palavras no topo — ONE WORD AND/OR A NUMBER é o mais rigoroso que '
                  'o teste usa — e mantém cada linha dentro dele.',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure, na primeira frase: a tese que toda a palestra foi '
          'construída para sustentar.',
    n2why='Transpiration, definido no mesmo fôlego que «releasing water '
          'vapour through the leaves». A resposta é o termo, não a definição.',
    n3why='Dois, para a Europa. Quatro é citado para a Austrália e logo '
          'chamado «upper bound» — um número que é relativizado não é a '
          'resposta.',
    n4why='«The technical term is interception loss» — o sinal mais claro que '
          'existe de que uma palavra vale um ponto.',
    n5why='Vinte a trinta. O que está impresso ao lado do espaço mostra que '
          'metade do intervalo ele quer.',
    n6why='Pit, dentro do aparte que o orador assinala como digressão. Um '
          'aparte está fora do argumento principal, não vazio.',
    n7why='Air quality, e o próprio orador a classifica — «the weakest '
          'evidence of the three». Um orador a ordenar os seus próprios '
          'pontos está a entregar-te a estrutura.',
    n8why='Trap. A complicação vem logo a seguir à afirmação que limita — as '
          'árvores retêm partículas, e podem reter também o ar poluído. O '
          'mesmo verbo, efeito oposto.',
    n9why='Mil e duzentas. Oitocentas é dito primeiro e corrigido na mesma '
          'frase — «no, I should be accurate» — a armadilha da correção da '
          'secção 1 à velocidade da secção 4.',
    n10why='Watering — «the watering, not the planting». A última linha de uma '
           'palestra é onde ela assenta a sua ideia, e o contraste é dito no '
           'mesmo fôlego.',
)

# ── Russian ─────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Section 4 — <em>лекция</em>',
    coverSub='Один говорящий, один длинный отрезок и единственный раздел без '
             'паузы в середине',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 вопросов',
    t1Eyebrow='Перед прослушиванием',
    t1Title='Это трудно по одной причине, и причина не в словаре',
    t1ah='Паузы нет',
    t1ab='Разделы с 1 по 3 останавливаются на середине, чтобы вы прочитали '
         'следующие вопросы. Раздел 4 идёт без остановки. Один говорящий, '
         'нет второго голоса, который перебьёт и повторит, — так что если вы '
         'потеряли место, ухватиться не за что.',
    t1an='Прочитайте все вопросы, прежде чем нажать play. Позже момента для '
         'этого не будет.',
    t1bh='Следите за указателями, а не за предложениями',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; <em>finally</em>. Лектор '
         'говорит вам, где вы находитесь, примерно раз в минуту, и эти слова '
         '— единственные опоры в длинном отрезке непрерывной речи.',
    t1bn='Если вы отстали, перестаньте догонять смысл и ждите следующего '
         'указателя. Он приближается.',
    t1ch='Лимит слов — это и есть проверяющий',
    t1cb='Заполнение заметок берёт слова из записи, поэтому ответ редко '
         'трудно расслышать. Балл теряют, написав три слова там, где '
         'разрешены два, или добавив слово, которое уже стоит рядом с '
         'пропуском.',
    t1cn='Прочитайте, что напечатано по обе стороны пропуска. Половина '
         'слишком длинных ответов повторяет слово, которое уже там было.',
    audEyebrow='Запись',
    audTitle='Вы услышите её один раз, без остановки',
    audNote='Фрагмент лекции о роли деревьев в городах, без паузы в середине. '
            'Сначала прочитайте все десять вопросов на следующих слайдах, затем '
            'нажмите play — здесь или на панели внизу любого слайда с вопросом. '
            'Запись продолжает играть, пока вы отвечаете.',
    notesEyebrow='Вопросы 1–10 &middot; Заполните заметки',
    notesTitle='Напишите ОДНО СЛОВО И/ИЛИ ЧИСЛО в каждый пропуск',
    notesHint='Каждый ответ произносится вслух, по порядку. Два приходят со '
              'вторым числом рядом, и из каждой пары засчитывается только одно.',
    t2Eyebrow='После записи',
    t2Title='Четыре места, где лекция раздаёт баллы',
    t2ah='Термин, определённый мимоходом',
    t2ab='<em>The technical term is interception loss</em> — и затем '
         'объяснение. Когда лектор говорит <em>the technical term is</em> '
         'или <em>that is</em>, только что прошло слово, за которое дают '
         'балл.',
    t2an='Определение — подсказка, а не ответ. Ответом обычно является сам '
         'термин.',
    t2bh='Число, которое исправляют',
    t2bb='Восемьсот фунтов, затем <em>no, I should be accurate</em>, затем '
         'тысяча двести. Ловушка с исправлением из раздела 1, пришедшая на '
         'скорости раздела 4, где нет второго говорящего, чтобы её '
         'подтвердить.',
    t2bn='И два градуса — ответ, тогда как четыре называют и тут же '
         'оговаривают как «an upper bound» — число, которое оговаривают, не '
         'то, что от вас хотят.',
    t2ch='Отступление, которое всё равно считается',
    t2cb='Двадцать секунд о корнях и тротуарах, которые лектор обозначает '
         'как отступление. Это вне главного рассуждения — и всё же там есть '
         'ответ, вопрос 6.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>. Отступление — смена '
         'темы, а не передышка.',
    actTitle='Прочитайте трёхминутную лекцию',
    actUse='Используйте не менее трёх:',
    actSpeakBrief='В парах. Возьмите то, что хорошо знаете, и говорите три минуты без '
                  'остановки, с тремя пронумерованными пунктами. Партнёр ведёт записи '
                  'и не имеет права ничего спрашивать. Затем сравните его записи с '
                  'тем, что вы хотели сказать.',
    actSpeak1='Говорящий: обозначайте каждый пункт вслух — <em>first</em>, '
              '<em>the second reason</em>, <em>finally</em>. Считайте их по ходу.',
    actSpeak2='Исправьте одно число на середине, как делает настоящий лектор, и '
              'посмотрите, дойдёт ли оно до записей.',
    actSpeak3='Сделайте одно двадцатисекундное отступление и объявите его '
              'таковым. Партнёр записывает его единственный пункт, не больше чем '
              'в трёх словах.',
    actWriteKind='Writing · 120–180 слов',
    actWriteBrief='Напишите заметки, с которыми слушатель должен был остаться: ваши '
                  'три пункта, числа и единственный термин, который вы определили. '
                  'Укажите лимит слов сверху — ONE WORD AND/OR A NUMBER — самый '
                  'строгий из тех, что использует тест, — и держите каждую строку в '
                  'его пределах.',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure, в первом предложении: тезис, ради которого '
          'выстроена вся лекция.',
    n2why='Transpiration, определённый на одном дыхании с «releasing water '
          'vapour through the leaves». Ответ — термин, а не определение.',
    n3why='Два, для Европы. Четыре называют для Австралии и сразу же '
          'оговаривают как «upper bound» — число, которое оговаривают, не '
          'ответ.',
    n4why='«The technical term is interception loss» — самый ясный из '
          'возможных сигналов, что слово стоит балла.',
    n5why='От двадцати до тридцати. То, что напечатано рядом с пропуском, '
          'показывает, какая половина диапазона нужна.',
    n6why='Pit, внутри отступления, которое лектор обозначает как таковое. '
          'Отступление вне главного рассуждения, но не пусто.',
    n7why='Air quality, и лектор сам его оценивает — «the weakest evidence of '
          'the three». Лектор, ранжирующий собственные пункты, вручает вам '
          'структуру.',
    n8why='Trap. Оговорка идёт сразу за утверждением, которое она '
          'ограничивает: деревья улавливают частицы — и могут удерживать и '
          'загрязнённый воздух. Тот же глагол, противоположный эффект.',
    n9why='Тысяча двести. Сначала сказано восемьсот и исправлено в том же '
          'предложении — «no, I should be accurate» — ловушка с исправлением '
          'из раздела 1 на скорости раздела 4.',
    n10why='Watering — «the watering, not the planting». Последняя строка '
           'лекции — там, где она ставит свою точку, и контраст произнесён на '
           'одном дыхании.',
)

# ── Arabic ──────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='<bdi>Section 4</bdi> — <em>المحاضرة</em>',
    coverSub='متكلم واحد، مقطع طويل واحد، والقسم الوحيد بلا توقف في المنتصف',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 أسئلة',
    t1Eyebrow='قبل الاستماع',
    t1Title='صعبٌ لسبب واحد، وليس هو المفردات',
    t1ah='لا توقف',
    t1ab='الأقسام من 1 إلى 3 تتوقف في المنتصف لتقرأ الأسئلة التالية. القسم 4 '
         'يمضي من أوله إلى آخره. متكلم واحد، ولا صوت ثانٍ يقاطع ويكرّر — فإن '
         'ضيّعت موضعك فلا شيء تتمسك به.',
    t1an='اقرأ كل الأسئلة قبل أن تضغط التشغيل. لن تجد لاحقًا لحظة لذلك.',
    t1bh='اتبع الإشارات، لا الجمل',
    t1bb='<em><bdi>First</bdi></em> &middot; <em><bdi>the second '
         'factor</bdi></em> &middot; <em><bdi>the third function</bdi></em> '
         '&middot; <em><bdi>finally</bdi></em>. يخبرك المحاضر أين أنت مرةً '
         'كل دقيقة تقريبًا، وهذه الكلمات هي المقابض الوحيدة في مقطع طويل من '
         'الكلام المتصل.',
    t1bn='إن انجرفت، فتوقف عن محاولة اللحاق بالمعنى وانتظر الإشارة التالية. '
         'إنها قادمة.',
    t1ch='حد الكلمات هو المصحّح',
    t1cb='إكمال الملاحظات يأخذ الكلمات من التسجيل، فنادرًا ما يكون الجواب '
         'صعب السمع. ما يُضيّع العلامة هو كتابة ثلاث كلمات حيث سُمح باثنتين، '
         'أو إضافة كلمة موجودة أصلًا بجانب الفراغ.',
    t1cn='اقرأ ما هو مطبوع على جانبي الفراغ. نصف الأجوبة الطويلة أكثر من '
         'اللازم تكرّر كلمة كانت هناك أصلًا.',
    audEyebrow='التسجيل',
    audTitle='ستسمعه مرة واحدة، من أوله إلى آخره',
    audNote='جزء من محاضرة عن دور الأشجار في المدن، بلا توقف في المنتصف. اقرأ '
            'الأسئلة العشرة كلها في الشرائح التالية أولًا، ثم اضغط التشغيل — '
            'هنا، أو في الشريط أسفل أي شريحة أسئلة. يستمر في التشغيل أثناء '
            'إجابتك.',
    notesEyebrow='الأسئلة 1–10 &middot; أكمل الملاحظات',
    notesTitle='اكتب كلمة واحدة و/أو رقمًا في كل فراغ',
    notesHint='كل جواب يُقال بصوت مسموع، بالترتيب. اثنان يأتيان ومعهما رقم ثانٍ '
              'بجانبهما، وواحد فقط من كل زوج هو المحتسب.',
    t2Eyebrow='بعد التسجيل',
    t2Title='المواضع الأربعة التي تضع فيها المحاضرة علاماتها',
    t2ah='المصطلح المعرَّف عرَضًا',
    t2ab='<em><bdi>The technical term is interception loss</bdi></em> — ثم '
         'شرح. حين يقول المحاضر <em><bdi>the technical term is</bdi></em> أو '
         '<em><bdi>that is</bdi></em>، فقد مرّت للتو كلمة تستحق علامة.',
    t2an='التعريف عون، لا جواب. الجواب عادةً هو المصطلح نفسه.',
    t2bh='الرقم الذي يُصحَّح',
    t2bb='ثمانمئة جنيه، ثم <em><bdi>no, I should be accurate</bdi></em>، ثم '
         'ألف ومئتان. فخّ التصحيح من القسم 1، يأتي بسرعة القسم 4 حيث لا '
         'متكلم ثانٍ يؤكده.',
    t2bn='ودرجتان هو الجواب بينما تُذكر أربع ثم تُوصف بأنها <bdi>"an upper '
         'bound"</bdi> — الرقم الذي يُقيَّد ليس الرقم المطلوب.',
    t2ch='الاستطراد الذي يُحتسب رغم ذلك',
    t2cb='عشرون ثانية عن الجذور والأرصفة، يصفها المحاضر بأنها استطراد. إنها '
         'خارج الحجة الرئيسية — ومع ذلك تحمل جوابًا، السؤال 6.',
    t2cn='<em><bdi>An aside</bdi></em> &middot; <em><bdi>somebody always '
         'asks</bdi></em> &middot; <em><bdi>that&rsquo;s a different '
         'lecture</bdi></em>. الاستطراد تغيير للموضوع، لا استراحة.',
    actTitle='ألقِ محاضرة الدقائق الثلاث',
    actUse='استعمل ثلاثًا على الأقل:',
    actSpeakBrief='في أزواج. خذ شيئًا تعرفه جيدًا وتحدث ثلاث دقائق دون توقف، بثلاث '
                  'نقاط مرقّمة. يدوّن شريكك الملاحظات ولا يُسمح له بأن يسأل شيئًا. ثم '
                  'قارنا ملاحظاته بما قصدت أن تقوله.',
    actSpeak1='المتكلم: أشِر إلى كل نقطة بصوت مسموع — <em><bdi>first</bdi></em>، '
              '<em><bdi>the second reason</bdi></em>، '
              '<em><bdi>finally</bdi></em>. وعُدّها وأنت تمضي.',
    actSpeak2='صحّح رقمًا واحدًا في المنتصف، كما يفعل المحاضر الحقيقي، وانظر هل '
              'يصل إلى الملاحظات.',
    actSpeak3='استطرد مرة واحدة عشرين ثانية وأعلن أنه استطراد. يدوّن شريكك نقطته '
              'الوحيدة، في ثلاث كلمات أو أقل.',
    actWriteKind='Writing · 120–180 كلمة',
    actWriteBrief='اكتب الملاحظات التي كان ينبغي أن يخرج بها المستمع: نقاطك الثلاث، '
                  'والأرقام، والمصطلح الوحيد الذي عرّفته. ضع حدًا للكلمات في الأعلى — '
                  '<bdi>ONE WORD AND/OR A NUMBER</bdi> هو الأصرم مما يستعمله الامتحان '
                  '— وأبقِ كل سطر داخله.',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='<bdi>Infrastructure</bdi>، في الجملة الأولى: الأطروحة التي بُنيت '
          'المحاضرة كلها لدعمها.',
    n2why='<bdi>Transpiration</bdi>، معرَّف في النفَس نفسه مع <bdi>"releasing '
          'water vapour through the leaves"</bdi>. الجواب هو المصطلح، لا '
          'التعريف.',
    n3why='اثنان، لأوروبا. تُذكر أربع لأستراليا وتُوصف فورًا بأنها '
          '<bdi>"upper bound"</bdi> — الرقم الذي يُقيَّد ليس الجواب.',
    n4why='<bdi>"The technical term is interception loss"</bdi> — أوضح إشارة '
          'ممكنة إلى أن كلمةً تستحق علامة.',
    n5why='عشرون إلى ثلاثين. ما هو مطبوع بجانب الفراغ يُظهر أي نصف من المدى '
          'مطلوب.',
    n6why='<bdi>Pit</bdi>، داخل الاستطراد الذي يصفه المحاضر بأنه استطراد. '
          'الاستطراد خارج الحجة الرئيسية، لا خالٍ.',
    n7why='<bdi>Air quality</bdi>، والمحاضر نفسه يصنّفها — <bdi>"the weakest '
          'evidence of the three"</bdi>. المحاضر الذي يرتّب نقاطه يسلّمك '
          'البنية.',
    n8why='<bdi>Trap</bdi>. يأتي التعقيد مباشرة بعد الادعاء الذي يحدّه — '
          'الأشجار تحتجز الجسيمات، ويمكنها أن تحتجز الهواء الملوَّث أيضًا. '
          'الفعل نفسه، والأثر معكوس.',
    n9why='ألف ومئتان. تُقال ثمانمئة أولًا وتُصحَّح في الجملة نفسها — '
          '<bdi>"no, I should be accurate"</bdi> — وهو فخّ التصحيح من القسم 1 '
          'بسرعة القسم 4.',
    n10why='<bdi>Watering</bdi> — <bdi>"the watering, not the planting"</bdi>. '
           'السطر الأخير من المحاضرة هو حيث تضع نقطتها، والتباين يُقال في '
           'النفَس نفسه.',
)

# ── Chinese ─────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Section 4 — <em>讲座</em>',
    coverSub='一位说话者，一段长篇连续讲话，也是唯一中间没有停顿的部分',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 道题',
    t1Eyebrow='听之前',
    t1Title='它难只有一个原因，而且不是词汇',
    t1ah='没有停顿',
    t1ab='第 1 到第 3 部分会在中途停下，让你阅读接下来的问题。第 4 '
         '部分一口气讲到底。只有一位说话者，没有第二个声音来打断和重复——所以一旦跟丢了，就没有任何东西可以抓住。',
    t1an='按播放之前先读完所有问题。之后不会再有时间去读。',
    t1bh='跟着路标走，而不是跟着句子',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; '
         '<em>finally</em>。讲者大约每分钟会告诉你一次讲到了哪里，而在一长段连续讲话里，这些词是唯一的抓手。',
    t1bn='如果你已经跟丢了，就别再试图追回意思，等下一个路标。它马上就来。',
    t1ch='字数限制就是评分标准',
    t1cb='笔记填空的词直接来自录音，所以答案很少难以听清。丢分的是在只允许两个词的地方写了三个词，或者加了一个空格旁边已经印着的词。',
    t1cn='读一读空格两边印着什么。超长答案里有一半重复了本来就在那里的词。',
    audEyebrow='录音',
    audTitle='你只会听一遍，一口气到底',
    audNote='一段关于城市中树木作用的讲座节选，中间没有停顿。先阅读接下来几页的全部十道题，再按播放——在这里，或在任何问题页底部的播放栏。你作答时录音会继续播放。',
    notesEyebrow='第 1–10 题 &middot; 完成笔记',
    notesTitle='在每个空格里填写一个单词和/或一个数字',
    notesHint='每个答案都按顺序出声说出。其中两个旁边还带着第二个数字，每一对里只有一个算数。',
    t2Eyebrow='听完之后',
    t2Title='讲座放置得分点的四个地方',
    t2ah='顺带定义的术语',
    t2ab='<em>The technical term is interception loss</em>——然后是一段解释。当讲者说 '
         '<em>the technical term is</em> 或 <em>that is</em> 时，一个值一分的词刚刚过去了。',
    t2an='定义是帮助，不是答案。答案通常是术语本身。',
    t2bh='被纠正的数字',
    t2bb='八百英镑，然后 <em>no, I should be accurate</em>，然后一千二百。第 1 部分的纠正陷阱，以第 4 '
         '部分的速度出现，而且没有第二个说话者来确认。',
    t2bn='两度是答案，而四被提到之后又被称为 "an upper bound"——一个被加了限定的数字不是他们想要的。',
    t2ch='照样算分的题外话',
    t2cb='二十秒关于树根和人行道的内容，讲者明确标为题外话。它偏离了主线——却仍然包含一个答案，第 6 题。',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>。题外话是换了话题，不是休息。',
    actTitle='来一场三分钟讲座',
    actUse='至少使用三个：',
    actSpeakBrief='两人一组。挑一个你熟悉的话题，不停顿地讲三分钟，带三个编号的要点。你的搭档做笔记，不允许提问。然后把他的笔记和你想表达的内容对照一下。',
    actSpeak1='讲者：每个要点都出声标示出来——<em>first</em>、<em>the second '
              'reason</em>、<em>finally</em>。边讲边数。',
    actSpeak2='在中途纠正一个数字，像真正的讲者那样，看看它有没有进入笔记。',
    actSpeak3='插一段二十秒的题外话，并明确说明这是题外话。你的搭档用三个词以内记下它唯一的要点。',
    actWriteKind='Writing · 120–180 词',
    actWriteBrief='写出听者最后应该记下的笔记：你的三个要点、那些数字，以及你定义的那个术语。在顶部设定字数限制——ONE WORD AND/OR A '
                  'NUMBER 是考试中最严格的一种——并让每一行都不超限。',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure，在第一句话里：整场讲座都是为了支撑这个论点而构建的。',
    n2why='Transpiration，与 "releasing water vapour through the leaves" '
          '同时给出定义。答案是术语，不是定义。',
    n3why='二，欧洲的数字。四是针对澳大利亚提到的，并立刻被称为 "upper bound"——一个被加了限定的数字不是答案。',
    n4why='"The technical term is interception loss"——这是表明一个词值一分的最清楚的信号。',
    n5why='二十到三十。空格旁边印着的内容说明它要的是范围的哪一半。',
    n6why='Pit，在讲者标为题外话的那段里。题外话偏离主线，但并不是空的。',
    n7why='Air quality，而且讲者自己给它打了分——"the weakest evidence of the '
          'three"。一个给自己的要点排序的讲者，是在把结构递给你。',
    n8why='Trap。限定紧跟在它所限制的论断之后——树木能截留颗粒物，也可能把被污染的空气困住。同一个动词，相反的效果。',
    n9why='一千二百。先说的是八百，并在同一句话里纠正——"no, I should be accurate"——这是第 1 部分的纠正陷阱以第 '
          '4 部分的速度出现。',
    n10why='Watering——"the watering, not the '
           'planting"。讲座的最后一句是它落下重点的地方，而对比就在同一口气里说出。',
)

# ── Japanese ────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Section 4 — <em>講義</em>',
    coverSub='話者は一人、長い一続きの話、そして途中に休みのない唯一のセクション',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 4',
    chipCount='10 問',
    t1Eyebrow='聞く前に',
    t1Title='難しい理由は一つだけで、それは語彙ではない',
    t1ah='休みがない',
    t1ab='セクション 1 から 3 は途中で止まり、次の問題を読む時間があります。セクション 4 '
         'は最後まで一気に進みます。話者は一人で、割り込んで繰り返してくれる二人目の声はありません。だから位置を見失うと、つかまるものが何もないのです。',
    t1an='再生を押す前に、すべての問題を読みましょう。あとでそのための時間は来ません。',
    t1bh='文ではなく、道しるべを追う',
    t1bb='<em>First</em> &middot; <em>the second factor</em> &middot; '
         '<em>the third function</em> &middot; '
         '<em>finally</em>。講師はおよそ一分に一度、今どこにいるかを教えてくれます。長く続く話の中で、それらの語だけが手がかりです。',
    t1bn='流されてしまったら、意味を追いかけるのをやめて次の道しるべを待ちましょう。すぐに来ます。',
    t1ch='語数制限が採点者',
    t1cb='ノート完成問題の語は録音からそのまま取られるので、答えが聞き取りにくいことはめったにありません。点を失うのは、二語までのところに三語を書くか、空所の横にすでにある語を付け足すことです。',
    t1cn='空所の両側に印刷されているものを読みましょう。長すぎる答えの半分は、すでにそこにあった語を繰り返しています。',
    audEyebrow='録音',
    audTitle='一度だけ、通して聞きます',
    audNote='都市における樹木の役割についての講義の一部で、途中に休みはありません。まず次のスライドの十問をすべて読み、それから再生を押してください。ここでも、問題スライドの下部のバーでも押せます。解答中も録音は流れ続けます。',
    notesEyebrow='問題 1–10 &middot; ノートを完成させる',
    notesTitle='各空所に一語および／または数字一つを書きなさい',
    notesHint='どの答えも順番に声に出して言われます。二つは横に別の数字を伴って現れ、各組のうち一つだけが正解です。',
    t2Eyebrow='録音のあとで',
    t2Title='講義が得点を置く四つの場所',
    t2ah='ついでに定義される用語',
    t2ab='<em>The technical term is interception loss</em>。そして説明が続きます。講師が '
         '<em>the technical term is</em> や <em>that is</em> '
         'と言ったとき、採点対象の語がちょうど通り過ぎたところです。',
    t2an='定義は助けであって答えではありません。答えはたいてい用語そのものです。',
    t2bh='訂正される数字',
    t2bb='八百ポンド、次に <em>no, I should be accurate</em>、そして千二百。セクション 1 '
         'の訂正の罠が、セクション 4 の速さで、確認してくれる二人目の話者なしに現れます。',
    t2bn='そして答えは二度で、四は口にされたあと "an upper bound" '
         'と呼ばれます。条件をつけられた数字は、求められている数字ではありません。',
    t2ch='それでも得点になる余談',
    t2cb='根と舗道についての二十秒。講師はそれを余談だと断ります。本筋から外れていますが、それでも答えが一つ、問題 6 が入っています。',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that&rsquo;s a different lecture</em>。余談は話題の転換であって、休憩ではありません。',
    actTitle='三分間の講義をする',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで。よく知っていることを取り上げ、番号をつけた三つの要点とともに、止まらずに三分間話します。相手はメモを取り、何も質問できません。そのあと、相手のメモとあなたが言おうとしたことを比べましょう。',
    actSpeak1='話す人：すべての要点を声に出して示しましょう。<em>first</em>、<em>the second '
              'reason</em>、<em>finally</em>。話しながら数えてください。',
    actSpeak2='本物の講師がするように、途中で数字を一つ訂正し、それがメモに届くか見てみましょう。',
    actSpeak3='二十秒の余談を一つ入れ、余談だと宣言しましょう。相手はその唯一の要点を三語以内でメモします。',
    actWriteKind='Writing · 120–180 語',
    actWriteBrief='聞き手が最後に持っているべきノートを書きましょう。あなたの三つの要点、数字、そして定義した一つの用語です。冒頭に語数制限を置き（ONE '
                  'WORD AND/OR A NUMBER が試験で使われる最も厳しいものです）、すべての行をその中に収めてください。',
    actPlaceholder='Point 1: … / cooled by: …',
    n1why='Infrastructure。最初の一文にあります。講義全体がそれを支えるために組み立てられている主張です。',
    n2why='Transpiration。"releasing water vapour through the leaves" '
          'と同じ息で定義されます。答えは用語であって定義ではありません。',
    n3why='二、ヨーロッパの数値です。四はオーストラリアについて口にされ、すぐに "upper bound" '
          'と呼ばれます。条件をつけられた数字は答えではありません。',
    n4why='"The technical term is interception '
          'loss"。ある語が一点に値することを示す、これ以上ないほど明確な合図です。',
    n5why='二十から三十。空所の横に印刷されているものが、範囲のどちら半分を求めているかを示します。',
    n6why='Pit。講師が余談だと断った部分の中にあります。余談は本筋から外れていますが、空っぽではありません。',
    n7why='Air quality。講師自身がそれを格付けします。"the weakest evidence of the '
          'three"。自分の要点を順位づける講師は、構成を手渡してくれているのです。',
    n8why='Trap。複雑な事情は、それが制限する主張の直後に来ます。樹木は微粒子を捕らえ、汚れた空気も閉じ込めてしまうことがあります。同じ動詞で、逆の効果です。',
    n9why='千二百。先に八百と言われ、同じ文の中で訂正されます。"no, I should be accurate"。セクション 1 '
          'の訂正の罠が、セクション 4 の速さで現れたものです。',
    n10why='Watering。"the watering, not the '
           'planting"。講義の最後の一行は要点が着地する場所で、対比は同じ息で語られます。',
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
