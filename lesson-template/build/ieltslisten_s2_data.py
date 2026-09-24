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
REVISED 2026-09-23 (IELTS audit): the script said "children&rsquo;s", and
edge-tts escapes its input, so the recording read the entity out (tts.py now
unescapes). The questions follow the recording in order, because the deck now
plays it while the learner answers: the old first multiple-choice item ("what
has changed?") repeated the café match and was answered in the first ten
seconds, so it gives way to the tour's route, the guide's last line. The
section pauses for reading time before Question 6, as the real Section 2
does. The guide contracts; the narrator does not.
"""

# ── the recording ──────────────────────────────────────────────────────
TURNS = [
    ('narrator',
     'Section two. You will hear a guide talking to a group of visitors at a '
     'public garden. First, you have some time to look at questions one to '
     'five.'),
    ('pause', 15),
    ('narrator', 'Now listen carefully and answer questions one to five.'),

    ('nz_f',
     "Good morning everyone, and welcome to Ashgrove Gardens. My name is "
     "Rowan and I'll be showing you round this morning. Before we set off, "
     "let me give you the layout, because the grounds are bigger than they "
     "look from the entrance."),
    ('nz_f',
     "You've all come in through the main gate. On your left, as you come "
     "through that gate, is the old glasshouse, and that's where the café is "
     "now. It was the ticket office until last year, so if you've got an "
     "older leaflet it'll tell you something different."),
    ('nz_f',
     "Directly ahead of you is the lake. You can't miss it. Behind the lake, "
     "on the far side from where we are standing, is the rose garden, and "
     "that's really the reason most people come in June."),
    ('nz_f',
     "Now, the car park. If you drove here you'll have parked to the east of "
     "the grounds, and right next to the car park is the children's play "
     "area. Two things beside the car park, in fact — the play area, and the "
     "bicycle racks."),
    ('nz_f',
     "The clock tower is the tall building you can see over the hedge, and "
     "the toilets are underneath it. It's the only building with a clock, so "
     "it's the easiest landmark in the garden."),
    ('nz_f',
     "One change to mention. The plant stall used to stand by the lake. It's "
     "moved — it's now right at the far end of the long path, beyond the "
     "greenhouse. People still walk to the lake looking for it, so I'm saying "
     "it twice: the far end of the long path."),

    ('narrator',
     'Before you hear the rest of the talk, you have some time to look at '
     'questions six to twelve.'),
    ('pause', 20),
    ('narrator', 'Now listen and answer questions six to twelve.'),

    ('nz_f',
     "A few practical things. The gardens are open from ten until half past "
     "five, every day except Monday. Entry is eight pounds, but there's no "
     "charge at all for anyone under sixteen."),
    ('nz_f',
     "The tour takes about ninety minutes and we finish back at the café. If "
     "you want to stay on afterwards you're very welcome; your ticket lasts "
     "all day."),
    ('nz_f',
     "Two warnings. The lower path, the one that runs along the stream, is "
     "closed at the moment — the bank is being repaired and it'll be closed "
     "until the spring. And please don't feed the birds at the lake. I know "
     "it's tempting, but the bread is genuinely bad for them."),
    ('nz_f',
     "Right. If you'd like to follow me, we'll start at the glasshouse and "
     "work our way round anticlockwise."),

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
              'is what a map task is. The play area shares its landmark with '
              'the bicycle racks &mdash; both are beside the car park &mdash; '
              'so on a real plan, where the racks would have a letter too, '
              '"next to the car park" on its own would not identify it. The '
              'plant stall is described twice precisely because it has '
              'moved.')

# ── Questions 6-8 · complete the notes ─────────────────────────────────
# The entry line said "(free under 16)" until 2026-09-25, which printed the
# very trap its explanation described; it now asks for the adult price.
NOTES = [
    ('Open until ______ every day except Monday',
     ['5.30|5:30|5.30pm|5.30 pm|5:30pm|5:30 pm|5.30 p.m.|5:30 p.m.|17.30|17:30'],
     'Ten until half past five. The closing time is the one asked for, and it '
     'arrives second in the same short sentence as the opening time.'),
    ('Adult entry: £______',
     ['8|8.00|eight|£8|£8.00'],
     'Eight pounds. The same sentence goes on to "no charge at all for anyone '
     'under sixteen", which is there to catch anyone who writes 0.'),
    ('The tour lasts about ______ minutes',
     ['90|ninety'],
     'Ninety minutes. Not the opening hours, and not "all day" &mdash; which '
     'is how long the ticket lasts, said one line later.'),
]

NOTES_BANK = []

# ── Questions 9-12 · multiple choice ───────────────────────────────────
MC = [
    dict(stem='What happens at the end of the tour?',
         options=['Visitors may stay on, because the ticket lasts all day.',
                  'Visitors are taken back to the main gate and let out.',
                  'Visitors pay a second time if they stay in the gardens.',
                  'Visitors must leave the gardens within the next hour.'],
         correct=0, why='m4why'),

    dict(stem='Why is the lower path closed?',
         options=['Because the birds beside it are being protected.',
                  'Because the bank of the stream is being repaired.',
                  'Because the plant stall has been moved on to it.',
                  'Because it floods every winter until the spring.'],
         correct=1, why='m2why'),

    dict(stem='What does the guide ask visitors not to do?',
         options=['Walk on the grass around the edge of the rose garden.',
                  'Take photographs inside the old glasshouse café.',
                  'Give any bread to the birds that live on the lake.',
                  'Leave the group before the tour reaches the café.'],
         correct=2, why='m3why'),

    dict(stem='How will the tour go round the gardens?',
         options=['Anticlockwise, starting at the rose garden.',
                  'Clockwise, starting at the old glasshouse.',
                  'Clockwise, starting from the rose garden.',
                  'Anticlockwise, starting at the glasshouse.'],
         correct=3, why='m5why'),
]
