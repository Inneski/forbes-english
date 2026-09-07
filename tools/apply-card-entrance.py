#!/usr/bin/env python3
"""Apply the 2026-09-07 wash + card-entrance change to already-built decks.

Normally a deck change means editing the builder and re-running it. Not this
time. Most shipped decks were built from an older template, so re-running
their builder drags in every template change since — on a sample of 75 decks
that was +32,000 lines of machinery (an exam audio player, gloss syncing,
ledger drawing) that those lessons never shipped with. That is a different
change from the one Innes asked for.

So this patches the two CSS edits into the built pages directly. That is not
a divergence from the template: lesson-template.html already carries the same
CSS, so a future rebuild produces the same result.

  1. Light theme only — thin the wash so the artwork carries:
       --wash-mid  8% -> 4% ,  --wash-edge 26% -> 17% ,  --bg-opacity .62 -> .74
  2. Every theme — the card entrance tokens, the keyframes, and the
     reduced-motion and print switches.

Usage:
    python3 tools/apply-card-entrance.py <file.html>...   # or a glob
    python3 tools/apply-card-entrance.py --check <files>  # report only

Idempotent: a page that already has the change is reported as "already".
"""
import sys, os

TOKENS_ANCHOR = "  --bg-opacity: 0.72;     /* background pattern strength — see doc §6 */"
TOKENS = TOKENS_ANCHOR + """

  /* Card entrance. The delay is the whole point: for that beat the slide
     shows nothing but the artwork. Raise --card-in-delay to linger longer on
     the picture, drop it to nothing to go back to cards-with-the-slide. */
  --card-in-delay: 0.14s;
  --card-in-step:  0.08s;   /* each further card follows this much later */
  --card-in-dur:   0.46s;
  --card-in-ease:  cubic-bezier(.34, 1.56, .64, 1);   /* overshoots, then settles */"""

CARD_ANCHOR = ".card + .card { margin-top: 16px; }"
CARD = CARD_ANCHOR + """

/* The card lands a beat AFTER the slide, so the artwork underneath is seen
   before it is covered — the pause is what makes the picture register at all.
   Overshoot in the easing curve gives the bounce; the card passes 1.0 and
   settles back. Timings live in one place so a lesson can retune the feel
   without hunting for four numbers (see doc §6). */
.slide.is-active .card {
  animation: card-pop var(--card-in-dur) var(--card-in-ease) both;
  animation-delay: var(--card-in-delay);
}
.slide.is-active .card + .card         { animation-delay: calc(var(--card-in-delay) + var(--card-in-step)); }
.slide.is-active .card + .card + .card { animation-delay: calc(var(--card-in-delay) + var(--card-in-step) * 2); }
@keyframes card-pop {
  from { opacity: 0; transform: scale(.92); }
  55%  { opacity: 1; }
  to   { opacity: 1; transform: none; }
}"""

OFF = """  .slide.is-active .card,
  .slide.is-active .card + .card,
  .slide.is-active .card + .card + .card {"""

RM_ANCHOR = "@media (prefers-reduced-motion: reduce) {"
RM = RM_ANCHOR + """
  /* No spring, no delay — the card is simply there. */
""" + OFF + """
    animation: none;
  }"""

PR_ANCHOR = "  .bg-layer, .deck-bar, .lang-select, .nav-btn, .deck-rail { display: none !important; }"
PR = PR_ANCHOR + """
  /* A delayed animation must never decide what lands on a printed page. */
""" + OFF + """
    animation: none !important; opacity: 1 !important; transform: none !important;
  }"""

WASH = [
    ("  --wash-mid:  color-mix(in srgb, var(--void) 8%, transparent);",
     "  --wash-mid:  color-mix(in srgb, var(--void) 4%, transparent);"),
    ("  --wash-edge: color-mix(in srgb, var(--void) 26%, transparent);",
     "  --wash-edge: color-mix(in srgb, var(--void) 17%, transparent);"),
    ("  --bg-opacity: 0.62;", "  --bg-opacity: 0.74;"),
]


def patch(path, check=False):
    s = open(path, encoding='utf-8').read()
    if 'card-pop' in s:
        return 'already', 0
    if CARD_ANCHOR not in s or TOKENS_ANCHOR not in s:
        return 'not a deck', 0          # no shared shell — leave it alone
    n = 0
    for anchor, block in ((TOKENS_ANCHOR, TOKENS), (CARD_ANCHOR, CARD)):
        s = s.replace(anchor, block, 1); n += 1
    # These two are optional: a deck may predate either block.
    for anchor, block in ((RM_ANCHOR, RM), (PR_ANCHOR, PR)):
        if anchor in s:
            s = s.replace(anchor, block, 1); n += 1
    # The wash is only thinned where it still holds the standard values. A
    # handful of decks were deliberately given a heavier wash because their
    # hero is busy or bright (HOUSE-STYLE §6: bump the wash only for the
    # lesson that needs it) — twin-peaks-b2-discussion, koolhas & Lamb and
    # forbes-gap-fill run 22%/44%. Thinning those by the same amounts would
    # undo a decision someone made on purpose, so they keep their wash and
    # take the card entrance only.
    hits = sum(1 for old, _ in WASH if old in s)
    light = 0
    if hits == len(WASH):
        for old, new in WASH:
            s = s.replace(old, new, 1); light += 1
    elif hits:
        kind_note = ' (kept its own heavier wash)'
    if not check:
        open(path, 'w', encoding='utf-8').write(s)
    if light:
        return 'light — wash thinned + card entrance', n
    if hits:
        return 'light — OWN heavier wash kept, card entrance only', n
    return 'dark — card entrance only', n


if __name__ == '__main__':
    args = sys.argv[1:]
    check = '--check' in args
    files = [a for a in args if a != '--check']
    if not files:
        print(__doc__); sys.exit(1)
    tally = {}
    for f in sorted(files):
        if not f.endswith('.html'):
            continue
        try:
            kind, n = patch(f, check)
        except Exception as e:
            kind, n = f'ERROR {e}', 0
        tally[kind] = tally.get(kind, 0) + 1
        if kind.startswith('ERROR') or 'OWN heavier' in kind:
            print(f"  {kind}  {f}")
    for k in sorted(tally):
        print(f"  {tally[k]:4d}  {k}")
