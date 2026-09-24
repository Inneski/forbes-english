# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Yes / No / Not Given.

Ten languages, teach cards in the six-item form: English, German and Spanish
from the start, and French, Italian, Portuguese, Russian, Arabic, Chinese and
Japanese added on 2026-09-24 (conventions in `ielts_langs.py`). `T['en']` is
the only copy of the English: `build_ieltsynng.py` reads the markup from it,
so the deck and the English gloss cannot drift apart.

Same split as the rest of the IELTS route (HOUSE-STYLE §8): the rule and the
reason travel, the English under test does not. Passages, statements, the six
sentence openings on the sorting slide and every example in <em> stay English
in every gloss, because the skill is reading that English and deciding whose
view it is.

The verdicts are split down the middle. The word before the dash — Yes, No,
Not Given — stays English: it is what the candidate writes on the answer
sheet, and the wrong word scores nothing. The gloss after it translates, so a
learner meeting Yes / No / Not Given for the first time knows what each one
claims before the first item.

"The writer" is "der Autor" and "el autor" on every slide: one noun, used the
same way throughout, so nobody wonders whether "der Verfasser" on slide 12 is
a different person.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
from ielts_langs import TAIL_MORE
from ieltsynng_data import VERDICTS

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
TAIL.update(TAIL_MORE)

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='The same three-way choice as True, False, Not Given &mdash; '
             'asked about what the writer thinks, not what the passage says',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='Same three-way choice, a different question',
    t1ah='Views, not facts',
    t1ab='True / False / Not Given asks what the passage <em>says</em>. '
         'Yes / No / Not Given asks what the writer <em>thinks</em>. The '
         'instructions give it away: <em>Do the following statements agree '
         'with the views of the writer?</em>',
    t1an='Sometimes the wording is <em>claims</em> rather than <em>views</em>. '
         'The method is the same.',
    t1bh='Where you meet it',
    t1bb='In passages that argue: opinion pieces, reviews, essays with a point '
         'to make. You will meet it most often in the last section, the one '
         'most likely to argue.',
    t1bn='Write the word the instructions ask for. YES on a True / False / '
         'Not Given question is marked wrong, even when you meant TRUE.',
    t1ch='Same check as True / False / Not Given',
    t1cb='<strong>Can I point at the sentence?</strong> Only now it has to be '
         'a sentence in which the writer speaks. If the only line you can '
         'find is someone else&rsquo;s opinion, you have not found the answer '
         'yet.',
    t1cn='YES and NO need the writer&rsquo;s voice. NOT GIVEN is the '
         'writer&rsquo;s silence.',

    t2Eyebrow='Before you start',
    t2Title='Whose voice is it?',
    t2ah='Views the writer reports',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. The view is in the passage, '
         'but the writer has not signed it. On its own, it can only give you '
         'NOT GIVEN.',
    t2an='These sentences state the claim in full, so word-matching finds '
         'them first. That is exactly what makes them traps.',
    t2bh='The writer&rsquo;s own voice',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'and far more often, no marker at all. In a passage that argues, a '
         'plain statement with nobody else&rsquo;s name on it is the '
         'writer&rsquo;s.',
    t2bn='Most markers point at other people&rsquo;s views; most of the '
         'writer&rsquo;s own views carry none.',
    t2ch='Reported, then judged',
    t2cb='<em>Supporters say it works. They are right.</em> The second '
         'sentence makes the view the writer&rsquo;s own. <em>They are '
         'wrong</em> would make the opposite the writer&rsquo;s view.',
    t2cn='One word can do it: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Before you start',
    t3Title='Admittedly &hellip; but',
    t3ah='The concession',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (which concedes the opposite of what '
         'follows it). The writer grants the other side a point &mdash; and '
         'it is still the writer speaking. A point conceded is a point the '
         'writer accepts.',
    t3an='Contradict a concession and the answer is NO, even when the '
         'statement sounds like the writer&rsquo;s side.',
    t3bh='The turn',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. What '
         'follows is the writer&rsquo;s main claim. It outweighs the '
         'concession; it does not cancel it.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> The writer holds both.',
    t3ch='What neither half says',
    t3cb='The turn invites you to finish the argument for the writer. Do not. '
         'A statement that goes further than either half &mdash; about what '
         'happened next, or what it all adds up to &mdash; is NOT GIVEN.',
    t3cn='<em>Cheaper to run</em> is not <em>cheaper overall</em>. Only one '
         'of them is on the page.',

    t4Eyebrow='Before you start',
    t4Title='How strongly does the writer mean it?',
    t4ah='Degree',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. The writer is claiming part of something. A statement '
         'claiming all of it &mdash; <em>completely</em>, <em>in every '
         'way</em>, <em>everything</em> &mdash; is NO.',
    t4an='The same rule as <em>most</em> against <em>all</em> on a True / '
         'False / Not Given paper.',
    t4bh='Hedges',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'A hedge says the writer thinks something possible, not that it is '
         'true. A statement making the claim outright is usually NOT GIVEN: '
         'the writer has neither agreed nor disagreed.',
    t4bn='Not NO. The writer has not denied it, only stopped short of '
         'promising it.',
    t4ch='Evaluation words',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. One word gives you the writer&rsquo;s attitude, and '
         'statements test it: <em>surprisingly</em> agrees with '
         '<em>unexpected</em>.',
    t4cn='The word judges one thing. Approving of a decision says nothing '
         'about the reason for it.',

    mcaEyebrow='Activity 1 · Whose view is it?',
    mcaTitle='Reported, or the writer&rsquo;s own?',
    mcbEyebrow='Activity 2 · The concession and the turn',
    mcbTitle='What is conceded, and what is claimed?',
    mccEyebrow='Activity 3 · How strongly?',
    mccTitle='How far does the writer commit?',

    r1why='The first sentence only reports the supporters. The second makes '
          'their view the writer&rsquo;s own: <em>they are right</em>. YES.',
    r2why='The critics&rsquo; view is in the passage, and the writer rejects '
          'it: <em>They are wrong</em>. Twenty thousand passengers a day is '
          'the writer&rsquo;s reason. NO.',
    r3why='The claim about crime is only reported (<em>it is often '
          'claimed</em>), and the writer sets it aside: <em>whatever the truth '
          'of that</em>. The writer&rsquo;s own view is about how pleasant the '
          'streets are. NOT GIVEN.',
    r4why='One word decides it. <em>Mistakenly</em> is the writer judging the '
          'parents&rsquo; assumption, so the writer holds the opposite: '
          'bilingual children do not fall behind. YES.',
    r5why='The writer concedes the cost and the delay, then turns: <em>Even '
          'so, I would build it again tomorrow</em>. The turn is the '
          'writer&rsquo;s verdict, and it is not &ldquo;a mistake&rdquo;. NO.',
    r6why='The writer concedes longer journeys and praises punctuality. '
          'Passenger numbers never come up: that reliable buses attract more '
          'people is your inference, not the writer&rsquo;s claim. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> means exams do '
          'have a place &mdash; the writer concedes it and names it: comparing '
          'students from different schools. A concession is the writer&rsquo;s '
          'own view. YES.',
    r8why='The writer is against it for beginners, but concedes the benefits '
          'outright: <em>obvious benefits, and I do not dispute them</em>. A '
          'concession is on the record too, so contradicting it is NO.',
    r9why='The writer hedges about the ban (<em>may have</em>) and mentions '
          '<em>other changes</em>, but never says which did more. Comparing '
          'them is your step, not the writer&rsquo;s. NOT GIVEN &mdash; not '
          'NO.',
    r10why='<em>Surprisingly</em> is the writer&rsquo;s reaction to the '
           'result, and <em>unexpectedly</em> is the same reaction in another '
           'word. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: three limits on the success, and any one of them rules '
           'out <em>everything</em>. NO.',
    r12why='The writer approves of the closure and criticises the '
           'announcement. Why the bridge was closed, the passage never says: '
           'safety is a likely reason, not the writer&rsquo;s claim. NOT GIVEN.',

    sortEyebrow='Activity 4 · On the record?',
    sortTitle='Sort the six openings',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='The writer’s own view',
    sortBin2='A view the writer only reports',
    sortWhy='Three of these put the writer on record. <em>I think</em> says '
            'so outright; <em>rightly</em> takes over a view the writer is '
            'reporting; <em>admittedly</em> grants a point the writer '
            'accepts. The other three name someone else&rsquo;s view and '
            'leave it there &mdash; until the writer judges it, a statement '
            'built on it is NOT GIVEN.',

    actTitle='Put the writer on record',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with an opinion piece to hand &mdash; a '
                  'newspaper column or a review will do. Each of you writes '
                  'four statements about it: one YES, one NO and two NOT '
                  'GIVEN, one of them built on a view the writer only '
                  'reports. Swap and answer. Defend each YES or NO with the '
                  'sentence in which the writer speaks; for a NOT GIVEN, '
                  'show that there is none.',
    actSpeak1='Before a YES or a NO counts, say whose voice the deciding '
              'sentence is in.',
    actSpeak2='Find the writer&rsquo;s concession, if there is one, and write '
              'one statement it makes YES and one it makes NO.',
    actSpeak3='Take a hedged sentence and say what the writer would have had '
              'to write for your statement to be YES.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write a short opinion paragraph, about a hundred words, on '
                  'a question you care about. Give it a reported view, a '
                  'concession and a turn. Then write three statements about it '
                  '&mdash; one YES, one NO, one NOT GIVEN &mdash; and the key, '
                  'quoting the words that decide each one.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
    **dict(VERDICTS)
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='Dieselbe Dreifachauswahl wie bei True, False, Not Given '
             '&mdash; gefragt wird, was der Autor denkt, nicht was der Text '
             'sagt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    optYes='Yes &mdash; der Autor stimmt dieser Aussage zu',
    optNo='No &mdash; der Autor widerspricht dieser Aussage',
    optNG='Not Given &mdash; der Autor sagt dazu nichts',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Dieselbe Dreifachauswahl, eine andere Frage',
    t1ah='Meinungen, nicht Fakten',
    t1ab='True / False / Not Given fragt, was der Text <em>sagt</em>. Yes / '
         'No / Not Given fragt, was der Autor <em>denkt</em>. Die '
         'Aufgabenstellung verrät es: <em>Do the following statements agree '
         'with the views of the writer?</em>',
    t1an='Manchmal steht dort <em>claims</em> statt <em>views</em>. Die '
         'Methode bleibt dieselbe.',
    t1bh='Wo dieser Fragetyp vorkommt',
    t1bb='In Texten, die argumentieren: Kommentare, Rezensionen, Essays mit '
         'einer These. Am häufigsten triffst du ihn im letzten Teil, der am '
         'ehesten argumentiert.',
    t1bn='Schreib das Wort, das die Aufgabe verlangt. YES bei einer True / '
         'False / Not Given-Frage wird als falsch gewertet, auch wenn du TRUE '
         'gemeint hast.',
    t1ch='Dieselbe Prüfung wie bei True / False / Not Given',
    t1cb='<strong>Kann ich auf den Satz zeigen?</strong> Nur muss es jetzt '
         'ein Satz sein, in dem der Autor selbst spricht. Findest du nur die '
         'Meinung eines anderen, hast du die Antwort noch nicht gefunden.',
    t1cn='YES und NO brauchen die Stimme des Autors. NOT GIVEN ist sein '
         'Schweigen.',

    t2Eyebrow='Bevor du beginnst',
    t2Title='Wessen Stimme ist das?',
    t2ah='Meinungen, die der Autor wiedergibt',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. Die Meinung steht im Text, '
         'aber der Autor hat sie nicht unterschrieben. Für sich allein ergibt '
         'sie nur NOT GIVEN.',
    t2an='Diese Sätze nennen die Behauptung vollständig, also findet man sie '
         'beim Wortabgleich zuerst. Genau das macht sie zu Fallen.',
    t2bh='Die eigene Stimme des Autors',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'und viel öfter gar kein Signal. In einem argumentierenden Text '
         'gehört ein schlichter Satz ohne fremden Namen dem Autor.',
    t2bn='Die meisten Signalwörter zeigen auf die Ansichten anderer; die '
         'meisten eigenen Ansichten des Autors tragen keines.',
    t2ch='Wiedergegeben, dann bewertet',
    t2cb='<em>Supporters say it works. They are right.</em> Mit dem zweiten '
         'Satz macht der Autor sich die Meinung zu eigen. <em>They are '
         'wrong</em> hieße: Er vertritt das Gegenteil.',
    t2cn='Ein Wort genügt: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Bevor du beginnst',
    t3Title='Admittedly &hellip; but',
    t3ah='Das Zugeständnis',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (das räumt das Gegenteil dessen ein, '
         'was folgt). Der Autor gesteht der Gegenseite einen Punkt zu '
         '&mdash; und es spricht immer noch der Autor. Ein zugestandener '
         'Punkt ist ein Punkt, den der Autor akzeptiert.',
    t3an='Widerspricht eine Aussage dem Zugeständnis, heißt die Antwort NO '
         '&mdash; auch wenn sie nach der Seite des Autors klingt.',
    t3bh='Die Wende',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. Was '
         'danach kommt, ist die Hauptaussage des Autors. Sie wiegt schwerer '
         'als das Zugeständnis, hebt es aber nicht auf.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> Der Autor vertritt beides.',
    t3ch='Was keine der beiden Hälften sagt',
    t3cb='Die Wende lädt dazu ein, das Argument für den Autor zu Ende zu '
         'führen. Tu es nicht. Eine Aussage, die weiter geht als beide Hälften '
         '&mdash; darüber, was danach geschah, oder was unterm Strich '
         'herauskommt &mdash; ist NOT GIVEN.',
    t3cn='<em>Cheaper to run</em> ist nicht <em>cheaper overall</em>. Nur '
         'eines davon steht im Text.',

    t4Eyebrow='Bevor du beginnst',
    t4Title='Wie entschieden meint der Autor es?',
    t4ah='Grad',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. Der Autor behauptet einen Teil. Eine Aussage, die das '
         'Ganze behauptet &mdash; <em>completely</em>, <em>in every way</em>, '
         '<em>everything</em> &mdash; ist NO.',
    t4an='Dieselbe Regel wie <em>most</em> gegen <em>all</em> bei True / '
         'False / Not Given.',
    t4bh='Abschwächungen',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Eine Abschwächung sagt, dass der Autor etwas für möglich hält, '
         'nicht, dass es stimmt. Eine Aussage, die die Behauptung ohne '
         'Einschränkung macht, ist meist NOT GIVEN: Der Autor hat weder '
         'zugestimmt noch widersprochen.',
    t4bn='Nicht NO. Der Autor hat es nicht bestritten, nur nicht versprochen.',
    t4ch='Wertende Wörter',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Ein Wort zeigt die Haltung des Autors, und Aussagen '
         'prüfen genau die: <em>surprisingly</em> passt zu '
         '<em>unexpected</em>.',
    t4cn='Das Wort bewertet eine Sache. Wer eine Entscheidung gutheißt, sagt '
         'damit nichts über ihren Grund.',

    mcaEyebrow='Aktivität 1 · Wessen Meinung ist das?',
    mcaTitle='Nur wiedergegeben, oder die des Autors?',
    mcbEyebrow='Aktivität 2 · Zugeständnis und Wende',
    mcbTitle='Was wird eingeräumt, was wird behauptet?',
    mccEyebrow='Aktivität 3 · Wie entschieden?',
    mccTitle='Wie weit legt sich der Autor fest?',

    r1why='Der erste Satz gibt die Befürworter nur wieder. Mit dem zweiten '
          'macht der Autor sich ihre Meinung zu eigen: <em>they are '
          'right</em>. YES.',
    r2why='Die Meinung der Kritiker steht im Text, und der Autor weist sie '
          'zurück: <em>They are wrong</em>. Zwanzigtausend Fahrgäste am Tag '
          'sind seine Begründung. NO.',
    r3why='Die Behauptung über Kriminalität wird nur wiedergegeben (<em>it is '
          'often claimed</em>), und der Autor lässt sie offen: <em>whatever '
          'the truth of that</em>. Seine eigene Ansicht betrifft, wie angenehm '
          'die Straßen sind. NOT GIVEN.',
    r4why='Ein Wort entscheidet. Mit <em>mistakenly</em> bewertet der Autor '
          'die Annahme der Eltern, also vertritt er das Gegenteil: '
          'zweisprachige Kinder fallen nicht zurück. YES.',
    r5why='Der Autor räumt die Kosten und die Verspätung ein, dann kommt die '
          'Wende: <em>Even so, I would build it again tomorrow</em>. Die Wende '
          'ist sein Urteil, und es lautet nicht „ein Fehler“. NO.',
    r6why='Der Autor räumt längere Fahrten ein und lobt die Pünktlichkeit. '
          'Fahrgastzahlen kommen nicht vor: Dass zuverlässige Busse mehr '
          'Menschen anziehen, ist deine Schlussfolgerung, nicht seine '
          'Behauptung. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> heißt: '
          'Prüfungen haben ihren Platz &mdash; der Autor räumt das ein und '
          'nennt ihn: Schüler verschiedener Schulen vergleichen. Ein '
          'Zugeständnis ist die eigene Meinung des Autors. YES.',
    r8why='Für Berufsanfänger ist der Autor dagegen, aber die Vorteile räumt '
          'er ausdrücklich ein: <em>obvious benefits, and I do not dispute '
          'them</em>. Auch ein Zugeständnis ist seine Meinung, also heißt ein '
          'Widerspruch dazu NO.',
    r9why='Der Autor schwächt die Aussage über das Verbot ab (<em>may '
          'have</em>) und erwähnt <em>other changes</em>, sagt aber nie, was '
          'mehr bewirkt hat. Der Vergleich ist dein Schritt, nicht der des '
          'Autors. NOT GIVEN &mdash; nicht NO.',
    r10why='<em>Surprisingly</em> ist die Reaktion des Autors auf das '
           'Ergebnis, und <em>unexpectedly</em> ist dieselbe Reaktion in einem '
           'anderen Wort. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: drei Einschränkungen des Erfolgs, und jede einzelne '
           'schließt <em>everything</em> aus. NO.',
    r12why='Der Autor heißt die Schließung gut und kritisiert die Ankündigung. '
           'Warum die Brücke geschlossen wurde, sagt der Text nie: Sicherheit '
           'ist ein naheliegender Grund, aber nicht die Behauptung des Autors. '
           'NOT GIVEN.',

    sortEyebrow='Aktivität 4 · Eigene Meinung?',
    sortTitle='Sortiere die sechs Satzanfänge',
    sortHint='Zieh jeden in eine Spalte &mdash; oder klicke einen an und dann '
             'die Spalte, in die er soll.',
    sortBin1='Die eigene Meinung des Autors',
    sortBin2='Eine Meinung, die er nur wiedergibt',
    sortWhy='Drei davon legen den Autor fest. <em>I think</em> sagt es '
            'direkt; <em>rightly</em> übernimmt eine Ansicht, über die der '
            'Autor berichtet; <em>admittedly</em> räumt einen Punkt ein, den '
            'der Autor akzeptiert. Die anderen drei nennen die Ansicht eines '
            'anderen und lassen sie stehen &mdash; bis der Autor sie '
            'bewertet, ist eine darauf gebaute Aussage NOT GIVEN.',

    actTitle='Den Autor beim Wort nehmen',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, mit einem Meinungstext zur Hand &mdash; eine '
                  'Zeitungskolumne oder eine Rezension reicht. Jeder '
                  'schreibt vier Aussagen dazu: eine YES, eine NO und zwei '
                  'NOT GIVEN, eine davon aufgebaut auf einer Ansicht, über '
                  'die der Autor nur berichtet. Tauscht und beantwortet sie. '
                  'Verteidigt jedes YES oder NO mit dem Satz, in dem der '
                  'Autor spricht; bei einem NOT GIVEN zeigt ihr, dass es '
                  'keinen gibt.',
    actSpeak1='Bevor ein YES oder ein NO zählt, sag, wessen Stimme im '
              'entscheidenden Satz spricht.',
    actSpeak2='Finde das Zugeständnis des Autors, falls es eins gibt, und '
              'schreib dazu eine Aussage, die YES ergibt, und eine, die NO '
              'ergibt.',
    actSpeak3='Nimm einen abgeschwächten Satz und sag, was der Autor hätte '
              'schreiben müssen, damit deine Aussage YES wäre.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreib einen kurzen Meinungsabsatz von etwa hundert '
                  'Wörtern zu einer Frage, die dir wichtig ist &mdash; mit '
                  'einer wiedergegebenen Meinung, einem Zugeständnis und einer '
                  'Wende. Dann schreib drei Aussagen dazu &mdash; eine YES, '
                  'eine NO, eine NOT GIVEN &mdash; und den Lösungsschlüssel, '
                  'mit den Wörtern, die jeweils entscheiden.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='La misma elección entre tres que en True, False, Not Given '
             '&mdash; pero sobre lo que piensa el autor, no sobre lo que '
             'dice el texto',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    optYes='Yes &mdash; el autor está de acuerdo',
    optNo='No &mdash; el autor no está de acuerdo',
    optNG='Not Given &mdash; el autor no lo dice',

    t1Eyebrow='Antes de empezar',
    t1Title='La misma elección entre tres, otra pregunta',
    t1ah='Opiniones, no hechos',
    t1ab='True / False / Not Given pregunta qué <em>dice</em> el texto. Yes / '
         'No / Not Given pregunta qué <em>piensa</em> el autor. El enunciado '
         'lo delata: <em>Do the following statements agree with the views of '
         'the writer?</em>',
    t1an='A veces pone <em>claims</em> en lugar de <em>views</em>. El método '
         'es el mismo.',
    t1bh='Dónde aparece',
    t1bb='En textos que argumentan: columnas de opinión, reseñas, ensayos con '
         'una tesis. Lo verás sobre todo en la última parte, que es la que más '
         'suele argumentar.',
    t1bn='Escribe la palabra que pide el enunciado. Un YES en una pregunta de '
         'True / False / Not Given se da por mal, aunque quisieras decir TRUE.',
    t1ch='La misma comprobación que en True / False / Not Given',
    t1cb='<strong>¿Puedo señalar la frase?</strong> Solo que ahora tiene que '
         'ser una frase en la que hable el autor. Si la única línea que '
         'encuentras es la opinión de otro, todavía no has encontrado la '
         'respuesta.',
    t1cn='YES y NO necesitan la voz del autor. NOT GIVEN es su silencio.',

    t2Eyebrow='Antes de empezar',
    t2Title='¿De quién es esa voz?',
    t2ah='Opiniones que el autor recoge',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. La opinión está en el texto, '
         'pero el autor no la ha firmado. Por sí sola, solo puede darte NOT '
         'GIVEN.',
    t2an='Estas frases enuncian la afirmación completa, así que el '
         'emparejamiento de palabras las encuentra primero. Precisamente eso '
         'las convierte en trampas.',
    t2bh='La voz del propio autor',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'y, mucho más a menudo, ninguna marca. En un texto que argumenta, una '
         'afirmación sin el nombre de nadie más es del autor.',
    t2bn='La mayoría de las marcas señalan opiniones ajenas; la mayoría de '
         'las opiniones propias del autor no llevan ninguna.',
    t2ch='Recogida, y luego juzgada',
    t2cb='<em>Supporters say it works. They are right.</em> Con la segunda '
         'frase el autor hace suya la opinión. <em>They are wrong</em> diría '
         'que defiende lo contrario.',
    t2cn='Basta una palabra: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Antes de empezar',
    t3Title='Admittedly &hellip; but',
    t3ah='La concesión',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (que concede lo contrario de lo que '
         'sigue). El autor concede un punto al otro lado &mdash; y sigue '
         'hablando el autor. Un punto concedido es un punto que el autor '
         'acepta.',
    t3an='Si una afirmación contradice la concesión, la respuesta es NO, '
         'aunque suene a la postura del autor.',
    t3bh='El giro',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. Lo que '
         'viene después es la tesis del autor. Pesa más que la concesión, pero '
         'no la anula.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> El autor sostiene las dos cosas.',
    t3ch='Lo que no dice ninguna mitad',
    t3cb='El giro te invita a terminar el argumento por el autor. No lo '
         'hagas. Una afirmación que va más allá de las dos mitades &mdash; '
         'sobre lo que pasó después, o sobre el balance final &mdash; es NOT '
         'GIVEN.',
    t3cn='<em>Cheaper to run</em> no es <em>cheaper overall</em>. Solo una de '
         'las dos está en el texto.',

    t4Eyebrow='Antes de empezar',
    t4Title='¿Con qué fuerza lo dice el autor?',
    t4ah='Grado',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. El autor afirma una parte. Una afirmación que lo abarca '
         'todo &mdash; <em>completely</em>, <em>in every way</em>, '
         '<em>everything</em> &mdash; es NO.',
    t4an='La misma regla que <em>most</em> frente a <em>all</em> en True / '
         'False / Not Given.',
    t4bh='Matizadores',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Un matiz dice que el autor cree algo posible, no que sea cierto. '
         'Una afirmación que lo dice sin reservas suele ser NOT GIVEN: el '
         'autor ni está de acuerdo ni en desacuerdo.',
    t4bn='No es NO. El autor no lo ha negado; solo se ha quedado sin '
         'prometerlo.',
    t4ch='Palabras que valoran',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Una palabra te da la actitud del autor, y las '
         'afirmaciones la ponen a prueba: <em>surprisingly</em> coincide con '
         '<em>unexpected</em>.',
    t4cn='La palabra juzga una cosa. Aprobar una decisión no dice nada de su '
         'motivo.',

    mcaEyebrow='Actividad 1 · ¿De quién es la opinión?',
    mcaTitle='¿Solo recogida, o del propio autor?',
    mcbEyebrow='Actividad 2 · La concesión y el giro',
    mcbTitle='¿Qué se concede y qué se afirma?',
    mccEyebrow='Actividad 3 · ¿Con qué fuerza?',
    mccTitle='¿Hasta dónde se compromete el autor?',

    r1why='La primera frase solo recoge a los partidarios. Con la segunda el '
          'autor hace suya su opinión: <em>they are right</em>. YES.',
    r2why='La opinión de los críticos está en el texto, y el autor la '
          'rechaza: <em>They are wrong</em>. Los veinte mil pasajeros al día '
          'son su razón. NO.',
    r3why='Lo de la delincuencia solo se recoge (<em>it is often claimed</em>), y el '
          'autor lo deja de lado: <em>whatever the truth of that</em>. Su '
          'propia opinión trata de lo agradables que son las calles. NOT GIVEN.',
    r4why='Lo decide una palabra. Con <em>mistakenly</em> el autor juzga lo '
          'que suponen los padres, así que sostiene lo contrario: los niños '
          'bilingües no se quedan atrás. YES.',
    r5why='El autor concede el coste y el retraso, y luego gira: <em>Even so, '
          'I would build it again tomorrow</em>. El giro es su veredicto, y no '
          'es «un error». NO.',
    r6why='El autor concede trayectos más largos y elogia la puntualidad. El '
          'número de pasajeros no aparece: que unos autobuses fiables atraigan '
          'a más gente es tu deducción, no lo que afirma el autor. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> quiere decir '
          'que los exámenes sí tienen su sitio: el autor lo concede y dice '
          'cuál es, comparar a alumnos de colegios distintos. Una concesión es '
          'opinión del propio autor. YES.',
    r8why='El autor está en contra para quien empieza, pero concede las '
          'ventajas sin rodeos: <em>obvious benefits, and I do not dispute '
          'them</em>. La concesión también es suya, así que contradecirla es '
          'NO.',
    r9why='El autor matiza lo de la prohibición (<em>may have</em>) y '
          'menciona <em>other changes</em>, pero nunca dice qué influyó más. '
          'Compararlos es un paso tuyo, no del autor. NOT GIVEN &mdash; no '
          'NO.',
    r10why='<em>Surprisingly</em> es la reacción del autor al resultado, y '
           '<em>unexpectedly</em> es la misma reacción con otra palabra. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: tres límites al éxito, y cualquiera de ellos descarta '
           '<em>everything</em>. NO.',
    r12why='El autor aprueba el cierre y critica el anuncio. Por qué se cerró '
           'el puente, el texto no lo dice nunca: la seguridad es un motivo '
           'probable, no lo que afirma el autor. NOT GIVEN.',

    sortEyebrow='Actividad 4 · ¿Suya, o solo recogida?',
    sortTitle='Clasifica los seis comienzos',
    sortHint='Arrastra cada uno a una columna &mdash; o haz clic en uno y '
             'luego en la columna que quieras.',
    sortBin1='La opinión del propio autor',
    sortBin2='Una opinión que solo recoge',
    sortWhy='Tres de ellas comprometen al autor. <em>I think</em> lo dice '
            'abiertamente; <em>rightly</em> hace suya una opinión que el '
            'autor está contando; <em>admittedly</em> concede un punto que '
            'el autor acepta. Las otras tres nombran la opinión de otro y la '
            'dejan ahí &mdash; hasta que el autor la juzga, una afirmación '
            'basada en ella es NOT GIVEN.',

    actTitle='Que el autor se moje',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con un artículo de opinión a mano; una '
                  'columna o una reseña sirven. Cada uno escribe cuatro '
                  'afirmaciones sobre él: una YES, una NO y dos NOT GIVEN, '
                  'una de ellas basada en una opinión que el autor solo '
                  'cuenta. Intercambiad y responded. Defended cada YES o NO '
                  'con la frase en la que habla el autor; para un NOT GIVEN, '
                  'mostrad que no la hay.',
    actSpeak1='Antes de que cuente un YES o un NO, di de quién es la voz de la '
              'frase que lo decide.',
    actSpeak2='Busca la concesión del autor, si la hay, y escribe una '
              'afirmación que dé YES y otra que dé NO.',
    actSpeak3='Coge una frase con matiz y di qué habría tenido que escribir el '
              'autor para que tu afirmación fuera YES.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe un párrafo de opinión breve, de unas cien palabras, '
                  'sobre una cuestión que te importe, con una opinión '
                  'recogida, una concesión y un giro. Luego escribe tres '
                  'afirmaciones sobre él &mdash; una YES, una NO y una NOT '
                  'GIVEN &mdash; y la clave, citando las palabras que deciden '
                  'cada una.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='Le même choix entre trois réponses que True, False, Not Given '
             '&mdash; mais sur ce que pense l’auteur, pas sur ce que dit le '
             'texte',
    chipLevel='C1 · Avancé', chipFocus='Reading · les deux modules',
    chipCount='18 points',

    optYes='Yes &mdash; l’auteur est d’accord',
    optNo='No &mdash; l’auteur n’est pas d’accord',
    optNG='Not Given &mdash; l’auteur ne le dit pas',

    t1Eyebrow='Avant de commencer',
    t1Title='Le même choix entre trois, une autre question',
    t1ah='Des opinions, pas des faits',
    t1ab='True / False / Not Given demande ce que le texte <em>dit</em>. '
         'Yes / No / Not Given demande ce que l’auteur <em>pense</em>. La '
         'consigne le trahit : <em>Do the following statements agree with '
         'the views of the writer?</em>',
    t1an='Parfois la consigne dit <em>claims</em> au lieu de <em>views</em>. '
         'La méthode est la même.',
    t1bh='Où on le rencontre',
    t1bb='Dans les textes qui argumentent : tribunes, critiques, essais qui '
         'défendent une thèse. Vous le verrez surtout dans la dernière partie, '
         'celle qui argumente le plus volontiers.',
    t1bn='Écrivez le mot que demande la consigne. Un YES à une question True / '
         'False / Not Given est compté faux, même si vous vouliez dire TRUE.',
    t1ch='La même vérification que pour True / False / Not Given',
    t1cb='<strong>Puis-je montrer la phrase du doigt ?</strong> Seulement, il '
         'faut désormais que ce soit une phrase où l’auteur parle lui-même. Si '
         'la seule ligne que vous trouvez est l’opinion de quelqu’un d’autre, '
         'vous n’avez pas encore trouvé la réponse.',
    t1cn='YES et NO ont besoin de la voix de l’auteur. NOT GIVEN, c’est son '
         'silence.',

    t2Eyebrow='Avant de commencer',
    t2Title='À qui est cette voix ?',
    t2ah='Les opinions que l’auteur rapporte',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. L’opinion est dans le texte, '
         'mais l’auteur ne l’a pas signée. À elle seule, elle ne peut donner '
         'que NOT GIVEN.',
    t2an='Ces phrases énoncent l’affirmation en entier, donc le repérage de '
         'mots les trouve en premier. C’est exactement ce qui en fait des '
         'pièges.',
    t2bh='La voix de l’auteur',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'et, bien plus souvent, aucune marque. Dans un texte qui argumente, '
         'une affirmation simple, sans le nom de personne d’autre, appartient à '
         'l’auteur.',
    t2bn='La plupart des marqueurs signalent l’avis des autres ; la plupart '
         'des avis de l’auteur n’en portent aucun.',
    t2ch='Rapportée, puis jugée',
    t2cb='<em>Supporters say it works. They are right.</em> Avec la deuxième '
         'phrase, l’auteur fait sienne l’opinion. <em>They are wrong</em> '
         'voudrait dire qu’il défend le contraire.',
    t2cn='Un seul mot suffit : <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Avant de commencer',
    t3Title='Admittedly &hellip; but',
    t3ah='La concession',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (qui concède le contraire de ce qui '
         'suit). L’auteur accorde un point à l’autre camp &mdash; et c’est '
         'toujours l’auteur qui parle. Un point concédé est un point que '
         'l’auteur accepte.',
    t3an='Si une affirmation contredit la concession, la réponse est NO, même '
         'quand elle semble aller dans le sens de l’auteur.',
    t3bh='Le tournant',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. Ce qui '
         'suit est la thèse principale de l’auteur. Elle l’emporte sur la '
         'concession, sans l’annuler.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> L’auteur soutient les deux.',
    t3ch='Ce qu’aucune des deux moitiés ne dit',
    t3cb='Le tournant vous invite à finir le raisonnement à la place de '
         'l’auteur. Ne le faites pas. Une affirmation qui va plus loin que les '
         'deux moitiés &mdash; sur ce qui s’est passé ensuite, ou sur le bilan '
         'd’ensemble &mdash; est NOT GIVEN.',
    t3cn='<em>Cheaper to run</em> n’est pas <em>cheaper overall</em>. Un seul '
         'des deux figure dans le texte.',

    t4Eyebrow='Avant de commencer',
    t4Title='Avec quelle force l’auteur l’affirme-t-il ?',
    t4ah='Le degré',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. L’auteur affirme une partie. Une affirmation qui prétend '
         'au tout &mdash; <em>completely</em>, <em>in every way</em>, '
         '<em>everything</em> &mdash; est NO.',
    t4an='La même règle que <em>most</em> contre <em>all</em> dans un True / '
         'False / Not Given.',
    t4bh='Les atténuations',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Une atténuation dit que l’auteur juge une chose possible, pas '
         'qu’elle est vraie. Une affirmation qui la pose sans réserve est en '
         'général NOT GIVEN : l’auteur n’a ni approuvé ni contredit.',
    t4bn='Pas NO. L’auteur ne l’a pas nié ; il s’est seulement abstenu de le '
         'promettre.',
    t4ch='Les mots qui jugent',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Un seul mot donne l’attitude de l’auteur, et les '
         'affirmations la mettent à l’épreuve : <em>surprisingly</em> va avec '
         '<em>unexpected</em>.',
    t4cn='Le mot juge une seule chose. Approuver une décision ne dit rien de '
         'sa raison.',

    mcaEyebrow='Activité 1 · À qui est cette opinion ?',
    mcaTitle='Rapportée, ou celle de l’auteur ?',
    mcbEyebrow='Activité 2 · La concession et le tournant',
    mcbTitle='Qu’est-ce qui est concédé, qu’est-ce qui est affirmé ?',
    mccEyebrow='Activité 3 · Avec quelle force ?',
    mccTitle='Jusqu’où l’auteur s’engage-t-il ?',

    r1why='La première phrase ne fait que rapporter les partisans. Avec la '
          'deuxième, l’auteur fait sienne leur opinion : <em>they are '
          'right</em>. YES.',
    r2why='L’opinion des critiques est dans le texte, et l’auteur la rejette : '
          '<em>They are wrong</em>. Vingt mille passagers par jour, voilà sa '
          'raison. NO.',
    r3why='L’affirmation sur la criminalité est seulement rapportée (<em>it is '
          'often claimed</em>), et l’auteur la met de côté : <em>whatever the '
          'truth of that</em>. Son opinion à lui porte sur l’agrément des rues. '
          'NOT GIVEN.',
    r4why='Un seul mot décide. Avec <em>mistakenly</em>, l’auteur juge ce que '
          'supposent les parents ; il pense donc le contraire : les enfants '
          'bilingues ne prennent pas de retard. YES.',
    r5why='L’auteur concède le coût et le retard, puis vient le tournant : '
          '<em>Even so, I would build it again tomorrow</em>. Le tournant est '
          'son verdict, et ce n’est pas « une erreur ». NO.',
    r6why='L’auteur concède des trajets plus longs et salue la ponctualité. Le '
          'nombre de passagers n’apparaît nulle part : que des bus fiables '
          'attirent plus de monde, c’est votre déduction, pas son affirmation. '
          'NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> signifie que '
          'les examens ont bien leur place : l’auteur le concède et précise '
          'laquelle, comparer des élèves d’écoles différentes. Une concession '
          'est l’opinion de l’auteur lui-même. YES.',
    r8why='L’auteur est contre pour les débutants, mais il concède franchement '
          'les avantages : <em>obvious benefits, and I do not dispute '
          'them</em>. La concession fait aussi partie de ses opinions ; la '
          'contredire, c’est NO.',
    r9why='L’auteur atténue à propos de l’interdiction (<em>may have</em>) '
          'et mentionne <em>other changes</em>, mais ne dit jamais ce qui a '
          'le plus compté. La comparaison est votre étape, pas celle de '
          'l’auteur. NOT GIVEN &mdash; pas NO.',
    r10why='<em>Surprisingly</em> est la réaction de l’auteur au résultat, et '
           '<em>unexpectedly</em> est la même réaction en un autre mot. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em> : trois limites au succès, et chacune suffit à exclure '
           '<em>everything</em>. NO.',
    r12why='L’auteur approuve la fermeture et critique l’annonce. Pourquoi le '
           'pont a été fermé, le texte ne le dit jamais : la sécurité est une '
           'raison probable, pas une affirmation de l’auteur. NOT GIVEN.',

    sortEyebrow='Activité 4 · Son opinion à lui ?',
    sortTitle='Classez les six débuts de phrase',
    sortHint='Faites glisser chacun dans une colonne &mdash; ou cliquez sur '
             'l’un d’eux, puis sur la colonne voulue.',
    sortBin1='L’opinion de l’auteur',
    sortBin2='Une opinion qu’il ne fait que rapporter',
    sortWhy='Trois de ces phrases engagent l’auteur. <em>I think</em> le dit '
            'ouvertement ; <em>rightly</em> reprend à son compte un avis que '
            'l’auteur rapporte ; <em>admittedly</em> concède un point que '
            'l’auteur accepte. Les trois autres nomment l’avis de quelqu’un '
            'd’autre et en restent là &mdash; tant que l’auteur ne le juge '
            'pas, une affirmation fondée dessus est NOT GIVEN.',

    actTitle='Prendre l’auteur au mot',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux, avec un texte d’opinion sous la main &mdash; une '
                  'chronique ou une critique suffit. Chacun écrit quatre '
                  'affirmations à son sujet : une YES, une NO et deux NOT '
                  'GIVEN, dont une fondée sur un avis que l’auteur ne fait '
                  'que rapporter. Échangez et répondez. Défendez chaque YES '
                  'ou NO avec la phrase où l’auteur parle ; pour un NOT '
                  'GIVEN, montrez qu’il n’y en a pas.',
    actSpeak1='Avant qu’un YES ou un NO compte, dites à qui appartient la voix '
              'de la phrase décisive.',
    actSpeak2='Trouvez la concession de l’auteur, s’il y en a une, et écrivez '
              'une affirmation qu’elle rend YES et une qu’elle rend NO.',
    actSpeak3='Prenez une phrase atténuée et dites ce que l’auteur aurait dû '
              'écrire pour que votre affirmation soit YES.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Écrivez un court paragraphe d’opinion, d’une centaine de '
                  'mots, sur une question qui vous tient à cœur, avec une '
                  'opinion rapportée, une concession et un tournant. Puis '
                  'écrivez trois affirmations à son sujet &mdash; une YES, une '
                  'NO, une NOT GIVEN &mdash; et le corrigé, en citant les mots '
                  'qui décident chacune.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='La stessa scelta fra tre risposte di True, False, Not Given '
             '&mdash; ma su ciò che pensa l’autore, non su ciò che dice il '
             'testo',
    chipLevel='C1 · Avanzato', chipFocus='Reading · entrambi i moduli',
    chipCount='18 punti',

    optYes='Yes &mdash; l’autore la pensa così',
    optNo='No &mdash; l’autore la pensa diversamente',
    optNG='Not Given &mdash; l’autore non lo dice',

    t1Eyebrow='Prima di cominciare',
    t1Title='La stessa scelta fra tre, un’altra domanda',
    t1ah='Opinioni, non fatti',
    t1ab='True / False / Not Given chiede che cosa <em>dice</em> il testo. '
         'Yes / No / Not Given chiede che cosa <em>pensa</em> l’autore. La '
         'consegna lo tradisce: <em>Do the following statements agree with '
         'the views of the writer?</em>',
    t1an='A volte la consegna dice <em>claims</em> invece di <em>views</em>. '
         'Il metodo è lo stesso.',
    t1bh='Dove lo trovi',
    t1bb='Nei testi che argomentano: editoriali, recensioni, saggi con una '
         'tesi. Lo incontrerai soprattutto nell’ultima sezione, quella che '
         'argomenta più volentieri.',
    t1bn='Scrivi la parola che chiede la consegna. Un YES a una domanda True / '
         'False / Not Given è considerato sbagliato, anche se intendevi TRUE.',
    t1ch='La stessa verifica di True / False / Not Given',
    t1cb='<strong>Posso indicare la frase?</strong> Solo che ora deve essere '
         'una frase in cui parla l’autore. Se l’unica riga che trovi è '
         'l’opinione di qualcun altro, non hai ancora trovato la risposta.',
    t1cn='YES e NO hanno bisogno della voce dell’autore. NOT GIVEN è il suo '
         'silenzio.',

    t2Eyebrow='Prima di cominciare',
    t2Title='Di chi è questa voce?',
    t2ah='Le opinioni che l’autore riporta',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. L’opinione è nel testo, ma '
         'l’autore non l’ha firmata. Da sola può dare soltanto NOT GIVEN.',
    t2an='Queste frasi enunciano l’affermazione per intero, quindi chi cerca '
         'le parole le trova per prime. È proprio questo a farne delle '
         'trappole.',
    t2bh='La voce dell’autore',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'e, molto più spesso, nessun segnale. In un testo che argomenta, '
         'un’affermazione semplice senza il nome di nessun altro è '
         'dell’autore.',
    t2bn='La maggior parte dei segnali indica le opinioni altrui; la maggior '
         'parte delle opinioni dell’autore non ne ha nessuno.',
    t2ch='Riportata, poi giudicata',
    t2cb='<em>Supporters say it works. They are right.</em> Con la seconda '
         'frase l’autore fa propria l’opinione. <em>They are wrong</em> '
         'vorrebbe dire che sostiene il contrario.',
    t2cn='Basta una parola: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Prima di cominciare',
    t3Title='Admittedly &hellip; but',
    t3ah='La concessione',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (che concede il contrario di ciò che '
         'segue). L’autore concede un punto all’altra parte &mdash; ed è '
         'sempre l’autore a parlare. Un punto concesso è un punto che '
         'l’autore accetta.',
    t3an='Se un’affermazione contraddice la concessione, la risposta è NO, '
         'anche quando sembra stare dalla parte dell’autore.',
    t3bh='La svolta',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. Quello '
         'che segue è la tesi principale dell’autore. Pesa più della '
         'concessione, ma non la cancella.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> L’autore sostiene entrambe le cose.',
    t3ch='Ciò che nessuna delle due metà dice',
    t3cb='La svolta ti invita a completare il ragionamento al posto '
         'dell’autore. Non farlo. Un’affermazione che va oltre le due metà '
         '&mdash; su ciò che è successo dopo, o sul bilancio complessivo '
         '&mdash; è NOT GIVEN.',
    t3cn='<em>Cheaper to run</em> non è <em>cheaper overall</em>. Solo uno dei '
         'due è nel testo.',

    t4Eyebrow='Prima di cominciare',
    t4Title='Con quanta forza lo afferma l’autore?',
    t4ah='Il grado',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. L’autore afferma una parte. Un’affermazione che pretende '
         'il tutto &mdash; <em>completely</em>, <em>in every way</em>, '
         '<em>everything</em> &mdash; è NO.',
    t4an='La stessa regola di <em>most</em> contro <em>all</em> in un True / '
         'False / Not Given.',
    t4bh='Le attenuazioni',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Un’attenuazione dice che l’autore ritiene una cosa possibile, non '
         'che sia vera. Un’affermazione che la sostiene senza riserve è di '
         'solito NOT GIVEN: l’autore non ha né concordato né dissentito.',
    t4bn='Non NO. L’autore non l’ha negato; si è solo fermato prima di '
         'prometterlo.',
    t4ch='Le parole che giudicano',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Una sola parola ti dà l’atteggiamento dell’autore, e '
         'le affermazioni lo mettono alla prova: <em>surprisingly</em> va '
         'd’accordo con <em>unexpected</em>.',
    t4cn='La parola giudica una sola cosa. Approvare una decisione non dice '
         'nulla sul suo motivo.',

    mcaEyebrow='Attività 1 · Di chi è questa opinione?',
    mcaTitle='Riportata, o dell’autore?',
    mcbEyebrow='Attività 2 · La concessione e la svolta',
    mcbTitle='Che cosa viene concesso, e che cosa affermato?',
    mccEyebrow='Attività 3 · Con quanta forza?',
    mccTitle='Fin dove si impegna l’autore?',

    r1why='La prima frase riporta soltanto i sostenitori. Con la seconda '
          'l’autore fa propria la loro opinione: <em>they are right</em>. YES.',
    r2why='L’opinione dei critici è nel testo, e l’autore la respinge: '
          '<em>They are wrong</em>. Ventimila passeggeri al giorno sono la sua '
          'ragione. NO.',
    r3why='L’affermazione sulla criminalità è solo riportata (<em>it is often '
          'claimed</em>), e l’autore la mette da parte: <em>whatever the truth '
          'of that</em>. La sua opinione riguarda quanto sono piacevoli le '
          'strade. NOT GIVEN.',
    r4why='Decide una sola parola. Con <em>mistakenly</em> l’autore giudica '
          'ciò che pensano i genitori, quindi sostiene il contrario: i bambini '
          'bilingui non restano indietro. YES.',
    r5why='L’autore concede il costo e il ritardo, poi arriva la svolta: '
          '<em>Even so, I would build it again tomorrow</em>. La svolta è il '
          'suo verdetto, e non è «un errore». NO.',
    r6why='L’autore concede tragitti più lunghi e loda la puntualità. Il '
          'numero dei passeggeri non compare mai: che autobus affidabili '
          'attirino più gente è una tua deduzione, non un’affermazione '
          'dell’autore. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> significa che '
          'gli esami un posto ce l’hanno: l’autore lo concede e dice quale, '
          'confrontare studenti di scuole diverse. Una concessione è '
          'un’opinione dell’autore stesso. YES.',
    r8why='L’autore è contrario per chi comincia, ma concede apertamente i '
          'vantaggi: <em>obvious benefits, and I do not dispute them</em>. '
          'Anche la concessione è una sua opinione, quindi contraddirla è NO.',
    r9why='L’autore attenua quanto al divieto (<em>may have</em>) e cita '
          '<em>other changes</em>, ma non dice mai che cosa abbia inciso di '
          'più. Il confronto è un passo tuo, non dell’autore. NOT GIVEN '
          '&mdash; non NO.',
    r10why='<em>Surprisingly</em> è la reazione dell’autore al risultato, e '
           '<em>unexpectedly</em> è la stessa reazione con un’altra parola. '
           'YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: tre limiti al successo, e ciascuno basta a escludere '
           '<em>everything</em>. NO.',
    r12why='L’autore approva la chiusura e critica l’annuncio. Perché il ponte '
           'sia stato chiuso, il testo non lo dice mai: la sicurezza è un '
           'motivo probabile, non un’affermazione dell’autore. NOT GIVEN.',

    sortEyebrow='Attività 4 · Opinione sua?',
    sortTitle='Classifica i sei inizi di frase',
    sortHint='Trascina ciascuno in una colonna &mdash; oppure clicca su uno e '
             'poi sulla colonna che vuoi.',
    sortBin1='L’opinione dell’autore',
    sortBin2='Un’opinione che si limita a riportare',
    sortWhy='Tre di queste impegnano l’autore. <em>I think</em> lo dice '
            'apertamente; <em>rightly</em> fa propria un’opinione che '
            'l’autore riporta; <em>admittedly</em> concede un punto che '
            'l’autore accetta. Le altre tre nominano l’opinione di qualcun '
            'altro e la lasciano lì &mdash; finché l’autore non la giudica, '
            'un’affermazione costruita su di essa è NOT GIVEN.',

    actTitle='Prendere l’autore in parola',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia, con un articolo d’opinione a portata di mano '
                  '&mdash; basta una rubrica o una recensione. Ognuno scrive '
                  'quattro affermazioni: una YES, una NO e due NOT GIVEN, '
                  'una delle quali basata su un’opinione che l’autore si '
                  'limita a riportare. Scambiatevele e rispondete. Difendete '
                  'ogni YES o NO con la frase in cui parla l’autore; per un '
                  'NOT GIVEN, mostrate che non c’è.',
    actSpeak1='Prima che un YES o un NO conti, di’ di chi è la voce nella frase '
              'decisiva.',
    actSpeak2='Trova la concessione dell’autore, se c’è, e scrivi '
              'un’affermazione che con essa risulta YES e una che risulta NO.',
    actSpeak3='Prendi una frase attenuata e di’ che cosa avrebbe dovuto '
              'scrivere l’autore perché la tua affermazione fosse YES.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Scrivi un breve paragrafo d’opinione, di un centinaio di '
                  'parole, su una questione che ti sta a cuore, con '
                  'un’opinione riportata, una concessione e una svolta. Poi '
                  'scrivi tre affermazioni sul paragrafo &mdash; una YES, una '
                  'NO, una NOT GIVEN &mdash; e la chiave, citando le parole che '
                  'decidono ciascuna.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='A mesma escolha entre três respostas de True, False, Not Given '
             '&mdash; mas sobre o que o autor pensa, não sobre o que o texto '
             'diz',
    chipLevel='C1 · Avançado', chipFocus='Reading · os dois módulos',
    chipCount='18 pontos',

    optYes='Yes &mdash; o autor concorda com isto',
    optNo='No &mdash; o autor discorda disto',
    optNG='Not Given &mdash; o autor não diz nada',

    t1Eyebrow='Antes de começar',
    t1Title='A mesma escolha entre três, outra pergunta',
    t1ah='Opiniões, não factos',
    t1ab='True / False / Not Given pergunta o que o texto <em>diz</em>. Yes / '
         'No / Not Given pergunta o que o autor <em>pensa</em>. O enunciado '
         'denuncia-o: <em>Do the following statements agree with the views of '
         'the writer?</em>',
    t1an='Às vezes o enunciado diz <em>claims</em> em vez de <em>views</em>. O '
         'método é o mesmo.',
    t1bh='Onde aparece',
    t1bb='Em textos que argumentam: artigos de opinião, críticas, ensaios com '
         'uma tese. Vais encontrá-lo sobretudo na última parte, a que mais '
         'tende a argumentar.',
    t1bn='Escreve a palavra que o enunciado pede. Um YES numa pergunta True / '
         'False / Not Given conta como errado, mesmo que quisesses dizer TRUE.',
    t1ch='A mesma verificação de True / False / Not Given',
    t1cb='<strong>Consigo apontar para a frase?</strong> Só que agora tem de '
         'ser uma frase em que fala o próprio autor. Se a única linha que '
         'encontras é a opinião de outra pessoa, ainda não encontraste a '
         'resposta.',
    t1cn='YES e NO precisam da voz do autor. NOT GIVEN é o seu silêncio.',

    t2Eyebrow='Antes de começar',
    t2Title='De quem é esta voz?',
    t2ah='As opiniões que o autor relata',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. A opinião está no texto, mas o '
         'autor não a assinou. Sozinha, só pode dar NOT GIVEN.',
    t2an='Estas frases enunciam a afirmação por inteiro, por isso quem '
         'procura palavras encontra-as primeiro. É exatamente isso que as '
         'torna armadilhas.',
    t2bh='A voz do próprio autor',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'e, muito mais vezes, marca nenhuma. Num texto que argumenta, uma '
         'afirmação simples, sem o nome de mais ninguém, é do autor.',
    t2bn='A maioria dos marcadores aponta para as opiniões dos outros; a '
         'maioria das opiniões do próprio autor não traz nenhum.',
    t2ch='Relatada, e depois julgada',
    t2cb='<em>Supporters say it works. They are right.</em> Com a segunda '
         'frase, o autor torna sua a opinião. <em>They are wrong</em> quereria '
         'dizer que defende o contrário.',
    t2cn='Basta uma palavra: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Antes de começar',
    t3Title='Admittedly &hellip; but',
    t3ah='A concessão',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (que concede o contrário do que vem a '
         'seguir). O autor dá razão ao outro lado num ponto &mdash; e '
         'continua a ser o autor a falar. Um ponto concedido é um ponto que '
         'o autor aceita.',
    t3an='Se uma afirmação contradiz a concessão, a resposta é NO, mesmo quando '
         'parece estar do lado do autor.',
    t3bh='A viragem',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. O que '
         'vem a seguir é a tese principal do autor. Pesa mais do que a '
         'concessão, mas não a anula.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> O autor defende as duas coisas.',
    t3ch='O que nenhuma das metades diz',
    t3cb='A viragem convida-te a acabar o raciocínio pelo autor. Não o faças. '
         'Uma afirmação que vai além das duas metades &mdash; sobre o que '
         'aconteceu depois, ou sobre o balanço final &mdash; é NOT GIVEN.',
    t3cn='<em>Cheaper to run</em> não é <em>cheaper overall</em>. Só um dos '
         'dois está no texto.',

    t4Eyebrow='Antes de começar',
    t4Title='Com que força o diz o autor?',
    t4ah='O grau',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. O autor afirma uma parte. Uma afirmação que reclama o '
         'todo &mdash; <em>completely</em>, <em>in every way</em>, '
         '<em>everything</em> &mdash; é NO.',
    t4an='A mesma regra de <em>most</em> contra <em>all</em> num True / False / '
         'Not Given.',
    t4bh='As atenuações',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Uma atenuação diz que o autor acha uma coisa possível, não que '
         'seja verdade. Uma afirmação que a faz sem reservas é normalmente '
         'NOT GIVEN: o autor não concordou nem discordou.',
    t4bn='Não é NO. O autor não o negou; apenas não chegou a prometê-lo.',
    t4ch='As palavras que avaliam',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Uma só palavra dá-te a atitude do autor, e as '
         'afirmações põem-na à prova: <em>surprisingly</em> condiz com '
         '<em>unexpected</em>.',
    t4cn='A palavra avalia uma coisa só. Aprovar uma decisão não diz nada '
         'sobre o seu motivo.',

    mcaEyebrow='Atividade 1 · De quem é esta opinião?',
    mcaTitle='Relatada, ou do próprio autor?',
    mcbEyebrow='Atividade 2 · A concessão e a viragem',
    mcbTitle='O que se concede, e o que se afirma?',
    mccEyebrow='Atividade 3 · Com que força?',
    mccTitle='Até onde se compromete o autor?',

    r1why='A primeira frase apenas relata os defensores. Com a segunda, o '
          'autor torna sua a opinião deles: <em>they are right</em>. YES.',
    r2why='A opinião dos críticos está no texto, e o autor rejeita-a: '
          '<em>They are wrong</em>. Vinte mil passageiros por dia são a sua '
          'razão. NO.',
    r3why='A afirmação sobre a criminalidade é só relatada (<em>it is often '
          'claimed</em>), e o autor põe-na de parte: <em>whatever the truth of '
          'that</em>. A opinião dele é sobre quão agradáveis ficam as ruas. '
          'NOT GIVEN.',
    r4why='Uma só palavra decide. Com <em>mistakenly</em>, o autor julga o que '
          'os pais supõem; logo, defende o contrário: as crianças bilingues '
          'não ficam para trás. YES.',
    r5why='O autor concede o custo e o atraso, e depois vem a viragem: '
          '<em>Even so, I would build it again tomorrow</em>. A viragem é o seu '
          'veredicto, e não é «um erro». NO.',
    r6why='O autor concede viagens mais longas e elogia a pontualidade. O '
          'número de passageiros nunca aparece: que autocarros fiáveis atraiam '
          'mais gente é uma dedução tua, não uma afirmação do autor. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> quer dizer que '
          'os exames têm o seu lugar: o autor concede-o e diz qual, comparar '
          'alunos de escolas diferentes. Uma concessão é opinião do próprio '
          'autor. YES.',
    r8why='O autor é contra para quem está a começar, mas concede as vantagens '
          'sem rodeios: <em>obvious benefits, and I do not dispute them</em>. A '
          'concessão também é opinião dele; contradizê-la é NO.',
    r9why='O autor atenua quanto à proibição (<em>may have</em>) e menciona '
          '<em>other changes</em>, mas nunca diz o que contou mais. '
          'Compará-los é um passo teu, não do autor. NOT GIVEN &mdash; não '
          'NO.',
    r10why='<em>Surprisingly</em> é a reação do autor ao resultado, e '
           '<em>unexpectedly</em> é a mesma reação noutra palavra. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: três limites ao sucesso, e qualquer um deles exclui '
           '<em>everything</em>. NO.',
    r12why='O autor aprova o encerramento e critica o anúncio. Porque é que a '
           'ponte foi fechada, o texto nunca diz: a segurança é um motivo '
           'provável, não uma afirmação do autor. NOT GIVEN.',

    sortEyebrow='Atividade 4 · Opinião do autor?',
    sortTitle='Classifica os seis inícios de frase',
    sortHint='Arrasta cada um para uma coluna &mdash; ou clica num deles e '
             'depois na coluna que quiseres.',
    sortBin1='A opinião do próprio autor',
    sortBin2='Uma opinião que ele só relata',
    sortWhy='Três destas comprometem o autor. <em>I think</em> di-lo '
            'abertamente; <em>rightly</em> assume uma opinião que o autor '
            'está a relatar; <em>admittedly</em> concede um ponto que o '
            'autor aceita. As outras três nomeiam a opinião de outra pessoa '
            'e deixam-na ficar &mdash; até o autor a julgar, uma afirmação '
            'construída sobre ela é NOT GIVEN.',

    actTitle='O autor, preto no branco',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares, com um artigo de opinião à mão &mdash; uma '
                  'crónica ou uma crítica servem. Cada um escreve quatro '
                  'afirmações sobre ele: uma YES, uma NO e duas NOT GIVEN, '
                  'uma delas construída sobre uma opinião que o autor só '
                  'relata. Troquem e respondam. Defendam cada YES ou NO com '
                  'a frase em que o autor fala; para um NOT GIVEN, mostrem '
                  'que não existe.',
    actSpeak1='Antes de um YES ou um NO contar, diz de quem é a voz na frase '
              'decisiva.',
    actSpeak2='Encontra a concessão do autor, se houver, e escreve uma '
              'afirmação que com ela dá YES e outra que dá NO.',
    actSpeak3='Pega numa frase atenuada e diz o que o autor teria de ter '
              'escrito para a tua afirmação ser YES.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Escreve um parágrafo de opinião curto, com cerca de cem '
                  'palavras, sobre uma questão que te importe, com uma opinião '
                  'relatada, uma concessão e uma viragem. Depois escreve três '
                  'afirmações sobre ele &mdash; uma YES, uma NO, uma NOT GIVEN '
                  '&mdash; e a chave, citando as palavras que decidem cada uma.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='Тот же выбор из трёх, что и в True, False, Not Given, &mdash; '
             'но о том, что думает автор, а не о том, что сказано в тексте',
    chipLevel='C1 · Продвинутый', chipFocus='Reading · оба модуля',
    chipCount='18 баллов',

    optYes='Yes &mdash; автор с этим согласен',
    optNo='No &mdash; автор с этим не согласен',
    optNG='Not Given &mdash; автор об этом молчит',

    t1Eyebrow='Прежде чем начать',
    t1Title='Тот же выбор из трёх, другой вопрос',
    t1ah='Мнения, а не факты',
    t1ab='True / False / Not Given спрашивает, что <em>сказано</em> в тексте. '
         'Yes / No / Not Given спрашивает, что <em>думает</em> автор. Задание '
         'само это выдаёт: <em>Do the following statements agree with the '
         'views of the writer?</em>',
    t1an='Иногда в задании стоит <em>claims</em> вместо <em>views</em>. Метод '
         'тот же.',
    t1bh='Где он встречается',
    t1bb='В текстах, где автор спорит: в колонках, рецензиях, эссе с тезисом. '
         'Чаще всего вы увидите его в последней части: она спорит охотнее '
         'остальных.',
    t1bn='Пишите то слово, которого требует задание. YES в вопросе True / '
         'False / Not Given засчитывается как ошибка, даже если вы имели в виду '
         'TRUE.',
    t1ch='Та же проверка, что и в True / False / Not Given',
    t1cb='<strong>Могу ли я указать на предложение?</strong> Только теперь это '
         'должно быть предложение, в котором говорит сам автор. Если '
         'единственная строка, которую вы нашли, &mdash; чужое мнение, ответ '
         'ещё не найден.',
    t1cn='YES и NO требуют голоса автора. NOT GIVEN &mdash; это его молчание.',

    t2Eyebrow='Прежде чем начать',
    t2Title='Чей это голос?',
    t2ah='Мнения, которые автор пересказывает',
    t2ab='<em>Critics argue</em>, <em>it is often claimed</em>, <em>according '
         'to</em>, <em>many people believe</em>. Мнение есть в тексте, но '
         'автор под ним не подписывался. Само по себе оно может дать только '
         'NOT GIVEN.',
    t2an='Эти предложения формулируют утверждение полностью, поэтому поиск '
         'совпадающих слов находит их первыми. Именно это и делает их '
         'ловушками.',
    t2bh='Собственный голос автора',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'а гораздо чаще никаких сигналов. В тексте, где автор спорит, простое '
         'утверждение без чужого имени принадлежит автору.',
    t2bn='Большинство маркеров указывают на чужие мнения; у большинства '
         'собственных мнений автора маркеров нет.',
    t2ch='Пересказано, затем оценено',
    t2cb='<em>Supporters say it works. They are right.</em> Вторым '
         'предложением автор делает это мнение своим. <em>They are wrong</em> '
         'означало бы, что он отстаивает противоположное.',
    t2cn='Хватает одного слова: <em>rightly</em>, <em>wrongly</em>, '
         '<em>mistakenly</em>.',

    t3Eyebrow='Прежде чем начать',
    t3Title='Admittedly &hellip; but',
    t3ah='Уступка',
    t3ab='<em>Admittedly</em>, <em>of course</em>, <em>it is true that</em>, '
         '<em>this is not to say</em> (здесь уступается противоположное '
         'тому, что следует дальше). Автор уступает другой стороне в '
         'каком-то пункте &mdash; и это по-прежнему говорит автор. '
         'Уступленный пункт &mdash; это пункт, с которым автор согласен.',
    t3an='Если утверждение противоречит уступке, ответ NO, даже когда оно '
         'звучит как позиция автора.',
    t3bh='Поворот',
    t3bb='<em>But</em>, <em>yet</em>, <em>even so</em>, <em>still</em>. Дальше '
         'идёт главный тезис автора. Он перевешивает уступку, но не отменяет '
         'её.',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> Автор придерживается и того, и другого.',
    t3ch='Чего не говорит ни одна из половин',
    t3cb='Поворот подталкивает вас досказать рассуждение за автора. Не делайте '
         'этого. Утверждение, которое идёт дальше обеих половин, &mdash; о '
         'том, что было потом, или о том, каков общий итог, &mdash; это NOT '
         'GIVEN.',
    t3cn='<em>Cheaper to run</em> &mdash; не то же самое, что <em>cheaper '
         'overall</em>. В тексте есть только одно из двух.',

    t4Eyebrow='Прежде чем начать',
    t4Title='Насколько твёрдо автор это утверждает?',
    t4ah='Степень',
    t4ab='<em>Largely</em>, <em>mostly</em>, <em>partly</em>, <em>to some '
         'extent</em>. Автор утверждает часть. Утверждение, которое претендует '
         'на всё целиком (<em>completely</em>, <em>in every way</em>, '
         '<em>everything</em>), &mdash; это NO.',
    t4an='То же правило, что <em>most</em> против <em>all</em> в True / False / '
         'Not Given.',
    t4bh='Смягчения',
    t4bb='<em>May</em>, <em>might</em>, <em>perhaps</em>, <em>it seems</em>. '
         'Смягчение говорит, что автор считает что-то возможным, а не '
         'истинным. Утверждение, которое говорит это без оговорок, обычно '
         'NOT GIVEN: автор ни согласился, ни возразил.',
    t4bn='Не NO. Автор этого не отрицал, он лишь не стал этого обещать.',
    t4ch='Оценочные слова',
    t4cb='<em>Surprisingly</em>, <em>sadly</em>, <em>rightly</em>, <em>was '
         'right to</em>. Одно слово передаёт отношение автора, и утверждения '
         'его проверяют: <em>surprisingly</em> сходится с '
         '<em>unexpected</em>.',
    t4cn='Слово оценивает что-то одно. Одобрить решение не значит сказать '
         'что-либо о его причине.',

    mcaEyebrow='Задание 1 · Чьё это мнение?',
    mcaTitle='Пересказанное или авторское?',
    mcbEyebrow='Задание 2 · Уступка и поворот',
    mcbTitle='Что уступается, а что утверждается?',
    mccEyebrow='Задание 3 · Насколько твёрдо?',
    mccTitle='Насколько далеко заходит автор?',

    r1why='Первое предложение лишь пересказывает сторонников. Вторым автор '
          'делает их мнение своим: <em>they are right</em>. YES.',
    r2why='Мнение критиков есть в тексте, и автор его отвергает: <em>They are '
          'wrong</em>. Двадцать тысяч пассажиров в день &mdash; его довод. NO.',
    r3why='Утверждение о преступности только пересказано (<em>it is often '
          'claimed</em>), и автор откладывает его в сторону: <em>whatever the '
          'truth of that</em>. Его собственное мнение &mdash; о том, насколько '
          'приятнее становятся улицы. NOT GIVEN.',
    r4why='Решает одно слово. Словом <em>mistakenly</em> автор оценивает '
          'предположение родителей, значит, сам он думает наоборот: '
          'дети-билингвы не отстают. YES.',
    r5why='Автор признаёт стоимость и задержку, а потом следует поворот: '
          '<em>Even so, I would build it again tomorrow</em>. Поворот &mdash; '
          'это его вердикт, и это не «ошибка». NO.',
    r6why='Автор признаёт, что поездки стали дольше, и хвалит пунктуальность. '
          'О числе пассажиров нет ни слова: что надёжные автобусы привлекают '
          'больше людей &mdash; ваш вывод, а не утверждение автора. NOT GIVEN.',
    r7why='<em>This is not to say that exams have no place</em> означает, что '
          'у экзаменов своё место есть: автор это признаёт и называет его '
          '&mdash; сравнивать учеников из разных школ. Уступка &mdash; это '
          'мнение самого автора. YES.',
    r8why='Для начинающих автор против, но преимущества признаёт прямо: '
          '<em>obvious benefits, and I do not dispute them</em>. Уступка '
          '&mdash; тоже его мнение, поэтому противоречить ей &mdash; это NO.',
    r9why='Автор смягчает сказанное о запрете (<em>may have</em>) и '
          'упоминает <em>other changes</em>, но нигде не говорит, что '
          'повлияло сильнее. Сравнение &mdash; ваш шаг, а не автора. NOT '
          'GIVEN, а не NO.',
    r10why='<em>Surprisingly</em> &mdash; реакция автора на результат, а '
           '<em>unexpectedly</em> &mdash; та же реакция другим словом. YES.',
    r11why='<em>Largely</em>, <em>most of the promised homes</em>, <em>a year '
           'late</em>: три ограничения успеха, и любое из них исключает '
           '<em>everything</em>. NO.',
    r12why='Автор одобряет закрытие и критикует объявление. Почему мост '
           'закрыли, текст нигде не говорит: безопасность &mdash; вероятная '
           'причина, но не утверждение автора. NOT GIVEN.',

    sortEyebrow='Задание 4 · Мнение автора?',
    sortTitle='Распределите шесть начал предложений',
    sortHint='Перетащите каждое в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Собственное мнение автора',
    sortBin2='Мнение, которое он лишь пересказывает',
    sortWhy='Три из них связывают автора. <em>I think</em> говорит это '
            'прямо; <em>rightly</em> делает своим мнение, которое автор '
            'пересказывает; <em>admittedly</em> уступает пункт, с которым '
            'автор согласен. Остальные три называют чужое мнение и на этом '
            'останавливаются &mdash; пока автор его не оценил, утверждение, '
            'построенное на нём, &mdash; NOT GIVEN.',

    actTitle='Поймать автора на слове',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах, с авторской колонкой под рукой &mdash; подойдёт '
                  'газетная колонка или рецензия. Каждый пишет по ней четыре '
                  'утверждения: одно YES, одно NO и два NOT GIVEN, одно из '
                  'них &mdash; на основе мнения, которое автор лишь '
                  'пересказывает. Обменяйтесь и ответьте. Каждое YES или NO '
                  'защищайте предложением, в котором говорит автор; для NOT '
                  'GIVEN покажите, что такого предложения нет.',
    actSpeak1='Прежде чем YES или NO будет засчитан, скажите, чей голос звучит '
              'в решающем предложении.',
    actSpeak2='Найдите уступку автора, если она есть, и напишите одно '
              'утверждение, для которого она даёт YES, и одно &mdash; для '
              'которого NO.',
    actSpeak3='Возьмите смягчённое предложение и скажите, что автору пришлось '
              'бы написать, чтобы ваше утверждение стало YES.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Напишите короткий абзац-мнение примерно на сто слов о '
                  'вопросе, который вам небезразличен, с пересказанным '
                  'мнением, уступкой и поворотом. Затем напишите к нему три '
                  'утверждения &mdash; одно YES, одно NO, одно NOT GIVEN '
                  '&mdash; и ключ, процитировав слова, которые решают каждое.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='الاختيار الثلاثي نفسه الذي في True, False, Not Given &mdash; '
             'لكن السؤال عمّا يراه الكاتب، لا عمّا يقوله النص',
    chipLevel='C1 · متقدّم', chipFocus='Reading · الوحدتان كلتاهما',
    chipCount='18 نقطة',

    optYes='Yes &mdash; الكاتب يوافق على هذا',
    optNo='No &mdash; الكاتب لا يوافق على هذا',
    optNG='Not Given &mdash; الكاتب لا يذكر ذلك',

    t1Eyebrow='قبل أن تبدأ',
    t1Title='الاختيار الثلاثي نفسه، وسؤال مختلف',
    t1ah='آراء لا حقائق',
    t1ab='يسأل True / False / Not Given عمّا <em>يقوله</em> النص، ويسأل Yes / '
         'No / Not Given عمّا <em>يراه</em> الكاتب. والتعليمات تكشف ذلك: '
         '<em>Do the following statements agree with the views of the '
         'writer?</em>',
    t1an='أحيانًا تقول التعليمات <em>claims</em> بدلًا من <em>views</em>. '
         'والطريقة واحدة.',
    t1bh='أين تصادفه',
    t1bb='في النصوص التي تحاجج: مقالات الرأي، والمراجعات، والمقالات التي '
         'تدافع عن فكرة. وستصادفه غالبًا في القسم الأخير، وهو الأكثر ميلًا '
         'إلى المحاججة.',
    t1bn='اكتب الكلمة التي تطلبها التعليمات. كلمة YES في سؤال True / False / '
         'Not Given تُحسب خطأً، حتى لو كنت تقصد TRUE.',
    t1ch='الفحص نفسه كما في True / False / Not Given',
    t1cb='<strong>هل أستطيع أن أشير إلى الجملة؟</strong> غير أنها يجب الآن أن '
         'تكون جملة يتكلّم فيها الكاتب نفسه. فإن كان السطر الوحيد الذي وجدته '
         'رأيَ شخص آخر، فأنت لم تجد الإجابة بعد.',
    t1cn='تحتاج YES وNO إلى صوت الكاتب. أما NOT GIVEN فهي صمته.',

    t2Eyebrow='قبل أن تبدأ',
    t2Title='صوتُ مَن هذا؟',
    t2ah='آراء ينقلها الكاتب',
    t2ab='عبارات مثل <em>Critics argue</em> و<em>it is often claimed</em> '
         'و<em>according to</em> و<em>many people believe</em>: الرأي موجود في '
         'النص، لكن الكاتب لم يوقّع عليه. وهو وحده لا يعطيك إلا NOT GIVEN.',
    t2an='هذه الجمل تذكر الادعاء كاملًا، فيعثر عليها أولًا من يطابق الكلمات. '
         'وهذا بالضبط ما يجعلها فخاخًا.',
    t2bh='صوت الكاتب نفسه',
    t2bb='عبارات مثل <em>I think</em> و<em>in my view</em> و<em>the truth '
         'is</em>، وفي أغلب الأحيان لا علامة على الإطلاق. في نص يحاجج، الجملة '
         'البسيطة التي لا تحمل اسم أحد آخر هي جملة الكاتب.',
    t2bn='معظم العلامات تشير إلى آراء الآخرين، ومعظم آراء الكاتب نفسه لا '
         'تحمل أي علامة.',
    t2ch='يُنقل ثم يُحكم عليه',
    t2cb='في المثال <em>Supporters say it works. They are right.</em> تجعل '
         'الجملة الثانية الرأيَ رأيَ الكاتب. ولو قال <em>They are wrong</em> '
         'لكان يتبنّى العكس.',
    t2cn='تكفي كلمة واحدة: <em>rightly</em> أو <em>wrongly</em> أو '
         '<em>mistakenly</em>.',

    t3Eyebrow='قبل أن تبدأ',
    t3Title='Admittedly &hellip; but',
    t3ah='التسليم',
    t3ab='عبارات <em>admittedly</em> و<em>of course</em> و<em>it is true '
         'that</em> و<em>this is not to say</em> (والأخيرة تسلّم بعكس ما '
         'يليها). يسلّم الكاتب للطرف الآخر بنقطة &mdash; ويظل الكاتب هو '
         'المتكلم. والنقطة المسلَّم بها نقطة يقبلها الكاتب.',
    t3an='إذا ناقضت العبارةُ التسليمَ فالإجابة NO، حتى لو بدت منسجمة مع موقف '
         'الكاتب.',
    t3bh='الانعطاف',
    t3bb='كلمات مثل <em>But</em> و<em>yet</em> و<em>even so</em> '
         'و<em>still</em>: ما يأتي بعدها هو الفكرة الرئيسية للكاتب. وهي أرجح '
         'من التسليم، لكنها لا تلغيه.',
    t3bn='في <em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> يتبنّى الكاتب الأمرين معًا.',
    t3ch='ما لا يقوله أيّ من الشقّين',
    t3cb='الانعطاف يغريك بأن تُكمل الحجة نيابةً عن الكاتب. لا تفعل. العبارة '
         'التي تتجاوز الشقّين معًا، عمّا حدث بعد ذلك أو عن الحصيلة النهائية، '
         'هي NOT GIVEN.',
    t3cn='عبارة <em>cheaper to run</em> ليست <em>cheaper overall</em>. واحدة '
         'منهما فقط موجودة في النص.',

    t4Eyebrow='قبل أن تبدأ',
    t4Title='ما مدى جزم الكاتب؟',
    t4ah='الدرجة',
    t4ab='كلمات مثل <em>Largely</em> و<em>mostly</em> و<em>partly</em> و<em>to '
         'some extent</em>: الكاتب يؤكّد جزءًا من الأمر. والعبارة التي تدّعي '
         'الكلّ، مثل <em>completely</em> و<em>in every way</em> '
         'و<em>everything</em>، هي NO.',
    t4an='القاعدة نفسها في <em>most</em> مقابل <em>all</em> في أسئلة True / '
         'False / Not Given.',
    t4bh='التلطيف',
    t4bb='كلمات مثل <em>may</em> و<em>might</em> و<em>perhaps</em> و<em>it '
         'seems</em>: التلطيف يعني أن الكاتب يرى الأمر ممكنًا، لا أنه صحيح. '
         'والعبارة التي تقرّر الادعاء دون تحفّظ تكون في الغالب NOT GIVEN: '
         'فالكاتب لم يوافق ولم يعارض.',
    t4bn='ليست NO. الكاتب لم ينكر ذلك، بل امتنع عن الوعد به فقط.',
    t4ch='كلمات التقييم',
    t4cb='كلمات مثل <em>Surprisingly</em> و<em>sadly</em> و<em>rightly</em> '
         'و<em>was right to</em>: كلمة واحدة تعطيك موقف الكاتب، والعبارات '
         'تختبره: <em>surprisingly</em> تتّفق مع <em>unexpected</em>.',
    t4cn='الكلمة تحكم على شيء واحد. استحسان قرارٍ ما لا يقول شيئًا عن سببه.',

    mcaEyebrow='النشاط 1 · رأيُ مَن هذا؟',
    mcaTitle='منقول، أم رأي الكاتب نفسه؟',
    mcbEyebrow='النشاط 2 · التسليم والانعطاف',
    mcbTitle='ما الذي يُسلَّم به، وما الذي يُؤكَّد؟',
    mccEyebrow='النشاط 3 · ما مدى الجزم؟',
    mccTitle='إلى أيّ حدّ يلتزم الكاتب؟',

    r1why='الجملة الأولى تنقل رأي المؤيّدين فقط، والثانية تجعله رأي الكاتب: '
          '<em>they are right</em>. YES.',
    r2why='رأي النقّاد موجود في النص، والكاتب يرفضه: <em>They are wrong</em>. '
          'وحجّته عشرون ألف راكب في اليوم. NO.',
    r3why='الادّعاء بشأن الجريمة منقول فقط (<em>it is often claimed</em>)، '
          'والكاتب يضعه جانبًا: <em>whatever the truth of that</em>. أما رأيه '
          'هو فيتعلّق بمدى طيب العيش في تلك الشوارع. NOT GIVEN.',
    r4why='كلمة واحدة تحسم الأمر. بكلمة <em>mistakenly</em> يحكم الكاتب على '
          'افتراض الآباء، فهو إذن يرى العكس: الأطفال ثنائيو اللغة لا يتأخّرون '
          'في المدرسة. YES.',
    r5why='يسلّم الكاتب بالتكلفة والتأخير، ثم يأتي الانعطاف: <em>Even so, I '
          'would build it again tomorrow</em>. والانعطاف هو حكمه، وليس «خطأً». '
          'NO.',
    r6why='يسلّم الكاتب بأن الرحلات صارت أطول ويمتدح الالتزام بالمواعيد. أما '
          'عدد الركاب فلا يُذكر أبدًا: أن الحافلات المنضبطة تجذب مزيدًا من '
          'الناس استنتاجك أنت، لا ادّعاء الكاتب. NOT GIVEN.',
    r7why='عبارة <em>This is not to say that exams have no place</em> تعني أن '
          'للامتحانات مكانًا: يسلّم الكاتب بذلك ويحدّده، وهو المقارنة بين طلاب '
          'من مدارس مختلفة. والتسليم رأي الكاتب نفسه. YES.',
    r8why='الكاتب يعارض العمل من المنزل للمبتدئين، لكنه يسلّم بالمزايا صراحةً: '
          '<em>obvious benefits, and I do not dispute them</em>. والتسليم رأيه '
          'أيضًا، فمناقضته NO.',
    r9why='يلطّف الكاتب كلامه عن الحظر (<em>may have</em>) ويذكر <em>other '
          'changes</em>، لكنه لا يقول أبدًا أيّهما كان أثره أكبر. المقارنة '
          'خطوتك أنت لا خطوة الكاتب. NOT GIVEN &mdash; لا NO.',
    r10why='كلمة <em>Surprisingly</em> هي ردّ فعل الكاتب على النتيجة، '
           'و<em>unexpectedly</em> هي ردّ الفعل نفسه بكلمة أخرى. YES.',
    r11why='الكلمات <em>Largely</em> و<em>most of the promised homes</em> '
           'و<em>a year late</em>: ثلاثة قيود على النجاح، وأيّ منها يكفي '
           'لاستبعاد <em>everything</em>. NO.',
    r12why='الكاتب يستحسن إغلاق الجسر وينتقد طريقة الإعلان عنه. أما سبب '
           'الإغلاق فلا يذكره النص أبدًا: السلامة سبب محتمل، لا ادّعاء '
           'للكاتب. NOT GIVEN.',

    sortEyebrow='النشاط 4 · رأي الكاتب؟',
    sortTitle='صنِّف بدايات الجمل الست',
    sortHint='اسحب كل بداية إلى عمود، أو انقر عليها ثم على العمود الذي '
             'تريده.',
    sortBin1='رأي الكاتب نفسه',
    sortBin2='رأي ينقله الكاتب فقط',
    sortWhy='ثلاث من هذه العبارات تُلزم الكاتب. <em>I think</em> تقول ذلك '
            'صراحةً، و<em>rightly</em> تتبنّى رأيًا ينقله الكاتب، '
            'و<em>admittedly</em> تسلّم بنقطة يقبلها الكاتب. أما الثلاث '
            'الأخرى فتذكر رأي غيره وتتركه عند ذلك &mdash; وحتى يحكم الكاتب '
            'عليه، تكون العبارة المبنية عليه NOT GIVEN.',

    actTitle='خُذِ الكاتب بكلامه',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي، ومعكما مقال رأي &mdash; يكفي عمود صحفي أو '
                  'مراجعة. يكتب كل منكما أربع عبارات عنه: واحدة YES، وواحدة '
                  'NO، واثنتين NOT GIVEN، إحداهما مبنية على رأي ينقله الكاتب '
                  'فقط. تبادلاها وأجيبا. دافعا عن كل YES أو NO بالجملة التي '
                  'يتكلم فيها الكاتب، وفي حالة NOT GIVEN بيّنا أنه لا توجد '
                  'جملة كهذه.',
    actSpeak1='قبل أن تُحتسب YES أو NO، قل صوتُ مَن هو في الجملة الحاسمة.',
    actSpeak2='جِد تسليم الكاتب إن وُجد، واكتب عبارة يجعلها YES وأخرى يجعلها '
              'NO.',
    actSpeak3='خذ جملة ملطّفة وقل ما كان على الكاتب أن يكتبه لتصبح عبارتك '
              'YES.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='اكتب فقرة رأي قصيرة من نحو مئة كلمة عن مسألة تهمّك، فيها '
                  'رأي منقول وتسليم وانعطاف. ثم اكتب ثلاث عبارات عنها، واحدة '
                  'YES وواحدة NO وواحدة NOT GIVEN، ومفتاح الإجابة مع اقتباس '
                  'الكلمات التي تحسم كلّ واحدة.',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='和 True, False, Not Given 一样的三选一——但问的是作者怎么想，而不是文章说了什么',
    chipLevel='C1 · 高级', chipFocus='Reading · 两个模块通用',
    chipCount='18 分',

    optYes='Yes &mdash; 作者同意这个说法',
    optNo='No &mdash; 作者不同意这个说法',
    optNG='Not Given &mdash; 作者未表态',

    t1Eyebrow='开始之前',
    t1Title='同样的三选一，不同的问题',
    t1ah='观点，而不是事实',
    t1ab='True / False / Not Given 问的是文章<em>说了</em>什么；Yes / No / Not '
         'Given 问的是作者<em>认为</em>什么。题目要求本身就透露了这一点：'
         '<em>Do the following statements agree with the views of the '
         'writer?</em>',
    t1an='有时题目用的是 <em>claims</em> 而不是 <em>views</em>，方法相同。',
    t1bh='在哪里遇到',
    t1bb='在有论证的文章里：评论文章、书评影评、提出论点的随笔。它最常出现在'
         '最后一部分，也就是最爱论证的那一篇。',
    t1bn='写题目要求的那个词。在 True / False / Not Given 题里写 YES 会被判错，'
         '哪怕你想表达的是 TRUE。',
    t1ch='和 True / False / Not Given 一样的检验',
    t1cb='<strong>我能指出是哪一句吗？</strong>只是现在，这一句必须是作者本人在'
         '说话。如果你找到的唯一一句是别人的观点，那你还没找到答案。',
    t1cn='YES 和 NO 需要作者本人的声音；NOT GIVEN 是作者的沉默。',

    t2Eyebrow='开始之前',
    t2Title='这是谁的声音？',
    t2ah='作者转述的观点',
    t2ab='<em>Critics argue</em>、<em>it is often claimed</em>、<em>according '
         'to</em>、<em>many people believe</em>。观点在文中，但作者并没有为它'
         '署名。单凭它，只能得出 NOT GIVEN。',
    t2an='这些句子把观点说得很完整，所以找词的人最先找到它们。这正是它们成为陷阱的原因。',
    t2bh='作者自己的声音',
    t2bb='<em>I think</em>、<em>in my view</em>、<em>the truth is</em>——而更多'
         '时候，根本没有任何标记。在一篇论证性文章里，没有挂上别人名字的普通'
         '陈述句，就是作者的话。',
    t2bn='大多数标记词指向的是别人的观点；作者自己的观点，大多不带任何标记。',
    t2ch='先转述，再评判',
    t2cb='<em>Supporters say it works. They are right.</em> 第二句让这个观点成'
         '了作者自己的观点。如果是 <em>They are wrong</em>，就说明作者持相反'
         '看法。',
    t2cn='一个词就够了：<em>rightly</em>、<em>wrongly</em>、'
         '<em>mistakenly</em>。',

    t3Eyebrow='开始之前',
    t3Title='Admittedly &hellip; but',
    t3ah='让步',
    t3ab='<em>Admittedly</em>、<em>of course</em>、<em>it is true '
         'that</em>、<em>this is not to say</em>（最后这个让步的是后文的反面）。作者承认对方的某一点——说话'
         '的仍然是作者。被让步的一点，就是作者接受的一点。',
    t3an='如果某个说法与让步的内容相矛盾，答案就是 NO，哪怕它听起来像是站在作者'
         '那一边。',
    t3bh='转折',
    t3bb='<em>But</em>、<em>yet</em>、<em>even so</em>、<em>still</em>。后面跟着'
         '的是作者的主要观点。它比让步更重要，但并不取消让步。',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> 两点作者都认同。',
    t3ch='两半都没说的内容',
    t3cb='转折会诱使你替作者把论证说完。别这么做。超出前后两半的说法——关于之后'
         '发生了什么，或者总体结论如何——都是 NOT GIVEN。',
    t3cn='<em>Cheaper to run</em> 不等于 <em>cheaper overall</em>。文中只有其中'
         '一个。',

    t4Eyebrow='开始之前',
    t4Title='作者说得有多肯定？',
    t4ah='程度',
    t4ab='<em>Largely</em>、<em>mostly</em>、<em>partly</em>、<em>to some '
         'extent</em>。作者只肯定了一部分。说成全部的说法——<em>completely</em>'
         '、<em>in every way</em>、<em>everything</em>——是 NO。',
    t4an='和 True / False / Not Given 里 <em>most</em> 对 <em>all</em> 是同一条'
         '规则。',
    t4bh='模糊限制语',
    t4bb='<em>May</em>、<em>might</em>、<em>perhaps</em>、<em>it '
         'seems</em>。模糊限制语表示作者认为某事有可能，而不是说它是真的。把同一件事说得毫无保留的陈述，通常是 NOT '
         'GIVEN：作者既没同意，也没反对。',
    t4bn='不是 NO。作者没有否认，只是没有打包票。',
    t4ch='评价词',
    t4cb='<em>Surprisingly</em>、<em>sadly</em>、<em>rightly</em>、<em>was '
         'right to</em>。一个词就能体现作者的态度，而题目考的正是这种态度：'
         '<em>surprisingly</em> 与 <em>unexpected</em> 意思一致。',
    t4cn='评价词只评判一件事。赞成一个决定，并不等于说出了这个决定的原因。',

    mcaEyebrow='练习 1 · 这是谁的观点？',
    mcaTitle='转述的，还是作者自己的？',
    mcbEyebrow='练习 2 · 让步与转折',
    mcbTitle='让步承认了什么，主张的又是什么？',
    mccEyebrow='练习 3 · 有多肯定？',
    mccTitle='作者表态到什么程度？',

    r1why='第一句只是转述支持者的说法。第二句让它成了作者的观点：<em>they are '
          'right</em>。YES。',
    r2why='批评者的观点在文中，而作者驳斥了它：<em>They are wrong</em>。每天两万'
          '名乘客就是作者的理由。NO。',
    r3why='关于犯罪的说法只是被转述（<em>it is often claimed</em>），作者把它搁'
          '在一边：<em>whatever the truth of that</em>。作者自己的观点是关于这些'
          '街道住起来有多舒适。NOT GIVEN。',
    r4why='一个词决定了答案。作者用 <em>mistakenly</em> 评判了家长们的想法，所以'
          '作者持相反观点：双语儿童在学校不会落后。YES。',
    r5why='作者承认了超支和延期，接着转折：<em>Even so, I would build it again '
          'tomorrow</em>。转折就是作者的结论，而结论不是“这是个错误”。NO。',
    r6why='作者承认有些行程变长了，并称赞了准点。乘客人数从未提及：可靠的公交会'
          '吸引更多人，是你的推断，而不是作者的说法。NOT GIVEN。',
    r7why='<em>This is not to say that exams have no place</em> 的意思是考试确实'
          '有它的位置：作者承认这一点，并说明是什么——比较来自不同学校的学生。'
          '让步本身就是作者的观点。YES。',
    r8why='作者反对刚入行的人在家办公，但坦然承认它的好处：<em>obvious '
          'benefits, and I do not dispute them</em>。让步同样是作者的观点，与之'
          '矛盾就是 NO。',
    r9why='作者对禁令的说法有所保留（<em>may have</em>），也提到了 <em>other '
          'changes</em>，但从没说哪个作用更大。比较它们是你的推断，不是作者的说法。NOT GIVEN——不是 NO。',
    r10why='<em>Surprisingly</em> 是作者对结果的反应，<em>unexpectedly</em> 是换'
           '一个词表达同样的反应。YES。',
    r11why='<em>Largely</em>、<em>most of the promised homes</em>、<em>a year '
           'late</em>：对成功的三个限定，任何一个都足以排除 '
           '<em>everything</em>。NO。',
    r12why='作者赞成关闭这座桥，批评了宣布的方式。桥为什么关闭，文中从未提及：'
           '安全是可能的原因，但不是作者的说法。NOT GIVEN。',

    sortEyebrow='练习 4 · 是作者自己的观点吗？',
    sortTitle='给这六个句子开头分类',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='作者自己的观点',
    sortBin2='作者只是转述的观点',
    sortWhy='其中三句让作者表了态。<em>I think</em> 直接说出来；<em>rightly</em> '
            '把作者转述的观点变成自己的；<em>admittedly</em> '
            '让步于作者接受的一点。另外三句只点出别人的观点，就此打住——在作者作出评判之前，基于它们的陈述都是 NOT GIVEN。',

    actTitle='让作者表明立场',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组，手边准备一篇评论文章——报纸专栏或书评都行。每人针对它写四个陈述：一个 YES，一个 NO，两个 NOT '
                  'GIVEN，其中一个建立在作者只是转述的观点上。交换并作答。每个 YES 或 NO，都用作者表态的那句话来辩护；对 '
                  'NOT GIVEN，要说明没有这样的句子。',
    actSpeak1='在 YES 或 NO 算数之前，先说出决定答案的那一句是谁的声音。',
    actSpeak2='找出作者的让步（如果有的话），写一个据此为 YES 的说法和一个据此为 '
              'NO 的说法。',
    actSpeak3='找一个用了模糊限制语的句子，说说作者要写成什么样，你的说法才会是 '
              'YES。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='就一个你关心的问题写一段约一百词的观点短文，其中要有一个转述'
                  '的观点、一个让步和一个转折。然后针对它写三个说法——一个 YES、'
                  '一个 NO、一个 NOT GIVEN——并写出答案，引用决定每个答案的'
                  '原词。',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='True, False, Not Given と同じ三択――ただし問われるのは本文の内容ではなく、筆者の考え',
    chipLevel='C1 · 上級', chipFocus='Reading · 両モジュール共通',
    chipCount='18 点',

    optYes='Yes &mdash; 筆者はこれに同意しています',
    optNo='No &mdash; 筆者はこれに反対しています',
    optNG='Not Given &mdash; 筆者は述べていません',

    t1Eyebrow='始める前に',
    t1Title='同じ三択、違う問い',
    t1ah='事実ではなく意見',
    t1ab='True / False / Not Given は本文が何を<em>言っているか</em>を問います。'
         'Yes / No / Not Given は筆者が何を<em>考えているか</em>を問います。指示'
         '文がそれを明かしています：<em>Do the following statements agree with '
         'the views of the writer?</em>',
    t1an='指示文が <em>views</em> ではなく <em>claims</em> になっていることもあり'
         'ます。解き方は同じです。',
    t1bh='どこで出会うか',
    t1bb='主張のある文章で出ます。論説、レビュー、自説を展開するエッセイなどです。'
         '特に多いのは最後のセクションで、最も論じる傾向が強いパートです。',
    t1bn='指示文が求める語を書いてください。True / False / Not Given の問題に '
         'YES と書くと、TRUE のつもりでも不正解になります。',
    t1ch='True / False / Not Given と同じ確かめ方',
    t1cb='<strong>その文を指させるか？</strong>ただし今度は、筆者自身が語っている'
         '文でなければなりません。見つかったのが他人の意見の一文だけなら、まだ答え'
         'は見つかっていません。',
    t1cn='YES と NO には筆者の声が必要です。NOT GIVEN は筆者の沈黙です。',

    t2Eyebrow='始める前に',
    t2Title='これは誰の声か？',
    t2ah='筆者が紹介するだけの意見',
    t2ab='<em>Critics argue</em>、<em>it is often claimed</em>、<em>according '
         'to</em>、<em>many people believe</em>。意見は本文にありますが、筆者は'
         'それに署名していません。それだけでは NOT GIVEN にしかなりません。',
    t2an='こうした文は主張を丸ごと述べているので、語の照合で真っ先に見つかります。まさにそれが罠になる理由です。',
    t2bh='筆者自身の声',
    t2bb='<em>I think</em>、<em>in my view</em>、<em>the truth is</em>――そして、'
         'はるかに多いのは何の目印もない場合です。論じる文章では、他の誰の名前も'
         '付いていない普通の文は筆者のものです。',
    t2bn='ほとんどの目印は他人の見解を指しています。筆者自身の見解の多くには、目印がありません。',
    t2ch='紹介してから評価する',
    t2cb='<em>Supporters say it works. They are right.</em> 二文目で、筆者はそ'
         'の意見を自分のものにしています。<em>They are wrong</em> なら、筆者は'
         '逆の立場だということです。',
    t2cn='一語で足ります：<em>rightly</em>、<em>wrongly</em>、'
         '<em>mistakenly</em>。',

    t3Eyebrow='始める前に',
    t3Title='Admittedly &hellip; but',
    t3ah='譲歩',
    t3ab='<em>Admittedly</em>、<em>of course</em>、<em>it is true '
         'that</em>、<em>this is not to say</em>（最後のものは、続く内容の反対を認めます）。筆者は相手側の一'
         '点を認めます――それでも話しているのは筆者です。認めた点は、筆者が受け入れている点です。',
    t3an='譲歩の内容に矛盾する文は、筆者の側の主張に聞こえても NO です。',
    t3bh='転換',
    t3bb='<em>But</em>、<em>yet</em>、<em>even so</em>、<em>still</em>。その後に'
         '来るのが筆者の主な主張です。譲歩より重いですが、譲歩を打ち消すわけでは'
         'ありません。',
    t3bn='<em>Admittedly, the trial was small. But its results were clear '
         'enough to act on.</em> 筆者はどちらも認めています。',
    t3ch='どちらの半分も言っていないこと',
    t3cb='転換は、筆者に代わって議論を最後まで言い切りたくさせます。そうしないで'
         'ください。前後どちらの半分よりも先へ進む文――その後どうなったか、全体と'
         'してどうなのか――は NOT GIVEN です。',
    t3cn='<em>Cheaper to run</em> は <em>cheaper overall</em> ではありません。'
         '本文にあるのは片方だけです。',

    t4Eyebrow='始める前に',
    t4Title='筆者はどれほど強く言っているか？',
    t4ah='程度',
    t4ab='<em>Largely</em>、<em>mostly</em>、<em>partly</em>、<em>to some '
         'extent</em>。筆者が主張しているのは一部です。全部だと言い切る文――'
         '<em>completely</em>、<em>in every way</em>、<em>everything</em>――は '
         'NO です。',
    t4an='True / False / Not Given の <em>most</em> 対 <em>all</em> と同じ規則'
         'です。',
    t4bh='ぼかし表現',
    t4bb='<em>May</em>、<em>might</em>、<em>perhaps</em>、<em>it '
         'seems</em>。ぼかし表現は、筆者がそれを可能だと考えていることを示すだけで、真実だとは言っていません。同じことを留保なしに述べ'
         'る文は、ふつう NOT GIVEN です：筆者は賛成も反対もしていません。',
    t4bn='NO ではありません。筆者は否定しておらず、保証するのを控えただけです。',
    t4ch='評価の言葉',
    t4cb='<em>Surprisingly</em>、<em>sadly</em>、<em>rightly</em>、<em>was '
         'right to</em>。一語で筆者の態度がわかり、設問はそこを試します：'
         '<em>surprisingly</em> は <em>unexpected</em> と一致します。',
    t4cn='評価の言葉が評価するのは一つのことだけです。決定を支持しても、その理由'
         'については何も言っていません。',

    mcaEyebrow='演習 1 · これは誰の意見か？',
    mcaTitle='紹介されただけか、筆者自身のものか？',
    mcbEyebrow='演習 2 · 譲歩と転換',
    mcbTitle='何が認められ、何が主張されているか？',
    mccEyebrow='演習 3 · どれほど強く？',
    mccTitle='筆者はどこまで言い切っているか？',

    r1why='一文目は支持者の意見を紹介しているだけです。二文目で筆者はその意見を'
          '自分のものにしています：<em>they are right</em>。YES。',
    r2why='批判者の意見は本文にありますが、筆者はそれを退けています：<em>They '
          'are wrong</em>。一日二万人の乗客が筆者の根拠です。NO。',
    r3why='犯罪についての主張は紹介されているだけで（<em>it is often '
          'claimed</em>）、筆者はそれを脇に置いています：<em>whatever the truth '
          'of that</em>。筆者自身の意見は、通りの住み心地についてです。NOT '
          'GIVEN。',
    r4why='一語で決まります。筆者は <em>mistakenly</em> で親たちの思い込みを評価'
          'しているので、筆者自身は逆の考えです：バイリンガルの子どもは学校で遅れ'
          'をとりません。YES。',
    r5why='筆者は費用と遅れを認め、それから転換します：<em>Even so, I would '
          'build it again tomorrow</em>。転換が筆者の結論であり、それは「間違い」'
          'ではありません。NO。',
    r6why='筆者は一部の移動が長くなったことを認め、定時運行を評価しています。乗客'
          '数には一度も触れていません。信頼できるバスが利用者を増やすというのはあ'
          'なたの推測で、筆者の主張ではありません。NOT GIVEN。',
    r7why='<em>This is not to say that exams have no place</em> は、試験にも役割'
          'があるという意味です。筆者はそれを認め、その役割を示しています――異なる'
          '学校の生徒を比べることです。譲歩は筆者自身の意見です。YES。',
    r8why='筆者は新人の在宅勤務には反対ですが、利点ははっきり認めています：'
          '<em>obvious benefits, and I do not dispute them</em>。譲歩も筆者の意見'
          'なので、それに矛盾すれば NO です。',
    r9why='筆者は禁止について <em>may have</em> とぼかし、<em>other changes</em> '
          'にも触れていますが、どちらがより効いたかは言っていません。比べるのはあなたの推論で、筆者の主張ではありません。NOT '
          'GIVEN――NO ではありません。',
    r10why='<em>Surprisingly</em> は結果に対する筆者の反応で、'
           '<em>unexpectedly</em> は同じ反応を別の語で言ったものです。YES。',
    r11why='<em>Largely</em>、<em>most of the promised homes</em>、<em>a year '
           'late</em>：成功に対する三つの限定で、どれか一つだけでも '
           '<em>everything</em> を否定します。NO。',
    r12why='筆者は閉鎖を支持し、発表のしかたを批判しています。橋がなぜ閉鎖された'
           'のか、本文はどこにも書いていません。安全はありそうな理由ですが、筆者の'
           '主張ではありません。NOT GIVEN。',

    sortEyebrow='演習 4 · 筆者自身の意見か？',
    sortTitle='六つの書き出しを分類しましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='筆者自身の意見',
    sortBin2='筆者が紹介しているだけの意見',
    sortWhy='このうち三つは筆者の立場を示しています。<em>I think</em> ははっきり言い、<em>rightly</em> '
            'は筆者が伝えている見解を自分のものにし、<em>admittedly</em> '
            'は筆者が受け入れる一点を認めます。残りの三つは他人の見解を挙げてそのままにしています――筆者が判断するまで、それに基づく文は '
            'NOT GIVEN です。',

    actTitle='筆者の言葉をつかまえる',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで、意見記事を手元に用意します――新聞のコラムや書評で十分です。それぞれがその記事について四つの文を書きます：Y'
                  'ES を一つ、NO を一つ、NOT GIVEN を二つで、そのうち一つは筆者が伝えているだけの見解をもとにします。交'
                  '換して答えましょう。YES と NO は筆者が語っている文で守り、NOT GIVEN '
                  'については、そういう文がないことを示します。',
    actSpeak1='YES や NO を認める前に、決め手となる文が誰の声かを言いましょう。',
    actSpeak2='筆者の譲歩があれば見つけ、それによって YES になる文と NO になる文を'
              '一つずつ書きましょう。',
    actSpeak3='ぼかし表現のある文を一つ選び、あなたの文が YES になるには筆者が何と'
              '書く必要があったかを言いましょう。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='あなたが関心を持っている問題について、百語ほどの短い意見文を書き'
                  'ましょう。紹介する意見、譲歩、転換を入れます。次に、それについ'
                  'て三つの文――YES、NO、NOT GIVEN を一つずつ――と解答を書き、そ'
                  'れぞれの決め手となる語句を引用します。',
    actPlaceholder='My paragraph: … Statement 1 (YES): … Decided by: …',
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
