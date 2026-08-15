# -*- coding: utf-8 -*-
"""Interface strings for Out of This World Part I, English and German.

The learner is a German school student, so the German is the working
language of the interface and every instruction and rule statement is
translated. What is never translated is the English being taught —
question stems, options, gap sentences, word banks and the target-language
chips all stay in English, because translating them would remove the
lesson.
"""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Out of <em>This World</em>',
    coverSub='Five hours to your English test — Part I: strategy, vocabulary and '
             'the two present tenses',
    chipLevel='A1+ / A2 &middot; Part I', chipFocus='Hours 1&ndash;3',
    chipCount='69 slides',

    mapE='Before you start', mapT='What is in the test?',
    mapN1='Getting this wrong costs marks you already knew how to earn.',
    mapN2='This is the largest part of the paper.',
    mapN3='Part II covers this in full.',
    planE='Your flight plan', planT='Three hours in this part',
    planN1='You will understand what an instruction is asking for, and know the '
           'space and food words by heart.',
    planN2='You will make statements, negatives and questions, and choose '
           'between the two tenses on purpose.',
    planN3='You will tell a finished story in the right order, and ask questions '
           'about it.',

    goldE='Hour 1 &middot; Test strategy', goldT='Read the instruction like a sat-nav',
    gold1h='Step 1 &mdash; find the verb',
    gold1n='The verb tells you what to <em>do</em>. Nothing else in the '
           'instruction does.',
    gold2h='Step 2 &mdash; find the target',
    gold2n='The target tells you what the examiner is looking for. Miss it and a '
           'correct sentence still scores nothing.',
    gold3h='Worked example',
    gold3n='Verb: complete. Target: past simple. Now you know both what to do and '
           'what to use.',
    u8E='Hour 1 &middot; Unit 8 words',
    u8T1='Science fiction (1 of 2)', u8T2='Science fiction (2 of 2)',
    catE='Hour 1 &middot; Food groups', catT='Meat, fruit, vegetable',
    cat1h='Meat &mdash; Fleisch',
    cat1n='Beef is from a cow, chicken from a bird, lamb from a young sheep.',
    cat2h='Fruit &mdash; Obst', cat2n='Sweet, and usually eaten raw.',
    cat3h='Vegetable &mdash; Gemüse',
    cat3n='Usually cooked, and not sweet. This is the group German learners lose '
          'marks on.',
    u9E='Hour 1 &middot; Unit 9 words', u9T1='Food (1 of 2)', u9T2='Food (2 of 2)',
    exE='Hour 1 &middot; Also on the menu',
    exT='Words the test uses that the word list forgot',

    vE='Hour 1 &middot; Activity 1', vT='Click the word that tells you what to do',
    fE='Hour 1 &middot; Activity 2', fT='Complete the sentence',
    fHint='Five words in the bank, five gaps. Each is used once.',
    cE='Hour 1 &middot; Activity 3', cT='Meat, fruit or vegetable?',
    cHint='Type one word: meat, fruit or vegetable.',
    oE='Hour 1 &middot; Activity 4', oT='Odd one out',
    tfE='Hour 1 &middot; Activity 5', tfT='True or false?',
    mE='Hour 1 &middot; Activity 6', mT='Complete the restaurant menu',
    mHint='Each word is used once. The clue after the dash tells you which one.',
    bankLabel='Word bank:',

    psE='Hour 2 &middot; Present simple',
    psT='Habits, and things that are always true',
    ps1h='Positive', ps1n='She, he and it add <em>-s</em>. Nothing else does.',
    ps2h='Negative', ps2n='The verb after don\'t / doesn\'t is always basic.',
    ps3h='Question',
    ps3n='Signal words: usually, often, sometimes, never, every day, on Mondays.',
    ppE='Hour 2 &middot; Present progressive', ppT='Happening right now',
    pp1h='Positive', pp1n='am / is / are, then the verb with <em>-ing</em>.',
    pp2h='Negative',
    pp2n='Only <em>am / is / are</em> changes. The <em>-ing</em> word never does.',
    pp3h='Question',
    pp3n='Signal words: now, at the moment, today, right now, Look!, Listen!',
    chE='Hour 2 &middot; The decision', chT='Which tense, and how you know',
    ch1h='Again and again → simple',
    ch1n='A habit, a routine, or something always true. It does not matter what '
         'is happening as you read.',
    ch2h='At this moment → progressive',
    ch2n='It is happening as you speak. Look! and Listen! are the clearest '
         'signals in the exam.',
    ch3h='Find the signal first',
    ch3n='Read the sentence for a time word before you look at the verb. The '
         'time word decides, every time.',
    ssE='Hour 2 &middot; Spelling', ssT='How she / he / it gets its -s',
    ss1h='Most verbs: add -s', ss2h='After -o, -ch, -sh, -ss: add -es',
    ss3h='Consonant + y: -y becomes -ies',
    ss3n='But <em>play → plays</em>: there is a vowel before the y, so nothing '
         'changes.',
    igE='Hour 2 &middot; Spelling', igT='Making the -ing form',
    ig1h='Most verbs: add -ing', ig2h='Ends in -e: drop the -e',
    ig2n='Never <em>makeing</em>. This one is tested.',
    ig3h='Short word, one consonant: double it',

    e2E='Hour 2 &middot; Activity 1', e2T='Fix the mistake',
    e2Hint='Each sentence has one mistake. Write only the missing part.',
    tnE='Hour 2 &middot; Activity 2', tnT='Simple or progressive?',
    tnHint='Find the time word first — it decides the tense.',
    paE='Hour 2 &middot; Activity 3', paT='Mia\'s Saturday — present simple',
    paHint='Use the present simple form of the verb in brackets.',
    pgE='Hour 2 &middot; Activity 4', pgT='Write the progressive form',
    pgHint='am / is / are, then the verb with -ing. Short forms are fine.',
    ngE='Hour 2 &middot; Activity 5', ngT='Make it negative',
    ngHint='don\'t or doesn\'t, then the basic verb. Full forms are accepted too.',
    mtE='Hour 2 &middot; Activity 6',
    mtT='Match the verb to its she / he / it form',
    mtHint='Click a verb, then click the form that goes with she, he or it.',

    reE='Hour 3 &middot; Past simple', reT='Most verbs simply take -ed',
    re1h='The rule',
    re1n='This covers most verbs in the language. Learn it first, then learn the '
         'exceptions.',
    re2h='Small spelling changes',
    re2n='Ends in -e: add only -d. Short word with one consonant: double it.',
    re3h='Some verbs change completely',
    re3n='These are the irregular verbs. There is no rule for them — the next two '
         'slides are the ones to learn.',
    irE='Hour 3 &middot; Irregular verbs',
    irT1='The thirteen you must know (1 of 2)',
    irT2='The thirteen you must know (2 of 2)',
    ddE='Hour 3 &middot; Negatives and questions',
    ddT='After did and didn\'t, the verb goes basic',
    dd1h='Positive', dd2h='Negative',
    dd2n='Not <em>didn\'t watched</em>. The past is already inside '
         '<em>didn\'t</em>.',
    dd3h='Question',
    dd3n='Not <em>Did you watched?</em> — same reason. This is the single most '
         'tested rule in Hour 3.',
    tkE='Hour 3 &middot; Time markers',
    tkT='The words that put a sentence in the past',
    tk1h='Pointing back from now',
    tk1n='German: gestern, letzte Woche, vor zwei Tagen.',
    tk2h='Moving the story on',
    tk2n='These count from the last event, not from now.',
    tk3h='suddenly = unexpectedly',
    tk3n='German <em>plötzlich</em>. It does <em>not</em> mean quickly — it means '
         'nobody saw it coming.',

    pvE='Hour 3 &middot; Activity 1', pvT='Write the past form',
    pvHint='Careful — not every verb here is irregular.',
    m3E='Hour 3 &middot; Activity 2', m3T='Match the verb to its past form',
    m3Hint='Click a verb, then click its past form.',
    e3E='Hour 3 &middot; Activity 3', e3T='Fix the mistake',
    e3Hint='Write only the missing verb.',
    orE='Hour 3 &middot; Activity 4', orT='Put Tom\'s story in order',
    orHint='Click the sentences in the order they happened.',
    stE='Hour 3 &middot; Activity 5', stT='The bright light — past simple',
    stHint='Use the past simple of the verb in brackets.',
    qE='Hour 3 &middot; Activity 6', qT='Write the question',
    qHint='Two gaps each: the question word, then the verb.',
    tmE='Hour 3 &middot; Activity 7', tmT='Choose the time marker',

    actTitle='Tell it, then write it', actUse='Use at least four:',
    actWriteKind='Writing &middot; 100–120 words',
    actSpeakBrief='One of you saw something strange last night. The other is the '
                  'reporter.',
    actSpeak1='Reporter: ask four questions with <em>Did you…?</em> Every verb '
              'after <em>did</em> stays basic.',
    actSpeak2='Witness: tell what happened, in order. Use <em>suddenly</em> once '
              'and <em>the next morning</em> once.',
    actSpeak3='Witness: say one thing you do <em>every day</em>, and one thing '
              'that is happening <em>right now</em>.',
    actSpeak4='Both: agree on one sentence for the newspaper, in the past simple, '
              'under twelve words.',
    actWriteBrief='Write the story of a strange night. Start with a time marker, '
                  'keep it in the past simple, and use at least three irregular '
                  'verbs.',
    actPlaceholder='Last night, I went into the garden. Suddenly, …',
    resPerfect='Full marks. You are ready for Hours 4 and 5.',
    resStrong='Strong. Go back over the items you missed, then start Part II.',
    resMid='A good base. The irregular verbs and the simple/progressive choice '
           'are where the misses cluster — read those slides again.',
    resLow='Read the teaching slides once more, then run it again. Every rule you '
           'need is on them, before the practice starts.',
)

