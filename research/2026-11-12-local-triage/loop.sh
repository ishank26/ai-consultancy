#!/bin/bash
# Tier 1: map every zone, then check and revise once (2 verification rounds max). Resumable: rerun this script.
cd /home/ishank/work/consultancy
D=research/2026-11-12-local-triage
python3 tools/batch.py area_mapper 3 $D/[0-9][0-9]-* --browser --skip-done --thinking high --timeout 3600 >> $D/map.log 2>&1
python3 tools/batch.py area_mapper 3 $D/[0-9][0-9]-* --browser --skip-done --thinking high --timeout 3600 >> $D/map.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 1 --kind zone > /dev/null
python3 tools/batch.py zone_checker 3 $D/verify-r1/* --browser --skip-done --thinking high --timeout 2400 >> $D/verify-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py revise $D 1 --kind zone fail-only
[ -d $D/revise-r1 ] && python3 tools/batch.py area_mapper 3 $D/revise-r1/* --browser --skip-done --thinking high --timeout 3600 >> $D/revise-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 2 --kind zone > /dev/null
[ -d $D/verify-r2 ] && python3 tools/batch.py zone_checker 3 $D/verify-r2/* --browser --skip-done --thinking high --timeout 2400 >> $D/verify-r2.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py table $D > $D/final.txt
echo done > $D/LOOP_DONE
