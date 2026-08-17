# -*- coding: utf-8 -*-
"""Escape from Grammar Jail (B1) — the 45-question test, rebuilt as a deck.

`full_grammar_test.html` was a scrolling autograded page: an intro card,
fifteen coloured section banners and forty-five question cards stacked
under them, with no teaching stage anywhere. It is now a 16:9 deck at the
same filename, so the live URL does not move.

Ten languages, and none of them retranslated
--------------------------------------------
This is the most multilingual lesson on the site. Three i18n tables were
committed beside this builder when the page was still a scrolling test and
they remain the source of truth: `ui_i18n.json`, `sections_i18n.json` and
`all_questions_i18n.json`. The first two are mapped onto deck key names in
`i18n_full_grammar_test.py`. The third is the interesting one.

**`UI_I18N` cannot carry the per-question layer, so it does not.**
`all_questions_i18n.json` is, per language, a 45x2 array: an L1 rendering
of the question and an L1 grammar note. Two things stop it becoming
`data-i18n` keys. It has no `en` column — correctly, since the questions
are already English — and `check-lesson.js` resolves a `data-i18n` key by
asking whether `UI_I18N.en[key]` is *truthy*, so ninety keys whose English
value is the empty string would each report as unresolved. The table
therefore stays in its own structure inside the lesson, as `QUESTION_L1`,
and is wired to the same `#langSelect` the engine builds:

  * every question slide carries `<span class="q-l1" data-qi="N">`, filled
    with `QUESTION_L1[lang][N][0]` — the L1 rendering of the question,
    visible before answering. Empty for English, which is the honest
    English state: there is no first language to gloss into.
  * the L1 grammar note, `[N][1]`, is appended to every `data-explain` in
    that question's container — the slide-level one *and* each option's
    own — so it arrives with the feedback whichever answer was chosen.
    Appending to the attribute rather than to the rendered feedback means
    the engine keeps writing the feedback, unchanged.
  * one `change` listener on the selector, registered after the engine's,
    so `currentLang` is already updated when it runs.

Nothing in `lesson-template.html` or `deck.py` is touched to do this.

`?lang=` still works, and the Italian stub still lands
-----------------------------------------------------
`full_grammar_test_italian.html` is a stub redirecting to
`full_grammar_test.html?lang=it`, and the deck template has no notion of a
query parameter — it always boots English. Rather than teach the shared
template a lesson-specific trick, the lesson reads `?lang=` itself and
drives the engine through its own UI: it sets `#langSelect.value` and
dispatches a `change` event, which is exactly what a reader clicking the
menu does. The URL is then kept in step as the reader switches, so a
chosen language survives a reload or a shared link. The stub is rewritten
by this builder and is unchanged in behaviour.

`D.mc` has no `explains=` in this tree
--------------------------------------
`lesson-template/build/README.md` documents `mc(..., explains=[...])`, and
`d11d5e1` really did add it — along with `assemble()` deriving
`data-theme` from the palette. Both were **reverted by `807e19c`**, which
uploaded a `deck.py` built on a base that predated them. This is the same
stale-base clobber the handoff records five times for `library.html` and
`seo.py`; nobody had checked `deck.py`. The feature is gone from the file
even though the README, the commit message and the handoff all describe it
as present.

Restoring it is a `deck.py` change, and `deck.py` was explicitly out of
bounds for this build, so `explains=` is a real keyword argument here
instead — `mc()` below is a verbatim port of the clobbered function, not
an injection pass over `D.mc`'s output. **Restoring `explains=` and the
`data-theme` derivation to `deck.py` is a job of its own** and is filed in
`docs/HANDOFF.md`.

The audit — what the forty-five questions were doing wrong
----------------------------------------------------------
Every one of the six recurring defects was present.

1. **Key position: 30 of 30.** The page shuffled options at render time,
   but every multiple-choice and every find-the-mistake item had its key
   at index 0 in the source, so the data itself was unusable anywhere the
   shuffle was not running — a printout, a review screen, a future reuse.
   Keys here are spread across all four positions and the distribution is
   asserted at build time on top of the engine's runtime shuffle.
2. **Key length: 1 of 30.** Only Q26 (`She has already finished her lunch.`
   at 35 characters against a field of 31) cleared the ratio and the
   four-character floor. Fixed the house way — a distractor lengthened,
   the key untouched.
3. **Right and wrong printed the same string, 45 times out of 45.**
   `showFeedback()` wrote `q.feedbackEn` whatever the learner clicked, so
   a learner who picked a distractor was told why the key was right. All
   thirty multiple-choice items now carry a per-option explanation saying
   why *that* option is wrong; the key falls through to the slide's own.
4. **The rule existed only in the feedback.** There was no teaching stage
   at all: fifteen grammar topics, and the whole of the explanation was a
   coloured section banner with a two-word label on it. Fifteen teaching
   slides now come before the questions that use them, and everything the
   feedback strings asserted is stated on one of them first.
5. **Ten of the fifteen gap hints listed the answer first.**
   `might / might not / could` for **might**, `must / mustn't / have to`
   for **must**, and eight more. The hint sets are kept — they are what
   makes a production task B1 rather than B2 — but the answer's position
   inside its own set is now spread across all four slots and asserted.
6. **Four items marked correct English wrong, or could not be answered
   from their own text.** These are the ones worth naming:

   * *"It's Doris's book"* was presented as containing a mistake, keyed to
     `Doris'`, and explained as "when a name ends in -s, just add an
     apostrophe, no extra s". `Doris's` is standard in current British and
     American usage, and the item directly contradicted the gap two
     questions earlier, which teaches apostrophe + s. Replaced with a
     genuine plural-possessive error (`my parent's cars` for two parents).
   * *"A: I have a headache. B: So do I."* was marked wrong in favour of
     *So have I*. With lexical `have`, *So do I* is the ordinary answer.
     Replaced with a real So/Neither error: a negative statement echoed
     with *So have I* instead of *Neither have I*.
   * *"Have you ___ been to London?"* offered ever / never / yet /
     already. All four are grammatical there, and three were marked wrong.
     It now tests the thing its own explanation claimed to test —
     *ever* between the subject and the participle — with four positions
     of the same sentence.
   * *"I prefer the blue ___"* offered **dress** as a distractor. *I
     prefer the blue dress* is correct English. Replaced.

   Two more were tightened rather than replaced: Q21 gained *so far*, so
   that the past-simple distractor is genuinely wrong rather than merely
   less idiomatic, and Q42 now says B *agrees*, without which *Neither did
   I* was as defensible as the key.

   In the same pass, five gaps were marked wrong for correct English
   because only one spelling was accepted: **will not** for *won't*,
   **have to** for *must*, **may** for *might*, **nor** for *neither*, and
   the curly apostrophe in *Tom's*. All are accepted now. The alternatives
   are expanded at build time in `alts()`, not by changing the engine's
   `gapOk` — a lesson that deliberately tests one spelling against another
   would be broken by a blanket engine change.

Also fixed, and not on the list: **five English feedback strings carried a
German gloss inside them** — *"'might not' = vielleicht nicht"*, *"already
= schon"*, *"Whose = wessen"*, and two more. Invisible to a Spanish
learner and wrong for an English one. The L1 gloss is what
`all_questions_i18n.json` is for, and it already says all five, in nine
languages.

Artwork
-------
Cover `grammarjail/arrival.jpg`, dark theme (median luminance 0.269), the
palette pasted verbatim from `extract-palette.py` with every contrast row
PASS. Seven more images carry the escape across the deck as backgrounds,
uncaptioned: the cell door for the modals of obligation, the camera rig for
preferences and plans, the pipework for predictions and the past, the
lookout for the present perfect, the corridor for experience and quantity,
the getaway on skates for the pronoun sections, the climb for the adverbs
and the last section. `jail-test-room.jpg` keeps the orientation slide and
`escape-the-cliff.jpg` keeps the results screen, as they did before.

Slide budget: 64. One cover, one orientation, fifteen teaching slides,
forty-five question slides, results, activation.
"""
import json
import os
import re
import sys

sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D
import i18n_full_grammar_test as I

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
TPL = os.path.join(ROOT, 'lesson-template', 'lesson-template.html')
OUT = os.path.join(ROOT, 'full_grammar_test.html')
STUB = os.path.join(ROOT, 'full_grammar_test_italian.html')
F = 'grammarjail'
E = I.T['en']

QUESTION_L1 = json.load(
    open(os.path.join(HERE, 'all_questions_i18n.json'), encoding='utf-8'))

# Two items were rewritten because the rule they taught was wrong (see the
# audit above), so the committed L1 note for them no longer describes what
# is on the slide. These two — and only these two — are replaced. The
# other 43 x 9 notes and all 45 x 9 prompts are used exactly as committed;
# every rewritten item is a "Find the mistake" whose prompt column already
# reads "Find the mistake." in every language.
L1_NOTE_OVERRIDES = {
    38: {
        'de': "Mehrere Besitzer: erst der Plural (<b>parents</b>), dann der "
              "Apostroph hinter dem -s: <b>parents'</b>.",
        'it': "Più possessori: prima il plurale (<b>parents</b>), poi "
              "l'apostrofo dopo la -s: <b>parents'</b>.",
        'es': "Varios poseedores: primero el plural (<b>parents</b>) y luego "
              "el apóstrofo tras la -s: <b>parents'</b>.",
        'fr': "Plusieurs possesseurs : d'abord le pluriel (<b>parents</b>), "
              "puis l'apostrophe après le -s : <b>parents'</b>.",
        'ja': "所有者が複数のときは、まず複数形（<b>parents</b>）にしてから、"
              "-s の後ろにアポストロフィを付ける：<b>parents'</b>。",
        'zh': "有多个所有者时先用复数（<b>parents</b>），再在 -s 后面加撇号："
              "<b>parents'</b>。",
        'ar': "عند تعدّد المالكين: الجمع أولاً (<b>parents</b>) ثم الفاصلة "
              "العليا بعد الـ -s: <b>parents'</b>.",
        'ru': "Владельцев несколько: сначала множественное число "
              "(<b>parents</b>), затем апостроф после -s: <b>parents'</b>.",
        'pt': "Vários possuidores: primeiro o plural (<b>parents</b>) e "
              "depois o apóstrofo após o -s: <b>parents'</b>.",
    },
    44: {
        'de': "Verneinter Satz → <b>Neither</b> + dasselbe Hilfsverb + I. "
              "<b>So</b> antwortet nur auf einen positiven Satz.",
        'it': "Frase negativa → <b>Neither</b> + lo stesso ausiliare + I. "
              "<b>So</b> risponde solo a una frase positiva.",
        'es': "Frase negativa → <b>Neither</b> + el mismo auxiliar + I. "
              "<b>So</b> solo responde a una frase afirmativa.",
        'fr': "Phrase négative → <b>Neither</b> + le même auxiliaire + I. "
              "<b>So</b> ne répond qu'à une phrase affirmative.",
        'ja': "否定文には <b>Neither</b> + 同じ助動詞 + I。<b>So</b> は肯定文"
              "にしか使えない。",
        'zh': "否定句用 <b>Neither</b> + 相同的助动词 + I。<b>So</b> 只用来"
              "附和肯定句。",
        'ar': "الجملة المنفية ← <b>Neither</b> + نفس الفعل المساعد + I. أمّا "
              "<b>So</b> فللجملة المثبتة فقط.",
        'ru': "Отрицательное высказывание → <b>Neither</b> + тот же "
              "вспомогательный глагол + I. <b>So</b> отвечает только на "
              "утвердительное.",
        'pt': "Frase negativa → <b>Neither</b> + o mesmo auxiliar + I. "
              "<b>So</b> só responde a uma frase afirmativa.",
    },
}

# Derived mechanically from grammarjail/arrival.jpg:
#   python3 lesson-template/extract-palette.py grammarjail/arrival.jpg
# Pasted verbatim. Dark theme — the hero's median luminance is 0.269 — and
# every row of the contrast report PASSES, the weakest being border on
# surface at 2.95:1 against a 1.25 floor.
PALETTE = '''  --hero: url('%s/arrival.jpg');

  --void          : #0c1214;
  --surface       : #151e22;
  --surface2      : #1d2a2e;
  --border        : #b33f39;
  --text          : #f5f2f2;
  --text-dim      : #bfa4a3;
  --accent        : #ef6963;
  --accent-bright : #f9a5a1;
  --accent-dim    : #d9251d;
  --secondary     : #0f2831;
  --contrast      : #1ded92;''' % F

# The escape, in order: arrival, the cell, the cameras, the works, the
# lookout, the corridor, the run, the climb. Fifteen grammar sections ride
# across seven of them. Uncaptioned — nothing on a slide describes what is
# in the picture behind it.
SECTION_BG = ['cell-door.jpg'] * 3 + ['watched.jpg'] * 2 \
    + ['valves.jpg'] * 2 + ['lookout.jpg'] * 2 + ['corridor-cat.jpg'] * 2 \
    + ['skating.jpg'] * 2 + ['cliff-climb.jpg'] * 2


# ── mc(), with explains= as a real argument ────────────────────────────
def mc(i, total, q, eyebrow_key, eyebrow, title_key, title, folder='', bg=None,
       ctx=None, explains=None):
    """A verbatim port of `deck.mc` as it stood at `d11d5e1`.

    `explains` is one entry per option: why THAT option is wrong. `None`
    leaves an option to the slide-level explanation, which is where the
    key belongs. The engine already prefers an option's own explanation.

    This lives here rather than in `deck.py` because the argument was
    clobbered out of the shared builder by `807e19c` and `deck.py` is out
    of bounds for this build. See the module docstring.
    """
    if explains is not None and len(explains) != len(q['options']):
        raise AssertionError(
            'mc: %d explains for %d options — one per option, None to skip'
            % (len(explains), len(q['options'])))

    def _opt(n, o):
        attrs = ' data-correct' if n == q['correct'] else ''
        if explains is not None and explains[n]:
            attrs += ' data-explain="%s"' % D.esc(explains[n])
        return '<button class="opt"%s>%s</button>' % (attrs, o)

    opts = "\n          ".join(_opt(n, o) for n, o in enumerate(q['options']))
    return '''
    <section class="slide" data-type="mc"%s>
      <div class="slide-head"><div>
        <div class="eyebrow"><span data-i18n="%s">%s</span> &middot; %d / %d</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
%s        <p class="q-stem">%s</p>
        <div class="opts">
          %s
        </div>
        <p class="feedback" data-explain="%s"></p>
      </div>
    </section>
''' % (D._bg(folder, bg), eyebrow_key, eyebrow, i, total, title_key, title,
       ('        <p class="q-ctx">%s</p>\n' % ctx) if ctx else '',
       q['stem'], opts, D.esc(q['why']))


def alts(*forms):
    """Every spelling a marker should accept, expanded at build time.

    `gapOk` compares a trimmed, lower-cased, space-collapsed string against
    a pipe-separated list. It does not normalise apostrophes, so the curly
    one a phone produces has to be listed. Doing it in the data rather than
    in the engine keeps a lesson that deliberately tests one spelling
    against another possible."""
    out = []
    for f in forms:
        for v in (f, f.replace("'", '’')):
            if v not in out:
                out.append(v)
    return '|'.join(out)


