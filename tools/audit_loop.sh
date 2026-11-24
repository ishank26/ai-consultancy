#!/bin/bash
# Write, verify and revise ONE audit until PASS (max 3 revisions). Usage: audit_loop.sh RUN TASK_ID
set -u
RUN=$1; ID=$2; T=$(dirname "$0")
W=$RUN/05-audits/$ID
python3 $T/run_agent.py audit_writer $W $W/brief.md --thinking high --timeout 900 >/dev/null
AUDIT=$W/output.md
for n in 0 1 2 3; do
  V=$RUN/06-verify$([ $n -gt 0 ] && echo -r$n)/$ID; mkdir -p $V
  cp $AUDIT $V/audit.md; cp $W/profile.json $W/analysis.json $V/
  cp $RUN/02a-industry/$(python3 -c "import json;print({c['id']:c['industry'] for c in json.load(open('$RUN/01-map/selection.json'))}['$ID'])")/output.json $V/industry.json
  sed 's/^Write the AI Opportunity Audit for \(.*\)\. Read profile.*/Verify the audit for \1. Files in your folder: audit.md, profile.json, analysis.json, industry.json. Check every factual claim in the audit section AND the "For the founder" email\/opener. Re-open the business pages and each cited URL yourself; for any benchmark behind an impact range, open the original source. Check the audit body is at most ~450 words. Record each check in claims_checked. Write the JSON to output.json./;/^RULES/,$d' $W/brief.md > $V/brief.md
  python3 $T/run_agent.py verifier $V $V/brief.md --thinking high --timeout 1800 >/dev/null
  verdict=$(python3 -c "import json;print(json.loads(open('$V/output.json').read(),strict=False)['verdict'])")
  echo "round $n: $verdict"
  [[ $verdict == PASS* ]] && { echo "FINAL $AUDIT"; exit 0; }
  [ $n -eq 3 ] && { echo "GAVE UP"; exit 1; }
  N=$RUN/05-audits-r$((n+1))/$ID; mkdir -p $N
  cp $AUDIT $N/audit.md; cp $W/profile.json $W/analysis.json $N/
  python3 -c "import json;print(json.dumps(json.loads(open('$V/output.json').read(),strict=False)['issues'],indent=1))" > $N/issues.json
  { echo 'REVISION. audit.md in your folder is the current audit (including the "For the founder" section). issues.json lists problems an independent verifier found. Apply every fix: remove or correct any unsupported or wrong claim (never replace it with a new unsourced claim). Keep the same format, founder section and Sources list. Write the full revised Markdown to output.md.'; echo; sed -n '/^RULES/,$p' $W/brief.md; } > $N/brief.md
  python3 $T/run_agent.py audit_writer $N $N/brief.md --thinking high --timeout 900 >/dev/null
  AUDIT=$N/output.md
done
