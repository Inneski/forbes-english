# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 3.

All ten IELTS languages (`ielts_langs.LANGS`), teach cards in the
six-item form. English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-10-05 (conventions in `ielts_langs.py`).

The split is the same as the rest of the route, and on this deck the rule
being translated is almost entirely about attribution: who holds which
position, and how a discussion signals that somebody has changed theirs. The
names — Maya, Ravi — and the phrases they actually say stay English, because
the task is following English speakers through an English argument.
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
    coverTitle='Section 3 &mdash; <em>the academic discussion</em>',
    coverSub='Three speakers, two of whom change their minds, and every '
             'question keyed to a person',
    chipLevel='C1', chipFocus='Listening &middot; Section 3',
    chipCount='12 questions',

    t1Eyebrow='Before you listen',
    t1Title='The section is not about the topic. It is about who said it.',
    t1ah='Three voices, and the questions name them',
    t1ab='Two students and a tutor discussing a piece of work. The questions '
         'ask what <em>Ravi</em> thinks, what they <em>decided</em>, what the '
         '<em>tutor</em> suggested. An answer heard perfectly and given to the '
         'wrong speaker scores nothing.',
    t1an='Write the names down in the preparation time. Then you are tracking '
         'people, not sentences.',
    t1bh='Positions move',
    t1bb='This is a discussion, so somebody will argue themselves out of the '
         'view they opened with. What is marked is where they <strong>end '
         'up</strong>, not the first thing they said.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at first</em> '
         '&middot; <em>but you&rsquo;re right</em>. Every one of them says a '
         'position just changed.',
    t1ch='Suggested is not decided',
    t1cb='A tutor proposes things the students do not do. Both go in the '
         'recording and only one is the answer, so a question about the '
         '<em>plan</em> is answered by the students and a question about the '
         '<em>advice</em> by the tutor.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> That is a suggestion being declined, in two lines.',

    audEyebrow='The recording',
    audTitle='You will hear it once',
    audNote='Two students, Maya and Ravi, discussing a research project with '
            'their tutor. Three voices. Read the questions on the next slides '
            'first, then press play &mdash; here, or in the bar at the foot of '
            'any question slide. The recording keeps playing while you answer, '
            'and you hear it once.',

    topicEyebrow='Question 1 &middot; The project',
    topicHint='It is given in the first few seconds, before anyone disagrees '
              'about anything.',
    mcaEyebrow='Question 2 &middot; The method',
    mcbEyebrow='Question 7 &middot; The deadline',
    whoEyebrow='Questions 3&ndash;6 &middot; Who holds this view?',
    whoTitle='Match each position to the person who ends up holding it',
    whoHint='Click a position, then a person. What counts is where each '
            'speaker finishes, not where they started.',

    notesEyebrow='Questions 8&ndash;10 &middot; The tutorial notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='All three numbers are agreed out loud. One of them is argued '
              'about at length and then kept unchanged.',

    t2Eyebrow='After the recording',
    t2Title='Three ways a discussion hides the answer',
    t2ah='The agreement that is not one',
    t2ab='Ravi says <em>exactly</em> &mdash; and then states something Maya '
         'did not say. She corrects him: <em>that&rsquo;s not quite what I '
         'meant</em>. Agreement words are not evidence that two people agree.',
    t2an='The tutor then separates them explicitly, which is the recording '
         'handing you the answer if you are still listening.',
    t2bh='The shared term',
    t2bb='Both students say <em>response rate</em>. Ravi means how many people '
         'reply; Maya means how quickly. One phrase, two meanings, two '
         'different answers keyed to two different people.',
    t2bn='When a phrase is repeated by a second speaker, check they are using '
         'it for the same thing.',
    t2ch='The number that survives the argument',
    t2cb='Sixty is questioned, defended, doubted and kept. A discussion that '
         'argues about a figure and then leaves it alone is standard, and the '
         'length of the argument is not a signal that the figure changed.',
    t2cn='What changed was the plan around it: a pilot, and a reminder.',

    mcEyebrow='Questions 11&ndash;12 &middot; The reading',
    mcTitle='What happened in the discussion?',

    n1why='Because there are only two of them. Ravi gives the reason in the '
          'same breath as the decision. The tutor&rsquo;s preference for '
          'interviews is real but it is not why they chose otherwise.',
    n2why='They would lose the analysis time. The tutor concedes it is '
          'possible &mdash; <em>you could</em> &mdash; before giving the '
          'objection, and a concession before an objection is not agreement.',
    n3why='The Harrison chapter. Maya finds it thin and all American; Ravi '
          'likes the framework. The sample size and the reminder are both '
          'settled by agreement, not disagreement.',
    n4why='Use the framework and say the context differs. The tutor turns the '
          'weakness into a strength &mdash; which is not the same as either '
          'dropping Harrison or treating the difference as a problem.',

    actTitle='Hold the thread',
    actUse='Use at least three:',
    actSpeakBrief='In threes: two of you argue a decision out &mdash; where to '
                  'hold an event, what to spend a budget on &mdash; and one '
                  'takes notes. Each arguer must change their mind exactly '
                  'once, out loud.',
    actSpeak1='Arguers: signal the change when you make it. <em>Actually, '
              'no&hellip;</em> or <em>I was against that at first, but&hellip;'
              '</em>',
    actSpeak2='Use one phrase for two different things on purpose, and see '
              'whether the note-taker separates them.',
    actSpeak3='Note-taker: read your notes back naming who holds what. Every '
              'wrong attribution is a lost mark.',
    actWriteKind='Writing · 120–180 words',
    actWriteBrief='Write the minutes of a three-person meeting: what was '
                  'suggested, what was decided, and who ended up holding '
                  'which view. One person must be recorded as having changed '
                  'position, and one suggestion as declined.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
)

