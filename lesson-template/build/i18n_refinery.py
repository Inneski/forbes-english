# -*- coding: utf-8 -*-
"""Interface strings for Active & Passive Voice (Refinery), English and German."""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Active &amp; <em>Passive Voice</em>',
    coverSub='Radio calls, shift handovers and incident reports — and why they are not written the same way',
    chipLevel='B1–B2 · Refinery deputy lead', chipFocus='Active &amp; passive',
    chipCount='16 slides',
    coreEyebrow='The difference, stated once',
    coreTitle='Who is at the front of the sentence?',
    k1h='Active',
    k1b='The doer comes first. You know exactly who did what — which is why commands and handovers are written this way.',
    k2h='Passive',
    k2b='The thing acted on comes first, and <em>becomes the subject of the sentence</em>. Who did it may follow with <em>by</em>, or may never be mentioned.',
    k3h='Why it matters here',
    k3b='Active assigns accountability. Passive is the standard for reports and procedures. A professional switches between them on purpose.',
    tabEyebrow='The form, in every tense you need',
    tabTitle='to be + past participle. That is the whole machine.',
    tabNote='Regular participles add <em>-ed</em>: test → tested, seal → sealed. Irregular ones change: write → written, do → done. The quick test: if it fits in <em>“The report was ___”</em>, it is the past participle.',
    useEyebrow='Choosing between them', useTitle='Speak in active. Write reports in passive.',
    u1h='Active when…',
    u1b='Commands are <em>always</em> active. “Bravo team, withdraw” beats “Bravo team is to be withdrawn” by a second, and a second is a long time on a radio.',
    u2h='Passive when…',
    u2b='“The isolation valve was confirmed closed at 14:32” is the register a report wants. <em>I confirmed it</em> is true, and reads as a statement rather than a record.',
    qEyebrow='Knowledge check', qTitle='Which one?',
    gapEyebrow='Turn it round', gapTitle='Complete the passive version',
    gapHint='The active sentence is above each gap. Keep the same tense.',
    matchEyebrow='The situation decides', matchTitle='Which voice, and why',
    matchHint='Click a situation, then click the voice it takes.',
    ordEyebrow='Making a passive', ordTitle='Put the four steps in order',
    ordHint='Click the steps in the order you carry them out.',
    actTitle='Say it, then write it', actUse='Use at least four:',
    actWriteKind='Writing · 120–160 words',
    actSpeakBrief='One of you is the deputy lead on the radio. The other is writing the report afterwards.',
    actSpeak1='Give four commands over the radio. Every one active, every one under eight words.',
    actSpeak2='Now report the same four events for the file. Every one passive.',
    actSpeak3='Describe a fault nobody has traced. Say it without naming anyone — and without sounding evasive.',
    actSpeak4='Convert this aloud: <em>The deputy lead inspected the bund wall after the incident.</em>',
    actWriteBrief='Write the incident report for a small flange fire: what happened, what was done, and at what time.',
    actPlaceholder='At 14:32 the isolation valve was confirmed closed.',
    resPerfect='Full marks. You can switch voice on purpose, which is the whole skill.',
    resStrong='Strong. The forms are secure — the choice of voice in borderline cases is what rewards another pass.',
    resMid='A good base. Go back to the tense table; most of the misses are the participle, not the idea.',
    resLow='Read the first three slides again, then run it once more. Decide who is at the front, then build the verb.',
)

