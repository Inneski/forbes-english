# -*- coding: utf-8 -*-
"""Interface strings for Make v Do (B1), English and German.

The taught items stay in English — they are the object of study. German carries
the explanation around them.

`resNext`, `actEyebrow` and `actSpeakKind` are deliberately NOT lifted from
chrome_i18n: this lesson passes its own text for all three, and lifting would
overwrite it with the generic string at runtime.
"""
import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Make <em>v</em> Do',
    coverSub='The rule that covers most of it, the handful that break it, and the phrasal verbs underneath',
    chipLevel='B1 · Intermediate',
    chipFocus='Collocation & phrasal verbs',
    chipCount='26 slides',

    t1e='The split, before anything is graded',
    t1t='One produces a thing. The other performs an activity.',
    t1ah='make → you produce something',
    t1an='<em>make a cake · make a plan · make a decision · make money · make noise · make progress</em>',
    t1bh='do → you perform an activity',
    t1bn='<em>do homework · do research · do the shopping · do the washing-up · do exercise</em>',
    t1ch='The test',
    t1cn='A cake, a plan, a decision — yes, so <em>make</em>. Homework and research are things you <em>did</em>, not things you made.',

    t2e='The exceptions',
    t2t='Four that break the rule, and have to be learned',
    t2ah='make a mistake',
    t2an='By the rule this should be <em>do</em>. It is not. Learn it as a phrase.',
    t2bh='do your best',
    t2bn='It takes <em>do</em> anyway. The mirror image of <em>make a mistake</em>.',
    t2ch='do business',
    t2cn='Also uncountable here — never <em>do a business</em>.',
    t2dh='do exercise',
    t2dn='One of the most reliable first-language slips in this pair.',

    t3e='Phrasal verbs · make',
    t3t='Four with <em>make</em>, grouped by particle',
    t3ah='make off with',
    t3an='<em>The raccoon made off with the sandwiches.</em>',
    t3bh='make up for',
    t3bn='<em>He bought coffee to make up for being late.</em>',
    t3ch='make of',
    t3cn='Nearly always a question: <em>what do you make of it?</em>',
    t3dh='make up',
    t3dn='Separable: <em>made it up</em>, never <em>made up it</em>.',

    t4e='Phrasal verbs · do',
    t4t='Four with <em>do</em> — and two that are easily swapped',
    t4ah='do away with',
    t4an='Formal, and used of rules and systems rather than objects.',
    t4bh='do without',
    t4bn='The pair to watch: <em>do away with</em> is your choice, <em>do without</em> is your circumstance.',
    t4ch='could do with',
    t4cn='Only in the conditional. There is no <em>I do with a coffee</em>.',
    t4dh='do up',
    t4dn='<em>doing up the barn</em>, and <em>do up your coat</em>.',

    gapEyebrow='make or do',
    gapTitle='Complete the sentence',
    bankLabel='Word bank:',
    colEyebrow='Which collocation?',
    colTitle='One of these is English',
    sortEyebrow='Sort',
    sortTitle='Which verb does each one take?',
    sortHint='Drag each expression into a box — or click the expression, then the box. A wrong first placement costs that item’s point.',
    pvEyebrow='Phrasal verbs',
    pvTitle='Complete the sentence',

    resNext='You know which verb. Now use them →',
    resPerfect='Full marks, including the ones that break the rule — which is the part that usually goes wrong.',
    resStrong='Strong. Check whether your misses were the exceptions or the phrasal verbs; they need different work.',
    resMid='A good base. Go back to the exceptions slide — four phrases carry most of the errors in this pair.',
    resLow='Read the first two slides again, then run it once more. The rule covers most of it; only four break it.',

    actEyebrow='Activation',
    actTitle='Say what you made and what you did',
    actUse='Use at least four:',
    actSpeakKind='Speaking · in pairs',
    actSpeakBrief='Last week, in detail. Your partner listens for a wrong collocation and stops you.',
    actSpeak1='Describe one decision you made and one task you did. Do not swap the verbs.',
    actSpeak2='Tell your partner about something you had to do without.',
    actSpeak3='Describe a mistake you made, and how you made up for it.',
    actSpeak4='Name one thing at work or at school you would do away with.',
    actWriteKind='Writing · 120–150 words',
    actWriteBrief='Write about a week when you were very busy: what you made, what you did, and what you had to do without.',
    actPlaceholder='Last week — what I made and what I did',
)