# The explanations for Questions 1, 3-6 and 8-10 sit beside their answers in
# the data module, which keeps the only copy of the English; they were plain
# strings there until 2026-09-23, so German and Spanish learners read them in
# English.
from ieltslisten_s3_data import TOPIC, WHO_WHY, DECISIONS
T['en']['g1why'] = TOPIC[0][2]
T['en']['whoWhy'] = WHO_WHY
T['en'].update(('d%dwhy' % (i + 1), r[2]) for i, r in enumerate(DECISIONS))

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Section 3 &mdash; <em>die akademische Diskussion</em>',
    coverSub='Drei Sprecher, zwei davon ändern ihre Meinung, und jede Frage '
             'ist an eine Person gebunden',
    chipLevel='C1', chipFocus='Listening &middot; Section 3',
    chipCount='12 Fragen',

    t1Eyebrow='Bevor du hörst',
    t1Title='Es geht nicht um das Thema, sondern darum, wer es gesagt hat.',
    t1ah='Drei Stimmen, und die Fragen nennen sie',
    t1ab='Zwei Studierende und ein Tutor besprechen eine Arbeit. Gefragt wird, '
         'was <em>Ravi</em> denkt, was sie <em>beschlossen</em> haben, was der '
         '<em>Tutor</em> vorgeschlagen hat. Eine perfekt gehörte Antwort, der '
         'falschen Person zugeordnet, bringt null.',
    t1an='Schreib die Namen in der Vorbereitungszeit auf. Dann verfolgst du '
         'Personen und nicht Sätze.',
    t1bh='Positionen bewegen sich',
    t1bb='Es ist eine Diskussion, also wird sich jemand aus der Meinung '
         'herausargumentieren, mit der er angefangen hat. Bewertet wird, wo '
         'jemand <strong>landet</strong>, nicht sein erster Satz.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at first</em> '
         '&middot; <em>but you&rsquo;re right</em>. Jedes davon meldet einen '
         'Positionswechsel.',
    t1ch='Vorgeschlagen ist nicht beschlossen',
    t1cb='Ein Tutor schlägt Dinge vor, die die Studierenden nicht tun. Beides '
         'steht in der Aufnahme und nur eines ist die Antwort: eine Frage nach '
         'dem <em>Plan</em> beantworten die Studierenden, eine nach dem '
         '<em>Rat</em> der Tutor.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> Ein abgelehnter Vorschlag, in zwei Zeilen.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal',
    audNote='Zwei Studierende, Maya und Ravi, besprechen ein Forschungsprojekt '
            'mit ihrem Tutor. Drei Stimmen. Lies zuerst die Fragen auf den '
            'nächsten Folien, dann drücke Play &mdash; hier oder in der Leiste '
            'unten auf jeder Fragenfolie. Die Aufnahme läuft weiter, während '
            'du antwortest, und du hörst sie einmal.',

    topicEyebrow='Frage 1 &middot; Das Projekt',
    topicHint='Es fällt in den ersten Sekunden, bevor irgendjemand '
              'widerspricht.',
    mcaEyebrow='Frage 2 &middot; Die Methode',
    mcbEyebrow='Frage 7 &middot; Die Frist',
    whoEyebrow='Fragen 3&ndash;6 &middot; Wer vertritt das?',
    whoTitle='Ordne jede Position der Person zu, die sie am Ende vertritt',
    whoHint='Klicke eine Position an, dann eine Person. Es zählt, wo jemand '
            'endet, nicht wo er angefangen hat.',

    notesEyebrow='Fragen 8&ndash;10 &middot; Die Besprechungsnotizen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Alle drei Zahlen werden laut vereinbart. Über eine wird lange '
              'gestritten &mdash; und sie bleibt unverändert.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Drei Arten, wie eine Diskussion die Antwort versteckt',
    t2ah='Die Zustimmung, die keine ist',
    t2ab='Ravi sagt <em>exactly</em> &mdash; und sagt dann etwas, das Maya gar '
         'nicht gesagt hat. Sie korrigiert ihn: <em>that&rsquo;s not quite what I '
         'meant</em>. Zustimmungswörter sind kein Beleg für Übereinstimmung.',
    t2an='Der Tutor trennt die beiden dann ausdrücklich &mdash; die Aufnahme '
         'reicht dir die Antwort, wenn du noch zuhörst.',
    t2bh='Der geteilte Begriff',
    t2bb='Beide Studierenden sagen <em>response rate</em>. Ravi meint, wie '
         'viele antworten; Maya, wie schnell. Ein Ausdruck, zwei Bedeutungen, '
         'zwei Antworten bei zwei verschiedenen Personen.',
    t2bn='Wenn ein zweiter Sprecher einen Ausdruck aufgreift, prüfe, ob er ihn '
         'für dasselbe benutzt.',
    t2ch='Die Zahl, die den Streit überlebt',
    t2cb='Sechzig wird infrage gestellt, verteidigt, bezweifelt &mdash; und '
         'behalten. Dass lange über eine Zahl gestritten wird, heißt nicht, '
         'dass sie sich ändert.',
    t2cn='Geändert hat sich der Plan drumherum: ein Pilot und eine '
         'Erinnerung.',

    mcEyebrow='Fragen 11&ndash;12 &middot; Die Lektüre',
    mcTitle='Was ist in der Diskussion passiert?',

    n1why='Weil sie nur zu zweit sind. Ravi nennt den Grund im selben Atemzug '
          'wie die Entscheidung. Die Vorliebe des Tutors für Interviews ist '
          'echt, aber nicht der Grund für ihre Wahl.',
    n2why='Sie verlören die Auswertungszeit. Der Tutor räumt ein, dass es '
          'ginge &mdash; <em>you could</em> &mdash; bevor der Einwand kommt, '
          'und ein Zugeständnis vor einem Einwand ist keine Zustimmung.',
    n3why='Das Harrison-Kapitel. Maya findet es dünn und rein amerikanisch, '
          'Ravi mag den Rahmen. Stichprobengröße und Erinnerung werden per '
          'Zustimmung geklärt, nicht im Streit.',
    n4why='Den Rahmen nutzen und sagen, dass der Kontext abweicht. Der Tutor '
          'macht aus der Schwäche eine Stärke &mdash; nicht dasselbe wie '
          'Harrison wegzulassen oder den Unterschied als Problem zu behandeln.',

    actTitle='Halte den Faden',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu dritt: zwei diskutieren eine Entscheidung aus &mdash; wo '
                  'eine Veranstaltung stattfindet, wofür ein Budget draufgeht '
                  '&mdash; einer schreibt mit. Jeder muss genau einmal laut '
                  'seine Meinung ändern.',
    actSpeak1='Diskutierende: kündigt den Wechsel an. <em>Actually, '
              'no&hellip;</em> oder <em>I was against that at first, '
              'but&hellip;</em>',
    actSpeak2='Benutzt absichtlich einen Ausdruck für zwei verschiedene Dinge '
              'und schaut, ob der Mitschreiber sie trennt.',
    actSpeak3='Mitschreiber: lies die Notizen zurück und nenne dabei, wer was '
              'vertritt. Jede falsche Zuordnung ist ein Punkt.',
    actWriteKind='Schreiben · 120–180 Wörter',
    actWriteBrief='Schreib das Protokoll einer Besprechung zu dritt: was '
                  'vorgeschlagen, was beschlossen wurde und wer am Ende '
                  'welche Meinung vertritt. Eine Person muss die Meinung '
                  'gewechselt haben, ein Vorschlag abgelehnt sein.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',

    # Questions 1, 3-6, 8-10: the English is registered from the data module.
    g1why='Zehn, in Mayas erstem Satz. Eine Section-3-Aufnahme nennt ihr Thema '
          'in den ersten Sekunden, bevor irgendjemand irgendetwas bestreitet.',
    whoWhy='Bei jeder Person steht der Zug, den sie macht, denn am Zug '
           'erkennst du die Meinung. Der Rat des Tutors wird gehört und '
           'abgelehnt; Maya nennt sechzig <em>in principle</em> in Ordnung und '
           'nimmt es sofort zurück; und „response rate“ sagen beide '
           'Studierenden über zwei verschiedene Dinge, die der Tutor dann für '
           'dich auseinanderhält: „Ravi’s talking about how many; Maya’s '
           'talking about how quickly.“',
    d1why='Drei Tage. Der Tutor nennt die Zahl, und die Studierenden '
          'wiederholen sie nie &mdash; der Tutor aber schon, einmal, in der '
          'Zusammenfassung am Ende.',
    d2why='Zehn. Ravi schlägt es vor, und Maya stimmt zu. Sie sagt, sie sei '
          'zuerst dagegen gewesen, aber die Antwort ist, wo sie am Ende steht.',
    d3why='Sechzig, unverändert. Die Zahl wird lange infrage gestellt und '
          'dann beibehalten &mdash; eine Diskussion, die über eine Zahl '
          'streitet und sie nicht ändert, ist ein typischer Zug in Section 3.',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Section 3 &mdash; <em>el debate académico</em>',
    coverSub='Tres hablantes, dos de los cuales cambian de opinión, y cada '
             'pregunta atada a una persona',
    chipLevel='C1', chipFocus='Listening &middot; Section 3',
    chipCount='12 preguntas',

    t1Eyebrow='Antes de escuchar',
    t1Title='No va del tema. Va de quién lo dijo.',
    t1ah='Tres voces, y las preguntas las nombran',
    t1ab='Dos estudiantes y un tutor hablando de un trabajo. Te preguntan qué '
         'piensa <em>Ravi</em>, qué <em>decidieron</em>, qué sugirió el '
         '<em>tutor</em>. Una respuesta oída perfectamente y atribuida a quien '
         'no es no puntúa.',
    t1an='Apunta los nombres en el tiempo de preparación. Así sigues a '
         'personas, no a frases.',
    t1bh='Las posturas se mueven',
    t1bb='Es un debate, así que alguien se va a sacar a sí mismo de la opinión '
         'con la que empezó. Lo que se califica es dónde <strong>acaba</strong>, '
         'no lo primero que dijo.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at first</em> '
         '&middot; <em>but you&rsquo;re right</em>. Cada uno avisa de un cambio de '
         'postura.',
    t1ch='Sugerido no es decidido',
    t1cb='Un tutor propone cosas que los estudiantes no hacen. Las dos están '
         'en la grabación y solo una es la respuesta: una pregunta sobre el '
         '<em>plan</em> la contestan los estudiantes y una sobre el '
         '<em>consejo</em>, el tutor.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> Una sugerencia rechazada, en dos líneas.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez',
    audNote='Dos estudiantes, Maya y Ravi, hablan de un proyecto de '
            'investigación con su tutor. Tres voces. Lee primero las preguntas '
            'de las diapositivas siguientes y luego dale a reproducir, aquí o '
            'en la barra de abajo de cualquier pregunta. La grabación sigue '
            'sonando mientras respondes, y la oyes una sola vez.',

    topicEyebrow='Pregunta 1 &middot; El proyecto',
    topicHint='Se dice en los primeros segundos, antes de que nadie discrepe '
              'de nada.',
    mcaEyebrow='Pregunta 2 &middot; El método',
    mcbEyebrow='Pregunta 7 &middot; El plazo',
    whoEyebrow='Preguntas 3&ndash;6 &middot; ¿De quién es esta postura?',
    whoTitle='Empareja cada postura con quien acaba sosteniéndola',
    whoHint='Haz clic en una postura y luego en una persona. Cuenta dónde '
            'acaba cada uno, no dónde empezó.',

    notesEyebrow='Preguntas 8&ndash;10 &middot; Las notas de la tutoría',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Los tres números se acuerdan en voz alta. Sobre uno se discute '
              'largo y tendido y se queda igual.',

    t2Eyebrow='Después de la grabación',
    t2Title='Tres maneras en que un debate esconde la respuesta',
    t2ah='El acuerdo que no lo es',
    t2ab='Ravi dice <em>exactly</em> y acto seguido dice algo que Maya no ha '
         'dicho. Ella le corrige: <em>that&rsquo;s not quite what I meant</em>. Las '
         'palabras de acuerdo no prueban que dos personas estén de acuerdo.',
    t2an='El tutor los separa después de forma explícita: la grabación te da '
         'la respuesta si sigues escuchando.',
    t2bh='El término compartido',
    t2bb='Los dos estudiantes dicen <em>response rate</em>. Ravi se refiere a '
         'cuántos contestan; Maya, a con qué rapidez. Una expresión, dos '
         'sentidos, dos respuestas atadas a dos personas distintas.',
    t2bn='Cuando un segundo hablante repite una expresión, comprueba que la '
         'use para lo mismo.',
    t2ch='El número que sobrevive a la discusión',
    t2cb='Sesenta se cuestiona, se defiende, se pone en duda y se mantiene. '
         'Que se discuta mucho sobre una cifra no significa que cambie.',
    t2cn='Lo que cambió fue el plan alrededor: un piloto y un recordatorio.',

    mcEyebrow='Preguntas 11&ndash;12 &middot; La lectura',
    mcTitle='¿Qué pasó en el debate?',

    n1why='Porque solo son dos. Ravi da el motivo en la misma frase que la '
          'decisión. La preferencia del tutor por las entrevistas es real, '
          'pero no es el motivo de su elección.',
    n2why='Perderían el tiempo de análisis. El tutor admite que se podría '
          '&mdash; <em>you could</em> &mdash; antes de poner la objeción, y '
          'una concesión antes de una objeción no es un acuerdo.',
    n3why='El capítulo de Harrison. Maya lo ve flojo y todo estadounidense; a '
          'Ravi le sirve el marco. El tamaño de la muestra y el recordatorio '
          'se resuelven de acuerdo, no discutiendo.',
    n4why='Usar el marco y decir que el contexto es distinto. El tutor '
          'convierte la debilidad en fortaleza, que no es lo mismo que dejar '
          'fuera a Harrison ni tratar la diferencia como un problema.',

    actTitle='Sigue el hilo',
    actUse='Usa al menos tres:',
    actSpeakBrief='De tres en tres: dos discuten una decisión &mdash; dónde '
                  'hacer un acto, en qué gastar un presupuesto &mdash; y uno '
                  'toma notas. Cada uno debe cambiar de opinión exactamente '
                  'una vez, en voz alta.',
    actSpeak1='Quienes discuten: avisad del cambio al hacerlo. <em>Actually, '
              'no&hellip;</em> o <em>I was against that at first, but&hellip;</em>',
    actSpeak2='Usad a propósito una misma expresión para dos cosas distintas y '
              'ved si quien toma notas las separa.',
    actSpeak3='Quien toma notas: lee las notas en voz alta diciendo quién '
              'sostiene qué. Cada atribución mal puesta es un punto perdido.',
    actWriteKind='Escritura · 120–180 palabras',
    actWriteBrief='Escribe el acta de una reunión de tres personas: qué se '
                  'sugirió, qué se decidió y quién acabó sosteniendo qué. Una '
                  'persona debe figurar como que cambió de postura, y una '
                  'sugerencia como rechazada.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',

    # Questions 1, 3-6, 8-10: the English is registered from the data module.
    g1why='Diez, en la primera frase de Maya. Una grabación de la Section 3 '
          'dice su tema en los primeros segundos, antes de que nadie discrepe '
          'de nada.',
    whoWhy='Cada persona aparece con el movimiento que hace, porque el '
           'movimiento es lo que te deja captar su postura. El consejo del '
           'tutor se escucha y se rechaza; Maya dice que sesenta está bien '
           '<em>in principle</em> y lo retira enseguida; y «response rate» lo '
           'dicen los dos estudiantes sobre dos cosas distintas, que el tutor '
           'luego te separa: «Ravi’s talking about how many; Maya’s talking '
           'about how quickly».',
    d1why='Tres días. El tutor da el número y los estudiantes no lo repiten '
          'nunca, aunque el tutor sí lo hace, una vez, en el resumen del final.',
    d2why='Diez. Ravi lo propone y Maya está de acuerdo. Dice que al principio '
          'estaba en contra, pero la respuesta es donde acaba.',
    d3why='Sesenta, sin cambios. Se discute largo y tendido y luego se '
          'mantiene: una conversación que discute un número y no lo cambia es '
          'un recurso típico de la Section 3.',
)


