# -*- coding: utf-8 -*-
"""Have Your Say 3 — Key Topics: South Africa (B1-B2). A house style 2 (panel)
deck, the content companion to the two comment-writing decks
(build_comment_sa.py).

Source: Innes's Word sheet "Key topics for your comment in your class test"
(Downloads, 2026-10-06) — five topics as bullet points (Independence,
Apartheid, Nelson Mandela, the Rainbow Nation, South Africa today), a "key
connection to remember", and four pictures. Nothing on the sheet is dropped:
every bullet is in a reading panel, and every one is tested at least once.

  1 Independence     — 2 panels, 3 key-word cards, MC x3
  2 Apartheid,       — 4 panels, sort x8 (under apartheid / since 1994),
    Mandela            MC x5
  3 Rainbow Nation,  — 3 panels, 4 key-word cards, gap x2 (6 blanks), MC x3
    today
  4 The connection   — order (five events, no dates on the pieces), MC x1,
                       then the sheet's own infographic as a revision divider
then results and the activation stage, whose writing task is the comment the
class test asks for, in the shape Have Your Say 1 teaches.

**Additions to the sheet, all checked:** "apartheid" is Afrikaans for
"apartness"; the means of resistance (strikes, protests, the ANC) and of
international pressure (sanctions, sports boycotts); the 1993 Nobel Peace
Prize shared with de Klerk; the term "Rainbow Nation" popularised by Desmond
Tutu; South Africa rejoined the Commonwealth in 1994; the Truth and
Reconciliation Commission (1996); 12 official languages since Sign Language
was added in 2023. The infographic's "no longer a British colony" (1910) is
loose — a dominion was still inside the Empire — so the panels say
"self-governing dominion", as the sheet's own text does.

**Art.** The sheet's four pictures, via comment_sa_kt_art.py (the white ground
swapped for the deck's paper; see that file). Three portrait flat-vector
pieces carry the stages: the flag heart (1), the patterned map (2), the
giraffe (3); stage 4 opens on the cover, and the infographic is shown whole
as the revision divider, after every question it would answer. HOUSE-STYLE
§5c's one-picture-per-section is met by stage. Every slide that is not a
panel or a divider names a one-sided plate (kt-*-quiz.jpg): the two-sided
cover, washed behind them, put the heart under every answer button.

**The infographic goes AFTER the questions on purpose.** It prints every date
and the key message, so shown first it is an answer sheet.

Reading panels stay English in every language: they are the text the test
is written in, and the questions test them.

Run from the repo root:  py lesson-template/build/build_comment_sa_kt.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import deck as D
import i18n_comment_sa_kt as I

TPL = 'lesson-template/lesson-template.html'
OUT = 'writing-a-comment-south-africa-key-topics.html'
F = 'CommentSouthAfrica'

E = I.T['en']

# py lesson-template/extract-palette.py CommentSouthAfrica/kt-hero.jpg --light
# (2026-10-06; every row PASS)
PALETTE = """  --hero: url('%s/kt-hero.jpg');

  --void          : #cbbdba;
  --surface       : #d8d0ce;
  --surface2      : #d0c6c4;
  --border        : #96744a;
  --text          : #2a1e11;
  --text-dim      : #5e482e;
  --accent        : #7c4400;
  --accent-bright : #623601;
  --accent-dim    : #e58511;
  --secondary     : #040d89;
  --contrast      : #075055;""" % F

HEART, MAP, GIRAFFE = 'kt-heart-paper.jpg', 'kt-africa-paper.jpg', 'kt-giraffe-paper.jpg'
# Behind the slides that are not panels: one picture per stage, on the right.
Q1, Q2, Q3 = 'kt-heart-quiz.jpg', 'kt-africa-quiz.jpg', 'kt-giraffe-quiz.jpg'

