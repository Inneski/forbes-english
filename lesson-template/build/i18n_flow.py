# -*- coding: utf-8 -*-
"""Interface strings for The Language of Flow (B2), English and German.

The instructions translate; the English being taught does not. The eight terms,
their glosses, the gap sentences, the five questions and their options all stay
in English on every setting — they are the lesson. At B2 the learner can read
an English rubric, but a translated one removes the last excuse for not
attempting the speaking task, which is the part that actually transfers.

The other eight languages ship as empty objects. That is an honest state: the
menu simply does not offer them. A half-filled language appears in the menu and
then falls back to English halfway down the slide, which is worse.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount', 'btnOpen']

T = {}

T['en'] = dict(
    coverTitle='The Language of <em>Flow</em>',
    coverSub='Peak performance, deep focus, and the vocabulary to discuss both',
    chipLevel='B2 · Psychology &amp; productivity', chipFocus='Academic vocabulary',
    chipCount='15 slides',

    shapeEyebrow='Before the vocabulary',
    shapeTitle='Four conditions, and flow is the result',
    s1='Not too easy, not too hard. Boredom sits on one side of that line and anxiety on the other; flow is the narrow band between them.',
    s2='You know what you are aiming at and you can see, moment to moment, whether it is working. Ambiguity is what breaks concentration.',
    s3='The activity is its own reward. Anything you would still do with the payment removed is a candidate.',
    s4='One thing, uninterrupted. Every switch of attention costs more than the seconds it appears to take.',

    vidEyebrow='Part one', vidTitle='Watch this first',
    vidBody='Four and a half minutes on what flow is and how the brain enters it. Watch it through before the vocabulary — the terms below all appear in it.',
    vidNote='Opens YouTube in a new tab.',

    termEyebrow='The eight terms', termTitleA='Four to describe the state',
    termTitleB='Four to describe the conditions',

    matchEyebrow='Say it in plain English', matchTitle='Six terms and what they actually mean',
    matchHint='Click a term, then click its meaning.',

    gapEyebrow='The terms in use', gapTitle='Complete the sentence',
    bankLabel='Word bank:',
    gapHint='One term per gap. Every term in the bank is used exactly once across the two screens.',

    qEyebrow='Comprehension', qTitle='What does the research say?',

    actTitle='Now argue about it', actUse='Use at least four:',
    actSpeakBrief='In pairs or small groups. Take a position and defend it — one prompt each, three minutes apiece.',
    actSpeak1='Describe a time you entered flow. What were the conditions? Use three of the terms.',
    actSpeak2='Notifications are said to be the enemy of flow. Redesign a working day to protect two uninterrupted hours.',
    actSpeak3='<em>Lost in the moment</em> is the informal version. Give three more English expressions for intense concentration.',
    actSpeak4='Struggle and discomfort have value too. To what extent should work feel like flow?',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Take the prompt you did not speak on and answer it in writing. Use at least four of the eight terms.',
    actPlaceholder='The clearest flow state I can remember was…',

    resPerfect='Full marks. The vocabulary is yours — now use it in the speaking task, which is the harder half.',
    resStrong='Strong. Check the ones you missed against the video, then go to the discussion.',
    resMid='A reasonable base. Re-watch the middle of the video; most of the misses cluster there.',
    resLow='Go back through the eight terms before the discussion — the prompts assume them.',
)

T['de'] = dict(
    coverTitle='Die Sprache des <em>Flow</em>',
    coverSub='Höchstleistung, tiefe Konzentration und das Vokabular, um über beides zu sprechen',
    chipLevel='B2 · Psychologie &amp; Produktivität', chipFocus='Akademischer Wortschatz',
    chipCount='15 Folien',

    shapeEyebrow='Vor dem Wortschatz',
    shapeTitle='Vier Bedingungen, und Flow ist das Ergebnis',
    s1='Nicht zu leicht, nicht zu schwer. Auf der einen Seite dieser Linie liegt Langeweile, auf der anderen Angst; Flow ist der schmale Bereich dazwischen.',
    s2='Sie wissen, worauf Sie zielen, und sehen von Moment zu Moment, ob es funktioniert. Unklarheit ist das, was Konzentration zerstört.',
    s3='Die Tätigkeit ist ihre eigene Belohnung. Alles, was Sie auch ohne Bezahlung noch täten, kommt infrage.',
    s4='Eine Sache, ohne Unterbrechung. Jeder Aufmerksamkeitswechsel kostet mehr als die Sekunden, die er zu dauern scheint.',

    vidEyebrow='Teil eins', vidTitle='Zuerst ansehen',
    vidBody='Viereinhalb Minuten darüber, was Flow ist und wie das Gehirn hineinfindet. Sehen Sie das Video ganz an, bevor Sie zum Wortschatz gehen — alle Begriffe kommen darin vor.',
    vidNote='Öffnet YouTube in einem neuen Tab.',

    termEyebrow='Die acht Begriffe', termTitleA='Vier für den Zustand',
    termTitleB='Vier für die Bedingungen',

    matchEyebrow='Auf gut Deutsch gesagt', matchTitle='Sechs Begriffe und was sie wirklich heißen',
    matchHint='Klicken Sie auf einen Begriff und dann auf seine Bedeutung.',

    gapEyebrow='Die Begriffe im Einsatz', gapTitle='Vervollständigen Sie den Satz',
    bankLabel='Wortliste:',
    gapHint='Ein Begriff pro Lücke. Jeder Begriff der Liste wird auf den beiden Folien genau einmal gebraucht.',

    qEyebrow='Verständnis', qTitle='Was sagt die Forschung?',

    actTitle='Jetzt diskutieren Sie', actUse='Mindestens vier verwenden:',
    actSpeakBrief='Zu zweit oder in kleinen Gruppen. Beziehen Sie Position und verteidigen Sie sie — eine Frage pro Person, je drei Minuten.',
    actSpeak1='Beschreiben Sie eine Situation im Flow. Welche Bedingungen lagen vor? Verwenden Sie drei der Begriffe.',
    actSpeak2='Benachrichtigungen gelten als Feind des Flow. Gestalten Sie einen Arbeitstag so um, dass zwei ununterbrochene Stunden geschützt sind.',
    actSpeak3='<em>Lost in the moment</em> ist die umgangssprachliche Variante. Nennen Sie drei weitere englische Wendungen für höchste Konzentration.',
    actSpeak4='Auch Mühe und Unbehagen haben ihren Wert. Inwieweit sollte sich Arbeit wie Flow anfühlen?',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Nehmen Sie die Frage, über die Sie nicht gesprochen haben, und beantworten Sie sie schriftlich. Mindestens vier der acht Begriffe verwenden.',
    actPlaceholder='Der deutlichste Flow-Zustand, an den ich mich erinnere, war…',

    resPerfect='Volle Punktzahl. Der Wortschatz sitzt — jetzt die Sprechaufgabe, das ist die schwerere Hälfte.',
    resStrong='Stark. Prüfen Sie die Fehler noch einmal am Video und gehen Sie dann zur Diskussion.',
    resMid='Eine brauchbare Grundlage. Sehen Sie sich die Mitte des Videos noch einmal an; dort häufen sich die Fehler.',
    resLow='Gehen Sie die acht Begriffe noch einmal durch, bevor Sie diskutieren — die Fragen setzen sie voraus.',
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