# ── French ──────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Section 3 — <em>la discussion universitaire</em>',
    coverSub="Trois voix, dont deux changent d'avis, et chaque question "
             'rattachée à une personne',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 questions',
    t1Eyebrow="Avant l'écoute",
    t1Title="La section ne porte pas sur le sujet. Elle porte sur qui l'a dit.",
    t1ah='Trois voix, et les questions les nomment',
    t1ab="Deux étudiants et un tuteur discutent d'un travail. Les questions "
         "demandent ce que pense <em>Ravi</em>, ce qu'ils ont "
         '<em>décidé</em>, ce que le <em>tuteur</em> a suggéré. Une réponse '
         'parfaitement entendue mais attribuée au mauvais locuteur ne '
         'rapporte rien.',
    t1an='Notez les prénoms pendant le temps de préparation. Vous suivez '
         'alors des personnes, pas des phrases.',
    t1bh='Les positions bougent',
    t1bb="C'est une discussion : quelqu'un va donc se convaincre lui-même "
         "d'abandonner l'avis qu'il défendait au départ. Ce qui est noté, "
         "c'est là où il <strong>finit</strong>, pas la première chose qu'il "
         'a dite.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re right</em>. Chacune de '
         "ces phrases annonce qu'une position vient de changer.",
    t1ch="Suggéré n'est pas décidé",
    t1cb='Un tuteur propose des choses que les étudiants ne font pas. Les '
         "deux figurent dans l'enregistrement et une seule est la réponse : "
         'une question sur le <em>plan</em> trouve sa réponse chez les '
         'étudiants, une question sur le <em>conseil</em> chez le tuteur.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> Voilà une suggestion déclinée, en deux répliques.',
    audEyebrow="L'enregistrement",
    audTitle="Vous l'entendrez une seule fois",
    audNote="Deux étudiants, Maya et Ravi, discutent d'un projet de recherche "
            "avec leur tuteur. Trois voix. Lisez d'abord les questions des "
            'diapositives suivantes, puis lancez la lecture — ici, ou dans la '
            "barre au bas de n'importe quelle diapositive de question. "
            "L'enregistrement continue pendant que vous répondez, et vous ne "
            "l'entendez qu'une fois.",
    topicEyebrow='Question 1 &middot; Le projet',
    topicHint='Il est donné dans les premières secondes, avant que quiconque ne '
              'soit en désaccord sur quoi que ce soit.',
    mcaEyebrow='Question 2 &middot; La méthode',
    mcbEyebrow="Question 7 &middot; L'échéance",
    whoEyebrow='Questions 3–6 &middot; Qui défend cet avis ?',
    whoTitle='Associez chaque position à la personne qui la tient en fin de '
             'compte',
    whoHint='Cliquez sur une position, puis sur une personne. Ce qui compte, '
            "c'est là où chaque locuteur termine, pas là où il a commencé.",
    notesEyebrow='Questions 8–10 &middot; Les notes du tutorat',
    notesTitle='Écrivez UN MOT ET/OU UN NOMBRE dans chaque espace',
    notesHint="Les trois nombres sont convenus à voix haute. L'un d'eux est "
              'longuement discuté, puis conservé tel quel.',
    t2Eyebrow="Après l'enregistrement",
    t2Title='Trois façons dont une discussion cache la réponse',
    t2ah="L'accord qui n'en est pas un",
    t2ab="Ravi dit <em>exactly</em> — puis énonce quelque chose que Maya n'a "
         'pas dit. Elle le corrige : <em>that&rsquo;s not quite what I '
         "meant</em>. Les mots d'accord ne prouvent pas que deux personnes "
         "sont d'accord.",
    t2an="Le tuteur les distingue ensuite explicitement : c'est "
         "l'enregistrement qui vous tend la réponse, si vous écoutez encore.",
    t2bh='Le terme partagé',
    t2bb='Les deux étudiants disent <em>response rate</em>. Ravi parle du '
         'nombre de personnes qui répondent ; Maya, de la rapidité. Une '
         'expression, deux sens, deux réponses différentes rattachées à deux '
         'personnes différentes.',
    t2bn='Quand une expression est reprise par un second locuteur, vérifiez '
         "qu'il l'emploie pour la même chose.",
    t2ch='Le nombre qui survit à la dispute',
    t2cb='Soixante est remis en question, défendu, mis en doute et conservé. '
         "Une discussion qui débat d'un chiffre puis le laisse tel quel est "
         "classique, et la longueur du débat n'est pas le signe que le "
         'chiffre a changé.',
    t2cn="Ce qui a changé, c'est le plan autour : un pilote, et un rappel.",
    mcEyebrow='Questions 11–12 &middot; La lecture',
    mcTitle="Que s'est-il passé dans la discussion ?",
    n1why="Parce qu'ils ne sont que deux. Ravi donne la raison dans le même "
          'souffle que la décision. La préférence du tuteur pour les '
          "entretiens est réelle, mais ce n'est pas pour cela qu'ils ont "
          'choisi autrement.',
    n2why="Ils perdraient le temps d'analyse. Le tuteur concède que c'est "
          "possible — <em>you could</em> — avant de donner l'objection, et "
          "une concession avant une objection n'est pas un accord.",
    n3why='Le chapitre de Harrison. Maya le trouve mince et entièrement '
          "américain ; Ravi aime le cadre. La taille de l'échantillon et le "
          'rappel sont tous deux réglés par un accord, pas par un désaccord.',
    n4why='Utiliser le cadre et dire que le contexte diffère. Le tuteur '
          "transforme la faiblesse en force — ce qui n'est ni abandonner "
          'Harrison, ni traiter la différence comme un problème.',
    actTitle='Gardez le fil',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief="Par trois : deux d'entre vous débattent d'une décision — où "
                  'organiser un événement, à quoi consacrer un budget — et le '
                  "troisième prend des notes. Chaque débatteur doit changer d'avis "
                  'exactement une fois, à voix haute.',
    actSpeak1='Débatteurs : signalez le changement au moment où vous le faites. '
              '<em>Actually, no&hellip;</em> ou <em>I was against that at first, '
              'but&hellip;</em>',
    actSpeak2='Employez volontairement une même expression pour deux choses '
              'différentes, et voyez si le preneur de notes les distingue.',
    actSpeak3='Preneur de notes : relisez vos notes en nommant qui défend quoi. '
              'Chaque attribution erronée est un point perdu.',
    actWriteKind='Writing · 120–180 mots',
    actWriteBrief="Rédigez le compte rendu d'une réunion à trois : ce qui a été "
                  'suggéré, ce qui a été décidé, et qui a fini par défendre quel '
                  'avis. Une personne doit être notée comme ayant changé de position, '
                  'et une suggestion comme déclinée.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='Dix, dans la première phrase de Maya. Un enregistrement de Section '
          '3 nomme son sujet dès les premières secondes, avant que quiconque '
          'ne soit en désaccord sur quoi que ce soit.',
    whoWhy="Chaque personne est nommée avec le mouvement qu'elle fait, parce "
           "que c'est au mouvement qu'on attrape l'avis. Le conseil du tuteur "
           'est entendu et décliné ; Maya juge soixante acceptable <em>in '
           'principle</em> et le reprend aussitôt ; et « response rate » est '
           'dit par les deux étudiants à propos de deux choses différentes, '
           'que le tuteur distingue ensuite pour vous : « Ravi&rsquo;s talking '
           'about how many; Maya&rsquo;s talking about how quickly. »',
    d1why='Trois jours. Le tuteur donne le nombre et les étudiants ne le '
          'répètent jamais — le tuteur, lui, le fait, une fois, dans le '
          'résumé final.',
    d2why="Dix. Ravi le propose et Maya accepte. Elle dit qu'elle était "
          'contre au départ, mais la réponse est là où elle finit.',
    d3why='Soixante, inchangé. Il est longuement remis en question puis '
          "conservé — une discussion qui débat d'un nombre sans le changer "
          'est un mouvement classique de la Section 3.',
)

