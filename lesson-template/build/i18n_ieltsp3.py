# -*- coding: utf-8 -*-
"""Interface strings for IELTS Speaking Part 3 — the discussion.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).
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
from ielts_langs import TAIL_MORE

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

TAIL.update(TAIL_MORE)

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='IELTS Speaking <em>Part 3</em>',
    coverSub='The discussion: answering for people in general, and holding '
             'the line when the examiner pushes back',
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
    t2Title='If the examiner pushes back, that is the task, not a verdict',
    t2ah='Pushback is part of the test',
    t2ab='Part 3 examiners often push back &mdash; asking whether a view '
         'holds everywhere, or putting the other side &mdash; however good '
         'the answer. It is not a signal that the answer was weak: it is how '
         'Part 3 finds out what you can do under pressure.',
    t2an='A well-made point can attract more pushback, not less, because it '
         'is worth pushing.',
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
         'coherence, and Fluency and Coherence is a quarter of the mark.',

    t3Eyebrow='Before you start',
    t3Title='How sure are you? Say so once, and mean it.',
    t3ah='Hedging is precise language',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. These are precise words doing a precise job, which '
         'Lexical Resource rewards &mdash; and modal verbs and frames like '
         '<em>it is argued that</em> show grammatical range as well.',
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
    q2why='<em>By and large</em> states what is usually true of the group. '
          'The other three mark your own case or your own view &mdash; fine '
          'for giving an opinion, but none of them turns a habit into a '
          'general claim.',
    q3why='A reason that applies to most people who move, given in one line. '
          'The cousin is an example with no claim in front of it, and the '
          'other two either overstate or refuse the question.',
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
    q9why='One hedge, then one limit. <em>Arguably possible&hellip; '
          'conceivably</em> is hedged into saying nothing, <em>It always '
          'works</em> refuses to grade at all, and <em>might possibly '
          'perhaps&hellip; maybe</em> stacks four hedges onto one verb.',
    q10why='The position disappears. Fluency and Coherence rewards a line of '
           'argument, and an answer that asserts nothing leaves no line to '
           'follow.',
    q11why='<em>It is often argued that</em> reports the view without adopting '
           'it. The other three put your own name to the claim before you have '
           'decided whether you want it.',
    q12why='Lexical Resource. A hedge is a precise word choice, and choosing '
           'the right degree of certainty is part of what that criterion '
           'rewards &mdash; though a modal hedge shows grammar too. No '
           'descriptor counts how many you use.',

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
    actSpeak3='Candidate: concede what is fair, keep the rest, and say how '
              'sure you are without hedging every clause.',
    actWriteKind='Writing · 180–250 words',
    actWriteBrief='Write out your best answer to one of the four questions you '
                  'were asked, as you would want to have said it: position, '
                  'reason, one example, and the concession that answers the '
                  'pushback before it arrives.',
    actPlaceholder='On the whole, people…',
)

# The ordering explanation sits in the data module, which keeps the only copy
# of the English. It was a plain string there until 2026-09-23, so German and
# Spanish learners read it in English.
from ieltsp3_data import ORDER_WHY
T['en']['orderWhy'] = ORDER_WHY

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='IELTS Speaking <em>Teil 3</em>',
    coverSub='Die Diskussion: für Menschen im Allgemeinen antworten und die '
             'Position halten, wenn der Prüfer dagegenhält',
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
    t2Title='Wenn der Prüfer dagegenhält, ist das die Aufgabe, kein Urteil',
    t2ah='Der Widerspruch ist vorgesehen',
    t2ab='Prüfer in Teil 3 halten oft dagegen &mdash; sie fragen, ob eine '
         'Sicht überall gilt, oder bringen die Gegenseite ins Spiel &mdash;, '
         'egal wie gut die Antwort war. Das ist kein Zeichen, dass die '
         'Antwort schwach war: So findet Teil 3 heraus, was du unter Druck '
         'kannst.',
    t2an='Ein gut gemachter Punkt kann mehr Gegenwind bekommen, nicht '
         'weniger, weil es sich lohnt, dagegenzuhalten.',
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
         'und Fluency and Coherence ist ein Viertel der Note.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Wie sicher bist du? Sag es einmal, und meine es.',
    t3ah='Abschwächen ist präzise Sprache',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. Das sind präzise Wörter für eine präzise Aufgabe, und '
         'Lexical Resource belohnt sie &mdash; Modalverben und Rahmen wie '
         '<em>it is argued that</em> zeigen außerdem grammatische Bandbreite.',
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
    q2why='<em>By and large</em> sagt, was für die Gruppe meistens gilt. Die '
          'anderen drei kennzeichnen deinen eigenen Fall oder deine eigene '
          'Sicht &mdash; gut, um eine Meinung zu äußern, aber keines macht '
          'aus einer Gewohnheit eine allgemeine Aussage.',
    q3why='Ein Grund, der für die meisten gilt, die umziehen, in einer '
          'Zeile. Der Cousin ist ein Beispiel ohne Aussage davor, und die '
          'anderen beiden übertreiben oder verweigern die Frage.',
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
    q9why='Eine Abschwächung, dann eine Einschränkung. <em>Arguably '
          'possible&hellip; conceivably</em> schwächt sich ins Nichts, <em>It '
          'always works</em> stuft gar nicht ein, und <em>might possibly '
          'perhaps&hellip; maybe</em> stapelt vier Abschwächungen auf ein Verb.',
    q10why='Die Position verschwindet. Fluency and Coherence belohnt eine '
           'Argumentationslinie, und eine Antwort, die nichts behauptet, '
           'lässt keine Linie übrig.',
    q11why='<em>It is often argued that</em> gibt die Ansicht wieder, ohne sie '
           'zu übernehmen. Die anderen drei setzen deinen Namen unter die '
           'Aussage, bevor du sie überhaupt willst.',
    q12why='Lexical Resource. Eine Abschwächung ist eine präzise Wortwahl, '
           'und den richtigen Grad an Sicherheit zu wählen gehört zu dem, '
           'was dieses Kriterium belohnt &mdash; wobei eine Abschwächung mit '
           'Modalverb auch Grammatik zeigt. Kein Deskriptor zählt, wie viele '
           'du benutzt.',

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
    actSpeak3='Kandidat: Gib zu, was stimmt, behalte den Rest und sag, wie '
              'sicher du bist, ohne jeden Satzteil abzuschwächen.',
    actWriteKind='Schreiben · 180–250 Wörter',
    actWriteBrief='Schreibe deine beste Antwort auf eine der vier Fragen so '
                  'auf, wie du sie gern gesagt hättest: Position, Grund, ein '
                  'Beispiel und das Zugeständnis, das den Widerspruch '
                  'beantwortet, bevor er kommt.',
    actPlaceholder='On the whole, people…',

    # The ordering explanation; English from the data module.
    orderWhy='Position, Begründung, Beispiel, Einschränkung. Das Beispiel '
             'kommt an dritter Stelle, weil es eine Aussage veranschaulicht, '
             'die schon gemacht ist &mdash; fängst du damit an, hört der '
             'Prüfer eine Anekdote statt eines Arguments. Die Einschränkung '
             'kommt zuletzt, und die Antwort endet wieder bei deiner '
             'Position: Du hast die Ausnahme selbst benannt, also hat '
             'Widerspruch weniger, woran er dich packen kann.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='IELTS Speaking <em>Parte 3</em>',
    coverSub='La discusión: responder por la gente en general y mantener la '
             'postura cuando el examinador lleva la contraria',
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
    t2Title='Si el examinador te lleva la contraria, es la tarea, no un '
            'veredicto',
    t2ah='La objeción está prevista',
    t2ab='En la Parte 3 los examinadores a menudo te llevan la contraria '
         '&mdash; preguntan si una idea vale en todas partes o plantean el '
         'otro lado &mdash;, por buena que sea la respuesta. No es señal de '
         'que la respuesta fuera floja: es como la Parte 3 averigua lo que '
         'sabes hacer bajo presión.',
    t2an='Un argumento bien hecho puede recibir más réplica, no menos, '
         'porque merece la pena replicarlo.',
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
    t2cn='Un giro silencioso confunde. Uno anunciado es coherencia, y '
         'Fluency and Coherence es la cuarta parte de la nota.',

    t3Eyebrow='Antes de empezar',
    t3Title='¿Cuánto de seguro estás? Dilo una vez, y en serio.',
    t3ah='Matizar es lenguaje preciso',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. Son palabras precisas haciendo un trabajo preciso, y '
         'Lexical Resource las premia &mdash; y los verbos modales y '
         'fórmulas como <em>it is argued that</em> muestran además variedad '
         'gramatical.',
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
    q2why='<em>By and large</em> expresa lo que suele ser verdad del grupo. '
          'Las otras tres marcan tu propio caso o tu propia opinión &mdash; '
          'válidas para opinar, pero ninguna convierte una costumbre en una '
          'afirmación general.',
    q3why='Una razón que vale para la mayoría de quienes se mudan, dicha en '
          'una línea. El primo es un ejemplo sin ninguna afirmación delante, '
          'y las otras dos exageran o se niegan a responder.',
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
    q9why='Un matizador y luego un límite. <em>Arguably possible&hellip; '
          'conceivably</em> se matiza hasta no decir nada, <em>It always '
          'works</em> no gradúa en absoluto y <em>might possibly '
          'perhaps&hellip; maybe</em> amontona cuatro matizadores sobre un '
          'solo verbo.',
    q10why='La postura desaparece. Fluency and Coherence premia una línea '
           'argumental, y una respuesta que no afirma nada no deja ninguna '
           'línea que seguir.',
    q11why='<em>It is often argued that</em> recoge la idea sin asumirla. Las '
           'otras tres ponen tu nombre bajo la afirmación antes de que hayas '
           'decidido si la quieres.',
    q12why='Lexical Resource. Un matiz es una elección de palabra precisa, y '
           'elegir el grado justo de certeza forma parte de lo que premia '
           'ese criterio &mdash; aunque un matiz con un modal muestra '
           'también gramática. Ningún descriptor cuenta cuántos usas.',

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
    actSpeak3='Candidato: concede lo que sea justo, mantén el resto y di lo '
              'seguro que estás sin matizar cada frase.',
    actWriteKind='Escritura · 180–250 palabras',
    actWriteBrief='Escribe tu mejor respuesta a una de las cuatro preguntas '
                  'que te hicieron, tal como te habría gustado decirla: '
                  'postura, razón, un ejemplo y la concesión que responde a la '
                  'objeción antes de que llegue.',
    actPlaceholder='On the whole, people…',

    # The ordering explanation; English from the data module.
    orderWhy='Postura, razón, ejemplo, límite. El ejemplo va tercero porque '
             'ilustra una afirmación ya hecha &mdash; si empiezas por él, el '
             'examinador oye una anécdota, no un argumento. El límite va al '
             'final, y la respuesta termina de nuevo en tu postura: ya has '
             'nombrado tú mismo la excepción, así que la réplica tiene menos '
             'donde agarrarte.',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='IELTS Speaking <em>Partie 3</em>',
    coverSub='La discussion : répondre pour les gens en général, et tenir sa '
             'position quand l’examinateur vous contredit',
    chipLevel='C1 · Avancé', chipFocus='Speaking Partie 3',
    chipCount='13 questions',

    t1Eyebrow='Avant de commencer',
    t1Title='La Partie 1 parlait de vous. La Partie 3 parle des gens.',
    t1ah='La personne change',
    t1ab='Partie 1 : &ldquo;Do you enjoy cooking?&rdquo; Partie 3 : &ldquo;Why do '
         'fewer people cook at home now?&rdquo; La seconde question ne porte pas '
         'sur votre cuisine. Répondez pour le groupe.',
    t1an='Si la réponse tient toujours une fois que vous en êtes retiré, c’est '
         'une réponse de Partie 3.',
    t1bh='Trois expressions qui généralisent',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Chacune '
         'dit « voilà ce qui est vrai en général », et chacune laisse de la place '
         'aux exceptions que l’examinateur s’apprête à soulever.',
    t1bn='<em>Tend to</em> est suivi d’un verbe simple : people <em>tend to '
         'arrive</em> late, jamais <em>tend to arriving</em> late.',
    t1ch='Votre vie compte quand même',
    t1cb='Un exemple, placé après l’affirmation générale, montre que vous y '
         'croyez. <em>A case in point is&hellip;</em> le signale comme une '
         'illustration et non comme toute la réponse.',
    t1cn='Un exemple, c’est un appui. Trois exemples, c’est une réponse de '
         'Partie 1 qui s’est allongée.',

    t2Eyebrow='Avant de commencer',
    t2Title='Si l’examinateur vous contredit, c’est l’exercice, pas un '
            'verdict',
    t2ah='La contradiction fait partie du test',
    t2ab='En Partie 3, les examinateurs contredisent souvent &mdash; ils '
         'demandent si un point de vue vaut partout, ou présentent l’autre '
         'camp &mdash;, quelle que soit la qualité de la réponse. Ce n’est '
         'pas le signe d’une réponse faible : c’est ainsi que la Partie 3 '
         'découvre ce que vous savez faire sous pression.',
    t2an='Un argument bien construit peut s’attirer plus d’objections, pas '
         'moins, parce qu’il vaut la peine d’être poussé.',
    t2bh='Concéder, puis nuancer',
    t2bb='Accordez à l’autre camp quelque chose de vrai, puis tenez bon : '
         '<em>That is true up to a point, though&hellip;</em> ou <em>I would '
         'accept that for smaller towns, but&hellip;</em>',
    t2bn='La proposition qui suit la concession porte votre position. S’arrêter '
         'à la concession, c’est comme ça qu’on perd un argument.',
    t2ch='Changer d’avis est permis',
    t2cb='Dites-le à voix haute et cela passe pour de la réflexion : '
         '<em>Actually, now that I say it&hellip;</em> ou <em>On reflection, I '
         'would put that differently.</em>',
    t2cn='Un revirement silencieux déroute celui qui écoute. Un revirement '
         'annoncé, c’est de la cohérence, et Fluency and Coherence représente un '
         'quart de la note.',

    t3Eyebrow='Avant de commencer',
    t3Title='À quel point êtes-vous sûr ? Dites-le une fois, et pour de bon.',
    t3ah='Nuancer, c’est parler avec précision',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. Ce sont des mots précis qui font un travail précis, et '
         'Lexical Resource les récompense &mdash; les verbes modaux et des '
         'tournures comme <em>it is argued that</em> montrent en outre '
         'l’étendue de votre grammaire.',
    t3an='Une nuance n’est pas un tic. <em>Sort of</em> et <em>kind of</em> sont '
         'des tics &mdash; ils ne graduent rien.',
    t3bh='Détachez l’affirmation de vous',
    t3bb='<em>It is often argued that&hellip;</em> et <em>There is a case for '
         'saying&hellip;</em> rapportent une position sans y apposer votre '
         'signature, ce qui vous laisse libre de la démonter une phrase plus '
         'loin.',
    t3bn='Utile sur un sujet que vous connaissez mal : vous pouvez dérouler '
         'l’argument sans le revendiquer.',
    t3ch='Nuancez une fois, pas partout',
    t3cb='Une affirmation graduée donne une impression de jugement. Quatre à la '
         'suite donnent une impression d’esquive, et une réponse qui nuance '
         'chaque proposition a cessé de dire quoi que ce soit.',
    t3cn='Engagez-vous dans la principale, limitez dans la proposition qui suit. '
         'Voilà la forme.',

    mcaEyebrow='Activité 1 · Le cas général',
    mcaTitle='Quelle réponse parle des gens, et pas de vous ?',
    mcbEyebrow='Activité 2 · Sous pression',
    mcbTitle='L’examinateur vient de vous contredire',
    mccEyebrow='Activité 3 · Degrés de certitude',
    mccTitle='À quel point êtes-vous sûr, et comment le dire ?',

    q1why='<em>On the whole</em> en fait une affirmation sur les lecteurs en '
          'général, et la proposition après <em>though</em> la garde honnête. La '
          'réponse sur le polar relève de la Partie 1 ; les deux autres ferment le '
          'sujet.',
    q2why='<em>By and large</em> énonce ce qui est généralement vrai du '
          'groupe. Les trois autres signalent votre propre cas ou votre '
          'propre avis &mdash; très bien pour donner une opinion, mais '
          'aucune ne fait d’une habitude une affirmation générale.',
    q3why='Une raison qui vaut pour la plupart des gens qui déménagent, en '
          'une ligne. Le cousin est un exemple sans affirmation devant lui, '
          'et les deux autres exagèrent ou refusent la question.',
    q4why='Après. L’affirmation est la réponse et l’exemple en est la preuve. '
          'Mettez l’exemple d’abord, et l’examinateur doit attendre pour savoir de '
          'quoi il est la preuve.',
    q5why='Elle accorde l’objection là où elle tient, puis maintient '
          'l’affirmation en vie. Un refus sec ne donne rien à travailler à '
          'l’examinateur ; une capitulation totale non plus.',
    q6why='Une concession suivie de <em>though</em> &mdash; la position y survit. '
          'Les trois autres refusent de bouger, abandonnent l’argument ou rendent '
          'aussitôt la parole.',
    q7why='Aucun problème, à condition de dire que vous le faites. La cohérence, '
          'c’est la possibilité pour l’auditeur de suivre le fil, et un changement '
          'd’avis annoncé se suit facilement.',
    q8why='Si vous savez tenir une position, ou la réviser, en anglais. '
          'L’examinateur n’a aucun intérêt pour le sujet et ne note aucune '
          'opinion &mdash; les quatre critères portent sur la langue.',
    q9why='Une nuance, puis une limite. <em>Arguably possible&hellip; '
          'conceivably</em> est nuancé au point de ne rien dire, <em>It always '
          'works</em> refuse toute gradation, et <em>might possibly '
          'perhaps&hellip; maybe</em> empile quatre nuances sur un seul verbe.',
    q10why='La position disparaît. Fluency and Coherence récompense une ligne '
           'd’argumentation, et une réponse qui n’affirme rien ne laisse aucune '
           'ligne à suivre.',
    q11why='<em>It is often argued that</em> rapporte le point de vue sans '
           'l’adopter. Les trois autres mettent votre nom sur l’affirmation avant '
           'que vous ayez décidé si vous la voulez.',
    q12why='Lexical Resource. Une nuance est un choix de mot précis, et '
           'choisir le bon degré de certitude fait partie de ce que ce '
           'critère récompense &mdash; même si une nuance exprimée par un '
           'modal montre aussi de la grammaire. Aucun descripteur ne compte '
           'combien vous en utilisez.',

    ordEyebrow='Activité 4 · La forme d’une réponse',
    ordTitle='Mettez les quatre étapes dans l’ordre',
    ordHint='Faites-les glisser dans l’ordre &mdash; ou cliquez sur l’une, puis '
            'sur la position voulue.',
    orderWhy='Position, raison, exemple, limite. L’exemple vient en '
             'troisième parce qu’il illustre une affirmation déjà faite '
             '&mdash; commencez par lui et l’examinateur entend une anecdote '
             'plutôt qu’un argument. La limite vient en dernier, et la '
             'réponse se termine sur votre position : vous avez nommé '
             'l’exception vous-même, donc une objection a moins de prise sur '
             'vous.',

    actTitle='Jouez une Partie 3',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='L’un de vous examine, l’autre répond, et un téléphone tient le '
                  'chrono. L’examinateur pose quatre questions sur un seul thème '
                  'et doit contredire au moins deux fois. Cinq minutes, puis '
                  'inversez.',
    actSpeak1='Candidat : répondez d’abord pour les gens en général, et seulement '
              'ensuite donnez un exemple personnel.',
    actSpeak2='Examinateur : contredisez le point le plus fort que vous entendez, '
              'pas le plus faible. Demandez s’il vaut partout.',
    actSpeak3='Candidat : concédez ce qui est juste, gardez le reste, et '
              'dites à quel point vous êtes sûr sans nuancer chaque '
              'proposition.',
    actWriteKind='Écriture · 180–250 mots',
    actWriteBrief='Rédigez votre meilleure réponse à l’une des quatre questions '
                  'qu’on vous a posées, telle que vous auriez voulu la dire : '
                  'position, raison, un exemple, et la concession qui répond à la '
                  'contradiction avant qu’elle n’arrive.',
    actPlaceholder='On the whole, people…',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='IELTS Speaking <em>Parte 3</em>',
    coverSub='La discussione: rispondere per le persone in generale e tenere '
             'la posizione quando l’esaminatore ti contraddice',
    chipLevel='C1 · Avanzato', chipFocus='Speaking Parte 3',
    chipCount='13 domande',

    t1Eyebrow='Prima di cominciare',
    t1Title='La Parte 1 chiedeva di te. La Parte 3 chiede delle persone.',
    t1ah='Cambia la persona',
    t1ab='Parte 1: &ldquo;Do you enjoy cooking?&rdquo; Parte 3: &ldquo;Why do fewer '
         'people cook at home now?&rdquo; La seconda domanda non riguarda la tua '
         'cucina. Rispondi per il gruppo.',
    t1an='Se la risposta sta ancora in piedi dopo averti tolto di mezzo, è una '
         'risposta da Parte 3.',
    t1bh='Tre espressioni che generalizzano',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Ognuna '
         'dice «questo è ciò che di solito è vero», e ognuna lascia spazio alle '
         'eccezioni che l’esaminatore sta per sollevare.',
    t1bn='<em>Tend to</em> vuole un verbo semplice: people <em>tend to '
         'arrive</em> late, mai <em>tend to arriving</em> late.',
    t1ch='La tua vita conta comunque',
    t1cb='Un esempio, messo dopo l’affermazione generale, mostra che ci credi. '
         '<em>A case in point is&hellip;</em> lo segnala come illustrazione e non '
         'come tutta la risposta.',
    t1cn='Un esempio è un sostegno. Tre esempi sono una risposta da Parte 1 che '
         'si è allungata.',

    t2Eyebrow='Prima di cominciare',
    t2Title='Se l’esaminatore ti contraddice, è il compito, non un verdetto',
    t2ah='L’obiezione fa parte del test',
    t2ab='Nella Parte 3 gli esaminatori spesso ti contraddicono &mdash; '
         'chiedono se un’opinione vale ovunque, o presentano l’altra parte '
         '&mdash;, per quanto buona sia la risposta. Non è un segnale che la '
         'risposta fosse debole: è così che la Parte 3 scopre che cosa sai '
         'fare sotto pressione.',
    t2an='Un punto ben costruito può attirare più obiezioni, non meno, '
         'perché vale la pena metterlo alla prova.',
    t2bh='Concedi, poi precisa',
    t2bb='Dai all’altra parte qualcosa di vero, poi tieni la posizione: '
         '<em>That is true up to a point, though&hellip;</em> oppure <em>I would '
         'accept that for smaller towns, but&hellip;</em>',
    t2bn='La frase dopo la concessione porta la tua posizione. Fermarsi alla '
         'concessione è il modo in cui un punto si perde.',
    t2ch='Cambiare idea è permesso',
    t2cb='Dillo ad alta voce e suona come ragionamento: <em>Actually, now that I '
         'say it&hellip;</em> oppure <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='Un dietrofront silenzioso confonde chi ascolta. Uno annunciato è '
         'coerenza, e Fluency and Coherence vale un quarto del voto.',

    t3Eyebrow='Prima di cominciare',
    t3Title='Quanto ne sei sicuro? Dillo una volta, e sul serio.',
    t3ah='Sfumare è linguaggio preciso',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. Sono parole precise che fanno un lavoro preciso, e '
         'Lexical Resource le premia &mdash; e i verbi modali e formule come '
         '<em>it is argued that</em> mostrano anche varietà grammaticale.',
    t3an='Un’attenuazione non è un riempitivo. <em>Sort of</em> e <em>kind '
         'of</em> sono riempitivi &mdash; non graduano niente.',
    t3bh='Stacca l’affermazione da te',
    t3bb='<em>It is often argued that&hellip;</em> e <em>There is a case for '
         'saying&hellip;</em> riportano una posizione senza metterci la tua '
         'firma, e ti lasciano libero di smontarla una frase dopo.',
    t3bn='Utile su un argomento che conosci poco: puoi portare avanti '
         'l’argomentazione senza farla tua.',
    t3ch='Attenua una volta, non dappertutto',
    t3cb='Un’affermazione graduata sembra giudizio. Quattro di fila sembrano '
         'evasione, e una risposta con un’attenuazione in ogni frase ha smesso di '
         'dire qualsiasi cosa.',
    t3cn='Impegnati nella principale, limita nella frase dopo. Questa è la forma.',

    mcaEyebrow='Attività 1 · Il caso generale',
    mcaTitle='Quale risposta parla delle persone, e non di te?',
    mcbEyebrow='Attività 2 · Sotto pressione',
    mcbTitle='L’esaminatore ti ha appena contraddetto',
    mccEyebrow='Attività 3 · Gradi di certezza',
    mccTitle='Quanto sei sicuro, e come lo dici?',

    q1why='<em>On the whole</em> ne fa un’affermazione sui lettori in generale, e '
          'la frase dopo <em>though</em> la mantiene onesta. La risposta sul '
          'giallo va bene per la Parte 1; le altre due chiudono l’argomento.',
    q2why='<em>By and large</em> dice ciò che di solito è vero per il '
          'gruppo. Le altre tre segnalano il tuo caso o la tua opinione '
          '&mdash; vanno bene per esprimere un parere, ma nessuna trasforma '
          'un’abitudine in un’affermazione generale.',
    q3why='Un motivo che vale per la maggior parte di chi si trasferisce, '
          'detto in una riga. Il cugino è un esempio senza un’affermazione '
          'davanti, e le altre due esagerano o rifiutano la domanda.',
    q4why='Dopo. L’affermazione è la risposta e l’esempio ne è la prova. Metti '
          'prima l’esempio e l’esaminatore deve aspettare per capire di che cosa '
          'è la prova.',
    q5why='Concede l’obiezione dove regge, poi tiene viva l’affermazione. Un '
          'rifiuto netto non dà all’esaminatore niente su cui lavorare; una resa '
          'totale nemmeno.',
    q6why='Una concessione seguita da <em>though</em> &mdash; la posizione '
          'sopravvive. Le altre tre si rifiutano di muoversi, abbandonano il punto '
          'o ripassano subito la parola.',
    q7why='Nessun problema, purché tu dica che lo stai facendo. La coerenza '
          'riguarda la possibilità di seguire il filo, e un cambio d’idea '
          'annunciato si segue facilmente.',
    q8why='Se sai tenere una posizione, o rivederla, in inglese. All’esaminatore '
          'l’argomento non interessa e non valuta opinioni &mdash; tutti e '
          'quattro i criteri riguardano la lingua.',
    q9why='Un’attenuazione, poi un limite. <em>Arguably possible&hellip; '
          'conceivably</em> è attenuato fino a non dire niente, <em>It always '
          'works</em> si rifiuta di graduare, e <em>might possibly '
          'perhaps&hellip; maybe</em> ammucchia quattro attenuazioni su un solo '
          'verbo.',
    q10why='La posizione sparisce. Fluency and Coherence premia una linea di '
           'argomentazione, e una risposta che non afferma niente non lascia '
           'nessuna linea da seguire.',
    q11why='<em>It is often argued that</em> riporta il punto di vista senza '
           'farlo proprio. Le altre tre mettono il tuo nome sull’affermazione '
           'prima che tu abbia deciso se la vuoi.',
    q12why='Lexical Resource. Una sfumatura è una scelta lessicale precisa, '
           'e scegliere il giusto grado di certezza fa parte di ciò che quel '
           'criterio premia &mdash; anche se una sfumatura con un modale '
           'mostra pure la grammatica. Nessun descrittore conta quante ne '
           'usi.',

    ordEyebrow='Attività 4 · La forma di una risposta',
    ordTitle='Metti in ordine le quattro mosse',
    ordHint='Trascinale nell’ordine giusto &mdash; oppure clicca su una e poi '
            'sulla posizione che vuoi.',
    orderWhy='Posizione, motivo, esempio, limite. L’esempio viene terzo '
             'perché illustra un’affermazione già fatta &mdash; se inizi da '
             'lì, l’esaminatore sente un aneddoto invece di un argomento. Il '
             'limite viene per ultimo, e la risposta si chiude tornando alla '
             'tua posizione: l’eccezione l’hai già nominata tu, quindi '
             'un’obiezione ha meno appigli.',

    actTitle='Fai una Parte 3',
    actUse='Usane almeno tre:',
    actSpeakBrief='Uno di voi fa l’esaminatore, l’altro risponde, e un telefono '
                  'tiene il tempo. L’esaminatore pone quattro domande su un solo '
                  'argomento e deve contraddire almeno due volte. Cinque minuti, '
                  'poi vi scambiate.',
    actSpeak1='Candidato: rispondi prima per le persone in generale, e solo dopo '
              'dai un esempio tuo.',
    actSpeak2='Esaminatore: contesta la cosa più forte che senti, non la più '
              'debole. Chiedi se vale ovunque.',
    actSpeak3='Candidato: concedi ciò che è giusto, tieni il resto e di’ '
              'quanto sei sicuro senza sfumare ogni frase.',
    actWriteKind='Scrittura · 180–250 parole',
    actWriteBrief='Scrivi la tua risposta migliore a una delle quattro domande che '
                  'ti sono state fatte, come avresti voluto dirla: posizione, '
                  'motivo, un esempio, e la concessione che risponde all’obiezione '
                  'prima che arrivi.',
    actPlaceholder='On the whole, people…',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='IELTS Speaking <em>Parte 3</em>',
    coverSub='A discussão: responder pelas pessoas em geral e manter a '
             'posição quando o examinador contraria',
    chipLevel='C1 · Avançado', chipFocus='Speaking Parte 3',
    chipCount='13 perguntas',

    t1Eyebrow='Antes de começar',
    t1Title='A Parte 1 perguntava por ti. A Parte 3 pergunta pelas pessoas.',
    t1ah='Muda a pessoa',
    t1ab='Parte 1: &ldquo;Do you enjoy cooking?&rdquo; Parte 3: &ldquo;Why do '
         'fewer people cook at home now?&rdquo; A segunda pergunta não é sobre a '
         'tua cozinha. Responde pelo grupo.',
    t1an='Se a resposta continua de pé quando tu sais dela, é uma resposta de '
         'Parte 3.',
    t1bh='Três expressões que generalizam',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Cada uma '
         'diz «isto é o que costuma ser verdade», e cada uma deixa espaço para as '
         'exceções que o examinador está prestes a levantar.',
    t1bn='<em>Tend to</em> leva um verbo simples: people <em>tend to arrive</em> '
         'late, nunca <em>tend to arriving</em> late.',
    t1ch='A tua vida continua a contar',
    t1cb='Um exemplo, colocado depois da afirmação geral, mostra que falas a '
         'sério. <em>A case in point is&hellip;</em> assinala-o como ilustração e '
         'não como a resposta toda.',
    t1cn='Um exemplo é apoio. Três exemplos são uma resposta de Parte 1 que se '
         'alongou.',

    t2Eyebrow='Antes de começar',
    t2Title='Se o examinador te contrariar, é a tarefa, não um veredicto',
    t2ah='A contestação faz parte do teste',
    t2ab='Na Parte 3, os examinadores contrariam muitas vezes &mdash; '
         'perguntam se uma opinião vale em todo o lado ou apresentam o outro '
         'lado &mdash;, por muito boa que seja a resposta. Não é sinal de '
         'que a resposta foi fraca: é assim que a Parte 3 descobre o que '
         'consegues fazer sob pressão.',
    t2an='Um argumento bem feito pode atrair mais objeções, e não menos, '
         'porque vale a pena pô-lo à prova.',
    t2bh='Concede e depois matiza',
    t2bb='Dá ao outro lado algo verdadeiro e depois mantém a tua posição: '
         '<em>That is true up to a point, though&hellip;</em> ou <em>I would '
         'accept that for smaller towns, but&hellip;</em>',
    t2bn='A oração depois da concessão leva a tua posição. Parar na concessão é '
         'a maneira de perder um argumento.',
    t2ch='Mudar de ideias é permitido',
    t2cb='Di-lo em voz alta e soa a raciocínio: <em>Actually, now that I say '
         'it&hellip;</em> ou <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='Uma reviravolta silenciosa confunde quem ouve. Uma anunciada é '
         'coerência, e Fluency and Coherence vale um quarto da nota.',

    t3Eyebrow='Antes de começar',
    t3Title='Até que ponto tens a certeza? Di-lo uma vez, e a sério.',
    t3ah='Atenuar é linguagem precisa',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. São palavras precisas a fazer um trabalho preciso, e o '
         'Lexical Resource premeia-as &mdash; e os verbos modais e fórmulas '
         'como <em>it is argued that</em> mostram também variedade '
         'gramatical.',
    t3an='Um matiz não é um bordão. <em>Sort of</em> e <em>kind of</em> são '
         'bordões &mdash; não graduam nada.',
    t3bh='Afasta a afirmação de ti',
    t3bb='<em>It is often argued that&hellip;</em> e <em>There is a case for '
         'saying&hellip;</em> relatam uma posição sem lhe pores a tua assinatura, '
         'o que te deixa livre para a desmontar uma frase depois.',
    t3bn='Útil num tema que conheces mal: podes desenvolver o argumento sem o '
         'reivindicar.',
    t3ch='Matiza uma vez, não em todo o lado',
    t3cb='Uma afirmação graduada soa a juízo. Quatro seguidas soam a evasão, e '
         'uma resposta com um matiz em cada oração deixou de dizer o que quer que '
         'seja.',
    t3cn='Compromete-te na oração principal e limita na seguinte. É essa a '
         'forma.',

    mcaEyebrow='Atividade 1 · O caso geral',
    mcaTitle='Que resposta fala das pessoas, e não de ti?',
    mcbEyebrow='Atividade 2 · Sob pressão',
    mcbTitle='O examinador acabou de discordar',
    mccEyebrow='Atividade 3 · Graus de certeza',
    mccTitle='Que certeza tens, e como o dizes?',

    q1why='<em>On the whole</em> faz disto uma afirmação sobre os leitores em '
          'geral, e a oração depois de <em>though</em> mantém-na honesta. A '
          'resposta do policial é de Parte 1; as outras duas encerram o tema.',
    q2why='<em>By and large</em> diz o que costuma ser verdade para o grupo. '
          'As outras três assinalam o teu caso ou a tua opinião &mdash; '
          'servem para dar uma opinião, mas nenhuma transforma um hábito '
          'numa afirmação geral.',
    q3why='Uma razão que vale para a maioria das pessoas que se mudam, dita '
          'numa linha. O primo é um exemplo sem nenhuma afirmação à frente, '
          'e as outras duas exageram ou recusam a pergunta.',
    q4why='Depois. A afirmação é a resposta e o exemplo é a prova. Põe o exemplo '
          'primeiro e o examinador tem de esperar para saber de que é que ele é '
          'prova.',
    q5why='Concede a objeção onde ela se aplica e mantém a afirmação viva. Uma '
          'recusa seca não dá ao examinador nada com que trabalhar; uma rendição '
          'total também não.',
    q6why='Uma concessão seguida de <em>though</em> &mdash; a posição sobrevive. '
          'As outras três recusam-se a ceder, abandonam o argumento ou devolvem '
          'logo a palavra.',
    q7why='Não há problema, desde que digas que o estás a fazer. A coerência tem '
          'a ver com quem ouve conseguir seguir o fio, e uma mudança de ideias '
          'anunciada segue-se com facilidade.',
    q8why='Se consegues manter uma posição, ou revê-la, em inglês. O examinador '
          'não tem interesse no tema e não avalia opiniões &mdash; os quatro '
          'critérios são de língua.',
    q9why='Um matiz e depois um limite. <em>Arguably possible&hellip; '
          'conceivably</em> está matizado até não dizer nada, <em>It always '
          'works</em> recusa graduar, e <em>might possibly perhaps&hellip; '
          'maybe</em> empilha quatro matizes num só verbo.',
    q10why='A posição desaparece. Fluency and Coherence premeia uma linha de '
           'argumentação, e uma resposta que não afirma nada não deixa nenhuma '
           'linha para seguir.',
    q11why='<em>It is often argued that</em> relata a opinião sem a adotar. As '
           'outras três põem o teu nome na afirmação antes de decidires se a '
           'queres.',
    q12why='Lexical Resource. Uma atenuação é uma escolha de palavra '
           'precisa, e escolher o grau certo de certeza faz parte do que '
           'esse critério premeia &mdash; embora uma atenuação com um modal '
           'mostre também gramática. Nenhum descritor conta quantas usas.',

    ordEyebrow='Atividade 4 · A forma de uma resposta',
    ordTitle='Põe os quatro passos por ordem',
    ordHint='Arrasta-os para a ordem certa &mdash; ou clica num deles e depois na '
            'posição que quiseres.',
    orderWhy='Posição, razão, exemplo, limite. O exemplo vem em terceiro '
             'porque ilustra uma afirmação já feita &mdash; se começares por '
             'ele, o examinador ouve uma história e não um argumento. O '
             'limite vem no fim, e a resposta termina de novo na tua '
             'posição: já nomeaste tu a exceção, por isso uma objeção tem '
             'menos por onde te apanhar.',

    actTitle='Faz uma Parte 3',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Um de vocês examina, o outro responde, e um telemóvel marca o '
                  'tempo. O examinador faz quatro perguntas sobre um só tema e '
                  'tem de discordar pelo menos duas vezes. Cinco minutos, e depois '
                  'troquem.',
    actSpeak1='Candidato: responde primeiro pelas pessoas em geral, e só depois dá '
              'um exemplo teu.',
    actSpeak2='Examinador: contesta a coisa mais forte que ouvires, não a mais '
              'fraca. Pergunta se vale em todo o lado.',
    actSpeak3='Candidato: concede o que for justo, mantém o resto e diz quão '
              'seguro estás sem atenuar cada frase.',
    actWriteKind='Escrita · 180–250 palavras',
    actWriteBrief='Escreve a tua melhor resposta a uma das quatro perguntas que te '
                  'fizeram, como gostarias de a ter dito: posição, razão, um '
                  'exemplo e a concessão que responde à contestação antes de ela '
                  'chegar.',
    actPlaceholder='On the whole, people…',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='IELTS Speaking <em>Часть 3</em>',
    coverSub='Обсуждение: отвечать за людей в целом и держать позицию, когда '
             'экзаменатор возражает',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking, часть 3',
    chipCount='13 вопросов',

    t1Eyebrow='Прежде чем начать',
    t1Title='Часть 1 спрашивала о вас. Часть 3 спрашивает о людях.',
    t1ah='Меняется лицо',
    t1ab='Часть 1: &ldquo;Do you enjoy cooking?&rdquo; Часть 3: &ldquo;Why do fewer '
         'people cook at home now?&rdquo; Второй вопрос не о вашей кухне. '
         'Отвечайте за группу.',
    t1an='Если ответ устоит, когда вас из него убрать, это ответ для части 3.',
    t1bh='Три обобщающих выражения',
    t1bb='<em>Tend to</em>, <em>on the whole</em>, <em>by and large</em>. Каждое '
         'говорит «так обычно бывает», и каждое оставляет место для исключений, '
         'которые экзаменатор вот-вот назовёт.',
    t1bn='После <em>tend to</em> идёт простой глагол: people <em>tend to '
         'arrive</em> late, никогда не <em>tend to arriving</em> late.',
    t1ch='Ваша жизнь всё равно важна',
    t1cb='Один пример после общего утверждения показывает, что вы говорите '
         'всерьёз. <em>A case in point is&hellip;</em> помечает его как '
         'иллюстрацию, а не как весь ответ.',
    t1cn='Один пример &mdash; это опора. Три примера &mdash; это затянувшийся '
         'ответ для части 1.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Если экзаменатор возражает, это задание, а не приговор',
    t2ah='Возражение &mdash; часть экзамена',
    t2ab='В части 3 экзаменаторы часто возражают &mdash; спрашивают, везде '
         'ли верна ваша точка зрения, или приводят другую сторону, &mdash; '
         'как бы хорош ни был ответ. Это не знак, что ответ слабый: так '
         'часть 3 выясняет, на что вы способны под давлением.',
    t2an='Хорошо построенный довод может вызвать больше возражений, а не '
         'меньше, потому что его стоит проверить на прочность.',
    t2bh='Уступите, затем уточните',
    t2bb='Признайте за другой стороной что-то верное, а потом стойте на своём: '
         '<em>That is true up to a point, though&hellip;</em> или <em>I would '
         'accept that for smaller towns, but&hellip;</em>',
    t2bn='Вашу позицию несёт часть предложения после уступки. Остановиться на '
         'уступке &mdash; значит потерять довод.',
    t2ch='Передумать можно',
    t2cb='Скажите об этом вслух, и это прозвучит как размышление: '
         '<em>Actually, now that I say it&hellip;</em> или <em>On reflection, I '
         'would put that differently.</em>',
    t2cn='Молчаливый разворот сбивает слушателя. Объявленный &mdash; это '
         'связность, а Fluency and Coherence &mdash; четверть оценки.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Насколько вы уверены? Скажите это один раз &mdash; и всерьёз.',
    t3ah='Смягчение &mdash; это точный язык',
    t3ab='<em>Broadly speaking</em>, <em>arguably</em>, <em>in most '
         'cases</em>. Это точные слова, выполняющие точную работу, и Lexical '
         'Resource их вознаграждает, &mdash; а модальные глаголы и '
         'конструкции вроде <em>it is argued that</em> к тому же показывают '
         'грамматический диапазон.',
    t3an='Смягчение &mdash; не слово-паразит. <em>Sort of</em> и <em>kind '
         'of</em> &mdash; паразиты: они ничего не градуируют.',
    t3bh='Снимите утверждение с себя',
    t3bb='<em>It is often argued that&hellip;</em> и <em>There is a case for '
         'saying&hellip;</em> излагают позицию, не ставя под ней вашей подписи, '
         'и оставляют вам свободу разобрать её предложением позже.',
    t3bn='Полезно в теме, которую вы знаете плохо: можно развернуть аргумент, не '
         'присваивая его.',
    t3ch='Смягчайте один раз, а не везде',
    t3cb='Одно градуированное утверждение звучит как суждение. Четыре подряд '
         '&mdash; как уклонение, а ответ со смягчением в каждой части уже '
         'вообще ничего не говорит.',
    t3cn='Утверждайте в главной части, ограничивайте в следующей. Вот и вся '
         'форма.',

    mcaEyebrow='Задание 1 · Общий случай',
    mcaTitle='Какой ответ о людях, а не о вас?',
    mcbEyebrow='Задание 2 · Под давлением',
    mcbTitle='Экзаменатор только что возразил',
    mccEyebrow='Задание 3 · Степени уверенности',
    mccTitle='Насколько вы уверены и как это сказать?',

    q1why='<em>On the whole</em> делает это утверждением о читателях в целом, а '
          'часть после <em>though</em> сохраняет честность. Ответ про детектив '
          'годится для части 1; два других закрывают тему.',
    q2why='<em>By and large</em> говорит о том, что обычно верно для группы. '
          'Остальные три обозначают ваш собственный случай или ваше мнение '
          '&mdash; это годится, чтобы высказать мнение, но ни одно не '
          'превращает привычку в общее утверждение.',
    q3why='Причина, верная для большинства переезжающих, сказанная в одну '
          'строку. Кузен &mdash; пример без утверждения перед ним, а два '
          'других варианта либо преувеличивают, либо уходят от вопроса.',
    q4why='После. Утверждение &mdash; это ответ, а пример &mdash; его '
          'доказательство. Поставьте пример первым, и экзаменатору придётся '
          'ждать, чтобы понять, что он доказывает.',
    q5why='Он признаёт возражение там, где оно верно, и сохраняет утверждение. '
          'Резкий отказ не даёт экзаменатору материала для работы; полная '
          'капитуляция тоже.',
    q6why='Уступка, за которой следует <em>though</em>, &mdash; позиция её '
          'переживает. Остальные три отказываются сдвинуться, бросают довод или '
          'сразу возвращают слово.',
    q7why='Никаких проблем, если вы скажете, что делаете это. Связность &mdash; '
          'это возможность для слушателя следить за нитью, а объявленная смена '
          'мнения легко отслеживается.',
    q8why='Умеете ли вы держать позицию или пересматривать её по-английски. '
          'Экзаменатору тема безразлична, и мнения он не оценивает &mdash; все '
          'четыре критерия касаются языка.',
    q9why='Одно смягчение, затем одно ограничение. <em>Arguably possible&hellip; '
          'conceivably</em> смягчено до полной пустоты, <em>It always works</em> '
          'вообще отказывается от градации, а <em>might possibly '
          'perhaps&hellip; maybe</em> громоздит четыре смягчения на один глагол.',
    q10why='Позиция исчезает. Fluency and Coherence вознаграждает линию '
           'аргументации, а ответ, который ничего не утверждает, не оставляет '
           'линии, за которой можно следить.',
    q11why='<em>It is often argued that</em> излагает мнение, не принимая его. '
           'Три других ставят ваше имя под утверждением раньше, чем вы решили, '
           'нужно ли оно вам.',
    q12why='Lexical Resource. Смягчение &mdash; точный выбор слова, а выбор '
           'нужной степени уверенности входит в то, что вознаграждает этот '
           'критерий, &mdash; хотя смягчение модальным глаголом показывает и '
           'грамматику. Ни один дескриптор не считает, сколько их у вас.',

    ordEyebrow='Задание 4 · Форма ответа',
    ordTitle='Расставьте четыре шага по порядку',
    ordHint='Перетащите их по порядку &mdash; или нажмите на один, а затем на '
            'нужное место.',
    orderWhy='Позиция, причина, пример, ограничение. Пример идёт третьим, '
             'потому что иллюстрирует уже высказанное утверждение, &mdash; '
             'начнёте с него, и экзаменатор услышит историю, а не аргумент. '
             'Ограничение идёт последним, и ответ возвращается к вашей '
             'позиции: исключение вы назвали сами, так что возражению меньше '
             'за что зацепиться.',

    actTitle='Проведите часть 3',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='Один из вас экзаменует, другой отвечает, а телефон следит за '
                  'временем. Экзаменатор задаёт четыре вопроса на одну тему и '
                  'должен возразить хотя бы дважды. Пять минут, потом '
                  'поменяйтесь.',
    actSpeak1='Кандидат: сначала ответьте за людей в целом и только потом '
              'приведите один свой пример.',
    actSpeak2='Экзаменатор: возражайте против самого сильного, что слышите, а не '
              'самого слабого. Спросите, везде ли это верно.',
    actSpeak3='Кандидат: уступите в том, что справедливо, сохраните '
              'остальное и скажите, насколько вы уверены, не смягчая каждую '
              'фразу.',
    actWriteKind='Письмо · 180–250 слов',
    actWriteBrief='Запишите свой лучший ответ на один из четырёх вопросов, которые '
                  'вам задали, так, как вы хотели бы его сказать: позиция, '
                  'причина, один пример и уступка, которая отвечает на возражение '
                  'ещё до того, как оно прозвучит.',
    actPlaceholder='On the whole, people…',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='IELTS Speaking <em>الجزء 3</em>',
    coverSub='النقاش: أن تجيب عن الناس عمومًا، وأن تثبت على موقفك حين يعترض '
             'الممتحن',
    chipLevel='C1 · متقدّم', chipFocus='Speaking · الجزء 3',
    chipCount='13 سؤالًا',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='الجزء 1 سأل عنك. الجزء 3 يسأل عن الناس.',
    t1ah='الشخص يتغيّر',
    t1ab='في الجزء 1: <bdi>&ldquo;Do you enjoy cooking?&rdquo;</bdi> وفي الجزء 3: '
         '<bdi>&ldquo;Why do fewer people cook at home now?&rdquo;</bdi> السؤال '
         'الثاني ليس عن مطبخك. '
         'أجب عن المجموعة.',
    t1an='إذا بقيت الإجابة قائمة بعد أن تُخرج نفسك منها، فهي إجابة للجزء 3.',
    t1bh='ثلاث عبارات للتعميم',
    t1bb='عبارات <em>tend to</em> و<em>on the whole</em> و<em>by and large</em> '
         'تقول كلٌّ منها «هذا ما يصحّ عادةً»، وتترك كلٌّ منها مجالًا للاستثناءات '
         'التي يوشك الممتحن أن يطرحها.',
    t1bn='بعد <em>tend to</em> يأتي فعل مجرّد: <bdi>people <em>tend to '
         'arrive</em> late</bdi>، لا <bdi><em>tend to arriving</em> late</bdi> '
         'أبدًا.',
    t1ch='حياتك تبقى مهمة',
    t1cb='مثال واحد، يأتي بعد الادّعاء العام، يُظهر أنك تعني ما تقول. وعبارة '
         '<em>A case in point is&hellip;</em> تُعلّمه على أنه توضيح لا الإجابة '
         'كلها.',
    t1cn='مثال واحد دعم. وثلاثة أمثلة إجابةٌ للجزء 1 طالت أكثر من اللازم.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='إن اعترض الممتحن، فتلك هي المهمة، لا حكم عليك',
    t2ah='الاعتراض جزء من الاختبار',
    t2ab='كثيرًا ما يعترض الممتحنون في الجزء 3 &mdash; فيسألون هل يصح رأي ما '
         'في كل مكان، أو يطرحون الجانب الآخر &mdash; مهما كانت الإجابة جيدة. '
         'ليس هذا علامة على ضعف الإجابة، بل هو الطريقة التي يكتشف بها الجزء '
         '3 ما تستطيع فعله تحت الضغط.',
    t2an='النقطة المحكمة قد تجلب اعتراضًا أكثر لا أقل، لأنها تستحق أن تُختبر.',
    t2bh='سلِّم ثم قيِّد',
    t2bb='أعطِ الطرف الآخر شيئًا صحيحًا ثم اثبت على موقفك: <em>That is true up '
         'to a point, though&hellip;</em> أو <em>I would accept that for smaller '
         'towns, but&hellip;</em>',
    t2bn='الجملة التي تلي التسليم تحمل موقفك. والتوقّف عند التسليم هو الطريقة '
         'التي تضيع بها الحجّة.',
    t2ch='تغيير رأيك مسموح',
    t2cb='قُله بصوت عالٍ فيبدو تفكيرًا: <em>Actually, now that I say '
         'it&hellip;</em> أو <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='التراجع الصامت يربك السامع، أما المُعلَن فتماسك، وFluency and '
         'Coherence ربع الدرجة.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='ما مدى يقينك؟ قُلها مرة واحدة، واعنِها.',
    t3ah='التحوّط لغة دقيقة',
    t3ab='عبارات <em>broadly speaking</em> و<em>arguably</em> و<em>in most '
         'cases</em> كلمات دقيقة تؤدي عملًا دقيقًا، ويكافئها Lexical '
         'Resource &mdash; كما أن أفعالًا مثل <em>may</em> و<em>might</em> '
         'وصيغًا مثل <em>it is argued that</em> تُظهر تنوعًا نحويًا أيضًا.',
    t3an='التلطيف ليس حشوًا. أما <em>sort of</em> و<em>kind of</em> فحشو، لا '
         'تدرّج شيئًا.',
    t3bh='أبعِد الادّعاء عن نفسك',
    t3bb='عبارتا <em>It is often argued that&hellip;</em> و<em>There is a case '
         'for saying&hellip;</em> تنقلان موقفًا دون أن توقّع عليه، فتبقى حرًّا في '
         'تفكيكه بعد جملة.',
    t3bn='مفيد في موضوع لا تعرف عنه الكثير: تستطيع أن تعرض الحجّة دون أن '
         'تتبنّاها.',
    t3ch='لطِّف مرة، لا في كل مكان',
    t3cb='ادّعاء واحد متدرّج يبدو حكمًا رشيدًا. أربعة متتالية تبدو تهرّبًا، '
         'والإجابة التي تحمل تلطيفًا في كل جملة لم تعد تقول شيئًا على الإطلاق.',
    t3cn='التزم في الجملة الرئيسية، وقيِّد في الجملة التي تليها. هذا هو الشكل.',

    mcaEyebrow='النشاط 1 · الحالة العامة',
    mcaTitle='أيّ إجابة تتحدّث عن الناس لا عنك؟',
    mcbEyebrow='النشاط 2 · تحت الضغط',
    mcbTitle='الممتحن خالفك للتو',
    mccEyebrow='النشاط 3 · درجات اليقين',
    mccTitle='ما مدى يقينك، وكيف تقوله؟',

    q1why='عبارة <em>On the whole</em> تجعله ادّعاءً عن القرّاء عمومًا، والجملة '
          'بعد <em>though</em> تبقيه صادقًا. إجابة الرواية البوليسية مكانها '
          'الجزء 1، والأخريان تغلقان الموضوع.',
    q2why='عبارة <em>by and large</em> تقول ما يصدق عادةً على المجموعة. أما '
          'الثلاث الأخرى فتشير إلى حالتك أو رأيك أنت &mdash; وهي مناسبة '
          'لإبداء الرأي، لكن أيًّا منها لا يحوّل عادة إلى حكم عام.',
    q3why='سبب يصدق على معظم من ينتقلون، في سطر واحد. أما ابن العم فمثال لا '
          'يسبقه ادعاء، والخياران الآخران إما يبالغان وإما يرفضان السؤال.',
    q4why='بعده. الادّعاء هو الإجابة والمثال دليل عليه. ضع المثال أولًا فيضطر '
          'الممتحن إلى الانتظار ليعرف على أيّ شيء هو دليل.',
    q5why='تسلّم بالاعتراض حيث يصحّ، ثم تُبقي الادّعاء حيًّا. الرفض القاطع لا '
          'يعطي الممتحن ما يعمل عليه، والاستسلام التام كذلك.',
    q6why='تسليم يليه <em>though</em>، فيصمد الموقف. أما الثلاث الأخرى فترفض '
          'التزحزح، أو تتخلّى عن الحجّة، أو تعيد الدور فورًا.',
    q7why='لا مشكلة، بشرط أن تقول إنك تفعل ذلك. التماسك يعني أن يستطيع السامع '
          'تتبّع الخيط، وتغيير الرأي المُعلَن سهل التتبّع.',
    q8why='هل تستطيع أن تتمسّك بموقف أو تراجعه بالإنجليزية. الممتحن لا مصلحة له '
          'في الموضوع ولا يقيّم الآراء، والمعايير الأربعة كلها لغة.',
    q9why='تلطيف واحد ثم قيد واحد. عبارة <em>Arguably possible&hellip; '
          'conceivably</em> ملطّفة حتى لا تقول شيئًا، و<em>It always works</em> '
          'ترفض التدرّج أصلًا، و<em>might possibly perhaps&hellip; maybe</em> '
          'تكدّس أربعة تلطيفات على فعل واحد.',
    q10why='يختفي الموقف. Fluency and Coherence يكافئ خطًّا في الحجّة، والإجابة '
           'التي لا تؤكّد شيئًا لا تترك خطًّا يُتتبَّع.',
    q11why='عبارة <em>It is often argued that</em> تنقل الرأي دون تبنّيه. أما '
           'الثلاث الأخرى فتضع اسمك على الادّعاء قبل أن تقرّر هل تريده.',
    q12why='المعيار Lexical Resource. التحوّط اختيار دقيق للكلمة، واختيار '
           'الدرجة الصحيحة من اليقين جزء مما يكافئه هذا المعيار &mdash; وإن '
           'كان التحوّط بفعل مساعد يُظهر النحو أيضًا. ولا يوجد معيار يعدّ كم '
           'مرة تستخدمه.',

    ordEyebrow='النشاط 4 · شكل الإجابة',
    ordTitle='رتّب الخطوات الأربع',
    ordHint='اسحبها إلى الترتيب الصحيح، أو انقر على واحدة ثم على الموضع الذي '
            'تريده.',
    orderWhy='الموقف، ثم السبب، ثم المثال، ثم الحدّ. يأتي المثال ثالثًا لأنه '
             'يوضّح ادعاءً سبق طرحه &mdash; ابدأ به فيسمع الممتحن حكاية لا '
             'حجة. ويأتي الحدّ أخيرًا، فتنتهي الإجابة عائدة إلى موقفك: لقد '
             'سمّيت الاستثناء بنفسك، فيقلّ ما يمسكك به الاعتراض.',

    actTitle='أدِر الجزء 3',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='أحدكما يمتحن والآخر يجيب، والهاتف يضبط الوقت. يطرح الممتحن '
                  'أربعة أسئلة عن موضوع واحد، وعليه أن يعترض مرتين على الأقل. '
                  'خمس دقائق، ثم تبادلا.',
    actSpeak1='المتقدّم: أجب أولًا عن الناس عمومًا، ثم أعطِ مثالًا واحدًا من '
              'حياتك.',
    actSpeak2='الممتحن: اعترض على أقوى ما تسمعه لا على أضعفه. واسأل هل يصحّ في كل '
              'مكان.',
    actSpeak3='المرشح: سلّم بما هو منصف، واحتفظ بالباقي، وقل مدى يقينك من '
              'دون أن تتحوّط في كل جملة.',
    actWriteKind='الكتابة · 180–250 كلمة',
    actWriteBrief='اكتب أفضل إجابة لديك عن أحد الأسئلة الأربعة التي طُرحت عليك، '
                  'كما كنت تتمنّى أن تقولها: الموقف، والسبب، ومثال واحد، والتسليم '
                  'الذي يجيب عن الاعتراض قبل أن يصل.',
    actPlaceholder='On the whole, people…',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='IELTS Speaking <em>第三部分</em>',
    coverSub='讨论：代表一般人来回答，并在考官反驳时守住立场',
    chipLevel='C1 · 高级', chipFocus='Speaking 第三部分',
    chipCount='13 道题',

    t1Eyebrow='开始之前',
    t1Title='第一部分问的是你，第三部分问的是人们。',
    t1ah='主语变了',
    t1ab='第一部分：&ldquo;Do you enjoy cooking?&rdquo; 第三部分：&ldquo;Why do '
         'fewer people cook at home now?&rdquo; 第二个问题问的不是你家的厨房。'
         '要替整个群体回答。',
    t1an='把你自己从答案里拿掉后答案依然成立，那就是第三部分的答案。',
    t1bh='三个表示概括的短语',
    t1bb='<em>Tend to</em>、<em>on the whole</em>、<em>by and large</em>。每一个'
         '都在说“通常是这样”，也都给考官即将提出的例外留了余地。',
    t1bn='<em>Tend to</em> 后面接动词原形：people <em>tend to arrive</em> '
         'late，绝不是 <em>tend to arriving</em> late。',
    t1ch='你自己的经历仍然有用',
    t1cb='在概括性的观点之后放一个例子，说明你是认真的。<em>A case in point '
         'is&hellip;</em> 把它标为例证，而不是整个回答。',
    t1cn='一个例子是支撑；三个例子，就是一个拖长了的第一部分回答。',

    t2Eyebrow='开始之前',
    t2Title='考官反驳，是任务的一部分，不是判决',
    t2ah='反驳是考试的一部分',
    t2ab='第三部分的考官经常会反驳——问你的观点是否处处成立，或提出另一方的看法——不管回答有多好。这并不说明回答差：第三部分正是通过这种方式看'
         '你在压力下能做什么。',
    t2an='论证得好的观点，可能会招来更多而不是更少的反驳，因为它值得推敲。',
    t2bh='先让步，再限定',
    t2bb='先承认对方说得对的部分，然后守住阵地：<em>That is true up to a point, '
         'though&hellip;</em> 或 <em>I would accept that for smaller towns, '
         'but&hellip;</em>',
    t2bn='让步之后的那半句话承载着你的立场。停在让步上，论点就丢了。',
    t2ch='改变想法是允许的',
    t2cb='把它说出来，听起来就是在思考：<em>Actually, now that I say '
         'it&hellip;</em> 或 <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='悄悄转向会让听者困惑；说出来的转向就是连贯，而 Fluency and Coherence '
         '占总分的四分之一。',

    t3Eyebrow='开始之前',
    t3Title='你有多确定？说一次，而且要当真。',
    t3ah='委婉限定是精确的语言',
    t3ab='<em>Broadly speaking</em>、<em>arguably</em>、<em>in most '
         'cases</em>。这些是做精确工作的精确词语，Lexical Resource 会奖励它们——而情态动词和 <em>it is '
         'argued that</em> 这样的句式，也能展示语法的广度。',
    t3an='模糊限制语不是口头禅。<em>Sort of</em> 和 <em>kind of</em> 才是口头禅'
         '——它们什么程度都没表达。',
    t3bh='把观点从自己身上移开',
    t3bb='<em>It is often argued that&hellip;</em> 和 <em>There is a case for '
         'saying&hellip;</em> 转述一个立场而不签上你的名字，让你可以在下一句就'
         '把它拆开。',
    t3bn='在你不太熟悉的话题上很有用：你可以展开论证，而不必认领它。',
    t3ch='限定一次，别处处限定',
    t3cb='一个有分寸的观点显得有判断力。连着四个就显得在回避，而每个分句都加了'
         '限定的回答，已经什么都没说了。',
    t3cn='在主句里表态，在后面的分句里限定。这就是结构。',

    mcaEyebrow='练习 1 · 普遍情况',
    mcaTitle='哪个回答说的是人们，而不是你？',
    mcbEyebrow='练习 2 · 压力之下',
    mcbTitle='考官刚刚反驳了你',
    mccEyebrow='练习 3 · 确定程度',
    mccTitle='有多确定，又怎么说出来？',

    q1why='<em>On the whole</em> 把它变成关于读者整体的观点，<em>though</em> 后面'
          '的分句让它保持实事求是。讲惊悚小说的那个回答属于第一部分；另外两个把'
          '话题聊死了。',
    q2why='<em>By and large</em> 说的是这个群体通常的情况。另外三个标记的是你自己的情况或看法——用来表达观点没问题，但没'
          '有一个能把个人习惯变成一般性的判断。',
    q3why='一个适用于大多数搬家者的理由，一句话说完。表哥是一个前面没有观点的例子，另外两个要么夸大，要么拒绝回答。',
    q4why='在后面。观点是答案，例子是它的证据。把例子放在前面，考官就得等着才知道'
          '它是在证明什么。',
    q5why='它在反驳成立的地方让步，同时让观点继续成立。一口回绝不给考官任何可接的'
          '东西；全盘投降也一样。',
    q6why='让步之后接 <em>though</em>——立场挺过来了。另外三个要么寸步不让，要么'
          '放弃论点，要么立刻把话头交回去。',
    q7why='没问题，只要你说出来你在这么做。连贯指的是听者能否跟上思路，而说出来的'
          '改变想法很好跟。',
    q8why='看你能不能用英语守住一个立场，或修正它。考官对话题本身没有立场，也不给'
          '观点打分——四项标准全是语言。',
    q9why='一个限定，再加一个范围。<em>Arguably possible&hellip; conceivably</em> '
          '限定到什么都没说，<em>It always works</em> 完全拒绝分级，<em>might '
          'possibly perhaps&hellip; maybe</em> 在一个动词上叠了四层限定。',
    q10why='立场消失了。Fluency and Coherence 奖励的是一条论证线，而什么都不断言'
           '的回答，没有任何线可以跟。',
    q11why='<em>It is often argued that</em> 转述观点而不采纳它。另外三个在你还没'
           '决定要不要这个观点之前，就把你的名字签了上去。',
    q12why='Lexical Resource。委婉限定是一种精确的用词，而选对确定的程度，正是这项标准奖励的内容之一——不过用情态动词来限定也'
           '能展示语法。没有任何一条描述会数你用了几个。',

    ordEyebrow='练习 4 · 回答的结构',
    ordTitle='把四个步骤排好顺序',
    ordHint='把它们拖到正确顺序——或者先点一个，再点你想放的位置。',
    orderWhy='立场、理由、例子、限定。例子排第三，因为它是为已经提出的观点作例证——先说例子，考官听到的就是一段故事，而不是论证。限定放在最'
             '后，回答再回到你的立场上：例外已经由你自己点明，反驳能抓住的地方就少了。',

    actTitle='来一轮第三部分',
    actUse='至少用上三个：',
    actSpeakBrief='一人当考官，一人作答，用手机计时。考官就同一个话题问四个问题，'
                  '而且至少要反驳两次。五分钟后交换。',
    actSpeak1='考生：先替普遍的人群作答，然后才举一个自己的例子。',
    actSpeak2='考官：反驳你听到的最有力的观点，而不是最弱的。问它是否处处成立。',
    actSpeak3='考生：承认合理的部分，守住其余的，说出你有多确定，但不要每个分句都加限定。',
    actWriteKind='写作 · 180–250 词',
    actWriteBrief='从你被问到的四个问题里选一个，把你最好的回答写出来，写成你希望'
                  '自己当时说出的样子：立场、理由、一个例子，以及在反驳到来之前就'
                  '回应它的让步。',
    actPlaceholder='On the whole, people…',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='IELTS Speaking <em>パート3</em>',
    coverSub='ディスカッション：人々一般について答え、試験官が反論しても立場を保つ',
    chipLevel='C1 · 上級', chipFocus='Speaking パート3',
    chipCount='13 問',

    t1Eyebrow='始める前に',
    t1Title='パート1はあなたについて。パート3は人々について。',
    t1ah='主語が変わる',
    t1ab='パート1：&ldquo;Do you enjoy cooking?&rdquo; パート3：&ldquo;Why do fewer '
         'people cook at home now?&rdquo; 二つ目の質問は、あなたの台所についてで'
         'はありません。集団について答えましょう。',
    t1an='自分を取り除いても答えが成り立つなら、それはパート3の答えです。',
    t1bh='一般化する三つの表現',
    t1bb='<em>Tend to</em>、<em>on the whole</em>、<em>by and large</em>。どれも'
         '「たいていはこうだ」と言い、試験官がこれから持ち出す例外の余地を残し'
         'ます。',
    t1bn='<em>Tend to</em> の後は動詞の原形です：people <em>tend to arrive</em> '
         'late。<em>tend to arriving</em> late とは決して言いません。',
    t1ch='自分の経験も役に立つ',
    t1cb='一般的な主張の後に例を一つ置けば、本気で言っていることが伝わります。'
         '<em>A case in point is&hellip;</em> は、それが答え全体ではなく例示だと示'
         'します。',
    t1cn='例が一つなら裏づけ。三つなら、長くなったパート1の答えです。',

    t2Eyebrow='始める前に',
    t2Title='試験官が反論しても、それは課題であって判定ではない',
    t2ah='反論は試験の一部',
    t2ab='パート3の試験官は、答えがどれほどよくても、よく反論します――その考えがどこでも成り立つのかを尋ねたり、反対の立場を持ち出したり。答え'
         'が弱かったという合図ではありません。プレッシャーの中で何ができるかを、パート3はこうして確かめるのです。',
    t2an='よくできた主張ほど、反論が減るどころか増えることがあります。押す価値があるからです。',
    t2bh='譲歩してから限定する',
    t2bb='相手側に正しい点を一つ認め、それから踏みとどまります：<em>That is true '
         'up to a point, though&hellip;</em> または <em>I would accept that for '
         'smaller towns, but&hellip;</em>',
    t2bn='譲歩の後の節があなたの立場を運びます。譲歩で止まれば、主張は失われ'
         'ます。',
    t2ch='考えを変えてもいい',
    t2cb='声に出せば、考えている証拠に聞こえます：<em>Actually, now that I say '
         'it&hellip;</em> または <em>On reflection, I would put that '
         'differently.</em>',
    t2cn='黙っての方向転換は聞き手を混乱させます。予告した転換は一貫性で、'
         'Fluency and Coherence は点数の4分の1です。',

    t3Eyebrow='始める前に',
    t3Title='どれくらい確信がある？ 一度だけ、本気で言う。',
    t3ah='ぼかしは正確な言葉',
    t3ab='<em>Broadly speaking</em>、<em>arguably</em>、<em>in most '
         'cases</em>。これらは正確な仕事をする正確な言葉で、Lexical Resource が評価します――さらに助動詞や '
         '<em>it is argued that</em> のような型は、文法の幅も示します。',
    t3an='ぼかしはつなぎ言葉ではありません。<em>Sort of</em> や <em>kind of</em> '
         'はつなぎ言葉で、何の度合いも示しません。',
    t3bh='主張を自分から切り離す',
    t3bb='<em>It is often argued that&hellip;</em> や <em>There is a case for '
         'saying&hellip;</em> は、自分の名前を署名せずに立場を紹介するので、一文後'
         'にそれを崩す自由が残ります。',
    t3bn='よく知らない話題で便利です。主張を自分のものにせずに議論を進められ'
         'ます。',
    t3ch='ぼかすのは一度、全部ではない',
    t3cb='度合いをつけた主張が一つなら判断力に見えます。四つ続けば逃げに見え、す'
         'べての節にぼかしのある答えは、もう何も言っていません。',
    t3cn='主節で言い切り、続く節で限定する。それが型です。',

    mcaEyebrow='演習 1 · 一般的な場合',
    mcaTitle='あなたではなく人々についての答えはどれか？',
    mcbEyebrow='演習 2 · プレッシャーの中で',
    mcbTitle='試験官が今、反論した',
    mccEyebrow='演習 3 · 確信の度合い',
    mccTitle='どれくらい確かで、それをどう言うか？',

    q1why='<em>On the whole</em> で読者一般についての主張になり、<em>though</em> '
          'の後の節が正直さを保っています。スリラーの答えはパート1向きで、ほかの'
          '二つは話題を閉じてしまいます。',
    q2why='<em>By and large</em> は集団について通常成り立つことを述べています。ほかの三つは自分自身の場合や意見を示すもの'
          'で――意見を言うには問題ありませんが、どれも習慣を一般的な主張に変えてはくれません。',
    q3why='引っ越す人の多くに当てはまる理由を一行で。いとこの話は前に主張のない例で、ほかの二つは誇張するか質問を拒んでいます。',
    q4why='後です。主張が答えで、例はその根拠です。例を先に置くと、試験官は何の根'
          '拠なのかがわかるまで待たされます。',
    q5why='反論が当たるところは認め、それでも主張を生かしています。きっぱり拒めば'
          '試験官は何も続けられず、全面降伏でも同じです。',
    q6why='譲歩の後に <em>though</em>――立場はそれを乗り越えます。ほかの三つは動こ'
          'うとしないか、主張を捨てるか、すぐに話を返してしまいます。',
    q7why='そうしていると言えば問題ありません。一貫性とは聞き手が話の筋を追えるか'
          'どうかで、予告された考えの変化は追いやすいのです。',
    q8why='英語で立場を保てるか、あるいは修正できるか。試験官は話題に利害がなく、'
          '意見は採点しません――四つの基準はすべて言語です。',
    q9why='ぼかしを一つ、そして限定を一つ。<em>Arguably possible&hellip; '
          'conceivably</em> はぼかしすぎて何も言っておらず、<em>It always '
          'works</em> は度合いをつけることを拒み、<em>might possibly '
          'perhaps&hellip; maybe</em> は一つの動詞に四つのぼかしを重ねています。',
    q10why='立場が消えます。Fluency and Coherence は議論の筋を評価し、何も主張し'
           'ない答えには追うべき筋がありません。',
    q11why='<em>It is often argued that</em> は、見解を採らずに紹介します。ほかの'
           '三つは、あなたがそれを望むかどうか決める前に、主張にあなたの名前を付け'
           'てしまいます。',
    q12why='Lexical Resource。ぼかしは正確な語の選択で、確信の度合いを正しく選ぶことは、この基準が評価するものの一部です――助'
           '動詞によるぼかしは文法も示しますが。使った数を数える記述はありません。',

    ordEyebrow='演習 4 · 答えの形',
    ordTitle='四つの手順を並べましょう',
    ordHint='ドラッグして並べてください。または一つをクリックしてから、置きたい'
            '位置をクリックします。',
    orderWhy='立場、理由、例、限定。例が三番目なのは、すでに述べた主張を例示するものだからです――例から始めると、試験官には議論ではなく思い'
             '出話に聞こえます。限定は最後に来て、答えはあなたの立場に戻って終わります。例外を自分で挙げてあるので、反論にはつけ入るすきが少'
             'なくなります。',

    actTitle='パート3をやってみる',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='一人が試験官、一人が受験者になり、スマートフォンで時間を計りま'
                  'す。試験官は一つのテーマについて四つ質問し、少なくとも二回は反'
                  '論しなければなりません。五分たったら交代しましょう。',
    actSpeak1='受験者：まず人々一般について答え、そのあとではじめて自分の例を一つ'
              '挙げましょう。',
    actSpeak2='試験官：聞こえた中でいちばん弱い点ではなく、いちばん強い点に反論し'
              'ましょう。それがどこでも成り立つのかを尋ねます。',
    actSpeak3='受験者：もっともな点は認め、残りは守り、すべての節をぼかさずに、どれくらい確かかを示しましょう。',
    actWriteKind='ライティング · 180–250 語',
    actWriteBrief='聞かれた四つの質問から一つ選び、自分が言いたかった形で最高の答'
                  'えを書きましょう：立場、理由、例を一つ、そして反論が来る前にそ'
                  'れに答える譲歩。',
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
