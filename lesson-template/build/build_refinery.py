# -*- coding: utf-8 -*-
"""Active & Passive Voice, Refinery Deputy Lead — rebuilt as a deck.

The content here was the strongest raw material in the batch: a five-tense
passive table, three side-by-side situations showing the same message in both
voices, and four worked transformations, all set on a working refinery. It all
survives. What did not survive is a genuinely serious bug and four smaller ones.

**Every wrong answer said "Correct."** The feedback array held one string per
question and the handler wrote it unconditionally, varying only the CSS class.
A learner who picked a distractor saw red styling above text beginning
"Correct. In 'The crew suppressed the fire'…". Six items out of six. The deck
engine writes the right message for the answer actually given.

**The colour key taught the opposite of the rule.** Section 0 tagged the
fronted noun of every passive as the <em>object</em> &mdash; "what receives the
action" &mdash; and section 3 then said that same noun "becomes the new
grammatical subject". Both cannot be true, and it is precisely the point
learners find hard. It is now stated once: the object moves to the front
<em>and becomes the subject</em>.

**Two keys were the longest option**, one of them by 63% and the only one
carrying a second sentence.

**Question 5 was broken twice over**: the nested quotation marks had been lost,
producing the run-on "The deluge system was activated is grammatically
incorrect", and the stem asked "what is wrong with this statement?" while two
of the three options answered that nothing was. It is now a clean
true-or-false about whether the agent is compulsory.

**And restart did not restart.** The button reset the view but not the score,
the locked buttons or the feedback, so the lesson could not be retaken without
reloading the page.

One thing deliberately not carried over: the free-text conversion checked its
answer by looking for the substrings "was inspected" and "bund wall", so "The
deputy lead was inspected by the bund wall" passed. It is a gap now, and the
open version moved to the activation stage where a human reads it.
"""
import sys
sys.path.insert(0, '/tmp')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'active_passive_refinery_lesson.html'
F = 'RefineryAP'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0d0c0a;
  --surface       : #191814;
  --surface2      : #25231e;
  --border        : #b77b67;
  --text          : #f5f3f2;
  --text-dim      : #bfaaa3;
  --accent        : #eaae9a;
  --accent-bright : #f9b6a0;
  --accent-dim    : #d57453;
  --secondary     : #a9b9b9;
  --contrast      : #1dedbd;''' % F

MC = [
    dict(stem='Which sentence is in the <strong>active</strong> voice?',
         options=['The crew suppressed the fire.',
                  'The fire was suppressed by the crew.',
                  'The fire has been extinguished.',
                  'The fire was reported at 09:14.'],
         correct=0,
         why='In <em>The crew suppressed the fire</em> the subject does the action. That is the whole definition. The other three all have something happening <em>to</em> the fire.'),
    dict(stem='Put into the passive: &ldquo;We test the gas detectors every quarter.&rdquo;',
         options=['The gas detectors are tested every quarter.',
                  'The gas detectors were tested every quarter.',
                  'The gas detectors are being tested every quarter.',
                  'The gas detectors have been tested every quarter.'],
         correct=0,
         why='The active is present simple, so the passive is present simple: <strong>are tested</strong>. <em>Were tested</em> moves it to the past; <em>are being tested</em> says it is happening at this moment.'),
    dict(stem='You are writing a formal incident report. Which phrasing belongs there?',
         options=['The evacuation was ordered at 09:45. All isolation valves were closed.',
                  'I ordered the evacuation at 09:45, and then we closed all of the valves.',
                  'Evacuation ordered at 09:45. Valves closed. All personnel accounted for.',
                  'We had the evacuation ordered at 09:45 and got all the valves closed up.'],
         correct=0,
         why='A report wants an objective tone, and the passive supplies it: <em>the evacuation was ordered</em>, not <em>I ordered the evacuation</em>. The third option is note form &mdash; fine in a log, not in a report.'),
    dict(stem='A fireground radio command should normally be&hellip;',
         options=['&ldquo;Bravo team, withdraw to the muster point.&rdquo;',
                  '&ldquo;Bravo team is to be withdrawn to the muster point.&rdquo;',
                  '&ldquo;The muster point is where Bravo team should now be.&rdquo;',
                  '&ldquo;Withdrawal to the muster point is required of Bravo.&rdquo;'],
         correct=0,
         why='Active, and as short as it can be made. Every passive version here is longer, and on a radio under load, longer is worse. A command names who acts and what they do.'),
    dict(stem='True or false: a passive sentence must always say who performed the action.',
         options=['False &mdash; the agent is optional, so <em>The deluge system was activated</em> is complete.',
                  'True &mdash; without a <em>by + agent</em> phrase a passive sentence is grammatically incomplete.',
                  'True in formal reports only &mdash; everywhere else the agent may safely be left out.',
                  'False &mdash; but only when the doer is genuinely unknown to the writer.'],
         correct=0,
         why='<strong>False.</strong> The agent is optional in the passive, and leaving it out is often the reason for choosing the passive in the first place &mdash; when the doer is unknown, obvious, or beside the point.'),
    dict(stem='Put into the passive: &ldquo;The refinery manager approved the emergency plan.&rdquo;',
         options=['The emergency plan was approved by the refinery manager.',
                  'The emergency plan is approved by the refinery manager.',
                  'The emergency plan has been approved by the manager.',
                  'The emergency plan will be approved by the manager.'],
         correct=0,
         why='<em>Approved</em> is past simple, so the passive is past simple: <strong>was approved</strong>. Each of the others is a real tense &mdash; just not this one.'),
]

