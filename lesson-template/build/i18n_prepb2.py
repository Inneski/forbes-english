# -*- coding: utf-8 -*-
"""Interface strings for Advanced Prepositions (B2).

English, German and Spanish, teach cards in the six-item form.

The Spanish is a full translation, not the stripped footnote the old page
carried. That page's `es:` field was unaccented throughout — "proposito",
"espanol", "razon", "exito", "solucion" — but it was doing something worth
keeping: naming the Spanish structure a learner maps the English onto. Those
mappings survive here, spelled correctly.

The English being taught stays English: stems, options, and the phrases
quoted inside an explanation.
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
    coverTitle='Advanced <em>Prepositions</em>',
    coverSub='Purpose, fixed phrases, dependent pairs and the phrasal verbs '
             'that carry them',
    chipLevel='B2 · Upper-intermediate', chipFocus='Prepositions',
    chipCount='28 questions',

    t1Eyebrow='Before you start',
    t1Title='Purpose: what a thing is for, why a person acts',
    t1ah='For + noun or -ing',
    t1ab='<strong>For</strong> names the <em>function</em> of a thing. Boots made '
         '<em>for walking</em>, an account <em>for paying fees</em>, a cream '
         '<em>for reducing lines</em>.',
    t1an='What follows is a noun or an <em>-ing</em> form, never a bare infinitive.',
    t1bh='To + infinitive',
    t1bb='<strong>To</strong> gives the <em>reason</em> a person does something. '
         'I go to the gym <em>to get fit</em>; she took the early train <em>to '
         'avoid the queues</em>.',
    t1bn='<em>In order to</em> is the same thing, one register up. There is no '
         '<em>in order for</em> to match it.',
    t1ch='The test that works',
    t1cb='Read what comes after the gap, not who the subject is. <em>For</em> '
         'takes a noun or an <em>-ing</em> form; <em>to</em> takes a bare '
         'infinitive. That test never fails.',
    t1cn='What the gap describes is the function of a thing, or the goal of an '
         'action &mdash; a person can be the subject of either.',

    t2Eyebrow='Before you start',
    t2Title='Fixed phrases: the preposition is not a slot',
    t2ah='The whole phrase is the word',
    t2ab='<em>In terms of</em>, <em>on behalf of</em>, <em>in spite of</em> '
         '&mdash; these are single items of vocabulary that happen to be three '
         'words long. Nothing inside them is chosen.',
    t2an='Learn them whole, the way you learn <em>however</em> or '
         '<em>nevertheless</em>.',
    t2bh='Bookended by prepositions',
    t2bb='Most take one preposition at each end: <em>on</em> the verge '
         '<em>of</em>, <em>at</em> the expense <em>of</em>, <em>for</em> the sake '
         '<em>of</em>. Drop either and the phrase stops working.',
    t2bn='The gap is usually the first one, because the second is almost always '
         '<em>of</em>.',
    t2ch='They mark register',
    t2cb='This set belongs to formal and written English &mdash; reports, '
         'speeches, meetings. Using them is part of sounding B2 rather than B1.',
    t2cn='<em>In spite of</em> and <em>despite</em> mean the same; '
         '<em>despite</em> takes no <em>of</em>.',

    t3Eyebrow='Before you start',
    t3Title='Verbs and adjectives that come with a preposition',
    t3ah='Same idea, different preposition',
    t3ab='You <em>accuse</em> someone <em>of</em> something but <em>blame</em> '
         'someone <em>for</em> it. The meanings are close; the prepositions are '
         'not interchangeable.',
    t3an='This is the pair that catches people out most often at B2.',
    t3bh='Three that take a person and a thing',
    t3bb='<em>Prevent</em> someone <em>from</em> doing it, <em>congratulate</em> '
         'someone <em>on</em> it, <em>succeed in</em> doing it. Each has exactly '
         'one preposition.',
    t3bn='<em>Succeed in</em> and <em>prevent from</em> are both followed by '
         '<em>-ing</em>, never an infinitive.',
    t3ch='What things are made of',
    t3cb='<em>Consist of</em> lists the parts; <em>specialise in</em> names the '
         'field. <em>Consist of</em> has no passive &mdash; nothing "is consisted '
         'of".',
    t3cn='<em>Comprise</em> means the same as <em>consist of</em> and takes no '
         'preposition at all.',

    t4Eyebrow='Before you start',
    t4Title='Phrasal verbs where the preposition is the meaning',
    t4ah='Three words, one verb',
    t4ab='<em>Look up to</em>, <em>look down on</em>, <em>put up with</em>, '
         '<em>come up with</em>. The whole string is the verb; no part of it can '
         'be changed or moved.',
    t4an='The object always comes after the entire phrase: put up with <em>the '
         'noise</em>.',
    t4bh='The direction carries the meaning',
    t4bb='Look <em>up to</em> someone is to admire them; look <em>down on</em> '
         'someone is to think yourself above them. One particle apart, opposite '
         'in meaning.',
    t4bn='The literal image survives here, which makes this pair unusually easy '
         'to remember.',
    t4ch='Nothing to work out',
    t4cb='<em>Get away with</em> is to escape consequences, <em>stand up for</em> '
         'is to defend, <em>cut down on</em> is to reduce. None of these is '
         'recoverable from the parts.',
    t4cn='These are the ones that make speech sound natural, so they are worth '
         'the memorising.',

    mcaEyebrow='Activity 1 · Purpose', mcaTitle='For, or to?',
    mcbEyebrow='Activity 2 · Fixed phrases', mcbTitle='Complete the expression',
    mccEyebrow='Activity 3 · Dependent pairs',
    mccTitle='Which preposition does the word take?',
    mcdEyebrow='Activity 4 · Phrasal verbs', mcdTitle='Finish the phrasal verb',

    q1why='<strong>For.</strong> The boots are a thing with a function, and a '
          'function takes <em>for</em> plus a noun or an <em>-ing</em> form.',
    q2why='<strong>To.</strong> A person is acting with a goal, and a goal takes '
          '<em>to</em> plus the infinitive &mdash; to get fit.',
    q3why='<strong>For.</strong> The account is a thing with an intended use, so '
          '<em>for paying</em>, not <em>to paying</em>.',
    q4why='<strong>To.</strong> He is a person with a reason for working two '
          'jobs. <em>To support</em> gives that reason.',
    q5why='<strong>For.</strong> The attachment is a tool, and what a tool is '
          'used for takes <em>for</em> plus <em>-ing</em>.',
    q6why='<strong>To.</strong> They arrived early in order to achieve '
          'something. That is a person with a goal, so <em>to get</em>.',
    q7why='<strong>For.</strong> The cream is a product with a stated purpose. '
          '<em>Specifically for reducing</em> names what it is meant to do.',

    q8why='<strong>On.</strong> <em>Depend on</em> is fixed and takes no other '
          'preposition. <em>Rely on</em> behaves the same way.',
    q9why='<strong>Of.</strong> <em>In terms of</em> introduces the particular '
          'aspect under discussion &mdash; here, salary rather than anything '
          'else.',
    q10why='<strong>On.</strong> <em>On behalf of</em> means speaking or acting '
           'as someone else&rsquo;s representative.',
    q11why='<strong>In.</strong> <em>In spite of</em> introduces a contrast. '
           '<em>Despite</em> means the same and takes no <em>of</em>.',
    q12why='<strong>On.</strong> <em>On the verge of</em> means very close to '
           'something happening, and it is almost always about something bad.',
    q13why='<strong>At.</strong> <em>At the expense of</em> means the gain caused '
           'a loss to someone or something else.',
    q14why='<strong>For.</strong> <em>For the sake of</em> gives the person or '
           'reason something is done for &mdash; here, the children.',

    q15why='<strong>Of.</strong> The pattern is <em>accuse someone of '
           'something</em>. <em>Blame</em> is the near-synonym that takes '
           '<em>for</em> instead.',
    q16why='<strong>For.</strong> The pattern is <em>blame someone for '
           'something</em>. Note that <em>accuse</em>, which is close in '
           'meaning, takes <em>of</em>.',
    q17why='<strong>In.</strong> <em>Succeed in doing something</em> is fixed, '
           'and what follows is always an <em>-ing</em> form, never an '
           'infinitive.',
    q18why='<strong>From.</strong> <em>Prevent someone from doing something</em> '
           'is fixed, and it too takes an <em>-ing</em> form.',
    q19why='<strong>On.</strong> <em>Congratulate someone on something</em> is '
           'the fixed pattern &mdash; on a promotion, on passing an exam.',
    q20why='<strong>In.</strong> <em>Specialise in something</em> names a '
           'professional field or area of expertise.',
    q21why='<strong>Of.</strong> <em>Consist of</em> lists what something is made '
           'up of. It has no passive form &mdash; nothing "is consisted of".',

    q22why='<strong>To.</strong> <em>Look up to someone</em> is to admire and '
           'respect them. Its opposite, <em>look down on</em>, is one particle '
           'away.',
    q23why='<strong>With.</strong> <em>Put up with something</em> is to tolerate '
           'it without complaining. All three words belong to the verb.',
    q24why='<strong>With.</strong> <em>Get away with something</em> is to escape '
           'the punishment or consequences for it.',
    q25why='<strong>With.</strong> <em>Come up with something</em> is to produce '
           'an idea or a plan &mdash; the object follows the whole phrase.',
    q26why='<strong>On.</strong> <em>Look down on someone</em> is to think '
           'yourself better than them. Compare <em>look up to</em>.',
    q27why='<strong>For.</strong> <em>Stand up for something</em> is to defend a '
           'belief or a principle, often at some cost.',
    q28why='<strong>On.</strong> <em>Cut down on something</em> is to reduce how '
           'much of it you consume or do.',

    resPerfect='Perfect score. Purpose, fixed phrases, dependent pairs and '
               'phrasal verbs — all under control.',
    resStrong='Strong work. Look again at the for/to split — that is usually '
              'where the last point goes.',
    resMid='A good base. Go back to the fixed-phrase slide: these are learned '
           'whole, not assembled.',
    resLow='Read the four teaching slides again and retry. None of this set is '
           'worked out from the parts.',

    actTitle='Make the case',
    actUse='Use at least three:',
    actSpeakBrief='A department is being cut. One of you speaks for the staff, '
                  'the other for management. Five minutes each side, then swap '
                  'roles and argue the opposite.',
    actSpeak1='Speak <em>on behalf of</em> your team and say what the decision '
              'would cost, <em>in terms of</em> morale as well as money.',
    actSpeak2='Concede one point — something you have had to <em>put up '
              'with</em> — then <em>come up with</em> an alternative.',
    actSpeak3='Argue that the saving comes <em>at the expense of</em> something '
              'the company cannot afford to lose.',
    actWriteKind='Writing · 180–250 words',
    actWriteBrief='Write the email your side sends afterwards: what was agreed, '
                  'what remains open, and what you are asking for next. It goes '
                  'to people who were not in the room, so nothing can be left '
                  'implied. Use at least three of the expressions above.',
    actPlaceholder='Following this morning’s meeting…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Präpositionen <em>für Fortgeschrittene</em>',
    coverSub='Zweck, feste Wendungen, abhängige Paare und die Phrasal Verbs, '
             'die sie tragen',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Präpositionen',
    chipCount='28 Fragen',

    t1Eyebrow='Bevor du anfängst',
    t1Title='Zweck: wofür eine Sache da ist, warum eine Person handelt',
    t1ah='For + Substantiv oder -ing',
    t1ab='<strong>For</strong> benennt die <em>Funktion</em> einer Sache. Stiefel '
         '<em>for walking</em>, ein Konto <em>for paying fees</em>, eine Creme '
         '<em>for reducing lines</em>.',
    t1an='Danach steht ein Substantiv oder eine <em>-ing</em>-Form, nie ein '
         'blanker Infinitiv.',
    t1bh='To + Infinitiv',
    t1bb='<strong>To</strong> nennt den <em>Grund</em>, aus dem eine Person etwas '
         'tut. I go to the gym <em>to get fit</em>; she took the early train <em>to '
         'avoid the queues</em>.',
    t1bn='<em>In order to</em> ist dasselbe, eine Stufe formeller. Ein passendes '
         '<em>in order for</em> gibt es nicht.',
    t1ch='Der Test, der funktioniert',
    t1cb='Lies, was nach der Lücke steht, nicht wer das Subjekt ist. '
         '<em>For</em> nimmt ein Substantiv oder eine <em>-ing</em>-Form; '
         '<em>to</em> nimmt den reinen Infinitiv. Dieser Test versagt nie.',
    t1cn='Die Lücke beschreibt den Zweck einer Sache oder das Ziel einer '
         'Handlung &mdash; eine Person kann bei beidem das Subjekt sein.',

    t2Eyebrow='Bevor du anfängst',
    t2Title='Feste Wendungen: die Präposition ist keine Lücke',
    t2ah='Die ganze Wendung ist das Wort',
    t2ab='<em>In terms of</em>, <em>on behalf of</em>, <em>in spite of</em> '
         '&mdash; das sind einzelne Vokabeln, die zufällig drei Wörter lang '
         'sind. Nichts darin wird gewählt.',
    t2an='Lerne sie als Ganzes, so wie du <em>however</em> oder '
         '<em>nevertheless</em> lernst.',
    t2bh='Von Präpositionen eingerahmt',
    t2bb='Die meisten haben an jedem Ende eine Präposition: <em>on</em> the verge '
         '<em>of</em>, <em>at</em> the expense <em>of</em>, <em>for</em> the sake '
         '<em>of</em>. Fehlt eine, funktioniert die Wendung nicht mehr.',
    t2bn='Gefragt ist meist die erste, denn die zweite ist fast immer '
         '<em>of</em>.',
    t2ch='Sie markieren das Register',
    t2cb='Diese Gruppe gehört zum formellen und geschriebenen Englisch &mdash; '
         'Berichte, Reden, Besprechungen. Sie zu benutzen gehört dazu, wenn man '
         'nach B2 statt B1 klingen will.',
    t2cn='<em>In spite of</em> und <em>despite</em> bedeuten dasselbe; '
         '<em>despite</em> steht ohne <em>of</em>.',

    t3Eyebrow='Bevor du anfängst',
    t3Title='Verben und Adjektive, die ihre Präposition mitbringen',
    t3ah='Gleiche Idee, andere Präposition',
    t3ab='Das Muster ist <em>accuse someone of</em> etwas, aber <em>blame '
         'someone for</em> etwas. Die Bedeutungen liegen '
         'nah beieinander, die Präpositionen sind nicht austauschbar.',
    t3an='Das ist das Paar, das auf B2 am häufigsten danebengeht.',
    t3bh='Drei mit Person und Sache',
    t3bb='<em>Prevent</em> jemanden <em>from</em> etwas zu tun, '
         '<em>congratulate</em> jemanden <em>on</em> etwas, <em>succeed in</em> '
         'etwas zu tun. Jedes hat genau eine Präposition.',
    t3bn='Nach <em>succeed in</em> und <em>prevent from</em> steht immer eine '
         '<em>-ing</em>-Form, nie ein Infinitiv.',
    t3ch='Woraus Dinge bestehen',
    t3cb='<em>Consist of</em> zählt die Teile auf; <em>specialise in</em> nennt '
         'das Fachgebiet. <em>Consist of</em> hat kein Passiv &mdash; nichts '
         '„is consisted of“.',
    t3cn='<em>Comprise</em> heißt dasselbe wie <em>consist of</em> und steht '
         'ganz ohne Präposition.',

    t4Eyebrow='Bevor du anfängst',
    t4Title='Phrasal Verbs, bei denen die Präposition die Bedeutung ist',
    t4ah='Drei Wörter, ein Verb',
    t4ab='<em>Look up to</em>, <em>look down on</em>, <em>put up with</em>, '
         '<em>come up with</em>. Die ganze Kette ist das Verb; kein Teil davon '
         'lässt sich ändern oder verschieben.',
    t4an='Das Objekt steht immer nach der vollständigen Wendung: put up with '
         '<em>the noise</em>.',
    t4bh='Die Richtung trägt die Bedeutung',
    t4bb='Look <em>up to</em> jemanden heißt, ihn zu bewundern; look <em>down '
         'on</em> jemanden heißt, sich über ihn zu stellen. Eine Partikel '
         'Unterschied, gegenteilige Bedeutung.',
    t4bn='Hier überlebt das wörtliche Bild, was dieses Paar ungewöhnlich leicht '
         'merkbar macht.',
    t4ch='Nichts zu erschließen',
    t4cb='<em>Get away with</em> heißt, ohne Folgen davonzukommen, <em>stand up '
         'for</em> heißt verteidigen, <em>cut down on</em> heißt reduzieren. '
         'Keines davon lässt sich aus den Teilen ableiten.',
    t4cn='Genau diese lassen Gesprochenes natürlich klingen, deshalb lohnt sich '
         'das Auswendiglernen.',

    mcaEyebrow='Übung 1 · Zweck', mcaTitle='For oder to?',
    mcbEyebrow='Übung 2 · Feste Wendungen', mcbTitle='Vervollständige den Ausdruck',
    mccEyebrow='Übung 3 · Abhängige Paare',
    mccTitle='Welche Präposition nimmt das Wort?',
    mcdEyebrow='Übung 4 · Phrasal Verbs', mcdTitle='Vervollständige das Phrasal Verb',

    q1why='<strong>For.</strong> Die Stiefel sind eine Sache mit einer Funktion, '
          'und eine Funktion nimmt <em>for</em> plus Substantiv oder '
          '<em>-ing</em>-Form.',
    q2why='<strong>To.</strong> Hier handelt eine Person mit einem Ziel, und ein '
          'Ziel nimmt <em>to</em> plus Infinitiv &mdash; to get fit.',
    q3why='<strong>For.</strong> Das Konto ist eine Sache mit einem '
          'Verwendungszweck, also <em>for paying</em>, nicht <em>to paying</em>.',
    q4why='<strong>To.</strong> Er ist eine Person mit einem Grund, zwei Jobs zu '
          'machen. <em>To support</em> nennt diesen Grund.',
    q5why='<strong>For.</strong> Der Aufsatz ist ein Werkzeug, und wofür ein '
          'Werkzeug da ist, steht mit <em>for</em> plus <em>-ing</em>.',
    q6why='<strong>To.</strong> Sie kamen früh, um etwas zu erreichen. Das ist '
          'eine Person mit einem Ziel, also <em>to get</em>.',
    q7why='<strong>For.</strong> Die Creme ist ein Produkt mit erklärtem Zweck. '
          '<em>Specifically for reducing</em> nennt, was sie leisten soll.',

    q8why='<strong>On.</strong> <em>Depend on</em> ist fest und nimmt keine '
          'andere Präposition. <em>Rely on</em> verhält sich genauso.',
    q9why='<strong>Of.</strong> <em>In terms of</em> führt den Aspekt ein, um den '
          'es gerade geht &mdash; hier das Gehalt und nichts anderes.',
    q10why='<strong>On.</strong> <em>On behalf of</em> heißt, als Vertretung '
           'einer anderen Person zu sprechen oder zu handeln.',
    q11why='<strong>In.</strong> <em>In spite of</em> leitet einen Gegensatz ein. '
           '<em>Despite</em> heißt dasselbe und steht ohne <em>of</em>.',
    q12why='<strong>On.</strong> <em>On the verge of</em> heißt kurz davor, dass '
           'etwas passiert &mdash; fast immer etwas Schlechtes.',
    q13why='<strong>At.</strong> <em>At the expense of</em> heißt, dass der '
           'Gewinn zulasten von jemandem oder etwas anderem ging.',
    q14why='<strong>For.</strong> <em>For the sake of</em> nennt die Person oder '
           'den Grund, für die etwas getan wird &mdash; hier die Kinder.',

    q15why='<strong>Of.</strong> Das Muster ist <em>accuse someone of '
           'something</em>. <em>Blame</em> ist das nahe Synonym, das stattdessen '
           '<em>for</em> nimmt.',
    q16why='<strong>For.</strong> Das Muster ist <em>blame someone for '
           'something</em>. <em>Accuse</em>, bedeutungsnah, nimmt dagegen '
           '<em>of</em>.',
    q17why='<strong>In.</strong> <em>Succeed in doing something</em> ist fest, '
           'und danach steht immer eine <em>-ing</em>-Form, nie ein Infinitiv.',
    q18why='<strong>From.</strong> <em>Prevent someone from doing something</em> '
           'ist fest und nimmt ebenfalls eine <em>-ing</em>-Form.',
    q19why='<strong>On.</strong> <em>Congratulate someone on something</em> ist '
           'das feste Muster &mdash; on a promotion, on passing an exam.',
    q20why='<strong>In.</strong> <em>Specialise in something</em> benennt ein '
           'Fachgebiet oder eine Spezialisierung.',
    q21why='<strong>Of.</strong> <em>Consist of</em> zählt auf, woraus etwas '
           'besteht. Ein Passiv gibt es nicht &mdash; nichts „is consisted of“.',

    q22why='<strong>To.</strong> <em>Look up to someone</em> heißt, jemanden zu '
           'bewundern und zu achten. Das Gegenteil, <em>look down on</em>, ist '
           'eine Partikel entfernt.',
    q23why='<strong>With.</strong> <em>Put up with something</em> heißt, etwas '
           'ohne Klagen hinzunehmen. Alle drei Wörter gehören zum Verb.',
    q24why='<strong>With.</strong> <em>Get away with something</em> heißt, der '
           'Strafe oder den Folgen dafür zu entgehen.',
    q25why='<strong>With.</strong> <em>Come up with something</em> heißt, eine '
           'Idee oder einen Plan hervorzubringen &mdash; das Objekt folgt der '
           'ganzen Wendung.',
    q26why='<strong>On.</strong> <em>Look down on someone</em> heißt, sich für '
           'besser zu halten als die Person. Vergleiche <em>look up to</em>.',
    q27why='<strong>For.</strong> <em>Stand up for something</em> heißt, eine '
           'Überzeugung oder ein Prinzip zu verteidigen, oft um einen Preis.',
    q28why='<strong>On.</strong> <em>Cut down on something</em> heißt, die Menge '
           'davon zu verringern, die man konsumiert oder tut.',

    resPerfect='Volle Punktzahl. Zweck, feste Wendungen, abhängige Paare und '
               'Phrasal Verbs — alles im Griff.',
    resStrong='Starke Leistung. Sieh dir die Trennung von for und to noch einmal '
              'an — dort geht meist der letzte Punkt verloren.',
    resMid='Eine gute Grundlage. Geh zurück zur Folie über feste Wendungen: die '
           'werden als Ganzes gelernt, nicht zusammengesetzt.',
    resLow='Lies die vier Lernfolien noch einmal und versuch es erneut. Nichts '
           'aus dieser Gruppe lässt sich aus den Teilen erschließen.',

    actTitle='Vertritt deine Position',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Eine Abteilung soll gestrichen werden. Eine Person spricht für '
                  'die Belegschaft, die andere für die Geschäftsführung. Fünf '
                  'Minuten pro Seite, dann tauscht die Rollen und argumentiert '
                  'das Gegenteil.',
    actSpeak1='Sprich <em>on behalf of</em> dein Team und sag, was die '
              'Entscheidung kosten würde — <em>in terms of</em> Moral und nicht '
              'nur Geld.',
    actSpeak2='Räume einen Punkt ein — etwas, das du <em>put up with</em> '
              'musstest — und <em>come up with</em> dann eine Alternative.',
    actSpeak3='Argumentiere, dass die Einsparung <em>at the expense of</em> '
              'etwas geht, auf das das Unternehmen nicht verzichten kann.',
    actWriteKind='Schreiben · 180–250 Wörter',
    actWriteBrief='Schreib die E-Mail, die deine Seite danach verschickt: was '
                  'vereinbart wurde, was offen bleibt und worum ihr als Nächstes '
                  'bittet. Sie geht an Leute, die nicht im Raum waren, also darf '
                  'nichts unausgesprochen bleiben. Verwende mindestens drei der '
                  'Ausdrücke oben.',
    actPlaceholder='Following this morning’s meeting…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Preposiciones <em>avanzadas</em>',
    coverSub='Finalidad, expresiones fijas, parejas dependientes y los phrasal '
             'verbs que las sostienen',
    chipLevel='B2 · Intermedio alto', chipFocus='Preposiciones',
    chipCount='28 preguntas',

    t1Eyebrow='Antes de empezar',
    t1Title='Finalidad: para qué sirve algo, por qué actúa alguien',
    t1ah='For + sustantivo o -ing',
    t1ab='<strong>For</strong> nombra la <em>función</em> de una cosa. Unas botas '
         '<em>for walking</em>, una cuenta <em>for paying fees</em>, una crema '
         '<em>for reducing lines</em>.',
    t1an='Detrás va un sustantivo o una forma en <em>-ing</em>, nunca un '
         'infinitivo sin <em>to</em>.',
    t1bh='To + infinitivo',
    t1bb='<strong>To</strong> da el <em>motivo</em> por el que una persona hace '
         'algo. I go to the gym <em>to get fit</em>; she took the early train <em>to '
         'avoid the queues</em>.',
    t1bn='<em>In order to</em> es lo mismo, un registro más formal. No existe un '
         '<em>in order for</em> equivalente.',
    t1ch='La prueba que funciona',
    t1cb='Lee lo que va después del hueco, no quién es el sujeto. <em>For</em> '
         'lleva un sustantivo o una forma en <em>-ing</em>; <em>to</em> lleva '
         'el infinitivo sin más. Esa prueba nunca falla.',
    t1cn='El hueco describe la función de una cosa o el objetivo de una acción '
         '&mdash; en los dos casos el sujeto puede ser una persona.',

    t2Eyebrow='Antes de empezar',
    t2Title='Expresiones fijas: la preposición no es un hueco',
    t2ah='La expresión entera es la palabra',
    t2ab='<em>In terms of</em>, <em>on behalf of</em>, <em>in spite of</em> '
         '&mdash; son piezas de vocabulario que casualmente tienen tres '
         'palabras. Dentro no se elige nada.',
    t2an='Apréndelas enteras, igual que aprendes <em>however</em> o '
         '<em>nevertheless</em>.',
    t2bh='Con preposición a cada lado',
    t2bb='La mayoría lleva una preposición en cada extremo: <em>on</em> the verge '
         '<em>of</em>, <em>at</em> the expense <em>of</em>, <em>for</em> the sake '
         '<em>of</em>. Si falta una, la expresión deja de funcionar.',
    t2bn='La que se pregunta suele ser la primera, porque la segunda es casi '
         'siempre <em>of</em>.',
    t2ch='Marcan el registro',
    t2cb='Este grupo pertenece al inglés formal y escrito &mdash; informes, '
         'discursos, reuniones. Usarlas forma parte de sonar a B2 y no a B1.',
    t2cn='<em>In spite of</em> y <em>despite</em> significan lo mismo; '
         '<em>despite</em> va sin <em>of</em>.',

    t3Eyebrow='Antes de empezar',
    t3Title='Verbos y adjetivos que traen su preposición',
    t3ah='Misma idea, distinta preposición',
    t3ab='El patrón es <em>accuse someone of</em> algo, pero <em>blame someone '
         'for</em> algo. Los significados están cerca; las '
         'preposiciones no son intercambiables.',
    t3an='Es la pareja que más se falla en B2.',
    t3bh='Tres que llevan persona y cosa',
    t3bb='<em>Prevent</em> a alguien <em>from</em> hacer algo, '
         '<em>congratulate</em> a alguien <em>on</em> algo, <em>succeed in</em> '
         'hacer algo. Cada uno tiene exactamente una preposición.',
    t3bn='Tras <em>succeed in</em> y <em>prevent from</em> siempre va una forma '
         'en <em>-ing</em>, nunca un infinitivo.',
    t3ch='De qué están hechas las cosas',
    t3cb='<em>Consist of</em> enumera las partes; <em>specialise in</em> nombra '
         'el campo. <em>Consist of</em> no tiene pasiva &mdash; nada "is '
         'consisted of".',
    t3cn='<em>Comprise</em> significa lo mismo que <em>consist of</em> y no '
         'lleva preposición alguna.',

    t4Eyebrow='Antes de empezar',
    t4Title='Phrasal verbs donde la preposición es el significado',
    t4ah='Tres palabras, un verbo',
    t4ab='<em>Look up to</em>, <em>look down on</em>, <em>put up with</em>, '
         '<em>come up with</em>. La cadena entera es el verbo; ninguna parte se '
         'puede cambiar ni mover.',
    t4an='El objeto va siempre detrás de la expresión completa: put up with '
         '<em>the noise</em>.',
    t4bh='La dirección lleva el significado',
    t4bb='Look <em>up to</em> a alguien es admirarlo; look <em>down on</em> a '
         'alguien es creerse superior. Una partícula de diferencia, significado '
         'contrario.',
    t4bn='Aquí sobrevive la imagen literal, lo que hace esta pareja '
         'excepcionalmente fácil de recordar.',
    t4ch='Nada que deducir',
    t4cb='<em>Get away with</em> es librarse de las consecuencias, <em>stand up '
         'for</em> es defender, <em>cut down on</em> es reducir. Ninguno se '
         'deduce de sus partes.',
    t4cn='Son justo los que hacen que el habla suene natural, así que merece la '
         'pena memorizarlos.',

    mcaEyebrow='Actividad 1 · Finalidad', mcaTitle='¿For o to?',
    mcbEyebrow='Actividad 2 · Expresiones fijas',
    mcbTitle='Completa la expresión',
    mccEyebrow='Actividad 3 · Parejas dependientes',
    mccTitle='¿Qué preposición lleva la palabra?',
    mcdEyebrow='Actividad 4 · Phrasal verbs',
    mcdTitle='Completa el phrasal verb',

    q1why='<strong>For.</strong> Las botas son una cosa con una función, y una '
          'función lleva <em>for</em> más sustantivo o forma en <em>-ing</em>. En '
          'español, "para andar".',
    q2why='<strong>To.</strong> Aquí una persona actúa con un objetivo, y un '
          'objetivo lleva <em>to</em> más infinitivo &mdash; to get fit, "para '
          'ponerse en forma".',
    q3why='<strong>For.</strong> La cuenta es una cosa con un uso previsto, así '
          'que <em>for paying</em>, no <em>to paying</em>.',
    q4why='<strong>To.</strong> Él es una persona con un motivo para trabajar en '
          'dos empleos. <em>To support</em> da ese motivo.',
    q5why='<strong>For.</strong> El accesorio es una herramienta, y para qué '
          'sirve una herramienta se dice con <em>for</em> más <em>-ing</em>.',
    q6why='<strong>To.</strong> Llegaron pronto para conseguir algo. Es una '
          'persona con un objetivo, así que <em>to get</em>.',
    q7why='<strong>For.</strong> La crema es un producto con una finalidad '
          'declarada. <em>Specifically for reducing</em> dice qué se supone que '
          'hace.',

    q8why='<strong>On.</strong> <em>Depend on</em> es fija y no admite otra '
          'preposición. <em>Rely on</em> funciona igual.',
    q9why='<strong>Of.</strong> <em>In terms of</em> introduce el aspecto del que '
          'se habla &mdash; aquí el salario y no otra cosa. Equivale a "en '
          'cuanto a".',
    q10why='<strong>On.</strong> <em>On behalf of</em> significa hablar o actuar '
           'en representación de otros: "en nombre de".',
    q11why='<strong>In.</strong> <em>In spite of</em> introduce un contraste, "a '
           'pesar de". <em>Despite</em> significa lo mismo y va sin <em>of</em>.',
    q12why='<strong>On.</strong> <em>On the verge of</em> significa "a punto de", '
           'muy cerca de que algo ocurra &mdash; casi siempre algo malo.',
    q13why='<strong>At.</strong> <em>At the expense of</em> significa "a costa '
           'de": la ganancia ha perjudicado a otra persona o cosa.',
    q14why='<strong>For.</strong> <em>For the sake of</em> nombra la persona o el '
           'motivo por el que se hace algo &mdash; "por el bien de", aquí los '
           'hijos.',

    q15why='<strong>Of.</strong> El patrón es <em>accuse someone of something</em>, '
           '"acusar a alguien de algo". <em>Blame</em>, tan parecido, lleva '
           '<em>for</em>.',
    q16why='<strong>For.</strong> El patrón es <em>blame someone for something</em>, '
           '"culpar a alguien por algo". <em>Accuse</em>, en cambio, lleva '
           '<em>of</em>.',
    q17why='<strong>In.</strong> <em>Succeed in doing something</em> es fijo, y '
           'detrás va siempre una forma en <em>-ing</em>, nunca un infinitivo.',
    q18why='<strong>From.</strong> <em>Prevent someone from doing something</em> '
           'es fijo y también lleva una forma en <em>-ing</em>.',
    q19why='<strong>On.</strong> <em>Congratulate someone on something</em> es el '
           'patrón fijo &mdash; "felicitar a alguien por algo".',
    q20why='<strong>In.</strong> <em>Specialise in something</em> nombra un campo '
           'profesional o una especialidad.',
    q21why='<strong>Of.</strong> <em>Consist of</em> enumera de qué está compuesto '
           'algo. No tiene pasiva &mdash; nada "is consisted of".',

    q22why='<strong>To.</strong> <em>Look up to someone</em> es admirar y respetar '
           'a alguien. Su contrario, <em>look down on</em>, está a una partícula '
           'de distancia.',
    q23why='<strong>With.</strong> <em>Put up with something</em> es aguantar algo '
           'sin quejarse. Las tres palabras forman el verbo.',
    q24why='<strong>With.</strong> <em>Get away with something</em> es librarse '
           'del castigo o de las consecuencias.',
    q25why='<strong>With.</strong> <em>Come up with something</em> es idear o '
           'proponer algo &mdash; el objeto va detrás de toda la expresión.',
    q26why='<strong>On.</strong> <em>Look down on someone</em> es creerse mejor '
           'que esa persona. Compara <em>look up to</em>.',
    q27why='<strong>For.</strong> <em>Stand up for something</em> es defender una '
           'idea o un principio, a menudo pagando un precio.',
    q28why='<strong>On.</strong> <em>Cut down on something</em> es reducir la '
           'cantidad que consumes o que haces.',

    resPerfect='Puntuación perfecta. Finalidad, expresiones fijas, parejas '
               'dependientes y phrasal verbs — todo controlado.',
    resStrong='Muy bien. Vuelve a mirar la separación entre for y to — ahí suele '
              'irse el último punto.',
    resMid='Buena base. Vuelve a la diapositiva de expresiones fijas: se '
           'aprenden enteras, no se montan.',
    resLow='Lee otra vez las cuatro diapositivas de enseñanza y prueba de nuevo. '
           'Nada de este grupo se deduce de sus partes.',

    actTitle='Defiende tu postura',
    actUse='Usa al menos tres:',
    actSpeakBrief='Van a suprimir un departamento. Una persona habla por la '
                  'plantilla y la otra por la dirección. Cinco minutos cada '
                  'lado, luego cambiad los papeles y defended lo contrario.',
    actSpeak1='Habla <em>on behalf of</em> tu equipo y di qué costaría la '
              'decisión, <em>in terms of</em> moral y no solo de dinero.',
    actSpeak2='Concede un punto — algo que has tenido que <em>put up with</em> — '
              'y después <em>come up with</em> una alternativa.',
    actSpeak3='Defiende que el ahorro sale <em>at the expense of</em> algo que la '
              'empresa no puede permitirse perder.',
    actWriteKind='Escritura · 180–250 palabras',
    actWriteBrief='Escribe el correo que envía tu parte después: qué se acordó, '
                  'qué queda abierto y qué pedís a continuación. Va dirigido a '
                  'gente que no estaba en la sala, así que nada puede quedar '
                  'sobrentendido. Usa al menos tres de las expresiones '
                  'anteriores.',
    actPlaceholder='Following this morning’s meeting…',
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
