# -*- coding: utf-8 -*-
"""Interface strings for Holding the Line (C1) - English, German, Spanish.

The scope boundary is HOUSE-STYLE §8 and it matters more than usual on this
deck, because almost everything a learner reads here is a line they are
expected to SAY. So:

  * the chrome translates - cover, eyebrows, slide titles, hints, the teaching
    cards that explain a rule, the situation lines above each question, the
    activation briefs, the result bands;
  * every line under test stays English - stems, options, gap sentences, the
    word banks, the sort items, the order chunks, the match terms and the
    phrases in the phrase-bank round. Translating those removes the exercise.

Two cards carry no head_key at all: the FORM cards on the passive and on
ONCE + PRESENT SIMPLE. Their heading IS the pattern being taught, so it stays
in English in every language - a German heading over an English pattern is
the half-finished screen §8 exists to prevent. Their notes translate, because
a note explains rather than cites.

Where a German or Spanish line quotes what the manager says - "Your time
efficiency is concerning", "Why isn't the lead deliverable ready?" - the
quotation stays English. It is the thing the learner has to answer, not an
instruction about the task.

resNext and actSpeakKind are declared here rather than lifted from CHROME:
CHROME carries a generic hand-off line and 'Discussion - in pairs', and this
deck says something else in both slots. A key that is lifted AND emitted
differently by the builder makes the slide change when a learner switches
language and back, which is the divergence recorded in i18n_escalating.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'btnFull',
        'scoreLabel', 'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer',
        'btnCopy', 'btnCopied', 'wordCount', 'actEyebrow', 'actSpeakWord',
        'actWriteWord']

# Template chrome that no lesson declares but check-lesson.js's I18N gate
# still resolves. Raw JS literals, emitted after the body.
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no permite este final'",
           'glossHide': "'Ocultar'",
           'glossShow': "'Traducir'",
           'ledClues': "'Pistas'",
           'ledDp': "'DP'",
           'ledTime': "'Tiempo'"},
    'ru': {'branchLocked': "'Ваш журнал не допускает такой финал'",
           'glossHide': "'Скрыть'",
           'glossShow': "'Перевести'",
           'ledClues': "'Подсказки'",
           'ledDp': "'DP'",
           'ledTime': "'Время'"},
}

T = {}

T['en'] = dict(
    coverTitle='Holding the <em>Line</em>',
    coverSub='What to say when work nobody gave you becomes work you are being '
             'blamed for',
    chipLevel='C1 &middot; Workplace pressure',
    chipFocus='Scope, facts and the ask',
    chipCount='COUNT slides',

    caseEyebrow='The situation',
    caseTitle='Three tasks given, one never allocated',
    caseH1='What you did',
    case1='You completed the three junior tasks you were assigned, inside the '
          'time allowance set for them.',
    caseN1='Not in dispute. Say it once, with the dates.',
    caseH2='What was never issued',
    case2='The lead tasks were not allocated to you, and no authority, sign-off '
          'or system access came with them.',
    caseN2='A task you were never given is not a task you failed.',
    caseH3='What is being said',
    case3='Your time efficiency is called concerning, and a fourth task arrives '
          'that nobody has put in writing.',
    caseN3='Two separate claims. Answer them separately.',

    passEyebrow='The first move',
    passTitle='Name the decision, not the person',
    passN1='No agent. Nobody in the room is named.',
    passH2='Why it is the safer sentence',
    pass2='&ldquo;You never gave me authority&rdquo; is a charge against your '
          'manager. The passive states the same fact and charges nobody.',
    passN2='A fact survives being forwarded to him. An accusation does not.',

    termsEyebrow='The vocabulary',
    termsTitle='The words for what you own',
    termsTitle2='The words for what you can do',
    termsHint='Click a term, then the line that defines it.',

    limitEyebrow='Say the limit',
    limitTitle='Complete the line',
    limitHint='One word per gap; each is used once across both screens.',
    bankLabel='Word bank:',

    roleEyebrow='Your remit',
    roleTitle='Which sentence would you send?',
    roleCtx1='Your manager, in front of the team: &ldquo;Why isn&rsquo;t the '
             'lead deliverable ready?&rdquo;',
    roleCtx2='He refers to a task you have never seen in the system.',
    roleCtx3='He asks you to account for the week.',

    movesEyebrow='Under criticism',
    movesTitle='Three moves that lower the temperature',
    movesH1='Ask for the instance',
    moves1='&ldquo;Could you give me a specific example?&rdquo; A judgement with '
           'no instance behind it cannot be answered &mdash; and does not have '
           'to be accepted.',
    movesN1='You are not arguing. You are asking what the claim is about.',
    movesH2='Stick to the facts',
    moves2='&ldquo;Can we stick to the facts, please?&rdquo; Then give the dates, '
           'the tickets, the hours &mdash; things a third person could check.',
    movesN2='Say it once. Twice and it is a slogan.',
    movesH3='Move the conversation',
    moves3='&ldquo;I would like to discuss the limits of my role at a convenient '
           'time.&rdquo; Ask for a length and a purpose.',
    movesN3='A corridor is not a room. Fifteen minutes and a door.',

    sortEyebrow='Before you say it',
    sortTitle='Fact, or verdict?',
    sortHint='Click a line, then the box it belongs in.',
    sortBin1='A fact anyone could check',
    sortBin2='A verdict about a person',

    critEyebrow='The criticism',
    critTitle='Answer it without agreeing to it',
    critCtx1='&ldquo;Your time efficiency is concerning.&rdquo;',
    critCtx2='The same conversation, still at your desk, still audible.',
    critCtx3='He repeats the word &ldquo;concerning&rdquo;.',

    ordEyebrow='Say it cleanly',
    ordTitle='Put the request in order',
    ordHint='Click the parts in order.',

    condEyebrow='The boundary',
    condTitle='Yes &mdash; once two things happen',
    condN1='ONCE, WHEN and AS SOON AS take the present for future time.',
    condH2='Name both conditions',
    cond2='Ownership, and access. Work with neither is work you can be blamed '
          'for and cannot actually do.',
    condN2='&ldquo;Formally allocated&rdquo; is what makes it a record.',

    askEyebrow='The ask',
    askTitle='Ask for the two things',
    askHint='One word per gap; each is used once across both screens.',
    askHint2='One word per gap &mdash; and the last line takes two.',

    corrEyebrow='The corridor',
    corrTitle='A fourth task, on the way to lunch',
    corrCtx='He tells you about it walking past your desk, and keeps walking.',

    funcEyebrow='The phrase bank',
    funcTitle='What each line actually does',
    funcHint='Click a line, then the job it does in the room.',

    resNext='Now run the meeting &rarr;',
    resPerfect='Full marks. You can hear the difference &mdash; now say it out '
               'loud, which is harder.',
    resStrong='Strong. Look again at the misses: most of them are a verdict '
              'standing where a date should be.',
    resMid='A workable base. Re-read the three rule slides before you speak.',
    resLow='Work through the three moves again. Nearly every miss is a '
           'judgement offered instead of a fact.',

    actTitle='Now run the meeting',
    actUse='Use at least four:',
    actSpeakKind='Speaking',
    actSpeakBrief='In pairs. Three minutes each, then swap roles and run it '
                  'again.',
    actSpeak1='You are the junior. He opens: &ldquo;Your time efficiency is '
              'concerning.&rdquo;',
    actSpeak2='Swap. A fourth task arrives in the corridor. Get it allocated or '
              'dropped.',
    actSpeak3='Same meeting, HR in the room. What changes, and what must not?',
    actSpeak4='The other side: when is a manager right to go outside your '
              'remit?',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='The email that asks for your role to be clarified: three '
                  'dated facts, one concession, one specific ask. Nothing about '
                  'character.',
    actPlaceholder='Dear Ana, following this morning&rsquo;s conversation, I '
                   'would like to set out what was allocated to me and '
                   'when&hellip;',
)

T['de'] = dict(
    coverTitle='Die <em>Linie</em> halten',
    coverSub='Was Sie sagen, wenn Arbeit, die Ihnen nie zugewiesen wurde, zu '
             'Arbeit wird, f&uuml;r die Sie kritisiert werden',
    chipLevel='C1 &middot; Druck am Arbeitsplatz',
    chipFocus='Zust&auml;ndigkeit, Fakten und die Bitte',
    chipCount='COUNT Folien',

    caseEyebrow='Die Ausgangslage',
    caseTitle='Drei Aufgaben erhalten, eine nie zugewiesen',
    caseH1='Was Sie getan haben',
    case1='Sie haben die drei Junior-Aufgaben, die Ihnen zugewiesen wurden, '
          'innerhalb der daf&uuml;r vorgesehenen Zeit erledigt.',
    caseN1='Unstrittig. Einmal sagen &mdash; mit Datum.',
    caseH2='Was nie erteilt wurde',
    case2='Die Lead-Aufgaben wurden Ihnen nicht zugewiesen, und weder Befugnis '
          'noch Freigabe noch Systemzugang kamen dazu.',
    caseN2='Eine Aufgabe, die Sie nie bekommen haben, ist keine Aufgabe, an der '
           'Sie gescheitert sind.',
    caseH3='Was behauptet wird',
    case3='Ihre Zeiteffizienz sei bedenklich &mdash; und eine vierte Aufgabe '
          'kommt, die niemand schriftlich festgehalten hat.',
    caseN3='Zwei getrennte Vorw&uuml;rfe. Getrennt beantworten.',

    passEyebrow='Der erste Schritt',
    passTitle='Die Entscheidung benennen, nicht die Person',
    passN1='Kein Handelnder. Niemand im Raum wird benannt.',
    passH2='Warum dieser Satz der sicherere ist',
    pass2='&bdquo;You never gave me authority&ldquo; ist ein Vorwurf an Ihre '
          'F&uuml;hrungskraft. Das Passiv nennt dieselbe Tatsache und '
          'beschuldigt niemanden.',
    passN2='Eine Tatsache &uuml;bersteht es, weitergeleitet zu werden. Ein '
           'Vorwurf nicht.',

    termsEyebrow='Der Wortschatz',
    termsTitle='Die W&ouml;rter f&uuml;r das, was Ihnen geh&ouml;rt',
    termsTitle2='Die W&ouml;rter f&uuml;r das, was Sie tun d&uuml;rfen',
    termsHint='Klicken Sie auf einen Begriff und dann auf die passende '
              'Definition.',

    limitEyebrow='Die Grenze benennen',
    limitTitle='Vervollst&auml;ndigen Sie den Satz',
    limitHint='Ein Wort pro L&uuml;cke; jedes wird auf den beiden Bildschirmen '
              'genau einmal gebraucht.',
    bankLabel='Wortliste:',

    roleEyebrow='Ihr Aufgabenbereich',
    roleTitle='Welchen Satz w&uuml;rden Sie abschicken?',
    roleCtx1='Ihre F&uuml;hrungskraft, vor dem Team: &bdquo;Why isn&rsquo;t the '
             'lead deliverable ready?&ldquo;',
    roleCtx2='Er spricht von einer Aufgabe, die Sie nie im System gesehen haben.',
    roleCtx3='Er verlangt Rechenschaft &uuml;ber die Woche.',

    movesEyebrow='Unter Kritik',
    movesTitle='Drei Schritte, die die Temperatur senken',
    movesH1='Nach dem konkreten Fall fragen',
    moves1='&bdquo;Could you give me a specific example?&ldquo; Ein Urteil ohne '
           'Beispiel dahinter l&auml;sst sich nicht beantworten &mdash; und muss '
           'nicht akzeptiert werden.',
    movesN1='Sie streiten nicht. Sie fragen, worum es konkret geht.',
    movesH2='Bei den Fakten bleiben',
    moves2='&bdquo;Can we stick to the facts, please?&ldquo; Dann Daten, Tickets, '
           'Stunden &mdash; Dinge, die ein Dritter pr&uuml;fen kann.',
    movesN2='Einmal sagen. Zweimal ist es eine Parole.',
    movesH3='Das Gespr&auml;ch verlegen',
    moves3='&bdquo;I would like to discuss the limits of my role at a convenient '
           'time.&ldquo; Nennen Sie Dauer und Zweck.',
    movesN3='Ein Flur ist kein Raum. F&uuml;nfzehn Minuten und eine T&uuml;r.',

    sortEyebrow='Bevor Sie es sagen',
    sortTitle='Tatsache oder Urteil?',
    sortHint='Klicken Sie auf eine Zeile und dann auf das passende Feld.',
    sortBin1='Eine &uuml;berpr&uuml;fbare Tatsache',
    sortBin2='Ein Urteil &uuml;ber eine Person',

    critEyebrow='Die Kritik',
    critTitle='Antworten, ohne zuzustimmen',
    critCtx1='&bdquo;Your time efficiency is concerning.&ldquo;',
    critCtx2='Dasselbe Gespr&auml;ch, immer noch am Schreibtisch, immer noch '
             'h&ouml;rbar.',
    critCtx3='Er wiederholt das Wort &bdquo;concerning&ldquo;.',

    ordEyebrow='Sauber formulieren',
    ordTitle='Bringen Sie die Bitte in die richtige Reihenfolge',
    ordHint='Klicken Sie die Teile der Reihe nach an.',

    condEyebrow='Die Grenze',
    condTitle='Ja &mdash; sobald zwei Dinge geschehen',
    condN1='ONCE, WHEN und AS SOON AS stehen mit Pr&auml;sens f&uuml;r die '
           'Zukunft.',
    condH2='Beide Bedingungen nennen',
    cond2='Verantwortung und Zugang. Arbeit ohne beides ist Arbeit, f&uuml;r die '
          'man Sie belangen kann und die Sie nicht erledigen k&ouml;nnen.',
    condN2='&bdquo;Formally allocated&ldquo; ist das, was daraus einen Nachweis '
           'macht.',

    askEyebrow='Die Bitte',
    askTitle='Bitten Sie um die zwei Dinge',
    askHint='Ein Wort pro L&uuml;cke; jedes wird auf den beiden Bildschirmen '
            'genau einmal gebraucht.',
    askHint2='Ein Wort pro L&uuml;cke &mdash; und die letzte Zeile nimmt zwei.',

    corrEyebrow='Der Flur',
    corrTitle='Eine vierte Aufgabe, auf dem Weg zum Essen',
    corrCtx='Er erw&auml;hnt sie im Vorbeigehen an Ihrem Schreibtisch &mdash; '
            'und geht weiter.',

    funcEyebrow='Die Formulierungen',
    funcTitle='Was jede Zeile tats&auml;chlich bewirkt',
    funcHint='Klicken Sie auf eine Zeile und dann auf ihre Funktion im '
             'Gespr&auml;ch.',

    resNext='Jetzt f&uuml;hren Sie das Gespr&auml;ch &rarr;',
    resPerfect='Volle Punktzahl. Sie h&ouml;ren den Unterschied &mdash; jetzt '
               'sprechen Sie ihn aus, das ist schwerer.',
    resStrong='Stark. Sehen Sie sich die Fehler an: Meist steht dort ein Urteil, '
              'wo ein Datum stehen m&uuml;sste.',
    resMid='Brauchbare Grundlage. Lesen Sie die drei Regelfolien noch einmal, '
           'bevor Sie sprechen.',
    resLow='Gehen Sie die drei Schritte noch einmal durch. Fast jeder Fehler ist '
           'ein Urteil anstelle einer Tatsache.',

    actTitle='Jetzt f&uuml;hren Sie das Gespr&auml;ch',
    actUse='Mindestens vier:',
    actSpeakKind='Sprechen',
    actSpeakBrief='Zu zweit. Je drei Minuten, dann Rollen tauschen und noch '
                  'einmal durchspielen.',
    actSpeak1='Sie sind die Junior-Kraft. Er beginnt: &bdquo;Your time '
              'efficiency is concerning.&ldquo;',
    actSpeak2='Tauschen. Im Flur kommt eine vierte Aufgabe. Zuweisen lassen '
              'oder streichen.',
    actSpeak3='Dasselbe Gespr&auml;ch, HR im Raum. Was &auml;ndert sich, was '
              'nicht?',
    actSpeak4='Die Gegenseite: Wann darf eine F&uuml;hrungskraft &uuml;ber Ihren '
              'Bereich hinausgehen?',
    actWriteKind='Schreiben &middot; 180&ndash;220 W&ouml;rter',
    actWriteBrief='Die E-Mail, die um Kl&auml;rung Ihrer Rolle bittet: drei '
                  'datierte Tatsachen, ein Zugest&auml;ndnis, eine konkrete '
                  'Bitte. Nichts &uuml;ber Charakter.',
    actPlaceholder='Dear Ana, following this morning&rsquo;s conversation, I '
                   'would like to set out what was allocated to me and '
                   'when&hellip;',
)

T['es'] = dict(
    coverTitle='Mantener la <em>l&iacute;nea</em>',
    coverSub='Qu&eacute; decir cuando el trabajo que nadie te asign&oacute; se '
             'convierte en el trabajo que te reprochan',
    chipLevel='C1 &middot; Presi&oacute;n en el trabajo',
    chipFocus='Competencias, hechos y la petici&oacute;n',
    chipCount='COUNT diapositivas',

    caseEyebrow='La situaci&oacute;n',
    caseTitle='Tres tareas asignadas, una nunca adjudicada',
    caseH1='Lo que hiciste',
    case1='Completaste las tres tareas junior que te asignaron, dentro del tiempo '
          'previsto para ellas.',
    caseN1='Eso no se discute. Dilo una vez, con las fechas.',
    caseH2='Lo que nunca se emiti&oacute;',
    case2='Las tareas principales no se te asignaron, y con ellas no lleg&oacute; '
          'ni autoridad, ni aprobaci&oacute;n, ni acceso al sistema.',
    caseN2='Una tarea que nunca te dieron no es una tarea en la que fallaste.',
    caseH3='Lo que se est&aacute; diciendo',
    case3='Dicen que tu eficiencia es preocupante, y llega una cuarta tarea que '
          'nadie ha puesto por escrito.',
    caseN3='Son dos acusaciones distintas. Resp&oacute;ndelas por separado.',

    passEyebrow='El primer movimiento',
    passTitle='Nombra la decisi&oacute;n, no a la persona',
    passN1='Sin agente. No se nombra a nadie de los presentes.',
    passH2='Por qu&eacute; es la frase m&aacute;s segura',
    pass2='&laquo;You never gave me authority&raquo; es una acusaci&oacute;n '
          'contra tu responsable. La pasiva expone el mismo hecho y no acusa a '
          'nadie.',
    passN2='Un hecho sobrevive a que se lo reenv&iacute;en a &eacute;l. Una '
           'acusaci&oacute;n no.',

    termsEyebrow='El vocabulario',
    termsTitle='Las palabras de lo que te pertenece',
    termsTitle2='Las palabras de lo que puedes hacer',
    termsHint='Haz clic en un t&eacute;rmino y luego en la l&iacute;nea que lo '
              'define.',

    limitEyebrow='Nombra el l&iacute;mite',
    limitTitle='Completa la frase',
    limitHint='Una palabra por hueco; cada una se usa una vez entre las dos '
              'pantallas.',
    bankLabel='Lista de palabras:',

    roleEyebrow='Tus competencias',
    roleTitle='&iquest;Qu&eacute; frase enviar&iacute;as?',
    roleCtx1='Tu responsable, delante del equipo: &laquo;Why isn&rsquo;t the '
             'lead deliverable ready?&raquo;',
    roleCtx2='Se refiere a una tarea que nunca has visto en el sistema.',
    roleCtx3='Te pide cuentas de la semana.',

    movesEyebrow='Bajo cr&iacute;tica',
    movesTitle='Tres movimientos que bajan la temperatura',
    movesH1='Pide el caso concreto',
    moves1='&laquo;Could you give me a specific example?&raquo; Un juicio sin un '
           'caso detr&aacute;s no se puede responder &mdash; y no hay por '
           'qu&eacute; aceptarlo.',
    movesN1='No est&aacute;s discutiendo. Est&aacute;s preguntando de qu&eacute; '
            'va la acusaci&oacute;n.',
    movesH2='Ci&ntilde;&eacute;te a los hechos',
    moves2='&laquo;Can we stick to the facts, please?&raquo; Y entonces das '
           'fechas, tickets, horas &mdash; cosas que un tercero puede comprobar.',
    movesN2='D&iacute;lo una vez. A la segunda es un eslogan.',
    movesH3='Cambia de sitio la conversaci&oacute;n',
    moves3='&laquo;I would like to discuss the limits of my role at a convenient '
           'time.&raquo; Pide una duraci&oacute;n y un objetivo.',
    movesN3='Un pasillo no es una sala. Quince minutos y una puerta.',

    sortEyebrow='Antes de decirlo',
    sortTitle='&iquest;Hecho o veredicto?',
    sortHint='Haz clic en una l&iacute;nea y luego en la caja que le '
             'corresponde.',
    sortBin1='Un hecho que cualquiera puede comprobar',
    sortBin2='Un veredicto sobre una persona',

    critEyebrow='La cr&iacute;tica',
    critTitle='Resp&oacute;ndela sin darle la raz&oacute;n',
    critCtx1='&laquo;Your time efficiency is concerning.&raquo;',
    critCtx2='La misma conversaci&oacute;n, a&uacute;n en tu mesa, a&uacute;n a '
             'o&iacute;dos de todos.',
    critCtx3='Repite la palabra &laquo;concerning&raquo;.',

    ordEyebrow='D&iacute;lo limpio',
    ordTitle='Ordena la petici&oacute;n',
    ordHint='Haz clic en las partes por orden.',

    condEyebrow='El l&iacute;mite',
    condTitle='S&iacute; &mdash; en cuanto pasen dos cosas',
    condN1='ONCE, WHEN y AS SOON AS llevan presente para hablar del futuro.',
    condH2='Nombra las dos condiciones',
    cond2='Propiedad y acceso. Un trabajo sin ninguna de las dos es un trabajo '
          'del que te pueden culpar y que no puedes hacer.',
    condN2='&laquo;Formally allocated&raquo; es lo que lo convierte en registro.',

    askEyebrow='La petici&oacute;n',
    askTitle='Pide las dos cosas',
    askHint='Una palabra por hueco; cada una se usa una vez entre las dos '
            'pantallas.',
    askHint2='Una palabra por hueco &mdash; y la &uacute;ltima l&iacute;nea '
             'lleva dos.',

    corrEyebrow='El pasillo',
    corrTitle='Una cuarta tarea, camino de comer',
    corrCtx='Te lo dice al pasar por delante de tu mesa, y sigue andando.',

    funcEyebrow='El banco de frases',
    funcTitle='Qu&eacute; hace realmente cada l&iacute;nea',
    funcHint='Haz clic en una l&iacute;nea y luego en la funci&oacute;n que '
             'cumple en la sala.',

    resNext='Ahora conduce la reuni&oacute;n &rarr;',
    resPerfect='Puntuaci&oacute;n perfecta. Oyes la diferencia &mdash; ahora '
               'd&iacute;la en voz alta, que cuesta m&aacute;s.',
    resStrong='Muy bien. Mira los fallos: casi siempre hay un veredicto donde '
              'deber&iacute;a haber una fecha.',
    resMid='Una base v&aacute;lida. Vuelve a las tres diapositivas de regla '
           'antes de hablar.',
    resLow='Repasa los tres movimientos. Casi todos los fallos son un juicio en '
           'lugar de un hecho.',

    actTitle='Ahora conduce la reuni&oacute;n',
    actUse='Usa al menos cuatro:',
    actSpeakKind='Hablar',
    actSpeakBrief='En parejas. Tres minutos cada uno, luego cambiad de papel y '
                  'repetid.',
    actSpeak1='Eres la persona junior. Abre con &laquo;Your time efficiency is '
              'concerning.&raquo;',
    actSpeak2='Cambiad. Llega una cuarta tarea en el pasillo: que te la asignen '
              'o fuera.',
    actSpeak3='La misma reuni&oacute;n, con RR. HH. &iquest;Qu&eacute; cambia y '
              'qu&eacute; no?',
    actSpeak4='La otra parte: &iquest;cu&aacute;ndo puede salirse de tus '
              'competencias?',
    actWriteKind='Escritura &middot; 180&ndash;220 palabras',
    actWriteBrief='El correo que pide aclarar tu puesto: tres hechos con fecha, '
                  'una concesi&oacute;n, una petici&oacute;n concreta. Nada '
                  'sobre el car&aacute;cter.',
    actPlaceholder='Dear Ana, following this morning&rsquo;s conversation, I '
                   'would like to set out what was allocated to me and '
                   'when&hellip;',
)

T['ru'] = dict(
    coverTitle='Держать <em>линию</em>',
    coverSub='Что сказать, когда работа, которую вам никто не поручал, '
             'становится работой, за которую вас упрекают',
    chipLevel='C1 &middot; Давление на работе',
    chipFocus='Полномочия, факты и просьба',
    chipCount='COUNT слайдов',

    caseEyebrow='Ситуация',
    caseTitle='Три задачи поручены, одна — никогда',
    caseH1='Что вы сделали',
    case1='Вы выполнили три младшие задачи, которые вам поручили, в отведённое '
          'на них время.',
    caseN1='Это не оспаривается. Скажите это один раз — с датами.',
    caseH2='Чего вам так и не выдали',
    case2='Ведущие задачи вам не поручали, и вместе с ними не пришло ни '
          'полномочий, ни права подписи, ни доступа к системе.',
    caseN2='Задача, которую вам не давали, — не та задача, которую вы провалили.',
    caseH3='Что вам говорят',
    case3='Вашу эффективность по времени называют тревожной, и приходит '
          'четвёртая задача, которую никто не зафиксировал письменно.',
    caseN3='Это два разных упрёка. Отвечайте на них по отдельности.',

    passEyebrow='Первый шаг',
    passTitle='Назовите решение, а не человека',
    passN1='Нет исполнителя. Никто в комнате не назван.',
    passH2='Почему эта фраза безопаснее',
    pass2='&laquo;You never gave me authority&raquo; — это обвинение в адрес '
          'руководителя. Пассив сообщает тот же факт и никого не обвиняет.',
    passN2='Факт переживает пересылку ему. Обвинение — нет.',

    termsEyebrow='Лексика',
    termsTitle='Слова о том, что принадлежит вам',
    termsTitle2='Слова о том, что вы вправе делать',
    termsHint='Нажмите на термин, затем на строку с определением.',

    limitEyebrow='Назовите границу',
    limitTitle='Дополните фразу',
    limitHint='По одному слову в пропуск; каждое используется один раз на двух '
              'экранах.',
    bankLabel='Банк слов:',

    roleEyebrow='Ваши полномочия',
    roleTitle='Какую фразу вы бы отправили?',
    roleCtx1='Руководитель, при всей команде: &laquo;Why isn&rsquo;t the lead '
             'deliverable ready?&raquo;',
    roleCtx2='Он говорит о задаче, которой вы никогда не видели в системе.',
    roleCtx3='Он требует отчёта за неделю.',

    movesEyebrow='Под критикой',
    movesTitle='Три шага, которые снижают градус',
    movesH1='Попросите конкретный пример',
    moves1='&laquo;Could you give me a specific example?&raquo; На оценку без '
           'примера ответить нельзя — и принимать её не обязательно.',
    movesN1='Вы не спорите. Вы спрашиваете, о чём именно речь.',
    movesH2='Держитесь фактов',
    moves2='&laquo;Can we stick to the facts, please?&raquo; Дальше — даты, '
           'тикеты, часы: то, что может проверить третий человек.',
    movesN2='Скажите один раз. На второй это уже лозунг.',
    movesH3='Перенесите разговор',
    moves3='&laquo;I would like to discuss the limits of my role at a convenient '
           'time.&raquo; Назовите длительность и цель.',
    movesN3='Коридор — не переговорная. Пятнадцать минут и дверь.',

    sortEyebrow='Прежде чем сказать',
    sortTitle='Факт или приговор?',
    sortHint='Нажмите на строку, затем на нужное поле.',
    sortBin1='Факт, который можно проверить',
    sortBin2='Приговор о человеке',

    critEyebrow='Критика',
    critTitle='Ответьте, не соглашаясь',
    critCtx1='&laquo;Your time efficiency is concerning.&raquo;',
    # Kept to one line in the 58% column the framed picture leaves: the fuller
    # "по-прежнему у вашего стола и по-прежнему слышно всем" wrapped to two and
    # put slide 14 7px over. §6 says shorten the line, never the type.
    critCtx2='Тот же разговор, у вашего стола, и всем всё слышно.',
    critCtx3='Он повторяет слово &laquo;concerning&raquo;.',

    ordEyebrow='Скажите это чисто',
    ordTitle='Соберите просьбу по порядку',
    ordHint='Нажимайте на части по порядку.',

    condEyebrow='Граница',
    condTitle='Да — как только выполнятся два условия',
    condN1='ONCE, WHEN и AS SOON AS требуют настоящего времени для будущего.',
    condH2='Назовите оба условия',
    cond2='Ответственность и доступ. Работа без того и другого — это работа, за '
          'которую вас накажут и которую вы не можете выполнить.',
    condN2='&laquo;Formally allocated&raquo; — это то, что превращает поручение '
           'в запись.',

    askEyebrow='Просьба',
    askTitle='Попросите о двух вещах',
    askHint='По одному слову в пропуск; каждое используется один раз на двух '
            'экранах.',
    askHint2='По одному слову в пропуск &mdash; а в последней строке два.',

    corrEyebrow='Коридор',
    corrTitle='Четвёртая задача — по дороге на обед',
    corrCtx='Он говорит об этом, проходя мимо вашего стола, и идёт дальше.',

    funcEyebrow='Банк фраз',
    funcTitle='Что на самом деле делает каждая фраза',
    funcHint='Нажмите на строку, затем на её роль в разговоре.',

    resNext='Теперь проведите разговор &rarr;',
    resPerfect='Полный балл. Разницу вы слышите — теперь произнесите её вслух, '
               'это труднее.',
    resStrong='Сильно. Посмотрите на ошибки: чаще всего там приговор вместо '
              'даты.',
    resMid='Рабочая основа. Перечитайте три слайда с правилами, прежде чем '
           'говорить.',
    resLow='Пройдите три шага заново. Почти каждая ошибка — это оценка вместо '
           'факта.',

    actTitle='Теперь проведите разговор',
    actUse='Минимум четыре:',
    actSpeakKind='Говорение',
    actSpeakBrief='В парах. По три минуты каждому, затем поменяйтесь ролями и '
                  'повторите.',
    actSpeak1='Вы — младший. Он начинает: &laquo;Your time efficiency is '
              'concerning.&raquo;',
    actSpeak2='Поменяйтесь. В коридоре — четвёртая задача. Оформить или снять.',
    actSpeak3='Тот же разговор, в комнате HR. Что меняется, а что нет?',
    actSpeak4='Другая сторона: когда можно выйти за ваши полномочия?',
    actWriteKind='Письмо &middot; 180&ndash;220 слов',
    actWriteBrief='Письмо с просьбой уточнить вашу роль: три факта с датами, '
                  'одна уступка, одна конкретная просьба. Ничего о характере.',
    actPlaceholder='Dear Ana, following this morning&rsquo;s conversation, I '
                   'would like to set out what was allocated to me and '
                   'when&hellip;',
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
