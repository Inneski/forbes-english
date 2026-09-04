#!/usr/bin/env python3
"""Lift the Memory Vault scenes out of the dark - once, mechanically.

Innes, on the first previews of the past perfect trio: "it all looks very
dark". Measured, not felt: the 41 Vault scenes averaged 16/255 in luminance
(min 11, max 26) against 88-158 for the other five reference sets, and the
deck template then dims a background to 72% on top of that. No text plate
would have saved it.

The lift is one curve on every scene: gain 1.15 then gamma 0.5, which takes
the set to a mean of 59 (min 47, max 74) - still a night-time set, now with
the brick, the banners and the water readable. Applied to the 1280x720 files
from the Vault (the originals are in Innes's V3 file, not in the repo), and
written back over past-perfect-time-signals/bg01-41.jpg at quality 90.

    python3 lesson-template/camp/lift_scenes.py <folder-of-original-jpgs>
"""
import glob, os, sys
import numpy as np
from PIL import Image

GAIN, GAMMA = 1.15, 0.5
SRC = sys.argv[1]
DST = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'past-perfect-time-signals')

for p in sorted(glob.glob(os.path.join(SRC, 'bg*.jpg'))):
    im = Image.open(p).convert('RGB')
    if im.size != (1280, 720):
        im = im.resize((1280, 720), Image.LANCZOS)
    a = np.asarray(im).astype(np.float32) / 255
    a = np.clip(a * GAIN, 0, 1) ** GAMMA
    out = Image.fromarray((a * 255 + 0.5).astype(np.uint8))
    out.save(os.path.join(DST, os.path.basename(p)), quality=88, optimize=True)
    print(os.path.basename(p))
