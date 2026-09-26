# -*- coding: utf-8 -*-
"""The pictures on the six plates at the top of library.html.

    python3 tools/build_hubs.py             # runs this with the other hubs
    python3 tools/build_library_plates.py   # just the pictures

library.html is hand-kept, and its hero band shows one plate per hub —
Sherpa Tensing, IELTS Academic, Block Camp, the role-playing games,
Grammar, and Work With Me (Innes, 2026-09-26: *"RPGS deserves an equal
button with IELTS, Block Camp & Sherpa ... Grammar has it's own cool hub
now ... Work with me is important"*). Each plate wears its hub's own
hero, so a plate and the page it opens show the same picture. The
sources are imported from the hub builders where they own them, so a
change of hero there reaches the library on the next build_hubs.

The copies are fixed-name web-sized JPEGs in `library-hub/`, because the
page that references them is hand-kept and a hashed name would put a
generated fence into it. PIL's encoder is deterministic: a rebuild from
the same source writes nothing. (A changed source keeps its name, so a
CDN may hold the old plate for a while; a rare event, accepted.)
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import seo                                   # noqa: E402

ROOT = seo.ROOT
ART = 'library-hub'
WIDTH, QUALITY = 800, 80


def sources():
    import build_grammar_hub
    import build_ielts_hub
    import build_rpg_hub
    return [
        ('sherpa', build_grammar_hub.SHERPA_ART),
        ('ielts', build_ielts_hub.HERO_SRC),
        ('block-camp', build_grammar_hub.BLOCKCAMP_ART),
        ('rpg', build_rpg_hub.HERO),
        ('grammar', build_grammar_hub.HERO),
        # The front page's own reader, for the plate that is about lessons
        # with Innes rather than a collection.
        ('work', 'HOUSE STYLE/blackisler_cool_female_student_studying_at_home_with_books_'
                 'No_f252909d-c97d-494b-b5b6-596be1e11502_2.png'),
    ]


def build(quiet=False):
    from PIL import Image
    os.makedirs(os.path.join(ROOT, ART), exist_ok=True)
    written = []
    for name, src_rel in sources():
        src = os.path.join(ROOT, src_rel)
        im = Image.open(src).convert('RGB')
        if im.width > WIDTH:
            im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=QUALITY, optimize=True, progressive=True)
        out = os.path.join(ROOT, ART, name + '.jpg')
        if not os.path.exists(out) or open(out, 'rb').read() != buf.getvalue():
            open(out, 'wb').write(buf.getvalue())
            written.append(name)
    if not quiet:
        print('  library-hub/: %d plates%s' % (len(sources()),
              ', wrote %s' % ', '.join(written) if written else ', all current'))
    return written


if __name__ == '__main__':
    build()
