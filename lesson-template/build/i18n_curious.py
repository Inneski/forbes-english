# -*- coding: utf-8 -*-
"""Interface strings for Conditionals in The Curious Incident, English and German."""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Conditionals in <em>The Curious Incident</em>',
    coverSub='Four conditional types, learned through the logic of Christopher Boone',
    chipLevel='B2 · Grammar in literature', chipFocus='Conditionals', chipCount='15 slides',
    condEyebrow='The four types, side by side',
    condTitle='What each conditional is actually claiming',
    c0h='Zero — always true',
    c0b='“If you heat water to 100°C, it boils.” No exceptions. Christopher’s favourite kind of sentence.',
    c1h='First — likely',
    c1b='“Unless he follows his routine, he <em>will</em> become distressed.” A real future.',
    c2h='Second — imagined',
    c2b='“If he <em>were</em> better at reading faces, it would be simpler.” Not true now, and unlikely.',
    c3h='Third — unreal past',
    c3b='“If he <em>hadn’t</em> found Wellington…” It did happen. This imagines the version where it did not.',
    connEyebrow='Everything else that starts a condition',
    connTitle='Four connectors and two inversions',
    n1h='unless',
    n1b='“<em>Unless</em> he follows his routine…” Never <em>will</em> or <em>would</em> after it.',
    n2h='provided that / as long as',
    n2b='“…<em>provided that</em> nobody interferes with his methods.” Present tense, always.',
    n3h='Were you to…',
    n3b='= <em>If you were to…</em> Slightly literary; Siobhan speaks like this, Christopher does not.',
    n4h='Had he…',
    n4b='“<em>Had</em> his father been honest earlier…” = <em>If his father had been honest…</em>',
    qEyebrow='Christopher’s logic', qTitle='Which conditional?',
    gapEyebrow='The exact form', gapTitle='Complete the conditional',
    gapHint='Five of the ten items in the bank belong to no gap here.',
    bankLabel='Word bank:',
    matchEyebrow='Two halves of one thought', matchTitle='Match the opening to its ending',
    matchHint='Click an opening, then click the ending that fits it.',
    actTitle='Imagine it otherwise', actUse='Use at least four:',
    actWriteKind='Writing · 150–200 words',
    actSpeakBrief='Christopher’s story turns on things people did and did not say. Argue about them.',
    actSpeak1='If Christopher had never found Wellington, what would the novel have been? Two versions each.',
    actSpeak2='Was the father right to lie? Answer with <em>if he hadn’t</em>, not with <em>yes</em> or <em>no</em>.',
    actSpeak3='Give Christopher three rules for a situation he finds hard, using <em>unless</em> and <em>as long as</em>.',
    actSpeak4='Take one regret of your own and say it twice: third conditional, then mixed.',
    actWriteBrief='Write the chapter Christopher would have written if his father had told him the truth on the first day.',
    actPlaceholder='If Father had told me the truth that evening,',
    resPerfect='Full marks — Christopher would approve of the precision. All four types, plus both inversions.',
    resStrong='Strong. The first three are secure; the third conditional and the inversions are what reward another pass.',
    resMid='A good base. Look again at the four-type slide, especially second versus third — that is where the misses cluster.',
    resLow='Read the two opening slides again, then run it once more. Decide the time frame first, then the form.',
)

T['de'] = dict(
    coverTitle='Bedingungssätze in <em>The Curious Incident</em>',
    coverSub='Vier Typen von Bedingungssätzen, gelernt an der Logik von Christopher Boone',
    chipLevel='B2 · Grammatik in der Literatur', chipFocus='Bedingungssätze', chipCount='15 Folien',
    condEyebrow='Die vier Typen nebeneinander',
    condTitle='Was jeder Bedingungssatz eigentlich behauptet',
    c0h='Typ 0 — immer wahr',
    c0b='„If you heat water to 100°C, it boils.“ Ohne Ausnahme. Christophers Lieblingssatzart.',
    c1h='Typ I — wahrscheinlich',
    c1b='„Unless he follows his routine, he <em>will</em> become distressed.“ Eine reale Zukunft.',
    c2h='Typ II — vorgestellt',
    c2b='„If he <em>were</em> better at reading faces, it would be simpler.“ Jetzt nicht der Fall, und unwahrscheinlich.',
    c3h='Typ III — irreale Vergangenheit',
    c3b='„If he <em>hadn’t</em> found Wellington…“ Es ist passiert. Hier wird die Version gedacht, in der es nicht passierte.',
    connEyebrow='Alles andere, was eine Bedingung einleitet',
    connTitle='Vier Konnektoren und zwei Inversionen',
    n1h='unless',
    n1b='„<em>Unless</em> he follows his routine…“ Danach niemals <em>will</em> oder <em>would</em>.',
    n2h='provided that / as long as',
    n2b='„…<em>provided that</em> nobody interferes with his methods.“ Immer Präsens.',
    n3h='Were you to…',
    n3b='= <em>If you were to…</em> Etwas literarisch; Siobhan spricht so, Christopher nicht.',
    n4h='Had he…',
    n4b='„<em>Had</em> his father been honest earlier…“ = <em>If his father had been honest…</em>',
    qEyebrow='Christophers Logik', qTitle='Welcher Bedingungssatz?',
    gapEyebrow='Die genaue Form', gapTitle='Vervollständigen Sie den Bedingungssatz',
    gapHint='Fünf der zehn Einträge in der Liste gehören in keine dieser Lücken.',
    bankLabel='Wortliste:',
    matchEyebrow='Zwei Hälften eines Gedankens', matchTitle='Ordnen Sie den Anfang seinem Ende zu',
    matchHint='Klicken Sie auf einen Anfang und dann auf das passende Ende.',
    actTitle='Stellen Sie es sich anders vor', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 150–200 Wörter',
    actSpeakBrief='Christophers Geschichte hängt daran, was Menschen sagten und was nicht. Streiten Sie darüber.',
    actSpeak1='Wenn Christopher Wellington nie gefunden hätte — was wäre der Roman geworden? Zwei Fassungen pro Person.',
    actSpeak2='Hatte der Vater recht zu lügen? Antworten Sie mit <em>if he hadn’t</em>, nicht mit <em>yes</em> oder <em>no</em>.',
    actSpeak3='Geben Sie Christopher drei Regeln für eine schwierige Situation — mit <em>unless</em> und <em>as long as</em>.',
    actSpeak4='Nehmen Sie ein eigenes Bedauern und sagen Sie es zweimal: Typ III, dann gemischt.',
    actWriteBrief='Schreiben Sie das Kapitel, das Christopher geschrieben hätte, wenn sein Vater ihm am ersten Tag die Wahrheit gesagt hätte.',
    actPlaceholder='If Father had told me the truth that evening,',
    resPerfect='Volle Punktzahl — Christopher würde die Präzision gutheißen. Alle vier Typen, dazu beide Inversionen.',
    resStrong='Stark. Die ersten drei sitzen; Typ III und die Inversionen lohnen einen zweiten Durchgang.',
    resMid='Eine gute Grundlage. Sehen Sie sich die Vier-Typen-Folie noch einmal an, vor allem Typ II gegen Typ III.',
    resLow='Lesen Sie die beiden Einstiegsfolien noch einmal und starten Sie neu. Erst den Zeithorizont, dann die Form.',
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
