# -*- coding: utf-8 -*-
"""Make sailing-the-seas-countania/chart-clean.jpg from Codex's clean draft.

    py lesson-template/build/countania_clean.py

The draft (incoming/sea-charts/countable-chart-clean-draft.png, Codex,
2026-10-04) kept two harbour dots where the titles COUNTANIA and
UNCOUNTANIA stand on the labelled chart, at (145,956) and (1378,956). They
are not harbours, so they are painted out here, in code, rather than by
asking for another repaint (docs/GRAMMAR-MAPS-PLAN.md section 2).
"""
import cv2
import numpy as np

SRC = 'incoming/sea-charts/countable-chart-clean-draft.png'
OUT = 'sailing-the-seas-countania/chart-clean.jpg'
STRAY = [(145, 956), (1378, 956)]

im = cv2.imread(SRC)
mask = np.zeros(im.shape[:2], np.uint8)
for x, y in STRAY:
    cv2.circle(mask, (x, y), 10, 255, -1)
out = cv2.inpaint(im, mask, 7, cv2.INPAINT_TELEA)
cv2.imwrite(OUT, out, [cv2.IMWRITE_JPEG_QUALITY, 88, cv2.IMWRITE_JPEG_PROGRESSIVE, 1])
print('wrote', OUT)
