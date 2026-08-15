# -*- coding: utf-8 -*-
"""Advanced Grammar in Context (B2) — rebuilt as a 16:9 deck.

Same filename, so the live URL does not change.

**A quarter of the marks were printed in the input boxes.** The error
correction activity rendered `placeholder="${q.placeholders[0]}…"`, and
the `placeholders` array was byte-identical to the first accepted answer
in all six fields. The learner read the grey ghost text and typed it.
There is no `placeholders` array here, no `placeholder` attribute on any
scored input, and nothing in this deck shows an answer before it is
given.

**Another quarter could not be lost.** The matching activity incremented
its counter on a correct match only; a wrong one flashed red, cost
nothing, and could be retried until it landed, and the exit gate to the
results screen opened only at 5/5. Every learner who saw a score scored
5/5 there. The shared match engine in `deck.py` still behaves that way —
it is thirty-odd shipped lessons' worth of behaviour and changing it is
not this rebuild's decision — so the five pairs are now five one-per-slide
"identify the structure" multiple-choice items, which also clears the
592px overflow the ten-row matching board measured at house-style type
and gives every item its own wrong-answer explanation.

With those two fixed, the reported score stops being `50 + 0.5 × real`.
The old scale had a floor of 50%: a learner who answered nothing
correctly was told they had "solid B2 foundations", and the bottom band
was unreachable by anyone who finished. All 21 points here are losable,
so the sub-50% band is reachable. The two-error correction item is two
gap rows and therefore **two points**, not one all-or-nothing point — the
engine counts gaps, not slides, and the old item scored zero for a
learner who fixed one of the two.

**The lesson contradicted itself about backshift.** One explanation said
the present perfect may stay un-shifted "for timeless facts reported
immediately"; two other items marked the un-shifted form wrong. Both
halves lived in post-answer feedback, and the word *backshift* did not
appear in the file at all. Backshift is now a table, its exceptions are a
slide of their own that says in as many words that both forms are correct
English, and every item that turns on it is written so that the context —
not a house preference — decides. `fitb[0]` accepts `was made` as well as
`had been made`.

**Four factual errors.** *Top Gear* did not move to Amazon: the
presenters did, and made a different programme, so the third-conditional
gap is now about the presenters and *The Grand Tour*. The Stig was not
introduced by Clarkson — the character is generally credited to producer
Andy Wilman and the first Stig was Perry McCarthy — and that false
attribution was the typed answer key, so the it-cleft now focuses the
Stig on the Power Lap board, which is what the Stig actually did. The
mixed conditional asserted that Hammond would still be presenting had he
not crashed; he crashed, returned within months and presented for another
eighteen years, so the counterfactual now runs to the programme's safety
rules. And "over 4.5 million viewers on its opening night" is not a
documented number — Amazon has never published viewing figures for *The
Grand Tour* — so the gap now takes the hedged premiere-record claim the
company did make.

The characters stay: Clarkson, Hammond, May and the Stig are all still
here, and the front-page image is settled. What has gone is the invented
speech. Clarkson no longer says "I will never apologise for what I said"
(he apologised publicly in May 2014); Hammond no longer says he would
have retired; and the conditional about the BBC suspension — which
editorialised about a physical assault on a real third party as something
a timely apology would have cured — is now a weather call on a shoot.
Where a person is quoted at all, the claim is either attested or plainly
hypothetical.

**Every distractor was broken English in four of the five multiple-choice
items** — a learner who had never heard of a cleft, a mixed conditional
or a complex passive scored by picking the only option that read as
English. The distractors are now well-formed sentences that are wrong for
a taught reason: a third conditional against a mixed one, a wh-cleft
against an it-cleft, the `It is known that…` pattern against the
`is known to…` pattern. Key lengths are unchanged; the distractors were
lengthened, never the key shortened, and the ANSWERS gate still passes.

**The keys were `[1,1,1,0,0]`** — B three times, A twice, never C, never
D — with `Math.random` appearing nowhere in the file, so every learner saw
the same letters in the same places, including after restarting. The ten
multiple-choice keys are now deranged across all four positions and the
distribution is asserted at build time; the engine shuffles on top of
that.

**Right and wrong said the same thing** on fifteen of twenty items: the
explanation body was byte-identical on both branches and only a two-word
prefix differed, while the matching activity showed one hardcoded string
— *"Look carefully at the grammar structure"* — for every wrong attempt
on every pair. Each of the thirty wrong options here carries its own
`data-explain`, injected after `D.mc` as `build_nature2.py` does, and
each of the eleven gaps has its own explanation.

**Fifteen of seventeen rules were learnable only by answering first.**
The whole of the teaching was 84 words in four boxes on an intro screen
that was hidden the moment the lesson started and could not be reached
again — while the sub-50% band told the learner to "re-read the reference
section", which did not exist. There are fourteen teaching slides here.
The third conditional was tested three times and taught nowhere; it has a
slide. So do backshift and its exceptions, the deixis shifts, what may
not go in an if-clause, both cleft frames, both complex-passive patterns,
stative verbs, and a terminology slide for the eleven terms the file used
before defining — *backshift* among them, which it never used at all.

**Gap input rejected correct English.** `trim().toLowerCase()` and
nothing else: a double space failed, and a curly apostrophe typed on a
phone failed against the straight one in the key, on the single item that
invites `hadn't`. Answers here are collapsed and expanded at build time
into curly-apostrophe and `-ize` variants, so `hadn’t moved` and
`revolutionized` are accepted, along with the alternatives the audit
listed. `deck.py` is untouched: the expansion is per-lesson data, not a
change to an engine thirty lessons share.

Also fixed: the two over-general cleft labels (an it-cleft does not
"emphasise the subject" — the lesson's own Veyron sentence focuses an
object) and the matching row that asked the learner to call a direct
quotation "reported speech"; the "exactly one error, highlighted in red"
instruction on a two-error item; the `\\u2713` CSS escape that rendered as
literal "u2713" on completed tabs; the restart that left the previous
run's finished board on screen with the first activity hidden; the inline
`<div style>` baked into a question stem; the "~30 minutes" claim on a
deck that is now 45–55; and the generic `<title>`.

The 714 KB base64 hero on line 162 was 94% of a 760 KB file, and sat
inside a bordered box in the page flow. It is now `--hero:
url('TopGearB2/hero.jpg')`, set once, driving the cover, the background
on every slide and the PDF export. `library.html` gains the thumbnail
entry it never had.

Artwork: `TopGearB2/hero.jpg` — 1672×941, exactly 16:9, the three
presenters against a police car. Median luminance 0.088, so this is a
dark deck; the palette is pasted verbatim from
`extract-palette.py TopGearB2/hero.jpg` and every row passes. The accent
is the Battenburg lime lifted off the car, the secondary and contrast are
its blue. Nothing here is hand-picked, and the five hardcoded
`rgba(0,0,0,…)` values, four `#fff`s and fourteen raw hex values of the
old file — including a hand-picked `--green` and `--red` — are gone.
There is no second image for this lesson, so no slide takes a `data-bg`.
"""
import re
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
import i18n_topgear as I

