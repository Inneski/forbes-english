# -*- coding: utf-8 -*-
"""Interface strings for Dino-Craft Part 0: The Briefing (C1), English and German.

Teach-card bodies translate (the six-item form) rather than staying English.
House style says the five-item form is usually right at B2 and above, but a
German heading over an English rule reads as a half-finished translation —
which is the thing §8 is trying to prevent. The English being *taught* still
stays English everywhere: the example structures, the question stems, the
options, the word bank and the target-language chips.
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
}

T = {}

T['en'] = dict(
    coverTitle='Dino-Craft <em>Part 0</em>',
    coverSub='The briefing — five activities to place your C1 English before the expedition sets out',
    chipLevel='C1 · Advanced', chipFocus='Placement briefing',
    chipCount='23 slides',

    conEyebrow='Before the questions', conTitle='Stating what the science accepts',
    con1h='The consensus passive',
    con1b='English reports settled findings in the passive and the simple past: '
          '<em>the T. rex was considered an apex predator</em>. The agent is left out '
          'because the point is the finding, not who found it.',
    con1n='Perfect and continuous forms sound like an unfinished process, not a conclusion.',
    con2h='Hedging a claim',
    con2b='Science rarely asserts flatly. <em>Widely believed to have been</em>, '
          '<em>is thought to be</em>, <em>appears to have</em> — the hedge marks how '
          'firmly the field holds the claim.',
    con2n='<em>Believed to have been</em> reports a present belief about the past.',
    con3h='The register carries it',
    con3b='A theory <em>gains traction</em>; a discovery <em>transforms our '
          'understanding</em>; a habitat is <em>disrupted</em>. At C1 the fixed '
          'collocation is the difference between fluent and merely correct.',
    con3n='Every one of these is a set phrase. Change one word and it stops sounding native.',

    cfEyebrow='The unreal past', cfTitle='A past that did not happen',
    cf1h='Third conditional',
    cf1b='An unreal past condition takes an unreal past result: <em>if the asteroid '
         'had not struck, the dinosaurs would have survived</em>. Both halves have to '
         'be in the past.',
    cf1n='A present result (<em>would survive</em>) turns it into a mixed conditional — a different sentence.',
    cf2h='How sure are you?',
    cf2b='Swap the modal to change the confidence: <em>would have</em> (certain), '
         '<em>might</em> or <em>could have</em> (possible), <em>may have</em> '
         '(possible, more formal).',
    cf2n='All of them keep <em>have + past participle</em>. That part does not move.',
    cf3h='Inversion drops the <em>if</em>',
    cf3b='<em>Had the asteroid not struck Earth…</em> is the formal equivalent of '
         '<em>if the asteroid had not struck Earth</em>. Invert the auxiliary and the '
         'subject, and delete <em>if</em>.',
    cf3n='Written register only. It is common in academic prose and rare in speech.',

    ppEyebrow='The trap', ppTitle='Participle clauses, and what goes wrong with them',
    pp1h='What it does',
    pp1b='<em>Having mined the amber block, the player…</em> compresses <em>after the '
         'player had mined</em> into three words. It signals that one action finished '
         'before the next began.',
    pp1n='<em>Having + past participle</em> for a completed action; <em>-ing</em> alone for a simultaneous one.',
    pp2h='The subject rule',
    pp2b='The participle has no subject of its own, so it borrows the subject of the '
         'main clause. Whoever did the first action must be the one doing the second.',
    pp2n='This is the whole rule. Everything below follows from it.',
    pp3h='The dangling participle',
    pp3b='<em>Having mined the amber block, the velociraptor was discovered.</em> The '
         'main clause subject is the velociraptor, so the sentence says the '
         'velociraptor did the mining.',
    pp3n='It is the commonest C1 writing error, and the writer almost never hears it.',

    mcEyebrow='Activity 1 · Multiple choice', mcTitle='Choose the form that fits',
    fibEyebrow='Activity 2 · The exact word', fibTitle='Collocation, register and precision',
    fibHint='Type the word. Several sentences accept more than one answer.',
    dndEyebrow='Activity 3 · Discourse markers', dndTitle='Put the right phrase in the gap',
    dndHint='Three of the eight phrases in the bank belong to no gap here.',
    bankLabel='Word bank:',
    matchEyebrow='Activity 4 · Terminology', matchTitle='The vocabulary the field actually uses',
    matchHint='Click a term, then click what it means.',
    ordEyebrow='Activity 5 · Sentence building', ordTitle='Put the sentence back together',
    ordHint='Click a chunk to place it, click a placed chunk to take it back.',

    actTitle='Brief the expedition', actUse='Use at least four:',
    actSpeakBrief='You are the expedition scientist; your partner is the sceptic who '
                  'wants the evidence. Three minutes each, then swap.',
    actSpeak1='Explain what the feathered fossils found in China changed, and how confident the field is about it.',
    actSpeak2='Argue what might have happened to the dinosaurs if the asteroid had missed. Stay in the unreal past throughout.',
    actSpeak3='Correct a popular misconception about dinosaurs — the size of a velociraptor, or their colour — without saying "that is wrong".',
    actSpeak4='Your partner claims the Pteranodon was a dinosaur. Put them right, politely, in one turn.',
    actWriteKind='Writing · 200–250 words',
    actWriteBrief='Write the briefing note the expedition team reads before it deploys. '
                  'Set out what is established, what is still contested, and what the '
                  'team should not assume. Hedge the claims that deserve hedging.',
    actPlaceholder='It is now widely accepted that…',

    resPerfect='Full marks. The consensus passive, the unreal past and the participle rule are all secure — go straight to Part I.',
    resStrong='Strong. Part I will suit you. Glance back at whichever activity cost you the points before you start it.',
    resMid='A solid C1 base with gaps. Re-read the three opening slides, then run the briefing again before Part I.',
    resLow='Work through the three teaching slides properly, then come back. The expedition assumes all three structures.',
)

T['de'] = dict(
    coverTitle='Dino-Craft <em>Teil 0</em>',
    coverSub='Das Briefing — fünf Aufgaben, die dein C1-Englisch einordnen, bevor die Expedition startet',
    chipLevel='C1 · Fortgeschritten', chipFocus='Einstufungs-Briefing',
    chipCount='23 Folien',

    conEyebrow='Vor den Fragen', conTitle='Wie man ausdrückt, was die Wissenschaft anerkennt',
    con1h='Das Konsens-Passiv',
    con1b='Gesicherte Erkenntnisse stehen im Englischen im Passiv und im Simple Past: '
          '<em>the T. rex was considered an apex predator</em>. Der Urheber entfällt, '
          'weil es um den Befund geht, nicht um den Finder.',
    con1n='Perfekt- und Verlaufsformen klingen nach unabgeschlossenem Prozess, nicht nach Ergebnis.',
    con2h='Eine Aussage abschwächen',
    con2b='Wissenschaft behauptet selten kategorisch. <em>Widely believed to have '
          'been</em>, <em>is thought to be</em>, <em>appears to have</em> — die '
          'Abschwächung zeigt, wie fest die Fachwelt die Aussage vertritt.',
    con2n='<em>Believed to have been</em> berichtet eine heutige Annahme über die Vergangenheit.',
    con3h='Das Register trägt es',
    con3b='Eine Theorie <em>gains traction</em>; eine Entdeckung <em>transforms our '
          'understanding</em>; ein Lebensraum wird <em>disrupted</em>. Auf C1 macht '
          'die feste Kollokation den Unterschied zwischen flüssig und bloß richtig.',
    con3n='Alles feste Wendungen. Ein Wort ausgetauscht, und es klingt nicht mehr muttersprachlich.',

    cfEyebrow='Die irreale Vergangenheit', cfTitle='Eine Vergangenheit, die nicht stattfand',
    cf1h='Conditional III',
    cf1b='Eine irreale Bedingung in der Vergangenheit verlangt eine irreale Folge in '
         'der Vergangenheit: <em>if the asteroid had not struck, the dinosaurs would '
         'have survived</em>. Beide Hälften stehen in der Vergangenheit.',
    cf1n='Eine Gegenwartsfolge (<em>would survive</em>) macht daraus ein Mixed Conditional — ein anderer Satz.',
    cf2h='Wie sicher bist du?',
    cf2b='Das Modalverb steuert die Sicherheit: <em>would have</em> (sicher), '
         '<em>might</em> oder <em>could have</em> (möglich), <em>may have</em> '
         '(möglich, förmlicher).',
    cf2n='Alle behalten <em>have + past participle</em>. Dieser Teil bleibt.',
    cf3h='Inversion ersetzt das <em>if</em>',
    cf3b='<em>Had the asteroid not struck Earth…</em> ist die förmliche Variante von '
         '<em>if the asteroid had not struck Earth</em>. Hilfsverb und Subjekt tauschen, '
         '<em>if</em> entfällt.',
    cf3n='Nur Schriftsprache. In akademischen Texten häufig, gesprochen selten.',

    ppEyebrow='Die Falle', ppTitle='Partizipialsätze — und was dabei schiefgeht',
    pp1h='Was er leistet',
    pp1b='<em>Having mined the amber block, the player…</em> verdichtet <em>after the '
         'player had mined</em> auf drei Wörter. Es zeigt an, dass eine Handlung vor '
         'der nächsten abgeschlossen war.',
    pp1n='<em>Having + past participle</em> für Abgeschlossenes, bloßes <em>-ing</em> für Gleichzeitiges.',
    pp2h='Die Subjektregel',
    pp2b='Der Partizipialsatz hat kein eigenes Subjekt und leiht sich das des '
         'Hauptsatzes. Wer die erste Handlung ausführt, muss auch die zweite ausführen.',
    pp2n='Das ist die ganze Regel. Alles Weitere folgt daraus.',
    pp3h='Das hängende Partizip',
    pp3b='<em>Having mined the amber block, the velociraptor was discovered.</em> '
         'Subjekt des Hauptsatzes ist der Velociraptor — der Satz behauptet also, '
         'der Velociraptor habe gegraben.',
    pp3n='Der häufigste C1-Schreibfehler, und der Schreibende hört ihn fast nie.',

    mcEyebrow='Aufgabe 1 · Multiple Choice', mcTitle='Wähle die passende Form',
    fibEyebrow='Aufgabe 2 · Das genaue Wort', fibTitle='Kollokation, Register und Präzision',
    fibHint='Tippe das Wort. Mehrere Sätze akzeptieren mehr als eine Antwort.',
    dndEyebrow='Aufgabe 3 · Konnektoren', dndTitle='Setze die passende Wendung in die Lücke',
    dndHint='Drei der acht Wendungen im Wortspeicher gehören in keine Lücke.',
    bankLabel='Wortspeicher:',
    matchEyebrow='Aufgabe 4 · Fachbegriffe', matchTitle='Das Vokabular, das die Fachwelt benutzt',
    matchHint='Klicke einen Begriff an, dann seine Bedeutung.',
    ordEyebrow='Aufgabe 5 · Satzbau', ordTitle='Setze den Satz wieder zusammen',
    ordHint='Klicke einen Baustein, um ihn zu setzen; klicke einen gesetzten an, um ihn zurückzunehmen.',

    actTitle='Briefe die Expedition', actUse='Benutze mindestens vier:',
    actSpeakBrief='Du bist der Expeditionswissenschaftler, dein Partner der Skeptiker, '
                  'der Belege will. Je drei Minuten, dann tauschen.',
    actSpeak1='Erkläre, was die gefiederten Fossilien aus China verändert haben — und wie sicher sich die Fachwelt dabei ist.',
    actSpeak2='Argumentiere, was mit den Dinosauriern hätte geschehen können, wenn der Asteroid vorbeigeflogen wäre. Bleib durchgehend in der irrealen Vergangenheit.',
    actSpeak3='Korrigiere einen verbreiteten Irrtum über Dinosaurier — die Größe eines Velociraptors oder ihre Farbe — ohne „das ist falsch“ zu sagen.',
    actSpeak4='Dein Partner behauptet, der Pteranodon sei ein Dinosaurier gewesen. Stell das höflich richtig, in einem Zug.',
    actWriteKind='Schreiben · 200–250 Wörter',
    actWriteBrief='Schreibe die Briefing-Notiz, die das Expeditionsteam vor dem Einsatz '
                  'liest. Halte fest, was gesichert ist, was noch strittig ist und was '
                  'das Team nicht voraussetzen darf. Schwäche ab, wo es angebracht ist.',
    actPlaceholder='It is now widely accepted that…',

    resPerfect='Volle Punktzahl. Konsens-Passiv, irreale Vergangenheit und Partizipialregel sitzen — geh direkt zu Teil I.',
    resStrong='Stark. Teil I passt zu dir. Sieh dir vorher noch einmal die Aufgabe an, die dich Punkte gekostet hat.',
    resMid='Solide C1-Grundlage mit Lücken. Lies die drei Einstiegsfolien noch einmal und wiederhole das Briefing vor Teil I.',
    resLow='Arbeite die drei Lehrfolien gründlich durch und komm dann zurück. Die Expedition setzt alle drei Strukturen voraus.',
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
