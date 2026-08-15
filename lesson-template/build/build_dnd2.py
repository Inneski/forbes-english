# -*- coding: utf-8 -*-
"""Build Part II of The Parisian Conquest from Part I.

Same engine, same hero, same characters — new campaign. Part I was about
winning the account; Part II is about keeping it, which is a different set
of language entirely: cadence, scope, crisis, bad numbers, renewal.
"""
import re

src = open('forbes-dnd-rpg.html', encoding='utf-8').read()
rooms = open('/tmp/dnd2_rooms.js', encoding='utf-8').read()

# ── 1. swap the ROOMS array ──────────────────────────────────────────
start = src.index('const ROOMS = [')
end = src.index('\n];', src.index("name: 'The Throne Room of Maison")) + len('\n];')
s = src[:start] + rooms.rstrip() + src[end:]

# ── 2. titles and chrome ─────────────────────────────────────────────
s = s.replace('<title>The Parisian Conquest | A Business RPG</title>',
              '<title>The Parisian Conquest II: The Long Winter | A Business RPG</title>', 1)
s = s.replace('<div class="main-title">The Parisian Conquest</div>',
              '<div class="main-title">The Parisian Conquest II</div>', 1)
s = s.replace('<div class="main-subtitle">A language &amp; strategy quest · C1 Advanced</div>',
              '<div class="main-subtitle">The Long Winter — keeping what you won · C1 Advanced</div>', 1)
s = s.replace('<div class="game-badge-title">Business RPG</div>',
              '<div class="game-badge-title">Business RPG · II</div>', 1)

# ── 3. dungeon map labels ────────────────────────────────────────────
for old, new in [('Cold Call', 'Kickoff'), ('Pitch Hall', 'Scope'),
                 ('Labyrinth', 'Crisis'), ('Treasury', 'Numbers'),
                 ('Throne Room', 'Renewal')]:
    s = s.replace(f'<span class="mn-label">{old}</span>',
                  f'<span class="mn-label">{new}</span>', 1)

# ── 4. intro ─────────────────────────────────────────────────────────
old_intro = s[s.index('<div class="intro-title">A Quest Begins</div>'):
              s.index('<button class="btn btn-gold" onclick="showScreen(\'screen-char\')">')]
new_intro = '''<div class="intro-title">The Winter After the Victory</div>
        <p class="intro-lore">
          You won. The contract with <strong>Maison Éclore</strong> is signed, the champagne is
          long finished, and the real work has started — the part nobody writes a case study about.<br><br>
          Winning an account and <em>keeping</em> one require almost opposite language. The pitch
          rewarded boldness. The next twelve months reward something harder: saying no without
          damage, delivering bad news before it is discovered, defending numbers that missed,
          and asking for more when you have not been perfect.<br><br>
          Five more dungeons. A brand manager who never chose you, a hall of small favours that
          bleeds you dry, a community crisis at 8:40 in the morning, a finance director with the
          figures printed, and finally the throne room again — twelve months older, with a year
          of evidence on the table.<br><br>
          Your class carries over. Your reputation does not. <em>Do not fumble.</em>
        </p>
        <p class="intro-lore" style="opacity:.75;font-size:.94em">
          Part I — <a href="forbes-dnd-rpg.html" style="color:#c8963e">The Parisian Conquest</a> —
          covers winning the account. You do not need it to play this, but the executives here
          remember you.
        </p>
        '''
s = s.replace(old_intro, new_intro, 1)

# ── 5. victory + game over copy ──────────────────────────────────────
s = s.replace("""  document.getElementById('vic-subtitle').textContent = `${G.name} of ${CLASSES[G.cls].name} \\u2014 Conqueror of Paris`;""",
              """  document.getElementById('vic-subtitle').textContent = `${G.name} of ${CLASSES[G.cls].name} \\u2014 Keeper of the Account`;""", 1)

old_msgs = s[s.index('  const msgs = ['):s.index('  document.getElementById(\'vic-msg\')')]
new_msgs = """  const msgs = [
    `Signed for two years, and Benelux with it. You did not win this by being brilliant in a room — you won it by being predictable for twelve months, honest on the worst morning, and precise about what you would not do. Véronique renews because it works, not because she is locked in.`,
    `The crisis in March is in the case study now, which is the surest sign it was handled. Camille defends your invoices internally. Thierry believes your forecasts. Julien uses the change-request sheet. None of that is glamorous. All of it is why you are still here.`,
    `Anyone can win a pitch. You kept an account through a missed quarter and a community backlash, and came out of it with a bigger remit. That is the harder skill, and almost nobody teaches it.`
  ];
"""
s = s.replace(old_msgs, new_msgs, 1)

old_go = s[s.index('  const goMsgs = ['):s.index("  document.getElementById('go-msg')")]
new_go = """  const goMsgs = [
    `The account is not lost in a single meeting — it is lost in the accumulation of small silences, absorbed favours and deadlines quietly missed. Somewhere in these five rooms, the trust ran out. Renewal goes to tender.`,
    `Delivery is unforgiving in a way that pitching never is: the client sees you every week, and every week is evidence. This time the evidence was against you. Read the coaching. Come back.`,
    `Maison Éclore will work with someone else next year. The work was not the problem — the language around the work was. That is fixable, and it is exactly what this quest is for.`
  ];
"""
s = s.replace(old_go, new_go, 1)

s = s.replace("['Fell in', ROOMS[G.room].name]", "['Lost it in', ROOMS[G.room].name]", 1)

# ── 6. reward-scroll wording that referenced the conquest ────────────
s = s.replace('Conqueror of Paris', 'Keeper of the Account')

open('forbes-dnd-rpg-part2.html', 'w', encoding='utf-8').write(s)
print('written:', len(s), 'bytes')
print('rooms:', s.count("eyebrow: 'Room"))
print('actions:', s.count("stat: '"))
print('coach notes:', s.count('coach:'))
