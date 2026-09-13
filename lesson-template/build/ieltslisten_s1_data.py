# -*- coding: utf-8 -*-
"""IELTS Listening Section 1 — the recording script and the ten items.

Section 1 is always a transactional conversation between two speakers in an
everyday context, and it is always the easiest section on the paper. What it
punishes is not comprehension but **transcription**: spelling a surname you
have only heard, writing a phone number at speaking speed, and noticing when a
speaker corrects themselves.

So the script is built around the four traps that actually lose marks, and
every one of them is in the recording on purpose:

  1. **A spelled surname.** NOVAKOVA is given letter by letter, once.
  2. **A self-correction.** The manager says Tuesday and then corrects to
     Thursday. Candidates who write the first thing they hear lose the mark,
     and this is the single commonest Section 1 error.
  3. **A distractor price.** Forty-two pounds is the answer; thirty-five is
     said first and is explicitly the non-member rate.
  4. **A number said in the British way.** The phone number uses "double" and
     "oh", neither of which a candidate expecting digit-by-digit will catch.

The answers are all one or two words or a number, which is what the word limit
allows on a real form-completion task.

THE RECORDING IS GENERATED, like everything else here: `tts.py` turns TURNS
into `ielts-listen-s1/section1.mp3`. Change the script, re-run the builder,
and the audio and the answer key stay in step. Never edit the mp3.
"""

