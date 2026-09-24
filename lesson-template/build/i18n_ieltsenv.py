# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Environment and Energy.

Ten languages: English, German and Spanish from the start; French,
Italian, Portuguese, Russian, Arabic, Chinese and Japanese added on
2026-09-24 (conventions in `ielts_langs.py`).

The usual split (HOUSE-STYLE §8), and on a topic bank it is the whole deck:
the pairings are the lesson. <em>Cut emissions</em>, <em>generate
electricity</em>, <em>sent to landfill</em> stay English inside the German and
Spanish cards, because the point is which English word the English noun takes.
What translates is the rule, the argument each idea arrives with, and every
explanation.

`sortWhy` is a key rather than a sentence so the sort explanation translates
with the rest — the engine resolves a data-explain key against UI_I18N.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from chrome_i18n import CHROME
from ielts_langs import TAIL_MORE

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

TAIL = {
    'en': {'branchLocked': "'Your ledger does not support this ending'",
           'glossHide': "'Hide'", 'glossShow': "'Translate'",
           'ledClues': "'Clues'", 'ledDp': "'DP'", 'ledTime': "'Time'"},
    'de': {'branchLocked': "'Dein Protokoll trägt dieses Ende nicht'",
           'glossHide': "'Ausblenden'", 'glossShow': "'Übersetzen'",
           'ledClues': "'Hinweise'", 'ledDp': "'DP'", 'ledTime': "'Zeit'"},
    'es': {'branchLocked': "'Tu registro no admite este final'",
           'glossHide': "'Ocultar'", 'glossShow': "'Traducir'",
           'ledClues': "'Pistas'", 'ledDp': "'DP'", 'ledTime': "'Tiempo'"},
}

TAIL.update(TAIL_MORE)

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='The first topic bank: three ideas, each with its pairings and '
             'its argument already attached',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Idea 1 of 3',
    t1Title='Emissions: four pairings and two arguments',
    t1ah='Cut them &mdash; the noun picks the verb',
    t1ab='Emissions are <em>cut</em>, <em>reduced</em> or <em>curbed</em>; a '
         'country <em>burns fossil fuels</em> and releases <em>greenhouse '
         'gases</em>; a city measures its <em>air quality</em>. The verb is '
         'chosen by the noun, and none of these is rare.',
    t1an='Four pairings, learnt whole. A bare <em>emissions</em> in the '
         'notebook is worth none of them.',
    t1bh='The footprint and the tax',
    t1bb='A person or a firm has a <em>carbon footprint</em>, and shrinking '
         'it is what a <em>carbon tax</em> is for. Both are fixed: the mark '
         'you leave is a <em>footprint</em>, not a trace, and the charge is a '
         '<em>tax</em>, not a fine.',
    t1bn='File them together. The tax exists because of the footprint.',
    t1ch='The argument it arrives with',
    t1cb='Two arguments come up again and again here. <strong>Who '
         'pays</strong>: dirty air lands on people who did not produce it. '
         '<strong>Targets against enforcement</strong>: a country can '
         'promise to halve its emissions and never fine a single factory.',
    t1cn='File the idea, and the paragraph is half-written before the '
         'question is read.',

    t2Eyebrow='Idea 2 of 3',
    t2Title='Renewables: generate, subsidise, phase out',
    t2ah='Generate: the verb to reach for',
    t2ab='A <em>wind farm</em> or a roof of <em>solar panels</em> '
         '<em>generates electricity</em>, and what it generates feeds the '
         '<em>national grid</em>. <em>Renewable energy</em> is the umbrella '
         'term; <em>renewables</em> on its own is the noun a Part 3 answer '
         'uses.',
    t2an='Four pairings and one umbrella noun. All plain, none of them rare.',
    t2bh='The precise word for the weakness',
    t2bb='The sun sets and the wind drops, so the supply is '
         '<em>intermittent</em>: it comes and goes on its own schedule. '
         'Several words sound close and mean something else, and the '
         'examiner counts the one that means what you meant.',
    t2bn='A near-miss that sounds advanced is still a miss; the plain word '
         'that lands is not.',
    t2ch='The argument it arrives with',
    t2cb='Governments <em>subsidise</em> renewables and <em>phase out '
         'coal</em>, and most essays on the topic weigh the same two '
         'tensions. <strong>Reliability against cost</strong>: cheap to '
         'generate, dear to store. <strong>Subsidy against the '
         'market</strong>: the panels exist because someone paid, and may '
         'need someone to keep paying.',
    t2cn='<em>Energy security</em> is the third term: a country that '
         'generates its own power cannot be cut off.',

    t3Eyebrow='Idea 3 of 3',
    t3Title='Consumption and waste: the pairing includes the preposition',
    t3ah='Sent to landfill, cut down on',
    t3ab='Rubbish is <em>sent to landfill</em>; a council reports its '
         '<em>recycling rates</em>; a shopper <em>cuts down on</em> '
         '<em>excess packaging</em>. The preposition belongs to the pairing: '
         'in British English <em>landfill</em> takes no article (American '
         'English says <em>a landfill</em>), and the phrasal verb is two '
         'particles, not one.',
    t3an='Write the whole thing. Half a phrasal verb is a miss.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='A bottle used once is <em>single-use plastic</em>; a society that '
         'expects to bin things has a <em>throwaway culture</em>; a scheme '
         'that pays you to bring the bottle back is a <em>deposit '
         'scheme</em>. Two adjective-noun pairings and a compound noun, none '
         'of them rare.',
    t3bn='<em>A throwaway culture</em> says more than <em>consumerism</em>: '
         'it names the habit, not just the system.',
    t3ch='The argument it arrives with',
    t3cb='Ask who should change and the answer is written. '
         '<strong>Individual against producer responsibility</strong>: a '
         'shopper can change <em>consumer habits</em>, but the packaging was '
         'decided before the shopper arrived. <strong>Convenience against '
         'cost</strong>: single-use is cheap now and paid for later.',
    t3cn='Both arguments run either way round, which is what makes them '
         'worth filing.',

    mcaEyebrow='Activity 1 · Emissions',
    mcaTitle='Which pairing, and which word?',
    mcbEyebrow='Activity 2 · Renewables',
    mcbTitle='Which pairing, and which word?',
    mccEyebrow='Activity 3 · Consumption and waste',
    mccTitle='Which pairing, and which word?',

    v1why='<em>Cut emissions</em> &mdash; or <em>reduce</em>, <em>lower</em> '
          'or <em>curb</em> them. <em>Lower down</em> and <em>shrink '
          'off</em> add a particle English does not use here, and '
          '<em>descend</em> means go down, not bring something down.',
    v2why='A <em>carbon footprint</em>. Nobody derives it &mdash; it is '
          'learnt whole, and a step, a trace or a fingerprint each announce '
          'that it was not.',
    v3why='Who pays. The cost of poor air lands on people who did not '
          'produce it &mdash; an argument this idea often arrives with, and '
          'a shape a Part 3 answer can borrow whole.',
    v4why='<em>A carbon tax</em> is the usual name (you will also meet '
          '<em>carbon price</em> and <em>carbon levy</em>). A fine punishes '
          'breaking a rule, a tariff is charged on imports, and a toll on a '
          'road or a bridge.',
    v5why='<em>Generate electricity</em> (or <em>produce</em> it). '
          '<em>Fabricate</em> and <em>manufacture</em> are for objects, and '
          '<em>originate</em> is not a verb anyone uses of power.',
    v6why='<em>Intermittent</em>: it comes and goes as part of how the '
          'source works. <em>Interrupted</em> is a break caused by an event, '
          '<em>infrequent</em> means rarely, and <em>intermediate</em> is a '
          'different word that merely sounds close.',
    v7why='<em>Phase out coal</em>. The particle is part of the verb, and '
          'only <em>out</em> carries the meaning of ending something in '
          'stages.',
    v8why='Subsidy against the market. The candidate grants that public '
          'money built the turbines, then asks whether the industry can ever '
          'do without it &mdash; one idea, both sides, the kind of developed '
          'answer Part 3 is built to draw out.',
    v9why='<em>Sent to landfill</em> &mdash; no article in British English, '
          'though American English says <em>a landfill</em>. The other three '
          'describe the same hole in the ground in words English does not '
          'use for it.',
    v10why='<em>Single-use plastic</em>. The adjective is hyphenated and '
           'fixed; the alternatives each mean the same thing, and each marks '
           'the writer as guessing.',
    v11why='<em>Cut down on</em> &mdash; or <em>cut back on</em>. A phrasal '
           'verb travels with all its particles: <em>cut off</em> and '
           '<em>cut away</em> are real verbs that mean something else, '
           'neither takes <em>on</em>, and <em>cut back off</em> is not '
           'English.',
    v12why='Producer over individual responsibility. The shopper is told to '
           'change while the decision that matters was taken in the '
           'packaging department. The argument and the pairing <em>excess '
           'packaging</em> arrive together.',

    sortEyebrow='Activity 4 · Filing by idea',
    sortTitle='File the six pairings',
    sortHint='Drag each one into a column &mdash; or click an item, then the '
             'column you want it in.',
    sortBin1='Emissions and energy',
    sortBin2='Consumption and waste',
    sortWhy='Filed by idea, each pairing sits next to the argument it '
            'serves. <em>Burn fossil fuels</em> and <em>phase out coal</em> '
            'are already half a paragraph on emissions and the move away '
            'from coal; <em>a throwaway '
            'culture</em> and <em>excess packaging</em> are half a paragraph '
            'on producer responsibility. Filed alphabetically they are six '
            'words, and under time you would have nothing to say with them.',

    actTitle='Answer from the bank',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. One of you is the examiner and asks three Part '
                  '3 questions on the environment &mdash; whether '
                  'governments or individuals should act on emissions, '
                  'whether renewables can replace coal, whether recycling is '
                  'worth the effort. The other answers using pairings from '
                  'the bank. Swap after three.',
    actSpeak1='Every answer carries at least one pairing from the bank, said '
              'whole &mdash; the verb with its noun, or the adjective with '
              'its noun.',
    actSpeak2='The examiner asks <em>why</em> after every answer. The '
              'follow-up has to use one of the arguments the idea arrived '
              'with: who pays, reliability against cost, individual against '
              'producer.',
    actSpeak3='If the word is not in the bank, describe the thing in plain '
              'English rather than reaching for a rare word.',
    actWriteKind='Writing · 150–200 words',
    actWriteBrief='Write one Task 2 body paragraph on one of the three ideas '
                  '&mdash; emissions, renewables, or consumption and waste. '
                  'Use at least five pairings from the bank and underline '
                  'each one. Then say which argument the paragraph is making.',
    actPlaceholder='The most effective way to cut emissions is…',
)