TPL = '/home/claude/forbes-english/lesson-template/lesson-template.html'
OUT = '/home/claude/forbes-english/forbes-english-b2-lesson.html'
F = 'TopGearB2'
E = I.T['en']

# Derived mechanically from TopGearB2/hero.jpg:
#   python3 lesson-template/extract-palette.py TopGearB2/hero.jpg
# Every row of the contrast report PASSES — text on surface 14.99:1, the
# weakest row (border on surface) 4.27:1 against a 1.25 floor. Dark theme:
# the hero's median pixel is at 0.088 luminance and the middle third, where
# the content sits, is 0.1075. The light variant collapses --accent and
# --accent-bright onto the same value, so it has no emphasis step at all.
PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #111415;
  --surface       : #1b2122;
  --surface2      : #242c2e;
  --border        : #84872b;
  --text          : #f5f5f2;
  --text-dim      : #bebfa3;
  --accent        : #e4ea2e;
  --accent-bright : #c0c600;
  --accent-dim    : #a2a616;
  --secondary     : #0355ad;
  --contrast      : #4c96f0;''' % F

# The backshift table, the struck-through error words, and the two
# example colours. The three tense values are copied from
# lesson-template/tense-palette.css per HOUSE-STYLE §5a — three on the
# slide, not four, and each lightened with color-mix because navy and
# maroon do not read on a dark canvas.
CSS = '''.gtab { width: 100%; border-collapse: collapse; font-size: 17px;
  line-height: 1.4; }
.gtab td { padding: 6px 8px; vertical-align: top;
  border-bottom: 1px solid color-mix(in srgb, var(--border) 28%, transparent); }
.gtab tr:last-child td { border-bottom: none; }
.gtab td:first-child { width: 46%; color: var(--text-dim); }
.gtab .arw { width: 24px; text-align: center; color: var(--accent-dim); }
.t-pres  { color: color-mix(in srgb, var(--t-present-simple) 42%, white);
  font-weight: 600; }
.t-past  { color: color-mix(in srgb, var(--t-past-simple) 84%, white);
  font-weight: 600; }
.t-pperf { color: color-mix(in srgb, var(--t-past-perfect) 45%, white);
  font-weight: 600; }
.q-stem s, .prose s { color: var(--no); text-decoration-color: var(--no);
  font-style: normal; }
.eg-no { color: var(--no); font-style: normal; }
.eg-ok { color: var(--ok); font-style: normal; }
'''
TENSE_VARS = ''':root {
  --t-present-simple: #16345C;
  --t-past-simple   : #B08968;
  --t-past-perfect  : #6E0B24;

  /* HOUSE-STYLE §5, the per-lesson wash bump, measured rather than
     guessed. This hero carries a cream sky band across its top ~10%,
     exactly where the eyebrow, the deck bar and the progress rail sit:
     bgmeasure.py reported a mean background luminance of 0.143 and body
     text at 2.77:1 against the brightest tenth of it, under the 3.5:1
     floor even with the standard halo. Raised to the documented
     0.20/0.38 for THIS lesson only. --bg-opacity stays at 0.72 — the
     artwork is not the problem, the sky is. */
  --wash-mid : rgba(0,0,0,0.20);
  --wash-edge: rgba(0,0,0,0.38);
}
'''

# Verbs that never take -ize in any variety of English, so the tolerance
# below must not touch them. None of them is an answer today; the list is
# here so that a later edit cannot quietly turn `advise` into `advize`.
NEVER_IZE = {
    'advertise', 'advise', 'arise', 'chastise', 'circumcise', 'comprise',
    'compromise', 'demise', 'despise', 'devise', 'disguise', 'excise',
    'exercise', 'franchise', 'improvise', 'incise', 'merchandise', 'precise',
    'premise', 'promise', 'revise', 'rise', 'supervise', 'surmise',
    'surprise', 'televise', 'wise',
}
_ISE = re.compile(r'\b(\w{3,}?)is(e|ed|es|ing|ation)\b')