# ── Italian ─────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Section 3 — <em>la discussione accademica</em>',
    coverSub='Tre voci, due delle quali cambiano idea, e ogni domanda legata a '
             'una persona',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 domande',
    t1Eyebrow='Prima di ascoltare',
    t1Title="La sezione non riguarda l'argomento. Riguarda chi l'ha detto.",
    t1ah='Tre voci, e le domande le nominano',
    t1ab='Due studenti e un tutor discutono di un lavoro. Le domande '
         'chiedono che cosa pensa <em>Ravi</em>, che cosa hanno '
         '<em>deciso</em>, che cosa ha suggerito il <em>tutor</em>. Una '
         'risposta sentita perfettamente ma attribuita alla persona '
         'sbagliata non vale nulla.',
    t1an='Scrivi i nomi durante il tempo di preparazione. Così segui le '
         'persone, non le frasi.',
    t1bh='Le posizioni si spostano',
    t1bb='È una discussione, quindi qualcuno finirà per convincersi ad '
         "abbandonare l'opinione con cui ha cominciato. Ciò che viene "
         'valutato è dove <strong>arriva alla fine</strong>, non la prima '
         'cosa che ha detto.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re right</em>. Ognuna di '
         'queste frasi segnala che una posizione è appena cambiata.',
    t1ch='Suggerito non è deciso',
    t1cb='Un tutor propone cose che gli studenti non fanno. Entrambe '
         'finiscono nella registrazione e solo una è la risposta: a una '
         'domanda sul <em>piano</em> rispondono gli studenti, a una domanda '
         'sul <em>consiglio</em> risponde il tutor.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> Ecco un suggerimento che viene rifiutato, in due '
         'battute.',
    audEyebrow='La registrazione',
    audTitle='La sentirai una sola volta',
    audNote='Due studenti, Maya e Ravi, discutono di un progetto di ricerca con '
            'il loro tutor. Tre voci. Leggi prima le domande nelle slide '
            'successive, poi premi play — qui, o nella barra in fondo a '
            'qualsiasi slide con una domanda. La registrazione continua mentre '
            'rispondi, e la senti una volta sola.',
    topicEyebrow='Domanda 1 &middot; Il progetto',
    topicHint='Viene dato nei primi secondi, prima che qualcuno sia in disaccordo '
              'su qualcosa.',
    mcaEyebrow='Domanda 2 &middot; Il metodo',
    mcbEyebrow='Domanda 7 &middot; La scadenza',
    whoEyebrow='Domande 3–6 &middot; Chi sostiene questa opinione?',
    whoTitle='Abbina ogni posizione alla persona che alla fine la sostiene',
    whoHint='Clicca una posizione, poi una persona. Conta dove ogni parlante '
            'finisce, non da dove è partito.',
    notesEyebrow='Domande 8–10 &middot; Gli appunti del tutorato',
    notesTitle='Scrivi UNA PAROLA E/O UN NUMERO in ogni spazio',
    notesHint='Tutti e tre i numeri vengono concordati ad alta voce. Uno di essi '
              "viene discusso a lungo e poi lasciato com'è.",
    t2Eyebrow='Dopo la registrazione',
    t2Title='Tre modi in cui una discussione nasconde la risposta',
    t2ah="L'accordo che non lo è",
    t2ab='Ravi dice <em>exactly</em> — e poi afferma qualcosa che Maya non '
         'ha detto. Lei lo corregge: <em>that&rsquo;s not quite what I '
         'meant</em>. Le parole di accordo non dimostrano che due persone '
         "siano d'accordo.",
    t2an='Il tutor poi li distingue esplicitamente: è la registrazione che '
         'ti consegna la risposta, se stai ancora ascoltando.',
    t2bh='Il termine condiviso',
    t2bb='Entrambi gli studenti dicono <em>response rate</em>. Ravi intende '
         "quante persone rispondono; Maya, quanto in fretta. Un'espressione, "
         'due significati, due risposte diverse legate a due persone '
         'diverse.',
    t2bn="Quando un'espressione viene ripetuta da un secondo parlante, "
         'verifica che la usi per la stessa cosa.',
    t2ch='Il numero che sopravvive alla discussione',
    t2cb='Sessanta viene messo in dubbio, difeso, contestato e mantenuto. '
         'Una discussione che litiga su una cifra e poi la lascia stare è la '
         'norma, e la lunghezza del litigio non è un segnale che la cifra '
         'sia cambiata.',
    t2cn='Ciò che è cambiato è il piano intorno: un pilota, e un promemoria.',
    mcEyebrow='Domande 11–12 &middot; La lettura',
    mcTitle='Che cosa è successo nella discussione?',
    n1why='Perché sono solo in due. Ravi dà il motivo nello stesso respiro '
          'della decisione. La preferenza del tutor per le interviste è '
          'reale, ma non è il motivo per cui hanno scelto diversamente.',
    n2why="Perderebbero il tempo per l'analisi. Il tutor ammette che è "
          "possibile — <em>you could</em> — prima di sollevare l'obiezione, e "
          "una concessione prima di un'obiezione non è un accordo.",
    n3why='Il capitolo di Harrison. Maya lo trova debole e tutto americano; a '
          'Ravi piace il quadro teorico. La dimensione del campione e il '
          'promemoria si risolvono entrambi con un accordo, non con un '
          'disaccordo.',
    n4why='Usare il quadro teorico e dire che il contesto è diverso. Il tutor '
          'trasforma la debolezza in un punto di forza — che non equivale né '
          'ad abbandonare Harrison né a trattare la differenza come un '
          'problema.',
    actTitle='Tieni il filo',
    actUse='Usane almeno tre:',
    actSpeakBrief='In tre: due di voi discutono una decisione — dove organizzare un '
                  'evento, come spendere un budget — e uno prende appunti. Chi '
                  'discute deve cambiare idea esattamente una volta, ad alta voce.',
    actSpeak1='Chi discute: segnala il cambiamento nel momento in cui lo fai. '
              '<em>Actually, no&hellip;</em> oppure <em>I was against that at '
              'first, but&hellip;</em>',
    actSpeak2='Usa di proposito una stessa espressione per due cose diverse, e '
              'guarda se chi prende appunti le distingue.',
    actSpeak3='Chi prende appunti: rileggi i tuoi appunti nominando chi sostiene '
              'cosa. Ogni attribuzione sbagliata è un punto perso.',
    actWriteKind='Writing · 120–180 parole',
    actWriteBrief='Scrivi il verbale di una riunione a tre: che cosa è stato '
                  'suggerito, che cosa è stato deciso, e chi alla fine ha sostenuto '
                  'quale opinione. Una persona deve risultare come qualcuno che ha '
                  'cambiato posizione, e un suggerimento come rifiutato.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='Dieci, nella prima frase di Maya. Una registrazione di Section 3 '
          'nomina il suo argomento nei primi secondi, prima che qualcuno sia '
          'in disaccordo su qualcosa.',
    whoWhy='Ogni persona è indicata con la mossa che fa, perché è dalla mossa '
           "che cogli l'opinione. Il consiglio del tutor viene ascoltato e "
           'rifiutato; Maya dice che sessanta va bene <em>in principle</em> e '
           'lo ritira subito; e «response rate» lo dicono entrambi gli '
           'studenti riferendosi a due cose diverse, che il tutor poi '
           'distingue per te: «Ravi&rsquo;s talking about how many; '
           'Maya&rsquo;s talking about how quickly.»',
    d1why='Tre giorni. Il tutor dà il numero e gli studenti non lo ripetono '
          'mai — il tutor invece sì, una volta, nel riepilogo finale.',
    d2why="Dieci. Ravi lo propone e Maya è d'accordo. Dice che all'inizio era "
          'contraria, ma la risposta è dove arriva alla fine.',
    d3why='Sessanta, invariato. Viene messo in dubbio a lungo e poi mantenuto '
          '— una discussione che litiga su un numero senza cambiarlo è una '
          'mossa classica della Section 3.',
)

