import json, pathlib
p = pathlib.Path("output.json")
d = json.loads(p.read_text())
s = p.read_text().replace("adu it history", "audit history")
json.loads(s)
p.write_text(s)
print("valid", len(s))
