# -*- coding: utf-8 -*-
"""Interface strings for Reading the Elevation (C1) — English and German.

The lesson content is monolingual by house-style rule 8: every stem, option,
gap sentence and explanation stays in English, because translating the target
language is the one thing the switcher must not do. What German covers is the
chrome — cover, eyebrows, section titles, hints, the activation briefs and the
result bands.

ledDp/ledTime/ledClues are lifted from CHROME rather than declared here: the
template's deck bar carries a hidden RPG ledger whose three labels are
data-i18n, and any deck built from the current template fails the checker's
"data-i18n with no English key" rule unless they resolve.

resNext is deliberately NOT lifted — this lesson wants its own line out of the
results screen, and a lifted key would silently take the chrome default.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'actEyebrow', 'actSpeakKind',
        'btnCopy', 'btnCopied', 'wordCount', 'ledDp', 'ledTime', 'ledClues']

T = {}

T['en'] = dict(
    coverTitle='Reading the <em>Elevation</em>',
    coverSub='Thirty-six words for saying what a building is made of, what time has done to it, and how it treats the buildings next door',
    chipLevel='C1 · Vocabulary',
    chipFocus='Architecture &amp; description',
    chipCount='28 slides',

    fabEyebrow='The fabric',
    fabTitle='What it is made of',
    timeEyebrow='What time does',
    timeTitle='Decay, and the decision to stop it',
    openEyebrow='Openings',
    openTitle='The way in, and the way light gets in',
    eyeEyebrow='In the eye',
    eyeTitle='What the building does to you',
    pastEyebrow='Talking to the past',
    pastTitle='Copy, tribute, or collision',

    placeEyebrow='One word, in place',
    placeTitle='Which word does the sentence want?',

    missEyebrow='The near miss',
    missTitle='Two words, one of them wrong',

    sortEyebrow='Taking a view',
    sortTitle='Praise, description, complaint',
    sortHint='Some of these words judge the building. Some only describe it. Sort all twelve.',

    gapEyebrow='Fill the gap',
    gapTitle='One word from the bank per space',
    gapHint='Case does not matter. Every word is used exactly once across the three slides.',
    bankLabel='Word bank:',

    matchEyebrow='Six more',
    matchTitle='Match the word to what it actually means',
    matchHint='Click a word, then click its meaning.',

    ordEyebrow='Build the sentence',
    ord1Title='A sentence about a material',
    ord2Title='A sentence about a neighbour',
    ordHint='Click the parts in order &middot; click one again to take it back',

    resNext='You can name what you are looking at. Now describe a real building &rarr;',

    actTitle='Describe a building out loud',
    actUse='Use at least five:',
    actSpeakBrief='In pairs. One prompt each, two minutes, then swap. If you can finish a prompt without using the words above, you have answered a different question.',
    actSpeak1='Describe the nearest building you can see: its fenestration, its threshold, one material. Thirty seconds.',
    actSpeak2='A developer wants to demolish a run-down warehouse. Argue for conserving it, not restoring it.',
    actSpeak3='Defend a building your partner calls obtrusive. Use eye-catching, conspicuous and unobtrusive, and mean the difference.',
    actSpeak4='A new terrace goes up in Georgian style. You say pastiche; your partner says homage.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write the walking-guide entry for one building you know well: what it is made of, what has happened to it, what it does to the eye, and how it treats its neighbours. No adjective twice.',
    actPlaceholder='From the bridge it reads as a single slab, until you notice …',

    resPerfect='All of it. You are describing buildings now, not gesturing at them.',
    resStrong='Strong. The families are clear — what is left is the near misses, and those are learned one pair at a time.',
    resMid='The vocabulary is in. Go back to the five teaching slides: pastiche against homage, and conserve against restore, are the two that cost most.',
    resLow='Read the five teaching slides again before the speaking task. These words come in families, and the family is easier to hold than the word.',
)

T['de'] = dict(
    coverTitle='Die <em>Fassade</em> lesen',
    coverSub='Sechsunddreißig Wörter dafür, woraus ein Gebäude besteht, was die Zeit mit ihm gemacht hat und wie es mit seinen Nachbarn umgeht',
    chipLevel='C1 · Wortschatz',
    chipFocus='Architektur &amp; Beschreibung',
    chipCount='28 Folien',

    fabEyebrow='Das Material',
    fabTitle='Woraus es gebaut ist',
    timeEyebrow='Was die Zeit tut',
    timeTitle='Verfall — und die Entscheidung, ihn aufzuhalten',
    openEyebrow='Öffnungen',
    openTitle='Der Weg hinein und der Weg des Lichts',
    eyeEyebrow='Im Auge',
    eyeTitle='Was das Gebäude mit einem macht',
    pastEyebrow='Im Gespräch mit der Vergangenheit',
    pastTitle='Kopie, Hommage oder Zusammenprall',

    placeEyebrow='Ein Wort, an seinen Platz',
    placeTitle='Welches Wort verlangt der Satz?',

    missEyebrow='Knapp daneben',
    missTitle='Zwei Wörter, eines davon falsch',

    sortEyebrow='Stellung beziehen',
    sortTitle='Lob, Beschreibung, Kritik',
    sortHint='Manche dieser Wörter bewerten das Gebäude, andere beschreiben es nur. Sortieren Sie alle zwölf.',

    gapEyebrow='Lücken füllen',
    gapTitle='Ein Wort aus der Liste pro Lücke',
    gapHint='Groß- und Kleinschreibung spielt keine Rolle. Jedes Wort wird über die drei Folien hinweg genau einmal gebraucht.',
    bankLabel='Wortliste:',

    matchEyebrow='Sechs weitere',
    matchTitle='Ordnen Sie jedem Wort seine tatsächliche Bedeutung zu',
    matchHint='Klicken Sie ein Wort an, dann seine Bedeutung.',

    ordEyebrow='Bauen Sie den Satz',
    ord1Title='Ein Satz über ein Material',
    ord2Title='Ein Satz über einen Nachbarn',
    ordHint='Klicke die Teile der Reihe nach an &middot; nochmal klicken nimmt einen zurück',

    resNext='Sie können benennen, was Sie sehen. Jetzt beschreiben Sie ein echtes Gebäude &rarr;',

    actTitle='Beschreiben Sie ein Gebäude — laut',
    actUse='Verwenden Sie mindestens fünf:',
    actSpeakBrief='Zu zweit. Ein Impuls pro Person, zwei Minuten, dann tauschen. Wer einen Impuls ohne die Wörter oben beenden kann, hat eine andere Frage beantwortet.',
    actSpeak1='Beschreiben Sie das nächste sichtbare Gebäude: Fensteranordnung, Schwelle, ein Material. Dreißig Sekunden.',
    actSpeak2='Ein Investor will ein heruntergekommenes Lagerhaus abreißen. Plädieren Sie für Erhalten statt Restaurieren.',
    actSpeak3='Verteidigen Sie ein Gebäude, das Ihr Gegenüber aufdringlich nennt. Benutzen Sie „eye-catching“, „conspicuous“ und „unobtrusive“.',
    actSpeak4='Eine neue Häuserzeile entsteht im georgianischen Stil. Sie sagen Pastiche, Ihr Gegenüber sagt Hommage.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreiben Sie den Stadtführer-Eintrag zu einem Gebäude, das Sie gut kennen: woraus es gebaut ist, was mit ihm geschehen ist, was es mit dem Auge macht und wie es mit seinen Nachbarn umgeht. Kein Adjektiv zweimal.',
    actPlaceholder='Von der Brücke aus wirkt es wie eine einzige Platte, bis man bemerkt …',

    resPerfect='Alles. Sie beschreiben Gebäude jetzt, statt auf sie zu zeigen.',
    resStrong='Stark. Die Wortfamilien sitzen — was bleibt, sind die knappen Fälle, und die lernt man paarweise.',
    resMid='Der Wortschatz ist da. Zurück zu den fünf Erklärfolien: pastiche gegen homage und conserve gegen restore kosten die meisten Punkte.',
    resLow='Lesen Sie die fünf Erklärfolien noch einmal, bevor Sie sprechen. Diese Wörter kommen in Familien, und die Familie behält man leichter als das einzelne Wort.',
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
