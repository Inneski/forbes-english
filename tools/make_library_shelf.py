"""The library hero's shelf (library.html, #library-books).

Innes's photograph of a wooden bookcase (2000 x 1116) with six face-out
books on its middle shelf. The six are cleared off: the panelled back wall
just above them, whose grain runs upright, is stretched down over them,
lightly re-grained and shaded, with a contact shadow along the shelf. The
picture is then cropped to the whole width of the case, shelves above and
below included, and written as library-hub/bookcase-photo.webp. The page's
own six books (CSS 3D, spine out, revolving to their covers) stand on the
cleared shelf; the script prints where that is.

    py tools/make_library_shelf.py incoming/library-books/bookcase-photo.jpg library-hub [preview-dir]

The source picture is local only (incoming/ is gitignored).
"""
import sys
from PIL import Image, ImageDraw

src = Image.open(sys.argv[1]).convert('RGB')
out = sys.argv[2]
X0, X1 = 408, 1606          # the middle bay, inside its uprights
WALL, SHELF = 432, 756      # where the books' tops begin; the shelf they stand on
CROP = (0, 60, 2000, 930)   # the whole case: more of the shelf above, so its rail sits clear of the top line

# the wall: the same panelling, clean, from under the middle shelf (its grain
# runs upright, so it stretches upright without showing), feathered into the
# wall that already shows above the books, and darkened to the same light
from PIL import ImageEnhance
patch = src.crop((X0, 808, X1, 918)).resize((X1 - X0, SHELF - WALL + 40), Image.BICUBIC)
patch = ImageEnhance.Brightness(patch).enhance(0.86)
mask = Image.new('L', patch.size, 255)
md = ImageDraw.Draw(mask)
for y in range(40):
    md.line([(0, y), (patch.width, y)], fill=int(255 * y / 40))
src.paste(patch, (X0, WALL - 40), mask)
d = ImageDraw.Draw(src, 'RGBA')
for i in range(14):                                 # contact shadow at the back of the shelf
    d.line([(X0, SHELF - 1 - i), (X1, SHELF - 1 - i)], fill=(18, 9, 3, 80 - i * 5))

case = src.crop(CROP)
case.save(out + '/bookcase-photo.webp', quality=86, method=6)
if len(sys.argv) > 3:
    case.resize((case.width // 2, case.height // 2)).save(sys.argv[3] + '/bookcase-photo-preview.png')
W, H = case.size
print('size %d x %d' % (W, H))
print('shelf top %.2f%% of the height up from the bottom = %.2fcqw' % ((CROP[3] - SHELF) / H * 100, (CROP[3] - SHELF) / W * 100))
print('clear height %.2fcqw; bay %.1f%% to %.1f%%' % ((SHELF - 350) / W * 100, X0 / W * 100, X1 / W * 100))
