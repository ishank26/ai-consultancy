#!/bin/bash
# Tier 2-3: browser triage of every mapped business in priority order, ranking after each pass, then one
# round of independent checks on the top 150 plus a random 10%. Resumable: rerun this script.
cd /home/ishank/work/consultancy
M=research/2026-11-12-local-triage
T=research/2026-11-12-triage
until [ -f $M/LOOP_DONE ]; do sleep 120; done
pkill -f "browser_harness.daemon" ; sleep 2
python3 tools/merge_zones.py $M
INNER="Milltown,East Brunswick,North Brunswick,New Brunswick,Highland Park,South River,Spotswood,Helmetta"
python3 tools/merge_zones.py $M batches $T 10 --towns "$INNER" --evidence "http,review,own website"
python3 tools/merge_zones.py $M batches $T 10 --towns "$INNER"
python3 tools/merge_zones.py $M batches $T 10 --evidence "http,review,own website"
python3 tools/merge_zones.py $M batches $T 10
for pass in 1 2; do
  for chunk in $(ls -d $T/b*/ | xargs -n 40 | tr ' ' ','); do
    python3 tools/batch.py triage_analyst 4 $(echo $chunk | tr ',' ' ') --browser --skip-done --thinking high --timeout 4200 >> $T/triage.log 2>&1
    python3 tools/avenues.py repair $T > /dev/null
    python3 tools/triage_tools.py rank $T >> $T/rank.log
  done
done
python3 tools/triage_tools.py checks $T $T/checks --top 150 --sample 0.1
python3 tools/batch.py triage_checker 4 $T/checks/c*/ --browser --skip-done --thinking high --timeout 4200 >> $T/checks.log 2>&1
python3 tools/batch.py triage_checker 4 $T/checks/c*/ --browser --skip-done --thinking high --timeout 4200 >> $T/checks.log 2>&1
python3 tools/avenues.py repair $T/checks > /dev/null
python3 tools/triage_tools.py apply $T $T/checks
echo done > $T/TRIAGE_DONE
