#!/usr/bin/env python3
"""Regenerate fonts/Monocraft-{Regular,Bold}.woff2 from the Monocraft v4 TTC.

    python3 lesson-template/build/rpg/subset_monocraft.py Monocraft.ttc

Only needed if the glyph set has to grow (say, Cyrillic for a Russian gloss).
Add the code points to UNICODES and re-run; rpg.py picks the files up."""
import os, sys
from fontTools.ttLib import TTCollection
from fontTools import subset

HERE = os.path.dirname(os.path.abspath(__file__))
UNICODES = (list(range(0x20, 0x7f)) + list(range(0xa0, 0x180)) +
            list(range(0x2000, 0x2070)) +
            [0x20ac, 0x2122, 0x2190, 0x2191, 0x2192, 0x2193, 0x2212, 0x25c6,
             0x25c7, 0x2665, 0x2661, 0x2b1b, 0x2b1c, 0x2726, 0x2727, 0x2605,
             0x2606, 0x2b50, 0x2714, 0x2716, 0x00d7, 0x2022, 0x25cf, 0x25cb,
             0x25a0, 0x25a1, 0x2588, 0x2591, 0x2592, 0x2593, 0x25b6, 0x25c0,
             0x25b2, 0x25bc, 0x2b06, 0x2b07, 0x21e7, 0x23f5, 0x23f4, 0x2b1a,
             0x270e, 0x2691, 0x2690, 0x1f512])
FACES = {'Regular': 'Regular', 'Bold': 'Bold'}   # subfamily name -> file suffix

def main(ttc):
    coll = TTCollection(ttc)
    for f in coll.fonts:
        sub = f['name'].getDebugName(2)
        if sub not in FACES:
            continue
        cmap = f.getBestCmap()
        have = [u for u in UNICODES if u in cmap]
        opts = subset.Options()
        opts.flavor = 'woff2'; opts.layout_features = ['*']; opts.name_IDs = ['*']
        s = subset.Subsetter(opts); s.populate(unicodes=have); s.subset(f)
        f.flavor = 'woff2'
        out = os.path.join(HERE, 'fonts', 'Monocraft-%s.woff2' % FACES[sub])
        f.save(out)
        print('%s: %d glyphs, %d bytes' % (out, len(have), os.path.getsize(out)))

if __name__ == '__main__':
    main(sys.argv[1])
