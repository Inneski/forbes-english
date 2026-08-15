# -*- coding: utf-8 -*-
"""Professional Speaking: product & market research (B1) — rebuilt as a deck.

This one is not a quiz and the rebuild had to respect that. It is a
teacher-led one-to-one speaking plan, roughly fifty minutes, built around a
product manager who sells roofing membranes: a warm-up, five spoken upgrades,
two roleplays, and a two-minute pitch. All of that survives, including the
teacher's own notes, which are the most useful thing in the file and now sit
on the slides where they are needed rather than in a block at the top.

Four things were fixed.

**A student's name had been find-and-replaced with the literal string "the
student", fifteen times**, including mid-sentence and at the start of headings,
so the lesson read as ungrammatical in a dozen places and was written entirely
around one male student. It is now addressed to whoever is in the room.

**The closing recap listed four of the five activities** and dropped the
two-minute pitch — the longest one, and the only one with a self-assessment.

**One explanation was simply wrong.** "'Make' is for physical things" — you
make a decision, an appointment, a suggestion, a profit. The correction was
right; the reason a B1 learner could falsify in one move. It now says what is
actually true: <em>conduct</em> is the collocation research takes.

**And upgrade five silently changed the tense** as well as fixing the error,
so a learner who produced the fully correct <em>We discuss the new product
with our suppliers</em> did not match the model. The tense change is gone; the
point is the preposition.

The five upgrades and the four question corrections are now scored, which
gives the deck a spine without touching the speaking work — a teacher can
still run them aloud, with the options on the wall.
"""
import sys
sys.path.insert(0, '/home/claude/forbes-english/lesson-template/build')
import deck as D

TPL = 'lesson-template/lesson-template.html'
OUT = 'forbes-english-product-speaking.html'
F = 'ProductSpeaking'

PALETTE = '''  --hero: url('%s/hero.jpg');

  --void          : #0b0b0c;
  --surface       : #151519;
  --surface2      : #1e1e24;
  --border        : #c26764;
  --text          : #f5f2f2;
  --text-dim      : #bfa4a3;
  --accent        : #f09f9c;
  --accent-bright : #fda7a3;
  --accent-dim    : #df5651;
  --secondary     : #335e90;
  --contrast      : #1ded90;''' % F

MC = [
    dict(ctx='&ldquo;I make market research with customers in England.&rdquo;',
         stem='How would you say that professionally?',
         options=['I conduct market research with customers in England.',
                  'I do some market research with the customers in England.',
                  'I am making market research with our customers in England.',
                  'I perform market researches with customers over in England.'],
         correct=0,
         why='Research takes <strong>conduct</strong> &mdash; and so do surveys, interviews and meetings. <em>Do research</em> is possible but flat; <em>research</em> is uncountable, so never <em>researches</em>.'),
    dict(ctx='&ldquo;I am responsible to develop the product strategy.&rdquo;',
         stem='How would you say that professionally?',
         options=['I am responsible for developing the product strategy.',
                  'I am responsible on developing our new product strategy.',
                  'I have the responsibility to develop the product strategy.',
                  'I am the responsible for developing the product strategy.'],
         correct=0,
         why='<strong>Responsible for</strong> + <em>-ing</em> is fixed. <em>Responsible to</em> exists, but it means answerable to a <em>person</em>: <em>I am responsible to the board.</em>'),
    dict(ctx='&ldquo;Customers have problems with the membrane when it is wet.&rdquo;',
         stem='How would you say that professionally?',
         options=['A common pain point is handling the membrane in wet conditions.',
                  'Customers are having a lot of problems with the membrane when wet.',
                  'There are some difficulties with this membrane in the wet weather.',
                  'The membrane is causing our customers problems when it gets wet.'],
         correct=0,
         why='<strong>Pain point</strong> is the product-management term, and it is more precise than <em>problem</em>: it names something the customer feels, which is what you are researching.'),
    dict(ctx='&ldquo;Can you make the membrane more lighter?&rdquo;',
         stem='How would you ask a supplier that?',
         options=['Would it be possible to reduce the weight of the material?',
                  'Can you please make the membrane a little bit more light?',
                  'Is it possible that you make the material lighter for us?',
                  'I want you to reduce the weight of this material, please.'],
         correct=0,
         why='<strong>Would it be possible to&hellip;?</strong> is polite and still direct &mdash; the standard way to ask a supplier for a change. Note also that <em>more lighter</em> is a double comparative: <em>lighter</em> already is the comparative.'),
    dict(ctx='&ldquo;We discuss with suppliers about the new product.&rdquo;',
         stem='How would you say that professionally?',
         options=['We discuss the new product with our suppliers.',
                  'We are discussing about the new product together with suppliers.',
                  'We have a discussion about the new product with our suppliers.',
                  'We talk with our suppliers about the new product regularly.'],
         correct=0,
         why='<strong>Discuss</strong> takes a direct object and no preposition: you discuss <em>something</em>, never <em>about something</em>. (Option C is correct English &mdash; a <em>discussion</em> does take <em>about</em> &mdash; but it is heavier.)'),
]

