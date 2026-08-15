# -*- coding: utf-8 -*-
"""Interface strings for the B2 advanced-grammar deck (Stranger Gears).

English and German, both complete. The generic chrome — buttons, score
label, the plural-aware word counter — is lifted verbatim from
`chrome_i18n.py` rather than retranslated, because it is identical in
every deck on the site.

Scope boundary, per the house style: the app's own chrome translates, the
English being taught does not. Question stems, options, gap sentences,
the example sentences on the teaching slides and the activation chips all
stay in English in every language. `deck.teach` puts a `data-i18n` on a
card's heading and its note but never on its body, which is where the
worked examples live — that split is deliberate and is why the German
here covers headings, titles, hints and instructions only.

`build_topgear.py` reads T['en'] directly, so a slide and its English
string cannot drift apart: there is one copy of each.
"""
import json
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel',
        'slideOf', 'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext',
        'actEyebrow', 'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    # ── cover ──
    coverTitle='Advanced Grammar <em>in Context</em>',
    coverSub='Reported speech, unreal conditionals, cleft sentences and '
             'complex passives — through Clarkson, Hammond, May and the Stig',
    chipLevel='B2 &middot; Grammar',
    chipFocus='Four structures',
    chipTime='45&ndash;55 minutes',
    chipCount='NN slides',

    # ── eyebrows ──
    tOrient='Orientation',
    tRep='Language focus &middot; Reported speech',
    tCond='Language focus &middot; Conditionals',
    tCleft='Language focus &middot; Cleft sentences',
    tPass='Language focus &middot; Complex passives',

    # ── 2. orientation ──
    o1T='Four structures, one programme',
    o1a='Reported speech',
    o1b='Unreal conditionals',
    o1c='Cleft sentences',
    o1d='Complex passives',
    o1n='Every rule tested later is stated on a slide first. Fifteen slides '
        'of language, twenty questions, then a speaking and writing task.',

    # ── 3. terminology ──
    o2T='The words this lesson uses',
    o2a='reporting verb',
    o2b='backshift',
    o2c='perfect infinitive',
    o2d='cleft',
    o2e='focus',
    o2f='complement',
    o2n='One more: a <strong>relative pronoun</strong> &mdash; <em>who</em>, '
        '<em>which</em>, <em>that</em> &mdash; stands in for a noun and opens '
        'a clause about it. When it is the subject of that clause, nothing '
        'else may be.',

    # ── 4. the backshift table ──
    r1T='Backshift: one step back',
    r1a='After <em>said</em>, <em>told</em>, <em>announced</em> &mdash; the '
        'reported tense steps back',
    r1n='Two tenses can land on the same one: a past simple and a present '
        'perfect both come out as the past perfect, so the report loses a '
        'distinction the original had.',

    # ── 5. what does not backshift ──
    r2T='When the tenses stay where they are',
    r2a='Still true now',
    r2b='Reported straight away',
    r2c='Already past',
    r2n='Both versions are correct English. <em>He said he loves fast cars</em> '
        'and <em>he said he loved fast cars</em> are each right &mdash; the '
        'shifted one simply holds the statement further away from you.',

    # ── 6. pronouns, time and place ──
    r3T='The other things that shift',
    r3a='People and things',
    r3b='Time and place',
    r3n='Shift them only when the situation has actually changed. Repeating '
        '<em>tomorrow</em> an hour later in the same room is right; repeating '
        'it a week later in another city is not.',

    # ── 7. third conditional ──
    c1T='The third conditional',
    c1a='The form',
    c1b='The meaning',
    c1n='Both halves are past and both are unreal: the crew did not check, and '
        'they did lose the day. <em>Might have</em> and <em>could have</em> '
        'replace <em>would have</em> when the result is less certain.',

    # ── 8. mixed conditional ──
    c2T='The mixed conditional',
    c2a='Third &mdash; past result',
    c2b='Mixed &mdash; present result',
    c2n='The <em>if</em>-clause is identical in both. Only the result moves: '
        '<em>would have</em> + past participle looks back, <em>would</em> + '
        'infinitive looks at now. <em>today</em>, <em>now</em> and '
        '<em>still</em> are the usual signals.',

    # ── 9. what cannot go in an if-clause ──
    c3T='Never in the <em>if</em>-clause',
    c3a='Not <em>would</em>',
    c3b='Not <em>will</em>',
    c3n='The condition sits one step further back than you expect, and '
        '<em>will</em> and <em>would</em> belong in the result clause only. '
        'The one exception is a polite request &mdash; <em>If you would wait '
        'here a moment</em> &mdash; which is not really a condition at all.',

    # ── 10. it-clefts ──
    f1T='It-clefts',
    f1a='The frame',
    f1b='The focus can be almost anything',
    f1n='Subjects, objects, times and places all take the spotlight equally '
        'well, so &ldquo;an it-cleft emphasises the subject&rdquo; is not the '
        'rule. Use <em>who</em> for a person and <em>that</em> for anything '
        'else &mdash; <em>that</em> is acceptable for a person too.',

    # ── 11. wh-clefts ──
    f2T='Wh-clefts, or pseudo-clefts',
    f2a='The frame',
    f2b='Against the it-cleft',
    f2n='The focus of a wh-cleft is the complement of <em>be</em>, so it can '
        'be a noun phrase or a whole clause: <em>What the three of them do '
        'best is argue about cars.</em>',

    # ── 12. that / which, never what ──
    f3T='<em>that</em> and <em>which</em> &mdash; never <em>what</em>',
    f3a='After an it-cleft',
    f3b='Why the mistake happens',
    f3n='A related trap: <em>which</em> as the subject of its own clause needs '
        'no pronoun after it. <em>&hellip;genuinely enthusiastic about cars, '
        'which is rare on television.</em>',

    # ── 13. complex passive, pattern 1 ──
    p1T='<em>It is thought that&hellip;</em>',
    p1a='The frame',
    p1b='What it does',
    p1n='This pattern is correct English and often the easier one to write: it '
        'keeps the clause intact, so no tense has to be folded into an '
        'infinitive.',

    # ── 14. complex passive, pattern 2 ──
    p2T='The subject moves to the front',
    p2a='Same time as the report',
    p2b='Earlier than the report',
    p2n='The two patterns say the same thing. What you cannot do is mix them: '
        '<em>The show is thought that it changed&hellip;</em> takes the subject '
        'from one and the clause from the other.',

    # ── 15. stative verbs ──
    p3T='Verbs that take no continuous',
    p3a='A state, not an activity',
    p3b='So the report stays simple',
    p3n='A few of them have a second, active meaning that does take the '
        'continuous &mdash; <em>I am seeing the producer at four</em>, '
        '<em>he is being difficult</em> &mdash; but never in the stative sense.',

    # ── activity headers ──
    a1E='Activity 1 &middot; Multiple choice',
    a1T='Choose the correct version',
    a2E='Activity 2 &middot; Complete the sentence',
    a2T='Type the missing words',
    a3E='Activity 3 &middot; Error correction',
    a3T='Repair the struck-through words',
    a4E='Activity 4 &middot; Identify the structure',
    a4T='Which label fits the sentence?',

    # ── gap hints: the scaffold, never the answer ──
    g1h='The spokesperson said: <em>&ldquo;We made the decision after a '
        'thorough internal review.&rdquo;</em> Report it, and keep it '
        'passive.',
    g2h='A third conditional <em>if</em>-clause, negative. The verb is '
        '<em>move</em>.',
    g3h='A complex passive built on <em>report</em>, with a perfect infinitive '
        '&mdash; the premiere came before the reporting.',
    g4h='An it-cleft putting the spotlight on <em>the Stig</em>. Three words, '
        'then the pronoun that links back.',
    g5h='A third-conditional result clause sitting inside a report. The verb is '
        '<em>film</em>.',

    e1h='Two sentences, two errors, one point each. Type what should replace '
        'the struck-through words.',
    e2h='The <em>if</em>-clause is carrying something that belongs in the '
        'result clause.',
    e3h='The subject is already at the front of the sentence, so the reporting '
        'verb cannot take a <em>that</em>-clause as well.',
    e4h='One of these verbs describes a state rather than an activity.',
    e5h='The tense is right. The report is written a week later, in another '
        'city.',

    # ── results ──
    resPerfect='Full marks. You are choosing these structures by what they do, '
               'not by what they sound like — which is the whole difficulty '
               'with all four of them.',
    resStrong='Strong. Look at where the misses sit: the clefts and the '
              'passives are recognition, while backshift is judgement, and '
              'those two need different kinds of practice.',
    resMid='A pass. The slides on backshift, the third conditional and the two '
           'cleft frames carry most of the marks here — work through those '
           'again before you retry.',
    resLow='Take the teaching slides again before you retry. Every rule tested '
           'here is stated on a slide before the questions begin, backshift '
           'and its exceptions first.',

    # ── activation ──
    actTitle='The press statement',
    actUse='Use at least four:',
    actSpeakBrief='A presenter has walked off a shoot in the middle of a film. '
                  'You are the production team, and the press are already '
                  'calling.',
    actSpeak1='One of you took the phone call. Report what the presenter '
              'actually said &mdash; three sentences, and not one word quoted '
              'directly.',
    actSpeak2='Swap. Argue about what should have been done differently that '
              'morning, in the third conditional throughout. A bare past '
              'simple loses the argument.',
    actSpeak3='Both: agree one sentence for the press that names nobody. Start '
              'it <em>It is thought that&hellip;</em> or <em>The decision is '
              'said to&hellip;</em>',
    actWriteKind='Writing &middot; 150&ndash;250 words',
    actWriteBrief='Write the statement the production company releases the next '
                  'morning: what was said, what was decided, what happens now. '
                  'Report everything &mdash; no direct quotation anywhere '
                  '&mdash; and use one cleft to put the emphasis where you '
                  'want it.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does
    # not decode entities — HOUSE-STYLE §13, in its attribute variant.
    actPlaceholder='Following yesterday’s filming, the production company '
                   'has confirmed that …',
)

