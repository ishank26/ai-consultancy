#!/bin/bash
# Research -> verify -> revise -> verify (2 rounds max) for the agent-readiness checklist.
cd /home/ishank/work/consultancy
D=research/2026-11-12-agent-readiness
python3 tools/batch.py advice_researcher 1 $D/01-* --thinking high --timeout 3000 > $D/research.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 1 --kind advice > /dev/null
python3 tools/batch.py advice_verifier 1 $D/verify-r1/* --thinking high --timeout 2400 > $D/verify-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py revise $D 1 --kind advice
[ -d $D/revise-r1 ] && python3 tools/batch.py advice_researcher 1 $D/revise-r1/* --thinking high --timeout 2400 > $D/revise-r1.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py verify $D 2 --kind advice > /dev/null
[ -d $D/verify-r2 ] && python3 tools/batch.py advice_verifier 1 $D/verify-r2/* --thinking high --timeout 2400 > $D/verify-r2.log 2>&1
python3 tools/avenues.py repair $D
python3 tools/avenues.py table $D > $D/final.txt
