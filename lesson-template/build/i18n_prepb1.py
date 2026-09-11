# -*- coding: utf-8 -*-
"""Interface strings for Prepositions Double Lesson (B1).

English, German and Spanish. Teach-card bodies use the six-item form, so the
rule text travels with its heading instead of sitting in English under a
translated title.

The English being taught stays English throughout — question stems, options
and the example phrases quoted inside an explanation. A German learner reads
the *rule* in German and the *evidence* in English, which is the split
HOUSE-STYLE §8 asks for.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Prepositions <em>Double Lesson</em>',
    coverSub='Place, time, movement, and the pairs that have to be learned whole',
    chipLevel='B1 · Intermediate', chipFocus='Prepositions',
    chipCount='27 questions',

    t1Eyebrow='Part 1 · Before you start',
    t1Title='In, on, at &mdash; the three that do most of the work',
    t1ah='Inside a space',
    t1ab='<strong>In</strong> means enclosed. A drawer, a box, a room, a pocket '
         '&mdash; if it has sides and something can sit inside them, it takes '
         '<em>in</em>.',
    t1an='The keys are <em>in</em> the drawer.',
    t1bh='On a surface',
    t1bb='<strong>On</strong> means touching a surface. The surface does not have '
         'to be flat or horizontal &mdash; a wall and a ceiling both take '
         '<em>on</em>.',
    t1bn='A map goes <em>on</em> the wall; a crack goes <em>in</em> it. The '
         'surface takes <em>on</em>, the material takes <em>in</em>.',
    t1ch='At a point',
    t1cb='<strong>At</strong> marks one specific point rather than an area '
         '&mdash; an entrance, a desk, a bus stop, the traffic lights.',
    t1cn='<em>At</em> fixes a spot on the map. <em>In</em> fills it.',

    t2Eyebrow='Part 1 · Before you start',
    t2Title='Four more that describe a position',
    t2ah='Two, or more than two',
    t2ab='<strong>Between</strong> needs exactly two clear points &mdash; the '
         'bank sits between the bakery and the pharmacy. <strong>Among</strong> '
         'puts you inside a larger, vaguer group of three or more.',
    t2an='Between two named things; among a crowd.',
    t2bh='Facing it',
    t2bb='<strong>Opposite</strong> means facing something, usually across a '
         'street or a room. The two things look at each other.',
    t2bn='Not the same as <em>next to</em>, which is side by side.',
    t2ch='Out of sight',
    t2cb='<strong>Behind</strong> puts something at the back of something else, '
         'often hidden by it &mdash; the cat behind the sofa.',
    t2cn='Its opposite is <em>in front of</em>, not <em>before</em>, which is '
         'about time.',

    t3Eyebrow='Part 1 · Before you start',
    t3Title='The same three words, now about time',
    t3ah='Long, medium, exact',
    t3ab='<strong>In</strong> takes the long periods &mdash; years, months, '
         'seasons. <strong>On</strong> takes days and dates. <strong>At</strong> '
         'takes clock times.',
    t3an='<em>In</em> 1998, <em>on</em> Saturday mornings, <em>at</em> 9 a.m.',
    t3bh='How long, or since when',
    t3bb='<strong>For</strong> takes a length of time &mdash; seven years, two '
         'hours. <strong>Since</strong> takes the point it started from &mdash; '
         'a date, an event.',
    t3bn='<em>For</em> seven years; <em>since</em> the promotion in March.',
    t3ch='Throughout, or no later than',
    t3cb='<strong>During</strong> means throughout an event. <strong>By</strong> '
         'marks a deadline &mdash; at that time or before it, never after.',
    t3cn='<em>By</em> Friday is a deadline; <em>until</em> Friday is a period '
         'that ends there.',

    t4Eyebrow='Part 2 · Before you start',
    t4Title='Movement: the path matters, not the place',
    t4ah='In, and onto',
    t4ab='<strong>Into</strong> is movement from outside to inside. '
         '<strong>Onto</strong> is movement that ends on top of a surface. Both '
         'describe arriving, not sitting still.',
    t4an='She walked <em>into</em> the office; he lifted the tray <em>onto</em> '
         'the table.',
    t4bh='Enclosed, or open',
    t4bb='<strong>Through</strong> goes in one side of an enclosed space and out '
         'the other &mdash; a tunnel, a forest. <strong>Across</strong> crosses '
         'an open area &mdash; a lake, a square.',
    t4bn='<em>Through</em> the tunnel; <em>across</em> the lake.',
    t4ch='Following a line',
    t4cb='<strong>Along</strong> follows the length of something &mdash; a '
         'river, a road. <strong>To</strong> is the plain one: movement or '
         'transfer towards a destination or a person.',
    t4cn='They jogged <em>along</em> the river; he handed the file <em>to</em> '
         'his manager.',

    t5Eyebrow='Part 2 · Before you start',
    t5Title='Some prepositions are not a choice at all',
    t5ah='The verb chooses for you',
    t5ab='Certain verbs take one fixed preposition and no other. You '
         '<em>depend on</em>, you <em>insist on</em>, you <em>apologise for</em>. '
         'There is no logic to recover &mdash; there is only the pair.',
    t5an='Learn the verb and its preposition as one item, the way you learn a word.',
    t5bh='So does the adjective',
    t5bb='Adjectives behave the same way. <em>Interested in</em>, <em>worried '
         'about</em>, <em>good at</em> &mdash; swapping the preposition does not '
         'give you a variant, it gives you an error.',
    t5bn='Good <em>at</em> a skill. Good <em>for</em> your health. Different '
         'pairs, different meanings.',
    t5ch='Why guessing fails',
    t5cb='Your own language pairs these words differently, so translating the '
         'preposition is the one strategy guaranteed to be wrong. The pair has '
         'to be memorised whole.',
    t5cn='If a fixed phrase feels swappable, that feeling is wrong.',

    mcaEyebrow='Activity 1 · Place', mcaTitle='Where is it?',
    mcbEyebrow='Activity 2 · Time', mcbTitle='When does it happen?',
    mccEyebrow='Activity 3 · Movement', mccTitle='Which way does it go?',
    mcdEyebrow='Activity 4 · Fixed pairs',
    mcdTitle='Which preposition does the word demand?',

    q1why='<strong>In.</strong> A drawer is an enclosed space, and so are boxes '
          'and rooms. Anything with sides you can put something inside takes '
          '<em>in</em>.',
    q2why='<strong>On.</strong> A wall is a surface, and surfaces take '
          '<em>on</em> &mdash; walls, floors, ceilings alike. It does not have '
          'to lie flat.',
    q3why='<strong>At.</strong> An entrance is one specific point rather than an '
          'area, like a desk or a bus stop. <em>In</em> the stadium would put '
          'you inside it.',
    q4why='<strong>Between.</strong> There are exactly two points of reference '
          'here, the bakery and the pharmacy, and <em>between</em> is the word '
          'for exactly two.',
    q5why='<strong>Among.</strong> The strangers are a larger, undefined group '
          '&mdash; three or more with no clear edges. That is <em>among</em>, '
          'not <em>between</em>.',
    q6why='<strong>Opposite.</strong> The cinema faces the supermarket across '
          'the street. <em>Opposite</em> is about facing, not about being '
          'beside.',
    q7why='<strong>Behind.</strong> The cat is at the back of the sofa and out '
          'of sight. <em>Behind</em> is position, and its opposite is <em>in '
          'front of</em>.',

    q8why='<strong>At.</strong> 9 a.m. is a precise clock time, and clock times '
          'take <em>at</em> &mdash; at noon, at midnight, at half past six.',
    q9why='<strong>On.</strong> Days and dates take <em>on</em>, and so does a '
          'named part of a day: on Monday, on 3 June, on Saturday mornings.',
    q10why='<strong>In.</strong> Years take <em>in</em>, along with months and '
           'seasons &mdash; the longer stretches of time.',
    q11why='<strong>For.</strong> Seven years is a length of time, and lengths '
           'take <em>for</em> &mdash; for two hours, for a week.',
    q12why='<strong>Since.</strong> The promotion in March is the point the '
           'feeling started from. <em>Since</em> takes a starting point; '
           '<em>for</em> takes a duration.',
    q13why='<strong>During.</strong> The presentation is the event the sleeping '
           'happened inside. <em>During</em> takes an event; <em>for</em> takes a '
           'number of minutes.',
    q14why='<strong>By.</strong> Friday is a deadline: the report must arrive at '
           'that time or before it. <em>Until</em> Friday would mean a period '
           'that ends there.',

    q15why='<strong>Into.</strong> She moves from outside the office to inside '
           'it. <em>Into</em> is entering; <em>in</em> alone would just be '
           'where she already was.',
    q16why='<strong>Onto.</strong> The tray ends up resting on the table&rsquo;s '
           'surface. <em>Onto</em> is the movement; <em>on</em> is the result.',
    q17why='<strong>Through.</strong> A tunnel is enclosed, and they go in one '
           'end and out the other. That is <em>through</em>, not '
           '<em>across</em>.',
    q18why='<strong>Across.</strong> A lake is an open area crossed from one '
           'side to the other. Open areas take <em>across</em>; enclosed ones '
           'take <em>through</em>.',
    q19why='<strong>Along.</strong> They follow the length of the river rather '
           'than crossing it. <em>Along</em> traces a line &mdash; a river, a '
           'road, a corridor.',
    q20why='<strong>To.</strong> The documents move towards a person. <em>To</em> '
           'is the plain preposition of destination and transfer.',

    q21why='<strong>To.</strong> <em>Look forward to</em> is fixed, and the '
           '<em>to</em> is a preposition, so a verb after it takes <em>-ing</em>: '
           'looking forward to seeing you.',
    q22why='<strong>For.</strong> <em>Apologise for</em> is the fixed pair, and '
           'what follows is the reason for the apology.',
    q23why='<strong>In.</strong> <em>Interested in</em> is a fixed adjective and '
           'preposition pair. No other preposition works after '
           '<em>interested</em>.',
    q24why='<strong>On.</strong> <em>Depend on</em> is fixed. So is <em>rely '
           'on</em>, which means much the same thing.',
    q25why='<strong>About.</strong> <em>Worried about</em> is the standard pair. '
           '<em>Worried for</em> exists but means fearing <em>on someone '
           'else&rsquo;s behalf</em>.',
    q26why='<strong>On.</strong> <em>Insist on</em> is fixed, and means to demand '
           'something firmly. A verb after it takes <em>-ing</em>: insisted on '
           'checking.',
    q27why='<strong>At.</strong> <em>Good at</em> goes before a skill or an '
           'activity. <em>Good for</em> is a different pair meaning beneficial.',

    resPerfect='Perfect score. Place, time, movement and the fixed pairs — all '
               'under control.',
    resStrong='Strong work. Look again at the fixed pairs — that is usually '
              'where the last point goes.',
    resMid='A good base. Go back to the two teaching slides on time: '
           'for/since and during/by are the usual culprits.',
    resLow='Read the five teaching slides again and retry. These are learned '
           'as pairs, not worked out.',

    actTitle='Describe where, when and how',
    actUse='Use at least three:',
    actSpeakBrief='One of you has just moved to the other’s town and needs to '
                  'find five places. One asks, one directs. Four minutes each, '
                  'then swap.',
    actSpeak1='Direct your partner to a shop that sits <em>between</em> two '
              'others, and to one <em>opposite</em> the station.',
    actSpeak2='Say how long you have lived where you live, using <em>for</em> '
              'and <em>since</em>, and what changed <em>during</em> that time.',
    actSpeak3='Tell your partner three things you are <em>good at</em>, '
              '<em>interested in</em> or <em>worried about</em>, and why.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write directions for a friend arriving at your local station '
                  'for the first time: where to meet you, how to get there, and '
                  'what time to be there by. Use at least three of the '
                  'expressions above.',
    actPlaceholder='Meet me at…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Präpositionen <em>Doppelstunde</em>',
    coverSub='Ort, Zeit, Bewegung und die Paare, die man als Ganzes lernen muss',
    chipLevel='B1 · Mittelstufe', chipFocus='Präpositionen',
    chipCount='27 Fragen',

    t1Eyebrow='Teil 1 · Bevor du anfängst',
    t1Title='In, on, at &mdash; die drei, die die meiste Arbeit machen',
    t1ah='In einem Raum',
    t1ab='<strong>In</strong> heißt umschlossen. Eine Schublade, eine Kiste, ein '
         'Zimmer, eine Tasche &mdash; wenn etwas Seiten hat und man etwas '
         'hineinlegen kann, steht <em>in</em>.',
    t1an='The keys are <em>in</em> the drawer.',
    t1bh='Auf einer Fläche',
    t1bb='<strong>On</strong> heißt, eine Fläche zu berühren. Die Fläche muss '
         'weder flach noch waagerecht sein &mdash; eine Wand und eine Decke '
         'nehmen beide <em>on</em>.',
    t1bn='A map hängt <em>on</em> the wall; a crack sitzt <em>in</em> it. Die '
         'Oberfläche nimmt <em>on</em>, das Material nimmt <em>in</em>.',
    t1ch='An einem Punkt',
    t1cb='<strong>At</strong> markiert einen bestimmten Punkt statt einer Fläche '
         '&mdash; einen Eingang, einen Schreibtisch, eine Haltestelle, die Ampel.',
    t1cn='<em>At</em> setzt einen Punkt auf die Karte. <em>In</em> füllt ihn aus.',

    t2Eyebrow='Teil 1 · Bevor du anfängst',
    t2Title='Vier weitere, die eine Position beschreiben',
    t2ah='Zwei, oder mehr als zwei',
    t2ab='<strong>Between</strong> braucht genau zwei klare Bezugspunkte '
         '&mdash; die Bank liegt zwischen der Bäckerei und der Apotheke. '
         '<strong>Among</strong> setzt dich in eine größere, unschärfere Gruppe '
         'von drei oder mehr.',
    t2an='Between bei zwei genannten Dingen; among in einer Menge.',
    t2bh='Gegenüber',
    t2bb='<strong>Opposite</strong> heißt, etwas zugewandt zu sein, meist über '
         'eine Straße oder einen Raum hinweg. Die beiden Dinge schauen '
         'einander an.',
    t2bn='Nicht dasselbe wie <em>next to</em>, das nebeneinander bedeutet.',
    t2ch='Außer Sicht',
    t2cb='<strong>Behind</strong> setzt etwas an die Rückseite von etwas '
         'anderem, oft dahinter verborgen &mdash; die Katze hinter dem Sofa.',
    t2cn='Das Gegenteil ist <em>in front of</em>, nicht <em>before</em>, das '
         'sich auf Zeit bezieht.',

    t3Eyebrow='Teil 1 · Bevor du anfängst',
    t3Title='Dieselben drei Wörter, jetzt für die Zeit',
    t3ah='Lang, mittel, genau',
    t3ab='<strong>In</strong> nimmt die langen Zeiträume &mdash; Jahre, Monate, '
         'Jahreszeiten. <strong>On</strong> nimmt Tage und Daten. '
         '<strong>At</strong> nimmt Uhrzeiten.',
    t3an='<em>In</em> 1998, <em>on</em> Saturday mornings, <em>at</em> 9 a.m.',
    t3bh='Wie lange, oder seit wann',
    t3bb='<strong>For</strong> nimmt eine Zeitspanne &mdash; sieben Jahre, zwei '
         'Stunden. <strong>Since</strong> nimmt den Punkt, an dem es begann '
         '&mdash; ein Datum, ein Ereignis.',
    t3bn='<em>For</em> seven years; <em>since</em> the promotion in March.',
    t3ch='Währenddessen, oder spätestens',
    t3cb='<strong>During</strong> heißt während eines Ereignisses. '
         '<strong>By</strong> markiert eine Frist &mdash; zu diesem Zeitpunkt '
         'oder davor, niemals danach.',
    t3cn='<em>By</em> Friday ist eine Frist; <em>until</em> Friday ist ein '
         'Zeitraum, der dann endet.',

    t4Eyebrow='Teil 2 · Bevor du anfängst',
    t4Title='Bewegung: der Weg zählt, nicht der Ort',
    t4ah='Hinein und hinauf',
    t4ab='<strong>Into</strong> ist Bewegung von außen nach innen. '
         '<strong>Onto</strong> ist Bewegung, die auf einer Fläche endet. Beide '
         'beschreiben ein Ankommen, kein Stillstehen.',
    t4an='She walked <em>into</em> the office; he lifted the tray <em>onto</em> '
         'the table.',
    t4bh='Umschlossen oder offen',
    t4bb='<strong>Through</strong> geht an einer Seite eines umschlossenen Raums '
         'hinein und an der anderen hinaus &mdash; ein Tunnel, ein Wald. '
         '<strong>Across</strong> überquert eine offene Fläche &mdash; einen '
         'See, einen Platz.',
    t4bn='<em>Through</em> the tunnel; <em>across</em> the lake.',
    t4ch='Einer Linie folgen',
    t4cb='<strong>Along</strong> folgt der Länge von etwas &mdash; einem Fluss, '
         'einer Straße. <strong>To</strong> ist das schlichte: Bewegung oder '
         'Übergabe hin zu einem Ziel oder einer Person.',
    t4cn='They jogged <em>along</em> the river; he handed the file <em>to</em> '
         'his manager.',

    t5Eyebrow='Teil 2 · Bevor du anfängst',
    t5Title='Manche Präpositionen sind gar keine Wahl',
    t5ah='Das Verb entscheidet für dich',
    t5ab='Bestimmte Verben nehmen genau eine feste Präposition und keine andere. '
         'Man sagt <em>depend on</em>, <em>insist on</em>, <em>apologise '
         'for</em>. Es gibt keine Logik zu rekonstruieren &mdash; es gibt nur '
         'das Paar.',
    t5an='Lerne das Verb und seine Präposition als eine Einheit, so wie du ein '
         'Wort lernst.',
    t5bh='Das Adjektiv auch',
    t5bb='Adjektive verhalten sich genauso. <em>Interested in</em>, <em>worried '
         'about</em>, <em>good at</em> &mdash; die Präposition zu tauschen gibt '
         'dir keine Variante, sondern einen Fehler.',
    t5bn='Good <em>at</em> bei einer Fähigkeit. Good <em>for</em> bei der '
         'Gesundheit. Andere Paare, andere Bedeutung.',
    t5ch='Warum Raten scheitert',
    t5cb='Deine eigene Sprache kombiniert diese Wörter anders, deshalb ist das '
         'Übersetzen der Präposition die einzige Strategie, die garantiert '
         'falsch ist. Das Paar muss als Ganzes gelernt werden.',
    t5cn='Wenn sich eine feste Wendung austauschbar anfühlt, täuscht dieses '
         'Gefühl.',

    mcaEyebrow='Übung 1 · Ort', mcaTitle='Wo ist es?',
    mcbEyebrow='Übung 2 · Zeit', mcbTitle='Wann passiert es?',
    mccEyebrow='Übung 3 · Bewegung', mccTitle='In welche Richtung geht es?',
    mcdEyebrow='Übung 4 · Feste Paare',
    mcdTitle='Welche Präposition verlangt das Wort?',

    q1why='<strong>In.</strong> Eine Schublade ist ein umschlossener Raum, ebenso '
          'Kisten und Zimmer. Alles mit Seiten, in das man etwas legen kann, '
          'nimmt <em>in</em>.',
    q2why='<strong>On.</strong> Eine Wand ist eine Fläche, und Flächen nehmen '
          '<em>on</em> &mdash; Wände, Böden und Decken gleichermaßen. Sie muss '
          'nicht waagerecht liegen.',
    q3why='<strong>At.</strong> Ein Eingang ist ein bestimmter Punkt und keine '
          'Fläche, wie ein Schreibtisch oder eine Haltestelle. <em>In</em> the '
          'stadium wäre im Inneren.',
    q4why='<strong>Between.</strong> Es gibt hier genau zwei Bezugspunkte, die '
          'Bäckerei und die Apotheke, und <em>between</em> ist das Wort für '
          'genau zwei.',
    q5why='<strong>Among.</strong> Die Fremden sind eine größere, unbestimmte '
          'Gruppe &mdash; drei oder mehr ohne klare Ränder. Das ist '
          '<em>among</em>, nicht <em>between</em>.',
    q6why='<strong>Opposite.</strong> Das Kino liegt dem Supermarkt über die '
          'Straße hinweg gegenüber. Bei <em>opposite</em> geht es um '
          'Zugewandtsein, nicht um Danebenstehen.',
    q7why='<strong>Behind.</strong> Die Katze ist an der Rückseite des Sofas und '
          'außer Sicht. <em>Behind</em> ist eine Position, und ihr Gegenteil ist '
          '<em>in front of</em>.',

    q8why='<strong>At.</strong> 9 a.m. ist eine genaue Uhrzeit, und Uhrzeiten '
          'nehmen <em>at</em> &mdash; at noon, at midnight, at half past six.',
    q9why='<strong>On.</strong> Tage und Daten nehmen <em>on</em>, und ein '
          'benannter Tagesabschnitt ebenso: on Monday, on 3 June, on Saturday '
          'mornings.',
    q10why='<strong>In.</strong> Jahre nehmen <em>in</em>, ebenso Monate und '
           'Jahreszeiten &mdash; die längeren Zeiträume.',
    q11why='<strong>For.</strong> Sieben Jahre ist eine Zeitspanne, und '
           'Zeitspannen nehmen <em>for</em> &mdash; for two hours, for a week.',
    q12why='<strong>Since.</strong> Die Beförderung im März ist der Punkt, an '
           'dem das Gefühl begann. <em>Since</em> nimmt einen Anfangspunkt; '
           '<em>for</em> nimmt eine Dauer.',
    q13why='<strong>During.</strong> Die Präsentation ist das Ereignis, in dessen '
           'Verlauf sie einschliefen. <em>During</em> nimmt ein Ereignis; '
           '<em>for</em> nimmt eine Anzahl von Minuten.',
    q14why='<strong>By.</strong> Freitag ist eine Frist: der Bericht muss zu '
           'diesem Zeitpunkt oder davor da sein. <em>Until</em> Friday wäre ein '
           'Zeitraum, der dann endet.',

    q15why='<strong>Into.</strong> Sie bewegt sich von außerhalb des Büros nach '
           'innen. <em>Into</em> ist das Hineingehen; <em>in</em> allein wäre '
           'nur, wo sie schon war.',
    q16why='<strong>Onto.</strong> Das Tablett landet auf der Fläche des '
           'Tisches. <em>Onto</em> ist die Bewegung; <em>on</em> ist das '
           'Ergebnis.',
    q17why='<strong>Through.</strong> Ein Tunnel ist umschlossen, und sie fahren '
           'an einem Ende hinein und am anderen hinaus. Das ist '
           '<em>through</em>, nicht <em>across</em>.',
    q18why='<strong>Across.</strong> Ein See ist eine offene Fläche, die man von '
           'einer Seite zur anderen überquert. Offene Flächen nehmen '
           '<em>across</em>, umschlossene <em>through</em>.',
    q19why='<strong>Along.</strong> Sie folgen der Länge des Flusses, statt ihn '
           'zu überqueren. <em>Along</em> zeichnet eine Linie nach &mdash; '
           'einen Fluss, eine Straße, einen Flur.',
    q20why='<strong>To.</strong> Die Unterlagen bewegen sich hin zu einer '
           'Person. <em>To</em> ist die schlichte Präposition für Ziel und '
           'Übergabe.',

    q21why='<strong>To.</strong> <em>Look forward to</em> ist fest, und das '
           '<em>to</em> ist eine Präposition &mdash; ein Verb danach steht auf '
           '<em>-ing</em>: looking forward to seeing you.',
    q22why='<strong>For.</strong> <em>Apologise for</em> ist das feste Paar, und '
           'was folgt, ist der Grund der Entschuldigung.',
    q23why='<strong>In.</strong> <em>Interested in</em> ist ein festes Paar aus '
           'Adjektiv und Präposition. Nach <em>interested</em> funktioniert '
           'keine andere.',
    q24why='<strong>On.</strong> <em>Depend on</em> ist fest. Ebenso <em>rely '
           'on</em>, das ungefähr dasselbe bedeutet.',
    q25why='<strong>About.</strong> <em>Worried about</em> ist das übliche Paar. '
           '<em>Worried for</em> gibt es, meint aber die Sorge <em>um jemand '
           'anderen</em>.',
    q26why='<strong>On.</strong> <em>Insist on</em> ist fest und heißt, etwas '
           'nachdrücklich zu verlangen. Ein Verb danach steht auf <em>-ing</em>: '
           'insisted on checking.',
    q27why='<strong>At.</strong> <em>Good at</em> steht vor einer Fähigkeit oder '
           'Tätigkeit. <em>Good for</em> ist ein anderes Paar und heißt '
           'zuträglich.',

    resPerfect='Volle Punktzahl. Ort, Zeit, Bewegung und die festen Paare — '
               'alles im Griff.',
    resStrong='Starke Leistung. Sieh dir die festen Paare noch einmal an — dort '
              'geht meist der letzte Punkt verloren.',
    resMid='Eine gute Grundlage. Geh zurück zu den beiden Lernfolien zur Zeit: '
           'for/since und during/by sind die üblichen Stolpersteine.',
    resLow='Lies die fünf Lernfolien noch einmal und versuch es erneut. Diese '
           'Paare werden gelernt, nicht hergeleitet.',

    actTitle='Beschreibe wo, wann und wie',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Eine, einer von euch ist gerade in die Stadt der anderen '
                  'Person gezogen und sucht fünf Orte. Eine Person fragt, die '
                  'andere erklärt den Weg. Vier Minuten pro Person, dann '
                  'tauschen.',
    actSpeak1='Lotse deinen Partner zu einem Laden, der <em>between</em> zwei '
              'anderen liegt, und zu einem <em>opposite</em> dem Bahnhof.',
    actSpeak2='Sag, wie lange du schon dort wohnst, wo du wohnst — mit '
              '<em>for</em> und <em>since</em> — und was sich <em>during</em> '
              'dieser Zeit verändert hat.',
    actSpeak3='Nenne deinem Partner drei Dinge, in denen du <em>good at</em> '
              'bist, an denen du <em>interested in</em> bist oder über die du '
              '<em>worried about</em> bist, und warum.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreibe einer Freundin oder einem Freund eine Wegbeschreibung '
                  'für die erste Ankunft an deinem Bahnhof: wo ihr euch trefft, '
                  'wie man dorthin kommt und bis wann man da sein soll. Verwende '
                  'mindestens drei der Ausdrücke oben.',
    actPlaceholder='Meet me at…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Preposiciones <em>Clase doble</em>',
    coverSub='Lugar, tiempo, movimiento y las parejas que hay que aprender enteras',
    chipLevel='B1 · Intermedio', chipFocus='Preposiciones',
    chipCount='27 preguntas',

    t1Eyebrow='Parte 1 · Antes de empezar',
    t1Title='In, on, at &mdash; las tres que hacen casi todo el trabajo',
    t1ah='Dentro de un espacio',
    t1ab='<strong>In</strong> significa cerrado. Un cajón, una caja, una '
         'habitación, un bolsillo &mdash; si tiene lados y algo puede quedarse '
         'dentro, lleva <em>in</em>.',
    t1an='The keys are <em>in</em> the drawer.',
    t1bh='Sobre una superficie',
    t1bb='<strong>On</strong> significa tocar una superficie. La superficie no '
         'tiene por qué ser plana ni horizontal &mdash; una pared y un techo '
         'llevan las dos <em>on</em>.',
    t1bn='A map va <em>on</em> the wall; a crack va <em>in</em> it. La '
         'superficie lleva <em>on</em>, el material lleva <em>in</em>.',
    t1ch='En un punto',
    t1cb='<strong>At</strong> marca un punto concreto en lugar de una zona '
         '&mdash; una entrada, un escritorio, una parada, el semáforo.',
    t1cn='<em>At</em> fija un punto en el mapa. <em>In</em> lo llena.',

    t2Eyebrow='Parte 1 · Antes de empezar',
    t2Title='Otras cuatro que describen una posición',
    t2ah='Dos, o más de dos',
    t2ab='<strong>Between</strong> necesita exactamente dos puntos de referencia '
         '&mdash; el banco está entre la panadería y la farmacia. '
         '<strong>Among</strong> te sitúa dentro de un grupo mayor y más difuso, '
         'de tres o más.',
    t2an='Between con dos cosas nombradas; among en una multitud.',
    t2bh='Enfrente',
    t2bb='<strong>Opposite</strong> significa estar frente a algo, normalmente al '
         'otro lado de una calle o de una sala. Las dos cosas se miran.',
    t2bn='No es lo mismo que <em>next to</em>, que es al lado.',
    t2ch='Fuera de la vista',
    t2cb='<strong>Behind</strong> coloca algo en la parte de atrás de otra cosa, '
         'a menudo oculto por ella &mdash; el gato detrás del sofá.',
    t2cn='Su contrario es <em>in front of</em>, no <em>before</em>, que es de '
         'tiempo.',

    t3Eyebrow='Parte 1 · Antes de empezar',
    t3Title='Las mismas tres palabras, ahora para el tiempo',
    t3ah='Largo, medio, exacto',
    t3ab='<strong>In</strong> lleva los periodos largos &mdash; años, meses, '
         'estaciones. <strong>On</strong> lleva días y fechas. '
         '<strong>At</strong> lleva las horas del reloj.',
    t3an='<em>In</em> 1998, <em>on</em> Saturday mornings, <em>at</em> 9 a.m.',
    t3bh='Cuánto tiempo, o desde cuándo',
    t3bb='<strong>For</strong> lleva una duración &mdash; siete años, dos horas. '
         '<strong>Since</strong> lleva el punto de partida &mdash; una fecha, un '
         'acontecimiento.',
    t3bn='<em>For</em> seven years; <em>since</em> the promotion in March.',
    t3ch='Durante, o como muy tarde',
    t3cb='<strong>During</strong> significa a lo largo de un acontecimiento. '
         '<strong>By</strong> marca un plazo &mdash; en ese momento o antes, '
         'nunca después.',
    t3cn='<em>By</em> Friday es un plazo; <em>until</em> Friday es un periodo '
         'que termina ahí.',

    t4Eyebrow='Parte 2 · Antes de empezar',
    t4Title='Movimiento: importa el recorrido, no el lugar',
    t4ah='Hacia dentro y hacia encima',
    t4ab='<strong>Into</strong> es movimiento de fuera hacia dentro. '
         '<strong>Onto</strong> es movimiento que termina encima de una '
         'superficie. Las dos describen una llegada, no una posición quieta.',
    t4an='She walked <em>into</em> the office; he lifted the tray <em>onto</em> '
         'the table.',
    t4bh='Cerrado o abierto',
    t4bb='<strong>Through</strong> entra por un lado de un espacio cerrado y sale '
         'por el otro &mdash; un túnel, un bosque. <strong>Across</strong> '
         'cruza una zona abierta &mdash; un lago, una plaza.',
    t4bn='<em>Through</em> the tunnel; <em>across</em> the lake.',
    t4ch='Seguir una línea',
    t4cb='<strong>Along</strong> sigue el largo de algo &mdash; un río, una '
         'carretera. <strong>To</strong> es la sencilla: movimiento o entrega '
         'hacia un destino o una persona.',
    t4cn='They jogged <em>along</em> the river; he handed the file <em>to</em> '
         'his manager.',

    t5Eyebrow='Parte 2 · Antes de empezar',
    t5Title='Algunas preposiciones no son una elección',
    t5ah='El verbo elige por ti',
    t5ab='Ciertos verbos llevan una preposición fija y ninguna otra. Se dice '
         '<em>depend on</em>, <em>insist on</em>, <em>apologise for</em>. No hay '
         'ninguna lógica que recuperar &mdash; solo existe la pareja.',
    t5an='Aprende el verbo y su preposición como una sola unidad, igual que '
         'aprendes una palabra.',
    t5bh='El adjetivo también',
    t5bb='Los adjetivos funcionan igual. <em>Interested in</em>, <em>worried '
         'about</em>, <em>good at</em> &mdash; cambiar la preposición no te da '
         'una variante, te da un error.',
    t5bn='Good <em>at</em> con una habilidad. Good <em>for</em> con la salud. '
         'Parejas distintas, significados distintos.',
    t5ch='Por qué falla adivinar',
    t5cb='Tu propia lengua combina estas palabras de otra manera, así que '
         'traducir la preposición es la única estrategia que seguro falla. La '
         'pareja hay que memorizarla entera.',
    t5cn='Si una expresión fija te parece intercambiable, esa sensación es '
         'falsa.',

    mcaEyebrow='Actividad 1 · Lugar', mcaTitle='¿Dónde está?',
    mcbEyebrow='Actividad 2 · Tiempo', mcbTitle='¿Cuándo ocurre?',
    mccEyebrow='Actividad 3 · Movimiento', mccTitle='¿En qué dirección va?',
    mcdEyebrow='Actividad 4 · Parejas fijas',
    mcdTitle='¿Qué preposición exige la palabra?',

    q1why='<strong>In.</strong> Un cajón es un espacio cerrado, igual que las '
          'cajas y las habitaciones. Todo lo que tiene lados y admite algo '
          'dentro lleva <em>in</em>.',
    q2why='<strong>On.</strong> Una pared es una superficie, y las superficies '
          'llevan <em>on</em> &mdash; paredes, suelos y techos por igual. No '
          'tiene que estar en horizontal.',
    q3why='<strong>At.</strong> Una entrada es un punto concreto, no una zona, '
          'como un escritorio o una parada. <em>In</em> the stadium sería dentro '
          'de él.',
    q4why='<strong>Between.</strong> Aquí hay exactamente dos puntos de '
          'referencia, la panadería y la farmacia, y <em>between</em> es la '
          'palabra para exactamente dos.',
    q5why='<strong>Among.</strong> Los desconocidos son un grupo mayor e '
          'indefinido &mdash; tres o más sin límites claros. Eso es '
          '<em>among</em>, no <em>between</em>.',
    q6why='<strong>Opposite.</strong> El cine está frente al supermercado, al '
          'otro lado de la calle. <em>Opposite</em> trata de estar enfrente, no '
          'al lado.',
    q7why='<strong>Behind.</strong> El gato está en la parte de atrás del sofá y '
          'fuera de la vista. <em>Behind</em> es posición, y su contrario es '
          '<em>in front of</em>.',

    q8why='<strong>At.</strong> Las 9 a.m. son una hora exacta, y las horas '
          'llevan <em>at</em> &mdash; at noon, at midnight, at half past six.',
    q9why='<strong>On.</strong> Los días y las fechas llevan <em>on</em>, y '
          'también una parte concreta de un día: on Monday, on 3 June, on '
          'Saturday mornings.',
    q10why='<strong>In.</strong> Los años llevan <em>in</em>, igual que los meses '
           'y las estaciones &mdash; los tramos de tiempo más largos.',
    q11why='<strong>For.</strong> Siete años es una duración, y las duraciones '
           'llevan <em>for</em> &mdash; for two hours, for a week.',
    q12why='<strong>Since.</strong> El ascenso de marzo es el punto en que empezó '
           'esa sensación. <em>Since</em> lleva un punto de partida; <em>for</em> '
           'lleva una duración.',
    q13why='<strong>During.</strong> La presentación es el acontecimiento durante '
           'el cual se quedaron dormidos. <em>During</em> lleva un '
           'acontecimiento; <em>for</em> lleva un número de minutos.',
    q14why='<strong>By.</strong> El viernes es un plazo: el informe debe llegar '
           'ese día o antes. <em>Until</em> Friday sería un periodo que termina '
           'ahí.',

    q15why='<strong>Into.</strong> Ella pasa de fuera de la oficina a dentro. '
           '<em>Into</em> es entrar; <em>in</em> a secas sería solo dónde ya '
           'estaba.',
    q16why='<strong>Onto.</strong> La bandeja acaba apoyada en la superficie de '
           'la mesa. <em>Onto</em> es el movimiento; <em>on</em> es el '
           'resultado.',
    q17why='<strong>Through.</strong> Un túnel es cerrado, y entran por un '
           'extremo y salen por el otro. Eso es <em>through</em>, no '
           '<em>across</em>.',
    q18why='<strong>Across.</strong> Un lago es una zona abierta que se cruza de '
           'un lado a otro. Las zonas abiertas llevan <em>across</em>; las '
           'cerradas, <em>through</em>.',
    q19why='<strong>Along.</strong> Siguen el largo del río en lugar de cruzarlo. '
           '<em>Along</em> recorre una línea &mdash; un río, una carretera, un '
           'pasillo.',
    q20why='<strong>To.</strong> Los documentos se mueven hacia una persona. '
           '<em>To</em> es la preposición sencilla de destino y entrega.',

    q21why='<strong>To.</strong> <em>Look forward to</em> es fija, y ese '
           '<em>to</em> es una preposición, así que el verbo que sigue va en '
           '<em>-ing</em>: looking forward to seeing you.',
    q22why='<strong>For.</strong> <em>Apologise for</em> es la pareja fija, y lo '
           'que sigue es el motivo de la disculpa.',
    q23why='<strong>In.</strong> <em>Interested in</em> es una pareja fija de '
           'adjetivo y preposición. Después de <em>interested</em> no funciona '
           'ninguna otra.',
    q24why='<strong>On.</strong> <em>Depend on</em> es fija. También lo es '
           '<em>rely on</em>, que significa prácticamente lo mismo.',
    q25why='<strong>About.</strong> <em>Worried about</em> es la pareja habitual. '
           '<em>Worried for</em> existe, pero expresa temor <em>por otra '
           'persona</em>.',
    q26why='<strong>On.</strong> <em>Insist on</em> es fija y significa exigir '
           'algo con firmeza. El verbo que sigue va en <em>-ing</em>: insisted '
           'on checking.',
    q27why='<strong>At.</strong> <em>Good at</em> va delante de una habilidad o '
           'una actividad. <em>Good for</em> es otra pareja y significa '
           'beneficioso.',

    resPerfect='Puntuación perfecta. Lugar, tiempo, movimiento y las parejas '
               'fijas — todo controlado.',
    resStrong='Muy bien. Vuelve a mirar las parejas fijas — ahí suele irse el '
              'último punto.',
    resMid='Buena base. Vuelve a las dos diapositivas de tiempo: for/since y '
           'during/by son los tropiezos habituales.',
    resLow='Lee otra vez las cinco diapositivas de enseñanza y prueba de nuevo. '
           'Estas parejas se aprenden, no se deducen.',

    actTitle='Describe dónde, cuándo y cómo',
    actUse='Usa al menos tres:',
    actSpeakBrief='Una de las dos personas acaba de mudarse a la ciudad de la '
                  'otra y necesita encontrar cinco sitios. Una pregunta, la otra '
                  'indica el camino. Cuatro minutos cada una, luego cambiad.',
    actSpeak1='Guía a tu compañero hasta una tienda que está <em>between</em> '
              'otras dos, y hasta otra <em>opposite</em> la estación.',
    actSpeak2='Di cuánto tiempo llevas viviendo donde vives, con <em>for</em> y '
              '<em>since</em>, y qué cambió <em>during</em> ese tiempo.',
    actSpeak3='Dile a tu compañero tres cosas en las que eres <em>good at</em>, '
              '<em>interested in</em> o <em>worried about</em>, y por qué.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe indicaciones para un amigo que llega por primera vez '
                  'a tu estación: dónde quedáis, cómo llegar y a qué hora debe '
                  'estar allí como muy tarde. Usa al menos tres de las '
                  'expresiones anteriores.',
    actPlaceholder='Meet me at…',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