# ══ the fifteen sections ═══════════════════════════════════════════════
# Each: two or three cards of rule + example, in English. The card bodies
# carry no data-i18n on purpose — this is the language being taught, and
# the house rule is that it stays English. The learner's own language
# arrives per question, from QUESTION_L1.
TEACH = [
    # 0 — might
    [('might',
      'Something is possible but not certain. <em>I might make pasta. It '
      'might rain later.</em>',
      'One form for every subject. <em>He mights</em> does not exist.'),
     ('might not',
      'The negative of a possibility. <em>She might not come &mdash; she has a '
      'cold.</em>',
      'No <em>to</em> after the modal, and the verb keeps its base form.')],
    # 1 — must / mustn't
    [('must',
      'An obligation, often one the speaker feels strongly about. <em>You must '
      'be home before ten.</em>',
      'Subject + <em>must</em> + base form, identical for everybody.'),
     ('mustn&rsquo;t',
      'A prohibition &mdash; the thing is forbidden. <em>You mustn&rsquo;t '
      'feed the animals.</em>',
      '<em>mustn&rsquo;t</em> and <em>don&rsquo;t have to</em> are opposites, '
      'not alternatives.')],
    # 2 — have to
    [('have to / has to',
      'An obligation that comes from outside: a rule, a timetable, a job. '
      '<em>He has to wear a uniform.</em>',
      'An ordinary verb, so it has a past: <em>I had to wear a uniform.</em>'),
     ('don&rsquo;t have to',
      'No necessity at all. <em>He works from home, so he doesn&rsquo;t have '
      'to drive.</em>',
      'Questions and negatives take <em>do</em> or <em>does</em>: <em>Do you '
      'have to work?</em>')],
    # 3 — like + -ing
    [('love / like / hate + -ing',
      '<em>My brother loves playing video games. She hates getting up '
      'early.</em>',
      'The <em>-ing</em> form is the safe choice after all three.'),
     ('Spelling',
      '<em>get &rarr; getting. run &rarr; running. swim &rarr; swimming.</em>',
      'One vowel between two consonants at the end: double the last letter.')],
    # 4 — be going to
    [('be going to',
      'A plan already made, or evidence you can see in front of you. <em>Look '
      'at those clouds. It&rsquo;s going to rain.</em>',
      '<em>be</em> is the part that changes: <em>I am, he is, we are</em>.'),
     ('and then the base form',
      '<em>She&rsquo;s going to study all weekend.</em>',
      'Never <em>going to studies</em>, never <em>going to studied</em>.')],
    # 5 — will / won't
    [('will',
      'A prediction, an offer, or a decision made as you speak. <em>I think '
      'she&rsquo;ll win.</em>',
      '<em>will</em> + base form, the same for every subject.'),
     ('won&rsquo;t',
      'The contraction of <em>will not</em>. <em>Don&rsquo;t worry &mdash; I '
      'won&rsquo;t forget.</em>',
      'Both are correct English; <em>won&rsquo;t</em> is the usual one in '
      'speech.')],
    # 6 — Past Simple
    [('Finished time',
      '<em>last Saturday, yesterday, in 2019, two hours ago.</em> <em>We went '
      'to the cinema last Saturday.</em>',
      'A finished time expression rules the present perfect out.'),
     ('Questions and negatives',
      '<em>Did she go to the party? She didn&rsquo;t go.</em>',
      '<em>did</em> already carries the past, so the main verb goes back to '
      'its base form.')],
    # 7 — Present Perfect
    [('have / has + past participle',
      '<em>I have eaten. My aunt has travelled to fifteen countries.</em>',
      'he, she and it take <em>has</em>. Everybody else takes <em>have</em>.'),
     ('The third form',
      '<em>see &rarr; saw &rarr; seen. go &rarr; went &rarr; gone. be &rarr; '
      'was &rarr; been.</em>',
      'The participle is the third form: <em>has seen</em>, never <em>has '
      'saw</em>.')],
    # 8 — already / yet / just
    [('already',
      'Sooner than expected, in a positive sentence. <em>I&rsquo;ve already '
      'eaten.</em>',
      'Between <em>have</em> and the participle.'),
     ('yet',
      'Negatives and questions only. <em>Have you finished yet?</em>',
      'At the end of the sentence.'),
     ('just',
      'A moment ago. <em>She&rsquo;s just left.</em>',
      'Between <em>have</em> and the participle, like <em>already</em>.')],
    # 9 — ever / never
    [('ever',
      'In questions about a whole life so far. <em>Have you ever been to '
      'London?</em>',
      'Between the subject and the participle &mdash; never at the end.'),
     ('never',
      'Negative on its own. <em>I&rsquo;ve never broken a bone.</em>',
      '<em>hasn&rsquo;t never</em> is a double negative, and English does not '
      'allow it.')],
    # 10 — some / any
    [('some',
      'Positive sentences, and offers or requests. <em>Would you like some '
      'tea?</em>',
      'A question does not change this: an offer still takes <em>some</em>.'),
     ('any',
      'Negatives and open questions. <em>We haven&rsquo;t got any milk '
      'left.</em>',
      'Uncountable nouns take no plural: <em>some information</em>, never '
      '<em>informations</em>.')],
    # 11 — one / ones
    [('one',
      'Stands in for a singular countable noun already mentioned. <em>I prefer '
      'the blue one.</em>',
      'It means another of the same kind. <em>it</em> would mean the very same '
      'thing.'),
     ('ones',
      'The plural stand-in. <em>The white ones or the black ones?</em>',
      'Match the noun you are replacing: <em>those ones</em>, never <em>those '
      'one</em>.')],
    # 12 — whose / possessive 's
    [('whose',
      'Asks who something belongs to. <em>Whose bag is this? &mdash; '
      'It&rsquo;s Sarah&rsquo;s.</em>',
      '<em>who&rsquo;s</em> is <em>who is</em>, and means something else '
      'entirely.'),
     ('&rsquo;s and s&rsquo;',
      'One owner: <em>Tom&rsquo;s keys</em>. Several owners: <em>my '
      'parents&rsquo; cars</em>.',
      'The apostrophe goes before the s for one, and after it for more than '
      'one.')],
    # 13 — Adverbs of manner
    [('Regular',
      '<em>quick &rarr; quickly. dangerous &rarr; dangerously.</em> Adjectives '
      'in <em>-y</em>: <em>happy &rarr; happily.</em>',
      'Drop the <em>y</em> and add <em>-ily</em>.'),
     ('Irregular',
      '<em>good &rarr; well. fast &rarr; fast. hard &rarr; hard.</em>',
      '<em>fastly</em> and <em>goodly</em> are not English words.')],
    # 14 — So / Neither
    [('So + auxiliary + I',
      'Agreeing with a positive statement. <em>I went to bed late. &mdash; So '
      'did I.</em>',
      'Copy the tense: <em>went</em> comes back as <em>did</em>.'),
     ('Neither + auxiliary + I',
      'Agreeing with a negative statement. <em>I can&rsquo;t stand horror '
      'films. &mdash; Neither can I.</em>',
      'The verb comes in front of <em>I</em>, as it does in a question.')],
]