MATCH = [
    ('You like this product?', 'What do you like about it?'),
    ('Is price important?', 'How important is price?'),
    ('You have problems?', 'What kind of problems do you have?'),
    ('What you need?', 'What do you need from a supplier?'),
]

CHIPS = ['conduct market research', 'responsible for&hellip;', 'a pain point',
         'Would it be possible to&hellip;?', 'discuss something with someone',
         'Based on our research&hellip;', 'So, if I understand correctly&hellip;']


def card(title, body, tone=None):
    return ('<div class="card"><p class="prose"><strong>%s</strong></p>'
            '<p class="prose" style="margin-top:8px;font-size:17px">%s</p></div>'
            % (title, body))


def plain(eyebrow_key, eyebrow, title_key, title, inner, bg=None):
    return '''
    <section class="slide" data-type="discuss"%s>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="%s">%s</div>
        <h2 class="slide-title" data-i18n="%s">%s</h2>
      </div></div>
      <div class="slide-body">
%s
      </div>
    </section>
''' % (D._bg(F, bg), eyebrow_key, eyebrow, title_key, title, inner)


def build():
    D.assert_no_key_is_longest(MC, 'Product speaking')
    logo = D.logo_from(TPL)

    warmup = plain('warmEyebrow', 'Activity 1 &middot; 5&ndash;8 minutes',
                   'warmTitle', 'Warm-up: talk about your work', '''
        <div class="cols" style="grid-template-columns:1.2fr 1fr">
          <div class="card">
            <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px" data-i18n="warmAsk">Ask these, one at a time</p>
            <ul class="act-list">
              <li>Can you describe your role? What are you responsible for day to day?</li>
              <li>What kinds of products do you manage? Who makes them, and who buys them?</li>
              <li>Who do you usually speak to in English &mdash; customers, suppliers, retailers, colleagues?</li>
              <li>What is the most difficult part of speaking English at work?</li>
              <li>Describe a recent conversation in English that was difficult. What made it hard?</li>
            </ul>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="warmTh">Teacher</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px" data-i18n="warmTb">Do not rush, and <em>do not correct yet</em>. Listen for grammar patterns, hesitation and vocabulary gaps, and make notes. The point of this activity is to hear how they talk about the job now &mdash; corrections come back later as language, not as a list of errors.</p>
          </div>
        </div>''', bg=None)

    listen = plain('listenEyebrow', 'Activity 1 &middot; while they speak',
                   'listenTitle', 'Four patterns to listen for', '''
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="lWrong">Likely to come up</strong></p>
            <p class="prose" style="margin-top:10px;font-size:19px;line-height:1.9">
              I <em>make</em> market research<br>
              responsible <em>to</em> develop<br>
              We discuss <em>about</em> suppliers<br>
              I am working <em>since</em> five years
            </p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="lRight">What you are aiming at</strong></p>
            <p class="prose" style="margin-top:10px;font-size:19px;line-height:1.9">
              I <strong>conduct</strong> market research<br>
              responsible <strong>for developing</strong><br>
              We discuss suppliers &mdash; no <em>about</em><br>
              I <strong>have been</strong> working <strong>for</strong> five years
            </p>
          </div>
        </div>''')

    drill = plain('drillEyebrow', 'Activity 2 &middot; from memory',
                  'drillTitle', 'Quick drill &mdash; no looking', '''
        <p class="prose dim" style="margin-bottom:12px;font-size:17px" data-i18n="drillHint">
          Read the situation. They answer with the phrase, out loud, without looking at the previous slides.
        </p>
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose" style="font-size:18px;line-height:2">
              You want to study your customers&rsquo; needs.<br>
              Your job is to manage the product range.<br>
              Roofers complain about slippery surfaces.
            </p>
          </div>
          <div class="card">
            <p class="prose" style="font-size:18px;line-height:2">
              &rarr; <em>I need to conduct&hellip;</em><br>
              &rarr; <em>I am responsible for&hellip;</em><br>
              &rarr; <em>A common pain point is&hellip;</em>
            </p>
            <p class="prose" style="font-size:18px;line-height:2;margin-top:6px">
              You want the supplier to change the weight. &rarr; <em>Would it be possible to&hellip;</em><br>
              You are talking to a supplier about an idea. &rarr; <em>We are discussing&hellip; with&hellip;</em>
            </p>
          </div>
        </div>''')

    roofer = plain('roofEyebrow', 'Activity 3 &middot; 12&ndash;15 minutes',
                   'roofTitle', 'Market research roleplay', '''
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="r1h">🎙 Student &mdash; product manager</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px" data-i18n="r1b">You are doing market research with a roofer in England. Find out how he chooses membranes, what goes wrong, and what would make his job easier. Ask open questions and follow up on every answer.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="r2h">🔨 Teacher &mdash; UK roofer</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px" data-i18n="r2b">Eighteen years on roofs. Straight-talking, slightly impatient. You decide what gets bought, not the contractor. <strong>Volunteer nothing</strong> &mdash; if the question is closed, answer yes or no and wait. That is what forces a better follow-up.</p>
          </div>
        </div>
        <div class="card" style="margin-top:12px">
          <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px" data-i18n="roofAns">Answers to use, in any order</p>
          <p class="prose" style="font-size:16px;line-height:1.75">
            &ldquo;Price matters &mdash; but if it tears on a windy day, it&rsquo;s a nightmare.&rdquo; &middot;
            &ldquo;If my supplier doesn&rsquo;t stock it, I won&rsquo;t use it.&rdquo; &middot;
            &ldquo;Some are too slippery when the roof is wet. That&rsquo;s a safety issue.&rdquo; &middot;
            &ldquo;The instructions are unclear &mdash; especially in the rain.&rdquo; &middot;
            &ldquo;Breathability, durability, ease of installation. In that order.&rdquo; &middot;
            &ldquo;I decide what we buy. The contractor leaves it to me.&rdquo;
          </p>
        </div>''')

    qbank = plain('qbEyebrow', 'Activity 3 &middot; the questions',
                  'qbTitle', 'Six questions, by what they do', '''
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose" style="font-size:17px;line-height:1.9">
              <span class="dim">Opening</span><br>&ldquo;What type of projects do you usually work on?&rdquo;<br>
              <span class="dim">Discovering needs</span><br>&ldquo;What do you look for when choosing a membrane?&rdquo;<br>
              <span class="dim">Finding problems</span><br>&ldquo;What problems do you have during installation?&rdquo;
            </p>
          </div>
          <div class="card">
            <p class="prose" style="font-size:17px;line-height:1.9">
              <span class="dim">Digging deeper</span><br>&ldquo;Can you give me an example of that?&rdquo;<br>
              <span class="dim">Buying decisions</span><br>&ldquo;Who decides which product to buy on site?&rdquo;<br>
              <span class="dim">Improvement</span><br>&ldquo;What would make the product easier to use?&rdquo;
            </p>
          </div>
        </div>
        <p class="prose dim" style="margin-top:12px;font-size:16px" data-i18n="qbNote">
          A guide, not a script. The follow-up matters more than the question &mdash; every answer above has a second question hiding in it.
        </p>''')

    supplier = plain('supEyebrow', 'Activity 4 &middot; 10&ndash;12 minutes',
                     'supTitle', 'Supplier discussion', '''
        <div class="cols" style="grid-template-columns:1fr 1fr">
          <div class="card">
            <p class="prose"><strong data-i18n="s1h">🎙 Student &mdash; product manager</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px" data-i18n="s1b">Report what the roofer actually told you in Activity 3 &mdash; not what you expected to hear. Then ask whether the product can change: feasibility, cost, timeline. Finish by summarising what was agreed.</p>
          </div>
          <div class="card">
            <p class="prose"><strong data-i18n="s2h">🔩 Teacher &mdash; supplier</strong></p>
            <p class="prose" style="margin-top:8px;font-size:17px" data-i18n="s2b">Interested, busy, numbers-focused. Reducing weight is possible. Grip coating adds <strong>8&ndash;12%</strong> to cost. Development takes <strong>4&ndash;6 months</strong>. Say those numbers out loud &mdash; the summary task depends on them. Ask for written specifications before you commit.</p>
          </div>
        </div>
        <div class="card" style="margin-top:12px">
          <p class="prose dim" style="font-size:14px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:6px" data-i18n="supPh">Six phrases to get in</p>
          <p class="prose" style="font-size:16px;line-height:1.75">
            &ldquo;Based on our customer research, we have noticed that&hellip;&rdquo; &middot;
            &ldquo;One important requirement from the market is&hellip;&rdquo; &middot;
            &ldquo;Would it be possible to adjust the&hellip;?&rdquo; &middot;
            &ldquo;How would this affect the production cost?&rdquo; &middot;
            &ldquo;What would be a realistic timeline?&rdquo; &middot;
            &ldquo;So, if I understand correctly&hellip;&rdquo;
          </p>
        </div>''')

    structure = plain('stEyebrow', 'Activity 5 &middot; before the timer',
                      'stTitle', 'Five stages, held in your head', '''
        <div class="cols" style="grid-template-columns:1fr 1fr 1fr 1fr 1fr">
          <div class="card"><p class="prose"><strong>1</strong></p><p class="prose" style="margin-top:6px;font-size:16px" data-i18n="st1">Introduce it<br><em>&ldquo;This product is designed for&hellip;&rdquo;</em></p></div>
          <div class="card"><p class="prose"><strong>2</strong></p><p class="prose" style="margin-top:6px;font-size:16px" data-i18n="st2">The purpose<br><em>&ldquo;Its main purpose is to&hellip;&rdquo;</em></p></div>
          <div class="card"><p class="prose"><strong>3</strong></p><p class="prose" style="margin-top:6px;font-size:16px" data-i18n="st3">The benefit<br><em>&ldquo;The main advantage is&hellip;&rdquo;</em></p></div>
          <div class="card"><p class="prose"><strong>4</strong></p><p class="prose" style="margin-top:6px;font-size:16px" data-i18n="st4">Compare<br><em>&ldquo;Compared with standard options&hellip;&rdquo;</em></p></div>
          <div class="card"><p class="prose"><strong>5</strong></p><p class="prose" style="margin-top:6px;font-size:16px" data-i18n="st5">Summarise<br><em>&ldquo;In simple terms, it helps&hellip;&rdquo;</em></p></div>
        </div>
        <p class="prose dim" style="margin-top:14px;font-size:17px" data-i18n="stNote">
          Two minutes, one product, no notes. Then they self-assess before you say anything: did they name the user, the purpose, one benefit, and a comparison?
        </p>''')

    slides = (
        D.cover(logo, 'Talking About <em>Your Product</em>',
                'A fifty-minute speaking lesson: research a customer, brief a supplier, pitch the thing',
                [('Level', 'B1 &middot; Professional speaking'),
                 ('Focus', 'Market research &amp; product'), ('Count', '17 slides')])
        + D.teach('runEyebrow', 'How to run it',
                  'runTitle', 'Three rules for the teacher',
                  [('h1h', 'Do not correct in Activity 1',
                    'Listen, note, and say nothing.',
                    'h1b', 'Corrections land far better later, as language you are teaching, than immediately, as a list of things they got wrong.'),
                   ('h2h', 'Every upgrade is said aloud, twice',
                    'Once slowly, once at normal speed.',
                    'h2b', 'The goal is muscle memory, not recognition. A phrase they have only read will not arrive when they need it.'),
                   ('h3h', 'Finish on three things',
                    'One praise, one correction, one upgrade.',
                    'h3b', 'Specific, in that order. &ldquo;Your structure was logical&rdquo; &middot; &ldquo;<em>conduct</em> research, not <em>make</em>&rdquo; &middot; &ldquo;try <em>the key advantage is&hellip;</em>&rdquo;')],
                  folder=F)
        + warmup
        + listen
        + "".join(D.mc(i + 1, len(MC), q, 'qEyebrow', 'Activity 2 &middot; say it better',
                       'qTitle', 'Say it professionally', folder=F, ctx=q['ctx'])
                  for i, q in enumerate(MC))
        + drill
        + roofer
        + qbank
        + D.match(MATCH, 'matchEyebrow', 'Activity 3 &middot; after the roleplay',
                  'matchTitle', 'Turn the closed question into an open one',
                  'matchHint', 'Click a weak question, then click the version that opens the conversation.',
                  'A closed question gets you a yes. An open one gets you a reason — and the reason is the research. Notice that every strong version here starts with a question word, not with you.',
                  folder=F)
        + supplier
        + structure
        + D.results('resNext', 'Now two minutes, one product, no notes →')
        + D.activate('The two-minute pitch', 'Use at least four:', CHIPS,
                     'Speaking &middot; timed, no notes',
                     'The teacher is a new retailer in Ireland who knows construction but not your range.',
                     ['Two minutes on one product: what it is, who uses it, what problem it solves.',
                      'Self-assess first: did you name a user, a purpose, a benefit and a comparison?',
                      'Prepare a different product for next time &mdash; same four things, same two minutes.',
                      'Bring five real questions a customer or supplier asked you in English this month.'],
                     'Writing &middot; 120&ndash;160 words',
                     'Write the email you would send the supplier after Activity 4: the feedback, the request, and what you agreed.',
                     'Dear Frank, following our call this morning,')
    )

    import i18n_prodspeak as I
    s = D.assemble(TPL, OUT, slides, PALETTE, 'Talking About Your Product — B1 speaking', I)
    print('wrote %s — %d slides, %d MC, %d pairs, %d bytes'
          % (OUT, s.count('<section class="slide'), len(MC), len(MATCH), len(s)))


if __name__ == '__main__':
    build()
