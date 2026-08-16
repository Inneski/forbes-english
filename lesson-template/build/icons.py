# -*- coding: utf-8 -*-
"""Line-drawn objects for the `search` slide type.

Deliberately unlabelled and deliberately plain: the learner has to
recognise the thing itself, which is the whole point of the task, so an
icon that needs its caption to be readable is a failed icon. They are
drawn on a 100x100 grid in `currentColor` so they inherit the lesson's
palette like everything else, and they carry no fill, so they read on a
dark deck and a light one without a second version.

Verify by eye before shipping a set: `python3 -c "import icons;
icons.contact_sheet('sheet.svg')"` writes every icon to one file.
"""

_S = ('<svg viewBox="0 0 100 100" fill="none" stroke="currentColor" '
      'stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round" '
      'aria-hidden="true">%s</svg>')

_PATHS = {
    # ── cell ──────────────────────────────────────────────────────
    'spoon': '<ellipse cx="50" cy="27" rx="15" ry="19"/>'
             '<path d="M50 46 L50 88"/>',
    'cup':   '<path d="M26 30 L32 78 Q33 84 39 84 L61 84 Q67 84 68 78 L74 30 Z"/>'
             '<path d="M74 40 Q88 40 88 52 Q88 63 73 63"/>',
    'book':  '<path d="M24 22 L50 30 L76 22 L76 76 L50 84 L24 76 Z"/>'
             '<path d="M50 30 L50 84"/>',
    'soap':  '<rect x="22" y="40" width="56" height="34" rx="13"/>'
             '<circle cx="70" cy="26" r="6"/><circle cx="82" cy="38" r="4"/>',
    'towel': '<path d="M24 20 L76 20 L76 80 L24 80 Z"/>'
             '<path d="M24 34 L76 34"/><path d="M24 66 L76 66"/>'
             '<path d="M38 20 L38 34"/><path d="M62 66 L62 80"/>',
    'comb':  '<path d="M18 34 L82 34 L82 50 L18 50 Z"/>'
             '<path d="M25 50 L25 74"/><path d="M36 50 L36 74"/>'
             '<path d="M47 50 L47 74"/><path d="M58 50 L58 74"/>'
             '<path d="M69 50 L69 74"/><path d="M80 50 L80 74"/>',

    # ── corridor ──────────────────────────────────────────────────
    'torch': '<path d="M30 34 L54 34 L54 66 L30 66 Z"/>'
             '<path d="M54 26 L70 18 L70 82 L54 74 Z"/>'
             '<path d="M80 34 L92 28"/><path d="M80 50 L94 50"/>'
             '<path d="M80 66 L92 72"/>',
    'bucket': '<path d="M24 34 L34 80 L66 80 L76 34 Z"/>'
              '<path d="M24 34 L76 34"/>'
              '<path d="M30 34 Q50 4 70 34"/>',
    'key':   '<circle cx="30" cy="50" r="16"/><circle cx="30" cy="50" r="5"/>'
             '<path d="M46 50 L88 50"/><path d="M72 50 L72 66"/>'
             '<path d="M84 50 L84 64"/>',
    'ladder': '<path d="M32 14 L32 86"/><path d="M68 14 L68 86"/>'
              '<path d="M32 28 L68 28"/><path d="M32 46 L68 46"/>'
              '<path d="M32 64 L68 64"/><path d="M32 82 L68 82"/>',
    'pipe':  '<path d="M14 32 L58 32 Q74 32 74 48 L74 88"/>'
             '<path d="M14 56 L46 56 Q50 56 50 60 L50 88"/>'
             '<path d="M12 26 L12 62"/><path d="M44 88 L80 88"/>',
    'hammer': '<path d="M20 16 Q30 24 30 32 Q30 40 20 48 L74 48 Q80 48 80 40 '
              'L80 24 Q80 16 74 16 Z"/>'
              '<path d="M44 48 L44 92 Q50 96 56 92 L56 48"/>',

    # ── barber shop ───────────────────────────────────────────────
    'scissors': '<circle cx="30" cy="76" r="11"/><circle cx="70" cy="76" r="11"/>'
                '<path d="M38 68 L76 16"/><path d="M62 68 L24 16"/>',
    'brush': '<path d="M34 20 L66 20 Q70 20 70 26 L70 52 Q70 58 66 58 L34 58 '
             'Q30 58 30 52 L30 26 Q30 20 34 20 Z"/>'
             '<path d="M38 20 L38 8"/><path d="M46 20 L46 6"/>'
             '<path d="M54 20 L54 6"/><path d="M62 20 L62 8"/>'
             '<path d="M44 58 L44 90"/><path d="M56 58 L56 90"/>'
             '<path d="M44 90 Q50 96 56 90"/>',
    # ── workshop ──────────────────────────────────────────────────
    'coat':  '<path d="M38 20 L50 30 L62 20 L82 32 L76 52 L68 48 L68 84 L32 84 '
             'L32 48 L24 52 L18 32 Z"/><path d="M50 30 L50 84"/>',
    'boot':  '<path d="M32 14 L54 14 L54 54 Q54 62 62 66 L82 76 Q88 79 88 86 '
             'L32 86 Z"/><path d="M32 66 L60 66"/>',
    'saw':   '<path d="M34 26 L92 26 L92 44 L34 44 Z"/>'
             '<path d="M34 44 L40 54 L46 44 L52 54 L58 44 L64 54 L70 44 '
             'L76 54 L82 44 L88 54 L92 44"/>'
             '<path d="M34 22 Q16 22 12 32 Q8 44 18 50 L34 50"/>'
             '<path d="M22 32 L26 42"/>',

    # ── water ─────────────────────────────────────────────────────
    'paddle': '<path d="M16 10 Q36 6 44 22 Q50 34 40 42 Q28 50 18 40 Q8 30 16 10 Z"/>'
              '<path d="M40 42 L84 86"/>'
              '<path d="M74 94 L92 76"/>',
    'rope':  '<ellipse cx="46" cy="50" rx="32" ry="24"/>'
             '<ellipse cx="46" cy="50" rx="21" ry="15"/>'
             '<ellipse cx="46" cy="50" rx="10" ry="7"/>'
             '<path d="M76 58 Q90 68 84 82 Q80 92 68 90"/>',
    'candle': '<path d="M50 10 Q60 22 50 30 Q40 22 50 10 Z"/>'
              '<path d="M50 30 L50 40"/>'
              '<path d="M34 40 L66 40 L66 88 L34 88 Z"/>'
              '<path d="M34 54 L66 54"/>',
}


