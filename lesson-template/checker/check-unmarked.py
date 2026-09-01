#!/usr/bin/env python3
"""An auxiliary shown as grammar, wearing no colour at all.

WHY THIS EXISTS. Innes, on Going To 2: "short forms of am/are/is in this doc
need to be blue - is this mistake throughout all of Block Camp? How many other
blunders are there that I have to search for?"

A fair question, and the honest answer was that nobody knew - because
check-colour-roles.py only ever asked whether a word ALREADY WEARING a role
class was wearing the right one. A word wearing no class at all was invisible
to it. Every contraction in the line - I'm, we're, she's - was in exactly that
blind spot, and so was any auxiliary somebody forgot to tag.

WHERE IT LOOKS, and why not everywhere. In body copy an auxiliary is just a
word: "the plan is real" needs no colour and colouring it would be noise. But
inside the places a deck DISPLAYS grammar - a paradigm row, an example list, a
formula, a question stem, a sort chip, an order tile - every auxiliary is on
screen precisely because it is grammar, and one of them left plain is a gap in
the system a learner is being asked to read.

So: take those regions, delete everything already inside a coloured span, and
see what auxiliaries are left standing.

    python3 lesson-template/checker/check-unmarked.py [deck.html ...]
"""
import glob, os, re, sys

# WHERE GRAMMAR IS ON DISPLAY - and this list is deliberately short, because
# the first version was not and drowned in its own noise.
#
#   .para-verb   a paradigm cell. Every word in one is there to be read as
#                form: "I'm going to build" is the paradigm, not a sentence.
#   exlist item  a short worked example, one per line, printed to be copied.
#   .formula     the shape itself.
#
# NOT question stems or gap rows: those are whole sentences, and an auxiliary
# inside one is doing a sentence's work, not being displayed. "Which sentence
# is a promise?" needs no colour on its 'is'. NOT sort chips or order tiles
# either - those are plain across the entire line by convention, and flagging
# them would be flagging the convention.
REGIONS = (r'<span class="para-verb">(.*?)</span>\s*</div>',
           r'<span class="exlist">(.*?)</span>',
           r'<span class="formula">(.*?)</span>')

COLOURED = re.compile(
    r'<(?:em|b|span)\s+class="(?:aux|pp|obj|agent|inf|modal|verb|neg|freq|sig|sent'
    r'|action|state'
    r'|t-[a-z-]+)"[^>]*>.*?</(?:em|b|span)>', re.S)

# Every form of be, do and have, plus the contractions they hide in, plus the
# modal that behaves like them. Taken from the decks, not from a grammar book.
AUX = (r"am|is|are|was|were|be|been|being|do|does|did|done|"
       r"have|has|had|will|shall|"
       r"isn|aren|wasn|weren|don|doesn|didn|haven|hasn|hadn|won")
WORD = re.compile(r'(?<![A-Za-z])(%s)(?![A-Za-z])' % AUX, re.I)
SHORT = re.compile(r'&rsquo;(m|re|s|ve|ll)(?![A-Za-z])')
# 'd and n't are left out: 'd is had or would and needs a reading,
# and n't is already covered by the negative's own colour.

RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'

ALLOW = {
    # ('deck.html', 'word'): 'why this one is bare on purpose'
}


def slides(src):
    return src[src.find('<section class="slide'):src.find('const UI_I18N')]


# WHAT THIS GATE IS SURE ABOUT, AND WHAT IT IS NOT.
#
# FAIL - a be CONTRACTION with no colour on it. I'm, we're, she's, they've
#   carry a be inside them wherever they appear, no summary line is built out
#   of them, and a paradigm that colours its full forms and leaves its short
#   forms plain is simply half-done. This is the class Innes found on Going To
#   2, and it is the one the gate can be trusted on.
#
# REVIEW - a bare auxiliary inside a paradigm cell, an example or a formula.
#   Reported, but it does NOT fail, because those three places also hold whole
#   example sentences and one-line summaries: "Your boots are filthy", "every
#   one of these is TEMPORARY", "We had two horses then". Whether the be inside
#   an illustrative sentence should wear the tense colour is a teaching
#   decision, not a defect - the descent says yes and the camp decks have never
#   said either way. Listing them is useful; convicting them would be the gate
#   inventing policy.
#
# The first cut reported all of it as failures - 73 of them - and the 13 that
# mattered were buried. A gate that cries wolf stops being read.
def bare_words(seg, out, review, strict):
    """What is left in one displayed fragment once the coloured spans go."""
    bare = COLOURED.sub(' ', seg)
    bare = re.sub(r'<s>.*?</s>', ' ', bare, flags=re.S)          # struck-through errors
    bare = re.sub(r'<span class="sup".*?</span></span>', ' ', bare, flags=re.S)
    plain = re.sub(r'<[^>]+>', '', bare)
    if strict:
        for w in WORD.findall(plain):
            review.append((w.lower(), plain.strip()[:56]))
    for w in SHORT.findall(bare):
        out.append(('&rsquo;' + w, plain.strip()[:56]))


def scan(body):
    out, review = [], []
    for pat in REGIONS:
        strict = 'para-verb' in pat
        for m in re.finditer(pat, body, re.S):
            # an exlist holds one example per <span>; reading the whole list as
            # a single blob ran the examples together and made the report
            # unreadable, which is how a gate stops being used
            segs = (re.findall(r'<span>(.*?)</span>', m.group(1), re.S)
                    if 'exlist' in pat else [m.group(1)])
            for seg in segs:
                bare_words(seg, out, review, strict)
    return out, review


def main(decks):
    total, per_deck, reviews = 0, [], []
    for deck in decks:
        name = os.path.basename(deck)
        found, review = scan(slides(open(deck, encoding='utf-8').read()))
        found = [f for f in found if (name, f[0]) not in ALLOW]
        if found:
            per_deck.append((name, found)); total += len(found)
        if review:
            reviews.append((name, review))
    print('\n  AN AUXILIARY SHOWN AS GRAMMAR, WEARING NO COLOUR   %d deck(s) scanned\n'
          % len(decks))
    if not total:
        print('    ' + GRN % 'PASS',
              'every be-contraction on display in the line carries a role')
    for name, found in per_deck:
        words = {}
        for w, where in found:
            words.setdefault(w, []).append(where)
        print('    ' + RED % 'FAIL', '%-34s %d' % (
            name.replace('blockcamp-', '').replace('.html', ''), len(found)))
        for w in sorted(words):
            print('           %-12s x%-3d %s' % (w, len(words[w]), DIM % words[w][0]))
    if total:
        print('\n  %d contraction(s) in %d deck(s)' % (total, len(per_deck)))
    n = sum(len(r) for _, r in reviews)
    print(DIM % ('\n  %d bare auxiliary/ies in a paradigm cell, for review, not failing.'
                 % n))
    print(DIM % '  Run with --review to list them: they are a teaching call, not a defect.')
    if '--review' in sys.argv:
        for name, review in reviews:
            print('\n    %s' % name.replace('blockcamp-', '').replace('.html', ''))
            for w, where in review:
                print('      %-8s %s' % (w, DIM % where))
    print()
    return 1 if total else 0
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or sorted(glob.glob('blockcamp-*.html'))))