# ── Portuguese ──────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Section 3 — <em>a discussão académica</em>',
    coverSub='Três vozes, duas das quais mudam de opinião, e cada pergunta '
             'ligada a uma pessoa',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 perguntas',
    t1Eyebrow='Antes de ouvir',
    t1Title='A secção não é sobre o tema. É sobre quem o disse.',
    t1ah='Três vozes, e as perguntas nomeiam-nas',
    t1ab='Dois estudantes e um tutor a discutir um trabalho. As perguntas '
         'querem saber o que <em>Ravi</em> pensa, o que eles '
         '<em>decidiram</em>, o que o <em>tutor</em> sugeriu. Uma resposta '
         'ouvida na perfeição mas atribuída à pessoa errada não vale nada.',
    t1an='Anota os nomes durante o tempo de preparação. Assim segues '
         'pessoas, não frases.',
    t1bh='As posições mudam',
    t1bb='É uma discussão, por isso alguém vai acabar por se convencer a '
         'abandonar a opinião com que começou. O que conta é onde '
         '<strong>acaba</strong>, não a primeira coisa que disse.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re right</em>. Cada uma '
         'destas frases anuncia que uma posição acabou de mudar.',
    t1ch='Sugerido não é decidido',
    t1cb='Um tutor propõe coisas que os estudantes não fazem. Ambas ficam na '
         'gravação e só uma é a resposta: a uma pergunta sobre o '
         '<em>plano</em> respondem os estudantes, a uma pergunta sobre o '
         '<em>conselho</em> responde o tutor.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> É uma sugestão a ser recusada, em duas falas.',
    audEyebrow='A gravação',
    audTitle='Vais ouvi-la uma só vez',
    audNote='Dois estudantes, Maya e Ravi, discutem um projeto de investigação '
            'com o seu tutor. Três vozes. Lê primeiro as perguntas nos '
            'diapositivos seguintes e depois carrega em play — aqui, ou na '
            'barra ao fundo de qualquer diapositivo de pergunta. A gravação '
            'continua enquanto respondes, e ouve-la uma só vez.',
    topicEyebrow='Pergunta 1 &middot; O projeto',
    topicHint='É dado nos primeiros segundos, antes de alguém discordar de alguma '
              'coisa.',
    mcaEyebrow='Pergunta 2 &middot; O método',
    mcbEyebrow='Pergunta 7 &middot; O prazo',
    whoEyebrow='Perguntas 3–6 &middot; Quem defende esta opinião?',
    whoTitle='Liga cada posição à pessoa que acaba por a defender',
    whoHint='Clica numa posição e depois numa pessoa. O que conta é onde cada '
            'falante termina, não onde começou.',
    notesEyebrow='Perguntas 8–10 &middot; As notas da tutoria',
    notesTitle='Escreve UMA PALAVRA E/OU UM NÚMERO em cada espaço',
    notesHint='Os três números são acordados em voz alta. Um deles é longamente '
              'discutido e depois mantido sem alteração.',
    t2Eyebrow='Depois da gravação',
    t2Title='Três maneiras de uma discussão esconder a resposta',
    t2ah='O acordo que não o é',
    t2ab='Ravi diz <em>exactly</em> — e depois afirma algo que Maya não '
         'disse. Ela corrige-o: <em>that&rsquo;s not quite what I '
         'meant</em>. Palavras de concordância não provam que duas pessoas '
         'concordam.',
    t2an='O tutor separa-os depois explicitamente: é a gravação a '
         'entregar-te a resposta, se ainda estiveres a ouvir.',
    t2bh='O termo partilhado',
    t2bb='Ambos os estudantes dizem <em>response rate</em>. Ravi refere-se a '
         'quantas pessoas respondem; Maya, à rapidez. Uma expressão, dois '
         'sentidos, duas respostas diferentes ligadas a duas pessoas '
         'diferentes.',
    t2bn='Quando uma expressão é repetida por um segundo falante, verifica '
         'se a usa para a mesma coisa.',
    t2ch='O número que sobrevive à discussão',
    t2cb='Sessenta é questionado, defendido, posto em dúvida e mantido. Uma '
         'discussão que debate um valor e depois o deixa como está é normal, '
         'e a duração do debate não é sinal de que o valor mudou.',
    t2cn='O que mudou foi o plano à volta: um piloto, e um lembrete.',
    mcEyebrow='Perguntas 11–12 &middot; A leitura',
    mcTitle='O que aconteceu na discussão?',
    n1why='Porque são só dois. Ravi dá a razão no mesmo fôlego que a decisão. '
          'A preferência do tutor por entrevistas é real, mas não é por isso '
          'que escolheram de outra forma.',
    n2why='Perderiam o tempo de análise. O tutor admite que é possível — '
          '<em>you could</em> — antes de apresentar a objeção, e uma '
          'concessão antes de uma objeção não é concordância.',
    n3why='O capítulo de Harrison. Maya acha-o fraco e todo americano; Ravi '
          'gosta do enquadramento. A dimensão da amostra e o lembrete são '
          'ambos resolvidos por acordo, não por desacordo.',
    n4why='Usar o enquadramento e dizer que o contexto é diferente. O tutor '
          'transforma a fraqueza em força — o que não é o mesmo que abandonar '
          'Harrison nem tratar a diferença como um problema.',
    actTitle='Segura o fio',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em grupos de três: dois discutem uma decisão — onde realizar um '
                  'evento, em que gastar um orçamento — e um toma notas. Cada um dos '
                  'que discutem tem de mudar de opinião exatamente uma vez, em voz '
                  'alta.',
    actSpeak1='Quem discute: assinala a mudança no momento em que a fazes. '
              '<em>Actually, no&hellip;</em> ou <em>I was against that at first, '
              'but&hellip;</em>',
    actSpeak2='Usa de propósito uma mesma expressão para duas coisas diferentes e '
              'vê se quem toma notas as distingue.',
    actSpeak3='Quem toma notas: lê as tuas notas em voz alta dizendo quem defende '
              'o quê. Cada atribuição errada é um ponto perdido.',
    actWriteKind='Writing · 120–180 palavras',
    actWriteBrief='Escreve a ata de uma reunião a três: o que foi sugerido, o que foi '
                  'decidido, e quem acabou por defender que opinião. Uma pessoa tem '
                  'de ficar registada como tendo mudado de posição, e uma sugestão '
                  'como recusada.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='Dez, na primeira frase de Maya. Uma gravação da Section 3 nomeia o '
          'seu tema nos primeiros segundos, antes de alguém discordar de '
          'alguma coisa.',
    whoWhy='Cada pessoa é indicada com o movimento que faz, porque é pelo '
           'movimento que apanhas a opinião. O conselho do tutor é ouvido e '
           'recusado; Maya diz que sessenta está bem <em>in principle</em> e '
           'retira-o logo a seguir; e «response rate» é dito por ambos os '
           'estudantes sobre duas coisas diferentes, que o tutor depois separa '
           'para ti: «Ravi&rsquo;s talking about how many; Maya&rsquo;s '
           'talking about how quickly.»',
    d1why='Três dias. O tutor dá o número e os estudantes nunca o repetem — '
          'mas o tutor repete-o, uma vez, no resumo final.',
    d2why='Dez. Ravi propõe-no e Maya concorda. Ela diz que ao princípio era '
          'contra, mas a resposta é onde ela acaba.',
    d3why='Sessenta, sem alteração. É longamente questionado e depois mantido '
          '— uma discussão que debate um número e não o muda é um movimento '
          'clássico da Section 3.',
)

