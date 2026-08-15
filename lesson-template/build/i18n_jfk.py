# -*- coding: utf-8 -*-
s = open('/tmp/jfk_stage1.html', encoding='utf-8').read()

EN = """const UI_I18N = {
  en: {
    /* ── chrome ── */
    btnStart:'Begin →', btnCheck:'Check', btnNext:'Next →', btnRestart:'Start again',
    orderHint:'Click the parts in order · click one again to take it back',
    scoreLabel:'Score', slideOf:(a,b)=>`${a} / ${b}`,
    fbCorrect:'Correct.', fbWrong:'Not quite.', fbAnswer:'Answer:',
    resNext:'Recognising the language is half of it. Now produce it →',
    actEyebrow:'Activation', actTitle:'Put it to work',
    actUse:'Use at least three:',
    actSpeakKind:'Discussion · in pairs', actWriteKind:'Writing · 180–220 words',
    actSpeakBrief:'Sixty years on, the file is still open. Talk it through.',
    actSpeak1:'An archive is holding documents that have been kept from the public for decades. Argue for releasing them now — then argue for keeping them sealed.',
    actSpeak2:'Your partner says no official account of anything can ever be trusted. Take the opposite position.',
    actSpeak3:'Describe a place you know well so precisely that your partner could walk it: what sits where, and what moves along, across and through it.',
    actWriteBrief:'Write an account of a public event — real or invented — that was re-examined years later. Place it exactly: where, then where more precisely, then when.',
    actPlaceholder:'Write your response here…',
    btnCopy:'Copy', btnCopied:'Copied',
    wordCount:(n)=>`${n} ${n===1?'word':'words'}`,
    resPerfect:'Flawless. Every single one.',
    resStrong:'Strong work — the rule has landed.',
    resMid:'Solid start. Worth one more pass.',
    resLow:'Review the language focus slides, then try again.',
    /* ── content ── */
    coverTitle:'JFK &amp; <em>Prepositions</em>',
    coverSub:'The small words that put an event in a place, in a decade, and under suspicion',
    chipLevel:'B2 Upper-Intermediate', chipFocus:'Prepositions', chipCount:'15 questions',

    t1e:'Language focus · 1 of 3', t1t:'Where it happened',
    t1a:'English marks a named public space with <strong>in</strong> — <em>in Dealey Plaza</em>, <em>in Fort Worth</em>. <strong>Inside</strong> needs walls. <strong>Within</strong> is formal and draws a boundary.',
    t1b:'Movement takes its own preposition. <strong>Along</strong> follows the length of a road, <strong>across</strong> cuts from one side to the other, <strong>through</strong> goes in one side and out again.',
    t1n:'A motorcade travels <em>along</em> Elm Street. A bullet passes <em>through</em> a body. Same street, different geometry.',

    t2e:'Language focus · 2 of 3', t2t:'Under suspicion',
    t2a:'Some nouns take one preposition and no other. <strong>Under</strong> goes with examination and pressure: <em>under suspicion</em>, <em>under scrutiny</em>, <em>under investigation</em>.',
    t2b:'Others live inside the verb. <strong>Tamper with</strong>, <strong>act on your own</strong>, <strong>die in office</strong> — swap the preposition and the phrase breaks.',
    t2n:'These are not rules you work out. They are collocations you collect — and the wrong one is instantly audible.',

    t3e:'Language focus · 3 of 3', t3t:'Place, then time, then why',
    t3a:'When several prepositional phrases stack up, English orders them: <strong>place</strong> first, then the <strong>more specific place</strong>, then <strong>time</strong>.',
    t3b:'<em>Kennedy gave his final speech <strong>at the Hotel Texas</strong> <strong>in Fort Worth</strong> <strong>on the morning of his death</strong>.</em>',
    t3n:'Purpose (<em>to investigate the events</em>) and simultaneous action (<em>demanding a re-examination</em>) come last of all.',

    a1t:'Choose the best preposition',
    a1e1:'Activity 1 · Place &amp; movement — 1/5', a1e2:'Activity 1 · Place &amp; movement — 2/5',
    a1e3:'Activity 1 · Place &amp; movement — 3/5', a1e4:'Activity 1 · Place &amp; movement — 4/5',
    a1e5:'Activity 1 · Place &amp; movement — 5/5',

    a2t:'Complete the sentence',
    a2e1:'Activity 2 · Fixed collocations — 1/5', a2e2:'Activity 2 · Fixed collocations — 2/5',
    a2e3:'Activity 2 · Fixed collocations — 3/5', a2e4:'Activity 2 · Fixed collocations — 4/5',
    a2e5:'Activity 2 · Fixed collocations — 5/5',

    a3t:'Build the sentence',
    a3e1:'Activity 3 · Word order — 1/5', a3e2:'Activity 3 · Word order — 2/5',
    a3e3:'Activity 3 · Word order — 3/5', a3e4:'Activity 3 · Word order — 4/5',
    a3e5:'Activity 3 · Word order — 5/5'
  },
  de: {
    btnStart:'Beginnen →', btnCheck:'Prüfen', btnNext:'Weiter →', btnRestart:'Neu starten',
    orderHint:'Klicke die Teile der Reihe nach an · nochmal klicken nimmt einen zurück',
    scoreLabel:'Punkte', slideOf:(a,b)=>`${a} / ${b}`,
    fbCorrect:'Richtig.', fbWrong:'Nicht ganz.', fbAnswer:'Antwort:',
    resNext:'Die Sprache zu erkennen ist die halbe Miete. Jetzt anwenden →',
    actEyebrow:'Anwendung', actTitle:'In die Praxis bringen',
    actUse:'Verwende mindestens drei:',
    actSpeakKind:'Diskussion · zu zweit', actWriteKind:'Schreiben · 180–220 Wörter',
    actSpeakBrief:'Sechzig Jahre später ist die Akte immer noch offen. Sprecht darüber.',
    actSpeak1:'Ein Archiv hält Dokumente zurück, die der Öffentlichkeit jahrzehntelang vorenthalten wurden. Argumentiere zuerst für die sofortige Freigabe — dann dafür, sie weiter unter Verschluss zu halten.',
    actSpeak2:'Dein Gegenüber behauptet, keiner offiziellen Darstellung könne man je trauen. Vertritt die Gegenposition.',
    actSpeak3:'Beschreibe einen Ort, den du gut kennst, so genau, dass dein Gegenüber ihn abgehen könnte: was wo steht und was sich entlang, quer hindurch oder durch ihn bewegt.',
    actWriteBrief:'Schreibe den Bericht über ein öffentliches Ereignis — echt oder erfunden —, das Jahre später neu untersucht wurde. Verorte es genau: wo, dann genauer wo, dann wann.',
    actPlaceholder:'Schreibe hier deine Antwort…',
    btnCopy:'Kopieren', btnCopied:'Kopiert',
    wordCount:(n)=>`${n} ${n===1?'Wort':'Wörter'}`,
    resPerfect:'Makellos. Alles richtig.',
    resStrong:'Starke Leistung — die Regel sitzt.',
    resMid:'Guter Anfang. Ein weiterer Durchgang lohnt sich.',
    resLow:'Sieh dir die Erklärungsfolien noch einmal an und versuche es erneut.',
    coverTitle:'JFK &amp; <em>Präpositionen</em>',
    coverSub:'Die kleinen Wörter, die ein Ereignis an einen Ort, in ein Jahrzehnt und unter Verdacht stellen',
    chipLevel:'B2 Obere Mittelstufe', chipFocus:'Präpositionen', chipCount:'15 Fragen',

    t1e:'Sprachlicher Schwerpunkt · 1 von 3', t1t:'Wo es geschah',
    t1a:'Für einen benannten öffentlichen Platz nimmt das Englische <strong>in</strong> — <em>in Dealey Plaza</em>, <em>in Fort Worth</em>. <strong>Inside</strong> braucht Wände. <strong>Within</strong> ist förmlich und zieht eine Grenze.',
    t1b:'Bewegung hat ihre eigene Präposition. <strong>Along</strong> folgt der Länge einer Straße, <strong>across</strong> quert sie von einer Seite zur anderen, <strong>through</strong> geht auf einer Seite hinein und auf der anderen hinaus.',
    t1n:'Eine Wagenkolonne fährt <em>along</em> Elm Street. Eine Kugel geht <em>through</em> einen Körper. Dieselbe Straße, andere Geometrie.',

    t2e:'Sprachlicher Schwerpunkt · 2 von 3', t2t:'Unter Verdacht',
    t2a:'Manche Substantive nehmen genau eine Präposition und keine andere. <strong>Under</strong> steht bei Prüfung und Druck: <em>under suspicion</em>, <em>under scrutiny</em>, <em>under investigation</em>.',
    t2b:'Andere stecken im Verb selbst. <strong>Tamper with</strong>, <strong>act on your own</strong>, <strong>die in office</strong> — tausche die Präposition aus, und die Wendung zerbricht.',
    t2n:'Das sind keine Regeln, die man herleitet. Das sind Kollokationen, die man sammelt — und die falsche hört man sofort.',

    t3e:'Sprachlicher Schwerpunkt · 3 von 3', t3t:'Ort, dann Zeit, dann Zweck',
    t3a:'Stehen mehrere Präpositionalphrasen hintereinander, ordnet das Englische sie: zuerst der <strong>Ort</strong>, dann der <strong>genauere Ort</strong>, dann die <strong>Zeit</strong>.',
    t3b:'<em>Kennedy gave his final speech <strong>at the Hotel Texas</strong> <strong>in Fort Worth</strong> <strong>on the morning of his death</strong>.</em>',
    t3n:'Zweck (<em>to investigate the events</em>) und gleichzeitige Handlung (<em>demanding a re-examination</em>) stehen ganz am Schluss.',

    a1t:'Wähle die passende Präposition',
    a1e1:'Aufgabe 1 · Ort &amp; Bewegung — 1/5', a1e2:'Aufgabe 1 · Ort &amp; Bewegung — 2/5',
    a1e3:'Aufgabe 1 · Ort &amp; Bewegung — 3/5', a1e4:'Aufgabe 1 · Ort &amp; Bewegung — 4/5',
    a1e5:'Aufgabe 1 · Ort &amp; Bewegung — 5/5',

    a2t:'Vervollständige den Satz',
    a2e1:'Aufgabe 2 · Feste Wendungen — 1/5', a2e2:'Aufgabe 2 · Feste Wendungen — 2/5',
    a2e3:'Aufgabe 2 · Feste Wendungen — 3/5', a2e4:'Aufgabe 2 · Feste Wendungen — 4/5',
    a2e5:'Aufgabe 2 · Feste Wendungen — 5/5',

    a3t:'Baue den Satz',
    a3e1:'Aufgabe 3 · Satzstellung — 1/5', a3e2:'Aufgabe 3 · Satzstellung — 2/5',
    a3e3:'Aufgabe 3 · Satzstellung — 3/5', a3e4:'Aufgabe 3 · Satzstellung — 4/5',
    a3e5:'Aufgabe 3 · Satzstellung — 5/5'
  },
  /* Fill these in later — English shows through until you do. */
  es:{}, fr:{}, it:{}, pt:{}, ru:{}, ar:{}, zh:{}, ja:{}
};"""

start = s.index('const UI_I18N = {')
end = s.index('};', s.index('es:{}, fr:{}')) + 2
s = s[:start] + EN + s[end:]
open('/home/claude/forbes-english/jfk_prepositions_b2.html', 'w', encoding='utf-8').write(s)
print('written')
