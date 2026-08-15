# -*- coding: utf-8 -*-
"""Interface strings for The Docket (B2), English and German."""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='The <em>Docket</em>',
    coverSub='Crime, the courtroom and the office — the vocabulary a true-crime series runs on',
    chipLevel='B2 · Vocabulary', chipFocus='Law &amp; the courtroom', chipCount='21 slides',
    vEyebrow='Before the case opens', vTitle='Six words the courtroom cannot do without',
    v1h='defraud · fraudulent',
    v1b='The verb takes a person as its object: you defraud <em>somebody</em> <em>out of</em> something.',
    v2h='inadmissible',
    v2b='Ruled case by case, not automatic. Improperly obtained evidence is <em>sometimes</em> excluded — never always.',
    v3h='revoke · mandatory',
    v3b='Watch what <em>mandatory</em> attaches to: a duty, a check, a disclosure. Never an offence.',
    v4h='grievance · offender',
    v4b='A grievance is raised, heard and either upheld or dismissed. It is the word both HR and the tribunal use.',
    pairEyebrow='The pair everyone gets wrong',
    pairTitle='prevalent, rampant, and the three reconciles',
    p1h='prevalent',
    p1b='Neutral. A dialect, a practice, a reputation, a species can all be prevalent, and nothing is implied about whether that is good.',
    p2h='rampant',
    p2b='Weeds, inflation, corruption, rumour. If you would not mind it spreading, it is not rampant.',
    p3h='reconcile × 3',
    p3b='Reconcile two <em>people</em>, two <em>views</em> (find where they agree), or one fact <em>with</em> another (make them fit). The third sense is what this case turns on.',
    qEyebrow='Exhibit A', qTitle='The word the record needs',
    gapEyebrow='Witness statement — E. Voss', gapTitle='Complete the testimony',
    gapHint='Nine words in the bank, seven gaps. Two are not needed.',
    bankLabel='Word bank:',
    matchEyebrow='The brief', matchTitle='Six words, precisely',
    matchHint='Click a word, then click its definition.',
    errEyebrow='Cross-examination', errTitle='Find the wrong word',
    actTitle='Take the stand', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='One witness, one counsel, one judge. Counsel may object; the judge rules.',
    actSpeak1='Counsel: establish what the witness saw, without ever asking a yes/no question.',
    actSpeak2='Witness: describe a practice as <em>prevalent</em>, then describe a different one as <em>rampant</em>. Justify both.',
    actSpeak3='Judge: rule one piece of evidence inadmissible, and say why in one sentence.',
    actSpeak4='All three: agree what the grievance actually was, in twelve words or fewer.',
    actWriteBrief='Write the witness statement for something you have actually seen go wrong at work. Formal register throughout — no <em>people person</em>.',
    actPlaceholder='My name is … At the time of the events, I was working as …',
    resPerfect='Acquitted on all counts. You can tell prevalent from rampant, which is more than most native speakers manage.',
    resStrong='A strong showing. The core vocabulary is secure — the cross-examination is where the last marks are.',
    resMid='Solid groundwork. Go back to the second teaching slide; prevalent, rampant and reconcile are where the misses cluster.',
    resLow='Read the two opening slides again, then run it once more. The words are precise, and precision is the whole subject here.',
)

