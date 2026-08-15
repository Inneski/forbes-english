# -*- coding: utf-8 -*-
import re

TPL = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = TPL

# ── 1. title ──────────────────────────────────────────────────────────
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>JFK &amp; Prepositions | Forbes English</title>')

# ── 2. hero + palette (derived from jfk/hero.jpg) ─────────────────────
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              "  --hero: url('jfk/hero.jpg');")
pal = {
 '--void':'#090e0c', '--surface':'#121c19', '--surface2':'#1a2924',
 '--border':'#ae6661', '--text':'#f5f2f2', '--text-dim':'#bfa5a3',
 '--accent':'#e59590', '--accent-bright':'#f4b3af', '--accent-dim':'#ce534b',
 '--secondary':'#050e0b', '--contrast':'#1ded95',
}
for k, v in pal.items():
    s = re.sub(r'(\n  ' + re.escape(k) + r'\s*: )#[0-9a-fA-F]{3,8};', lambda m: m.group(1) + v + ';', s, count=1)

# ══ SLIDES ════════════════════════════════════════════════════════════
MC = [
 ("Kennedy was assassinated <em>_______</em> Dealey Plaza in Dallas, Texas, on 22 November 1963.",
  [("inside", "'Inside' implies an enclosed interior with walls — a plaza is open ground."),
   ("within", "'Within' is formal and draws a boundary; it is not how English names a public square."),
   ("in", None),
   ("around", "'Around' suggests movement in the vicinity rather than a fixed location.")],
  "in",
  "<strong>In</strong> is the standard preposition for named public spaces, squares and plazas."),

 ("The Warren Commission concluded that Lee Harvey Oswald acted <em>_______</em> his own, without co-conspirators.",
  [("on", None),
   ("by", "'By himself' works, but 'by his own' is not English — the possessive needs 'on'."),
   ("for", "'For his own' is incomplete; it needs a noun after it, as in 'for his own reasons'."),
   ("in", "'In his own' also needs a noun — 'in his own words', for instance.")],
  "on",
  "<strong>On his own</strong> is a fixed expression meaning independently, without help."),

 ("The presidential motorcade was travelling <em>_______</em> Elm Street when the shots were fired.",
  [("along", None),
   ("across", "'Across' means from one side to the other — that would cross the street, not follow it."),
   ("through", "'Through' means entering and leaving something enclosed, like a tunnel or a crowd."),
   ("over", "'Over' suggests passing above something rather than following a road.")],
  "along",
  "<strong>Along</strong> describes movement following the length of a road or path."),

 ("Many documents relating to the assassination were kept <em>_______</em> the public for decades.",
  [("away from", "Possible in speech, but 'kept away from' suggests physical distance, not concealment."),
   ("hidden from", "'Hidden' is a second verb, not a preposition — the sentence already has 'kept'."),
   ("from", None),
   ("out of reach of", "Too long and too literal; it describes distance rather than deliberate withholding.")],
  "from",
  "<strong>Keep something from someone</strong> means to withhold or conceal it deliberately."),

 ("The CIA has been <em>_______</em> suspicion ever since declassified files suggested prior knowledge of Oswald.",
  [("below", "'Below' is purely spatial — it describes a position, not a state."),
   ("beneath", "'Beneath' is the literary form of 'below'; it does not collocate with 'suspicion'."),
   ("under", None),
   ("within", "'Within' draws a boundary around something; suspicion is not a container.")],
  "under",
  "<strong>Under suspicion</strong> is a fixed collocation, like 'under scrutiny' and 'under investigation'."),
]

GAP = [
 ("Oswald was shot dead <input class=\"gap\" data-answer=\"by\" size=\"7\" aria-label=\"gap\"> a Dallas nightclub owner named Jack Ruby, just two days after the assassination.",
  "<strong>By</strong> introduces the agent in a passive sentence — the person who performed the action."),
 ("Kennedy was the fourth US president to die <input class=\"gap\" data-answer=\"in\" size=\"7\" aria-label=\"gap\"> office, following Lincoln, Garfield and McKinley.",
  "<strong>In office</strong> is the fixed expression for the period when a politician holds their post."),
 ("The &lsquo;magic bullet&rsquo; theory claims that a single bullet passed <input class=\"gap\" data-answer=\"through\" size=\"9\" aria-label=\"gap\"> both Kennedy and Governor Connally.",
  "<strong>Pass through</strong> describes movement entering and leaving a solid object or body."),
 ("The grassy knoll — a small hill to the right of the motorcade — has been <input class=\"gap\" data-answer=\"under\" size=\"8\" aria-label=\"gap\"> intense scrutiny for over sixty years.",
  "<strong>Under scrutiny</strong> follows the same pattern as 'under suspicion': 'under' goes with examination and pressure."),
 ("Some theorists argue that evidence was tampered <input class=\"gap\" data-answer=\"with\" size=\"7\" aria-label=\"gap\"> before it could be properly examined by independent investigators.",
  "<strong>Tamper with</strong> is a fixed phrasal verb — the preposition cannot be separated from it."),
]

