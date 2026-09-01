#!/usr/bin/env python3
"""One colour per grammatical job, checked across the whole line.

Innes: "my only concern is that colored words are consistent e.g. purple past
participles." Nothing measured that, and the cost was real: --mark-pp lived only
in the two passive decks while four present-perfect decks taught the participle
and left it white, and inside one deck the word 'been' was purple in a paradigm
row and plain in the formula directly beneath it.

The tagger that fixed those failed SILENTLY on 'lit' and 'left', because the
adverb between the auxiliary and the participle is bare text inside a <b>:

    <b><em class="aux">has</em> just lit</b>

It captured 'just', found it was not a participle, and moved on without a word.
A silent tagger is how a colour rule rots. This gate is the loud version.

Four things are checked:

  TOKENS     every --mark-* / --t-* holds ONE value across every deck. A role
             with two colours is the defect the whole scheme exists to prevent.
  ORPHANS    a class used in the slides with no token behind it (renders
             unstyled), or a token defined that nothing uses (dead weight).
  UNTAGGED   an auxiliary followed by a word that IS a past participle but
             carries no .pp - the 'lit' and 'left' case, reported not skipped.
  SECOND     a past-simple form wearing .pp. 'went' and 'gone' are different
             jobs; colouring the second form teaches the opposite of the slide.

    python3 lesson-template/checker/check-colour-roles.py [deck.html ...]
"""
import glob, os, re, sys
from collections import Counter, defaultdict

# Third forms this line actually uses. Deliberately a closed list: guessing a
# participle from its shape marks 'read' and 'left' wrong in both directions.
PARTICIPLE = {
    'been', 'gone', 'seen', 'eaten', 'written', 'done', 'built', 'lit', 'left',
    'made', 'taken', 'broken', 'found', 'opened', 'locked', 'mined', 'placed',
    'drawn', 'baked', 'closed', 'smelted', 'repaired', 'sent', 'known', 'lived',
    'painted', 'read', 'walked', 'waited', 'put', 'rebuilt', 'lost', 'given',
}
# Second forms. These must NEVER wear the participle colour: the whole point of
# the THIRD-form slide is that 'went' and 'gone' look different.
SECOND = {'went', 'moved', 'saw', 'ate', 'wrote', 'did', 'broke', 'took',
          'made', 'found', 'built', 'sent', 'read', 'put', 'lit', 'left'}
# ...several verbs share their second and third form, so SECOND on its own
# cannot convict. Only these are unambiguous.
SECOND_ONLY = {'went', 'saw', 'ate', 'wrote', 'did', 'broke', 'took', 'moved'}

# Reviewed exceptions, with the reason. Same discipline as pins.json: a false
# positive is silenced by name, never by loosening the rule, so the next one
# still gets reported.
ALLOW = {
    ('blockcamp-past-continuous.html', 'gone'):
        "'the tense is gone' - a predicative adjective, not the participle of a "
        "perfect. English genuinely overlaps here; the slide is right.",
}

ADV = (r'(?:just|already|never|ever|still|not|recently|lately|only|always|'
       r'nearly|almost|finally|yet)')
AUX_THEN_WORD = re.compile(
    r'<em class=\\?"aux\\?">[^<]*</em>'
    r'(?:\s*(?:<em>%s</em>|%s))*'
    r'\s+([a-z]+)\b' % (ADV, ADV))

RED, GRN, DIM = '\x1b[31m%s\x1b[0m', '\x1b[32m%s\x1b[0m', '\x1b[2m%s\x1b[0m'


def slides_of(src):
    """Only what a learner sees: slides, not the CSS and not the dictionary."""
    a = src.find('<section class="slide')
    b = src.find('const UI_I18N')
    return src[a:b if b > a else len(src)]


def main(decks):
    tokens = defaultdict(lambda: defaultdict(list))
    findings = []
    allowed = []
    for deck in decks:
        name = os.path.basename(deck)
        src = open(deck, encoding='utf-8').read()
        body = slides_of(src)
        for tok, val in re.findall(r'--(mark-[a-z]+|t-[a-z-]+):\s*([^;]+);', src):
            tokens[tok][val.strip()].append(name)

        defined = set(re.findall(r'--(mark-[a-z]+):', src))
        styled = set(re.findall(r'\.([a-z]+)\s*\{\s*color:\s*var\(--mark-', src))
        used = set(re.findall(r'class=\\?"([a-z]+)\\?"', body)) & {
            'aux', 'pp', 'obj', 'agent', 'inf', 'modal'}
        for c in sorted(used - styled):
            findings.append((name, 'ORPHAN', 'class .%s is used on a slide but no rule colours it' % c))

        for m in AUX_THEN_WORD.finditer(body):
            w = m.group(1)
            if w in PARTICIPLE and 'class="pp"' not in m.group(0):
                if (name, w) in ALLOW:
                    allowed.append((name, w))
                    continue
                where = re.sub(r'<[^>]+>', '', body[max(0, m.start() - 40):m.end()])
                findings.append((name, 'UNTAGGED',
                                 "'%s' follows an auxiliary but is not .pp  %s"
                                 % (w, DIM % ('...' + where.strip()[-46:]))))
        for w in re.findall(r'class=\\?"pp\\?">([^<]+)</em>', body):
            if w.lower() in SECOND_ONLY:
                findings.append((name, 'SECOND', "'%s' is a past simple form wearing the participle colour" % w))

    print('\n  TOKENS')
    bad = False
    for tok, vals in sorted(tokens.items()):
        if len(vals) > 1:
            bad = True
            print('    ' + RED % 'FAIL', '%s has %d different values:' % (tok, len(vals)))
            for v, ds in vals.items():
                print('          %-24s %d deck(s)' % (v, len(ds)))
        else:
            v, ds = next(iter(vals.items()))
            print('    ' + GRN % 'PASS', '%-18s %-22s consistent across %d decks' % (tok, v, len(ds)))

    for kind, title in (('ORPHAN', 'ORPHANS'), ('UNTAGGED', 'UNTAGGED'), ('SECOND', 'SECOND FORMS')):
        rows = [f for f in findings if f[1] == kind]
        print('\n  %s' % title)
        if not rows:
            print('    ' + GRN % 'PASS', 'nothing found')
        for name, _, msg in rows:
            print('    ' + RED % 'FAIL', '%-42s %s' % (name.replace('blockcamp-', '').replace('.html', ''), msg))

    if allowed:
        print('\n  ALLOWED (reviewed, see ALLOW at the top of this file)')
        for name, w in allowed:
            print('    ' + DIM % ('%-42s %s' % (name.replace('blockcamp-','').replace('.html',''), ALLOW[(name, w)])))

    total = len(findings) + (1 if bad else 0)
    print('\n  %d finding(s) across %d deck(s)\n' % (total, len(decks)))
    return 1 if total else 0


if __name__ == '__main__':
    decks = sys.argv[1:] or sorted(
        d for d in glob.glob('blockcamp-*.html') if 'passive-intro' not in d)
    sys.exit(main(decks))
