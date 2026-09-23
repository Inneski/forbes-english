# -*- coding: utf-8 -*-
"""Interface strings for IELTS Reading: Yes / No / Not Given.

English, German and Spanish, teach cards in the six-item form. `T['en']` is
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

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Yes, No, <em>Not Given</em>',
    coverSub='The same three answers as True, False, Not Given &mdash; asked '
             'about what the writer thinks, not what the passage says',
    chipLevel='C1 · Advanced', chipFocus='Reading · both modules',
    chipCount='18 points',

    t1Eyebrow='Before you start',
    t1Title='Same three answers, a different question',
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
    t1ch='The test has not changed',
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
         'them first. That is exactly why they trap.',
    t2bh='The writer&rsquo;s own voice',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'and far more often, no marker at all. In a passage that argues, a '
         'plain statement with nobody else&rsquo;s name on it is the '
         'writer&rsquo;s.',
    t2bn='Markers point at the other voices. Most of the writer&rsquo;s own '
         'views are unmarked.',
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
         '<em>this is not to say</em>. The writer grants the other side a '
         'point &mdash; and it is still the writer speaking. A point conceded '
         'is a point the writer accepts.',
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
         'A hedge commits the writer to nothing. A statement making the claim '
         'outright is NOT GIVEN: the writer has neither agreed nor disagreed.',
    t4bn='Not NO. The writer has not denied it, only refused to promise it.',
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
    r9why='<em>May have</em> commits the writer to nothing, and <em>other '
          'changes</em> says why. The writer has not agreed and has not '
          'disagreed. NOT GIVEN &mdash; not NO.',
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
    sortWhy='Only the left column is the writer&rsquo;s own view. <em>I '
            'think</em> says so outright; <em>rightly</em> takes over a view '
            'the writer is reporting; <em>admittedly</em> grants a point the '
            'writer accepts. The right column names someone else&rsquo;s view '
            'and leaves it there &mdash; until the writer judges it, a '
            'statement built on it is NOT GIVEN.',

    actTitle='Put the writer on record',
    actUse='Use at least three:',
    actSpeakBrief='In pairs, with an opinion piece to hand &mdash; a newspaper '
                  'column or a review will do. One of you writes four '
                  'statements about it: one YES, one NO, two NOT GIVEN, and at '
                  'least one that repeats a view the writer only reports. '
                  'Swap, answer, and defend each verdict by reading out the '
                  'sentence in which the writer speaks.',
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
    coverSub='Dieselben drei Antworten wie bei True, False, Not Given &mdash; '
             'nur geht es darum, was der Autor denkt, nicht was der Text sagt',
    chipLevel='C1 · Fortgeschritten', chipFocus='Reading · beide Module',
    chipCount='18 Punkte',

    optYes='Yes &mdash; der Autor stimmt dieser Aussage zu',
    optNo='No &mdash; der Autor widerspricht dieser Aussage',
    optNG='Not Given &mdash; der Autor sagt dazu nichts',

    t1Eyebrow='Bevor du beginnst',
    t1Title='Dieselben drei Antworten, eine andere Frage',
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
    t1ch='Die Prüfung bleibt dieselbe',
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
    t2an='Solche Sätze nennen die Behauptung vollständig, deshalb findet '
         'Wortabgleich sie zuerst. Genau darum sind sie eine Falle.',
    t2bh='Die eigene Stimme des Autors',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'und viel öfter gar kein Signal. In einem argumentierenden Text '
         'gehört ein schlichter Satz ohne fremden Namen dem Autor.',
    t2bn='Signale zeigen auf die anderen Stimmen. Die meisten Ansichten des '
         'Autors stehen ohne Signal da.',
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
         '<em>this is not to say</em>. Der Autor räumt der Gegenseite einen '
         'Punkt ein &mdash; und spricht dabei immer noch selbst. Was er '
         'zugesteht, hält er für richtig.',
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
         'Eine Abschwächung legt den Autor auf nichts fest. Eine Aussage, die '
         'dasselbe ohne Einschränkung behauptet, ist NOT GIVEN: Der Autor hat '
         'weder zugestimmt noch widersprochen.',
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
    r9why='<em>May have</em> legt den Autor auf nichts fest, und <em>other '
          'changes</em> sagt, warum. Er hat weder zugestimmt noch '
          'widersprochen. NOT GIVEN &mdash; nicht NO.',
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
    sortWhy='Nur die linke Spalte ist die eigene Meinung des Autors. <em>I '
            'think</em> sagt es direkt; mit <em>rightly</em> macht er sich '
            'eine wiedergegebene Meinung zu eigen; mit <em>admittedly</em> '
            'räumt er einen Punkt ein, den er akzeptiert. Die rechte Spalte '
            'nennt die Meinung anderer und lässt sie stehen &mdash; solange '
            'der Autor sie nicht bewertet, ist eine Aussage darüber NOT GIVEN.',

    actTitle='Den Autor beim Wort nehmen',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit, mit einem Meinungstext zur Hand &mdash; eine '
                  'Zeitungskolumne oder eine Rezension genügt. Einer schreibt '
                  'vier Aussagen dazu: eine YES, eine NO, zwei NOT GIVEN, und '
                  'mindestens eine, die eine nur wiedergegebene Meinung '
                  'aufgreift. Tauschen, beantworten, und jedes Urteil '
                  'verteidigen, indem ihr den Satz vorlest, in dem der Autor '
                  'selbst spricht.',
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
    coverSub='Las mismas tres respuestas que en True, False, Not Given, pero '
             'sobre lo que piensa el autor, no sobre lo que dice el texto',
    chipLevel='C1 · Avanzado', chipFocus='Reading · los dos módulos',
    chipCount='18 puntos',

    optYes='Yes &mdash; el autor está de acuerdo',
    optNo='No &mdash; el autor no está de acuerdo',
    optNG='Not Given &mdash; el autor no lo dice',

    t1Eyebrow='Antes de empezar',
    t1Title='Las mismas tres respuestas, otra pregunta',
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
    t1ch='La prueba no ha cambiado',
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
    t2an='Estas frases enuncian la afirmación entera, así que cotejar '
         'palabras las encuentra primero. Justo por eso son una trampa.',
    t2bh='La voz del propio autor',
    t2bb='<em>I think</em>, <em>in my view</em>, <em>the truth is</em> &mdash; '
         'y, mucho más a menudo, ninguna marca. En un texto que argumenta, una '
         'afirmación sin el nombre de nadie más es del autor.',
    t2bn='Las marcas señalan las otras voces. La mayoría de las opiniones del '
         'autor van sin marca.',
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
         '<em>this is not to say</em>. El autor le concede un punto a la otra '
         'parte, y sigue hablando él. Lo que concede, lo acepta.',
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
         'Un matiz no compromete al autor a nada. Una afirmación rotunda de lo '
         'mismo es NOT GIVEN: el autor ni ha dicho que sí ni ha dicho que no.',
    t4bn='No es NO. El autor no lo ha negado; solo no se ha comprometido.',
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
    r9why='<em>May have</em> no compromete al autor a nada, y <em>other '
          'changes</em> dice por qué. Ni ha dicho que sí ni ha dicho que no. '
          'NOT GIVEN, no NO.',
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
    sortWhy='Solo la columna de la izquierda es opinión del autor. <em>I '
            'think</em> lo dice abiertamente; <em>rightly</em> hace suya una '
            'opinión que recoge; <em>admittedly</em> concede un punto que el '
            'autor acepta. La columna de la derecha nombra la opinión de otros '
            'y la deja ahí: mientras el autor no la juzgue, una afirmación '
            'basada en ella es NOT GIVEN.',

    actTitle='Que el autor se moje',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas, con un texto de opinión a mano: vale una '
                  'columna de periódico o una reseña. Uno escribe cuatro '
                  'afirmaciones sobre él: una YES, una NO, dos NOT GIVEN, y al '
                  'menos una que repita una opinión que el autor solo recoge. '
                  'Intercambiad, responded y defended cada veredicto leyendo '
                  'en voz alta la frase en la que habla el autor.',
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
