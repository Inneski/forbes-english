# -*- coding: utf-8 -*-
"""Interface strings for The Nature Agency Part 1 (C1), English and German.

The taught items stay in English throughout — they are the object of study.
German carries the explanation around them.

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
    coverTitle='The <em>Nature Agency</em>',
    coverSub='Elena Voss’s first weeks as a field officer — and the second sense of every word she already knew',
    chipLevel='C1 · Advanced',
    chipFocus='Sense discrimination & register',
    chipCount='36 slides',

    t1e='Before the first question',
    t1t='This section is not testing whether you know these words',
    t1ah='You already know them',
    t1an='Not one of them is rare. That is deliberate, and it is the point of the exercise.',
    t1bh='It tests which <em>sense</em>',
    t1bn='Usually the second sense — the formal, technical or idiomatic one, not the one you learned first.',
    t1ch='Five words appear twice',
    t1cn='Each is tested once in each sense, on consecutive slides. When you meet a word for the second time, ask what changed.',

    t2e='The transferable part',
    t2t='Three tells for picking the right sense',
    t2ah='1 · The collocation',
    t2an='<em>A report circulates</em> is a rumour. <em>To report a sighting</em> is an account. Same word, different company.',
    t2bh='2 · The grammar',
    t2bn='<em>Reconcile X with Y</em> makes two things fit. <em>Reconcile with Y</em> repairs a relationship. Count the objects.',
    t2ch='3 · The register',
    t2cn='A formal sentence pulls a formal sense. <em>In receipt of your letter</em> is not the slip from a till.',

    t3e='Contrast one',
    t3t='<em>report</em> — three senses, and one of them is a sound',
    t3ah='a report <span class="dim">(noun)</span>',
    t3an='Also the formal written kind — <em>the annual report</em>. The article and the verb around it tell you which.',
    t3bh='to report <span class="dim">(verb)</span>',
    t3bn='Takes a direct object. Also <em>report to</em> someone — the person you answer to.',
    t3ch='the report <span class="dim">(of a rifle)</span>',
    t3cn='Rare in general English and routine in this one. On a reserve dealing with poaching and culls, it is the sense you will need in writing.',

    t4e='Contrast two and three',
    t4t='<em>critic</em> and <em>decay</em> — opinion, and word class',
    t4ah='critic — the objector',
    t4an='Unfavourable by definition. Comes with <em>vocal</em>, <em>fierce</em>, <em>outspoken</em>.',
    t4bh='critic — the reviewer',
    t4bn='Carries no judgement at all. A critic in this sense can love everything they review.',
    t4ch='decay — verb, then noun',
    t4cn='The article is the tell. Adjectives such as <em>visible</em> or <em>advanced</em> can only modify the noun.',

    t5e='Contrast four',
    t5t='<em>reconcile</em> — the preposition tells you the sense',
    t5ah='reconcile X <em>with</em> Y',
    t5an='Two objects. Bookkeeping, evidence, competing versions of a number. Nothing to do with feelings.',
    t5bh='reconcile <em>with</em> Y',
    t5bn='No direct object. People, or groups of them.',
    t5ch='Why it generalises',
    t5cn='The same test settles <em>dwell</em> on the next slide, and dozens of verbs beyond this lesson.',

    t6e='Contrast five',
    t6t='<em>dwell</em> — add a preposition, change the subject',
    t6ah='dwell <span class="dim">(somewhere)</span>',
    t6an='Formal and a little archaic. It survives mostly in <em>dwelling</em>, which is the word a planning document uses for a house.',
    t6bh='dwell <em>on</em> <span class="dim">(something)</span>',
    t6bn='Almost always something unhappy. To dwell on a success is to boast; the word expects a grievance.',
    t6ch='Same tell as <em>reconcile</em>',
    t6cn='Two pairs, one rule. This is the tell worth carrying out of the lesson.',

    t7e='The pair that matters most here',
    t7t='<em>prevalent</em> or <em>rampant</em> — both mean widespread',
    t7ah='prevalent',
    t7an='Neutral. It reports a frequency and passes no judgement. Any disapproval in the sentence comes from other words.',
    t7bh='rampant',
    t7bn='Carries two things at once: widespread, <em>and</em> bad, <em>and</em> nobody is stopping it. Never a compliment.',
    t7ch='For a conservation agency',
    t7cn='Choosing the wrong one in a site report either understates a problem or editorialises about a healthy population.',

    t8e='Register',
    t8t='The formal senses these same words carry',
    t8ah='in receipt of',
    t8an='Formal acknowledgement that something arrived. Not the slip of paper — the same word doing near-legal work.',
    t8bh='to launder',
    t8bn='From <em>laundry</em>. To wash money is to make illegal money look clean. Also <em>airing dirty laundry</em> — private disputes made public.',
    t8ch='the decay of an institution',
    t8cn='The rot sense, applied to something abstract. This is the register a field officer writes reports in.',
    t8dh='domineering',
    t8dn='Arrogant and controlling — the near-opposite of <em>humble</em>, which you will meet shortly.',

    qEyebrow='Which sense is it?',
    qTitle='Read the sentence, then choose',
    gapEyebrow='The exact word',
    gapTitle='Complete the briefing',
    gapHint='Every word in the bank is used exactly once on this slide.',
    bankLabel='Word bank:',
    sortEyebrow='Register',
    sortTitle='Sort these by how formal they are',
    sortTitle2='Sort these by how formal they are',
    sortHint='Drag each term into a box — or click the term, then the box. A wrong first placement costs that term’s point.',

    resNext='You can pick the sense. Now produce it →',
    resPerfect='Full marks. You can hear the difference between two senses of the same word, which is most of what C1 is.',
    resStrong='Strong. The contrasts have landed — the register slide is the one worth a second look.',
    resMid='A good base. Go back to the three tells: collocation, grammar, register. Most misses come from skipping the second.',
    resLow='Read the opening slides again before retrying. The skill is picking the sense, not learning new words.',

    actEyebrow='Activation',
    actTitle='Write the site report',
    actUse='Use at least four:',
    actSpeakKind='Speaking · in pairs',
    actSpeakBrief='One field officer, one landowner. The survey figures do not agree.',
    actSpeak1='Report a sighting formally, then report a rumour. Make the difference audible.',
    actSpeak2='Say the snaring is <em>prevalent</em>. Then say the knotweed is <em>rampant</em>. Explain to your partner why you did not swap the words.',
    actSpeak3='Reconcile your figures with theirs — then reconcile with them.',
    actSpeak4='Disagree without becoming domineering.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write the summary paragraph of a site report: what you observed, what is disputed, and what you recommend. Formal register throughout.',
    actPlaceholder='Site report — eastern slope, October',
)

T['de'] = dict(
    coverTitle='The <em>Nature Agency</em>',
    coverSub='Elena Voss’ erste Wochen im Außendienst — und die zweite Bedeutung jedes Wortes, das sie schon kannte',
    chipLevel='C1 · Fortgeschritten',
    chipFocus='Bedeutungsunterscheidung & Register',
    chipCount='36 Folien',

    t1e='Vor der ersten Frage',
    t1t='Hier wird nicht geprüft, ob Sie diese Wörter kennen',
    t1ah='Sie kennen sie bereits',
    t1an='Keines davon ist selten. Das ist Absicht und genau der Sinn der Übung.',
    t1bh='Geprüft wird, <em>welche</em> Bedeutung',
    t1bn='Meist die zweite — die formelle, fachliche oder idiomatische, nicht die zuerst gelernte.',
    t1ch='Fünf Wörter kommen zweimal vor',
    t1cn='Jedes wird einmal in jeder Bedeutung geprüft, auf aufeinanderfolgenden Folien. Fragen Sie beim zweiten Mal, was sich geändert hat.',

    t2e='Der übertragbare Teil',
    t2t='Drei Hinweise auf die richtige Bedeutung',
    t2ah='1 · Die Kollokation',
    t2an='<em>A report circulates</em> ist ein Gerücht. <em>To report a sighting</em> ist eine Meldung. Gleiches Wort, andere Umgebung.',
    t2bh='2 · Die Grammatik',
    t2bn='<em>Reconcile X with Y</em> bringt zwei Dinge in Einklang. <em>Reconcile with Y</em> versöhnt. Zählen Sie die Objekte.',
    t2ch='3 · Das Register',
    t2cn='Ein formeller Satz zieht eine formelle Bedeutung nach sich. <em>In receipt of your letter</em> ist nicht der Kassenbon.',

    t3e='Gegensatz eins',
    t3t='<em>report</em> — drei Bedeutungen, und eine davon ist ein Geräusch',
    t3ah='a report <span class="dim">(Substantiv)</span>',
    t3an='Auch der formelle schriftliche Bericht — <em>the annual report</em>. Artikel und Verb verraten, welche Bedeutung gilt.',
    t3bh='to report <span class="dim">(Verb)</span>',
    t3bn='Mit direktem Objekt. Auch <em>report to</em> jemandem — die Person, der man unterstellt ist.',
    t3ch='the report <span class="dim">(eines Gewehrs)</span>',
    t3cn='Im Alltagsenglisch selten, in dieser Lektion Routine. Auf einem Schutzgebiet mit Wilderei und Abschüssen ist es die Bedeutung, die man schriftlich braucht.',

    t4e='Gegensatz zwei und drei',
    t4t='<em>critic</em> und <em>decay</em> — Wertung und Wortart',
    t4ah='critic — der Kritiker im Sinne von Gegner',
    t4an='Per Definition ablehnend. Steht bei <em>vocal</em>, <em>fierce</em>, <em>outspoken</em>.',
    t4bh='critic — der Rezensent',
    t4bn='Völlig wertfrei. Ein Kritiker in diesem Sinne kann alles lieben, was er bespricht.',
    t4ch='decay — erst Verb, dann Substantiv',
    t4cn='Der Artikel ist der Hinweis. Adjektive wie <em>visible</em> oder <em>advanced</em> können nur das Substantiv näher bestimmen.',

    t5e='Gegensatz vier',
    t5t='<em>reconcile</em> — die Präposition verrät die Bedeutung',
    t5ah='reconcile X <em>with</em> Y',
    t5an='Zwei Objekte. Buchhaltung, Belege, widersprüchliche Zahlen. Nichts mit Gefühlen zu tun.',
    t5bh='reconcile <em>with</em> Y',
    t5bn='Kein direktes Objekt. Personen oder Gruppen.',
    t5ch='Warum das übertragbar ist',
    t5cn='Derselbe Test klärt <em>dwell</em> auf der nächsten Folie — und Dutzende Verben über diese Lektion hinaus.',

    t6e='Gegensatz fünf',
    t6t='<em>dwell</em> — eine Präposition dazu, und das Thema wechselt',
    t6ah='dwell <span class="dim">(irgendwo)</span>',
    t6an='Formell und leicht altertümlich. Erhalten vor allem in <em>dwelling</em>, dem Wort für Wohngebäude in Bauunterlagen.',
    t6bh='dwell <em>on</em> <span class="dim">(etwas)</span>',
    t6bn='Fast immer etwas Unerfreuliches. Über einen Erfolg zu „dwell“ heißt angeben; das Wort erwartet einen Kummer.',
    t6ch='Gleicher Hinweis wie bei <em>reconcile</em>',
    t6cn='Zwei Paare, eine Regel. Das ist der Hinweis, den man aus der Lektion mitnimmt.',

    t7e='Das hier wichtigste Paar',
    t7t='<em>prevalent</em> oder <em>rampant</em> — beide heißen „weit verbreitet“',
    t7ah='prevalent',
    t7an='Neutral. Es nennt eine Häufigkeit und wertet nicht. Missbilligung im Satz kommt von anderen Wörtern.',
    t7bh='rampant',
    t7bn='Trägt zweierlei zugleich: weit verbreitet, <em>und</em> schlecht, <em>und</em> niemand stoppt es. Nie ein Lob.',
    t7ch='Für eine Naturschutzbehörde',
    t7cn='Eine heimische Art ist <strong>prevalent</strong>. Eine invasive Art ist <strong>rampant</strong>.',

    t8e='Register',
    t8t='Die formellen Bedeutungen derselben Wörter',
    t8ah='in receipt of',
    t8an='Formelle Bestätigung des Eingangs. Nicht der Kassenbon — dasselbe Wort in nahezu juristischer Funktion.',
    t8bh='to launder',
    t8bn='Von <em>laundry</em>. Geld zu waschen heißt, illegales Geld sauber aussehen zu lassen. Auch <em>airing dirty laundry</em> — Privates öffentlich machen.',
    t8ch='the decay of an institution',
    t8cn='Die Verfallsbedeutung, auf Abstraktes angewandt. Das ist das Register, in dem Berichte geschrieben werden.',
    t8dh='domineering',
    t8dn='Herrisch und kontrollierend — das nahezu Gegenteil von <em>humble</em>, das gleich vorkommt.',

    qEyebrow='Welche Bedeutung ist gemeint?',
    qTitle='Lesen Sie den Satz und wählen Sie',
    gapEyebrow='Das genaue Wort',
    gapTitle='Vervollständigen Sie das Briefing',
    gapHint='Jedes Wort aus dem Wortspeicher wird auf dieser Folie genau einmal verwendet.',
    bankLabel='Wortspeicher:',
    sortEyebrow='Register',
    sortTitle='Ordnen Sie nach Formalität',
    sortTitle2='Ordnen Sie nach Formalität',
    sortHint='Ziehen Sie jeden Begriff in ein Feld — oder klicken Sie erst den Begriff, dann das Feld. Eine falsche erste Zuordnung kostet den Punkt für diesen Begriff.',

    resNext='Sie erkennen die Bedeutung. Jetzt produzieren Sie sie →',
    resPerfect='Volle Punktzahl. Sie hören den Unterschied zwischen zwei Bedeutungen desselben Wortes — das ist der Kern von C1.',
    resStrong='Stark. Die Gegensätze sitzen — die Registerfolie lohnt noch einen zweiten Blick.',
    resMid='Eine gute Grundlage. Zurück zu den drei Hinweisen: Kollokation, Grammatik, Register. Die meisten Fehler entstehen, wenn der zweite übersprungen wird.',
    resLow='Lesen Sie die Einstiegsfolien noch einmal, bevor Sie es erneut versuchen. Es geht ums Erkennen der Bedeutung, nicht um neue Wörter.',

    actEyebrow='Anwendung',
    actTitle='Schreiben Sie den Standortbericht',
    actUse='Verwenden Sie mindestens vier:',
    actSpeakKind='Sprechen · zu zweit',
    actSpeakBrief='Eine Person im Außendienst, eine Person als Grundeigentümer. Die Erhebungszahlen stimmen nicht überein.',
    actSpeak1='Melden Sie erst formell eine Sichtung, dann ein Gerücht. Machen Sie den Unterschied hörbar.',
    actSpeak2='Sagen Sie, die Schlingenstellerei sei <em>prevalent</em>. Dann, der Staudenknöterich sei <em>rampant</em>. Erklären Sie, warum Sie die Wörter nicht getauscht haben.',
    actSpeak3='Gleichen Sie Ihre Zahlen mit deren Zahlen ab — und versöhnen Sie sich dann mit der Person.',
    actSpeak4='Widersprechen Sie, ohne herrisch zu werden.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreiben Sie den zusammenfassenden Absatz eines Standortberichts: was Sie beobachtet haben, was strittig ist, was Sie empfehlen. Durchgehend formelles Register.',
    actPlaceholder='Site report — eastern slope, October',
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
