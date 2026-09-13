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
    coverSub='One speaker, four minutes, and the only section with no break in '
             'the middle',
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
         'handholds in four minutes of continuous speech.',
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
    audNote='Part of a lecture on the role of trees in cities. Four minutes '
            'with no break. Press play when you have read every question.',

    notesEyebrow='Questions 1&ndash;6 &middot; Complete the notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='Every answer is said aloud. Two of them are said twice, with '
              'the second version being the one that counts.',

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
    t2ch='The aside with nothing in it',
    t2cb='Twenty seconds about roots and pavements, containing no answers at '
         'all, placed exactly where a tiring candidate starts writing down '
         'whatever they hear.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that is a different lecture</em>. He tells you it is a '
         'digression. Believe him and rest.',

    mcEyebrow='Questions 7&ndash;10 &middot; The argument',
    mcTitle='What was the lecturer actually saying?',

    p1why='As infrastructure rather than decoration &mdash; he says it in his '
          'first twenty seconds, and the whole lecture is organised to support '
          'it. Openings carry the thesis; that is what they are for.',
    p2why='Dense trees over a narrow street can trap polluted air instead of '
          'letting it disperse. He raises it as a complication to his own '
          'point, which is where an honest lecturer puts the hardest question.',
    p3why='Real, but largely avoidable with the right planting pit. He grants '
          'the damage and the repair bill before he limits them &mdash; a '
          'concession is not a retraction.',
    p4why='The watering, not the planting. He says so explicitly in the last '
          'line, and it is the point the whole cost paragraph exists to make.',

    actTitle='Give the four-minute lecture',
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
              'partner should write nothing during it.',
    actWriteKind='Writing · 120–180 words',
    actWriteBrief='Write the notes a listener should have ended up with: your '
                  'three points, the numbers, and the one term you defined. '
                  'Keep every line to two words or fewer after the heading, '
                  'which is the real limit a note task sets.',
    actPlaceholder='Point 1: … / cooled by: …',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 4 &mdash; <em>die Vorlesung</em>',
    coverSub='Ein Sprecher, vier Minuten, und der einzige Teil ohne Pause in '
             'der Mitte',
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
         'einzigen Haltegriffe in vier Minuten Dauerrede.',
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
            'Städten. Vier Minuten ohne Pause. Drücke Play, wenn du jede Frage '
            'gelesen hast.',

    notesEyebrow='Fragen 1&ndash;6 &middot; Notizen vervollständigen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Jede Antwort wird laut gesagt. Zwei davon zweimal &mdash; die '
              'zweite Fassung zählt.',

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
    t2ch='Der Einschub ohne Inhalt',
    t2cb='Zwanzig Sekunden über Wurzeln und Gehwege, ganz ohne Antworten, '
         'genau dort platziert, wo ein ermüdender Kandidat anfängt, alles '
         'mitzuschreiben, was er hört.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that is a different lecture</em>. Er sagt dir, dass es eine '
         'Abschweifung ist. Glaub ihm und ruh dich aus.',

    mcEyebrow='Fragen 7&ndash;10 &middot; Die Argumentation',
    mcTitle='Was hat der Vortragende eigentlich gesagt?',

    p1why='Als Infrastruktur statt als Dekoration &mdash; er sagt es in den '
          'ersten zwanzig Sekunden, und die ganze Vorlesung ist darauf '
          'gebaut. Anfänge tragen die These; dafür sind sie da.',
    p2why='Dichte Bäume über einer engen Straße können verschmutzte Luft '
          'festhalten, statt sie entweichen zu lassen. Er bringt es als '
          'Einwand gegen den eigenen Punkt &mdash; dort steht bei einem '
          'ehrlichen Vortrag die schwerste Frage.',
    p3why='Real, aber mit der richtigen Pflanzgrube weitgehend vermeidbar. Er '
          'räumt Schaden und Reparaturkosten ein, bevor er sie einschränkt '
          '&mdash; ein Zugeständnis ist kein Rückzug.',
    p4why='Das Gießen, nicht das Pflanzen. Er sagt es ausdrücklich im letzten '
          'Satz, und der ganze Kostenabschnitt existiert für diesen Punkt.',

    actTitle='Halte die Vier-Minuten-Vorlesung',
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
              'solche an. Dein Partner soll dabei nichts schreiben.',
    actWriteKind='Schreiben · 120–180 Wörter',
    actWriteBrief='Schreib die Notizen auf, mit denen ein Zuhörer hätte '
                  'enden sollen: deine drei Punkte, die Zahlen und der eine '
                  'Begriff, den du definiert hast. Jede Zeile nach der '
                  'Überschrift höchstens zwei Wörter &mdash; das ist das echte '
                  'Limit einer Notizenaufgabe.',
    actPlaceholder='Point 1: … / cooled by: …',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 4 &mdash; <em>la conferencia</em>',
    coverSub='Una sola voz, cuatro minutos, y la única parte sin pausa en '
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
         'asideros en cuatro minutos seguidos.',
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
            'ciudades. Cuatro minutos sin pausa. Dale a reproducir cuando '
            'hayas leído todas las preguntas.',

    notesEyebrow='Preguntas 1&ndash;6 &middot; Completa las notas',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Todas las respuestas se dicen en voz alta. Dos se dicen dos '
              'veces, y vale la segunda versión.',

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
    t2ch='El inciso sin nada dentro',
    t2cb='Veinte segundos sobre raíces y aceras, sin una sola respuesta, '
         'puestos justo donde un candidato cansado empieza a apuntar todo lo '
         'que oye.',
    t2cn='<em>An aside</em> &middot; <em>somebody always asks</em> &middot; '
         '<em>that is a different lecture</em>. Te dice que es una digresión. '
         'Créele y descansa.',

    mcEyebrow='Preguntas 7&ndash;10 &middot; El argumento',
    mcTitle='¿Qué estaba diciendo en realidad?',

    p1why='Como infraestructura y no como decoración: lo dice en los primeros '
          'veinte segundos, y toda la conferencia está montada para '
          'sostenerlo. Las aperturas llevan la tesis; para eso están.',
    p2why='Los árboles densos sobre una calle estrecha pueden atrapar el aire '
          'contaminado en vez de dejarlo dispersarse. Lo plantea como '
          'complicación de su propio punto, que es donde un buen conferenciante '
          'pone la pregunta más difícil.',
    p3why='Real, pero evitable en gran medida con el hoyo de plantación '
          'adecuado. Admite el daño y la factura antes de limitarlos: una '
          'concesión no es una retirada.',
    p4why='El riego, no la plantación. Lo dice explícitamente en la última '
          'línea, y todo el párrafo de costes existe para eso.',

    actTitle='Da la conferencia de cuatro minutos',
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
              'compañero no debería escribir nada mientras dura.',
    actWriteKind='Escritura · 120–180 palabras',
    actWriteBrief='Escribe las notas con las que debería haber acabado quien '
                  'te escuchaba: tus tres puntos, las cifras y el término que '
                  'definiste. Cada línea, después del encabezado, de dos '
                  'palabras como mucho: ese es el límite real de una tarea de '
                  'notas.',
    actPlaceholder='Point 1: … / cooled by: …',
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