# ══ the forty-five questions ═══════════════════════════════════════════
# qi is the index into all_questions_i18n.json and must not move: it is
# what binds a slide to its nine translations.
MC = [
    dict(qi=0, sec=0, correct=2,
         stem='I&rsquo;m not sure about dinner. I ______ make pasta.',
         options=['might to make', 'might makes', 'might make', 'mights make'],
         why='<strong>might</strong> + the base form. No <em>to</em>, no '
             '<em>-s</em>, whoever the subject is.',
         explains=[
             '<em>to</em> never follows a modal. This marks the verb twice '
             'over.',
             'The <em>-s</em> belongs to the present simple. After a modal the '
             'verb keeps its base form.',
             None,
             'A modal has one form for every subject. <em>mights</em> is not '
             'an English word.']),

    dict(qi=2, sec=0, correct=1,
         stem='Find the mistake: <i>&ldquo;It mights rain &mdash; take an '
              'umbrella.&rdquo;</i>',
         options=['It mights rain — take an umbrella.',
                  'It might rain — take an umbrella.',
                  'It might to rain — take an umbrella.',
                  'It is might rain — take an umbrella.'],
         why='<strong>might</strong> has one form for every subject, so it is '
             '<em>it might rain</em>.',
         explains=[
             'That is the sentence as it stands, and <em>mights</em> is the '
             'mistake in it.',
             None,
             'The <em>-s</em> is gone, but <em>to</em> after a modal is a '
             'second mistake.',
             '<em>is might</em> puts two verbs where one belongs. A modal '
             'never needs <em>be</em> in front of it.']),

    dict(qi=3, sec=1, correct=3,
         stem='You ______ feed the animals. It&rsquo;s against the rules.',
         options=['don&rsquo;t have to', 'shouldn&rsquo;t to', 'must not to',
                  'mustn&rsquo;t'],
         why='<strong>mustn&rsquo;t</strong> is a prohibition: the rules '
             'forbid it.',
         explains=[
             '<em>don&rsquo;t have to</em> means it is not necessary. The '
             'rules here forbid it, which is the opposite.',
             '<em>to</em> cannot follow a modal, and advice is not the same as '
             'a rule.',
             'The negative is right, but <em>to</em> after a modal is not '
             'English.',
             None]),

    dict(qi=5, sec=1, correct=2,
         stem='Find the mistake: <i>&ldquo;She musts finish her homework '
              'before dinner.&rdquo;</i>',
         options=['She musts finish her homework before dinner.',
                  'She must to finish her homework before dinner.',
                  'She must finish her homework before dinner.',
                  'She must finishes her homework before dinner.'],
         why='<strong>must</strong> takes no <em>-s</em>, and the verb after '
             'it stays in the base form.',
         explains=[
             'That is the sentence with the mistake still in it: '
             '<em>musts</em>.',
             'The <em>-s</em> is gone, but <em>to</em> after a modal is a new '
             'mistake.',
             None,
             'The modal is right now, but the <em>-s</em> has only moved onto '
             'the next verb.']),

    dict(qi=6, sec=2, correct=1,
         stem='He works from home, so he ______ drive to the office.',
         options=['mustn&rsquo;t', 'doesn&rsquo;t have to',
                  'don&rsquo;t have to', 'hasn&rsquo;t to'],
         why='<strong>doesn&rsquo;t have to</strong> &mdash; there is no '
             'necessity. Nothing here forbids driving.',
         explains=[
             '<em>mustn&rsquo;t</em> forbids. Working from home makes the '
             'drive unnecessary, not against the rules.',
             None,
             '<em>he</em> takes <em>doesn&rsquo;t</em>. <em>don&rsquo;t</em> '
             'goes with I, you, we and they.',
             '<em>have to</em> is an ordinary verb, so its negative needs '
             '<em>do</em>.']),

    dict(qi=8, sec=2, correct=0,
         stem='Find the mistake: <i>&ldquo;I have to wore a uniform at my old '
              'school.&rdquo;</i>',
         options=['I had to wear a uniform at my old school.',
                  'I have to wore a uniform at my old school.',
                  'I have to wearing a uniform at my old school.',
                  'I must wore a uniform at my old school.'],
         why='The past of <em>have to</em> is <strong>had to</strong>, and the '
             'verb after it returns to its base form.',
         explains=[
             None,
             'That is the sentence as it stands. <em>have to</em> cannot be '
             'followed by a past form.',
             '<em>have to</em> takes the base form, never <em>-ing</em>, and '
             'this leaves the sentence in the present.',
             '<em>must</em> has no past form of its own, and <em>wore</em> '
             'still cannot follow it.']),

    dict(qi=9, sec=3, correct=3,
         stem='My little brother ______ video games.',
         options=['loves to playing', 'love playing', 'loves play',
                  'loves playing'],
         why='After <em>love</em> the <strong>-ing</strong> form is the safe '
             'choice, and <em>brother</em> takes the <em>-s</em>.',
         explains=[
             '<em>to</em> and <em>-ing</em> cannot both be there. It is '
             '<em>loves to play</em> or <em>loves playing</em>.',
             '<em>My little brother</em> is he, so the verb needs its '
             '<em>-s</em>.',
             'A bare base form cannot follow <em>love</em>.',
             None]),

    dict(qi=11, sec=3, correct=2,
         stem='Find the mistake: <i>&ldquo;James likes run in the park every '
              'morning.&rdquo;</i>',
         options=['James likes run in the park every morning.',
                  'James likes to running in the park every morning.',
                  'James likes running in the park every morning.',
                  'James like running in the park every morning.'],
         why='After <em>like</em> the verb takes <strong>-ing</strong>. What '
             'it never takes is the bare base form.',
         explains=[
             'That is the sentence with the mistake in it: a bare base form '
             'after <em>likes</em>.',
             '<em>to</em> and <em>-ing</em> together is one form too many. '
             'Pick one.',
             None,
             'The <em>-ing</em> is right, but <em>James</em> is he and the '
             'verb has lost its <em>-s</em>.']),

    dict(qi=12, sec=4, correct=1,
         stem='Look at those clouds. It ______ rain.',
         options=['will going to', '&rsquo;s going to', 'go to', 'is going'],
         why='<strong>be + going to</strong> + base form. Evidence you can see '
             'points to <em>going to</em>.',
         explains=[
             '<em>will</em> and <em>going to</em> are two different futures. '
             'Use one or the other.',
             None,
             'That is the present simple of <em>go</em>, and it says nothing '
             'about a future event.',
             '<em>to</em> is missing. The structure is <em>be going '
             '<strong>to</strong></em> + base form.']),

    dict(qi=14, sec=4, correct=3,
         stem='Find the mistake: <i>&ldquo;She&rsquo;s going to studies all '
              'weekend.&rdquo;</i>',
         options=['She&rsquo;s going to studies all weekend.',
                  'She going to study all weekend.',
                  'She&rsquo;s going to studied all weekend.',
                  'She&rsquo;s going to study all weekend.'],
         why='After <em>going to</em> the verb is always the <strong>base '
             'form</strong> &mdash; no <em>-s</em>, no <em>-ed</em>.',
         explains=[
             'That is the sentence as written, and <em>studies</em> is the '
             'mistake in it.',
             'The verb is right now, but <em>be</em> has gone. <em>going '
             'to</em> cannot stand without it.',
             '<em>-ed</em> is a past form, and <em>going to</em> looks '
             'forward.',
             None]),

    dict(qi=15, sec=5, correct=0,
         stem='I think she ______ the competition &mdash; she&rsquo;s '
              'incredibly talented.',
         options=['&rsquo;ll win', '&rsquo;ll wins', 'will winning',
                  'won&rsquo;t win'],
         why='<strong>will</strong> + base form, the same for every subject.',
         explains=[
             None,
             'Nothing takes an <em>-s</em> after <em>will</em>. The modal '
             'already carries the person.',
             '<em>-ing</em> needs <em>be</em> in front of it. After a modal '
             'the verb is plain.',
             'Grammatical, but it predicts the opposite of what the rest of '
             'the sentence says.']),

    dict(qi=17, sec=5, correct=2,
         stem='Find the mistake: <i>&ldquo;He wills become a famous footballer '
              'one day.&rdquo;</i>',
         options=['He wills become a famous footballer one day.',
                  'He will becomes a famous footballer one day.',
                  'He will become a famous footballer one day.',
                  'He will became a famous footballer one day.'],
         why='<strong>will</strong> never takes <em>-s</em>, and the verb '
             'after it stays in its base form.',
         explains=[
             'That is the sentence with its mistake in it: <em>wills</em>.',
             'The <em>-s</em> has only moved. Neither word takes it.',
             None,
             '<em>became</em> is a past form, and <em>will</em> is talking '
             'about the future.']),

    dict(qi=18, sec=6, correct=1,
         stem='We ______ to the cinema last Saturday.',
         options=['have gone', 'went', 'gone', 'go'],
         why='<strong>went</strong> &mdash; <em>last Saturday</em> is finished '
             'time, and finished time takes the past simple.',
         explains=[
             'The present perfect cannot sit with a finished time expression '
             'like <em>last Saturday</em>.',
             None,
             '<em>gone</em> is the past participle and needs <em>have</em> or '
             '<em>has</em> in front of it.',
             'The present simple describes habits, and this is one finished '
             'evening.']),

    dict(qi=20, sec=6, correct=3,
         stem='Find the mistake: <i>&ldquo;Did she went to the party?&rdquo;'
              '</i>',
         options=['Did she went to the party?', 'Did she goes to the party?',
                  'Did she going to the party?', 'Did she go to the party?'],
         why='<strong>did</strong> already carries the past, so the main verb '
             'goes back to its base form.',
         explains=[
             'That is the sentence as written. Two past forms in one question '
             'is one too many.',
             '<em>did</em> takes the base form, and the <em>-s</em> belongs to '
             'the present simple anyway.',
             '<em>-ing</em> would need <em>was</em>, not <em>did</em>.',
             None]),

    dict(qi=21, sec=7, correct=2,
         stem='My aunt Jessica ______ to more than fifteen countries so far.',
         options=['have travelled', 'has travel', 'has travelled',
                  'travelled'],
         why='<strong>has travelled</strong> &mdash; <em>she</em> takes '
             '<em>has</em>, and <em>travel</em> doubles its <em>l</em>.',
         explains=[
             '<em>My aunt Jessica</em> is she, and she takes <em>has</em>.',
             '<em>has</em> needs a past participle after it, not a base form.',
             None,
             'The past simple would close the count off. <em>so far</em> says '
             'it is still running.']),

    dict(qi=23, sec=7, correct=1,
         stem='Find the mistake: <i>&ldquo;He has saw this film three '
              'times.&rdquo;</i>',
         options=['He has saw this film three times.',
                  'He has seen this film three times.',
                  'He have seen this film three times.',
                  'He has see this film three times.'],
         why='The past participle of <em>see</em> is <strong>seen</strong>. '
             '<em>saw</em> is the past simple.',
         explains=[
             'That is the sentence as written, and <em>saw</em> is the '
             'mistake.',
             None,
             'The participle is right now, but <em>he</em> takes '
             '<em>has</em>, not <em>have</em>.',
             '<em>see</em> is the base form. After <em>has</em> English needs '
             'the third form.']),

    dict(qi=24, sec=8, correct=0,
         stem='Don&rsquo;t make dinner &mdash; I&rsquo;ve ______ eaten.',
         options=['already', 'yet', 'just yet', 'never'],
         why='<strong>already</strong> sits between <em>have</em> and the '
             'participle, and says it happened sooner than expected.',
         explains=[
             None,
             '<em>yet</em> belongs to negatives and questions, and it goes at '
             'the end of the sentence.',
             '<em>just yet</em> only works after a negative: <em>not just '
             'yet</em>.',
             'That would say the meal has never happened, which is no reason '
             'to skip dinner.']),

    dict(qi=26, sec=8, correct=2,
         stem='Find the mistake: <i>&ldquo;She has yet finished her '
              'lunch.&rdquo;</i>',
         options=['She has yet finished her lunch.',
                  'She yet has finished her lunch.',
                  'She has already finished her lunch.',
                  'She has already finish her lunch.'],
         why='A positive statement takes <strong>already</strong>. '
             '<em>yet</em> only works in negatives and questions.',
         explains=[
             'That is the sentence as written, with <em>yet</em> in a positive '
             'statement.',
             'Moving <em>yet</em> does not help: it is the wrong word for a '
             'positive sentence.',
             None,
             'The right word, but <em>has</em> needs a participle after it.']),

    dict(qi=27, sec=9, correct=1,
         stem='You want to ask about a whole life, not about this week. Which '
              'one is correct English?',
         options=['Have you been ever to London?',
                  'Have you ever been to London?',
                  'Have ever you been to London?',
                  'Have you been to London ever?'],
         why='<strong>ever</strong> goes between the subject and the past '
             'participle: <em>have you ever been</em>.',
         explains=[
             '<em>ever</em> has to come before the participle, not after it.',
             None,
             'Nothing goes between the auxiliary and the subject in a '
             'question.',
             'End position is where <em>yet</em> goes. <em>ever</em> sits in '
             'front of the participle.']),

    dict(qi=29, sec=9, correct=0,
         stem='Find the mistake: <i>&ldquo;She hasn&rsquo;t never won a '
              'competition.&rdquo;</i>',
         options=['She has never won a competition.',
                  'She hasn&rsquo;t never won a competition.',
                  'She has never win a competition.',
                  'She hasn&rsquo;t ever not won a competition.'],
         why='<strong>never</strong> is already negative, so the auxiliary '
             'stays positive: <em>has never</em>.',
         explains=[
             None,
             'That is the sentence as written &mdash; two negatives doing one '
             'job.',
             'The double negative is gone, but <em>has</em> needs the '
             'participle <em>won</em>.',
             'Three negatives now, and they cancel each other into nonsense.']),

    dict(qi=30, sec=10, correct=2,
         stem='We haven&rsquo;t got ______ milk left.',
         options=['some', 'no any', 'any', 'much any'],
         why='A negative sentence takes <strong>any</strong>. <em>some</em> '
             'belongs to positives, offers and requests.',
         explains=[
             '<em>some</em> goes in positive sentences, and this one is '
             'already negative.',
             '<em>no</em> and <em>any</em> are both negating. One of them has '
             'to go.',
             None,
             '<em>much</em> and <em>any</em> cannot stack. <em>much milk</em> '
             'on its own would work.']),

    dict(qi=32, sec=10, correct=3,
         stem='Find the mistake: <i>&ldquo;I&rsquo;d like some informations, '
              'please.&rdquo;</i>',
         options=['I&rsquo;d like some informations, please.',
                  'I&rsquo;d like any information, please.',
                  'I&rsquo;d like some an information, please.',
                  'I&rsquo;d like some information, please.'],
         why='<strong>information</strong> is uncountable: no plural '
             '<em>-s</em>, and no <em>a</em> or <em>an</em> in front of it.',
         explains=[
             'That is the sentence as written. <em>informations</em> does not '
             'exist.',
             'The plural is gone, but a request takes <em>some</em>, not '
             '<em>any</em>.',
             '<em>an</em> cannot go with an uncountable noun, and it cannot '
             'follow <em>some</em> either.',
             None]),

    dict(qi=33, sec=11, correct=1,
         stem='I like the red dress, but I prefer the blue ______.',
         options=['ones', 'one', 'it', 'the one'],
         why='<strong>one</strong> stands in for a single countable noun '
             'already mentioned.',
         explains=[
             '<em>ones</em> is the plural, and there is one dress here.',
             None,
             '<em>it</em> would mean the red dress itself. <em>one</em> points '
             'at a different dress of the same kind.',
             '<em>the</em> is already in the sentence, so this repeats it.']),

    dict(qi=35, sec=11, correct=0,
         stem='Find the mistake: <i>&ldquo;I don&rsquo;t like these glasses. I '
              'prefer those one.&rdquo;</i>',
         options=['I don&rsquo;t like these glasses. I prefer those ones.',
                  'I don&rsquo;t like these glasses. I prefer those one.',
                  'I don&rsquo;t like these glasses. I prefer that ones.',
                  'I don&rsquo;t like these glasses. I prefer those it.'],
         why='<em>glasses</em> is plural, so its stand-in is plural too: '
             '<strong>those ones</strong>.',
         explains=[
             None,
             'That is the sentence as written: a plural <em>those</em> with a '
             'singular <em>one</em>.',
             '<em>that</em> is singular and <em>ones</em> is plural, so they '
             'still disagree.',
             '<em>it</em> is singular, and it points back at the same pair '
             'rather than at a different one.']),

    dict(qi=36, sec=12, correct=3,
         stem='______ bag is this? &mdash; It&rsquo;s Sarah&rsquo;s.',
         options=['Who&rsquo;s', 'Who', 'Which', 'Whose'],
         why='<strong>Whose</strong> asks who something belongs to, and the '
             'answer names an owner.',
         explains=[
             '<em>Who&rsquo;s</em> is <em>who is</em>, which would put two '
             'verbs in one question.',
             '<em>Who</em> asks about a person, not about an owner.',
             '<em>Which</em> asks you to pick from a set. The answer names an '
             'owner instead.',
             None]),

    dict(qi=38, sec=12, correct=2,
         stem='Find the mistake: <i>&ldquo;These are my parent&rsquo;s cars '
              '&mdash; they both drive to work.&rdquo;</i>',
         options=['These are my parent&rsquo;s cars — they both drive to work.',
                  'These are my parents cars — they both drive to work.',
                  'These are my parents&rsquo; cars — they both drive to work.',
                  'These are my parents&rsquo;s cars — they both drive to '
                  'work.'],
         why='Two owners, so the noun goes plural first and the apostrophe '
             'follows the <em>-s</em>: <strong>parents&rsquo;</strong>.',
         explains=[
             'That is the sentence as written. <em>parent&rsquo;s</em> is one '
             'parent, and the sentence says both of them drive.',
             'The plural is right, but with nothing marking possession these '
             'are two nouns side by side.',
             None,
             'A plural already ending in <em>-s</em> takes the apostrophe '
             'alone. No second s is added.']),

    dict(qi=39, sec=13, correct=0,
         stem='She did really ______ in the test &mdash; she got 98%!',
         options=['well', 'good', 'goodly', 'badly'],
         why='<strong>well</strong> is the adverb of <em>good</em>, and it '
             'describes how she did.',
         explains=[
             None,
             '<em>good</em> is the adjective. It describes a thing, not the '
             'way something is done.',
             '<em>goodly</em> is not a modern English word.',
             'The right kind of word, but 98% is not a bad result.']),

    dict(qi=41, sec=13, correct=1,
         stem='Find the mistake: <i>&ldquo;He drives fastly and '
              'dangerously.&rdquo;</i>',
         options=['He drives fastly and dangerous.',
                  'He drives fast and dangerously.',
                  'He drives fastly and dangerously.',
                  'He drives fast and dangerous.'],
         why='<strong>fast</strong> is both adjective and adverb, so it never '
             'takes <em>-ly</em>. <em>dangerously</em> does.',
         explains=[
             'Two mistakes at once: <em>fastly</em> does not exist, and '
             '<em>dangerous</em> has lost its <em>-ly</em>.',
             None,
             'That is the sentence as written, and <em>fastly</em> is the '
             'mistake in it.',
             '<em>fast</em> is right, but driving is described by adverbs and '
             '<em>dangerous</em> is an adjective.']),

    dict(qi=42, sec=14, correct=2,
         stem='A: &ldquo;I went to bed really late last night.&rdquo; &nbsp; B '
              'agrees: &ldquo;______&rdquo;',
         options=['So do I.', 'So have I.', 'So did I.', 'Neither did I.'],
         why='<strong>So did I.</strong> &mdash; the echo copies the tense: '
             '<em>went</em> comes back as <em>did</em>.',
         explains=[
             '<em>do</em> is present, and A is talking about last night.',
             '<em>have</em> would echo a present perfect, not a past simple.',
             None,
             '<em>Neither</em> agrees with a negative, and A&rsquo;s sentence '
             'is positive.']),

    dict(qi=44, sec=14, correct=3,
         stem='Find the mistake: <i>&ldquo;A: I have never been to Spain. '
              '&nbsp;B: So have I.&rdquo;</i>',
         options=['A: I have never been to Spain. B: So did I.',
                  'A: I have never been to Spain. B: Neither did I.',
                  'A: I have never been to Spain. B: So have I.',
                  'A: I have never been to Spain. B: Neither have I.'],
         why='A negative statement is echoed with <strong>Neither</strong>, '
             'and the auxiliary stays the one A used.',
         explains=[
             'Two problems: <em>So</em> follows a positive, and <em>did</em> '
             'does not echo <em>have been</em>.',
             '<em>Neither</em> is right, but the auxiliary has changed. A said '
             '<em>have</em>.',
             'That is the reply as written, and A&rsquo;s statement is '
             'negative.',
             None]),
]

