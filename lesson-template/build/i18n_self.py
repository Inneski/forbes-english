# -*- coding: utf-8 -*-
"""Interface strings for The Language of Self-Improvement (B1), English and German."""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='The Language of <em>Self-Improvement</em>',
    coverSub='Habits, mindset and the case for small steps — the words for talking about getting better',
    chipLevel='B1 · Intermediate', chipFocus='Personal development', chipCount='17 slides',
    vidEyebrow='Before anything else',
    vidTitle='Three and a half minutes, and then the argument',
    vidNote='Watch it first. The next three cards are what he argues, so you can check whether you heard the same thing.',
    v1h='Thirty days is the unit',
    v1b='Long enough for a habit to form, short enough that you can see the end from the start.',
    v2h='Small beats dramatic',
    v2b='The changes that <em>stick</em> are the sustainable ones. The dramatic ones come back off.',
    v3h='And the part people miss:',
    v3b='the months stopped “flying by forgotten”. Doing something deliberately each day made the time countable — and therefore memorable.',
    readEyebrow='From the reading', readTitle='Why small steps lead to big changes',
    r1h='Start smaller than feels serious',
    r1b='People stall because the change they picture is too big to begin. The size of the first step is the only thing that decides whether there is a second one.',
    r2h='The 1% rule',
    r2b='The arithmetic is the argument. Small and daily compounds; large and occasional does not.',
    r3h='Build the habit, not the willpower',
    r3b='Willpower runs out. A habit does not need any, which is why it outlasts motivation.',
    mindEyebrow='The other half of it', mindTitle='Mindset, and knowing yourself',
    m1h='A growth mindset',
    m1b='The practical test: after a failure, do you name a thing to practise, or a fact about yourself?',
    m2h='Mistakes are information',
    m2b='People with a growth mindset see a mistake as a reason to change the method, not a reason to stop.',
    m3h='It is not only about goals',
    m3b='The reading ends here, and it is the harder half: once you know who you are, the choices get easier to make.',
    matchEyebrow='Eight words, six of them here', matchTitle='Match the word to what it means',
    matchHint='Click a word, then click its meaning.',
    qEyebrow='Video and reading', qTitle='What did it actually say?',
    gapEyebrow='The right word', gapTitle='Complete the sentence',
    gapHint='Two of the ten words in the bank belong to no gap here.',
    bankLabel='Word bank:',
    actTitle='Thirty days from now', actUse='Use at least four:',
    actWriteKind='Writing · 120–160 words',
    actSpeakBrief='Speak for at least a minute on each. Short answers do not count.',
    actSpeak1='Name a good habit you already have. How did it start — deliberately, or by accident?',
    actSpeak2='Describe a time you felt overwhelmed. What did you actually do about it?',
    actSpeak3='Do you agree that small changes beat big ones? Give one example from your own life.',
    actSpeak4='Some people say always try to improve; others say accept yourself. Can both be true?',
    actWriteBrief='Choose your own 30-day challenge and write the plan: what, when, how you will know it worked.',
    actPlaceholder='For the next thirty days I am going to…',
    resPerfect='Full marks. You can talk about habits and mindset without reaching for a dictionary.',
    resStrong='Strong. The vocabulary is secure — the difference between <em>fulfilling</em> and <em>enjoyable</em> is worth one more look.',
    resMid='A good base. Go back to the reading slides; most of the misses come from the 1% rule and the habit argument.',
    resLow='Watch the talk again and reread the two reading slides, then run it once more. The words come after the idea.',
)