def icon(name):
    """The SVG for one object, ready to drop inside a .find button."""
    if name not in _PATHS:
        raise KeyError('no icon named %r — have %s' % (name, sorted(_PATHS)))
    return _S % _PATHS[name]


def contact_sheet(path='icons-sheet.svg', cols=6):
    """Every icon on one page, so a set can be judged by eye at once."""
    names = sorted(_PATHS)
    rows = (len(names) + cols - 1) // cols
    cell = 120
    out = ['<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
           'viewBox="0 0 %d %d" style="background:#12161a">'
           % (cols * cell, rows * cell, cols * cell, rows * cell)]
    for n, name in enumerate(names):
        x, y = (n % cols) * cell + 10, (n // cols) * cell + 6
        out.append('<g transform="translate(%d,%d)" stroke="#e8d9b8" fill="none" '
                   'stroke-width="4.5" stroke-linecap="round" '
                   'stroke-linejoin="round">%s</g>' % (x, y, _PATHS[name]))
        out.append('<text x="%d" y="%d" fill="#8fa0ad" font-size="11" '
                   'font-family="monospace" text-anchor="middle">%s</text>'
                   % (x + 50, y + 114, name))
    out.append('</svg>')
    open(path, 'w', encoding='utf-8').write('\n'.join(out))
    return path


if __name__ == '__main__':
    print(contact_sheet(), len(_PATHS), 'icons')