def alts(*answers):
    """Every genuinely correct spelling of a gap answer, one string.

    The engine lowercases and collapses whitespace on the learner's side
    but compares against the authored string as written, so the three
    tolerances the audit asked for are produced here instead of in an
    engine thirty lessons share: whitespace collapsed, the curly
    apostrophe an iOS keyboard produces accepted against the straight
    one, and -ise/-ize accepted both ways. The first entry is canonical —
    it is what the feedback prints as the answer."""
    out = []
    for a in answers:
        a = re.sub(r'\s+', ' ', a).strip()
        assert a and '|' not in a, 'gap answer %r cannot contain a pipe' % a
        forms = [a]

        def swap(m):
            return m.group(0) if m.group(0).lower() in NEVER_IZE \
                else m.group(1) + 'iz' + m.group(2)
        z = _ISE.sub(swap, a)
        if z != a:
            forms.append(z)
        for f in list(forms):
            if "'" in f:
                forms.append(f.replace("'", '’'))
        for f in forms:
            if f not in out:
                out.append(f)
    return '|'.join(out)


# ── guards ─────────────────────────────────────────────────────────────
def assert_key_is_deranged(mc, label='MC'):
    """The old file's keys were [1,1,1,0,0] and nothing shuffled.

    Two of the four positions carried zero probability across the whole
    activity, the pattern was identical for every learner, and it
    survived a restart unchanged. This is a distribution, not a per-item
    fact, so it is measured across every multiple-choice item in the
    deck: all four positions used, none starved."""
    n = len(mc)
    keys = [q['correct'] for q in mc]
    counts = [keys.count(i) for i in range(4)]
    assert 0 not in counts, (
        '%s: position(s) %s never carry the key (%s)'
        % (label, [i for i, c in enumerate(counts) if not c], counts))
    assert max(counts) - min(counts) <= max(1, n // 5), (
        '%s: the key distribution is lopsided (%s)' % (label, counts))
    return counts


def assert_no_answer_is_shown(html):
    """Nothing may reveal an answer before it is given.

    The defect this replaces was a `placeholder` attribute holding the
    accepted answer verbatim, so the check is deliberately blunt: no
    scored input carries a placeholder at all, and no `data-answer`
    string appears anywhere else in the document."""
    for m in re.finditer(r'<input[^>]*class="gap"[^>]*>', html):
        assert 'placeholder' not in m.group(0), \
            'a gap input carries a placeholder: %s' % m.group(0)[:120]
    # And nothing a learner can read before answering may contain any
    # accepted answer — not just the canonical one. The check is per row
    # plus the slide's own head and hint, because two rows on one slide
    # legitimately discuss different words. `data-explain` is excluded:
    # it is an attribute, written into the page only after marking.
    def visible(chunk):
        return re.sub(r'<[^>]+>', ' ',
                      re.sub(r'data-explain="[^"]*"', '', chunk)).lower()

    for slide in re.findall(r'<section class="slide"[^>]*data-type="gap".*?'
                            r'</section>', html, re.S):
        chunks = slide.split('<div class="card gap-row"')
        head = visible(chunks[0])
        for chunk in chunks[1:]:
            found = re.findall(r'data-answer="([^"]+)"', chunk)
            assert len(found) == 1, 'one gap per row, or scoring loses one'
            text = head + ' ' + visible(chunk)
            for alt in found[0].split('|'):
                assert alt.lower() not in text, \
                    'the accepted answer %r is readable before it is given' % alt


def mc_slide(i, total, q, ek, tk, folder='', bg=None):
    """D.mc, plus a per-distractor explanation.

    The shared builder writes one explanation per slide, which is what
    produced identical feedback for right and wrong on fifteen of the
    twenty items this replaces. Rather than change a builder thirty
    lessons share, the attribute is injected here: each wrong option says
    why *it* is wrong and the key falls through to the slide's own
    `why`. The engine already prefers an option's own explanation."""
    html = D.mc(i, total, q, ek, E[ek], tk, E[tk], folder=folder, bg=bg)
    ex = q['opt_why']
    assert len(ex) == len(q['options']), 'opt_why must line up with options'
    assert ex[q['correct']] is None, 'the key takes the slide explanation'
    assert all(x for n, x in enumerate(ex) if n != q['correct']), \
        'every distractor needs its own explanation'
    parts = html.split('<button class="opt"')
    out = [parts[0]]
    for n, chunk in enumerate(parts[1:]):
        attr = ' data-explain="%s"' % D.esc(ex[n]) if ex[n] else ''
        out.append('<button class="opt"%s%s' % (attr, chunk))
    return ''.join(out)


def teach(ek, tk, cards, cols=None):
    """cards: list of (head_key_or_None, body_html, note_key_or_None)."""
    return D.teach(ek, E[ek], tk, E[tk],
                   [(hk, E[hk] if hk else '', body, nk, E[nk] if nk else None)
                    for hk, body, nk in cards],
                   cols=cols, folder=F)


