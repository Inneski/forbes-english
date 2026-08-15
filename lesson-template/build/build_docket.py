# -*- coding: utf-8 -*-
"""The Docket (B2) — rebuilt as a deck.

The true-crime framing is good and the vocabulary set is genuinely useful, so
both survive whole. Almost every item, however, needed work, and two were
broken past the point where a learner could answer them.

**Cross-examination set 5 shipped with an authoring note in it.** The
explanation read, verbatim: "Sentence A is correct as written &mdash; wait, let
us look again. All three sentences here are correctly formed&hellip; none of
these have errors&hellip; the answer is B." The key pointed at A. So a learner
who clicked the keyed sentence was told "Correct" and then told the answer was
a different one. The item is rewritten.

**Set 4 named no fix and hardcoded the wrong letter.** Its wrongWord and
correctWord were both "clue", so the page could not say what the sentence
should have been; and the explanation said "the error is in sentence B" while
the engine shuffled the sentences on every render, so the letter it named was
right only by luck. One of its three sentences also carried no underline at
all, disqualifying it on sight and narrowing a three-way choice to two.

**The witness statement taught the error it was naming.** Gap 5 keyed
<em>rampant</em> into a sentence that read "&hellip;had been <em>rampant</em>
&mdash; no, I mean rampant is the wrong word. I mean its reputation was
widespread." The word the sentence steers you towards is <em>prevalent</em>,
and <em>prevalent</em> was not in the bank &mdash; while activity 3, two
screens later, defines the pair correctly. The statement now uses both words,
each in a sentence that needs it.

Three more. <em>Mandatory</em> was tested through "the former clerk's offence
was mandatory", which is not a thing an offence can be, and it was the longest
option on its slide. <em>Inadmissible</em> was taught as an absolute &mdash;
"evidence collected without a warrant&hellip; could not be presented in court
under any circumstances" &mdash; which is false in every common-law
jurisdiction. And <em>cleavage</em> was set as a B2 target in "a routine
cleavage dispute", which is not idiomatic in any register a learner will meet.

And, as everywhere in this batch, there was no teaching: twenty-five scored
items and not one line of presentation before them.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-the-docket-b2.html'
F = 'Docket'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0e0b09;
  --surface       : #1c1712;
  --surface2      : #29211a;
  --border        : #9a443c;
  --text          : #f5f2f2;
  --text-dim      : #bfa6a3;
  --accent        : #e66256;
  --accent-bright : #f39991;
  --accent-dim    : #be2f22;
  --secondary     : #4e7e9f;
  --contrast      : #1ded9a;''' % F

MC = [
    dict(stem='The prosecution alleged that the accused had tried to ______ elderly victims out of their savings by posing as a bank official.',
         options=['defraud', 'displace', 'discount', 'detour'],
         correct=0,
         why='To <strong>defraud</strong> someone is to take their money or property by deception. The others are decoys built from the same prefix: <em>displace</em> is to move something, <em>discount</em> is a price reduction, <em>detour</em> is a longer route.'),
    dict(stem='The judge ruled that the recording had been obtained improperly and was therefore ______ &mdash; the jury never heard it.',
         options=['inadmissible', 'insufficient', 'unaccountable', 'irreconcilable'],
         correct=0,
         why='<strong>Inadmissible</strong> means the court will not receive it as evidence. Note the limit: evidence is ruled inadmissible <em>by a judge, case by case</em>. There is no rule that improperly obtained evidence is automatically excluded.'),
    dict(stem='After twenty years, the parole board voted to ______ the restriction that had stopped him leaving the state.',
         options=['revoke', 'reconcile', 'accompany', 'resist'],
         correct=0,
         why='To <strong>revoke</strong> is to cancel something officially &mdash; a licence, an order, a restriction. <em>Reconcile</em> is to bring two things or people back into agreement.'),
    dict(stem='At the press conference the detective stood at the ______ and read the statement without taking a single question.',
         options=['lectern', 'rotunda', 'skirting', 'ministry'],
         correct=0,
         why='A <strong>lectern</strong> is the stand you put your notes on. A <em>rotunda</em> is a round room, <em>skirting</em> is the board at the foot of a wall, and a <em>ministry</em> is a government department.'),
    dict(stem='The court heard that co-operation with the enquiry was ______: every former employee was required by law to take part.',
         options=['mandatory', 'contingent', 'incidental', 'provisional'],
         correct=0,
         why='<strong>Mandatory</strong> means required by law or rule. Note what it attaches to &mdash; a <em>duty</em> can be mandatory; an offence cannot. The colon here does the teaching: the clause after it is the definition.'),
    dict(stem='What began as a routine ______ over an unpaid delivery had escalated into a full civil war inside the company.',
         options=['grievance', 'showdown', 'swagger', 'chatter'],
         correct=0,
         why='A <strong>grievance</strong> is a formal complaint about being wronged &mdash; the word HR and the courts both use. A <em>showdown</em> is the final confrontation, which is what it became, not what it started as.'),
]

GAPS = [
    ('My name is Elena Voss. At the time, I was working as an assessor for a large ______ in the city centre.',
     ['law firm'],
     'A <strong>law firm</strong> is a business of solicitors or attorneys. Two words, and the only two-word answer in the bank.'),
    ('The managing partner began to behave in a way I can only describe as ______ &mdash; he was falsifying the receipts sent to clients.',
     ['fraudulent'],
     '<strong>Fraudulent</strong> means obtained or done by deception. It is the adjective belonging to <em>fraud</em> and to <em>defraud</em>.'),
    ('I am not easily rattled, but working there became genuinely ______ &mdash; I could not sleep and I dreaded going in.',
     ['stressful'],
     'A situation is <strong>stressful</strong>; a person is <em>stressed</em>. There is no such adjective as <em>stressy</em>, which is what a great many learners reach for.'),
    ('For a long time I tried to ______ what I was seeing with the idea that he was simply disorganised.',
     ['reconcile'],
     'Here <strong>reconcile A with B</strong> means to make two things fit together. It is the third sense of the word in this lesson: you also reconcile <em>people</em>, and you reconcile <em>opposing views</em>.'),
    ('The firm was well known throughout the city &mdash; its reputation was ______ in every chambers and every court.',
     ['prevalent'],
     '<strong>Prevalent</strong> means widespread, common, found everywhere. It carries no judgement: a reputation, a practice or a dialect can be prevalent.'),
    ('By the end the falsification was ______ &mdash; it had spread through every department, entirely unchecked.',
     ['rampant'],
     '<strong>Rampant</strong> also means widespread, but only of something bad, and only when nothing is stopping it. Weeds, inflation and corruption are rampant. A reputation is not.'),
    ('When I reported it to the ______ of Justice, they told me to collect whatever documentation I could find.',
     ['ministry'],
     'A <strong>ministry</strong> is a government department. In a real title it takes capitals &mdash; the Ministry of Justice &mdash; but the common noun does not.'),
]
BANK = sorted(['law firm', 'fraudulent', 'stressful', 'reconcile', 'prevalent',
               'rampant', 'ministry', 'revoke', 'swagger'])

MATCH = [
    ('mandatory', 'Required by law; compulsory'),
    ('fraudulent', 'Obtained by criminal deception'),
    ('prevalent', 'Widespread &mdash; and neutral about it'),
    ('rampant', 'Widespread, unchecked, and bad'),
    ('offender', 'A person who commits an illegal act'),
    ('grievance', 'A formal complaint about being wronged'),
]

ERRORS = [
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['The judge told the defendant to stop <u>grumbling</u> under his breath.',
                  'She tried to <u>soothe</u> the frightened child by speaking very quietly.',
                  'The therapist warned him not to <u>dwell on</u> the traumatic event.',
                  'The clerk was asked to <u>corroborate</u> the times given in the statement.'],
         correct=0,
         why='<strong>Grumbling</strong> is complaining out loud and bad-temperedly, usually about a situation. Speaking quietly to yourself is <strong>muttering</strong>. The other three are all used correctly.'),
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['The board agreed to <u>mimic</u> the accounting software used by a competitor.',
                  'The contract terms were <u>insufficient</u> to prove intent &mdash; too vague.',
                  'Fraud of this kind was particularly <u>prevalent</u> in cash economies.',
                  'The auditor was asked to <u>scrutinise</u> every invoice from that quarter.'],
         correct=0,
         why='To <strong>mimic</strong> is to imitate, usually mockingly or superficially. A board does not mimic software &mdash; it <strong>adopts</strong> it, meaning it decides to use it formally.'),
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['She wrote code that would <u>ignite</u> the backup if the server went offline.',
                  'Both parties finally agreed to <u>reconcile</u> their differences and settle.',
                  'He always took the defendant&rsquo;s background into <u>account</u> first.',
                  'The witness was unable to <u>recall</u> the exact sequence of events.'],
         correct=0,
         why='<strong>Ignite</strong> is to set on fire. A process is <strong>triggered</strong> or <em>initiated</em>. Nothing in a data centre ignites, and if it does you have a different problem.'),
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['She feared her report would be seen as a <u>clue</u> to her own involvement.',
                  'The consultant urged them to <u>take into account</u> the effect on morale.',
                  'The CEO&rsquo;s conduct was <u>rampant</u>, spreading through every level.',
                  'Counsel asked the witness to <u>clarify</u> what she had meant by that.'],
         correct=0,
         why='A <strong>clue</strong> is a hint that helps solve a mystery. What she feared was that her report would be taken as <strong>evidence</strong> &mdash; or <em>proof</em> &mdash; of her own part in it.'),
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['The company decided to <u>fall apart</u> its overseas division.',
                  'The suspect was quick <u>on the draw</u> and had deleted the files already.',
                  'He had a habit of <u>shooting from the hip</u> without consulting anyone.',
                  'The firm was ordered to <u>disclose</u> every document from that period.'],
         correct=0,
         why='<strong>Fall apart</strong> is intransitive: a thing falls apart by itself. You cannot fall apart something. To take something apart deliberately is to <strong>dismantle</strong> it.'),
    dict(stem='One of these uses its underlined word wrongly. Which?',
         options=['The analyst was described in the report as a real <u>people person</u>.',
                  'The intern had not been a <u>volunteer</u> &mdash; she had in fact been paid.',
                  'His client had been <u>swindled</u> by a fraudster posing as an official.',
                  'The panel was asked to <u>disregard</u> everything said before the recess.'],
         correct=0,
         why='Every one of these words means what it should. The fault is <strong>register</strong>: <em>a real people person</em> is fine in conversation and wrong in a formal report, where you would write <em>she worked well with witnesses</em>.'),
]

CHIPS = ['defraud', 'inadmissible', 'revoke', 'mandatory', 'a grievance',
         'prevalent', 'rampant', 'corroborate']


def build():
    D.assert_no_key_is_longest(MC, 'Docket MC')
    D.assert_no_key_is_longest(ERRORS, 'Docket errors')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    slides = (
        D.cover(logo, 'The <em>Docket</em>',
                'Crime, the courtroom and the office &mdash; the vocabulary a true-crime series runs on',
                [('Level', 'B2 &middot; Vocabulary'), ('Focus', 'Law &amp; the courtroom'),
                 ('Count', '21 slides')])
        + D.teach('vEyebrow', 'Before the case opens',
                  'vTitle', 'Six words the courtroom cannot do without',
                  [('v1h', 'defraud &middot; fraudulent',
                    'To take money by deception, and the adjective for it.',
                    'v1b', 'The verb takes a person as its object: you defraud <em>somebody</em> <em>out of</em> something.'),
                   ('v2h', 'inadmissible',
                    'Evidence a judge will not let the court receive.',
                    'v2b', 'Ruled case by case, not automatic. Improperly obtained evidence is <em>sometimes</em> excluded &mdash; never always.'),
                   ('v3h', 'revoke &middot; mandatory',
                    'To cancel officially &middot; required by law.',
                    'v3b', 'Watch what <em>mandatory</em> attaches to: a duty, a check, a disclosure. Never an offence.'),
                   ('v4h', 'grievance &middot; offender',
                    'A formal complaint &middot; a person who breaks the law.',
                    'v4b', 'A grievance is raised, heard and either upheld or dismissed. It is the word both HR and the tribunal use.')],
                  cols='1fr 1fr 1fr 1fr', folder=F, bg='bench.jpg')
        + D.teach('pairEyebrow', 'The pair everyone gets wrong',
                  'pairTitle', 'prevalent, rampant, and the three reconciles',
                  [('p1h', 'prevalent',
                    'Widespread. Common. Found all over.',
                    'p1b', 'Neutral. A dialect, a practice, a reputation, a species can all be prevalent, and nothing is implied about whether that is good.'),
                   ('p2h', 'rampant',
                    'Widespread, unchecked &mdash; and bad.',
                    'p2b', 'Weeds, inflation, corruption, rumour. If you would not mind it spreading, it is not rampant.'),
                   ('p3h', 'reconcile &times; 3',
                    'people &middot; views &middot; facts',
                    'p3b', 'Reconcile two <em>people</em>, two <em>views</em> (find where they agree), or one fact <em>with</em> another (make them fit). The third sense is what this case turns on.')],
                  folder=F, bg='desk.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Exhibit A',
                       'qTitle', 'The word the record needs', folder=F,
                       bg='gallery.jpg' if i % 3 == 2 else None)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 3, part, BANK, 'gapEyebrow',
                        'Witness statement &mdash; E. Voss',
                        'gapTitle', 'Complete the testimony', folder=F,
                        hint_key='gapHint',
                        hint='Nine words in the bank, seven gaps. Two are not needed.',
                        width=200, size=17)
                  for n, part in enumerate([GAPS[:3], GAPS[3:5], GAPS[5:]]))
        + D.match(MATCH, 'matchEyebrow', 'The brief',
                  'matchTitle', 'Six words, precisely',
                  'matchHint', 'Click a word, then click its definition.',
                  'The case hinges on the middle two. Prevalent and rampant both mean widespread, and only one of them passes judgement — which is exactly why a careful witness picks between them.',
                  folder=F, bg='desk.jpg')
        + "".join(D.mc(i + 1, len(ERRORS), q, 'errEyebrow', 'Cross-examination',
                       'errTitle', 'Find the wrong word', folder=F,
                       bg='gallery.jpg' if i % 3 == 1 else None)
                  for i, q in enumerate(ERRORS))
        + D.results('resNext', 'You have the vocabulary. Now put it on the record →')
        + D.activate('Take the stand', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in threes',
                     'One witness, one counsel, one judge. Counsel may object; the judge rules.',
                     ['Counsel: establish what the witness saw, without ever asking a yes/no question.',
                      'Witness: describe a practice as <em>prevalent</em>, then describe a different one as <em>rampant</em>. Justify both.',
                      'Judge: rule one piece of evidence inadmissible, and say why in one sentence.',
                      'All three: agree what the grievance actually was, in twelve words or fewer.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the witness statement for something you have actually seen go wrong at work. Formal register throughout &mdash; no <em>people person</em>.',
                     'My name is … At the time of the events, I was working as …')
    )

    import i18n_docket as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'The Docket — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d errors, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH),
             len(ERRORS), pos, len(s)))


if __name__ == '__main__':
    build()
