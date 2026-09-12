# -*- coding: utf-8 -*-
"""Interface strings for IELTS Speaking Part 3 — the discussion.

English, German and Spanish, teach cards in the six-item form so the rule text
travels with its heading.

The split on translation follows HOUSE-STYLE §8: the English under test stays
English. Every phrase the learner is being taught to say — <em>on the whole</em>,
<em>that is true up to a point</em>, <em>it is often argued that</em> — is left
in English inside the German and Spanish cards, because a Spanish rendering of
the phrase is not the thing the learner has to produce in the room. What
translates is the rule around it, and the reason it matters.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

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
    coverTitle='IELTS Speaking <em>Part 3</em>',
    coverSub='The discussion: answering for people in general, and holding the '
             'line when the examiner disagrees',
    chipLevel='C1 · Advanced', chipFocus='Speaking Part 3',
    chipCount='13 questions',

    t1Eyebrow='Before you start',
    t1Title='Part 1 asked about you. Part 3 asks about people.',
    t1ah='The person changes',
    t1ab='Part 1: &ldquo;Do you enjoy cooking?&rdquo; Part 3: &ldquo;Why do '
         'fewer people cook at home now?&rdquo; The second question is not '
         'about your kitchen. Answer for the group.',
    t1an='If the answer would still stand with you removed from it, it is a '
         'Part 3 answer.',
    t1bh='Three phrases that generalise',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Each '
         'says &ldquo;this is what is usually true&rdquo;, and each leaves room '
         'for the exceptions the examiner is about to raise.',
    t1bn='<em>Tend to</em> takes a plain verb: people <em>tend to arrive</em> '
         'late, never <em>tend to arriving</em> late.',
    t1ch='Your own life still counts',
    t1cb='One example, placed after the general claim, shows you mean it. '
         '<em>A case in point is&hellip;</em> marks it as an illustration '
         'rather than as the whole answer.',
    t1cn='One example is support. Three examples is a Part 1 answer that has '
         'run long.',

    t2Eyebrow='Before you start',
    t2Title='The examiner disagrees. That is the task, not a verdict.',
    t2ah='Pushback is scripted',
    t2ab='Examiners are trained to challenge in Part 3, whatever you say. It '
         'is not a signal that the answer was weak &mdash; it is the part of '
         'the test that finds out what you can do under pressure.',
    t2an='A well-made point often attracts more pushback, not less, precisely '
         'because it is worth pushing.',
    t2bh='Concede, then qualify',
    t2bb='Give the other side something true, then keep your ground: <em>That '
         'is true up to a point, though&hellip;</em> or <em>I would accept '
         'that for smaller towns, but&hellip;</em>',
    t2bn='The clause after the concession carries your position. Stopping at '
         'the concession is how a point gets lost.',
    t2ch='Changing your mind is allowed',
    t2cb='Say it aloud and it reads as thinking: <em>Actually, now that I say '
         'it&hellip;</em> or <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='A silent reversal confuses the listener. A signalled one is '
         'coherence, and coherence is a quarter of the mark.',

    t3Eyebrow='Before you start',
    t3Title='How sure are you? Say so once, and mean it.',
    t3ah='Hedging is vocabulary',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. These are precise words doing a precise job, and '
         'precision is what Lexical Resource measures.',
    t3an='A hedge is not a filler. <em>Sort of</em> and <em>kind of</em> are '
         'fillers &mdash; they grade nothing.',
    t3bh='Move the claim off yourself',
    t3bb='<em>It is often argued that&hellip;</em> and <em>There is a case for '
         'saying&hellip;</em> report a position without signing your name to '
         'it, which leaves you free to take it apart a sentence later.',
    t3bn='Useful on a topic you know little about: you can run the argument '
         'without claiming it.',
    t3ch='Hedge once, not everywhere',
    t3cb='One graded claim reads as judgement. Four in a row reads as evasion, '
         'and an answer carrying a hedge on every clause has stopped saying '
         'anything at all.',
    t3cn='Commit in the main clause, limit in the clause after it. That is the '
         'shape.',

    mcaEyebrow='Activity 1 · The general case',
    mcaTitle='Which answer is about people, not about you?',
    mcbEyebrow='Activity 2 · Under pressure',
    mcbTitle='The examiner has just disagreed',
    mccEyebrow='Activity 3 · Degrees of certainty',
    mccTitle='How sure, and how do you say it?',

    q1why='<em>On the whole</em> makes it a claim about readers in general, and '
          'the clause after <em>though</em> keeps it honest. The thriller '
          'answer belongs in Part 1; the other two close the topic down.',
    q2why='<em>By and large</em> states what is usually true of the group. The '
          'other three announce that only you are being described, which is '
          'the habit Part 3 is asking you to drop.',
    q3why='A reason that applies to everyone who moves, given in one line. The '
          'cousin is an example with no claim in front of it, and the other '
          'two either overstate or refuse the question.',
    q4why='After. The claim is the answer and the example is evidence for it. '
          'Put the example first and the examiner has to wait to find out what '
          'it is evidence of.',
    q5why='It grants the objection where it holds, then keeps the claim alive. '
          'Flat refusal gives the examiner nothing to work with; total '
          'surrender gives them nothing either.',
    q6why='A concession followed by <em>though</em> &mdash; the position '
          'survives it. The other three refuse to move, abandon the point, or '
          'hand the turn straight back.',
    q7why='Not a problem, provided you say that you are doing it. Coherence is '
          'about whether the listener can follow the thread, and a signalled '
          'change of mind is easy to follow.',
    q8why='Whether you can hold a line, or revise one, in English. The '
          'examiner has no stake in the topic and marks no opinions &mdash; '
          'all four criteria are language.',
    q9why='One hedge, then one limit. The second is hedged into saying '
          'nothing, the third refuses to grade at all, and the fourth stacks '
          'four hedges onto a single verb.',
    q10why='The position disappears. Fluency and Coherence rewards a line of '
           'argument, and an answer that asserts nothing leaves no line to '
           'follow.',
    q11why='<em>It is often argued that</em> reports the view without adopting '
           'it. The other three put your own name to the claim before you have '
           'decided whether you want it.',
    q12why='Lexical Resource. A hedge is a precise word choice, and picking '
           'the right degree of certainty is exactly what that criterion '
           'measures. No descriptor counts how many you use.',

    ordEyebrow='Activity 4 · The shape of an answer',
    ordTitle='Put the four moves in order',
    ordHint='Drag them into order &mdash; or click one, then the position you '
            'want it in.',

    actTitle='Run a Part 3',
    actUse='Use at least three:',
    actSpeakBrief='One of you examines, one answers, and a phone holds the '
                  'clock. The examiner asks four questions on a single '
                  'topic and must disagree at least twice. Five minutes, '
                  'then swap.',
    actSpeak1='Candidate: answer for people in general first, and only then '
              'give one example of your own.',
    actSpeak2='Examiner: push back on the strongest thing you hear, not the '
              'weakest. Ask whether it holds everywhere.',
    actSpeak3='Candidate: concede what is fair, keep the rest, and grade how '
              'sure you are exactly once.',
    actWriteKind='Writing · 180–250 words',
    actWriteBrief='Write out your best answer to one of the four questions you '
                  'were asked, as you would want to have said it: position, '
                  'reason, one example, and the concession that answers the '
                  'pushback before it arrives.',
    actPlaceholder='On the whole, people…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='IELTS Speaking <em>Teil 3</em>',
    coverSub='Die Diskussion: für die Allgemeinheit antworten und die Position '
             'halten, wenn der Prüfer widerspricht',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking Teil 3',
    chipCount='13 Fragen',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Teil 1 fragte nach dir. Teil 3 fragt nach den Menschen.',
    t1ah='Die Person wechselt',
    t1ab='Teil 1: &ldquo;Do you enjoy cooking?&rdquo; Teil 3: &ldquo;Why do '
         'fewer people cook at home now?&rdquo; Die zweite Frage zielt nicht '
         'auf deine Küche. Antworte für die Gruppe.',
    t1an='Wenn die Antwort auch ohne dich noch stimmt, ist es eine Antwort für '
         'Teil 3.',
    t1bh='Drei Wendungen, die verallgemeinern',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Jede '
         'sagt: &bdquo;so ist es üblicherweise&ldquo; &mdash; und jede lässt '
         'Raum für die Ausnahmen, die der Prüfer gleich nennen wird.',
    t1bn='<em>Tend to</em> steht mit dem Grundverb: people <em>tend to '
         'arrive</em> late, nie <em>tend to arriving</em> late.',
    t1ch='Dein eigenes Leben zählt weiterhin',
    t1cb='Ein Beispiel, nach der allgemeinen Aussage platziert, zeigt, dass du '
         'es ernst meinst. <em>A case in point is&hellip;</em> markiert es als '
         'Beleg und nicht als die ganze Antwort.',
    t1cn='Ein Beispiel stützt. Drei Beispiele sind eine Teil-1-Antwort, die zu '
         'lang geraten ist.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Der Prüfer widerspricht. Das ist die Aufgabe, kein Urteil.',
    t2ah='Der Widerspruch ist vorgesehen',
    t2ab='Prüfer sind darauf geschult, in Teil 3 zu widersprechen &mdash; egal '
         'was du sagst. Es ist kein Zeichen für eine schwache Antwort, sondern '
         'der Teil der Prüfung, der zeigt, was du unter Druck kannst.',
    t2an='Ein gut gebauter Punkt zieht oft mehr Widerspruch an, gerade weil er '
         'es wert ist.',
    t2bh='Zugestehen, dann einschränken',
    t2bb='Gib der Gegenseite etwas Wahres, dann halte deine Position: <em>That '
         'is true up to a point, though&hellip;</em> oder <em>I would accept '
         'that for smaller towns, but&hellip;</em>',
    t2bn='Der Satzteil nach dem Zugeständnis trägt deine Position. Beim '
         'Zugeständnis stehen zu bleiben, ist der Weg, den Punkt zu verlieren.',
    t2ch='Die Meinung zu ändern ist erlaubt',
    t2cb='Sprich es aus, dann klingt es nach Nachdenken: <em>Actually, now '
         'that I say it&hellip;</em> oder <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='Eine stille Kehrtwende verwirrt. Eine angekündigte ist Kohärenz &mdash; '
         'und Kohärenz ist ein Viertel der Note.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Wie sicher bist du? Sag es einmal, und meine es.',
    t3ah='Abschwächen ist Wortschatz',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most cases</em>. '
         'Das sind präzise Wörter mit einer präzisen Aufgabe, und Präzision ist '
         'genau das, was Lexical Resource misst.',
    t3an='Eine Abschwächung ist kein Füllwort. <em>Sort of</em> und <em>kind '
         'of</em> sind Füllwörter &mdash; sie stufen nichts ein.',
    t3bh='Die Aussage von dir wegrücken',
    t3bb='<em>It is often argued that&hellip;</em> und <em>There is a case for '
         'saying&hellip;</em> geben eine Position wieder, ohne sie zu '
         'unterschreiben &mdash; du kannst sie einen Satz später zerlegen.',
    t3bn='Nützlich bei einem Thema, von dem du wenig weißt: du führst das '
         'Argument, ohne es zu beanspruchen.',
    t3ch='Einmal abschwächen, nicht überall',
    t3cb='Eine eingestufte Aussage klingt nach Urteil. Vier hintereinander '
         'klingen nach Ausweichen, und eine Antwort mit einer Abschwächung in '
         'jedem Satzteil sagt gar nichts mehr.',
    t3cn='Im Hauptsatz festlegen, im Satz danach einschränken. Das ist die '
         'Form.',

    mcaEyebrow='Aktivität 1 · Der allgemeine Fall',
    mcaTitle='Welche Antwort handelt von den Menschen, nicht von dir?',
    mcbEyebrow='Aktivität 2 · Unter Druck',
    mcbTitle='Der Prüfer hat gerade widersprochen',
    mccEyebrow='Aktivität 3 · Grade der Sicherheit',
    mccTitle='Wie sicher &mdash; und wie sagst du es?',

    q1why='<em>On the whole</em> macht daraus eine Aussage über Leser im '
          'Allgemeinen, und der Teil nach <em>though</em> hält sie ehrlich. '
          'Die Thriller-Antwort gehört in Teil 1; die anderen beiden beenden '
          'das Thema.',
    q2why='<em>By and large</em> sagt, was für die Gruppe üblicherweise gilt. '
          'Die anderen drei kündigen an, dass nur von dir die Rede ist &mdash; '
          'genau die Gewohnheit, die Teil 3 ablegen lässt.',
    q3why='Ein Grund, der für alle gilt, die umziehen, in einer Zeile. Der '
          'Cousin ist ein Beispiel ohne Aussage davor, und die anderen beiden '
          'übertreiben oder verweigern die Frage.',
    q4why='Danach. Die Aussage ist die Antwort, das Beispiel ist der Beleg '
          'dafür. Steht das Beispiel vorn, muss der Prüfer warten, um zu '
          'erfahren, wofür es ein Beleg ist.',
    q5why='Es räumt den Einwand dort ein, wo er gilt, und hält die Aussage am '
          'Leben. Blanke Ablehnung gibt dem Prüfer nichts, völlige Aufgabe '
          'ebenso wenig.',
    q6why='Ein Zugeständnis, gefolgt von <em>though</em> &mdash; die Position '
          'überlebt es. Die anderen drei bewegen sich nicht, geben den Punkt '
          'auf oder reichen das Wort sofort zurück.',
    q7why='Kein Problem, solange du es aussprichst. Kohärenz fragt, ob der '
          'Zuhörer dem Faden folgen kann, und ein angekündigter Sinneswandel '
          'ist leicht zu verfolgen.',
    q8why='Ob du eine Linie halten oder überarbeiten kannst &mdash; auf '
          'Englisch. Der Prüfer hat kein Interesse am Thema und bewertet keine '
          'Meinungen; alle vier Kriterien sind Sprache.',
    q9why='Eine Abschwächung, dann eine Einschränkung. Die zweite schwächt sich '
          'ins Nichts, die dritte stuft gar nicht ein, und die vierte stapelt '
          'vier Abschwächungen auf ein Verb.',
    q10why='Die Position verschwindet. Fluency and Coherence belohnt eine '
           'Argumentationslinie, und eine Antwort, die nichts behauptet, '
           'lässt keine Linie übrig.',
    q11why='<em>It is often argued that</em> gibt die Ansicht wieder, ohne sie '
           'zu übernehmen. Die anderen drei setzen deinen Namen unter die '
           'Aussage, bevor du sie überhaupt willst.',
    q12why='Lexical Resource. Eine Abschwächung ist eine präzise Wortwahl, und '
           'den richtigen Grad zu treffen, ist genau das, was dieses Kriterium '
           'misst. Kein Deskriptor zählt, wie viele du benutzt.',

    ordEyebrow='Aktivität 4 · Die Form einer Antwort',
    ordTitle='Bring die vier Schritte in die richtige Reihenfolge',
    ordHint='Zieh sie in die richtige Reihenfolge &mdash; oder klicke einen an '
            'und dann die Position, an die er soll.',

    actTitle='Führt einen Teil 3 durch',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Einer prüft, einer antwortet, das Handy hält die Zeit. '
                  'Der Prüfer stellt vier Fragen zu einem Thema und muss '
                  'mindestens zweimal widersprechen. Fünf Minuten, dann '
                  'tauschen.',
    actSpeak1='Kandidat: antworte zuerst für die Allgemeinheit und erst danach '
              'mit einem eigenen Beispiel.',
    actSpeak2='Prüfer: widersprich dem stärksten Punkt, den du hörst, nicht '
              'dem schwächsten. Frage, ob er überall gilt.',
    actSpeak3='Kandidat: gestehe zu, was fair ist, halte den Rest, und stufe '
              'genau einmal ein, wie sicher du bist.',
    actWriteKind='Schreiben · 180–250 Wörter',
    actWriteBrief='Schreibe deine beste Antwort auf eine der vier Fragen so '
                  'auf, wie du sie gern gesagt hättest: Position, Grund, ein '
                  'Beispiel und das Zugeständnis, das den Widerspruch '
                  'beantwortet, bevor er kommt.',
    actPlaceholder='On the whole, people…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='IELTS Speaking <em>Parte 3</em>',
    coverSub='El debate: responder sobre la gente en general y mantener tu '
             'postura cuando el examinador te lleva la contraria',
    chipLevel='C1 · Avanzado', chipFocus='Speaking Parte 3',
    chipCount='13 preguntas',

    t1Eyebrow='Antes de empezar',
    t1Title='La Parte 1 preguntaba por ti. La Parte 3 pregunta por la gente.',
    t1ah='Cambia la persona',
    t1ab='Parte 1: &ldquo;Do you enjoy cooking?&rdquo; Parte 3: &ldquo;Why do '
         'fewer people cook at home now?&rdquo; La segunda pregunta no va de '
         'tu cocina. Responde por el grupo.',
    t1an='Si la respuesta sigue siendo cierta sin ti dentro, es una respuesta '
         'de Parte 3.',
    t1bh='Tres expresiones que generalizan',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Cada '
         'una dice &laquo;esto es lo habitual&raquo; y deja sitio a las '
         'excepciones que el examinador está a punto de sacar.',
    t1bn='<em>Tend to</em> lleva el verbo en su forma base: people <em>tend to '
         'arrive</em> late, nunca <em>tend to arriving</em> late.',
    t1ch='Tu propia vida sigue contando',
    t1cb='Un ejemplo, colocado después de la afirmación general, demuestra que '
         'lo dices en serio. <em>A case in point is&hellip;</em> lo marca como '
         'ilustración y no como la respuesta entera.',
    t1cn='Un ejemplo apoya. Tres ejemplos son una respuesta de Parte 1 que se '
         'ha alargado.',

    t2Eyebrow='Antes de empezar',
    t2Title='El examinador discrepa. Esa es la tarea, no un veredicto.',
    t2ah='La objeción está prevista',
    t2ab='Los examinadores están formados para rebatir en la Parte 3, digas lo '
         'que digas. No indica que tu respuesta fuera floja: es la parte de la '
         'prueba que averigua qué sabes hacer bajo presión.',
    t2an='Un argumento bien construido suele atraer más objeciones, no menos, '
         'precisamente porque merece la pena rebatirlo.',
    t2bh='Concede y luego matiza',
    t2bb='Dale a la otra parte algo cierto y luego mantén tu terreno: <em>That '
         'is true up to a point, though&hellip;</em> o <em>I would accept that '
         'for smaller towns, but&hellip;</em>',
    t2bn='La oración que sigue a la concesión es la que lleva tu postura. '
         'Quedarse en la concesión es como se pierde el argumento.',
    t2ch='Cambiar de opinión está permitido',
    t2cb='Dilo en voz alta y suena a estar pensando: <em>Actually, now that I '
         'say it&hellip;</em> o <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='Un giro silencioso confunde. Uno anunciado es coherencia, y la '
         'coherencia es la cuarta parte de la nota.',

    t3Eyebrow='Antes de empezar',
    t3Title='¿Cuánto de seguro estás? Dilo una vez, y en serio.',
    t3ah='Matizar es vocabulario',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most cases</em>. '
         'Son palabras precisas con una función precisa, y la precisión es '
         'justo lo que mide Lexical Resource.',
    t3an='Un matizador no es una muletilla. <em>Sort of</em> y <em>kind of</em> '
         'son muletillas: no gradúan nada.',
    t3bh='Aleja la afirmación de ti',
    t3bb='<em>It is often argued that&hellip;</em> y <em>There is a case for '
         'saying&hellip;</em> recogen una postura sin firmarla, lo que te deja '
         'libre para desmontarla una frase después.',
    t3bn='Útil en un tema del que sabes poco: expones el argumento sin hacerlo '
         'tuyo.',
    t3ch='Matiza una vez, no en todo',
    t3cb='Una afirmación graduada suena a criterio. Cuatro seguidas suenan a '
         'evasiva, y una respuesta con un matizador en cada oración ya no dice '
         'nada.',
    t3cn='Comprométete en la oración principal y limita en la siguiente. Esa '
         'es la forma.',

    mcaEyebrow='Actividad 1 · El caso general',
    mcaTitle='¿Qué respuesta habla de la gente y no de ti?',
    mcbEyebrow='Actividad 2 · Bajo presión',
    mcbTitle='El examinador acaba de discrepar',
    mccEyebrow='Actividad 3 · Grados de certeza',
    mccTitle='¿Cuánto de seguro, y cómo lo dices?',

    q1why='<em>On the whole</em> la convierte en una afirmación sobre los '
          'lectores en general, y la parte tras <em>though</em> la mantiene '
          'honesta. La respuesta del thriller es de Parte 1; las otras dos '
          'cierran el tema.',
    q2why='<em>By and large</em> dice lo que suele ser cierto del grupo. Las '
          'otras tres anuncian que solo se habla de ti, que es justo la '
          'costumbre que la Parte 3 te pide dejar.',
    q3why='Una razón que vale para todo el que se muda, en una línea. El primo '
          'es un ejemplo sin afirmación delante, y las otras dos exageran o '
          'esquivan la pregunta.',
    q4why='Después. La afirmación es la respuesta y el ejemplo es la prueba. '
          'Si el ejemplo va primero, el examinador tiene que esperar para '
          'saber de qué es prueba.',
    q5why='Concede la objeción donde se sostiene y mantiene viva la '
          'afirmación. La negativa seca no le da nada al examinador; la '
          'rendición total, tampoco.',
    q6why='Una concesión seguida de <em>though</em>: la postura sobrevive. Las '
          'otras tres no se mueven, abandonan el argumento o devuelven el '
          'turno de inmediato.',
    q7why='No es un problema, siempre que digas que lo estás haciendo. La '
          'coherencia mide si quien escucha puede seguir el hilo, y un cambio '
          'de opinión anunciado se sigue sin esfuerzo.',
    q8why='Si sabes sostener una postura, o revisarla, en inglés. Al '
          'examinador el tema le da igual y no califica opiniones: los cuatro '
          'criterios son lengua.',
    q9why='Un matizador y luego un límite. La segunda se matiza hasta no decir '
          'nada, la tercera no gradúa en absoluto y la cuarta amontona cuatro '
          'matizadores sobre un solo verbo.',
    q10why='La postura desaparece. Fluency and Coherence premia una línea '
           'argumental, y una respuesta que no afirma nada no deja ninguna '
           'línea que seguir.',
    q11why='<em>It is often argued that</em> recoge la idea sin asumirla. Las '
           'otras tres ponen tu nombre bajo la afirmación antes de que hayas '
           'decidido si la quieres.',
    q12why='Lexical Resource. Un matizador es una elección léxica precisa, y '
           'acertar con el grado de certeza es exactamente lo que mide ese '
           'criterio. Ningún descriptor cuenta cuántos usas.',

    ordEyebrow='Actividad 4 · La forma de una respuesta',
    ordTitle='Ordena los cuatro pasos',
    ordHint='Arrástralos hasta ordenarlos &mdash; o haz clic en uno y luego en '
            'la posición que quieras.',

    actTitle='Haced una Parte 3',
    actUse='Usa al menos tres:',
    actSpeakBrief='Uno examina, otro responde y el móvil lleva el tiempo. El '
                  'examinador hace cuatro preguntas sobre un solo tema y '
                  'debe discrepar al menos dos veces. Cinco minutos y '
                  'cambiad.',
    actSpeak1='Candidato: responde primero por la gente en general y solo '
              'después da un ejemplo propio.',
    actSpeak2='Examinador: rebate lo más fuerte que oigas, no lo más flojo. '
              'Pregunta si eso vale en todas partes.',
    actSpeak3='Candidato: concede lo que sea justo, conserva el resto y gradúa '
              'tu certeza exactamente una vez.',
    actWriteKind='Escritura · 180–250 palabras',
    actWriteBrief='Escribe tu mejor respuesta a una de las cuatro preguntas '
                  'que te hicieron, tal como te habría gustado decirla: '
                  'postura, razón, un ejemplo y la concesión que responde a la '
                  'objeción antes de que llegue.',
    actPlaceholder='On the whole, people…',
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
