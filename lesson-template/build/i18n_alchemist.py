# -*- coding: utf-8 -*-
"""Interface strings for The Alchemist B2, English and German.

Vocabulary notes and reading notes are attached from the data tables in
build_alchemist.py rather than retyped.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME
import build_alchemist as B

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='The <em>Alchemist</em>',
    coverSub='Santiago, the desert, and the past perfect — a B2 reading and '
             'grammar lesson on Paulo Coelho&rsquo;s novel',
    chipLevel='B2 &middot; Literature', chipFocus='Narrative past tenses',
    chipCount='31 slides',

    alE='Before you read', alT='What alchemy actually was',
    al1h='The stated goal',
    al1n='Practised across the Islamic world, China, India and Europe for well '
         'over a thousand years, by people who were entirely serious.',
    al2h='What it really produced',
    al2n='Newton wrote more on alchemy than on physics. Modern chemistry grew '
         'directly out of it.',
    al3h='What the novel does with it',
    al3n='Santiago is not trying to make gold. He is the material being '
         'worked on.',
    whE='Before you read', whT='Who is who',
    wh1h='Santiago',
    wh1n='He is never named in some translations — he is simply &ldquo;the '
         'boy&rdquo;.',
    wh2h='The old man &middot; the crystal merchant',
    wh2n='The old man claims to be Melchizedek, a king. The merchant is the '
         'counter-example: a man who has a dream and will not go.',
    wh3h='The Englishman &middot; Fatima &middot; the alchemist',
    wh3n='The Englishman studies alchemy in books; the alchemist practises it. '
         'The book has a view about which of the two learns anything.',
    ktE='Before you read', ktT='Two terms the book invents',
    kt1h='Personal Legend',
    kt1n='Capitalised throughout, as a proper noun. In the Portuguese original '
         'it is <em>Lenda Pessoal</em>.',
    kt2h='The Soul of the World',
    kt2n='This is the book&rsquo;s metaphysics in one phrase, and it is what '
         'the alchemist teaches Santiago to listen to.',
    kt3h='Omens',
    kt3n='The first vocabulary word in this lesson, and the mechanism the '
         'entire plot runs on.',

    rdE='The story',
    rdT1='The story so far &mdash; 1 of 5', rdT2='The story so far &mdash; 2 of 5',
    rdT3='The story so far &mdash; 3 of 5', rdT4='The story so far &mdash; 4 of 5',
    rdT5='The story so far &mdash; 5 of 5',
    cE='Comprehension', cT='Check your understanding',

    vE='Vocabulary',
    vT1='Ten words (1 of 3)', vT2='Ten words (2 of 3)', vT3='Ten words (3 of 3)',
    vgE='Vocabulary in use', vgT='Complete the sentence',
    vgHint='Eight words in the bank, six gaps. Two are not needed.',
    bankLabel='Word bank:',
    vmE='Vocabulary', vmT='Match the word to its meaning',
    vmHint='Click a word, then click its meaning.',

    g1E='Grammar &middot; narrative past',
    g1T='The past perfect: had + past participle',
    g1ah='What it does',
    g1an='He sold the sheep because he <em>had decided</em> to go. Deciding '
         'first, selling second.',
    g1bh='The form',
    g1bn='No <em>has</em>, no agreement, no exceptions. Negative: '
         '<em>hadn&rsquo;t told</em>.',
    g1ch='Adverb placement',
    g1cn='Between the auxiliary and the participle. <em>Already had left</em> '
         'is the commonest slip.',
    g2E='Grammar &middot; narrative past', g2T='When you do NOT need it',
    g2ah='When the order is already clear',
    g2an='<em>Before</em> and <em>after</em> do the ordering themselves, so '
         'the past perfect becomes optional here. Both versions of that '
         'sentence are correct English.',
    g2bh='When events are told in order',
    g2bn='Three past simples. Reaching for <em>had</em> here says these '
         'happened before some other past moment — and there isn&rsquo;t one.',
    g2ch='The test',
    g2cn='If yes, use it. If you are just moving forwards, past simple. '
         'Overusing the past perfect is as wrong as missing it, and much more '
         'common at B2.',
    gqE='Grammar &middot; practice', gqT='Past simple or past perfect?',
    ggE='Grammar &middot; practice', ggT='Write the correct form',
    ggHint='Use the words in brackets. Decide first whether you are stepping '
           'back.',

    actTitle='Personal Legends', actUse='Use at least four:',
    actWriteKind='Writing &middot; 200–250 words',
    actSpeakBrief='The crystal merchant has a dream and never goes. Santiago '
                  'goes. One of you defends each.',
    actSpeak1='Merchant&rsquo;s side: argue that the dream is worth more '
              'unrealised. Use <em>by the time</em> once.',
    actSpeak2='Santiago&rsquo;s side: argue the opposite, and use <em>had '
              'already</em> at least twice.',
    actSpeak3='Both: tell one true story about giving something up. Two past '
              'perfects, no more &mdash; watch the overuse.',
    actSpeak4='Both: agree on what the novel is actually claiming, in one '
              'sentence, and say whether you believe it.',
    actWriteBrief='Is a Personal Legend a useful idea or a comforting one? Use '
                  'the novel as evidence, in narrative past tenses, and step '
                  'back with the past perfect at least twice.',
    actPlaceholder='Santiago had been content with his flock long before the '
                   'dream first came…',
    resPerfect='Full marks. You can tell when the past perfect is doing work '
               'and when it is just decoration.',
    resStrong='Strong. If your misses were in the grammar, check whether you '
              'were reaching for <em>had</em> when the events were already in '
              'order.',
    resMid='A solid pass. Read the &ldquo;when you do NOT need it&rdquo; slide '
           'again — overuse is the commoner error at B2.',
    resLow='Go back through the five story slides and the two grammar slides, '
           'then run it again.',
)

T['de'] = dict(
    coverTitle='The <em>Alchemist</em>',
    coverSub='Santiago, die Wüste und das Past Perfect — eine B2-Lektion zu '
             'Lesen und Grammatik über Paulo Coelhos Roman',
    chipLevel='B2 &middot; Literatur', chipFocus='Erzählzeiten der Vergangenheit',
    chipCount='31 Folien',

    alE='Bevor du liest', alT='Was Alchemie tatsächlich war',
    al1h='Das erklärte Ziel',
    al1n='Über mehr als tausend Jahre in der islamischen Welt, in China, '
         'Indien und Europa betrieben — von Menschen, die es vollkommen ernst '
         'meinten.',
    al2h='Was dabei wirklich entstand',
    al2n='Newton schrieb mehr über Alchemie als über Physik. Die moderne '
         'Chemie ist direkt daraus hervorgegangen.',
    al3h='Was der Roman damit macht',
    al3n='Santiago will kein Gold herstellen. Er ist das Material, an dem '
         'gearbeitet wird.',
    whE='Bevor du liest', whT='Wer ist wer',
    wh1h='Santiago',
    wh1n='In manchen Übersetzungen wird er nie benannt — er heißt schlicht '
         '„der Junge“.',
    wh2h='Der alte Mann &middot; der Kristallhändler',
    wh2n='Der alte Mann gibt sich als König Melchisedek aus. Der Händler ist '
         'das Gegenbeispiel: jemand mit einem Traum, der nicht aufbricht.',
    wh3h='Der Engländer &middot; Fatima &middot; der Alchemist',
    wh3n='Der Engländer studiert Alchemie in Büchern; der Alchemist übt sie '
         'aus. Der Roman hat eine klare Meinung dazu, wer von beiden etwas '
         'lernt.',
    ktE='Bevor du liest', ktT='Zwei Begriffe, die der Roman erfindet',
    kt1h='Personal Legend',
    kt1n='Durchgehend großgeschrieben, wie ein Eigenname. Im portugiesischen '
         'Original: <em>Lenda Pessoal</em>.',
    kt2h='The Soul of the World',
    kt2n='Die Metaphysik des Buches in einer Wendung — und genau das lehrt der '
         'Alchemist Santiago wahrzunehmen.',
    kt3h='Omens',
    kt3n='Das erste Vokabel dieser Lektion und der Mechanismus, auf dem die '
         'ganze Handlung läuft.',

    rdE='Die Geschichte',
    rdT1='Die Geschichte bisher &mdash; 1 von 5',
    rdT2='Die Geschichte bisher &mdash; 2 von 5',
    rdT3='Die Geschichte bisher &mdash; 3 von 5',
    rdT4='Die Geschichte bisher &mdash; 4 von 5',
    rdT5='Die Geschichte bisher &mdash; 5 von 5',
    cE='Leseverständnis', cT='Prüfe dein Verständnis',

    vE='Wortschatz',
    vT1='Zehn Wörter (1 von 3)', vT2='Zehn Wörter (2 von 3)',
    vT3='Zehn Wörter (3 von 3)',
    vgE='Wortschatz im Einsatz', vgT='Vervollständige den Satz',
    vgHint='Acht Wörter in der Liste, sechs Lücken. Zwei werden nicht '
           'gebraucht.',
    bankLabel='Wortliste:',
    vmE='Wortschatz', vmT='Ordne dem Wort seine Bedeutung zu',
    vmHint='Klicke ein Wort an und dann seine Bedeutung.',

    g1E='Grammatik &middot; Erzählzeiten',
    g1T='Das Past Perfect: had + Partizip Perfekt',
    g1ah='Was es leistet',
    g1an='He sold the sheep because he <em>had decided</em> to go. Zuerst die '
         'Entscheidung, dann der Verkauf.',
    g1bh='Die Form',
    g1bn='Kein <em>has</em>, keine Anpassung, keine Ausnahmen. Verneinung: '
         '<em>hadn&rsquo;t told</em>.',
    g1ch='Stellung des Adverbs',
    g1cn='Zwischen Hilfsverb und Partizip. <em>Already had left</em> ist der '
         'häufigste Fehler.',
    g2E='Grammatik &middot; Erzählzeiten', g2T='Wann du es NICHT brauchst',
    g2ah='Wenn die Reihenfolge schon klar ist',
    g2an='<em>Before</em> und <em>after</em> ordnen die Ereignisse selbst; '
         'damit wird das Past Perfect hier optional. Beide Fassungen dieses '
         'Satzes sind korrektes Englisch.',
    g2bh='Wenn die Ereignisse der Reihe nach erzählt werden',
    g2bn='Dreimal Past Simple. Ein <em>had</em> würde behaupten, all das sei '
         'vor einem anderen Zeitpunkt geschehen — und den gibt es nicht.',
    g2ch='Die Probe',
    g2cn='Wenn ja, benutze es. Wenn du nur vorwärts erzählst: Past Simple. '
         'Übermäßiger Gebrauch ist genauso falsch wie ein fehlendes Past '
         'Perfect — und auf B2 sehr viel häufiger.',
    gqE='Grammatik &middot; Übung', gqT='Past Simple oder Past Perfect?',
    ggE='Grammatik &middot; Übung', ggT='Schreibe die richtige Form',
    ggHint='Benutze die Wörter in Klammern. Entscheide zuerst, ob du einen '
           'Schritt zurückgehst.',

    actTitle='Personal Legends', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben &middot; 200–250 Wörter',
    actSpeakBrief='Der Kristallhändler hat einen Traum und bricht nie auf. '
                  'Santiago bricht auf. Jede Person vertritt eine Seite.',
    actSpeak1='Seite des Händlers: Argumentiere, dass ein Traum unerfüllt mehr '
              'wert ist. Benutze einmal <em>by the time</em>.',
    actSpeak2='Seite Santiagos: Argumentiere dagegen und benutze mindestens '
              'zweimal <em>had already</em>.',
    actSpeak3='Beide: Erzählt je eine wahre Geschichte darüber, etwas '
              'aufgegeben zu haben. Höchstens zwei Past Perfects.',
    actSpeak4='Beide: Einigt euch in einem Satz darauf, was der Roman '
              'eigentlich behauptet, und sagt, ob ihr es glaubt.',
    actWriteBrief='Ist eine „Personal Legend“ eine nützliche Idee oder eine '
                  'tröstliche? Belege mit dem Roman, in den Erzählzeiten der '
                  'Vergangenheit, und gehe mindestens zweimal mit dem Past '
                  'Perfect einen Schritt zurück.',
    actPlaceholder='Santiago had been content with his flock long before the '
                   'dream first came…',
    resPerfect='Volle Punktzahl. Du erkennst, wann das Past Perfect arbeitet — '
               'und wann es bloß Dekoration ist.',
    resStrong='Stark. Lagen deine Fehler in der Grammatik, prüfe, ob du nach '
              '<em>had</em> gegriffen hast, obwohl die Reihenfolge schon klar '
              'war.',
    resMid='Sicher bestanden. Lies die Folie „Wann du es NICHT brauchst“ noch '
           'einmal — Übergebrauch ist auf B2 der häufigere Fehler.',
    resLow='Geh die fünf Folien der Geschichte und die zwei Grammatikfolien '
           'noch einmal durch und starte dann neu.',
)

for _w, _d, _k, _en in B.VOCAB:
    T['en'][_k] = _en

_DE_VOCAB = {
    'v1': 'Eine dunkle Wolke am Hochzeitsmorgen ist ein <em>bad omen</em>. '
          'Fast immer mit Adjektiv: good, bad, ill.',
    'v2': 'Auch Vögel treten im <em>flock</em> auf. Rinder in einer herd, '
          'Fische in einem shoal.',
    'v3': 'Im britischen Englisch ist <em>caravan</em> auch der Wohnwagen. Der '
          'Kontext trennt beides eindeutig.',
    'v4': 'Auch übertragen: <em>an oasis of calm</em>. Plural: <em>oases</em>.',
    'v5': 'Man <em>pursues a dream</em>, eine Laufbahn, einen Abschluss. '
          'Gehoben; alltäglich sagt man <em>chase</em> oder <em>go after</em>.',
    'v6': 'Heute etwas altertümlich oder fachlich: a wine merchant, a merchant '
          'ship.',
    'v7': '<em>Destined to</em> + Verb oder <em>destined for</em> + Nomen. Das '
          'Adjektiv, um das dieser Roman streitet.',
    'v8': 'Meist unzählbar: <em>years of hardship</em>. Nicht dasselbe wie '
          '<em>hardness</em>.',
    'v9': 'Die Gerichtsbedeutung ist heute die häufigere — achte auf den '
          'Kontext: <em>the trials of the journey</em> meint diese hier.',
    'v10': 'Unzählbar. Nicht dasselbe wie Intelligenz oder Wissen — Weisheit '
           'ist, was man damit anfängt.',
}
T['de'].update(_DE_VOCAB)

for _txt, _nk, _en in B.PARAS:
    T['en'][_nk] = _en

_DE_PARAS = {
    'p1n': 'Beachte <em>content with</em> — zufrieden, nicht auf mehr aus. '
           'Genau diesen Zustand stört die Geschichte.',
    'p2n': 'Er <em>verkauft</em> die Herde, er lässt sie nicht zurück. Der '
           'Unterschied zählt: Es ist ein bewusster Tausch, kein Weglaufen.',
    'p3n': 'Vier der Vokabeln stehen in diesem Absatz: <em>merchant</em>, '
           '<em>caravan</em>, <em>oasis</em>, <em>hardship</em>.',
    'p4n': '<em>Trial</em> meint hier keinen Prozess, sondern eine Prüfung '
           'dessen, was jemand aushält — die ältere Bedeutung.',
    'p5n': 'Der Schatz ist also echt <em>und</em> der Weg war der Punkt. Eine '
           'Lesart, die nur eines von beidem behält, ist dünner als das Buch.',
}
T['de'].update(_DE_PARAS)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
