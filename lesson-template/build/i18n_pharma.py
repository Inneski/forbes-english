# -*- coding: utf-8 -*-
"""Interface strings for The Pharma Sales Interview (B2-C1) — English and German.

This module is the single source for the deck's English text as well as its
German. build_pharma.py imports T['en'] and emits the slides from it rather
than carrying its own copy, which is deliberate: i18n_escalating.py documents
nine keys whose English value drifted from the text in the shipped page, so a
learner switching to German and back got a different, longer slide. Reading
both from one dict makes that class of defect unrepresentable here.

Scope boundary, same as every other deck: the switcher translates the app's
own chrome — cover, section titles, card headings, the notes under them, the
activation briefs, the result bands. It does NOT translate the English being
taught. Every question stem, option, gap sentence, word bank, sort item,
order chunk, explanation and target-language chip stays in English in both
languages, and so do the quoted example lines inside the teaching cards: those
are the sentences the learner has to be able to say, not instructions about
the task. The same applies inside actSpeak1-4, where the interviewer's
questions are quoted — the learner answers those in English.

The card bodies are therefore held in the builder, not here. Only heads and
notes carry keys.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

# Emitted from CHROME verbatim, sorted in with the body. resNext and
# actSpeakKind are NOT lifted: this deck writes its own, and lifting them
# would mean the English page showed the lesson's line while every other
# language silently showed the generic chrome one.
LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'btnOpen',
        'scoreLabel', 'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer',
        'actEyebrow', 'btnCopy', 'btnCopied', 'wordCount']

# Template deck chrome that no lesson declares — the branch ledger's three
# labels, the two glossary buttons and the locked-branch message. Raw JS
# literals, emitted after the body. check-lesson.js's I18N gate fails any
# deck where a data-i18n does not resolve, and these are chrome, so they are
# copied from the template rather than re-invented per lesson.
TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'",
           'glossShow': "'Translate'",
           'ledClues': "'Clues'",
           'ledDp': "'DP'",
           'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'",
           'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'",
           'ledDp': "'DP'",
           'ledTime': "'Zeit'"},
}

T = {}

T['en'] = dict(
    coverTitle='The Pharma Sales <em>Interview</em>',
    coverSub='Two rounds in English, a panel that is not native either, and a track record you have to make audible',
    chipLevel='B2&ndash;C1 &middot; Pharmaceutical sales',
    chipFocus='Fluency under pressure, not vocabulary',
    chipCount='COUNT slides',

    # ── T1 the room ────────────────────────────────────────────────────
    roomEyebrow='The room you are actually walking into',
    roomTitle='A Spanish panel, a German organisation, and English as everyone&rsquo;s second language',
    roomH1='Nobody in the room is a native speaker',
    room1='The winner is not the best English. It is the clearest. Your panel is decoding while it listens, and effort spent decoding is attention not spent on your record.',
    roomH2='Latin words are easier here, not harder',
    room2='A Spanish listener recognises <em>demonstrate</em>, <em>sufficient</em>, <em>obtain</em> instantly. It is the small phrasal verbs that stall them &mdash; the opposite of the usual advice.',
    roomH3='Signpost, and they will follow you anywhere',
    room3='Say how many parts there are before you give them. A listener who knows a list has two items waits for the second; one who does not interrupts.',
    roomH4='Silence is not the emergency',
    room4='A three-second pause reads as thinking. Panels forgive pauses. What they notice is a sentence that restarts three times.',

    # ── T2 buying time ─────────────────────────────────────────────────
    timeEyebrow='When the word will not come',
    timeTitle='Buying three seconds without sounding lost',
    timeH1='Repeat the question as a frame',
    time1='It buys you a second, and it confirms you understood. On a panel working in its second language, doing that openly is a courtesy rather than a stall.',
    timeH2='Name the shape of the answer',
    time2='Now you have a structure to walk into and they have one to wait through. It also stops you starting the same sentence twice.',
    timeH3='Flag the pause instead of filling it',
    time3='A stated pause is a decision. An unstated one is a gap, and the panel fills a gap with its own guess about why you stopped.',
    timeH4='Reach for the near word, then correct upward',
    time4='Say the plain version and repair it out loud. Hunting in silence for <em>payers</em> costs you more than arriving at it a second late.',

    # ── T3 the shape ───────────────────────────────────────────────────
    shapeEyebrow='The shape that survives a second language',
    shapeTitle='Situation &rarr; Move &rarr; Number',
    shapeH1='Situation, in one sentence',
    shape1='One sentence, and stop. The panel does not need the org chart, and every extra clause is another one they have to decode.',
    shapeH2='The move &mdash; what you did, not what happened',
    shape2='First person, active, past simple. <em>We were restructured</em> is a thing that happened to you and tells a panel nothing about you.',
    shapeH3='The number, last',
    shape3='End on it. It is what they write down, and the last thing said is the thing repeated to the person who was not in the room.',

    # ── T4 the numbers sentence ────────────────────────────────────────
    numEyebrow='Making a record audible',
    numTitle='The sentence your track record lives in',
    numH1='Took it from X to Y, in Z',
    num1='The cleanest results sentence in English. A start, an end and a time frame in eleven words, and nothing in it a panel has to take on trust.',
    numH2='Grew, delivered, exceeded',
    num2='Transitive and precise. <em>Was responsible for</em> is the phrase that turns a strong record back into a job description.',
    numH3='Say what you owned, not what you were given',
    num3='<em>I was in charge of</em> is passive in feeling even when it is active in grammar. Hiring panels listen for the verb you choose here.',

    # ── T5 the move ────────────────────────────────────────────────────
    moveEyebrow='The question both interviews will ask',
    moveTitle='Why leave a company like that for one a fraction of the size?',
    moveH1='Move toward, never away',
    move1='A sentence that criticises your current employer is stored by the panel as a prediction about how you will one day talk about them.',
    moveH2='Name what the smaller company has',
    move2='Speed, ownership, proximity to the decision. Say the thing they already believe about themselves &mdash; it is what the question is testing.',
    moveH3='Concede the cost',
    move3='Naming what the move costs you is what makes the reason credible. An answer with no trade-off in it sounds rehearsed, because it usually is.',

    # ── the exercises ──────────────────────────────────────────────────
    sortEyebrow='Sort it before you say it',
    sortTitleA='Which of these makes a non-native panel work harder?',
    sortHintA='Click a line, then click the box it belongs in. Nothing on the right is bad English.',
    sortTitleB='A claim they can check, or a claim about yourself?',
    sortHintB='Both columns are true. Only one of them survives a panel that has heard forty candidates.',

    bankLabel='Word bank:',
    gapEyebrow='The language of the answer',
    gapTitle='Complete the sentence',
    gapHint='One word per gap. Each word in the bank is used exactly once across the two slides.',

    ordEyebrow='Build the sentence',
    ordTitleA='The turnaround answer',
    ordHintA='Click the parts in order. Situation, then the move, then the number &mdash; and it ends on the number.',
    ordTitleB='The reason for moving',
    ordHintB='Click the parts in order. Concede the cost first, then move toward what you want.',

    qEyebrow='Choose the version that works',
    qTitle='Which one would you actually say?',

    # ── activation ─────────────────────────────────────────────────────
    actTitle='Now say it out loud, against a clock',
    actUse='Use at least four:',
    actSpeakKind='Discussion &middot; in pairs',
    actSpeakBrief='In pairs. Ninety seconds per answer, no notes, and swap after each one.',
    actSpeak1='Your partner asks: &ldquo;Tell me about a territory you turned around.&rdquo; Situation, move, number, and stop there.',
    actSpeak2='Swap. &ldquo;Why leave a company like that one for us?&rdquo; Concede the cost, then move toward.',
    actSpeak3='Your partner asks something unprepared. Use a stall phrase out loud first &mdash; they are listening for it.',
    actSpeak4='Now badly on purpose: the same answer, full of idiom. Your partner says where they lost you.',
    actWriteKind='Writing &middot; 180&ndash;220 words',
    actWriteBrief='Both answers you will be asked for. &ldquo;Tell me about yourself&rdquo; in eight sentences, situation to number; &ldquo;Why this move?&rdquo; in four, with one conceded cost. No adjective a panel cannot check.',
    actPlaceholder='I have spent the last six years in pharmaceutical sales, the last three leading a team of…',

    resNext='Recognising the better answer is the easy half. Now produce it &rarr;',
    resPerfect='Full marks. You can hear the difference &mdash; saying it under pressure is the other skill, and that is the activation slide.',
    resStrong='Strong. Look again at the ones you missed: most of them are a phrasal verb or a claim nobody can check.',
    resMid='A workable base. Re-read the two slides on shape and on the numbers sentence before you do the speaking task.',
    resLow='Go back through the five teaching slides. Almost every miss here is an adjective where a number belonged.',
)

T['de'] = dict(
    coverTitle='Das Vorstellungsgespr&auml;ch im <em>Pharmavertrieb</em>',
    coverSub='Zwei Runden auf Englisch, ein Panel, das auch nicht muttersprachlich ist, und eine Bilanz, die h&ouml;rbar werden muss',
    chipLevel='B2&ndash;C1 &middot; Pharmavertrieb',
    chipFocus='Sprachfluss unter Druck, nicht Vokabular',
    chipCount='COUNT Folien',

    roomEyebrow='Der Raum, in den Sie wirklich gehen',
    roomTitle='Ein spanisches Panel, eine deutsche Organisation &mdash; und Englisch ist f&uuml;r alle die zweite Sprache',
    roomH1='Niemand im Raum ist Muttersprachler',
    room1='Es gewinnt nicht das beste Englisch, sondern das klarste. Ihr Panel dekodiert beim Zuh&ouml;ren, und diese M&uuml;he fehlt danach bei Ihrer Bilanz.',
    roomH2='Lateinische W&ouml;rter sind hier leichter, nicht schwerer',
    room2='Eine spanische Zuh&ouml;rerin erkennt <em>demonstrate</em>, <em>sufficient</em>, <em>obtain</em> sofort. Es sind die kleinen Phrasal Verbs, die sie ausbremsen &mdash; das Gegenteil des &uuml;blichen Ratschlags.',
    roomH3='Wegweiser geben &mdash; man folgt Ihnen &uuml;berallhin',
    room3='Sagen Sie vorab, aus wie vielen Teilen die Antwort besteht. Wer zwei Punkte erwartet, wartet den zweiten ab; wer nicht, unterbricht.',
    roomH4='Stille ist nicht der Notfall',
    room4='Drei Sekunden Pause wirken wie Nachdenken. Pausen verzeiht ein Panel. Auff&auml;llig wird der Satz, der dreimal neu ansetzt.',

    timeEyebrow='Wenn das Wort nicht kommt',
    timeTitle='Drei Sekunden gewinnen, ohne verloren zu klingen',
    timeH1='Wiederholen Sie die Frage als Rahmen',
    time1='Das verschafft Ihnen eine Sekunde und best&auml;tigt, dass Sie verstanden haben. Vor einem Panel in seiner Zweitsprache ist das H&ouml;flichkeit, kein Hinhalten.',
    timeH2='Benennen Sie die Form der Antwort',
    time2='Jetzt haben Sie eine Struktur, in die Sie hineinlaufen, und das Panel eine, die es abwartet. Es verhindert auch, denselben Satz zweimal zu beginnen.',
    timeH3='Markieren Sie die Pause, statt sie zu f&uuml;llen',
    time3='Eine angek&uuml;ndigte Pause ist eine Entscheidung. Eine unangek&uuml;ndigte ist eine L&uuml;cke &mdash; und die f&uuml;llt das Panel mit einer eigenen Vermutung.',
    timeH4='Greifen Sie zum naheliegenden Wort und korrigieren Sie nach oben',
    time4='Sagen Sie die einfache Fassung und reparieren Sie sie laut. Stumm nach <em>payers</em> zu suchen kostet mehr, als eine Sekunde sp&auml;ter dort anzukommen.',

    shapeEyebrow='Die Form, die eine Zweitsprache &uuml;bersteht',
    shapeTitle='Situation &rarr; Ma&szlig;nahme &rarr; Zahl',
    shapeH1='Situation, in einem Satz',
    shape1='Ein Satz, dann Schluss. Das Panel braucht kein Organigramm, und jeder Nebensatz ist einer mehr, den es dekodieren muss.',
    shapeH2='Die Ma&szlig;nahme &mdash; was Sie taten, nicht was geschah',
    shape2='Erste Person, Aktiv, Past Simple. <em>We were restructured</em> ist etwas, das Ihnen zugesto&szlig;en ist, und sagt &uuml;ber Sie nichts aus.',
    shapeH3='Die Zahl zum Schluss',
    shape3='H&ouml;ren Sie darauf auf. Sie wird notiert &mdash; und das Zuletztgesagte ist das, was der Person weitererz&auml;hlt wird, die nicht im Raum war.',

    numEyebrow='Eine Bilanz h&ouml;rbar machen',
    numTitle='Der Satz, in dem Ihre Bilanz steckt',
    numH1='Von X auf Y gebracht, in Z',
    num1='Der sauberste Ergebnissatz im Englischen. Anfang, Ende und Zeitraum in elf W&ouml;rtern &mdash; und nichts darin muss man Ihnen glauben.',
    numH2='Grew, delivered, exceeded',
    num2='Transitiv und pr&auml;zise. <em>Was responsible for</em> ist die Wendung, die aus einer starken Bilanz wieder eine Stellenbeschreibung macht.',
    numH3='Sagen Sie, was Sie verantwortet haben, nicht was man Ihnen gab',
    num3='<em>I was in charge of</em> wirkt passiv, auch wenn es grammatisch aktiv ist. Panels achten genau auf das Verb, das Sie hier w&auml;hlen.',

    moveEyebrow='Die Frage, die beide Gespr&auml;che stellen werden',
    moveTitle='Warum ein solches Unternehmen f&uuml;r eines verlassen, das einen Bruchteil so gro&szlig; ist?',
    moveH1='Hin zu etwas, nie weg von etwas',
    move1='Ein Satz, der den jetzigen Arbeitgeber kritisiert, wird vom Panel als Vorhersage dar&uuml;ber abgelegt, wie Sie eines Tages &uuml;ber es selbst sprechen werden.',
    moveH2='Benennen Sie, was das kleinere Haus hat',
    move2='Tempo, Verantwortung, N&auml;he zur Entscheidung. Sagen Sie das, was man dort ohnehin &uuml;ber sich glaubt &mdash; genau das pr&uuml;ft die Frage.',
    moveH3='R&auml;umen Sie den Preis ein',
    move3='Erst wenn Sie benennen, was der Wechsel Sie kostet, wird der Grund glaubw&uuml;rdig. Eine Antwort ohne Abw&auml;gung klingt einstudiert &mdash; meistens zu Recht.',

    sortEyebrow='Sortieren, bevor Sie es sagen',
    sortTitleA='Was davon macht einem nicht-muttersprachlichen Panel mehr M&uuml;he?',
    sortHintA='Klicken Sie eine Zeile an und dann das Feld, in das sie geh&ouml;rt. Nichts rechts ist schlechtes Englisch.',
    sortTitleB='Eine &uuml;berpr&uuml;fbare Angabe oder eine Behauptung &uuml;ber sich selbst?',
    sortHintB='Beide Spalten sind wahr. Nur eine &uuml;bersteht ein Panel, das vierzig Kandidaten geh&ouml;rt hat.',

    bankLabel='Wortliste:',
    gapEyebrow='Die Sprache der Antwort',
    gapTitle='Vervollst&auml;ndigen Sie den Satz',
    gapHint='Ein Wort pro L&uuml;cke. Jedes Wort der Liste wird auf den beiden Folien genau einmal gebraucht.',

    ordEyebrow='Bauen Sie den Satz',
    ordTitleA='Die Turnaround-Antwort',
    ordHintA='Klicken Sie die Teile der Reihe nach an. Situation, dann die Ma&szlig;nahme, dann die Zahl &mdash; und es endet auf der Zahl.',
    ordTitleB='Der Grund f&uuml;r den Wechsel',
    ordHintB='Klicken Sie die Teile der Reihe nach an. Erst den Preis einr&auml;umen, dann hin zu dem, was Sie wollen.',

    qEyebrow='W&auml;hlen Sie die Fassung, die funktioniert',
    qTitle='Welche w&uuml;rden Sie wirklich sagen?',

    actTitle='Jetzt laut, und gegen die Uhr',
    actUse='Mindestens vier verwenden:',
    actSpeakKind='Diskussion &middot; zu zweit',
    actSpeakBrief='Zu zweit. Neunzig Sekunden pro Antwort, ohne Notizen, nach jeder tauschen.',
    actSpeak1='Ihr Gegen&uuml;ber fragt: &ldquo;Tell me about a territory you turned around.&rdquo; Situation, Ma&szlig;nahme, Zahl &mdash; und dort aufh&ouml;ren.',
    actSpeak2='Tauschen. &ldquo;Why leave a company like that one for us?&rdquo; Erst den Preis einr&auml;umen, dann hin zu dem, was Sie wollen.',
    actSpeak3='Ihr Gegen&uuml;ber fragt etwas Unvorbereitetes. Erst h&ouml;rbar eine Verz&ouml;gerungswendung &mdash; darauf wird geachtet.',
    actSpeak4='Jetzt absichtlich schlecht: dieselbe Antwort, voller Idiome. Ihr Gegen&uuml;ber sagt, wo es abgerissen ist.',
    actWriteKind='Schreiben &middot; 180&ndash;220 W&ouml;rter',
    actWriteBrief='Beide Antworten, nach denen gefragt wird. &ldquo;Tell me about yourself&rdquo; in acht S&auml;tzen, von der Situation bis zur Zahl; &ldquo;Why this move?&rdquo; in vier, mit einem einger&auml;umten Preis. Kein Adjektiv, das ein Panel nicht pr&uuml;fen kann.',
    actPlaceholder='I have spent the last six years in pharmaceutical sales, the last three leading a team of…',

    resNext='Die bessere Antwort zu erkennen ist die leichte H&auml;lfte. Jetzt produzieren Sie sie &rarr;',
    resPerfect='Volle Punktzahl. Sie h&ouml;ren den Unterschied &mdash; ihn unter Druck zu sagen ist die andere F&auml;higkeit, und daf&uuml;r gibt es die Aktivierungsfolie.',
    resStrong='Stark. Sehen Sie sich die Fehler noch einmal an: Meist steckt ein Phrasal Verb darin oder eine Behauptung, die niemand pr&uuml;fen kann.',
    resMid='Eine brauchbare Grundlage. Lesen Sie die Folien zur Form und zum Ergebnissatz noch einmal, bevor Sie die Sprech&uuml;bung machen.',
    resLow='Gehen Sie die f&uuml;nf Lehrfolien noch einmal durch. Fast jeder Fehler hier ist ein Adjektiv an der Stelle einer Zahl.',
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