# ── Russian ─────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Section 3 — <em>академическая дискуссия</em>',
    coverSub='Три голоса, двое из которых меняют мнение, и каждый вопрос '
             'привязан к человеку',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 вопросов',
    t1Eyebrow='Перед прослушиванием',
    t1Title='Раздел не о теме. Он о том, кто это сказал.',
    t1ah='Три голоса, и вопросы называют их по именам',
    t1ab='Два студента и преподаватель обсуждают работу. Вопросы спрашивают, '
         'что думает <em>Ravi</em>, что они <em>решили</em>, что предложил '
         '<em>преподаватель</em>. Ответ, услышанный идеально, но приписанный '
         'не тому говорящему, не приносит ни балла.',
    t1an='Запишите имена во время подготовки. Тогда вы следите за людьми, а '
         'не за предложениями.',
    t1bh='Позиции сдвигаются',
    t1bb='Это дискуссия, поэтому кто-то в споре сам откажется от мнения, с '
         'которого начал. Оценивается то, к чему он <strong>приходит в '
         'итоге</strong>, а не первое, что он сказал.',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re right</em>. Каждая из '
         'этих фраз сообщает: позиция только что изменилась.',
    t1ch='Предложено — не значит решено',
    t1cb='Преподаватель предлагает то, чего студенты не делают. В записи '
         'есть и то и другое, а ответ только один: на вопрос о '
         '<em>плане</em> отвечают студенты, на вопрос о <em>совете</em> — '
         'преподаватель.',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> Вот предложение, которое отклоняют, в двух '
         'репликах.',
    audEyebrow='Запись',
    audTitle='Вы услышите её один раз',
    audNote='Два студента, Maya и Ravi, обсуждают исследовательский проект со '
            'своим преподавателем. Три голоса. Сначала прочитайте вопросы на '
            'следующих слайдах, затем нажмите play — здесь или на панели внизу '
            'любого слайда с вопросом. Запись продолжает играть, пока вы '
            'отвечаете, и звучит один раз.',
    topicEyebrow='Вопрос 1 &middot; Проект',
    topicHint='Он назван в первые секунды, прежде чем кто-либо с чем-либо не '
              'согласится.',
    mcaEyebrow='Вопрос 2 &middot; Метод',
    mcbEyebrow='Вопрос 7 &middot; Срок',
    whoEyebrow='Вопросы 3–6 &middot; Кто придерживается этого мнения?',
    whoTitle='Соотнесите каждую позицию с человеком, который в итоге её '
             'придерживается',
    whoHint='Нажмите на позицию, затем на человека. Важно, где каждый говорящий '
            'заканчивает, а не где он начал.',
    notesEyebrow='Вопросы 8–10 &middot; Заметки с консультации',
    notesTitle='Напишите ОДНО СЛОВО И/ИЛИ ЧИСЛО в каждый пропуск',
    notesHint='Все три числа согласуются вслух. Об одном из них долго спорят, а '
              'затем оставляют без изменений.',
    t2Eyebrow='После записи',
    t2Title='Три способа, которыми дискуссия скрывает ответ',
    t2ah='Согласие, которое не согласие',
    t2ab='Ravi говорит <em>exactly</em> — а затем произносит то, чего Maya '
         'не говорила. Она поправляет его: <em>that&rsquo;s not quite what I '
         'meant</em>. Слова согласия не доказывают, что двое согласны.',
    t2an='Затем преподаватель явно разделяет их — запись сама вручает вам '
         'ответ, если вы ещё слушаете.',
    t2bh='Общий термин',
    t2bb='Оба студента говорят <em>response rate</em>. Ravi имеет в виду, '
         'сколько людей отвечают; Maya — как быстро. Одна фраза, два '
         'значения, два разных ответа, привязанных к двум разным людям.',
    t2bn='Когда фразу повторяет второй говорящий, проверьте, что он '
         'использует её для того же самого.',
    t2ch='Число, которое переживает спор',
    t2cb='Шестьдесят ставят под вопрос, защищают, сомневаются в нём и '
         'оставляют. Дискуссия, которая спорит о цифре и затем оставляет её '
         'в покое, — обычное дело, и длина спора не сигнал, что цифра '
         'изменилась.',
    t2cn='Изменился план вокруг неё: пилотный опрос и напоминание.',
    mcEyebrow='Вопросы 11–12 &middot; Чтение',
    mcTitle='Что произошло в дискуссии?',
    n1why='Потому что их только двое. Ravi называет причину на одном дыхании '
          'с решением. Предпочтение преподавателя к интервью реально, но не '
          'поэтому они выбрали другое.',
    n2why='Они потеряли бы время на анализ. Преподаватель признаёт, что это '
          'возможно — <em>you could</em>, — прежде чем высказать возражение, '
          'а уступка перед возражением не есть согласие.',
    n3why='Глава Harrison. Maya находит её слабой и целиком американской; '
          'Ravi нравится её теоретическая схема. Размер выборки и напоминание '
          'решаются согласием, а не разногласием.',
    n4why='Использовать схему и сказать, что контекст отличается. '
          'Преподаватель превращает слабость в силу — а это не то же самое, '
          'что отказаться от Harrison или считать различие проблемой.',
    actTitle='Держите нить',
    actUse='Используйте не менее трёх:',
    actSpeakBrief='По трое: двое спорят о решении — где провести мероприятие, на что '
                  'потратить бюджет, — а третий ведёт записи. Каждый из спорящих '
                  'должен ровно один раз изменить мнение, вслух.',
    actSpeak1='Спорящие: обозначайте перемену в момент, когда она происходит. '
              '<em>Actually, no&hellip;</em> или <em>I was against that at first, '
              'but&hellip;</em>',
    actSpeak2='Намеренно используйте одну фразу для двух разных вещей и '
              'посмотрите, разделит ли их тот, кто ведёт записи.',
    actSpeak3='Ведущий записи: прочитайте свои заметки вслух, называя, кто что '
              'отстаивает. Каждая ошибочная атрибуция — потерянный балл.',
    actWriteKind='Writing · 120–180 слов',
    actWriteBrief='Напишите протокол встречи троих: что было предложено, что решено и '
                  'кто в итоге придерживался какого мнения. Один человек должен быть '
                  'записан как изменивший позицию, а одно предложение — как '
                  'отклонённое.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='Десять, в первой фразе Maya. Запись Section 3 называет свою тему в '
          'первые секунды, прежде чем кто-либо с чем-либо не согласится.',
    whoWhy='Каждый человек назван вместе с ходом, который он делает, потому '
           'что именно по ходу вы ловите мнение. Совет преподавателя выслушан '
           'и отклонён; Maya называет шестьдесят приемлемым <em>in '
           'principle</em> и сразу берёт слова назад; а «response rate» оба '
           'студента говорят о двух разных вещах, которые преподаватель затем '
           'разделяет для вас: «Ravi&rsquo;s talking about how many; '
           'Maya&rsquo;s talking about how quickly.»',
    d1why='Три дня. Преподаватель называет число, и студенты его не повторяют '
          '— а преподаватель повторяет, один раз, в итоговом резюме.',
    d2why='Десять. Ravi предлагает, Maya соглашается. Она говорит, что '
          'сначала была против, но ответ — то, к чему она приходит в итоге.',
    d3why='Шестьдесят, без изменений. Его долго ставят под вопрос, а затем '
          'оставляют — дискуссия, которая спорит о числе и не меняет его, '
          'стандартный ход Section 3.',
)

