# -*- coding: utf-8 -*-
"""Interface strings for Talking About Your Product (B1), English and German.

Note that this lesson is teacher-led, so a good deal of the translated text is
addressed to the teacher rather than the learner. The English being taught —
the five upgrades, the question bank, the roleplay lines — stays in English.
"""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Talking About <em>Your Product</em>',
    coverSub='A fifty-minute speaking lesson: research a customer, brief a supplier, pitch the thing',
    chipLevel='B1 · Professional speaking', chipFocus='Market research &amp; product',
    chipCount='17 slides',
    runEyebrow='How to run it', runTitle='Three rules for the teacher',
    h1h='Do not correct in Activity 1',
    h1b='Corrections land far better later, as language you are teaching, than immediately, as a list of things they got wrong.',
    h2h='Every upgrade is said aloud, twice',
    h2b='The goal is muscle memory, not recognition. A phrase they have only read will not arrive when they need it.',
    h3h='Finish on three things',
    h3b='Specific, in that order. “Your structure was logical” · “<em>conduct</em> research, not <em>make</em>” · “try <em>the key advantage is…</em>”',
    warmEyebrow='Activity 1 · 5–8 minutes', warmTitle='Warm-up: talk about your work',
    warmAsk='Ask these, one at a time', warmTh='Teacher',
    warmTb='Do not rush, and <em>do not correct yet</em>. Listen for grammar patterns, hesitation and vocabulary gaps, and make notes. The point of this activity is to hear how they talk about the job now — corrections come back later as language, not as a list of errors.',
    listenEyebrow='Activity 1 · while they speak', listenTitle='Four patterns to listen for',
    lWrong='Likely to come up', lRight='What you are aiming at',
    qEyebrow='Activity 2 · say it better', qTitle='Say it professionally',
    drillEyebrow='Activity 2 · from memory', drillTitle='Quick drill — no looking',
    drillHint='Read the situation. They answer with the phrase, out loud, without looking at the previous slides.',
    roofEyebrow='Activity 3 · 12–15 minutes', roofTitle='Market research roleplay',
    r1h='🎙 Student — product manager',
    r1b='You are doing market research with a roofer in England. Find out how he chooses membranes, what goes wrong, and what would make his job easier. Ask open questions and follow up on every answer.',
    r2h='🔨 Teacher — UK roofer',
    r2b='Eighteen years on roofs. Straight-talking, slightly impatient. You decide what gets bought, not the contractor. <strong>Volunteer nothing</strong> — if the question is closed, answer yes or no and wait. That is what forces a better follow-up.',
    roofAns='Answers to use, in any order',
    qbEyebrow='Activity 3 · the questions', qbTitle='Six questions, by what they do',
    qbNote='A guide, not a script. The follow-up matters more than the question — every answer above has a second question hiding in it.',
    matchEyebrow='Activity 3 · after the roleplay',
    matchTitle='Turn the closed question into an open one',
    matchHint='Click a weak question, then click the version that opens the conversation.',
    supEyebrow='Activity 4 · 10–12 minutes', supTitle='Supplier discussion',
    s1h='🎙 Student — product manager',
    s1b='Report what the roofer actually told you in Activity 3 — not what you expected to hear. Then ask whether the product can change: feasibility, cost, timeline. Finish by summarising what was agreed.',
    s2h='🔩 Teacher — supplier',
    s2b='Interested, busy, numbers-focused. Reducing weight is possible. Grip coating adds <strong>8–12%</strong> to cost. Development takes <strong>4–6 months</strong>. Say those numbers out loud — the summary task depends on them. Ask for written specifications before you commit.',
    supPh='Six phrases to get in',
    stEyebrow='Activity 5 · before the timer', stTitle='Five stages, held in your head',
    st1='Introduce it<br><em>“This product is designed for…”</em>',
    st2='The purpose<br><em>“Its main purpose is to…”</em>',
    st3='The benefit<br><em>“The main advantage is…”</em>',
    st4='Compare<br><em>“Compared with standard options…”</em>',
    st5='Summarise<br><em>“In simple terms, it helps…”</em>',
    stNote='Two minutes, one product, no notes. Then they self-assess before you say anything: did they name the user, the purpose, one benefit, and a comparison?',
    actTitle='The two-minute pitch', actUse='Use at least four:',
    actWriteKind='Writing · 120–160 words',
    actSpeakBrief='The teacher is a new retailer in Ireland who knows construction but not your range.',
    actSpeak1='Two minutes on one product: what it is, who uses it, what problem it solves.',
    actSpeak2='Self-assess first: did you name a user, a purpose, a benefit and a comparison?',
    actSpeak3='Prepare a different product for next time — same four things, same two minutes.',
    actSpeak4='Bring five real questions a customer or supplier asked you in English this month.',
    actWriteBrief='Write the email you would send the supplier after Activity 4: the feedback, the request, and what you agreed.',
    actPlaceholder='Dear Frank, following our call this morning,',
    resPerfect='Every upgrade and every question. Those nine phrases are the ones that make the difference at work.',
    resStrong='Strong. The upgrades are secure — the open questions are what to rehearse before the next real call.',
    resMid='A good base. Go back to the four patterns slide; that is where the misses come from.',
    resLow='Say each of the five upgrades aloud twice, then run it again. Recognising them is not the same as producing them.',
)

