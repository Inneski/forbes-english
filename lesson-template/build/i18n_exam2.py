# -*- coding: utf-8 -*-
"""Interface strings for Out of This World Part II, English and German."""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Out of <em>This World</em>',
    coverSub='Part II: some and any, one and ones, reading technique, and the '
             'mock test',
    chipLevel='A1+ / A2 &middot; Part II', chipFocus='Hours 4&ndash;5',
    chipCount='50 slides',

    saE='Hour 4 &middot; some or any', saT='The rule, and then the exception',
    sa1h='Positive → some', sa1n='This one never changes.',
    sa2h='Negative → any',
    sa2n='After <em>not</em>, <em>isn\'t</em>, <em>don\'t</em> — always '
         '<em>any</em>.',
    sa3h='Question → any',
    sa3n='When you genuinely do not know the answer. Keep reading — the next '
         'slide is the case that catches people out.',
    sbE='Hour 4 &middot; The case that catches people out',
    sbT='Offers and requests take some — even as questions',
    sb1h='An offer',
    sb1n='You are giving, not asking. <em>Would you like…?</em> is always an '
         'offer.',
    sb2h='A request',
    sb2n='You are asking for a thing, not asking whether it exists.',
    sb3h='The overlap',
    sb3n='In a café this is really a request, so both are natural. In the test, '
         '<em>any</em> is the safe answer to a plain question — but you now know '
         'why you hear both.',
    ooE='Hour 4 &middot; one or ones',
    ooT='So you do not have to say the noun twice',
    oo1h='one — singular', oo1n='One thing.',
    oo2h='ones — plural',
    oo2n='More than one thing. Shoes, glasses, trousers and jeans are always '
         'plural in English.',
    oo3h='How to decide',
    oo3n='The question tells you. <em>Which shoes…?</em> → plural → '
         '<em>ones</em>. Nothing else decides it.',
    rmE='Hour 4 &middot; Reading method',
    rmT1='Before you read the questions (1 of 2)', rmT2='Then answer (2 of 2)',
    rm1h='1 &middot; Read the title', rm2h='2 &middot; Look at any picture',
    rm3h='3 &middot; Underline the facts',
    rm3n='Almost every True/False item is decided by one of these. Underline '
         'them and the answers are already on the page.',
    rm4h='4 &middot; Read the question twice', rm5h='5 &middot; Find the line',
    rm5n='If you cannot find the line, your answer is a guess. An answer that '
         '"sounds right" is the classic trap.',
    rm6h='6 &middot; Full sentence if asked',
    rm6n='If the instruction says <em>in full sentences</em>, one word scores '
         'nothing — however right it is.',

    sgE='Hour 4 &middot; Activity 1', sgT='some or any?',
    sgHint='Decide what the sentence is doing first: stating, denying, asking, '
           'offering.',
    ogE='Hour 4 &middot; Activity 2', ogT='one or ones?',
    ogHint='Look back at the noun in the question.',
    r1E='Hour 4 &middot; Reading 1', r1T='Mia\'s restaurant',
    r1N='Underline the names, the food and the word <em>left</em> before you '
        'turn the page.',
    tf1E='Hour 4 &middot; Activity 3', tf1T='True or false?',
    fsE='Hour 4 &middot; Full sentences', fsT='What a full answer looks like',
    fs1h='Where did Mia go yesterday?',
    fs1n='The answer reuses the words of the question. That is the whole '
         'technique.',
    fs2h='What did her brother eat?',
    fs2n='Past question → past answer. <em>Ate</em>, not <em>eat</em>.',
    fs3h='What did they buy later?',
    fs3n='Not "ice cream". A full sentence needs a subject and a verb.',
    dgE='Hour 4 &middot; Activity 4', dgT='At the restaurant — some or any?',
    dgHint='Read who is speaking. A waiter offers; a customer asks.',
    doE='Hour 4 &middot; Activity 5', doT='In the shop — one or ones?',
    doHint='The assistant\'s question tells you singular or plural.',
    r2E='Hour 4 &middot; Reading 2', r2T='Emma\'s restaurant visit',
    r2N='Watch the day, the two dishes, and the words <em>left</em>, '
        '<em>small</em> and <em>large</em>.',
    tf2E='Hour 4 &middot; Activity 6', tf2T='True or false?',
    r5E='Hour 4 &middot; Activity 6', r5T='Complete from the text',
    mxE='Hour 4 &middot; Activity 7', mxT='Mixed: some, any, one, ones',
    mxHint='All four are in play now. Decide what the sentence is doing, then '
           'whether the thing is singular or plural.',

    stE='Hour 5 &middot; Guided writing', stT='The shape of a story that scores',
    st1h='Beginning',
    st1n='Two sentences is enough. Start with a time marker and the examiner '
         'knows immediately that you can use one.',
    st2h='Middle, then the problem',
    st2n='A story with no problem is a list. The problem is what makes the '
         'reader keep going.',
    st3h='Ending',
    st3n='Finish it. An unfinished story loses marks even if every sentence in '
         'it is correct.',
    phE='Hour 5 &middot; Guided writing', phT='Phrases to join it together',
    ph1h='To begin', ph2h='To go on', ph3h='For the surprise, and the end',
    ph3n='Use three or four across the whole text. Ten is worse than three — it '
         'stops being a story and becomes a list of connectors.',
    mdE='Hour 5 &middot; Model text',
    mdT1='A story that does the job (1 of 2)',
    mdN1='Bold marks every checklist item as it happens: a time marker to open, '
         '<em>some</em>, and <em>suddenly</em> for the surprise.',
    mdT2='A story that does the job (2 of 2)',
    mdN2='112 words in total. Note <em>any</em> in the negative, <em>one</em> '
         'twice, and three irregular pasts — <em>gave</em>, <em>went</em>, '
         '<em>had</em>. The old model was 99 words and never showed '
         '<em>one</em> at all.',
    ecE='Hour 5 &middot; Before the mock test',
    ecT='The five mistakes the error-correction section tests',
    ec1h='The -s, and don\'t / doesn\'t',
    ec1n='she / he / it → doesn\'t. Everyone else → don\'t.',
    ec2h='The base verb after did',
    ec2n='Never <em>did she went</em>. The past is inside <em>did</em>.',
    ec3h='any in negatives, ones for plurals',
    ec3n='And <em>Look!</em> always forces the progressive. Five rules — that is '
         'the whole section.',

    v5E='Mock test &middot; Section 1', v5T='Vocabulary',
    v5Hint='No word bank this time — this is the test.',
    g5E='Mock test &middot; Section 2', g5T='Grammar',
    r3E='Mock test &middot; Section 3', r3T='The space camp',
    r3N='Three questions follow. Underline first.',
    r3qE='Mock test &middot; Section 3', r3qT='True or false?',
    r3gE='Mock test &middot; Section 3', r3gT='Complete from the text',
    e5E='Mock test &middot; Section 4', e5T='Error correction',
    e5Hint='Each sentence has one mistake. Write the correction only.',
    s5E='Mock test &middot; Section 5',
    s5T='some &middot; any &middot; one &middot; ones',
    r4E='Mock test &middot; Section 6', r4T='The space museum',
    r4N='Four questions follow — two true/false, one gap and one multiple '
        'choice.',
    r4qE='Mock test &middot; Section 6', r4qT='True or false?',
    r4gE='Mock test &middot; Section 6', r4gT='Complete from the text',
    r4mE='Mock test &middot; Section 6', r4mT='Why?',

    actTitle='The Alien in the Restaurant', actUse='Use at least four:',
    actWriteKind='Writing &middot; 100–120 words',
    actSpeakBrief='One of you is the waiter. The other has brought an alien to '
                  'dinner.',
    actSpeak1='Waiter: offer four things, every offer with <em>some</em>. Two of '
              'them have run out — say so with <em>any</em>.',
    actSpeak2='Customer: order using <em>one</em> and <em>ones</em> at least '
              'once each. Do not repeat the noun.',
    actSpeak3='Both: the alien does not like the first dish. Sort it out without '
              'either of you being rude.',
    actSpeak4='Both: tell the story afterwards in the past simple, in six '
              'sentences, starting with a time marker.',
    actWriteBrief='Write "The Alien in the Restaurant". Check it against the '
                  'model: a time marker to open, some and any used correctly, '
                  'one or ones once, three irregular past verbs, and a real '
                  'ending.',
    actPlaceholder='Last Saturday, an alien came into our restaurant. Suddenly, …',
    resPerfect='Full marks on the mock. You are ready for the real thing.',
    resStrong='Strong. Look at which section your misses came from and read that '
              'hour again — the mock is a diagnosis, not a verdict.',
    resMid='A solid pass. Sections 4 and 5 are usually where the marks are: five '
           'rules, and they are all on the slide before the mock.',
    resLow='Go back to Hour 4 and read the two some/any slides and the one/ones '
           'slide again, then run the mock a second time.',
)