# (qi, section, sentence, accepted answers, hint set, why)
# The hint set is target language, so it is not translated and it is not a
# `.bank-chip`: the answer's position inside it is spread across all four
# slots instead of sitting first, which it did in ten of the fifteen.
GAPS = [
    (1, 0, 'She ______ not come to the party &mdash; she has a cold.',
     alts('might', 'may'), ['could', 'might', 'may', 'might not'],
     '<strong>might not</strong> is "perhaps not". The modal keeps one form '
     'and the verb stays plain. <em>may</em> is accepted here too.'),
    (4, 1, 'You ______ be home before ten. It&rsquo;s a school night.',
     alts('must', 'have to'), ['have to', "mustn't", 'must'],
     '<strong>must</strong> states an obligation. <em>have to</em> says the '
     'same thing here and is accepted.'),
    (7, 2, '______ you have to work at the weekend?',
     alts('do'), ['does', 'have', 'do', 'must'],
     '<em>have to</em> is an ordinary verb, so a question needs '
     '<strong>do</strong> or <strong>does</strong> in front of it.'),
    (10, 3, 'She hates ______ up early on Saturdays.',
     alts('getting'), ['get', 'gets', 'to get', 'getting'],
     '<em>hate</em> takes the <strong>-ing</strong> form, and <em>get</em> '
     'doubles its <em>t</em>.'),
    (13, 4, 'We ______ not going to finish the project today.',
     alts('are'), ['are', 'am', 'is'],
     '<strong>are</strong> &mdash; <em>be</em> is the part of <em>going to</em> '
     'that agrees with the subject.'),
    (16, 5, 'Don&rsquo;t worry &mdash; I ______ forget your birthday.',
     alts("won't", 'will not'), ["wouldn't", 'will not', "won't"],
     '<strong>won&rsquo;t</strong> is the contraction of <em>will not</em>, '
     'and both are accepted.'),
    (19, 6, '______ you enjoy the concert last night?',
     alts('did'), ['have', 'was', 'do', 'did'],
     '<strong>Did</strong> + subject + base form. <em>last night</em> is '
     'finished time.'),
    (22, 7, 'I ______ never eaten sushi in my life.',
     alts('have'), ['has', 'have', 'had'],
     '<em>I</em> takes <strong>have</strong>, and <em>never</em> sits between '
     'it and the participle.'),
    (25, 8, 'Have you finished your homework ______?',
     alts('yet'), ['already', 'ever', 'just', 'yet'],
     '<strong>yet</strong> goes at the end of a question or a negative. A '
     'positive statement would take <em>already</em>.'),
    (28, 9, 'I&rsquo;ve ______ broken a bone &mdash; I&rsquo;ve been very '
            'lucky.',
     alts('never'), ['never', 'not', 'ever', 'yet'],
     '<strong>never</strong> makes the sentence negative by itself, so '
     '<em>not</em> would be one negative too many.'),
    (31, 10, 'Would you like ______ tea?',
     alts('some'), ['any', 'some'],
     'An offer takes <strong>some</strong>, even though the sentence is a '
     'question.'),
    (34, 11, 'Which trainers do you prefer &mdash; the white ones or the black '
             '______?',
     alts('ones'), ['them', 'one', 'ones'],
     '<em>trainers</em> is plural, so its stand-in is <strong>ones</strong>.'),
    (37, 12, 'These are Tom______ keys &mdash; he left them on the table.',
     alts("'s"), ["'s", 's', "s'"],
     'A singular name takes apostrophe + <strong>s</strong>: <em>Tom&rsquo;s '
     'keys</em>.'),
    (40, 13, 'The children were playing ______ outside. (happy)',
     alts('happily'), ['happy', 'happyly', 'happily'],
     'An adjective ending in <em>-y</em> drops the <em>y</em> and takes '
     '<strong>-ily</strong>.'),
    (43, 14, 'A: I can&rsquo;t stand horror films. &nbsp;B: ______ can I.',
     alts('neither', 'nor'), ['so', 'neither', 'nor'],
     'A negative statement is echoed with <strong>Neither</strong>. '
     '<em>Nor</em> is accepted as well.'),
]

