# -*- coding: utf-8 -*-
"""Interface strings for Present Perfect with Lego (B1).

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading. The English being taught — the example
sentences, the stems, the options, the signal words on the sort slide — stays
English throughout.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
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

T['en'] = dict(
    coverTitle='Present Perfect, <em>Brick by Brick</em>',
    coverSub='Two tenses that look the same, and the one question that separates them',
    chipLevel='B1 · Intermediate', chipFocus='Present perfect simple &amp; continuous',
    chipCount='24 slides',

    shEyebrow='Before the questions', shTitle='One tense, two shapes',
    sh1h='The simple form', sh1b=
        '<strong>Have</strong> or <strong>has</strong> + past participle: <em>she '
        '<strong>has built</strong> the castle</em>. It reports a finished action '
        'whose result is still here now.',
    sh1n='The castle exists. That is the point of the sentence.',
    sh2h='The continuous form', sh2b=
        '<strong>Have</strong> or <strong>has been</strong> + <em>-ing</em>: <em>she '
        '<strong>has been building</strong> the castle</em>. It reports the activity '
        'itself, running up to now.',
    sh2n='It may be finished, it may not. The sentence is not saying.',
    sh3h='Both connect past to present', sh3b=
        'Neither one is a past tense. Both say something about <em>now</em>: the '
        'result of the action, or the activity that produced it. Past simple cuts '
        'that link.',
    sh3n='<em>I built it yesterday</em> is over. <em>I have built it</em> reaches into now.',

    chEyebrow='The one question', chTitle='Result, or activity?',
    ch1h='Ask what the sentence is about', ch1b=
        'If it is about the <strong>outcome</strong> &mdash; what now exists, how many '
        'times, whether it is done &mdash; use the simple. If it is about the '
        '<strong>doing</strong> &mdash; how long, why you are tired, the mess on the '
        'table &mdash; use the continuous.',
    ch1n='One question, asked every time. Everything below follows from it.',
    ch2h='Counting means simple', ch2b=
        '<em>Three times</em>, <em>twice</em>, <em>the third time</em> count finished '
        'events, and you cannot count an activity that is still running. <em>He '
        '<strong>has dropped</strong> it three times</em>.',
    ch2n='<em>Has been dropping</em> would describe a habit, not three events.',
    ch3h='Duration means continuous', ch3b=
        '<em>For two days</em>, <em>all morning</em>, <em>since 2019</em> measure how '
        'long. <em>She <strong>has been working</strong> on it for two days</em> '
        '&mdash; the length is the news.',
    ch3n='<em>For</em> and <em>since</em> both take the continuous when duration is the point.',

    stEyebrow='The exception', stTitle='Some verbs have no continuous',
    st1h='State verbs', st1b=
        '<em>Be</em>, <em>have</em> (own), <em>know</em>, <em>like</em>, '
        '<em>believe</em>, <em>seem</em> describe states, not activities. A state has '
        'no <em>-ing</em> form here, however long it lasts.',
    st1n='<em>I have known her for years</em>, never <em>have been knowing</em>.',
    st2h='<em>Have</em> is two verbs', st2b=
        'Owning is a state: <em>How many minifigures <strong>have you got</strong>?</em> '
        'Doing something is not: <em>we <strong>have been having</strong> trouble with '
        'step 12</em> is fine.',
    st2n='If <em>have</em> means <em>own</em>, no continuous. If it means <em>experience</em>, it is allowed.',
    st3h='The tired-hands test', st3b=
        'When a present state is explained by a recent activity, the state takes the '
        'simple and the activity takes the continuous: <em>my hands hurt because I '
        '<strong>have been sorting</strong> pieces</em>.',
    st3n='Two clauses, two tenses, and each one is doing a different job.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Simple or continuous?',
    q1why='<strong>Has built.</strong> <em>Three times</em> counts finished builds, and '
          'counting always takes the simple. <em>This week</em> keeps the period open, '
          'which is why it is not the past simple.',
    q2why='<strong>Has been sorting.</strong> The pieces everywhere are the evidence of '
          'the activity, not of a finished result. That is the continuous&rsquo;s whole '
          'job.',
    q3why='<strong>Haven&rsquo;t opened.</strong> <em>Yet</em> in a negative points at '
          'one expected action that has not happened. There is no activity to describe '
          'here &mdash; nothing has started.',
    q4why='<strong>Has been collecting.</strong> <em>Since he was six</em> measures a '
          'stretch of time that has not ended. Duration takes the continuous.',
    q5why='<strong>Have you got.</strong> <em>Have</em> meaning <em>own</em> is a state '
          'verb, and state verbs have no continuous form &mdash; however long you have '
          'owned them.',
    q6why='<strong>Have been.</strong> <em>Be</em> is a state verb, so the instructions '
          'cannot <em>have been being</em> confusing. The state runs up to now in the '
          'simple.',
    q7why='<strong>Have been sorting.</strong> The hurting hands are a present result '
          'explained by a recent activity, and <em>for the last hour</em> measures it.',

    fibEyebrow='Activity 2 · The exact form', fibTitle='Complete the sentence',
    fibHint='The verb is given in brackets. Contractions are accepted.',
    g1why='<strong>Have finished.</strong> <em>Already</em> marks a completed task with '
          'a result you can act on &mdash; you can start the next set.',
    g2why='<strong>Has been working.</strong> <em>For two days</em> measures how long, '
          'and the crane is still not done.',
    g3why='<strong>Haven&rsquo;t found.</strong> <em>Yet</em> with a negative: one '
          'expected outcome, still missing.',
    g4why='<strong>Have been building.</strong> <em>Since 2019</em> opens a period that '
          'is still running, and every weekend inside it is the activity.',
    g5why='<strong>Has dropped.</strong> <em>The third time</em> counts events, and you '
          'count with the simple.',
    g6why='<strong>Have been reading.</strong> The tired eyes now are explained by the '
          'reading, which is the activity, not the result.',
    g7why='<strong>Has completed.</strong> All twelve are finished and standing &mdash; '
          'a total, so the simple. <em>Have completed</em> is also accepted: British '
          'English treats <em>team</em> as either singular or plural.',

    ordEyebrow='Activity 3 · Sentence building', ordTitle='Put the sentence back together',
    ordHint='Click a chunk to place it, click a placed chunk to take it back.',
    o1why='<strong>She has designed her own spaceship model.</strong> One finished piece '
          'of work, and it exists now.',
    o2why='<strong>He has been painting bricks all morning.</strong> <em>All morning</em> '
          'measures the activity, so the continuous.',
    o3why='<strong>We have never seen such a huge set.</strong> <em>Never</em> asks about '
          'a whole life up to now &mdash; experience, so the simple.',
    o4why='<strong>The twins have been arguing about the instructions.</strong> The '
          'arguing is what the sentence is about, and it may still be going on.',
    o5why='<strong>I have already sorted the blue pieces.</strong> <em>Already</em>: the '
          'job is done and the result is on the table.',
    o6why='<strong>She has been waiting for the new set for months.</strong> <em>For '
          'months</em> is the length of an unfinished wait.',

    sortEyebrow='Activity 4 · The signal words', sortTitle='Which form does each one call for?',
    sortHint='Click a word to place it, click a placed word to take it back.',
    sortWhy='Three of these count or ask about a whole experience &mdash; <em>just</em>, '
            '<em>ever</em>, <em>how many times</em> &mdash; and counting takes the '
            'simple. The other three measure a stretch of time: <em>for the last few '
            'hours</em>, <em>all day</em>, <em>lately</em>. Length takes the continuous. '
            'If you can put a number to it, use the simple; if you can put a clock to '
            'it, use the continuous.',

    actTitle='Report on the build', actUse='Use at least four:',
    actSpeakBrief='One of you has been building all weekend; the other has just walked '
                  'in and wants to know what happened. Three minutes each, then swap.',
    actSpeak1='Say what you have finished today and what you have been working on but not finished.',
    actSpeak2='Explain why the room looks like this. Use the activity, not the result.',
    actSpeak3='Ask your partner three questions with <em>ever</em>, and follow each answer up.',
    actSpeak4='Describe something you have been doing since you were a child.',
    actWriteKind='Writing · 120–150 words',
    actWriteBrief='Write the message you would send a friend after a weekend of '
                  'building. Say what you have finished, what you have been working on, '
                  'how long it has taken, and what you still have not managed. Use both '
                  'forms and make each one earn its place.',
    actPlaceholder='I have finally finished the…',

    resPerfect='Full marks. You are asking the right question — result or activity — every time.',
    resStrong='Strong. Look again at the state verbs; that is usually the last mark.',
    resMid='Good base. Go back to the second slide: counting takes the simple, measuring takes the continuous.',
    resLow='Read the three opening slides again. One question decides all twenty-six of these.',
)

T['de'] = dict(
    coverTitle='Present Perfect, <em>Stein für Stein</em>',
    coverSub='Zwei Formen, die gleich aussehen — und die eine Frage, die sie trennt',
    chipLevel='B1 · Mittelstufe', chipFocus='Present Perfect Simple &amp; Continuous',
    chipCount='24 Folien',

    shEyebrow='Vor den Fragen', shTitle='Eine Zeitform, zwei Gestalten',
    sh1h='Die einfache Form', sh1b=
        '<strong>Have</strong> oder <strong>has</strong> + Partizip II: <em>she '
        '<strong>has built</strong> the castle</em>. Sie meldet eine abgeschlossene '
        'Handlung, deren Ergebnis jetzt noch da ist.',
    sh1n='Die Burg steht. Genau darum geht es dem Satz.',
    sh2h='Die Verlaufsform', sh2b=
        '<strong>Have</strong> oder <strong>has been</strong> + <em>-ing</em>: <em>she '
        '<strong>has been building</strong> the castle</em>. Sie meldet die Tätigkeit '
        'selbst, die bis jetzt läuft.',
    sh2n='Sie kann fertig sein oder nicht. Der Satz sagt das nicht.',
    sh3h='Beide verbinden Vergangenheit und Gegenwart', sh3b=
        'Keine der beiden ist eine Vergangenheitsform. Beide sagen etwas über '
        '<em>jetzt</em>: über das Ergebnis oder über die Tätigkeit dahinter. Das Past '
        'Simple kappt diese Verbindung.',
    sh3n='<em>I built it yesterday</em> ist vorbei. <em>I have built it</em> reicht bis heute.',

    chEyebrow='Die eine Frage', chTitle='Ergebnis oder Tätigkeit?',
    ch1h='Frag, worum es dem Satz geht', ch1b=
        'Geht es um das <strong>Ergebnis</strong> &mdash; was jetzt da ist, wie oft, ob '
        'es fertig ist &mdash;, dann die einfache Form. Geht es um das <strong>Tun</strong> '
        '&mdash; wie lange, warum du müde bist, die Unordnung auf dem Tisch &mdash;, '
        'dann die Verlaufsform.',
    ch1n='Eine Frage, jedes Mal. Alles Weitere folgt daraus.',
    ch2h='Zählen heißt einfache Form', ch2b=
        '<em>Three times</em>, <em>twice</em>, <em>the third time</em> zählen '
        'abgeschlossene Ereignisse, und eine laufende Tätigkeit lässt sich nicht '
        'zählen. <em>He <strong>has dropped</strong> it three times</em>.',
    ch2n='<em>Has been dropping</em> beschriebe eine Gewohnheit, keine drei Ereignisse.',
    ch3h='Dauer heißt Verlaufsform', ch3b=
        '<em>For two days</em>, <em>all morning</em>, <em>since 2019</em> messen, wie '
        'lange. <em>She <strong>has been working</strong> on it for two days</em> '
        '&mdash; die Dauer ist die Nachricht.',
    ch3n='<em>For</em> und <em>since</em> nehmen beide die Verlaufsform, wenn die Dauer zählt.',

    stEyebrow='Die Ausnahme', stTitle='Manche Verben haben keine Verlaufsform',
    st1h='Zustandsverben', st1b=
        '<em>Be</em>, <em>have</em> (besitzen), <em>know</em>, <em>like</em>, '
        '<em>believe</em>, <em>seem</em> beschreiben Zustände, keine Tätigkeiten. Ein '
        'Zustand hat hier keine <em>-ing</em>-Form, so lange er auch dauert.',
    st1n='<em>I have known her for years</em>, nie <em>have been knowing</em>.',
    st2h='<em>Have</em> sind zwei Verben', st2b=
        'Besitzen ist ein Zustand: <em>How many minifigures <strong>have you '
        'got</strong>?</em> Etwas tun nicht: <em>we <strong>have been having</strong> '
        'trouble with step 12</em> geht.',
    st2n='Heißt <em>have</em> „besitzen“, keine Verlaufsform. Heißt es „erleben“, ist sie erlaubt.',
    st3h='Der Müde-Hände-Test', st3b=
        'Erklärt eine Tätigkeit einen gegenwärtigen Zustand, steht der Zustand in der '
        'einfachen Form und die Tätigkeit in der Verlaufsform: <em>my hands hurt '
        'because I <strong>have been sorting</strong> pieces</em>.',
    st3n='Zwei Teilsätze, zwei Formen, und jede tut etwas anderes.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Einfach oder Verlaufsform?',
    q1why='<strong>Has built.</strong> <em>Three times</em> zählt fertige Bauten, und '
          'Zählen nimmt immer die einfache Form. <em>This week</em> hält den Zeitraum '
          'offen — darum kein Past Simple.',
    q2why='<strong>Has been sorting.</strong> Die Teile überall sind der Beleg für die '
          'Tätigkeit, nicht für ein fertiges Ergebnis. Genau dafür ist die Verlaufsform '
          'da.',
    q3why='<strong>Haven&rsquo;t opened.</strong> <em>Yet</em> in einem verneinten Satz '
          'zeigt auf eine erwartete Handlung, die nicht stattgefunden hat. Es gibt hier '
          'keine Tätigkeit zu beschreiben.',
    q4why='<strong>Has been collecting.</strong> <em>Since he was six</em> misst eine '
          'Spanne, die nicht zu Ende ist. Dauer nimmt die Verlaufsform.',
    q5why='<strong>Have you got.</strong> <em>Have</em> im Sinn von „besitzen“ ist ein '
          'Zustandsverb, und Zustandsverben haben keine Verlaufsform.',
    q6why='<strong>Have been.</strong> <em>Be</em> ist ein Zustandsverb; die Anleitung '
          'kann nicht <em>have been being</em> verwirrend sein. Der Zustand reicht in '
          'der einfachen Form bis jetzt.',
    q7why='<strong>Have been sorting.</strong> Die schmerzenden Hände sind ein '
          'gegenwärtiges Ergebnis, erklärt durch eine Tätigkeit, und <em>for the last '
          'hour</em> misst sie.',

    fibEyebrow='Aufgabe 2 · Die genaue Form', fibTitle='Vervollständige den Satz',
    fibHint='Das Verb steht in Klammern. Kurzformen werden akzeptiert.',
    g1why='<strong>Have finished.</strong> <em>Already</em> markiert eine erledigte '
          'Aufgabe mit einem Ergebnis, mit dem man weiterarbeiten kann.',
    g2why='<strong>Has been working.</strong> <em>For two days</em> misst, wie lange — '
          'und der Kran ist noch nicht fertig.',
    g3why='<strong>Haven&rsquo;t found.</strong> <em>Yet</em> mit Verneinung: ein '
          'erwartetes Ergebnis, das noch fehlt.',
    g4why='<strong>Have been building.</strong> <em>Since 2019</em> öffnet einen '
          'Zeitraum, der noch läuft, und jedes Wochenende darin ist die Tätigkeit.',
    g5why='<strong>Has dropped.</strong> <em>The third time</em> zählt Ereignisse, und '
          'gezählt wird mit der einfachen Form.',
    g6why='<strong>Have been reading.</strong> Die müden Augen erklären sich aus dem '
          'Lesen — der Tätigkeit, nicht dem Ergebnis.',
    g7why='<strong>Has completed.</strong> Alle zwölf stehen fertig da — eine '
          'Gesamtzahl, also die einfache Form. <em>Have completed</em> wird ebenfalls '
          'akzeptiert: im britischen Englisch kann <em>team</em> Singular oder Plural '
          'sein.',

    ordEyebrow='Aufgabe 3 · Satzbau', ordTitle='Setze den Satz wieder zusammen',
    ordHint='Klicke einen Baustein an, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',
    o1why='<strong>She has designed her own spaceship model.</strong> Eine fertige '
          'Arbeit, und sie existiert jetzt.',
    o2why='<strong>He has been painting bricks all morning.</strong> <em>All morning</em> '
          'misst die Tätigkeit, also Verlaufsform.',
    o3why='<strong>We have never seen such a huge set.</strong> <em>Never</em> fragt nach '
          'dem ganzen Leben bis jetzt — Erfahrung, also die einfache Form.',
    o4why='<strong>The twins have been arguing about the instructions.</strong> Der '
          'Streit ist das Thema des Satzes und läuft womöglich noch.',
    o5why='<strong>I have already sorted the blue pieces.</strong> <em>Already</em>: '
          'erledigt, und das Ergebnis liegt auf dem Tisch.',
    o6why='<strong>She has been waiting for the new set for months.</strong> <em>For '
          'months</em> ist die Länge eines noch nicht beendeten Wartens.',

    sortEyebrow='Aufgabe 4 · Die Signalwörter', sortTitle='Welche Form verlangt jedes davon?',
    sortHint='Klicke ein Wort an, um es zu setzen; klicke ein gesetztes an, um es zurückzunehmen.',
    sortWhy='Drei davon zählen oder fragen nach der ganzen Erfahrung — <em>just</em>, '
            '<em>ever</em>, <em>how many times</em> —, und Zählen nimmt die einfache '
            'Form. Die anderen drei messen eine Zeitspanne: <em>for the last few '
            'hours</em>, <em>all day</em>, <em>lately</em>. Länge nimmt die Verlaufsform. '
            'Kannst du eine Zahl dranschreiben, nimm die einfache Form; kannst du eine '
            'Uhr dranhalten, die Verlaufsform.',

    actTitle='Berichte vom Bauen', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer hat das ganze Wochenende gebaut, die andere kommt gerade herein '
                  'und will wissen, was passiert ist. Je drei Minuten, dann tauschen.',
    actSpeak1='Sag, was du heute fertig hast und woran du gearbeitet, aber nicht fertig geworden bist.',
    actSpeak2='Erklär, warum der Raum so aussieht. Nimm die Tätigkeit, nicht das Ergebnis.',
    actSpeak3='Stell deinem Partner drei Fragen mit <em>ever</em> und hak jedes Mal nach.',
    actSpeak4='Beschreibe etwas, das du seit deiner Kindheit machst.',
    actWriteKind='Schreiben · 120–150 Wörter',
    actWriteBrief='Schreibe die Nachricht, die du einer Freundin nach einem Wochenende '
                  'voller Bauen schicken würdest. Sag, was du fertig hast, woran du '
                  'gearbeitet hast, wie lange es gedauert hat und was du immer noch nicht '
                  'geschafft hast. Benutze beide Formen, jede mit einem Grund.',
    actPlaceholder='I have finally finished the…',

    resPerfect='Volle Punktzahl. Du stellst jedes Mal die richtige Frage — Ergebnis oder Tätigkeit.',
    resStrong='Stark. Sieh dir die Zustandsverben noch einmal an; dort fehlt meist der letzte Punkt.',
    resMid='Gute Grundlage. Zurück zur zweiten Folie: Zählen nimmt die einfache Form, Messen die Verlaufsform.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Eine Frage entscheidet alle sechsundzwanzig Aufgaben.',
)

T['es'] = dict(
    coverTitle='Present Perfect, <em>pieza a pieza</em>',
    coverSub='Dos formas que se parecen y la única pregunta que las separa',
    chipLevel='B1 · Intermedio', chipFocus='Present perfect simple y continuo',
    chipCount='24 diapositivas',

    shEyebrow='Antes de las preguntas', shTitle='Un tiempo verbal, dos formas',
    sh1h='La forma simple', sh1b=
        '<strong>Have</strong> o <strong>has</strong> + participio: <em>she '
        '<strong>has built</strong> the castle</em>. Informa de una acción terminada '
        'cuyo resultado sigue aquí ahora.',
    sh1n='El castillo existe. De eso va la frase.',
    sh2h='La forma continua', sh2b=
        '<strong>Have</strong> o <strong>has been</strong> + <em>-ing</em>: <em>she '
        '<strong>has been building</strong> the castle</em>. Informa de la actividad '
        'misma, que llega hasta ahora.',
    sh2n='Puede estar terminada o no. La frase no lo dice.',
    sh3h='Las dos unen pasado y presente', sh3b=
        'Ninguna es un tiempo pasado. Las dos dicen algo sobre <em>ahora</em>: el '
        'resultado de la acción o la actividad que lo produjo. El pasado simple corta '
        'ese vínculo.',
    sh3n='<em>I built it yesterday</em> se acabó. <em>I have built it</em> llega hasta hoy.',

    chEyebrow='La única pregunta', chTitle='¿Resultado o actividad?',
    ch1h='Pregunta de qué va la frase', ch1b=
        'Si va del <strong>resultado</strong> &mdash; qué existe ahora, cuántas veces, '
        'si está hecho &mdash;, usa la simple. Si va del <strong>hacer</strong> &mdash; '
        'cuánto tiempo, por qué estás cansado, el desorden en la mesa &mdash;, usa la '
        'continua.',
    ch1n='Una pregunta, siempre la misma. Todo lo demás se deduce.',
    ch2h='Contar pide la forma simple', ch2b=
        '<em>Three times</em>, <em>twice</em>, <em>the third time</em> cuentan sucesos '
        'terminados, y una actividad en marcha no se puede contar. <em>He <strong>has '
        'dropped</strong> it three times</em>.',
    ch2n='<em>Has been dropping</em> describiría una costumbre, no tres sucesos.',
    ch3h='La duración pide la continua', ch3b=
        '<em>For two days</em>, <em>all morning</em>, <em>since 2019</em> miden cuánto '
        'tiempo. <em>She <strong>has been working</strong> on it for two days</em> '
        '&mdash; la duración es la noticia.',
    ch3n='<em>For</em> y <em>since</em> piden la continua cuando lo que importa es la duración.',

    stEyebrow='La excepción', stTitle='Algunos verbos no tienen forma continua',
    st1h='Verbos de estado', st1b=
        '<em>Be</em>, <em>have</em> (poseer), <em>know</em>, <em>like</em>, '
        '<em>believe</em>, <em>seem</em> describen estados, no actividades. Un estado no '
        'tiene forma en <em>-ing</em> aquí, por mucho que dure.',
    st1n='<em>I have known her for years</em>, nunca <em>have been knowing</em>.',
    st2h='<em>Have</em> son dos verbos', st2b=
        'Poseer es un estado: <em>How many minifigures <strong>have you got</strong>?</em> '
        'Hacer algo no lo es: <em>we <strong>have been having</strong> trouble with step '
        '12</em> es correcto.',
    st2n='Si <em>have</em> es «poseer», sin continua. Si es «experimentar», se permite.',
    st3h='La prueba de las manos cansadas', st3b=
        'Cuando una actividad reciente explica un estado presente, el estado va en '
        'simple y la actividad en continua: <em>my hands hurt because I <strong>have '
        'been sorting</strong> pieces</em>.',
    st3n='Dos oraciones, dos formas, y cada una hace un trabajo distinto.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='¿Simple o continua?',
    q1why='<strong>Has built.</strong> <em>Three times</em> cuenta construcciones '
          'terminadas, y contar siempre pide la simple. <em>This week</em> mantiene el '
          'periodo abierto: por eso no es pasado simple.',
    q2why='<strong>Has been sorting.</strong> Las piezas por todas partes son la prueba '
          'de la actividad, no de un resultado terminado. Para eso está la continua.',
    q3why='<strong>Haven&rsquo;t opened.</strong> <em>Yet</em> en negativa señala una '
          'acción esperada que no ha ocurrido. Aquí no hay actividad que describir.',
    q4why='<strong>Has been collecting.</strong> <em>Since he was six</em> mide un tramo '
          'que no ha terminado. La duración pide la continua.',
    q5why='<strong>Have you got.</strong> <em>Have</em> con el sentido de «poseer» es un '
          'verbo de estado, y los verbos de estado no tienen forma continua.',
    q6why='<strong>Have been.</strong> <em>Be</em> es un verbo de estado; las '
          'instrucciones no pueden <em>have been being</em> confusas. El estado llega '
          'hasta ahora en la forma simple.',
    q7why='<strong>Have been sorting.</strong> Las manos doloridas son un resultado '
          'presente explicado por una actividad reciente, y <em>for the last hour</em> '
          'la mide.',

    fibEyebrow='Actividad 2 · La forma exacta', fibTitle='Completa la frase',
    fibHint='El verbo está entre paréntesis. Se aceptan contracciones.',
    g1why='<strong>Have finished.</strong> <em>Already</em> marca una tarea terminada con '
          'un resultado con el que ya se puede seguir.',
    g2why='<strong>Has been working.</strong> <em>For two days</em> mide cuánto tiempo, y '
          'la grúa sigue sin terminar.',
    g3why='<strong>Haven&rsquo;t found.</strong> <em>Yet</em> con negativa: un resultado '
          'esperado que todavía falta.',
    g4why='<strong>Have been building.</strong> <em>Since 2019</em> abre un periodo que '
          'sigue en marcha, y cada fin de semana dentro de él es la actividad.',
    g5why='<strong>Has dropped.</strong> <em>The third time</em> cuenta sucesos, y se '
          'cuenta con la simple.',
    g6why='<strong>Have been reading.</strong> Los ojos cansados se explican por la '
          'lectura, que es la actividad, no el resultado.',
    g7why='<strong>Has completed.</strong> Los doce están terminados y en pie: un total, '
          'así que la simple. <em>Have completed</em> también se acepta: el inglés '
          'británico trata <em>team</em> como singular o plural.',

    ordEyebrow='Actividad 3 · Construcción de frases', ordTitle='Reconstruye la frase',
    ordHint='Haz clic en un fragmento para colocarlo; haz clic en uno colocado para retirarlo.',
    o1why='<strong>She has designed her own spaceship model.</strong> Un trabajo '
          'terminado, y existe ahora.',
    o2why='<strong>He has been painting bricks all morning.</strong> <em>All morning</em> '
          'mide la actividad, así que continua.',
    o3why='<strong>We have never seen such a huge set.</strong> <em>Never</em> pregunta '
          'por toda una vida hasta ahora — experiencia, así que la simple.',
    o4why='<strong>The twins have been arguing about the instructions.</strong> La '
          'discusión es el tema de la frase y puede seguir.',
    o5why='<strong>I have already sorted the blue pieces.</strong> <em>Already</em>: '
          'hecho, y el resultado está sobre la mesa.',
    o6why='<strong>She has been waiting for the new set for months.</strong> <em>For '
          'months</em> es la duración de una espera sin terminar.',

    sortEyebrow='Actividad 4 · Las palabras clave', sortTitle='¿Qué forma pide cada una?',
    sortHint='Haz clic en una palabra para colocarla; haz clic en una colocada para retirarla.',
    sortWhy='Tres de ellas cuentan o preguntan por la experiencia entera — <em>just</em>, '
            '<em>ever</em>, <em>how many times</em> —, y contar pide la simple. Las otras '
            'tres miden un tramo de tiempo: <em>for the last few hours</em>, <em>all '
            'day</em>, <em>lately</em>. La duración pide la continua. Si le puedes poner '
            'un número, usa la simple; si le puedes poner un reloj, la continua.',

    actTitle='Informa sobre la construcción', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno lleva todo el fin de semana construyendo; el otro acaba de entrar '
                  'y quiere saber qué ha pasado. Tres minutos cada uno, luego cambiad.',
    actSpeak1='Di qué has terminado hoy y en qué has estado trabajando sin terminarlo.',
    actSpeak2='Explica por qué la habitación está así. Usa la actividad, no el resultado.',
    actSpeak3='Haz tres preguntas a tu compañero con <em>ever</em> y repregunta cada vez.',
    actSpeak4='Describe algo que llevas haciendo desde que eras pequeño.',
    actWriteKind='Escritura · 120–150 palabras',
    actWriteBrief='Escribe el mensaje que le mandarías a un amigo tras un fin de semana '
                  'construyendo. Di qué has terminado, en qué has estado trabajando, '
                  'cuánto tiempo te ha llevado y qué sigues sin conseguir. Usa las dos '
                  'formas y que cada una se gane su sitio.',
    actPlaceholder='I have finally finished the…',

    resPerfect='Puntuación perfecta. Haces la pregunta correcta — resultado o actividad — cada vez.',
    resStrong='Muy bien. Repasa los verbos de estado; ahí suele quedarse el último punto.',
    resMid='Buena base. Vuelve a la segunda diapositiva: contar pide la simple, medir pide la continua.',
    resLow='Relee las tres diapositivas iniciales. Una sola pregunta decide las veintiséis.',
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
