# -*- coding: utf-8 -*-
"""Interface strings for the A2 Alcatraz escape-room deck.

All ten languages, complete. The generic chrome is lifted verbatim from
`chrome_i18n.py` rather than retranslated.

Scope boundary, per the house style: the app's own chrome translates,
the English being taught does not. Question stems, options, gap
sentences, word banks, sorting items, the object names on the search
slides and the activation chips stay in English in every language.

One deliberate departure from the B2 decks. `deck.teach` now takes an
optional key for a card's *body* as well as its heading, and this lesson
uses it. At A2 a learner cannot read a rule stated only in English —
that is the level's whole problem — so the rules translate and only the
worked examples inside them stay English. The examples are the lesson.

`build_alcatraz.py` reads T['en'] directly, so a slide and its English
string cannot drift apart: there is one copy of each.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'btnOpen',
        'scoreLabel', 'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer',
        'resNext', 'actEyebrow', 'actSpeakKind', 'btnCopy', 'btnCopied',
        'wordCount']

T = {}

T['en'] = dict(
    # ── cover ──
    coverTitle='Escape from <em>Alcatraz</em>',
    coverSub='Five locked rooms, five pieces of English. Find the numbers, '
             'open the last gate.',
    chipLevel='A2 &middot; Elementary',
    chipFocus='Escape room',
    chipTime='50&ndash;60 minutes',
    chipCount='NN slides',

    # ── the rail ──
    railStops='Cell|Corridor|Shop|Workshop|Water',

    # ── eyebrows ──
    eIsland='Before you start',
    eCell='Room 1 &middot; Your cell',
    eCorridor='Room 2 &middot; The corridor',
    eShop='Room 3 &middot; The barber shop',
    eWork='Room 4 &middot; The workshop',
    eWater='Room 5 &middot; The water',
    eLock='The last gate',
    eFind='Find it &middot; against the clock',

    # ── orientation ──
    t1='Welcome to The Rock',
    h1a='Alcatraz was a prison on a small island in San Francisco Bay. It '
        'opened in 1934 and closed in 1963.',
    b1a='The island is about 1.25 miles (2 km) from the city. People called '
        'it <strong>The Rock</strong>.',
    h1b='In twenty-nine years there were fourteen escape attempts. No '
        'prisoner is officially recorded as escaping successfully.',
    b1b='The water is cold &mdash; about 10&ndash;13&deg;C &mdash; and the '
        'currents are <strong>strong</strong>.',
    n1='One man, John Paul Scott, did reach land by swimming in December '
       '1962. He was found on the shore, cold and exhausted, and taken back.',

    t2='Tonight you are going to leave',
    h2a='You are a prisoner in B Block. Tonight you have one night and five '
        'rooms: your cell, the corridor, the barber shop, the workshop and '
        'the water.',
    b2a='In every room you find <strong>one number</strong>. The five '
        'numbers open the last gate.',
    h2b='The rail at the bottom of the screen remembers the numbers for '
        'you, so you can think about the English instead.',
    b2b='Some rooms have a clock. When you see the clock, look '
        '<strong>fast</strong>.',
    n2='Everything in this lesson happened on a real island. The prisoner '
       'is invented; the escape in 1962 was not.',

    # ── room 1: prepositions of place ──
    t3='Where is it? in, on, under, behind',
    h3a='Use these words to say where something is: <strong>in, on, under, '
        'behind, next to, between, above</strong>.',
    b3a='The spoon is <strong>under</strong> the bed. The vent is '
        '<strong>behind</strong> the sink. The photo is <strong>on</strong> '
        'the wall.',
    h3b='After the preposition comes <em>the</em> and the thing. Never add '
        '<em>to</em>.',
    b3b='&#10003; The light is <strong>above the</strong> door.<br>'
        '&#10007; The light is above <em>to</em> the door.',
    n3='<em>Next to</em> is two words. <em>Between</em> needs two things and '
       'the word <em>and</em>.',
    t4='Say where it is',
    t5='Two things, one word',
    t6='Write the missing word',
    t7='Something to dig with',

    # ── room 2: there is / there are ──
    t8='There is one. There are two.',
    h8a='One thing: <strong>There is</strong>. More than one: <strong>There '
        'are</strong>.',
    b8a='There <strong>is</strong> a ladder. There <strong>are</strong> '
        'three pipes.',
    h8b='Questions and negatives keep the same pattern.',
    b8b='<strong>Is there</strong> a guard? &mdash; No, there '
        '<strong>isn&rsquo;t</strong>. <strong>Are there</strong> any '
        'lights? &mdash; No, there <strong>aren&rsquo;t</strong>.',
    n8='Water, air, noise and light have no plural form: say <em>there is '
       'some water</em>, never <em>there are some waters</em>.',
    t9='One or more than one?',
    t10='Write the missing word',
    t11='Put each one in its box',
    t12='Something to see with',

    # ── room 3: past simple ──
    t13='What they did: the past simple',
    h13a='For finished actions in the past, use the past simple. Many '
         'common verbs are irregular, so you have to learn them.',
    b13a='make &rarr; <strong>made</strong> &middot; take &rarr; '
         '<strong>took</strong> &middot; get &rarr; <strong>got</strong> '
         '&middot; go &rarr; <strong>went</strong> &middot; put &rarr; '
         '<strong>put</strong> &middot; cut &rarr; <strong>cut</strong>',
    h13b='In negatives and questions use <em>did</em>, and then the base '
         'form of the verb.',
    b13b='They <strong>didn&rsquo;t take</strong> the boat. '
         '<strong>Did</strong> they <strong>make</strong> a raft?',
    n13='After <em>did</em> and <em>didn&rsquo;t</em>, never use the past '
        'form. <em>Did they took&hellip;</em> is wrong.',

    t14='June 1962',
    h14a='In June 1962 three men left Alcatraz: Frank Morris and the '
         'brothers John and Clarence Anglin. A fourth man, Allen West, '
         'stayed behind.',
    b14a='They <strong>made</strong> false heads from paper, paint and real '
         'hair, and <strong>put</strong> them in their beds.',
    h14b='They took more than fifty raincoats and made a rubber boat. Then '
         'they climbed to the roof and went down to the water.',
    b14b='The FBI <strong>looked</strong> for them for seventeen years and '
         '<strong>closed</strong> the case in 1979. Nobody '
         '<strong>found</strong> them.',
    n14='West did not open his vent in time. He stayed in his cell, and '
        'afterwards he told the investigators how the plan worked.',
    t15='Choose the past form',
    t16='Write the missing verb',
    t17='Build the sentence',
    t18='Something to cut with',

    # ── room 4: can / must ──
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = it is possible. <strong>can&rsquo;t</strong> '
         '= it is not possible.',
    b19a='You <strong>can</strong> hear the guard on the stairs. You '
         '<strong>can&rsquo;t</strong> swim in this water for long &mdash; '
         'it is too cold.',
    h19b='<strong>must</strong> = it is necessary. '
         '<strong>mustn&rsquo;t</strong> = it is forbidden.',
    b19b='You <strong>must</strong> be quiet. You '
         '<strong>mustn&rsquo;t</strong> use a light.',
    n19='After all four, use the base verb with no <em>to</em>. <em>You must '
        'to go</em> is wrong.',
    t20='Forbidden, or not necessary?',
    t21='Read the rule',
    t22='Rule or crime?',
    t23='Fifty of these make a boat',

    # ── room 5: comparatives + going to ──
    t24='colder, stronger, more dangerous',
    h24a='Short adjectives take <strong>-er</strong> and then '
         '<strong>than</strong>.',
    b24a='cold &rarr; <strong>colder</strong> &middot; strong &rarr; '
         '<strong>stronger</strong> &middot; safe &rarr; '
         '<strong>safer</strong> &middot; big &rarr; <strong>bigger</strong>',
    h24b='Long adjectives take <strong>more</strong> in front, and '
         '<strong>than</strong> after.',
    b24b='The north shore is <strong>more dangerous than</strong> the east '
         'shore.',
    n24='Two irregular ones you need tonight: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',

    t25='A plan you have already made',
    h25a='For a plan you have already decided, use <strong>be going to</strong> '
         'and then the base verb.',
    b25a='I<strong>&rsquo;m going to</strong> take the paddle. We<strong>'
         '&rsquo;re going to</strong> leave at ten.',
    h25b='The negative and the question change the verb <em>be</em>, and '
         'nothing else.',
    b25b='They<strong>&rsquo;re not going to</strong> wait. '
         '<strong>Are</strong> you <strong>going to</strong> swim?',
    n25='<em>Going to go</em> is correct English, even though it sounds '
        'strange the first time you say it.',
    t26='Compare the two sides',
    t27='Write the missing word',
    t28='Which one is a plan?',
    t29='Something to row with',

    # ── shared activity hints ──
    orderHint='Click the parts in order &middot; click one again to take it '
              'back',
    sortHint='Click a phrase, then click the box it belongs in.',
    bankLabel='Word bank:',

    # ── the final check ──
    eCheck='The check &middot; all five rooms',
    tCheck='The guard is checking the cells',
    hC1='A guard is walking the block with a list. Before you reach the '
        'gate, you have to get past him.',
    bC1='Nine questions. All five rooms, mixed together, and no rule on '
        'the screen this time.',
    hC2='Nothing new is tested here. Every question uses language from a '
        'room you have already been in.',
    bC2='Prepositions &middot; there is / there are &middot; the past '
        'simple &middot; must and mustn&rsquo;t &middot; comparatives and '
        '<em>going to</em>',
    nC='If you lose one, go back to that room and read the rule slide '
       'again before you try the gate.',
    x1='Where is it?',
    x2='One or more than one?',
    x3='What happened?',
    x4='Possible, or forbidden?',
    x5='Compare the two shores',
    x6='Plan or habit?',
    x7='Write the missing words',
    x8='Write the missing words',
    x9='Build the sentence',

    # ── the lock ──
    t30='Five numbers, one gate',
    lockStem='You have one number from every room. This lock takes them '
             '<strong>backwards</strong> &mdash; from the last room to the '
             'first.',
    lockWhy='<strong>Backwards</strong> means from the end to the beginning: '
            'the water first, then the workshop, the shop, the corridor, and '
            'your cell last.',

    # ── results ──
    resPerfect='Every door, first time. You are off the island.',
    resStrong='Strong work. The boat is in the water.',
    resMid='You are out of the cell. Go back through the rooms you lost.',
    resLow='The guards found you before the gate. Read the rule slides again '
           'and start over.',

    # ── activation ──
    actTitle='Tonight, in your own words',
    actUse='Use at least three:',
    actSpeakBrief='One of you is the prisoner, one is the guard. Change '
                  'roles after each prompt.',
    actSpeak1='Guard: ask where five things are in the cell. Prisoner: '
              'answer with under, behind, next to, on and between.',
    actSpeak2='Prisoner: tell your partner the plan for tonight. Say four '
              'things with <em>I am going to</em>.',
    actSpeak3='Guard: give five rules with <em>must</em> and <em>mustn&rsquo;t</em>. '
              'Prisoner: say why one of them is a bad rule.',
    actWriteKind='Writing &middot; 80&ndash;120 words',
    actWriteBrief='You are in the boat. Write a short letter to your family: '
                  'where you were, what you took, what you did, and what you '
                  'are going to do now. Use two comparatives.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does
    # not decode entities — HOUSE-STYLE §13 in its attribute form.
    actPlaceholder='Last night I was in my cell. Under the bed there was …',
)

T['de'] = dict(
    coverTitle='Flucht aus <em>Alcatraz</em>',
    coverSub='Fünf verschlossene Räume, fünf Stück Englisch. Finde die '
             'Zahlen und öffne das letzte Tor.',
    chipLevel='A2 &middot; Grundstufe',
    chipFocus='Escape Room',
    chipTime='50&ndash;60 Minuten',
    chipCount='NN Folien',
    railStops='Zelle|Gang|Laden|Werkstatt|Wasser',
    eIsland='Bevor es losgeht',
    eCell='Raum 1 &middot; Deine Zelle',
    eCorridor='Raum 2 &middot; Der Gang',
    eShop='Raum 3 &middot; Der Friseurladen',
    eWork='Raum 4 &middot; Die Werkstatt',
    eWater='Raum 5 &middot; Das Wasser',
    eLock='Das letzte Tor',
    eFind='Finde es &middot; gegen die Uhr',
    t1='Willkommen auf The Rock',
    h1a='Alcatraz war ein Gefängnis auf einer kleinen Insel in der Bucht von '
        'San Francisco. Es wurde 1934 eröffnet und 1963 geschlossen.',
    b1a='Die Insel liegt etwa 1,25 Meilen (2 km) von der Stadt entfernt. Man '
        'nannte sie <strong>The Rock</strong>.',
    h1b='In neunundzwanzig Jahren gab es vierzehn Fluchtversuche. Offiziell '
        'ist kein Gefangener erfolgreich entkommen.',
    b1b='Das Wasser ist kalt &mdash; etwa 10&ndash;13&nbsp;&deg;C &mdash; und '
        'die Strömungen sind <strong>stark</strong>.',
    n1='Ein Mann, John Paul Scott, erreichte im Dezember 1962 schwimmend das '
       'Festland. Man fand ihn unterkühlt am Ufer und brachte ihn zurück.',
    t2='Heute Nacht gehst du',
    h2a='Du bist Gefangener im B-Block. Du hast eine Nacht und fünf Räume: '
        'deine Zelle, den Gang, den Friseurladen, die Werkstatt und das '
        'Wasser.',
    b2a='In jedem Raum findest du <strong>eine Zahl</strong>. Die fünf Zahlen '
        'öffnen das letzte Tor.',
    h2b='Die Leiste unten merkt sich die Zahlen für dich, damit du an das '
        'Englische denken kannst.',
    b2b='In manchen Räumen läuft eine Uhr. Wenn du die Uhr siehst, schau '
        '<strong>schnell</strong>.',
    n2='Alles hier spielt auf einer echten Insel. Der Gefangene ist erfunden, '
       'die Flucht von 1962 war es nicht.',
    t3='Wo ist es? in, on, under, behind',
    h3a='Mit diesen Wörtern sagst du, wo etwas ist: <strong>in, on, under, '
        'behind, next to, between, above</strong>.',
    b3a='The spoon is <strong>under</strong> the bed. The vent is '
        '<strong>behind</strong> the sink. The photo is <strong>on</strong> '
        'the wall.',
    h3b='Nach der Präposition kommt <em>the</em> und die Sache. Niemals '
        '<em>to</em> dazwischen.',
    b3b='&#10003; The light is <strong>above the</strong> door.<br>'
        '&#10007; The light is above <em>to</em> the door.',
    n3='<em>Next to</em> sind zwei Wörter. <em>Between</em> braucht zwei '
       'Dinge und das Wort <em>and</em>.',
    t4='Sag, wo es ist',
    t5='Zwei Dinge, ein Wort',
    t6='Schreib das fehlende Wort',
    t7='Etwas zum Graben',
    t8='There is eins. There are zwei.',
    h8a='Eine Sache: <strong>There is</strong>. Mehr als eine: '
        '<strong>There are</strong>.',
    b8a='There <strong>is</strong> a ladder. There <strong>are</strong> '
        'three pipes.',
    h8b='Frage und Verneinung folgen demselben Muster.',
    b8b='<strong>Is there</strong> a guard? &mdash; No, there '
        '<strong>isn&rsquo;t</strong>. <strong>Are there</strong> any '
        'lights? &mdash; No, there <strong>aren&rsquo;t</strong>.',
    n8='Wasser, Luft, Lärm und Licht haben keinen Plural: <em>there is some '
       'water</em>, nie <em>there are some waters</em>.',
    t9='Eins oder mehr als eins?',
    t10='Schreib das fehlende Wort',
    t11='Sortiere jedes in seinen Kasten',
    t12='Etwas zum Sehen',
    t13='Was sie taten: das Past Simple',
    h13a='Für abgeschlossene Handlungen in der Vergangenheit nimmst du das '
         'Past Simple. Viele häufige Verben sind unregelmäßig.',
    b13a='make &rarr; <strong>made</strong> &middot; take &rarr; '
         '<strong>took</strong> &middot; get &rarr; <strong>got</strong> '
         '&middot; go &rarr; <strong>went</strong> &middot; put &rarr; '
         '<strong>put</strong> &middot; cut &rarr; <strong>cut</strong>',
    h13b='In Verneinung und Frage steht <em>did</em>, danach der Infinitiv '
         'ohne <em>to</em>.',
    b13b='They <strong>didn&rsquo;t take</strong> the boat. '
         '<strong>Did</strong> they <strong>make</strong> a raft?',
    n13='Nach <em>did</em> und <em>didn&rsquo;t</em> nie die Vergangenheits'
        'form. <em>Did they took&hellip;</em> ist falsch.',
    t14='Juni 1962',
    h14a='Im Juni 1962 verließen drei Männer Alcatraz: Frank Morris und die '
         'Brüder John und Clarence Anglin. Ein vierter, Allen West, blieb '
         'zurück.',
    b14a='They <strong>made</strong> false heads from paper, paint and real '
         'hair, and <strong>put</strong> them in their beds.',
    h14b='Sie nahmen über fünfzig Regenmäntel und bauten daraus ein '
         'Gummiboot. Dann stiegen sie aufs Dach und hinunter zum Wasser.',
    b14b='The FBI <strong>looked</strong> for them for seventeen years and '
         '<strong>closed</strong> the case in 1979. Nobody '
         '<strong>found</strong> them.',
    n14='West bekam sein Lüftungsgitter nicht rechtzeitig auf. Er blieb in '
        'seiner Zelle und erklärte den Ermittlern später den Plan.',
    t15='Wähle die Vergangenheitsform',
    t16='Schreib das fehlende Verb',
    t17='Bau den Satz',
    t18='Etwas zum Schneiden',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = es ist möglich. '
         '<strong>can&rsquo;t</strong> = es ist nicht möglich.',
    b19a='You <strong>can</strong> hear the guard on the stairs. You '
         '<strong>can&rsquo;t</strong> swim in this water for long &mdash; '
         'it is too cold.',
    h19b='<strong>must</strong> = es ist notwendig. '
         '<strong>mustn&rsquo;t</strong> = es ist verboten.',
    b19b='You <strong>must</strong> be quiet. You '
         '<strong>mustn&rsquo;t</strong> use a light.',
    n19='Nach allen vieren steht der Infinitiv ohne <em>to</em>. <em>You must '
        'to go</em> ist falsch.',
    t20='Verboten oder nicht nötig?',
    t21='Lies die Vorschrift',
    t22='Vorschrift oder Vergehen?',
    t23='Fünfzig davon ergeben ein Boot',
    t24='colder, stronger, more dangerous',
    h24a='Kurze Adjektive bekommen <strong>-er</strong> und danach '
         '<strong>than</strong>.',
    b24a='cold &rarr; <strong>colder</strong> &middot; strong &rarr; '
         '<strong>stronger</strong> &middot; safe &rarr; '
         '<strong>safer</strong> &middot; big &rarr; <strong>bigger</strong>',
    h24b='Lange Adjektive bekommen <strong>more</strong> davor und '
         '<strong>than</strong> danach.',
    b24b='The north shore is <strong>more dangerous than</strong> the east '
         'shore.',
    n24='Zwei unregelmäßige, die du heute Nacht brauchst: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='Ein Plan, den du schon gefasst hast',
    h25a='Für einen schon gefassten Plan nimmst du <strong>be going to</strong> '
         'und danach den Infinitiv.',
    b25a='I<strong>&rsquo;m going to</strong> take the paddle. We<strong>'
         '&rsquo;re going to</strong> leave at ten.',
    h25b='Verneinung und Frage verändern nur das Verb <em>be</em>, sonst '
         'nichts.',
    b25b='They<strong>&rsquo;re not going to</strong> wait. '
         '<strong>Are</strong> you <strong>going to</strong> swim?',
    n25='<em>Going to go</em> ist korrektes Englisch, auch wenn es beim '
        'ersten Mal seltsam klingt.',
    t26='Vergleiche die beiden Seiten',
    t27='Schreib das fehlende Wort',
    t28='Welcher Satz ist ein Plan?',
    t29='Etwas zum Rudern',
    orderHint='Klicke die Teile der Reihe nach an &middot; nochmal klicken '
              'nimmt einen zurück',
    sortHint='Klicke einen Ausdruck an, dann den Kasten, in den er gehört.',
    bankLabel='Wortliste:',
    eCheck='Die Kontrolle &middot; alle fünf Räume',
    tCheck='Der Wärter kontrolliert die Zellen',
    hC1='Ein Wärter geht mit einer Liste durch den Block. Bevor du zum Tor '
        'kommst, musst du an ihm vorbei.',
    bC1='Neun Fragen. Alle fünf Räume gemischt &mdash; und diesmal steht '
        'keine Regel auf dem Bildschirm.',
    hC2='Hier wird nichts Neues geprüft. Jede Frage nutzt Sprache aus einem '
        'Raum, in dem du schon warst.',
    bC2='Präpositionen &middot; there is / there are &middot; Past Simple '
        '&middot; must und mustn&rsquo;t &middot; Komparative und '
        '<em>going to</em>',
    nC='Wenn du eine verlierst, geh in den Raum zurück und lies die '
       'Regelfolie noch einmal, bevor du es am Tor versuchst.',
    x1='Wo ist es?',
    x2='Eins oder mehr als eins?',
    x3='Was ist passiert?',
    x4='Möglich oder verboten?',
    x5='Vergleiche die beiden Ufer',
    x6='Plan oder Gewohnheit?',
    x7='Schreib die fehlenden Wörter',
    x8='Schreib die fehlenden Wörter',
    x9='Bau den Satz',
    t30='Fünf Zahlen, ein Tor',
    lockStem='Du hast aus jedem Raum eine Zahl. Dieses Schloss nimmt sie '
             '<strong>rückwärts</strong> &mdash; vom letzten Raum zum ersten.',
    lockWhy='<strong>Backwards</strong> heißt vom Ende zum Anfang: zuerst das '
            'Wasser, dann die Werkstatt, der Laden, der Gang und zuletzt '
            'deine Zelle.',
    resPerfect='Jede Tür beim ersten Versuch. Du bist von der Insel runter.',
    resStrong='Starke Leistung. Das Boot liegt im Wasser.',
    resMid='Du bist aus der Zelle raus. Geh die Räume noch mal durch, die du '
           'verloren hast.',
    resLow='Die Wärter hatten dich vor dem Tor. Lies die Regelfolien noch '
           'einmal und fang von vorn an.',
    actTitle='Heute Nacht, in deinen eigenen Worten',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Einer ist der Gefangene, einer der Wärter. Tauscht nach '
                  'jedem Impuls die Rollen.',
    actSpeak1='Wärter: frag, wo fünf Dinge in der Zelle sind. Gefangener: '
              'antworte mit under, behind, next to, on und between.',
    actSpeak2='Gefangener: erzähl deinem Partner den Plan für heute Nacht. '
              'Sag vier Dinge mit <em>I am going to</em>.',
    actSpeak3='Wärter: gib fünf Vorschriften mit <em>must</em> und '
              '<em>mustn&rsquo;t</em>. Gefangener: sag, warum eine davon '
              'schlecht ist.',
    actWriteKind='Schreiben &middot; 80&ndash;120 Wörter',
    actWriteBrief='Du sitzt im Boot. Schreib einen kurzen Brief an deine '
                  'Familie: wo du warst, was du mitgenommen hast, was du '
                  'getan hast und was du jetzt tun wirst. Nutze zwei '
                  'Komparative.',
    actPlaceholder='Last night I was in my cell. Under the bed there was …',
)


# The worked examples inside the rule cards are the English being taught.
# They are copied from English into every language rather than typed out
# nine more times, so a fix to an example cannot land in one language and
# miss the other eight. Same for the writing placeholder, which models
# the sentence the learner is about to write.
EXAMPLE_KEYS = ['b3a', 'b3b', 'b8a', 'b8b', 'b13a', 'b13b', 'b14a', 'b14b',
                'b19a', 'b19b', 'b24a', 'b24b', 'b25a', 'b25b',
                'actPlaceholder']

T['es'] = dict(
    coverTitle='Fuga de <em>Alcatraz</em>',
    coverSub='Cinco salas cerradas, cinco piezas de inglés. Encuentra los '
             'números y abre la última puerta.',
    chipLevel='A2 &middot; Elemental', chipFocus='Sala de escape',
    chipTime='50&ndash;60 minutos', chipCount='NN diapositivas',
    railStops='Celda|Pasillo|Barbería|Taller|Agua',
    eIsland='Antes de empezar', eCell='Sala 1 &middot; Tu celda',
    eCorridor='Sala 2 &middot; El pasillo', eShop='Sala 3 &middot; La barbería',
    eWork='Sala 4 &middot; El taller', eWater='Sala 5 &middot; El agua',
    eLock='La última puerta', eFind='Encuéntralo &middot; contra el reloj',
    t1='Bienvenido a The Rock',
    h1a='Alcatraz era una prisión en una isla pequeña de la bahía de San '
        'Francisco. Abrió en 1934 y cerró en 1963.',
    b1a='La isla está a unas 1,25 millas (2 km) de la ciudad. La llamaban '
        '<strong>The Rock</strong>.',
    h1b='En veintinueve años hubo catorce intentos de fuga. Oficialmente, '
        'no consta que ningún preso lograra escapar.',
    b1b='El agua está fría &mdash; unos 10&ndash;13&nbsp;&deg;C &mdash; y '
        'las corrientes son <strong>fuertes</strong>.',
    n1='Un hombre, John Paul Scott, sí llegó a tierra nadando en diciembre '
       'de 1962. Lo encontraron en la orilla, helado y agotado, y lo '
       'devolvieron a la isla.',
    t2='Esta noche te vas',
    h2a='Eres un preso del bloque B. Tienes una noche y cinco salas: tu '
        'celda, el pasillo, la barbería, el taller y el agua.',
    b2a='En cada sala encuentras <strong>un número</strong>. Los cinco '
        'números abren la última puerta.',
    h2b='La barra de abajo recuerda los números por ti, para que puedas '
        'pensar en el inglés.',
    b2b='En algunas salas corre un reloj. Cuando veas el reloj, mira '
        '<strong>rápido</strong>.',
    n2='Todo esto ocurre en una isla real. El preso es inventado; la fuga '
       'de 1962 no lo fue.',
    t3='¿Dónde está? in, on, under, behind',
    h3a='Con estas palabras dices dónde está algo: <strong>in, on, under, '
        'behind, next to, between, above</strong>.',
    h3b='Después de la preposición va <em>the</em> y la cosa. Nunca añadas '
        '<em>to</em>.',
    n3='<em>Next to</em> son dos palabras. <em>Between</em> necesita dos '
       'cosas y la palabra <em>and</em>.',
    t4='Di dónde está', t5='Dos cosas, una palabra',
    t6='Escribe la palabra que falta', t7='Algo para cavar',
    t8='There is uno. There are dos.',
    h8a='Una cosa: <strong>There is</strong>. Más de una: <strong>There '
        'are</strong>.',
    h8b='La pregunta y la negación siguen el mismo patrón.',
    n8='Water, air, noise y light no tienen plural: <em>there is some '
       'water</em>, nunca <em>there are some waters</em>.',
    t9='¿Uno o más de uno?', t10='Escribe la palabra que falta',
    t11='Pon cada uno en su caja', t12='Algo para ver',
    t13='Lo que hicieron: el past simple',
    h13a='Para acciones terminadas en el pasado se usa el past simple. '
         'Muchos verbos frecuentes son irregulares.',
    h13b='En la negación y la pregunta se usa <em>did</em> y después el '
         'infinitivo sin <em>to</em>.',
    n13='Después de <em>did</em> y <em>didn&rsquo;t</em> nunca va la forma '
        'de pasado. <em>Did they took&hellip;</em> es incorrecto.',
    t14='Junio de 1962',
    h14a='En junio de 1962 tres hombres salieron de Alcatraz: Frank Morris '
         'y los hermanos John y Clarence Anglin. Un cuarto, Allen West, se '
         'quedó atrás.',
    h14b='Se llevaron más de cincuenta impermeables e hicieron una balsa de '
         'goma. Después subieron al tejado y bajaron hasta el agua.',
    n14='West no consiguió abrir su rejilla a tiempo. Se quedó en su celda '
        'y después explicó el plan a los investigadores.',
    t15='Elige la forma de pasado', t16='Escribe el verbo que falta',
    t17='Construye la frase', t18='Algo para cortar',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = es posible. <strong>can&rsquo;t</strong> = '
         'no es posible.',
    h19b='<strong>must</strong> = es necesario. <strong>mustn&rsquo;t</strong> '
         '= está prohibido.',
    n19='Después de los cuatro va el infinitivo sin <em>to</em>. <em>You '
        'must to go</em> es incorrecto.',
    t20='¿Prohibido o no necesario?', t21='Lee la norma',
    t22='¿Norma o delito?', t23='Cincuenta de estos hacen una balsa',
    t24='colder, stronger, more dangerous',
    h24a='Los adjetivos cortos añaden <strong>-er</strong> y después '
         '<strong>than</strong>.',
    h24b='Los adjetivos largos llevan <strong>more</strong> delante y '
         '<strong>than</strong> detrás.',
    n24='Dos irregulares que necesitas esta noche: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='Un plan que ya has decidido',
    h25a='Para un plan ya decidido se usa <strong>be going to</strong> y '
         'después el infinitivo.',
    h25b='La negación y la pregunta solo cambian el verbo <em>be</em>.',
    n25='<em>Going to go</em> es inglés correcto, aunque la primera vez '
        'suene raro.',
    t26='Compara las dos orillas', t27='Escribe la palabra que falta',
    t28='¿Cuál es un plan?', t29='Algo para remar',
    orderHint='Haz clic en las partes en orden &middot; vuelve a hacer clic '
              'para quitar una',
    sortHint='Haz clic en una expresión y luego en la caja a la que '
             'pertenece.',
    bankLabel='Banco de palabras:',
    eCheck='El control &middot; las cinco salas',
    tCheck='El guardia está revisando las celdas',
    hC1='Un guardia recorre el bloque con una lista. Antes de llegar a la '
        'puerta tienes que pasar por delante de él.',
    bC1='Nueve preguntas. Las cinco salas mezcladas y esta vez sin ninguna '
        'regla en pantalla.',
    hC2='Aquí no se prueba nada nuevo. Cada pregunta usa lengua de una sala '
        'en la que ya has estado.',
    bC2='Preposiciones &middot; there is / there are &middot; past simple '
        '&middot; must y mustn&rsquo;t &middot; comparativos y '
        '<em>going to</em>',
    nC='Si fallas alguna, vuelve a esa sala y lee otra vez la diapositiva '
       'de la regla antes de probar en la puerta.',
    x1='¿Dónde está?', x2='¿Uno o más de uno?', x3='¿Qué pasó?',
    x4='¿Posible o prohibido?', x5='Compara las dos orillas',
    x6='¿Plan o costumbre?', x7='Escribe las palabras que faltan',
    x8='Escribe las palabras que faltan', x9='Construye la frase',
    t30='Cinco números, una puerta',
    lockStem='Tienes un número de cada sala. Esta cerradura los toma '
             '<strong>al revés</strong> &mdash; de la última sala a la '
             'primera.',
    lockWhy='<strong>Backwards</strong> significa del final al principio: '
            'primero el agua, después el taller, la barbería, el pasillo y '
            'al final tu celda.',
    resPerfect='Todas las puertas a la primera. Estás fuera de la isla.',
    resStrong='Buen trabajo. La balsa ya está en el agua.',
    resMid='Has salido de la celda. Vuelve a las salas que perdiste.',
    resLow='Los guardias te cogieron antes de la puerta. Lee otra vez las '
           'diapositivas de las reglas y empieza de nuevo.',
    actTitle='Esta noche, con tus palabras',
    actUse='Usa al menos tres:',
    actSpeakBrief='Uno es el preso y otro el guardia. Cambiad de papel '
                  'después de cada consigna.',
    actSpeak1='Guardia: pregunta dónde están cinco cosas de la celda. '
              'Preso: responde con under, behind, next to, on y between.',
    actSpeak2='Preso: cuéntale a tu compañero el plan de esta noche. Di '
              'cuatro cosas con <em>I am going to</em>.',
    actSpeak3='Guardia: da cinco normas con <em>must</em> y '
              '<em>mustn&rsquo;t</em>. Preso: di por qué una de ellas es '
              'mala.',
    actWriteKind='Escritura &middot; 80&ndash;120 palabras',
    actWriteBrief='Estás en la balsa. Escribe una carta corta a tu familia: '
                  'dónde estabas, qué te llevaste, qué hiciste y qué vas a '
                  'hacer ahora. Usa dos comparativos.',
)

T['fr'] = dict(
    coverTitle='Évasion d&rsquo;<em>Alcatraz</em>',
    coverSub='Cinq salles fermées, cinq morceaux d&rsquo;anglais. Trouve '
             'les chiffres et ouvre la dernière porte.',
    chipLevel='A2 &middot; Élémentaire', chipFocus='Escape game',
    chipTime='50&ndash;60 minutes', chipCount='NN diapositives',
    railStops='Cellule|Couloir|Coiffeur|Atelier|Eau',
    eIsland='Avant de commencer', eCell='Salle 1 &middot; Ta cellule',
    eCorridor='Salle 2 &middot; Le couloir',
    eShop='Salle 3 &middot; Le salon de coiffure',
    eWork='Salle 4 &middot; L&rsquo;atelier', eWater='Salle 5 &middot; L&rsquo;eau',
    eLock='La dernière porte', eFind='Trouve-le &middot; contre la montre',
    t1='Bienvenue sur The Rock',
    h1a='Alcatraz était une prison sur une petite île de la baie de San '
        'Francisco. Elle a ouvert en 1934 et fermé en 1963.',
    b1a='L&rsquo;île est à environ 1,25 mile (2 km) de la ville. On '
        'l&rsquo;appelait <strong>The Rock</strong>.',
    h1b='En vingt-neuf ans il y a eu quatorze tentatives d&rsquo;évasion. '
        'Officiellement, aucun détenu n&rsquo;a réussi à s&rsquo;évader.',
    b1b='L&rsquo;eau est froide &mdash; environ 10&ndash;13&nbsp;&deg;C '
        '&mdash; et les courants sont <strong>forts</strong>.',
    n1='Un homme, John Paul Scott, a bien atteint la terre à la nage en '
       'décembre 1962. On l&rsquo;a retrouvé sur le rivage, gelé et épuisé, '
       'et ramené sur l&rsquo;île.',
    t2='Cette nuit, tu pars',
    h2a='Tu es détenu dans le bloc B. Tu as une nuit et cinq salles : ta '
        'cellule, le couloir, le salon de coiffure, l&rsquo;atelier et '
        'l&rsquo;eau.',
    b2a='Dans chaque salle tu trouves <strong>un chiffre</strong>. Les cinq '
        'chiffres ouvrent la dernière porte.',
    h2b='La barre en bas retient les chiffres pour toi, pour que tu puisses '
        'penser à l&rsquo;anglais.',
    b2b='Dans certaines salles une horloge tourne. Quand tu la vois, '
        'regarde <strong>vite</strong>.',
    n2='Tout se passe sur une île réelle. Le détenu est inventé ; '
       'l&rsquo;évasion de 1962 ne l&rsquo;était pas.',
    t3='Où est-ce ? in, on, under, behind',
    h3a='Ces mots disent où se trouve quelque chose : <strong>in, on, '
        'under, behind, next to, between, above</strong>.',
    h3b='Après la préposition viennent <em>the</em> et la chose. Jamais '
        '<em>to</em>.',
    n3='<em>Next to</em> s&rsquo;écrit en deux mots. <em>Between</em> '
       'demande deux choses et le mot <em>and</em>.',
    t4='Dis où c&rsquo;est', t5='Deux choses, un mot',
    t6='Écris le mot qui manque', t7='Quelque chose pour creuser',
    t8='There is un. There are deux.',
    h8a='Une chose : <strong>There is</strong>. Plus d&rsquo;une : '
        '<strong>There are</strong>.',
    h8b='La question et la négation suivent le même schéma.',
    n8='Water, air, noise et light n&rsquo;ont pas de pluriel : <em>there '
       'is some water</em>, jamais <em>there are some waters</em>.',
    t9='Un ou plusieurs ?', t10='Écris le mot qui manque',
    t11='Mets chacun dans sa boîte', t12='Quelque chose pour voir',
    t13='Ce qu&rsquo;ils ont fait : le past simple',
    h13a='Pour des actions terminées au passé, on utilise le past simple. '
         'Beaucoup de verbes courants sont irréguliers.',
    h13b='À la forme négative et interrogative on met <em>did</em>, puis la '
         'base verbale.',
    n13='Après <em>did</em> et <em>didn&rsquo;t</em>, jamais la forme du '
        'passé. <em>Did they took&hellip;</em> est faux.',
    t14='Juin 1962',
    h14a='En juin 1962, trois hommes ont quitté Alcatraz : Frank Morris et '
         'les frères John et Clarence Anglin. Un quatrième, Allen West, est '
         'resté.',
    h14b='Ils ont pris plus de cinquante imperméables et en ont fait un '
         'canot. Puis ils sont montés sur le toit et descendus jusqu&rsquo;à '
         'l&rsquo;eau.',
    n14='West n&rsquo;a pas ouvert sa grille à temps. Il est resté dans sa '
        'cellule et a ensuite expliqué le plan aux enquêteurs.',
    t15='Choisis la forme du passé', t16='Écris le verbe qui manque',
    t17='Construis la phrase', t18='Quelque chose pour couper',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = c&rsquo;est possible. '
         '<strong>can&rsquo;t</strong> = ce n&rsquo;est pas possible.',
    h19b='<strong>must</strong> = c&rsquo;est nécessaire. '
         '<strong>mustn&rsquo;t</strong> = c&rsquo;est interdit.',
    n19='Après les quatre, la base verbale sans <em>to</em>. <em>You must '
        'to go</em> est faux.',
    t20='Interdit ou pas nécessaire ?', t21='Lis le règlement',
    t22='Règle ou faute ?', t23='Cinquante de ceux-ci font un canot',
    t24='colder, stronger, more dangerous',
    h24a='Les adjectifs courts prennent <strong>-er</strong> puis '
         '<strong>than</strong>.',
    h24b='Les adjectifs longs prennent <strong>more</strong> devant et '
         '<strong>than</strong> après.',
    n24='Deux irréguliers utiles cette nuit : good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='Un projet déjà décidé',
    h25a='Pour un projet déjà décidé, on utilise <strong>be going to</strong> '
         'puis la base verbale.',
    h25b='La négation et la question ne changent que le verbe <em>be</em>.',
    n25='<em>Going to go</em> est correct en anglais, même si cela surprend '
        'la première fois.',
    t26='Compare les deux rives', t27='Écris le mot qui manque',
    t28='Laquelle est un projet ?', t29='Quelque chose pour ramer',
    orderHint='Clique sur les parties dans l&rsquo;ordre &middot; reclique '
              'pour en retirer une',
    sortHint='Clique sur une expression, puis sur la boîte où elle va.',
    bankLabel='Banque de mots :',
    eCheck='Le contrôle &middot; les cinq salles',
    tCheck='Le gardien inspecte les cellules',
    hC1='Un gardien parcourt le bloc avec une liste. Avant la porte, il faut '
        'passer devant lui.',
    bC1='Neuf questions. Les cinq salles mélangées, et cette fois aucune '
        'règle à l&rsquo;écran.',
    hC2='Rien de nouveau ici. Chaque question reprend la langue d&rsquo;une '
        'salle où tu es déjà passé.',
    bC2='Prépositions &middot; there is / there are &middot; past simple '
        '&middot; must et mustn&rsquo;t &middot; comparatifs et '
        '<em>going to</em>',
    nC='Si tu en perds une, retourne dans cette salle et relis la règle '
       'avant de tenter la porte.',
    x1='Où est-ce ?', x2='Un ou plusieurs ?', x3='Que s&rsquo;est-il passé ?',
    x4='Possible ou interdit ?', x5='Compare les deux rives',
    x6='Projet ou habitude ?', x7='Écris les mots qui manquent',
    x8='Écris les mots qui manquent', x9='Construis la phrase',
    t30='Cinq chiffres, une porte',
    lockStem='Tu as un chiffre par salle. Cette serrure les prend '
             '<strong>à l&rsquo;envers</strong> &mdash; de la dernière '
             'salle à la première.',
    lockWhy='<strong>Backwards</strong> veut dire de la fin au début : '
            'l&rsquo;eau d&rsquo;abord, puis l&rsquo;atelier, le coiffeur, '
            'le couloir, et ta cellule en dernier.',
    resPerfect='Chaque porte du premier coup. Tu as quitté l&rsquo;île.',
    resStrong='Beau travail. Le canot est à l&rsquo;eau.',
    resMid='Tu es sorti de la cellule. Repasse par les salles que tu as '
           'ratées.',
    resLow='Les gardiens t&rsquo;ont eu avant la porte. Relis les '
           'diapositives des règles et recommence.',
    actTitle='Cette nuit, avec tes mots',
    actUse='Utilise au moins trois :',
    actSpeakBrief='L&rsquo;un est le détenu, l&rsquo;autre le gardien. '
                  'Échangez les rôles après chaque consigne.',
    actSpeak1='Gardien : demande où sont cinq choses dans la cellule. '
              'Détenu : réponds avec under, behind, next to, on et between.',
    actSpeak2='Détenu : raconte le plan de cette nuit à ton binôme. Dis '
              'quatre choses avec <em>I am going to</em>.',
    actSpeak3='Gardien : donne cinq règles avec <em>must</em> et '
              '<em>mustn&rsquo;t</em>. Détenu : dis pourquoi l&rsquo;une '
              'est mauvaise.',
    actWriteKind='Écriture &middot; 80&ndash;120 mots',
    actWriteBrief='Tu es dans le canot. Écris une courte lettre à ta '
                  'famille : où tu étais, ce que tu as pris, ce que tu as '
                  'fait et ce que tu vas faire maintenant. Utilise deux '
                  'comparatifs.',
)

T['it'] = dict(
    coverTitle='Fuga da <em>Alcatraz</em>',
    coverSub='Cinque stanze chiuse, cinque pezzi di inglese. Trova i numeri '
             'e apri l&rsquo;ultimo cancello.',
    chipLevel='A2 &middot; Elementare', chipFocus='Escape room',
    chipTime='50&ndash;60 minuti', chipCount='NN diapositive',
    railStops='Cella|Corridoio|Barbiere|Officina|Acqua',
    eIsland='Prima di cominciare', eCell='Stanza 1 &middot; La tua cella',
    eCorridor='Stanza 2 &middot; Il corridoio',
    eShop='Stanza 3 &middot; Il barbiere',
    eWork='Stanza 4 &middot; L&rsquo;officina',
    eWater='Stanza 5 &middot; L&rsquo;acqua',
    eLock='L&rsquo;ultimo cancello', eFind='Trovalo &middot; contro il tempo',
    t1='Benvenuto su The Rock',
    h1a='Alcatraz era un carcere su una piccola isola nella baia di San '
        'Francisco. Aprì nel 1934 e chiuse nel 1963.',
    b1a='L&rsquo;isola dista circa 1,25 miglia (2 km) dalla città. La '
        'chiamavano <strong>The Rock</strong>.',
    h1b='In ventinove anni ci furono quattordici tentativi di fuga. '
        'Ufficialmente nessun detenuto risulta essere fuggito.',
    b1b='L&rsquo;acqua è fredda &mdash; circa 10&ndash;13&nbsp;&deg;C '
        '&mdash; e le correnti sono <strong>forti</strong>.',
    n1='Un uomo, John Paul Scott, raggiunse davvero la terraferma a nuoto '
       'nel dicembre 1962. Lo trovarono sulla riva, gelato e sfinito, e lo '
       'riportarono indietro.',
    t2='Stanotte te ne vai',
    h2a='Sei un detenuto del blocco B. Hai una notte e cinque stanze: la '
        'cella, il corridoio, il barbiere, l&rsquo;officina e l&rsquo;acqua.',
    b2a='In ogni stanza trovi <strong>un numero</strong>. I cinque numeri '
        'aprono l&rsquo;ultimo cancello.',
    h2b='La barra in basso ricorda i numeri al posto tuo, così puoi pensare '
        'all&rsquo;inglese.',
    b2b='In alcune stanze parte un orologio. Quando lo vedi, guarda '
        '<strong>in fretta</strong>.',
    n2='Tutto questo succede su un&rsquo;isola vera. Il detenuto è '
       'inventato; la fuga del 1962 no.',
    t3='Dov&rsquo;è? in, on, under, behind',
    h3a='Con queste parole dici dove si trova qualcosa: <strong>in, on, '
        'under, behind, next to, between, above</strong>.',
    h3b='Dopo la preposizione vengono <em>the</em> e la cosa. Mai <em>to</em>.',
    n3='<em>Next to</em> sono due parole. <em>Between</em> vuole due cose e '
       'la parola <em>and</em>.',
    t4='Di&rsquo; dov&rsquo;è', t5='Due cose, una parola',
    t6='Scrivi la parola mancante', t7='Qualcosa per scavare',
    t8='There is uno. There are due.',
    h8a='Una cosa: <strong>There is</strong>. Più di una: <strong>There '
        'are</strong>.',
    h8b='Domanda e negazione seguono lo stesso schema.',
    n8='Water, air, noise e light non hanno plurale: <em>there is some '
       'water</em>, mai <em>there are some waters</em>.',
    t9='Uno o più di uno?', t10='Scrivi la parola mancante',
    t11='Metti ognuno nella sua scatola', t12='Qualcosa per vedere',
    t13='Che cosa fecero: il past simple',
    h13a='Per azioni concluse nel passato si usa il past simple. Molti verbi '
         'comuni sono irregolari.',
    h13b='Nella negazione e nella domanda si usa <em>did</em> e poi la forma '
         'base del verbo.',
    n13='Dopo <em>did</em> e <em>didn&rsquo;t</em> mai la forma passata. '
        '<em>Did they took&hellip;</em> è sbagliato.',
    t14='Giugno 1962',
    h14a='Nel giugno 1962 tre uomini lasciarono Alcatraz: Frank Morris e i '
         'fratelli John e Clarence Anglin. Un quarto, Allen West, rimase.',
    h14b='Presero più di cinquanta impermeabili e ne fecero un gommone. Poi '
         'salirono sul tetto e scesero fino all&rsquo;acqua.',
    n14='West non riuscì ad aprire la griglia in tempo. Rimase in cella e '
        'poi spiegò il piano agli inquirenti.',
    t15='Scegli la forma passata', t16='Scrivi il verbo mancante',
    t17='Costruisci la frase', t18='Qualcosa per tagliare',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = è possibile. <strong>can&rsquo;t</strong> = '
         'non è possibile.',
    h19b='<strong>must</strong> = è necessario. <strong>mustn&rsquo;t</strong> '
         '= è vietato.',
    n19='Dopo tutti e quattro va la forma base senza <em>to</em>. <em>You '
        'must to go</em> è sbagliato.',
    t20='Vietato o non necessario?', t21='Leggi la regola',
    t22='Regola o reato?', t23='Cinquanta di questi fanno una barca',
    t24='colder, stronger, more dangerous',
    h24a='Gli aggettivi corti prendono <strong>-er</strong> e poi '
         '<strong>than</strong>.',
    h24b='Gli aggettivi lunghi prendono <strong>more</strong> davanti e '
         '<strong>than</strong> dopo.',
    n24='Due irregolari che ti servono stanotte: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='Un piano già deciso',
    h25a='Per un piano già deciso si usa <strong>be going to</strong> e poi '
         'la forma base.',
    h25b='Negazione e domanda cambiano solo il verbo <em>be</em>.',
    n25='<em>Going to go</em> è inglese corretto, anche se la prima volta '
        'suona strano.',
    t26='Confronta le due rive', t27='Scrivi la parola mancante',
    t28='Quale è un piano?', t29='Qualcosa per remare',
    orderHint='Clicca le parti in ordine &middot; clicca di nuovo per '
              'toglierne una',
    sortHint='Clicca un&rsquo;espressione, poi la scatola in cui va.',
    bankLabel='Banca di parole:',
    eCheck='Il controllo &middot; tutte e cinque le stanze',
    tCheck='La guardia sta controllando le celle',
    hC1='Una guardia percorre il blocco con una lista. Prima del cancello '
        'devi passargli davanti.',
    bC1='Nove domande. Tutte e cinque le stanze mescolate, e stavolta '
        'nessuna regola sullo schermo.',
    hC2='Qui non si prova niente di nuovo. Ogni domanda usa la lingua di una '
        'stanza in cui sei già stato.',
    bC2='Preposizioni &middot; there is / there are &middot; past simple '
        '&middot; must e mustn&rsquo;t &middot; comparativi e '
        '<em>going to</em>',
    nC='Se ne sbagli una, torna in quella stanza e rileggi la regola prima '
       'di provare al cancello.',
    x1='Dov&rsquo;è?', x2='Uno o più di uno?', x3='Che cosa è successo?',
    x4='Possibile o vietato?', x5='Confronta le due rive',
    x6='Piano o abitudine?', x7='Scrivi le parole mancanti',
    x8='Scrivi le parole mancanti', x9='Costruisci la frase',
    t30='Cinque numeri, un cancello',
    lockStem='Hai un numero da ogni stanza. Questa serratura li prende '
             '<strong>al contrario</strong> &mdash; dall&rsquo;ultima '
             'stanza alla prima.',
    lockWhy='<strong>Backwards</strong> vuol dire dalla fine all&rsquo;inizio: '
            'prima l&rsquo;acqua, poi l&rsquo;officina, il barbiere, il '
            'corridoio e per ultima la tua cella.',
    resPerfect='Ogni porta al primo colpo. Sei fuori dall&rsquo;isola.',
    resStrong='Bel lavoro. La barca è in acqua.',
    resMid='Sei uscito dalla cella. Ripassa le stanze che hai perso.',
    resLow='Le guardie ti hanno preso prima del cancello. Rileggi le '
           'diapositive delle regole e ricomincia.',
    actTitle='Stanotte, con parole tue',
    actUse='Usane almeno tre:',
    actSpeakBrief='Uno fa il detenuto, uno la guardia. Scambiatevi i ruoli '
                  'dopo ogni spunto.',
    actSpeak1='Guardia: chiedi dove sono cinque cose nella cella. Detenuto: '
              'rispondi con under, behind, next to, on e between.',
    actSpeak2='Detenuto: racconta al compagno il piano di stanotte. Di&rsquo; '
              'quattro cose con <em>I am going to</em>.',
    actSpeak3='Guardia: dai cinque regole con <em>must</em> e '
              '<em>mustn&rsquo;t</em>. Detenuto: spiega perché una è una '
              'brutta regola.',
    actWriteKind='Scrittura &middot; 80&ndash;120 parole',
    actWriteBrief='Sei sulla barca. Scrivi una breve lettera alla tua '
                  'famiglia: dov&rsquo;eri, che cosa hai preso, che cosa hai '
                  'fatto e che cosa farai adesso. Usa due comparativi.',
)

T['pt'] = dict(
    coverTitle='Fuga de <em>Alcatraz</em>',
    coverSub='Cinco salas trancadas, cinco peças de inglês. Encontra os '
             'números e abre o último portão.',
    chipLevel='A2 &middot; Elementar', chipFocus='Sala de fuga',
    chipTime='50&ndash;60 minutos', chipCount='NN diapositivos',
    railStops='Cela|Corredor|Barbearia|Oficina|Água',
    eIsland='Antes de começar', eCell='Sala 1 &middot; A tua cela',
    eCorridor='Sala 2 &middot; O corredor',
    eShop='Sala 3 &middot; A barbearia', eWork='Sala 4 &middot; A oficina',
    eWater='Sala 5 &middot; A água', eLock='O último portão',
    eFind='Encontra-o &middot; contra o relógio',
    t1='Bem-vindo a The Rock',
    h1a='Alcatraz era uma prisão numa pequena ilha da baía de São Francisco. '
        'Abriu em 1934 e fechou em 1963.',
    b1a='A ilha fica a cerca de 1,25 milhas (2 km) da cidade. Chamavam-lhe '
        '<strong>The Rock</strong>.',
    h1b='Em vinte e nove anos houve catorze tentativas de fuga. Oficialmente, '
        'não há registo de nenhum preso ter escapado.',
    b1b='A água é fria &mdash; cerca de 10&ndash;13&nbsp;&deg;C &mdash; e as '
        'correntes são <strong>fortes</strong>.',
    n1='Um homem, John Paul Scott, chegou mesmo a terra a nado em dezembro '
       'de 1962. Encontraram-no na margem, gelado e exausto, e levaram-no de '
       'volta.',
    t2='Esta noite vais embora',
    h2a='És um preso do bloco B. Tens uma noite e cinco salas: a tua cela, o '
        'corredor, a barbearia, a oficina e a água.',
    b2a='Em cada sala encontras <strong>um número</strong>. Os cinco números '
        'abrem o último portão.',
    h2b='A barra em baixo guarda os números por ti, para poderes pensar no '
        'inglês.',
    b2b='Em algumas salas há um relógio a contar. Quando o vires, olha '
        '<strong>depressa</strong>.',
    n2='Tudo isto passa-se numa ilha real. O preso é inventado; a fuga de '
       '1962 não foi.',
    t3='Onde está? in, on, under, behind',
    h3a='Com estas palavras dizes onde está alguma coisa: <strong>in, on, '
        'under, behind, next to, between, above</strong>.',
    h3b='Depois da preposição vem <em>the</em> e a coisa. Nunca <em>to</em>.',
    n3='<em>Next to</em> são duas palavras. <em>Between</em> precisa de duas '
       'coisas e da palavra <em>and</em>.',
    t4='Diz onde está', t5='Duas coisas, uma palavra',
    t6='Escreve a palavra que falta', t7='Algo para escavar',
    t8='There is um. There are dois.',
    h8a='Uma coisa: <strong>There is</strong>. Mais do que uma: '
        '<strong>There are</strong>.',
    h8b='A pergunta e a negativa seguem o mesmo padrão.',
    n8='Water, air, noise e light não têm plural: <em>there is some '
       'water</em>, nunca <em>there are some waters</em>.',
    t9='Um ou mais do que um?', t10='Escreve a palavra que falta',
    t11='Põe cada um na sua caixa', t12='Algo para ver',
    t13='O que eles fizeram: o past simple',
    h13a='Para ações terminadas no passado usa-se o past simple. Muitos '
         'verbos comuns são irregulares.',
    h13b='Na negativa e na pergunta usa-se <em>did</em> e depois a forma base '
         'do verbo.',
    n13='Depois de <em>did</em> e <em>didn&rsquo;t</em> nunca a forma do '
        'passado. <em>Did they took&hellip;</em> está errado.',
    t14='Junho de 1962',
    h14a='Em junho de 1962 três homens saíram de Alcatraz: Frank Morris e os '
         'irmãos John e Clarence Anglin. Um quarto, Allen West, ficou para '
         'trás.',
    h14b='Levaram mais de cinquenta gabardinas e fizeram um bote de borracha. '
         'Depois subiram ao telhado e desceram até à água.',
    n14='West não conseguiu abrir a grelha a tempo. Ficou na cela e depois '
        'explicou o plano aos investigadores.',
    t15='Escolhe a forma do passado', t16='Escreve o verbo que falta',
    t17='Constrói a frase', t18='Algo para cortar',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = é possível. <strong>can&rsquo;t</strong> = '
         'não é possível.',
    h19b='<strong>must</strong> = é necessário. <strong>mustn&rsquo;t</strong> '
         '= é proibido.',
    n19='Depois dos quatro vem a forma base sem <em>to</em>. <em>You must to '
        'go</em> está errado.',
    t20='Proibido ou não necessário?', t21='Lê a regra',
    t22='Regra ou crime?', t23='Cinquenta destes fazem um bote',
    t24='colder, stronger, more dangerous',
    h24a='Os adjetivos curtos levam <strong>-er</strong> e depois '
         '<strong>than</strong>.',
    h24b='Os adjetivos longos levam <strong>more</strong> à frente e '
         '<strong>than</strong> atrás.',
    n24='Dois irregulares de que precisas esta noite: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='Um plano já decidido',
    h25a='Para um plano já decidido usa-se <strong>be going to</strong> e '
         'depois a forma base.',
    h25b='A negativa e a pergunta mudam só o verbo <em>be</em>.',
    n25='<em>Going to go</em> é inglês correto, mesmo que à primeira soe '
        'estranho.',
    t26='Compara as duas margens', t27='Escreve a palavra que falta',
    t28='Qual delas é um plano?', t29='Algo para remar',
    orderHint='Clica nas partes por ordem &middot; clica outra vez para '
              'retirar uma',
    sortHint='Clica numa expressão e depois na caixa a que pertence.',
    bankLabel='Banco de palavras:',
    eCheck='O controlo &middot; as cinco salas',
    tCheck='O guarda está a revistar as celas',
    hC1='Um guarda percorre o bloco com uma lista. Antes do portão tens de '
        'passar por ele.',
    bC1='Nove perguntas. As cinco salas misturadas e desta vez sem nenhuma '
        'regra no ecrã.',
    hC2='Aqui não se testa nada de novo. Cada pergunta usa língua de uma sala '
        'onde já estiveste.',
    bC2='Preposições &middot; there is / there are &middot; past simple '
        '&middot; must e mustn&rsquo;t &middot; comparativos e '
        '<em>going to</em>',
    nC='Se perderes uma, volta a essa sala e lê outra vez a regra antes de '
       'tentares o portão.',
    x1='Onde está?', x2='Um ou mais do que um?', x3='O que aconteceu?',
    x4='Possível ou proibido?', x5='Compara as duas margens',
    x6='Plano ou hábito?', x7='Escreve as palavras que faltam',
    x8='Escreve as palavras que faltam', x9='Constrói a frase',
    t30='Cinco números, um portão',
    lockStem='Tens um número de cada sala. Esta fechadura recebe-os '
             '<strong>ao contrário</strong> &mdash; da última sala para a '
             'primeira.',
    lockWhy='<strong>Backwards</strong> significa do fim para o princípio: '
            'primeiro a água, depois a oficina, a barbearia, o corredor e por '
            'último a tua cela.',
    resPerfect='Todas as portas à primeira. Saíste da ilha.',
    resStrong='Bom trabalho. O bote está na água.',
    resMid='Saíste da cela. Volta às salas que perdeste.',
    resLow='Os guardas apanharam-te antes do portão. Lê outra vez os '
           'diapositivos das regras e recomeça.',
    actTitle='Esta noite, por tuas palavras',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Um é o preso, o outro é o guarda. Troquem de papéis depois '
                  'de cada tarefa.',
    actSpeak1='Guarda: pergunta onde estão cinco coisas na cela. Preso: '
              'responde com under, behind, next to, on e between.',
    actSpeak2='Preso: conta ao teu par o plano desta noite. Diz quatro coisas '
              'com <em>I am going to</em>.',
    actSpeak3='Guarda: dá cinco regras com <em>must</em> e '
              '<em>mustn&rsquo;t</em>. Preso: diz porque é que uma delas é má.',
    actWriteKind='Escrita &middot; 80&ndash;120 palavras',
    actWriteBrief='Estás no bote. Escreve uma carta curta à tua família: onde '
                  'estavas, o que levaste, o que fizeste e o que vais fazer '
                  'agora. Usa dois comparativos.',
)

T['ru'] = dict(
    coverTitle='Побег из <em>Алькатраса</em>',
    coverSub='Пять запертых комнат, пять кусочков английского. Найди числа '
             'и открой последние ворота.',
    chipLevel='A2 &middot; Начальный', chipFocus='Квест',
    chipTime='50&ndash;60 минут', chipCount='NN слайдов',
    railStops='Камера|Коридор|Парикмахерская|Мастерская|Вода',
    eIsland='Прежде чем начать', eCell='Комната 1 &middot; Твоя камера',
    eCorridor='Комната 2 &middot; Коридор',
    eShop='Комната 3 &middot; Парикмахерская',
    eWork='Комната 4 &middot; Мастерская', eWater='Комната 5 &middot; Вода',
    eLock='Последние ворота', eFind='Найди &middot; на время',
    t1='Добро пожаловать на «Скалу»',
    h1a='Алькатрас — тюрьма на маленьком острове в заливе Сан-Франциско. Она '
        'открылась в 1934 году и закрылась в 1963-м.',
    b1a='До города около 1,25 мили (2 км). Остров называли <strong>The '
        'Rock</strong> — «Скала».',
    h1b='За двадцать девять лет было четырнадцать попыток побега. Официально '
        'ни один заключённый не считается сбежавшим.',
    b1b='Вода холодная — около 10&ndash;13&nbsp;&deg;C, а течения '
        '<strong>сильные</strong>.',
    n1='Один человек, Джон Пол Скотт, всё же доплыл до берега в декабре 1962 '
       'года. Его нашли на берегу, замёрзшего и обессиленного, и вернули '
       'обратно.',
    t2='Сегодня ночью ты уходишь',
    h2a='Ты заключённый в блоке B. У тебя одна ночь и пять комнат: камера, '
        'коридор, парикмахерская, мастерская и вода.',
    b2a='В каждой комнате ты находишь <strong>одну цифру</strong>. Пять цифр '
        'открывают последние ворота.',
    h2b='Полоса внизу запоминает цифры за тебя, чтобы ты думал об английском.',
    b2b='В некоторых комнатах идут часы. Увидел часы — смотри '
        '<strong>быстро</strong>.',
    n2='Всё это происходит на настоящем острове. Заключённый выдуман; побег '
       '1962 года — нет.',
    t3='Где это? in, on, under, behind',
    h3a='Этими словами говорят, где что-то находится: <strong>in, on, under, '
        'behind, next to, between, above</strong>.',
    h3b='После предлога идёт <em>the</em> и сам предмет. Никогда не '
        'добавляй <em>to</em>.',
    n3='<em>Next to</em> — два слова. <em>Between</em> требует двух предметов '
       'и слова <em>and</em>.',
    t4='Скажи, где это', t5='Две вещи, одно слово',
    t6='Впиши пропущенное слово', t7='Чем можно копать',
    t8='There is — один. There are — два.',
    h8a='Один предмет: <strong>There is</strong>. Больше одного: '
        '<strong>There are</strong>.',
    h8b='Вопрос и отрицание строятся по той же схеме.',
    n8='Water, air, noise и light не имеют множественного числа: <em>there is '
       'some water</em>, но не <em>there are some waters</em>.',
    t9='Один или больше?', t10='Впиши пропущенное слово',
    t11='Разложи по коробкам', t12='Чем можно светить',
    t13='Что они сделали: past simple',
    h13a='Для законченных действий в прошлом используется past simple. Многие '
         'частые глаголы неправильные.',
    h13b='В отрицании и вопросе ставится <em>did</em>, а затем начальная '
         'форма глагола.',
    n13='После <em>did</em> и <em>didn&rsquo;t</em> никогда не ставится форма '
        'прошедшего времени. <em>Did they took&hellip;</em> — ошибка.',
    t14='Июнь 1962 года',
    h14a='В июне 1962 года трое покинули Алькатрас: Фрэнк Моррис и братья '
         'Джон и Кларенс Энглин. Четвёртый, Аллен Уэст, остался.',
    h14b='Они взяли больше пятидесяти плащей и сделали резиновую лодку. Потом '
         'поднялись на крышу и спустились к воде.',
    n14='Уэст не успел снять решётку вентиляции. Он остался в камере и позже '
        'рассказал следователям, как работал план.',
    t15='Выбери форму прошедшего времени', t16='Впиши пропущенный глагол',
    t17='Собери предложение', t18='Чем можно резать',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = это возможно. <strong>can&rsquo;t</strong> = '
         'это невозможно.',
    h19b='<strong>must</strong> = это необходимо. <strong>mustn&rsquo;t</strong> '
         '= это запрещено.',
    n19='После всех четырёх идёт начальная форма без <em>to</em>. <em>You '
        'must to go</em> — ошибка.',
    t20='Запрещено или не обязательно?', t21='Прочитай правило',
    t22='Правило или нарушение?', t23='Пятьдесят таких — это лодка',
    t24='colder, stronger, more dangerous',
    h24a='Короткие прилагательные получают <strong>-er</strong> и затем '
         '<strong>than</strong>.',
    h24b='Длинные прилагательные получают <strong>more</strong> впереди и '
         '<strong>than</strong> после.',
    n24='Два неправильных, которые нужны сегодня ночью: good &rarr; '
        '<strong>better</strong>, bad &rarr; <strong>worse</strong>.',
    t25='План, который ты уже принял',
    h25a='Для уже принятого плана используется <strong>be going to</strong> и '
         'затем начальная форма глагола.',
    h25b='В отрицании и вопросе меняется только глагол <em>be</em>.',
    n25='<em>Going to go</em> — правильный английский, хотя в первый раз '
        'звучит странно.',
    t26='Сравни два берега', t27='Впиши пропущенное слово',
    t28='Где здесь план?', t29='Чем можно грести',
    orderHint='Нажимай части по порядку &middot; нажми ещё раз, чтобы убрать',
    sortHint='Нажми на выражение, затем на коробку, куда оно относится.',
    bankLabel='Банк слов:',
    eCheck='Проверка &middot; все пять комнат',
    tCheck='Охранник проверяет камеры',
    hC1='Охранник идёт по блоку со списком. Прежде чем дойти до ворот, надо '
        'пройти мимо него.',
    bC1='Девять вопросов. Все пять комнат вперемешку — и на этот раз никакого '
        'правила на экране.',
    hC2='Ничего нового здесь не проверяется. В каждом вопросе язык из комнаты, '
        'где ты уже был.',
    bC2='Предлоги &middot; there is / there are &middot; past simple &middot; '
        'must и mustn&rsquo;t &middot; сравнительная степень и '
        '<em>going to</em>',
    nC='Если ошибся — вернись в ту комнату и перечитай правило, прежде чем '
       'идти к воротам.',
    x1='Где это?', x2='Один или больше?', x3='Что произошло?',
    x4='Возможно или запрещено?', x5='Сравни два берега',
    x6='План или привычка?', x7='Впиши пропущенные слова',
    x8='Впиши пропущенные слова', x9='Собери предложение',
    t30='Пять цифр, одни ворота',
    lockStem='У тебя есть цифра из каждой комнаты. Этот замок принимает их '
             '<strong>наоборот</strong> — от последней комнаты к первой.',
    lockWhy='<strong>Backwards</strong> значит от конца к началу: сначала '
            'вода, затем мастерская, парикмахерская, коридор и в конце твоя '
            'камера.',
    resPerfect='Каждая дверь с первого раза. Ты ушёл с острова.',
    resStrong='Отличная работа. Лодка на воде.',
    resMid='Из камеры ты вышел. Вернись в комнаты, где терял очки.',
    resLow='Охрана взяла тебя до ворот. Перечитай слайды с правилами и начни '
           'заново.',
    actTitle='Сегодня ночью — своими словами',
    actUse='Используй хотя бы три:',
    actSpeakBrief='Один — заключённый, другой — охранник. Меняйтесь ролями '
                  'после каждого задания.',
    actSpeak1='Охранник: спроси, где в камере пять предметов. Заключённый: '
              'отвечай с under, behind, next to, on и between.',
    actSpeak2='Заключённый: расскажи партнёру план на эту ночь. Скажи четыре '
              'вещи с <em>I am going to</em>.',
    actSpeak3='Охранник: дай пять правил с <em>must</em> и '
              '<em>mustn&rsquo;t</em>. Заключённый: скажи, почему одно из них '
              'плохое.',
    actWriteKind='Письмо &middot; 80&ndash;120 слов',
    actWriteBrief='Ты в лодке. Напиши короткое письмо семье: где ты был, что '
                  'взял, что сделал и что собираешься делать теперь. '
                  'Используй две сравнительные формы.',
)

T['ar'] = dict(
    coverTitle='الهروب من <em>ألكاتراز</em>',
    coverSub='خمس غرف مغلقة، وخمس قطع من الإنجليزية. اعثر على الأرقام وافتح '
             'البوابة الأخيرة.',
    chipLevel='A2 &middot; مبتدئ', chipFocus='غرفة الهروب',
    chipTime='50&ndash;60 دقيقة', chipCount='NN شريحة',
    railStops='الزنزانة|الممر|الحلاق|الورشة|الماء',
    eIsland='قبل أن تبدأ', eCell='الغرفة 1 &middot; زنزانتك',
    eCorridor='الغرفة 2 &middot; الممر', eShop='الغرفة 3 &middot; الحلاق',
    eWork='الغرفة 4 &middot; الورشة', eWater='الغرفة 5 &middot; الماء',
    eLock='البوابة الأخيرة', eFind='اعثر عليه &middot; والوقت يجري',
    t1='أهلاً بك في «الصخرة»',
    h1a='ألكاتراز سجن على جزيرة صغيرة في خليج سان فرانسيسكو. فُتح عام 1934 '
        'وأُغلق عام 1963.',
    b1a='تبعد الجزيرة نحو 1.25 ميل (2 كم) عن المدينة. كانوا يسمّونها '
        '<strong>The Rock</strong>.',
    h1b='في تسعة وعشرين عاماً وقعت أربع عشرة محاولة هروب. ورسمياً لا يوجد '
        'سجين مسجَّل أنه نجح في الهروب.',
    b1b='الماء بارد — نحو 10&ndash;13 درجة مئوية — والتيارات '
        '<strong>قوية</strong>.',
    n1='رجل واحد، جون بول سكوت، وصل فعلاً إلى البر سباحةً في ديسمبر 1962. '
       'وُجد على الشاطئ منهكاً من البرد وأُعيد إلى الجزيرة.',
    t2='الليلة سترحل',
    h2a='أنت سجين في المبنى B. أمامك ليلة واحدة وخمس غرف: زنزانتك، والممر، '
        'ومحل الحلاقة، والورشة، والماء.',
    b2a='في كل غرفة تجد <strong>رقماً واحداً</strong>. الأرقام الخمسة تفتح '
        'البوابة الأخيرة.',
    h2b='الشريط في الأسفل يحفظ الأرقام بدلاً عنك، لتفكّر أنت في الإنجليزية.',
    b2b='في بعض الغرف ساعة تعدّ. حين ترى الساعة، انظر '
        '<strong>بسرعة</strong>.',
    n2='كل هذا يجري على جزيرة حقيقية. السجين من نسج الخيال، أما هروب 1962 '
       'فليس كذلك.',
    t3='أين هو؟ in, on, under, behind',
    h3a='بهذه الكلمات تقول أين يوجد الشيء: <strong>in, on, under, behind, '
        'next to, between, above</strong>.',
    h3b='بعد حرف الجر يأتي <em>the</em> ثم الشيء. ولا تضف <em>to</em> أبداً.',
    n3='<em>Next to</em> كلمتان. و<em>between</em> تحتاج شيئين وكلمة '
       '<em>and</em>.',
    t4='قل أين هو', t5='شيئان وكلمة واحدة',
    t6='اكتب الكلمة الناقصة', t7='شيء تحفر به',
    t8='There is للمفرد. There are للجمع.',
    h8a='شيء واحد: <strong>There is</strong>. أكثر من واحد: <strong>There '
        'are</strong>.',
    h8b='السؤال والنفي يتبعان النمط نفسه.',
    n8='الكلمات water وair وnoise وlight لا جمع لها: <em>there is some '
       'water</em> وليس <em>there are some waters</em>.',
    t9='واحد أم أكثر؟', t10='اكتب الكلمة الناقصة',
    t11='ضع كل واحدة في صندوقها', t12='شيء ترى به',
    t13='ما الذي فعلوه: الماضي البسيط',
    h13a='للأفعال المنتهية في الماضي نستعمل الماضي البسيط. وكثير من الأفعال '
         'الشائعة شاذّة.',
    h13b='في النفي والسؤال نستعمل <em>did</em> ثم الفعل في صيغته الأساسية.',
    n13='بعد <em>did</em> و<em>didn&rsquo;t</em> لا تأتي صيغة الماضي أبداً. '
        '<em>Did they took&hellip;</em> خطأ.',
    t14='يونيو 1962',
    h14a='في يونيو 1962 غادر ثلاثة رجال ألكاتراز: فرانك موريس والأخوان جون '
         'وكلارنس أنغلين. وبقي رابع هو ألن ويست.',
    h14b='أخذوا أكثر من خمسين معطف مطر وصنعوا منها قارباً مطاطياً، ثم صعدوا '
         'إلى السطح ونزلوا إلى الماء.',
    n14='لم يفتح ويست فتحة التهوية في الوقت المناسب، فبقي في زنزانته وشرح '
        'الخطة للمحققين فيما بعد.',
    t15='اختر صيغة الماضي', t16='اكتب الفعل الناقص',
    t17='ركّب الجملة', t18='شيء تقصّ به',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = هذا ممكن. <strong>can&rsquo;t</strong> = هذا '
         'غير ممكن.',
    h19b='<strong>must</strong> = هذا ضروري. <strong>mustn&rsquo;t</strong> = '
         'هذا ممنوع.',
    n19='بعد الأربعة جميعاً يأتي الفعل الأساسي بلا <em>to</em>. <em>You must '
        'to go</em> خطأ.',
    t20='ممنوع أم غير ضروري؟', t21='اقرأ القاعدة',
    t22='قاعدة أم مخالفة؟', t23='خمسون من هذه تصنع قارباً',
    t24='colder, stronger, more dangerous',
    h24a='الصفات القصيرة تأخذ <strong>-er</strong> ثم <strong>than</strong>.',
    h24b='الصفات الطويلة تأخذ <strong>more</strong> قبلها و<strong>than</strong> '
         'بعدها.',
    n24='صفتان شاذّتان تحتاجهما الليلة: good &rarr; <strong>better</strong>، '
        'وbad &rarr; <strong>worse</strong>.',
    t25='خطة قرّرتها من قبل',
    h25a='للخطة المقرَّرة سلفاً نستعمل <strong>be going to</strong> ثم الفعل '
         'الأساسي.',
    h25b='النفي والسؤال يغيّران الفعل <em>be</em> فقط، لا غير.',
    n25='<em>Going to go</em> إنجليزية صحيحة، وإن بدت غريبة أول مرة.',
    t26='قارن بين الشاطئين', t27='اكتب الكلمة الناقصة',
    t28='أيّها خطة؟', t29='شيء تجدّف به',
    orderHint='انقر الأجزاء بالترتيب &middot; انقر مرة أخرى لإرجاع جزء',
    sortHint='انقر على العبارة ثم على الصندوق الذي تنتمي إليه.',
    bankLabel='بنك الكلمات:',
    eCheck='التفتيش &middot; الغرف الخمس',
    tCheck='الحارس يفتّش الزنزانات',
    hC1='حارس يمشي في المبنى ومعه قائمة. قبل أن تصل إلى البوابة عليك أن تمرّ '
        'من أمامه.',
    bC1='تسعة أسئلة. الغرف الخمس مختلطة، وهذه المرة بلا قاعدة على الشاشة.',
    hC2='لا شيء جديد يُختبر هنا. كل سؤال يستعمل لغة غرفة مررت بها من قبل.',
    bC2='حروف الجر &middot; there is / there are &middot; الماضي البسيط '
        '&middot; must وmustn&rsquo;t &middot; صيغة المقارنة و'
        '<em>going to</em>',
    nC='إذا أخطأت في سؤال، فعُد إلى تلك الغرفة واقرأ القاعدة مرة أخرى قبل أن '
       'تجرّب البوابة.',
    x1='أين هو؟', x2='واحد أم أكثر؟', x3='ماذا حدث؟',
    x4='ممكن أم ممنوع؟', x5='قارن بين الشاطئين',
    x6='خطة أم عادة؟', x7='اكتب الكلمات الناقصة',
    x8='اكتب الكلمات الناقصة', x9='ركّب الجملة',
    t30='خمسة أرقام وبوابة واحدة',
    lockStem='معك رقم من كل غرفة. هذا القفل يأخذها <strong>بالعكس</strong> — '
             'من الغرفة الأخيرة إلى الأولى.',
    lockWhy='<strong>Backwards</strong> تعني من النهاية إلى البداية: الماء '
            'أولاً، ثم الورشة، فالحلاق، فالممر، وزنزانتك في الآخر.',
    resPerfect='كل باب من المحاولة الأولى. لقد غادرت الجزيرة.',
    resStrong='عمل قوي. القارب في الماء.',
    resMid='خرجت من الزنزانة. ارجع إلى الغرف التي خسرت فيها.',
    resLow='أمسك بك الحرّاس قبل البوابة. اقرأ شرائح القواعد من جديد وابدأ من '
           'البداية.',
    actTitle='الليلة، بكلماتك أنت',
    actUse='استعمل ثلاثة على الأقل:',
    actSpeakBrief='واحد منكما السجين والآخر الحارس. تبادلا الدورين بعد كل '
                  'مهمة.',
    actSpeak1='الحارس: اسأل عن مكان خمسة أشياء في الزنزانة. السجين: أجب '
              'باستعمال under وbehind وnext to وon وbetween.',
    actSpeak2='السجين: احكِ لزميلك خطة هذه الليلة. قل أربعة أشياء بـ<em>I am '
              'going to</em>.',
    actSpeak3='الحارس: أعطِ خمس قواعد بـ<em>must</em> و<em>mustn&rsquo;t</em>. '
              'السجين: قل لماذا واحدة منها سيئة.',
    actWriteKind='كتابة &middot; 80&ndash;120 كلمة',
    actWriteBrief='أنت في القارب. اكتب رسالة قصيرة إلى عائلتك: أين كنت، وماذا '
                  'أخذت، وماذا فعلت، وماذا ستفعل الآن. استعمل صيغتَي مقارنة.',
)

T['zh'] = dict(
    coverTitle='逃离<em>恶魔岛</em>',
    coverSub='五个上锁的房间，五块英语。找齐数字，打开最后一道门。',
    chipLevel='A2 &middot; 初级', chipFocus='密室逃脱',
    chipTime='50&ndash;60 分钟', chipCount='NN 张幻灯片',
    railStops='牢房|通道|理发室|工场|海水',
    eIsland='开始之前', eCell='第 1 间 &middot; 你的牢房',
    eCorridor='第 2 间 &middot; 通道', eShop='第 3 间 &middot; 理发室',
    eWork='第 4 间 &middot; 工场', eWater='第 5 间 &middot; 海水',
    eLock='最后一道门', eFind='限时找出来',
    t1='欢迎来到「岩石岛」',
    h1a='恶魔岛是旧金山湾一座小岛上的监狱，1934 年启用，1963 年关闭。',
    b1a='小岛离城市大约 1.25 英里（2 公里）。人们叫它 <strong>The '
        'Rock</strong>。',
    h1b='二十九年里共有十四次越狱行动。官方记录中，没有一名囚犯成功逃脱。',
    b1b='海水很冷，大约 10&ndash;13&nbsp;&deg;C，而且水流<strong>很急</strong>。',
    n1='1962 年 12 月，一个叫约翰·保罗·斯科特的人确实游到了岸边。他被人发现'
       '时又冷又虚脱，随后被送了回去。',
    t2='今晚你要走了',
    h2a='你是 B 区的囚犯。你只有一夜，要经过五个地方：牢房、通道、理发室、'
        '工场和海水。',
    b2a='每个房间里都有<strong>一个数字</strong>。五个数字能打开最后一道门。',
    h2b='屏幕下方那条栏会替你记住数字，好让你专心想英语。',
    b2b='有些房间有计时。看到计时，就要<strong>快看</strong>。',
    n2='这一切发生在一座真实的岛上。囚犯是虚构的，1962 年的越狱不是。',
    t3='它在哪里？in, on, under, behind',
    h3a='用这些词说明东西在哪里：<strong>in, on, under, behind, next to, '
        'between, above</strong>。',
    h3b='介词后面接 <em>the</em> 和那样东西，绝不能加 <em>to</em>。',
    n3='<em>Next to</em> 是两个词。<em>Between</em> 需要两样东西，还要有 '
       '<em>and</em>。',
    t4='说出它在哪里', t5='两样东西，一个词',
    t6='写出缺少的词', t7='用来挖的东西',
    t8='There is 一个。There are 两个。',
    h8a='一样东西用 <strong>There is</strong>；多于一样用 <strong>There '
        'are</strong>。',
    h8b='疑问句和否定句用同样的结构。',
    n8='water、air、noise、light 没有复数：说 <em>there is some water</em>，'
       '不能说 <em>there are some waters</em>。',
    t9='一个还是不止一个？', t10='写出缺少的词',
    t11='把每一个放进它的框里', t12='用来照明的东西',
    t13='他们做了什么：一般过去时',
    h13a='表示过去完成的动作用一般过去时。很多常用动词是不规则的。',
    h13b='否定和疑问用 <em>did</em>，后面接动词原形。',
    n13='<em>did</em> 和 <em>didn&rsquo;t</em> 后面绝不用过去式。<em>Did they '
        'took&hellip;</em> 是错的。',
    t14='1962 年 6 月',
    h14a='1962 年 6 月，三个人离开了恶魔岛：弗兰克·莫里斯和约翰、克拉伦斯·'
         '安格林兄弟。第四人艾伦·韦斯特留了下来。',
    h14b='他们拿了五十多件雨衣，做成一只橡皮艇，然后爬上屋顶，下到水边。',
    n14='韦斯特没能及时打开通风口，只好留在牢房里，后来向调查人员讲出了整个'
        '计划。',
    t15='选出过去式', t16='写出缺少的动词',
    t17='把句子组起来', t18='用来剪的东西',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = 有可能。<strong>can&rsquo;t</strong> = 不可能。',
    h19b='<strong>must</strong> = 必须。<strong>mustn&rsquo;t</strong> = 禁止。',
    n19='这四个后面都接不带 <em>to</em> 的动词原形。<em>You must to go</em> '
        '是错的。',
    t20='禁止，还是不必？', t21='读一读规定',
    t22='规定还是违规？', t23='五十件这个能做一只船',
    t24='colder, stronger, more dangerous',
    h24a='短的形容词加 <strong>-er</strong>，后面用 <strong>than</strong>。',
    h24b='长的形容词前面加 <strong>more</strong>，后面用 <strong>than</strong>。',
    n24='今晚要用的两个不规则形式：good &rarr; <strong>better</strong>，bad '
        '&rarr; <strong>worse</strong>。',
    t25='已经定下的计划',
    h25a='已经决定的计划用 <strong>be going to</strong>，后面接动词原形。',
    h25b='否定和疑问只改动词 <em>be</em>，其他不变。',
    n25='<em>Going to go</em> 是正确的英语，虽然第一次听上去有点怪。',
    t26='比较两边的岸', t27='写出缺少的词',
    t28='哪一句是计划？', t29='用来划船的东西',
    orderHint='按顺序点击各部分 &middot; 再点一次可以拿回来',
    sortHint='先点一个短语，再点它该去的框。',
    bankLabel='词库：',
    eCheck='检查 &middot; 五个房间', tCheck='看守正在查房',
    hC1='一名看守拿着名单走过牢区。要到那道门，你得先过他这一关。',
    bC1='九道题。五个房间混在一起，而且这次屏幕上没有规则。',
    hC2='这里不考新东西。每一题用的都是你去过的房间里的语言。',
    bC2='介词 &middot; there is / there are &middot; 一般过去时 &middot; must '
        '和 mustn&rsquo;t &middot; 比较级和 <em>going to</em>',
    nC='答错一题，就回那个房间把规则那一页再读一遍，然后再去闯门。',
    x1='它在哪里？', x2='一个还是不止一个？', x3='发生了什么？',
    x4='可能，还是禁止？', x5='比较两边的岸',
    x6='计划还是习惯？', x7='写出缺少的词', x8='写出缺少的词',
    x9='把句子组起来',
    t30='五个数字，一道门',
    lockStem='每个房间你都拿到一个数字。这把锁要<strong>倒着</strong>输入 —— '
             '从最后一个房间回到第一个。',
    lockWhy='<strong>Backwards</strong> 就是从最后往前：先是海水，然后是工场、'
            '理发室、通道，最后才是你的牢房。',
    resPerfect='每一道门都一次通过。你离开这座岛了。',
    resStrong='做得好。船已经下水了。',
    resMid='你出了牢房。回去把丢分的房间再走一遍。',
    resLow='还没到门口就被看守抓住了。把规则页再读一遍，重新开始。',
    actTitle='今晚，用你自己的话说',
    actUse='至少用三个：',
    actSpeakBrief='一人扮囚犯，一人扮看守。每做完一题就换角色。',
    actSpeak1='看守：问牢房里五样东西在哪里。囚犯：用 under、behind、next to、'
              'on 和 between 回答。',
    actSpeak2='囚犯：把今晚的计划讲给同伴听，用 <em>I am going to</em> 说四'
              '件事。',
    actSpeak3='看守：用 <em>must</em> 和 <em>mustn&rsquo;t</em> 说五条规定。'
              '囚犯：说出其中一条为什么不合理。',
    actWriteKind='写作 &middot; 80&ndash;120 词',
    actWriteBrief='你已经在船上。给家人写一封短信：你在哪里、拿了什么、做了'
                  '什么、接下来打算做什么。用上两个比较级。',
)

T['ja'] = dict(
    coverTitle='<em>アルカトラズ</em>からの脱出',
    coverSub='鍵のかかった五つの部屋と、五つの英語。数字を集めて最後の門を'
             '開けよう。',
    chipLevel='A2 &middot; 初級', chipFocus='脱出ゲーム',
    chipTime='50&ndash;60 分', chipCount='NN 枚',
    railStops='独房|通路|理髪室|作業場|海',
    eIsland='はじめる前に', eCell='部屋 1 &middot; 独房',
    eCorridor='部屋 2 &middot; 通路', eShop='部屋 3 &middot; 理髪室',
    eWork='部屋 4 &middot; 作業場', eWater='部屋 5 &middot; 海',
    eLock='最後の門', eFind='時間内に見つける',
    t1='ザ・ロックへようこそ',
    h1a='アルカトラズはサンフランシスコ湾の小さな島にあった刑務所です。'
        '1934年に開き、1963年に閉鎖されました。',
    b1a='島は街から約1.25マイル（2キロ）。人々は <strong>The Rock</strong>（岩）'
        'と呼びました。',
    h1b='29年間で脱走の試みは14回。公式には、脱走に成功した囚人は記録されて'
        'いません。',
    b1b='水は冷たく、およそ10&ndash;13&nbsp;&deg;C。潮の流れも'
        '<strong>速い</strong>です。',
    n1='1962年12月、ジョン・ポール・スコットという男が実際に泳いで岸まで'
       'たどり着きました。低体温で衰弱した状態で発見され、連れ戻されました。',
    t2='今夜、あなたは出て行く',
    h2a='あなたはBブロックの囚人です。使えるのは一晩と五つの場所 —— 独房、'
        '通路、理髪室、作業場、そして海。',
    b2a='どの部屋にも<strong>数字が一つ</strong>あります。五つそろえば最後の'
        '門が開きます。',
    h2b='画面下のバーが数字を覚えていてくれます。あなたは英語に集中してくだ'
        'さい。',
    b2b='時計が動く部屋もあります。時計が見えたら<strong>すばやく</strong>'
        '探しましょう。',
    n2='舞台は実在の島です。囚人は架空ですが、1962年の脱走は実話です。',
    t3='どこにある？ in, on, under, behind',
    h3a='物の位置はこれらの語で表します：<strong>in, on, under, behind, next '
        'to, between, above</strong>。',
    h3b='前置詞のあとは <em>the</em> と物。<em>to</em> は決して入れません。',
    n3='<em>Next to</em> は二語です。<em>Between</em> は二つの物と '
       '<em>and</em> が要ります。',
    t4='どこにあるか言う', t5='二つの物、一つの語',
    t6='足りない語を書く', t7='掘るための道具',
    t8='There is は一つ。There are は二つ以上。',
    h8a='一つなら <strong>There is</strong>、二つ以上なら <strong>There '
        'are</strong>。',
    h8b='疑問文と否定文も同じ形をとります。',
    n8='water, air, noise, light に複数形はありません。<em>there is some '
       'water</em> であって <em>there are some waters</em> ではありません。',
    t9='一つ？ それとも二つ以上？', t10='足りない語を書く',
    t11='それぞれの箱に入れる', t12='明かりになるもの',
    t13='彼らがしたこと：過去形',
    h13a='過去に終わった動作には過去形を使います。よく使う動詞には不規則な'
         'ものが多くあります。',
    h13b='否定文と疑問文では <em>did</em> を使い、そのあとは動詞の原形です。',
    n13='<em>did</em>・<em>didn&rsquo;t</em> のあとに過去形は使いません。'
        '<em>Did they took&hellip;</em> は誤りです。',
    t14='1962年6月',
    h14a='1962年6月、三人がアルカトラズを出ました。フランク・モリスと、'
         'ジョンとクラレンスのアングリン兄弟です。四人目のアレン・ウェストは'
         '残りました。',
    h14b='彼らは50着以上のレインコートを集めてゴムボートを作り、屋根に上って'
         '海まで下りました。',
    n14='ウェストは通風口を間に合わせられず、独房に残り、のちに捜査官へ計画を'
        '説明しました。',
    t15='過去形を選ぶ', t16='足りない動詞を書く',
    t17='文を組み立てる', t18='切るための道具',
    t19='can, can&rsquo;t, must, mustn&rsquo;t',
    h19a='<strong>can</strong> = できる。<strong>can&rsquo;t</strong> = '
         'できない。',
    h19b='<strong>must</strong> = しなければならない。'
         '<strong>mustn&rsquo;t</strong> = してはいけない。',
    n19='四つとも、あとには <em>to</em> のない原形が続きます。<em>You must to '
        'go</em> は誤りです。',
    t20='禁止か、不要か', t21='規則を読む',
    t22='規則か、違反か', t23='50着でボートになるもの',
    t24='colder, stronger, more dangerous',
    h24a='短い形容詞は <strong>-er</strong> をつけ、そのあとに '
         '<strong>than</strong> を置きます。',
    h24b='長い形容詞は前に <strong>more</strong>、あとに <strong>than</strong>。',
    n24='今夜必要な不規則な二つ：good &rarr; <strong>better</strong>、bad '
        '&rarr; <strong>worse</strong>。',
    t25='すでに決めてある計画',
    h25a='すでに決めた計画には <strong>be going to</strong> を使い、そのあとは'
         '動詞の原形です。',
    h25b='否定文と疑問文で変わるのは <em>be</em> だけです。',
    n25='<em>Going to go</em> は正しい英語です。初めは奇妙に聞こえますが。',
    t26='二つの岸を比べる', t27='足りない語を書く',
    t28='計画はどれ？', t29='漕ぐための道具',
    orderHint='順番にクリック &middot; もう一度クリックで戻せます',
    sortHint='語句をクリックしてから、入る箱をクリックします。',
    bankLabel='語群：',
    eCheck='点検 &middot; 五つの部屋すべて', tCheck='看守が独房を調べている',
    hC1='看守がリストを持って区画を歩いています。門にたどり着く前に、彼の前を'
        '通らなければなりません。',
    bC1='九問。五つの部屋が混ざっていて、今度は画面に規則は出ません。',
    hC2='新しいことは出ません。どの問題も、すでに通った部屋の英語です。',
    bC2='前置詞 &middot; there is / there are &middot; 過去形 &middot; must と '
        'mustn&rsquo;t &middot; 比較級と <em>going to</em>',
    nC='落としたら、その部屋に戻って規則のページを読み直してから門へ。',
    x1='どこにある？', x2='一つ？ 二つ以上？', x3='何があった？',
    x4='できる？ それとも禁止？', x5='二つの岸を比べる',
    x6='計画？ それとも習慣？', x7='足りない語を書く', x8='足りない語を書く',
    x9='文を組み立てる',
    t30='五つの数字、一つの門',
    lockStem='各部屋で数字を一つずつ手に入れました。この錠は'
             '<strong>逆から</strong>受けつけます —— 最後の部屋から最初の'
             '部屋へ。',
    lockWhy='<strong>Backwards</strong> は終わりから始めへ、という意味です。'
            'まず海、次に作業場、理髪室、通路、最後に独房。',
    resPerfect='どの扉も一度で。島を出ました。',
    resStrong='よくできました。ボートは海の上です。',
    resMid='独房からは出られました。落とした部屋をもう一度回りましょう。',
    resLow='門の前で看守に捕まりました。規則のページを読み直して、最初から。',
    actTitle='今夜のことを、自分の言葉で',
    actUse='三つ以上使うこと：',
    actSpeakBrief='一人が囚人、一人が看守。課題ごとに役を交代します。',
    actSpeak1='看守：独房にある五つの物の場所をたずねる。囚人：under, behind, '
              'next to, on, between を使って答える。',
    actSpeak2='囚人：今夜の計画を相手に話す。<em>I am going to</em> を使って'
              '四つ言う。',
    actSpeak3='看守：<em>must</em> と <em>mustn&rsquo;t</em> で規則を五つ出す。'
              '囚人：そのうち一つがなぜ良くないか言う。',
    actWriteKind='ライティング &middot; 80&ndash;120 語',
    actWriteBrief='あなたはボートの上です。家族へ短い手紙を書いてください。'
                  'どこにいたか、何を持ち出したか、何をしたか、これから何を'
                  'するか。比較級を二つ使うこと。',
)

# The examples are English in every language, by design (see above).
for _c in T:
    if _c != 'en':
        for _k in EXAMPLE_KEYS:
            T[_c][_k] = T['en'][_k]


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT
                        else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in sorted(T.items()):
        m, x = base - set(d), set(d) - base
        print('%-3s %3d' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else 'complete',
              ('EXTRA %s' % sorted(x)) if x else '')