GAPS = [
    ('<em>The safety officer filed the near-miss report.</em><br>The near-miss report ______ by the safety officer.',
     ['was filed'],
     'Past simple &rarr; <strong>was filed</strong>. The object moves to the front and becomes the subject; the agent goes to the end with <em>by</em>.'),
    ('<em>The crew extinguished the flange fire.</em><br>The flange fire ______ by the crew.',
     ['was extinguished'],
     'Past simple again &rarr; <strong>was extinguished</strong>. Note the participle: <em>extinguish</em> is regular, so it simply adds <em>-ed</em>.'),
    ('<em>Engineers have completed the fireproofing inspection.</em><br>The fireproofing inspection ______.',
     ['has been completed'],
     'Present perfect &rarr; <strong>has been completed</strong>. <em>Engineers</em> is dropped: nobody needs to know which ones, which is exactly when the passive earns its place.'),
    ('<em>The shift commander will update the emergency plan.</em><br>The emergency plan ______ next month.',
     ['will be updated'],
     'Future &rarr; <strong>will be updated</strong>. The pattern is always <em>will be</em> + past participle, whatever the verb.'),
    ('<em>Somebody must inspect all equipment before use.</em><br>All equipment ______ before use.',
     ['must be inspected'],
     'Modal &rarr; <strong>must be inspected</strong>. This is the standard sentence shape of a written procedure, and it is why SOPs read the way they do.'),
]

MATCH = [
    ('Giving an order on the fireground', 'Active &mdash; short, and it names who acts'),
    ('Writing the incident report', 'Passive &mdash; objective, and the doer recedes'),
    ('Drafting a standard operating procedure', 'Passive &mdash; <em>must be checked before each shift</em>'),
    ('Recording a shift handover', 'Active &mdash; who did what, on the record'),
    ('Reporting a fault nobody has traced yet', 'Passive &mdash; because the doer is genuinely unknown'),
]

STEPS = ['Move the object to the front &mdash; it becomes the new subject',
         'Change the verb to the right form of <em>to be</em>, keeping the tense',
         'Add the past participle',
         'Add <em>by</em> + the original subject &mdash; or leave it out']

CHIPS = ['was isolated', 'has been repaired', 'will be briefed', 'must be inspected',
         'is tested daily', 'by the deputy lead']


