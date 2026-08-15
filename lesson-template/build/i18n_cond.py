# -*- coding: utf-8 -*-
"""Interface strings for Business Conditionals (B2), English and German."""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Business <em>Conditionals</em>',
    coverSub='The three conditionals, plus the formal inversions that carry professional correspondence',
    chipLevel='B2 · Grammar', chipFocus='Conditionals at work', chipCount='15 slides',
    rulesEyebrow='The rules, stated once', rulesTitle='Three conditionals, three time frames',
    c1h='First — real',
    c1b='“If the board approves the merger, the company <em>will expand</em>.” Something that may well happen.',
    c2h='Second — hypothetical',
    c2b='“If I <em>were</em> in your position, I <em>would</em> renegotiate.” Unlikely, or simply imagined.',
    c3h='Third — unreal past',
    c3b='“If the CEO <em>had announced</em> it, the board <em>would have had</em> time.” It did not happen. This is regret.',
    formEyebrow='What business writing does instead',
    formTitle='Four formal variants worth recognising on sight',
    v1h='unless',
    v1b='“<em>Unless</em> the client confirms by Friday…” Never <em>will</em> after it.',
    v2h='provided that / once',
    v2b='“<em>Provided that</em> all stakeholders agree…” Present tense, always.',
    v3h='Should + subject + verb',
    v3b='“<em>Should this be</em> required…” = <em>If this should be required…</em>',
    v4h='Had + subject + participle',
    v4b='“<em>Had we reviewed</em> the agreement…” = <em>If we had reviewed…</em>',
    qEyebrow='Choose the conditional', qTitle='Complete the sentence',
    vEyebrow='The form in brackets', vTitle='Put the verb in the right tense',
    vHint='Type the form of the bracketed verb that the conditional needs.',
    eEyebrow='Straight from the inbox', eTitle='Complete the email extract',
    eHint='Three of the eight phrases in the bank are wrong for these gaps.',
    bankLabel='Word bank:',
    actTitle='Write the difficult email', actUse='Use at least four:',
    actWriteKind='Writing · 120–160 words',
    actSpeakBrief='Argue both sides. One of you is the supplier, one the client.',
    actSpeak1='A delivery is late. State the consequence with <em>unless</em>, without threatening.',
    actSpeak2='Offer something conditionally: <em>provided that…</em> Make the condition specific.',
    actSpeak3='Look back at a decision that went wrong. Use the inversion: <em>Had we…</em>',
    actSpeak4='Offer help formally with <em>Should this be required…</em> Then say the same thing casually.',
    actWriteBrief='A supplier has missed two deadlines. Write the email that sets a condition without ending the relationship.',
    actPlaceholder='Dear Mr Harrington,',
    resPerfect='Full marks. The inversions are the part most B2 learners never reach — you have them.',
    resStrong='Strong. The three conditionals are secure; the formal variants reward another pass.',
    resMid='A solid base. Look again at the third conditional — <em>would have</em> + participle is where the misses cluster.',
    resLow='Go back to the two rule slides and run it again. The time frame first, the form after.',
)

T['de'] = dict(
    coverTitle='Business-<em>Conditionals</em>',
    coverSub='Die drei Bedingungssätze und die formellen Inversionen, die geschäftliche Korrespondenz tragen',
    chipLevel='B2 · Grammatik', chipFocus='Bedingungssätze im Beruf', chipCount='15 Folien',
    rulesEyebrow='Die Regeln, einmal ausgesprochen',
    rulesTitle='Drei Bedingungssätze, drei Zeithorizonte',
    c1h='Typ I — real',
    c1b='„If the board approves the merger, the company <em>will expand</em>.“ Etwas, das durchaus eintreten kann.',
    c2h='Typ II — hypothetisch',
    c2b='„If I <em>were</em> in your position, I <em>would</em> renegotiate.“ Unwahrscheinlich oder schlicht gedacht.',
    c3h='Typ III — irreale Vergangenheit',
    c3b='„If the CEO <em>had announced</em> it, the board <em>would have had</em> time.“ Es ist nicht passiert. Das ist Bedauern.',
    formEyebrow='Was geschäftliches Schreiben stattdessen tut',
    formTitle='Vier formelle Varianten, die man auf einen Blick erkennen sollte',
    v1h='unless',
    v1b='„<em>Unless</em> the client confirms by Friday…“ Danach niemals <em>will</em>.',
    v2h='provided that / once',
    v2b='„<em>Provided that</em> all stakeholders agree…“ Immer Präsens.',
    v3h='Should + Subjekt + Verb',
    v3b='„<em>Should this be</em> required…“ = <em>If this should be required…</em>',
    v4h='Had + Subjekt + Partizip',
    v4b='„<em>Had we reviewed</em> the agreement…“ = <em>If we had reviewed…</em>',
    qEyebrow='Wählen Sie den Bedingungssatz', qTitle='Vervollständigen Sie den Satz',
    vEyebrow='Die Form in Klammern', vTitle='Setzen Sie das Verb in die richtige Zeit',
    vHint='Tippen Sie die Form des eingeklammerten Verbs, die der Bedingungssatz verlangt.',
    eEyebrow='Direkt aus dem Postfach', eTitle='Vervollständigen Sie den E-Mail-Auszug',
    eHint='Drei der acht Wendungen in der Liste passen zu keiner dieser Lücken.',
    bankLabel='Wortliste:',
    actTitle='Schreiben Sie die unangenehme E-Mail', actUse='Mindestens vier verwenden:',
    actWriteKind='Schreiben · 120–160 Wörter',
    actSpeakBrief='Vertreten Sie beide Seiten. Eine Person liefert, die andere bestellt.',
    actSpeak1='Eine Lieferung ist verspätet. Nennen Sie die Konsequenz mit <em>unless</em>, ohne zu drohen.',
    actSpeak2='Bieten Sie etwas unter einer Bedingung an: <em>provided that…</em> Machen Sie die Bedingung konkret.',
    actSpeak3='Blicken Sie auf eine falsche Entscheidung zurück. Nutzen Sie die Inversion: <em>Had we…</em>',
    actSpeak4='Bieten Sie förmlich Hilfe an: <em>Should this be required…</em> Sagen Sie dasselbe dann salopp.',
    actWriteBrief='Ein Lieferant hat zwei Termine verpasst. Schreiben Sie die E-Mail, die eine Bedingung setzt, ohne die Beziehung zu beenden.',
    actPlaceholder='Dear Mr Harrington,',
    resPerfect='Volle Punktzahl. Die Inversionen erreichen die meisten B2-Lernenden nie — Sie schon.',
    resStrong='Stark. Die drei Grundtypen sitzen; die formellen Varianten lohnen einen zweiten Durchgang.',
    resMid='Eine solide Grundlage. Sehen Sie sich Typ III noch einmal an — bei <em>would have</em> + Partizip häufen sich die Fehler.',
    resLow='Zurück zu den beiden Regelfolien, dann noch einmal. Erst der Zeithorizont, dann die Form.',
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
