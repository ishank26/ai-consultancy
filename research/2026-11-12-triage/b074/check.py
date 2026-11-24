import json,re,io
p='output.json'
d=json.load(open(p))
for b in d['businesses']:
    for s in b['sources']:
        if 'facebook' in s.lower():
            print('FB source found', s)
print(len(d['businesses']), [b['ref'] for b in d['businesses']])