T['de'] = dict(
    coverTitle='Make <em>v</em> Do',
    coverSub='Die Regel, die das meiste abdeckt, die wenigen Ausnahmen und die Phrasal Verbs darunter',
    chipLevel='B1 · Mittelstufe',
    chipFocus='Kollokation & Phrasal Verbs',
    chipCount='26 Folien',

    t1e='Die Unterscheidung, bevor etwas bewertet wird',
    t1t='Das eine erzeugt eine Sache. Das andere führt eine Tätigkeit aus.',
    t1ah='make → du erzeugst etwas',
    t1an='<em>make a cake · make a plan · make a decision · make money · make noise · make progress</em>',
    t1bh='do → du führst eine Tätigkeit aus',
    t1bn='<em>do homework · do research · do the shopping · do the washing-up · do exercise</em>',
    t1ch='Die Probe',
    t1cn='Ein Kuchen, ein Plan, eine Entscheidung — ja, also <em>make</em>. Hausaufgaben und Forschung sind Dinge, die man <em>getan</em> hat, nicht hergestellt.',

    t2e='Die Ausnahmen',
    t2t='Vier, die die Regel brechen und gelernt werden müssen',
    t2ah='make a mistake',
    t2an='Nach der Regel müsste es <em>do</em> heißen. Tut es nicht. Als feste Wendung lernen.',
    t2bh='do your best',
    t2bn='Nimmt trotzdem <em>do</em>. Das Spiegelbild von <em>make a mistake</em>.',
    t2ch='do business',
    t2cn='Hier außerdem unzählbar — niemals <em>do a business</em>.',
    t2dh='do exercise',
    t2dn='„Sport machen“ führt hier besonders zuverlässig zum falschen Verb.',

    t3e='Phrasal Verbs · make',
    t3t='Vier mit <em>make</em>, nach Partikel geordnet',
    t3ah='make off with',
    t3an='<em>The raccoon made off with the sandwiches.</em> — damit verschwinden.',
    t3bh='make up for',
    t3bn='<em>He bought coffee to make up for being late.</em> — ausgleichen.',
    t3ch='make of',
    t3cn='Fast immer als Frage: <em>what do you make of it?</em> — davon halten.',
    t3dh='make up',
    t3dn='Trennbar: <em>made it up</em>, nie <em>made up it</em>. — erfinden.',

    t4e='Phrasal Verbs · do',
    t4t='Vier mit <em>do</em> — und zwei, die leicht verwechselt werden',
    t4ah='do away with',
    t4an='Formell, eher für Regeln und Systeme als für Gegenstände. — abschaffen.',
    t4bh='do without',
    t4bn='Das Paar zum Aufpassen: <em>do away with</em> ist deine Entscheidung, <em>do without</em> deine Lage.',
    t4ch='could do with',
    t4cn='Nur im Konditional. Es gibt kein <em>I do with a coffee</em>. — gut gebrauchen können.',
    t4dh='do up',
    t4dn='<em>doing up the barn</em> (renovieren) und <em>do up your coat</em> (zumachen).',

    gapEyebrow='make oder do',
    gapTitle='Vervollständigen Sie den Satz',
    bankLabel='Wortspeicher:',
    colEyebrow='Welche Kollokation?',
    colTitle='Eine davon ist Englisch',
    sortEyebrow='Sortieren',
    sortTitle='Welches Verb nimmt jeder Ausdruck?',
    sortHint='Ziehen Sie jeden Ausdruck in ein Feld — oder klicken Sie erst den Ausdruck, dann das Feld. Eine falsche erste Zuordnung kostet den Punkt.',
    pvEyebrow='Phrasal Verbs',
    pvTitle='Vervollständigen Sie den Satz',

    resNext='Sie wissen, welches Verb. Jetzt anwenden →',
    resPerfect='Volle Punktzahl, inklusive der Ausnahmen — genau die gehen sonst schief.',
    resStrong='Stark. Prüfen Sie, ob Ihre Fehler bei den Ausnahmen oder den Phrasal Verbs lagen; das sind zwei verschiedene Baustellen.',
    resMid='Eine gute Grundlage. Zurück zur Ausnahmen-Folie — vier Wendungen verursachen die meisten Fehler.',
    resLow='Lesen Sie die ersten beiden Folien noch einmal und starten Sie neu. Die Regel deckt das meiste ab; nur vier brechen sie.',

    actEyebrow='Anwendung',
    actTitle='Sagen Sie, was Sie gemacht und was Sie getan haben',
    actUse='Verwenden Sie mindestens vier:',
    actSpeakKind='Sprechen · zu zweit',
    actSpeakBrief='Die letzte Woche, im Detail. Ihr Gegenüber hört auf falsche Kollokationen und unterbricht Sie.',
    actSpeak1='Beschreiben Sie eine Entscheidung, die Sie getroffen haben, und eine Aufgabe, die Sie erledigt haben. Vertauschen Sie die Verben nicht.',
    actSpeak2='Erzählen Sie von etwas, auf das Sie verzichten mussten.',
    actSpeak3='Beschreiben Sie einen Fehler, den Sie gemacht haben, und wie Sie ihn ausgeglichen haben.',
    actSpeak4='Nennen Sie eine Sache in Arbeit oder Schule, die Sie abschaffen würden.',
    actWriteKind='Schreiben · 120–150 Wörter',
    actWriteBrief='Schreiben Sie über eine sehr volle Woche: was Sie gemacht haben, was Sie getan haben und worauf Sie verzichten mussten.',
    actPlaceholder='Last week — what I made and what I did',
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
