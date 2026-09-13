# -*- coding: utf-8 -*-
"""Interface strings for IELTS Vocabulary: Environment and Energy.

English, German and Spanish, teach cards in the six-item form.

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

T = {}

# ── English ────────────────────────────────────────────────────────────
T['en'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='The first topic bank: three ideas, each with its pairings and '
             'its argument already attached',
    chipLevel='C1 · Advanced', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 points',

    t1Eyebrow='Idea 1 of 3',
    t1Title='Emissions: three pairings and two arguments',
    t1ah='Cut them &mdash; the verb is fixed',
    t1ab='Emissions are <em>cut</em> or <em>reduced</em>; a country '
         '<em>burns fossil fuels</em> and releases <em>greenhouse gases</em>; '
         'a city measures its <em>air quality</em>. The verb is chosen by the '
         'noun, and none of the four is rare.',
    t1an='Four pairings, learnt whole. A bare <em>emissions</em> in the '
         'notebook is worth none of them.',
    t1bh='The footprint and the tax',
    t1bb='A person or a firm has a <em>carbon footprint</em>, and shrinking '
         'it is what a <em>carbon tax</em> is for. Neither noun can be '
         'derived: nobody guesses <em>footprint</em>, and nobody guesses that '
         'the charge is called a <em>tax</em>.',
    t1bn='File them together. The tax exists because of the footprint.',
    t1ch='The argument it arrives with',
    t1cb='Two shapes carry most Part 3 answers here. <strong>Who '
         'pays</strong>: dirty air lands on people who did not produce it. '
         '<strong>Targets against enforcement</strong>: a country can promise '
         'to halve its emissions and never fine a single factory.',
    t1cn='File the idea, and the paragraph is half-written before the '
         'question is read.',

    t2Eyebrow='Idea 2 of 3',
    t2Title='Renewables: generate, subsidise, phase out',
    t2ah='Generate, not make',
    t2ab='A <em>wind farm</em> or a roof of <em>solar panels</em> '
         '<em>generates electricity</em>, and what it generates feeds the '
         '<em>national grid</em>. <em>Renewable energy</em> is the umbrella '
         'term; <em>renewables</em> on its own is the noun a Part 3 answer '
         'uses.',
    t2an='Four pairings and one umbrella noun. All plain, all fixed.',
    t2bh='The precise word for the weakness',
    t2bb='The sun sets and the wind drops, so the supply is '
         '<em>intermittent</em>: it comes and goes on its own schedule. '
         'Several words sound close and mean something else, and the '
         'examiner counts the one that means what you meant.',
    t2bn='A near-miss that sounds advanced scores below the plain word that '
         'lands.',
    t2ch='The argument it arrives with',
    t2cb='Governments <em>subsidise</em> renewables and <em>phase out '
         'coal</em>, and every essay on the topic weighs the same two pairs. '
         '<strong>Reliability against cost</strong>: cheap to generate, dear '
         'to store. <strong>Subsidy against the market</strong>: the panels '
         'exist because someone paid, and may need someone to keep paying.',
    t2cn='<em>Energy security</em> is the third term: a country that '
         'generates its own power cannot be cut off.',

    t3Eyebrow='Idea 3 of 3',
    t3Title='Consumption and waste: the pairing includes the preposition',
    t3ah='Sent to landfill, cut down on',
    t3ab='Rubbish is <em>sent to landfill</em>; a council reports its '
         '<em>recycling rates</em>; a shopper <em>cuts down on</em> '
         '<em>excess packaging</em>. The preposition belongs to the pairing: '
         '<em>landfill</em> takes no article, and the phrasal verb is two '
         'particles, not one.',
    t3an='Write the whole thing. Half a phrasal verb is a miss.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='A bottle used once is <em>single-use plastic</em>; a society that '
         'expects to bin things has a <em>throwaway culture</em>; a scheme '
         'that pays you to bring the bottle back is a <em>deposit '
         'scheme</em>. Three adjective-noun pairings, all C1, none rare.',
    t3bn='<em>A throwaway culture</em> is worth more than '
         '<em>consumerism</em> because it is precise.',
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

    v1why='<em>Cut emissions</em>, or <em>reduce</em> them. The verb is '
          'fixed by the noun; the other three are a verb from another '
          'language wearing English clothes, and the examiner hears each one '
          'as a miss.',
    v2why='A <em>carbon footprint</em>. Nobody derives it &mdash; it is '
          'learnt whole, and a step, a trace or a fingerprint each announce '
          'that it was not.',
    v3why='Who pays. The cost of poor air lands on people who did not '
          'produce it &mdash; the argument this idea most often arrives '
          'with, and a shape a Part 3 answer can borrow whole.',
    v4why='A <em>carbon tax</em>. The charge on a tonne of CO&#8322; is '
          'called a tax in every English debate about it; fine, tariff and '
          'toll each name a different thing.',
    v5why='<em>Generate electricity</em>. Fabricate and manufacture are for '
          'objects, and originate is not a verb anyone uses of power. The '
          'plain verb is the one the noun takes.',
    v6why='<em>Intermittent</em>: it comes and goes of its own accord. '
          'Interrupted means somebody stopped it, infrequent means rarely, '
          'and intermediate is a different word that merely sounds close.',
    v7why='<em>Phase out coal</em>. The particle is part of the verb, and '
          'only <em>out</em> carries the meaning of ending something in '
          'stages.',
    v8why='Subsidy against the market. The candidate grants that public '
          'money built the turbines, then asks whether the industry can ever '
          'do without it &mdash; one idea, both sides, which is what Part 3 '
          'rewards.',
    v9why='<em>Sent to landfill</em>, no article. The verb is send and the '
          'noun is landfill; the other three describe the same hole in the '
          'ground in words English never uses for it.',
    v10why='<em>Single-use plastic</em>. The adjective is hyphenated and '
           'fixed; the alternatives each mean the same thing, and each marks '
           'the writer as guessing.',
    v11why='<em>Cut down on</em>. A phrasal verb is one unit with both its '
           'particles, and swapping either gives a phrase that does not '
           'exist.',
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
            'are already half a paragraph on who pays; <em>a throwaway '
            'culture</em> and <em>excess packaging</em> are half a paragraph '
            'on producer responsibility. Filed alphabetically they are six '
            'words, and under time you would have nothing to say with them.',

    actTitle='Answer from the bank',
    actUse='Use at least three:',
    actSpeakBrief='In pairs. One of you is the examiner and asks three Part 3 '
                  'questions on the environment &mdash; whether governments '
                  'or individuals should act on emissions, whether renewables '
                  'can replace coal, whether recycling is worth the effort. '
                  'The other answers using only pairings from the bank. Swap '
                  'after three.',
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
    coverSub='Die erste Themensammlung: drei Ideen, jede mit ihren Paarungen '
             'und ihrem Argument im Schlepptau',
    chipLevel='C1 · Fortgeschritten', chipFocus='Speaking &amp; Writing Task 2',
    chipCount='18 Punkte',

    t1Eyebrow='Idee 1 von 3',
    t1Title='Emissionen: drei Paarungen und zwei Argumente',
    t1ah='Cut them &mdash; das Verb steht fest',
    t1ab='Emissions werden <em>cut</em> oder <em>reduced</em>; ein Land '
         '<em>burns fossil fuels</em> und setzt <em>greenhouse gases</em> '
         'frei; eine Stadt misst ihre <em>air quality</em>. Das Substantiv '
         'wählt das Verb, und keines der vier ist selten.',
    t1an='Vier Paarungen, als Ganzes gelernt. Ein nacktes <em>emissions</em> '
         'im Heft ist keine davon wert.',
    t1bh='Der Fußabdruck und die Steuer',
    t1bb='Eine Person oder eine Firma hat einen <em>carbon footprint</em>, '
         'und ihn zu verkleinern ist der Zweck einer <em>carbon tax</em>. '
         'Keines der beiden Substantive lässt sich herleiten: niemand rät '
         '<em>footprint</em>, und niemand rät, dass die Abgabe <em>tax</em> '
         'heißt.',
    t1bn='Zusammen ablegen. Die Steuer gibt es wegen des Fußabdrucks.',
    t1ch='Das Argument, das mitkommt',
    t1cb='Zwei Formen tragen die meisten Antworten in Teil 3. <strong>Wer '
         'zahlt</strong>: schmutzige Luft trifft Menschen, die sie nicht '
         'verursacht haben. <strong>Ziele gegen Durchsetzung</strong>: ein '
         'Land kann versprechen, seine Emissionen zu halbieren, und nie eine '
         'einzige Fabrik bestrafen.',
    t1cn='Leg die Idee ab, und der Absatz ist halb geschrieben, bevor du die '
         'Frage gelesen hast.',

    t2Eyebrow='Idee 2 von 3',
    t2Title='Erneuerbare: generate, subsidise, phase out',
    t2ah='Generate, nicht make',
    t2ab='Eine <em>wind farm</em> oder ein Dach voller <em>solar panels</em> '
         '<em>generates electricity</em>, und was erzeugt wird, speist das '
         '<em>national grid</em>. <em>Renewable energy</em> ist der '
         'Oberbegriff; <em>renewables</em> allein ist das Substantiv, das '
         'eine Antwort in Teil 3 verwendet.',
    t2an='Vier Paarungen und ein Oberbegriff. Alle schlicht, alle fest.',
    t2bh='Das genaue Wort für die Schwäche',
    t2bb='Die Sonne geht unter und der Wind legt sich, also ist die '
         'Versorgung <em>intermittent</em>: sie kommt und geht nach eigenem '
         'Plan. Mehrere Wörter klingen ähnlich und bedeuten etwas anderes, '
         'und der Prüfer zählt das, das bedeutet, was du meintest.',
    t2bn='Ein Fastreffer, der gehoben klingt, liegt unter dem schlichten '
         'Wort, das trifft.',
    t2ch='Das Argument, das mitkommt',
    t2cb='Regierungen <em>subsidise</em> Erneuerbare und <em>phase out '
         'coal</em>, und jeder Aufsatz zum Thema wägt dieselben zwei Paare '
         'ab. <strong>Zuverlässigkeit gegen Kosten</strong>: billig zu '
         'erzeugen, teuer zu speichern. <strong>Subvention gegen '
         'Markt</strong>: die Module gibt es, weil jemand gezahlt hat, und '
         'vielleicht muss jemand weiterzahlen.',
    t2cn='<em>Energy security</em> ist der dritte Begriff: ein Land, das '
         'seinen Strom selbst erzeugt, kann nicht abgeschnitten werden.',

    t3Eyebrow='Idee 3 von 3',
    t3Title='Konsum und Abfall: die Präposition gehört zur Paarung',
    t3ah='Sent to landfill, cut down on',
    t3ab='Müll wird <em>sent to landfill</em>; eine Gemeinde meldet ihre '
         '<em>recycling rates</em>; ein Käufer <em>cuts down on</em> '
         '<em>excess packaging</em>. Die Präposition gehört zur Paarung: '
         '<em>landfill</em> steht ohne Artikel, und das Phrasal Verb hat '
         'zwei Partikel, nicht eine.',
    t3an='Schreib das Ganze. Ein halbes Phrasal Verb ist ein Fehlgriff.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='Eine einmal benutzte Flasche ist <em>single-use plastic</em>; eine '
         'Gesellschaft, die Dinge wegwirft, hat eine <em>throwaway '
         'culture</em>; ein System, das dich fürs Zurückbringen bezahlt, '
         'ist ein <em>deposit scheme</em>. Drei Adjektiv-Substantiv-'
         'Paarungen, alle C1, keine selten.',
    t3bn='<em>A throwaway culture</em> ist mehr wert als '
         '<em>consumerism</em>, weil es genau ist.',
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
    mcaTitle='Welche Paarung, und welches Wort?',
    mcbEyebrow='Aktivität 2 · Erneuerbare',
    mcbTitle='Welche Paarung, und welches Wort?',
    mccEyebrow='Aktivität 3 · Konsum und Abfall',
    mccTitle='Welche Paarung, und welches Wort?',

    v1why='<em>Cut emissions</em>, oder <em>reduce</em>. Das Verb ist durch '
          'das Substantiv festgelegt; die anderen drei sind ein Verb aus '
          'einer anderen Sprache in englischer Kleidung, und der Prüfer hört '
          'jedes als Fehlgriff.',
    v2why='Ein <em>carbon footprint</em>. Niemand leitet es her &mdash; es '
          'wird als Ganzes gelernt, und step, trace oder fingerprint '
          'verraten, dass es das nicht wurde.',
    v3why='Wer zahlt. Die Kosten schlechter Luft treffen Menschen, die sie '
          'nicht verursacht haben &mdash; das Argument, mit dem diese Idee '
          'am häufigsten ankommt, und eine Form, die eine Antwort in Teil 3 '
          'ganz übernehmen kann.',
    v4why='Eine <em>carbon tax</em>. Die Abgabe auf eine Tonne CO&#8322; '
          'heißt in jeder englischen Debatte darüber tax; fine, tariff und '
          'toll benennen jeweils etwas anderes.',
    v5why='<em>Generate electricity</em>. Fabricate und manufacture sind für '
          'Gegenstände, und originate verwendet niemand für Strom. Das '
          'schlichte Verb ist das, das das Substantiv nimmt.',
    v6why='<em>Intermittent</em>: es kommt und geht von selbst. Interrupted '
          'heißt, jemand hat es gestoppt, infrequent heißt selten, und '
          'intermediate ist ein anderes Wort, das nur ähnlich klingt.',
    v7why='<em>Phase out coal</em>. Die Partikel gehört zum Verb, und nur '
          '<em>out</em> trägt die Bedeutung, etwas schrittweise zu beenden.',
    v8why='Subvention gegen Markt. Der Kandidat räumt ein, dass öffentliches '
          'Geld die Turbinen gebaut hat, und fragt dann, ob die Branche je '
          'ohne auskommt &mdash; eine Idee, beide Seiten, genau das, was '
          'Teil 3 belohnt.',
    v9why='<em>Sent to landfill</em>, ohne Artikel. Das Verb ist send und '
          'das Substantiv landfill; die anderen drei beschreiben dasselbe '
          'Loch im Boden mit Wörtern, die das Englische dafür nie verwendet.',
    v10why='<em>Single-use plastic</em>. Das Adjektiv ist mit Bindestrich '
           'und fest; die Alternativen bedeuten alle dasselbe, und jede '
           'verrät, dass geraten wurde.',
    v11why='<em>Cut down on</em>. Ein Phrasal Verb ist eine Einheit mit '
           'beiden Partikeln, und wer eine tauscht, erhält eine Phrase, die '
           'es nicht gibt.',
    v12why='Hersteller vor Einzelnem. Der Käufer soll sich ändern, während '
           'die entscheidende Wahl in der Verpackungsabteilung getroffen '
           'wurde. Das Argument und die Paarung <em>excess packaging</em> '
           'kommen zusammen an.',

    sortEyebrow='Aktivität 4 · Nach Ideen ablegen',
    sortTitle='Lege die sechs Paarungen ab',
    sortHint='Zieh jede in eine Spalte &mdash; oder klicke ein Element an und '
             'dann die Spalte, in die es soll.',
    sortBin1='Emissionen und Energie',
    sortBin2='Konsum und Abfall',
    sortWhy='Nach Ideen abgelegt, liegt jede Paarung neben dem Argument, dem '
            'sie dient. <em>Burn fossil fuels</em> und <em>phase out '
            'coal</em> sind schon ein halber Absatz darüber, wer zahlt; '
            '<em>a throwaway culture</em> und <em>excess packaging</em> ein '
            'halber Absatz über die Verantwortung der Hersteller. '
            'Alphabetisch abgelegt sind es sechs Wörter, und unter Zeitdruck '
            'hättest du nichts damit zu sagen.',

    actTitle='Antworte aus der Sammlung',
    actUse='Verwende mindestens drei:',
    actSpeakBrief='Zu zweit. Einer ist der Prüfer und stellt drei Fragen aus '
                  'Teil 3 zur Umwelt &mdash; ob Regierungen oder Einzelne '
                  'gegen Emissionen handeln sollen, ob Erneuerbare Kohle '
                  'ersetzen können, ob Recycling die Mühe lohnt. Der andere '
                  'antwortet nur mit Paarungen aus der Sammlung. Nach drei '
                  'Fragen tauschen.',
    actSpeak1='Jede Antwort trägt mindestens eine Paarung aus der Sammlung, '
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
                  'und Abfall. Verwende mindestens fünf Paarungen aus der '
                  'Sammlung und unterstreich jede. Dann sag, welches Argument '
                  'der Absatz macht.',
    actPlaceholder='The most effective way to cut emissions is…',
)

# ── Spanish ────────────────────────────────────────────────────────────
T['es'] = dict(
    coverTitle='Environment <em>and Energy</em>',
    coverSub='El primer banco temático: tres ideas, cada una con sus parejas '
             'y su argumento ya enganchado',
    chipLevel='C1 · Avanzado', chipFocus='Speaking y Writing Task 2',
    chipCount='18 puntos',

    t1Eyebrow='Idea 1 de 3',
    t1Title='Emisiones: tres parejas y dos argumentos',
    t1ah='Cut them: el verbo es fijo',
    t1ab='Las emissions se <em>cut</em> o se <em>reduce</em>; un país '
         '<em>burns fossil fuels</em> y libera <em>greenhouse gases</em>; '
         'una ciudad mide su <em>air quality</em>. El sustantivo elige el '
         'verbo, y ninguno de los cuatro es raro.',
    t1an='Cuatro parejas, aprendidas enteras. Un <em>emissions</em> suelto '
         'en el cuaderno no vale ninguna de ellas.',
    t1bh='La huella y el impuesto',
    t1bb='Una persona o una empresa tiene un <em>carbon footprint</em>, y '
         'reducirlo es para lo que sirve una <em>carbon tax</em>. Ninguno de '
         'los dos sustantivos se deduce: nadie adivina <em>footprint</em>, y '
         'nadie adivina que el cobro se llama <em>tax</em>.',
    t1bn='Archívalos juntos. El impuesto existe por la huella.',
    t1ch='El argumento con el que llega',
    t1cb='Dos formas sostienen la mayoría de las respuestas de la Parte 3. '
         '<strong>Quién paga</strong>: el aire sucio cae sobre gente que no '
         'lo produjo. <strong>Objetivos contra cumplimiento</strong>: un '
         'país puede prometer reducir sus emisiones a la mitad y no multar '
         'nunca a una sola fábrica.',
    t1cn='Archiva la idea y el párrafo está medio escrito antes de leer la '
         'pregunta.',

    t2Eyebrow='Idea 2 de 3',
    t2Title='Renovables: generate, subsidise, phase out',
    t2ah='Generate, no make',
    t2ab='Una <em>wind farm</em> o un tejado de <em>solar panels</em> '
         '<em>generates electricity</em>, y lo que genera alimenta el '
         '<em>national grid</em>. <em>Renewable energy</em> es el término '
         'paraguas; <em>renewables</em> a secas es el sustantivo que usa una '
         'respuesta de la Parte 3.',
    t2an='Cuatro parejas y un término paraguas. Todos llanos, todos fijos.',
    t2bh='La palabra exacta para la debilidad',
    t2bb='El sol se pone y el viento cae, así que el suministro es '
         '<em>intermittent</em>: viene y va a su propio ritmo. Varias '
         'palabras suenan parecido y significan otra cosa, y el examinador '
         'cuenta la que significa lo que querías decir.',
    t2bn='Un casi-acierto que suena avanzado puntúa menos que la palabra '
         'llana que encaja.',
    t2ch='El argumento con el que llega',
    t2cb='Los gobiernos <em>subsidise</em> las renovables y <em>phase out '
         'coal</em>, y todo ensayo sobre el tema sopesa las mismas dos '
         'parejas. <strong>Fiabilidad contra coste</strong>: barato de '
         'generar, caro de almacenar. <strong>Subvención contra '
         'mercado</strong>: los paneles existen porque alguien pagó, y quizá '
         'alguien tenga que seguir pagando.',
    t2cn='<em>Energy security</em> es el tercer término: a un país que '
         'genera su propia energía no se le puede cortar.',

    t3Eyebrow='Idea 3 de 3',
    t3Title='Consumo y residuos: la preposición forma parte de la pareja',
    t3ah='Sent to landfill, cut down on',
    t3ab='La basura se <em>sent to landfill</em>; un ayuntamiento informa de '
         'sus <em>recycling rates</em>; un comprador <em>cuts down on</em> '
         '<em>excess packaging</em>. La preposición pertenece a la pareja: '
         '<em>landfill</em> va sin artículo, y el phrasal verb tiene dos '
         'partículas, no una.',
    t3an='Escríbelo entero. Medio phrasal verb es un fallo.',
    t3bh='Single-use, throwaway, deposit',
    t3bb='Una botella que se usa una vez es <em>single-use plastic</em>; una '
         'sociedad que espera tirar las cosas tiene una <em>throwaway '
         'culture</em>; un sistema que te paga por devolver la botella es un '
         '<em>deposit scheme</em>. Tres parejas adjetivo-sustantivo, todas '
         'C1, ninguna rara.',
    t3bn='<em>A throwaway culture</em> vale más que <em>consumerism</em> '
         'porque es precisa.',
    t3ch='El argumento con el que llega',
    t3cb='Pregunta quién debería cambiar y la respuesta ya está escrita. '
         '<strong>Individuo contra productor</strong>: un comprador puede '
         'cambiar sus <em>consumer habits</em>, pero el envase se decidió '
         'antes de que llegara. <strong>Comodidad contra coste</strong>: lo '
         'de un solo uso es barato ahora y se paga después.',
    t3cn='Los dos argumentos funcionan en ambos sentidos, y por eso vale la '
         'pena archivarlos.',

    mcaEyebrow='Actividad 1 · Emisiones',
    mcaTitle='¿Qué pareja, y qué palabra?',
    mcbEyebrow='Actividad 2 · Renovables',
    mcbTitle='¿Qué pareja, y qué palabra?',
    mccEyebrow='Actividad 3 · Consumo y residuos',
    mccTitle='¿Qué pareja, y qué palabra?',

    v1why='<em>Cut emissions</em>, o <em>reduce</em>. El verbo lo fija el '
          'sustantivo; los otros tres son un verbo de otro idioma vestido de '
          'inglés, y el examinador oye cada uno como un fallo.',
    v2why='Un <em>carbon footprint</em>. Nadie lo deduce: se aprende entero, '
          'y step, trace o fingerprint anuncian que no fue así.',
    v3why='Quién paga. El coste del aire sucio cae sobre gente que no lo '
          'produjo: el argumento con el que esta idea llega más a menudo, y '
          'una forma que una respuesta de la Parte 3 puede tomar entera.',
    v4why='Una <em>carbon tax</em>. El cobro por tonelada de CO&#8322; se '
          'llama tax en todo debate en inglés sobre el tema; fine, tariff y '
          'toll nombran cada uno otra cosa.',
    v5why='<em>Generate electricity</em>. Fabricate y manufacture son para '
          'objetos, y originate no lo usa nadie para la energía. El verbo '
          'llano es el que lleva el sustantivo.',
    v6why='<em>Intermittent</em>: viene y va por sí solo. Interrupted '
          'significa que alguien lo paró, infrequent significa rara vez, e '
          'intermediate es otra palabra que solo suena parecido.',
    v7why='<em>Phase out coal</em>. La partícula forma parte del verbo, y '
          'solo <em>out</em> lleva el sentido de terminar algo por etapas.',
    v8why='Subvención contra mercado. El candidato concede que el dinero '
          'público levantó las turbinas y luego pregunta si el sector podrá '
          'prescindir de él: una idea, los dos lados, justo lo que premia la '
          'Parte 3.',
    v9why='<em>Sent to landfill</em>, sin artículo. El verbo es send y el '
          'sustantivo landfill; los otros tres describen el mismo agujero en '
          'el suelo con palabras que el inglés nunca usa para él.',
    v10why='<em>Single-use plastic</em>. El adjetivo lleva guion y es fijo; '
           'las alternativas significan lo mismo, y cada una delata que se '
           'está adivinando.',
    v11why='<em>Cut down on</em>. Un phrasal verb es una unidad con sus dos '
           'partículas, y cambiar cualquiera da una frase que no existe.',
    v12why='Productor por encima del individuo. Al comprador se le pide que '
           'cambie mientras la decisión que importa se tomó en el '
           'departamento de envases. El argumento y la pareja <em>excess '
           'packaging</em> llegan juntos.',

    sortEyebrow='Actividad 4 · Archivar por ideas',
    sortTitle='Archiva las seis parejas',
    sortHint='Arrastra cada una a una columna &mdash; o haz clic en un '
             'elemento y luego en la columna que quieras.',
    sortBin1='Emisiones y energía',
    sortBin2='Consumo y residuos',
    sortWhy='Archivada por ideas, cada pareja queda junto al argumento al que '
            'sirve. <em>Burn fossil fuels</em> y <em>phase out coal</em> ya '
            'son medio párrafo sobre quién paga; <em>a throwaway culture</em> '
            'y <em>excess packaging</em>, medio párrafo sobre la '
            'responsabilidad del productor. Archivadas por orden alfabético '
            'son seis palabras, y con el reloj en marcha no tendrías nada '
            'que decir con ellas.',

    actTitle='Responde desde el banco',
    actUse='Usa al menos tres:',
    actSpeakBrief='En parejas. Uno es el examinador y hace tres preguntas de '
                  'la Parte 3 sobre el medio ambiente: si deben actuar los '
                  'gobiernos o los individuos frente a las emisiones, si las '
                  'renovables pueden sustituir al carbón, si reciclar merece '
                  'el esfuerzo. El otro responde solo con parejas del banco. '
                  'Cambio de papeles a las tres.',
    actSpeak1='Cada respuesta lleva al menos una pareja del banco, dicha '
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
                  'residuos. Usa al menos cinco parejas del banco y subraya '
                  'cada una. Luego di qué argumento defiende el párrafo.',
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
