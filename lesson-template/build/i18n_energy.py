# -*- coding: utf-8 -*-
"""Interface strings for Managing Energy Projects (B2), English and German."""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Managing <em>Energy Projects</em>',
    coverSub='Planning, risk, budgets and stakeholders — the language the industry actually runs on',
    chipLevel='B2 · Upper-intermediate', chipFocus='Energy project management',
    chipCount='16 slides',
    jargonEyebrow='The words that carry weight',
    jargonTitle='Five phrases you will hear in every status meeting',
    j1h='behind schedule',
    j1b='Not a pause, and not a renegotiated date. Those are said differently, and the difference matters in a report.',
    j2h='scope of works',
    j2b='<em>Revised upward</em> means more work. It is rarely announced as a schedule or budget change, but it is one.',
    j3h='to flag a risk',
    j3b='Flagging is a written act. If it was only said in a corridor, it was not flagged.',
    j4h='contingency budget',
    j4b='Deliberately not tied to any line item. Spending it on a known cost defeats the point.',
    seqEyebrow='Two sequences worth knowing cold', seqTitle='The lifecycle, and the risk process',
    sq1='Project lifecycle', sq2='Risk management',
    qEyebrow='In the status meeting', qTitle='What does it mean?',
    gapEyebrow='The exact term', gapTitle='Complete the report',
    gapHint='Every word in the bank is used exactly once across the three slides.',
    bankLabel='Word bank:',
    ordEyebrow='Sequence', ordTitle='Put the project lifecycle in order',
    ordHint='Click the steps in the order they happen.',
    actTitle='Run the status meeting', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='One project manager, one client, one finance lead. Fifteen minutes, one agenda.',
    actSpeak1='Report that the project is behind schedule. Do not use the word <em>problem</em>.',
    actSpeak2='The scope has been revised upward. Explain what that does to the budget.',
    actSpeak3='Flag one critical risk, and propose who should own it.',
    actSpeak4='Close by confirming what goes to the steering committee, and by when.',
    actWriteBrief='Write the risk section of a monthly status report: one critical risk, its impact, and the mitigation.',
    actPlaceholder='Risk register — October update',
    resPerfect='Full marks. You could sit in a project review and follow every word of it.',
    resStrong='Strong. The vocabulary is secure — the two sequences are what reward one more pass.',
    resMid='A good base. Go back to the lifecycle slide; feasibility before FEED is the ordering that matters most.',
    resLow='Read the two opening slides again, then run it once more. The terms first, the sequences after.',
)

T['de'] = dict(
    coverTitle='<em>Energieprojekte</em> steuern',
    coverSub='Planung, Risiko, Budget und Beteiligte — die Sprache, mit der die Branche tatsächlich arbeitet',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Projektmanagement im Energiesektor',
    chipCount='16 Folien',
    jargonEyebrow='Die Wörter mit Gewicht',
    jargonTitle='Fünf Wendungen, die in jedem Statusmeeting fallen',
    j1h='behind schedule',
    j1b='Keine Pause und kein neu verhandelter Termin. Beides sagt man anders — und im Bericht macht der Unterschied etwas aus.',
    j2h='scope of works',
    j2b='<em>Revised upward</em> heißt: mehr Arbeit. Es wird selten als Termin- oder Budgetänderung angekündigt, ist aber eine.',
    j3h='to flag a risk',
    j3b='Flaggen ist ein schriftlicher Akt. Was nur auf dem Flur gesagt wurde, wurde nicht geflaggt.',
    j4h='contingency budget',
    j4b='Bewusst keiner Position zugeordnet. Wer damit bekannte Kosten deckt, hebt den Zweck auf.',
    seqEyebrow='Zwei Abläufe, die sitzen müssen',
    seqTitle='Der Projektlebenszyklus und der Risikoprozess',
    sq1='Projektlebenszyklus', sq2='Risikomanagement',
    qEyebrow='Im Statusmeeting', qTitle='Was bedeutet das?',
    gapEyebrow='Der genaue Begriff', gapTitle='Vervollständigen Sie den Bericht',
    gapHint='Jedes Wort der Liste wird über die drei Folien hinweg genau einmal gebraucht.',
    bankLabel='Wortliste:',
    ordEyebrow='Reihenfolge', ordTitle='Bringen Sie den Projektlebenszyklus in die richtige Reihenfolge',
    ordHint='Klicken Sie die Schritte in der Reihenfolge an, in der sie stattfinden.',
    actTitle='Leiten Sie das Statusmeeting', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Eine Projektleitung, eine Kundenseite, eine Finanzleitung. Fünfzehn Minuten, eine Tagesordnung.',
    actSpeak1='Melden Sie, dass das Projekt in Verzug ist. Ohne das Wort <em>problem</em> zu benutzen.',
    actSpeak2='Der Leistungsumfang wurde erweitert. Erklären Sie, was das für das Budget bedeutet.',
    actSpeak3='Flaggen Sie ein kritisches Risiko und schlagen Sie vor, wer es verantworten sollte.',
    actSpeak4='Schließen Sie, indem Sie festhalten, was wann an den Lenkungsausschuss geht.',
    actWriteBrief='Schreiben Sie den Risikoabschnitt eines Monatsberichts: ein kritisches Risiko, seine Auswirkung, die Gegenmaßnahme.',
    actPlaceholder='Risk register — October update',
    resPerfect='Volle Punktzahl. Sie könnten in einem Projektreview sitzen und jedem Wort folgen.',
    resStrong='Stark. Der Wortschatz sitzt — die beiden Abläufe lohnen noch einen Durchgang.',
    resMid='Eine gute Grundlage. Zurück zur Lebenszyklus-Folie: Machbarkeit vor FEED ist die Reihenfolge, auf die es ankommt.',
    resLow='Lesen Sie die beiden Einstiegsfolien noch einmal und starten Sie neu. Erst die Begriffe, dann die Abläufe.',
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