# ── reading panels: English in every language ─────────────────────────
READ = {
    1: ['South Africa was once part of the British Empire. In <strong>1910</strong> '
        'the Union of South Africa became a <strong>self-governing dominion</strong>: '
        'it ran its own affairs, but it was still inside the Empire.',
        'In <strong>1961</strong> it became a <strong>republic</strong> and left the '
        'Commonwealth. From then on, it made all its own political decisions.'],
    2: ['But independence did not mean freedom and equality for all. By 1961 '
        '<strong>apartheid</strong> was already in place.',
        'The country governed itself, yet most of its people had no vote and few '
        'rights. Self-government was, in practice, government by a white minority.'],
    3: ['<strong>Apartheid</strong> — Afrikaans for “apartness” — was a system of '
        'racial <strong>segregation</strong>, introduced officially in '
        '<strong>1948</strong>. The law classified every person by race, and each '
        'group had different rights.',
        'The white minority controlled the government. Black South Africans faced '
        'severe <strong>discrimination</strong> in housing, education, work and '
        'freedom of movement.'],
    4: ['Resistance inside South Africa — strikes, protests, the ANC — and pressure '
        'from abroad, such as sanctions and sports boycotts, slowly broke the system.',
        'In <strong>1994</strong> South Africa held its first democratic election: '
        'for the first time, people of all races could vote.'],
    5: ['Nelson Mandela was a leader of the African National Congress (ANC), which '
        'fought against apartheid. Because of his political activities he spent '
        '<strong>27 years</strong> in prison.',
        'He was released in <strong>1990</strong> and worked with President '
        'F. W. de Klerk to negotiate the end of apartheid. In <strong>1994</strong> '
        'he became South Africa’s first Black president.'],
    6: ['Mandela chose <strong>reconciliation</strong> over revenge: he asked the '
        'country to build a future together rather than punish the past.',
        'He became an international symbol of democracy and of the fight against '
        'racial discrimination. In 1993 he and de Klerk shared the Nobel Peace Prize.'],
    7: ['The term <strong>“Rainbow Nation”</strong> describes South Africa as a '
        'diverse country, with people from many cultural, ethnic and linguistic '
        'backgrounds. Archbishop Desmond Tutu made it popular after the end of apartheid.',
        'It stands for unity, reconciliation and living together despite '
        'differences. South Africa has <strong>12 official languages</strong>.'],
    8: ['The Rainbow Nation is an important national ideal. But it is still '
        'challenged by deep social and economic <strong>inequality</strong>.',
        'Poverty, unemployment, unequal access to opportunities and crime remain '
        'serious problems — and many of them can be traced back to apartheid.'],
    9: ['South Africa today is a democracy with a <strong>diverse</strong> population, '
        'a strong cultural identity and an active civil society. It has changed '
        'enormously since 1994.',
        'Yet the effects of apartheid can still be seen, above all in economic and '
        'social inequality. Today’s South Africa shows both progress and continuing '
        'challenges.'],
}


def panel(n, eyebrow, pic, side='left', pos=None):
    a, b = READ[n]
    return D.panel(eyebrow, E[eyebrow], 's%dt' % n, E['s%dt' % n],
                   [(None, a), (None, b)], folder=F, pic=pic, side=side, pos=pos)


def divider(n, pic):
    return D.divider('d%dt' % n, E['d%dt' % n], 'd%dn' % n, E['d%dn' % n],
                     folder=F, pic=pic)


# (English head, body key, English example) — six-item form, so the
# definition translates and the word and its example stay English.
WORDS1 = [('dominion', 'w1b1', 'In 1910 South Africa became a self-governing DOMINION.'),
          ('republic', 'w1b2', 'France and the USA are REPUBLICS; the UK is not.'),
          ('the Commonwealth', 'w1b3', 'South Africa left in 1961 and rejoined in 1994.')]
WORDS2 = [('segregation', 'w2b1', 'Buses, beaches and schools were SEGREGATED.'),
          ('discrimination', 'w2b2', 'She faced DISCRIMINATION at work because of her age.'),
          ('reconciliation', 'w2b3', 'The Truth and RECONCILIATION Commission began in 1996.'),
          ('inequality', 'w2b4', 'INEQUALITY between rich and poor areas is still high.')]


def words(title_key, items, bg, cols=None):
    return D.teach('eW', E['eW'], title_key, E[title_key],
                   [(None, h, bk, E[bk], None, ex) for h, bk, ex in items],
                   cols=cols, folder=F, bg=bg)


