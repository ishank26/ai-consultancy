# Edge and vision AI avenues: research memo, 2026-11-12

**Method.** Sixteen DeepSeek v4.1 Flash researchers each took one avenue: a camera, sensor or on-device model
service sold to independent businesses with 5–200 staff around Milltown. An independent DeepSeek verifier
re-opened the sources behind each brief's numbers, prices, legal rules and outcomes. Briefs then went through
revise-and-reverify rounds until they passed (status table at the end). The final verifiers checked 30–58 claims per
brief. The full briefs are in `NN-avenue/`, with their revisions in `revise-rN/` and verdicts in `verify-rN/`.

Scores and rankings below come from the researchers' own fit scores (out of 100). The recommendations in the
second half are my judgment as orchestrator and are labeled as such.

## The finding that changes the plan: New Jersey alarm licensing

New Jersey treats much of this work as a licensed **alarm business**. Neither research pass could open the
state's guidance on this, so I read the statute myself: N.J.S.A. 45:5A-2 as amended by P.L.2021, c.2,
approved January 21, 2021 ([text](https://pub.njleg.gov/bills/2020/PL21/2_.PDF)).
- **What counts as an alarm business:** selling, installing, servicing or maintaining "electronic security
  systems", which expressly include CCTV and access control. It also covers "artificial intelligence and
  evolving technology used for physical security applications", meaning any device, computer or software used
  for detection, security, surveillance or monitoring of unauthorized access.
- **"Installation" includes the site survey and the system design,** not just mounting the hardware.
- **Who is exempt:** the 1997 act exempts licensed electrical contractors and their employees, plus regulated
  telephone and cable companies ([P.L.1997, c.305](https://pub.njleg.gov/bills/9697/PL97/305_.HTM)).

**What this means:**
- **Shoplifting detection, site intrusion and gate monitoring** are squarely licensed work. So are cameras
  sold for security.
- **Sensors for temperature, leaks or vibration are not security systems,** so they appear to fall outside
  it. The statute's definitions are about warning of intrusion and discouraging crime.
- **Cameras used for operations** (table state, dock flow, counting, quality inspection) are a grey area,
  because the act's CCTV definition is broad. Get a written answer from the Division of Consumer Affairs, or
  work with a licensed alarm or electrical contractor, before quoting any camera install.

## How the 16 avenues ranked

Fit score sub-scores: demand 20, local buyers 15, ability to pay 15, technical feasibility 20, low legal risk
15, defensibility 15. The Licensing column is my reading of the statute above, not legal advice.

| Fit | Avenue | Fine-tuning needed? | Pilot cost (researcher's estimate) | Licensing |
|---|---|---|---|---|
| 78 | Warehouse dock safety and flow (near-misses, dock-door dwell) | Mostly no; zones and calibration | $8k–18k | Grey area (cameras) |
| 74 | Cold-chain and food-safety sensors (coolers, HACCP-style logs) | No; rules on NJ temperature limits | $1.2k–4.1k | Outside (sensors) |
| 72 | Other: self-storage gate monitoring, unstaffed gyms, laundromats | No for the core | $5.7k–11k | Licensed (security) |
| 69 | Multifamily leak, freeze and boiler sensors, plus common-area cameras | Mostly no | $5k–10.4k | Sensors outside; cameras licensed |
| 69 | Machine and equipment monitoring (vibration, current) | No; baselining | $7k–18k | Outside (sensors) |
| 68 | Edge stack (cross-cutting; see below) | VLM almost never; detector usually | $5k–15k kit | — |
| 67 | Warehouse receiving: counts, damage photos, label and BOL reading | Detector yes, on the site's own cartons | $6k–15k | Grey area |
| 67 | Manufacturing visual QC stations | No for the first version (trains on good parts only) | $6.5k–20k | Likely outside (inspection station) |
| 66 | Construction site cameras (PPE, progress, intrusion) | PPE classes yes | $6k–12k | Intrusion licensed |
| 66 | Auto shop intake (condition photos, plates, bay timing) | Detector lightly | $4k–9k | Grey area |
| 66 | NJ compliance-by-design service (cross-cutting) | — | — | Unauthorized-practice-of-law risk |
| 63 | Trucking yard and gate vision (DVIR photos, seals) | Detector yes | $6k–12k | Grey area |
| 60 | Restaurant kitchen line (handwash, gloves, ticket times) | Yes, narrowly | $4.5k–11k | Grey area; staff monitoring |
| 60 | Retail shelf gaps and price tags | Detector yes (300–800 labeled images per store) | $4.5k–9.5k | Grey area |
| 57 | Restaurant table state (open, seated, needs bussing) | Calibration per restaurant | $2.4k–6.8k | Grey area |
| 57 | Retail loss prevention without face recognition | Item-level scan detection needs a custom detector | $5k–9k | Licensed (security) |

## Your three ideas, specifically

**Restaurant table waiting and cleaning (fit 57).**
- **It works technically.** The proven design is person detection, a zone drawn over each table and simple
  state rules. A small vision-language model is only needed to double-check unclear cases.
- **The business case is weaker than it looks.** Restaurant margins are thin. Presto launched a vision
  product, ran it with a franchisee and then dropped it ([Restaurant Business,
  2025](https://www.restaurantbusinessonline.com/technology/restaurants-take-closer-look-computer-vision)).
  Maître'd sells the same per-table product.
- **The evidence for the benefit is indirect.** It comes from a field study of 94,404 restaurant visits:
  longer waits meant more parties leaving before being seated and a longer gap before they came back
  ([J. Operations Management, 2018](https://doi.org/10.1016/j.jom.2018.05.001)). No study measures table
  cameras themselves.

**Shoplifting (fit 57, the lowest).**
- **High risk.** The FTC banned Rite Aid from facial recognition for five years after false matches led staff
  to follow, search and eject innocent customers
  ([FTC](https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without)).
  Separately, a 2026 loss-prevention study found self-checkout raises shrink by 22% on average in its first
  year ([ECR](https://ecrloss.com/research-paper/self-checkout-loss-report-2026/)).
- **Licensed work.** In NJ it requires an alarm license.
- **The safe version is narrow:** match camera events against checkout data and send short clips to a person
  for review. No face recognition and no automatic accusations.

**Fine-tuning a small vision model (LFM2.5-VL, Cactus).** Every brief reached the same verdict:
- **The vision-language model is rarely what needs fine-tuning.** Detectors need training on each site's own
  images. A 2–4B vision-language model is best used only when a rule fires, to describe or double-check a
  flagged frame.
- **Small models are weak at counting.** In a peer-reviewed counting test where objects were partly hidden,
  even GPT-4o got 14.75% of counts wrong
  ([ICCV 2025](https://openaccess.thecvf.com/content/ICCV2025/papers/Pothiraj_CAPTURE_Evaluating_Spatial_Reasoning_in_Vision_Language_Models_via_Occluded_ICCV_2025_paper.pdf)).
- **Running the model continuously gets expensive.** An independent benchmark ran LFM2.5-VL-3B on an NVIDIA
  Jetson Orin NX: about 2.35 seconds for one image, and only 2 cameras stayed under a 3-second response
  ([OpenZeka, 2026](https://whitepapers.openzeka.com/vlm-inference-benchmarks/lfm2-5-vl-3b/jetson-orin-nx-16gb/q8-0-llama-cpp/)).
- **Cactus fits phones and tablets,** for example a supervisor photographing a shelf or a damaged pallet, not
  fixed cameras.

**AI sensors.** These are the strongest group:
- They are deterministic rules that need no training.
- They are outside the alarm licensing rules.
- They don't film customers or staff.
- They have a clear compliance hook. FDA's study of deli food safety (2015–16 data) found 70.0% of delis out
  of compliance on holding refrigerated food at the right temperature
  ([FDA](https://www.fda.gov/media/148247/download)).

## Recommendation (orchestrator judgment)

1. **Lead with sensors.** Sell a cold-chain and food-safety monitoring package to restaurants, delis, bakeries
   and grocers. It is the cheapest pilot, needs no license, and is easy to explain on a walk-in ("who checks
   the walk-in at 2 am?"). Add equipment monitoring for machine shops and laundromats. Add leak and boiler
   sensors for property managers, which also fits RCP Management from the last run.
2. **Make camera work for warehouses the second track,** once the licensing answer is in: dock safety, dwell
   time and receiving counts. It scored highest (78), Middlesex is a warehouse corridor, and it pairs with the
   trucking and 3PL track from the 2026-11-11 run. Plan on a licensed installer partner.
3. **Keep restaurant table state as an upsell** for restaurants already using the sensors, not a first offer.
   Don't sell shoplifting or other security products unless you get licensed.
4. **Build one reusable kit:**
   - **Recorder and rules:** Frigate on an N100 mini PC ($249.99).
   - **Detector:** a Coral USB accelerator ($111) or a Hailo module.
   - **Vision-language model, only when needed:** LFM2.5-VL-3B or Qwen3.5-2B/4B, on a Jetson Orin Nano
     Super ($249).
   - **Sensor hub:** Home Assistant.
   - **Licensing:** Ultralytics YOLO is AGPL-3.0, so either buy their enterprise license or ship
     Apache-licensed detectors such as RF-DETR.
5. **Rules for every install:** no face recognition, audio off, a person reviews every alert, written staff
   notice, and a written retention schedule. A lawyer writes the notices; the consultancy does not.

## Open questions for you

- Get a Division of Consumer Affairs determination on operations cameras, apply for an alarm license, or
  partner with a licensed installer?
- Lead with the sensor package, or test camera demand first?

## Verification status

All 16 briefs passed independent verification. "Passed in round" is the verification round with the final
PASS (round 1 checked the first drafts; none passed there). Verifiers may PASS a brief that still has minor
notes; those notes (column "notes") are in each `verify-rN/<avenue>/output.json` and were not fixed.
`avenues.json` is the playbook built from these final versions; `gate.py prep-analysis` hands each analyst
only the avenues for its industry.

| Avenue | Passed in round | Fit | Verdict | Notes | Claims confirmed |
|---|---|---|---|---|---|
| 01-restaurant-table-state | 5 | 57 | PASS | 4 | 33/33 |
| 02-restaurant-kitchen-line | 3 | 60 | PASS | 4 | 39/42 |
| 03-cold-chain-food-safety-sensors | 3 | 74 | PASS | 6 | 29/31 |
| 04-retail-loss-prevention-nonbiometric | 3 | 57 | PASS | 2 | 40/40 |
| 05-retail-shelf-inventory | 3 | 60 | PASS | 7 | 33/35 |
| 06-warehouse-dock-safety | 3 | 78 | PASS | 9 | 38/39 |
| 07-warehouse-receiving-damage-count | 3 | 67 | PASS | 4 | 38/38 |
| 08-manufacturing-visual-qc | 3 | 67 | PASS | 7 | 40/40 |
| 09-equipment-monitoring-sensors | 4 | 69 | PASS | 3 | 38/39 |
| 10-construction-site-vision | 3 | 66 | PASS | 5 | 37/40 |
| 11-trucking-fleet-vision | 3 | 63 | PASS | 4 | 36/36 |
| 12-property-sensors-multifamily | 5 | 69 | PASS | 5 | 29/30 |
| 13-auto-service-intake | 3 | 66 | PASS | 4 | 33/34 |
| 14-other-local-physical-services | 5 | 72 | PASS | 7 | 43/43 |
| 15-edge-vlm-stack | 5 | 68 | PASS | 8 | 55/58 |
| 16-nj-camera-sensor-law | 3 | 66 | PASS | 5 | 34/35 |
