#!/bin/bash
# Paused-triage wrap-up: wait for the last in-flight batches, rank, then one round of independent checks on the
# top 150 plus a random 10% of the rest (the original scope). Resumable: rerun this script.
cd /home/ishank/work/consultancy
T=research/2026-11-12-triage
for b in b154 b155 b156 b157; do
  for i in $(seq 1 90); do [ -f $T/$b/status.json ] && break; sleep 30; done
done
python3 tools/avenues.py repair $T > /dev/null
python3 tools/triage_tools.py rank $T >> $T/rank.log
[ -d $T/checks ] || python3 tools/triage_tools.py checks $T $T/checks --top 150 --sample 0.1 >> $T/rank.log
python3 tools/batch.py triage_checker 4 $T/checks/c*/ --browser --skip-done --thinking high --timeout 4200 >> $T/checks.log 2>&1
python3 tools/avenues.py repair $T/checks > /dev/null
python3 tools/triage_tools.py apply $T $T/checks >> $T/rank.log
echo done > $T/CHECKS_DONE