# ── multiple choice ────────────────────────────────────────────────────
MC1 = [
    dict(stem='In 1910, the Union of South Africa became ____.',
         options=['a fully independent republic', 'a self-governing dominion',
                  'a colony ruled from London', 'a democracy with equal rights'],
         correct=1, why='q1w'),
    dict(stem='What happened in 1961?',
         options=['It joined the Commonwealth and the British Empire.',
                  'It ended apartheid and held its first free vote.',
                  'It elected its first Black president by free vote.',
                  'It became a republic and left the Commonwealth.'],
         correct=3, why='q2w'),
    dict(stem='Why did independence not bring freedom for everyone?',
         options=['Because apartheid was already in place.',
                  'Because Britain still made every decision.',
                  'Because the country had no government yet.',
                  'Because only the Commonwealth could make laws.'],
         correct=0, why='q3w'),
]
MC2 = [
    dict(stem='Apartheid was introduced officially in ____.',
         options=['1910', '1961', '1948', '1990'], correct=2, why='q4w'),
    dict(stem='Under apartheid, Black South Africans faced discrimination in ____.',
         options=['only national elections, not daily life',
                  'housing, education, work and travel',
                  'only the cities, never in the countryside',
                  'English-speaking schools, but nowhere else'],
         correct=1, why='q5w'),
    dict(stem='How long did Nelson Mandela spend in prison?',
         options=['17 years', '7 years', '37 years', '27 years'], correct=3, why='q6w'),
    dict(stem='Mandela negotiated the end of apartheid with ____.',
         options=['President F. W. de Klerk', 'Archbishop Desmond Tutu',
                  'the British government', 'Queen Elizabeth II'],
         correct=0, why='q7w'),
    dict(stem='In 1994, Nelson Mandela became ____.',
         options=['the first president of the republic',
                  'South Africa’s first Black president',
                  'the last prime minister of apartheid',
                  'the head of the British Commonwealth'],
         correct=1, why='q8w'),
]
MC3 = [
    dict(stem='What does the term “Rainbow Nation” describe?',
         options=['a flag with all the colours of the rainbow',
                  'a nation where everyone speaks one language',
                  'a country of many cultures living together',
                  'the political party that won the 1994 vote'],
         correct=2, why='q9w'),
    dict(stem='How many official languages does South Africa have?',
         options=['2', '12', '9', '20'], correct=1, why='q10w'),
    dict(stem='Which of these is still a major challenge in South Africa today?',
         options=['a lack of democracy', 'rule from London',
                  'economic inequality', 'apartheid laws'],
         correct=2, why='q11w'),
]
MC4 = [
    dict(stem='Which sentence sums up the key connection?',
         options=['Independence in 1961 brought freedom and equality for all.',
                  'Apartheid ended in 1910, when Britain gave independence.',
                  'Freedom came first, and independence followed in 1994.',
                  'Independence came first; freedom for all came much later.'],
         correct=3, why='q12w'),
]
for group in (MC1, MC2, MC3, MC4):
    D.assert_no_key_is_longest(group)

# ── gap fill: (rows, bank) ─────────────────────────────────────────────
GAPS = [
    ([('Apartheid was a system of racial ______, introduced by law in 1948.',
       ['segregation|discrimination'], 'g1w1'),
      ('Mandela became a symbol of ______ because he chose peace over revenge.',
       ['reconciliation'], 'g1w2'),
      ('In 1961 South Africa became a ______ and left the Commonwealth.',
       ['republic'], 'g1w3')],
     ['republic', 'dominion', 'segregation', 'reconciliation', 'independence']),
    ([('The gap between rich and poor — economic ______ — is still a big challenge.',
       ['inequality|inequalities'], 'g2w1'),
      ('Black South Africans faced severe ______ in housing, education and work.',
       ['discrimination'], 'g2w2'),
      ('South Africa has a ______ population, with many cultures and languages.',
       ['diverse'], 'g2w3')],
     ['diverse', 'poverty', 'inequality', 'discrimination', 'democracy']),
]
for rows, bank in GAPS:
    D.assert_bank_is_not_a_key(bank, [a for _, ans, _ in rows for a in ans])

# ── sort: under apartheid, or since 1994 ──────────────────────────────
SORT_ITEMS = [
    ('People are classified by race.', 0),
    ('People of all races can vote.', 1),
    ('Black South Africans cannot vote in national elections.', 0),
    ('The constitution protects equal rights for everyone.', 1),
    ('The law decides where people of each race can live.', 0),
    ('Nelson Mandela is elected president.', 1),
    ('Many schools and beaches are for one race only.', 0),
    ('The country has 12 official languages.', 1),
]

# ── order: the events with no dates on them, so it tests the history,
#    not whether 1948 comes before 1961 ─────────────────────────────────
ORDER = ['the Union of South Africa was formed',
         'apartheid became law',
         'the country became a republic',
         'Mandela was released from prison',
         'all races voted for the first time']