T['de'] = dict(
    coverTitle='Out of <em>This World</em>',
    coverSub='Fünf Stunden bis zur Englischarbeit — Teil I: Strategie, Wortschatz '
             'und die zwei Präsensformen',
    chipLevel='A1+ / A2 &middot; Teil I', chipFocus='Stunden 1&ndash;3',
    chipCount='69 Folien',

    mapE='Bevor es losgeht', mapT='Was kommt in der Arbeit dran?',
    mapN1='Hier Punkte zu verlieren tut besonders weh — du hättest sie gekonnt.',
    mapN2='Das ist der größte Teil der Arbeit.',
    mapN3='Teil II behandelt das vollständig.',
    planE='Dein Flugplan', planT='Drei Stunden in diesem Teil',
    planN1='Du verstehst, was eine Aufgabenstellung von dir will, und kannst die '
           'Weltraum- und Essenswörter auswendig.',
    planN2='Du bildest Aussagen, Verneinungen und Fragen und wählst bewusst '
           'zwischen den beiden Zeiten.',
    planN3='Du erzählst eine abgeschlossene Geschichte in der richtigen '
           'Reihenfolge und stellst Fragen dazu.',

    goldE='Stunde 1 &middot; Prüfungsstrategie',
    goldT='Lies die Aufgabenstellung wie ein Navi',
    gold1h='Schritt 1 &mdash; finde das Verb',
    gold1n='Das Verb sagt dir, was du <em>tun</em> sollst. Sonst nichts in der '
           'Aufgabe.',
    gold2h='Schritt 2 &mdash; finde das Ziel',
    gold2n='Das Ziel sagt dir, worauf die Lehrkraft achtet. Übersiehst du es, '
           'bringt auch ein richtiger Satz keine Punkte.',
    gold3h='Beispiel',
    gold3n='Verb: complete. Ziel: past simple. Jetzt weißt du beides — was zu tun '
           'ist und was du benutzen sollst.',
    u8E='Stunde 1 &middot; Wörter aus Unit 8',
    u8T1='Science-Fiction (1 von 2)', u8T2='Science-Fiction (2 von 2)',
    catE='Stunde 1 &middot; Lebensmittelgruppen', catT='Fleisch, Obst, Gemüse',
    cat1h='Meat &mdash; Fleisch',
    cat1n='Beef kommt vom Rind, chicken vom Huhn, lamb vom jungen Schaf.',
    cat2h='Fruit &mdash; Obst', cat2n='Süß und meistens roh gegessen.',
    cat3h='Vegetable &mdash; Gemüse',
    cat3n='Meistens gekocht und nicht süß. Bei dieser Gruppe verlieren deutsche '
          'Lernende die meisten Punkte.',
    u9E='Stunde 1 &middot; Wörter aus Unit 9',
    u9T1='Essen (1 von 2)', u9T2='Essen (2 von 2)',
    exE='Stunde 1 &middot; Steht auch auf der Karte',
    exT='Wörter, die drankommen, aber in der Liste fehlen',

    vE='Stunde 1 &middot; Aufgabe 1',
    vT='Klicke das Wort an, das dir sagt, was du tun sollst',
    fE='Stunde 1 &middot; Aufgabe 2', fT='Vervollständige den Satz',
    fHint='Fünf Wörter in der Liste, fünf Lücken. Jedes wird einmal gebraucht.',
    cE='Stunde 1 &middot; Aufgabe 3', cT='Fleisch, Obst oder Gemüse?',
    cHint='Schreibe ein Wort: meat, fruit oder vegetable.',
    oE='Stunde 1 &middot; Aufgabe 4', oT='Was passt nicht dazu?',
    tfE='Stunde 1 &middot; Aufgabe 5', tfT='Richtig oder falsch?',
    mE='Stunde 1 &middot; Aufgabe 6', mT='Vervollständige die Speisekarte',
    mHint='Jedes Wort wird einmal gebraucht. Der Hinweis nach dem Gedankenstrich '
          'verrät dir, welches.',
    bankLabel='Wortliste:',

    psE='Stunde 2 &middot; Present Simple',
    psT='Gewohnheiten und Dinge, die immer gelten',
    ps1h='Aussage',
    ps1n='She, he und it bekommen ein <em>-s</em>. Sonst niemand.',
    ps2h='Verneinung',
    ps2n='Das Verb nach don\'t / doesn\'t steht immer in der Grundform.',
    ps3h='Frage',
    ps3n='Signalwörter: usually, often, sometimes, never, every day, on Mondays.',
    ppE='Stunde 2 &middot; Present Progressive', ppT='Passiert gerade jetzt',
    pp1h='Aussage', pp1n='am / is / are, dann das Verb mit <em>-ing</em>.',
    pp2h='Verneinung',
    pp2n='Nur <em>am / is / are</em> ändert sich. Das <em>-ing</em>-Wort nie.',
    pp3h='Frage',
    pp3n='Signalwörter: now, at the moment, today, right now, Look!, Listen!',
    chE='Stunde 2 &middot; Die Entscheidung',
    chT='Welche Zeit — und woran du es erkennst',
    ch1h='Immer wieder → Simple',
    ch1n='Eine Gewohnheit, ein Ablauf oder etwas immer Gültiges. Es spielt keine '
         'Rolle, was gerade passiert, während du liest.',
    ch2h='Genau jetzt → Progressive',
    ch2n='Es passiert, während du sprichst. Look! und Listen! sind die '
         'deutlichsten Signale in der Arbeit.',
    ch3h='Erst das Signal suchen',
    ch3n='Suche im Satz zuerst ein Zeitwort, bevor du auf das Verb schaust. Das '
         'Zeitwort entscheidet — jedes Mal.',
    ssE='Stunde 2 &middot; Rechtschreibung',
    ssT='Wie she / he / it zu seinem -s kommt',
    ss1h='Die meisten Verben: -s anhängen',
    ss2h='Nach -o, -ch, -sh, -ss: -es anhängen',
    ss3h='Mitlaut + y: aus -y wird -ies',
    ss3n='Aber <em>play → plays</em>: vor dem y steht ein Selbstlaut, also ändert '
         'sich nichts.',
    igE='Stunde 2 &middot; Rechtschreibung', igT='So bildest du die -ing-Form',
    ig1h='Die meisten Verben: -ing anhängen',
    ig2h='Endet auf -e: das -e fällt weg',
    ig2n='Niemals <em>makeing</em>. Das wird abgefragt.',
    ig3h='Kurzes Wort, ein Mitlaut: verdoppeln',

    e2E='Stunde 2 &middot; Aufgabe 1', e2T='Korrigiere den Fehler',
    e2Hint='In jedem Satz steckt ein Fehler. Schreibe nur den fehlenden Teil.',
    tnE='Stunde 2 &middot; Aufgabe 2', tnT='Simple oder Progressive?',
    tnHint='Suche zuerst das Zeitwort — es entscheidet über die Zeit.',
    paE='Stunde 2 &middot; Aufgabe 3', paT='Mias Samstag — Present Simple',
    paHint='Benutze die Present-Simple-Form des Verbs in Klammern.',
    pgE='Stunde 2 &middot; Aufgabe 4', pgT='Schreibe die Progressive-Form',
    pgHint='am / is / are, dann das Verb mit -ing. Kurzformen sind erlaubt.',
    ngE='Stunde 2 &middot; Aufgabe 5', ngT='Verneine den Satz',
    ngHint='don\'t oder doesn\'t, dann die Grundform. Auch die Langform wird '
           'akzeptiert.',
    mtE='Stunde 2 &middot; Aufgabe 6',
    mtT='Ordne dem Verb seine she / he / it-Form zu',
    mtHint='Klicke ein Verb an und dann die Form, die zu she, he oder it passt.',

    reE='Stunde 3 &middot; Past Simple',
    reT='Die meisten Verben bekommen einfach -ed',
    re1h='Die Regel',
    re1n='Das gilt für die meisten Verben der Sprache. Lerne zuerst das, dann die '
         'Ausnahmen.',
    re2h='Kleine Schreibänderungen',
    re2n='Endet auf -e: nur -d anhängen. Kurzes Wort mit einem Mitlaut: '
         'verdoppeln.',
    re3h='Manche Verben ändern sich ganz',
    re3n='Das sind die unregelmäßigen Verben. Für sie gibt es keine Regel — die '
         'nächsten zwei Folien sind zum Lernen da.',
    irE='Stunde 3 &middot; Unregelmäßige Verben',
    irT1='Die dreizehn, die du können musst (1 von 2)',
    irT2='Die dreizehn, die du können musst (2 von 2)',
    ddE='Stunde 3 &middot; Verneinung und Frage',
    ddT='Nach did und didn\'t steht die Grundform',
    dd1h='Aussage', dd2h='Verneinung',
    dd2n='Nicht <em>didn\'t watched</em>. Die Vergangenheit steckt schon in '
         '<em>didn\'t</em>.',
    dd3h='Frage',
    dd3n='Nicht <em>Did you watched?</em> — gleicher Grund. Das ist die am '
         'häufigsten abgefragte Regel in Stunde 3.',
    tkE='Stunde 3 &middot; Zeitangaben',
    tkT='Die Wörter, die einen Satz in die Vergangenheit setzen',
    tk1h='Zurück von jetzt aus',
    tk1n='Deutsch: gestern, letzte Woche, vor zwei Tagen.',
    tk2h='Die Geschichte weitertragen',
    tk2n='Diese zählen ab dem letzten Ereignis, nicht ab jetzt.',
    tk3h='suddenly = unerwartet',
    tk3n='Deutsch <em>plötzlich</em>. Es heißt <em>nicht</em> „schnell“ — es '
         'heißt, dass niemand damit gerechnet hat.',

    pvE='Stunde 3 &middot; Aufgabe 1', pvT='Schreibe die Vergangenheitsform',
    pvHint='Vorsicht — nicht jedes Verb hier ist unregelmäßig.',
    m3E='Stunde 3 &middot; Aufgabe 2',
    m3T='Ordne dem Verb seine Vergangenheitsform zu',
    m3Hint='Klicke ein Verb an und dann seine Vergangenheitsform.',
    e3E='Stunde 3 &middot; Aufgabe 3', e3T='Korrigiere den Fehler',
    e3Hint='Schreibe nur das fehlende Verb.',
    orE='Stunde 3 &middot; Aufgabe 4',
    orT='Bringe Toms Geschichte in die richtige Reihenfolge',
    orHint='Klicke die Sätze in der Reihenfolge an, in der sie passiert sind.',
    stE='Stunde 3 &middot; Aufgabe 5', stT='Das helle Licht — Past Simple',
    stHint='Benutze das Past Simple des Verbs in Klammern.',
    qE='Stunde 3 &middot; Aufgabe 6', qT='Schreibe die Frage',
    qHint='Zwei Lücken pro Satz: erst das Fragewort, dann das Verb.',
    tmE='Stunde 3 &middot; Aufgabe 7', tmT='Wähle die richtige Zeitangabe',

    actTitle='Erst erzählen, dann schreiben', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben &middot; 100–120 Wörter',
    actSpeakBrief='Eine Person hat letzte Nacht etwas Seltsames gesehen. Die '
                  'andere ist von der Zeitung.',
    actSpeak1='Zeitung: Stelle vier Fragen mit <em>Did you…?</em> Jedes Verb nach '
              '<em>did</em> bleibt in der Grundform.',
    actSpeak2='Zeugin/Zeuge: Erzähle der Reihe nach, was passiert ist. Benutze '
              'einmal <em>suddenly</em> und einmal <em>the next morning</em>.',
    actSpeak3='Zeugin/Zeuge: Nenne eine Sache, die du <em>jeden Tag</em> machst, '
              'und eine, die <em>gerade jetzt</em> passiert.',
    actSpeak4='Beide: Einigt euch auf einen Satz für die Zeitung, im Past Simple, '
              'unter zwölf Wörtern.',
    actWriteBrief='Schreibe die Geschichte einer seltsamen Nacht. Beginne mit '
                  'einer Zeitangabe, bleibe im Past Simple und benutze '
                  'mindestens drei unregelmäßige Verben.',
    actPlaceholder='Last night, I went into the garden. Suddenly, …',
    resPerfect='Volle Punktzahl. Du bist bereit für Stunde 4 und 5.',
    resStrong='Stark. Schau dir die verpassten Aufgaben noch einmal an und starte '
              'dann Teil II.',
    resMid='Gute Grundlage. Die unregelmäßigen Verben und die Wahl zwischen '
           'Simple und Progressive sind die Stellen mit den meisten Fehlern — '
           'lies die Folien dazu noch einmal.',
    resLow='Lies die Erklärfolien noch einmal und starte neu. Jede Regel, die du '
           'brauchst, steht dort — vor den Übungen.',
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
