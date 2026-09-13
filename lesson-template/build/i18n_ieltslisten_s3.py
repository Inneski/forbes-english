# -*- coding: utf-8 -*-
"""Interface strings for IELTS Listening Section 3.

English, German and Spanish, teach cards in the six-item form.

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
         '&middot; <em>but you are right</em>. Every one of them says a '
         'position just changed.',
    t1ch='Suggested is not decided',
    t1cb='A tutor proposes things the students do not do. Both go in the '
         'recording and only one is the answer, so a question about the '
         '<em>plan</em> is answered by the students and a question about the '
         '<em>advice</em> by the tutor.',
    t1cn='<em>I would still push you towards&hellip; Fair enough, your '
         'decision.</em> That is a suggestion being declined, in two lines.',

    audEyebrow='The recording',
    audTitle='You will hear it once',
    audNote='Two students, Maya and Ravi, discussing a research project with '
            'their tutor. Three voices. Press play when you are ready. No '
            'pause and no rewind, exactly as in the test.',

    whoEyebrow='Questions 1&ndash;5 &middot; Who holds this view?',
    whoTitle='Match each position to the person who ends up holding it',
    whoHint='Click a position, then a person. What counts is where each '
            'speaker finishes, not where they started.',

    notesEyebrow='Questions 6&ndash;8 &middot; The tutorial notes',
    notesTitle='Write ONE WORD AND/OR A NUMBER in each gap',
    notesHint='All three numbers are agreed out loud. One of them is argued '
              'about at length and then kept unchanged.',

    t2Eyebrow='After the recording',
    t2Title='Three ways a discussion hides the answer',
    t2ah='The agreement that is not one',
    t2ab='Ravi says <em>exactly</em> &mdash; and then states something Maya '
         'did not say. She corrects him: <em>that is not quite what I '
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

    mcEyebrow='Questions 9&ndash;12 &middot; Following the thread',
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
         '&middot; <em>but you are right</em>. Jedes davon meldet einen '
         'Positionswechsel.',
    t1ch='Vorgeschlagen ist nicht beschlossen',
    t1cb='Ein Tutor schlägt Dinge vor, die die Studierenden nicht tun. Beides '
         'steht in der Aufnahme und nur eines ist die Antwort: eine Frage nach '
         'dem <em>Plan</em> beantworten die Studierenden, eine nach dem '
         '<em>Rat</em> der Tutor.',
    t1cn='<em>I would still push you towards&hellip; Fair enough, your '
         'decision.</em> Ein abgelehnter Vorschlag, in zwei Zeilen.',

    audEyebrow='Die Aufnahme',
    audTitle='Du hörst sie einmal',
    audNote='Zwei Studierende, Maya und Ravi, besprechen ein Forschungsprojekt '
            'mit ihrem Tutor. Drei Stimmen. Drücke Play, wenn du bereit bist. '
            'Kein Pausieren, kein Zurückspulen &mdash; wie in der Prüfung.',

    whoEyebrow='Fragen 1&ndash;5 &middot; Wer vertritt das?',
    whoTitle='Ordne jede Position der Person zu, die sie am Ende vertritt',
    whoHint='Klicke eine Position an, dann eine Person. Es zählt, wo jemand '
            'endet, nicht wo er angefangen hat.',

    notesEyebrow='Fragen 6&ndash;8 &middot; Die Besprechungsnotizen',
    notesTitle='Schreibe EIN WORT UND/ODER EINE ZAHL in jede Lücke',
    notesHint='Alle drei Zahlen werden laut vereinbart. Über eine wird lange '
              'gestritten &mdash; und sie bleibt unverändert.',

    t2Eyebrow='Nach der Aufnahme',
    t2Title='Drei Arten, wie eine Diskussion die Antwort versteckt',
    t2ah='Die Zustimmung, die keine ist',
    t2ab='Ravi sagt <em>exactly</em> &mdash; und sagt dann etwas, das Maya gar '
         'nicht gesagt hat. Sie korrigiert ihn: <em>that is not quite what I '
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

    mcEyebrow='Fragen 9&ndash;12 &middot; Dem Faden folgen',
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
         '&middot; <em>but you are right</em>. Cada uno avisa de un cambio de '
         'postura.',
    t1ch='Sugerido no es decidido',
    t1cb='Un tutor propone cosas que los estudiantes no hacen. Las dos están '
         'en la grabación y solo una es la respuesta: una pregunta sobre el '
         '<em>plan</em> la contestan los estudiantes y una sobre el '
         '<em>consejo</em>, el tutor.',
    t1cn='<em>I would still push you towards&hellip; Fair enough, your '
         'decision.</em> Una sugerencia rechazada, en dos líneas.',

    audEyebrow='La grabación',
    audTitle='La oirás una vez',
    audNote='Dos estudiantes, Maya y Ravi, hablan de un proyecto de '
            'investigación con su tutor. Tres voces. Dale a reproducir cuando '
            'estés listo. Sin pausa y sin rebobinar, igual que en el examen.',

    whoEyebrow='Preguntas 1&ndash;5 &middot; ¿De quién es esta postura?',
    whoTitle='Empareja cada postura con quien acaba sosteniéndola',
    whoHint='Haz clic en una postura y luego en una persona. Cuenta dónde '
            'acaba cada uno, no dónde empezó.',

    notesEyebrow='Preguntas 6&ndash;8 &middot; Las notas de la tutoría',
    notesTitle='Escribe UNA PALABRA Y/O UN NÚMERO en cada hueco',
    notesHint='Los tres números se acuerdan en voz alta. Sobre uno se discute '
              'largo y tendido y se queda igual.',

    t2Eyebrow='Después de la grabación',
    t2Title='Tres maneras en que un debate esconde la respuesta',
    t2ah='El acuerdo que no lo es',
    t2ab='Ravi dice <em>exactly</em> y acto seguido dice algo que Maya no ha '
         'dicho. Ella le corrige: <em>that is not quite what I meant</em>. Las '
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

    mcEyebrow='Preguntas 9&ndash;12 &middot; Seguir el hilo',
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