# ── the recording ──────────────────────────────────────────────────────
# Two speakers and a narrator. The caller is Australian and the manager is
# British, which is ordinary for the real test and stops the two voices
# blurring into each other.
TURNS = [
    ('narrator',
     'Section one. You will hear a telephone conversation between a woman and '
     'the manager of a community sports centre. First, you have some time to '
     'look at questions one to ten.'),
    ('narrator',
     'Now listen carefully and answer questions one to ten.'),

    ('gb_m', 'Good morning, Fairfield Community Centre, Douglas speaking.'),
    ('au_f', 'Oh, good morning. I wanted to ask about the adult swimming '
             'classes, if that is all right.'),
    ('gb_m', 'Of course. Have you been to the centre before at all?'),
    ('au_f', 'No, never. I have just moved into the area.'),
    ('gb_m', 'Right, then I will take a few details and set you up. Can I '
             'start with your name?'),
    ('au_f', 'Yes, it is Petra. Petra Novakova.'),
    ('gb_m', 'Petra. And how do you spell the surname?'),
    ('au_f', 'It is N, O, V, A, K, O, V, A. Novakova.'),
    ('gb_m', 'N, O, V, A, K, O, V, A. Thank you. And a contact number?'),
    ('au_f', 'It is oh seven seven double oh, nine double oh, six four two.'),
    ('gb_m', 'Let me read that back. Oh seven seven double oh, nine double oh, '
             'six four two. Is that right?'),
    ('au_f', 'That is it, yes.'),

    ('gb_m', 'Lovely. Now, the adult beginners class runs on a Tuesday '
             'evening — sorry, I beg your pardon, that is the children. The '
             'adult class is Thursday.'),
    ('au_f', 'Thursday. Good, that suits me better anyway.'),
    ('gb_m', 'And it starts at six thirty, so if you can be poolside by twenty '
             'past, that is ideal.'),
    ('au_f', 'Six thirty. Right.'),
    ('gb_m', 'The course is ten weeks. For non-members it is thirty-five '
             'pounds, but as you are joining the centre you would pay the '
             'member rate, which is forty-two pounds for the term.'),
    ('au_f', 'Sorry — forty-two for members, and that is for the whole term?'),
    ('gb_m', 'For the whole term, yes. It works out cheaper.'),

    ('au_f', 'And is there anything I need to bring?'),
    ('gb_m', 'Just the usual — costume and a towel. The one thing people '
             'forget is a cap. You cannot get in the water without a swimming '
             'cap, and we do sell them at reception.'),
    ('au_f', 'A cap. I will write that down.'),
    ('gb_m', 'We have two pools, by the way. The classes are in the small '
             'pool, not the main one, so come through the side entrance.'),
    ('au_f', 'The small pool, side entrance. And parking?'),
    ('gb_m', 'There is a car park, but it fills up by six. Most people use the '
             'street behind the library — it is free after five.'),
    ('au_f', 'That is useful, thank you. Actually, can I ask — a friend '
             'mentioned the centre, but I also saw something in the local '
             'paper about the new pool.'),
    ('gb_m', 'That would have been the refurbishment. We reopened in March.'),

    ('narrator',
     'That is the end of section one. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section1.mp3'

# ── Questions 1-6 · form completion ────────────────────────────────────
# The word limit on a real form task is ONE WORD AND/OR A NUMBER, and the
# answers here respect it. The pipe form is the engine's list of accepted
# spellings: a candidate who writes the number with or without the pound sign
# has heard it correctly either way.
FORM = [
    ('Surname: ______', ['Novakova|NOVAKOVA'],
     'Spelled out once, letter by letter. Nothing else in the recording '
     'spells anything, so the moment a speaker starts giving letters, that is '
     'an answer being dictated.'),
    ('Telephone: ______', ['07700900642|07700 900 642'],
     '"Double oh" is two noughts and "oh" is one. Written out, the number is '
     '07700 900 642 — and a candidate waiting for eleven separate digits will '
     'not have heard eleven.'),
    ('Class day: ______', ['Thursday'],
     'He says Tuesday and corrects himself in the same breath: "sorry, I beg '
     'your pardon, that is the children." The answer is always the correction, '
     'never the first thing said.'),
    ('Starts at: ______', ['6.30|6:30|half past six|6.30pm|18.30|18:30'],
     'Six thirty. Twenty past is when to arrive poolside, which is the sort '
     'of nearby number that is put there to be written down by mistake.'),
    ('Cost for members: £______', ['42|42.00|forty-two'],
     'Thirty-five is said first and is labelled as the non-member rate. She '
     'is joining, so she pays forty-two.'),
    ('Must bring a swimming ______', ['cap'],
     'Costume and towel are "the usual". The cap is the one he singles out as '
     'the thing people forget, and a Section 1 answer is nearly always the '
     'item that gets emphasised.'),
]

# NO WORD BANK, deliberately. A real form-completion task gives you nothing to
# choose from — you write what you heard — and a bank would turn a listening
# item into a matching item. `deck.gap()` takes an empty bank and renders no
# chip row, which is what we want.
FORM_BANK = []

# Three gaps a slide, not six. Six rows plus the heading runs past the canvas,
# and HOUSE-STYLE §6 is explicit that the answer is more slides rather than
# smaller type.
FORM_SLIDES = [FORM[:3], FORM[3:]]

# ── Questions 7-10 · multiple choice ───────────────────────────────────
# Keys rotated so they land at i % 4 rather than clustering.
MC = [
    dict(stem='Where do the adult classes take place?',
         options=['In the small pool, through the side entrance.',
                  'In the main pool, through the side entrance.',
                  'In the small pool, through the main entrance.',
                  'In the main pool, through the front reception.'],
         correct=0, why='l1why'),

    dict(stem='What does he advise about parking?',
         options=['The centre car park is free after five o&rsquo;clock.',
                  'The street behind the library is free after five.',
                  'There is no parking of any kind near the centre.',
                  'The car park is usually empty before six o&rsquo;clock.'],
         correct=1, why='l2why'),

    dict(stem='The course lasts',
         options=['six weeks, paid for by the single session.',
                  'one term, paid for by the single session.',
                  'ten weeks, paid for as one whole term.',
                  'ten months, paid for as one whole term.'],
         correct=2, why='l3why'),

    dict(stem='Why did the centre reopen in March?',
         options=['Because a friend of hers had recommended it.',
                  'Because the local paper had run a campaign.',
                  'Because the classes had grown too popular.',
                  'Because the building had been refurbished.'],
         correct=3, why='l4why'),
]
