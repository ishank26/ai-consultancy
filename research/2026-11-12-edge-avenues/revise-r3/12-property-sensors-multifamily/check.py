import json
d = json.load(open('output.json'))
print("valid JSON, keys:", len(d))
fs = d['fit_score']
sub = {k: fs[k] for k in ['demand','local_buyers','ability_to_pay','technical_feasibility','legal_risk_low','defensibility']}
print(sub, "sum:", sum(sub.values()), "total:", fs['total'])
print("Mercy url:", [m['source_url'] for m in d['measured_outcomes'] if 'mercyhousing' in m['source_url']])
print("30%" in json.dumps(d), "$10,000" in json.dumps(d))
