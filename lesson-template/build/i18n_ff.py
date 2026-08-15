# -*- coding: utf-8 -*-
s = open('/tmp/ff_stage1.html', encoding='utf-8').read()
BLOCK = """const UI_I18N = {
  en: {
    /* ── chrome ── */
    btnStart:'Begin →', btnCheck:'Check', btnNext:'Next →', btnRestart:'Start again',
    orderHint:'Click the parts in order · click one again to take it back',
    scoreLabel:'Score', slideOf:(a,b)=>`${a} / ${b}`,
    fbCorrect:'Correct.', fbWrong:'Not quite.', fbAnswer:'Answer:',
    resNext:'Recognising the language is half of it. Now produce it →',
    actEyebrow:'Activation', actTitle:'Put it to work',
    actUse:'Use at least three:',
    actSpeakKind:'Discussion · in pairs', actWriteKind:'Writing · 150–200 words',
    actSpeakBrief:'No right or wrong answers here. Speak freely, and use as many of these forms as you can.',
    actSpeak1:'What did you absolutely have to get done this week — and what did you not have to do after all?',
    actSpeak2:'Describe a typical shift at the station. What does a firefighter have to do, and what must they never do?',
    actSpeak3:'Think of a time you had to make a fast decision. Looking back, what should you have done differently?',
    actWriteBrief:'Write a short report of one shift or one call-out. Use at least one past form, one rule, one future obligation and one regret.',
    actPlaceholder:'Write your response here…',
    btnCopy:'Copy', btnCopied:'Copied',
    wordCount:(n)=>`${n} ${n===1?'word':'words'}`,
    resPerfect:'Flawless. Every single one.',
    resStrong:'Strong work — the rule has landed.',
    resMid:'Solid start. Worth one more pass.',
    resLow:'Review the language focus slides, then try again.',
    /* ── content ── */
    coverTitle:'Must &amp; <em>Have To</em>',
    coverSub:'English for German firefighters — every tense, from the shift you had to work to the call you should have taken',
    chipLevel:'B1–B2', chipFocus:'Modals of obligation', chipCount:'17 questions',
    gapT:'Complete the sentence',

    t1e:'Language focus · 1 of 6', t1t:'Whose obligation is it?',
    t1a:'<strong>Must</strong> comes from inside the speaker — your own conviction, your own decision, or an order you are giving. <em>I must train harder. You must leave now.</em>',
    t1b:'<strong>Have to</strong> comes from outside — a regulation, a rota, a rank above you. <em>All firefighters have to wear a helmet on site.</em>',
    t1n:'Both translate <em>müssen</em>. English makes you say where the pressure is coming from, and German does not — which is why this is the hard one.',

    t2e:'Language focus · 2 of 6', t2t:'Must has no past',
    t2a:'There is no past form of <strong>must</strong>. <em>I must go yesterday</em> is not a sentence. The past of both <em>must</em> and <em>have to</em> is <strong>had to</strong>.',
    t2b:'For the present perfect, <em>have to</em> behaves like any other verb: <strong>has had to</strong> / <strong>have had to</strong>. <em>He has had to do overtime twice this week.</em>',
    t2n:'<em>Wir mussten evakuieren</em> → <em>We had to evacuate.</em> Never <em>we musted</em>, never <em>we must evacuated</em>.',

    t3e:'Language focus · 3 of 6', t3t:'Forbidden is not the same as unnecessary',
    t3a:'<strong>Must not</strong> = <em>darf nicht</em>. It forbids. <em>You must not enter that building.</em>',
    t3b:'<strong>Don\\'t have to</strong> = <em>braucht nicht</em>. It releases you. <em>He doesn\\'t have to attend the meeting.</em>',
    t3n:'This is the most expensive mistake on the list. Telling a colleague they <em>must not</em> come, when you meant they need not, changes an invitation into a ban.',

    t4e:'Language focus · 4 of 6', t4t:'The future splits the same way',
    t4a:'A decision you have made yourself keeps <strong>must</strong>. <em>I must go to the gym next week — I have decided.</em>',
    t4b:'An obligation arriving from outside takes <strong>will have to</strong>. <em>The new regulation starts next month; everyone will have to follow it.</em>',
    t4n:'<em>Wird … müssen</em> is almost always <strong>will have to</strong>. If you can point at the rule, use it.',

    t5e:'Language focus · 5 of 6', t5t:'Looking back at what went wrong',
    t5a:'<strong>Should have</strong> + past participle — the right thing, which did not happen. <em>You should have raised the alarm earlier.</em><br><strong>Shouldn\\'t have</strong> — the wrong thing, which did. <em>He shouldn\\'t have entered that building.</em>',
    t5b:'<strong>Needn\\'t have</strong> + past participle — something unnecessary that was done anyway. <em>You needn\\'t have stayed all night.</em> You did stay; it simply was not needed.',
    t5n:'All three are <em>hätte(n) … sollen</em> territory: a regret or a criticism, aimed at a past that cannot be changed.',

    t6e:'Language focus · 6 of 6', t6t:'If it were bigger',
    t6a:'An unreal condition makes the obligation unreal too: <strong>would have to</strong>. <em>If the fire were bigger, you would have to evacuate the whole area.</em>',
    t6b:'The <em>if</em> is often invisible. <em>Without the new vehicle, we would have to wait much longer</em> — <em>ohne …</em> is doing the same work as an <em>if</em>-clause.',
    t6n:'Konjunktiv II, in one phrase: <em>müsste</em> → <strong>would have to</strong>.',

    a1e1:'Activity 1 · The past — 1/2', a1e2:'Activity 1 · The past — 2/2',
    a2e1:'Activity 2 · The present — 1/2', a2e2:'Activity 2 · The present — 2/2',
    a3e1:'Activity 3 · The future — 1/2', a3e2:'Activity 3 · The future — 2/2',
    a4e1:'Activity 4 · Regret &amp; criticism — 1/3', a4e2:'Activity 4 · Regret &amp; criticism — 2/3',
    a4e3:'Activity 4 · Regret &amp; criticism — 3/3',
    a5e1:'Activity 5 · Conditional'
  },
  de: {
    btnStart:'Beginnen →', btnCheck:'Prüfen', btnNext:'Weiter →', btnRestart:'Neu starten',
    orderHint:'Klicke die Teile der Reihe nach an · nochmal klicken nimmt einen zurück',
    scoreLabel:'Punkte', slideOf:(a,b)=>`${a} / ${b}`,
    fbCorrect:'Richtig.', fbWrong:'Nicht ganz.', fbAnswer:'Antwort:',
    resNext:'Die Sprache zu erkennen ist die halbe Miete. Jetzt anwenden →',
    actEyebrow:'Anwendung', actTitle:'In die Praxis bringen',
    actUse:'Verwende mindestens drei:',
    actSpeakKind:'Diskussion · zu zweit', actWriteKind:'Schreiben · 150–200 Wörter',
    actSpeakBrief:'Hier gibt es kein Richtig oder Falsch. Sprich frei und verwende so viele dieser Formen wie möglich.',
    actSpeak1:'Was musstest du diese Woche unbedingt erledigen — und was hättest du am Ende doch nicht tun müssen?',
    actSpeak2:'Beschreibe eine typische Schicht auf der Wache. Was muss eine Feuerwehrfrau tun, und was darf sie auf keinen Fall tun?',
    actSpeak3:'Denk an eine Situation, in der du schnell entscheiden musstest. Was hättest du im Rückblick anders machen sollen?',
    actWriteBrief:'Schreibe einen kurzen Bericht über eine Schicht oder einen Einsatz. Verwende mindestens eine Vergangenheitsform, eine Vorschrift, eine Zukunftspflicht und ein Bedauern.',
    actPlaceholder:'Schreibe hier deine Antwort…',
    btnCopy:'Kopieren', btnCopied:'Kopiert',
    wordCount:(n)=>`${n} ${n===1?'Wort':'Wörter'}`,
    resPerfect:'Makellos. Alles richtig.',
    resStrong:'Starke Leistung — die Regel sitzt.',
    resMid:'Guter Anfang. Ein weiterer Durchgang lohnt sich.',
    resLow:'Sieh dir die Erklärungsfolien noch einmal an und versuche es erneut.',
    coverTitle:'Must &amp; <em>Have To</em>',
    coverSub:'Englisch für deutsche Feuerwehrleute — alle Zeiten, von der Schicht, die du machen musstest, bis zum Anruf, den du hättest annehmen sollen',
    chipLevel:'B1–B2', chipFocus:'Modalverben der Pflicht', chipCount:'17 Fragen',
    gapT:'Vervollständige den Satz',

    t1e:'Sprachlicher Schwerpunkt · 1 von 6', t1t:'Wessen Pflicht ist es?',
    t1a:'<strong>Must</strong> kommt von innen — deine eigene Überzeugung, dein eigener Entschluss oder ein Befehl, den du gibst. <em>I must train harder. You must leave now.</em>',
    t1b:'<strong>Have to</strong> kommt von außen — eine Vorschrift, ein Dienstplan, ein Vorgesetzter. <em>All firefighters have to wear a helmet on site.</em>',
    t1n:'Beides heißt <em>müssen</em>. Das Englische zwingt dich zu sagen, woher der Druck kommt — das Deutsche nicht. Genau das macht es schwer.',

    t2e:'Sprachlicher Schwerpunkt · 2 von 6', t2t:'Must hat keine Vergangenheit',
    t2a:'Es gibt keine Vergangenheitsform von <strong>must</strong>. <em>I must go yesterday</em> ist kein Satz. Die Vergangenheit von <em>must</em> und <em>have to</em> lautet <strong>had to</strong>.',
    t2b:'Im Present Perfect verhält sich <em>have to</em> wie jedes andere Verb: <strong>has had to</strong> / <strong>have had to</strong>. <em>He has had to do overtime twice this week.</em>',
    t2n:'<em>Wir mussten evakuieren</em> → <em>We had to evacuate.</em> Niemals <em>we musted</em>, niemals <em>we must evacuated</em>.',

    t3e:'Sprachlicher Schwerpunkt · 3 von 6', t3t:'Verboten ist nicht dasselbe wie unnötig',
    t3a:'<strong>Must not</strong> = <em>darf nicht</em>. Es verbietet. <em>You must not enter that building.</em>',
    t3b:'<strong>Don\\'t have to</strong> = <em>braucht nicht</em>. Es befreit. <em>He doesn\\'t have to attend the meeting.</em>',
    t3n:'Das ist der teuerste Fehler auf dieser Liste. Wer einem Kollegen sagt, er <em>must not</em> kommen, obwohl er nicht kommen <em>muss</em>, macht aus einer Einladung ein Verbot.',

    t4e:'Sprachlicher Schwerpunkt · 4 von 6', t4t:'Die Zukunft teilt sich genauso',
    t4a:'Ein selbst gefasster Entschluss behält <strong>must</strong>. <em>I must go to the gym next week — I have decided.</em>',
    t4b:'Eine Pflicht von außen nimmt <strong>will have to</strong>. <em>The new regulation starts next month; everyone will have to follow it.</em>',
    t4n:'<em>Wird … müssen</em> ist fast immer <strong>will have to</strong>. Wenn du auf die Vorschrift zeigen kannst, nimm es.',

    t5e:'Sprachlicher Schwerpunkt · 5 von 6', t5t:'Der Blick zurück auf das, was schiefging',
    t5a:'<strong>Should have</strong> + Partizip II — das Richtige, das nicht geschah. <em>You should have raised the alarm earlier.</em><br><strong>Shouldn\\'t have</strong> — das Falsche, das geschah. <em>He shouldn\\'t have entered that building.</em>',
    t5b:'<strong>Needn\\'t have</strong> + Partizip II — etwas Unnötiges, das trotzdem getan wurde. <em>You needn\\'t have stayed all night.</em> Du bist geblieben; nötig war es nicht.',
    t5n:'Alle drei sind <em>hätte(n) … sollen</em>: ein Bedauern oder ein Vorwurf, gerichtet auf eine Vergangenheit, die sich nicht mehr ändern lässt.',

    t6e:'Sprachlicher Schwerpunkt · 6 von 6', t6t:'Wenn er größer wäre',
    t6a:'Eine irreale Bedingung macht auch die Pflicht irreal: <strong>would have to</strong>. <em>If the fire were bigger, you would have to evacuate the whole area.</em>',
    t6b:'Das <em>if</em> ist oft unsichtbar. <em>Without the new vehicle, we would have to wait much longer</em> — <em>ohne …</em> leistet hier dasselbe wie ein <em>if</em>-Satz.',
    t6n:'Konjunktiv II in einer Wendung: <em>müsste</em> → <strong>would have to</strong>.',

    a1e1:'Aufgabe 1 · Vergangenheit — 1/2', a1e2:'Aufgabe 1 · Vergangenheit — 2/2',
    a2e1:'Aufgabe 2 · Gegenwart — 1/2', a2e2:'Aufgabe 2 · Gegenwart — 2/2',
    a3e1:'Aufgabe 3 · Zukunft — 1/2', a3e2:'Aufgabe 3 · Zukunft — 2/2',
    a4e1:'Aufgabe 4 · Vorwurf &amp; Bedauern — 1/3', a4e2:'Aufgabe 4 · Vorwurf &amp; Bedauern — 2/3',
    a4e3:'Aufgabe 4 · Vorwurf &amp; Bedauern — 3/3',
    a5e1:'Aufgabe 5 · Konjunktiv'
  },
  /* Fill these in later — English shows through until you do. */
  es:{}, fr:{}, it:{}, pt:{}, ru:{}, ar:{}, zh:{}, ja:{}
};"""
start = s.index('const UI_I18N = {')
end = s.index('};', s.index('es:{}, fr:{}')) + 2
s = s[:start] + BLOCK + s[end:]
open('/home/claude/forbes-english/english_firefighter_v3.html', 'w', encoding='utf-8').write(s)
print('written')