# ══ ACTIVITY 1 — five multiple-choice items ════════════════════════════
# Every distractor is a well-formed English sentence that is wrong for a
# reason taught on a slide. In the old set, three of the four items had
# three ill-formed distractors each and could be answered by ear.
MC = [
    # Reported speech: deixis. Key at index 2.
    dict(correct=2,
         stem='On the day of the shoot Clarkson told the producer: '
              '<em>&ldquo;I am filming the review here today.&rdquo;</em> '
              'A month later, in London, which report is correct?',
         options=[
             'Clarkson told the producer that he was filming the review here '
             'today.',
             'Clarkson told the producer that he had filmed the review there '
             'that day.',
             'Clarkson told the producer that he was filming the review there '
             'that day.',
             'Clarkson told the producer that I was filming the review there '
             'on that day.'],
         why='The present continuous steps back to the past continuous, and '
             'the pointing words move with it: <em>here &rarr; there</em>, '
             '<em>today &rarr; that day</em>, <em>I &rarr; he</em>.',
         opt_why=[
             'Every tense is right, but <em>here</em> and <em>today</em> still '
             'point at the track on the day of the shoot. A month later in '
             'London they point at the wrong place and the wrong day.',
             'The past perfect says the filming was already finished before he '
             'spoke. He was in the middle of it, so the present continuous '
             'steps back only as far as the past continuous.',
             None,
             '<em>I</em> still refers to whoever is speaking now, so this '
             'reports that <strong>you</strong> were filming. The pronoun '
             'shifts with the speaker: <em>I &rarr; he</em>.']),

    # Reported speech: present perfect. Key at index 0.
    dict(correct=0,
         stem='In 2013 the producers announced: <em>&ldquo;Top Gear has been '
              'the most widely watched factual programme in the '
              'world.&rdquo;</em> Reporting that announcement today, which '
              'version is correct?',
         options=[
             'The producers announced that Top Gear had been the most widely '
             'watched factual programme.',
             'The producers announced that Top Gear has been the most widely '
             'watched factual programme.',
             'The producers announced that Top Gear was the most widely '
             'watched factual programme then.',
             'The producers announced that Top Gear would be the most widely '
             'watched factual programme.'],
         why='Present perfect steps back to past perfect. The un-shifted form '
             'is available while the statement is still being treated as true '
             'now &mdash; and this one belongs to 2013.',
         opt_why=[
             None,
             'Keeping the present perfect claims the record still stands as '
             'you write. The sentence reports what was said in 2013, so the '
             'perfect steps back: <em>has been &rarr; had been</em>.',
             'The past simple reports a finished period and drops the '
             '&ldquo;up to that point&rdquo; the perfect carried. That '
             'distinction is exactly what the past perfect preserves.',
             '<em>Would be</em> turns the announcement into a prediction. The '
             'producers were describing a record already held, not one they '
             'expected to hold.']),

    # Mixed conditional. Key at index 3.
    dict(correct=3,
         stem='Hammond&rsquo;s 2006 crash at Elvington is why the '
              'programme&rsquo;s safety rules are as strict as they are now. '
              'Which sentence states that as a <em>past condition with a '
              'present result</em>?',
         options=[
             'If Hammond hadn&rsquo;t crashed in 2006, the crew wouldn&rsquo;t '
             'have rebuilt the dragster afterwards.',
             'If Hammond didn&rsquo;t crash so often, the show wouldn&rsquo;t '
             'need such strict safety rules at all.',
             'If Hammond crashes again this year, the show will tighten its '
             'safety rules even further.',
             'If Hammond hadn&rsquo;t crashed in 2006, the show wouldn&rsquo;t '
             'have such strict safety rules today.'],
         why='Mixed conditional: <em>if</em> + past perfect for the past '
             'condition, <em>would</em> + infinitive for the result that is '
             'still true today.',
         opt_why=[
             'A third conditional. The <em>if</em>-clause is right, but '
             '<em>wouldn&rsquo;t have rebuilt</em> puts the result back in the '
             'past, and the question asks for a result that holds now.',
             'A second conditional. <em>Didn&rsquo;t crash</em> describes an '
             'unreal present habit rather than the one event of 2006.',
             'A first conditional &mdash; a real future condition. Nothing '
             'here is unreal, and nothing here is about 2006.',
             None]),

    # It-cleft. Key at index 1.
    dict(correct=1,
         stem='Which sentence is an <em>it-cleft</em> that puts the spotlight '
              'on <em>the chemistry between the three of them</em>?',
         options=[
             'What makes the programme work is the chemistry between the three '
             'of them.',
             'It is the chemistry between the three of them that makes the '
             'programme work.',
             'The chemistry between the three of them is what makes the '
             'programme work.',
             'It was the three of them who gave the programme the chemistry it '
             'needed.'],
         why='<em>It</em> + <em>be</em> + focus + <em>that</em>/<em>who</em> + '
             'the rest. The chemistry sits in the focus slot, so that is what '
             'is emphasised.',
         opt_why=[
             'A wh-cleft, and a good sentence &mdash; but it opens with '
             '<em>What</em> and holds the focus back to the end. The question '
             'asks for the <em>it</em>-frame.',
             None,
             'A reversed wh-cleft: the focus comes first and <em>what</em> '
             'follows it. Still not <em>It + be + focus + that</em>.',
             'This is an it-cleft, but the spotlight falls on <strong>the '
             'three of them</strong>, not on the chemistry. Whatever sits '
             'between <em>was</em> and <em>who</em> is the focus.']),

    # Complex passive + stative. Key at index 0.
    dict(correct=0,
         stem='Aviation is a documented enthusiasm of James May&rsquo;s. Which '
              'sentence reports that as a passive with <em>James May</em> as '
              'its subject?',
         options=[
             'James May is known to have a serious interest in aviation '
             'history.',
             'It is known that James May has a serious interest in aviation '
             'history.',
             'People know James May to have a serious interest in aviation '
             'history.',
             'James May is being known to have a serious interest in aviation '
             'history.'],
         why='Subject + passive reporting verb + <em>to</em> + infinitive. The '
             'subject of the report is the person the claim is about.',
         opt_why=[
             None,
             'Correct English, and the other complex-passive pattern &mdash; '
             'but its subject is the empty <em>It</em>, and the question asks '
             'for <em>James May</em> in that slot.',
             'Grammatical and rather formal, but active: <em>people</em> are '
             'doing the knowing. A passive report leaves them out of it.',
             '<em>Know</em> is a stative verb &mdash; it names a state, not an '
             'activity &mdash; so it takes no continuous form, active or '
             'passive. <em>Is known</em>, never <em>is being known</em>.']),
]

