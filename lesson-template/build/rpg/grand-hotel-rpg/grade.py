"""Take the amber cast out of the Grand Hotel plates (Innes, 2026-10-03:
"grade the colours so the yellow isnt so yellow").

    py lesson-template/build/rpg/grand-hotel-rpg/grade.py <raw.webp> …   # prints the cast

The plates in block-camp/grand-hotel-rpg/ were written with grade(im) at the
defaults below, then saved WEBP quality 84. `wb` is the one knob: 0.55 of the
plate's own cast removed.

A per-image partial white balance in Lab (shift a*/b* toward neutral by the
image's own mean cast, weighted to midtones so lamps stay warm), then a
saturation pull on the yellow-orange hue band only.
"""
import sys, numpy as np, cv2

def grade(rgb, wb=0.55, sat=0.80, keep_hi=0.6):
    f = rgb.astype(np.float32) / 255.0
    lab = cv2.cvtColor(f, cv2.COLOR_RGB2Lab)          # L 0..100, a/b ~ -127..127
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    # the cast: chroma mean over midtones (exclude lamps and shadows)
    m = (L > 20) & (L < 80)
    ma, mb = float(a[m].mean()), float(b[m].mean())
    # weight: full in mids, tapering to (1-keep_hi) in highlights so bulbs stay warm
    w = np.clip(1.0 - keep_hi * np.clip((L - 70) / 30, 0, 1), 0, 1)
    w *= np.clip(L / 15, 0, 1)                        # leave deep blacks alone
    a2 = a - wb * 0.5 * ma * w
    b2 = b - wb * mb * w
    # desaturate the yellow/orange band (hue 40..100 deg in Lab ab-plane)
    h = np.degrees(np.arctan2(b2, a2)) % 360
    band = np.clip(1 - np.abs(h - 70) / 40, 0, 1)
    k = 1 - (1 - sat) * band
    a2 *= k; b2 *= k
    out = cv2.cvtColor(np.dstack([L, a2, b2]).astype(np.float32), cv2.COLOR_Lab2RGB)
    return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8), (ma, mb)

if __name__ == '__main__':
    from PIL import Image
    for src in sys.argv[1:]:
        im = np.array(Image.open(src).convert('RGB'))
        g, cast = grade(im)
        print(src, 'cast a=%.1f b=%.1f' % cast, 'mean before', im.reshape(-1, 3).mean(0).round(), 'after', g.reshape(-1, 3).mean(0).round())
