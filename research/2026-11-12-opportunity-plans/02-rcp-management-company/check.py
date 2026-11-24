import json, sys
d = json.load(open("output.json"))
print("valid json, keys:", len(d))
req = ["business","opportunity","problem","solution","build_plan","competitors","running_costs","suggested_pricing","leverage","edge_vs_competitors","risks_compliance","feasibility","discovery_questions","caveats","data_gaps"]
print("missing:", [k for k in req if k not in d])
print("competitors:", len(d["competitors"]), "costs:", len(d["running_costs"]), "risks:", len(d["risks_compliance"]))
