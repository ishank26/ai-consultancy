# Run 2026-11-11 — Phase 0 plan

Orchestrator: Claude (Opus 5.5). Subagents: DeepSeek v4.1 Flash via Command Code (pi + pi-web-access:
web_search, fetch_content, get_search_content, source_check). Launcher: tools/run_agent.py, tools/batch.py.

CONFIG
- HOME_BASE: Milltown, NJ 08850. RADIUS: 15 miles (East Brunswick, New Brunswick, North Brunswick, Edison,
  South Brunswick, Piscataway, Highland Park, Old Bridge, Monroe, Sayreville, South River, Spotswood,
  Metuchen, Woodbridge, South Plainfield, Franklin Twp/Somerset, Jamesburg, Matawan/Old Bridge edge).
- BATCH_SIZE: 50 researched; top 10 get full audits.
- TARGET_SIZE: 5–200 employees, independent or regional; no national chains, corporate franchises, government.
- INDUSTRIES: the 13 in the pack.
- EXCLUDE: none supplied (the pack's placeholder was left blank). Flagged as an open question in RUN_LOG.

Industry mix: 13 industries x ~4 = 50 (logistics/3PL and trucking get 4 each; Middlesex County is a
warehouse corridor). Mapper runs once per industry for ~6 candidates (~78 total buffer).

Model split: one model (DeepSeek v4.1 Flash) for every role as the owner asked; thinking "high" for
industry analyst, opportunity analyst and verifier, "medium" for mapper, researcher and writer.
Parallelism: 6 subagents at a time (host has ~6.5 GB free; production bots share it).
Orchestrator checks between phases: schema, source URLs, >=3 facts, dedupe, size and chain rules.