# The activation strip. `check-lesson.js`'s BANK gate walks every
# `.bank-chip` on the page, and these are bank chips, so they are written
# as phrases rather than bare headwords: no chip is an exact match for a
# gap answer, which is also better production practice.
ACT_CHIPS = ['might not', 'you mustn&rsquo;t', 'doesn&rsquo;t have to',
             'loves playing', 'it&rsquo;s going to', 'I won&rsquo;t forget',
             'have you ever', 'not &hellip; yet', 'so did I',
             'neither can I']

CSS = '''
.q-ctx { margin: 0 0 4px; }
.q-l1 {
  display: block; min-height: 22px;
  font-family: var(--font-ui); font-size: 16px; line-height: 1.35;
  color: var(--accent-bright);
}
.gap-row .q-l1 { min-height: 0; margin-top: 6px; font-size: 15px; }
.gap-set {
  display: block; margin-top: 8px;
  font-family: var(--font-mono); font-size: 14px; letter-spacing: .04em;
  color: var(--text-dim);
}
.fb-l1 { display: block; margin-top: 3px; font-size: .9em; opacity: .85; }
'''

# Wired to the engine from outside it: nothing in lesson-template.html or
# deck.py changes. `currentLang` is a top-level `let` in a classic script,
# so it lives in the shared global lexical environment and a later script
# can read it. The change listener is registered after the engine's, so
# `currentLang` is already the new value by the time this runs.
SCRIPT = '''<script>
/* ── The per-question layer, in nine languages ─────────────────────────
   UI_I18N is a flat key/value table and this is a 45x2 array per language
   with no English column, so it does not fit there and is not forced in.
   It is wired to the same selector instead. See build_full_grammar_test.py.
   ─────────────────────────────────────────────────────────────────── */
const QUESTION_L1 = %s;

/* Each question's container: the whole slide for multiple choice, the row
   for a gap. The English explanation is kept as written so that switching
   language never appends a second note. */
const l1Targets = [...document.querySelectorAll('.q-l1[data-qi]')].map(el => {
  const box = el.closest('.gap-row') || el.closest('.slide');
  return {
    el, qi: +el.dataset.qi,
    explains: [...box.querySelectorAll('[data-explain]')].map(x => ({
      node: x, en: x.getAttribute('data-explain')
    }))
  };
});

function applyQuestionL1() {
  const table = QUESTION_L1[currentLang] || null;
  l1Targets.forEach(t => {
    const pair = table && table[t.qi];
    t.el.innerHTML = pair ? pair[0] : '';
    t.explains.forEach(x => x.node.setAttribute('data-explain',
      pair && pair[1] ? x.en + ' <span class="fb-l1">' + pair[1] + '</span>'
                      : x.en));
  });
}

/* ── ?lang=, without teaching the shared template about query strings ──
   full_grammar_test_italian.html redirects here with ?lang=it. Rather
   than patch the engine, drive it through the control a reader uses. */
(function () {
  const sel = document.getElementById('langSelect');
  sel.addEventListener('change', () => {
    applyQuestionL1();
    try {
      const u = new URL(location.href);
      u.searchParams.set('lang', currentLang);
      history.replaceState(null, '', u);
    } catch (e) { /* file:// — nothing to keep */ }
  });
  let want = null;
  try { want = new URLSearchParams(location.search).get('lang'); } catch (e) {}
  if (want && want !== sel.value &&
      [...sel.options].some(o => o.value === want)) {
    sel.value = want;
    sel.dispatchEvent(new Event('change'));
  } else {
    applyQuestionL1();
  }
})();
</script>'''

