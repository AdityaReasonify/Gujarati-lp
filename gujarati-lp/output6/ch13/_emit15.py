import json, collections

src = 'learning_plan_logical.json'
dst = 'learning_plan_textbook.json'

with open(src, encoding='utf-8') as f:
    plan = json.load(f, object_pairs_hook=collections.OrderedDict)

# traversal order of topic ids in the logical plan
traversal = [t['topic_id'] for m in plan['modules']
             for s in m['segments'] for t in s['topics']]

with open('05b_textbook_order.json', encoding='utf-8') as f:
    printed = json.load(f)['textbook_order']

assert traversal == printed, (traversal, printed)

# ONLY change: ordering flag. Ids, nodes, sequence untouched.
plan['ordering'] = 'textbook'

with open(dst, 'w', encoding='utf-8') as f:
    json.dump(plan, f, ensure_ascii=False, indent=1)
    f.write('\n')

# post-checks
with open(dst, encoding='utf-8') as f:
    out = json.load(f)
t2 = [t['topic_id'] for m in out['modules'] for s in m['segments'] for t in s['topics']]
print('ordering        :', out['ordering'])
print('plan_id         :', out['plan_id'])
print('topics identical:', t2 == traversal, len(t2))
print('modules         :', len(out['modules']))
print('objectives      :', len(out.get('objectives', [])))
print('keys identical  :', list(out.keys()) == list(plan.keys()))
# diff-vs-source: only the ordering value may differ
a = json.load(open(src, encoding='utf-8')); a['ordering'] = 'textbook'
print('byte-equal ex-ordering:', a == out)
