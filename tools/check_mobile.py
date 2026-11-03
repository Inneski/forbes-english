#!/usr/bin/env python3
"""Does every page still work on a phone?

    py tools/check_mobile.py            # exits non-zero on a failure
    py tools/check_mobile.py -v         # name every page it looked at

A static gate, not a browser one, so it runs in a cloud session where the
live site and a real viewport are both out of reach. It checks the three
things that were actually broken on 2026-10-29, each of which is a property
of the file rather than of a rendering:

  1. A DECK carries flow mode. Below a 0.62 fit the 1280x720 stage is drawn
     at 0.28 on a phone -- 5.3px body text -- so fitStage() must set
     `is-flow` and the page must carry the stylesheet that reads it. A
     builder re-run picks both up from lesson-template.html; a deck built
     before 2026-10-29 gets them from tools/mobile.py. Either way the file
     has to end up with both, and this is what notices when it does not.

  2. An RPG pins the way on. The panel is a translucent sheet over a
     painting with no scrollbar a learner will see; on the Kraken at 360x560
     the NEXT button sat 276px below the fold of it. So the sheet's last
     action must be `position:sticky` on a phone, and the scroll that puts
     the verdict on screen must not be the single-requestAnimationFrame one
     that measured the panel at its old height and moved nothing.

  3. EVERY page says it is for a phone at all -- one <meta name="viewport">.

It cannot tell you a slide is ugly. Run the pages at 360x560 for that; what
this catches is the regression, which is a page quietly losing the fix when
its builder is run again.
"""
import io, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = ('.claude', 'node_modules', 'docs', 'incoming', 'lesson-template')

G, R, Y, Z = '\033[32m', '\033[31m', '\033[33m', '\033[0m'
if os.name == 'nt' and not os.environ.get('WT_SESSION'):
    try:
        import ctypes
        ctypes.windll.kernel32.SetConsoleMode(
            ctypes.windll.kernel32.GetStdHandle(-11), 7)
    except Exception:
        G = R = Y = Z = ''


def pages():
    for pat in ('*.html', '*/*.html'):
        for p in sorted(glob.glob(os.path.join(ROOT, pat))):
            rel = os.path.relpath(p, ROOT).replace('\\', '/')
            if rel.split('/')[0] in SKIP_DIRS:
                continue
            yield rel, p


def main():
    verbose = '-v' in sys.argv
    fails, decks, rpgs, total = [], 0, 0, 0

    for rel, path in pages():
        try:
            s = io.open(path, encoding='utf-8', newline='').read()
        except Exception as e:
            fails.append((rel, 'unreadable: %s' % e))
            continue
        total += 1
        bad = []

        # 3. every page
        if len(re.findall(r'<meta[^>]+name=["\']viewport["\']', s)) != 1:
            bad.append('no single <meta name="viewport">')

        # 1. decks
        if 'fitStage' in s and 'class="stage"' in s:
            decks += 1
            if "classList.toggle('is-flow'" not in s:
                bad.append("fitStage() does not set is-flow -- run tools/mobile.py")
            if 'html.is-flow .stage' not in s:
                bad.append('no flow-mode stylesheet -- run tools/mobile.py')
            # the transform has to be cleared, or the page scrolls a scaled stage
            if "if (phone) { stage.style.transform = ''; return; }" not in s:
                bad.append('fitStage() still scales the stage on a phone')
            # a turned phone changes which layout the deck is in, not just its
            # scale, so the one resize listener is doubled up
            if 'orientationchange' not in s:
                bad.append('no orientationchange listener -- run tools/mobile.py')

        # 2. RPGs
        if 'function closePanel(' in s and 'id="content"' in s:
            # the descent map carries the panel helpers but has no question
            # sheet of its own; it is a route map, and has nothing to pin.
            if 'class="option"' in s or "class=\\\"option" in s or 'optMarkup' in s:
                rpgs += 1
                if '.content>.continue:last-child' not in s:
                    bad.append('the panel does not pin its last action on a phone')
                if 'requestAnimationFrame(fitPanel)}' in s:
                    bad.append('still scrolls with one requestAnimationFrame (see rpg.py)')
                if '--sheet-pad' not in s:
                    bad.append('no --sheet-pad: the pinned bar cannot bleed to the sheet edge')

        if bad:
            fails.append((rel, '; '.join(bad)))
        elif verbose:
            print('  %sok%s   %s' % (G, Z, rel))

    print()
    for rel, why in fails:
        print('  %sFAIL%s  %-52s %s' % (R, Z, rel, why))
    print('\n  %d pages, %d decks, %d RPGs' % (total, decks, rpgs))
    if fails:
        print('  %s%d page%s need attention%s'
              % (R, len(fails), '' if len(fails) == 1 else 's', Z))
        sys.exit(1)
    print('  %severy page is ready for a phone%s' % (G, Z))


if __name__ == '__main__':
    main()