STUB_HTML = '''<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Escape from Grammar Jail — Forbes English</title>
<link rel="canonical" href="full_grammar_test.html">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0; url=full_grammar_test.html?lang=it">
<script>location.replace('full_grammar_test.html?lang=it');</script>
</head>
<body style="font-family:system-ui,sans-serif;background:#0c1214;color:#f5f2f2;
             display:grid;place-items:center;min-height:100vh;margin:0;
             text-align:center;padding:24px">
<p>Questa lezione vive in un unico file, con tutte le lingue.
<a href="full_grammar_test.html?lang=it" style="color:#ef6963">Continua qui</a>.</p>
</body>
</html>
'''


# ── guards ─────────────────────────────────────────────────────────────
def assert_key_is_deranged(mc, label='MC'):
    """Every key sat at index 0 — all thirty of them.

    A per-item fact cannot express what is wrong with that, so it is
    measured as a distribution over the whole deck: all four positions
    used, none starved. The engine shuffles at runtime as well; this is
    about the data being usable on its own."""
    n = len(mc)
    counts = [sum(1 for q in mc if q['correct'] == i) for i in range(4)]
    assert 0 not in counts, (
        '%s: position(s) %s never carry the key (%s)'
        % (label, [i for i, c in enumerate(counts) if not c], counts))
    assert max(counts) - min(counts) <= max(1, n // 5), (
        '%s: the key distribution is lopsided (%s)' % (label, counts))
    return counts


def assert_hint_position_is_deranged(gaps):
    """Ten of fifteen hint sets opened with their own answer."""
    pos = []
    for _, _, _, answers, hint, _ in gaps:
        first = answers.split('|')[0]
        assert first in hint, 'the answer %r is not in its own hint set' % first
        pos.append(hint.index(first))
    counts = [pos.count(i) for i in range(4)]
    assert 0 not in counts, (
        'hint sets: slot(s) %s never hold the answer (%s)'
        % ([i for i, c in enumerate(counts) if not c], counts))
    assert max(counts) - min(counts) <= 3, \
        'hint sets: the answer sits in one slot too often (%s)' % counts
    return counts


def assert_no_answer_is_shown(html):
    """No scored input may carry its answer — or anything else — as a
    placeholder, and one gap per row, always.

    `checkGaps` marks every input in a row now, but `maxScore` counts each
    `.gap` on the slide, and the pairing is only safe while a row holds
    exactly one. Both halves are cheap and both have shipped broken."""
    for m in re.finditer(r'<input[^>]*class="gap"[^>]*>', html):
        assert 'placeholder' not in m.group(0), \
            'a gap input carries a placeholder: %s' % m.group(0)[:120]
    n = 0
    for slide in re.findall(r'<section class="slide"[^>]*data-type="gap".*?'
                            r'</section>', html, re.S):
        for chunk in slide.split('<div class="card gap-row"')[1:]:
            found = re.findall(r'data-answer="([^"]+)"', chunk)
            assert len(found) == 1, 'one gap per row, or scoring loses one'
            n += 1
    return n


