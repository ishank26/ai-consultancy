import json
d = json.load(open('output.json'))
print(d['segment'])
print(d['one_line'][:120])
print('offerings', len(d['offerings']))
print('tiers total', sum(len(o['tiers']) for o in d['offerings']))
print(json.dumps(d['price_ranges'], indent=1)[:600])
