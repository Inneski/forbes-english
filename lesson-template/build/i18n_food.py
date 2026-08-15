# -*- coding: utf-8 -*-
"""Interface strings for Ordering Food & Drink (A1 Part 2), English and German.

The instructions translate; the English being taught does not. The six
situations and their options, the dialogue, the word bank, the six phrases and
the five sentences to repair all stay in English on every setting — they are
the lesson. The other eight languages ship as empty objects, which is an
honest state: the menu simply does not offer them. A half-filled language is
the state to avoid, because it appears in the menu and then falls back to
English halfway down the screen.
"""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Ordering Food &amp; <em>Drink</em>',
    coverSub='Part two: from the door to the bill, in the words people actually use',
    chipLevel='A1 · Part 2 of 2', chipFocus='Restaurant English', chipCount='16 slides',
    shapeEyebrow='Before the questions',
    shapeTitle='Three phrases carry the whole meal',
    p1='To order. Short for <em>I would like</em> — softer than <em>I want</em>, which sounds like a demand.',
    p2='To ask for something. The verb after it never changes: <em>bring</em>, not <em>to bring</em> or <em>bringing</em>.',
    p3='To get attention, and to open a complaint. Without it the same sentence sounds angry.',
    menuEyebrow='The menu, in order',
    menuTitle='The words on the card, and the ones you will be asked',
    courseH='The courses',
    courseB='American menus say <em>appetizer</em> and <em>entrée</em> instead of <em>starter</em> and <em>main course</em>. Same meal.',
    askH='Three questions you will be asked',
    askB='Steak has exactly three answers: <em>rare</em>, <em>medium</em>, <em>well done</em>.',
    qEyebrow='In the restaurant', qTitle='What do you say?',
    gapEyebrow='The whole meal, in order', gapTitle='Complete the conversation',
    bankLabel='Word bank:',
    fixEyebrow='One word out of place', fixTitle='Repair the sentence',
    fixHint='The crossed-out word is wrong. Type the word that belongs there.',
    fixLabel='It should be:',
    matchEyebrow='What it really means', matchTitle='Six phrases you will hear or need',
    matchHint='Click a phrase, then click what it means.',
    actTitle='Run the whole meal', actUse='Use at least four:',
    actWriteKind='Writing · 60–90 words',
    actSpeakBrief='One waiter, one customer. Then swap, and make the second run harder.',
    actSpeak1='Arrive without a reservation. The waiter must find you a table anyway.',
    actSpeak2='Order a starter and a main. Ask the waiter to recommend one of them.',
    actSpeak3='Something is wrong with the food. Complain without once saying “bad”.',
    actSpeak4='Ask for separate bills, and check whether service is included.',
    actWriteBrief='Write the conversation you had, as a dialogue. Waiter first.',
    actPlaceholder='Waiter: Good evening — do you have a reservation?',
    resPerfect='Full marks. You could walk into a restaurant tonight and be understood.',
    resStrong='Strong. The phrases have landed — the polite openings are what to practise aloud.',
    resMid='A good base. Go back to the three phrases; most of the misses start there.',
    resLow='Read the first two slides again, then run it once more. The phrases first, the questions after.',
)

T['de'] = dict(
    coverTitle='Essen &amp; <em>Trinken</em> bestellen',
    coverSub='Teil zwei: von der Tür bis zur Rechnung, in den Wendungen, die wirklich benutzt werden',
    chipLevel='A1 · Teil 2 von 2', chipFocus='Englisch im Restaurant', chipCount='16 Folien',
    shapeEyebrow='Vor den Aufgaben',
    shapeTitle='Drei Wendungen tragen das ganze Essen',
    p1='Zum Bestellen. Kurzform von <em>I would like</em> — höflicher als <em>I want</em>, das wie eine Forderung klingt.',
    p2='Um etwas zu bitten. Das Verb danach bleibt unverändert: <em>bring</em>, nicht <em>to bring</em> oder <em>bringing</em>.',
    p3='Um Aufmerksamkeit zu bekommen und eine Beschwerde zu eröffnen. Ohne diese Wendung klingt derselbe Satz verärgert.',
    menuEyebrow='Die Speisekarte, der Reihe nach',
    menuTitle='Die Wörter auf der Karte — und die Fragen, die kommen',
    courseH='Die Gänge',
    courseB='Auf amerikanischen Karten stehen <em>appetizer</em> und <em>entrée</em> statt <em>starter</em> und <em>main course</em>. Dasselbe Essen.',
    askH='Drei Fragen, die Ihnen gestellt werden',
    askB='Beim Steak gibt es genau drei Antworten: <em>rare</em>, <em>medium</em>, <em>well done</em>.',
    qEyebrow='Im Restaurant', qTitle='Was sagen Sie?',
    gapEyebrow='Das ganze Essen, der Reihe nach', gapTitle='Vervollständigen Sie das Gespräch',
    bankLabel='Wortliste:',
    fixEyebrow='Ein Wort sitzt falsch', fixTitle='Reparieren Sie den Satz',
    fixHint='Das durchgestrichene Wort ist falsch. Tippen Sie das Wort, das dorthin gehört.',
    fixLabel='Richtig wäre:',
    matchEyebrow='Was es wirklich heißt', matchTitle='Sechs Wendungen, die Sie hören oder brauchen',
    matchHint='Klicken Sie auf eine Wendung und dann auf ihre Bedeutung.',
    actTitle='Das ganze Essen durchspielen', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 60–90 Wörter',
    actSpeakBrief='Einer bedient, einer bestellt. Dann tauschen — und den zweiten Durchgang schwerer machen.',
    actSpeak1='Sie kommen ohne Reservierung. Der Kellner muss trotzdem einen Tisch finden.',
    actSpeak2='Bestellen Sie eine Vorspeise und ein Hauptgericht. Lassen Sie sich eines davon empfehlen.',
    actSpeak3='Mit dem Essen stimmt etwas nicht. Beschweren Sie sich, ohne einmal „bad“ zu sagen.',
    actSpeak4='Bitten Sie um getrennte Rechnungen und fragen Sie, ob die Bedienung inbegriffen ist.',
    actWriteBrief='Schreiben Sie Ihr Gespräch als Dialog auf. Der Kellner beginnt.',
    actPlaceholder='Waiter: Good evening — do you have a reservation?',
    resPerfect='Volle Punktzahl. Sie könnten heute Abend in ein Restaurant gehen und verstanden werden.',
    resStrong='Stark. Die Wendungen sitzen — üben Sie jetzt die höflichen Einstiege laut.',
    resMid='Eine gute Grundlage. Gehen Sie zu den drei Wendungen zurück; dort beginnen die meisten Fehler.',
    resLow='Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Erst die Wendungen, dann die Fragen.',
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