T['de'] = dict(
    coverTitle='Out of <em>This World</em>',
    coverSub='Teil II: some und any, one und ones, Lesetechnik und der '
             'Übungstest',
    chipLevel='A1+ / A2 &middot; Teil II', chipFocus='Stunden 4&ndash;5',
    chipCount='50 Folien',

    saE='Stunde 4 &middot; some oder any',
    saT='Die Regel — und dann die Ausnahme',
    sa1h='Bejahter Satz → some', sa1n='Das ändert sich nie.',
    sa2h='Verneinung → any',
    sa2n='Nach <em>not</em>, <em>isn\'t</em>, <em>don\'t</em> — immer '
         '<em>any</em>.',
    sa3h='Frage → any',
    sa3n='Wenn du die Antwort wirklich nicht kennst. Lies weiter — auf der '
         'nächsten Folie kommt der Fall, über den alle stolpern.',
    sbE='Stunde 4 &middot; Der Fall, über den alle stolpern',
    sbT='Angebote und Bitten nehmen some — auch als Frage',
    sb1h='Ein Angebot',
    sb1n='Du gibst etwas, du fragst nicht. <em>Would you like…?</em> ist immer '
         'ein Angebot.',
    sb2h='Eine Bitte',
    sb2n='Du bittest um eine Sache und fragst nicht, ob es sie gibt.',
    sb3h='Die Überschneidung',
    sb3n='Im Café ist das eigentlich eine Bitte, also klingen beide natürlich. '
         'In der Arbeit ist <em>any</em> bei einer echten Frage die sichere '
         'Antwort — aber jetzt weißt du, warum man beides hört.',
    ooE='Stunde 4 &middot; one oder ones',
    ooT='Damit du das Nomen nicht zweimal sagen musst',
    oo1h='one — Einzahl', oo1n='Eine Sache.',
    oo2h='ones — Mehrzahl',
    oo2n='Mehr als eine Sache. Shoes, glasses, trousers und jeans stehen im '
         'Englischen immer in der Mehrzahl.',
    oo3h='So entscheidest du',
    oo3n='Die Frage sagt es dir. <em>Which shoes…?</em> → Mehrzahl → '
         '<em>ones</em>. Sonst entscheidet nichts.',
    rmE='Stunde 4 &middot; Lesetechnik',
    rmT1='Bevor du die Fragen liest (1 von 2)',
    rmT2='Und dann antworten (2 von 2)',
    rm1h='1 &middot; Lies die Überschrift',
    rm2h='2 &middot; Schau dir das Bild an',
    rm3h='3 &middot; Unterstreiche die Fakten',
    rm3n='Fast jede Richtig/Falsch-Aufgabe entscheidet sich an einer davon. '
         'Unterstreiche sie, und die Antworten stehen schon auf dem Blatt.',
    rm4h='4 &middot; Lies die Frage zweimal',
    rm5h='5 &middot; Finde die Zeile',
    rm5n='Wenn du die Zeile nicht findest, ist deine Antwort geraten. Eine '
         'Antwort, die „richtig klingt“, ist die klassische Falle.',
    rm6h='6 &middot; Ganzer Satz, wenn verlangt',
    rm6n='Steht in der Aufgabe <em>in full sentences</em>, bringt ein einzelnes '
         'Wort keine Punkte — so richtig es auch ist.',

    sgE='Stunde 4 &middot; Aufgabe 1', sgT='some oder any?',
    sgHint='Entscheide zuerst, was der Satz tut: feststellen, verneinen, fragen, '
           'anbieten.',
    ogE='Stunde 4 &middot; Aufgabe 2', ogT='one oder ones?',
    ogHint='Schau in der Frage nach, welches Nomen gemeint ist.',
    r1E='Stunde 4 &middot; Lesetext 1', r1T='Mias Restaurantbesuch',
    r1N='Unterstreiche die Namen, das Essen und das Wort <em>left</em>, bevor du '
        'weiterklickst.',
    tf1E='Stunde 4 &middot; Aufgabe 3', tf1T='Richtig oder falsch?',
    fsE='Stunde 4 &middot; Ganze Sätze', fsT='So sieht eine ganze Antwort aus',
    fs1h='Where did Mia go yesterday?',
    fs1n='Die Antwort benutzt die Wörter der Frage wieder. Das ist die ganze '
         'Technik.',
    fs2h='What did her brother eat?',
    fs2n='Frage in der Vergangenheit → Antwort in der Vergangenheit. '
         '<em>Ate</em>, nicht <em>eat</em>.',
    fs3h='What did they buy later?',
    fs3n='Nicht „ice cream“. Ein ganzer Satz braucht Subjekt und Verb.',
    dgE='Stunde 4 &middot; Aufgabe 4', dgT='Im Restaurant — some oder any?',
    dgHint='Achte darauf, wer spricht. Die Bedienung bietet an, der Gast fragt.',
    doE='Stunde 4 &middot; Aufgabe 5', doT='Im Geschäft — one oder ones?',
    doHint='Die Frage der Verkäuferin verrät dir Einzahl oder Mehrzahl.',
    r2E='Stunde 4 &middot; Lesetext 2', r2T='Emmas Restaurantbesuch',
    r2N='Achte auf den Wochentag, die zwei Gerichte und die Wörter '
        '<em>left</em>, <em>small</em> und <em>large</em>.',
    tf2E='Stunde 4 &middot; Aufgabe 6', tf2T='Richtig oder falsch?',
    r5E='Stunde 4 &middot; Aufgabe 6', r5T='Ergänze aus dem Text',
    mxE='Stunde 4 &middot; Aufgabe 7', mxT='Gemischt: some, any, one, ones',
    mxHint='Jetzt sind alle vier im Spiel. Entscheide erst, was der Satz tut, '
           'dann ob die Sache Einzahl oder Mehrzahl ist.',

    stE='Stunde 5 &middot; Angeleitetes Schreiben',
    stT='Der Aufbau einer Geschichte, die Punkte bringt',
    st1h='Anfang',
    st1n='Zwei Sätze reichen. Beginne mit einer Zeitangabe — dann weiß die '
         'Lehrkraft sofort, dass du das kannst.',
    st2h='Mitte, dann das Problem',
    st2n='Eine Geschichte ohne Problem ist eine Aufzählung. Das Problem hält die '
         'Lesenden bei der Stange.',
    st3h='Schluss',
    st3n='Schreib sie zu Ende. Eine unfertige Geschichte kostet Punkte, auch '
         'wenn jeder Satz darin richtig ist.',
    phE='Stunde 5 &middot; Angeleitetes Schreiben',
    phT='Wendungen, die den Text zusammenhalten',
    ph1h='Zum Anfangen', ph2h='Zum Weitererzählen',
    ph3h='Für die Überraschung und den Schluss',
    ph3n='Drei oder vier im ganzen Text. Zehn sind schlechter als drei — dann '
         'ist es keine Geschichte mehr, sondern eine Liste von Bindewörtern.',
    mdE='Stunde 5 &middot; Modelltext',
    mdT1='Eine Geschichte, die funktioniert (1 von 2)',
    mdN1='Fett markiert jeden Punkt der Checkliste an der Stelle, an der er '
         'vorkommt: Zeitangabe am Anfang, <em>some</em> und <em>suddenly</em> '
         'für die Überraschung.',
    mdT2='Eine Geschichte, die funktioniert (2 von 2)',
    mdN2='Insgesamt 112 Wörter. Beachte <em>any</em> in der Verneinung, zweimal '
         '<em>one</em> und drei unregelmäßige Vergangenheitsformen — '
         '<em>gave</em>, <em>went</em>, <em>had</em>. Der alte Modelltext hatte '
         '99 Wörter und zeigte <em>one</em> überhaupt nicht.',
    ecE='Stunde 5 &middot; Vor dem Übungstest',
    ecT='Die fünf Fehler, die im Korrekturteil abgefragt werden',
    ec1h='Das -s und don\'t / doesn\'t',
    ec1n='she / he / it → doesn\'t. Alle anderen → don\'t.',
    ec2h='Die Grundform nach did',
    ec2n='Niemals <em>did she went</em>. Die Vergangenheit steckt in '
         '<em>did</em>.',
    ec3h='any bei Verneinung, ones bei Mehrzahl',
    ec3n='Und <em>Look!</em> erzwingt immer das Progressive. Fünf Regeln — mehr '
         'ist der ganze Teil nicht.',

    v5E='Übungstest &middot; Teil 1', v5T='Wortschatz',
    v5Hint='Diesmal ohne Wortliste — das hier ist der Test.',
    g5E='Übungstest &middot; Teil 2', g5T='Grammatik',
    r3E='Übungstest &middot; Teil 3', r3T='Das Weltraumcamp',
    r3N='Es folgen drei Fragen. Erst unterstreichen.',
    r3qE='Übungstest &middot; Teil 3', r3qT='Richtig oder falsch?',
    r3gE='Übungstest &middot; Teil 3', r3gT='Ergänze aus dem Text',
    e5E='Übungstest &middot; Teil 4', e5T='Fehlerkorrektur',
    e5Hint='In jedem Satz steckt ein Fehler. Schreibe nur die Korrektur.',
    s5E='Übungstest &middot; Teil 5',
    s5T='some &middot; any &middot; one &middot; ones',
    r4E='Übungstest &middot; Teil 6', r4T='Das Weltraummuseum',
    r4N='Es folgen vier Fragen — zwei richtig/falsch, eine Lücke und eine '
        'Auswahlfrage.',
    r4qE='Übungstest &middot; Teil 6', r4qT='Richtig oder falsch?',
    r4gE='Übungstest &middot; Teil 6', r4gT='Ergänze aus dem Text',
    r4mE='Übungstest &middot; Teil 6', r4mT='Warum?',

    actTitle='The Alien in the Restaurant',
    actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben &middot; 100–120 Wörter',
    actSpeakBrief='Eine Person ist die Bedienung. Die andere hat einen '
                  'Außerirdischen zum Essen mitgebracht.',
    actSpeak1='Bedienung: Biete vier Dinge an, jedes Angebot mit <em>some</em>. '
              'Zwei davon sind aus — sag das mit <em>any</em>.',
    actSpeak2='Gast: Bestelle und benutze <em>one</em> und <em>ones</em> je '
              'mindestens einmal. Wiederhole das Nomen nicht.',
    actSpeak3='Beide: Dem Außerirdischen schmeckt das erste Gericht nicht. Klärt '
              'das, ohne dass jemand unhöflich wird.',
    actSpeak4='Beide: Erzählt die Geschichte danach im Past Simple, in sechs '
              'Sätzen, beginnend mit einer Zeitangabe.',
    actWriteBrief='Schreibe „The Alien in the Restaurant“. Prüfe deinen Text am '
                  'Modell: Zeitangabe am Anfang, some und any richtig benutzt, '
                  'einmal one oder ones, drei unregelmäßige '
                  'Vergangenheitsformen und ein richtiger Schluss.',
    actPlaceholder='Last Saturday, an alien came into our restaurant. Suddenly, …',
    resPerfect='Volle Punktzahl im Übungstest. Du bist bereit für die echte '
               'Arbeit.',
    resStrong='Stark. Schau nach, aus welchem Teil deine Fehler kamen, und lies '
              'die Stunde noch einmal — der Übungstest ist eine Diagnose, kein '
              'Urteil.',
    resMid='Sicher bestanden. Teil 4 und 5 sind meistens die Punktebringer: fünf '
           'Regeln, und die stehen alle auf der Folie vor dem Übungstest.',
    resLow='Geh zurück zu Stunde 4 und lies die beiden some/any-Folien und die '
           'one/ones-Folie noch einmal, dann mach den Übungstest ein zweites '
           'Mal.',
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
