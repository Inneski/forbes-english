# -*- coding: utf-8 -*-
import re
TPL = open('lesson-template/lesson-template.html', encoding='utf-8').read()
s = TPL
s = s.replace('<title>Lesson Title | Forbes English</title>',
              '<title>Must &amp; Have To — Firefighter English | Forbes English</title>')
s = s.replace("  --hero: url('sample-hero.jpg');   /* real lessons: url('<folder>/hero.jpg') */",
              "  --hero: url('firefighter/hero.jpg');")
pal = {'--void':'#090e0b','--surface':'#121c17','--surface2':'#1a2921','--border':'#985f46',
       '--text':'#f5f3f2','--text-dim':'#bfaca3','--accent':'#e08a64','--accent-bright':'#efb69c',
       '--accent-dim':'#bc582d','--secondary':'#4e7a94','--contrast':'#1dedc9'}
for k, v in pal.items():
    s = re.sub(r'(\n  ' + re.escape(k) + r'\s*: )#[0-9a-fA-F]{3,8};', lambda m: m.group(1) + v + ';', s, count=1)

def esc(x): return x.replace('"', '&quot;')

def teach(pfx, bg=None):
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

def gap(eyekey, titlekey, rows, bg=None):
    """rows: list of (german_cue, english_before, answer, english_after, explain)"""
    b = f' data-bg="{bg}"' if bg else ''
    out = []
    for cue, before, ans, after, exp in rows:
        size = max(8, len(ans) + 2)
        out.append(f'''        <div class="gap-row">
          <p class="cue">{cue}</p>
          <p class="q-stem">{before}<input class="gap" data-answer="{esc(ans)}" size="{size}" aria-label="gap">{after}</p>
          <p class="feedback" data-explain="{esc(exp)}"></p>
        </div>''')
    return f'''
    <section class="slide" data-type="gap"{b}>
      <div class="slide-head"><div>
        <div class="eyebrow" data-i18n="{eyekey}">Activity</div>
        <h2 class="slide-title" data-i18n="{titlekey}">Complete the sentence</h2>
      </div></div>
      <div class="slide-body">
{chr(10).join(out)}
        <div style="margin-top:18px">
          <button class="btn" data-action="check" data-i18n="btnCheck">Check</button>
        </div>
      </div>
    </section>
'''

E = {
 1:"<strong>Had to</strong> is the past of <em>have to</em> — and the past of <em>must</em> as well, because <em>must</em> has no past form.",
 2:"<strong>Had to</strong> again: <em>musste</em> → simple past. There is no other option in English.",
 3:"<strong>Has had to</strong> — the present perfect of <em>have to</em>: <em>has</em> + <em>had to</em>.",
 4:"<strong>Have to</strong>. The obligation comes from an official regulation, from outside the speaker.",
 5:"<strong>Must</strong>. This is the speaker's own conviction, not somebody else's rule.",
 6:"<strong>Must not</strong> means forbidden — <em>darf nicht</em>. It is not the negative of <em>have to</em>.",
 7:"<strong>Doesn't have to</strong> means it is not necessary — <em>braucht nicht</em>. Very different from <em>must not</em>.",
 8:"<strong>Must</strong>. A personal decision about the future takes <em>must</em>, not <em>will have to</em>.",
 9:"<strong>Will have to</strong>. A future obligation imposed from outside — a new regulation.",
 10:"<strong>Will have to</strong>. The rule, not the commander, creates the obligation.",
 11:"<strong>Should have</strong> + past participle: the right thing, which did not happen.",
 12:"<strong>Should have</strong> + past participle — regret about something you did not do.",
 13:"<strong>Shouldn't have</strong> + past participle: he did it, and it was the wrong thing to do.",
 14:"<strong>Needn't have</strong> + past participle: you did it, but it was not necessary. Not the same as <em>shouldn't have</em>.",
 15:"<strong>Should have</strong> + past participle — a personal regret about a past decision.",
 16:"<strong>Would have to</strong>. The condition is unreal, so the obligation is conditional too.",
 17:"<strong>Would have to</strong>. <em>Ohne …</em> carries the same unreal condition as an <em>if</em>-clause.",
}

