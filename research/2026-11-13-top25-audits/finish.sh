#!/bin/bash
# Finish round 2 for the two tasks the main loop left short: NJP's revision timed out, and Menlo's re-check was never set up.
cd /home/ishank/work/consultancy
R=research/2026-11-13-top25-audits
python3 tools/batch.py audit_writer 1 $R/05-audits-r1/24-njp-associates --skip-done --thinking high --timeout 1800 >> $R/audits.log 2>&1
python3 tools/revise.py reverify $R 1
python3 tools/batch.py verifier 2 $R/06-verify-r1/24-njp-associates $R/06-verify-r1/25-menlo-engineering-associates-inc --browser --skip-done --thinking high --timeout 2400 >> $R/verify.log 2>&1
python3 tools/avenues.py repair $R/06-verify-r1 > /dev/null 2>&1
python3 tools/top_audits.py pack $R
echo done > $R/LOOP_DONE