T['de'] = dict(
    coverTitle='Über <em>Ihr Produkt</em> sprechen',
    coverSub='Eine fünfzigminütige Sprechstunde: Kundschaft befragen, Lieferanten briefen, das Produkt vorstellen',
    chipLevel='B1 · Berufliches Sprechen', chipFocus='Marktforschung &amp; Produkt',
    chipCount='17 Folien',
    runEyebrow='So läuft die Stunde', runTitle='Drei Regeln für die Lehrkraft',
    h1h='In Aktivität 1 nicht korrigieren',
    h1b='Korrekturen kommen später viel besser an — als Sprache, die Sie vermitteln, nicht als Liste dessen, was falsch war.',
    h2h='Jede Verbesserung wird zweimal laut gesagt',
    h2b='Es geht um Automatisierung, nicht um Wiedererkennen. Eine nur gelesene Wendung ist im Ernstfall nicht da.',
    h3h='Am Ende drei Dinge',
    h3b='Konkret, in dieser Reihenfolge. „Ihr Aufbau war logisch“ · „<em>conduct</em> research, nicht <em>make</em>“ · „versuchen Sie <em>the key advantage is…</em>“',
    warmEyebrow='Aktivität 1 · 5–8 Minuten', warmTitle='Aufwärmen: über die eigene Arbeit sprechen',
    warmAsk='Diese Fragen einzeln stellen', warmTh='Lehrkraft',
    warmTb='Nicht drängen und <em>noch nicht korrigieren</em>. Achten Sie auf Grammatikmuster, Zögern und Wortschatzlücken, und machen Sie sich Notizen. Es geht darum zu hören, wie über den Beruf jetzt gesprochen wird — Korrekturen kommen später als Sprache zurück, nicht als Fehlerliste.',
    listenEyebrow='Aktivität 1 · beim Zuhören', listenTitle='Vier Muster, auf die Sie achten',
    lWrong='Kommt erfahrungsgemäß vor', lRight='Worauf Sie hinarbeiten',
    qEyebrow='Aktivität 2 · besser sagen', qTitle='Sagen Sie es professionell',
    drillEyebrow='Aktivität 2 · aus dem Gedächtnis', drillTitle='Schnelldurchlauf — ohne nachzusehen',
    drillHint='Lesen Sie die Situation vor. Die Antwort kommt laut und ohne Blick auf die vorherigen Folien.',
    roofEyebrow='Aktivität 3 · 12–15 Minuten', roofTitle='Rollenspiel Marktforschung',
    r1h='🎙 Lernende:r — Produktmanagement',
    r1b='Sie machen Marktforschung bei einem Dachdecker in England. Finden Sie heraus, wie er Bahnen auswählt, was schiefgeht und was ihm die Arbeit erleichtern würde. Offene Fragen, und zu jeder Antwort eine Nachfrage.',
    r2h='🔨 Lehrkraft — Dachdecker aus England',
    r2b='Achtzehn Jahre auf Dächern. Direkt, etwas ungeduldig. Sie entscheiden, was gekauft wird, nicht die Baufirma. <strong>Sagen Sie nichts von sich aus</strong> — bei einer geschlossenen Frage nur ja oder nein und dann warten. Genau das erzwingt die bessere Nachfrage.',
    roofAns='Antworten, in beliebiger Reihenfolge',
    qbEyebrow='Aktivität 3 · die Fragen', qbTitle='Sechs Fragen, nach ihrer Funktion',
    qbNote='Ein Leitfaden, kein Skript. Die Nachfrage zählt mehr als die Frage — in jeder Antwort oben steckt eine zweite.',
    matchEyebrow='Aktivität 3 · nach dem Rollenspiel',
    matchTitle='Aus der geschlossenen Frage eine offene machen',
    matchHint='Klicken Sie auf eine schwache Frage und dann auf die Fassung, die das Gespräch öffnet.',
    supEyebrow='Aktivität 4 · 10–12 Minuten', supTitle='Gespräch mit dem Lieferanten',
    s1h='🎙 Lernende:r — Produktmanagement',
    s1b='Berichten Sie, was der Dachdecker in Aktivität 3 tatsächlich gesagt hat — nicht, was Sie erwartet hatten. Fragen Sie dann, ob das Produkt geändert werden kann: Machbarkeit, Kosten, Zeitplan. Fassen Sie am Ende zusammen.',
    s2h='🔩 Lehrkraft — Lieferant',
    s2b='Interessiert, im Stress, zahlenorientiert. Gewichtsreduktion ist möglich. Eine Antirutsch-Beschichtung kostet <strong>8–12 %</strong> mehr. Entwicklung dauert <strong>4–6 Monate</strong>. Sagen Sie diese Zahlen laut — die Zusammenfassungsaufgabe hängt daran. Verlangen Sie eine schriftliche Spezifikation.',
    supPh='Sechs Wendungen, die vorkommen sollen',
    stEyebrow='Aktivität 5 · vor dem Timer', stTitle='Fünf Schritte, im Kopf behalten',
    st1='Vorstellen<br><em>„This product is designed for…“</em>',
    st2='Der Zweck<br><em>„Its main purpose is to…“</em>',
    st3='Der Nutzen<br><em>„The main advantage is…“</em>',
    st4='Vergleichen<br><em>„Compared with standard options…“</em>',
    st5='Zusammenfassen<br><em>„In simple terms, it helps…“</em>',
    stNote='Zwei Minuten, ein Produkt, keine Notizen. Danach zuerst die Selbsteinschätzung, bevor Sie etwas sagen: Wurden Nutzer, Zweck, ein Nutzen und ein Vergleich genannt?',
    actTitle='Der Zwei-Minuten-Pitch', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 120–160 Wörter',
    actSpeakBrief='Die Lehrkraft ist ein neuer Händler in Irland, der sich mit Bau auskennt, aber nicht mit Ihrem Sortiment.',
    actSpeak1='Zwei Minuten zu einem Produkt: was es ist, wer es nutzt, welches Problem es löst.',
    actSpeak2='Erst selbst einschätzen: Wurden Nutzer, Zweck, Nutzen und ein Vergleich genannt?',
    actSpeak3='Bereiten Sie fürs nächste Mal ein anderes Produkt vor — dieselben vier Punkte, dieselben zwei Minuten.',
    actSpeak4='Bringen Sie fünf echte Fragen mit, die Kundschaft oder Lieferanten Ihnen diesen Monat auf Englisch gestellt haben.',
    actWriteBrief='Schreiben Sie die E-Mail, die Sie dem Lieferanten nach Aktivität 4 schicken würden: das Feedback, die Bitte und das Vereinbarte.',
    actPlaceholder='Dear Frank, following our call this morning,',
    resPerfect='Jede Verbesserung und jede Frage. Diese neun Wendungen sind die, die im Beruf den Unterschied machen.',
    resStrong='Stark. Die Verbesserungen sitzen — proben Sie die offenen Fragen vor dem nächsten echten Gespräch.',
    resMid='Eine gute Grundlage. Zurück zur Folie mit den vier Mustern; dort entstehen die Fehler.',
    resLow='Sagen Sie jede der fünf Verbesserungen zweimal laut und starten Sie dann neu. Wiedererkennen ist nicht dasselbe wie Produzieren.',
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
