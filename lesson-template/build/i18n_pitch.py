# -*- coding: utf-8 -*-
"""Interface strings for The Design Pitch, English and German.

The instructions translate; the English being taught does not. The seven
scenarios and their options, the twelve-phrase phrasebook, the gap sentences
and the five pitch moves all stay in English on every setting — they are the
lesson. The other eight languages ship empty, which keeps them out of the menu
rather than half-filling the interface.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='The Design <em>Pitch</em>',
    coverSub='Language, narrative and persuasion — how designers make an idea land',
    chipLevel='B2 · Professional communication', chipFocus='Design &amp; creative pitching',
    chipCount='15 slides',
    narrEyebrow='Before anything else', narrTitle='A pitch is an argument, not a description',
    n1h='1 · The tension',
    n1b='Without a tension there is nothing for the building to resolve, and nothing for you to say.',
    n2h='2 · The decision',
    n2b='Departing from a norm you have not named reads as ignorance. Naming it reads as judgement.',
    n3h='3 · The translation',
    n3b='If a non-specialist cannot repeat your idea back, you have described the drawing, not the concept.',
    phraseEyebrow='The phrasebook', phraseTitle='Twelve phrases, in the three places you need them',
    pcol1='Starting a narrative', pcol2='Describing a concept', pcol3='Responding to feedback',
    qEyebrow='In the room', qTitle='Which one lands?',
    gapEyebrow='The working verbs', gapTitle='The words that do the lifting',
    gapHint='These five words carry most of a design pitch. Type the one that belongs.',
    bankLabel='Word bank:',
    matchEyebrow='What the phrase is doing', matchTitle='Five moves from a real pitch',
    matchHint='Click a phrase, then click what it does.',
    actTitle='Pitch it', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='One designer, two clients. The clients must interrupt at least twice.',
    actSpeak1='Open on the tension your concept resolves. Two sentences, no specification.',
    actSpeak2='A client says it does not fit their brand. Respond without defending the work.',
    actSpeak3='A client cuts the budget by a fifth. Reframe it in front of them.',
    actSpeak4='Close by naming what this is a direction for, not a solution to.',
    actWriteBrief='Write the opening of a pitch for a building you know well. Start from the tension.',
    actPlaceholder='The concept grew out of…',
    resPerfect='Full marks. You can open on an idea, hold a client&rsquo;s objection, and close without closing the door.',
    resStrong='Strong. The structure is there — the phrases for handling feedback are what to rehearse.',
    resMid='A good base. Go back to the three moves: tension, decision, translation. Most misses start at translation.',
    resLow='Read the first two slides again, then run it once more. The narrative first, the vocabulary after.',
)

T['de'] = dict(
    coverTitle='Der Design-<em>Pitch</em>',
    coverSub='Sprache, Erzählung und Überzeugung — wie Gestalter eine Idee ankommen lassen',
    chipLevel='B2 · Berufliche Kommunikation', chipFocus='Design &amp; kreatives Pitchen',
    chipCount='15 Folien',
    narrEyebrow='Zuallererst', narrTitle='Ein Pitch ist ein Argument, keine Beschreibung',
    n1h='1 · Die Spannung',
    n1b='Ohne Spannung gibt es nichts, was das Gebäude auflösen könnte — und nichts zu sagen.',
    n2h='2 · Die Entscheidung',
    n2b='Von einer Norm abzuweichen, die man nicht benannt hat, wirkt ahnungslos. Sie zu benennen wirkt wie ein Urteil.',
    n3h='3 · Die Übersetzung',
    n3b='Wenn ein Laie Ihre Idee nicht wiedergeben kann, haben Sie die Zeichnung beschrieben, nicht das Konzept.',
    phraseEyebrow='Das Phrasenrepertoire',
    phraseTitle='Zwölf Wendungen für die drei Stellen, an denen Sie sie brauchen',
    pcol1='Eine Erzählung eröffnen', pcol2='Ein Konzept beschreiben', pcol3='Auf Feedback reagieren',
    qEyebrow='Im Raum', qTitle='Was kommt an?',
    gapEyebrow='Die tragenden Wörter', gapTitle='Die Wörter, die die Arbeit machen',
    gapHint='Diese fünf Wörter tragen einen Design-Pitch. Tippen Sie das passende ein.',
    bankLabel='Wortliste:',
    matchEyebrow='Was die Wendung leistet', matchTitle='Fünf Züge aus einem echten Pitch',
    matchHint='Klicken Sie auf eine Wendung und dann auf ihre Funktion.',
    actTitle='Pitchen Sie', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Eine Person gestaltet, zwei sind Kundschaft. Die Kundschaft unterbricht mindestens zweimal.',
    actSpeak1='Eröffnen Sie mit der Spannung, die Ihr Konzept auflöst. Zwei Sätze, keine Spezifikation.',
    actSpeak2='Die Kundschaft sagt, es passe nicht zur Marke. Antworten Sie, ohne die Arbeit zu verteidigen.',
    actSpeak3='Das Budget wird um ein Fünftel gekürzt. Deuten Sie das vor Ort um.',
    actSpeak4='Schließen Sie, indem Sie es als Richtung benennen, nicht als fertige Lösung.',
    actWriteBrief='Schreiben Sie den Anfang eines Pitches für ein Gebäude, das Sie gut kennen. Beginnen Sie mit der Spannung.',
    actPlaceholder='The concept grew out of…',
    resPerfect='Volle Punktzahl. Sie eröffnen mit einer Idee, halten einen Einwand aus und schließen, ohne die Tür zuzumachen.',
    resStrong='Stark. Die Struktur sitzt — proben Sie jetzt die Wendungen für den Umgang mit Feedback.',
    resMid='Eine gute Grundlage. Zurück zu den drei Zügen: Spannung, Entscheidung, Übersetzung. Die meisten Fehler beginnen bei der Übersetzung.',
    resLow='Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Erst die Erzählung, dann der Wortschatz.',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
