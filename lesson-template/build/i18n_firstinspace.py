# -*- coding: utf-8 -*-
"""Interface strings for Who Was First in Space? (C1) — English, German, Spanish.

House style §8: the English being taught never translates. The four reading
cards, question stems with a blank, options, gap sentences, the sentence to
build and the target chips stay English in every build. What translates is
the chrome, the card headings, the teaching bodies (six-item form, so the
rule travels with its heading), every explanation and the task instructions.
Grammar tokens stay in CAPS English in every language.

The builder reads its English straight out of T['en'], so there is one copy
of each string.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'btnCopy', 'btnCopied',
        'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Who Was <em>First</em> in Space?',
    coverSub='Before Gagarin, a handful of balloonists watched the blue sky turn black. '
             'Did they get there first?',
    chipLevel='C1 · Advanced', chipFocus='Reading · argument · inversion after ONLY',
    chipCount='25 slides',

    leadEyebrow='Before you read', leadTitle='Three questions to argue about',
    l1h='Who went first?',
    l1b='Who was the first person in space? How sure are you — and how do you know?',
    l2h='Where is the edge?',
    l2b='Where does space begin: 10 km up, 100 km, further? What would you base the line on?',
    l3h='What colour is space?',
    l3b='Why is the day sky blue? What would you expect to see if you kept on climbing?',

    readEyebrow='Read', readEyebrow1='Read · 1 of 4', readEyebrow2='Read · 2 of 4',
    readEyebrow3='Read · 3 of 4', readEyebrow4='Read · 4 of 4',
    r1Title='Where does space begin?',
    r1ah='The official lines', r1bh='The dictionary line',
    r1n='The writer calls the official figures arbitrary: chosen for aircraft, not for space.',
    r2Title='A blue universe',
    r2ah='What people believed', r2bh='The writer’s proposal',
    r2n='A third kind of definition: not practical, not scientific, but historical.',
    r3Title='The balloonists',
    r3ah='1935 · Explorer II', r3bh='1956–57 · Strato-Lab I and Manhigh II',
    r3n='Notice the moment the colour changes from “dark blue” to “black”.',
    r4Title='Faster, but not looking',
    r4ah='The rocket pilots', r4bh='The view that counted',
    r4n='The writer’s verdict: their claim is at least as good as Gagarin’s.',

    qEyebrow='Check your reading', qTitle='Choose the best answer',

    wordsEyebrow='Vocabulary', wordsTitle='Words for limits, records and risk',
    w1h='Drawing lines',
    w1b='<strong>arbitrary</strong> — chosen without a real reason<br>'
        '<strong>delimit</strong> — fix the limits of something<br>'
        '<strong>a benchmark</strong> — the standard you measure by',
    w1n='“These definitions are ultimately arbitrary.”',
    w2h='Firsts and records',
    w2b='<strong>unprecedented</strong> — never done before<br>'
        '<strong>a feat</strong> — an impressive achievement<br>'
        '<strong>within touching distance</strong> — very close to it',
    w2n='“Balloonists were already within touching distance in the 1930s.”',
    w3h='Danger and doubt',
    w3b='<strong>prematurely</strong> — too early<br>'
        '<strong>lethal</strong> — able to kill<br>'
        '<strong>humbled</strong> — made to feel small, less proud',
    w3n='“He returned from his flight humbled.”',
    matchEyebrow='Vocabulary', matchTitle='What do they mean?',
    matchHint='Click a word, then click its meaning.',
    matchWhy='All five come from the article. <strong>Within touching distance</strong> is '
             'figurative: very close to achieving something, not physically near it.',
    vEyebrow='Vocabulary in context', vTitle='Choose the word that fits',

    gramEyebrow='Grammar', gramTitle='ONLY + time or place: inversion',
    g1h='The pattern',
    g1b='Put ONLY + a time or place phrase first, and the AUXILIARY comes before the '
        'SUBJECT, as in a question.',
    g1n='Only in the 17th century <strong>did scientists</strong> begin to imagine a black universe.',
    g2h='Which auxiliary?',
    g2b='Use the auxiliary the sentence already has (BE, HAVE, CAN). If it has none, add '
        'DO / DOES / DID.',
    g2n='Only 630,000 km out <strong>are there</strong> no atoms left. · Only then '
        '<strong>did they</strong> see it.',
    g3h='Why use it?',
    g3b='It puts the surprise first: not earlier, not lower — only here. It is formal, '
        'written and persuasive.',
    g3n='Normal order is still correct: “Scientists only began to imagine it in the 17th century.”',
    gapEyebrow='Grammar', gapTitle='Complete the inversion',
    gapHint='Type one auxiliary from the word bank. Some are not used.',
    bankLabel='Word bank:',
    orderEyebrow='Grammar', orderTitle='Build the sentence',
    orderHint='Click the pieces in order. One piece is left over.',

    argEyebrow='The language of argument', argTitle='How the writer makes the case',
    a1h='Conceding',
    a1b='Grant the obvious point before you push back. It makes the rest sound fair.',
    a1n='“It seems absurd to argue that the Apollo astronauts never visited space — and I’m not going to do that.”',
    a2h='Building the case',
    a2b='Present the claim as arguable rather than proven, and keep it after the concession.',
    a2n='“A good case can be made that …” · “I would still argue that …”',
    a3h='Landing it',
    a3b='End on a measured, personal verdict — firm, but not a fact.',
    a3n='“In my book, their claim is at least as good as Gagarin’s.”',
    sEyebrow='The language of argument', sTitle='Choose the best answer',
    s1stem='Which sentence CONCEDES a point before arguing against it?',

    resNext='Now make your own case →',
    actTitle='Who really went first?', actUse='Use at least three:',
    actSpeakKind='Speaking · in groups',
    actSpeakBrief='Who deserves the title “first in space”? Each person argues for one '
                  'candidate: the balloonists, the rocket pilots, Gagarin, or the Kármán line.',
    actSpeak1='Make your case, but concede one point to the other side first.',
    actSpeak2='Use ONLY + inversion at least once: “Only at 23 km did …”.',
    actSpeak3='Is a definition based on what people SEE more meaningful than one based on a number? Why?',
    actSpeak4='Think of another “first” that depends on the definition — the first computer, the first film. Who really went first?',
    actWriteKind='Writing · 180–220 words',
    actWriteBrief='Write a letter to the editor of a science magazine that ran this article. '
                  'Agree or disagree that the balloonists have as good a claim as Gagarin. '
                  'Concede one point, make your case, end with a verdict.',
    actPlaceholder='Dear Editor, I read with interest your article on …',

    resPerfect='Perfect score. You followed the argument and the grammar that carries it.',
    resStrong='Very good. Check the slides for anything you missed, then try the activation.',
    resMid='A good start. Re-read the four reading slides and the inversion rule, then try again.',
    resLow='Read the article slides again slowly, then the teaching slides, and repeat.',

    q1why='The writer says these limits are about what certain technologies can do — where '
          'wings or balloons stop working — not about where space actually is.',
    q2why='By the dictionary definition space starts where the atmosphere ends, and its last '
          'traces lie about 630,000 km out. No crew has gone that far, not even Apollo 13.',
    q3why='People thought night was Earth’s own shadow, hiding a blue universe beyond it '
          'for a few hours. Scientists only began to picture a black universe in the 17th century.',
    q4why='Stevens and Anderson called it “very dark indeed”, but still blue. Black came in '
          '1956, with Ross and Lewis on Strato-Lab I.',
    q5why='Bridgeman went higher than the balloonists, but only for seconds, and he admitted he '
          'had been too busy to look. The writer’s test is SEEING the sky turn black.',
    q6why='Shatner crossed the Kármán line, yet the moment that felt like space to him was '
          'watching the blue disappear. That supports the writer’s cultural definition.',
    v1why='<strong>Unprecedented</strong> = never done or known before. The other three mean '
          'ordinary or unimportant, the opposite of a record.',
    v2why='<strong>Prematurely</strong> = earlier than planned. A faulty valve ended the flight '
          'after several minutes at the top.',
    s1why='“Admittedly … but …” grants the other side’s point, then pushes back. The other '
          'three simply assert one side.',
    s2why='<strong>In my book</strong> = in my opinion. It is a personal verdict, stated firmly; '
          'it has nothing to do with an actual book.',
    gp1why='ONLY + time phrase first, so the auxiliary comes before the subject. The verb '
           'has no auxiliary of its own, so we add DID (past). COULD also works.',
    gp2why='A general truth, so present: DOES + the sky + begin. DID also works in a story about one flight.',
    gp3why='The sentence already has a modal, so the modal moves: CAN / COULD + a human + survive.',
    gp4why='The verb is BE, so BE itself moves: ARE + there. No DO is needed with BE.',
    ordWhy='ONLY + time phrase, then DID before the subject: “did scientists begin”, not '
           '“scientists did begin”.',
)

T['de'] = dict(
    coverTitle='Wer war <em>zuerst</em> im All?',
    coverSub='Vor Gagarin sahen ein paar Ballonfahrer, wie der blaue Himmel schwarz wurde. '
             'Waren sie zuerst dort?',
    chipLevel='C1 · Fortgeschritten', chipFocus='Lesen · Argumentation · Inversion nach ONLY',
    chipCount='25 Folien',

    leadEyebrow='Vor dem Lesen', leadTitle='Drei Fragen zum Diskutieren',
    l1h='Wer war zuerst?',
    l1b='Wer war der erste Mensch im All? Wie sicher bist du — und woher weißt du das?',
    l2h='Wo ist die Grenze?',
    l2b='Wo beginnt das All: in 10 km Höhe, in 100 km, weiter oben? Worauf würdest du die Grenze stützen?',
    l3h='Welche Farbe hat das All?',
    l3b='Warum ist der Himmel am Tag blau? Was würdest du sehen, wenn du immer weiter steigst?',

    readEyebrow='Lesen', readEyebrow1='Lesen · 1 von 4', readEyebrow2='Lesen · 2 von 4',
    readEyebrow3='Lesen · 3 von 4', readEyebrow4='Lesen · 4 von 4',
    r1Title='Wo beginnt das All?',
    r1ah='Die offiziellen Grenzen', r1bh='Die Grenze laut Wörterbuch',
    r1n='Der Autor nennt die offiziellen Zahlen willkürlich: gewählt für Flugzeuge, nicht für das All.',
    r2Title='Ein blaues Universum',
    r2ah='Was man glaubte', r2bh='Der Vorschlag des Autors',
    r2n='Eine dritte Art von Definition: nicht praktisch, nicht wissenschaftlich, sondern historisch.',
    r3Title='Die Ballonfahrer',
    r3ah='1935 · Explorer II', r3bh='1956–57 · Strato-Lab I und Manhigh II',
    r3n='Achte auf den Moment, in dem die Farbe von „dunkelblau“ zu „schwarz“ wechselt.',
    r4Title='Schneller, aber ohne hinzusehen',
    r4ah='Die Raketenpiloten', r4bh='Der Blick, der zählte',
    r4n='Das Urteil des Autors: Ihr Anspruch ist mindestens so gut wie der von Gagarin.',

    qEyebrow='Leseverständnis', qTitle='Wähle die beste Antwort',

    wordsEyebrow='Wortschatz', wordsTitle='Wörter für Grenzen, Rekorde und Risiko',
    w1h='Grenzen ziehen',
    w1b='<strong>arbitrary</strong> — willkürlich, ohne echten Grund gewählt<br>'
        '<strong>delimit</strong> — die Grenzen von etwas festlegen<br>'
        '<strong>a benchmark</strong> — der Maßstab, an dem man misst',
    w1n='„These definitions are ultimately arbitrary.“',
    w2h='Premieren und Rekorde',
    w2b='<strong>unprecedented</strong> — noch nie dagewesen<br>'
        '<strong>a feat</strong> — eine beeindruckende Leistung<br>'
        '<strong>within touching distance</strong> — ganz kurz davor',
    w2n='„Balloonists were already within touching distance in the 1930s.“',
    w3h='Gefahr und Zweifel',
    w3b='<strong>prematurely</strong> — zu früh, vorzeitig<br>'
        '<strong>lethal</strong> — tödlich<br>'
        '<strong>humbled</strong> — demütig geworden, weniger stolz',
    w3n='„He returned from his flight humbled.“',
    matchEyebrow='Wortschatz', matchTitle='Was bedeuten sie?',
    matchHint='Klicke auf ein Wort, dann auf seine Bedeutung.',
    matchWhy='Alle fünf stammen aus dem Artikel. <strong>Within touching distance</strong> ist '
             'bildlich gemeint: kurz davor, etwas zu erreichen — nicht räumlich nah.',
    vEyebrow='Wortschatz im Kontext', vTitle='Wähle das passende Wort',

    gramEyebrow='Grammatik', gramTitle='ONLY + Zeit oder Ort: Inversion',
    g1h='Das Muster',
    g1b='Steht ONLY + eine Zeit- oder Ortsangabe am Anfang, kommt das AUXILIARY vor das '
        'SUBJECT — wie in einer Frage.',
    g1n='Only in the 17th century <strong>did scientists</strong> begin to imagine a black universe.',
    g2h='Welches Hilfsverb?',
    g2b='Nimm das Hilfsverb, das der Satz schon hat (BE, HAVE, CAN). Hat er keines, ergänze '
        'DO / DOES / DID.',
    g2n='Only 630,000 km out <strong>are there</strong> no atoms left. · Only then '
        '<strong>did they</strong> see it.',
    g3h='Wozu?',
    g3b='Die Überraschung kommt nach vorn: nicht früher, nicht tiefer — nur hier. Formell, '
        'schriftlich und überzeugend.',
    g3n='Die normale Wortstellung bleibt richtig: „Scientists only began to imagine it in the 17th century.“',
    gapEyebrow='Grammatik', gapTitle='Ergänze die Inversion',
    gapHint='Tippe ein Hilfsverb aus der Wortliste. Nicht alle werden gebraucht.',
    bankLabel='Wortliste:',
    orderEyebrow='Grammatik', orderTitle='Bilde den Satz',
    orderHint='Klicke die Teile in der richtigen Reihenfolge an. Ein Teil bleibt übrig.',

    argEyebrow='Die Sprache der Argumentation', argTitle='Wie der Autor argumentiert',
    a1h='Zugeständnis',
    a1b='Räume den offensichtlichen Punkt ein, bevor du widersprichst. So klingt der Rest fair.',
    a1n='“It seems absurd to argue that the Apollo astronauts never visited space — and I’m not going to do that.”',
    a2h='Das Argument aufbauen',
    a2b='Stelle die These als vertretbar dar, nicht als bewiesen — und halte nach dem Zugeständnis an ihr fest.',
    a2n='“A good case can be made that …” · “I would still argue that …”',
    a3h='Der Abschluss',
    a3b='Schließe mit einem maßvollen, persönlichen Urteil — bestimmt, aber keine Tatsache.',
    a3n='“In my book, their claim is at least as good as Gagarin’s.”',
    sEyebrow='Die Sprache der Argumentation', sTitle='Wähle die beste Antwort',
    s1stem='Welcher Satz räumt zuerst einen Punkt ein und argumentiert dann dagegen?',

    resNext='Jetzt vertritt deine eigene Position →',
    actTitle='Wer war wirklich zuerst?', actUse='Verwende mindestens drei:',
    actSpeakKind='Sprechen · in Gruppen',
    actSpeakBrief='Wer verdient den Titel „zuerst im All“? Jede Person vertritt einen '
                  'Kandidaten: die Ballonfahrer, die Raketenpiloten, Gagarin oder die Kármán-Linie.',
    actSpeak1='Vertritt deine Position, aber räume der Gegenseite zuerst einen Punkt ein.',
    actSpeak2='Verwende mindestens einmal ONLY + Inversion: „Only at 23 km did …“.',
    actSpeak3='Ist eine Definition nach dem, was Menschen SEHEN, bedeutsamer als eine Zahl? Warum?',
    actSpeak4='Nenne eine andere „Premiere“, die von der Definition abhängt — der erste Computer, der erste Film. Wer war wirklich zuerst?',
    actWriteKind='Schreiben · 180–220 Wörter',
    actWriteBrief='Schreib einen Leserbrief an die Wissenschaftszeitschrift, die diesen Artikel '
                  'gebracht hat. Stimm zu oder widersprich: Haben die Ballonfahrer einen ebenso '
                  'guten Anspruch wie Gagarin? Räume einen Punkt ein, argumentiere, schließe mit einem Urteil.',
    actPlaceholder='Dear Editor, I read with interest your article on …',

    resPerfect='Volle Punktzahl. Du bist der Argumentation und ihrer Grammatik gefolgt.',
    resStrong='Sehr gut. Sieh dir die Folien zu deinen Fehlern an, dann ab zur Aktivierung.',
    resMid='Ein guter Anfang. Lies die vier Lesefolien und die Inversionsregel noch einmal und versuch es erneut.',
    resLow='Lies die Artikelfolien noch einmal langsam, dann die Lernfolien, und wiederhole.',

    q1why='Der Autor sagt, diese Grenzen beschreiben, was bestimmte Technik kann — wo Flügel '
          'oder Ballone nicht mehr tragen —, nicht, wo das All tatsächlich beginnt.',
    q2why='Laut Wörterbuch beginnt das All dort, wo die Atmosphäre endet, und ihre letzten '
          'Spuren liegen etwa 630.000 km entfernt. So weit ist keine Crew gekommen, nicht einmal Apollo 13.',
    q3why='Man hielt die Nacht für den Schatten der Erde, der ein blaues Universum für einige '
          'Stunden verdeckt. Erst im 17. Jahrhundert stellten sich Forscher ein schwarzes Universum vor.',
    q4why='Stevens und Anderson nannten ihn „very dark indeed“, aber noch blau. Schwarz kam '
          '1956, mit Ross und Lewis in Strato-Lab I.',
    q5why='Bridgeman flog höher als die Ballonfahrer, aber nur Sekunden lang, und er gab zu, '
          'zu beschäftigt zum Hinsehen gewesen zu sein. Der Maßstab des Autors ist das SEHEN des schwarzen Himmels.',
    q6why='Shatner überquerte die Kármán-Linie, doch nach All fühlte sich für ihn der Moment '
          'an, als das Blau verschwand. Das stützt die kulturelle Definition des Autors.',
    v1why='<strong>Unprecedented</strong> = noch nie dagewesen. Die anderen drei bedeuten '
          'gewöhnlich oder unwichtig — das Gegenteil eines Rekords.',
    v2why='<strong>Prematurely</strong> = früher als geplant. Ein defektes Ventil beendete den '
          'Flug nach einigen Minuten in der Höhe.',
    s1why='„Admittedly … but …“ räumt den Punkt der Gegenseite ein und widerspricht dann. Die '
          'anderen drei behaupten nur eine Seite.',
    s2why='<strong>In my book</strong> = meiner Meinung nach. Ein persönliches, bestimmtes '
          'Urteil — mit einem echten Buch hat es nichts zu tun.',
    gp1why='ONLY + Zeitangabe am Anfang, also kommt das Hilfsverb vor das Subjekt. Das Verb hat '
           'kein eigenes Hilfsverb, also ergänzen wir DID (Vergangenheit). COULD geht auch.',
    gp2why='Eine allgemeine Tatsache, also Präsens: DOES + the sky + begin. DID geht auch in einer Erzählung über einen Flug.',
    gp3why='Der Satz hat schon ein Modalverb, also wandert das Modalverb: CAN / COULD + a human + survive.',
    gp4why='Das Verb ist BE, also wandert BE selbst: ARE + there. Bei BE braucht man kein DO.',
    ordWhy='ONLY + Zeitangabe, dann DID vor dem Subjekt: „did scientists begin“, nicht '
           '„scientists did begin“.',
)

T['es'] = dict(
    coverTitle='¿Quién llegó <em>primero</em> al espacio?',
    coverSub='Antes de Gagarin, un puñado de aeronautas en globo vio cómo el cielo azul se '
             'volvía negro. ¿Llegaron ellos primero?',
    chipLevel='C1 · Avanzado', chipFocus='Lectura · argumentación · inversión tras ONLY',
    chipCount='25 diapositivas',

    leadEyebrow='Antes de leer', leadTitle='Tres preguntas para debatir',
    l1h='¿Quién fue primero?',
    l1b='¿Quién fue la primera persona en el espacio? ¿Hasta qué punto estás seguro, y cómo lo sabes?',
    l2h='¿Dónde está el límite?',
    l2b='¿Dónde empieza el espacio: a 10 km, a 100 km, más arriba? ¿En qué basarías esa línea?',
    l3h='¿De qué color es el espacio?',
    l3b='¿Por qué el cielo es azul de día? ¿Qué esperarías ver si siguieras subiendo?',

    readEyebrow='Lectura', readEyebrow1='Lectura · 1 de 4', readEyebrow2='Lectura · 2 de 4',
    readEyebrow3='Lectura · 3 de 4', readEyebrow4='Lectura · 4 de 4',
    r1Title='¿Dónde empieza el espacio?',
    r1ah='Las líneas oficiales', r1bh='La línea del diccionario',
    r1n='El autor llama arbitrarias a las cifras oficiales: pensadas para aviones, no para el espacio.',
    r2Title='Un universo azul',
    r2ah='Lo que se creía', r2bh='La propuesta del autor',
    r2n='Un tercer tipo de definición: ni práctica ni científica, sino histórica.',
    r3Title='Los aeronautas',
    r3ah='1935 · Explorer II', r3bh='1956–57 · Strato-Lab I y Manhigh II',
    r3n='Fíjate en el momento en que el color pasa de «azul oscuro» a «negro».',
    r4Title='Más rápidos, pero sin mirar',
    r4ah='Los pilotos de cohetes', r4bh='La vista que contó',
    r4n='El veredicto del autor: su reivindicación es al menos tan válida como la de Gagarin.',

    qEyebrow='Comprensión lectora', qTitle='Elige la mejor respuesta',

    wordsEyebrow='Vocabulario', wordsTitle='Palabras para límites, récords y riesgo',
    w1h='Trazar líneas',
    w1b='<strong>arbitrary</strong> — arbitrario, elegido sin una razón real<br>'
        '<strong>delimit</strong> — fijar los límites de algo<br>'
        '<strong>a benchmark</strong> — el referente con el que se mide',
    w1n='«These definitions are ultimately arbitrary.»',
    w2h='Primeras veces y récords',
    w2b='<strong>unprecedented</strong> — sin precedentes<br>'
        '<strong>a feat</strong> — una hazaña<br>'
        '<strong>within touching distance</strong> — a un paso de lograrlo',
    w2n='«Balloonists were already within touching distance in the 1930s.»',
    w3h='Peligro y duda',
    w3b='<strong>prematurely</strong> — antes de tiempo<br>'
        '<strong>lethal</strong> — letal, capaz de matar<br>'
        '<strong>humbled</strong> — con más humildad, menos orgulloso',
    w3n='«He returned from his flight humbled.»',
    matchEyebrow='Vocabulario', matchTitle='¿Qué significan?',
    matchHint='Haz clic en una palabra y luego en su significado.',
    matchWhy='Las cinco salen del artículo. <strong>Within touching distance</strong> es '
             'figurado: muy cerca de lograr algo, no cerca físicamente.',
    vEyebrow='Vocabulario en contexto', vTitle='Elige la palabra adecuada',

    gramEyebrow='Gramática', gramTitle='ONLY + tiempo o lugar: inversión',
    g1h='El patrón',
    g1b='Si ONLY + una expresión de tiempo o lugar va al principio, el AUXILIARY va antes del '
        'SUBJECT, como en una pregunta.',
    g1n='Only in the 17th century <strong>did scientists</strong> begin to imagine a black universe.',
    g2h='¿Qué auxiliar?',
    g2b='Usa el auxiliar que ya tiene la oración (BE, HAVE, CAN). Si no tiene ninguno, añade '
        'DO / DOES / DID.',
    g2n='Only 630,000 km out <strong>are there</strong> no atoms left. · Only then '
        '<strong>did they</strong> see it.',
    g3h='¿Para qué?',
    g3b='Pone la sorpresa delante: no antes, no más abajo — solo aquí. Es formal, escrito y persuasivo.',
    g3n='El orden normal sigue siendo correcto: «Scientists only began to imagine it in the 17th century.»',
    gapEyebrow='Gramática', gapTitle='Completa la inversión',
    gapHint='Escribe un auxiliar del banco de palabras. Algunos no se usan.',
    bankLabel='Banco de palabras:',
    orderEyebrow='Gramática', orderTitle='Construye la oración',
    orderHint='Haz clic en las piezas en orden. Sobra una pieza.',

    argEyebrow='El lenguaje de la argumentación', argTitle='Cómo argumenta el autor',
    a1h='Conceder',
    a1b='Admite el punto evidente antes de rebatir. Así el resto suena justo.',
    a1n='“It seems absurd to argue that the Apollo astronauts never visited space — and I’m not going to do that.”',
    a2h='Construir el argumento',
    a2b='Presenta la tesis como defendible, no como demostrada, y mantenla tras la concesión.',
    a2n='“A good case can be made that …” · “I would still argue that …”',
    a3h='Cerrar',
    a3b='Termina con un veredicto personal y mesurado: firme, pero no un hecho.',
    a3n='“In my book, their claim is at least as good as Gagarin’s.”',
    sEyebrow='El lenguaje de la argumentación', sTitle='Elige la mejor respuesta',
    s1stem='¿Qué oración CONCEDE un punto antes de argumentar en contra?',

    resNext='Ahora defiende tu propia postura →',
    actTitle='¿Quién llegó realmente primero?', actUse='Usa al menos tres:',
    actSpeakKind='Expresión oral · en grupos',
    actSpeakBrief='¿Quién merece el título de «primero en el espacio»? Cada persona defiende a '
                  'un candidato: los aeronautas, los pilotos de cohetes, Gagarin o la línea de Kármán.',
    actSpeak1='Defiende tu postura, pero concede antes un punto a la otra parte.',
    actSpeak2='Usa ONLY + inversión al menos una vez: «Only at 23 km did …».',
    actSpeak3='¿Es más significativa una definición basada en lo que se VE que una basada en una cifra? ¿Por qué?',
    actSpeak4='Piensa en otro «primero» que dependa de la definición: el primer ordenador, la primera película. ¿Quién fue realmente primero?',
    actWriteKind='Expresión escrita · 180–220 palabras',
    actWriteBrief='Escribe una carta al director de la revista científica que publicó este '
                  'artículo. ¿Tienen los aeronautas un derecho tan válido como Gagarin? Concede un '
                  'punto, argumenta y termina con un veredicto.',
    actPlaceholder='Dear Editor, I read with interest your article on …',

    resPerfect='Puntuación perfecta. Has seguido el argumento y la gramática que lo sostiene.',
    resStrong='Muy bien. Repasa las diapositivas de lo que fallaste y pasa a la activación.',
    resMid='Buen comienzo. Vuelve a leer las cuatro diapositivas de lectura y la regla de inversión, e inténtalo otra vez.',
    resLow='Lee de nuevo despacio las diapositivas del artículo, luego las de teoría, y repite.',

    q1why='El autor dice que estos límites tienen que ver con lo que pueden hacer ciertas '
          'tecnologías —dónde dejan de sostenerse alas o globos—, no con dónde está el espacio.',
    q2why='Según el diccionario, el espacio empieza donde acaba la atmósfera, y sus últimos '
          'rastros están a unos 630.000 km. Ninguna tripulación ha llegado tan lejos, ni siquiera el Apolo 13.',
    q3why='Se creía que la noche era la sombra de la Tierra, que ocultaba durante unas horas un '
          'universo azul. Hasta el siglo XVII no se empezó a imaginar un universo negro.',
    q4why='Stevens y Anderson lo describieron como «very dark indeed», pero aún azul. El negro '
          'llegó en 1956, con Ross y Lewis en el Strato-Lab I.',
    q5why='Bridgeman subió más que los aeronautas, pero solo unos segundos, y admitió que estaba '
          'demasiado ocupado para mirar. El criterio del autor es VER el cielo volverse negro.',
    q6why='Shatner cruzó la línea de Kármán, pero el momento que para él fue el espacio fue ver '
          'desaparecer el azul. Eso apoya la definición cultural del autor.',
    v1why='<strong>Unprecedented</strong> = sin precedentes. Las otras tres significan corriente '
          'o sin importancia: lo contrario de un récord.',
    v2why='<strong>Prematurely</strong> = antes de lo previsto. Una válvula defectuosa terminó el '
          'vuelo tras unos minutos en la cima.',
    s1why='«Admittedly … but …» concede el punto de la otra parte y luego lo rebate. Las otras '
          'tres solo afirman un lado.',
    s2why='<strong>In my book</strong> = en mi opinión. Es un veredicto personal y firme; no '
          'tiene nada que ver con un libro.',
    gp1why='ONLY + expresión de tiempo al principio, así que el auxiliar va antes del sujeto. El '
           'verbo no tiene auxiliar propio, así que añadimos DID (pasado). COULD también vale.',
    gp2why='Una verdad general, así que presente: DOES + the sky + begin. DID también vale si se narra un vuelo concreto.',
    gp3why='La oración ya tiene un modal, así que se mueve el modal: CAN / COULD + a human + survive.',
    gp4why='El verbo es BE, así que se mueve el propio BE: ARE + there. Con BE no hace falta DO.',
    ordWhy='ONLY + expresión de tiempo, luego DID antes del sujeto: «did scientists begin», no '
           '«scientists did begin».',
)

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