# ── Arabic ──────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='<bdi>Section 3</bdi> — <em>المناقشة الأكاديمية</em>',
    coverSub='ثلاثة أصوات، اثنان منها يغيّران رأيهما، وكل سؤال مرتبط بشخص',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 سؤالًا',
    t1Eyebrow='قبل الاستماع',
    t1Title='القسم ليس عن الموضوع. بل عمّن قاله.',
    t1ah='ثلاثة أصوات، والأسئلة تسمّيها',
    t1ab='طالبان ومشرف يناقشون عملًا. تسأل الأسئلة ما رأي '
         '<em><bdi>Ravi</bdi></em>، وماذا <em>قرّرا</em>، وماذا اقترح '
         '<em>المشرف</em>. الجواب الذي تسمعه بوضوح كامل ثم تنسبه إلى المتكلم '
         'الخطأ لا يحصد شيئًا.',
    t1an='اكتب الأسماء في وقت التحضير. حينئذٍ تتابع أشخاصًا، لا جُملًا.',
    t1bh='المواقف تتحرك',
    t1bb='هذه مناقشة، لذا سيُقنع أحدهم نفسه بالتخلي عن الرأي الذي بدأ به. ما '
         'يُحتسب هو حيث <strong>ينتهي</strong>، لا أول ما قاله.',
    t1bn='<em><bdi>Actually, no</bdi></em> &middot; <em><bdi>I was against '
         'that at first</bdi></em> &middot; <em><bdi>but you&rsquo;re '
         'right</bdi></em>. كل واحدة منها تقول إن موقفًا تغيّر للتو.',
    t1ch='المقترَح ليس المقرَّر',
    t1cb='يقترح المشرف أشياء لا يفعلها الطالبان. كلاهما في التسجيل وواحد فقط '
         'هو الجواب، فالسؤال عن <em>الخطة</em> يجيب عنه الطالبان، والسؤال عن '
         '<em>النصيحة</em> يجيب عنه المشرف.',
    t1cn='<em><bdi>I&rsquo;d still push you towards&hellip; Fair enough, '
         'your decision.</bdi></em> هذا اقتراح يُرفض، في سطرين.',
    audEyebrow='التسجيل',
    audTitle='ستسمعه مرة واحدة',
    audNote='طالبان، <bdi>Maya</bdi> و<bdi>Ravi</bdi>، يناقشان مشروعًا بحثيًا '
            'مع مشرفهما. ثلاثة أصوات. اقرأ الأسئلة في الشرائح التالية أولًا، ثم '
            'اضغط التشغيل — هنا، أو في الشريط أسفل أي شريحة أسئلة. يستمر '
            'التسجيل أثناء إجابتك، وتسمعه مرة واحدة.',
    topicEyebrow='السؤال 1 &middot; المشروع',
    topicHint='يُذكر في الثواني الأولى، قبل أن يختلف أحد على أي شيء.',
    mcaEyebrow='السؤال 2 &middot; المنهج',
    mcbEyebrow='السؤال 7 &middot; الموعد النهائي',
    whoEyebrow='الأسئلة 3–6 &middot; من يتبنّى هذا الرأي؟',
    whoTitle='طابق كل موقف مع الشخص الذي ينتهي به الأمر متبنّيًا له',
    whoHint='انقر على موقف، ثم على شخص. ما يُحتسب هو حيث ينتهي كل متكلم، لا حيث '
            'بدأ.',
    notesEyebrow='الأسئلة 8–10 &middot; ملاحظات اللقاء الإشرافي',
    notesTitle='اكتب كلمة واحدة و/أو رقمًا في كل فراغ',
    notesHint='الأرقام الثلاثة كلها يُتفق عليها بصوت مسموع. أحدها يُجادَل فيه '
              'طويلًا ثم يُترك بلا تغيير.',
    t2Eyebrow='بعد التسجيل',
    t2Title='ثلاث طرائق تخفي بها المناقشة الجواب',
    t2ah='الاتفاق الذي ليس اتفاقًا',
    t2ab='يقول <bdi>Ravi</bdi> <em><bdi>exactly</bdi></em> — ثم يذكر شيئًا '
         'لم تقله <bdi>Maya</bdi>. فتصحّح له: <em><bdi>that&rsquo;s not '
         'quite what I meant</bdi></em>. كلمات الاتفاق ليست دليلًا على أن '
         'شخصين متفقان.',
    t2an='ثم يفصل المشرف بينهما صراحةً، وهذا هو التسجيل يسلّمك الجواب إن كنت '
         'ما تزال تستمع.',
    t2bh='المصطلح المشترك',
    t2bb='الطالبان كلاهما يقولان <em><bdi>response rate</bdi></em>. يعني '
         '<bdi>Ravi</bdi> كم شخصًا يردّ؛ وتعني <bdi>Maya</bdi> بأي سرعة. '
         'عبارة واحدة، معنيان، جوابان مختلفان مرتبطان بشخصين مختلفين.',
    t2bn='حين يكرّر متكلم ثانٍ عبارةً، تحقّق من أنه يستعملها للشيء نفسه.',
    t2ch='الرقم الذي ينجو من الجدال',
    t2cb='ستون يُشكَّك فيه ويُدافَع عنه ويُرتاب فيه ويُحتفظ به. المناقشة '
         'التي تجادل في رقم ثم تتركه كما هو أمر معتاد، وطول الجدال ليس إشارة '
         'إلى أن الرقم تغيّر.',
    t2cn='ما تغيّر هو الخطة حوله: دراسة تجريبية، وتذكير.',
    mcEyebrow='السؤالان 11–12 &middot; القراءة',
    mcTitle='ماذا حدث في المناقشة؟',
    n1why='لأنهما اثنان فقط. يذكر <bdi>Ravi</bdi> السبب في النفَس نفسه مع '
          'القرار. ميل المشرف إلى المقابلات حقيقي لكنه ليس سبب اختيارهما غير '
          'ذلك.',
    n2why='سيخسران وقت التحليل. يسلّم المشرف بأن ذلك ممكن — <em><bdi>you '
          'could</bdi></em> — قبل أن يذكر الاعتراض، والتنازل قبل الاعتراض ليس '
          'موافقة.',
    n3why='فصل <bdi>Harrison</bdi>. تجده <bdi>Maya</bdi> ضعيفًا وأمريكيًّا '
          'بالكامل؛ ويعجب <bdi>Ravi</bdi> إطارُه النظري. حجم العيّنة والتذكير '
          'يُحسمان كلاهما بالاتفاق، لا بالاختلاف.',
    n4why='استعمال الإطار النظري والقول إن السياق مختلف. يحوّل المشرف نقطة '
          'الضعف إلى قوة — وهذا ليس كالتخلي عن <bdi>Harrison</bdi> ولا '
          'كاعتبار الاختلاف مشكلة.',
    actTitle='أمسك بخيط الحديث',
    actUse='استعمل ثلاثًا على الأقل:',
    actSpeakBrief='في مجموعات ثلاثية: اثنان منكم يتجادلان حول قرار — أين يُقام حدث، '
                  'على ماذا تُنفق ميزانية — والثالث يدوّن الملاحظات. على كل مجادل أن '
                  'يغيّر رأيه مرة واحدة بالضبط، بصوت مسموع.',
    actSpeak1='المجادلان: أشيرا إلى التغيير حين تقومان به. <em><bdi>Actually, '
              'no&hellip;</bdi></em> أو <em><bdi>I was against that at first, '
              'but&hellip;</bdi></em>',
    actSpeak2='استعمل عبارة واحدة لشيئين مختلفين عن قصد، وانظر هل يفصل بينهما '
              'مدوّن الملاحظات.',
    actSpeak3='مدوّن الملاحظات: اقرأ ملاحظاتك مسمّيًا من يتبنّى أي رأي. كل نسبة '
              'خاطئة علامة ضائعة.',
    actWriteKind='Writing · 120–180 كلمة',
    actWriteBrief='اكتب محضر اجتماع لثلاثة أشخاص: ما اقتُرح، وما قُرّر، ومن انتهى به '
                  'الأمر متبنّيًا أي رأي. يجب أن يُسجَّل شخص واحد بوصفه غيّر موقفه، '
                  'واقتراح واحد بوصفه مرفوضًا.',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='عشرة، في أول جملة تقولها <bdi>Maya</bdi>. تسجيل <bdi>Section '
          '3</bdi> يسمّي موضوعه في الثواني الأولى، قبل أن يختلف أحد على أي '
          'شيء.',
    whoWhy='كل شخص مسمّى مع الحركة التي يقوم بها، لأن الحركة هي ما تلتقط به '
           'الرأي. نصيحة المشرف تُسمع وتُرفض؛ و<bdi>Maya</bdi> تصف الستين '
           'بأنها مقبولة <em><bdi>in principle</bdi></em> ثم تتراجع فورًا؛ '
           'و<bdi>"response rate"</bdi> يقولها الطالبان عن شيئين مختلفين، ثم '
           'يفصل المشرف بينهما لك: <bdi>"Ravi&rsquo;s talking about how many; '
           'Maya&rsquo;s talking about how quickly."</bdi>',
    d1why='ثلاثة أيام. يذكر المشرف الرقم ولا يكرّره الطالبان أبدًا — لكن '
          'المشرف يكرّره، مرة واحدة، في الملخص في النهاية.',
    d2why='عشرة. يقترحها <bdi>Ravi</bdi> وتوافق <bdi>Maya</bdi>. تقول إنها '
          'كانت ضدها في البداية، لكن الجواب هو حيث تنتهي.',
    d3why='ستون، بلا تغيير. يُشكَّك فيه طويلًا ثم يُحتفظ به — المناقشة التي '
          'تجادل في رقم ولا تغيّره حركة معتادة في <bdi>Section 3</bdi>.',
)

# ── Chinese ─────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Section 3 — <em>学术讨论</em>',
    coverSub='三位说话者，其中两位改变了想法，而每个问题都对应一个人',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 道题',
    t1Eyebrow='听之前',
    t1Title='这一部分考的不是话题，而是谁说的。',
    t1ah='三个声音，而问题点名道姓',
    t1ab='两名学生和一位导师在讨论一份作业。问题问的是 <em>Ravi</em> '
         '怎么想、他们<em>决定</em>了什么、<em>导师</em>建议了什么。听得一清二楚却归到错误的说话者身上的答案，一分也拿不到。',
    t1an='在准备时间里把名字写下来。这样你追踪的就是人，而不是句子。',
    t1bh='立场会移动',
    t1bb='这是一场讨论，所以总有人会在争论中放弃自己一开始的观点。评分看的是他<strong>最终的立场</strong>，而不是他最先说的话。',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re right</em>。每一句都在说：立场刚刚变了。',
    t1ch='建议过不等于决定了',
    t1cb='导师提出的事情，学生并不去做。两者都在录音里，而答案只有一个：关于<em>计划</em>的问题由学生回答，关于<em>建议</em>的问题由导师回答。',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> 这就是一条建议被拒绝的过程，只用了两句话。',
    audEyebrow='录音',
    audTitle='你只会听一遍',
    audNote='两名学生 Maya 和 Ravi '
            '正在和导师讨论一个研究项目。三个声音。先阅读接下来几页的问题，再按播放——在这里，或在任何问题页底部的播放栏。你作答时录音会继续播放，而且只播一遍。',
    topicEyebrow='第 1 题 &middot; 项目',
    topicHint='它在最初几秒就给出了，在任何人对任何事产生分歧之前。',
    mcaEyebrow='第 2 题 &middot; 方法',
    mcbEyebrow='第 7 题 &middot; 截止日期',
    whoEyebrow='第 3–6 题 &middot; 谁持这种观点？',
    whoTitle='把每个立场和最终持有它的人配对',
    whoHint='先点一个立场，再点一个人。算的是每位说话者最后停在哪里，而不是从哪里开始。',
    notesEyebrow='第 8–10 题 &middot; 辅导笔记',
    notesTitle='在每个空格里填写一个单词和/或一个数字',
    notesHint='三个数字都是当场出声商定的。其中一个被长时间争论，然后原样保留。',
    t2Eyebrow='听完之后',
    t2Title='讨论隐藏答案的三种方式',
    t2ah='并非同意的同意',
    t2ab='Ravi 说 <em>exactly</em>——然后说出的却是 Maya 没说过的话。她纠正他：<em>that&rsquo;s '
         'not quite what I meant</em>。表示同意的词并不能证明两个人真的意见一致。',
    t2an='随后导师明确地把两人的意思分开——如果你还在听，这就是录音把答案递到你手上。',
    t2bh='共用的术语',
    t2bb='两名学生都说了 <em>response rate</em>。Ravi 指的是有多少人回复；Maya '
         '指的是回复得多快。一个短语，两种含义，两个不同的答案对应两个不同的人。',
    t2bn='当一个短语被第二个说话者重复时，核对一下他们指的是不是同一件事。',
    t2ch='在争论中幸存的数字',
    t2cb='六十被质疑、被辩护、被怀疑，最后被保留。一场讨论围着一个数字争论然后又不去动它，这很常见；争论的长度并不说明数字变了。',
    t2cn='变的是围绕它的计划：一次试点，和一次提醒。',
    mcEyebrow='第 11–12 题 &middot; 解读',
    mcTitle='讨论中发生了什么？',
    n1why='因为他们只有两个人。Ravi 在说出决定的同时就给出了理由。导师偏爱访谈是真的，但这不是他们另作选择的原因。',
    n2why='他们会失去分析的时间。导师先承认这是可能的——<em>you could</em>——然后才提出反对；反对之前的让步并不是同意。',
    n3why='Harrison 的那一章。Maya 觉得它单薄而且全是美国的材料；Ravi '
          '喜欢它的框架。样本规模和提醒都是靠一致意见解决的，而不是分歧。',
    n4why='使用这个框架，并说明背景不同。导师把弱点变成了优点——这既不等于放弃 Harrison，也不等于把差异当成问题。',
    actTitle='抓住线索',
    actUse='至少使用三个：',
    actSpeakBrief='三人一组：两人就一项决定展开争论——在哪里举办活动、预算花在什么上——第三人做笔记。每位争论者都必须恰好改变一次想法，并且说出来。',
    actSpeak1='争论者：在改变想法的那一刻就把它标示出来。<em>Actually, no&hellip;</em> 或 <em>I was '
              'against that at first, but&hellip;</em>',
    actSpeak2='故意用同一个短语表达两件不同的事，看看做笔记的人能否把它们区分开。',
    actSpeak3='做笔记的人：把笔记读出来，说明谁持什么观点。每一处归属错误都是一分丢失。',
    actWriteKind='Writing · 120–180 词',
    actWriteBrief='写一份三人会议的纪要：建议了什么、决定了什么、谁最终持有哪种观点。必须有一个人被记录为改变了立场，有一条建议被记录为遭到拒绝。',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='十，在 Maya 的第一句话里。Section 3 的录音在开头几秒就点出话题，在任何人对任何事产生分歧之前。',
    whoWhy='每个人都和他做出的动作一起被点名，因为正是通过动作你才能抓住观点。导师的建议被听到然后被拒绝；Maya 说六十 <em>in '
           'principle</em> 可以，随即又收回；而 "response rate" '
           '两名学生都说了，指的却是两件不同的事，导师随后替你把它们分开："Ravi&rsquo;s talking about how '
           'many; Maya&rsquo;s talking about how quickly."',
    d1why='三天。导师给出这个数字，学生从未重复——不过导师在结尾的总结里重复了一次。',
    d2why='十。Ravi 提出，Maya 同意。她说自己起初是反对的，但答案是她最终的立场。',
    d3why='六十，没有变化。它被长时间质疑，然后被保留——一场讨论围着一个数字争论却不改变它，是 Section 3 的标准套路。',
)

