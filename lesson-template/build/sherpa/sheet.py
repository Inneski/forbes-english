# -*- coding: utf-8 -*-
"""Tile a folder of slide screenshots into one contact sheet.

    py lesson-template/build/sherpa/sheet.py <dir> <out.png> [cols] [width]
"""
import os
import sys

from PIL import Image

d, out = sys.argv[1], sys.argv[2]
cols = int(sys.argv[3]) if len(sys.argv) > 3 else 4
tw = int(sys.argv[4]) if len(sys.argv) > 4 else 480
files = sorted(f for f in os.listdir(d) if f.endswith('.png'))
th = int(tw * 9 / 16)
rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols * tw + (cols + 1) * 8, rows * th + (rows + 1) * 8), (40, 40, 40))
for i, f in enumerate(files):
    im = Image.open(os.path.join(d, f)).convert('RGB').resize((tw, th), Image.LANCZOS)
    r, c = divmod(i, cols)
    sheet.paste(im, (8 + c * (tw + 8), 8 + r * (th + 8)))
sheet.save(out)
print(out, sheet.size, len(files), 'slides')
