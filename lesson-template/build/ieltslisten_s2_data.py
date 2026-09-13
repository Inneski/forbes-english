# -*- coding: utf-8 -*-
"""IELTS Listening Section 2 — the monologue and the map.

Section 2 is one speaker talking to a group: a tour guide, a manager showing
people round, a radio announcement about a local facility. Two things change
from Section 1 and both make it harder.

  1. **Nobody asks a question.** In Section 1 the second speaker keeps
     checking — "sorry, forty-two?" — and every check is a free repeat. A
     monologue never repeats itself, so a detail missed is a detail gone.
  2. **The map task arrives.** Labelling a plan is the one IELTS task that is
     not really about English at all: it is about holding an orientation in
     your head while somebody walks you through a space in words.

**WHY THIS DECK MATCHES INSTEAD OF LABELLING A MAP.** A real map task gives
you a drawn plan with letters on it, and we have no drawn plan — the artwork
for this lesson is photographic-style illustration, not a diagram with A to H
marked. Rather than fake it, the deck tests the same skill in the form it can
honestly support: five places, five positions, matched from the description.
That is exactly what a candidate does before they ever look at the letters,
and the teach card says plainly that the real paper hands you a map.

The recording is a garden tour, and the traps are the ones map tasks actually
use:

  * **a relative direction that depends on where you are standing** — "on your
    left as you come through the gate";
  * **a place mentioned and then moved** — the plant stall used to be by the
    lake and is now at the end of the long path;
  * **two things beside the same landmark**, so the landmark alone does not
    identify either.

One speaker, a New Zealand voice — a different accent from Section 1's pairing
on purpose, because the route should expose a learner to the spread the real
test uses rather than the same two voices five times.
"""

# ── the recording ──────────────────────────────────────────────────────
TURNS = [
    ('narrator',
     'Section two. You will hear a guide talking to a group of visitors at a '
     'public garden. First, you have some time to look at questions one to '
     'twelve.'),
    ('narrator', 'Now listen carefully and answer questions one to twelve.'),

    ('nz_f',
     'Good morning everyone, and welcome to Ashgrove Gardens. My name is '
     'Rowan and I will be showing you round this morning. Before we set off, '
     'let me give you the layout, because the grounds are bigger than they '
     'look from the entrance.'),
    ('nz_f',
     'You have all come in through the main gate. On your left, as you come '
     'through that gate, is the old glasshouse, and that is where the café is '
     'now. It was the ticket office until last year, so if you have an older '
     'leaflet it will tell you something different.'),
    ('nz_f',
     'Directly ahead of you is the lake. You cannot miss it. Behind the lake, '
     'on the far side from where we are standing, is the rose garden, and '
     'that is really the reason most people come in June.'),
    ('nz_f',
     'Now, the car park. If you drove here you will have parked to the east '
     'of the grounds, and right next to the car park is the children&rsquo;s '
     'play area. Two things beside the car park, in fact — the play area, and '
     'the bicycle racks.'),
    ('nz_f',
     'The clock tower is the tall building you can see over the hedge, and '
     'the toilets are underneath it. It is the only building with a clock, so '
     'it is the easiest landmark in the garden.'),
    ('nz_f',
     'One change to mention. The plant stall used to stand by the lake. It '
     'has moved — it is now right at the far end of the long path, beyond the '
     'greenhouse. People still walk to the lake looking for it, so I am '
     'saying it twice: the far end of the long path.'),

    ('nz_f',
     'A few practical things. The gardens are open from ten until half past '
     'five, every day except Monday. Entry is eight pounds, but there is no '
     'charge at all for anyone under sixteen.'),
    ('nz_f',
     'The tour takes about ninety minutes and we finish back at the café. If '
     'you want to stay on afterwards you are very welcome; your ticket lasts '
     'all day.'),
    ('nz_f',
     'Two warnings. The lower path, the one that runs along the stream, is '
     'closed at the moment — the bank is being repaired and it will be closed '
     'until the spring. And please do not feed the birds at the lake. I know '
     'it is tempting, but the bread is genuinely bad for them.'),
    ('nz_f',
     'Right. If you would like to follow me, we will start at the glasshouse '
     'and work our way round anticlockwise.'),

    ('narrator',
     'That is the end of section two. You now have half a minute to check '
     'your answers.'),
]

AUDIO = 'section2.mp3'

# ── Questions 1-5 · where things are ───────────────────────────────────
# The definition side is where the answer lives, so the terms are the places
# and the definitions are the positions — a candidate who held the orientation
# can place all five, and one who only remembers landmarks cannot separate the
# play area from the bicycle racks.
PLACES = [
    ('The café', 'In the old glasshouse, left of the main gate'),
    ('The rose garden', 'On the far side of the lake'),
    ('The play area', 'Beside the car park, east of the grounds'),
    ('The toilets', 'Underneath the clock tower'),
    ('The plant stall', 'At the far end of the long path'),
]

PLACES_WHY = ('Every one of these is given relative to something else, which '
              'is what a map task is. Two of them share a landmark &mdash; the '
              'play area and the bicycle racks are both beside the car park '
              '&mdash; so "next to the car park" on its own does not identify '
              'either, and the plant stall is described twice precisely '
              'because it has moved.')

# ── Questions 6-8 · complete the notes ─────────────────────────────────
NOTES = [
    ('Open until ______ every day except Monday',
     ['5.30|5:30|half past five|17.30|17:30'],
     'Ten until half past five. The closing time is the one asked for, and it '
     'arrives second in the same short sentence as the opening time.'),
    ('Entry: £______ (free under 16)',
     ['8|8.00|eight'],
     'Eight pounds. "No charge at all for anyone under sixteen" is the same '
     'sentence, and it is there so that a candidate half-listening writes '
     '"free".'),
    ('The tour lasts about ______ minutes',
     ['90|ninety'],
     'Ninety minutes. Not the opening hours, and not "all day" &mdash; which '
     'is how long the ticket lasts, said one line later.'),
]

NOTES_BANK = []

# ── Questions 9-12 · multiple choice ───────────────────────────────────
MC = [
    dict(stem='What has changed at the gardens recently?',
         options=['The glasshouse is a café rather than a ticket office.',
                  'The glasshouse is a ticket office rather than a café.',
                  'The main gate has been moved to the eastern side.',
                  'The rose garden has been replanted beside the lake.'],
         correct=0, why='m1why'),

    dict(stem='Why is the lower path closed?',
         options=['Because the birds beside it are being protected.',
                  'Because the bank of the stream is being repaired.',
                  'Because the plant stall has been moved on to it.',
                  'Because it floods every winter until the spring.'],
         correct=1, why='m2why'),

    dict(stem='What does the guide ask visitors not to do?',
         options=['Walk along the stream path beyond the greenhouse.',
                  'Take photographs inside the old glasshouse café.',
                  'Give any bread to the birds that live on the lake.',
                  'Leave the group before the tour reaches the café.'],
         correct=2, why='m3why'),

    dict(stem='What happens at the end of the tour?',
         options=['Visitors must leave the gardens within the next hour.',
                  'Visitors are taken back to the main gate and let out.',
                  'Visitors pay a second time if they stay in the gardens.',
                  'Visitors may stay on, because the ticket lasts all day.'],
         correct=3, why='m4why'),
]
