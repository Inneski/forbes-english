# -*- coding: utf-8 -*-
import re, json, html

src = open('koolhas & Lamb.html', encoding='utf-8').read()

def jsblock(name, opener):
    i = src.index(name); j = src.index('\n];' if opener == '[' else '\n};', i)
    return src[i:j]

# ── pull the three data sets out of the page ──────────────────────────
mc = []
blk = jsblock('const mcQuestions = [', '[')
for chunk in re.split(r'\n  \{\n', blk)[1:]:
    def g(k):
        m = re.search(k + r':\s*"((?:[^"\\]|\\.)*)"', chunk)
        return m.group(1).replace('\\"', '"').replace("\\'", "'") if m else ''
    choices = re.findall(r'\{ label: "([A-D])", text: "((?:[^"\\]|\\.)*)" \}', chunk)
    correct = int(re.search(r'correct:\s*(\d)', chunk).group(1))
    mc.append({'context': g('context'), 'q': g('question'),
               'choices': [c[1].replace('\\"','"').replace("\\'","'") for c in choices],
               'correct': correct, 'explain': g('explanation')})

fitb = []
blk = jsblock('const fitbData = {', '{')
bank = re.search(r'wordBank:\s*\[(.*?)\]', blk, re.S).group(1)
BANK = re.findall(r'"([^"]+)"', bank)
for chunk in re.split(r'\n    \{\n', blk)[1:]:
    def g(k):
        m = re.search(k + r':\s*"((?:[^"\\]|\\.)*)"', chunk)
        return m.group(1).replace('\\"','"').replace("\\'","'") if m else ''
    fitb.append({'before': g('before'), 'blank': g('blank'),
                 'after': g('after'), 'explain': g('explanation')})

order = []
blk = jsblock('const reorderData = [', '[')
for chunk in re.split(r'\n  \{\n', blk)[1:]:
    segs = re.findall(r'"((?:[^"\\]|\\.)*)"', re.search(r'segments:\s*\[(.*?)\]', chunk, re.S).group(1))
    ex = re.search(r'explanation:\s*"((?:[^"\\]|\\.)*)"', chunk)
    order.append({'segs': [s.replace('\\"','"').replace("\\'","'") for s in segs],
                  'explain': ex.group(1).replace('\\"','"').replace("\\'","'") if ex else ''})

print('mc', len(mc), 'fitb', len(fitb), 'order', len(order), '| bank', BANK)
json.dump({'mc':mc,'fitb':fitb,'order':order,'bank':BANK}, open('/tmp/kool.json','w'), indent=1)
