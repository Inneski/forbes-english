# -*- coding: utf-8 -*-
"""Interface strings for the open-answer practice deck, English and German.

Only the chrome and the instructions translate. The eight scenarios, the tasks
and the model answers stay in English on every setting — producing English is
the entire exercise.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Say it in <em>your own words</em>',
    coverSub='Eight situations, no options to choose from — write the answer, then read one that works',
    chipLevel='B2 · Open practice', chipFocus='Meetings, calls &amp; email',
    chipCount='13 slides',
    howEyebrow='How to use this', howTitle='Write first. The model answer is not the point.',
    h1h='1 · Write it',
    h1b='Reading a good answer teaches you almost nothing. Producing a bad one and then reading a good one teaches you a great deal.',
    h2h='2 · Compare the moves',
    h2b='The model answers are one version, not the version. Yours may be better; check that it does the same jobs.',
    h3h='3 · Say it again',
    h3b='One phrase per scenario is a realistic rate. Eight new phrases from one lesson is not.',
    movesEyebrow='What nearly every answer needs',
    movesTitle='Acknowledge, be specific, offer something',
    m1h='Acknowledge',
    m1b='Conceding what is true costs nothing and buys you the right to say the rest.',
    m2h='Be specific',
    m2b='A date or a number turns a soft statement into something the other person can act on.',
    m3h='Offer something',
    m3b='Bad news, a refusal and a request all need a second half. Without one you have only made a statement.',
    sEyebrow='Situation', sCtx='The situation', sTask='Your task',
    sModel='One way to say it — read after you have written',
    actTitle='Run three of them live', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='Pick three scenarios. Your partner plays the other side and does not make it easy.',
    actSpeak1='Cold call: your partner tries to end the call inside fifteen seconds.',
    actSpeak2='Bad news: your partner asks twice who is at fault. Answer once, then move on.',
    actSpeak3='Complaint: your partner is not satisfied by your first reply. Do not repeat yourself.',
    actSpeak4='Close: your partner says “let me think about it.” Find out what is actually in the way.',
    actWriteBrief='Pick the scenario you found hardest and write it properly. Then rewrite it in half the words.',
    actPlaceholder='Dear Ms Chen,',
    resPerfect='', resStrong='', resMid='', resLow='',
)

T['de'] = dict(
    coverTitle='Sagen Sie es <em>in eigenen Worten</em>',
    coverSub='Acht Situationen, keine Auswahlmöglichkeiten — schreiben Sie die Antwort, lesen Sie dann eine, die funktioniert',
    chipLevel='B2 · Freies Üben', chipFocus='Meetings, Anrufe &amp; E-Mail',
    chipCount='13 Folien',
    howEyebrow='So arbeiten Sie damit',
    howTitle='Erst schreiben. Die Musterantwort ist nicht der Punkt.',
    h1h='1 · Schreiben Sie',
    h1b='Eine gute Antwort zu lesen bringt fast nichts. Eine schlechte zu produzieren und danach eine gute zu lesen bringt sehr viel.',
    h2h='2 · Vergleichen Sie die Schritte',
    h2b='Die Musterantworten sind eine Fassung, nicht die Fassung. Ihre kann besser sein; prüfen Sie nur, ob sie dieselben Aufgaben erfüllt.',
    h3h='3 · Sagen Sie es noch einmal',
    h3b='Eine Wendung pro Situation ist ein realistisches Tempo. Acht neue Wendungen aus einer Lektion sind es nicht.',
    movesEyebrow='Was fast jede Antwort braucht',
    movesTitle='Bestätigen, konkret werden, etwas anbieten',
    m1h='Bestätigen',
    m1b='Zuzugeben, was stimmt, kostet nichts und verschafft Ihnen das Recht, den Rest zu sagen.',
    m2h='Konkret werden',
    m2b='Ein Datum oder eine Zahl macht aus einer vagen Aussage etwas, womit das Gegenüber arbeiten kann.',
    m3h='Etwas anbieten',
    m3b='Schlechte Nachrichten, Absagen und Bitten brauchen alle eine zweite Hälfte. Ohne sie haben Sie nur etwas festgestellt.',
    sEyebrow='Situation', sCtx='Die Situation', sTask='Ihre Aufgabe',
    sModel='Eine mögliche Formulierung — erst lesen, wenn Sie geschrieben haben',
    actTitle='Spielen Sie drei davon durch', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Wählen Sie drei Situationen. Ihr Gegenüber spielt die andere Seite und macht es Ihnen nicht leicht.',
    actSpeak1='Kaltakquise: Ihr Gegenüber versucht, das Gespräch in fünfzehn Sekunden zu beenden.',
    actSpeak2='Schlechte Nachricht: Ihr Gegenüber fragt zweimal nach der Schuld. Antworten Sie einmal und gehen Sie weiter.',
    actSpeak3='Beschwerde: Ihre erste Antwort genügt dem Gegenüber nicht. Wiederholen Sie sich nicht.',
    actSpeak4='Abschluss: Ihr Gegenüber sagt „let me think about it.“ Finden Sie heraus, was wirklich im Weg steht.',
    actWriteBrief='Nehmen Sie die schwierigste Situation und schreiben Sie sie sauber aus. Dann noch einmal in der Hälfte der Wörter.',
    actPlaceholder='Dear Ms Chen,',
    resPerfect='', resStrong='', resMid='', resLow='',
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