T['de'] = dict(
    coverTitle='Die Sprache der <em>Selbstverbesserung</em>',
    coverSub='Gewohnheiten, Haltung und das Argument für kleine Schritte — die Wörter, um übers Besserwerden zu sprechen',
    chipLevel='B1 · Mittelstufe', chipFocus='Persönliche Entwicklung', chipCount='17 Folien',
    vidEyebrow='Ganz zu Anfang',
    vidTitle='Dreieinhalb Minuten — und dann das Argument',
    vidNote='Sehen Sie es zuerst. Die nächsten drei Karten geben seine Argumente wieder, damit Sie prüfen können, ob Sie dasselbe gehört haben.',
    v1h='Dreißig Tage sind die Einheit',
    v1b='Lang genug, dass eine Gewohnheit entsteht, kurz genug, dass man vom Start aus das Ende sieht.',
    v2h='Klein schlägt spektakulär',
    v2b='Was <em>bleibt</em>, sind die tragfähigen Änderungen. Die spektakulären fallen wieder ab.',
    v3h='Und der Teil, den man überhört:',
    v3b='die Monate „flogen nicht mehr vergessen vorbei“. Jeden Tag bewusst etwas zu tun machte die Zeit zählbar — und damit erinnerbar.',
    readEyebrow='Aus dem Lesetext', readTitle='Warum kleine Schritte große Veränderungen bringen',
    r1h='Kleiner anfangen, als es ernsthaft wirkt',
    r1b='Menschen bleiben stehen, weil die Veränderung, die sie sich vorstellen, zu groß zum Anfangen ist. Nur die Größe des ersten Schritts entscheidet, ob es einen zweiten gibt.',
    r2h='Die 1-%-Regel',
    r2b='Die Rechnung ist das Argument. Klein und täglich verzinst sich; groß und gelegentlich nicht.',
    r3h='Bauen Sie die Gewohnheit, nicht die Willenskraft',
    r3b='Willenskraft geht aus. Eine Gewohnheit braucht keine — deshalb überlebt sie die Motivation.',
    mindEyebrow='Die andere Hälfte', mindTitle='Haltung — und sich selbst kennen',
    m1h='Ein Wachstumsdenken',
    m1b='Der praktische Test: Nennen Sie nach einem Misserfolg etwas zum Üben oder eine Tatsache über sich selbst?',
    m2h='Fehler sind Information',
    m2b='Wer ein Wachstumsdenken hat, sieht im Fehler einen Grund, die Methode zu ändern — nicht aufzuhören.',
    m3h='Es geht nicht nur um Ziele',
    m3b='Hier endet der Lesetext, und das ist die schwerere Hälfte: Wer sich selbst kennt, trifft leichter Entscheidungen.',
    matchEyebrow='Acht Wörter, sechs davon hier', matchTitle='Ordnen Sie das Wort seiner Bedeutung zu',
    matchHint='Klicken Sie auf ein Wort und dann auf seine Bedeutung.',
    qEyebrow='Video und Lesetext', qTitle='Was wurde tatsächlich gesagt?',
    gapEyebrow='Das richtige Wort', gapTitle='Vervollständigen Sie den Satz',
    gapHint='Zwei der zehn Wörter in der Liste gehören in keine dieser Lücken.',
    bankLabel='Wortliste:',
    actTitle='In dreißig Tagen', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 120–160 Wörter',
    actSpeakBrief='Sprechen Sie zu jedem Punkt mindestens eine Minute. Kurze Antworten zählen nicht.',
    actSpeak1='Nennen Sie eine gute Gewohnheit, die Sie schon haben. Wie ist sie entstanden — absichtlich oder zufällig?',
    actSpeak2='Beschreiben Sie eine Situation, in der Sie überfordert waren. Was haben Sie tatsächlich getan?',
    actSpeak3='Schlagen kleine Änderungen wirklich große? Nennen Sie ein Beispiel aus Ihrem eigenen Leben.',
    actSpeak4='Die einen sagen: immer besser werden. Die anderen: sich annehmen. Kann beides stimmen?',
    actWriteBrief='Wählen Sie Ihre eigene 30-Tage-Aufgabe und schreiben Sie den Plan: was, wann, und woran Sie den Erfolg erkennen.',
    actPlaceholder='For the next thirty days I am going to…',
    resPerfect='Volle Punktzahl. Sie können über Gewohnheiten und Haltung sprechen, ohne zum Wörterbuch zu greifen.',
    resStrong='Stark. Der Wortschatz sitzt — der Unterschied zwischen <em>fulfilling</em> und <em>enjoyable</em> lohnt noch einen Blick.',
    resMid='Eine gute Grundlage. Zurück zu den Lesefolien; die meisten Fehler betreffen die 1-%-Regel und das Gewohnheitsargument.',
    resLow='Sehen Sie den Vortrag noch einmal und lesen Sie die beiden Lesefolien, dann starten Sie neu. Die Wörter kommen nach der Idee.',
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