ORDER = [
 (["Kennedy", "gave his final speech", "at the Hotel Texas", "in Fort Worth", "on the morning of his death"],
  "Subject → verb phrase → place → more specific place → time. In English the time expression comes last."),
 (["The Warren Commission", "was established", "within weeks", "of the assassination", "to investigate the events"],
  "<strong>Within weeks of</strong> is a two-part prepositional phrase. The infinitive of purpose comes last."),
 (["Protesters", "gathered", "outside the Warren Commission building", "throughout the inquiry", "demanding a full re-examination"],
  "Place ('outside') comes before time ('throughout'). The participle phrase describes simultaneous action and comes last."),
 (["A recording device", "was found", "beneath the dashboard", "of the presidential limousine", "after the car was examined"],
  "<strong>Beneath</strong> gives the specific place, 'of' links it to the whole, and 'after' places it in sequence."),
 (["The case files", "were transferred", "from the National Archives", "to a secure location", "prior to their planned release"],
  "<strong>From … to</strong> expresses movement between two points. 'Prior to' introduces the time clause and comes last."),
]

def mc_slide(n, stem, opts, key, explain):
    buttons = []
    for text, why in opts:
        attrs = ' data-correct' if text == key else ''
        if why:
            attrs += ' data-explain="%s"' % why.replace('"', '&quot;')
        buttons.append('          <button class="opt"%s>%s</button>' % (attrs, text))
    return f'''
    <section class="slide" data-type="mc">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a1e{n}">Activity 1 · Place &amp; movement — {n}/5</div>
        <h2 class="slide-title" data-i18n="a1t">Choose the best preposition</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{stem}</p>
        <div class="opts two-up">
{chr(10).join(buttons)}
        </div>
        <p class="feedback" data-explain="{explain.replace('"','&quot;')}"></p>
      </div>
    </section>
'''

def gap_slide(n, stem, explain):
    return f'''
    <section class="slide" data-type="gap">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a2e{n}">Activity 2 · Fixed collocations — {n}/5</div>
        <h2 class="slide-title" data-i18n="a2t">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
        <p class="q-stem">{stem}</p>
        <div style="margin-top:22px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{explain.replace('"','&quot;')}"></p>
      </div>
    </section>
'''

def order_slide(n, chunks, explain):
    return f'''
    <section class="slide" data-type="order">
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="a3e{n}">Activity 3 · Word order — {n}/5</div>
        <h2 class="slide-title" data-i18n="a3t">Build the sentence</h2>
      </div></div>
      <div class="slide-body">
        <div class="order-hint" data-i18n="orderHint">Click the parts in order · click one again to take it back</div>
        <div class="order" data-answer="{'|'.join(chunks)}"></div>
        <div style="margin-top:18px">
          <button class="btn" data-action="check-order" data-i18n="btnCheck">Check</button>
        </div>
        <p class="feedback" data-explain="{explain.replace('"','&quot;')}"></p>
      </div>
    </section>
'''

def teach_slide(pfx, bg=None):
    b = f' data-bg="{bg}"' if bg else ''
    return f'''
    <section class="slide" data-type="teach"{b}>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="{pfx}e">Language focus</div>
        <h2 class="slide-title" data-i18n="{pfx}t">Title</h2>
      </div></div>
      <div class="slide-body">
        <div class="cols">
          <div class="card"><p class="prose" data-i18n="{pfx}a">A</p></div>
          <div class="card"><p class="prose" data-i18n="{pfx}b">B</p></div>
        </div>
        <div class="card" style="margin-top:16px">
          <p class="prose dim" data-i18n="{pfx}n">Note</p>
        </div>
      </div>
    </section>
'''

# Build the new slide block by surgery on the template's own markup.
start = s.index('    <!-- ── TEACHING SLIDE ───────────────────────────────────── -->')
end   = s.index('    <!-- ── RESULTS ──────────────────────────────────────────── -->')

body = teach_slide('t1')
body += ''.join(mc_slide(i + 1, *MC[i]) for i in range(5))
body += teach_slide('t2', 'jfk/sunglasses.jpg')
body += ''.join(gap_slide(i + 1, *GAP[i]) for i in range(5))
body += teach_slide('t3', 'jfk/skyline.jpg')
body += ''.join(order_slide(i + 1, *ORDER[i]) for i in range(5))

s = s[:start] + body + '\n' + s[end:]

# Activation target chips
s = s.replace('''          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>''',
'''          <span class="bank-chip">in Dealey Plaza</span>
          <span class="bank-chip">on his own</span>
          <span class="bank-chip">under suspicion</span>
          <span class="bank-chip">tampered with</span>
          <span class="bank-chip">along Elm Street</span>''')

open('/tmp/jfk_stage1.html', 'w', encoding='utf-8').write(s)
print('slides built')
