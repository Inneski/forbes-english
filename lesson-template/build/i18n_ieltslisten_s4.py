# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 4.

English, German and Spanish, teach cards in the six-item form.

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