# ── Japanese ────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Section 3 — <em>アカデミックな討論</em>',
    coverSub='三人の話者、そのうち二人は考えを変え、どの問題も人物に結びついています',
    chipLevel='C1',
    chipFocus='Listening &middot; Section 3',
    chipCount='12 問',
    t1Eyebrow='聞く前に',
    t1Title='このセクションはテーマを問うのではありません。誰が言ったかを問うのです。',
    t1ah='三つの声、そして問題はその名前を挙げる',
    t1ab='二人の学生と一人の指導教員が課題について話し合います。問題は、<em>Ravi</em> '
         'はどう考えているか、二人は何を<em>決めた</em>か、<em>指導教員</em>は何を提案したかを問います。完璧に聞き取れていても、違う話者に結びつけた答えは一点にもなりません。',
    t1an='準備時間に名前を書き留めましょう。そうすれば追うのは文ではなく人になります。',
    t1bh='立場は動く',
    t1bb='これは討論なので、誰かが議論の中で最初の意見を自ら手放します。採点されるのは<strong>最終的にどこに落ち着いたか</strong>であり、最初に言ったことではありません。',
    t1bn='<em>Actually, no</em> &middot; <em>I was against that at '
         'first</em> &middot; <em>but you&rsquo;re '
         'right</em>。どれも、立場が今まさに変わったことを告げています。',
    t1ch='提案されたことは決まったことではない',
    t1cb='指導教員は、学生がやらないことを提案します。どちらも録音に入っていて、答えは一つだけです。<em>計画</em>についての問題には学生が、<em>助言</em>についての問題には指導教員が答えを与えます。',
    t1cn='<em>I&rsquo;d still push you towards&hellip; Fair enough, your '
         'decision.</em> 提案が断られる場面が、二行で示されています。',
    audEyebrow='録音',
    audTitle='一度だけ聞きます',
    audNote='二人の学生 Maya と Ravi '
            'が、指導教員と研究プロジェクトについて話し合います。三つの声です。まず次のスライドの問題を読み、それから再生を押してください。ここでも、問題スライドの下部のバーでも押せます。解答中も録音は流れ続け、聞けるのは一度だけです。',
    topicEyebrow='問題 1 &middot; プロジェクト',
    topicHint='最初の数秒で示されます。誰かが何かに反対する前です。',
    mcaEyebrow='問題 2 &middot; 方法',
    mcbEyebrow='問題 7 &middot; 締め切り',
    whoEyebrow='問題 3–6 &middot; この意見を持つのは誰？',
    whoTitle='それぞれの立場を、最終的にそれを持つ人物と結びつけましょう',
    whoHint='立場をクリックし、次に人物をクリックします。重要なのは各話者が最後にどこに着くかで、どこから始めたかではありません。',
    notesEyebrow='問題 8–10 &middot; 指導のメモ',
    notesTitle='各空所に一語および／または数字一つを書きなさい',
    notesHint='三つの数字はすべて声に出して合意されます。そのうち一つは長く議論されたあと、そのまま維持されます。',
    t2Eyebrow='録音のあとで',
    t2Title='討論が答えを隠す三つのやり方',
    t2ah='同意ではない同意',
    t2ab='Ravi は <em>exactly</em> と言い、そのあとで Maya '
         'が言っていないことを述べます。彼女は訂正します：<em>that&rsquo;s not quite what I '
         'meant</em>。同意の言葉は、二人が同意している証拠にはなりません。',
    t2an='その後、指導教員が二人の意味をはっきり区別します。まだ聞いていれば、録音が答えを手渡してくれる場面です。',
    t2bh='共有された用語',
    t2bb='二人の学生はどちらも <em>response rate</em> と言います。Ravi は何人が返答するかを、Maya '
         'はどれだけ早く返答するかを指しています。一つの語句、二つの意味、二人の人物に結びついた二つの異なる答えです。',
    t2bn='ある語句を二人目の話者が繰り返したら、同じ意味で使っているか確かめましょう。',
    t2ch='議論を生き残る数字',
    t2cb='六十は疑問視され、擁護され、疑われ、そして維持されます。ある数値について議論したあと、そのまま残す討論は標準的で、議論の長さは数値が変わった合図ではありません。',
    t2cn='変わったのは、その周りの計画です。予備調査と、リマインダーです。',
    mcEyebrow='問題 11–12 &middot; 読み取り',
    mcTitle='討論で何が起きたか？',
    n1why='二人しかいないからです。Ravi '
          'は決定と同じ息でその理由を述べます。指導教員がインタビューを好むのは本当ですが、二人が別の方法を選んだ理由ではありません。',
    n2why='分析の時間を失うからです。指導教員は反対を述べる前に、可能だと認めます。<em>you '
          'could</em>。反対の前の譲歩は同意ではありません。',
    n3why='Harrison の章です。Maya はそれを薄く、すべてアメリカの話だと感じます。Ravi '
          'は枠組みを気に入っています。サンプル数とリマインダーはどちらも不一致ではなく合意で決まります。',
    n4why='枠組みを使い、文脈が異なると述べること。指導教員は弱点を強みに変えます。これは Harrison '
          'を捨てることでも、違いを問題として扱うことでもありません。',
    actTitle='筋を見失わない',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='三人一組で。二人がある決定について議論し（イベントをどこで開くか、予算を何に使うか）、一人がメモを取ります。議論する二人は、それぞれちょうど一度、声に出して考えを変えなければなりません。',
    actSpeak1='議論する人：考えを変えるときにそれを合図しましょう。<em>Actually, no&hellip;</em> または <em>I '
              'was against that at first, but&hellip;</em>',
    actSpeak2='一つの語句をわざと二つの異なる意味で使い、メモを取る人がそれを区別できるか見てみましょう。',
    actSpeak3='メモを取る人：誰がどの意見を持っているかを挙げながらメモを読み返しましょう。帰属を間違えるごとに一点を失います。',
    actWriteKind='Writing · 120–180 語',
    actWriteBrief='三人の会議の議事録を書きましょう。何が提案され、何が決まり、誰が最終的にどの意見を持ったか。一人は立場を変えた人として、一つの提案は断られたものとして記録しなければなりません。',
    actPlaceholder='Suggested: … Decided: … Maya now holds that …',
    g1why='十。Maya の最初の一文にあります。Section 3 の録音は、誰かが何かに反対する前の冒頭数秒でテーマを示します。',
    whoWhy='それぞれの人物は、その人が取る動きとともに名前が挙がります。動きこそが意見を捉える手がかりだからです。指導教員の助言は聞かれたうえで断られます。Maya '
           'は六十を <em>in principle</em> 問題ないと言い、すぐに撤回します。そして "response rate" '
           'は二人の学生が別々のことについて口にし、指導教員があとで区別してくれます："Ravi&rsquo;s talking about '
           'how many; Maya&rsquo;s talking about how quickly."',
    d1why='三日。指導教員がその数字を言い、学生は一度も繰り返しません。ただし指導教員は、最後のまとめで一度繰り返します。',
    d2why='十。Ravi が提案し、Maya が同意します。彼女は最初は反対だったと言いますが、答えは彼女が最終的に落ち着いた場所です。',
    d3why='六十、変更なし。長く疑問視されたあと維持されます。数字について議論しながら変えない討論は、Section 3 の定番の動きです。',
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
