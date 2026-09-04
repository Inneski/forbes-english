# -*- coding: utf-8 -*-
"""Interface strings for Active & Passive Voice, Lego edition (B1).

English, German and Spanish. Teach-card bodies use the six-item form so the
rule travels with its heading. The English being taught — the example
sentences, the stems, the options — stays English throughout.

The original page's explanations named option letters ("option C is wrong
because…"). Positions are dealt fresh in `pav_data.py` and shuffled again at
runtime, so every explanation here names the language instead, which is what
it should have done anyway.
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
    coverTitle='Active &amp; <em>Passive</em>',
    coverSub='Who did it, who it was done to, and when English decides not to say',
    chipLevel='B1 · Intermediate', chipFocus='The passive voice',
    chipCount='19 slides',

    voEyebrow='Before the questions', voTitle='Two voices, one event',
    vo1h='Active: the subject acts', vo1b=
        'Subject, verb, object. <em>Lego <strong>releases</strong> new sets every '
        'year.</em> The subject does the releasing, and this is the ordinary way '
        'English puts a sentence together.',
    vo1n='Direct, short, and the right default. The passive is the marked choice.',
    vo2h='Passive: the subject receives', vo2b=
        '<strong>Be</strong> + past participle. <em>New sets <strong>are '
        'released</strong> every year.</em> The subject is on the receiving end, and '
        'the doer can be named with <em>by</em> or left out entirely.',
    vo2n='Same event, different thing in the spotlight.',
    vo3h='Three steps to turn one into the other', vo3b=
        'The object becomes the subject; the verb becomes <em>be</em> + past '
        'participle <strong>in the original tense</strong>; the old subject becomes '
        '<em>by</em> + agent, and that part is optional.',
    vo3n='<em>Ole Kirk Christiansen founded Lego</em> &rarr; <em>Lego was founded by Ole Kirk Christiansen</em>.',

    tnEyebrow='The mechanism', tnTitle='<em>Be</em> carries the tense, always',
    tn1h='The simple tenses', tn1b=
        'Present: <em>Lego makes bricks</em> &rarr; <em>bricks <strong>are made</strong></em>. '
        'Past: <em>they built a castle</em> &rarr; <em>a castle <strong>was built</strong></em>. '
        'Only <em>be</em> moves; the participle never changes.',
    tn1n='<em>Is / are</em> for the present, <em>was / were</em> for the past.',
    tn2h='The perfect tenses', tn2b=
        '<em>She has tested the set</em> &rarr; <em>the set <strong>has been '
        'tested</strong></em>. <em>He had launched it</em> &rarr; <em>it <strong>had '
        'been launched</strong></em>. The perfect keeps its auxiliary and adds '
        '<em>been</em>.',
    tn2n='<em>Has been</em>, <em>had been</em> &mdash; two words, and both are needed.',
    tn3h='Modals and the infinitive', tn3b=
        'After a modal, <em>be</em> stays bare: <em>you can assemble it</em> &rarr; '
        '<em>it <strong>can be assembled</strong></em>. The passive infinitive is '
        '<em>to be</em> + past participle: <em>designs that might <strong>be turned '
        'into</strong> sets</em>.',
    tn3n='A modal never takes <em>been</em>. <em>Can been assembled</em> is not English.',

    whEyebrow='Why bother', whTitle='When the passive is the better sentence',
    wh1h='When nobody knows who', wh1b=
        '<em>The brick <strong>was dropped</strong>.</em> If the doer is unknown, or '
        'obvious, or beside the point, the active forces you to invent a subject. '
        'The passive lets you leave it out.',
    wh1n='It is not evasion. Often it is simply the only honest sentence available.',
    wh2h='When the result is the news', wh2b=
        'Reports, labels, instructions and science put the thing first: <em>the design '
        '<strong>was patented</strong> in 1958</em>. The patent office is not what the '
        'sentence is about.',
    wh2n='This is why formal writing uses it so much — and why it can sound cold.',
    wh3h='The three mistakes', wh3b=
        'Never <em>was been</em> &mdash; it is either <em>was</em> or <em>has been</em>. '
        'Agree with the new subject: <em>the bricks <strong>were</strong> made</em>. '
        'And use the participle, not the past: <em>was <strong>written</strong></em>, '
        'not <em>was wrote</em>.',
    wh3n='Every one of these comes from forgetting that <em>be</em> is the verb doing the work.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Read the voice',
    q1why='<strong>The new Lego model was released last Tuesday.</strong> <em>Was</em> '
          '+ past participle, and the model is on the receiving end. The others all '
          'have a subject doing the action.',
    q2why='<strong>Lego sets are bought by millions of children every year.</strong> '
          'The object becomes the subject, <em>buy</em> becomes <em>are bought</em> in '
          'the same present tense, and the old subject takes <em>by</em>.',
    q3why='<strong>A team in Denmark.</strong> The agent is whoever performs the action, '
          'and it is the phrase after <em>by</em> &mdash; not the grammatical subject, '
          'which is what receives it.',
    q4why='<strong>The Lego bricks were sorted by colour before assembly.</strong> '
          'Plural subject, so <em>were</em>; and <em>sorted</em> is the participle. Note '
          'that <em>by colour</em> here is a method, not an agent.',
    q5why='<strong>Because the founder&rsquo;s identity is less important than the '
          'company&rsquo;s history.</strong> The passive is a choice about focus. It is '
          'not more polite, not always more formal, and not a way of hiding anything.',
    q6why='<strong>New Lego themes have been introduced every year for decades.</strong> '
          'Present perfect passive is <em>have / has</em> + <em>been</em> + past '
          'participle. Drop <em>been</em> and it is active; drop <em>have</em> and it '
          'is a simple past.',
    q7why='<strong>Both <em>was</em> and <em>been</em> are used together.</strong> It is '
          'either <em>was released</em> or <em>has been released</em>. <em>Was been</em> '
          'is the single commonest passive error in English.',

    fibEyebrow='Activity 2 · The exact form', fibTitle='Put the verb into the passive',
    fibHint='The verb and the tense are both given. Contractions are accepted.',
    g1why='<strong>Has been assembled.</strong> Present perfect passive: <em>has</em> + '
          '<em>been</em> + participle. One set, so <em>has</em>.',
    g2why='<strong>Are manufactured.</strong> Present simple passive, and the subject is '
          '75 billion elements &mdash; plural, so <em>are</em>.',
    g3why='<strong>Are written.</strong> <em>Instructions</em> is plural, and the '
          'participle of <em>write</em> is <em>written</em>, never <em>wrote</em>.',
    g4why='<strong>Was patented.</strong> Simple past passive, one design, so '
          '<em>was</em>. The patent office is the agent and nobody needs it named.',
    g5why='<strong>Was launched.</strong> Simple past passive inside a <em>before</em> '
          'clause &mdash; the clause takes the tense of the sentence around it.',
    g6why='<strong>Be turned into.</strong> After a modal, <em>be</em> stays bare: '
          '<em>might be turned into</em>. <em>Might been</em> and <em>might to be</em> '
          'are both wrong.',

    matchEyebrow='Activity 3 · The transformation', matchTitle='Match the active to its passive',
    matchHint='Click an active sentence, then click its passive.',
    matchWhy='Read each pair backwards to check it: the passive subject should be the '
             'active object, the tense should be identical, and the phrase after '
             '<em>by</em> should be the active subject. If any of the three does not '
             'line up, the transformation has gone wrong somewhere.',

    ordEyebrow='Activity 4 · Sentence building', ordTitle='Build the passive sentence',
    ordHint='Click a chunk to place it, click a placed chunk to take it back.',
    o1why='<strong>Lego City has been sold in over 50 countries.</strong> Present '
          'perfect passive: <em>has</em>, then <em>been</em>, then the participle, in '
          'that order and no other.',
    o2why='<strong>The instruction booklet was translated into 15 languages.</strong> '
          'Simple past passive, singular subject, and no agent &mdash; nobody needs to '
          'know which translators.',

    actTitle='Write the museum label', actUse='Use at least four:',
    actSpeakBrief='One of you is a museum guide, the other a visitor who keeps asking '
                  '&ldquo;but who actually did it?&rdquo;. Three minutes each, then '
                  'swap.',
    actSpeak1='Describe how something in the room was made, without saying who made it.',
    actSpeak2='Your partner asks who is responsible. Answer twice: once naming the agent, once leaving it out.',
    actSpeak3='Explain a rule at your school or workplace using the passive three times.',
    actSpeak4='Tell the story of an object you own — where it was made, when it was given to you, what has been done to it since.',
    actWriteKind='Writing · 120–150 words',
    actWriteBrief='Write the label a museum would put beside a famous object. Say when '
                  'it was made, what it was made from, how it has been used and where '
                  'it is kept now. Name an agent only where the reader would actually '
                  'want to know.',
    actPlaceholder='This model was built in…',

    resPerfect='Full marks. You can build the passive and, more importantly, say when it earns its place.',
    resStrong='Strong. Check the perfect forms once more — <em>been</em> is where the last mark usually goes.',
    resMid='Good base. Go back to the second slide: <em>be</em> carries the tense, and the participle never moves.',
    resLow='Read the three opening slides again. Three steps turn any active sentence into a passive one.',
)

T['de'] = dict(
    coverTitle='Aktiv &amp; <em>Passiv</em>',
    coverSub='Wer es getan hat, wem es widerfuhr — und wann das Englische es lieber nicht sagt',
    chipLevel='B1 · Mittelstufe', chipFocus='Das Passiv',
    chipCount='19 Folien',

    voEyebrow='Vor den Fragen', voTitle='Zwei Diathesen, ein Vorgang',
    vo1h='Aktiv: das Subjekt handelt', vo1b=
        'Subjekt, Verb, Objekt. <em>Lego <strong>releases</strong> new sets every '
        'year.</em> Das Subjekt tut das Herausbringen, und so baut das Englische einen '
        'Satz normalerweise.',
    vo1n='Direkt, kurz und die richtige Voreinstellung. Das Passiv ist die markierte Wahl.',
    vo2h='Passiv: das Subjekt empfängt', vo2b=
        '<strong>Be</strong> + Partizip II. <em>New sets <strong>are released</strong> '
        'every year.</em> Das Subjekt steht auf der Empfängerseite, und der Urheber '
        'kann mit <em>by</em> genannt oder ganz weggelassen werden.',
    vo2n='Derselbe Vorgang, ein anderes Wort im Scheinwerfer.',
    vo3h='Drei Schritte von einem zum anderen', vo3b=
        'Das Objekt wird Subjekt; das Verb wird <em>be</em> + Partizip II <strong>in '
        'der ursprünglichen Zeitform</strong>; das alte Subjekt wird <em>by</em> + '
        'Urheber, und dieser Teil ist optional.',
    vo3n='<em>Ole Kirk Christiansen founded Lego</em> &rarr; <em>Lego was founded by Ole Kirk Christiansen</em>.',

    tnEyebrow='Der Mechanismus', tnTitle='<em>Be</em> trägt immer die Zeitform',
    tn1h='Die einfachen Zeiten', tn1b=
        'Präsens: <em>Lego makes bricks</em> &rarr; <em>bricks <strong>are '
        'made</strong></em>. Vergangenheit: <em>they built a castle</em> &rarr; <em>a '
        'castle <strong>was built</strong></em>. Nur <em>be</em> bewegt sich; das '
        'Partizip ändert sich nie.',
    tn1n='<em>Is / are</em> für die Gegenwart, <em>was / were</em> für die Vergangenheit.',
    tn2h='Die Perfektformen', tn2b=
        '<em>She has tested the set</em> &rarr; <em>the set <strong>has been '
        'tested</strong></em>. <em>He had launched it</em> &rarr; <em>it <strong>had '
        'been launched</strong></em>. Das Perfekt behält sein Hilfsverb und ergänzt '
        '<em>been</em>.',
    tn2n='<em>Has been</em>, <em>had been</em> — zwei Wörter, und beide werden gebraucht.',
    tn3h='Modalverben und der Infinitiv', tn3b=
        'Nach einem Modalverb bleibt <em>be</em> nackt: <em>you can assemble it</em> '
        '&rarr; <em>it <strong>can be assembled</strong></em>. Der Passivinfinitiv ist '
        '<em>to be</em> + Partizip: <em>designs that might <strong>be turned '
        'into</strong> sets</em>.',
    tn3n='Ein Modalverb nimmt nie <em>been</em>. <em>Can been assembled</em> ist kein Englisch.',

    whEyebrow='Wozu das Ganze', whTitle='Wann das Passiv der bessere Satz ist',
    wh1h='Wenn niemand weiß, wer', wh1b=
        '<em>The brick <strong>was dropped</strong>.</em> Ist der Urheber unbekannt, '
        'offensichtlich oder unwichtig, zwingt das Aktiv dazu, ein Subjekt zu erfinden. '
        'Das Passiv erlaubt, es wegzulassen.',
    wh1n='Das ist kein Ausweichen. Oft ist es schlicht der einzige ehrliche Satz.',
    wh2h='Wenn das Ergebnis die Nachricht ist', wh2b=
        'Berichte, Etiketten, Anleitungen und Wissenschaft stellen die Sache voran: '
        '<em>the design <strong>was patented</strong> in 1958</em>. Das Patentamt ist '
        'nicht das Thema des Satzes.',
    wh2n='Darum benutzt formelles Schreiben es so oft — und darum klingt es leicht kalt.',
    wh3h='Die drei Fehler', wh3b=
        'Nie <em>was been</em> — es heißt entweder <em>was</em> oder <em>has been</em>. '
        'Kongruenz mit dem neuen Subjekt: <em>the bricks <strong>were</strong> made</em>. '
        'Und das Partizip, nicht das Präteritum: <em>was <strong>written</strong></em>, '
        'nicht <em>was wrote</em>.',
    wh3n='Alle drei entstehen daraus, dass man vergisst: <em>be</em> ist hier das arbeitende Verb.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Erkenne die Diathese',
    q1why='<strong>The new Lego model was released last Tuesday.</strong> <em>Was</em> + '
          'Partizip, und das Modell steht auf der Empfängerseite. Bei den anderen tut '
          'ein Subjekt die Handlung.',
    q2why='<strong>Lego sets are bought by millions of children every year.</strong> Das '
          'Objekt wird Subjekt, <em>buy</em> wird <em>are bought</em> in derselben '
          'Gegenwart, und das alte Subjekt bekommt <em>by</em>.',
    q3why='<strong>A team in Denmark.</strong> Der Urheber ist, wer die Handlung ausführt, '
          'und das ist die Phrase nach <em>by</em> — nicht das grammatische Subjekt, das '
          'sie empfängt.',
    q4why='<strong>The Lego bricks were sorted by colour before assembly.</strong> '
          'Pluralsubjekt, also <em>were</em>; <em>sorted</em> ist das Partizip. <em>By '
          'colour</em> ist hier eine Methode, kein Urheber.',
    q5why='<strong>Because the founder&rsquo;s identity is less important than the '
          'company&rsquo;s history.</strong> Das Passiv ist eine Entscheidung über den '
          'Fokus. Es ist nicht höflicher, nicht immer förmlicher und kein Mittel zum '
          'Verbergen.',
    q6why='<strong>New Lego themes have been introduced every year for decades.</strong> '
          'Present Perfect Passiv heißt <em>have / has</em> + <em>been</em> + Partizip. '
          'Ohne <em>been</em> ist es Aktiv, ohne <em>have</em> ein Simple Past.',
    q7why='<strong>Beide, <em>was</em> und <em>been</em>, stehen zusammen.</strong> Es '
          'heißt entweder <em>was released</em> oder <em>has been released</em>. <em>Was '
          'been</em> ist der häufigste Passivfehler im Englischen.',

    fibEyebrow='Aufgabe 2 · Die genaue Form', fibTitle='Setze das Verb ins Passiv',
    fibHint='Verb und Zeitform sind vorgegeben. Kurzformen werden akzeptiert.',
    g1why='<strong>Has been assembled.</strong> Present Perfect Passiv: <em>has</em> + '
          '<em>been</em> + Partizip. Ein Set, also <em>has</em>.',
    g2why='<strong>Are manufactured.</strong> Present Simple Passiv, und das Subjekt sind '
          '75 Milliarden Elemente — Plural, also <em>are</em>.',
    g3why='<strong>Are written.</strong> <em>Instructions</em> ist Plural, und das '
          'Partizip von <em>write</em> ist <em>written</em>, nie <em>wrote</em>.',
    g4why='<strong>Was patented.</strong> Simple Past Passiv, ein Design, also <em>was</em>. '
          'Das Patentamt ist der Urheber, und niemand muss ihn nennen.',
    g5why='<strong>Was launched.</strong> Simple Past Passiv in einem <em>before</em>-Satz '
          '— der Nebensatz nimmt die Zeit des Satzes um ihn herum.',
    g6why='<strong>Be turned into.</strong> Nach einem Modalverb bleibt <em>be</em> nackt: '
          '<em>might be turned into</em>. <em>Might been</em> und <em>might to be</em> '
          'sind beide falsch.',

    matchEyebrow='Aufgabe 3 · Die Umformung', matchTitle='Ordne dem Aktivsatz sein Passiv zu',
    matchHint='Klicke einen Aktivsatz an, dann sein Passiv.',
    matchWhy='Prüfe jedes Paar rückwärts: Das Passivsubjekt sollte das Aktivobjekt sein, '
             'die Zeitform identisch, und die Phrase nach <em>by</em> das Aktivsubjekt. '
             'Passt eines davon nicht, ist bei der Umformung etwas schiefgegangen.',

    ordEyebrow='Aufgabe 4 · Satzbau', ordTitle='Bau den Passivsatz',
    ordHint='Klicke einen Baustein an, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',
    o1why='<strong>Lego City has been sold in over 50 countries.</strong> Present Perfect '
          'Passiv: <em>has</em>, dann <em>been</em>, dann das Partizip — in dieser '
          'Reihenfolge und in keiner anderen.',
    o2why='<strong>The instruction booklet was translated into 15 languages.</strong> '
          'Simple Past Passiv, Singularsubjekt, kein Urheber — niemand muss wissen, '
          'welche Übersetzer.',

    actTitle='Schreib das Museumsschild', actUse='Benutze mindestens vier:',
    actSpeakBrief='Einer ist Museumsführer, die andere eine Besucherin, die immer wieder '
                  'fragt: „Aber wer hat es denn gemacht?“ Je drei Minuten, dann tauschen.',
    actSpeak1='Beschreibe, wie etwas im Raum hergestellt wurde, ohne zu sagen, wer es gemacht hat.',
    actSpeak2='Dein Partner fragt, wer verantwortlich ist. Antworte zweimal: einmal mit Urheber, einmal ohne.',
    actSpeak3='Erklär eine Regel an deiner Schule oder Arbeit und benutze dabei dreimal das Passiv.',
    actSpeak4='Erzähl die Geschichte eines Gegenstands: wo er gemacht, wann er dir geschenkt wurde und was seitdem damit passiert ist.',
    actWriteKind='Schreiben · 120–150 Wörter',
    actWriteBrief='Schreibe das Schild, das ein Museum neben einen berühmten Gegenstand '
                  'stellen würde. Sag, wann er gemacht wurde, woraus, wie er benutzt '
                  'wurde und wo er heute aufbewahrt wird. Nenne einen Urheber nur da, wo '
                  'die Leserin es wirklich wissen will.',
    actPlaceholder='This model was built in…',

    resPerfect='Volle Punktzahl. Du kannst das Passiv bilden und — wichtiger — sagen, wann es sich lohnt.',
    resStrong='Stark. Sieh dir die Perfektformen noch einmal an; bei <em>been</em> fehlt meist der letzte Punkt.',
    resMid='Gute Grundlage. Zurück zur zweiten Folie: <em>be</em> trägt die Zeit, das Partizip bewegt sich nie.',
    resLow='Lies die drei Einstiegsfolien noch einmal. Drei Schritte machen aus jedem Aktivsatz einen Passivsatz.',
)

T['es'] = dict(
    coverTitle='Activa y <em>pasiva</em>',
    coverSub='Quién lo hizo, a quién le pasó y cuándo el inglés prefiere no decirlo',
    chipLevel='B1 · Intermedio', chipFocus='La voz pasiva',
    chipCount='19 diapositivas',

    voEyebrow='Antes de las preguntas', voTitle='Dos voces, un mismo suceso',
    vo1h='Activa: el sujeto actúa', vo1b=
        'Sujeto, verbo, objeto. <em>Lego <strong>releases</strong> new sets every '
        'year.</em> El sujeto hace el lanzamiento, y así arma el inglés una frase '
        'normalmente.',
    vo1n='Directa, breve y la opción por defecto. La pasiva es la elección marcada.',
    vo2h='Pasiva: el sujeto recibe', vo2b=
        '<strong>Be</strong> + participio. <em>New sets <strong>are released</strong> '
        'every year.</em> El sujeto está en el lado receptor, y el agente puede '
        'nombrarse con <em>by</em> o quedarse fuera.',
    vo2n='El mismo suceso, otra palabra bajo el foco.',
    vo3h='Tres pasos para pasar de una a otra', vo3b=
        'El objeto pasa a sujeto; el verbo pasa a <em>be</em> + participio <strong>en el '
        'tiempo original</strong>; el sujeto antiguo pasa a <em>by</em> + agente, y esa '
        'parte es opcional.',
    vo3n='<em>Ole Kirk Christiansen founded Lego</em> &rarr; <em>Lego was founded by Ole Kirk Christiansen</em>.',

    tnEyebrow='El mecanismo', tnTitle='<em>Be</em> lleva siempre el tiempo verbal',
    tn1h='Los tiempos simples', tn1b=
        'Presente: <em>Lego makes bricks</em> &rarr; <em>bricks <strong>are '
        'made</strong></em>. Pasado: <em>they built a castle</em> &rarr; <em>a castle '
        '<strong>was built</strong></em>. Solo se mueve <em>be</em>; el participio no '
        'cambia nunca.',
    tn1n='<em>Is / are</em> para el presente, <em>was / were</em> para el pasado.',
    tn2h='Los tiempos perfectos', tn2b=
        '<em>She has tested the set</em> &rarr; <em>the set <strong>has been '
        'tested</strong></em>. <em>He had launched it</em> &rarr; <em>it <strong>had '
        'been launched</strong></em>. El perfecto conserva su auxiliar y añade '
        '<em>been</em>.',
    tn2n='<em>Has been</em>, <em>had been</em>: dos palabras, y hacen falta las dos.',
    tn3h='Modales e infinitivo', tn3b=
        'Tras un modal, <em>be</em> va desnudo: <em>you can assemble it</em> &rarr; '
        '<em>it <strong>can be assembled</strong></em>. El infinitivo pasivo es <em>to '
        'be</em> + participio: <em>designs that might <strong>be turned into</strong> '
        'sets</em>.',
    tn3n='Un modal nunca lleva <em>been</em>. <em>Can been assembled</em> no es inglés.',

    whEyebrow='Para qué', whTitle='Cuándo la pasiva es la mejor frase',
    wh1h='Cuando nadie sabe quién', wh1b=
        '<em>The brick <strong>was dropped</strong>.</em> Si el agente es desconocido, '
        'obvio o irrelevante, la activa te obliga a inventar un sujeto. La pasiva '
        'permite dejarlo fuera.',
    wh1n='No es evasión. A menudo es la única frase honesta disponible.',
    wh2h='Cuando la noticia es el resultado', wh2b=
        'Informes, etiquetas, instrucciones y ciencia ponen la cosa por delante: <em>the '
        'design <strong>was patented</strong> in 1958</em>. La oficina de patentes no es '
        'de lo que va la frase.',
    wh2n='Por eso la escritura formal la usa tanto — y por eso puede sonar fría.',
    wh3h='Los tres errores', wh3b=
        'Nunca <em>was been</em>: es <em>was</em> o <em>has been</em>. Concuerda con el '
        'nuevo sujeto: <em>the bricks <strong>were</strong> made</em>. Y usa el '
        'participio, no el pasado: <em>was <strong>written</strong></em>, no <em>was '
        'wrote</em>.',
    wh3n='Los tres salen de olvidar que aquí el verbo que trabaja es <em>be</em>.',

    mcEyebrow='Actividad 1 · Opción múltiple', mcTitle='Reconoce la voz',
    q1why='<strong>The new Lego model was released last Tuesday.</strong> <em>Was</em> + '
          'participio, y el modelo está en el lado receptor. En las demás hay un sujeto '
          'que hace la acción.',
    q2why='<strong>Lego sets are bought by millions of children every year.</strong> El '
          'objeto pasa a sujeto, <em>buy</em> pasa a <em>are bought</em> en el mismo '
          'presente, y el sujeto antiguo lleva <em>by</em>.',
    q3why='<strong>A team in Denmark.</strong> El agente es quien ejecuta la acción, y es '
          'la frase que sigue a <em>by</em> — no el sujeto gramatical, que es quien la '
          'recibe.',
    q4why='<strong>The Lego bricks were sorted by colour before assembly.</strong> Sujeto '
          'plural, así que <em>were</em>; y <em>sorted</em> es el participio. Aquí <em>by '
          'colour</em> es un método, no un agente.',
    q5why='<strong>Because the founder&rsquo;s identity is less important than the '
          'company&rsquo;s history.</strong> La pasiva es una decisión sobre el foco. No '
          'es más educada, no siempre es más formal y no sirve para esconder nada.',
    q6why='<strong>New Lego themes have been introduced every year for decades.</strong> '
          'El presente perfecto pasivo es <em>have / has</em> + <em>been</em> + '
          'participio. Sin <em>been</em> es activa; sin <em>have</em> es pasado simple.',
    q7why='<strong>Aparecen juntos <em>was</em> y <em>been</em>.</strong> Es <em>was '
          'released</em> o <em>has been released</em>. <em>Was been</em> es el error de '
          'pasiva más común del inglés.',

    fibEyebrow='Actividad 2 · La forma exacta', fibTitle='Pon el verbo en pasiva',
    fibHint='Se dan el verbo y el tiempo. Se aceptan contracciones.',
    g1why='<strong>Has been assembled.</strong> Presente perfecto pasivo: <em>has</em> + '
          '<em>been</em> + participio. Un set, así que <em>has</em>.',
    g2why='<strong>Are manufactured.</strong> Presente simple pasivo, y el sujeto son 75 '
          'mil millones de piezas: plural, así que <em>are</em>.',
    g3why='<strong>Are written.</strong> <em>Instructions</em> es plural, y el participio '
          'de <em>write</em> es <em>written</em>, nunca <em>wrote</em>.',
    g4why='<strong>Was patented.</strong> Pasado simple pasivo, un diseño, así que '
          '<em>was</em>. La oficina de patentes es el agente y no hace falta nombrarla.',
    g5why='<strong>Was launched.</strong> Pasado simple pasivo dentro de una oración con '
          '<em>before</em>: la subordinada toma el tiempo de la frase que la rodea.',
    g6why='<strong>Be turned into.</strong> Tras un modal, <em>be</em> va desnudo: '
          '<em>might be turned into</em>. <em>Might been</em> y <em>might to be</em> son '
          'ambos incorrectos.',

    matchEyebrow='Actividad 3 · La transformación', matchTitle='Relaciona la activa con su pasiva',
    matchHint='Haz clic en una frase activa y luego en su pasiva.',
    matchWhy='Comprueba cada pareja al revés: el sujeto de la pasiva debe ser el objeto '
             'de la activa, el tiempo debe ser idéntico y lo que sigue a <em>by</em> debe '
             'ser el sujeto de la activa. Si alguna de las tres no encaja, la '
             'transformación ha fallado en algún punto.',

    ordEyebrow='Actividad 4 · Construcción de frases', ordTitle='Construye la frase pasiva',
    ordHint='Haz clic en un fragmento para colocarlo; haz clic en uno colocado para retirarlo.',
    o1why='<strong>Lego City has been sold in over 50 countries.</strong> Presente '
          'perfecto pasivo: <em>has</em>, luego <em>been</em>, luego el participio, en '
          'ese orden y en ningún otro.',
    o2why='<strong>The instruction booklet was translated into 15 languages.</strong> '
          'Pasado simple pasivo, sujeto singular y sin agente: nadie necesita saber qué '
          'traductores.',

    actTitle='Escribe la cartela del museo', actUse='Usa al menos cuatro:',
    actSpeakBrief='Uno es guía de museo y el otro un visitante que insiste en preguntar '
                  '«¿pero quién lo hizo de verdad?». Tres minutos cada uno, luego '
                  'cambiad.',
    actSpeak1='Describe cómo se fabricó algo de la sala, sin decir quién lo hizo.',
    actSpeak2='Tu compañero pregunta quién es responsable. Responde dos veces: una nombrando al agente y otra sin él.',
    actSpeak3='Explica una norma de tu centro o tu trabajo usando la pasiva tres veces.',
    actSpeak4='Cuenta la historia de un objeto tuyo: dónde se hizo, cuándo te lo dieron y qué se ha hecho con él desde entonces.',
    actWriteKind='Escritura · 120–150 palabras',
    actWriteBrief='Escribe la cartela que un museo pondría junto a un objeto famoso. Di '
                  'cuándo se hizo, de qué está hecho, cómo se ha usado y dónde se guarda '
                  'ahora. Nombra al agente solo donde el lector querría saberlo de '
                  'verdad.',
    actPlaceholder='This model was built in…',

    resPerfect='Puntuación perfecta. Sabes formar la pasiva y, más importante, cuándo merece la pena.',
    resStrong='Muy bien. Repasa una vez más los tiempos perfectos: en <em>been</em> suele irse el último punto.',
    resMid='Buena base. Vuelve a la segunda diapositiva: <em>be</em> lleva el tiempo y el participio no se mueve.',
    resLow='Relee las tres diapositivas iniciales. Tres pasos convierten cualquier frase activa en pasiva.',
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
