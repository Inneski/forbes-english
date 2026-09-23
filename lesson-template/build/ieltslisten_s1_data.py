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

REVISED 2026-09-23 (IELTS audit):
  - The prices did not add up. Non-members paid thirty-five pounds and members
    forty-two, and joining "works out cheaper". Non-members now pay thirty-five
    a MONTH; members pay forty-two for the whole ten-week term.
  - The deck now plays the recording while the learner answers (see
    deck.audio, data-carry), so the questions follow the recording in order,
    as the real paper's do: the old "The course lasts" multiple-choice item,
    whose answer came in the middle of the form, is a form line (Question 5),
    and the three multiple-choice items are the three facts after the break.
  - Like the real Section 1 it pauses for reading time at the start and
    before Questions 8-10.
  - Speakers contract, as people do. The narrator does not.

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
     'look at questions one to seven.'),
    ('pause', 15),
    ('narrator', 'Now listen carefully and answer questions one to seven.'),

    ('gb_m', 'Good morning, Fairfield Community Centre, Douglas speaking.'),
    ('au_f', "Oh, good morning. I wanted to ask about the adult swimming "
             "classes, if that's all right."),
    ('gb_m', 'Of course. Have you been to the centre before at all?'),
    ('au_f', "No, never. I've just moved into the area."),
    ('gb_m', "Right, then I'll take a few details and set you up. Can I start "
             "with your name?"),
    ('au_f', "Yes, it's Petra. Petra Novakova."),
    ('gb_m', 'Petra. And how do you spell the surname?'),
    ('au_f', "It's N, O, V, A, K, O, V, A. Novakova."),
    ('gb_m', 'N, O, V, A, K, O, V, A. Thank you. And a contact number?'),
    ('au_f', "It's oh seven seven double oh, nine double oh, six four two."),
    ('gb_m', 'Let me read that back. Oh seven seven double oh, nine double oh, '
             'six four two. Is that right?'),
    ('au_f', "That's it, yes."),

    ('gb_m', "Lovely. Now, the adult beginners class runs on a Tuesday evening "
             "— sorry, I beg your pardon, that's the children. The adult class "
             "is Thursday."),
    ('au_f', 'Thursday. Good, that suits me better anyway.'),
    ('gb_m', "And it starts at six thirty, so if you can be poolside by twenty "
             "past, that's ideal."),
    ('au_f', 'Six thirty. Right.'),
    ('gb_m', "The course runs for ten weeks. For non-members it's thirty-five "
             "pounds a month, but as you're joining the centre you'd pay the "
             "member rate, which is forty-two pounds for the whole term."),
    ('au_f', "Sorry — forty-two for members, and that's for the whole term?"),
    ('gb_m', 'For the whole term, yes. It works out a lot cheaper.'),

    ('au_f', 'And is there anything I need to bring?'),
    ('gb_m', "Just the usual — a costume and a towel. The one thing people "
             "forget is a cap. You can't get in the water without a swimming "
             "cap, and we do sell them at reception."),
    ('au_f', "A cap. I'll write that down."),

    ('narrator',
     'Before you hear the rest of the conversation, you have some time to '
     'look at questions eight to ten.'),
    ('pause', 20),
    ('narrator', 'Now listen and answer questions eight to ten.'),

    ('gb_m', "We've got two pools, by the way. The classes are in the small "
             "pool, not the main one, so come through the side entrance."),
    ('au_f', 'The small pool, side entrance. And parking?'),
    ('gb_m', "There's a car park, but it fills up by six. Most people use the "
             "street behind the library — it's free after five."),
    ('au_f', "That's useful, thank you. Actually, can I ask — a friend "
             "mentioned the centre, but I also saw something in the local "
             "paper about the new pool."),
    ('gb_m', 'That would have been the refurbishment. We reopened in March.'),

    ('narrator',
     'That is the end of section one. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section1.mp3'

# ── Questions 1-7 · form completion ────────────────────────────────────
# The word limit on a real form task is ONE WORD AND/OR A NUMBER, and the
# answers here respect it — which is also why "half past six" is not in the
# accepted list: it is three words. The pipe form is the engine's list of
# accepted spellings.
FORM = [
    ('Surname: ______', ['Novakova|NOVAKOVA'],
     'Spelled out once, letter by letter. The moment a speaker starts giving '
     'letters, an answer is being dictated.'),
    ('Telephone: ______', ['07700900642|07700 900 642|07700-900-642'],
     '"Double oh" is two noughts and "oh" is one: 07700 900 642. A candidate '
     'waiting for eleven separate digits never hears eleven.'),
    ('Class day: ______', ['Thursday'],
     "He says Tuesday and corrects himself at once: \"sorry, I beg your "
     "pardon, that's the children.\" The answer is always the correction."),
    ('Starts at: ______',
     ['6.30|6:30|6.30pm|6.30 pm|6:30pm|6:30 pm|18.30|18:30'],
     'Six thirty. Twenty past is when to arrive poolside, which is the sort '
     'of nearby number that is put there to be written down by mistake.'),
    ('Length of course: ______ weeks', ['10|ten'],
     'Ten, said once, just before the prices. The member price that follows '
     'covers the same ten weeks &mdash; "the whole term".'),
    ('Cost for members: £______', ['42|42.00|forty-two'],
     'Thirty-five is said first, and it is the monthly rate for non-members. '
     'She is joining, so she pays forty-two for the whole term.'),
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

# Three, two and two a slide. Four rows plus the heading run past the canvas
# once the explanations show, and HOUSE-STYLE §6 is explicit that the answer
# is more slides rather than smaller type.
FORM_SLIDES = [FORM[:3], FORM[3:5], FORM[5:]]

# ── Questions 8-10 · multiple choice ───────────────────────────────────
# The three facts after the break, in the order they are heard.
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

    dict(stem='Why did the centre reopen in March?',
         options=['Because a friend of hers had recommended it.',
                  'Because the local paper had run a campaign.',
                  'Because the building had been refurbished.',
                  'Because the classes had grown too popular.'],
         correct=2, why='l4why'),
]