# ══ ACTIVITY 2 — five gap-fill items ═══════════════════════════════════
GAPS = [
    ('g1h', 'A BBC spokesperson told journalists that the decision ______ '
            'after a thorough internal review.',
     alts('had been made', 'was made'),
     'Past simple passive backshifts to past perfect passive: <em>had been</em> '
     '+ past participle. Leaving it as <em>was made</em> is also correct '
     'English &mdash; a past simple may stay where it is &mdash; so both are '
     'marked right.', 240),

    ('g2h', 'If the presenters ______ to Amazon, The Grand Tour would never '
            'have existed.',
     alts('had not moved', "hadn't moved"),
     'Third conditional: <em>if</em> + past perfect. They did move and the '
     'programme did come about, so both halves are unreal. <em>Would have</em> '
     'can never appear in the <em>if</em>-clause.', 240),

    ('g3h', 'The Grand Tour ______ Amazon&rsquo;s record for the biggest '
            'premiere on the service.',
     alts('is reported to have broken', 'was reported to have broken',
          'has been reported to have broken', 'is said to have broken',
          'is believed to have broken'),
     '<em>is</em> + past participle of the reporting verb + <em>to have</em> + '
     'past participle. The perfect infinitive puts the premiere before the '
     'reporting &mdash; and the hedge is doing real work, because Amazon has '
     'never published a figure.', 330),

    ('g4h', 'It ______ set every timed lap on the Power Lap board.',
     alts('was the Stig who', 'was the Stig that'),
     'It-cleft: <em>It + was + focus + who/that</em>. <em>Who</em> is the usual '
     'choice for a person; <em>that</em> is also correct.', 240),

    ('g5h', 'A crew member said that the team ______ the whole segment in one '
            'day if the rain had held off.',
     alts('would have filmed', 'would have shot'),
     'The conditional perfect &mdash; <em>would have</em> + past participle '
     '&mdash; is already past and already unreal, so reporting it changes '
     'nothing. Nothing backshifts here.', 240),
]

# ══ ACTIVITY 3 — five error-correction items, six gaps ═════════════════
# The first is two rows, so it is worth two points. The old item put two
# errors behind one all-or-nothing point and told the learner, in its own
# instruction box, that each sentence contained "exactly one".
ERRORS = [
    ('e1h', [
        ('It was the Bugatti Veyron <s>what</s> ______ Clarkson called the '
         'greatest car ever made.',
         alts('that', 'which'),
         'Inside an it-cleft the link is <em>that</em> or <em>which</em>, never '
         '<em>what</em>. <em>What</em> already means <em>the thing that</em>, '
         'and <em>It</em> has done that job.'),
        ('The hosts are genuinely enthusiastic about cars, <s>which it is</s> '
         '______ rare on television.',
         alts('which is'),
         '<em>Which</em> is the subject of its own clause, so no second subject '
         'may follow it. <em>Which it is</em> has two.')], 240),

    ('e2h', [
        ('If the crew <s>would have checked</s> ______ the forecast, they might '
         'not have lost a day of filming.',
         alts('had checked'),
         '<em>Would have</em> belongs in the result clause only. The '
         '<em>if</em>-clause of a third conditional takes the past perfect.')],
     240),

    ('e3h', [
        ('The show <s>is thought that it revolutionised</s> ______ automotive '
         'journalism.',
         alts('is thought to have revolutionised',
              'is believed to have revolutionised',
              'is considered to have revolutionised',
              'is said to have revolutionised'),
         'Two patterns exist and this mixes them. Either <em>It is thought that '
         'the show revolutionised&hellip;</em> or <em>The show is thought to '
         'have revolutionised&hellip;</em> &mdash; with the subject at the '
         'front, the reporting verb takes a perfect infinitive.')], 380),

    ('e4h', [
        ('James May <s>is being known</s> ______ to have a serious interest in '
         'aviation history.',
         alts('is known'),
         '<em>Know</em> is stative: it names a state, not an activity, so it '
         'has no continuous form. The passive report is <em>is known</em>.')],
     240),

    ('e5h', [
        ('Clarkson told the crew that he would test <s>this car here '
         'tomorrow</s> ______.',
         alts('that car there the next day', 'that car there the following day'),
         'The tense was already right. What had to move were the pointing '
         'words: <em>this &rarr; that</em>, <em>here &rarr; there</em>, '
         '<em>tomorrow &rarr; the next day</em> &mdash; because the report is '
         'made a week later and somewhere else.')], 340),
]

# ══ ACTIVITY 4 — five "identify the structure" items ═══════════════════
# These five replace the matching board, which could not be lost and
# overflowed the canvas by 2px at house-style type. Two of its labels were
# also wrong: an it-cleft does not "emphasise the subject of the action"
# (the lesson's own Veyron sentence focuses an object), and a direct
# quotation is not reported speech.
L_REP = 'Reported speech &mdash; a reporting verb and a backshifted ' \
        '<em>that</em>-clause'
L_MIX = 'Mixed conditional &mdash; a past condition with a result that is ' \
        'true now'
L_3RD = 'Third conditional &mdash; a past condition with a past result that ' \
        'did not happen'
