#!/bin/bash
# Website health checks for hijacked, hacked, parked or lapsed domains: audit, check, revise once, check
# again (2 verification rounds max), then build the pack. Resumable: rerun this script.
cd /home/ishank/work/consultancy
D=research/2026-11-13-rescue-audits
python3 tools/batch.py rescue_auditor 3 $D/[0-9][0-9]-* --browser --skip-done --thinking high --timeout 3600 >> $D/audit.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 1 --kind rescue > /dev/null
python3 tools/batch.py rescue_checker 3 $D/verify-r1/* --browser --skip-done --thinking high --timeout 2400 >> $D/verify-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py revise $D 1 --kind rescue fail-only
[ -d $D/revise-r1 ] && python3 tools/batch.py rescue_auditor 3 $D/revise-r1/* --browser --skip-done --thinking high --timeout 3600 >> $D/revise-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 2 --kind rescue > /dev/null
[ -d $D/verify-r2 ] && python3 tools/batch.py rescue_checker 3 $D/verify-r2/* --browser --skip-done --thinking high --timeout 2400 >> $D/verify-r2.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py table $D > $D/final.txt
python3 tools/rescue_pack.py $D >> $D/final.txt
echo done > $D/LOOP_DONE