T['de'] = dict(
    coverTitle='Advanced Grammar <em>in Context</em>',
    coverSub='Indirekte Rede, irreale Bedingungssätze, Cleft-Sätze und '
             'komplexe Passivformen — mit Clarkson, Hammond, May und dem Stig',
    chipLevel='B2 &middot; Grammatik',
    chipFocus='Vier Strukturen',
    chipTime='45&ndash;55 Minuten',
    chipCount='NN Folien',

    tOrient='Orientierung',
    tRep='Sprachfokus &middot; Indirekte Rede',
    tCond='Sprachfokus &middot; Bedingungssätze',
    tCleft='Sprachfokus &middot; Cleft-Sätze',
    tPass='Sprachfokus &middot; Komplexe Passivformen',

    o1T='Vier Strukturen, eine Sendung',
    o1a='Indirekte Rede',
    o1b='Irreale Bedingungssätze',
    o1c='Cleft-Sätze',
    o1d='Komplexe Passivformen',
    o1n='Jede Regel, die später abgefragt wird, steht vorher auf einer Folie. '
        'Fünfzehn Folien Sprache, zwanzig Aufgaben, danach eine Sprech- und '
        'eine Schreibaufgabe.',

    o2T='Die Fachbegriffe dieser Lektion',
    o2a='reporting verb &mdash; Redeeinleitendes Verb',
    o2b='backshift &mdash; Zeitenverschiebung',
    o2c='perfect infinitive &mdash; Infinitiv Perfekt',
    o2d='cleft &mdash; Spaltsatz',
    o2e='focus &mdash; das Hervorgehobene',
    o2f='complement &mdash; Ergänzung',
    o2n='Und noch einer: Ein <strong>relative pronoun</strong> '
        '(Relativpronomen) &mdash; <em>who</em>, <em>which</em>, <em>that</em> '
        '&mdash; steht für ein Substantiv und eröffnet einen Nebensatz dazu. '
        'Ist es selbst das Subjekt dieses Nebensatzes, darf nichts anderes es '
        'sein.',

    r1T='Backshift: einen Schritt zurück',
    r1a='Nach <em>said</em>, <em>told</em>, <em>announced</em> &mdash; die '
        'berichtete Zeitform rückt zurück',
    r1n='Zwei Zeitformen können auf derselben landen: Past Simple und Present '
        'Perfect werden beide zum Past Perfect. Der Bericht verliert damit '
        'eine Unterscheidung, die das Original noch hatte.',

    r2T='Wenn die Zeitformen bleiben, wo sie sind',
    r2a='Gilt weiterhin',
    r2b='Sofort weitergegeben',
    r2c='Schon Vergangenheit',
    r2n='Beide Fassungen sind korrektes Englisch. <em>He said he loves fast '
        'cars</em> und <em>he said he loved fast cars</em> sind beide richtig '
        '&mdash; die verschobene Form rückt die Aussage nur weiter von dir weg.',

    r3T='Was sich sonst noch verschiebt',
    r3a='Personen und Dinge',
    r3b='Zeit und Ort',
    r3n='Verschiebe sie nur, wenn sich die Situation tatsächlich geändert hat. '
        '<em>Tomorrow</em> eine Stunde später im selben Raum zu wiederholen ist '
        'richtig; eine Woche später in einer anderen Stadt nicht.',

    c1T='Der Third Conditional',
    c1a='Die Form',
    c1b='Die Bedeutung',
    c1n='Beide Hälften sind Vergangenheit und beide sind irreal: Das Team hat '
        'nicht nachgesehen, und der Tag ging verloren. <em>Might have</em> und '
        '<em>could have</em> ersetzen <em>would have</em>, wenn das Ergebnis '
        'weniger sicher ist.',

    c2T='Der gemischte Bedingungssatz',
    c2a='Third &mdash; Ergebnis in der Vergangenheit',
    c2b='Mixed &mdash; Ergebnis in der Gegenwart',
    c2n='Der <em>if</em>-Satz ist in beiden identisch. Nur der Hauptsatz '
        'wechselt: <em>would have</em> + Partizip Perfekt blickt zurück, '
        '<em>would</em> + Infinitiv blickt auf jetzt. <em>today</em>, '
        '<em>now</em> und <em>still</em> sind die üblichen Signale.',

    c3T='Niemals im <em>if</em>-Satz',
    c3a='Kein <em>would</em>',
    c3b='Kein <em>will</em>',
    c3n='Der Bedingungssatz steht eine Stufe weiter zurück, als man erwartet, '
        'und <em>will</em> und <em>would</em> gehören ausschließlich in den '
        'Hauptsatz. Die einzige Ausnahme ist die höfliche Bitte &mdash; '
        '<em>If you would wait here a moment</em> &mdash; und die ist gar keine '
        'echte Bedingung.',

    f1T='It-Clefts',
    f1a='Das Gerüst',
    f1b='Hervorgehoben werden kann fast alles',
    f1n='Subjekte, Objekte, Zeit- und Ortsangaben lassen sich gleichermaßen '
        'hervorheben &mdash; „ein It-Cleft betont das Subjekt“ ist also keine '
        'Regel. <em>Who</em> für Personen, <em>that</em> für alles andere; '
        '<em>that</em> ist auch bei Personen zulässig.',

    f2T='Wh-Clefts oder Pseudo-Clefts',
    f2a='Das Gerüst',
    f2b='Im Vergleich zum It-Cleft',
    f2n='Das Hervorgehobene eines Wh-Clefts ist die Ergänzung zu <em>be</em> '
        'und kann deshalb eine Nominalphrase oder ein ganzer Satz sein: '
        '<em>What the three of them do best is argue about cars.</em>',

    f3T='<em>that</em> und <em>which</em> &mdash; nie <em>what</em>',
    f3a='Nach einem It-Cleft',
    f3b='Warum der Fehler entsteht',
    f3n='Eine verwandte Falle: <em>which</em> als Subjekt seines eigenen '
        'Nebensatzes braucht kein weiteres Pronomen. '
        '<em>&hellip;genuinely enthusiastic about cars, which is rare on '
        'television.</em>',

    p1T='<em>It is thought that&hellip;</em>',
    p1a='Das Gerüst',
    p1b='Wozu es dient',
    p1n='Dieses Muster ist korrektes Englisch und oft das leichtere: Es lässt '
        'den Nebensatz unangetastet, sodass keine Zeitform in einen Infinitiv '
        'gepresst werden muss.',

    p2T='Das Subjekt rückt nach vorn',
    p2a='Gleichzeitig mit dem Bericht',
    p2b='Früher als der Bericht',
    p2n='Beide Muster sagen dasselbe. Nur mischen darf man sie nicht: '
        '<em>The show is thought that it changed&hellip;</em> nimmt das Subjekt '
        'aus dem einen und den Nebensatz aus dem anderen.',

    p3T='Verben ohne Verlaufsform',
    p3a='Ein Zustand, keine Tätigkeit',
    p3b='Deshalb bleibt der Bericht einfach',
    p3n='Einige davon haben eine zweite, handlungsbezogene Bedeutung, die sehr '
        'wohl eine Verlaufsform bildet &mdash; <em>I am seeing the producer at '
        'four</em>, <em>he is being difficult</em> &mdash; im Zustandssinn '
        'jedoch nie.',

    a1E='Aufgabe 1 &middot; Multiple Choice',
    a1T='Wähle die richtige Fassung',
    a2E='Aufgabe 2 &middot; Ergänze den Satz',
    a2T='Tippe die fehlenden Wörter',
    a3E='Aufgabe 3 &middot; Fehlerkorrektur',
    a3T='Repariere die durchgestrichenen Wörter',
    a4E='Aufgabe 4 &middot; Struktur erkennen',
    a4T='Welche Beschreibung passt zum Satz?',

    g1h='Der Sprecher sagte: <em>&ldquo;We made the decision after a thorough '
        'internal review.&rdquo;</em> Gib es wieder &mdash; und bleibe im '
        'Passiv.',
    g2h='Ein <em>if</em>-Satz im Third Conditional, verneint. Das Verb ist '
        '<em>move</em>.',
    g3h='Ein komplexes Passiv mit <em>report</em>, dazu ein Infinitiv Perfekt '
        '&mdash; die Premiere lag vor der Berichterstattung.',
    g4h='Ein It-Cleft, das <em>the Stig</em> hervorhebt. Drei Wörter, dann das '
        'rückverweisende Pronomen.',
    g5h='Ein Hauptsatz des Third Conditional, eingebettet in einen Bericht. Das '
        'Verb ist <em>film</em>.',

    e1h='Zwei Sätze, zwei Fehler, je ein Punkt. Tippe, was an die Stelle der '
        'durchgestrichenen Wörter gehört.',
    e2h='Der <em>if</em>-Satz trägt etwas, das in den Hauptsatz gehört.',
    e3h='Das Subjekt steht bereits vorn, deshalb kann das redeeinleitende Verb '
        'nicht zusätzlich einen <em>that</em>-Satz nehmen.',
    e4h='Eines dieser Verben beschreibt einen Zustand und keine Tätigkeit.',
    e5h='Die Zeitform stimmt. Der Bericht entsteht eine Woche später, in einer '
        'anderen Stadt.',

    resPerfect='Volle Punktzahl. Du wählst diese Strukturen danach aus, was sie '
               'leisten, und nicht danach, wie sie klingen — genau darin liegt '
               'die Schwierigkeit bei allen vieren.',
    resStrong='Stark. Sieh dir an, wo die Fehler liegen: Clefts und Passiv sind '
              'Wiedererkennen, der Backshift ist Abwägen, und beides braucht '
              'eine andere Art von Übung.',
    resMid='Bestanden. Die Folien zum Backshift, zum Third Conditional und zu '
           'den beiden Cleft-Gerüsten tragen hier die meisten Punkte — arbeite '
           'sie noch einmal durch, bevor du es erneut versuchst.',
    resLow='Lies die Erklärfolien noch einmal, bevor du es erneut versuchst. '
           'Jede hier abgefragte Regel steht vor den Aufgaben auf einer Folie, '
           'der Backshift und seine Ausnahmen zuerst.',

    actTitle='Die Pressemitteilung',
    actUse='Mindestens vier verwenden:',
    actSpeakBrief='Ein Moderator hat mitten im Dreh die Aufnahme verlassen. Ihr '
                  'seid das Produktionsteam, und die Presse ruft bereits an.',
    actSpeak1='Eine Person hat den Anruf angenommen. Gib wieder, was der '
              'Moderator tatsächlich gesagt hat &mdash; drei Sätze, und kein '
              'einziges Wort wörtlich zitiert.',
    actSpeak2='Tauscht die Rollen. Streitet darüber, was an diesem Morgen '
              'anders hätte laufen sollen, durchgehend im Third Conditional. '
              'Ein bloßes Past Simple verliert die Diskussion.',
    actSpeak3='Beide: Einigt euch auf einen Satz für die Presse, der niemanden '
              'namentlich nennt. Beginnt ihn mit <em>It is thought '
              'that&hellip;</em> oder <em>The decision is said to&hellip;</em>',
    actWriteKind='Schreiben &middot; 150&ndash;250 Wörter',
    actWriteBrief='Schreibe die Mitteilung, die die Produktionsfirma am '
                  'nächsten Morgen herausgibt: was gesagt wurde, was '
                  'entschieden wurde, wie es weitergeht. Alles in indirekter '
                  'Rede &mdash; nirgends ein wörtliches Zitat &mdash; und ein '
                  'Cleft-Satz, um die Betonung dorthin zu legen, wo du sie '
                  'haben willst.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does
    # not decode entities — HOUSE-STYLE §13, in its attribute variant.
    actPlaceholder='Following yesterday’s filming, the production company '
                   'has confirmed that …',
)


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
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)),
              ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
