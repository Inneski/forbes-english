# -*- coding: utf-8 -*-
"""Interface strings for Carrying the Load (C1) — English and German.

The lesson content itself is monolingual by request: every stem, option and
explanation is English. What the switcher translates is the interface — cover,
section titles, the activation briefs and the result bands — which is what
house-style rule 5 and check-lesson.js require, and what every other deck does.

ledDp/ledTime/ledClues are lifted from CHROME rather than declared here. The
template's deck bar carries a hidden RPG ledger whose three labels are
data-i18n, so any deck built from the current template fails the checker's
"data-i18n with no English key" rule unless they resolve. They are chrome, so
they were added to chrome_i18n for all ten languages instead of being
re-declared per lesson.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount',
        'ledDp', 'ledTime', 'ledClues']

T = {}

T['en'] = dict(
    coverTitle='Carrying the <em>Load</em>',
    coverSub='What to say to the colleague who does not pull their weight — and what to say next when saying it once does not work',
    chipLevel='C1 · Business English',
    chipFocus='Feedback &amp; escalation',
    chipCount='58 slides',

    readEyebrow='Reading',
    r1Title='The cost of silence',
    r2Title='Posture before words',
    r3Title='The unit of feedback',
    r4Title='Feedback about the feedback',
    r5Title='Counsel, not rescue',

    rungEyebrow='The four rungs',
    rung1Title='You do not skip a rung',
    rung2Title='And if the rung above gives way',

    ckEyebrow='Comprehension',
    ckTitle='Did you read it closely?',

    anRefEyebrow='Before you sort',
    anRefTitle='Four jobs a sentence can do',
    anEyebrow='Anatomy',
    anTitle='What is this line actually doing?',

    esEyebrow='Escalate',
    esTitle='Choose the move',

    phEyebrow='The language of the imbalance',
    ph1Title='Carrying, and being seen to carry',
    ph2Title='Deflecting, escalating, owning',
    woEyebrow='Words',
    woTitle='One word fits the collocation',

    grEyebrow='Before the grammar',
    grTitle='Two ways to take yourself out of the sentence',
    foEyebrow='Form',
    foTitle='Grammar under pressure',

    actTitle='Have the conversation',
    actUse='Use at least four:',
    actSpeakBrief='One of you is the colleague, one is you. Swap after the second prompt — the deflection is harder to do well than it looks.',
    actSpeak1='Deliver round one: behaviour a camera saw, impact on you, one question. Nothing else.',
    actSpeak2='Deflect. Name two other people and a system problem, and sound entirely reasonable doing it.',
    actSpeak3='Feed back the deflection, in under forty seconds, without raising your voice or your eyebrows.',
    actSpeak4='Brief the manager in three sentences: the pattern with numbers, what you tried, the question you want answered.',
    actSpeak5='A month on, nothing has changed. Give the manager feedback without once assigning them a motive.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write the message you would send your manager after two rounds of direct feedback have failed. Pattern with dates, impact in the first person, what you already tried, one open question — and no interpretation of anyone&rsquo;s motives.',
    actPlaceholder='Hi … — I wanted to flag something before the next cycle rather than after it.',

    resPerfect='You are running this conversation, not surviving it. Behaviour, impact, question — and nothing in between.',
    resStrong='Strong. The formula is yours; the remaining points are all in the wording, not the structure.',
    resMid='The shape is there. Go back to the anatomy slides — interpretation is still slipping into sentences that look factual.',
    resLow='Read the five reading slides again before the speaking stage. The whole lesson turns on three parts and one forbidden fourth.',
)

T['de'] = dict(
    coverTitle='Die <em>Last</em> tragen',
    coverSub='Was man dem Kollegen sagt, der seinen Teil nicht leistet — und was man danach sagt, wenn einmal sagen nicht reicht',
    chipLevel='C1 · Business-Englisch',
    chipFocus='Feedback &amp; Eskalation',
    chipCount='58 Folien',

    readEyebrow='Lesetext',
    r1Title='Was das Schweigen kostet',
    r2Title='Die Haltung kommt vor den Worten',
    r3Title='Die Grundeinheit des Feedbacks',
    r4Title='Feedback über das Feedback',
    r5Title='Rat, nicht Rettung',

    rungEyebrow='Die vier Stufen',
    rung1Title='Keine Stufe wird übersprungen',
    rung2Title='Und wenn die Stufe darüber nachgibt',

    ckEyebrow='Leseverständnis',
    ckTitle='Haben Sie genau gelesen?',

    anRefEyebrow='Vor dem Sortieren',
    anRefTitle='Vier Aufgaben, die ein Satz haben kann',
    anEyebrow='Anatomie',
    anTitle='Was tut dieser Satz eigentlich?',

    esEyebrow='Eskalieren',
    esTitle='Wählen Sie den nächsten Schritt',

    phEyebrow='Die Sprache des Ungleichgewichts',
    ph1Title='Tragen — und sichtbar tragen',
    ph2Title='Abwehren, eskalieren, Verantwortung behalten',
    woEyebrow='Wortschatz',
    woTitle='Nur ein Wort passt in die Kollokation',

    grEyebrow='Vor der Grammatik',
    grTitle='Zwei Wege, sich selbst aus dem Satz herauszunehmen',
    foEyebrow='Form',
    foTitle='Grammatik unter Druck',

    actTitle='Führen Sie das Gespräch',
    actUse='Verwenden Sie mindestens vier:',
    actSpeakBrief='Einer von Ihnen ist der Kollege, einer sind Sie selbst. Tauschen Sie nach dem zweiten Impuls — das Abwehren gut zu spielen ist schwerer, als es aussieht.',
    actSpeak1='Runde eins: das Verhalten, das eine Kamera gesehen hätte, die Auswirkung auf Sie, eine Frage. Sonst nichts.',
    actSpeak2='Wehren Sie ab. Nennen Sie zwei andere Personen und ein Systemproblem — und klingen Sie dabei völlig vernünftig.',
    actSpeak3='Geben Sie Feedback zur Abwehr, in unter vierzig Sekunden, ohne die Stimme oder die Augenbrauen zu heben.',
    actSpeak4='Informieren Sie die Führungskraft in drei Sätzen: das Muster mit Zahlen, was Sie versucht haben, die Frage, die Sie beantwortet haben wollen.',
    actSpeak5='Einen Monat später hat sich nichts geändert. Geben Sie der Führungskraft Feedback, ohne ihr ein einziges Mal ein Motiv zu unterstellen.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreiben Sie die Nachricht an Ihre Führungskraft, nachdem zwei Runden direktes Feedback nichts bewirkt haben. Muster mit Daten, Auswirkung in der Ich-Form, was Sie bereits versucht haben, eine offene Frage — und keine Deutung fremder Motive.',
    actPlaceholder='Hallo … — ich wollte etwas ansprechen, bevor der nächste Zyklus beginnt, nicht danach.',

    resPerfect='Sie führen dieses Gespräch, statt es zu überstehen. Verhalten, Auswirkung, Frage — und nichts dazwischen.',
    resStrong='Stark. Die Formel sitzt; die restlichen Punkte liegen in der Formulierung, nicht im Aufbau.',
    resMid='Die Struktur steht. Zurück zu den Anatomie-Folien — die Deutung schleicht sich noch in Sätze, die sachlich aussehen.',
    resLow='Lesen Sie die fünf Lesefolien noch einmal, bevor Sie sprechen. Alles hängt an drei Teilen und einem verbotenen vierten.',
)


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