ROWS = {
 1:("Gestern mussten wir sehr schnell reagieren.", "Yesterday, we ", "had to", " react very quickly."),
 2:("Der Feuerwehrmann musste die Leiter aufstellen.", "The firefighter ", "had to", " put up the ladder."),
 3:("Er hat diese Woche schon zweimal Überstunden machen müssen.", "He ", "has had to", " do overtime twice this week already."),
 4:("Es gibt eine offizielle Vorschrift: Alle müssen einen Helm tragen.", "According to regulations, all firefighters ", "have to", " wear a helmet on site."),
 5:("Ich persönlich bin überzeugt: Das ist wirklich sehr gefährlich!", "I think this building is really dangerous — everyone ", "must", " leave now!"),
 6:("Du darfst auf keinen Fall das Gebäude betreten — Lebensgefahr!", "You ", "must not|mustn't", " enter that building — it is life-threatening!"),
 7:("Es ist kein Pflichttermin — er braucht nicht zu kommen.", "It is optional — he ", "doesn't have to|does not have to", " attend the meeting."),
 8:("Ich habe mir fest vorgenommen: Nächste Woche gehe ich ins Fitnessstudio.", "I ", "must", " go to the gym next week — I've already decided."),
 9:("Die neue Vorschrift tritt nächsten Monat in Kraft.", "The new regulation starts next month — everyone ", "will have to", " follow it."),
 10:("Nach dem Einsatz wird der Kommandant einen Bericht erstatten müssen.", "After the operation, the commander ", "will have to", " submit a full report."),
 11:("Du hättest früher Alarm schlagen sollen!", "You ", "should have|should've", " raised the alarm earlier! We lost time."),
 12:("Wir hätten mehr trainieren sollen — der Einsatz war sehr schwierig.", "We ", "should have|should've", " trained more — the operation was very difficult."),
 13:("Er hat das Gebäude betreten — das war falsch und gefährlich.", "He ", "shouldn't have|should not have", " entered that building — it was far too dangerous."),
 14:("Es war doch gar nicht nötig, dass du die ganze Nacht geblieben bist!", "You ", "needn't have|need not have", " stayed all night — the situation was under control!"),
 15:("Der Einsatzleiter bedauert: Ich hätte die Entscheidung anders treffen sollen.", "The incident commander says: &ldquo;I ", "should have|should've", " made a different decision.&rdquo;"),
 16:("Wenn der Brand größer wäre, müsstest du alle evakuieren.", "If the fire were bigger, you ", "would have to|'d have to", " evacuate the whole area."),
 17:("Ohne das neue Fahrzeug müssten wir viel länger warten.", "Without the new vehicle, we ", "would have to|'d have to", " wait much longer."),
}

def R(*ids):
    return [(ROWS[i][0], ROWS[i][1], ROWS[i][2], ROWS[i][3], E[i]) for i in ids]

body  = teach('t1')
body += teach('t2', 'firefighter/street.jpg')
body += gap('a1e1', 'gapT', R(1, 2))
body += gap('a1e2', 'gapT', R(3))
body += teach('t3')
body += gap('a2e1', 'gapT', R(4, 5))
body += gap('a2e2', 'gapT', R(6, 7))
body += teach('t4', 'firefighter/field.jpg')
body += gap('a3e1', 'gapT', R(8, 9))
body += gap('a3e2', 'gapT', R(10))
body += teach('t5')
body += gap('a4e1', 'gapT', R(11, 12))
body += gap('a4e2', 'gapT', R(13, 14))
body += gap('a4e3', 'gapT', R(15))
body += teach('t6', 'firefighter/street.jpg')
body += gap('a5e1', 'gapT', R(16, 17))

start = s.index('    <!-- ── TEACHING SLIDE ───────────────────────────────────── -->')
end   = s.index('    <!-- ── RESULTS ──────────────────────────────────────────── -->')
s = s[:start] + body + '\n' + s[end:]

s = s.replace('''          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>
          <span class="bank-chip">target phrase</span>''',
'''          <span class="bank-chip">had to</span>
          <span class="bank-chip">have to</span>
          <span class="bank-chip">must not</span>
          <span class="bank-chip">don't have to</span>
          <span class="bank-chip">will have to</span>
          <span class="bank-chip">should have</span>''')

# A German cue line above each stem — small, dimmed, clearly not the target language.
s = s.replace('.q-stem {', '''.cue {
  font-family: var(--font-mono); font-size: 12.5px; line-height: 1.4;
  color: var(--text-dim); margin-bottom: 6px;
}
.gap-row + .gap-row { margin-top: 22px; }
.q-stem {''', 1)

open('/tmp/ff_stage1.html', 'w', encoding='utf-8').write(s)
print('ok')
