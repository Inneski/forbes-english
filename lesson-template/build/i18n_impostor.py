# -*- coding: utf-8 -*-
"""Interface strings for Impostor Syndrome (C1), English and Japanese.

The vocabulary notes and the reading-paragraph notes carry their two
language versions inside the data tables in build_impostor.py, so they are
pulled from there rather than retyped — one place to edit, and no risk of
the English drifting from the Japanese. That import is safe in both
directions: build_impostor only imports this module inside its __main__
block.

Scope, as always: chrome and instructions translate. The English being
taught does not. The previous version of this lesson translated the
closing line of the reading into Japanese, which removed the sentence it
existed to demonstrate, and two rows of the discourse-marker table the
same way.
"""
import json, sys
sys.path.insert(0, '/tmp')
from chrome_i18n import CHROME
import build_impostor as B

LIFT = ['btnStart', 'btnCheck', 'btnNext', 'btnRestart', 'scoreLabel', 'slideOf',
        'fbCorrect', 'fbWrong', 'fbAnswer', 'resNext', 'actEyebrow',
        'actSpeakKind', 'btnCopy', 'btnCopied', 'wordCount']

T = {}

T['en'] = dict(
    coverTitle='Impostor <em>Syndrome</em>',
    coverSub='Why do high achievers feel like frauds? — advanced reading, '
             'academic style and a cultural comparison',
    chipLevel='C1 &middot; Academic English',
    chipFocus='Psychology &amp; society', chipCount='45 slides',

    preE='Before you read', preT='Three things to hold in mind',
    pre1h='The claim',
    pre1n='Decide now whether you believe that, and see whether the text '
          'changes your mind.',
    pre2h='The cultural question',
    pre2n='Does a culture that expects public modesty make private doubt '
          'easier to voice, or harder? There is no single right answer, and '
          'the text does not give one.',
    pre3h='The language',
    pre3n='The grammar section is built from sentences in the reading. Mark '
          'the careful ones as you go.',

    vE='Vocabulary',
    vT1='Twelve words (1 of 4)', vT2='Twelve words (2 of 4)',
    vT3='Twelve words (3 of 4)', vT4='Twelve words (4 of 4)',
    vgE='Vocabulary in use', vgT='Complete the sentence',
    vgHint='One word per gap, in the form the sentence needs.',
    vmE='Vocabulary', vmT='Match the term to its definition',
    vmHint='Click a term, then click its definition.',

    rdE='The text',
    rdT1='Reading &mdash; paragraph 1 of 8', rdT2='Reading &mdash; paragraph 2 of 8',
    rdT3='Reading &mdash; paragraph 3 of 8', rdT4='Reading &mdash; paragraph 4 of 8',
    rdT5='Reading &mdash; paragraph 5 of 8', rdT6='Reading &mdash; paragraph 6 of 8',
    rdT7='Reading &mdash; paragraph 7 of 8', rdT8='Reading &mdash; paragraph 8 of 8',

    cE='Critical comprehension', cT='Read for what is implied',

    nomE='Academic style', nomT='Nominalisation: turn the verb into a noun',
    nom1h='The move',
    nom1n='The verb becomes the head noun and the clause collapses into a noun '
          'phrase.',
    nom2h='Why it is done',
    nom2n='It lets you drop the agent. <em>Their acceptance</em> does not say '
          'who accepted them.',
    nom3h='The cost',
    nom3n='Two nominalisations in a sentence is style; four is fog. C1 writing '
          'is knowing where to stop.',
    ngE='Academic style', ngT='Write the noun form',
    ngHint='One word: the noun that the verb or adjective becomes.',

    hedE='Academic style',
    hedT='Hedging: claiming exactly as much as the evidence allows',
    hed1h='The devices',
    hed1n='Modal verbs, reporting verbs, and adverbs of frequency all do this '
          'work.',
    hed2h='What it is not',
    hed2n='This is where it differs from kenson (謙遜). Kenson is about the '
          'speaker; hedging is about the evidence.',
    hed3h='The test',
    hed3n='If yes, hedge it. Paragraph 7 of the reading fails that test — '
          '<em>surefire</em> is the one place the text overcommits.',
    hgE='Academic style', hgT='Choose the hedge',

    colE='Academic style',
    colT='Collocation: the verb that belongs with the noun',
    col1h='Why it matters at C1',
    col1n='<em>Have self-doubt</em> is not an error. <em>Harbour '
          'self-doubt</em> is what a reader of academic English expects.',
    col2h='How to learn them',
    col2n='Learn <em>garner an accolade</em>, not <em>garner</em>. The '
          'vocabulary cards in this lesson give the collocates for exactly '
          'this reason.',
    col3h='Register travels with them',
    col3n='All four are formal. Using one in casual speech is as marked as '
          'using <em>get</em> in a paper.',
    cgE='Academic style', cgT='Complete the collocation',
    dmE='Academic style', dmT='Match the function to the sentence from the text',
    dmHint='Click a function, then click the sentence that performs it.',

    errE='Before the error correction', errT='Five mistakes, and why each one happens',
    err1h='despite / in spite of',
    err1n='The two get crossed, and <em>despite of</em> is the result. There '
          'is no such phrase.',
    err2h='affect / effect &middot; -ly on adjectives',
    err2n='And an adjective after <em>is</em> stays an adjective: <em>is more '
          'prevalent</em>, not <em>is more prevalently</em>.',
    err3h='that / which &middot; parallel gerunds',
    err3n='After feeling, idea, fact and belief, the clause takes <em>that</em>. '
          'And both sides of <em>than</em> must take the same form.',
    egE='Error correction', egT='Write the correction',
    egHint='One word each. Only the wrong word changes.',

    cu1E='Cultural connections', cu1T='謙遜 (kenson) and impostor feelings',
    cu1ah='Kenson is public',
    cu1an='It is a social performance, and everyone in the room knows it is '
          'one.',
    cu1bh='Impostor feeling is private',
    cu1bn='The difference is whether you would be relieved to stop.',
    cu1ch='The open question',
    cu1cn='It may make the words available — or it may make the real thing '
          'impossible to distinguish from the performance.',
    cu2E='Cultural connections', cu2T='空気を読む and pluralistic ignorance',
    cu2ah='The same mechanism',
    cu2an='And both involve getting it wrong, in the same direction, at the '
          'same time as everyone else.',
    cu2bh='Where they differ',
    cu2bn='Reading the room is something you can be good at. Pluralistic '
          'ignorance is what happens when everyone reads it correctly and it '
          'is still wrong.',
    cu2ch='Why the text cares',
    cu2cn='One person saying it out loud breaks the ignorance for everyone in '
          'earshot.',
    cu3E='Cultural connections', cu3T='受験 (juken) and the achievement paradox',
    cu3ah='The setup',
    cu3an='Entry is framed as the culmination of the effort — the point at '
          'which the question is settled.',
    cu3bh='What happens inside',
    cu3bn='Paragraph 5: highly skilled people assume everyone else is equally '
          'skilled. A selective institution makes that assumption locally '
          'true.',
    cu3ch='The paradox',
    cu3cn='This is a good example for the writing task: universal psychology, '
          'culturally specific trigger.',

    actTitle='To what extent is it universal?', actUse='Use at least four:',
    actWriteKind='Writing &middot; 200–250 words',
    actSpeakBrief='One of you argues that the phenomenon is universal. The '
                  'other argues that culture shapes it.',
    actSpeak1='Universal side: use two pieces of evidence from the text, and '
              'hedge both to exactly the strength the text supports.',
    actSpeak2='Cultural side: use kenson or juken as a specific case. A '
              'general claim about "Japanese culture" will not do.',
    actSpeak3='Both: find one point where you actually agree, and say what it '
              'is in one sentence.',
    actSpeak4='Both: identify one claim your opponent overstated, and offer '
              'them the hedge that would fix it.',
    actWriteBrief='To what extent is impostor syndrome a universal '
                  'psychological experience, and to what extent is it shaped '
                  'by cultural and social factors? Use evidence from the text '
                  'and at least two nominalisations.',
    actPlaceholder='The question of whether impostor feelings are universal or '
                   'culturally contingent is…',
    resPerfect='Full marks. The comprehension questions here test implication '
               'rather than recall, so this is a real result.',
    resStrong='Strong. Look again at any comprehension item you missed — the '
              'distractors are all defensible readings, and knowing why they '
              'are wrong is the skill.',
    resMid='A solid pass. The academic-style section is where the marks '
           'usually are: hedging, nominalisation, collocation.',
    resLow='Read the eight paragraphs again before you retry. Every '
           'comprehension answer is traceable to one sentence in the text.',
)

