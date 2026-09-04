# -*- coding: utf-8 -*-
"""Interface strings for Tense Review — Minecraft Edition (B2).

English, German and Spanish, the minimum every deck now ships. Teach-card
bodies use the six-item form, so the rule text moves with its heading rather
than leaving a translated heading over an English paragraph. The English being
*taught* — the tense names, the example sentences, the stems and options —
stays English throughout.
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
    coverTitle='Tenses in the <em>Overworld</em>',
    coverSub='Twelve tenses, thirty questions, and the three decisions that pick between them',
    chipLevel='B2 · Upper-intermediate', chipFocus='The twelve tenses',
    chipCount='21 slides',

    axEyebrow='Before the questions', axTitle='Three questions choose the tense',
    ax1h='When?', ax1b=
        'Past, present or future. This picks the auxiliary and nothing else: '
        '<em>was</em>, <em>is</em>, <em>will be</em>. Every one of the twelve '
        'tenses answers this first.',
    ax1n='Get this wrong and no amount of aspect will rescue the sentence.',
    ax2h='Finished, or still running?', ax2b=
        'The simple form reports a whole event: <em>he built the portal</em>. '
        'The continuous shows it in progress and unfinished at that moment: '
        '<em>he was building the portal</em>.',
    ax2n='This is why an interruption takes the continuous and the interruption itself takes the simple.',
    ax3h='Finished before what?', ax3b=
        'The perfect ties one time to another. <em>Had built</em> is finished '
        'before a past point; <em>has built</em> before now; <em>will have '
        'built</em> before a future point.',
    ax3n='Twelve tenses is three times two times two. Nothing else is going on.',

    pcEyebrow='The family learners avoid', pcTitle='Perfect continuous: how long, up to when',
    pc1h='What it adds', pc1b=
        '<strong>Have been + -ing</strong> takes the perfect&rsquo;s link between '
        'two times and asks how long the activity ran up to the later one. '
        '<em>I have been mining all morning</em> counts the morning.',
    pc1n='The simple perfect counts results; the continuous counts duration.',
    pc2h='All three times', pc2b=
        '<em>She <strong>has been</strong> crafting</em> (up to now), <em>he '
        '<strong>had been</strong> carrying it</em> (up to a past moment), '
        '<em>I <strong>will have been</strong> working nine hours</em> (up to a '
        'future moment).',
    pc2n='The auxiliary changes; <em>been + -ing</em> never does.',
    pc3h='The tell in the sentence', pc3b=
        'A stretch of time (<em>for three days</em>, <em>all morning</em>, '
        '<em>for nine hours</em>) next to a boundary (<em>by the time&hellip;</em>, '
        '<em>since&hellip;</em>) is asking for a perfect continuous.',
    pc3n='No duration in the sentence? Then the simple perfect is almost always right.',

    trEyebrow='The two traps', trTitle='Where B2 loses the marks',
    tr1h='Finished time blocks the present perfect', tr1b=
        '<em>Last year</em>, <em>in 2011</em>, <em>yesterday</em> close the time '
        'off, and the present perfect needs it open. <em>I have visited the End '
        'last year</em> is not English &mdash; it is <em>I visited</em>.',
    tr1n='<em>At the time of writing</em> and <em>since 1.16</em> keep it open, so those take the perfect.',
    tr2h='Time clauses do not take <em>will</em>', tr2b=
        'After <em>when</em>, <em>by the time</em>, <em>as soon as</em>, <em>until</em>, '
        'English uses a present form for future meaning: <em>when the player '
        '<strong>enters</strong> the Deep Dark&hellip;</em>',
        
    tr2n='The main clause still takes <em>will</em>. Only the time clause drops it.',
    tr3h='<em>While</em> wants something in progress', tr3b=
        '<em>While</em> and <em>as</em> set up a background action, so they take a '
        'continuous form. The thing that cuts across it &mdash; the Creeper, the '
        'Ghast &mdash; is a single event and takes the simple.',
    tr3n='<em>While the Wither has destroyed</em> fails on this; it wants <em>was destroying</em>.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Choose the form that fits',
    q1why='<strong>Will have been exploring.</strong> <em>By the time&hellip;</em> sets '
          'a future boundary and <em>for over three days</em> measures the run up to '
          'it &mdash; future perfect continuous.',
    q2why='<strong>Had been carrying.</strong> The carrying was already under way when '
          'the explosion cut across it, and the explosion is in the past &mdash; so '
          'the carrying is further back still.',
    q3why='<strong>Have broken.</strong> <em>Since the 1.16 update</em> opens a period '
          'that has not closed, and the record has been broken repeatedly inside it. '
          'Present perfect simple: the count matters, not the duration.',
    q4why='<strong>Was building.</strong> <em>While</em> marks the background action, '
          'so it takes the continuous; the Ghast&rsquo;s fireball is the single event '
          'that interrupts it and stays simple.',
    q5why='<strong>Responds.</strong> A permanent game mechanic is a general truth, and '
          'general truths take the present simple. Nothing here is in progress or '
          'connected to another time.',
    q6why='<strong>Will have been working.</strong> Same shape as question 1: a future '
          'boundary (<em>by the time the stream ends</em>) and a measured stretch '
          '(<em>nine hours</em>) running up to it.',

    fibEyebrow='Activity 2 · The live commentary', fibTitle='Complete the streamer&rsquo;s sentence',
    fibHint='The tense and the verb are given. Contractions are accepted.',
    g1why='<strong>Have been mining.</strong> The morning is not over and the mining '
          'ran through it &mdash; duration up to now.',
    g2why='<strong>Had built.</strong> The building finished before he logged off, '
          'which is itself in the past. Two past points, so the earlier one goes back '
          'a step.',
    g3why='<strong>Was.</strong> A single completed state at a definite past moment '
          '(this morning, on logging in). No link to another time, so no perfect.',
    g4why='<strong>Is going to be.</strong> A prediction from present evidence &mdash; '
          'he is looking at the run so far. <em>Will</em> would be a decision made on '
          'the spot instead.',
    g5why='<strong>Will have been playing.</strong> <em>By the time I beat the '
          'dragon</em> is the future boundary; <em>almost 100 days</em> is the stretch '
          'running up to it.',
    g6why='<strong>Am fighting.</strong> <em>While</em> again, but this time the '
          'background action is in the present &mdash; so present continuous rather '
          'than past.',
    g7why='<strong>Didn&rsquo;t realise.</strong> <em>Last time</em> is a closed past '
          'reference, which rules out the present perfect and leaves the past simple.',

    sortEyebrow='Activity 3 · Judgement',
    sortTitle='Is the sentence sound, or is the tense wrong?',
    sortHint='Click a sentence to place it, click a placed sentence to take it back.',
    sortWhy='The two failures are the ones on the trap slide. <em>A Creeper was '
            'exploding</em> makes a single sudden event into a background process; an '
            'explosion is over the moment it happens, so it takes the past simple. '
            '<em>I have visited the End last year</em> puts a closed time reference '
            'next to a present perfect, which cannot hold it. The other three are '
            'right: a permanent mechanic in the present simple, an activity still '
            'running in the present perfect continuous, and one past action placed '
            'before another in the past perfect.',

    matchEyebrow='Activity 4 · The register', matchTitle='Match the term to what it means',
    matchHint='Click a term, then click its meaning.',
    matchWhy='These six are how players and streamers actually talk, and none of them '
             'means what a dictionary would guess. <em>Grind</em> is not grinding, '
             '<em>aggro</em> is a verb made from a noun made from an adjective, and '
             '<em>spawn</em> has moved a long way from fish.',

    ecEyebrow='Activity 5 · Repair the sentence', ecTitle='One wrong form in each',
    ecHint='Type the corrected verb only, exactly as it should appear.',
    e1why='<strong>Become.</strong> A permanent game rule is a general truth, so the '
          'present simple. The present continuous would say it is happening right now, '
          'once.',
    e2why='<strong>Released.</strong> <em>In 2011</em> closes the time off, and a '
          'closed time cannot take the present perfect.',
    e3why='<strong>Has sold.</strong> <em>At the time of writing</em> leaves the period '
          'open and the total is still climbing &mdash; present perfect.',
    e4why='<strong>Enters.</strong> After <em>when</em>, English uses a present form '
          'for future meaning. <em>Will</em> stays in the main clause and out of the '
          'time clause.',
    e5why='<strong>Had been working.</strong> The work ran for over a year up to the '
          'announcement, which is itself past &mdash; duration up to a past boundary.',
    e6why='<strong>Was destroying.</strong> <em>While</em> wants the background action '
          'in progress; the player&rsquo;s bed is the single event that happens inside '
          'it.',

    actTitle='Narrate the run', actUse='Use at least four:',
    actSpeakBrief='One of you is the streamer recapping the session, the other is a '
                  'viewer who joined late and needs the story in order. Four minutes '
                  'each, then swap.',
    actSpeak1='Recap the last hour of a game to someone who missed it. Say what had already happened before they arrived.',
    actSpeak2='Describe something you have been doing for weeks and still have not finished.',
    actSpeak3='Predict where your build will be by the end of the month, and say how long you will have been working on it.',
    actSpeak4='Tell the story of something that went wrong while you were doing something else.',
    actWriteKind='Writing · 180–220 words',
    actWriteBrief='Write the day-47 update post for a hardcore survival series. Cover '
                  'what you had done before the session, what you have been working on '
                  'since, what went wrong while you were away from base, and what you '
                  'will have finished by day 50. Use at least six different tenses and '
                  'make each one earn its place.',
    actPlaceholder='Day 47. Before I logged off last night I had already…',

    resPerfect='Full marks. You are choosing tenses by what the sentence needs, not by what sounds familiar.',
    resStrong='Strong. Check the perfect continuous slide once more — that is where the last marks usually sit.',
    resMid='Good base. Go back to the two traps: closed time with the present perfect, and <em>will</em> in a time clause.',
    resLow='Read the three opening slides again. Twelve tenses is three questions, asked in order.',
)

T['de'] = dict(
    coverTitle='Zeiten in der <em>Overworld</em>',
    coverSub='Zwölf Zeitformen, dreißig Fragen und die drei Entscheidungen, die zwischen ihnen wählen',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Die zwölf Zeitformen',
    chipCount='21 Folien',

    axEyebrow='Vor den Fragen', axTitle='Drei Fragen wählen die Zeitform',
    ax1h='Wann?', ax1b=
        'Vergangenheit, Gegenwart oder Zukunft. Das legt nur das Hilfsverb fest: '
        '<em>was</em>, <em>is</em>, <em>will be</em>. Jede der zwölf Zeitformen '
        'beantwortet zuerst diese Frage.',
    ax1n='Stimmt das nicht, rettet kein Aspekt den Satz mehr.',
    ax2h='Abgeschlossen oder noch im Lauf?', ax2b=
        'Die einfache Form meldet ein ganzes Ereignis: <em>he built the portal</em>. '
        'Die Verlaufsform zeigt es in Bewegung und in diesem Moment unabgeschlossen: '
        '<em>he was building the portal</em>.',
    ax2n='Darum steht die Unterbrechung im Simple und das Unterbrochene in der Verlaufsform.',
    ax3h='Abgeschlossen vor was?', ax3b=
        'Das Perfekt verknüpft zwei Zeitpunkte. <em>Had built</em> ist vor einem '
        'Punkt in der Vergangenheit fertig, <em>has built</em> vor jetzt, <em>will '
        'have built</em> vor einem Punkt in der Zukunft.',
    ax3n='Zwölf Zeitformen sind drei mal zwei mal zwei. Mehr passiert hier nicht.',

    pcEyebrow='Die Familie, die alle meiden', pcTitle='Perfect Continuous: wie lange, bis wann',
    pc1h='Was es hinzufügt', pc1b=
        '<strong>Have been + -ing</strong> nimmt die Verbindung des Perfekts zwischen '
        'zwei Zeitpunkten und fragt, wie lange die Handlung bis zum späteren lief. '
        '<em>I have been mining all morning</em> zählt den Vormittag.',
    pc1n='Das einfache Perfekt zählt Ergebnisse, die Verlaufsform zählt Dauer.',
    pc2h='Alle drei Zeitstufen', pc2b=
        '<em>She <strong>has been</strong> crafting</em> (bis jetzt), <em>he '
        '<strong>had been</strong> carrying it</em> (bis zu einem Punkt in der '
        'Vergangenheit), <em>I <strong>will have been</strong> working nine hours</em> '
        '(bis zu einem Punkt in der Zukunft).',
    pc2n='Das Hilfsverb wechselt; <em>been + -ing</em> nie.',
    pc3h='Das Signal im Satz', pc3b=
        'Eine Zeitspanne (<em>for three days</em>, <em>all morning</em>, <em>for nine '
        'hours</em>) neben einer Grenze (<em>by the time&hellip;</em>, '
        '<em>since&hellip;</em>) verlangt ein Perfect Continuous.',
    pc3n='Keine Dauer im Satz? Dann ist fast immer das einfache Perfekt richtig.',

    trEyebrow='Die zwei Fallen', trTitle='Wo B2 die Punkte verliert',
    tr1h='Abgeschlossene Zeit blockiert das Present Perfect', tr1b=
        '<em>Last year</em>, <em>in 2011</em>, <em>yesterday</em> schließen den '
        'Zeitraum ab, und das Present Perfect braucht ihn offen. <em>I have visited '
        'the End last year</em> ist kein Englisch &mdash; es heißt <em>I visited</em>.',
    tr1n='<em>At the time of writing</em> und <em>since 1.16</em> halten ihn offen — dort steht das Perfekt.',
    tr2h='Temporalsätze nehmen kein <em>will</em>', tr2b=
        'Nach <em>when</em>, <em>by the time</em>, <em>as soon as</em>, <em>until</em> '
        'benutzt das Englische eine Präsensform für Zukunftsbedeutung: <em>when the '
        'player <strong>enters</strong> the Deep Dark&hellip;</em>',
    tr2n='Der Hauptsatz behält <em>will</em>. Nur der Temporalsatz verliert es.',
    tr3h='<em>While</em> will etwas im Verlauf', tr3b=
        '<em>While</em> und <em>as</em> eröffnen eine Hintergrundhandlung und verlangen '
        'deshalb eine Verlaufsform. Was quer hineinfährt &mdash; der Creeper, der Ghast '
        '&mdash; ist ein einzelnes Ereignis und steht im Simple.',
    tr3n='<em>While the Wither has destroyed</em> scheitert daran; es braucht <em>was destroying</em>.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Wähle die passende Form',
    q1why='<strong>Will have been exploring.</strong> <em>By the time&hellip;</em> setzt '
          'eine Grenze in der Zukunft, und <em>for over three days</em> misst den Lauf '
          'bis dorthin &mdash; Future Perfect Continuous.',
    q2why='<strong>Had been carrying.</strong> Das Tragen war schon im Gang, als die '
          'Explosion hineinfuhr, und die Explosion liegt in der Vergangenheit &mdash; '
          'das Tragen also noch weiter zurück.',
    q3why='<strong>Have broken.</strong> <em>Since the 1.16 update</em> öffnet einen '
          'Zeitraum, der nicht geschlossen ist, und der Rekord fiel darin mehrfach. '
          'Present Perfect Simple: es zählt die Anzahl, nicht die Dauer.',
    q4why='<strong>Was building.</strong> <em>While</em> markiert die '
          'Hintergrundhandlung, also Verlaufsform; der Feuerball des Ghasts ist das '
          'einzelne Ereignis, das sie unterbricht, und bleibt im Simple.',
    q5why='<strong>Responds.</strong> Eine dauerhafte Spielmechanik ist eine allgemeine '
          'Tatsache, und die steht im Present Simple. Nichts hier läuft gerade ab oder '
          'ist mit einer anderen Zeit verknüpft.',
    q6why='<strong>Will have been working.</strong> Dieselbe Form wie in Frage 1: eine '
          'Grenze in der Zukunft (<em>by the time the stream ends</em>) und eine '
          'gemessene Spanne (<em>nine hours</em>) davor.',

    fibEyebrow='Aufgabe 2 · Der Live-Kommentar', fibTitle='Vervollständige den Satz des Streamers',
    fibHint='Zeitform und Verb sind vorgegeben. Kurzformen werden akzeptiert.',
    g1why='<strong>Have been mining.</strong> Der Vormittag ist nicht vorbei und das '
          'Graben zog sich durch ihn &mdash; Dauer bis jetzt.',
    g2why='<strong>Had built.</strong> Das Bauen war vor dem Ausloggen fertig, und das '
          'Ausloggen liegt selbst in der Vergangenheit. Zwei Punkte, also geht der '
          'frühere einen Schritt zurück.',
    g3why='<strong>Was.</strong> Ein einzelner abgeschlossener Zustand zu einem '
          'bestimmten Zeitpunkt in der Vergangenheit. Keine Verbindung zu einer anderen '
          'Zeit, also kein Perfekt.',
    g4why='<strong>Is going to be.</strong> Eine Vorhersage aus vorliegenden Indizien '
          '&mdash; er sieht den bisherigen Lauf. <em>Will</em> wäre eine Entscheidung '
          'im Moment des Sprechens.',
    g5why='<strong>Will have been playing.</strong> <em>By the time I beat the '
          'dragon</em> ist die Grenze in der Zukunft, <em>almost 100 days</em> die '
          'Spanne davor.',
    g6why='<strong>Am fighting.</strong> Wieder <em>while</em>, aber diesmal liegt die '
          'Hintergrundhandlung in der Gegenwart &mdash; also Present Continuous statt '
          'Past.',
    g7why='<strong>Didn&rsquo;t realise.</strong> <em>Last time</em> ist ein '
          'abgeschlossener Bezug in der Vergangenheit; das schließt das Present Perfect '
          'aus und lässt das Past Simple.',

    sortEyebrow='Aufgabe 3 · Urteil',
    sortTitle='Ist der Satz in Ordnung, oder stimmt die Zeitform nicht?',
    sortHint='Klicke einen Satz an, um ihn zu setzen; klicke einen gesetzten Satz an, um ihn zurückzunehmen.',
    sortWhy='Die zwei Fehler sind genau die von der Fallen-Folie. <em>A Creeper was '
            'exploding</em> macht aus einem einzelnen plötzlichen Ereignis einen '
            'Hintergrundprozess; eine Explosion ist im selben Moment vorbei und steht '
            'im Past Simple. <em>I have visited the End last year</em> stellt einen '
            'abgeschlossenen Zeitbezug neben ein Present Perfect, das ihn nicht tragen '
            'kann. Die anderen drei stimmen: eine dauerhafte Mechanik im Present '
            'Simple, eine noch laufende Tätigkeit im Present Perfect Continuous und '
            'eine vergangene Handlung vor einer anderen im Past Perfect.',

    matchEyebrow='Aufgabe 4 · Das Register', matchTitle='Ordne dem Begriff seine Bedeutung zu',
    matchHint='Klicke einen Begriff an, dann seine Bedeutung.',
    matchWhy='Diese sechs sind, wie Spielerinnen und Streamer tatsächlich reden, und '
             'keines heißt, was ein Wörterbuch vermuten ließe. <em>Grind</em> hat '
             'nichts mit Mahlen zu tun, <em>aggro</em> ist ein Verb aus einem Substantiv '
             'aus einem Adjektiv, und <em>spawn</em> ist weit vom Fischlaich entfernt.',

    ecEyebrow='Aufgabe 5 · Repariere den Satz', ecTitle='In jedem eine falsche Form',
    ecHint='Tippe nur das korrigierte Verb, genau so, wie es dastehen soll.',
    e1why='<strong>Become.</strong> Eine dauerhafte Spielregel ist eine allgemeine '
          'Tatsache, also Present Simple. Das Present Continuous würde sagen, es '
          'passiere gerade jetzt, einmalig.',
    e2why='<strong>Released.</strong> <em>In 2011</em> schließt den Zeitraum ab, und ein '
          'abgeschlossener Zeitraum verträgt kein Present Perfect.',
    e3why='<strong>Has sold.</strong> <em>At the time of writing</em> lässt den Zeitraum '
          'offen, und die Zahl steigt weiter &mdash; Present Perfect.',
    e4why='<strong>Enters.</strong> Nach <em>when</em> benutzt das Englische eine '
          'Präsensform für Zukunftsbedeutung. <em>Will</em> bleibt im Hauptsatz.',
    e5why='<strong>Had been working.</strong> Die Arbeit lief über ein Jahr bis zur '
          'Ankündigung, die selbst vergangen ist &mdash; Dauer bis zu einer Grenze in '
          'der Vergangenheit.',
    e6why='<strong>Was destroying.</strong> <em>While</em> verlangt die '
          'Hintergrundhandlung im Verlauf; das Bett der Spielerin ist das einzelne '
          'Ereignis darin.',

    actTitle='Erzähl den Run', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer ist der Streamer und fasst die Session zusammen, der andere ist '
                  'ein Zuschauer, der spät dazukam und die Geschichte der Reihe nach '
                  'braucht. Je vier Minuten, dann tauschen.',
    actSpeak1='Fasse die letzte Stunde für jemanden zusammen, der sie verpasst hat. Sag, was schon passiert war, bevor er kam.',
    actSpeak2='Beschreibe etwas, das du seit Wochen machst und immer noch nicht fertig hast.',
    actSpeak3='Sag voraus, wo dein Bau Ende des Monats sein wird, und wie lange du dann daran gearbeitet haben wirst.',
    actSpeak4='Erzähl, wie etwas schiefging, während du gerade etwas anderes gemacht hast.',
    actWriteKind='Schreiben · 180–220 Wörter',
    actWriteBrief='Schreibe den Update-Post zu Tag 47 einer Hardcore-Survival-Reihe. '
                  'Sag, was du vor der Session schon erledigt hattest, woran du seitdem '
                  'arbeitest, was schiefging, während du weg von der Basis warst, und '
                  'was du bis Tag 50 fertig haben wirst. Benutze mindestens sechs '
                  'verschiedene Zeitformen, jede mit einem Grund.',
    actPlaceholder='Day 47. Before I logged off last night I had already…',

    resPerfect='Volle Punktzahl. Du wählst die Zeitform nach dem, was der Satz braucht, nicht nach dem, was vertraut klingt.',
    resStrong='Stark. Sieh dir die Folie zum Perfect Continuous noch einmal an — dort liegen meist die letzten Punkte.',
    resMid='Gute Grundlage. Zurück zu den zwei Fallen: abgeschlossene Zeit mit Present Perfect, und <em>will</em> im Temporalsatz.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Zwölf Zeitformen sind drei Fragen, der Reihe nach gestellt.',
)

T['es'] = dict(
    coverTitle='Los tiempos en el <em>Overworld</em>',
    coverSub='Doce tiempos verbales, treinta preguntas y las tres decisiones que eligen entre ellos',
    chipLevel='B2 · Intermedio alto', chipFocus='Los doce tiempos verbales',
    chipCount='21 diapositivas',

    axEyebrow='Antes de las preguntas', axTitle='Tres preguntas eligen el tiempo verbal',
    ax1h='¿Cuándo?', ax1b=
        'Pasado, presente o futuro. Esto fija solo el auxiliar: <em>was</em>, '
        '<em>is</em>, <em>will be</em>. Los doce tiempos responden primero a esta '
        'pregunta.',
    ax1n='Si esto falla, ningún aspecto salva ya la frase.',
    ax2h='¿Terminado o todavía en marcha?', ax2b=
        'La forma simple informa de un suceso completo: <em>he built the portal</em>. '
        'La continua lo muestra en curso y sin terminar en ese momento: <em>he was '
        'building the portal</em>.',
    ax2n='Por eso lo interrumpido va en continuo y la interrupción en simple.',
    ax3h='¿Terminado antes de qué?', ax3b=
        'El perfecto ata un tiempo a otro. <em>Had built</em> está terminado antes de '
        'un punto pasado; <em>has built</em>, antes de ahora; <em>will have built</em>, '
        'antes de un punto futuro.',
    ax3n='Doce tiempos son tres por dos por dos. No pasa nada más.',

    pcEyebrow='La familia que se evita', pcTitle='Perfecto continuo: cuánto tiempo, hasta cuándo',
    pc1h='Qué añade', pc1b=
        '<strong>Have been + -ing</strong> toma el vínculo que el perfecto establece '
        'entre dos momentos y pregunta cuánto duró la actividad hasta el segundo. '
        '<em>I have been mining all morning</em> cuenta la mañana.',
    pc1n='El perfecto simple cuenta resultados; el continuo cuenta duración.',
    pc2h='Los tres momentos', pc2b=
        '<em>She <strong>has been</strong> crafting</em> (hasta ahora), <em>he '
        '<strong>had been</strong> carrying it</em> (hasta un momento pasado), <em>I '
        '<strong>will have been</strong> working nine hours</em> (hasta un momento '
        'futuro).',
    pc2n='El auxiliar cambia; <em>been + -ing</em> nunca.',
    pc3h='La pista en la frase', pc3b=
        'Un tramo de tiempo (<em>for three days</em>, <em>all morning</em>, <em>for '
        'nine hours</em>) junto a un límite (<em>by the time&hellip;</em>, '
        '<em>since&hellip;</em>) está pidiendo un perfecto continuo.',
    pc3n='¿No hay duración en la frase? Entonces casi siempre toca el perfecto simple.',

    trEyebrow='Las dos trampas', trTitle='Dónde se pierden los puntos en B2',
    tr1h='El tiempo cerrado bloquea el present perfect', tr1b=
        '<em>Last year</em>, <em>in 2011</em>, <em>yesterday</em> cierran el periodo, y '
        'el present perfect lo necesita abierto. <em>I have visited the End last '
        'year</em> no es inglés &mdash; es <em>I visited</em>.',
    tr1n='<em>At the time of writing</em> y <em>since 1.16</em> lo dejan abierto, así que ahí sí va el perfecto.',
    tr2h='Las oraciones temporales no llevan <em>will</em>', tr2b=
        'Tras <em>when</em>, <em>by the time</em>, <em>as soon as</em>, <em>until</em>, '
        'el inglés usa una forma de presente con significado futuro: <em>when the '
        'player <strong>enters</strong> the Deep Dark&hellip;</em>',
    tr2n='La oración principal conserva <em>will</em>. Solo la temporal lo pierde.',
    tr3h='<em>While</em> quiere algo en curso', tr3b=
        '<em>While</em> y <em>as</em> abren una acción de fondo, así que piden una forma '
        'continua. Lo que la atraviesa &mdash; el creeper, el ghast &mdash; es un '
        'suceso único y va en simple.',
    tr3n='<em>While the Wither has destroyed</em> falla aquí; pide <em>was destroying</em>.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='Elige la forma que encaja',
    q1why='<strong>Will have been exploring.</strong> <em>By the time&hellip;</em> fija '
          'un límite futuro y <em>for over three days</em> mide el recorrido hasta él '
          '&mdash; futuro perfecto continuo.',
    q2why='<strong>Had been carrying.</strong> Llevaba la espada desde antes de que la '
          'explosión lo cortara, y la explosión ya es pasado &mdash; así que lo otro '
          'está aún más atrás.',
    q3why='<strong>Have broken.</strong> <em>Since the 1.16 update</em> abre un periodo '
          'que no se ha cerrado, y el récord ha caído varias veces dentro de él. '
          'Present perfect simple: importa el número, no la duración.',
    q4why='<strong>Was building.</strong> <em>While</em> marca la acción de fondo, así '
          'que va en continuo; la bola de fuego del ghast es el suceso único que la '
          'interrumpe y se queda en simple.',
    q5why='<strong>Responds.</strong> Una mecánica permanente del juego es una verdad '
          'general, y las verdades generales van en present simple. Aquí nada está en '
          'curso ni conectado con otro momento.',
    q6why='<strong>Will have been working.</strong> La misma forma que en la pregunta 1: '
          'un límite futuro (<em>by the time the stream ends</em>) y un tramo medido '
          '(<em>nine hours</em>) que llega hasta él.',

    fibEyebrow='Actividad 2 · El comentario en directo', fibTitle='Completa la frase del streamer',
    fibHint='Se dan el tiempo verbal y el verbo. Se aceptan contracciones.',
    g1why='<strong>Have been mining.</strong> La mañana no ha terminado y la excavación '
          'la ha recorrido entera &mdash; duración hasta ahora.',
    g2why='<strong>Had built.</strong> La construcción terminó antes de que se '
          'desconectara, y eso ya es pasado. Dos momentos pasados, así que el anterior '
          'retrocede un paso.',
    g3why='<strong>Was.</strong> Un estado único y cerrado en un momento pasado concreto. '
          'Sin vínculo con otro momento, así que sin perfecto.',
    g4why='<strong>Is going to be.</strong> Una predicción a partir de indicios presentes '
          '&mdash; está mirando lo que lleva. <em>Will</em> sería una decisión tomada en '
          'ese instante.',
    g5why='<strong>Will have been playing.</strong> <em>By the time I beat the dragon</em> '
          'es el límite futuro; <em>almost 100 days</em>, el tramo que llega hasta él.',
    g6why='<strong>Am fighting.</strong> Otra vez <em>while</em>, pero ahora la acción de '
          'fondo está en presente &mdash; así que presente continuo, no pasado.',
    g7why='<strong>Didn&rsquo;t realise.</strong> <em>Last time</em> es una referencia '
          'pasada cerrada, lo que descarta el present perfect y deja el pasado simple.',

    sortEyebrow='Actividad 3 · Criterio',
    sortTitle='¿La frase está bien o el tiempo verbal falla?',
    sortHint='Haz clic en una frase para colocarla; haz clic en una colocada para retirarla.',
    sortWhy='Los dos fallos son justo los de la diapositiva de las trampas. <em>A Creeper '
            'was exploding</em> convierte un suceso único y repentino en un proceso de '
            'fondo; una explosión se acaba en el mismo instante, así que va en pasado '
            'simple. <em>I have visited the End last year</em> pone una referencia '
            'temporal cerrada junto a un present perfect, que no la admite. Las otras '
            'tres están bien: una mecánica permanente en present simple, una actividad '
            'aún en marcha en present perfect continuous y una acción pasada situada '
            'antes de otra en past perfect.',

    matchEyebrow='Actividad 4 · El registro', matchTitle='Relaciona el término con su significado',
    matchHint='Haz clic en un término y luego en su significado.',
    matchWhy='Estos seis son como hablan de verdad jugadores y streamers, y ninguno '
             'significa lo que supondría un diccionario. <em>Grind</em> no tiene que ver '
             'con moler, <em>aggro</em> es un verbo sacado de un sustantivo sacado de un '
             'adjetivo, y <em>spawn</em> se ha alejado mucho de los peces.',

    ecEyebrow='Actividad 5 · Repara la frase', ecTitle='Una forma incorrecta en cada una',
    ecHint='Escribe solo el verbo corregido, tal como debe aparecer.',
    e1why='<strong>Become.</strong> Una regla permanente del juego es una verdad general, '
          'así que present simple. El presente continuo diría que ocurre ahora mismo, '
          'una vez.',
    e2why='<strong>Released.</strong> <em>In 2011</em> cierra el periodo, y un periodo '
          'cerrado no admite el present perfect.',
    e3why='<strong>Has sold.</strong> <em>At the time of writing</em> deja el periodo '
          'abierto y el total sigue subiendo &mdash; present perfect.',
    e4why='<strong>Enters.</strong> Tras <em>when</em>, el inglés usa una forma de '
          'presente con significado futuro. <em>Will</em> se queda en la oración '
          'principal.',
    e5why='<strong>Had been working.</strong> El trabajo duró más de un año hasta el '
          'anuncio, que ya es pasado &mdash; duración hasta un límite pasado.',
    e6why='<strong>Was destroying.</strong> <em>While</em> quiere la acción de fondo en '
          'curso; la cama del jugador es el suceso único que ocurre dentro.',

    actTitle='Narra la partida', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno es el streamer que resume la sesión y el otro un espectador que '
                  'llegó tarde y necesita la historia en orden. Cuatro minutos cada uno, '
                  'luego cambiad.',
    actSpeak1='Resume la última hora a alguien que se la perdió. Di qué había pasado ya antes de que llegara.',
    actSpeak2='Describe algo que llevas semanas haciendo y aún no has terminado.',
    actSpeak3='Predice dónde estará tu construcción a final de mes y cuánto tiempo llevarás trabajando en ella.',
    actSpeak4='Cuenta cómo algo salió mal mientras estabas haciendo otra cosa.',
    actWriteKind='Escritura · 180–220 palabras',
    actWriteBrief='Escribe la entrada del día 47 de una serie de supervivencia hardcore. '
                  'Cuenta qué habías hecho antes de la sesión, en qué llevas trabajando '
                  'desde entonces, qué salió mal mientras estabas lejos de la base y qué '
                  'habrás terminado para el día 50. Usa al menos seis tiempos verbales '
                  'distintos y que cada uno se gane su sitio.',
    actPlaceholder='Day 47. Before I logged off last night I had already…',

    resPerfect='Puntuación perfecta. Eliges el tiempo por lo que pide la frase, no por lo que te suena.',
    resStrong='Muy bien. Repasa una vez más la diapositiva del perfecto continuo — ahí suelen quedar los últimos puntos.',
    resMid='Buena base. Vuelve a las dos trampas: tiempo cerrado con present perfect, y <em>will</em> en una oración temporal.',
    resLow='Relee las tres diapositivas iniciales. Doce tiempos son tres preguntas, hechas en orden.',
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
