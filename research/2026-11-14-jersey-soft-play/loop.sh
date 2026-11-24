#!/bin/bash
# One hand-added business, end to end: triage, independent check, profile, analysis, audit, check, one revision,
# second check (2 verification rounds max), the pack and the printable leave-behind. Resumable: rerun this script.
# DeepSeek agents do every research step; Claude reviews the outputs between the stages marked REVIEW in RUN_LOG.
cd /home/ishank/work/consultancy
R=research/2026-11-14-jersey-soft-play
T=$R/triage
setsid nohup python3 tools/watch.py $R --every 60 --stall-mins 15 > $R/watch.out 2>&1 < /dev/null &

# Stage 1: triage and its checker (same tools as the 2026-11-12 run).
python3 tools/batch.py triage_analyst 1 $T/b001 --browser --skip-done --thinking high --timeout 3600 >> $R/triage.log 2>&1
python3 tools/triage_tools.py rank $T
python3 tools/triage_tools.py checks $T $T/checks --top 1 --sample 0
python3 tools/batch.py triage_checker 1 $T/checks/c* --browser --skip-done --thinking high --timeout 2400 >> $R/triage.log 2>&1
python3 tools/triage_tools.py apply $T $T/checks
python3 - <<'EOF' || { echo "STOP: not operating after triage" > $R/LOOP_DONE; exit 0; }
import json,sys
b=json.load(open('research/2026-11-14-jersey-soft-play/triage/ranking.json'))[0]
print('triage:', b.get('status'), '| check:', b.get('check'), '| site:', b.get('website'))
sys.exit(0 if str(b.get('status','')).lower().startswith('operating') else 1)
EOF

# Stage 2: deep audit in the runs/2026-11-11 layout.
python3 $R/setup_one.py
python3 tools/batch.py business_researcher 1 $R/02b-business/* --browser --skip-done --thinking high --timeout 3600 >> $R/profiles.log 2>&1
python3 tools/avenues.py repair $R/02b-business > /dev/null
python3 tools/gate.py profiles $R > $R/gate-profiles.txt
python3 tools/gate.py prep-analysis $R >> $R/gate-profiles.txt
for d in $R/03-analysis/*/; do
  id=$(basename $d)
  cp $R/02b-business/$id/triage.json $d/triage.json
  grep -q triage.json $d/brief.md || echo 'Also read triage.json: a browser review of the web presence, listing and agent readiness (see wrong_claims for corrections). Use capability G for front-door gaps it shows that the profile confirms.' >> $d/brief.md
done
python3 tools/batch.py opportunity_analyst 1 $R/03-analysis/* --skip-done --thinking high --timeout 1800 >> $R/analysis.log 2>&1
python3 tools/avenues.py repair $R/03-analysis > /dev/null
python3 tools/top_audits.py writers $R
python3 tools/batch.py audit_writer 1 $R/05-audits/* --skip-done --thinking high --timeout 900 >> $R/audits.log 2>&1
python3 tools/top_audits.py verify $R
python3 tools/batch.py verifier 1 $R/06-verify/* --browser --skip-done --thinking high --timeout 2400 >> $R/verify.log 2>&1
python3 tools/avenues.py repair $R/06-verify > /dev/null
python3 tools/revise.py prep $R 1
[ -d $R/05-audits-r1 ] && python3 tools/batch.py audit_writer 1 $R/05-audits-r1/* --skip-done --thinking high --timeout 1800 >> $R/audits.log 2>&1
[ -d $R/05-audits-r1 ] && python3 tools/revise.py reverify $R 1
[ -d $R/06-verify-r1 ] && python3 tools/batch.py verifier 1 $R/06-verify-r1/* --browser --skip-done --thinking high --timeout 2400 >> $R/verify.log 2>&1
python3 tools/avenues.py repair $R/06-verify-r1 > /dev/null 2>&1
python3 tools/top_audits.py pack $R
python3 tools/leave_behind.py audit $R > $R/leave-behind.out 2>&1
echo done > $R/LOOP_DONE
