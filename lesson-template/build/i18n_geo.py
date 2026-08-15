# -*- coding: utf-8 -*-
"""Interface strings for The Language of Geoscience (C1, technical English).

English and German, both complete. The generic chrome — buttons, score
label, the plural-aware word counter — is lifted verbatim from
`chrome_i18n.py` rather than retranslated, because it is identical in
every deck on the site.

Scope boundary, per the house style: the app's own chrome translates, the
English being taught does not. Question stems, options, gap sentences,
the word bank, the example sentences on the teaching slides and the
activation chips all stay in English in every language.

That boundary bites harder here than on a grammar deck. The card headings
on the language slides are often *the phrase being taught* — `net pay`,
`four-way closure`, `vitrinite reflectance`, `fault throw`. Those stay in
English in the German build, because translating them would remove the
thing the learner is here to acquire. Headings that are merely structural
labels — "What it is", "How a seal fails" — are German, as are every
title, note, hint, instruction and results message.

`build_geo.py` reads T['en'] directly, so a slide and its English string
cannot drift apart: there is one copy of each.
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
    coverTitle='The Language of <em>Geoscience</em>',
    coverSub='Technical phrases and field expressions used by practising '
             'geoscientists — from the wellsite to the seminar room',
    chipLevel='C1 &middot; Technical English',
    chipFocus='Subsurface geoscience',
    chipTime='50&ndash;60 minutes',
    chipCount='NN slides',

    # ── eyebrows ──
    tOrient='Orientation',
    tRes='Language focus &middot; Rock, trap and seal',
    tSrc='Language focus &middot; Source rock and logs',
    tStr='Language focus &middot; Structure and pressure',
    tWell='Language focus &middot; Wellsite to production',
    tGlos='Language focus &middot; Glossary',

    # ── 2. orientation ──
    oT='Who this deck is for, and how it works',
    oa='English for practising geoscientists',
    ob='Nothing is tested before it is taught',
    on='Nineteen scored items: six phrases in context, six field-note '
       'sentences and seven report terms. The chip at the top of every slide '
       'shows your running total out of nineteen.',

    # ── 3. porosity ──
    p1T='Porosity: the matrix and the fractures',
    p1a='matrix porosity',
    p1b='fracture porosity',
    p1n='A reservoir with both is said to <strong>exhibit dual porosity '
        'behaviour</strong>: matrix storage feeding fracture flow. Modelling '
        'the two as one system gives the wrong production forecast.',

    # ── 4. traps ──
    p2T='Two ways a trap is made',
    p2a='structural trapping',
    p2b='stratigraphic trapping',
    p2n='Stratigraphic traps are usually subtler on seismic than structural '
        'ones, which is why a review panel will ask whether one has been '
        'ruled out.',

    # ── 5. the seal ──
    p3T='The seal, and how it fails',
    p3a='What seals a trap',
    p3b='How a seal fails',
    p3n='<strong>Seal integrity</strong> is the cap rock&rsquo;s capacity to '
        'keep the column in the trap. Uncertainty about it is one of the '
        'commonest reasons a prospect is risked down.',

    # ── 6. maturity ──
    s1T='Source rock: immature, oil window, overmature',
    s1a='Immature',
    s1b='The oil window',
    s1c='Overmature',
    s1n='Maturity follows burial depth and temperature history, not age '
        'alone. Cracking is the mechanism that turns oil into gas &mdash; not '
        'a separate way of losing it.',

    # ── 7. saturation ──
    s2T='Water saturation and what the logs see',
    s2a='water saturation (Sw)',
    s2b='Why resistivity is read beside it',
    s2n='<strong>Anomalously high water saturation</strong> means a share of '
        'water larger than the other measurements would lead you to expect. '
        'It is a flag for the interpreter, not a result.',

    # ── 8. the resistivity anomaly ──
    s3T='When high resistivity does not mean pay',
    s3a='Wet, and still resistive',
    s3b='The opposite anomaly',
    s3n='Conductive minerals therefore cannot explain an interval that is '
        'both wet and highly resistive: they cause the reverse. Fresh '
        'formation water is the textbook explanation, with very low porosity '
        'and invasion next.',

    # ── 9. cross-bedding ──
    s4T='Cross-bedding and what it records',
    s4a='What it is',
    s4b='What it tells you',
    s4n='Currents build cross-beds in fluvial, aeolian, tidal and deltaic '
        'settings alike, so a field note says the structure is <em>consistent '
        'with</em> a high-energy river system &mdash; never that it proves one.',

    # ── 10. stem glossary ──
    gT='Six terms the questions use',
    ga='four-way closure',
    gb='net pay',
    gc='mud weight',
    gd='bubble point',
    ge='cuttings',
    gf='depth conversion',
    gn='Two more: <em>subsea</em> &mdash; measured from sea level, not from '
       'the rig floor &mdash; and <em>aquifer support</em>, water moving in '
       'from below to hold reservoir pressure up.',

    # ── 11. activity 1 divider ──
    d1T='Reading the formation',
    d1a='Six phrases, each in context',
    d1n='Choose one option. You will be told why your answer was right or '
        'wrong before you move on, so read the feedback even when you score.',

    # ── 18. structure ──
    b1T='Anticlines, crests and closure',
    b1a='the crest',
    b1b='closure',
    b1n='A structure map is contoured on a horizon and quoted in metres '
        'subsea: the crest sits inside the innermost contour, and the surface '
        'deepens outwards from it.',

    # ── 19. pressure ──
    b2T='Pore pressure, overpressure and mud weight',
    b2a='The hydrostatic gradient',
    b2b='overpressure',
    b2n='Too light a mud and the formation flows into the well &mdash; a well '
        'control incident. Too heavy and the mud fractures the formation and '
        'is lost into it.',

    # ── 20. wellsite ──
    b3T='Shows in the cuttings, porosity in the log',
    b3a='oil shows',
    b3b='effective porosity',
    b3n='The two porosities are easy to confuse in a report. A figure quoted '
        'after cut-offs and exclusions is the effective one.',

    # ── 21. time and depth ──
    b4T='From travel time to depth',
    b4a='two-way time',
    b4b='the check-shot survey',
    b4n='Get the velocity model wrong and a mapped crest moves or a closure '
        'disappears. Depth conversion is where a good seismic interpretation '
        'is most often lost.',

    # ── 22. drive mechanisms ──
    b5T='What pushes the oil to the well',
    b5a='solution gas drive',
    b5b='gas cap drive',
    b5c='water drive',
    b5n='With limited aquifer support and no gas cap, solution gas is what is '
        'left &mdash; which is why the recovery factor in that case is '
        'expected to be modest.',

    # ── 29/30. activity 3 glossary ──
    m1T='Seven terms from the report &mdash; maturity, faults, seals',
    m1a='vitrinite reflectance',
    m1b='fault throw',
    m1c='capillary entry pressure',
    m1d='gas&ndash;water contact',
    m1n='Note the pair: throw and heave are the two components of one '
        'displacement, so quoting the wrong one misstates the offset at '
        'reservoir level.',
    m2T='&mdash; and reservoir quality, pressure, facies',
    m2a='net-to-gross ratio',
    m2b='overpressure',
    m2c='facies association',
    m2n='All seven appear in the questions that follow, each inside a '
        'sentence of the kind you would meet in a report.',

    # ── activity headers ──
    a1E='Activity 1 &middot; Reading the formation',
    a1T='What does the phrase mean here?',
    a2E='Activity 2 &middot; Completing the field notes',
    a2T='Choose the phrase that fits',
    a3E='Activity 3 &middot; Correlating the sections',
    a3T='What the term means in the report',
    bankLabel='Word bank:',

    # ── gap hints: the scaffold, never the answer ──
    h1='The cuttings carried traces of oil that no longer moves.',
    h2='The high point of the fold, picked off the structure map.',
    h3='Porosity, but only the part of it that can flow.',
    h4='The pressure of the fluid in the pores, which the mud weight has to '
       'balance.',
    h5='The downhole survey that ties travel time to true depth.',
    h6='The drive mechanism left when there is neither an aquifer nor a gas '
       'cap.',

    # ── results ──
    resPerfect='Full marks. You are reading these phrases the way the report '
               'writer meant them, including the two that turn on a '
               'distinction rather than a definition: effective against total '
               'porosity, and a wet interval that still logs as resistive.',
    resStrong='Strong. Look at where the misses fall. The phrases about rock '
              'and trap tend to be learned once; the ones about pressure, '
              'saturation and drive mechanism have to be re-read against the '
              'numbers every time.',
    resMid='A pass. Go back to the slides on the seal, on water saturation '
           'and on the drive mechanisms. Most of the marks here sit on those '
           'three, and each of them is a distinction rather than a single '
           'term.',
    resLow='Work through the language slides again before you retry. Every '
           'phrase tested here is explained on a slide before the questions '
           'begin, and the glossary slides carry the terms the reports use '
           'around them.',

    # ── activation ──
    actTitle='The prospect review',
    actUse='Use at least four:',
    actSpeakBrief='Your team is presenting a prospect to a joint-venture '
                  'partner. They have read the summary, and they are not yet '
                  'convinced.',
    actSpeak1='Present the trap in two minutes: what makes the closure, what '
              'seals it, and what you know about the source rock charging it.',
    actSpeak2='Swap. As the partner, press on the risk you think is highest '
              '&mdash; seal integrity or charge &mdash; and make the '
              'presenter defend the ranking out loud.',
    actSpeak3='Both: the petrophysicist reports anomalously high water '
              'saturation across an interval that logs as resistive. Agree '
              'what you will tell the partner it might mean.',
    actWriteKind='Writing &middot; 150&ndash;250 words',
    actWriteBrief='Write the reservoir summary for the well completion '
                  'report: what the logs showed over the pay interval, what '
                  'the shows in the cuttings say about charge, and which '
                  'recovery mechanism the model expects. Hedge what is '
                  'uncertain.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does not
    # decode entities — HOUSE-STYLE §13 in its attribute form.
    actPlaceholder='Over the interval 2,380–2,398 m subsea the logs indicate …',
)

T['de'] = dict(
    coverTitle='The Language of <em>Geoscience</em>',
    coverSub='Fachbegriffe und Feldausdrücke, wie sie Geowissenschaftler im '
             'Beruf verwenden — von der Bohrstelle bis zum Vortragssaal',
    chipLevel='C1 &middot; Fachenglisch',
    chipFocus='Geologie des Untergrunds',
    chipTime='50&ndash;60 Minuten',
    chipCount='NN Folien',

    tOrient='Orientierung',
    tRes='Sprachfokus &middot; Gestein, Falle und Abdeckung',
    tSrc='Sprachfokus &middot; Muttergestein und Bohrlochmessung',
    tStr='Sprachfokus &middot; Struktur und Druck',
    tWell='Sprachfokus &middot; Von der Bohrstelle zur Förderung',
    tGlos='Sprachfokus &middot; Glossar',

    oT='Für wen diese Lektion ist und wie sie aufgebaut ist',
    oa='English for practising geoscientists',
    ob='Nichts wird abgefragt, bevor es erklärt wurde',
    on='Neunzehn bewertete Aufgaben: sechs Wendungen im Kontext, sechs '
       'Sätze aus Feldnotizen und sieben Fachbegriffe aus Berichten. Die '
       'Anzeige oben auf jeder Folie zeigt deinen Punktestand von neunzehn.',

    p1T='Porosität: Matrix und Klüfte',
    p1a='matrix porosity',
    p1b='fracture porosity',
    p1n='Ein Reservoir mit beidem <strong>exhibits dual porosity '
        'behaviour</strong>: Die Matrix speichert, die Klüfte leiten. Wer '
        'beides als ein System modelliert, erhält die falsche Förderprognose.',

    p2T='Zwei Arten, wie eine Falle entsteht',
    p2a='structural trapping',
    p2b='stratigraphic trapping',
    p2n='Stratigraphische Fallen sind seismisch meist unauffälliger als '
        'strukturelle. Genau deshalb fragt ein Gutachtergremium, ob sie '
        'ausgeschlossen wurden.',

    p3T='Die Abdeckung und wie sie versagt',
    p3a='Was eine Falle abdichtet',
    p3b='Wie eine Abdeckung versagt',
    p3n='<strong>Seal integrity</strong> ist die Fähigkeit des Deckgebirges, '
        'die Kohlenwasserstoffsäule in der Falle zu halten. Zweifel daran '
        'sind einer der häufigsten Gründe, ein Prospekt abzuwerten.',

    s1T='Muttergestein: unreif, Ölfenster, überreif',
    s1a='Immature &mdash; unreif',
    s1b='The oil window &mdash; das Ölfenster',
    s1c='Overmature &mdash; überreif',
    s1n='Die Reife hängt von Versenkungstiefe und Temperaturgeschichte ab, '
        'nicht vom Alter allein. <em>Cracking</em> ist der Mechanismus, der '
        'Öl in Gas umwandelt — kein zusätzlicher Verlustweg.',

    s2T='Wassersättigung und was die Messungen sehen',
    s2a='water saturation (Sw)',
    s2b='Warum der Widerstand danebensteht',
    s2n='<strong>Anomalously high water saturation</strong> heißt: mehr '
        'Wasser, als die übrigen Messwerte erwarten lassen. Das ist ein '
        'Warnsignal für die Auswertung, kein Ergebnis.',

    s3T='Wenn hoher Widerstand nicht Kohlenwasserstoffe bedeutet',
    s3a='Wasserführend und trotzdem hochohmig',
    s3b='Die umgekehrte Anomalie',
    s3n='Leitfähige Minerale können ein Intervall, das zugleich wasserführend '
        'und hochohmig ist, deshalb nicht erklären: Sie bewirken das '
        'Gegenteil. Süßes Formationswasser ist die Lehrbucherklärung, danach '
        'sehr geringe Porosität und Filtratinvasion.',

    s4T='Schrägschichtung und was sie festhält',
    s4a='Was es ist',
    s4b='Was es dir verrät',
    s4n='Strömungen erzeugen Schrägschichtung in fluviatilen, äolischen, '
        'gezeitengeprägten und deltaischen Milieus gleichermaßen. Eine '
        'Feldnotiz sagt deshalb <em>consistent with</em> — nie, dass es '
        'bewiesen sei.',

    gT='Sechs Begriffe, die in den Aufgaben vorkommen',
    ga='four-way closure',
    gb='net pay',
    gc='mud weight',
    gd='bubble point',
    ge='cuttings',
    gf='depth conversion',
    gn='Zwei weitere: <em>subsea</em> — gemessen ab Meeresspiegel, nicht ab '
       'Bohrtisch — und <em>aquifer support</em>: Wasser strömt von unten '
       'nach und hält den Lagerstättendruck.',

    d1T='Die Formation lesen',
    d1a='Sechs Wendungen, jede im Kontext',
    d1n='Wähle eine Option. Du erfährst vor dem Weiterklicken, warum deine '
        'Antwort richtig oder falsch war — lies die Rückmeldung auch dann, '
        'wenn du punktest.',

    b1T='Antiklinalen, Kulminationen und Schluss',
    b1a='the crest',
    b1b='closure',
    b1n='Eine Strukturkarte wird auf einen Horizont konturiert und in Metern '
        '<em>subsea</em> angegeben: Die Kulmination liegt innerhalb der '
        'innersten Isolinie, nach außen fällt die Fläche ab.',

    b2T='Porendruck, Überdruck und Spülungsgewicht',
    b2a='Der hydrostatische Gradient',
    b2b='overpressure',
    b2n='Ist die Spülung zu leicht, strömt die Formation in die Bohrung — ein '
        '<em>well control incident</em>. Ist sie zu schwer, bricht sie die '
        'Formation auf und geht in ihr verloren.',

    b3T='Spuren im Bohrklein, Porosität im Log',
    b3a='oil shows',
    b3b='effective porosity',
    b3n='Die beiden Porositäten werden in Berichten leicht verwechselt. Ein '
        'Wert, der nach Grenzwerten und Abzügen genannt wird, ist der '
        'effektive.',

    b4T='Von der Laufzeit zur Tiefe',
    b4a='two-way time',
    b4b='the check-shot survey',
    b4n='Stimmt das Geschwindigkeitsmodell nicht, verschiebt sich die '
        'kartierte Kulmination oder der Schluss verschwindet. An der '
        '<em>depth conversion</em> scheitert eine gute seismische '
        'Interpretation am häufigsten.',

    b5T='Was das Öl zur Bohrung treibt',
    b5a='solution gas drive',
    b5b='gas cap drive',
    b5c='water drive',
    b5n='Ohne nennenswerten Aquifer und ohne Gaskappe bleibt das gelöste Gas '
        '— und deshalb erwartet man in diesem Fall einen bescheidenen '
        'Entölungsgrad.',

    m1T='Sieben Begriffe aus dem Bericht &mdash; Reife, Störungen, Abdeckung',
    m1a='vitrinite reflectance',
    m1b='fault throw',
    m1c='capillary entry pressure',
    m1d='gas&ndash;water contact',
    m1n='Beachte das Paar: <em>throw</em> und <em>heave</em> sind die beiden '
        'Komponenten ein und derselben Verschiebung. Die falsche zu nennen, '
        'verfälscht den Versatz auf Reservoirniveau.',
    m2T='&mdash; und Reservoirqualität, Druck, Fazies',
    m2a='net-to-gross ratio',
    m2b='overpressure',
    m2c='facies association',
    m2n='Alle sieben tauchen in den folgenden Aufgaben auf, jeweils in einem '
        'Satz, wie er so in einem Bericht stehen könnte.',

    a1E='Aufgabe 1 &middot; Die Formation lesen',
    a1T='Was bedeutet die Wendung hier?',
    a2E='Aufgabe 2 &middot; Feldnotizen vervollständigen',
    a2T='Wähle die passende Wendung',
    a3E='Aufgabe 3 &middot; Profile korrelieren',
    a3T='Was der Begriff im Bericht bedeutet',
    bankLabel='Wortspeicher:',

    h1='Das Bohrklein enthielt Spuren von Öl, das sich nicht mehr bewegt.',
    h2='Der höchste Punkt der Falte, von der Strukturkarte abgegriffen.',
    h3='Porosität, aber nur der Anteil, der auch fließen kann.',
    h4='Der Druck der Fluide im Porenraum, den das Spülungsgewicht '
       'ausgleichen muss.',
    h5='Die Bohrlochmessung, die Laufzeit an die wahre Tiefe bindet.',
    h6='Der Fördermechanismus, der bleibt, wenn weder Aquifer noch Gaskappe '
       'da sind.',

    resPerfect='Volle Punktzahl. Du liest diese Wendungen so, wie der '
               'Berichtschreiber sie gemeint hat — auch die beiden, bei denen '
               'es auf eine Unterscheidung ankommt und nicht auf eine '
               'Definition: effektive gegen totale Porosität, und ein '
               'wasserführendes Intervall, das trotzdem hochohmig misst.',
    resStrong='Stark. Sieh dir an, wo die Fehler liegen. Die Wendungen zu '
              'Gestein und Falle lernt man einmal; die zu Druck, Sättigung '
              'und Fördermechanismus muss man jedes Mal neu gegen die Zahlen '
              'lesen.',
    resMid='Bestanden. Geh noch einmal zu den Folien über die Abdeckung, über '
           'die Wassersättigung und über die Fördermechanismen. Dort liegen '
           'die meisten Punkte, und jedes dieser drei Themen ist eine '
           'Unterscheidung und kein Einzelbegriff.',
    resLow='Arbeite die Sprachfolien noch einmal durch, bevor du es erneut '
           'versuchst. Jede hier abgefragte Wendung steht vor den Aufgaben '
           'auf einer Folie, und die Glossarfolien tragen die Begriffe, die '
           'in den Berichten daneben stehen.',

    actTitle='Die Prospektbesprechung',
    actUse='Mindestens vier verwenden:',
    actSpeakBrief='Euer Team stellt einem Joint-Venture-Partner ein Prospekt '
                  'vor. Er hat die Zusammenfassung gelesen und ist noch nicht '
                  'überzeugt.',
    actSpeak1='Stell die Falle in zwei Minuten vor: Was erzeugt den Schluss, '
              'was dichtet ihn ab, und was weißt du über das Muttergestein, '
              'das sie füllt?',
    actSpeak2='Tauscht die Rollen. Bohre als Partner bei dem Risiko nach, das '
              'du für das größte hältst &mdash; <em>seal integrity</em> oder '
              'Füllung &mdash; und lass die Reihenfolge laut begründen.',
    actSpeak3='Beide: Die Petrophysik meldet <em>anomalously high water '
              'saturation</em> über einem Intervall, das hochohmig misst. '
              'Einigt euch auf eine mögliche Erklärung für den Partner.',
    actWriteKind='Schreiben &middot; 150&ndash;250 Wörter',
    actWriteBrief='Schreibe die Reservoir-Zusammenfassung für den '
                  '<em>well completion report</em>: was die Messungen über '
                  'dem Nettomächtigkeitsintervall gezeigt haben, was die '
                  'Spuren im Bohrklein über die Füllung sagen und welchen '
                  'Fördermechanismus das Modell erwartet. Formuliere '
                  'Unsicheres vorsichtig.',
    # A real character, not an entity: applyLang assigns this to
    # el.placeholder as a JS string, and a DOM property assignment does not
    # decode entities — HOUSE-STYLE §13 in its attribute form.
    actPlaceholder='Over the interval 2,380–2,398 m subsea the logs indicate …',
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
