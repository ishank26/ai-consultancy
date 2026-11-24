# Pricing and top-10 opportunity plans: memo, 2026-11-12

The living version of this memo is the owner's learnings doc (https://claude.ai/artifact/EMuddoisDyw3YPYGAq4Wkx).
The price card and recommendations are Claude's synthesis (inference). Prices marked "checked" were
re-opened by Claude on 2026-11-12; the rest come from briefs that may carry open verifier notes (see
RUN_LOG.md here and in `../2026-11-12-pricing/`).

## Price card (inference)

| Offer | Pilot (credited to setup) | Setup | Monthly |
|---|---|---|---|
| Intake agent, voice + forms | $1,200-1,500 | $2,500-3,500 | $450-650 with ~500-2,000 min |
| Back-office desk (certificates, quotes, close, QC documents) | $1,500-2,500 | $3,500-5,000 | $550-850 |
| Property triage, per 3 communities | $2,500-6,000 | $5,000 | $750 |
| Cold-chain sensors, per location | none needed | $500-1,500 | $150-200 incl. hardware |

Anchors (checked): Smith.ai AI Receptionist Pro $150/75 calls, Enterprise $500/300 calls; Sameday from
$449/500 min and $789/1,000 min; Ruby $250/50 min to $1,725/500 min, no setup fee; Retell $0.07-0.31/min;
NJ AI Automation $500 audit, $1,500-5,000 build, $250-1,000/mo; ConnectedFresh ~$190-210/mo for 4-6 units.
LEX Reception $375/150 min to $675/500 min (LawNext directory, third-party, July 2026).

## Top 10

| Business | Build | Closest competitors | Planner price: pilot / setup / monthly | Tech/commercial, time | Edge | Round 2 |
|---|---|---|---|---|---|---|
| RAM Law | Bilingual after-hours voice + form intake, deadline/duplicate flags, callbacks | Smith.ai $150; AI Esquire $497; Ruby $250 | $1,500 / $3,500 / $650 | 4/3, 7-8 wk | NJ injury intake, Spanish, case write-back (unconfirmed) | PASS |
| RCP Management | Email/form/phone triage creating Vantaca tickets | Vantaca's own AI; Agent on Call $99 | $6,000 / $5,000 / $750 (3 communities) | 4/3, ~7 wk | Ticket write-back; Vantaca competes | FAIL, 7 notes |
| Rich's Plumbing | After-hours voice agent, gas/CO hard stop, warm transfer | Sameday $449; Ruby $250; AnswerConnect $350 | $1,200 / $2,400 / $450 | 3/3, ~3 wk build + 4 wk pilot | Narrow; Vapi warm transfer experimental | PASS |
| Soden Agency | Certificate desk on AMS360 API, licensed staff approve | Salience $499/150 certs; Native Base $2,499 | $1,500 / $3,500 / $750-850 | 3/3, 8-10 wk part-time | AMS write-back; licensing limits | FAIL, 2 notes |
| Albany County Fasteners | RFQ to Shopware-priced draft quote + certs | Qotora $149-799; AY Automate $3k/mo | $2,500 / $5,000 / $750 | 3/4, 10-12 wk | Their pricing rules; ITAR risk | PASS |
| Sayrebrook Vet | Triage with practice-signed red-flag protocol | VetRec $299; 24PetLine $449 | $1,500 / $3,500 / $550 | 3/3, ~4 wk | Weak | PASS |
| Fraser Brothers | One lead record across 3 brands' forms, inbox, missed calls | RingReady $39; Awava $1,997 + $397 | $2,500 / $4,500 / $550-950 | 4/3, ~7 wk | Multi-brand routing | PASS |
| Wiley Lavender Maknoor | After-hours intake, conflict screen, partner approval, Cal.com | Smith.ai $150; LEX $375; Ruby $250 | $750 / $2,200 / $275 | 4/3, 6 wk | Approval queue; local | PASS |
| Benaka | Federal QC reports and checklists in their Word templates | Procore, Raken (quote); Fieldwire $39-89/user | $1,800 / $3,500 / $450 | 3/3, ~8 wk | No direct rival; federal data rules | PASS |
| Gaines & Associates | QBO pre-close assistant (Intuit MCP server) | Botkeeper $149; Double $10-50/client; Uncat $9/client | $2,000 / $4,500 / $550 (5 books) | 3/3, 6 wk | Firm's checklist, review-first posting | FAIL, 6 notes |

## Recommendations (inference)

1. Lead with law firms (RAM Law, Wiley Lavender): both plans passed, highest technical scores, and
   off-the-shelf tools lack Spanish, conflict screening, partner approval and write-back. Home services
   (Rich's) would be sold against Sameday at the same $449 for the same scope.
2. Build the intake core once. Six of ten are the same agent, but planners chose Telnyx, Vapi and Retell.
   Pick one (Retell suggested: documented booking, warm transfer, fallback mode, no platform fee), with
   Pipecat or LiveKit Agents as the self-host exit.
3. Use one price card; planners priced the same intake product from $275 to $650 a month.
4. First builds take about 14-23 founder-days each, so a side business runs about one build at a time.
5. Running costs are about $15-210 a month per client; the margin is founder time.
