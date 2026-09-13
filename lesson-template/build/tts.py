# -*- coding: utf-8 -*-
"""Turn a scripted conversation into one mp3, the way the Listening decks need.

Innes chose synthetic voices for the IELTS Listening recordings on 2026-09-13.
This is the tool that makes them, and like every other asset on this site the
audio is GENERATED: the script lives in a Python module, this turns it into a
file, and re-running it reproduces the recording exactly. Never hand-edit an
mp3 in the lesson folder — change the script and run the builder again.

WHY edge-tts AND NOT THE VOICES ALREADY ON THE MACHINE. Windows SAPI offers
three voices here — Hazel (en-GB), Zira (en-US) and Hedda (de-DE). Two usable
English voices, both female, both the old concatenative desktop quality. A
Section 1 conversation needs two speakers and Section 3 needs three, so SAPI
cannot cast a single one of these recordings, let alone give the spread of
accents the real test uses. `pip install edge-tts` brings free neural voices
in British, Australian, New Zealand, Irish, Canadian and American English,
male and female, with no API key. That is what IELTS sounds like.

HOW THE PIECES ARE JOINED. edge-tts writes CBR MPEG-1 Layer III, and such
files concatenate byte-for-byte: the frames of the second file are simply the
next frames of the stream. Verified rather than assumed — 217 frames plus 244
frames came back as 461, and 5.21s + 5.86s as 11.06s. So there is no encoder
here, no ffmpeg, and no dependency beyond edge-tts itself.

Usage from a builder:

    import tts
    tts.render(TURNS, 'ielts-listen-s1/section1.mp3')

where TURNS is a list of (voice_key, text). Voice keys are the short names in
VOICES below, so a script reads as a cast list rather than as a pile of
Microsoft voice ids.
"""
import asyncio
import os
import subprocess
import sys
import tempfile

# The cast. Short keys so a script reads as dialogue, and a spread of accents
# because that is what the test does: British, Australian, New Zealand, Irish
# and North American all appear in real papers.
VOICES = {
    'narrator':  'en-GB-SoniaNeural',      # the exam narrator is always RP
    'gb_m':      'en-GB-ThomasNeural',
    'gb_f':      'en-GB-LibbyNeural',
    'gb_m2':     'en-GB-RyanNeural',
    'au_f':      'en-AU-NatashaNeural',
    'au_m':      'en-AU-WilliamMultilingualNeural',
    'nz_f':      'en-NZ-MollyNeural',
    'nz_m':      'en-NZ-MitchellNeural',
    'ie_m':      'en-IE-ConnorNeural',
    'ca_f':      'en-CA-ClaraNeural',
    'us_f':      'en-US-AriaNeural',
    'us_m':      'en-US-GuyNeural',
}

# The exam voice is unhurried. Neural voices default faster than an IELTS
# recording, and a candidate writing an answer while listening needs the
# slower pace; -8% lands close to the real thing without sounding dragged.
RATE = '-8%'


def _synth(voice, text, out, rate=RATE):
    """One turn. Shells out to the edge-tts CLI rather than using the library
    directly: the CLI handles its own asyncio loop, which keeps this callable
    from a plain synchronous builder without an event-loop dance."""
    # --rate=-8% and NOT --rate -8%: a value starting with a minus is read as
    # the next flag by argparse, and the CLI dies with "expected one argument".
    cmd = [sys.executable, '-m', 'edge_tts', '--voice', voice,
           '--rate=' + rate, '--text', text, '--write-media', out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0 or not os.path.exists(out) or os.path.getsize(out) < 500:
        raise RuntimeError('edge-tts failed for %s: %s'
                           % (voice, (r.stderr or r.stdout)[-300:]))


def duration(path):
    """Seconds, read from the MPEG frame headers.

    There is no ffmpeg on this machine and no reason to add one. Walking the
    frames is exact for CBR and is what proves a joined file really is the sum
    of its parts."""
    BR = {1: [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 0],
          2: [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160, 0]}
    SR = {1: [44100, 48000, 32000, 0], 2: [22050, 24000, 16000, 0],
          0: [11025, 12000, 8000, 0]}
    d = open(path, 'rb').read()
    i, total = 0, 0.0
    if d[:3] == b'ID3':
        i = 10 + (d[6] << 21 | d[7] << 14 | d[8] << 7 | d[9])
    while i < len(d) - 4:
        if d[i] == 0xFF and (d[i + 1] & 0xE0) == 0xE0:
            ver = 1 if (d[i + 1] >> 3) & 3 == 3 else (2 if (d[i + 1] >> 3) & 3 == 2 else 0)
            layer = (d[i + 1] >> 1) & 3
            br_i, sr_i, pad = (d[i + 2] >> 4) & 0xF, (d[i + 2] >> 2) & 3, (d[i + 2] >> 1) & 1
            if ver and layer == 1 and br_i not in (0, 15) and sr_i != 3:
                spf = 1152 if ver == 1 else 576
                flen = int((spf // 8) * BR[ver][br_i] * 1000 // SR[ver][sr_i]) + pad
                if flen > 4:
                    total += spf / SR[ver][sr_i]
                    i += flen
                    continue
        i += 1
    return total


def render(turns, out_path, rate=RATE):
    """turns: list of (voice_key, text). Writes one mp3 and returns its length.

    The gap between turns is whatever leading and trailing silence the voice
    itself supplies — roughly a third of a second, which is about what two
    people leave each other. No artificial pause is inserted, because there is
    no encoder here to make one and the natural padding sounds better than a
    splice would.
    """
    os.makedirs(os.path.dirname(out_path) or '.', exist_ok=True)
    parts = []
    with tempfile.TemporaryDirectory() as tmp:
        for n, (who, text) in enumerate(turns):
            voice = VOICES.get(who, who)
            p = os.path.join(tmp, '%03d.mp3' % n)
            _synth(voice, text, p, rate)
            parts.append(p)
        with open(out_path, 'wb') as f:
            for p in parts:
                f.write(open(p, 'rb').read())
        # A joined file whose length is not the sum of its parts means the
        # frames did not line up, and the deck would ship a recording that
        # stops early — silently, because the player reads its duration from
        # the same broken stream. Checked here while the parts still exist.
        want = sum(duration(p) for p in parts)
    secs = duration(out_path)
    assert abs(secs - want) < 0.25, (
        '%s is %.2fs but its %d parts total %.2fs — the frames did not join'
        % (out_path, secs, len(parts), want))
    print('  %s — %d turns, %d:%02d, %d KB'
          % (out_path, len(turns), int(secs // 60), int(secs % 60),
             os.path.getsize(out_path) // 1024))
    return secs