L_IT = 'It-cleft &mdash; <em>It</em> + <em>be</em> + focus + <em>that</em> ' \
       'or <em>who</em>'
L_WH = 'Wh-cleft &mdash; <em>What</em> + clause + <em>be</em> + focus'
L_PAS = 'Complex passive &mdash; a passive reporting verb followed by an ' \
        'infinitive'
L_ITH = 'Complex passive &mdash; <em>It is thought that</em> plus a clause ' \
        'with its own subject'
L_REL = 'Relative clause &mdash; <em>which</em> as the subject of its own ' \
        'clause'

W_NOCOND = 'No <em>if</em>, no condition, and nothing unreal in the sentence.'
W_NOTIT = 'An it-cleft opens with <em>It</em> + <em>be</em> + the focus. This '\
          'sentence opens with its own real subject.'

IDENT = [
    # Key at index 3.
    dict(correct=3,
         stem='<em>He announced that he was resigning from the programme with '
              'immediate effect.</em>',
         options=[L_PAS, L_MIX, L_IT, L_REP],
         why='<em>Announced</em> is the reporting verb, and <em>was '
             'resigning</em> is the backshifted present continuous of '
             '<em>&ldquo;I am resigning&rdquo;</em>.',
         opt_why=[
             'A complex passive needs a passive reporting verb &mdash; <em>is '
             'said</em>, <em>is thought</em>. Here <em>announced</em> is '
             'active and the speaker is named.',
             W_NOCOND + ' This reports something that actually happened.',
             W_NOTIT, None]),

    # Key at index 1.
    dict(correct=1,
         stem='<em>If Hammond hadn&rsquo;t crashed in 2006, the safety rules '
              'would be looser today.</em>',
         options=[L_3RD, L_MIX, L_REP, L_WH],
         why='A past condition (<em>hadn&rsquo;t crashed</em>) with a present '
             'result (<em>would be</em>). The two halves belong to different '
             'times, which is what makes it mixed.',
         opt_why=[
             'A third conditional would put the result in the past as well '
             '&mdash; <em>would have been looser</em>. <em>Would be</em> '
             'points at now.',
             None,
             'Nothing is being reported: there is no reporting verb and no '
             '<em>that</em>-clause.',
             'A wh-cleft begins with <em>What</em> and ends on its focus. This '
             'begins with a condition.']),

    # Key at index 0.
    dict(correct=0,
         stem='<em>It was the Stig who set the fastest lap of the series.</em>',
         options=[L_IT, L_WH, L_ITH, L_MIX],
         why='<em>It + was + the Stig + who</em>. The focus sits between '
             '<em>was</em> and <em>who</em>, and <em>who</em> is used because '
             'the focus is a person.',
         opt_why=[
             None,
             'A wh-cleft would open with <em>What</em> and hold the focus to '
             'the end. This one names the focus in its third word.',
             'There is no reporting verb here and nothing passive. The Stig is '
             'doing the setting.',
             W_NOCOND]),

    # Key at index 2.
    dict(correct=2,
         stem='<em>The show is said to have changed motoring television for '
              'ever.</em>',
         options=[L_ITH, L_REP, L_PAS, L_IT],
         why='<em>is said</em> + <em>to have changed</em>: a passive reporting '
             'verb plus a perfect infinitive, because the change came before '
             'the reporting.',
         opt_why=[
             'The right family, the wrong pattern. <em>It is thought '
             'that&hellip;</em> keeps a full clause; this sentence has moved '
             '<em>the show</em> to the front and left an infinitive behind.',
             'There is a reporting verb, but it is passive and nobody is named '
             'as having said it. Reported speech tells you who spoke.',
             None,
             W_NOTIT]),

    # Key at index 3.
    dict(correct=3,
         stem='<em>What the three of them do best is argue about cars.</em>',
         options=[L_MIX, L_REL, L_IT, L_WH],
         why='<em>What</em> + clause + <em>be</em> + focus. The focus is '
             'everything after <em>is</em>, and it can be a clause: <em>argue '
             'about cars</em>.',
         opt_why=[
             W_NOCOND,
             'A relative clause describes a noun that has already appeared. '
             'Nothing at all precedes <em>What</em> here.',
             'An it-cleft would run <em>It is arguing about cars that they do '
             'best</em>. This one opens with <em>What</em>.',
             None]),
]