T['ja'] = dict(
    coverTitle='Impostor <em>Syndrome</em>',
    coverSub='なぜ優秀な人ほど「自分は偽物だ」と感じるのか — 上級読解、'
             'アカデミック文体、そして文化比較',
    chipLevel='C1 &middot; アカデミック英語',
    chipFocus='心理学と社会', chipCount='45 スライド',

    preE='読む前に', preT='頭に置いておきたい三つのこと',
    pre1h='本文の主張',
    pre1n='今の時点で賛成か反対かを決めておき、読んだあとで考えが変わったか'
          '확認してください。',
    pre2h='文化に関する問い',
    pre2n='公の場での謙遜を求める文化は、内面の不安を口に出しやすくするのか、'
          'しにくくするのか。唯一の正解はなく、本文も答えを示しません。',
    pre3h='注目する表現',
    pre3n='文法パートは本文の文からそのまま作られています。慎重な言い回しに'
          '印をつけながら読みましょう。',

    vE='語彙',
    vT1='12の語（1/4）', vT2='12の語（2/4）',
    vT3='12の語（3/4）', vT4='12の語（4/4）',
    vgE='語彙の運用', vgT='文を完成させましょう',
    vgHint='各空欄に1語。文に合う形で書いてください。',
    vmE='語彙', vmT='語と定義を結びつけましょう',
    vmHint='語をクリックし、次にその定義をクリックしてください。',

    rdE='本文',
    rdT1='本文 — 第1段落（全8段落）', rdT2='本文 — 第2段落（全8段落）',
    rdT3='本文 — 第3段落（全8段落）', rdT4='本文 — 第4段落（全8段落）',
    rdT5='本文 — 第5段落（全8段落）', rdT6='本文 — 第6段落（全8段落）',
    rdT7='本文 — 第7段落（全8段落）', rdT8='本文 — 第8段落（全8段落）',

    cE='批判的読解', cT='書かれていない含意を読み取る',

    nomE='アカデミック文体', nomT='名詞化 — 動詞を名詞に変える',
    nom1h='操作の中身',
    nom1n='動詞が主要な名詞になり、節が名詞句にまとまります。',
    nom2h='なぜそうするのか',
    nom2n='行為者を省けるからです。<em>Their acceptance</em> は「誰が'
          '受け入れたか」を言いません。',
    nom3h='代償',
    nom3n='一文に名詞化が二つなら文体、四つなら霧です。どこでやめるかを'
          '知っているのがC1の書き手です。',
    ngE='アカデミック文体', ngT='名詞形を書きましょう',
    ngHint='1語で。動詞や形容詞が変化した名詞形を書きます。',

    hedE='アカデミック文体',
    hedT='ヘッジ — 証拠が支える分だけ主張する',
    hed1h='使う表現',
    hed1n='法助動詞、報告動詞、頻度の副詞がこの役割を担います。',
    hed2h='ヘッジではないもの',
    hed2n='ここが謙遜との違いです。謙遜は話し手についての態度、ヘッジは'
          '証拠についての態度です。',
    hed3h='判定の目安',
    hed3n='そうなら、ヘッジをかけましょう。本文第7段落はこの基準を'
          '満たしていません。<em>surefire</em> は本文で唯一言い過ぎている'
          '箇所です。',
    hgE='アカデミック文体', hgT='適切なヘッジを選びましょう',

    colE='アカデミック文体', colT='コロケーション — 名詞に付く動詞',
    col1h='C1で重要な理由',
    col1n='文法が完璧でも語の組み合わせが不自然になることがあります。'
          '<em>have self-doubt</em> は誤りではありませんが、'
          '<em>harbour self-doubt</em> が期待される形です。',
    col2h='覚え方',
    col2n='<em>garner</em> ではなく <em>garner an accolade</em> として'
          '覚えます。語彙カードにコロケーションを載せているのはそのためです。',
    col3h='語域も一緒についてくる',
    col3n='四つとも硬い語です。日常会話で使うと、論文で <em>get</em> を'
          '使うのと同じくらい浮きます。',
    cgE='アカデミック文体', cgT='コロケーションを完成させましょう',
    dmE='アカデミック文体', dmT='機能と本文中の文を結びつけましょう',
    dmHint='機能をクリックし、次にその働きをしている文をクリックしてください。',

    errE='誤り訂正の前に', errT='五つの誤りと、それが起きる理由',
    err1h='despite / in spite of',
    err1n='二つが混ざって <em>despite of</em> になります。そのような表現は'
          'ありません。',
    err2h='affect / effect と形容詞の -ly',
    err2n='また <em>is</em> のあとは形容詞のままです。<em>is more '
          'prevalent</em> であって <em>is more prevalently</em> ではありません。',
    err3h='that / which と並列の動名詞',
    err3n='feeling, idea, fact, belief のあとの節は <em>that</em> を取ります。'
          'また <em>than</em> の前後は同じ形にそろえます。',
    egE='誤り訂正', egT='正しい形を書きましょう',
    egHint='それぞれ1語。誤っている語だけを直します。',

    cu1E='文化との接続', cu1T='謙遜とインポスター体験',
    cu1ah='謙遜は公のふるまい',
    cu1an='社会的な振る舞いであり、その場の全員がそれを承知しています。',
    cu1bh='インポスター体験は私的なもの',
    cu1bn='違いは「やめられるなら安堵するかどうか」です。',
    cu1ch='開かれた問い',
    cu1cn='言葉が用意されることで語りやすくなるのか、それとも本物の不安が'
          '型どおりの謙遜と区別できなくなるのか。',
    cu2E='文化との接続', cu2T='空気を読むことと多元的無知',
    cu2ah='同じ仕組み',
    cu2an='どちらも、全員が同じ方向に、同時に読み違えます。',
    cu2bh='違うところ',
    cu2bn='空気を読むのは上達しうる技術です。多元的無知は、全員が正しく'
          '読んでもなお結果が誤っている状態です。',
    cu2ch='本文がここに触れる理由',
    cu2cn='誰か一人が口に出せば、その場の全員の無知が破れるからです。',
    cu3E='文化との接続', cu3T='受験と達成のパラドックス',
    cu3ah='前提',
    cu3an='一度の選抜のために何年も準備します。合格はその努力の到達点として'
          '語られます。',
    cu3bh='入ったあとで起きること',
    cu3bn='第5段落。優秀な人ほど他人も同じだと考えます。選抜性の高い環境は、'
          'その思い込みを局所的に本当にしてしまいます。',
    cu3ch='パラドックス',
    cu3cn='選抜が厳しいほど、それ自体は問いを解決しません。ライティング課題に'
          '使える例です — 心理は普遍的、引き金は文化固有。',

    actTitle='どこまで普遍的なのか', actUse='最低4つ使うこと:',
    actWriteKind='ライティング &middot; 200–250語',
    actSpeakBrief='一方は「普遍的な現象だ」、もう一方は「文化が形づくる」と'
                  '主張します。',
    actSpeak1='普遍派: 本文から根拠を二つ挙げ、本文が支える強さちょうどに'
              'ヘッジをかけて述べること。',
    actSpeak2='文化派: 謙遜か受験を具体例として使うこと。「日本文化は〜」と'
              'いう一般論では不可。',
    actSpeak3='二人とも: 実際に意見が一致する点を一つ見つけ、一文で述べること。',
    actSpeak4='二人とも: 相手が言い過ぎた主張を一つ指摘し、それを直すヘッジを'
              '提案すること。',
    actWriteBrief='インポスター体験はどこまで普遍的な心理現象であり、どこまで'
                  '文化的・社会的要因に形づくられているか。本文の根拠と、'
                  '名詞化を最低二つ使って書いてください。',
    actPlaceholder='The question of whether impostor feelings are universal or '
                   'culturally contingent is…',
    resPerfect='満点です。ここでの読解問題は暗記ではなく含意を問うものなので、'
               'これは確かな結果です。',
    resStrong='good。間違えた読解問題を見直してください。誤答肢はどれも'
              '「ありうる読み」であり、なぜ違うのかを言えることが力になります。',
    resMid='しっかり合格圏です。得点差が出るのはアカデミック文体のパート — '
           'ヘッジ、名詞化、コロケーションです。',
    resLow='もう一度8つの段落を読んでから再挑戦してください。読解問題の答えは'
           'すべて本文の一文にたどれます。',
)

# The vocabulary collocation lines and the reading notes live in the data
# tables, one per language, so they are attached here rather than retyped.
for _w, _p, _d, _k, _en, _ja in B.VOCAB:
    T['en'][_k] = _en
    T['ja'][_k] = _ja
for _pk, _txt, _nk, _en, _ja in B.PARAS:
    T['en'][_nk] = _en
    T['ja'][_nk] = _ja


def render(code):
    d = dict(T[code])
    for k in LIFT:
        d[k] = CHROME[code][k]
    return '{\n' + ',\n'.join(
        '    %s: %s' % (k, d[k] if k in LIFT else json.dumps(d[k], ensure_ascii=False))
        for k in sorted(d)) + '\n  }'


if __name__ == '__main__':
    base = set(T['en'])
    for c, d in T.items():
        m, x = base - set(d), set(d) - base
        print('%-3s %2d' % (c, len(d)), ('MISSING %s' % sorted(m)) if m else '',
              ('EXTRA %s' % sorted(x)) if x else '')