T['de'] = dict(
    coverTitle='Aktiv &amp; <em>Passiv</em>',
    coverSub='Funksprüche, Schichtübergaben und Einsatzberichte — und warum man sie nicht gleich schreibt',
    chipLevel='B1–B2 · Stellvertretende Leitung Raffinerie', chipFocus='Aktiv &amp; Passiv',
    chipCount='16 Folien',
    coreEyebrow='Der Unterschied, einmal gesagt',
    coreTitle='Wer steht vorn im Satz?',
    k1h='Aktiv',
    k1b='Der Handelnde kommt zuerst. Man weiß genau, wer was getan hat — deshalb werden Befehle und Übergaben so formuliert.',
    k2h='Passiv',
    k2b='Das Betroffene kommt zuerst und <em>wird zum Subjekt des Satzes</em>. Wer es getan hat, kann mit <em>by</em> folgen — oder ganz wegbleiben.',
    k3h='Warum das hier zählt',
    k3b='Aktiv weist Verantwortung zu. Passiv ist der Standard für Berichte und Verfahrensanweisungen. Profis wechseln bewusst zwischen beidem.',
    tabEyebrow='Die Form, in jeder Zeit, die Sie brauchen',
    tabTitle='to be + Partizip Perfekt. Das ist der ganze Mechanismus.',
    tabNote='Regelmäßige Partizipien bekommen <em>-ed</em>: test → tested, seal → sealed. Unregelmäßige ändern sich: write → written, do → done. Der Schnelltest: Passt es in <em>„The report was ___“</em>, ist es das Partizip Perfekt.',
    useEyebrow='Die Wahl zwischen beiden', useTitle='Sprechen Sie aktiv. Berichte schreiben Sie passiv.',
    u1h='Aktiv, wenn…',
    u1b='Befehle sind <em>immer</em> aktiv. „Bravo team, withdraw“ ist eine Sekunde schneller als „Bravo team is to be withdrawn“ — und am Funk ist eine Sekunde lang.',
    u2h='Passiv, wenn…',
    u2b='„The isolation valve was confirmed closed at 14:32“ ist das Register, das ein Bericht verlangt. <em>I confirmed it</em> stimmt zwar, klingt aber wie eine Aussage, nicht wie ein Protokoll.',
    qEyebrow='Wissenscheck', qTitle='Welcher Satz?',
    gapEyebrow='Drehen Sie es um', gapTitle='Vervollständigen Sie die Passivform',
    gapHint='Der Aktivsatz steht jeweils über der Lücke. Behalten Sie die Zeit bei.',
    matchEyebrow='Die Situation entscheidet', matchTitle='Welches Genus verbi — und warum',
    matchHint='Klicken Sie auf eine Situation und dann auf die Form, die sie verlangt.',
    ordEyebrow='Ein Passiv bauen', ordTitle='Bringen Sie die vier Schritte in die richtige Reihenfolge',
    ordHint='Klicken Sie die Schritte in der Reihenfolge an, in der Sie sie ausführen.',
    actTitle='Erst sagen, dann schreiben', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 120–160 Wörter',
    actSpeakBrief='Eine Person ist die stellvertretende Leitung am Funk. Die andere schreibt danach den Bericht.',
    actSpeak1='Geben Sie vier Funkbefehle. Alle aktiv, alle unter acht Wörtern.',
    actSpeak2='Protokollieren Sie dieselben vier Vorgänge für die Akte. Alle passiv.',
    actSpeak3='Beschreiben Sie eine Störung, deren Ursache niemand kennt. Ohne jemanden zu nennen — und ohne ausweichend zu klingen.',
    actSpeak4='Formen Sie laut um: <em>The deputy lead inspected the bund wall after the incident.</em>',
    actWriteBrief='Schreiben Sie den Einsatzbericht zu einem kleinen Flanschbrand: was geschah, was getan wurde und um welche Uhrzeit.',
    actPlaceholder='At 14:32 the isolation valve was confirmed closed.',
    resPerfect='Volle Punktzahl. Sie wechseln das Genus verbi bewusst — genau darum geht es.',
    resStrong='Stark. Die Formen sitzen — die Wahl in Grenzfällen lohnt einen zweiten Durchgang.',
    resMid='Eine gute Grundlage. Zurück zur Zeitentabelle; die meisten Fehler betreffen das Partizip, nicht die Idee.',
    resLow='Lesen Sie die ersten drei Folien noch einmal und starten Sie neu. Erst entscheiden, wer vorn steht, dann das Verb bauen.',
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
