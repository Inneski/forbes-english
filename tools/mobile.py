#!/usr/bin/env python3
"""Put flow mode into every deck that is already built.

    py tools/mobile.py            # write
    py tools/mobile.py --check    # report, change nothing

Innes, 2026-10-29: "I tried to open Kraken on a mobile and it didnt even have
a next button. I want you to work hard on optimising the website for mobile
use."

WHY THIS EXISTS AT ALL
----------------------
`lesson-template.html` is the chrome, and `deck.py`'s assemble() copies the
whole file and splices the slides into it. So a fix to the chrome reaches a
deck only when that deck's builder is run again. Measured on 2026-10-29:
165 built pages carry fitStage(), in FOUR different versions -- 155 of them
still the one from before .is-phone existed, which means the phone arrows
Innes asked for on 2026-10-13 never reached nine decks in ten. Running 163
builders to deliver a stylesheet is a day of risk (retired builders that
refuse, builders a peer has open, a hero that has moved) for a change that
touches no content.

So this does what tools/seo.py does: it rewrites a generated region of every
built page from one source. The source is lesson-template.html -- the CSS
between FLOW-MODE-BEGIN and FLOW-MODE-END, and the whole of fitStage(). A
builder re-run afterwards produces the same bytes, because it reads the same
template, so the two routes agree rather than fighting.

WHAT IT TOUCHES
---------------
Nothing but those two regions, and only in a page that has a .stage and a
fitStage() to replace. Run it twice and the second run reports no change.
The flow block goes in its own <style data-flow> element at the end of
</head>, after the deck's own stylesheet, so it is last on equal specificity
and a deck's own later rules are the ones it still has to outrank by weight.

ORDER
-----
Any time after a builder runs, before tools/seo.py. seo.py rewrites the
<head>'s metadata and does not read or write this block; running it first is
harmless, running this one after a build is not optional -- a rebuilt deck
goes back to the template's own copy of fitStage, which is the same one, so
in practice only the <style data-flow> has to be put back.
"""
import io, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, 'lesson-template', 'lesson-template.html')

# Pages that are not decks, or are the template itself.
SKIP_DIRS = ('.claude', 'node_modules', 'lesson-template', 'docs', 'incoming')

FIT = re.compile(r'function fitStage\(\)\s*\{.*?\n\}', re.S)
ORIENT = "addEventListener('orientationchange', () => setTimeout(fitStage, 0));"
FLOW_STYLE = re.compile(r'[ \t]*<style data-flow>.*?</style>\n?', re.S)


def template_parts():
    s = io.open(TPL, encoding='utf-8', newline='').read()
    a = s.index('/* FLOW-MODE-BEGIN')
    b = s.index('/* FLOW-MODE-END */') + len('/* FLOW-MODE-END */')
    css = s[a:b]
    m = FIT.search(s)
    assert m, 'lesson-template.html has no fitStage() to copy'
    assert 'is-flow' in m.group(0), 'the template fitStage does not set is-flow'
    return css, m.group(0)


def pages():
    out = []
    for pat in ('*.html', '*/*.html'):
        for p in glob.glob(os.path.join(ROOT, pat)):
            rel = os.path.relpath(p, ROOT).replace('\\', '/')
            if rel.split('/')[0] in SKIP_DIRS:
                continue
            out.append((rel, p))
    return sorted(out)


def patch(s, css, fit):
    """Return (new_source, [what changed])."""
    done = []

    # 1. fitStage. Four versions are in the wild; all four are replaced by the
    #    template's, which is the only one that knows about flow mode.
    m = FIT.search(s)
    if m and m.group(0) != fit:
        s = s[:m.start()] + fit + s[m.end():]
        done.append('fitStage')

    # 1b. A turned phone now changes which layout the deck is in, not just the
    #     scale, so the one resize listener is doubled up. Guarded, so a
    #     second run does not add a second copy.
    if ORIENT not in s:
        # fireshield-pitch.html writes the same line with double quotes; it is
        # the one deck with chrome of its own, and it is the reason this looks
        # for both rather than for one exact string.
        m = re.search(r'addEventListener\(["\']resize["\'], fitStage\);', s)
        if m:
            s = s[:m.end()] + '\n' + ORIENT + s[m.end():]
            done.append('orientationchange')

    # 2. The flow stylesheet, in its own element so it can be found again and
    #    replaced whole rather than diffed. A deck built since flow mode landed
    #    already carries the block inline, in the chrome it copied from the
    #    template; giving it a second identical copy would only make the next
    #    person wonder which one is live. Any stale <style data-flow> from an
    #    earlier run of this tool is taken out in that case.
    block = '<style data-flow>\n' + css + '\n</style>\n'
    old = FLOW_STYLE.search(s)
    inline = s.find('FLOW-MODE-BEGIN')
    if inline >= 0 and (not old or inline < old.start()):
        if old:
            s = s[:old.start()] + s[old.end():]
            done.append('css (dropped duplicate)')
        return s, done
    if old:
        if old.group(0).strip() != block.strip():
            s = s[:old.start()] + block + s[old.end():]
            done.append('css')
    else:
        i = s.find('</head>')
        if i < 0:
            return s, done
        s = s[:i] + block + s[i:]
        done.append('css')
    return s, done


def main():
    check = '--check' in sys.argv
    css, fit = template_parts()
    changed, already, skipped = [], 0, 0
    for rel, path in pages():
        try:
            s = io.open(path, encoding='utf-8', newline='').read()
        except Exception as e:
            print('! unreadable %s (%s)' % (rel, e))
            continue
        # A deck is a page with the 1280x720 stage and the function that fits
        # it. Everything else on the site -- the home page, the library, the
        # hubs, the RPGs -- is laid out responsively already or has its own
        # chrome, and must not be given a stylesheet about a stage it has not
        # got.
        if 'fitStage' not in s or 'class="stage"' not in s:
            skipped += 1
            continue
        new, done = patch(s, css, fit)
        if not done:
            already += 1
            continue
        changed.append((rel, done))
        if not check:
            io.open(path, 'w', encoding='utf-8', newline='').write(new)

    for rel, done in changed:
        print('%s %-54s %s' % ('would patch' if check else 'patched', rel, '+'.join(done)))
    print('\n%d deck%s %s, %d already current, %d page%s are not decks'
          % (len(changed), '' if len(changed) == 1 else 's',
             'need patching' if check else 'patched',
             already, skipped, '' if skipped == 1 else 's'))
    if check and changed:
        sys.exit(1)


if __name__ == '__main__':
    main()
