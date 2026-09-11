# -*- coding: utf-8 -*-
"""Interface strings for Advanced Prepositions (B2) — Part 2.

English, German and Spanish, teach cards in the six-item form.

As with Part 1, the Spanish here is a full translation rather than the
unaccented footnote the source page carried — "disminucion", "comparacion",
"situacion dificil", "perdida" — but it keeps what that footnote did well,
which was naming the Spanish structure behind the English one.

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
    coverTitle='Advanced Prepositions <em>Part 2</em>',
    coverSub='The prepositions that carry figures, formal phrases and everyday '
             'phrasal verbs',
    chipLevel='B2 · Upper-intermediate', chipFocus='Prepositions',
    chipCount='28 questions',

    t1Eyebrow='Before you start',
    t1Title='Talking about figures: three words, three jobs',
    t1ah='In, of, by',
    t1ab='A rise <em>in</em> demand names <em>what</em> is growing. An increase '
         '<em>of</em> eight percent gives the <em>size</em>. Costs dropping '
         '<em>by</em> a fifth gives the size of the <em>change</em>.',
    t1an='All three can appear in one sentence, each doing a different job.',
    t1bh='From here to there',
    t1bb='<strong>From X to Y</strong> marks the two ends of a change &mdash; '
         'the fleet grew <em>from</em> nine vans <em>to</em> forty. The '
         'starting point comes first.',
    t1bn='The size of a change takes <em>by</em> after a verb (rose <em>by</em> '
         '500) and <em>of</em> after a noun (an increase <em>of</em> 500). '
         '<em>From&hellip;to</em> names the two ends instead.',
    t1ch='Comparing and qualifying',
    t1cb='<em>Compared to</em> sets two things side by side. <em>A shortage '
         'of</em> names what is missing. <em>With regard to</em> narrows to one '
         'aspect.',
    t1cn='<em>With regard to</em> is formal and singular &mdash; never <em>with '
         'regards to</em>, which is a sign-off.',

    t2Eyebrow='Before you start',
    t2Title='More fixed phrases, and the trap inside them',
    t2ah='The <em>in</em> family',
    t2ab='<em>In charge of</em>, <em>in favour of</em>, <em>in return for</em>, '
         '<em>in addition to</em>. Four phrases that all open with <em>in</em> '
         '&mdash; which is why the first half is rarely the difficult part.',
    t2an='If the phrase describes a role or a position, the odds favour '
         '<em>in</em>.',
    t2bh='States, not places',
    t2bb='<em>Out of the question</em>, <em>under control</em>, <em>beyond '
         'doubt</em>. Each describes a condition something is in, and none of '
         'them is literal.',
    t2bn='<em>Beyond</em> means past the point where it could be argued &mdash; '
         'the same <em>beyond</em> as in <em>beyond repair</em>.',
    t2ch='The tail is not always <em>of</em>',
    t2cb='In charge <em>of</em>, in favour <em>of</em>, but in return <em>for</em> '
         'and in addition <em>to</em>. Learning the opening preposition is only '
         'half the phrase.',
    t2cn='This is why they are memorised whole rather than by rule.',

    t3Eyebrow='Before you start',
    t3Title='More dependent pairs, including one real trap',
    t3ah='When <em>to</em> is not an infinitive',
    t3ab='You <em>object to</em> something, and that <em>to</em> is a preposition '
         '&mdash; so a verb after it takes <em>-ing</em>. The neighbours objected '
         '<em>to</em> the trees <em>being cut down</em>, never <em>to be cut '
         'down</em>.',
    t3an='The same trap sits inside <em>look forward to</em> and <em>be used '
         'to</em>.',
    t3bh='Trusting and mentioning',
    t3bb='<em>Rely on</em> someone to do something. <em>Refer to</em> something '
         'in a speech or a text. Both fixed, neither negotiable.',
    t3bn='<em>Refer to</em> also means "look something up", with the same '
         'preposition.',
    t3ch='Leaving, gaining, boasting',
    t3cb='You <em>resign from</em> a post and <em>benefit from</em> a scheme '
         '&mdash; both take <em>from</em>. You <em>boast about</em> something, '
         'and <em>excuse</em> someone <em>for</em> it.',
    t3cn='Two verbs sharing a preposition is the exception here, not the rule.',

    t4Eyebrow='Before you start',
    t4Title='Handling, recovering, delaying, bumping into',
    t4ah='Both take <em>with</em>',
    t4ab='You <em>deal with</em> a problem and you <em>cope with</em> pressure. '
         '<em>Deal with</em> is about solving it; <em>cope with</em> is about '
         'surviving it.',
    t4an='A manager deals with a conflict. The team copes with the workload.',
    t4bh='Getting past it, or putting it off',
    t4bb='<em>Get over</em> something is to recover from it emotionally. <em>Put '
         'off</em> something is to postpone it &mdash; and it is the decision, '
         'not the person, that gets put off.',
    t4bn='<em>Put someone off</em> exists too, and means to discourage them. '
         'Different verb.',
    t4ch='By chance, or behind',
    t4cb='<em>Come across</em> and <em>run into</em> both mean by chance. '
         '<em>Run into</em> is only used of people; <em>come across</em> is '
         'the usual one for things. <em>Fall behind</em> is to slip back '
         'against a plan.',
    t4cn='You come across a photo; you run into an old teacher.',

    mcaEyebrow='Activity 1 · Trends and quantity',
    mcaTitle='Which preposition carries the figure?',
    mcbEyebrow='Activity 2 · Fixed phrases', mcbTitle='Complete the expression',
    mccEyebrow='Activity 3 · Dependent pairs',
    mccTitle='Which preposition does the word take?',
    mcdEyebrow='Activity 4 · Phrasal verbs', mcdTitle='Finish the phrasal verb',

    q1why='<strong>In.</strong> <em>A rise in something</em> names the area that '
          'is growing &mdash; here, demand. The figure itself has not been given '
          'yet.',
    q2why='<strong>Of.</strong> <em>An increase of</em> plus an amount gives the '
          'exact size of the rise. Compare <em>an increase in revenue</em>, '
          'which names the area instead.',
    q3why='<strong>By.</strong> <em>Fall by</em> or <em>drop by</em> plus an '
          'amount states the size of the decrease &mdash; how much was lost, not '
          'what it fell to.',
    q4why='<strong>From.</strong> <em>Rise from X to Y</em> names the two ends '
          'of the change. A dated starting figure is an end point, not an '
          'increment, so it takes <em>from</em> rather than <em>by</em>.',
    q5why='<strong>To.</strong> <em>Compared to</em> introduces a direct '
          'comparison between two things.',
    q6why='<strong>Of.</strong> <em>A shortage of something</em> states exactly '
          'what is lacking &mdash; here, affordable housing.',
    q7why='<strong>With.</strong> <em>With regard to</em> is a formal fixed '
          'phrase meaning "concerning". It is singular: <em>with regards to</em> '
          'is a sign-off, not a preposition.',

    q8why='<strong>In.</strong> <em>In charge of something</em> means responsible '
          'for running it.',
    q9why='<strong>In.</strong> <em>In favour of something</em> means supporting '
          'it or agreeing with it.',
    q10why='<strong>In.</strong> <em>In return for something</em> means as an '
           'exchange for it. Note the tail is <em>for</em>, not <em>of</em>.',
    q11why='<strong>Of.</strong> <em>Out of the question</em> means completely '
           'impossible &mdash; a state, not a place.',
    q12why='<strong>Under.</strong> <em>Under control</em> means a difficult '
           'situation is being managed successfully.',
    q13why='<strong>Beyond.</strong> <em>Beyond doubt</em> means past the point '
           'where it could be argued &mdash; the same <em>beyond</em> as in '
           '<em>beyond repair</em>.',
    q14why='<strong>In.</strong> <em>In addition to something</em> means as well '
           'as it. The tail here is <em>to</em>, not <em>of</em>.',

    q15why='<strong>On.</strong> <em>Rely on someone</em> is to trust them to do '
           'what is needed. <em>Depend on</em> works the same way.',
    q16why='<strong>To.</strong> <em>Object to something</em> is to oppose it '
           '&mdash; and that <em>to</em> is a preposition, so a verb after it '
           'takes <em>-ing</em>: objected to the road <em>being built</em>.',
    q17why='<strong>For.</strong> <em>Excuse someone for something</em> is the '
           'formal apology pattern, and what follows takes <em>-ing</em>.',
    q18why='<strong>About.</strong> <em>Boast about something</em> is to speak '
           'proudly of it, sometimes more proudly than is welcome.',
    q19why='<strong>From.</strong> <em>Resign from a position</em> is to leave a '
           'job voluntarily. The preposition is <em>from</em>, never <em>of</em>.',
    q20why='<strong>To.</strong> <em>Refer to something</em> is to mention or '
           'allude to it. It also means to look something up.',
    q21why='<strong>From.</strong> <em>Benefit from something</em> is to gain an '
           'advantage from it &mdash; the same <em>from</em> as <em>resign '
           'from</em>.',

    q22why='<strong>With.</strong> <em>Deal with something</em> is to manage or '
           'resolve a problem &mdash; to actually settle it.',
    q23why='<strong>With.</strong> <em>Cope with something</em> is to handle a '
           'hard situation. Unlike <em>deal with</em>, it does not claim the '
           'problem is solved.',
    q24why='<strong>Over.</strong> <em>Get over something</em> is to recover '
           'emotionally from it &mdash; a loss, a shock, a disappointment.',
    q25why='<strong>Off.</strong> <em>Put off something</em> is to postpone it. '
           '<em>Put someone off</em> is a different verb meaning to discourage '
           'them.',
    q26why='<strong>Across.</strong> <em>Come across something</em> is to find it '
           'by chance. It is used for things; for people, use <em>run into</em>.',
    q27why='<strong>Into.</strong> <em>Run into someone</em> is to meet them '
           'unexpectedly. It is used for people; for things, use <em>come '
           'across</em>.',
    q28why='<strong>Behind.</strong> <em>Fall behind schedule</em> is to slip '
           'back against a plan &mdash; later than intended, not stopped.',

    resPerfect='Perfect score. Figures, fixed phrases, dependent pairs and '
               'phrasal verbs — all under control.',
    resStrong='Strong work. Look again at in/of/by with figures — that is '
              'usually where the last point goes.',
    resMid='A good base. Go back to the first teaching slide: in names the area, '
           'of gives the size, by gives the change.',
    resLow='Read the four teaching slides again and retry. None of this set is '
           'worked out from the parts.',

    actTitle='Present the figures',
    actUse='Use at least three:',
    actSpeakBrief='One of you presents this quarter’s results to the board; the '
                  'other is a board member who does not accept them. Four '
                  'minutes each, then swap.',
    actSpeak1='Describe one number that went up and one that went down, using '
              '<em>a rise in</em>, <em>an increase of</em> and <em>fall by</em> '
              'correctly.',
    actSpeak2='Say how this quarter looks <em>compared to</em> the last, and what '
              'you are still <em>in charge of</em> fixing.',
    actSpeak3='Push back: ask what is being done about the one figure that is not '
              'yet <em>under control</em>.',
    actWriteKind='Writing · 180–250 words',
    actWriteBrief='Write the paragraph that opens the quarterly report: what '
                  'rose, what fell, by how much, and what you are doing about '
                  'the one figure that is behind. Use at least three of the '
                  'expressions above.',
    actPlaceholder='In the three months to September…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Präpositionen für Fortgeschrittene <em>Teil 2</em>',
    coverSub='Die Präpositionen für Zahlen, formelle Wendungen und alltägliche '
             'Phrasal Verbs',
    chipLevel='B2 · Obere Mittelstufe', chipFocus='Präpositionen',
    chipCount='28 Fragen',

    t1Eyebrow='Bevor du anfängst',
    t1Title='Über Zahlen sprechen: drei Wörter, drei Aufgaben',
    t1ah='In, of, by',
    t1ab='A rise <em>in</em> demand benennt, <em>was</em> wächst. An increase '
         '<em>of</em> eight percent nennt die <em>Größe</em>. Costs dropping '
         '<em>by</em> a fifth nennt die Größe der <em>Veränderung</em>.',
    t1an='Alle drei können in einem Satz stehen und dort je eine andere Aufgabe '
         'haben.',
    t1bh='Von hier nach dort',
    t1bb='<strong>From X to Y</strong> markiert die beiden Enden einer '
         'Veränderung &mdash; the fleet grew <em>from</em> nine vans <em>to</em> '
         'forty. Der Ausgangspunkt steht zuerst.',
    t1bn='Die Höhe einer Veränderung steht nach einem Verb mit <em>by</em> '
         '(rose <em>by</em> 500) und nach einem Substantiv mit <em>of</em> (an '
         'increase <em>of</em> 500). <em>From&hellip;to</em> nennt stattdessen '
         'die beiden Enden.',
    t1ch='Vergleichen und einschränken',
    t1cb='<em>Compared to</em> stellt zwei Dinge nebeneinander. <em>A shortage '
         'of</em> benennt, was fehlt. <em>With regard to</em> grenzt auf einen '
         'Aspekt ein.',
    t1cn='<em>With regard to</em> ist formell und steht im Singular &mdash; nie '
         '<em>with regards to</em>, das ist eine Grußformel.',

    t2Eyebrow='Bevor du anfängst',
    t2Title='Weitere feste Wendungen und die Falle darin',
    t2ah='Die <em>in</em>-Familie',
    t2ab='<em>In charge of</em>, <em>in favour of</em>, <em>in return for</em>, '
         '<em>in addition to</em>. Vier Wendungen, die alle mit <em>in</em> '
         'beginnen &mdash; deshalb ist die erste Hälfte selten das Problem.',
    t2an='Wenn die Wendung eine Rolle oder eine Position beschreibt, spricht '
         'vieles für <em>in</em>.',
    t2bh='Zustände, keine Orte',
    t2bb='<em>Out of the question</em>, <em>under control</em>, <em>beyond '
         'doubt</em>. Jede beschreibt einen Zustand, in dem sich etwas befindet, '
         'und keine davon ist wörtlich gemeint.',
    t2bn='<em>Beyond</em> heißt jenseits des Punktes, an dem sich noch streiten '
         'ließe &mdash; dasselbe <em>beyond</em> wie in <em>beyond repair</em>.',
    t2ch='Der Schluss ist nicht immer <em>of</em>',
    t2cb='In charge <em>of</em>, in favour <em>of</em>, aber in return '
         '<em>for</em> und in addition <em>to</em>. Die erste Präposition zu '
         'kennen ist erst die halbe Wendung.',
    t2cn='Genau deshalb lernt man sie als Ganzes und nicht über eine Regel.',

    t3Eyebrow='Bevor du anfängst',
    t3Title='Weitere abhängige Paare, darunter eine echte Falle',
    t3ah='Wenn <em>to</em> kein Infinitiv ist',
    t3ab='Das Muster ist <em>object to</em> etwas, und dieses <em>to</em> ist eine '
         'Präposition &mdash; ein Verb danach steht also auf <em>-ing</em>. '
         'The neighbours objected <em>to</em> the trees <em>being cut '
         'down</em>, nie <em>to be cut down</em>.',
    t3an='Dieselbe Falle steckt in <em>look forward to</em> und <em>be used '
         'to</em>.',
    t3bh='Vertrauen und erwähnen',
    t3bb='<em>Rely on</em> jemanden, damit er etwas tut. <em>Refer to</em> etwas in '
         'einer Rede oder einem Text. Beide fest, beide nicht verhandelbar.',
    t3bn='<em>Refer to</em> heißt auch „etwas nachschlagen“, mit derselben '
         'Präposition.',
    t3ch='Gehen, gewinnen, prahlen',
    t3cb='Man <em>resigns from</em> einem Posten und <em>benefits from</em> einer '
         'Regelung &mdash; beide mit <em>from</em>. Man <em>boasts about</em> '
         'etwas und <em>excuses</em> jemanden <em>for</em> etwas.',
    t3cn='Dass sich zwei Verben eine Präposition teilen, ist hier die Ausnahme, '
         'nicht die Regel.',

    t4Eyebrow='Bevor du anfängst',
    t4Title='Bewältigen, verarbeiten, aufschieben, zufällig treffen',
    t4ah='Beide mit <em>with</em>',
    t4ab='Man <em>deals with</em> einem Problem und <em>copes with</em> Druck. '
         'Bei <em>deal with</em> geht es ums Lösen; bei <em>cope with</em> ums '
         'Durchhalten.',
    t4an='A manager deals with a conflict. The team copes with the workload.',
    t4bh='Darüber hinwegkommen oder es aufschieben',
    t4bb='<em>Get over</em> etwas heißt, es emotional zu verarbeiten. <em>Put '
         'off</em> etwas heißt, es aufzuschieben &mdash; und aufgeschoben wird '
         'die Entscheidung, nicht die Person.',
    t4bn='<em>Put someone off</em> gibt es auch und heißt, jemanden abzuschrecken. '
         'Anderes Verb.',
    t4ch='Zufällig, oder hinterher',
    t4cb='<em>Come across</em> und <em>run into</em> heißen beide zufällig. '
         '<em>Run into</em> gilt nur für Menschen; <em>come across</em> ist '
         'das übliche für Dinge. <em>Fall behind</em> heißt, hinter einen Plan '
         'zurückzufallen.',
    t4cn='You come across a photo; you run into an old teacher.',

    mcaEyebrow='Übung 1 · Entwicklungen und Mengen',
    mcaTitle='Welche Präposition trägt die Zahl?',
    mcbEyebrow='Übung 2 · Feste Wendungen',
    mcbTitle='Vervollständige den Ausdruck',
    mccEyebrow='Übung 3 · Abhängige Paare',
    mccTitle='Welche Präposition nimmt das Wort?',
    mcdEyebrow='Übung 4 · Phrasal Verbs',
    mcdTitle='Vervollständige das Phrasal Verb',

    q1why='<strong>In.</strong> <em>A rise in something</em> benennt den Bereich, '
          'der wächst &mdash; hier die Nachfrage. Die Zahl selbst steht noch '
          'nicht da.',
    q2why='<strong>Of.</strong> <em>An increase of</em> plus Betrag nennt die '
          'genaue Höhe des Anstiegs. Vergleiche <em>an increase in revenue</em>, '
          'das den Bereich benennt.',
    q3why='<strong>By.</strong> <em>Fall by</em> oder <em>drop by</em> plus Betrag '
          'nennt die Höhe des Rückgangs &mdash; wie viel verloren ging, nicht '
          'worauf es fiel.',
    q4why='<strong>From.</strong> <em>Rise from X to Y</em> nennt die beiden '
          'Enden der Veränderung. Eine datierte Ausgangszahl ist ein Endpunkt '
          'und kein Zuwachs, steht also mit <em>from</em> und nicht mit '
          '<em>by</em>.',
    q5why='<strong>To.</strong> <em>Compared to</em> leitet einen direkten '
          'Vergleich zwischen zwei Dingen ein.',
    q6why='<strong>Of.</strong> <em>A shortage of something</em> benennt genau, '
          'woran es mangelt &mdash; hier an bezahlbarem Wohnraum.',
    q7why='<strong>With.</strong> <em>With regard to</em> ist eine formelle feste '
          'Wendung und heißt „bezüglich“. Sie steht im Singular: <em>with '
          'regards to</em> ist eine Grußformel.',

    q8why='<strong>In.</strong> <em>In charge of something</em> heißt, für etwas '
          'verantwortlich zu sein.',
    q9why='<strong>In.</strong> <em>In favour of something</em> heißt, etwas zu '
          'unterstützen oder ihm zuzustimmen.',
    q10why='<strong>In.</strong> <em>In return for something</em> heißt im '
           'Austausch dafür. Beachte den Schluss <em>for</em>, nicht <em>of</em>.',
    q11why='<strong>Of.</strong> <em>Out of the question</em> heißt völlig '
           'ausgeschlossen &mdash; ein Zustand, kein Ort.',
    q12why='<strong>Under.</strong> <em>Under control</em> heißt, dass eine '
           'schwierige Lage erfolgreich beherrscht wird.',
    q13why='<strong>Beyond.</strong> <em>Beyond doubt</em> heißt jenseits des '
           'Punktes, an dem sich streiten ließe &mdash; dasselbe <em>beyond</em> '
           'wie in <em>beyond repair</em>.',
    q14why='<strong>In.</strong> <em>In addition to something</em> heißt zusätzlich '
           'dazu. Der Schluss ist hier <em>to</em>, nicht <em>of</em>.',

    q15why='<strong>On.</strong> <em>Rely on someone</em> heißt, sich darauf zu '
           'verlassen, dass die Person tut, was nötig ist. <em>Depend on</em> '
           'funktioniert genauso.',
    q16why='<strong>To.</strong> <em>Object to something</em> heißt, sich dagegen '
           'zu stellen &mdash; und dieses <em>to</em> ist eine Präposition, ein '
           'Verb danach steht also auf <em>-ing</em>: objected to the road '
           '<em>being built</em>.',
    q17why='<strong>For.</strong> <em>Excuse someone for something</em> ist das '
           'Muster der förmlichen Entschuldigung, und danach steht eine '
           '<em>-ing</em>-Form.',
    q18why='<strong>About.</strong> <em>Boast about something</em> heißt, stolz '
           'davon zu sprechen, manchmal stolzer als erwünscht.',
    q19why='<strong>From.</strong> <em>Resign from a position</em> heißt, eine '
           'Stelle freiwillig aufzugeben. Die Präposition ist <em>from</em>, nie '
           '<em>of</em>.',
    q20why='<strong>To.</strong> <em>Refer to something</em> heißt, es zu '
           'erwähnen oder darauf anzuspielen. Es heißt auch, etwas '
           'nachzuschlagen.',
    q21why='<strong>From.</strong> <em>Benefit from something</em> heißt, einen '
           'Vorteil daraus zu ziehen &mdash; dasselbe <em>from</em> wie bei '
           '<em>resign from</em>.',

    q22why='<strong>With.</strong> <em>Deal with something</em> heißt, ein Problem '
           'zu bearbeiten oder zu lösen &mdash; es also wirklich zu erledigen.',
    q23why='<strong>With.</strong> <em>Cope with something</em> heißt, eine '
           'schwierige Lage zu bewältigen. Anders als <em>deal with</em> '
           'behauptet es nicht, dass das Problem gelöst ist.',
    q24why='<strong>Over.</strong> <em>Get over something</em> heißt, es emotional '
           'zu verarbeiten &mdash; einen Verlust, einen Schock, eine '
           'Enttäuschung.',
    q25why='<strong>Off.</strong> <em>Put off something</em> heißt, es '
           'aufzuschieben. <em>Put someone off</em> ist ein anderes Verb und '
           'heißt, jemanden abzuschrecken.',
    q26why='<strong>Across.</strong> <em>Come across something</em> heißt, es '
           'zufällig zu finden. Es gilt für Dinge; für Menschen nimmt man '
           '<em>run into</em>.',
    q27why='<strong>Into.</strong> <em>Run into someone</em> heißt, jemanden '
           'unerwartet zu treffen. Es gilt für Menschen; für Dinge nimmt man '
           '<em>come across</em>.',
    q28why='<strong>Behind.</strong> <em>Fall behind schedule</em> heißt, hinter '
           'einen Plan zurückzufallen &mdash; später als geplant, nicht gestoppt.',

    resPerfect='Volle Punktzahl. Zahlen, feste Wendungen, abhängige Paare und '
               'Phrasal Verbs — alles im Griff.',
    resStrong='Starke Leistung. Sieh dir in/of/by bei Zahlen noch einmal an — '
              'dort geht meist der letzte Punkt verloren.',
    resMid='Eine gute Grundlage. Geh zurück zur ersten Lernfolie: in benennt den '
           'Bereich, of die Größe, by die Veränderung.',
    resLow='Lies die vier Lernfolien noch einmal und versuch es erneut. Nichts '
           'aus dieser Gruppe lässt sich aus den Teilen erschließen.',

    actTitle='Präsentiere die Zahlen',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Eine Person stellt dem Vorstand die Quartalszahlen vor, die '
                  'andere ist ein Vorstandsmitglied, das sie nicht akzeptiert. '
                  'Vier Minuten pro Person, dann tauschen.',
    actSpeak1='Beschreibe eine Zahl, die gestiegen ist, und eine, die gefallen '
              'ist — mit <em>a rise in</em>, <em>an increase of</em> und '
              '<em>fall by</em>, jeweils richtig eingesetzt.',
    actSpeak2='Sag, wie dieses Quartal <em>compared to</em> dem letzten dasteht '
              'und wofür du weiterhin <em>in charge of</em> bist.',
    actSpeak3='Hak nach: frag, was gegen die eine Zahl unternommen wird, die noch '
              'nicht <em>under control</em> ist.',
    actWriteKind='Schreiben · 180–250 Wörter',
    actWriteBrief='Schreib den Absatz, mit dem der Quartalsbericht beginnt: was '
                  'gestiegen ist, was gefallen ist, um wie viel, und was du '
                  'gegen die eine Zahl unternimmst, die hinterherhinkt. '
                  'Verwende mindestens drei der Ausdrücke oben.',
    actPlaceholder='In the three months to September…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Preposiciones avanzadas <em>Parte 2</em>',
    coverSub='Las preposiciones que sostienen las cifras, las expresiones '
             'formales y los phrasal verbs del día a día',
    chipLevel='B2 · Intermedio alto', chipFocus='Preposiciones',
    chipCount='28 preguntas',

    t1Eyebrow='Antes de empezar',
    t1Title='Hablar de cifras: tres palabras, tres funciones',
    t1ah='In, of, by',
    t1ab='A rise <em>in</em> demand nombra <em>qué</em> está creciendo. An '
         'increase <em>of</em> eight percent da el <em>tamaño</em>. Costs '
         'dropping <em>by</em> a fifth da el tamaño del <em>cambio</em>.',
    t1an='Las tres pueden aparecer en una misma frase, cada una con su función.',
    t1bh='De aquí a allí',
    t1bb='<strong>From X to Y</strong> marca los dos extremos de un cambio '
         '&mdash; the fleet grew <em>from</em> nine vans <em>to</em> forty. El '
         'punto de partida va primero.',
    t1bn='El tamaño de un cambio lleva <em>by</em> tras un verbo (rose '
         '<em>by</em> 500) y <em>of</em> tras un sustantivo (an increase '
         '<em>of</em> 500). <em>From&hellip;to</em> nombra en cambio los dos '
         'extremos.',
    t1ch='Comparar y acotar',
    t1cb='<em>Compared to</em> pone dos cosas una al lado de la otra. <em>A '
         'shortage of</em> nombra lo que falta. <em>With regard to</em> acota a '
         'un solo aspecto.',
    t1cn='<em>With regard to</em> es formal y va en singular &mdash; nunca '
         '<em>with regards to</em>, que es una despedida.',

    t2Eyebrow='Antes de empezar',
    t2Title='Más expresiones fijas, y la trampa que llevan dentro',
    t2ah='La familia de <em>in</em>',
    t2ab='<em>In charge of</em>, <em>in favour of</em>, <em>in return for</em>, '
         '<em>in addition to</em>. Cuatro expresiones que empiezan por '
         '<em>in</em> &mdash; por eso la primera mitad rara vez es la difícil.',
    t2an='Si la expresión describe un papel o una posición, lo probable es '
         '<em>in</em>.',
    t2bh='Estados, no lugares',
    t2bb='<em>Out of the question</em>, <em>under control</em>, <em>beyond '
         'doubt</em>. Cada una describe una condición en la que está algo, y '
         'ninguna es literal.',
    t2bn='<em>Beyond</em> significa más allá del punto en que se podría discutir '
         '&mdash; el mismo <em>beyond</em> de <em>beyond repair</em>.',
    t2ch='El final no siempre es <em>of</em>',
    t2cb='In charge <em>of</em>, in favour <em>of</em>, pero in return '
         '<em>for</em> e in addition <em>to</em>. Saber la preposición inicial '
         'es solo media expresión.',
    t2cn='Por eso se memorizan enteras y no por regla.',

    t3Eyebrow='Antes de empezar',
    t3Title='Más parejas dependientes, con una trampa de verdad',
    t3ah='Cuando <em>to</em> no es un infinitivo',
    t3ab='El patrón es <em>object to</em> algo, y ese <em>to</em> es una preposición '
         '&mdash; así que el verbo que sigue va en <em>-ing</em>. The neighbours '
         'objected <em>to</em> the trees <em>being cut down</em>, nunca <em>to be '
         'cut down</em>.',
    t3an='La misma trampa está dentro de <em>look forward to</em> y <em>be used '
         'to</em>.',
    t3bh='Confiar y mencionar',
    t3bb='<em>Rely on</em> alguien para que haga algo. <em>Refer to</em> algo en '
         'un discurso o un texto. Las dos fijas, ninguna negociable.',
    t3bn='<em>Refer to</em> también significa "consultar algo", con la misma '
         'preposición.',
    t3ch='Irse, ganar, presumir',
    t3cb='Se dice <em>resign from</em> un puesto y <em>benefit from</em> un plan '
         '&mdash; los dos con <em>from</em>. Y <em>boast about</em> algo, y '
         '<em>excuse someone for</em> algo.',
    t3cn='Que dos verbos compartan preposición es aquí la excepción, no la regla.',

    t4Eyebrow='Antes de empezar',
    t4Title='Resolver, superar, aplazar, encontrarse por casualidad',
    t4ah='Las dos llevan <em>with</em>',
    t4ab='Se dice <em>deal with</em> un problema y <em>cope with</em> la presión. '
         '<em>Deal with</em> va de resolverlo; <em>cope with</em> va de '
         'sobrellevarlo.',
    t4an='A manager deals with a conflict. The team copes with the workload.',
    t4bh='Superarlo, o dejarlo para después',
    t4bb='<em>Get over</em> algo es superarlo emocionalmente. <em>Put off</em> '
         'algo es aplazarlo &mdash; y lo que se aplaza es la decisión, no la '
         'persona.',
    t4bn='<em>Put someone off</em> también existe y significa desanimar a '
         'alguien. Otro verbo.',
    t4ch='Por casualidad, o por detrás',
    t4cb='<em>Come across</em> y <em>run into</em> significan las dos por '
         'casualidad. <em>Run into</em> solo se usa con personas; <em>come '
         'across</em> es el habitual para cosas. <em>Fall behind</em> es '
         'quedarse atrás respecto a un plan.',
    t4cn='You come across a photo; you run into an old teacher.',

    mcaEyebrow='Actividad 1 · Tendencias y cantidad',
    mcaTitle='¿Qué preposición sostiene la cifra?',
    mcbEyebrow='Actividad 2 · Expresiones fijas',
    mcbTitle='Completa la expresión',
    mccEyebrow='Actividad 3 · Parejas dependientes',
    mccTitle='¿Qué preposición lleva la palabra?',
    mcdEyebrow='Actividad 4 · Phrasal verbs',
    mcdTitle='Completa el phrasal verb',

    q1why='<strong>In.</strong> <em>A rise in something</em> nombra el área que '
          'crece &mdash; aquí la demanda. La cifra todavía no se ha dado.',
    q2why='<strong>Of.</strong> <em>An increase of</em> más una cantidad da el '
          'tamaño exacto de la subida. Compara <em>an increase in revenue</em>, '
          'que nombra el área.',
    q3why='<strong>By.</strong> <em>Fall by</em> o <em>drop by</em> más una '
          'cantidad indica el tamaño de la bajada &mdash; cuánto se perdió, no '
          'hasta dónde cayó.',
    q4why='<strong>From.</strong> <em>Rise from X to Y</em> nombra los dos '
          'extremos del cambio. Una cifra de partida con fecha es un extremo, '
          'no un incremento, así que lleva <em>from</em> y no <em>by</em>.',
    q5why='<strong>To.</strong> <em>Compared to</em> introduce una comparación '
          'directa entre dos cosas.',
    q6why='<strong>Of.</strong> <em>A shortage of something</em> indica '
          'exactamente de qué hay escasez &mdash; aquí, de vivienda asequible.',
    q7why='<strong>With.</strong> <em>With regard to</em> es una expresión fija '
          'formal que significa "con respecto a". Va en singular: <em>with '
          'regards to</em> es una despedida.',

    q8why='<strong>In.</strong> <em>In charge of something</em> significa ser '
          'responsable de gestionarlo.',
    q9why='<strong>In.</strong> <em>In favour of something</em> significa '
          'apoyarlo o estar de acuerdo con ello.',
    q10why='<strong>In.</strong> <em>In return for something</em> significa a '
           'cambio de ello. Fíjate en que el final es <em>for</em>, no '
           '<em>of</em>.',
    q11why='<strong>Of.</strong> <em>Out of the question</em> significa '
           'totalmente imposible &mdash; un estado, no un lugar.',
    q12why='<strong>Under.</strong> <em>Under control</em> significa que una '
           'situación difícil se está gestionando con éxito.',
    q13why='<strong>Beyond.</strong> <em>Beyond doubt</em> significa más allá del '
           'punto en que se podría discutir &mdash; el mismo <em>beyond</em> de '
           '<em>beyond repair</em>.',
    q14why='<strong>In.</strong> <em>In addition to something</em> significa '
           'además de ello. Aquí el final es <em>to</em>, no <em>of</em>.',

    q15why='<strong>On.</strong> <em>Rely on someone</em> es confiar en que esa '
           'persona hará lo necesario. <em>Depend on</em> funciona igual.',
    q16why='<strong>To.</strong> <em>Object to something</em> es oponerse a ello '
           '&mdash; y ese <em>to</em> es una preposición, así que el verbo que '
           'sigue va en <em>-ing</em>: objected to the road <em>being built</em>.',
    q17why='<strong>For.</strong> <em>Excuse someone for something</em> es el '
           'patrón de la disculpa formal, y lo que sigue va en <em>-ing</em>.',
    q18why='<strong>About.</strong> <em>Boast about something</em> es hablar de '
           'ello con orgullo, a veces con más del deseable.',
    q19why='<strong>From.</strong> <em>Resign from a position</em> es dejar un '
           'puesto voluntariamente. La preposición es <em>from</em>, nunca '
           '<em>of</em>.',
    q20why='<strong>To.</strong> <em>Refer to something</em> es mencionarlo o '
           'aludir a ello. También significa consultar algo.',
    q21why='<strong>From.</strong> <em>Benefit from something</em> es sacar '
           'ventaja de ello &mdash; el mismo <em>from</em> que <em>resign '
           'from</em>.',

    q22why='<strong>With.</strong> <em>Deal with something</em> es gestionar o '
           'resolver un problema &mdash; zanjarlo de verdad.',
    q23why='<strong>With.</strong> <em>Cope with something</em> es sobrellevar '
           'una situación difícil. A diferencia de <em>deal with</em>, no afirma '
           'que el problema esté resuelto.',
    q24why='<strong>Over.</strong> <em>Get over something</em> es superarlo '
           'emocionalmente &mdash; una pérdida, un susto, una decepción.',
    q25why='<strong>Off.</strong> <em>Put off something</em> es aplazarlo. '
           '<em>Put someone off</em> es otro verbo y significa desanimar a '
           'alguien.',
    q26why='<strong>Across.</strong> <em>Come across something</em> es '
           'encontrarlo por casualidad. Se usa con cosas; con personas, '
           '<em>run into</em>.',
    q27why='<strong>Into.</strong> <em>Run into someone</em> es encontrarse con '
           'esa persona por sorpresa. Se usa con personas; con cosas, <em>come '
           'across</em>.',
    q28why='<strong>Behind.</strong> <em>Fall behind schedule</em> es quedarse '
           'atrás respecto a un plan &mdash; más tarde de lo previsto, no '
           'parado.',

    resPerfect='Puntuación perfecta. Cifras, expresiones fijas, parejas '
               'dependientes y phrasal verbs — todo controlado.',
    resStrong='Muy bien. Vuelve a mirar in/of/by con cifras — ahí suele irse el '
              'último punto.',
    resMid='Buena base. Vuelve a la primera diapositiva: in nombra el área, of '
           'da el tamaño, by da el cambio.',
    resLow='Lee otra vez las cuatro diapositivas de enseñanza y prueba de nuevo. '
           'Nada de este grupo se deduce de sus partes.',

    actTitle='Presenta las cifras',
    actUse='Usa al menos tres:',
    actSpeakBrief='Una persona presenta los resultados del trimestre al consejo; '
                  'la otra es un miembro del consejo que no los acepta. Cuatro '
                  'minutos cada una, luego cambiad.',
    actSpeak1='Describe una cifra que subió y otra que bajó, usando bien <em>a '
              'rise in</em>, <em>an increase of</em> y <em>fall by</em>.',
    actSpeak2='Di cómo queda este trimestre <em>compared to</em> el anterior, y '
              'de qué sigues <em>in charge of</em> arreglar.',
    actSpeak3='Replica: pregunta qué se está haciendo con la única cifra que '
              'todavía no está <em>under control</em>.',
    actWriteKind='Escritura · 180–250 palabras',
    actWriteBrief='Escribe el párrafo que abre el informe trimestral: qué '
                  'subió, qué bajó, cuánto, y qué estás haciendo con la única '
                  'cifra que va retrasada. Usa al menos tres de las expresiones '
                  'anteriores.',
    actPlaceholder='In the three months to September…',
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