def build():
    logo = D.logo_from(TPL)

    slides = "".join([
        D.cover(logo, E['coverTitle'], E['coverSub'],
                [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                 ('Count', E['chipCount'])]),

        # ── stage 1 · independence ─────────────────────────────────────
        divider(1, 'kt-heart-wide.jpg'),
        panel(1, 'e1', HEART),
        words('w1t', WORDS1, Q1),
        panel(2, 'e1', HEART, side='right'),
    ] + [
        D.mc(i + 1, len(MC1), q, 'e1', E['e1'], 'mcT', E['mcT'], folder=F, bg=Q1)
        for i, q in enumerate(MC1)
    ] + [
        # ── stage 2 · apartheid and Mandela ────────────────────────────
        divider(2, 'kt-africa-wide.jpg'),
        panel(3, 'e2', MAP),
        panel(4, 'e2', MAP, side='right'),
        D.sort_slide([E['binA'], E['binB']], SORT_ITEMS,
                     'e2', E['e2'], 'sortT', E['sortT'],
                     'sortHint', E['sortHint'], 'sortWhy',
                     bin_keys=['binA', 'binB'], folder=F, bg=Q2),
        D.mc(1, 2, MC2[0], 'e2', E['e2'], 'mcT', E['mcT'], folder=F, bg=Q2),
        D.mc(2, 2, MC2[1], 'e2', E['e2'], 'mcT', E['mcT'], folder=F, bg=Q2),
        panel(5, 'e2b', MAP, pos='50% 85%'),
        panel(6, 'e2b', MAP, side='right', pos='50% 85%'),
    ] + [
        D.mc(i + 1, 3, q, 'e2b', E['e2b'], 'mcT', E['mcT'], folder=F, bg=Q2)
        for i, q in enumerate(MC2[2:])
    ] + [
        # ── stage 3 · the Rainbow Nation, today ────────────────────────
        divider(3, 'kt-giraffe-wide.jpg'),
        panel(7, 'e3', GIRAFFE),
        panel(8, 'e3', GIRAFFE, side='right', pos='50% 20%'),
        panel(9, 'e3b', GIRAFFE),
        words('w2t', WORDS2, Q3, cols='1fr 1fr'),
    ] + [
        D.gap(i + 1, len(GAPS), rows, bank, 'eW', E['eW'], 'gapT', E['gapT'],
              folder=F, bg=Q3, hint=E['gapHint'], hint_key='gapHint', width=190)
        for i, (rows, bank) in enumerate(GAPS)
    ] + [
        D.mc(1, 1, MC3[0], 'e3', E['e3'], 'mcT', E['mcT'], folder=F, bg=Q3),
        D.mc(1, 2, MC3[1], 'e3b', E['e3b'], 'mcT', E['mcT'], folder=F, bg=Q3),
        D.mc(2, 2, MC3[2], 'e3b', E['e3b'], 'mcT', E['mcT'], folder=F, bg=Q3),

        # ── stage 4 · the key connection ───────────────────────────────
        divider(4, 'kt-hero.jpg'),
        D.order(ORDER, 'e4', E['e4'], 'orderT', E['orderT'],
                'orderHint', E['orderHint'], 'orderWhy', folder=F, bg=Q2),
        D.mc(1, 1, MC4[0], 'e4', E['e4'], 'mcT', E['mcT'], folder=F, bg=Q1),
        divider(5, 'kt-overview-wide.jpg'),

        # ── results, then activation (§10b: activation is last) ────────
        D.results(folder=F, bg=Q2),
        D.activate(E['actTitle'], E['actUse'],
                   ['a self-governing dominion', 'became a republic',
                    'racial segregation', 'discrimination', 'was released',
                    'reconciliation', 'the Rainbow Nation', 'economic inequality'],
                   'Speaking', E['actSpeakBrief'],
                   [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                   E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'],
                   folder=F, bg=Q3),
    ])

    D.assemble(TPL, OUT, slides, PALETTE,
               'Have Your Say 3 — Key Topics for a Comment: South Africa (B1-B2)',
               I, langs=('en', 'de', 'es'))
    print('wrote %s — %d slides' % (OUT, slides.count('<section class="slide')))


if __name__ == '__main__':
    build()
