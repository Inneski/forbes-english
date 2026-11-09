"""Cut a render's subject out of its background, for an HS2 picture zone.

HS2's zone is built for transparent cut-outs: an opaque square render lands
on the white page as a boxed sticker (HANDOFF, Comeback Ride, 2026-11-08).
Midjourney with --sref to a screen-print plate paints a full scene whatever
the prompt says about "plain background", so the subject is lifted out here.

    py tools/cut_subject.py <render.png> <Folder/slot.png> [--height 900]

rembg (isnet-general-use, the same model as tools/pop_plate.py) gives the
mask; small specks are dropped, the edge is feathered by one pixel, and the
image is trimmed to the subject with a small margin. The output is a PNG
with alpha, which deck.plate() treats as a cut-out.
Run from the repo root.
"""
import argparse

import numpy as np
from PIL import Image, ImageFilter


def cut(src, dst, height=900, margin=12):
    from rembg import new_session, remove
    im = Image.open(src).convert('RGB')
    m = remove(im, session=new_session('isnet-general-use'), only_mask=True)
    a = np.array(m.convert('L')).astype(np.float32)
    a[a < 24] = 0                                  # specks and haze
    try:
        from scipy import ndimage
        lab, n = ndimage.label(a > 128)
        if n > 1:
            sizes = ndimage.sum(np.ones_like(a), lab, range(1, n + 1))
            keep = np.isin(lab, [i + 1 for i, s in enumerate(sizes)
                                 if s >= 0.01 * sizes.max()])
            grown = ndimage.binary_dilation(keep, iterations=6)
            a[~grown] = 0
    except ImportError:
        pass
    alpha = Image.fromarray(a.astype(np.uint8)).filter(ImageFilter.GaussianBlur(0.8))
    out = im.convert('RGBA')
    out.putalpha(alpha)
    box = alpha.point(lambda v: 255 if v > 16 else 0).getbbox()
    if not box:
        raise SystemExit('no subject found in %s' % src)
    l, t, r, b = box
    out = out.crop((max(0, l - margin), max(0, t - margin),
                    min(im.width, r + margin), min(im.height, b + margin)))
    if out.height > height:
        out = out.resize((round(out.width * height / out.height), height), Image.LANCZOS)
    out.save(dst, optimize=True)
    cover = (np.array(out)[..., 3] > 128).mean()
    print('%s -> %s  %dx%d  subject %.0f%% of box' % (src, dst, out.width, out.height, cover * 100))


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('src')
    ap.add_argument('dst')
    ap.add_argument('--height', type=int, default=900)
    a = ap.parse_args()
    cut(a.src, a.dst, a.height)
