# -*- coding: utf-8 -*-
"""Managing Energy Projects (B2) — rebuilt as a deck.

Everything scored survives: five comprehension items on the jargon, the
eight-term word bank, and both six-step sequences. The lifecycle and the risk
process are the real content of this lesson, so they now also appear as a
teaching slide before anybody is asked to reconstruct them from memory.

Two of the five multiple-choice keys were the longest option on their slide;
those distractors were lengthened. The rest already sat within a character or
two, which is what a well-built item looks like.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-lesson-managing energy.html'
F = 'Energy'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0b0d0a;
  --surface       : #161915;
  --surface2      : #20241e;
  --border        : #c1b18c;
  --text          : #f5f4f2;
  --text-dim      : #bfb7a3;
  --accent        : #f0e2c3;
  --accent-bright : #ffbe2f;
  --accent-dim    : #d9bd7e;
  --secondary     : #eda591;
  --contrast      : #1dc1ed;''' % F

MC = [
    dict(ctx='A project manager at a wind farm development company says the project is currently <strong>behind schedule</strong>.',
         stem='What does that most likely mean in a project meeting?',
         options=['The project timeline has been formally extended at the stakeholders&rsquo; request',
                  'The project has not reached its milestones within the planned timeframe',
                  'The project team is currently working ahead of the agreed deliverables',
                  'The project has been paused because of regulatory compliance issues'],
         correct=1,
         why='<strong>Behind schedule</strong> means the milestones have slipped against the original plan. It is not a renegotiated timeline and not a pause &mdash; both of those would be said differently.'),
    dict(ctx='An offshore oil project status report reads: <strong>&ldquo;The scope of works has been revised upward.&rdquo;</strong>',
         stem='What does that indicate?',
         options=['The quality standards being applied to the project have been raised',
                  'The overall cost estimate for the project has been reduced somewhat',
                  'Additional tasks or deliverables have been added to the project',
                  'The project team&rsquo;s capacity has grown because of several new hires'],
         correct=2,
         why='<strong>Scope</strong> is what work the project includes. <em>Revised upward</em> means more of it &mdash; which usually means schedule and budget consequences too.'),
    dict(ctx='A colleague says: <strong>&ldquo;We need to flag this as a critical risk before the steering committee meeting.&rdquo;</strong>',
         stem='What is the appropriate action?',
         options=['Prepare a detailed financial audit report for the board to review in full',
                  'Formally document and escalate a significant problem to senior decision-makers',
                  'Inform the relevant regulator about a compliance failure found on the project',
                  'Cancel the next steering committee meeting until the issue has been resolved'],
         correct=1,
         why='To <strong>flag</strong> a risk is to identify it formally and put it in front of the people who can act. <em>Before the steering committee</em> is the escalation.'),
    dict(ctx='A solar project manager states: <strong>&ldquo;We have a contingency budget of 12% built into the overall project cost.&rdquo;</strong>',
         stem='What is that contingency for?',
         options=['To fund marketing and public relations activity during construction',
                  'To reward the project team on successful delivery of the project',
                  'To provide financial headroom for unforeseen costs and risk events',
                  'To cover the cost of regulatory permits and environmental reports'],
         correct=2,
         why='A <strong>contingency budget</strong> is a reserve against what nobody planned for. It is deliberately not tied to any line item &mdash; that is what makes it a contingency.'),
    dict(ctx='A project debrief states: <strong>&ldquo;Lessons learned from the commissioning phase have been documented.&rdquo;</strong>',
         stem='Why does that matter?',
         options=['To satisfy the legal requirements for project documentation under energy law',
                  'To formally close the project and release the team from their contracts',
                  'To capture insights and improve processes in future energy projects',
                  'To give the client evidence that all deliverables were fully completed'],
         correct=2,
         why='<strong>Lessons learned</strong> is knowledge management: what went well and what did not, recorded so the next project starts further along.'),
]

GAPS = [
    ('Before committing capital to the offshore wind project, the board commissioned a full ______ study.',
     ['feasibility'],
     'A <strong>feasibility</strong> study asks whether a project is technically and financially viable at all, before anyone commits money.'),
    ('The plan identified eight key ______ to track progress, including turbine installation and grid connection.',
     ['milestones'],
     '<strong>Milestones</strong> are the checkpoints that mark a phase or a major deliverable as done.'),
    ('All key ______ &mdash; the ministry, local communities and the lead investor &mdash; were invited to the consultation.',
     ['stakeholders'],
     '<strong>Stakeholders</strong> are anyone with an interest in the project or affected by it. Note that it reaches well beyond the people paying for it.'),
    ('The team uses a set of ______ to measure performance: cost variance, schedule adherence, safety incidents.',
     ['KPIs'],
     '<strong>KPIs</strong> &mdash; key performance indicators &mdash; are the measurable values that say whether the project is hitting its targets.'),
    ('Given the scale of the plant, a ______ approach was agreed: civil works first, electromechanical second.',
     ['phased'],
     'A <strong>phased</strong> approach splits a project into stages, which spreads the risk and the resourcing.'),
    ('The manager decided to ______ the budget overrun to the executive sponsor, as it exceeded her threshold.',
     ['escalate'],
     'To <strong>escalate</strong> is to hand an issue up when it is bigger than the authority you hold.'),
    ('The contract included a detailed list of ______: which reports, models and systems the contractor must provide.',
     ['deliverables'],
     '<strong>Deliverables</strong> are the specific outputs handed over. Vagueness here is where contract disputes begin.'),
    ('The ______ strategy for specialised drilling equipment involved a competitive tender across five suppliers.',
     ['procurement'],
     '<strong>Procurement</strong> covers sourcing, tendering and buying everything a project needs.'),
]
BANK = sorted(['stakeholders', 'deliverables', 'procurement', 'feasibility',
               'milestones', 'escalate', 'KPIs', 'phased'])

LIFECYCLE = ['Concept &amp; feasibility assessment', 'Front-end engineering design (FEED)',
             'Procurement &amp; contracting', 'Construction &amp; installation',
             'Commissioning &amp; testing', 'Operations &amp; handover']
RISK = ['Identify potential risks across all project areas',
        'Assess the likelihood and impact of each risk',
        'Develop mitigation and contingency strategies',
        'Assign risk owners and response actions',
        'Monitor and review the risk register regularly',
        'Report residual risks to the steering committee']

CHIPS = ['behind schedule', 'scope of works', 'flag a risk', 'contingency budget',
         'lessons learned', 'escalate', 'stakeholders', 'KPIs']


def build():
    D.assert_no_key_is_longest(MC, 'Energy')
    pos = D.assert_bank_is_not_a_key(BANK, [a for _, aa, _ in GAPS for a in aa])
    logo = D.logo_from(TPL)

    def col(key, head, items):
        return (key, head,
                "<br>".join('<strong>%d.</strong> %s' % (n + 1, t) for n, t in enumerate(items)),
                None, None)

    slides = (
        D.cover(logo, 'Managing <em>Energy Projects</em>',
                'Planning, risk, budgets and stakeholders &mdash; the language the industry actually runs on',
                [('Level', 'B2 &middot; Upper-intermediate'), ('Focus', 'Energy project management'),
                 ('Count', '16 slides')])
        + D.teach('jargonEyebrow', 'The words that carry weight',
                  'jargonTitle', 'Five phrases you will hear in every status meeting',
                  [('j1h', 'behind schedule',
                    'Milestones have slipped against the plan.',
                    'j1b', 'Not a pause, and not a renegotiated date. Those are said differently, and the difference matters in a report.'),
                   ('j2h', 'scope of works',
                    'What the project includes &mdash; its boundary.',
                    'j2b', '<em>Revised upward</em> means more work. It is rarely announced as a schedule or budget change, but it is one.'),
                   ('j3h', 'to flag a risk',
                    'To identify it formally and put it in front of decision-makers.',
                    'j3b', 'Flagging is a written act. If it was only said in a corridor, it was not flagged.'),
                   ('j4h', 'contingency budget',
                    'Reserve held against what nobody planned for.',
                    'j4b', 'Deliberately not tied to any line item. Spending it on a known cost defeats the point.')],
                  cols='1fr 1fr 1fr 1fr', folder=F)
        + D.teach('seqEyebrow', 'Two sequences worth knowing cold',
                  'seqTitle', 'The lifecycle, and the risk process',
                  [col('sq1', 'Project lifecycle', LIFECYCLE),
                   col('sq2', 'Risk management', RISK)],
                  cols='1fr 1fr', folder=F, bg='plant.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'In the status meeting',
                       'qTitle', 'What does it mean?', folder=F,
                       ctx=q['ctx'], bg='plant.jpg' if i % 2 else None)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 3, part, BANK, 'gapEyebrow', 'The exact term',
                        'gapTitle', 'Complete the report', folder=F,
                        hint_key='gapHint',
                        hint='Every word in the bank is used exactly once across the three slides.',
                        width=200, size=18)
                  for n, part in enumerate([GAPS[:3], GAPS[3:6], GAPS[6:]]))
        + D.order(LIFECYCLE, 'ordEyebrow', 'Sequence',
                  'ordTitle', 'Put the project lifecycle in order',
                  'ordHint', 'Click the phases in the order they happen.',
                  'Feasibility answers whether to build at all; FEED answers what exactly to build. Getting those two the wrong way round is the expensive mistake this order exists to prevent.',
                  folder=F, bg='plant.jpg')
        + D.order(RISK, 'ordEyebrow', 'Sequence',
                  'ordTitle', 'Put the risk process in order',
                  'ordHint', 'Click the steps in the order they happen.',
                  'Identify, assess, mitigate, assign, monitor, report. Assigning an owner before assessing the impact is how a register fills up with risks nobody has weighed.',
                  folder=F)
        + D.results('resNext', 'You know the words. Now run a meeting in them →')
        + D.activate('Run the status meeting', 'Use at least four:', CHIPS,
                     'Roleplay &middot; in threes',
                     'One project manager, one client, one finance lead. Fifteen minutes, one agenda.',
                     ['Report that the project is behind schedule. Do not use the word <em>problem</em>.',
                      'The scope has been revised upward. Explain what that does to the budget.',
                      'Flag one critical risk, and propose who should own it.',
                      'Close by confirming what goes to the steering committee, and by when.'],
                     'Writing &middot; 150&ndash;200 words',
                     'Write the risk section of a monthly status report: one critical risk, its impact, and the mitigation.',
                     'Risk register — October update')
    )

    import i18n_energy as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Managing Energy Projects — B2', I)
    print('wrote %s — %d slides, %d MC, %d gaps, 2 sequences, bank %s, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), pos, len(s)))


if __name__ == '__main__':
    build()