T['de'] = dict(
    coverTitle='The <em>Docket</em>',
    coverSub='Verbrechen, Gerichtssaal und Büro — der Wortschatz, von dem eine True-Crime-Serie lebt',
    chipLevel='B2 · Wortschatz', chipFocus='Recht &amp; Gerichtssaal', chipCount='21 Folien',
    vEyebrow='Bevor der Fall aufgerufen wird',
    vTitle='Sechs Wörter, ohne die kein Gerichtssaal auskommt',
    v1h='defraud · fraudulent',
    v1b='Das Verb nimmt eine Person als Objekt: man betrügt <em>jemanden</em> <em>um</em> etwas.',
    v2h='inadmissible',
    v2b='Wird im Einzelfall entschieden, nicht automatisch. Rechtswidrig erlangte Beweise werden <em>manchmal</em> ausgeschlossen — nie immer.',
    v3h='revoke · mandatory',
    v3b='Achten Sie darauf, worauf sich <em>mandatory</em> bezieht: eine Pflicht, eine Prüfung, eine Offenlegung. Niemals auf eine Straftat.',
    v4h='grievance · offender',
    v4b='Eine Beschwerde wird eingereicht, angehört und dann entweder anerkannt oder zurückgewiesen. Sowohl die Personalabteilung als auch das Gericht benutzen dieses Wort.',
    pairEyebrow='Das Paar, das alle verwechseln',
    pairTitle='prevalent, rampant — und die drei reconciles',
    p1h='prevalent',
    p1b='Neutral. Ein Dialekt, eine Praxis, ein Ruf, eine Art können alle „prevalent“ sein, ohne dass damit ein Urteil verbunden wäre.',
    p2h='rampant',
    p2b='Unkraut, Inflation, Korruption, Gerüchte. Wenn es Ihnen nichts ausmachen würde, dass es sich ausbreitet, ist es nicht „rampant“.',
    p3h='reconcile × 3',
    p3b='Man versöhnt zwei <em>Menschen</em>, bringt zwei <em>Positionen</em> zusammen oder bringt eine Tatsache <em>mit</em> einer anderen in Einklang. Um die dritte Bedeutung geht es hier.',
    qEyebrow='Beweisstück A', qTitle='Das Wort, das ins Protokoll gehört',
    gapEyebrow='Zeugenaussage — E. Voss', gapTitle='Vervollständigen Sie die Aussage',
    gapHint='Neun Wörter in der Liste, sieben Lücken. Zwei werden nicht gebraucht.',
    bankLabel='Wortliste:',
    matchEyebrow='Der Schriftsatz', matchTitle='Sechs Wörter, genau genommen',
    matchHint='Klicken Sie auf ein Wort und dann auf seine Definition.',
    errEyebrow='Kreuzverhör', errTitle='Finden Sie das falsche Wort',
    actTitle='In den Zeugenstand', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Eine Person im Zeugenstand, eine als Anwaltschaft, eine als Gericht. Es darf Einspruch erhoben werden; das Gericht entscheidet.',
    actSpeak1='Anwaltschaft: Ermitteln Sie, was die Person gesehen hat — ohne eine einzige Ja/Nein-Frage.',
    actSpeak2='Zeugenstand: Beschreiben Sie eine Praxis als <em>prevalent</em> und eine andere als <em>rampant</em>. Begründen Sie beides.',
    actSpeak3='Gericht: Erklären Sie ein Beweismittel für unzulässig und sagen Sie in einem Satz, warum.',
    actSpeak4='Alle drei: Einigen Sie sich in höchstens zwölf Wörtern darauf, worin die Beschwerde eigentlich bestand.',
    actWriteBrief='Schreiben Sie die Zeugenaussage zu etwas, das Sie tatsächlich bei der Arbeit haben schiefgehen sehen. Durchgehend förmliches Register — kein <em>people person</em>.',
    actPlaceholder='My name is … At the time of the events, I was working as …',
    resPerfect='In allen Punkten freigesprochen. Sie unterscheiden prevalent von rampant — das schaffen die wenigsten Muttersprachler.',
    resStrong='Starke Vorstellung. Der Kernwortschatz sitzt — die letzten Punkte liegen im Kreuzverhör.',
    resMid='Solide Grundlage. Zurück zur zweiten Lehrfolie; bei prevalent, rampant und reconcile häufen sich die Fehler.',
    resLow='Lesen Sie die beiden Einstiegsfolien noch einmal und starten Sie neu. Die Wörter sind präzise — und Präzision ist hier das ganze Thema.',
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
