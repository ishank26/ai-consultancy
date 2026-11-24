# Run log: pricing research, 2026-11-12

- **Agents:** 10 pricing researchers, one per segment (AI receptionists, human answering, home-services call
  AI, legal intake, property-management AI, leak/freeze sensors, cold-chain sensors, voice-agent platform
  costs, AI agency pricing, insurance certificate automation). DeepSeek v4.1 Flash via `pi`, thinking
  "high", 3-5 at a time. Every task exited 0.
- **Rounds (capped at 2 by the owner):** round 1, 10 FAIL (82% of 324 checked claims confirmed). After one
  revision, round 2: 1 PASS (09 agency pricing), 9 FAIL with 5-10 open notes each. No further revision; the
  open notes in `verify-r2/*/output.json` mark those claims unverified.
- **Common catches:** price on a different page or tier than cited, monthly and annual billing mixed,
  setup fees missed, third-party estimates presented as list prices, ranges that excluded their own cited
  prices, unlabelled inference. These are now a self-check section in `prompts/pricing_researcher.md`.
- **Checked by the orchestrator (2026-11-12):** Smith.ai AI Receptionist (Free/Pro $150/Enterprise $500),
  Ruby ($250/50 min to $1,725/500 min, no setup fee), Retell ($0.07-$0.31/min; parts as listed), Sameday
  (from $449/500 min, $789/1,000 min), NJ AI Automation ($500 audit, $1,500-$5,000 build, $250-$1,000/mo),
  ConnectedFresh (~$150/location + ~$10/unit, ~$190-$210/mo for 4-6 units). LEX Reception hides prices; the
  LawNext directory lists $375/150 min, $395/300 min, $675/500 min (updated 2026-07-30).
- **Repaired:** `verify-r1/03-home-services-call-ai/output.json` had unescaped quotes (raw copy kept).
- **Synthesis:** the price card and anchors are in the owner's learnings doc
  (https://claude.ai/artifact/EMuddoisDyw3YPYGAq4Wkx) and in `../2026-11-12-opportunity-plans/MEMO.md`.
