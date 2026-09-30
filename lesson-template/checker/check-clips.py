#!/usr/bin/env python3
"""Check the correct-answer clips in the Block Camp decks.

A clip plays once on a right answer and then HOLDS ITS LAST FRAME behind the
slide. A clip that ends on a fade to black therefore leaves the slide black.
That shipped on 2026-09-30 (Past Simple slide 17, "I left the village...":
brightness 131 -> 24 over its last 20 frames) and Innes found it on his
laptop. Cut such a clip before the fade (ffmpeg -t) when encoding it.

For every data-clip / data-clip-loop / data-clip-high in blockcamp-*.html:
  - the file exists;
  - its last frame is not a fade: FAIL if the final frame is under 45% of the
    brightest frame in its last two seconds and darker than 60/255, or under
    15/255 outright. A clip that is dark all the way through (a night scene)
    passes, because it does not drop.
Also checks that every data-bg picture exists.

    py lesson-template/checker/check-clips.py            # all decks
    py lesson-template/checker/check-clips.py deck.html  # some
"""
import glob, os, re, subprocess, sys
import numpy as np
import imageio_ffmpeg

ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
FF = imageio_ffmpeg.get_ffmpeg_exe()


def tail_brightness(path):
    out = subprocess.run([FF, '-v', 'error', '-sseof', '-2', '-i', path, '-vf',
                          'fps=12,scale=32:18,format=gray', '-f', 'rawvideo', '-'],
                         capture_output=True).stdout
    a = np.frombuffer(out, np.uint8)
    return a.reshape(-1, 18, 32).mean(axis=(1, 2)) if a.size else np.array([])


def main(argv):
    decks = argv or sorted(glob.glob(os.path.join(ROOT, 'blockcamp-*.html')))
    fails, clips = 0, {}
    for deck in decks:
        s = open(os.path.join(ROOT, os.path.basename(deck)) if not os.path.isabs(deck) else deck,
                 encoding='utf-8').read()
        name = os.path.basename(deck)
        s = re.sub(r'<!--.*?-->', '', s, flags=re.S)       # the template documents data-bg in a comment
        tags = re.findall(r'<section class="slide"[^>]*>', s)
        for pic in set(m for t in tags for m in re.findall(r'data-bg="([^"]+)"', t)):
            if not os.path.exists(os.path.join(ROOT, pic)):
                print(f'FAIL {name}: picture missing: {pic}'); fails += 1
        for attr in [m for t in tags for m in re.findall(r'data-clip(?:-loop|-high)?="([^"]+)"', t)]:
            for c in attr.split():
                clips.setdefault(c, set()).add(name)
    for c, users in sorted(clips.items()):
        p = os.path.join(ROOT, c)
        if not os.path.exists(p):
            print(f'FAIL {c}: missing (used by {", ".join(sorted(users))})'); fails += 1
            continue
        b = tail_brightness(p)
        if not b.size:
            print(f'FAIL {c}: could not decode'); fails += 1
            continue
        end, peak = float(b[-1]), float(b.max())
        if end < 15 or (end < 60 and end < 0.45 * peak):
            print(f'FAIL {c}: ends on a fade ({peak:.0f} -> {end:.0f}); the slide would hold a dark frame '
                  f'(used by {", ".join(sorted(users))})')
            fails += 1
    print(f'{len(clips)} clips in {len(decks)} decks: ' + ('PASS' if not fails else f'{fails} FAIL'))
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
