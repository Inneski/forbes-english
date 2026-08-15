# -*- coding: utf-8 -*-
"""Interface strings for Stranger Things B1, English and German.

The paragraph notes live in the data table in build_stranger.py and are
attached at the bottom, so the English exists in one place. That import is
safe: build_stranger only imports this module inside its __main__ block.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME
import build_stranger as B

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Stranger <em>Things</em>',
    coverSub='Hawkins, 1983 — tenses, the German traps, and the words the '
             'story actually uses',
    chipLevel='B1 &middot; for German learners',
    chipFocus='Tenses &amp; vocabulary', chipCount='42 slides',

    t1E='The four tenses this lesson uses', t1T='Present simple and past simple',
    t1ah='Present simple &mdash; habits and facts',
    t1an='Signals: every day, usually, often, never, on Mondays. She/he/it '
         'takes <em>-s</em>.',
    t1bh='Past simple &mdash; one finished action',
    t1bn='Signals: yesterday, last week, in 1983, two days ago. Regular verbs '
         'take <em>-ed</em>; many common ones do not.',
    t1ch='The test between them',
    t1cn='A stated past time forces the past simple. A repeated time forces '
         'the present simple. Find the time word before you look at the verb.',
    t2E='The four tenses this lesson uses',
    t2T='Present continuous &mdash; and why it is here',
    t2ah='The form', t2an='Eleven <em>is hiding</em> in the woods. Right now, '
                          'as we speak.',
    t2bh='Signals',
    t2bn='If the sentence points at this moment, the continuous is the only '
         'choice.',
    t2ch='Why it matters here',
    t2cn='It is the commonest wrong option in the questions ahead. You cannot '
         'reject a form you have never been shown.',
    t3E='The four tenses this lesson uses',
    t3T='Present perfect &mdash; and the German trap in it',
    t3ah='The form',
    t3an='I <em>have never seen</em> it. She <em>has escaped</em>. We '
         '<em>haven\'t spoken</em>.',
    t3bh='When',
    t3bn='And always after <em>since</em> and <em>for</em> when the situation '
         'still holds.',
    t3ch='The trap',
    t3cn='✗ <em>We don\'t speak since Monday.</em> ✓ <em>We haven\'t spoken '
         'since Monday.</em> This single pattern is worth more marks than any '
         'other on this page.',
    t4E='The four tenses this lesson uses',
    t4T='The participles you need for the perfect',
    t4n='The perfect needs the third form, not the past simple. <em>I have '
        'spoke</em> is the error; <em>I have spoken</em> is the sentence.',
    t5E='One more structure', t5T='The first conditional',
    t5ah='The pattern',
    t5an='If I <em>don\'t study</em>, I <em>will get</em> a bad grade.',
    t5bh='The rule that gets broken',
    t5bn='✗ <em>If I will not study…</em> — this is the single commonest '
         'conditional error in German-speaking classrooms.',
    t5ch='Why it is called the first',
    t5cn='Two scored items on this page depend on it. German uses the present '
         'in both halves too, which is why the <em>will</em> slips in.',

    gtE='German traps', gtT='Four false friends and a fixed preposition',
    gt1h='machen &rarr; do, not make',
    gt1n='<em>Make</em> is for producing a thing: make a cake, make a noise, '
         'make a plan.',
    gt2h='bekommen &rarr; get, not become',
    gt2n='English <em>become</em> = <em>werden</em>. &bdquo;I became a '
         'message&ldquo; says you turned into one.',
    gt3h='lernen &rarr; study or learn',
    gt3n='And two fixed forms: <em>good at</em> something, <em>rely on</em> '
         'somebody. Neither preposition follows the German.',

    g1E='Grammar &middot; Activity 1', g1T='Choose the correct form',
    g2E='Grammar &middot; Activity 2', g2T='Fix the German mistake',

    vE='Vocabulary', vT='Six words the story needs',
    vn='All six appear in the reading, and four of them are tested. Learn them '
       'here and the questions later are straightforward.',
    vgE='Vocabulary &middot; Activity 1', vgT='Complete the sentence',
    vgHint='One word per gap. Every one of them is on the slide before this.',
    vmE='Vocabulary &middot; Activity 2', vmT='Match the word to its meaning',
    vmHint='Click a word, then click its meaning.',

    rE='The text',
    rT1='Reading &mdash; part 1 of 4', rT2='Reading &mdash; part 2 of 4',
    rT3='Reading &mdash; part 3 of 4', rT4='Reading &mdash; part 4 of 4',
    rqE='Reading &middot; Comprehension', rqT='What does the text say?',
    rcE='Reading &middot; Vocabulary in context',
    rcT='What does the word mean here?',

    eE='Spot the mistake', eT='Write the correction',
    eHint='Each sentence has one error. Write only the part that changes.',
    sE='Word stress', sT='Where does the stress fall?',

    actTitle='Hawkins, one week later', actUse='Use at least four:',
    actWriteKind='Writing &middot; 120–150 words',
    actSpeakBrief='One of you was in Hawkins that week. The other is from the '
                  'local paper.',
    actSpeak1='Reporter: ask three questions with <em>Have you ever…?</em> and '
              'one with <em>How long…?</em>',
    actSpeak2='Witness: answer using <em>since</em> at least twice. Watch the '
              'tense — <em>since</em> takes the perfect.',
    actSpeak3='Both: make three first-conditional predictions about what '
              'happens next in the town.',
    actSpeak4='Both: say one thing each of you is <em>good at</em>, and one '
              'person you <em>rely on</em>. Watch both prepositions.',
    actWriteBrief='Write the newspaper report of the week Will Byers went '
                  'missing. Past simple for what happened, present perfect for '
                  'what has changed since.',
    actPlaceholder='Last November, a twelve-year-old boy went missing in '
                   'Hawkins, Indiana. Since then, …',
    resPerfect='Full marks. You can tell the perfect from the past simple, '
               'which is the whole battle at B1.',
    resStrong='Strong. Check which section your misses came from — if they '
              'cluster in the German traps, those are pure memory and worth '
              'ten minutes.',
    resMid='A solid pass. Go back to the present perfect slide: <em>since</em> '
           'plus the perfect is where most of the marks on this page live.',
    resLow='Read the five teaching slides again before you retry. Every rule '
           'tested here is on one of them, before the questions start.',
)

T['de'] = dict(
    coverTitle='Stranger <em>Things</em>',
    coverSub='Hawkins, 1983 — Zeiten, die typischen deutschen Fehler und die '
             'Wörter, die in der Geschichte wirklich vorkommen',
    chipLevel='B1 &middot; für deutschsprachige Lernende',
    chipFocus='Zeiten &amp; Wortschatz', chipCount='42 Folien',

    t1E='Die vier Zeiten in dieser Lektion',
    t1T='Present Simple und Past Simple',
    t1ah='Present Simple &mdash; Gewohnheiten und Tatsachen',
    t1an='Signalwörter: every day, usually, often, never, on Mondays. Bei '
         'she/he/it kommt ein <em>-s</em> dazu.',
    t1bh='Past Simple &mdash; eine abgeschlossene Handlung',
    t1bn='Signalwörter: yesterday, last week, in 1983, two days ago. '
         'Regelmäßige Verben bekommen <em>-ed</em>; viele häufige nicht.',
    t1ch='So unterscheidest du sie',
    t1cn='Eine genannte Zeit in der Vergangenheit erzwingt das Past Simple. '
         'Eine wiederholte Zeit erzwingt das Present Simple. Suche das '
         'Zeitwort, bevor du auf das Verb schaust.',
    t2E='Die vier Zeiten in dieser Lektion',
    t2T='Present Continuous &mdash; und warum es hier steht',
    t2ah='Die Form',
    t2an='Eleven <em>is hiding</em> in the woods. Genau jetzt, während wir '
         'sprechen.',
    t2bh='Signalwörter',
    t2bn='Zeigt der Satz auf diesen Moment, ist das Continuous die einzige '
         'Möglichkeit.',
    t2ch='Warum das hier wichtig ist',
    t2cn='Es ist die häufigste falsche Antwortmöglichkeit in den Aufgaben, '
         'die folgen. Man kann keine Form ablehnen, die einem nie gezeigt '
         'wurde.',
    t3E='Die vier Zeiten in dieser Lektion',
    t3T='Present Perfect &mdash; und die deutsche Falle darin',
    t3ah='Die Form',
    t3an='I <em>have never seen</em> it. She <em>has escaped</em>. We '
         '<em>haven\'t spoken</em>.',
    t3bh='Wann',
    t3bn='Und immer nach <em>since</em> und <em>for</em>, wenn die Situation '
         'noch andauert.',
    t3ch='Die Falle',
    t3cn='✗ <em>We don\'t speak since Monday.</em> ✓ <em>We haven\'t spoken '
         'since Monday.</em> Dieses eine Muster bringt mehr Punkte als alles '
         'andere auf dieser Seite.',
    t4E='Die vier Zeiten in dieser Lektion',
    t4T='Die Partizipien, die du für das Perfect brauchst',
    t4n='Das Perfect braucht die dritte Form, nicht das Past Simple. <em>I '
        'have spoke</em> ist der Fehler; <em>I have spoken</em> ist der Satz.',
    t5E='Eine Struktur noch', t5T='Der If-Satz Typ 1',
    t5ah='Das Muster',
    t5an='If I <em>don\'t study</em>, I <em>will get</em> a bad grade.',
    t5bh='Die Regel, die gebrochen wird',
    t5bn='✗ <em>If I will not study…</em> — der mit Abstand häufigste Fehler '
         'bei If-Sätzen im deutschsprachigen Unterricht.',
    t5ch='Warum „Typ 1“',
    t5cn='Zwei bewertete Aufgaben auf dieser Seite hängen davon ab. Auch im '
         'Deutschen steht in beiden Hälften Präsens — daher rutscht das '
         '<em>will</em> hinein.',

    gtE='Typische deutsche Fehler',
    gtT='Vier falsche Freunde und zwei feste Präpositionen',
    gt1h='machen &rarr; do, nicht make',
    gt1n='<em>Make</em> ist für das Herstellen einer Sache: make a cake, make '
         'a noise, make a plan.',
    gt2h='bekommen &rarr; get, nicht become',
    gt2n='Englisch <em>become</em> heißt <em>werden</em>. „I became a message“ '
         'sagt, dass du selbst zu einer Nachricht geworden bist.',
    gt3h='lernen &rarr; study oder learn',
    gt3n='Dazu zwei feste Formen: <em>good at</em> etwas, <em>rely on</em> '
         'jemanden. Keine der beiden Präpositionen folgt dem Deutschen.',

    g1E='Grammatik &middot; Aufgabe 1', g1T='Wähle die richtige Form',
    g2E='Grammatik &middot; Aufgabe 2', g2T='Korrigiere den deutschen Fehler',

    vE='Wortschatz', vT='Sechs Wörter, die die Geschichte braucht',
    vn='Alle sechs kommen im Lesetext vor, vier werden abgefragt. Wer sie hier '
       'lernt, hat es später leicht.',
    vgE='Wortschatz &middot; Aufgabe 1', vgT='Vervollständige den Satz',
    vgHint='Ein Wort pro Lücke. Alle stehen auf der Folie davor.',
    vmE='Wortschatz &middot; Aufgabe 2', vmT='Ordne dem Wort seine Bedeutung zu',
    vmHint='Klicke ein Wort an und dann seine Bedeutung.',

    rE='Der Text',
    rT1='Lesetext &mdash; Teil 1 von 4', rT2='Lesetext &mdash; Teil 2 von 4',
    rT3='Lesetext &mdash; Teil 3 von 4', rT4='Lesetext &mdash; Teil 4 von 4',
    rqE='Lesen &middot; Verständnis', rqT='Was steht im Text?',
    rcE='Lesen &middot; Wortschatz im Kontext',
    rcT='Was bedeutet das Wort hier?',

    eE='Finde den Fehler', eT='Schreibe die Korrektur',
    eHint='In jedem Satz steckt ein Fehler. Schreibe nur den Teil, der sich '
          'ändert.',
    sE='Wortbetonung', sT='Wo liegt die Betonung?',

    actTitle='Hawkins, eine Woche später', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben &middot; 120–150 Wörter',
    actSpeakBrief='Eine Person war in jener Woche in Hawkins. Die andere '
                  'arbeitet bei der Lokalzeitung.',
    actSpeak1='Zeitung: Stelle drei Fragen mit <em>Have you ever…?</em> und '
              'eine mit <em>How long…?</em>',
    actSpeak2='Zeugin/Zeuge: Antworte mindestens zweimal mit <em>since</em>. '
              'Achte auf die Zeit — <em>since</em> verlangt das Perfect.',
    actSpeak3='Beide: Stellt drei Vorhersagen im If-Satz Typ 1 darüber auf, '
              'was als Nächstes in der Stadt passiert.',
    actSpeak4='Beide: Nennt je eine Sache, in der ihr <em>good at</em> seid, '
              'und je eine Person, auf die ihr euch <em>rely on</em>. Achtet '
              'auf beide Präpositionen.',
    actWriteBrief='Schreibe den Zeitungsbericht über die Woche, in der Will '
                  'Byers verschwand. Past Simple für das, was passiert ist; '
                  'Present Perfect für das, was sich seitdem verändert hat.',
    actPlaceholder='Last November, a twelve-year-old boy went missing in '
                   'Hawkins, Indiana. Since then, …',
    resPerfect='Volle Punktzahl. Du unterscheidest Perfect und Past Simple — '
               'darum geht es auf B1 im Kern.',
    resStrong='Stark. Schau nach, aus welchem Teil deine Fehler kamen. Häufen '
              'sie sich bei den deutschen Fehlern, ist das reine '
              'Merkarbeit — zehn Minuten reichen.',
    resMid='Sicher bestanden. Zurück zur Present-Perfect-Folie: <em>since</em> '
           'plus Perfect ist die Stelle mit den meisten Punkten.',
    resLow='Lies die fünf Erklärfolien noch einmal, bevor du es erneut '
           'versuchst. Jede abgefragte Regel steht auf einer davon — vor den '
           'Aufgaben.',
)

for _pk, _txt, _nk, _en in B.PARAS:
    T['en'][_nk] = _en

_DE_NOTES = {
    'r1n': 'Zwei der fett gedruckten Wörter werden später abgefragt. '
           '<em>Appear</em> heißt hier „erscheinen / verfügbar werden“, nicht '
           '„aus dem Nichts auftauchen“.',
    'r2n': '<em>Has escaped</em> ist Present Perfect: Es geschah vor diesem '
           'Moment der Geschichte, und das Ergebnis — sie ist draußen — gilt '
           'weiterhin.',
    'r3n': 'Achte auf die Reihenfolge: Sie wurde jahrelang '
           '<em>festgehalten</em> und floh <em>dann</em>. Eine Verständnisfrage '
           'hängt davon ab.',
    'r4n': 'Beachte <em>within days</em>. Staffel 1 umfasst etwa eine Woche — '
           'die Freundschaft entsteht schnell, und genau das macht sie stark.',
}
for _k, _v in _DE_NOTES.items():
    T['de'][_k] = _v


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
