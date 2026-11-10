# -*- coding: utf-8 -*-
"""Common Mistakes Review, Parts 1-3 (B1, for Spanish speakers). House
style 1, three decks from one builder.

Rebuilt 2026-11-06 from three one-question-at-a-time scrolling pages (14
multiple-choice items each, with a Spanish hint line), under Innes's "make
them house style 2". Each part is now 19 slides: a speaking warm-up, the 14
items one per slide, a recap of what the items taught, results, activation.

Every item is kept. Fixed in the audit:
  * The hint line gave the answer on Parts 1-2: "ES: depend ON something",
    "married TO someone", "lend = prestar", "travel to + lugar", "asistir a =
    to attend", "interested IN", "good AT". Every hint is now a nudge that
    names the trap, not the answer — Part 3's own approach. They translate.
  * Two answers printed in the stem: P1 Q6 asked about "the underlined
    letter" with no underline and the key, "nature", printed after the
    question. P2 Q6/Q7 stems already contained the preposition the options
    supplied, so the key built "interested in in history", "good at at maths".
  * Second correct answers: P1 Q1 "express something to her", P1 Q5 "Did you
    read any of his books?", P1 Q14 "travel in different countries", P2 Q2
    "I felt very nervous", P2 Q3 "wait for the meeting", P2 Q4 "Suddenly I
    remembered I had left my keys", P2 Q13 "I am actually working on a new
    project" are all good English. Stems or distractors changed so the key
    is the only right answer.
  * P3 Q13: "This documentary is so boring! I can't stop thinking about it."
    Now "I fell asleep after ten minutes."
  * P1 Q8's key was the only long option (12 against 5-6); P1 Q10's options
    were Spanish though nothing about the item is Spanish. Both rewritten.
    P1 Q2 and P2 Q1 are about Spanish words and keep Spanish options.
  * The old explanations were half English, half "ES: …". Each is now one
    explanation, in the learner's language.

Art: none existed, so all fifteen slots are stand-ins with briefs (see
docs/ARTWORK-standins.md). The three pages had no library thumbnail and
showed as "Coming soon"; they now point at their stand-in heroes.

Run from the repo root:  py lesson-template/build/build_mistakes_review.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
import deck as D
import i18n_mistakes_review as I
import hs1

TPL = 'lesson-template/lesson-template.html'
F = 'MistakesReview'


def q(stem, options, correct):
    return dict(stem=stem.replace('___', '____'), options=options, correct=correct)


PARTS = {
    1: dict(
        out='forbes-english-common-mistakes-review.html',
        title='Common Mistakes Review (B1)',
        scheme='rose',
        # py lesson-template/extract-palette.py MistakesReview/standin-p1-hero.jpg --paper
        palette=None,
        art={
            'p1-hero': ('write', 'a red pencil correcting one line on a sheet of ruled paper, one word circled, no letters'),
            'p1-talk': ('talk', 'two coffee cups on a small table with two speech bubbles rising from them'),
            'p1-a': ('mail', 'a hand passing a folded note across a desk to another hand'),
            'p1-b': ('time', 'a wall calendar and a train ticket pinned side by side'),
            'p1-act': ('pair', 'two chairs facing each other across a small round table'),
        },
        talk=[
            'Which English mistake do you make most often?',
            'Which English word is hardest for you to pronounce?',
            'Do you translate from your own language when you speak English?',
            'What do you do when you don’t know a word?',
            'Is it better to correct a mistake at once, or later?',
            'Which English word do you always forget?',
        ],
        items=[
            q('When I need to ___ something to her, I need AI to help me.',
              ['explicate', 'explain', 'expose', 'exploit'], 1),
            q('Which English verb translates the Spanish verb “pedir”?',
              ['to answer', 'to ask', 'to tell', 'to say'], 1),
            q('I need ___ activate my account.', ['activate', 'that I', 'activating', 'to'], 3),
            q('Choose the correct sentence.', ['He is died.', 'He is dead.', 'He died is.', 'He has dead.'], 1),
            q('___ you read any of his books? — Yes, I’ve read two of them.', ['Do', 'Did', 'Have', 'Are'], 2),
            q('PRONUNCIATION: in which word does a letter make the same sound as “ch” in “chair”?',
              ['nature', 'message', 'effortless', 'cinema'], 0),
            q('I need to explain something ___ her.', ['at', 'for', 'with', 'to'], 3),
            q('“From time to time” means …', ['all the time', 'occasionally', 'almost never', 'every hour'], 1),
            q('Which sentences are correct? (1) I paid credit card. (2) I paid with my card. (3) I paid by credit card.',
              ['Only 1', 'Only 2', '2 and 3', '1 and 2'], 2),
            q('“To be on time” means …', ['to be late', 'to be punctual', 'to be too early', 'to be absent'], 1),
            q('It depends ___ the case.', ['of', 'from', 'on', 'in'], 2),
            q('Choose the correct sentence.', ['He is a strange people.', 'He is a strange person.',
                                              'He are a strange person.', 'He is strange peoples.'], 1),
            q('I have lived here ___ 2010.', ['for', 'since', 'from', 'at'], 1),
            q('I travelled ___ Madrid by train yesterday — the journey took three hours.',
              ['at', 'in', 'on', 'to'], 3),
        ],
        recap=[
            ('r1', ['explain something TO someone', 'ask FOR something', 'it depends ON',
                    'travel TO a place', 'pay BY card / WITH my card']),
            ('r2', ['need TO + verb', 'he IS dead · he DIED', 'HAVE you read …? (experience)',
                    'SINCE 2010 · FOR ten years', 'a person · two people']),
            ('r3', ['explain, not explicate', 'from time to time = occasionally',
                    'on time = punctual', 'nature: the t sounds /tʃ/']),
        ],
        chips=['since', 'depends on', 'explain to', 'on time', 'need to', 'from time to time', 'by card'],
    ),
    2: dict(
        out='forbes-english-common-mistakes-review-part2.html',
        title='Common Mistakes Review — Part 2: False Friends (B1)',
        scheme='cool',
        palette=None,
        art={
            'p2-hero': ('people', 'two keys that look the same, one fits the lock and one does not'),
            'p2-talk': ('talk', 'two figures on a bench, one speech bubble between them'),
            'p2-a': ('words', 'an open dictionary drawn as a flat block with a ribbon bookmark'),
            'p2-b': ('build', 'a wedding ring, a geometry compass and a history book on a shelf'),
            'p2-act': ('pair', 'two seats at a café table with two cups'),
        },
        talk=[
            'Which English word looks like a word in your language but means something else?',
            'Have you ever said something embarrassing in English?',
            'Which prepositions do you find hardest?',
            'Are you good at remembering new words? What is your trick?',
            'What are you interested in at the moment?',
            'Who do you ask when you need to borrow something?',
        ],
        items=[
            q('“Actually, I’m not free tonight.” Here, “actually” means …',
              ['actualmente', 'en realidad', 'ahora mismo', 'en este momento'], 1),
            q('I felt very ___ when I forgot her name in front of everyone.',
              ['pregnant', 'embarrassed', 'embarrassing', 'ashamed of'], 1),
            q('I need to ___ the meeting tomorrow morning.', ['assist', 'attend', 'attend to', 'assist to'], 1),
            q('I didn’t ___ how late it was until I looked at my phone.',
              ['realize', 'remember', 'recall', 'remind'], 0),
            q('She is married ___ a doctor.', ['with', 'to', 'for', 'by'], 1),
            q('I’m really ___ history.', ['interested on', 'interested in', 'interested for', 'interested at'], 1),
            q('He’s very ___ maths.', ['good in', 'good at', 'good on', 'good for'], 1),
            q('Choose the correct sentence.', ['I do my homework and I make mistakes.',
                                              'I make my homework and I do mistakes.',
                                              'I make my homework and I make mistakes.',
                                              'I do my homework and I do mistakes.'], 0),
            q('PRONUNCIATION: which letter is silent in “island”?', ['i', 's', 'l', 'd'], 1),
            q('Can you ___ me some money? I’ll pay you back on Friday.',
              ['borrow', 'lend', 'loan me from', 'rent'], 1),
            q('Choose the correct sentence.', ['I am agree.', 'I agree.', 'I am agreeing with.', 'I do agreeing.'], 1),
            q('She’s a very ___ person: she never overreacts and always thinks things through.',
              ['sensitive', 'sensible', 'sensory', 'senseless'], 1),
            q('Which word means “at the present time”?', ['actually', 'currently', 'eventually', 'lately'], 1),
            q('I look forward to ___ from you soon.', ['hear', 'hearing', 'heard', 'to hear'], 1),
        ],
        recap=[
            ('r1', ['actually = in fact', 'currently = at the moment', 'embarrassed = avergonzado',
                    'attend a meeting · assist = help', 'sensible = showing good judgement',
                    'realize = understand suddenly']),
            ('r2', ['married TO', 'interested IN', 'good AT', 'look forward TO + -ing']),
            ('r3', ['DO homework · MAKE a mistake', 'LEND me · BORROW from you', 'I agree (not I am agree)',
                    'island: the s is silent']),
        ],
        chips=['interested in', 'look forward to hearing', 'attended', 'currently', 'lend', 'good at', 'actually'],
    ),
    3: dict(
        out='forbes-english-common-mistakes-review-part3.html',
        title='Common Mistakes Review — Part 3: Think Before You Choose (B1)',
        scheme='warm',
        palette=None,
        art={
            'p3-hero': ('idea', 'a hand hesitating between two doors, one open and one closed'),
            'p3-talk': ('talk', 'two speech bubbles above a film reel'),
            'p3-a': ('food', 'an empty plate, a fork and a wall clock at one o’clock'),
            'p3-b': ('film', 'one cinema seat and a tub of popcorn, the screen glowing'),
            'p3-act': ('pair', 'two stools at a counter with two cups'),
        },
        talk=[
            'What kind of music do you listen to while you work or cook?',
            'What is the best piece of advice anyone has given you?',
            'What makes a film boring, and what makes it interesting?',
            'How many people do you speak English with every week?',
            'What was the last thing you waited for for a long time?',
            'Where do you get your news from?',
        ],
        items=[
            q('Choose the correct sentence.', ['I have 25 years old.', 'I am 25 years old.',
                                              'I have 25 years.', 'I am having 25 years.'], 1),
            q('We arrived ___ the airport two hours early.', ['to', 'at', 'in', 'on'], 1),
            q('This restaurant is very different ___ the one we went to last week.',
              ['than', 'from', 'of', 'with'], 1),
            q('Let’s ___ the plan before we decide anything.',
              ['discuss about', 'discuss', 'discuss on', 'discuss of'], 1),
            q('Choose the correct sentence.', ['She gave me some advices.', 'She gave me some advice.',
                                              'She gave me an advices.', 'She gave me an advice.'], 1),
            q('How ___ people came to the party?', ['much', 'many', 'a lot', 'few'], 1),
            q('I’m really ___. Can we stop for lunch soon?', ['having hunger', 'hunger', 'hungry', 'with hunger'], 2),
            q('There were ___ people at the concert than we expected.', ['less', 'fewer', 'little', 'much'], 1),
            q('Look, that’s my dog ___ the photo!', ['at', 'on', 'in', 'to'], 2),
            q('I love to ___ music while I’m cooking.', ['listen', 'listen to', 'hear to', 'listen at'], 1),
            q('Could you ___ me outside the cinema? I’ll only be five minutes.',
              ['wait', 'wait for', 'wait to', 'hope'], 1),
            q('PRONUNCIATION: how many syllables does “comfortable” have in natural spoken English?',
              ['2', '3', '4', '5'], 1),
            q('This documentary is so ___! I fell asleep after ten minutes.', ['bored', 'boring', 'bore', 'to bore'], 1),
            q('Choose the correct sentence.', ['The news are terrible today.', 'The news is terrible today.',
                                              'The news were terrible today.', 'The news be terrible today.'], 1),
        ],
        recap=[
            ('r1', ['I AM 25 · I AM hungry', 'discuss the plan (no about)', 'listen TO · wait FOR']),
            ('r2', ['some advice (no -s, no a)', 'how MANY people · FEWER people', 'the news IS']),
            ('r3', ['arrive AT the airport · IN London', 'different FROM', 'IN the photo',
                    'boring (the thing) · bored (you)', 'comfortable: three syllables']),
        ],
        chips=['different from', 'some advice', 'arrived at', 'boring', 'fewer', 'how many', 'listen to'],
    ),
}

# Palettes: py lesson-template/extract-palette.py MistakesReview/standin-pN-hero.jpg --paper
# (2026-11-06, every row PASS). Re-derive when a real hero lands.
PALETTES = {
    1: '''
  --void          : #fcf9f9;
  --surface       : #f2e9e5;
  --surface2      : #f7f2f0;
  --border        : #d0a495;
  --text          : #231713;
  --text-dim      : #594640;
  --accent        : #c63100;
  --accent-bright : #9d2700;
  --accent-dim    : #eebbaa;
  --secondary     : #f0c06b;
  --contrast      : #096d56;''',
    2: '''
  --void          : #f9fafc;
  --surface       : #e5ebf2;
  --surface2      : #f0f3f7;
  --border        : #95add0;
  --text          : #231813;
  --text-dim      : #594840;
  --accent        : #b23600;
  --accent-bright : #892a00;
  --accent-dim    : #f0bea8;
  --secondary     : #f9fbfe;
  --contrast      : #096d5b;''',
    3: '''
  --void          : #fcfbf9;
  --surface       : #f2efe6;
  --surface2      : #f7f5f0;
  --border        : #cfbf96;
  --text          : #231e13;
  --text-dim      : #595140;
  --accent        : #865c00;
  --accent-bright : #5d4000;
  --accent-dim    : #f0d9a8;
  --secondary     : #282b38;
  --contrast      : #0b6b84;''',
}


# Where the key sits in the SOURCE: the engine shuffles on screen, but
# check-lesson's KEYS gate reads the source, and Part 2 had the key at B in
# 12 of 14. Moved, never reordered otherwise: a swap with the option at the
# target position.
DEAL = [2, 0, 3, 1, 0, 2, 1, 3, 2, 0, 1, 3, 0, 2]


def deal(it, i):
    o = list(it['options'])
    t = DEAL[i % len(DEAL)]
    c = it['correct']
    o[c], o[t] = o[t], o[c]
    return dict(it, options=o, correct=t)



# House style 1 (HOUSE-STYLE §000, 2026-11-09): one Midjourney plate per
# slide, his style images at --stylize 200. <part>-<slot>.jpg in
# MistakesReview/; the stand-ins are house style 2 only and are no longer used.
PLATES = {
    1: {
        'hero': 'a young woman at a café table puzzling over an English notebook, a phone beside her',
        'talk': 'two coffee cups on a small café table by a window',
        'q1': 'a woman explaining a drawing to a friend across a kitchen table',
        'q2': 'a customer raising a hand to ask a waiter something in a busy café',
        'q3': 'a hand holding a phone with a big glowing activation button',
        'q4': 'a dead houseplant with drooping brown leaves beside a watering can',
        'q5': 'a woman holding up a stack of novels by the same author',
        'q6': 'a green landscape of hills and trees, nature seen through a window',
        'q7': 'a man whispering a secret into a friend’s ear',
        'q8': 'a man glancing at a clock on the wall now and then while working',
        'q10': 'a woman arriving at a meeting room door exactly as the clock strikes nine',
        'q11': 'a person standing at a crossroads looking at two signposts',
        'q12': 'a man in an odd hat and mismatched clothes standing in a crowd',
        'q13': 'a cosy house with a garden and a tree that has grown tall over the years',
        'q14': 'a train crossing the Spanish plains towards Madrid',
        'results': 'an open notebook with corrections and a pencil on a café table',
    },
    2: {
        'hero': 'two people looking at each other’s reflections in a pair of mirrors, one surprised',
        'talk': 'two friends on a park bench talking',
        'q1': 'a woman politely shaking her head at an invitation on her phone in the evening',
        'q2': 'a man blushing red in front of a group of people at a party',
        'q3': 'a woman walking into a conference room with a coffee in the morning',
        'q4': 'a startled woman looking at her phone showing a late hour, dark outside',
        'q5': 'a wedding couple, the groom in a doctor’s white coat',
        'q6': 'a student absorbed in a big history book with ancient ruins drawn in it',
        'q7': 'a boy solving a maths problem on a blackboard with ease',
        'q9': 'a small island with one palm tree in a calm sea',
        'q10': 'one friend handing banknotes to another',
        'q12': 'a calm woman thinking carefully, a chess board in front of her',
        'q13': 'a woman checking the time on a big modern station clock',
        'q14': 'a person opening a letter by a window with a smile',
        'results': 'a pair of reading glasses on top of an open English dictionary',
    },
    3: {
        'hero': 'a thoughtful young man choosing between two doors in a bright corridor',
        'talk': 'a man cooking in a kitchen with a radio playing music',
        'q1': 'a birthday cake with candles on a table',
        'q2': 'travellers with suitcases arriving at an airport terminal',
        'q3': 'two restaurant fronts side by side, one fancy and one simple',
        'q4': 'colleagues discussing a plan around a table covered with papers',
        'q5': 'an older woman giving advice to a younger friend on a park bench',
        'q6': 'a crowded house party with people dancing',
        'q7': 'two hikers with empty stomachs looking at a restaurant sign',
        'q9': 'a framed photo of a dog on a shelf',
        'q10': 'a woman listening to music on headphones while cooking',
        'q11': 'a man waiting outside a cinema checking his watch',
        'q12': 'a big comfortable armchair in a sunny room',
        'q13': 'a man asleep on the sofa in front of a documentary on television',
        'q14': 'a person reading bad news in a newspaper at breakfast',
        'results': 'a pencil and an eraser on a corrected test paper',
    },
}
POP = {1: {'hero': (None, 'square'), 'q4': (None, 'free')},
       2: {'hero': (None, 'square'), 'q10': (None, 'blob')},
       3: {'hero': (None, 'square'), 'q12': (None, 'free')}}


def slides(n, spec, E):
    p = 'p%d-' % n
    K = hs1.Deck(F, pop={p + k: v for k, v in POP[n].items()}, hero=p + 'hero',
                 cover_name='pop-cover-p%d' % n, title_px=52, cover_w=44)
    s = [K.cover(E, [('Level', E['chipLevel']), ('Focus', E['chipFocus']), ('Count', E['chipCount'])]),
         K.frame(K.talk('eW', 'tkT', spec['talk'], E), p + 'talk')]
    K.stage()
    items = [deal(it, i) for i, it in enumerate(spec['items'])]
    D.assert_no_key_is_longest(items, 'part %d' % n)
    for i, it in enumerate(items, 1):
        it = dict(it, why='w%d' % i)
        slot = p + 'q%d' % i if 'q%d' % i in PLATES[n] else None
        sl = D.mc(i, len(items), it, 'eQ', E['eQ'], 'mcT', E['mcT'],
                  ctx=E['h%d' % i], ctx_key='h%d' % i)
        s.append(K.frame(sl, slot, text=(it['stem'] + ' ' + E['h%d' % i], it['options'])))
    # three recap cards: no room for a picture (texture field)
    s.append(D.rules('eR', E['eR'], 'recT', E['recT'],
                     [((k, E[k]), [(None, b) for b in bullets], None) for k, bullets in spec['recap']]))
    K.stage()
    s.append(K.frame(D.results(), p + 'results'))
    s.append(K.activation(D.activate(E['actTitle'], E['actUse'], spec['chips'], 'Speaking', E['actSpeakBrief'],
                        [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                        E['actWriteKind'], E['actWriteBrief'], E['actPlaceholder'])))
    return "".join(s), K


def build(only=None):
    for n, spec in PARTS.items():
        if only and n not in only:
            continue
        if not os.path.exists(os.path.join(F, 'p%d-hero.jpg' % n)):
            # its house style 1 art has not landed: leave the live page alone
            print('part %d: no p%d-hero.jpg yet, skipped' % (n, n))
            continue
        mod = I.module(n)
        body, K = slides(n, spec, mod.T['en'])
        K.assemble(spec['out'], body, spec['title'], mod, ('en', 'de', 'es'),
                   extra_css='html[data-style="editorial"] .slide:has(.q-ctx) .opt '
                             '{ padding-top: 7px; padding-bottom: 7px; }')


if __name__ == '__main__':
    build()