def build():
    key_spread = assert_key_is_deranged(MC + IDENT, 'all multiple choice')
    D.assert_no_key_is_longest(MC, 'Activity 1')
    D.assert_no_key_is_longest(IDENT, 'Activity 4')

    logo = D.logo_from(TPL)
    S = [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Time', E['chipTime']), ('Count', E['chipCount'])])]

    # ── 2. orientation ──
    S += [teach('tOrient', 'o1T', [
        ('o1a', 'What somebody said, folded into a sentence of your own: '
                '<em>He said that he was leaving.</em> The tenses usually step '
                'back one.', None),
        ('o1b', 'Two of them here: the third (<em>if</em> + past perfect '
                '&rarr; <em>would have</em>) and the mixed, where a past '
                'condition has a result that is true now.', None),
        ('o1c', 'A sentence deliberately split in two so that one part takes '
                'the spotlight: <em>It was the Stig who&hellip;</em>, '
                '<em>What I like is&hellip;</em>', None),
        ('o1d', 'Reporting what people say without naming any of them: <em>It '
                'is thought that&hellip;</em>, <em>The show is said to '
                'have&hellip;</em>', 'o1n')], cols='1fr 1fr')]

    # ── 3. terminology ──
    S += [teach('tOrient', 'o2T', [
        ('o2a', 'the verb carrying the report: <em>say, tell, announce, claim, '
                'admit, deny</em>', None),
        ('o2b', 'the step back in tense a report takes after a past reporting '
                'verb', None),
        ('o2c', '<em>to have</em> + past participle &mdash; for an event '
                'earlier than the report', None),
        ('o2d', 'a sentence split in two so that one part is pushed into the '
                'spotlight', None),
        ('o2e', 'the part the cleft puts in that spotlight', None),
        ('o2f', 'what follows <em>be</em> and completes it: <em>What I like '
                '<strong>is the noise</strong></em>', 'o2n')],
        cols='1fr 1fr 1fr')]

    # ── 4. the backshift table ──
    row = ('<tr><td>%s</td><td class="arw">&rarr;</td><td>%s</td></tr>')
    table = ('<table class="gtab">'
             + row % ('<span class="t-pres">present simple</span> &mdash; '
                      '<em>&ldquo;I love that car&rdquo;</em>',
                      '<span class="t-past">past simple</span> &mdash; '
                      '<em>he loved that car</em>')
             + row % ('<span class="t-past">past simple</span> &mdash; '
                      '<em>&ldquo;I drove it&rdquo;</em>',
                      '<span class="t-pperf">past perfect</span> &mdash; '
                      '<em>he had driven it</em>')
             # Present perfect is left uncoloured on purpose. It has its
             # own colour in tense-palette.css, but §5a caps a slide at
             # three, and painting it with the present-simple navy would
             # say it is the present simple.
             + row % ('present perfect &mdash; '
                      '<em>&ldquo;I have driven it&rdquo;</em>',
                      '<span class="t-pperf">past perfect</span> &mdash; '
                      '<em>he had driven it</em>')
             + row % ('<em>&ldquo;I will test it&rdquo;</em>',
                      '<em>he would test it</em>')
             + row % ('<em>&ldquo;I can test it&rdquo;</em>',
                      '<em>he could test it</em>')
             + row % ('<em>&ldquo;I must test it&rdquo;</em>',
                      '<em>he had to test it</em>')
             + '</table>')
    S += [teach('tRep', 'r1T', [('r1a', table, 'r1n')], cols='1fr')]

    # ── 5. what does not backshift ──
    S += [teach('tRep', 'r2T', [
        ('r2a', '<em>Clarkson said that he <strong>loves</strong> fast '
                'cars.</em> The liking has not stopped, so the present may '
                'stay.', None),
        ('r2b', '<em>She has just said that the shoot <strong>starts</strong> '
                'at six.</em> No time has passed, so nothing needs to move.',
         None),
        ('r2c', '<em>would, could, should, might, ought to, had to</em> '
                'have nowhere further back to go.', 'r2n')],
        cols='1fr 1fr 1fr')]

    # ── 6. pronouns, time and place ──
    S += [teach('tRep', 'r3T', [
        ('r3a', '<em>I &rarr; he/she</em> &middot; <em>we &rarr; they</em> '
                '&middot; <em>my &rarr; his/her</em> &middot; <em>this car '
                '&rarr; that car</em> &middot; <em>these &rarr; those</em>',
         None),
        ('r3b', '<em>now &rarr; then</em> &middot; <em>today &rarr; that '
                'day</em> &middot; <em>tomorrow &rarr; the next day</em> '
                '&middot; <em>yesterday &rarr; the day before</em> &middot; '
                '<em>here &rarr; there</em>', 'r3n')], cols='1fr 1fr')]

    # ── 7. third conditional ──
    S += [teach('tCond', 'c1T', [
        ('c1a', '<em><strong>If</strong> + past perfect</em> &nbsp;&rarr;&nbsp; '
                '<em><strong>would have</strong> + past participle</em>', None),
        ('c1b', 'A past that did not happen, and the past result it would have '
                'had. <em>If the crew had checked the forecast, they would not '
                'have lost a day.</em>', 'c1n')], cols='1fr 1fr')]

    # ── 8. mixed conditional ──
    S += [teach('tCond', 'c2T', [
        ('c2a', '<em>If Hammond had not crashed in 2006, the crew '
                '<strong>would not have rebuilt</strong> the dragster.</em>',
         None),
        ('c2b', '<em>If Hammond had not crashed in 2006, the show '
                '<strong>would not have</strong> such strict safety rules '
                'today.</em>', 'c2n')], cols='1fr 1fr')]

    # ── 9. what cannot go in an if-clause ──
    S += [teach('tCond', 'c3T', [
        ('c3a', '<s class="eg-no">If Clarkson would have checked&hellip;</s> '
                '&nbsp;&rarr;&nbsp; <em class="eg-ok">If Clarkson had '
                'checked&hellip;</em>', None),
        ('c3b', '<s class="eg-no">If it will rain tomorrow&hellip;</s> '
                '&nbsp;&rarr;&nbsp; <em class="eg-ok">If it rains '
                'tomorrow&hellip;</em>', 'c3n')], cols='1fr 1fr')]

    # ── 10. it-clefts ──
    S += [teach('tCleft', 'f1T', [
        ('f1a', '<em>It</em> + <em>be</em> + <strong>focus</strong> + '
                '<em>that</em>/<em>who</em> + the rest of the sentence.', None),
        ('f1b', 'a person: <em>It was <strong>the Stig</strong> who set the '
                'lap.</em><br>an object: <em>It was <strong>the Veyron</strong> '
                'that he called the greatest.</em><br>a time: <em>It was '
                '<strong>in 2006</strong> that Hammond crashed.</em>', 'f1n')],
        cols='1fr 1fr')]

    # ── 11. wh-clefts ──
    S += [teach('tCleft', 'f2T', [
        ('f2a', '<em>What</em> + clause + <em>be</em> + <strong>focus</strong>. '
                '<em>What I like is the arguing.</em>', None),
        ('f2b', 'The it-cleft names the focus first; the wh-cleft makes you '
                'wait for it. <em>It is the arguing that I like</em> / '
                '<em>What I like is the arguing.</em>', 'f2n')],
        cols='1fr 1fr')]

    # ── 12. that / which, never what ──
    S += [teach('tCleft', 'f3T', [
        ('f3a', '<em>It was the Veyron <strong>that</strong> he called the '
                'greatest car ever made.</em> Never <s class="eg-no">the '
                'Veyron what he called</s>.', None),
        ('f3b', '<em>What</em> belongs at the front of a wh-cleft, where it '
                'means <em>the thing that</em>. Inside an it-cleft that job has '
                'already been done by <em>It</em>.', 'f3n')], cols='1fr 1fr')]

    # ── 13. complex passive, pattern 1 ──
    S += [teach('tPass', 'p1T', [
        ('p1a', '<em>It</em> + <em>is/was</em> + <strong>said, thought, '
                'believed, reported, known</strong> + <em>that</em> + a full '
                'clause.', None),
        ('p1b', 'It reports an opinion without saying whose. <em>It is thought '
                'that the show changed motoring television.</em>', 'p1n')],
        cols='1fr 1fr')]

    # ── 14. complex passive, pattern 2 ──
    S += [teach('tPass', 'p2T', [
        ('p2a', '<em>The show <strong>is said to be</strong> the most watched '
                'of its kind.</em> Subject + passive reporting verb + '
                '<em>to</em> + infinitive.', None),
        ('p2b', '<em>The show <strong>is said to have changed</strong> motoring '
                'television.</em> The perfect infinitive puts the event before '
                'the report.', 'p2n')], cols='1fr 1fr')]

    # ── 15. stative verbs ──
    S += [teach('tPass', 'p3T', [
        ('p3a', '<em>know, believe, understand, mean, own, seem, prefer, '
                'need, belong</em>', None),
        ('p3b', '<em>James May <strong>is known</strong> to&hellip;</em> '
                '&mdash; never <s class="eg-no">is being known</s>.', 'p3n')],
        cols='1fr 1fr')]

    # ── Activity 1 ──
    S += [mc_slide(i + 1, len(MC), q, 'a1E', 'a1T', folder=F)
          for i, q in enumerate(MC)]

    # ── Activity 2 ──
    for n, (hk, sentence, answer, why, width) in enumerate(GAPS, 1):
        S += [D.gap(n, len(GAPS), [(sentence, [answer], why)], None,
                    'a2E', E['a2E'], 'a2T', E['a2T'], folder=F,
                    hint=E[hk], hint_key=hk, width=width, size=20)]

    # ── Activity 3 ──
    # Item 1 is two rows, so the engine counts it as two gaps and awards
    # two points. One row per gap is deliberate: `checkGaps` marks the
    # first `.gap` in each `.gap-row`, so two inputs inside one row would
    # leave the second unscoreable.
    for n, (hk, rows, width) in enumerate(ERRORS, 1):
        S += [D.gap(n, len(ERRORS),
                    [(s, [a], w) for s, a, w in rows], None,
                    'a3E', E['a3E'], 'a3T', E['a3T'], folder=F,
                    hint=E[hk], hint_key=hk, width=width, size=19)]

    # ── Activity 4 ──
    S += [mc_slide(i + 1, len(IDENT), q, 'a4E', 'a4T', folder=F)
          for i, q in enumerate(IDENT)]

    # ── results and activation ──
    S += [D.results(),
          D.activate(E['actTitle'], E['actUse'],
                     ['told me that&hellip;', 'had already + past participle',
                      'If &hellip; hadn&rsquo;t &hellip;, &hellip; would have '
                      '&hellip;',
                      'If &hellip; hadn&rsquo;t &hellip;, &hellip; would '
                      '&hellip; now',
                      'It was &hellip; who/that &hellip;',
                      'What &hellip; is &hellip;', 'It is thought that &hellip;',
                      'is said to have &hellip;'],
                     'Discussion &middot; in pairs', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'])]
    return S, key_spread


if __name__ == '__main__':
    slides, key_spread = build()
    body = "".join(slides)
    n = body.count('<section class="slide')
    body = body.replace('NN slides', '%d slides' % n)
    I.T['en']['chipCount'] = '%d slides' % n
    I.T['de']['chipCount'] = '%d Folien' % n

    s = D.assemble(TPL, OUT, body, PALETTE,
                   'Advanced Grammar in Context — B2', I)
    s = s.replace('</style>\n</head>', TENSE_VARS + CSS + '</style>\n</head>', 1)
    assert 'data:image' not in s, 'a base64 blob survived into the build'
    assert_no_answer_is_shown(s)
    open(OUT, 'w', encoding='utf-8').write(s)
    print('wrote %s — %d bytes, %d slides' % (OUT, len(s), n))
    print('MC key positions A/B/C/D: %s' % key_spread)
    print('scored points: %d mc + %d gaps + %d error gaps + %d identify = %d'
          % (len(MC), len(GAPS), sum(len(r) for _, r, _ in ERRORS), len(IDENT),
             len(MC) + len(GAPS) + sum(len(r) for _, r, _ in ERRORS)
             + len(IDENT)))
