#!/bin/bash
# Tier 4 deep audits for the top 25 of the triage ranking: profile, analysis, audit, verify, revise once,
# verify again (2 verification rounds max), then the deliverables pack. Starts after the website health
# checks finish so the two runs do not compete for memory. Resumable: rerun this script.
cd /home/ishank/work/consultancy
R=research/2026-11-13-top25-audits
until [ -f research/2026-11-13-rescue-audits/LOOP_DONE ]; do sleep 120; done
setsid nohup python3 tools/watch.py $R --every 60 --stall-mins 15 > $R/watch.out 2>&1 < /dev/null &
python3 tools/batch.py business_researcher 3 $R/02b-business/* --browser --skip-done --thinking high --timeout 3600 >> $R/profiles.log 2>&1
python3 tools/avenues.py repair $R/02b-business > /dev/null
python3 tools/gate.py profiles $R > $R/gate-profiles.txt
python3 tools/gate.py prep-analysis $R >> $R/gate-profiles.txt
for d in $R/03-analysis/*/; do
  id=$(basename $d)
  cp $R/02b-business/$id/triage.json $d/triage.json
  grep -q triage.json $d/brief.md || echo 'Also read triage.json: an earlier browser review of the website, listing and agent readiness (see wrong_claims for corrections). Use capability G for front-door gaps it shows that the profile confirms.' >> $d/brief.md
done
python3 tools/batch.py opportunity_analyst 3 $R/03-analysis/* --skip-done --thinking high --timeout 1800 >> $R/analysis.log 2>&1
python3 tools/avenues.py repair $R/03-analysis > /dev/null
python3 tools/top_audits.py writers $R
python3 tools/batch.py audit_writer 4 $R/05-audits/* --skip-done --thinking high --timeout 900 >> $R/audits.log 2>&1
python3 tools/top_audits.py verify $R
python3 tools/batch.py verifier 3 $R/06-verify/* --browser --skip-done --thinking high --timeout 2400 >> $R/verify.log 2>&1
python3 tools/avenues.py repair $R/06-verify > /dev/null
python3 tools/revise.py prep $R 1
[ -d $R/05-audits-r1 ] && python3 tools/batch.py audit_writer 4 $R/05-audits-r1/* --skip-done --thinking high --timeout 900 >> $R/audits.log 2>&1
[ -d $R/05-audits-r1 ] && python3 tools/revise.py reverify $R 1
[ -d $R/06-verify-r1 ] && python3 tools/batch.py verifier 3 $R/06-verify-r1/* --browser --skip-done --thinking high --timeout 2400 >> $R/verify.log 2>&1
python3 tools/avenues.py repair $R/06-verify-r1 > /dev/null 2>&1
python3 tools/top_audits.py pack $R
echo done > $R/LOOP_DONE
