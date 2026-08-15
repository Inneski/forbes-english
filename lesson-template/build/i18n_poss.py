# -*- coding: utf-8 -*-
"""Interface strings for Mine, Yours, Hers (A1), English and German.

At A1 the German matters more than it does higher up the site: a beginner who
cannot read the instruction cannot start the exercise. Note that the six
English pronouns themselves are never translated — they are the lesson.
"""
import json, sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Mine. Yours. <em>Hers. Ours.</em>',
    coverSub='Lena and Sophie are at school in Hamburg, and everything in the corridor belongs to somebody',
    chipLevel='A1 · Grammar', chipFocus='Possessive pronouns', chipCount='16 slides',
    tabEyebrow='The whole rule, on one slide', tabTitle='Two words for the same thing',
    tabL='With a noun', tabR='Without a noun',
    tabNote='The word on the right is used when the noun <strong>disappears</strong>. Most of them add <strong>-s</strong>. Only <em>his</em> stays the same.',
    whoEyebrow='One more thing', whoTitle='The word depends on who is speaking',
    w1h='I am speaking', w1b='Lena: “That sandwich is <strong>mine</strong>.”',
    w2h='I am speaking to you', w2b='Sophie to Lena: “Is this pencil <strong>yours</strong>?”',
    w3h='Nobody is speaking',
    w3b='“The two girls share a desk. The desk is <strong>theirs</strong>.”',
    qEyebrow='In the corridor', qTitle='Choose the right word',
    typEyebrow='Type the word', typTitle='Complete the sentence',
    typHint='No list this time — type the word yourself.',
    bnkEyebrow='Choose from the list', bnkTitle='Complete the sentence',
    bnkHint='Six words, five gaps. One word is not needed.',
    bankLabel='Word bank:',
    matchEyebrow='The pairs', matchTitle='Match the two forms',
    matchHint='Click a phrase on the left, then its partner.',
    actTitle='Whose is it?', actUse='Use at least four:',
    actWriteKind='Writing · 40–60 words',
    actSpeakBrief='Put four or five things on the table between you — pens, phones, keys, a bag.',
    actSpeak1='Point at something and ask: “Is this <em>yours</em>?” Answer with <em>mine</em> or a name.',
    actSpeak2='Now describe the table to a third person. Everything becomes <em>hers</em>, <em>his</em> or <em>theirs</em>.',
    actSpeak3='Find two things you share with your partner. “That one is <em>ours</em>.”',
    actSpeak4='Say the same sentence twice: once with the noun, once without. <em>my pen</em> → <em>mine</em>.',
    actWriteBrief='Write five sentences about your classroom. Use a different word each time.',
    actPlaceholder='The blue bag is hers. The pens are…',
    resPerfect='Perfect. Lena and Sophie are very impressed — you know all six.',
    resStrong='Very good. Almost all of them. Look once more at <em>hers</em> and <em>theirs</em>.',
    resMid='Good work. Go back to the table slide — the two columns are the whole rule.',
    resLow='Nice try. Read the first two slides again, then start again. You can do it.',
)

T['de'] = dict(
    coverTitle='Mine. Yours. <em>Hers. Ours.</em>',
    coverSub='Lena und Sophie sind in Hamburg in der Schule, und alles auf dem Flur gehört irgendwem',
    chipLevel='A1 · Grammatik', chipFocus='Possessivpronomen', chipCount='16 Folien',
    tabEyebrow='Die ganze Regel auf einer Folie', tabTitle='Zwei Wörter für dieselbe Sache',
    tabL='Mit Nomen', tabR='Ohne Nomen',
    tabNote='Das Wort rechts steht, wenn das Nomen <strong>verschwindet</strong>. Die meisten bekommen ein <strong>-s</strong>. Nur <em>his</em> bleibt gleich.',
    whoEyebrow='Noch eine Sache', whoTitle='Das Wort hängt davon ab, wer spricht',
    w1h='Ich spreche', w1b='Lena: „That sandwich is <strong>mine</strong>.“',
    w2h='Ich spreche mit dir', w2b='Sophie zu Lena: „Is this pencil <strong>yours</strong>?“',
    w3h='Niemand spricht',
    w3b='„The two girls share a desk. The desk is <strong>theirs</strong>.“',
    qEyebrow='Auf dem Flur', qTitle='Wählen Sie das richtige Wort',
    typEyebrow='Tippen Sie das Wort', typTitle='Vervollständigen Sie den Satz',
    typHint='Diesmal ohne Liste — tippen Sie das Wort selbst.',
    bnkEyebrow='Wählen Sie aus der Liste', bnkTitle='Vervollständigen Sie den Satz',
    bnkHint='Sechs Wörter, fünf Lücken. Ein Wort wird nicht gebraucht.',
    bankLabel='Wortliste:',
    matchEyebrow='Die Paare', matchTitle='Ordnen Sie die beiden Formen zu',
    matchHint='Klicken Sie links auf eine Wendung und dann auf ihr Gegenstück.',
    actTitle='Wem gehört das?', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 40–60 Wörter',
    actSpeakBrief='Legen Sie vier oder fünf Dinge zwischen sich auf den Tisch — Stifte, Handy, Schlüssel, eine Tasche.',
    actSpeak1='Zeigen Sie auf etwas und fragen Sie: „Is this <em>yours</em>?“ Antworten Sie mit <em>mine</em> oder einem Namen.',
    actSpeak2='Beschreiben Sie den Tisch jetzt einer dritten Person. Alles wird zu <em>hers</em>, <em>his</em> oder <em>theirs</em>.',
    actSpeak3='Finden Sie zwei Dinge, die Ihnen beiden gehören. „That one is <em>ours</em>.“',
    actSpeak4='Sagen Sie denselben Satz zweimal: einmal mit Nomen, einmal ohne. <em>my pen</em> → <em>mine</em>.',
    actWriteBrief='Schreiben Sie fünf Sätze über Ihr Klassenzimmer. Jedes Mal ein anderes Wort.',
    actPlaceholder='The blue bag is hers. The pens are…',
    resPerfect='Perfekt. Lena und Sophie sind sehr beeindruckt — Sie können alle sechs.',
    resStrong='Sehr gut. Fast alle. Sehen Sie sich <em>hers</em> und <em>theirs</em> noch einmal an.',
    resMid='Gut gemacht. Gehen Sie zur Tabellenfolie zurück — die zwei Spalten sind die ganze Regel.',
    resLow='Guter Versuch. Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Sie schaffen das.',
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