# ── German ─────────────────────────────────────────────────────────────
T['de'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='Die erste Themensammlung: drei Ideen, jede mit ihren Wortverbindungen '
             'und ihrem Argument im Schlepptau',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 Punkte',

    t1Eyebrow='Idee 1 von 3',
    t1Title='Emissionen: vier Wortverbindungen und zwei Argumente',
    t1ah='Senken &mdash; das Substantiv wählt das Verb',
    t1ab='Emissionen werden <em>cut</em>, <em>reduced</em> oder '
         '<em>curbed</em>; ein Land <em>burns fossil fuels</em> und setzt '
         '<em>greenhouse gases</em> frei; eine Stadt misst ihre <em>air '
         'quality</em>. Das Verb wählt das Substantiv, und keines davon ist '
         'selten.',
    t1an='Vier Wortverbindungen, als Ganzes gelernt. Ein nacktes <em>emissions</em> '
         'im Heft ist keine davon wert.',
    t1bh='Der Fußabdruck und die Steuer',
    t1bb='Eine Person oder eine Firma hat einen <em>carbon footprint</em>, '
         'und ihn zu verkleinern ist der Zweck einer <em>carbon tax</em>. '
         'Beide sind feste Wörter: die Spur, die du hinterlässt, ist ein '
         '<em>footprint</em>, kein trace, und die Abgabe ist eine '
         '<em>tax</em>, keine fine.',
    t1bn='Zusammen ablegen. Die Steuer gibt es wegen des Fußabdrucks.',
    t1ch='Das Argument, das mitkommt',
    t1cb='Zwei Argumente kommen hier immer wieder. <strong>Wer '
         'zahlt</strong>: Schlechte Luft trifft Menschen, die sie nicht '
         'verursacht haben. <strong>Ziele gegen Durchsetzung</strong>: Ein '
         'Land kann versprechen, seine Emissionen zu halbieren, und nie eine '
         'einzige Fabrik bestrafen.',
    t1cn='Leg die Idee ab, und der Absatz ist halb geschrieben, bevor du die '
         'Frage gelesen hast.',

    t2Eyebrow='Idee 2 von 3',
    t2Title='Erneuerbare: generate, subsidise, phase out',
    t2ah='Generate: das Verb, nach dem man greift',
    t2ab='Eine <em>wind farm</em> oder ein Dach voller <em>solar panels</em> '
         '<em>generates electricity</em>, und was erzeugt wird, speist das '
         '<em>national grid</em>. <em>Renewable energy</em> ist der '
         'Oberbegriff; <em>renewables</em> allein ist das Substantiv, das '
         'eine Antwort in Teil 3 verwendet.',
    t2an='Vier Wortverbindungen und ein Oberbegriff. Alle schlicht, keine '
         'davon selten.',
    t2bh='Das genaue Wort für die Schwäche',
    t2bb='Die Sonne geht unter und der Wind legt sich, also ist die '
         'Versorgung <em>intermittent</em>: sie kommt und geht nach eigenem '
         'Plan. Mehrere Wörter klingen ähnlich und bedeuten etwas anderes, '
         'und der Prüfer zählt das, das bedeutet, was du meintest.',
    t2bn='Ein Fehlgriff, der fortgeschritten klingt, bleibt ein Fehlgriff; '
         'das schlichte Wort, das sitzt, nicht.',
    t2ch='Das Argument, das mitkommt',
    t2cb='Regierungen <em>subsidise</em> erneuerbare Energien und <em>phase '
         'out coal</em>, und die meisten Aufsätze zum Thema wägen dieselben '
         'zwei Spannungen ab. <strong>Verlässlichkeit gegen Kosten</strong>: '
         'billig zu erzeugen, teuer zu speichern. <strong>Subvention gegen '
         'Markt</strong>: Die Paneele gibt es, weil jemand bezahlt hat, und '
         'vielleicht muss jemand weiterzahlen.',
    t2cn='<em>Energy security</em> ist der dritte Begriff: ein Land, das '
         'seinen Strom selbst erzeugt, kann nicht abgeschnitten werden.',

    t3Eyebrow='Idee 3 von 3',
    t3Title='Konsum und Abfall: die Präposition gehört zur Wortverbindung',
    t3ah='Sent to landfill, cut down on',
    t3ab='Müll wird <em>sent to landfill</em>; eine Gemeinde meldet ihre '
         '<em>recycling rates</em>; eine Käuferin <em>cuts down on</em> '
         '<em>excess packaging</em>. Die Präposition gehört zur '
         'Wortverbindung: Im britischen Englisch steht <em>landfill</em> '
         'ohne Artikel (im amerikanischen <em>a landfill</em>), und das '
         'Phrasal Verb hat zwei Partikeln, nicht eine.',
    t3an='Schreib das Ganze. Ein halbes Phrasal Verb ist ein Fehlgriff.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='Eine Flasche für einmal ist <em>single-use plastic</em>; eine '
         'Gesellschaft, die Dinge wegwirft, hat eine <em>throwaway '
         'culture</em>; ein System, das dich für die Rückgabe der Flasche '
         'bezahlt, ist ein <em>deposit scheme</em>. Zwei Verbindungen aus '
         'Adjektiv und Substantiv und ein zusammengesetztes Substantiv, '
         'keine davon selten.',
    t3bn='<em>A throwaway culture</em> sagt mehr als <em>consumerism</em>: '
         'Es benennt die Gewohnheit, nicht nur das System.',
    t3ch='Das Argument, das mitkommt',
    t3cb='Frag, wer sich ändern soll, und die Antwort steht. '
         '<strong>Einzelner gegen Hersteller</strong>: ein Käufer kann seine '
         '<em>consumer habits</em> ändern, aber die Verpackung wurde '
         'entschieden, bevor er den Laden betrat. <strong>Bequemlichkeit '
         'gegen Kosten</strong>: Einweg ist jetzt billig und wird später '
         'bezahlt.',
    t3cn='Beide Argumente laufen in beide Richtungen, und genau deshalb '
         'lohnt es sich, sie abzulegen.',

    mcaEyebrow='Aktivität 1 · Emissionen',
    mcaTitle='Welche Wortverbindung, und welches Wort?',
    mcbEyebrow='Aktivität 2 · Erneuerbare',
    mcbTitle='Welche Wortverbindung, und welches Wort?',
    mccEyebrow='Aktivität 3 · Konsum und Abfall',
    mccTitle='Welche Wortverbindung, und welches Wort?',

    v1why='<em>Cut emissions</em> &mdash; oder <em>reduce</em>, '
          '<em>lower</em> bzw. <em>curb</em> sie. <em>Lower down</em> und '
          '<em>shrink off</em> fügen eine Partikel hinzu, die das Englische '
          'hier nicht benutzt, und <em>descend</em> heißt hinuntergehen, '
          'nicht etwas senken.',
    v2why='Ein <em>carbon footprint</em>. Niemand leitet es her &mdash; es '
          'wird als Ganzes gelernt, und step, trace oder fingerprint '
          'verraten, dass es das nicht wurde.',
    v3why='Wer zahlt. Die Kosten schlechter Luft treffen Menschen, die sie '
          'nicht verursacht haben &mdash; ein Argument, mit dem diese Idee '
          'oft kommt, und eine Form, die eine Antwort in Teil 3 ganz '
          'übernehmen kann.',
    v4why='<em>A carbon tax</em> ist der übliche Name (man hört auch '
          '<em>carbon price</em> und <em>carbon levy</em>). Ein '
          '<em>fine</em> bestraft einen Regelverstoß, ein <em>tariff</em> '
          'wird auf Importe erhoben und eine <em>toll</em> auf Straßen oder '
          'Brücken.',
    v5why='<em>Generate electricity</em> (oder <em>produce</em>). '
          '<em>Fabricate</em> und <em>manufacture</em> gelten Gegenständen, '
          'und <em>originate</em> benutzt niemand für Strom.',
    v6why='<em>Intermittent</em>: Es kommt und geht, weil die Quelle so '
          'funktioniert. <em>Interrupted</em> ist eine Unterbrechung durch '
          'ein Ereignis, <em>infrequent</em> heißt selten, und '
          '<em>intermediate</em> ist ein anderes Wort, das nur ähnlich '
          'klingt.',
    v7why='<em>Phase out coal</em>. Die Partikel gehört zum Verb, und nur '
          '<em>out</em> trägt die Bedeutung, etwas schrittweise zu beenden.',
    v8why='Subvention gegen Markt. Der Kandidat räumt ein, dass öffentliches '
          'Geld die Turbinen gebaut hat, und fragt dann, ob die Branche je '
          'ohne auskommt &mdash; eine Idee, beide Seiten, genau die '
          'ausgebaute Antwort, die Teil 3 hervorlocken soll.',
    v9why='<em>Sent to landfill</em> &mdash; im britischen Englisch ohne '
          'Artikel, im amerikanischen <em>a landfill</em>. Die anderen drei '
          'beschreiben dasselbe Loch im Boden mit Wörtern, die das Englische '
          'dafür nicht benutzt.',
    v10why='<em>Single-use plastic</em>. Das Adjektiv ist mit Bindestrich '
           'und fest; die Alternativen bedeuten alle dasselbe, und jede '
           'verrät, dass geraten wurde.',
    v11why='<em>Cut down on</em> &mdash; oder <em>cut back on</em>. Ein '
           'Phrasal Verb reist mit allen seinen Partikeln: <em>cut off</em> '
           'und <em>cut away</em> sind echte Verben mit anderer Bedeutung, '
           'keines nimmt <em>on</em>, und <em>cut back off</em> ist kein '
           'Englisch.',
    v12why='Hersteller vor Einzelnem. Der Käufer soll sich ändern, während '
           'die entscheidende Wahl in der Verpackungsabteilung getroffen '
           'wurde. Das Argument und die Wortverbindung <em>excess packaging</em> '
           'kommen zusammen an.',

    sortEyebrow='Aktivität 4 · Nach Ideen ablegen',
    sortTitle='Lege die sechs Wortverbindungen ab',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Emissionen und Energie',
    sortBin2='Konsum und Abfall',
    sortWhy='Nach Ideen abgelegt, liegt jede Wortverbindung neben dem Argument, dem '
            'sie dient. <em>Burn fossil fuels</em> und <em>phase out '
            'coal</em> sind schon ein halber Absatz über Emissionen und den '
            'Ausstieg aus der Kohle; '
            '<em>a throwaway culture</em> und <em>excess packaging</em> ein '
            'halber Absatz über die Verantwortung der Hersteller. '
            'Alphabetisch abgelegt sind es sechs Wörter, und unter Zeitdruck '
            'hättest du nichts damit zu sagen.',

    actTitle='Antworte aus der Sammlung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Einer ist der Prüfer und stellt drei Fragen aus '
                  'Teil 3 zur Umwelt &mdash; ob Regierungen oder Einzelne '
                  'bei den Emissionen handeln sollten, ob erneuerbare '
                  'Energien die Kohle ersetzen können, ob sich Recycling '
                  'lohnt. Der andere antwortet mit Wortverbindungen aus der '
                  'Sammlung. Nach drei Fragen tauschen.',
    actSpeak1='Jede Antwort trägt mindestens eine Wortverbindung aus der Sammlung, '
              'ganz gesagt &mdash; das Verb mit seinem Substantiv oder das '
              'Adjektiv mit seinem Substantiv.',
    actSpeak2='Der Prüfer fragt nach jeder Antwort <em>why</em>. Die '
              'Nachfrage muss eines der Argumente nutzen, mit denen die Idee '
              'angekommen ist: wer zahlt, Zuverlässigkeit gegen Kosten, '
              'Einzelner gegen Hersteller.',
    actSpeak3='Steht das Wort nicht in der Sammlung, beschreib die Sache in '
              'schlichtem Englisch, statt nach einem seltenen Wort zu '
              'greifen.',
    actWriteKind='Schreiben · 150–200 Wörter',
    actWriteBrief='Schreib einen Hauptteil-Absatz für Task 2 zu einer der '
                  'drei Ideen &mdash; Emissionen, Erneuerbare oder Konsum '
                  'und Abfall. Verwende mindestens fünf Wortverbindungen aus der '
                  'Sammlung und unterstreich jede. Dann sag, welches Argument '
                  'der Absatz macht.',
    actPlaceholder='The most effective way to cut emissions is…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='El primer banco temático: tres ideas, cada una con sus combinaciones '
             'y su argumento ya enganchado',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing Task 2',
    chipCount='18 puntos',

    t1Eyebrow='Idea 1 de 3',
    t1Title='Emisiones: cuatro combinaciones y dos argumentos',
    t1ah='Reducirlas: el sustantivo elige el verbo',
    t1ab='Las emisiones se <em>cut</em>, <em>reduce</em> o <em>curb</em>; un '
         'país <em>burns fossil fuels</em> y libera <em>greenhouse '
         'gases</em>; una ciudad mide su <em>air quality</em>. El verbo lo '
         'elige el sustantivo, y ninguno es raro.',
    t1an='Cuatro combinaciones, aprendidas enteras. Un <em>emissions</em> suelto '
         'en el cuaderno no vale ninguna de ellas.',
    t1bh='La huella y el impuesto',
    t1bb='Una persona o una empresa tiene un <em>carbon footprint</em>, y '
         'reducirlo es para lo que sirve una <em>carbon tax</em>. Las dos '
         'son fijas: la marca que dejas es una <em>footprint</em>, no una '
         'trace, y el cobro es una <em>tax</em>, no una fine.',
    t1bn='Archívalos juntos. El impuesto existe por la huella.',
    t1ch='El argumento con el que llega',
    t1cb='Aquí vuelven una y otra vez dos argumentos. <strong>Quién '
         'paga</strong>: el aire sucio cae sobre gente que no lo produjo. '
         '<strong>Objetivos frente a cumplimiento</strong>: un país puede '
         'prometer reducir a la mitad sus emisiones y no multar jamás a una '
         'sola fábrica.',
    t1cn='Archiva la idea y el párrafo está medio escrito antes de leer la '
         'pregunta.',

    t2Eyebrow='Idea 2 de 3',
    t2Title='Renovables: generate, subsidise, phase out',
    t2ah='Generate: el verbo al que recurrir',
    t2ab='Una <em>wind farm</em> o un tejado de <em>solar panels</em> '
         '<em>generates electricity</em>, y lo que genera alimenta el '
         '<em>national grid</em>. <em>Renewable energy</em> es el término '
         'paraguas; <em>renewables</em> a secas es el sustantivo que usa una '
         'respuesta de la Parte 3.',
    t2an='Cuatro combinaciones y un sustantivo paraguas. Todas sencillas, '
         'ninguna rara.',
    t2bh='La palabra exacta para la debilidad',
    t2bb='El sol se pone y el viento cae, así que el suministro es '
         '<em>intermittent</em>: viene y va a su propio ritmo. Varias '
         'palabras suenan parecido y significan otra cosa, y el examinador '
         'cuenta la que significa lo que querías decir.',
    t2bn='Un fallo que suena avanzado sigue siendo un fallo; la palabra '
         'sencilla que acierta, no.',
    t2ch='El argumento con el que llega',
    t2cb='Los gobiernos <em>subsidise</em> las renovables y <em>phase out '
         'coal</em>, y la mayoría de los ensayos sobre el tema sopesan las '
         'mismas dos tensiones. <strong>Fiabilidad frente a coste</strong>: '
         'barata de generar, cara de almacenar. <strong>Subvención frente a '
         'mercado</strong>: los paneles existen porque alguien pagó, y quizá '
         'alguien tenga que seguir pagando.',
    t2cn='<em>Energy security</em> es el tercer término: a un país que '
         'genera su propia energía no se le puede cortar.',

    t3Eyebrow='Idea 3 de 3',
    t3Title='Consumo y residuos: la preposición forma parte de la combinación',
    t3ah='Sent to landfill, cut down on',
    t3ab='La basura se <em>sends to landfill</em>; un ayuntamiento informa '
         'de sus <em>recycling rates</em>; un comprador <em>cuts down '
         'on</em> <em>excess packaging</em>. La preposición forma parte de '
         'la combinación: en inglés británico <em>landfill</em> va sin '
         'artículo (el americano dice <em>a landfill</em>), y el phrasal '
         'verb tiene dos partículas, no una.',
    t3an='Escríbelo entero. Medio phrasal verb es un fallo.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='Una botella de un solo uso es <em>single-use plastic</em>; una '
         'sociedad que espera tirarlo todo tiene una <em>throwaway '
         'culture</em>; un sistema que te paga por devolver la botella es un '
         '<em>deposit scheme</em>. Dos combinaciones de adjetivo y '
         'sustantivo y un sustantivo compuesto, ninguno raro.',
    t3bn='<em>A throwaway culture</em> dice más que <em>consumerism</em>: '
         'nombra el hábito, no solo el sistema.',
    t3ch='El argumento con el que llega',
    t3cb='Pregunta quién debería cambiar y la respuesta ya está escrita. '
         '<strong>Individuo contra productor</strong>: un comprador puede '
         'cambiar sus <em>consumer habits</em>, pero el envase se decidió '
         'antes de que llegara. <strong>Comodidad contra coste</strong>: lo '
         'de un solo uso es barato ahora y se paga después.',
    t3cn='Los dos argumentos funcionan en ambos sentidos, y por eso vale la '
         'pena archivarlos.',

    mcaEyebrow='Actividad 1 · Emisiones',
    mcaTitle='¿Qué combinación, y qué palabra?',
    mcbEyebrow='Actividad 2 · Renovables',
    mcbTitle='¿Qué combinación, y qué palabra?',
    mccEyebrow='Actividad 3 · Consumo y residuos',
    mccTitle='¿Qué combinación, y qué palabra?',

    v1why='<em>Cut emissions</em> &mdash; o <em>reduce</em>, <em>lower</em> '
          'o <em>curb</em>. <em>Lower down</em> y <em>shrink off</em> añaden '
          'una partícula que el inglés no usa aquí, y <em>descend</em> '
          'significa bajar uno mismo, no bajar algo.',
    v2why='Un <em>carbon footprint</em>. Nadie lo deduce: se aprende entero, '
          'y step, trace o fingerprint anuncian que no fue así.',
    v3why='Quién paga. El coste del aire contaminado cae sobre gente que no '
          'lo produjo &mdash; un argumento con el que esta idea llega a '
          'menudo, y una forma que una respuesta de la Parte 3 puede tomar '
          'entera.',
    v4why='<em>A carbon tax</em> es el nombre habitual (también verás '
          '<em>carbon price</em> y <em>carbon levy</em>). Un <em>fine</em> '
          'castiga incumplir una norma, un <em>tariff</em> grava las '
          'importaciones y un <em>toll</em>, una carretera o un puente.',
    v5why='<em>Generate electricity</em> (o <em>produce</em>). '
          '<em>Fabricate</em> y <em>manufacture</em> son para objetos, y '
          '<em>originate</em> no lo usa nadie para la energía.',
    v6why='<em>Intermittent</em>: va y viene por cómo funciona la fuente. '
          '<em>Interrupted</em> es un corte causado por un suceso, '
          '<em>infrequent</em> significa poco frecuente, e '
          '<em>intermediate</em> es otra palabra que solo suena parecida.',
    v7why='<em>Phase out coal</em>. La partícula forma parte del verbo, y '
          'solo <em>out</em> lleva el sentido de terminar algo por etapas.',
    v8why='Subvención frente a mercado. El candidato admite que el dinero '
          'público construyó las turbinas y luego pregunta si la industria '
          'podrá prescindir de él algún día &mdash; una idea, los dos lados, '
          'el tipo de respuesta desarrollada que la Parte 3 busca provocar.',
    v9why='<em>Sent to landfill</em> &mdash; sin artículo en inglés '
          'británico, aunque el americano dice <em>a landfill</em>. Las '
          'otras tres describen el mismo agujero en el suelo con palabras '
          'que el inglés no usa para eso.',
    v10why='<em>Single-use plastic</em>. El adjetivo lleva guion y es fijo; '
           'las alternativas significan lo mismo, y cada una delata que se '
           'está adivinando.',
    v11why='<em>Cut down on</em> &mdash; o <em>cut back on</em>. Un phrasal '
           'verb viaja con todas sus partículas: <em>cut off</em> y <em>cut '
           'away</em> son verbos reales con otro significado, ninguno lleva '
           '<em>on</em>, y <em>cut back off</em> no es inglés.',
    v12why='Productor por encima del individuo. Al comprador se le pide que '
           'cambie mientras la decisión que importa se tomó en el '
           'departamento de envases. El argumento y la combinación <em>excess '
           'packaging</em> llegan juntos.',

    sortEyebrow='Actividad 4 · Archivar por ideas',
    sortTitle='Archiva las seis combinaciones',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Emisiones y energía',
    sortBin2='Consumo y residuos',
    sortWhy='Archivada por ideas, cada combinación queda junto al argumento al que '
            'sirve. <em>Burn fossil fuels</em> y <em>phase out coal</em> ya '
            'son medio párrafo sobre las emisiones y el abandono del carbón; '
            '<em>a throwaway culture</em> '
            'y <em>excess packaging</em>, medio párrafo sobre la '
            'responsabilidad del productor. Archivadas por orden alfabético '
            'son seis palabras, y con el reloj en marcha no tendrías nada '
            'que decir con ellas.',

    actTitle='Responde desde el banco',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Uno hace de examinador y plantea tres '
                  'preguntas de la Parte 3 sobre el medio ambiente &mdash; '
                  'si deben actuar los gobiernos o las personas sobre las '
                  'emisiones, si las renovables pueden sustituir al carbón, '
                  'si merece la pena reciclar. El otro responde con '
                  'combinaciones del banco. Cambiad tras tres preguntas.',
    actSpeak1='Cada respuesta lleva al menos una combinación del banco, dicha '
              'entera: el verbo con su sustantivo o el adjetivo con su '
              'sustantivo.',
    actSpeak2='El examinador pregunta <em>why</em> después de cada '
              'respuesta. La réplica tiene que usar uno de los argumentos con '
              'los que llegó la idea: quién paga, fiabilidad contra coste, '
              'individuo contra productor.',
    actSpeak3='Si la palabra no está en el banco, describe la cosa en inglés '
              'llano en vez de ir a por una palabra rara.',
    actWriteKind='Escritura · 150–200 palabras',
    actWriteBrief='Escribe un párrafo de desarrollo de Task 2 sobre una de '
                  'las tres ideas: emisiones, renovables, o consumo y '
                  'residuos. Usa al menos cinco combinaciones del banco y subraya '
                  'cada una. Luego di qué argumento defiende el párrafo.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── French ─────────────────────────────────────────────────────────────
T['fr'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='La première réserve thématique : trois idées, chacune avec ses '
             'associations et son argument déjà attaché',
    chipLevel='C1 · Avancé', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Idée 1 sur 3',
    t1Title='Les émissions : quatre associations et deux arguments',
    t1ah='Les réduire &mdash; le nom choisit le verbe',
    t1ab='Les émissions sont <em>cut</em>, <em>reduced</em> ou '
         '<em>curbed</em> ; un pays <em>burns fossil fuels</em> et rejette '
         'des <em>greenhouse gases</em> ; une ville mesure son <em>air '
         'quality</em>. Le verbe est choisi par le nom, et aucun n’est rare.',
    t1an='Quatre associations, apprises en bloc. Un <em>emissions</em> tout seul '
         'dans le carnet ne vaut aucune d’elles.',
    t1bh='L’empreinte et la taxe',
    t1bb='Une personne ou une entreprise a une <em>carbon footprint</em>, et la '
         'réduire, c’est le rôle d’une <em>carbon tax</em>. Les deux sont figées : '
         'la marque qu’on laisse est une <em>footprint</em>, pas une trace, et le '
         'prélèvement est une <em>tax</em>, pas une amende.',
    t1bn='Rangez-les ensemble. La taxe existe à cause de l’empreinte.',
    t1ch='L’argument qui vient avec',
    t1cb='Deux arguments reviennent sans cesse ici. <strong>Qui '
         'paie</strong> : l’air pollué retombe sur des gens qui ne l’ont pas '
         'produit. <strong>Objectifs contre application</strong> : un pays '
         'peut promettre de diviser ses émissions par deux sans jamais '
         'sanctionner une seule usine.',
    t1cn='Rangez l’idée, et le paragraphe est à moitié écrit avant même de lire '
         'la question.',

    t2Eyebrow='Idée 2 sur 3',
    t2Title='Les renouvelables : <em>generate</em>, <em>subsidise</em>, '
            '<em>phase out</em>',
    t2ah='Generate : le verbe à privilégier',
    t2ab='Un <em>wind farm</em> ou un toit de <em>solar panels</em> '
         '<em>generates electricity</em>, et ce qu’il produit alimente le '
         '<em>national grid</em>. <em>Renewable energy</em> est le terme '
         'générique ; <em>renewables</em> tout seul est le nom qu’emploie une '
         'réponse de Part 3.',
    t2an='Quatre associations et un nom générique. Toutes simples, aucune '
         'rare.',
    t2bh='Le mot précis pour la faiblesse',
    t2bb='Le soleil se couche et le vent tombe : l’approvisionnement est donc '
         '<em>intermittent</em>, il va et vient à son propre rythme. Plusieurs '
         'mots se ressemblent et veulent dire autre chose, et l’examinateur '
         'compte celui qui dit ce que vous vouliez dire.',
    t2bn='Un raté qui sonne savant reste un raté ; le mot simple qui tombe '
         'juste, non.',
    t2ch='L’argument qui vient avec',
    t2cb='Les gouvernements <em>subsidise</em> les renouvelables et '
         '<em>phase out coal</em>, et la plupart des essais sur le sujet '
         'pèsent les deux mêmes tensions. <strong>Fiabilité contre '
         'coût</strong> : bon marché à produire, cher à stocker. '
         '<strong>Subvention contre marché</strong> : les panneaux existent '
         'parce que quelqu’un a payé, et il faudra peut-être continuer à '
         'payer.',
    t2cn='<em>Energy security</em> est le troisième terme : un pays qui produit '
         'sa propre énergie ne peut pas être coupé.',

    t3Eyebrow='Idée 3 sur 3',
    t3Title='Consommation et déchets : l’association inclut la préposition',
    t3ah='<em>Sent to landfill</em>, <em>cut down on</em>',
    t3ab='Les déchets sont <em>sent to landfill</em> ; une municipalité '
         'publie ses <em>recycling rates</em> ; un client <em>cuts down '
         'on</em> <em>excess packaging</em>. La préposition fait partie de '
         'l’association : en anglais britannique, <em>landfill</em> se passe '
         'd’article (l’anglais américain dit <em>a landfill</em>), et le '
         'phrasal verb a deux particules, pas une.',
    t3an='Écrivez le tout. La moitié d’un verbe à particules, c’est raté.',
    t3bh='<em>Single-use</em>, <em>throwaway</em>, <em>deposit</em>',
    t3bb='Une bouteille utilisée une fois, c’est du <em>single-use '
         'plastic</em> ; une société qui s’attend à tout jeter a une '
         '<em>throwaway culture</em> ; un dispositif qui vous paie pour '
         'rapporter la bouteille est un <em>deposit scheme</em>. Deux '
         'associations adjectif-nom et un nom composé, aucun rare.',
    t3bn='<em>A throwaway culture</em> en dit plus que <em>consumerism</em> '
         ': l’expression nomme l’habitude, pas seulement le système.',
    t3ch='L’argument qui vient avec',
    t3cb='Demandez qui doit changer, et la réponse est écrite. <strong>La '
         'responsabilité individuelle contre celle du producteur</strong> : un '
         'client peut changer ses <em>consumer habits</em>, mais l’emballage a '
         'été décidé avant son arrivée. <strong>La commodité contre le '
         'coût</strong> : le jetable est bon marché aujourd’hui et se paie plus '
         'tard.',
    t3cn='Les deux arguments fonctionnent dans les deux sens, et c’est ce qui '
         'les rend dignes d’être rangés.',

    mcaEyebrow='Activité 1 · Les émissions',
    mcaTitle='Quelle association, et quel mot ?',
    mcbEyebrow='Activité 2 · Les renouvelables',
    mcbTitle='Quelle association, et quel mot ?',
    mccEyebrow='Activité 3 · Consommation et déchets',
    mccTitle='Quelle association, et quel mot ?',

    v1why='<em>Cut emissions</em> &mdash; ou <em>reduce</em>, <em>lower</em> '
          'ou <em>curb</em>. <em>Lower down</em> et <em>shrink off</em> '
          'ajoutent une particule que l’anglais n’emploie pas ici, et '
          '<em>descend</em> veut dire descendre, pas faire baisser quelque '
          'chose.',
    v2why='Une <em>carbon footprint</em>. Personne ne la déduit &mdash; on '
          'l’apprend en bloc, et <em>step</em>, <em>trace</em> ou '
          '<em>fingerprint</em> annoncent chacun qu’on ne l’a pas apprise.',
    v3why='Qui paie. Le coût de l’air pollué retombe sur des gens qui ne '
          'l’ont pas produit &mdash; un argument qui accompagne souvent '
          'cette idée, et une forme qu’une réponse de Partie 3 peut '
          'reprendre telle quelle.',
    v4why='<em>A carbon tax</em> est le nom habituel (on rencontre aussi '
          '<em>carbon price</em> et <em>carbon levy</em>). Un <em>fine</em> '
          'sanctionne une infraction, un <em>tariff</em> frappe les '
          'importations et un <em>toll</em>, une route ou un pont.',
    v5why='<em>Generate electricity</em> (ou <em>produce</em>). '
          '<em>Fabricate</em> et <em>manufacture</em> s’appliquent à des '
          'objets, et <em>originate</em> n’est pas un verbe qu’on emploie '
          'pour l’énergie.',
    v6why='<em>Intermittent</em> : elle va et vient à cause du '
          'fonctionnement de la source. <em>Interrupted</em> désigne une '
          'coupure due à un événement, <em>infrequent</em> veut dire rare, '
          'et <em>intermediate</em> est un autre mot qui se contente de '
          'sonner pareil.',
    v7why='<em>Phase out coal</em>. La particule fait partie du verbe, et seul '
          '<em>out</em> porte l’idée de mettre fin à quelque chose par étapes.',
    v8why='Subvention contre marché. Le candidat admet que l’argent public a '
          'construit les éoliennes, puis demande si la filière pourra un '
          'jour s’en passer &mdash; une idée, les deux côtés, le genre de '
          'réponse développée que la Partie 3 cherche à obtenir.',
    v9why='<em>Sent to landfill</em> &mdash; sans article en anglais '
          'britannique, même si l’anglais américain dit <em>a landfill</em>. '
          'Les trois autres décrivent le même trou dans le sol avec des mots '
          'que l’anglais n’emploie pas pour cela.',
    v10why='<em>Single-use plastic</em>. L’adjectif prend un trait d’union et '
           'il est figé ; les autres veulent dire la même chose, et chacune '
           'trahit un rédacteur qui devine.',
    v11why='<em>Cut down on</em> &mdash; ou <em>cut back on</em>. Un phrasal '
           'verb voyage avec toutes ses particules : <em>cut off</em> et '
           '<em>cut away</em> sont de vrais verbes au sens différent, aucun '
           'ne prend <em>on</em>, et <em>cut back off</em> n’est pas de '
           'l’anglais.',
    v12why='La responsabilité du producteur avant celle de l’individu. On dit au '
           'client de changer alors que la décision qui compte a été prise au '
           'service emballage. L’argument et l’association <em>excess '
           'packaging</em> arrivent ensemble.',

    sortEyebrow='Activité 4 · Ranger par idée',
    sortTitle='Rangez les six associations',
    sortHint='Faites glisser chacune dans une colonne &mdash; ou cliquez sur '
             'un élément, puis sur la colonne voulue.',
    sortBin1='Émissions et énergie',
    sortBin2='Consommation et déchets',
    sortWhy='Rangée par idée, chaque association se trouve à côté de l’argument '
            'qu’elle sert. <em>Burn fossil fuels</em> et <em>phase out coal</em> '
            'sont déjà la moitié d’un paragraphe sur les émissions et l’abandon '
            'du charbon ; <em>a throwaway culture</em> et <em>excess '
            'packaging</em> sont la moitié d’un paragraphe sur la responsabilité '
            'du producteur. Rangées par ordre alphabétique, ce sont six mots, et '
            'sous la pression du temps vous n’auriez rien à dire avec eux.',

    actTitle='Répondez avec la réserve',
    actUse='Utilisez-en au moins trois :',
    actSpeakBrief='À deux. L’un joue l’examinateur et pose trois questions '
                  'de Partie 3 sur l’environnement &mdash; les gouvernements '
                  'ou les individus doivent-ils agir sur les émissions, les '
                  'renouvelables peuvent-elles remplacer le charbon, le '
                  'recyclage en vaut-il la peine. L’autre répond avec les '
                  'associations de la banque. Échangez après trois questions.',
    actSpeak1='Chaque réponse contient au moins une association de la réserve, '
              'dite en entier &mdash; le verbe avec son nom, ou l’adjectif avec '
              'son nom.',
    actSpeak2='L’examinateur demande <em>why</em> après chaque réponse. La '
              'relance doit utiliser l’un des arguments qui venaient avec '
              'l’idée : qui paie, la fiabilité contre le coût, l’individu contre '
              'le producteur.',
    actSpeak3='Si le mot n’est pas dans la réserve, décrivez la chose en anglais '
              'simple plutôt que d’aller chercher un mot rare.',
    actWriteKind='Écriture · 150–200 mots',
    actWriteBrief='Écrivez un paragraphe de développement de Task 2 sur l’une '
                  'des trois idées &mdash; émissions, renouvelables, ou '
                  'consommation et déchets. Utilisez au moins cinq associations '
                  'de la réserve et soulignez chacune. Puis dites quel argument '
                  'le paragraphe défend.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Italian ────────────────────────────────────────────────────────────
T['it'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='La prima banca tematica: tre idee, ognuna con le sue combinazioni '
             'e il suo argomento già attaccato',
    chipLevel='C1 · Avanzato', chipFocus='Speaking e Writing Task 2',
    chipCount='18 punti',

    t1Eyebrow='Idea 1 di 3',
    t1Title='Le emissioni: quattro combinazioni e due argomenti',
    t1ah='Ridurle: è il nome a scegliere il verbo',
    t1ab='Le emissioni si <em>cut</em>, <em>reduce</em> o <em>curb</em>; un '
         'paese <em>burns fossil fuels</em> e rilascia <em>greenhouse '
         'gases</em>; una città misura la sua <em>air quality</em>. Il verbo '
         'lo sceglie il nome, e nessuno è raro.',
    t1an='Quattro combinazioni, imparate intere. Un <em>emissions</em> da solo sul '
         'quaderno non ne vale nessuna.',
    t1bh='L’impronta e la tassa',
    t1bb='Una persona o un’azienda ha una <em>carbon footprint</em>, e ridurla è '
         'lo scopo di una <em>carbon tax</em>. Entrambe sono fisse: il segno che '
         'lasci è una <em>footprint</em>, non una traccia, e il prelievo è una '
         '<em>tax</em>, non una multa.',
    t1bn='Archiviale insieme. La tassa esiste a causa dell’impronta.',
    t1ch='L’argomento che arriva con lei',
    t1cb='Qui due argomenti tornano di continuo. <strong>Chi paga</strong>: '
         'l’aria inquinata ricade su persone che non l’hanno prodotta. '
         '<strong>Obiettivi contro applicazione</strong>: un paese può '
         'promettere di dimezzare le emissioni e non multare mai una sola '
         'fabbrica.',
    t1cn='Archivia l’idea, e il paragrafo è scritto a metà prima ancora di '
         'leggere la domanda.',

    t2Eyebrow='Idea 2 di 3',
    t2Title='Le rinnovabili: <em>generate</em>, <em>subsidise</em>, '
            '<em>phase out</em>',
    t2ah='Generate: il verbo a cui ricorrere',
    t2ab='Un <em>wind farm</em> o un tetto di <em>solar panels</em> '
         '<em>generates electricity</em>, e ciò che produce alimenta il '
         '<em>national grid</em>. <em>Renewable energy</em> è il termine '
         'ombrello; <em>renewables</em> da solo è il nome che usa una risposta '
         'di Part 3.',
    t2an='Quattro combinazioni e un nome ombrello. Tutte semplici, nessuna '
         'rara.',
    t2bh='La parola precisa per il punto debole',
    t2bb='Il sole tramonta e il vento cala, quindi la fornitura è '
         '<em>intermittent</em>: va e viene con i suoi tempi. Diverse parole '
         'suonano simili e vogliono dire altro, e l’esaminatore conta quella che '
         'dice ciò che intendevi.',
    t2bn='Un errore che suona avanzato resta un errore; la parola semplice '
         'che va a segno no.',
    t2ch='L’argomento che arriva con lei',
    t2cb='I governi <em>subsidise</em> le rinnovabili e <em>phase out '
         'coal</em>, e la maggior parte dei saggi sul tema soppesa le stesse '
         'due tensioni. <strong>Affidabilità contro costo</strong>: '
         'economica da produrre, cara da immagazzinare. <strong>Sussidio '
         'contro mercato</strong>: i pannelli esistono perché qualcuno ha '
         'pagato, e forse qualcuno dovrà continuare a pagare.',
    t2cn='<em>Energy security</em> è il terzo termine: un paese che produce la '
         'propria energia non può essere tagliato fuori.',

    t3Eyebrow='Idea 3 di 3',
    t3Title='Consumi e rifiuti: la combinazione comprende la preposizione',
    t3ah='<em>Sent to landfill</em>, <em>cut down on</em>',
    t3ab='I rifiuti vengono <em>sent to landfill</em>; un comune comunica i '
         'suoi <em>recycling rates</em>; un acquirente <em>cuts down on</em> '
         '<em>excess packaging</em>. La preposizione fa parte della '
         'combinazione: nell’inglese britannico <em>landfill</em> non vuole '
         'l’articolo (l’americano dice <em>a landfill</em>), e il phrasal '
         'verb ha due particelle, non una.',
    t3an='Scrivi tutto. Mezzo phrasal verb è un errore.',
    t3bh='<em>Single-use</em>, <em>throwaway</em>, <em>deposit</em>',
    t3bb='Una bottiglia usata una volta è <em>single-use plastic</em>; una '
         'società che si aspetta di buttare tutto ha una <em>throwaway '
         'culture</em>; un sistema che ti paga per riportare la bottiglia è '
         'un <em>deposit scheme</em>. Due combinazioni aggettivo-nome e un '
         'nome composto, nessuno raro.',
    t3bn='<em>A throwaway culture</em> dice più di <em>consumerism</em>: '
         'nomina l’abitudine, non solo il sistema.',
    t3ch='L’argomento che arriva con lei',
    t3cb='Chiediti chi deve cambiare e la risposta è scritta. <strong>'
         'Responsabilità individuale contro responsabilità del '
         'produttore</strong>: un cliente può cambiare le sue <em>consumer '
         'habits</em>, ma l’imballaggio è stato deciso prima che arrivasse. '
         '<strong>Comodità contro costo</strong>: l’usa e getta costa poco oggi '
         'e si paga dopo.',
    t3cn='Entrambi gli argomenti funzionano nei due sensi, ed è questo che li '
         'rende degni di essere archiviati.',

    mcaEyebrow='Attività 1 · Le emissioni',
    mcaTitle='Quale combinazione, e quale parola?',
    mcbEyebrow='Attività 2 · Le rinnovabili',
    mcbTitle='Quale combinazione, e quale parola?',
    mccEyebrow='Attività 3 · Consumi e rifiuti',
    mccTitle='Quale combinazione, e quale parola?',

    v1why='<em>Cut emissions</em> &mdash; oppure <em>reduce</em>, '
          '<em>lower</em> o <em>curb</em>. <em>Lower down</em> e <em>shrink '
          'off</em> aggiungono una particella che l’inglese qui non usa, e '
          '<em>descend</em> vuol dire scendere, non abbassare qualcosa.',
    v2why='Una <em>carbon footprint</em>. Nessuno la ricava &mdash; si impara '
          'intera, e <em>step</em>, <em>trace</em> o <em>fingerprint</em> '
          'dichiarano ciascuno che non la si è imparata.',
    v3why='Chi paga. Il costo dell’aria inquinata ricade su persone che non '
          'l’hanno prodotta &mdash; un argomento con cui questa idea arriva '
          'spesso, e una forma che una risposta della Parte 3 può prendere '
          'intera.',
    v4why='<em>A carbon tax</em> è il nome abituale (si trovano anche '
          '<em>carbon price</em> e <em>carbon levy</em>). Un <em>fine</em> '
          'punisce una violazione, un <em>tariff</em> colpisce le '
          'importazioni e un <em>toll</em> una strada o un ponte.',
    v5why='<em>Generate electricity</em> (oppure <em>produce</em>). '
          '<em>Fabricate</em> e <em>manufacture</em> si usano per gli '
          'oggetti, e <em>originate</em> nessuno lo usa per l’energia.',
    v6why='<em>Intermittent</em>: va e viene per come funziona la fonte. '
          '<em>Interrupted</em> è un’interruzione causata da un evento, '
          '<em>infrequent</em> vuol dire raro, e <em>intermediate</em> è '
          'un’altra parola che suona solo simile.',
    v7why='<em>Phase out coal</em>. La particella fa parte del verbo, e solo '
          '<em>out</em> porta il senso di porre fine a qualcosa per gradi.',
    v8why='Sussidio contro mercato. Il candidato ammette che il denaro '
          'pubblico ha costruito le turbine, poi chiede se il settore potrà '
          'mai farne a meno &mdash; un’idea, entrambi i lati, il tipo di '
          'risposta sviluppata che la Parte 3 vuole far emergere.',
    v9why='<em>Sent to landfill</em> &mdash; senza articolo nell’inglese '
          'britannico, anche se l’americano dice <em>a landfill</em>. Le '
          'altre tre descrivono lo stesso buco nel terreno con parole che '
          'l’inglese non usa per questo.',
    v10why='<em>Single-use plastic</em>. L’aggettivo ha il trattino ed è fisso; '
           'le alternative vogliono dire la stessa cosa, e ognuna segnala chi '
           'scrive tirando a indovinare.',
    v11why='<em>Cut down on</em> &mdash; oppure <em>cut back on</em>. Un '
           'phrasal verb viaggia con tutte le sue particelle: <em>cut '
           'off</em> e <em>cut away</em> sono verbi veri con un altro '
           'significato, nessuno dei due vuole <em>on</em>, e <em>cut back '
           'off</em> non è inglese.',
    v12why='La responsabilità del produttore prima di quella dell’individuo. Al '
           'cliente si dice di cambiare mentre la decisione che conta è stata '
           'presa nel reparto imballaggi. L’argomento e la combinazione '
           '<em>excess packaging</em> arrivano insieme.',

    sortEyebrow='Attività 4 · Archiviare per idee',
    sortTitle='Archivia le sei combinazioni',
    sortHint='Trascina ciascuna in una colonna &mdash; oppure clicca su un '
             'elemento e poi sulla colonna che vuoi.',
    sortBin1='Emissioni ed energia',
    sortBin2='Consumi e rifiuti',
    sortWhy='Archiviata per idea, ogni combinazione sta accanto all’argomento '
            'che serve. <em>Burn fossil fuels</em> e <em>phase out coal</em> sono '
            'già mezzo paragrafo sulle emissioni e sull’abbandono del carbone; '
            '<em>a throwaway culture</em> ed <em>excess packaging</em> sono mezzo '
            'paragrafo sulla responsabilità del produttore. In ordine alfabetico '
            'sono sei parole, e sotto pressione non avresti niente da dire con '
            'esse.',

    actTitle='Rispondi con la banca',
    actUse='Usane almeno tre:',
    actSpeakBrief='In coppia. Uno fa l’esaminatore e pone tre domande della '
                  'Parte 3 sull’ambiente &mdash; se debbano agire sulle '
                  'emissioni i governi o i singoli, se le rinnovabili '
                  'possano sostituire il carbone, se valga la pena '
                  'riciclare. L’altro risponde con le combinazioni della '
                  'raccolta. Dopo tre domande, scambiatevi.',
    actSpeak1='Ogni risposta contiene almeno una combinazione della banca, detta '
              'per intero &mdash; il verbo con il suo nome, o l’aggettivo con il '
              'suo nome.',
    actSpeak2='L’esaminatore chiede <em>why</em> dopo ogni risposta. Il seguito '
              'deve usare uno degli argomenti che arrivavano con l’idea: chi '
              'paga, affidabilità contro costo, individuo contro produttore.',
    actSpeak3='Se la parola non è nella banca, descrivi la cosa in inglese '
              'semplice invece di cercare una parola rara.',
    actWriteKind='Scrittura · 150–200 parole',
    actWriteBrief='Scrivi un paragrafo centrale di Task 2 su una delle tre idee '
                  '&mdash; emissioni, rinnovabili, o consumi e rifiuti. Usa '
                  'almeno cinque combinazioni della banca e sottolineale tutte. '
                  'Poi di’ quale argomento sostiene il paragrafo.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Portuguese ─────────────────────────────────────────────────────────
T['pt'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='O primeiro banco temático: três ideias, cada uma com as suas '
             'combinações e o seu argumento já agarrado',
    chipLevel='C1 · Avançado', chipFocus='Speaking e Writing Task 2',
    chipCount='18 pontos',

    t1Eyebrow='Ideia 1 de 3',
    t1Title='As emissões: quatro combinações e dois argumentos',
    t1ah='Reduzi-las: é o nome que escolhe o verbo',
    t1ab='As emissões são <em>cut</em>, <em>reduced</em> ou <em>curbed</em>; '
         'um país <em>burns fossil fuels</em> e liberta <em>greenhouse '
         'gases</em>; uma cidade mede a sua <em>air quality</em>. O verbo é '
         'escolhido pelo nome, e nenhum é raro.',
    t1an='Quatro combinações, aprendidas inteiras. Um <em>emissions</em> sozinho '
         'no caderno não vale nenhuma delas.',
    t1bh='A pegada e o imposto',
    t1bb='Uma pessoa ou uma empresa tem uma <em>carbon footprint</em>, e '
         'reduzi-la é para isso que serve uma <em>carbon tax</em>. As duas são '
         'fixas: a marca que deixas é uma <em>footprint</em>, não um rasto, e a '
         'cobrança é uma <em>tax</em>, não uma multa.',
    t1bn='Arquiva-as juntas. O imposto existe por causa da pegada.',
    t1ch='O argumento que vem com ela',
    t1cb='Dois argumentos voltam uma e outra vez aqui. <strong>Quem '
         'paga</strong>: o ar poluído cai sobre pessoas que não o '
         'produziram. <strong>Metas contra fiscalização</strong>: um país '
         'pode prometer reduzir as emissões para metade e nunca multar uma '
         'única fábrica.',
    t1cn='Arquiva a ideia, e o parágrafo fica meio escrito antes de leres a '
         'pergunta.',

    t2Eyebrow='Ideia 2 de 3',
    t2Title='As renováveis: <em>generate</em>, <em>subsidise</em>, '
            '<em>phase out</em>',
    t2ah='Generate: o verbo a que recorrer',
    t2ab='Um <em>wind farm</em> ou um telhado de <em>solar panels</em> '
         '<em>generates electricity</em>, e o que produz alimenta o <em>national '
         'grid</em>. <em>Renewable energy</em> é o termo geral; '
         '<em>renewables</em> sozinho é o nome que uma resposta de Part 3 usa.',
    t2an='Quatro combinações e um nome abrangente. Todas simples, nenhuma '
         'rara.',
    t2bh='A palavra exata para o ponto fraco',
    t2bb='O sol põe-se e o vento abranda, por isso o abastecimento é '
         '<em>intermittent</em>: vai e vem ao seu próprio ritmo. Várias palavras '
         'soam parecidas e querem dizer outra coisa, e o examinador conta a que '
         'diz o que tu querias dizer.',
    t2bn='Um erro que soa avançado continua a ser um erro; a palavra simples '
         'que acerta, não.',
    t2ch='O argumento que vem com ela',
    t2cb='Os governos <em>subsidise</em> as renováveis e <em>phase out '
         'coal</em>, e a maioria dos ensaios sobre o tema pesa as mesmas '
         'duas tensões. <strong>Fiabilidade contra custo</strong>: barata de '
         'gerar, cara de armazenar. <strong>Subsídio contra '
         'mercado</strong>: os painéis existem porque alguém pagou, e talvez '
         'alguém tenha de continuar a pagar.',
    t2cn='<em>Energy security</em> é o terceiro termo: um país que produz a sua '
         'própria energia não pode ficar sem ela por decisão de outro.',

    t3Eyebrow='Ideia 3 de 3',
    t3Title='Consumo e resíduos: a combinação inclui a preposição',
    t3ah='<em>Sent to landfill</em>, <em>cut down on</em>',
    t3ab='O lixo é <em>sent to landfill</em>; uma câmara municipal divulga '
         'as suas <em>recycling rates</em>; um consumidor <em>cuts down '
         'on</em> <em>excess packaging</em>. A preposição faz parte da '
         'combinação: no inglês britânico, <em>landfill</em> não leva artigo '
         '(o americano diz <em>a landfill</em>), e o phrasal verb tem duas '
         'partículas, não uma.',
    t3an='Escreve tudo. Meio phrasal verb é um erro.',
    t3bh='<em>Single-use</em>, <em>throwaway</em>, <em>deposit</em>',
    t3bb='Uma garrafa usada uma vez é <em>single-use plastic</em>; uma '
         'sociedade que conta deitar tudo fora tem uma <em>throwaway '
         'culture</em>; um sistema que te paga por devolveres a garrafa é um '
         '<em>deposit scheme</em>. Duas combinações de adjetivo e nome e um '
         'nome composto, nenhum raro.',
    t3bn='<em>A throwaway culture</em> diz mais do que <em>consumerism</em>: '
         'nomeia o hábito, não só o sistema.',
    t3ch='O argumento que vem com ela',
    t3cb='Pergunta quem deve mudar e a resposta está escrita. <strong>'
         'Responsabilidade individual contra a do produtor</strong>: um '
         'consumidor pode mudar os seus <em>consumer habits</em>, mas a '
         'embalagem foi decidida antes de ele chegar. <strong>Conveniência '
         'contra custo</strong>: o descartável é barato agora e paga-se '
         'depois.',
    t3cn='Os dois argumentos funcionam nos dois sentidos, e é isso que os torna '
         'dignos de ser arquivados.',

    mcaEyebrow='Atividade 1 · As emissões',
    mcaTitle='Que combinação, e que palavra?',
    mcbEyebrow='Atividade 2 · As renováveis',
    mcbTitle='Que combinação, e que palavra?',
    mccEyebrow='Atividade 3 · Consumo e resíduos',
    mccTitle='Que combinação, e que palavra?',

    v1why='<em>Cut emissions</em> &mdash; ou <em>reduce</em>, <em>lower</em> '
          'ou <em>curb</em>. <em>Lower down</em> e <em>shrink off</em> '
          'acrescentam uma partícula que o inglês aqui não usa, e '
          '<em>descend</em> quer dizer descer, não fazer baixar alguma coisa.',
    v2why='Uma <em>carbon footprint</em>. Ninguém a deduz &mdash; aprende-se '
          'inteira, e <em>step</em>, <em>trace</em> ou <em>fingerprint</em> '
          'anunciam, cada um, que não foi aprendida.',
    v3why='Quem paga. O custo do ar poluído cai sobre pessoas que não o '
          'produziram &mdash; um argumento com que esta ideia chega muitas '
          'vezes, e uma forma que uma resposta da Parte 3 pode aproveitar '
          'inteira.',
    v4why='<em>A carbon tax</em> é o nome habitual (também vais encontrar '
          '<em>carbon price</em> e <em>carbon levy</em>). Uma <em>fine</em> '
          'castiga uma infração, uma <em>tariff</em> incide sobre '
          'importações e uma <em>toll</em>, sobre uma estrada ou uma ponte.',
    v5why='<em>Generate electricity</em> (ou <em>produce</em>). '
          '<em>Fabricate</em> e <em>manufacture</em> são para objetos, e '
          '<em>originate</em> não é um verbo que alguém use para energia.',
    v6why='<em>Intermittent</em>: vem e vai por causa do modo como a fonte '
          'funciona. <em>Interrupted</em> é um corte causado por um '
          'acontecimento, <em>infrequent</em> quer dizer raro, e '
          '<em>intermediate</em> é outra palavra que só soa parecida.',
    v7why='<em>Phase out coal</em>. A partícula faz parte do verbo, e só '
          '<em>out</em> traz o sentido de acabar com algo por etapas.',
    v8why='Subsídio contra mercado. O candidato admite que o dinheiro '
          'público construiu as turbinas e depois pergunta se a indústria '
          'alguma vez vai passar sem ele &mdash; uma ideia, os dois lados, o '
          'tipo de resposta desenvolvida que a Parte 3 procura provocar.',
    v9why='<em>Sent to landfill</em> &mdash; sem artigo no inglês britânico, '
          'embora o americano diga <em>a landfill</em>. As outras três '
          'descrevem o mesmo buraco no chão com palavras que o inglês não '
          'usa para isso.',
    v10why='<em>Single-use plastic</em>. O adjetivo leva hífen e é fixo; as '
           'alternativas querem dizer o mesmo, e cada uma denuncia quem está a '
           'adivinhar.',
    v11why='<em>Cut down on</em> &mdash; ou <em>cut back on</em>. Um phrasal '
           'verb viaja com todas as suas partículas: <em>cut off</em> e '
           '<em>cut away</em> são verbos verdadeiros com outro sentido, '
           'nenhum leva <em>on</em>, e <em>cut back off</em> não é inglês.',
    v12why='A responsabilidade do produtor antes da individual. Diz-se ao '
           'consumidor que mude, quando a decisão que conta foi tomada no '
           'departamento de embalagens. O argumento e a combinação <em>excess '
           'packaging</em> chegam juntos.',

    sortEyebrow='Atividade 4 · Arquivar por ideias',
    sortTitle='Arquiva as seis combinações',
    sortHint='Arrasta cada uma para uma coluna &mdash; ou clica num elemento e '
             'depois na coluna que quiseres.',
    sortBin1='Emissões e energia',
    sortBin2='Consumo e resíduos',
    sortWhy='Arquivada por ideia, cada combinação fica ao lado do argumento que '
            'serve. <em>Burn fossil fuels</em> e <em>phase out coal</em> já são '
            'meio parágrafo sobre as emissões e o abandono do carvão; <em>a '
            'throwaway culture</em> e <em>excess packaging</em> são meio parágrafo '
            'sobre a responsabilidade do produtor. Por ordem alfabética são seis '
            'palavras, e com o tempo a apertar não terias nada a dizer com elas.',

    actTitle='Responde com o banco',
    actUse='Usa pelo menos três:',
    actSpeakBrief='Em pares. Um faz de examinador e faz três perguntas da '
                  'Parte 3 sobre o ambiente &mdash; se devem ser os governos '
                  'ou as pessoas a agir sobre as emissões, se as renováveis '
                  'podem substituir o carvão, se vale a pena reciclar. O '
                  'outro responde com combinações do banco. Troquem depois '
                  'de três perguntas.',
    actSpeak1='Cada resposta tem pelo menos uma combinação do banco, dita '
              'inteira &mdash; o verbo com o seu nome, ou o adjetivo com o seu '
              'nome.',
    actSpeak2='O examinador pergunta <em>why</em> depois de cada resposta. A '
              'continuação tem de usar um dos argumentos que vinham com a ideia: '
              'quem paga, fiabilidade contra custo, indivíduo contra produtor.',
    actSpeak3='Se a palavra não está no banco, descreve a coisa em inglês simples '
              'em vez de ires buscar uma palavra rara.',
    actWriteKind='Escrita · 150–200 palavras',
    actWriteBrief='Escreve um parágrafo de desenvolvimento de Task 2 sobre uma das '
                  'três ideias &mdash; emissões, renováveis, ou consumo e '
                  'resíduos. Usa pelo menos cinco combinações do banco e '
                  'sublinha cada uma. Depois diz que argumento o parágrafo '
                  'defende.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Russian ────────────────────────────────────────────────────────────
T['ru'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='Первый тематический запас: три идеи, у каждой свои сочетания и '
             'готовый аргумент',
    chipLevel='C1 · Продвинутый', chipFocus='Speaking и Writing Task 2',
    chipCount='18 баллов',

    t1Eyebrow='Идея 1 из 3',
    t1Title='Выбросы: четыре сочетания и два аргумента',
    t1ah='Сокращать: глагол выбирает существительное',
    t1ab='Выбросы <em>cut</em>, <em>reduce</em> или <em>curb</em>; страна '
         '<em>burns fossil fuels</em> и выпускает <em>greenhouse gases</em>; '
         'город измеряет свой <em>air quality</em>. Глагол выбирает '
         'существительное, и ни одно из этих слов не редкое.',
    t1an='Четыре сочетания, выученные целиком. Голое <em>emissions</em> в '
         'тетради не стоит ни одного из них.',
    t1bh='След и налог',
    t1bb='У человека или компании есть <em>carbon footprint</em>, и уменьшать '
         'его &mdash; задача <em>carbon tax</em>. Оба сочетания устойчивы: '
         'оставленная отметка &mdash; это <em>footprint</em>, а не trace, а '
         'сбор &mdash; это <em>tax</em>, а не штраф.',
    t1bn='Храните их вместе. Налог существует из-за следа.',
    t1ch='Аргумент, который идёт в комплекте',
    t1cb='Здесь снова и снова возникают два аргумента. <strong>Кто '
         'платит</strong>: грязный воздух достаётся людям, которые его не '
         'создавали. <strong>Цели против их соблюдения</strong>: страна '
         'может пообещать вдвое сократить выбросы и ни разу не оштрафовать '
         'ни одну фабрику.',
    t1cn='Сохраните идею &mdash; и абзац наполовину написан ещё до того, как вы '
         'прочитали вопрос.',

    t2Eyebrow='Идея 2 из 3',
    t2Title='Возобновляемая энергия: <em>generate</em>, <em>subsidise</em>, '
            '<em>phase out</em>',
    t2ah='Generate: глагол, к которому стоит тянуться',
    t2ab='<em>Wind farm</em> или крыша с <em>solar panels</em> <em>generates '
         'electricity</em>, и то, что вырабатывается, поступает в <em>national '
         'grid</em>. <em>Renewable energy</em> &mdash; общий термин; '
         '<em>renewables</em> отдельно &mdash; существительное, которое '
         'использует ответ Part 3.',
    t2an='Четыре сочетания и одно обобщающее существительное. Все простые, '
         'ни одного редкого.',
    t2bh='Точное слово для слабого места',
    t2bb='Солнце садится, ветер стихает, поэтому снабжение '
         '<em>intermittent</em>: оно то есть, то нет, по собственному графику. '
         'Несколько слов звучат похоже и значат другое, а экзаменатор '
         'засчитывает то, которое значит именно то, что вы хотели сказать.',
    t2bn='Промах, который звучит продвинуто, остаётся промахом; простое '
         'слово, попавшее в цель, &mdash; нет.',
    t2ch='Аргумент, который идёт в комплекте',
    t2cb='Правительства <em>subsidise</em> возобновляемую энергетику и '
         '<em>phase out coal</em>, и большинство эссе на эту тему взвешивают '
         'те же два противоречия. <strong>Надёжность против '
         'стоимости</strong>: дёшево производить, дорого хранить. '
         '<strong>Субсидии против рынка</strong>: панели существуют, потому '
         'что кто-то заплатил, и, возможно, платить придётся и дальше.',
    t2cn='<em>Energy security</em> &mdash; третий термин: страну, которая сама '
         'вырабатывает энергию, нельзя от неё отрезать.',

    t3Eyebrow='Идея 3 из 3',
    t3Title='Потребление и отходы: предлог входит в сочетание',
    t3ah='<em>Sent to landfill</em>, <em>cut down on</em>',
    t3ab='Мусор <em>is sent to landfill</em>; муниципалитет сообщает свои '
         '<em>recycling rates</em>; покупатель <em>cuts down on</em> '
         '<em>excess packaging</em>. Предлог входит в сочетание: в '
         'британском английском <em>landfill</em> идёт без артикля (в '
         'американском &mdash; <em>a landfill</em>), а у фразового глагола '
         'две частицы, а не одна.',
    t3an='Пишите целиком. Половина фразового глагола &mdash; это ошибка.',
    t3bh='<em>Single-use</em>, <em>throwaway</em>, <em>deposit</em>',
    t3bb='Бутылка на один раз &mdash; это <em>single-use plastic</em>; '
         'общество, которое привыкло всё выбрасывать, &mdash; это '
         '<em>throwaway culture</em>; система, которая платит вам за возврат '
         'бутылки, &mdash; это <em>deposit scheme</em>. Два сочетания '
         'прилагательного с существительным и одно составное '
         'существительное, ни одного редкого.',
    t3bn='<em>A throwaway culture</em> говорит больше, чем '
         '<em>consumerism</em>: оно называет привычку, а не только систему.',
    t3ch='Аргумент, который идёт в комплекте',
    t3cb='Спросите, кто должен меняться, &mdash; и ответ готов. <strong>Личная '
         'ответственность против ответственности производителя</strong>: '
         'покупатель может изменить свои <em>consumer habits</em>, но упаковку '
         'выбрали до того, как он пришёл. <strong>Удобство против '
         'стоимости</strong>: одноразовое дёшево сейчас, а платить придётся '
         'потом.',
    t3cn='Оба аргумента работают в обе стороны &mdash; поэтому их и стоит '
         'хранить.',

    mcaEyebrow='Задание 1 · Выбросы',
    mcaTitle='Какое сочетание и какое слово?',
    mcbEyebrow='Задание 2 · Возобновляемая энергия',
    mcbTitle='Какое сочетание и какое слово?',
    mccEyebrow='Задание 3 · Потребление и отходы',
    mccTitle='Какое сочетание и какое слово?',

    v1why='<em>Cut emissions</em> &mdash; или <em>reduce</em>, '
          '<em>lower</em>, <em>curb</em>. <em>Lower down</em> и <em>shrink '
          'off</em> добавляют частицу, которой английский здесь не '
          'использует, а <em>descend</em> значит спускаться самому, а не '
          'снижать что-то.',
    v2why='<em>Carbon footprint</em>. Его никто не выводит &mdash; его учат '
          'целиком, и <em>step</em>, <em>trace</em> или <em>fingerprint</em> '
          'сразу показывают, что не выучили.',
    v3why='Кто платит. Цена грязного воздуха достаётся людям, которые его не '
          'создавали, &mdash; аргумент, с которым эта идея часто приходит, и '
          'форма, которую ответ в части 3 может взять целиком.',
    v4why='<em>A carbon tax</em> &mdash; обычное название (встречаются также '
          '<em>carbon price</em> и <em>carbon levy</em>). <em>Fine</em> '
          '&mdash; наказание за нарушение правил, <em>tariff</em> взимается '
          'с импорта, а <em>toll</em> &mdash; за проезд по дороге или мосту.',
    v5why='<em>Generate electricity</em> (или <em>produce</em>). '
          '<em>Fabricate</em> и <em>manufacture</em> &mdash; для предметов, '
          'а <em>originate</em> об энергии никто не говорит.',
    v6why='<em>Intermittent</em>: оно то есть, то нет из-за того, как '
          'работает источник. <em>Interrupted</em> &mdash; перерыв, '
          'вызванный событием, <em>infrequent</em> значит редкий, а '
          '<em>intermediate</em> &mdash; другое слово, которое лишь похоже '
          'по звучанию.',
    v7why='<em>Phase out coal</em>. Частица &mdash; часть глагола, и только '
          '<em>out</em> несёт смысл поэтапного прекращения.',
    v8why='Субсидии против рынка. Кандидат признаёт, что турбины построены '
          'на государственные деньги, а затем спрашивает, сможет ли отрасль '
          'когда-нибудь обойтись без них, &mdash; одна идея, обе стороны, '
          'тот развёрнутый ответ, которого добивается часть 3.',
    v9why='<em>Sent to landfill</em> &mdash; без артикля в британском '
          'английском, хотя в американском говорят <em>a landfill</em>. '
          'Остальные три описывают ту же яму в земле словами, которыми '
          'английский её не называет.',
    v10why='<em>Single-use plastic</em>. Прилагательное пишется через дефис и '
           'закреплено; варианты значат то же самое, и каждый выдаёт автора, '
           'который угадывает.',
    v11why='<em>Cut down on</em> &mdash; или <em>cut back on</em>. Фразовый '
           'глагол идёт со всеми своими частицами: <em>cut off</em> и '
           '<em>cut away</em> &mdash; настоящие глаголы с другим значением, '
           'ни один не берёт <em>on</em>, а <em>cut back off</em> &mdash; не '
           'английский.',
    v12why='Ответственность производителя важнее личной. Покупателю говорят '
           'измениться, а решение, которое имеет значение, приняли в отделе '
           'упаковки. Аргумент и сочетание <em>excess packaging</em> приходят '
           'вместе.',

    sortEyebrow='Задание 4 · Храним по идеям',
    sortTitle='Разложите шесть сочетаний',
    sortHint='Перетащите каждое в столбец &mdash; или нажмите на него, а затем '
             'на нужный столбец.',
    sortBin1='Выбросы и энергия',
    sortBin2='Потребление и отходы',
    sortWhy='Если хранить по идеям, каждое сочетание лежит рядом с аргументом, '
            'которому служит. <em>Burn fossil fuels</em> и <em>phase out '
            'coal</em> &mdash; это уже пол-абзаца о выбросах и отказе от угля; '
            '<em>a throwaway culture</em> и <em>excess packaging</em> &mdash; '
            'пол-абзаца об ответственности производителя. По алфавиту это шесть '
            'слов, и под давлением времени вам нечего было бы с ними сказать.',

    actTitle='Отвечайте из запаса',
    actUse='Используйте хотя бы три:',
    actSpeakBrief='В парах. Один &mdash; экзаменатор и задаёт три вопроса '
                  'части 3 об окружающей среде &mdash; должны ли действовать '
                  'в отношении выбросов правительства или отдельные люди, '
                  'может ли возобновляемая энергетика заменить уголь, стоит '
                  'ли заниматься переработкой. Другой отвечает, используя '
                  'сочетания из банка. После трёх вопросов поменяйтесь.',
    actSpeak1='Каждый ответ содержит хотя бы одно сочетание из запаса, сказанное '
              'целиком, &mdash; глагол со своим существительным или '
              'прилагательное со своим существительным.',
    actSpeak2='После каждого ответа экзаменатор спрашивает <em>why</em>. В '
              'продолжении нужно использовать один из аргументов, пришедших с '
              'идеей: кто платит, надёжность против стоимости, личность против '
              'производителя.',
    actSpeak3='Если слова нет в запасе, опишите предмет простым английским, а не '
              'тянитесь за редким словом.',
    actWriteKind='Письмо · 150–200 слов',
    actWriteBrief='Напишите один абзац основной части Task 2 по одной из трёх '
                  'идей &mdash; выбросы, возобновляемая энергия или потребление '
                  'и отходы. Используйте не меньше пяти сочетаний из запаса и '
                  'подчеркните каждое. Затем скажите, какой аргумент отстаивает '
                  'абзац.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Arabic ─────────────────────────────────────────────────────────────
T['ar'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='الرصيد الموضوعي الأول: ثلاث أفكار، لكل منها تلازماتها وحجّتها '
             'الجاهزة',
    chipLevel='C1 · متقدّم', chipFocus='Speaking وWriting Task 2',
    chipCount='18 نقطة',

    t1Eyebrow='الفكرة 1 من 3',
    t1Title='الانبعاثات: أربعة تلازمات وحجّتان',
    t1ah='خفّضها &mdash; الاسم يختار الفعل',
    t1ab='الانبعاثات تُوصف بـ<em>cut</em> أو <em>reduced</em> أو '
         '<em>curbed</em>؛ والبلد <em>burns fossil fuels</em> ويطلق '
         '<em>greenhouse gases</em>؛ والمدينة تقيس <em>air quality</em>. '
         'الاسم هو الذي يختار الفعل، ولا شيء من ذلك نادر.',
    t1an='أربعة تلازمات تُتعلَّم كاملة. أما كلمة <em>emissions</em> وحدها في '
         'الدفتر فلا تساوي أيًّا منها.',
    t1bh='البصمة والضريبة',
    t1bb='للشخص أو الشركة <em>carbon footprint</em>، وتقليصها هو غرض <em>carbon '
         'tax</em>. كلاهما ثابت: الأثر الذي تتركه <em>footprint</em> لا trace، '
         'والرسم المفروض <em>tax</em> لا غرامة.',
    t1bn='احفظهما معًا. فالضريبة موجودة بسبب البصمة.',
    t1ch='الحجّة التي تأتي معها',
    t1cb='حجتان تتكرران هنا مرة بعد مرة. <strong>من يدفع</strong>: الهواء '
         'الملوّث يقع على أناس لم ينتجوه. <strong>الأهداف مقابل '
         'التطبيق</strong>: يمكن لبلد أن يعد بخفض انبعاثاته إلى النصف ثم لا '
         'يغرّم مصنعًا واحدًا.',
    t1cn='احفظ الفكرة، فتكون الفقرة نصف مكتوبة قبل أن تقرأ السؤال.',

    t2Eyebrow='الفكرة 2 من 3',
    t2Title='الطاقة المتجدّدة: <em>generate</em> و<em>subsidise</em> و<em>phase '
            'out</em>',
    t2ah='الفعل <em>generate</em>: الفعل الذي تلجأ إليه',
    t2ab='الـ<em>wind farm</em> أو سطح عليه <em>solar panels</em> '
         '<em>generates electricity</em>، وما يولّده يغذّي <em>national '
         'grid</em>. وعبارة <em>renewable energy</em> هي المصطلح الجامع، أما '
         '<em>renewables</em> وحدها فهي الاسم الذي تستخدمه إجابة Part 3.',
    t2an='أربعة تلازمات واسم جامع واحد. كلها بسيطة، ولا شيء منها نادر.',
    t2bh='الكلمة الدقيقة لنقطة الضعف',
    t2bb='تغرب الشمس وتسكن الريح، فيكون الإمداد <em>intermittent</em>: يأتي '
         'ويذهب وفق جدوله الخاص. كلمات عدة تبدو قريبة وتعني شيئًا آخر، والممتحن '
         'يحتسب الكلمة التي تعني ما قصدته.',
    t2bn='الإخفاق الذي يبدو متقدمًا يظل إخفاقًا، أما الكلمة البسيطة التي '
         'تصيب فلا.',
    t2ch='الحجّة التي تأتي معها',
    t2cb='الحكومات <em>subsidise</em> الطاقة المتجددة و<em>phase out '
         'coal</em>، ومعظم المقالات عن الموضوع توازن بين التوترين نفسيهما. '
         '<strong>الموثوقية مقابل الكلفة</strong>: رخيصة في التوليد، مكلفة '
         'في التخزين. <strong>الدعم مقابل السوق</strong>: الألواح موجودة لأن '
         'أحدًا دفع، وقد يلزم أن يواصل أحد الدفع.',
    t2cn='المصطلح الثالث <em>energy security</em>: الدولة التي تولّد طاقتها '
         'بنفسها لا يمكن قطعها عنها.',

    t3Eyebrow='الفكرة 3 من 3',
    t3Title='الاستهلاك والنفايات: حرف الجر جزء من التلازم',
    t3ah='<em>Sent to landfill</em> و<em>cut down on</em>',
    t3ab='القمامة <em>sent to landfill</em>؛ والبلدية تعلن <em>recycling '
         'rates</em>؛ والمتسوق <em>cuts down on</em> <em>excess '
         'packaging</em>. حرف الجر جزء من التلازم: في الإنجليزية البريطانية '
         'تأتي <em>landfill</em> بلا أداة (والأمريكية تقول <em>a '
         'landfill</em>)، وللفعل المركّب أداتان لا واحدة.',
    t3an='اكتب التعبير كله. فنصف الفعل المركّب خطأ.',
    t3bh='<em>Single-use</em> و<em>throwaway</em> و<em>deposit</em>',
    t3bb='الزجاجة التي تُستخدم مرة واحدة هي <em>single-use plastic</em>؛ '
         'والمجتمع الذي يتوقع أن يرمي الأشياء لديه <em>throwaway '
         'culture</em>؛ والنظام الذي يدفع لك مقابل إعادة الزجاجة هو '
         '<em>deposit scheme</em>. تلازمان من صفة واسم، واسم مركّب، ولا شيء '
         'منها نادر.',
    t3bn='عبارة <em>a throwaway culture</em> تقول أكثر مما تقوله '
         '<em>consumerism</em>: فهي تسمّي العادة لا النظام وحده.',
    t3ch='الحجّة التي تأتي معها',
    t3cb='اسأل من يجب أن يتغيّر فتكون الإجابة مكتوبة. <strong>مسؤولية الفرد '
         'مقابل مسؤولية المنتِج</strong>: يستطيع المتسوّق أن يغيّر <em>consumer '
         'habits</em>، لكن التغليف تقرّر قبل وصوله. <strong>الراحة مقابل '
         'التكلفة</strong>: ما يُستعمل مرة واحدة رخيص الآن ويُدفع ثمنه لاحقًا.',
    t3cn='كلتا الحجّتين تصلح في الاتجاهين، وهذا ما يجعلهما جديرتين بالحفظ.',

    mcaEyebrow='النشاط 1 · الانبعاثات',
    mcaTitle='أيّ تلازم، وأيّ كلمة؟',
    mcbEyebrow='النشاط 2 · الطاقة المتجدّدة',
    mcbTitle='أيّ تلازم، وأيّ كلمة؟',
    mccEyebrow='النشاط 3 · الاستهلاك والنفايات',
    mccTitle='أيّ تلازم، وأيّ كلمة؟',

    v1why='الصحيح <em>cut emissions</em> &mdash; أو <em>reduce</em> أو '
          '<em>lower</em> أو <em>curb</em>. أما <em>lower down</em> '
          'و<em>shrink off</em> فتضيفان أداة لا تستخدمها الإنجليزية هنا، '
          'و<em>descend</em> تعني أن تنزل أنت، لا أن تُنزل شيئًا.',
    v2why='الصحيح <em>carbon footprint</em>. لا أحد يستنتجها، بل تُتعلَّم كاملة، '
          'و<em>step</em> و<em>trace</em> و<em>fingerprint</em> تعلن كلٌّ منها '
          'أنها لم تُتعلَّم.',
    v3why='من يدفع. كلفة الهواء الملوّث تقع على أناس لم ينتجوه &mdash; حجة '
          'كثيرًا ما تأتي معها هذه الفكرة، وشكل يمكن لإجابة في الجزء 3 أن '
          'تستعيره كاملًا.',
    v4why='عبارة <em>a carbon tax</em> هي الاسم المعتاد (وستجد أيضًا '
          '<em>carbon price</em> و<em>carbon levy</em>). فالـ<em>fine</em> '
          'عقوبة على مخالفة قاعدة، والـ<em>tariff</em> رسم على الواردات، '
          'والـ<em>toll</em> رسم على طريق أو جسر.',
    v5why='الصحيح <em>generate electricity</em> (أو <em>produce</em>). أما '
          '<em>fabricate</em> و<em>manufacture</em> فللأشياء المصنوعة، '
          'و<em>originate</em> لا يستخدمها أحد للطاقة.',
    v6why='الصحيح <em>intermittent</em>: يأتي ويذهب بسبب طريقة عمل المصدر. '
          'أما <em>interrupted</em> فانقطاع يسببه حدث، و<em>infrequent</em> '
          'تعني نادرًا، و<em>intermediate</em> كلمة أخرى يقترب صوتها فقط.',
    v7why='الصحيح <em>phase out coal</em>. الأداة جزء من الفعل، ووحدها '
          '<em>out</em> تحمل معنى إنهاء الشيء على مراحل.',
    v8why='الدعم مقابل السوق. يقرّ المرشح بأن المال العام هو الذي بنى '
          'التوربينات، ثم يسأل هل ستستغني الصناعة عنه يومًا &mdash; فكرة '
          'واحدة بجانبيها، وهو نوع الإجابة المطوّرة التي صُمّم الجزء 3 '
          'لاستخراجها.',
    v9why='الصحيح <em>sent to landfill</em> &mdash; بلا أداة في الإنجليزية '
          'البريطانية، وإن كانت الأمريكية تقول <em>a landfill</em>. أما '
          'الثلاثة الأخرى فتصف الحفرة نفسها في الأرض بكلمات لا تستخدمها '
          'الإنجليزية لها.',
    v10why='الصحيح <em>single-use plastic</em>. الصفة موصولة بشرطة وثابتة، '
           'والبدائل تعني الشيء نفسه، وكلٌّ منها يفضح كاتبًا يخمّن.',
    v11why='الصحيح <em>cut down on</em> &mdash; أو <em>cut back on</em>. '
           'الفعل المركّب ينتقل بكل أدواته: <em>cut off</em> و<em>cut '
           'away</em> فعلان حقيقيان بمعنى آخر، ولا يأخذ أيّ منهما '
           '<em>on</em>، و<em>cut back off</em> ليست إنجليزية.',
    v12why='مسؤولية المنتِج قبل مسؤولية الفرد. يُطلب من المتسوّق أن يتغيّر بينما '
           'اتُّخذ القرار المهم في قسم التغليف. والحجّة والتلازم <em>excess '
           'packaging</em> يأتيان معًا.',

    sortEyebrow='النشاط 4 · الحفظ بحسب الفكرة',
    sortTitle='احفظ التلازمات الستة في مكانها',
    sortHint='اسحب كل تلازم إلى عمود، أو انقر عليه ثم على العمود الذي تريده.',
    sortBin1='الانبعاثات والطاقة',
    sortBin2='الاستهلاك والنفايات',
    sortWhy='حين تحفظ بحسب الفكرة، يقع كل تلازم بجانب الحجّة التي يخدمها. فعبارتا '
            '<em>burn fossil fuels</em> و<em>phase out coal</em> نصف فقرة جاهزة '
            'عن الانبعاثات والتخلّي عن الفحم، و<em>a throwaway culture</em> '
            'و<em>excess packaging</em> نصف فقرة عن مسؤولية المنتِج. أما بالترتيب '
            'الأبجدي فهي ست كلمات، ولن يكون لديك تحت ضغط الوقت ما تقوله بها.',

    actTitle='أجب من الرصيد',
    actUse='استخدم ثلاثة منها على الأقل:',
    actSpeakBrief='اعملا في ثنائي. يؤدي أحدكما دور الممتحن ويطرح ثلاثة أسئلة '
                  'من الجزء 3 عن البيئة &mdash; هل ينبغي أن تتحرك الحكومات '
                  'أم الأفراد بشأن الانبعاثات، وهل تستطيع الطاقة المتجددة أن '
                  'تحل محل الفحم، وهل يستحق التدوير العناء. ويجيب الآخر '
                  'مستخدمًا تلازمات من البنك. تبادلا الأدوار بعد ثلاثة أسئلة.',
    actSpeak1='كل إجابة تحمل تلازمًا واحدًا على الأقل من الرصيد، يُقال كاملًا: '
              'الفعل مع اسمه، أو الصفة مع اسمها.',
    actSpeak2='يسأل الممتحن <em>why</em> بعد كل إجابة. ويجب أن تستخدم المتابعة '
              'إحدى الحجج التي جاءت مع الفكرة: من يدفع، أو الموثوقية مقابل '
              'التكلفة، أو الفرد مقابل المنتِج.',
    actSpeak3='إذا لم تكن الكلمة في الرصيد، فصِف الشيء بإنجليزية بسيطة بدل أن '
              'تمدّ يدك إلى كلمة نادرة.',
    actWriteKind='الكتابة · 150–200 كلمة',
    actWriteBrief='اكتب فقرة من صلب مقال Task 2 عن إحدى الأفكار الثلاث: '
                  'الانبعاثات، أو الطاقة المتجدّدة، أو الاستهلاك والنفايات. '
                  'استخدم خمسة تلازمات على الأقل من الرصيد وضع خطًّا تحت كل '
                  'منها. ثم قل أيّ حجّة تقدّمها الفقرة.',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Chinese ────────────────────────────────────────────────────────────
T['zh'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='第一个话题词库：三个观点，每个都配好了搭配，也带好了论点',
    chipLevel='C1 · 高级', chipFocus='Speaking 与 Writing Task 2',
    chipCount='18 分',

    t1Eyebrow='观点 1 / 3',
    t1Title='排放：四个搭配，两个论点',
    t1ah='减少排放——名词决定动词',
    t1ab='排放可以 <em>cut</em>、<em>reduce</em> 或 <em>curb</em>；一个国家 <em>burns '
         'fossil fuels</em>，释放 <em>greenhouse gases</em>；一座城市测量它的 <em>air '
         'quality</em>。动词由名词决定，这些都不是生僻词。',
    t1an='四个搭配，整体记住。笔记本上光秃秃的一个 <em>emissions</em>，一个搭配'
         '都抵不上。',
    t1bh='足迹与税',
    t1bb='一个人或一家公司有 <em>carbon footprint</em>，而缩小它正是 <em>carbon '
         'tax</em> 的用途。两者都是固定说法：留下的痕迹是 <em>footprint</em>，不是 '
         'trace；收的钱是 <em>tax</em>，不是罚款。',
    t1bn='把它们放在一起记。有了足迹，才有这笔税。',
    t1ch='它自带的论点',
    t1cb='这里有两个论点反复出现。<strong>谁来付代价</strong>：脏空气落在并非制造它的人身上。<strong>目标与执行</st'
         'rong>：一个国家可以承诺把排放减半，却从不罚一家工厂。',
    t1cn='把观点存好，还没读题，段落就已经写了一半。',

    t2Eyebrow='观点 2 / 3',
    t2Title='可再生能源：<em>generate</em>、<em>subsidise</em>、<em>phase '
            'out</em>',
    t2ah='Generate：首选的动词',
    t2ab='<em>Wind farm</em> 或铺满 <em>solar panels</em> 的屋顶 <em>generates '
         'electricity</em>，发出的电并入 <em>national grid</em>。<em>Renewable '
         'energy</em> 是总称；单独的 <em>renewables</em> 则是 Part 3 回答里用的'
         '名词。',
    t2an='四个搭配加一个统称名词。都很朴素，没有一个生僻。',
    t2bh='说弱点的那个准确的词',
    t2bb='太阳下山、风停下来，所以供应是 <em>intermittent</em> 的：按自己的节奏'
         '时有时无。有几个词听起来很像，意思却不同，而考官只认那个准确表达你意'
         '思的词。',
    t2bn='听起来高级的失误仍然是失误；用对了的朴素词则不是。',
    t2ch='它自带的论点',
    t2cb='政府 <em>subsidise</em> 可再生能源并 <em>phase out '
         'coal</em>，这个话题的大多数文章都在权衡同样两组矛盾。<strong>可靠与成本</strong>：发电便宜，储存昂贵。<st'
         'rong>补贴与市场</strong>：这些面板之所以存在，是因为有人付了钱，而且可能还得有人继续付。',
    t2cn='第三个词是 <em>energy security</em>：自己发电的国家，别人断不了它的电。',

    t3Eyebrow='观点 3 / 3',
    t3Title='消费与垃圾：搭配里包括介词',
    t3ah='<em>Sent to landfill</em>、<em>cut down on</em>',
    t3ab='垃圾 <em>is sent to landfill</em>；市政当局公布 <em>recycling '
         'rates</em>；购物者 <em>cuts down on</em> <em>excess '
         'packaging</em>。介词是搭配的一部分：在英式英语里 <em>landfill</em> 不加冠词（美式英语说 <em>a '
         'landfill</em>），而这个短语动词有两个小品词，不是一个。',
    t3an='整个写下来。短语动词只写一半就是错。',
    t3bh='<em>Single-use</em>、<em>throwaway</em>、<em>deposit</em>',
    t3bb='用一次就扔的瓶子是 <em>single-use plastic</em>；习惯把东西一扔了之的社会有一种 '
         '<em>throwaway culture</em>；付钱让你把瓶子退回来的办法是 <em>deposit '
         'scheme</em>。两个形容词加名词的搭配，一个复合名词，都不生僻。',
    t3bn='<em>A throwaway culture</em> 比 <em>consumerism</em> '
         '说得更多：它点出的是习惯，而不只是制度。',
    t3ch='它自带的论点',
    t3cb='问一句“谁该改变”，答案就写好了。<strong>个人责任与生产者责任'
         '</strong>：顾客可以改变自己的 <em>consumer habits</em>，但包装在顾客到'
         '来之前就定下了。<strong>方便与成本</strong>：一次性的东西现在便宜，代'
         '价以后再付。',
    t3cn='两个论点正反都说得通，所以才值得存起来。',

    mcaEyebrow='练习 1 · 排放',
    mcaTitle='哪个搭配，哪个词？',
    mcbEyebrow='练习 2 · 可再生能源',
    mcbTitle='哪个搭配，哪个词？',
    mccEyebrow='练习 3 · 消费与垃圾',
    mccTitle='哪个搭配，哪个词？',

    v1why='<em>Cut emissions</em>——或者 <em>reduce</em>、<em>lower</em>、<em>curb'
          '</em>。<em>Lower down</em> 和 <em>shrink off</em> 加了英语在这里不用的小品词，而 '
          '<em>descend</em> 是自己往下走，不是让某物降下来。',
    v2why='<em>Carbon footprint</em>。没人能推导出来——只能整体记住，而 '
          '<em>step</em>、<em>trace</em> 或 <em>fingerprint</em> 每一个都暴露出'
          '没记住。',
    v3why='谁来付代价。空气污染的代价落在并非制造它的人身上——这个观点常常伴随这一话题出现，也是第三部分的回答可以整个借用的结构。',
    v4why='<em>A carbon tax</em> 是通常的叫法（你也会见到 <em>carbon price</em> 和 '
          '<em>carbon levy</em>）。<em>Fine</em> 是对违规的罚款，<em>tariff</em> '
          '针对进口征收，<em>toll</em> 则是道路或桥梁的通行费。',
    v5why='<em>Generate electricity</em>（或 <em>produce</em>）。<em>Fabricate</e'
          'm> 和 <em>manufacture</em> 用于物品，而 <em>originate</em> 没有人用来说电力。',
    v6why='<em>Intermittent</em>：由于能源本身的工作方式而时有时无。<em>Interrupted</em> '
          '是某个事件造成的中断，<em>infrequent</em> 是不常见，<em>intermediate</em> '
          '则是另一个只是发音相近的词。',
    v7why='<em>Phase out coal</em>。小品词是动词的一部分，只有 <em>out</em> 带有'
          '“分阶段终止”的意思。',
    v8why='补贴与市场。考生承认是公共资金建起了风机，然后问这个产业能否有一天不再依赖它——一个观点，两个方面，正是第三部分想引出的那种充分展开'
          '的回答。',
    v9why='<em>Sent to landfill</em>——英式英语不加冠词，不过美式英语说 <em>a '
          'landfill</em>。另外三个用英语不会用的词，描述地上的同一个坑。',
    v10why='<em>Single-use plastic</em>。这个形容词带连字符，是固定的；其他选项'
           '意思相同，但每一个都暴露出写的人在猜。',
    v11why='<em>Cut down on</em>——或者 <em>cut back '
           'on</em>。短语动词连同所有小品词一起使用：<em>cut off</em> 和 <em>cut away</em> '
           '是真实存在、意思不同的动词，都不接 <em>on</em>，而 <em>cut back off</em> 不是英语。',
    v12why='生产者责任先于个人责任。人们让顾客去改变，可真正要紧的决定是在包装'
           '部门做的。这个论点和 <em>excess packaging</em> 这个搭配是一起来的。',

    sortEyebrow='练习 4 · 按观点归档',
    sortTitle='把六个搭配归档',
    sortHint='把每一项拖到一栏里——或者先点一项，再点你想放进的那一栏。',
    sortBin1='排放与能源',
    sortBin2='消费与垃圾',
    sortWhy='按观点归档，每个搭配就挨着它所服务的论点。<em>Burn fossil '
            'fuels</em> 和 <em>phase out coal</em> 已经是关于排放和弃用煤炭的半'
            '段话；<em>a throwaway culture</em> 和 <em>excess packaging</em> 是'
            '关于生产者责任的半段话。按字母排，它们只是六个词，时间紧迫时你拿'
            '它们什么也说不出来。',

    actTitle='从词库里作答',
    actUse='至少用上三个：',
    actSpeakBrief='两人一组。一人当考官，就环境问题问三个第三部分的问题——在排放问题上应该由政府还是个人采取行动，可再生能源能否取代煤'
                  '炭，回收是否值得。另一人用词库里的搭配来回答。三个问题后交换。',
    actSpeak1='每个回答至少带一个词库里的搭配，而且要完整说出——动词加它的名词，'
              '或形容词加它的名词。',
    actSpeak2='每个回答之后，考官都问一句 <em>why</em>。接下来的回答必须用上这个'
              '观点自带的某个论点：谁来买单、可靠性与成本、个人与生产者。',
    actSpeak3='如果词库里没有那个词，就用简单的英语把东西描述出来，而不是去够'
              '一个生僻词。',
    actWriteKind='写作 · 150–200 词',
    actWriteBrief='就三个观点之一——排放、可再生能源，或消费与垃圾——写一段 '
                  'Task 2 的主体段。至少用上词库里的五个搭配，并给每一个画线。'
                  '然后说明这一段在论证哪个论点。',
    actPlaceholder='The most effective way to cut emissions is…',
)


# ── Japanese ───────────────────────────────────────────────────────────
T['ja'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='最初のトピック語彙集：三つのアイデアに、それぞれの組み合わせと議論が'
             'はじめからついています',
    chipLevel='C1 · 上級', chipFocus='Speaking・Writing Task 2',
    chipCount='18 点',

    t1Eyebrow='アイデア 1 / 3',
    t1Title='排出：四つの組み合わせと二つの議論',
    t1ah='減らす――動詞を選ぶのは名詞',
    t1ab='排出は <em>cut</em>、<em>reduce</em>、<em>curb</em> されます。国は <em>burns '
         'fossil fuels</em> し、<em>greenhouse gases</em> を出し、都市は <em>air '
         'quality</em> を測ります。動詞は名詞が選び、どれも珍しい語ではありません。',
    t1an='四つの組み合わせを丸ごと覚えましょう。ノートにただ <em>emissions</em> '
         'とだけ書いても、そのどれにも及びません。',
    t1bh='フットプリントと税',
    t1bb='個人や企業には <em>carbon footprint</em> があり、それを小さくするのが '
         '<em>carbon tax</em> の役目です。どちらも決まった言い方で、残る跡は '
         'trace ではなく <em>footprint</em>、課されるお金は罰金ではなく '
         '<em>tax</em> です。',
    t1bn='一緒にしまっておきましょう。税があるのは、フットプリントがあるから'
         'です。',
    t1ch='ついてくる議論',
    t1cb='ここでは二つの論点が何度も出てきます。<strong>誰が払うか</strong>：汚れた空気は、それを出していない人々に降りかかる。'
         '<strong>目標対実施</strong>：国は排出を半減すると約束しながら、工場を一つも罰しないことができる。',
    t1cn='アイデアをしまっておけば、問いを読む前に段落は半分書けています。',

    t2Eyebrow='アイデア 2 / 3',
    t2Title='再生可能エネルギー：<em>generate</em>、<em>subsidise</em>、'
            '<em>phase out</em>',
    t2ah='Generate：まず使うべき動詞',
    t2ab='<em>Wind farm</em> や <em>solar panels</em> を載せた屋根は <em>generates '
         'electricity</em> し、生まれた電気は <em>national grid</em> に送られま'
         'す。<em>Renewable energy</em> は総称で、単独の <em>renewables</em> が '
         'Part 3 の答えで使う名詞です。',
    t2an='四つの組み合わせと一つの総称名詞。どれも平易で、珍しいものはありません。',
    t2bh='弱点を表す正確な語',
    t2bb='日は沈み、風はやむので、供給は <em>intermittent</em> です。自分の都合で'
         '来たり来なかったりします。似た響きで意味の違う語がいくつもあり、試験官'
         'が数えるのは、あなたの言いたいことを正しく表した語です。',
    t2bn='高度に聞こえる外れは、やはり外れです。的中した平易な語は違います。',
    t2ch='ついてくる議論',
    t2cb='政府は再生可能エネルギーを <em>subsidise</em> し、<em>phase out coal</em> '
         'します。このテーマのエッセイの多くは、同じ二つの緊張関係を比べています。<strong>信頼性対コスト</strong>：作るのは安く'
         '、ためるのは高い。<strong>補助金対市場</strong>：パネルがあるのは誰かが払ったからで、これからも誰かが払い続けなければ'
         'ならないかもしれない。',
    t2cn='三つ目の語は <em>energy security</em>：自国で電気をつくる国は、外から'
         '止められません。',

    t3Eyebrow='アイデア 3 / 3',
    t3Title='消費と廃棄物：組み合わせには前置詞も含まれる',
    t3ah='<em>Sent to landfill</em>、<em>cut down on</em>',
    t3ab='ごみは <em>sent to landfill</em>、自治体は <em>recycling rates</em> '
         'を公表し、買い物客は <em>excess packaging</em> を <em>cuts down on</em> '
         'します。前置詞は組み合わせの一部です：イギリス英語では <em>landfill</em> に冠詞を付けず（アメリカ英語では '
         '<em>a landfill</em>）、この句動詞の小辞は一つではなく二つです。',
    t3an='全体を書きましょう。句動詞の半分だけでは誤りです。',
    t3bh='<em>Single-use</em>、<em>throwaway</em>、<em>deposit</em>',
    t3bb='一度使って捨てるボトルは <em>single-use plastic</em>、物を捨てるのが当たり前の社会には '
         '<em>throwaway culture</em> があり、ボトルを返すとお金がもらえる仕組みは <em>deposit '
         'scheme</em> です。形容詞と名詞の組み合わせが二つと複合名詞が一つ、どれも珍しくはありません。',
    t3bn='<em>A throwaway culture</em> は <em>consumerism</em> '
         'より多くを語ります：制度だけでなく、習慣を名指しているからです。',
    t3ch='ついてくる議論',
    t3cb='誰が変わるべきかと問えば、答えはもう書けています。<strong>個人の責任対'
         '生産者の責任</strong>：買い物客は自分の <em>consumer habits</em> を変え'
         'られますが、包装は客が来る前に決まっていました。<strong>便利さ対コスト'
         '</strong>：使い捨ては今は安く、代償はあとで払います。',
    t3cn='どちらの議論も逆向きにも使えます。だからこそ、しまっておく価値があり'
         'ます。',

    mcaEyebrow='演習 1 · 排出',
    mcaTitle='どの組み合わせで、どの語か？',
    mcbEyebrow='演習 2 · 再生可能エネルギー',
    mcbTitle='どの組み合わせで、どの語か？',
    mccEyebrow='演習 3 · 消費と廃棄物',
    mccTitle='どの組み合わせで、どの語か？',

    v1why='<em>Cut emissions</em>――または <em>reduce</em>、<em>lower</em>、<em>cur'
          'b</em>。<em>Lower down</em> と <em>shrink off</em> '
          'は、英語がここでは使わない小辞を加えていて、<em>descend</em> は自分が下りることで、何かを下げることではありません。',
    v2why='<em>Carbon footprint</em>。理屈で導く人はいません――丸ごと覚えるもの'
          'で、<em>step</em>、<em>trace</em>、<em>fingerprint</em> はどれも、覚え'
          'ていないことを告げてしまいます。',
    v3why='誰が払うか。汚れた空気のコストは、それを出していない人々に降りかかる――この考えによく伴う論点で、パート3の答えがそのまま借りられる'
          '形です。',
    v4why='<em>A carbon tax</em> がふつうの呼び方です（<em>carbon price</em> や '
          '<em>carbon levy</em> も見かけます）。<em>Fine</em> '
          'は規則違反への罰金、<em>tariff</em> は輸入に課されるもの、<em>toll</em> は道路や橋の通行料です。',
    v5why='<em>Generate electricity</em>（または '
          '<em>produce</em>）。<em>Fabricate</em> と <em>manufacture</em> '
          'は物について使い、<em>originate</em> を電力について使う人はいません。',
    v6why='<em>Intermittent</em>：エネルギー源の仕組みのせいで、あったりなかったりする。<em>Interrupted</'
          'em> は出来事による中断、<em>infrequent</em> はまれ、<em>intermediate</em> '
          'は響きが似ているだけの別の語です。',
    v7why='<em>Phase out coal</em>。小辞は動詞の一部で、段階的に終わらせるという'
          '意味を担えるのは <em>out</em> だけです。',
    v8why='補助金対市場。受験者は、公的資金がタービンを建てたことを認めたうえで、この産業がいつかそれなしでやっていけるのかと問う――一つの考え'
          'の両面で、パート3が引き出そうとしている、展開のある答えです。',
    v9why='<em>Sent to landfill</em>――イギリス英語では冠詞なしですが、アメリカ英語では <em>a '
          'landfill</em> と言います。ほかの三つは、地面の同じ穴を、英語ではそう呼ばない語で表しています。',
    v10why='<em>Single-use plastic</em>。形容詞はハイフンつきで、決まった形です。'
           'ほかの選択肢は同じ意味でも、どれも書き手が当てずっぽうだとわかってしま'
           'います。',
    v11why='<em>Cut down on</em>――または <em>cut back '
           'on</em>。句動詞はすべての小辞と一緒に使います：<em>cut off</em> と <em>cut away</em> '
           'は意味の違う実在の動詞で、どちらも <em>on</em> を取らず、<em>cut back off</em> '
           'は英語ではありません。',
    v12why='個人の責任より生産者の責任。買い物客には変われと言われますが、大事な決'
           '定は包装部門で下されていました。この議論と <em>excess packaging</em> '
           'という組み合わせは一緒にやって来ます。',

    sortEyebrow='演習 4 · アイデアごとにしまう',
    sortTitle='六つの組み合わせをしまいましょう',
    sortHint='それぞれを列にドラッグしてください。または項目をクリックしてから、'
             '入れたい列をクリックします。',
    sortBin1='排出とエネルギー',
    sortBin2='消費と廃棄物',
    sortWhy='アイデアごとにしまうと、どの組み合わせも、それが支える議論の隣に置か'
            'れます。<em>Burn fossil fuels</em> と <em>phase out coal</em> は、排出'
            'と石炭からの転換についての段落の半分です。<em>a throwaway '
            'culture</em> と <em>excess packaging</em> は、生産者の責任についての'
            '段落の半分です。アルファベット順にしまえばただの六語で、時間に追われ'
            'ているときには、それで言えることが何もありません。',

    actTitle='語彙集から答える',
    actUse='少なくとも三つ使いましょう：',
    actSpeakBrief='ペアで。一人が試験官になり、環境についてパート3の質問を三つします――排出について行動すべきなのは政府か個人か、再生'
                  '可能エネルギーは石炭に代われるか、リサイクルはする価値があるか。もう一人は語彙集の組み合わせを使って答えます。三問ご'
                  'とに交代しましょう。',
    actSpeak1='どの答えにも、語彙集の組み合わせを少なくとも一つ、丸ごと入れること'
              '――動詞とその名詞、または形容詞とその名詞。',
    actSpeak2='試験官は答えのたびに <em>why</em> と尋ねます。続きの答えでは、その'
              'アイデアについてきた議論を一つ使うこと：誰が払うか、信頼性対コスト、'
              '個人対生産者。',
    actSpeak3='語彙集にない語なら、難しい語に手を伸ばさず、平易な英語でそのものを'
              '説明しましょう。',
    actWriteKind='ライティング · 150–200 語',
    actWriteBrief='三つのアイデア――排出、再生可能エネルギー、消費と廃棄物――のど'
                  'れかについて、Task 2 の本論の段落を一つ書きましょう。語彙集の組'
                  'み合わせを少なくとも五つ使い、それぞれに下線を引きます。そのあ'
                  'と、その段落がどの議論を展開しているかを書きます。',
    actPlaceholder='The most effective way to cut emissions is…',
)


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    rows = ['    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
            for k in sorted(d)]
    rows += ['    %s: %s' % (k, TAIL[code][k]) for k in sorted(TAIL[code])]
    return '{\n' + ',\n'.join(rows) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
