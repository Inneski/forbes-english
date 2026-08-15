# -*- coding: utf-8 -*-
"""Interface strings for the nature agency vocabulary deck, Part 2.

English and German, both complete. The generic chrome — buttons, score
label, the plural-aware word counter — is lifted verbatim from
`chrome_i18n.py` rather than retranslated, because it is identical in
every deck on the site.

Scope boundary, per the house style: the app's own chrome translates, the
English being taught does not. Question stems, options, gap sentences,
the sixteen field terms, the example sentences and the activation chips
all stay in English in every language.
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
    coverTitle='The Wildlife and <em>Countryside</em> Agency',
    coverSub='Vocabulary in the field, Part 2 — eight confusable pairs, '
             'seventeen briefings and sixteen terms',
    chipLevel='C1 &middot; Part 2 of 2',
    chipFocus='Word choice &amp; register',
    chipCount='NN slides',

    # ── front matter ──
    b1E='Before you begin', b1T='Six weeks in',
    b1ah='Where you are', b1bh='Part 1 comes first',
    b1bn='You can take this part on its own, but you will be choosing between '
         'a word you have been taught and a word you have not. Part 1 removes '
         'that guesswork.',
    bhE='Before you begin', bhT='The hide',
    b2E='Before you begin', b2T='Four words the briefings assume you know',
    b2n='All four appear inside question stems later on. They are glossed here '
        'so that no item is testing whether you happen to know the jargon.',

    # ── teaching ──
    tpE='Confusable pairs', tfE='Field language',

    t1T='Three questions that separate a pair',
    t1ah='1 &middot; What does it go with?',
    t1bh='2 &middot; What follows it?',
    t1ch='3 &middot; Who says it?',
    t1cn='Every pair ahead yields to one of these three. Ask them in order: '
         'what it goes with, what follows it, who says it.',

    t2T='stressy / stressful',
    t2n='This pair turns on register as much as sense. <em>Stressy</em> '
        'belongs in the staff room; a written report says <em>anxious</em>.',

    t3T='physician / physicist',
    t3ah='-ian &rarr; the practitioner',
    t3bh='-ist &rarr; the specialist, -er &rarr; the doer',
    t3n='All three endings name a <em>person</em>, so the ending alone will '
        'not choose for you &mdash; but it does tell you the option is a '
        'person and not an act. A physician treats you; a physicist models '
        'your floodwater.',

    t4T='offence / offender', t4ah='the act', t4bh='the person',
    t4n='British English spells the act <em>offence</em>; American English '
        'spells it <em>offense</em>. The person is <em>offender</em> on both '
        'sides of the Atlantic. This lesson is British throughout.',

    t5T='mystical / mysterious',
    t5n='A quick test. If somebody has opened an inquiry, the thing is '
        '<em>mysterious</em>. If somebody has lit a candle, it is '
        '<em>mystical</em>.',

    t6T='defraud / swindle &mdash; what follows',
    t6n='Same crime, different frame. <em>Out of</em> is the single most '
        'reliable signal that <em>swindle</em> is the verb wanted: it is the '
        'pattern that decides, not the meaning.',

    t7T='One root, four slots',
    t7n='The verb, the noun and the adjective are each tested in a different '
        'section of this lesson. Knowing the family lets you move between them '
        'inside a sentence instead of reaching for the one form you remember.',

    t8T='legal / logical',
    t8n='A decision can be legal and not logical, or logical and not legal. '
        'Ask which authority the sentence is appealing to: a statute, or an '
        'argument.',

    t9T='a requirement / several requirements',
    t9ah='the determiner decides',
    t9bh='and a collective noun takes either',
    t9n='British English lets a collective noun take a plural verb when you '
        'mean the individuals in it &mdash; <em>the team prefer</em>, <em>the '
        'panel disagree</em>, <em>the government are divided</em>. Both forms '
        'are correct; the meaning shifts.',

    t10T='revoke / resist',
    t10ah='revoke + something you granted',
    t10bh='resist + something pulling at you',
    t10n='Two verbs of refusal separated entirely by what follows them. '
         'Nothing grants you a temptation, and no permit pulls.',

    t11T='Report English and staff-room English',
    t11ah='in the staff room', t11bh='in the written report',
    t11n='Nothing in the left-hand column is wrong English. All of it is wrong '
         'in a document a landowner&rsquo;s solicitor may read. Knowing a word '
         'is not the same as knowing where it goes.',

    t12T='Four teeth, front to back',
    t12n='Carnivores carry the enlarged canine, which is the tooth the trapped '
         'fox had fractured. Three of these four turn up as wrong options and '
         'are worth knowing on sight.',

    t13T='crane, flock, survey',
    t13n='Two of these have a second meaning that arrives first for most '
         'learners &mdash; the machine, and land measurement. On a reserve it '
         'is the bird and the habitat sense that are in use.',

    t14T='Taking it into account',
    t14ah='four ways to say it', t14bh='spark and ignite',
    t14n='The four phrases on the left are interchangeable in a briefing. '
         '<em>Spark</em> is the one that has quietly become a verb about '
         'causes rather than about fire &mdash; and that is now its commonest '
         'use in a report.',

    # ── section dividers ──
    d1E='Section 1 of 3', d1T='Word choice',
    d1n='The options are shuffled every time the deck loads, so the letters '
        'mean nothing. Read all four before you choose.',
    d2E='Section 2 of 3', d2T='Complete the briefing',
    d2n='The line above each sentence gives you the sense and the length. '
        'Press Enter, or use Check, to mark the slide.',
    d3E='Section 3 of 3', d3T='Sixteen field terms',
    d3n='The first box you choose for a word is the one that scores. Put it in '
        'the wrong box and the point is gone, so read before you place.',

    # ── activity headers ──
    s1E='Section 1 &middot; Word choice', s1T='Choose the word that fits',
    s2E='Section 2 &middot; Complete the briefing',
    s2T='Type the missing word',
    s3rE='Section 3 &middot; The terms',
    s3aT='Sixteen field terms &mdash; 1 of 4',
    s3bT='Sixteen field terms &mdash; 2 of 4',
    s3cT='Sixteen field terms &mdash; 3 of 4',
    s3dT='Sixteen field terms &mdash; 4 of 4',
    s3E='Section 3 &middot; Sort by sense',
    s3s1T='Which field does the word belong to?',
    s3s2T='Which field does the word belong to?',
    s3s3T='Short and sudden, or slow and repeating?',
    s3s1h='Click a word, then click the box it belongs in. The first box you '
          'choose is the one that counts.',
    s3s2h='Click a word, then click the box it belongs in. The first box you '
          'choose is the one that counts.',
    s3s3h='Click a word, then click the box it belongs in. The first box you '
          'choose is the one that counts.',

    # ── gap hints: sense plus length, before the answer ──
    g1h='A sharp division or split, used of rock structure &mdash; 8 letters, '
        'begins with c.',
    g2h='Two words completing the idiom &ldquo;to consider something alongside '
        'other factors&rdquo;.',
    g3h='First: a tall stand with a sloping top for a speaker&rsquo;s notes '
        '&mdash; 7 letters. Second: a round, domed room &mdash; 7 letters, '
        'begins with r.',
    g4h='First: to gently calm a frightened animal &mdash; 6 letters, begins '
        'with s. Second: to catch and twist something up in something else '
        '&mdash; 8 letters.',
    g5h='First: casual, unconfirmed talk about other people &mdash; 6 letters. '
        'Second: what something is worth, as a figure &mdash; 5 letters.',
    g6h='First: warm approval expressed openly &mdash; 6 letters. Second: to '
        'complain in a low-level, bad-tempered way &mdash; 7 letters.',
    g7h='First: to like one option better than another &mdash; watch the '
        'agreement after a collective noun. Second: informal &mdash; a public '
        'performance, 3 letters.',
    g8h='The high-street professional who tests eyesight and fits glasses '
        '&mdash; 8 letters, and one of the <em>-ian</em> family.',
    g9h='A chair fitted with wheels, used by people who cannot walk unaided '
        '&mdash; one word, 10 letters.',
    g10h='A road junction where traffic circles a central island &mdash; 10 '
         'letters, and thoroughly British.',
    g11h='A two-word phrase for somebody who enjoys and is good at dealing '
         'with others.',
    g12h='The distinctive parts or aspects of something &mdash; plural noun, '
         '8 letters.',

    # ── results ──
    resPerfect='Full marks. You are separating the pairs by collocation and '
               'register rather than by feel, which is exactly what C1 asks '
               'for.',
    resStrong='Strong. Look at where the misses cluster: if they sit in '
              'Section 1, go back to the pair slides; if they sit in Section '
              '2, it is recall rather than choice, and that is a different '
              'kind of practice.',
    resMid='A solid pass. The eight pair slides carry most of the marks on '
           'this deck &mdash; work through them again and ask the three '
           'questions in order before you answer.',
    resLow='Take the teaching slides again before you retry, and take Part 1 '
           'first if you have not. Every rule tested here is taught before the '
           'questions start.',

    # ── activation ──
    actTitle='The permit letter', actUse='Use at least four:',
    actSpeakBrief='A landowner has just been told his access permit is being '
                  'revoked after a third breach.',
    actSpeak1='One of you is the field officer. Deliver the decision, name the '
              'byelaw and hold the line when he pushes back.',
    actSpeak2='Swap roles. This time the landowner says a consultant swindled '
              'him out of the grant that paid for the work. Take that into '
              'account &mdash; without reversing the decision.',
    actSpeak3='Both: your draft newsletter says the team were <em>stressy</em> '
              'about the inspection and that Tomas had a <em>gig</em>. Argue '
              'the register, item by item, and agree a written version.',
    actWriteKind='Writing &middot; 150&ndash;250 words',
    actWriteBrief='Write the site note that goes to the landowner&rsquo;s '
                  'solicitor: what the breach was, which byelaw applies, and '
                  'what happens next. Report register throughout &mdash; '
                  'nothing from the staff room.',
    actPlaceholder='Following the site visit of 14 March, the Agency has '
                   'revoked …',
)

T['de'] = dict(
    coverTitle='The Wildlife and <em>Countryside</em> Agency',
    coverSub='Fachwortschatz im Gelände, Teil 2 — acht verwechselbare Paare, '
             'siebzehn Einträge und sechzehn Begriffe',
    chipLevel='C1 &middot; Teil 2 von 2',
    chipFocus='Wortwahl &amp; Register',
    chipCount='NN Folien',

    b1E='Bevor du beginnst', b1T='Sechs Wochen im Dienst',
    b1ah='Wo du bist', b1bh='Teil 1 kommt zuerst',
    b1bn='Du kannst diesen Teil auch allein bearbeiten, aber dann wählst du '
         'zwischen einem Wort, das dir beigebracht wurde, und einem, das dir '
         'nicht beigebracht wurde. Teil 1 nimmt dieses Raten heraus.',
    bhE='Bevor du beginnst',
    bhT='The hide',
    b2E='Bevor du beginnst',
    b2T='Vier Wörter, die die Aufgaben voraussetzen',
    b2n='Alle vier tauchen später in den Aufgabentexten auf. Sie werden hier '
        'erklärt, damit keine Aufgabe abfragt, ob du zufällig das Fachwort '
        'kennst.',

    tpE='Verwechselbare Paare', tfE='Sprache im Gelände',

    t1T='Drei Fragen, die ein Paar trennen',
    t1ah='1 &middot; Womit steht es zusammen?',
    t1bh='2 &middot; Was folgt darauf?',
    t1ch='3 &middot; Wer sagt es?',
    t1cn='Jedes Paar auf den folgenden Folien lässt sich mit einer dieser drei '
         'Fragen klären. Stelle sie in dieser Reihenfolge: Womit steht es '
         'zusammen, was folgt darauf, wer sagt es.',

    t2T='stressy / stressful',
    t2n='Bei diesem Paar entscheidet das Register genauso stark wie die '
        'Bedeutung. <em>Stressy</em> gehört in den Pausenraum; ein '
        'schriftlicher Bericht schreibt <em>anxious</em>.',

    t3T='physician / physicist',
    t3ah='-ian &rarr; die ausübende Person',
    t3bh='-ist &rarr; die Fachperson, -er &rarr; die handelnde Person',
    t3n='Alle drei Endungen bezeichnen eine <em>Person</em>, die Endung allein '
        'entscheidet also nicht &mdash; sie sagt dir aber, dass die Option '
        'eine Person ist und keine Handlung. Ein physician behandelt dich; ein '
        'physicist modelliert dein Hochwasser.',

    t4T='offence / offender', t4ah='die Tat', t4bh='die Person',
    t4n='Im britischen Englisch schreibt man die Tat <em>offence</em>, im '
        'amerikanischen <em>offense</em>. Die Person heißt beiderseits des '
        'Atlantiks <em>offender</em>. Diese Lektion ist durchgehend britisch.',

    t5T='mystical / mysterious',
    t5n='Eine schnelle Probe: Wenn jemand eine Untersuchung eingeleitet hat, '
        'ist die Sache <em>mysterious</em>. Wenn jemand eine Kerze angezündet '
        'hat, ist sie <em>mystical</em>.',

    t6T='defraud / swindle &mdash; was danach folgt',
    t6n='Dasselbe Delikt, ein anderer Rahmen. <em>Out of</em> ist das '
        'verlässlichste Signal dafür, dass <em>swindle</em> gemeint ist: Es '
        'entscheidet das Muster, nicht die Bedeutung.',

    t7T='Eine Wurzel, vier Formen',
    t7n='Verb, Substantiv und Adjektiv werden in dieser Lektion jeweils in '
        'einem anderen Abschnitt abgefragt. Wer die Wortfamilie kennt, kann im '
        'Satz zwischen den Formen wechseln, statt immer zu der einen Form zu '
        'greifen, die gerade einfällt.',

    t8T='legal / logical',
    t8n='Eine Entscheidung kann legal und unlogisch sein oder logisch und '
        'nicht legal. Frage, auf welche Instanz sich der Satz beruft: auf ein '
        'Gesetz oder auf ein Argument.',

    t9T='a requirement / several requirements',
    t9ah='der Begleiter entscheidet',
    t9bh='und ein Sammelbegriff nimmt beides',
    t9n='Im britischen Englisch darf ein Sammelbegriff ein Verb im Plural '
        'nehmen, wenn die einzelnen Mitglieder gemeint sind &mdash; <em>the '
        'team prefer</em>, <em>the panel disagree</em>, <em>the government are '
        'divided</em>. Beide Formen sind richtig; die Bedeutung verschiebt '
        'sich.',

    t10T='revoke / resist',
    t10ah='revoke + etwas, das man gewährt hat',
    t10bh='resist + etwas, das an einem zieht',
    t10n='Zwei Verben der Verweigerung, unterschieden allein durch das, was '
         'darauf folgt. Niemand gewährt dir eine Versuchung, und keine '
         'Genehmigung zieht an dir.',

    t11T='Berichtsenglisch und Pausenraumenglisch',
    t11ah='im Pausenraum', t11bh='im schriftlichen Bericht',
    t11n='Nichts in der linken Spalte ist falsches Englisch. Alles davon ist '
         'falsch in einem Dokument, das die Anwältin eines Grundbesitzers '
         'lesen könnte. Ein Wort zu kennen ist nicht dasselbe, wie zu wissen, '
         'wohin es gehört.',

    t12T='Vier Zähne, von vorn nach hinten',
    t12n='Fleischfresser haben den vergrößerten canine &mdash; genau den Zahn, '
         'den der Fuchs in der Falle gebrochen hatte. Drei dieser vier '
         'erscheinen als falsche Antwortmöglichkeiten und lohnen sich auf den '
         'ersten Blick.',

    t13T='crane, flock, survey',
    t13n='Zwei davon haben eine zweite Bedeutung, die den meisten Lernenden '
         'zuerst einfällt &mdash; der Kran und die Landvermessung. Im '
         'Schutzgebiet sind der Vogel und die Kartierung gemeint.',

    t14T='Etwas berücksichtigen',
    t14ah='vier Arten, es zu sagen', t14bh='spark und ignite',
    t14n='Die vier Wendungen links sind in einem Bericht austauschbar. '
         '<em>Spark</em> ist die, die still und leise zu einem Verb über '
         'Ursachen geworden ist statt über Feuer &mdash; und das ist heute '
         'ihre häufigste Verwendung im Bericht.',

    d1E='Abschnitt 1 von 3', d1T='Wortwahl',
    d1n='Die Antwortmöglichkeiten werden bei jedem Laden neu gemischt, die '
        'Buchstaben bedeuten also nichts. Lies alle vier, bevor du wählst.',
    d2E='Abschnitt 2 von 3', d2T='Ergänze den Eintrag',
    d2n='Die Zeile über jedem Satz nennt dir die Bedeutung und die Länge. '
        'Drücke Enter oder klicke auf Prüfen, um die Folie auszuwerten.',
    d3E='Abschnitt 3 von 3', d3T='Sechzehn Fachbegriffe',
    d3n='Die erste Box, die du für ein Wort wählst, zählt. Landet es in der '
        'falschen Box, ist der Punkt weg &mdash; also erst lesen, dann legen.',

    s1E='Abschnitt 1 &middot; Wortwahl', s1T='Wähle das passende Wort',
    s2E='Abschnitt 2 &middot; Ergänze den Eintrag',
    s2T='Tippe das fehlende Wort',
    s3rE='Abschnitt 3 &middot; Die Begriffe',
    s3aT='Sechzehn Fachbegriffe &mdash; 1 von 4',
    s3bT='Sechzehn Fachbegriffe &mdash; 2 von 4',
    s3cT='Sechzehn Fachbegriffe &mdash; 3 von 4',
    s3dT='Sechzehn Fachbegriffe &mdash; 4 von 4',
    s3E='Abschnitt 3 &middot; Nach Bedeutung sortieren',
    s3s1T='In welches Feld gehört das Wort?',
    s3s2T='In welches Feld gehört das Wort?',
    s3s3T='Kurz und plötzlich oder langsam und wiederkehrend?',
    s3s1h='Klicke ein Wort an und dann die Box, in die es gehört. Die erste '
          'Box, die du wählst, zählt.',
    s3s2h='Klicke ein Wort an und dann die Box, in die es gehört. Die erste '
          'Box, die du wählst, zählt.',
    s3s3h='Klicke ein Wort an und dann die Box, in die es gehört. Die erste '
          'Box, die du wählst, zählt.',

    g1h='Eine scharfe Trennung oder Spaltung, hier über den Aufbau von Gestein '
        '&mdash; 8 Buchstaben, beginnt mit c.',
    g2h='Zwei Wörter, die die Wendung „etwas neben anderen Faktoren '
        'berücksichtigen“ vervollständigen.',
    g3h='Erstens: ein hohes Pult mit schräger Ablage für die Notizen einer '
        'sprechenden Person &mdash; 7 Buchstaben. Zweitens: ein runder Raum '
        'mit Kuppel &mdash; 7 Buchstaben, beginnt mit r.',
    g4h='Erstens: ein verängstigtes Tier sanft beruhigen &mdash; 6 Buchstaben, '
        'beginnt mit s. Zweitens: etwas in etwas anderem verfangen oder '
        'verwickeln &mdash; 8 Buchstaben.',
    g5h='Erstens: beiläufiges, unbestätigtes Gerede über andere &mdash; 6 '
        'Buchstaben. Zweitens: was etwas als Zahl wert ist &mdash; 5 '
        'Buchstaben.',
    g6h='Erstens: offen ausgesprochene Anerkennung &mdash; 6 Buchstaben. '
        'Zweitens: sich auf leise, mürrische Art beschweren &mdash; 7 '
        'Buchstaben.',
    g7h='Erstens: eine Möglichkeit lieber mögen als eine andere &mdash; achte '
        'auf die Kongruenz nach einem Sammelbegriff. Zweitens: umgangs&shy;'
        'sprachlich &mdash; ein öffentlicher Auftritt, 3 Buchstaben.',
    g8h='Die Fachkraft auf der Einkaufsstraße, die das Sehvermögen prüft und '
        'Brillen anpasst &mdash; 8 Buchstaben, aus der <em>-ian</em>-Familie.',
    g9h='Ein Stuhl mit Rädern für Menschen, die nicht selbstständig gehen '
        'können &mdash; ein Wort, 10 Buchstaben.',
    g10h='Eine Kreuzung, an der der Verkehr um eine Mittelinsel fährt &mdash; '
         '10 Buchstaben, und durch und durch britisch.',
    g11h='Eine Wendung aus zwei Wörtern für jemanden, der gern und gut mit '
         'anderen Menschen umgeht.',
    g12h='Die charakteristischen Teile oder Aspekte von etwas &mdash; '
         'Substantiv im Plural, 8 Buchstaben.',

    resPerfect='Volle Punktzahl. Du trennst die Paare über Kollokation und '
               'Register statt über Gefühl &mdash; genau das verlangt C1.',
    resStrong='Stark. Schau, wo sich die Fehler häufen: Liegen sie in '
              'Abschnitt 1, gehe zurück zu den Paar-Folien; liegen sie in '
              'Abschnitt 2, geht es um Abruf und nicht um Auswahl, und das ist '
              'eine andere Art von Übung.',
    resMid='Sicher bestanden. Die acht Paar-Folien tragen die meisten Punkte '
           'dieses Decks &mdash; arbeite sie noch einmal durch und stelle die '
           'drei Fragen der Reihe nach, bevor du antwortest.',
    resLow='Lies die Erklärfolien noch einmal, bevor du es erneut versuchst, '
           'und mache zuerst Teil 1, falls noch nicht geschehen. Jede hier '
           'abgefragte Regel wird vor den Aufgaben erklärt.',

    actTitle='Der Brief zur Genehmigung', actUse='Mindestens vier verwenden:',
    actSpeakBrief='Einem Grundbesitzer wurde soeben mitgeteilt, dass seine '
                  'Zugangsgenehmigung nach dem dritten Verstoß entzogen wird.',
    actSpeak1='Eine Person ist die Aufsichtsperson im Gelände. Teile die '
              'Entscheidung mit, nenne die byelaw und bleibe dabei, wenn '
              'Widerspruch kommt.',
    actSpeak2='Tauscht die Rollen. Diesmal sagt der Grundbesitzer, ein Berater '
              'habe ihn um die Fördermittel gebracht, mit denen die Arbeiten '
              'bezahlt wurden. Berücksichtige das &mdash; ohne die '
              'Entscheidung zurückzunehmen.',
    actSpeak3='Beide: Im Entwurf eures Rundbriefs steht, das Team sei '
              '<em>stressy</em> wegen der Inspektion gewesen und Tomas habe '
              'einen <em>gig</em> gehabt. Diskutiert das Register Punkt für '
              'Punkt und einigt euch auf eine schriftliche Fassung.',
    actWriteKind='Schreiben &middot; 150&ndash;250 Wörter',
    actWriteBrief='Schreibe die Aktennotiz an die Anwältin des '
                  'Grundbesitzers: worin der Verstoß bestand, welche byelaw '
                  'greift und wie es weitergeht. Durchgehend Berichtsregister '
                  '&mdash; nichts aus dem Pausenraum.',
    actPlaceholder='Following the site visit of 14 March, the Agency has '
                   'revoked …',
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