def assert_bank_is_not_a_key(html):
    """A build-time replica of check-lesson.js's BANK gate.

    The gate is page-wide, not per-slide: it walks every `.bank-chip` in
    document order, dedupes, and fails if the gap answers appear among
    them in gap order. Running the same algorithm here means a bank that
    would fail the checker fails the build first, and says why."""
    seen = []
    for m in re.finditer(r'<span class="bank-chip">(.*?)</span>', html, re.S):
        t = re.sub(r'\s+', ' ', m.group(1)).strip()
        if t and t not in seen:
            seen.append(t)
    answers = [m.group(1).split('|')[0].strip() for m in
               re.finditer(r'<input class="gap" data-answer="([^"]+)"', html)]
    found = [seen.index(a) for a in answers if a in seen]
    assert not (len(found) >= 2 and all(x < y for x, y in zip(found, found[1:]))), \
        'the bank chips list the gap answers in gap order (%s)' % found
    return len(seen)


def assert_no_backward_reference(html):
    """Learner-facing text never mentions a previous version of a lesson."""
    body = re.sub(r'<script.*?</script>', '', html, flags=re.S)
    for phrase in ('old version', 'previous version', 'the old test',
                   'used to say', 'this lesson used to', 'earlier version'):
        assert phrase not in body.lower(), \
            'learner-facing text refers to a previous version: %r' % phrase


# ── slides ─────────────────────────────────────────────────────────────
def teach(n):
    return D.teach('sec%dE' % n, E['sec%dE' % n], 'sec%dT' % n,
                   E['sec%dT' % n],
                   [(None, head, body, None, note)
                    for head, body, note in TEACH[n]],
                   cols='1fr ' * len(TEACH[n]),
                   folder=F, bg=SECTION_BG[n])


def build():
    key_spread = assert_key_is_deranged(MC, 'all multiple choice')
    hint_spread = assert_hint_position_is_deranged(GAPS)
    D.assert_no_key_is_longest(MC, 'multiple choice')
    assert len(MC) + len(GAPS) == 45, 'forty-five questions, no more, no less'
    assert sorted(q['qi'] for q in MC) + sorted(g[0] for g in GAPS) != [], ''
    seen_qi = sorted([q['qi'] for q in MC] + [g[0] for g in GAPS])
    assert seen_qi == list(range(45)), \
        'the question indices must still map 1:1 onto the i18n tables'

    logo = D.logo_from(TPL)
    S = [D.cover(logo, E['coverTitle'], E['coverSub'],
                 [('Level', E['chipLevel']), ('Focus', E['chipFocus']),
                  ('Count', E['chipCount'])])]

    # ── orientation ──
    S += [D.teach('chipFocus', E['chipFocus'], 'orTitle', E['orTitle'], [
        ('orTagA', E['orTagA'],
         'Four options, shuffled every time the deck opens. Read the whole '
         'set before you choose.', None, None),
        ('orTagB', E['orTagB'],
         'Type the missing word into the box. The words under the sentence '
         'are the field to choose from.', None, None),
        ('orTagC', E['orTagC'],
         'One sentence, four versions. Three of them still have something '
         'wrong with them.', None,
         'Every answer is explained, right or wrong. Pick a support language '
         'from the menu at the top of the screen and the questions and the '
         'explanations arrive in it as well.'),
    ], cols='1fr 1fr 1fr', folder=F, bg='jail-test-room.jpg')]

    # ── the fifteen sections ──
    gaps_by_section = {}
    for g in GAPS:
        gaps_by_section.setdefault(g[1], []).append(g)
    mc_by_section = {}
    for q in MC:
        mc_by_section.setdefault(q['sec'], []).append(q)

    for n in range(15):
        S += [teach(n)]
        for q in mc_by_section[n]:
            S += [mc(q['qi'] + 1, 45, q, 'sec%dE' % n, E['sec%dE' % n],
                     'sec%dT' % n, E['sec%dT' % n], folder=F, bg=SECTION_BG[n],
                     ctx='<span class="q-l1" data-qi="%d"></span>' % q['qi'],
                     explains=q['explains'])]
        for qi, sec, sentence, answers, hint, why in gaps_by_section[n]:
            row = (sentence
                   + '<span class="gap-set">%s</span>'
                     % ' &middot; '.join(hint)
                   + '<span class="q-l1" data-qi="%d"></span>' % qi,
                   [answers], why)
            S += [D.gap(qi + 1, 45, [row], None, 'sec%dE' % n, E['sec%dE' % n],
                        'sec%dT' % n, E['sec%dT' % n], folder=F,
                        bg=SECTION_BG[n], width=170, size=23)]

    S += [D.results(folder=F, bg='escape-the-cliff.jpg'),
          D.activate(E['actTitle'], E['actUse'], ACT_CHIPS,
                     'Discussion &middot; in pairs', E['actSpeakBrief'],
                     [E['actSpeak1'], E['actSpeak2'], E['actSpeak3']],
                     E['actWriteKind'], E['actWriteBrief'],
                     E['actPlaceholder'], folder=F, bg='cliff-climb.jpg')]
    return S, key_spread, hint_spread


if __name__ == '__main__':
    slides, key_spread, hint_spread = build()
    body = "".join(slides)
    n = body.count('<section class="slide')

    l1 = {code: [[a, L1_NOTE_OVERRIDES.get(i, {}).get(code, b)]
                 for i, (a, b) in enumerate(rows)]
          for code, rows in QUESTION_L1.items()}
    for qi, table in L1_NOTE_OVERRIDES.items():
        for code in table:
            assert l1[code][qi][1] == table[code], 'override %d/%s' % (qi, code)
    assert set(l1) | {'en'} == set(I.LANGS), \
        'the per-question layer must cover every language but English'

    s = D.assemble(TPL, OUT, body, PALETTE,
                   'Escape from Grammar Jail (B1) | Forbes English', I,
                   langs=I.LANGS)
    s = s.replace('</style>\n</head>', CSS + '</style>\n</head>', 1)
    script = SCRIPT % json.dumps(l1, ensure_ascii=False)
    assert s.count('</script>\n</body>') == 1
    s = s.replace('</script>\n</body>', '</script>\n' + script + '\n</body>', 1)

    assert 'data:image' not in s, 'a base64 blob survived into the build'
    points = assert_no_answer_is_shown(s)
    chips = assert_bank_is_not_a_key(s)
    assert_no_backward_reference(s)
    # The five English feedback strings that carried a German gloss inside
    # them. Checked against the slide markup, which is the English layer;
    # the same words are legitimate inside UI_I18N.de and QUESTION_L1.de.
    for gone in ('vielleicht nicht', '= schon', 'wessen', 'nicht dürfen',
                 'nicht müssen', "in German"):
        assert gone not in body, \
            'a German gloss survived inside an English string: %r' % gone

    open(OUT, 'w', encoding='utf-8').write(s)
    open(STUB, 'w', encoding='utf-8').write(STUB_HTML)

    print('wrote %s — %d bytes, %d slides' % (os.path.basename(OUT), len(s), n))
    print('wrote %s — redirect to ?lang=it' % os.path.basename(STUB))
    print('MC key positions A/B/C/D: %s' % key_spread)
    print('gap-hint answer slots  : %s' % hint_spread)
    print('scored points: %d multiple choice + %d gaps = %d'
          % (len(MC), points, len(MC) + points))
    print('languages: %d complete, %d with a per-question layer'
          % (len(I.LANGS), len(l1)))
    print('bank chips on the page: %d' % chips)
