# -*- coding: utf-8 -*-
"""One harness for the whole descent: same page, different auxiliary."""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
sys.path.insert(0, 'lesson-template')
import passive_diagram as P
import passive_shapes as S
from build_c10 import assemble, hero, rule_grid, MARK_FLAG, MARK_TABLE, MARK_FORK, MARK_CLOCK, MARK_PANES
from build_c11_12_13 import chart, fork, signals, interactive, questions, js, palette

DARK_CSS = '''
  /* ── descent overrides: the three places the ascent hard-codes light ── */
  .diagram-panel.is-now{background:#1B2229;border-color:#33434F;}
  .opt-btn{background:var(--card);color:var(--ink);}
  .opt-btn:hover{filter:brightness(1.35);}
  .card,.rule-card,.chart-wrap,.signal-box,.diagram-card,.diagram-panel{box-shadow:0 2px 12px rgba(0,0,0,.45);}
'''


def build(t):
    """t: a dict describing one descent camp."""
    if t.get('shape'):
        fn = getattr(S, t['shape'])
        dia = lambda uid, groups=False: fn(uid, groups)
    else:
        dia = lambda uid, groups=False: P.descent(
            uid, t['stops'], t['bx'], t['block'], t['reveal'], 'BY&#8230;',
            t['ink'], t['ghost'], groups, t['aria'])

    camps = '''<div class="camp" id="rules">
      ''' + MARK_FLAG + '''
      <div class="camp-label">Descent briefing</div>
      <h2>When to use it</h2>
      <p class="chart-note" style="margin:-6px 0 18px">The passive is not a different tense. It is the ''' + t['tense'] + ''' with the doer let go &mdash; and the reason you let them go is always one of these six.</p>
      ''' + rule_grid([
        ('You do not know who', 'Nobody can tell you the doer, so the sentence does without one.', t['ex'][0]),
        ('The doer does not matter', 'The event is the news; who did it is a footnote.', t['ex'][1]),
        ('The doer is obvious', 'Saying it would be a waste of everyone&#39;s time.', t['ex'][2]),
        ('You would rather not say', 'The passive is how English removes a person from a sentence.', t['ex'][3]),
        ('Putting the important thing first', 'Whatever you put at the front is what the sentence is about.', t['ex'][4]),
        ('Putting the doer back with <em>by</em>', 'When the doer <em>is</em> the point, it goes at the end.', t['ex'][5]),
    ]) + '''
    </div>

    <div class="camp" id="form">
      ''' + MARK_TABLE + '''
      <div class="camp-label">Building the passive</div>
      <h2>How it&#39;s built</h2>
      ''' + rule_grid([
        ('Affirmative', 'subject + <strong>%s</strong> + past participle' % t['chain'], t['form'][0]),
        ('Negative', 'the <em>not</em> goes after the first auxiliary', t['form'][1]),
        ('Questions', 'the first auxiliary moves to the front', t['form'][2]),
        ('With the doer', '&hellip; + <strong>by</strong> + doer, at the end', t['form'][3]),
    ], 'form-grid') + chart(
        'Turning an active sentence around',
        'Three moves, always the same: the object comes to the front, the verb becomes '
        '<em>%s</em> + participle, and the old subject either disappears or goes to the back behind '
        '<em>by</em>. Only the middle step changes from camp to camp.' % t['chain'],
        ['Active', 'Passive', 'What moved'], t['turn']) + chart(
        'Conjugation chart',
        t['conj_note'],
        ['Subject', 'Affirmative', 'Negative', 'Question'], t['conj']) + chart(
        'Three mistakes worth naming',
        'Almost every error with this one is one of these three.',
        ['Not this', 'This', 'Why'], t['mistakes']) + '''
    </div>

    ''' + fork(
        'Active or passive?',
        'Neither is better. The question is only what the sentence is about &mdash; because whatever you '
        'put at the front is what the reader will think it is about.',
        ['Question', 'Passive', 'Active'],
        [['What is the sentence about?', 'The thing it happens to.<br>%s' % t['pair'][0],
          'The one who does it.<br>%s' % t['pair'][1]],
         ['Do you know the doer?', 'Often not &mdash; and you do not need to.', 'Yes, and you are naming them.'],
         ['Where does the doer go?', 'At the end with <em>by</em>, or nowhere at all.', 'At the front, as the subject.'],
         ['Which is shorter?', 'Longer by two or three words.', 'Usually shorter. Prefer it when both work.']],
        t['note'],
        [(t['back'], '&larr; %s, active' % t['back_label']),
         ('sherpa-tensing-route-map.html', 'The route map')]) + signals(
        None or 'Reach for the passive when',
        ['the doer is unknown', 'the doer is irrelevant', 'the doer is obvious',
         'the process is the point', 'a report needs distance', 'the object is the topic'],
        'Verbs with no passive at all',
        ['happen &middot; occur', 'arrive &middot; go &middot; come', 'die &middot; live',
         'exist &middot; belong', 'seem &middot; appear', 'become &middot; fall'],
        'The test for whether a verb can go passive: does it take an object? <em>They built it</em> has '
        'one, so it turns. <em>It happened</em> has none, so it cannot.') + interactive(
        MARK_PANES, 'Interactive', 'The event, and the doer you dropped',
        'The block is the same block as the ascent, lit from above instead of fading into the dark &mdash; '
        'because the tense has not changed, only the light. Inside it sits a dashed box: the doer. It is '
        'drawn inside the event rather than beside it because the doer is not a moment in time, it is a '
        'part of the sentence &mdash; and it is dashed because most of the time nobody says it. Click '
        'either to see it in a sentence.',
        dia(t['uid'] + 'b', groups=True),
        ['panel-event', 'The event &mdash; now the subject',
         'panel-agent', 'The doer &mdash; optional, and usually gone'])

    return assemble(
        hero(t['eyebrow'], t['h1'], t['lede'], dia(t['uid'])),
        camps,
        js([], [], ['shape-event', 'panel-event', 'shape-agent', 'panel-agent'],
           [t['ink'], t['ghost']])
        .replace('var exA = [\n\n];', 'var exA = [\n  %s\n];' % ",\n  ".join('"%s"' % e for e in t['panelA']))
        .replace('var exB = [\n\n];', 'var exB = [\n  %s\n];' % ",\n  ".join('"%s"' % e for e in t['panelB'])),
        questions(t['quiz']),
        palette(*t['palette']).replace('--card:#FFFFFF;', '--card:%s;' % t['card']),
        '<title>%s</title>' % t['title'],
        [('/* ── NOW vs WILL DIAGRAM CAMP ── */', '/* ── EVENT vs DOER DIAGRAM CAMP ── */'),
         ('// ── NOW vs WILL diagram interactivity ──', '// ── the event and the dropped doer ──'),
         ('"Clean run. You can tell a decision from a plan, and a belief from a forecast."',
          '"Clean run. You can turn a sentence around and you know when the doer is worth keeping."'),
         ('"Solid progress. Worth a look back at camp five before camp eight."',
          '"Solid progress. Worth a look back at the active version before you go on."'),
         ('"Good first attempt. The will/going to fork is the part to read again."',
          '"Good first attempt. The auxiliary chain is the part to read again."'),
         ('Return to base camp', 'Back to the route map'),
         ('\n</style>', DARK_CSS + '</style>')],
        t['file'])

    import re as _re
    _s = open(t['file'], encoding='utf-8').read()
    _i = _s.find('<div class="tr-bar"')
    if _i >= 0:
        _j = _s.index('</div>', _s.rindex('</button>', _i)) + 6
        _s = _s[:_i] + _s[_j:]
    _s = _re.sub(r'\n// ── example translations.*?\n\}\);\n\n(?=// ──|var )', '\n', _s, count=1, flags=_re.S)
    open(t['file'], 'w', encoding='utf-8').write(_s)
    return _s