def build():
    D.assert_no_key_is_longest(MC, 'Refinery')
    logo = D.logo_from(TPL)

    table = '''
    <section class="slide" data-type="teach" data-bg="%s/wide.jpg">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="tabEyebrow">The form, in every tense you need</div>
        <h2 class="slide-title" data-i18n="tabTitle">to be + past participle. That is the whole machine.</h2>
      </div></div>
      <div class="slide-body">
        <div class="card">
          <p class="prose" style="font-size:19px;line-height:2.1">
            <span class="dim">present simple</span> &nbsp; is / are + participle &nbsp;&mdash;&nbsp; The alarm <strong>is tested</strong> daily.<br>
            <span class="dim">past simple</span> &nbsp; was / were + participle &nbsp;&mdash;&nbsp; The valve <strong>was closed</strong> immediately.<br>
            <span class="dim">present perfect</span> &nbsp; has / have been + participle &nbsp;&mdash;&nbsp; The pump <strong>has been repaired</strong>.<br>
            <span class="dim">future</span> &nbsp; will be + participle &nbsp;&mdash;&nbsp; All staff <strong>will be briefed</strong> tomorrow.<br>
            <span class="dim">modal</span> &nbsp; must / should be + participle &nbsp;&mdash;&nbsp; Equipment <strong>must be inspected</strong>.
          </p>
        </div>
        <div class="card" style="margin-top:12px">
          <p class="prose" style="font-size:17px" data-i18n="tabNote">
            Regular participles add <em>-ed</em>: test &rarr; tested, seal &rarr; sealed. Irregular ones change: write &rarr; written, do &rarr; done. The quick test: if it fits in <em>&ldquo;The report was ___&rdquo;</em>, it is the past participle.
          </p>
        </div>
      </div>
    </section>
''' % F

    slides = (
        D.cover(logo, 'Active &amp; <em>Passive Voice</em>',
                'Radio calls, shift handovers and incident reports &mdash; and why they are not written the same way',
                [('Level', 'B1&ndash;B2 &middot; Refinery deputy lead'),
                 ('Focus', 'Active &amp; passive'), ('Count', '16 slides')])
        + D.teach('coreEyebrow', 'The difference, stated once',
                  'coreTitle', 'Who is at the front of the sentence?',
                  [('k1h', 'Active',
                    '<strong>The team leader isolated the valve.</strong>',
                    'k1b', 'The doer comes first. You know exactly who did what &mdash; which is why commands and handovers are written this way.'),
                   ('k2h', 'Passive',
                    '<strong>The valve was isolated.</strong>',
                    'k2b', 'The thing acted on comes first, and <em>becomes the subject of the sentence</em>. Who did it may follow with <em>by</em>, or may never be mentioned.'),
                   ('k3h', 'Why it matters here',
                    'Your words move people in a live incident.',
                    'k3b', 'Active assigns accountability. Passive is the standard for reports and procedures. A professional switches between them on purpose.')],
                  folder=F)
        + table
        + D.teach('useEyebrow', 'Choosing between them',
                  'useTitle', 'Speak in active. Write reports in passive.',
                  [('u1h', 'Active when&hellip;',
                    'you give an order &middot; you name who is responsible &middot; you are on the radio &middot; you brief the team &middot; you record a handover',
                    'u1b', 'Commands are <em>always</em> active. &ldquo;Bravo team, withdraw&rdquo; beats &ldquo;Bravo team is to be withdrawn&rdquo; by a second, and a second is a long time on a radio.'),
                   ('u2h', 'Passive when&hellip;',
                    'you write the incident report &middot; the action matters more than the actor &middot; the doer is unknown &middot; you draft an SOP &middot; the matter is sensitive',
                    'u2b', '&ldquo;The isolation valve was confirmed closed at 14:32&rdquo; is the register a report wants. <em>I confirmed it</em> is true, and reads as a statement rather than a record.')],
                  cols='1fr 1fr', folder=F, bg='wide.jpg')
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Knowledge check',
                       'qTitle', 'Which one?', folder=F,
                       bg='wide.jpg' if i % 2 else None)
                  for i, q in enumerate(MC))
        + "".join(D.gap(n + 1, 2, part, None, 'gapEyebrow', 'Turn it round',
                        'gapTitle', 'Complete the passive version', folder=F,
                        hint_key='gapHint',
                        hint='The active sentence is above each gap. Keep the same tense.',
                        width=230, size=17)
                  for n, part in enumerate([GAPS[:3], GAPS[3:]]))
        + D.match(MATCH, 'matchEyebrow', 'The situation decides',
                  'matchTitle', 'Which voice, and why',
                  'matchHint', 'Click a situation, then click the voice it takes.',
                  'Note the last one: the passive is not only a register choice. Sometimes you use it because you honestly do not yet know who did it, and writing an active sentence would mean inventing an actor.',
                  folder=F)
        + D.order(STEPS, 'ordEyebrow', 'Making a passive',
                  'ordTitle', 'Put the four steps in order',
                  'ordHint', 'Click the steps in the order you carry them out.',
                  'The fourth step is the one that is optional, and that is the point most people miss: a passive sentence with no by-phrase is complete, not unfinished.',
                  folder=F, bg='wide.jpg')
        + D.results('resNext', 'Now write one of each, about your own shift →')
        + D.activate('Say it, then write it', 'Use at least four:', CHIPS,
                     'Speaking &middot; in pairs',
                     'One of you is the deputy lead on the radio. The other is writing the report afterwards.',
                     ['Give four commands over the radio. Every one active, every one under eight words.',
                      'Now report the same four events for the file. Every one passive.',
                      'Describe a fault nobody has traced. Say it without naming anyone &mdash; and without sounding evasive.',
                      'Convert this aloud: <em>The deputy lead inspected the bund wall after the incident.</em>'],
                     'Writing &middot; 120&ndash;160 words',
                     'Write the incident report for a small flange fire: what happened, what was done, and at what time.',
                     'At 14:32 the isolation valve was confirmed closed.')
    )

    import i18n_refinery as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Active & Passive Voice — Refinery', I)
    print('wrote %s — %d slides, %d MC, %d gaps, %d pairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(GAPS), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
