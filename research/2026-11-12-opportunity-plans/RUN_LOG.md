# Run log: top-10 opportunity plans, 2026-11-12

- **Agents:** 10 opportunity planners, one per audited business from `runs/2026-11-11` (ranks 1-10), each
  given its audit, profile and analysis. DeepSeek v4.1 Flash via `pi`, thinking "high", 3 at a time. Every
  task exited 0.
- **Rounds (capped at 2):** round 1, 1 PASS (Albany County Fasteners) and 9 FAIL (87% of 368 checked claims
  confirmed). After one revision, round 2: 7 PASS (RAM Law, Rich's, Albany, Sayrebrook, Fraser, Wiley
  Lavender, Benaka), 3 FAIL (RCP 7 notes, Soden 2, Gaines 6). Open notes are in `verify-r2/*/output.json`.
- **Common catches:** founder-day totals not matching the phase table or pilot length, competitor tier
  prices recomputed instead of copied, integrations marked confirmed from a pricing page rather than docs,
  feasibility and effort not labelled as inference, business facts not on the business's own pages,
  mis-cited FCC and RPC references. Now a self-check section in `prompts/opportunity_planner.md`.
- **Launcher slip:** the first plan-verifier launch ran before its folders existed and made a stray `*`
  folder (removed); relaunched. A wait loop matched its own command line and stalled round 2 for a while;
  fixed by anchoring the pattern.
- **Repaired:** `verify-r2/03-rich-s-plumbing-heating-air-co/output.json` (unescaped quotes; raw kept). With
  the repair it reads PASS.
- **Not done:** no business contacted; planners' suggested prices are inference and differ for the same
  product ($275-$650/mo for intake), so use the price card in MEMO.md.
