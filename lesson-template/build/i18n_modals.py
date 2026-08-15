# -*- coding: utf-8 -*-
"""Interface strings for Modal Verbs (B1), English and German.

The instructions translate; the English being taught does not. The modals
themselves, the ski sentences, the word bank and the chunks all stay in
English on every setting. The other eight languages ship empty so they stay
out of the menu rather than half-filling the interface.
"""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Modal <em>Verbs</em>',
    coverSub='can · could · must · should · might · will · would — learned on a mountain',
    chipLevel='B1 · Grammar', chipFocus='Modal verbs', chipCount='20 slides',
    mEyebrow='What each one does', mTitle='Seven modals, four jobs',
    m1h='Ability',
    m1b='“She <em>can</em> ski black runs.” “When she was younger she <em>could</em> ski perfectly.”',
    m2h='Obligation &amp; advice',
    m2b='<em>Must not</em> is forbidden. <em>Should not</em> is only a bad idea. The gap between them is the whole point.',
    m3h='Certainty',
    m3b='“You <em>will</em> improve.” “The lift <em>might not</em> open.”',
    m4h='Politeness',
    m4b='These two carry almost every polite request you will ever need to make.',
    fEyebrow='The form — it never changes', fTitle='Modal, then the bare verb. Always.',
    f1h='Statement',
    f1b='Never <em>to check</em>, never <em>checking</em>. The modal takes the plain verb.',
    f2h='Negative &amp; question',
    f2b='Negative: modal + <em>not</em> + verb. Question: the modal jumps to the front. No <em>do</em>, ever.',
    f3h='Talking about the past',
    f3b='Modal + <em>have</em> + past participle. <em>Might leave</em> and <em>should book</em> point at the future instead.',
    qEyebrow='On the mountain', qTitle='Choose the modal',
    gapEyebrow='Which modal', gapTitle='Complete the sentence',
    gapHint='Some answers are two words. Type them exactly as they appear in the bank.',
    bankLabel='Word bank:',
    fixEyebrow='One modal is wrong', fixTitle='Repair the sentence',
    fixHint='The crossed-out modal is wrong. Type the form that belongs there.',
    ordEyebrow='Word order', ordTitle='Build the sentence',
    ordHint='Click the chunks in the right order.',
    actTitle='Use all seven', actUse='Use at least four:',
    actWriteKind='Writing · 80–120 words',
    actSpeakBrief='One of you works at the ski school. The other has never skied.',
    actSpeak1='Give three pieces of advice, and one absolute rule. Make the difference audible.',
    actSpeak2='Ask politely for three things: a lesson, boots in your size, and the forecast.',
    actSpeak3='Something went wrong yesterday. Say what you should have done differently.',
    actSpeak4='Speculate about why your friend is late. Use <em>might have</em> twice.',
    actWriteBrief='Write the safety notice for a ski resort. Rules with <em>must</em>, advice with <em>should</em>.',
    actPlaceholder='All skiers must…',
    resPerfect='Full marks. You can hear the difference between a rule, a recommendation and a guess.',
    resStrong='Strong. The present forms are solid — the past ones (<em>should have</em>, <em>might have</em>) reward another pass.',
    resMid='A good base. Go back to the form slide: modal, then the bare verb, and <em>have</em> + participle for the past.',
    resLow='Read the first two slides again, then run it once more. Meaning first, form after.',
)

T['de'] = dict(
    coverTitle='Modal<em>verben</em>',
    coverSub='can · could · must · should · might · will · would — gelernt auf dem Berg',
    chipLevel='B1 · Grammatik', chipFocus='Modalverben', chipCount='20 Folien',
    mEyebrow='Was jedes davon leistet', mTitle='Sieben Modalverben, vier Aufgaben',
    m1h='Fähigkeit',
    m1b='„She <em>can</em> ski black runs.“ „When she was younger she <em>could</em> ski perfectly.“',
    m2h='Pflicht &amp; Rat',
    m2b='<em>Must not</em> heißt verboten. <em>Should not</em> heißt nur: keine gute Idee. Auf diesen Unterschied kommt es an.',
    m3h='Sicherheit',
    m3b='„You <em>will</em> improve.“ „The lift <em>might not</em> open.“',
    m4h='Höflichkeit',
    m4b='Diese beiden tragen fast jede höfliche Bitte, die Sie je formulieren müssen.',
    fEyebrow='Die Form — sie ändert sich nie', fTitle='Modalverb, dann der reine Infinitiv. Immer.',
    f1h='Aussage',
    f1b='Nie <em>to check</em>, nie <em>checking</em>. Nach dem Modalverb steht der reine Infinitiv.',
    f2h='Verneinung &amp; Frage',
    f2b='Verneinung: Modalverb + <em>not</em> + Verb. Frage: Das Modalverb rückt nach vorn. Niemals <em>do</em>.',
    f3h='Über die Vergangenheit sprechen',
    f3b='Modalverb + <em>have</em> + Partizip Perfekt. <em>Might leave</em> und <em>should book</em> zeigen dagegen in die Zukunft.',
    qEyebrow='Auf dem Berg', qTitle='Wählen Sie das Modalverb',
    gapEyebrow='Welches Modalverb', gapTitle='Vervollständigen Sie den Satz',
    gapHint='Manche Antworten bestehen aus zwei Wörtern. Tippen Sie sie genau so wie in der Wortliste.',
    bankLabel='Wortliste:',
    fixEyebrow='Ein Modalverb ist falsch', fixTitle='Reparieren Sie den Satz',
    fixHint='Das durchgestrichene Modalverb ist falsch. Tippen Sie die Form, die dorthin gehört.',
    ordEyebrow='Wortstellung', ordTitle='Bauen Sie den Satz',
    ordHint='Klicken Sie die Bausteine in der richtigen Reihenfolge an.',
    actTitle='Alle sieben verwenden', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 80–120 Wörter',
    actSpeakBrief='Eine Person arbeitet in der Skischule, die andere stand noch nie auf Skiern.',
    actSpeak1='Geben Sie drei Ratschläge und eine absolute Regel. Der Unterschied muss hörbar sein.',
    actSpeak2='Bitten Sie höflich um drei Dinge: eine Stunde, Schuhe in Ihrer Größe und die Wettervorhersage.',
    actSpeak3='Gestern ist etwas schiefgegangen. Sagen Sie, was Sie hätten anders machen sollen.',
    actSpeak4='Spekulieren Sie, warum Ihre Begleitung zu spät kommt. Verwenden Sie zweimal <em>might have</em>.',
    actWriteBrief='Schreiben Sie den Sicherheitshinweis eines Skigebiets. Regeln mit <em>must</em>, Rat mit <em>should</em>.',
    actPlaceholder='All skiers must…',
    resPerfect='Volle Punktzahl. Sie hören den Unterschied zwischen Regel, Empfehlung und Vermutung.',
    resStrong='Stark. Die Gegenwartsformen sitzen — die Vergangenheitsformen (<em>should have</em>, <em>might have</em>) lohnen einen zweiten Durchgang.',
    resMid='Eine gute Grundlage. Zurück zur Formfolie: Modalverb, dann der reine Infinitiv — und <em>have</em> + Partizip für die Vergangenheit.',
    resLow='Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Erst die Bedeutung, dann die Form.',
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
