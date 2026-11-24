# Patterns memo — batch 2026-11-11 (50 businesses, Milltown NJ + 15 mi)

**Recurring pain points (150 opportunities across 50 businesses)**
- **The front door.** Most of these businesses take requests by phone during office hours, through one
  web form, or through a shared inbox, with nothing after 4–5 pm. This came up in every industry and is
  why operational agents (capability A) made up 96 of the 150 opportunities. The biggest clusters were
  legal intake, healthcare front desks, HVAC and plumbing emergency lines, property-management resident
  requests and insurance service requests.
- **Document and compliance packs.** Certified payroll and subcontractor prequalification (construction),
  certificates of insurance and endorsements (insurance), EDI exceptions and retailer chargebacks (3PL),
  SOC 1 evidence and tax-season document chasing (accounting), and QC paperwork on federal jobs. These are
  repetitive, high-stakes and outside what a chatbot subscription does.
- **Quote and RFQ desks.** Machine shops, steel fabricators, truckers, B2B e-commerce and 3PLs take quote
  requests by form or phone, and an estimator turns each into a priced draft by hand.
- **Knowledge in people's heads.** Knowledge agents (capability C, 31 opportunities) built on the firm's own
  SOPs, carrier guidelines or past projects, aimed at staff turnover and new-hire ramp-up.
- Research agents (B, 6) and edge/physical AI (E, 1) rarely came out of public evidence. Neither can be
  seen from outside the business, so neither should be the lead offer at first contact.

**Most sellable offers**
1. **24/7 intake, triage and booking agent.** An intake or after-hours agent was proposed in all 13 industries, the pilot is narrow, and
   the result is easy to measure (missed or after-hours inquiries captured, time to first response). It is
   also the easiest to explain on a walk-in.
2. **Compliance and document desk agents** (certificates of insurance, certified payroll, EDI and
   chargeback evidence). They are worth more per client, the clients have obvious reasons to pay, and the
   design is hard to copy without integration work.
3. **Quote-desk agents** for manufacturing, trucking and 3PL, where faster quotes win business.

**Strongest first niche**
Average Lead Scores were close (software/IT 69.3 to legal 76.8), and each business was scored once by a
single analyst, so read differences under about 3 points as noise. On the evidence:
- **Legal (small litigation, family and estate firms)** had the highest average (76.8, with all 4 firms at
  74 or above). It has a repeatable intake product and clear confidentiality reasons to want a private
  deployment, which is the consultancy's edge.
- **Trucking/drayage and 3PL in the Middlesex warehouse corridor.** Trucking averaged 75.0. The highest
  score in the batch (PDR, 82) was a 3PL with 250–300+ staff, over the size cap, so it was excluded. Its
  audit is kept as an extra. The work is integration-heavy (EDI, WMS, dock and pier appointments), which
  fits "beyond DIY", but the pilots are larger.

Recommendation: lead with legal intake as the productized offer, and run trucking/3PL as the
higher-value second track. Healthcare scored well (75.5) but carries HIPAA and BAA overhead for a first
pilot.

**Changes for the next batch**
- **Calibrate scoring.** Scores clustered between 63 and 82, with 8 businesses tied at 76. Next time, have
  one analyst re-score the top 20 side by side against fixed anchors.
- **Fix the audit writer before verification.** All 11 first drafts failed verification (the original 10
  plus Gaines, which replaced PDR). The causes were word count (520–680 words), impact ranges that didn't
  follow from their stated assumptions, "businesses like yours often…" lines read as unsourced claims,
  claims about our own clients in the outreach notes, and two misquoted studies (NBER w31161 and the
  Stanford legal-AI hallucination study). It took up to 3 revision rounds to clear them. The tightened
  writer rules in `tools/revise.py` (shown arithmetic, no peer generalizations, no claims about
  ourselves) should be part of the first draft from now on; Gaines used them and passed on its second
  revision.
- **Narrow the impact ranges.** Multiplying every low input and every high input made the ranges honest
  but wide (some vary 10x, for example $3.6k–$45k). For outreach, consider a single "likely case" with the
  range in a footnote, or confirm volumes on the first call.
- **Enforce size with the business's own pages.** Mapper headcounts are often guesses. PDR passed as
  "51–200" but its own About page says 300+. Have the researcher confirm headcount and drop at Phase 2.
- **Pre-filter for observable strain.** 21 of 50 profiles had thin evidence, mostly small firms with no
  hiring posts or reviews. Require at least one hiring or review signal at the mapping stage.
- **Drop or narrow software/IT and B2B services.** These were the lowest averages, and MSPs partly compete
  with the consultancy.
- **Fill in EXCLUDE** (for example, conflicts with the founder's employer) before the next run.
- **Try a single-industry deep dive:** legal across all of Middlesex and Monmouth, 30 firms.
