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

Five things are checked:

  TOKENS     every --mark-* / --t-* holds ONE value across every deck. A role
             with two colours is the defect the whole scheme exists to prevent.
  ORPHANS    a class used in the slides with no token behind it (renders
             unstyled), or a token defined that nothing uses (dead weight).
  UNTAGGED   an auxiliary followed by a word that IS a past participle but
             carries no .pp - the 'lit' and 'left' case, reported not skipped.
  SECOND     a past-simple form wearing .pp. 'went' and 'gone' are different
             jobs; colouring the second form teaches the opposite of the slide.
  AUXJOB     .aux on a word that is not doing the auxiliary's job. THIS GATE
             MISSED EVERY ONE OF THESE and Innes found all six by eye, over
             four separate messages: "green 'was'? ", "'had' is green for no
             reason", "why is has/have/am in green", "green colored words -
             what is the logic here?". They were the past copula in an
             example ("when I was a child"), the lexical verb on the one
             slide whose subject is that it is NOT an auxiliary ("I have a
             sword"), a copula in a sentence about the tense ("every step is
             PAST SIMPLE"), a second form in a table of second forms
             ("have -> had"), and - the one that gives the game away - the
             GERMAN word 'am' in the gloss "am Ende", which an automated
             tagger matched as the English auxiliary.
             A be/have/do form is an auxiliary only when a verb follows it.
             If what follows is a determiner, a pronoun, a preposition or
             nothing at all, it is the main verb and the green is a lie.

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


# ── AUXJOB ───────────────────────────────────────────────────────────────
# A be/have/do form is an AUXILIARY only when a verb follows it. These are the
# words that, following one, prove it is the MAIN verb instead: you cannot say
# "is a", "have a sword", "was small" and still be looking at an auxiliary.
BE_HAVE_DO = {'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being',
              'have', 'has', 'had', 'do', 'does', 'did',
              "isn't", "aren't", "wasn't", "weren't", "haven't", "hasn't",
              "hadn't", "don't", "doesn't", "didn't"}
# THE FIRST VERSION CONVICTED ON DETERMINERS ONLY, AND IT WAS TOO TIMID.
# Auditing every .aux in the line against the word that follows it turned up a
# whole family it could not see: "your hands are FILTHY", "I am EXHAUSTED",
# "the ground is still WET", "you are OUT of breath", "there is PAINT on your
# hands". Every one is a copula with a predicate, and every one was green.
# So the test is inverted. An auxiliary is only an auxiliary when a VERB
# follows it, and a verb is recognisable: an -ing form, a known participle, or
# anything at all after do/does/did (which take a bare infinitive). A pronoun
# means an inverted question - "Have you eaten?" - and the verb is one word
# further on, so those are read through. An adverb or 'not' is read through
# too. Anything else convicts.
PRONOUN = {'i', 'you', 'he', 'she', 'it', 'we', 'they', 'there',
           'anybody', 'somebody', 'everybody', 'nobody', 'anyone', 'someone'}
ADVERBS = {'not', 'just', 'already', 'never', 'ever', 'still', 'recently',
           'lately', 'only', 'always', 'nearly', 'almost', 'finally', 'yet',
           'usually', 'often', 'sometimes', 'probably', 'really', 'also'}
DO_FORMS = {'do', 'does', 'did', "don't", "doesn't", "didn't"}
# Verbs the line uses that neither end in -ing nor sit in PARTICIPLE.
IRREGULAR_PP = {
    'grown', 'known', 'seen', 'given', 'taken', 'driven', 'flown', 'thrown',
    'worn', 'torn', 'drawn', 'blown', 'shown', 'spoken', 'broken', 'chosen',
    'frozen', 'risen', 'written', 'ridden', 'eaten', 'beaten', 'fallen',
    'forgotten', 'hidden', 'sung', 'run', 'won', 'begun', 'lost', 'sent',
    'built', 'kept', 'left', 'made', 'found', 'put', 'read', 'said', 'done',
    'gone', 'been', 'had', 'got', 'met', 'paid', 'sold', 'told', 'heard',
}
EXTRA_VERB = {'be', 'been', 'being', 'going', 'go', 'come', 'get', 'have',
              'had', 'has', 'take', 'build', 'leave', 'rain', 'snow', 'call',
              'wait', 'win', 'quit', 'run', 'try', 'plant', 'hatch', 'burst',
              'explode', 'fall', 'hand', 'tell', 'like', 'matter'}
# Glosses are not English grammar demonstrations. Any .aux inside a .sup is
# wrong by construction - that is how the German 'am' in "am Ende" got green.
GLOSS = re.compile(r'<span class=\\?"sup\\?"[^>]*>.*?</span>\s*</span>', re.S)
# The tag, then the next word - through a closing </em>, a </b>, a <b>, an
# adverb, whatever the markup puts between them.
AUX_NEXT = re.compile(
    r'<em class=\\?"aux\\?">([^<]*)</em>'
    r'((?:</?[a-z][^>]*>|\s|&[a-z]+;)*)'
    r'([A-Za-z\u2019\']*)')


def auxjob(name, body, findings, allowed):
    """.aux on a word that is not doing an auxiliary's job."""
    for m in GLOSS.finditer(body):
        for g in re.finditer(r'<em class=\\?"aux\\?">([^<]*)</em>', m.group(0)):
            findings.append((name, 'AUXJOB',
                             "'%s' is inside a translation gloss - a gloss is "
                             "not English grammar, so nothing in it is an "
                             "auxiliary" % g.group(1)))
    # A paradigm cell whose ENTIRE content is the be/have/do form is a verb
    # table, not a structure: "have -> had" lists the second form of a lexical
    # verb. That is the past-simple 'had' case.
    for w in re.findall(r'<span class="para-verb"><em class=\\?"aux\\?">([^<]+)</em></span>', body):
        findings.append((name, 'AUXJOB',
                         "'%s' is the whole of a paradigm cell - a verb table "
                         "lists lexical forms, not auxiliaries" % w))
    for m in AUX_NEXT.finditer(body):
        word = re.sub(r'&[a-z]+;', "'", m.group(1)).strip().lower()
        nxt = re.sub(r'&[a-z]+;', "'", m.group(3)).strip().lower()
        if word not in BE_HAVE_DO:
            continue
        # Read through the words that are never the verb itself.
        if nxt in ADVERBS or nxt in PRONOUN:
            continue
        # A formula pill legitimately ENDS on the auxiliary
        # ("SUBJECT + am / are / is + VERB-ing"), so an empty follower proves
        # nothing.
        if not nxt:
            continue
        if word in DO_FORMS:          # do/does/did take a bare infinitive
            continue
        # A regular participle is any -ed form, and there is no closed list
        # of those. 'worked', 'grown', 'changed', 'wanted' and 'counted' were
        # all convicted by the first inverted version; the irregulars that do
        # not end in -ed are named in IRREGULAR_PP below.
        if (nxt.endswith('ing') or nxt.endswith('ed') or nxt in PARTICIPLE
                or nxt in SECOND or nxt in EXTRA_VERB or nxt in IRREGULAR_PP):
            continue
        if (name, word) in ALLOW:
            allowed.append((name, word))
            continue
        where = re.sub(r'<[^>]+>', '', m.group(0))
        findings.append((name, 'AUXJOB',
                         "'%s' is followed by '%s', which is not a verb - so this "
                         "is a main verb wearing the auxiliary colour  %s"
                         % (word, nxt, DIM % where.strip()[:44])))


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
        auxjob(name, body, findings, allowed)
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

    for kind, title in (('ORPHAN', 'ORPHANS'), ('UNTAGGED', 'UNTAGGED'),
                        ('SECOND', 'SECOND FORMS'), ('AUXJOB', 'AUXILIARY DOING ANOTHER JOB')):
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
