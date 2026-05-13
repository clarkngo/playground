# Changelog — Root Playground & Global

Path: `/` (main `index.html`, `CLAUDE.md`, shared infrastructure)
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-05-10

### [feature] `classroom-activities/data-governance/module-05.html` — Module 05 Lab Guide
- Created full lab guide: "SmartFactory — The IoT Data Chaos" (Data Ingestion & Medallion Architecture)
- Purple theme (`#6e40c9`), 6 task accordion parts: API Ingestion, Databricks Setup, Bronze Layer, Silver Layer, CSV Sensor Ingestion, Architecture + OpenMetadata
- Two dataset schemas: OpenWeather API JSON (7 fields) and IoT Sensor CSV (5 sample rows including null fault row S005)
- Medallion badge CSS classes: `.lc-bronze` (amber), `.lc-silver` (gray), `.lc-gold` (yellow), `.lc-raw` (muted)
- SQL block border `#6e40c9` (purple), SQL keyword color `.sk` set to `#bc8cff`
- 4 deliverables: D1 Notebook, D2 OpenMetadata screenshots (4 tables), D3 Data Lake vs Warehouse comparison, D4 IoT Architecture Design
- Reflection on Bronze/Silver separation as governance requirement vs. software engineering practice

### [feature] `classroom-activities/data-governance/module-05-deliverables.html` — Module 05 Student Submission
- Created student submission page with purple theme matching module-05
- D1: Notebook viewer with 10 cells (In [1]–[10]) — API simulation, weather Bronze/Silver, sensor CSV Bronze/Silver, live output cells for save confirmations and row counts
- D2: 4 OpenMetadata placeholder slots — `weather_bronze` Bronze, `weather_silver` Silver, `sensor_bronze` Bronze, `sensor_silver` Silver
- D3: 6-feature Data Lake vs Warehouse comparison table (data type, schema approach, storage cost, use case, data quality, governance role) with lab-specific examples in every row
- D4: SmartFactory IoT architecture table — 7 layers (Sensors → Ingestion → Bronze → Silver → Gold → Catalog → Dashboard) with technology choices and governance roles
- Process notes card documenting Bronze intentional null retention, no .format() anti-pattern, OpenMetadata saveAsTable() requirement

### [feature] `classroom-activities/data-governance/index.html` — Module 05 card added
- Added Module 05 card with purple `#6e40c9` accent
- Tags: Medallion Architecture, OpenWeather API, Databricks, PySpark, IoT Sensors, OpenMetadata
- Links to `module-05.html` and `module-05-deliverables.html`

## 2026-05-06

### [feature] Class notes — Module 6 Architecture
- Created `class-notes/data-governance/module-06.html` — 17-section notes on "Architecture" with GitHub dark theme
- Section 1: Architecture Fundamentals — logical vs physical, three levels (high-level, network, systems)
- Section 2: Data Architecture — interrelationships, scaled (centralized + distributed) architecture pattern
- Section 3: Data Design Principles — quality, efficiency, reliability, user-intuitive; consumer-first denormalization; ServiceNow API ID resolution example
- Section 4: OLTP & Transactional Systems — characteristics, ACID, why OLTP is a poor analytics platform
- Section 5: Data Stores, Warehouses & Data Marts — centralized warehouse diagram, star schema, data mart trade-offs
- Section 6: Operational RDS/ORDS — definition, golden source aggregation, Vanguard ORDS on Redshift example
- Section 7: Why RDS Matters & Trade-offs — 4 benefits, read scaling strategies, 5 cons (eventual consistency, schema drift, cost)
- Section 8: CQRS Pattern — commands vs queries, write/read database separation diagram, in-memory query layer
- Section 9: CQRS at Scale — multi-technology data layer, ML vs analytics consumers, syntactic translation engine
- Section 10: RDS Components — governance/technical metadata, validation rules, versioned service contracts, integrity & quality checks table
- Section 11: RDS Tiers — 6-layer `.tier-stack` diagram: marketplace, central metadata, providers, incoming, access, consumer
- Section 12: Data Ingestion — batch/streaming/event-driven/CDC modes, schema evolution, idempotency, backfill
- Section 13: COTS, APIs & SaaS — vendor lock-in minimization, API integration challenges table (rate limits, pagination, schema drift)
- Section 14: Historical Data Service — SCD Type 1/2/3 table, immutability principle, retention policies
- Section 15: Design Variations — row/columnar/document/key-value/time-series/graph store comparison table
- Section 16: Data Replication — Sqoop/rsync/StorSimple/AWS Gateway/WanDisco, provider responsibilities, metadata replication
- Section 17: Access, File Manipulation & Delivery — fine-grained access, file manipulation pipeline, intelligent consumption, on-demand RDS, data delivery contract elements table, cross-domain integration considerations table
- New CSS: `.tier-stack`/`.tier-row`/`.tier-body`/`.tier-chip` (layered tier diagram), `.cqrs-wrap`/`.cqrs-side`/`.cqrs-mid` (CQRS split diagram)
- `class-notes/data-governance/index.html`: added Module 06 card, updated progress to "6 of 6 modules"
- `class-notes/index.html`: updated badge to "6 Modules"
- JS syntax check: passed; no console errors

### [feature] Class notes — index pages and breadcrumb navigation
- Created `class-notes/index.html` — top-level course browser showing "Data Governance" as a clickable card (Active · 5 Modules badge)
- Created `class-notes/data-governance/index.html` — module list with numbered cards (01–05), descriptions, topic tags, progress bar ("5 of 5 modules"), and breadcrumb: Playground → Class Notes → Data Governance
- Updated breadcrumbs in all 5 module files: "Class Notes" now links to `../index.html` and "Data Governance" links to `index.html`; previously both were plain text

### [feature] Class notes — Module 5 Collection
- Created `class-notes/data-governance/module-05.html` — 17-section notes on "Collection" with GitHub dark theme
- Section 1: What We Want from Data — collect→store→transform→analyze→act pipeline, noise-to-signal framing
- Section 2: Collection, Transformation & Business Rules — ETL vs ELT distinction, business rule examples
- Section 3: Designing & Managing Data Processes — 5-step process creation lifecycle (identify → design → implement → operate → retire)
- Section 4: Data Management Metrics & the CDO — 8-metric table, CDO charter and responsibilities
- Section 5: Digital Disruption — 6-wave `.evo-strip` timeline (e-commerce, mobile, AI, IoT, cloud, sharing economy)
- Section 6: Fragmentation of Data — siloed systems, manual management, language fragmentation
- Section 7: Reasons for Data Disruption — 9-row table with reason, description, and symptom columns
- Section 8: Architecture Evolution — Point-to-Point → Hub-and-Spoke (ESB) with visual `.arch-box` diagrams and Big Ball of Mud warning
- Section 9: Data Warehouses & Limitations — advantages vs limitations, data mart workaround
- Section 10: Data Lakes — 3-zone model (raw/cleansed/curated), warehouse vs lake comparison table, data swamp warning
- Section 11: Lakehouse — Delta Lake, OneLake/Microsoft Fabric, Fabric vs Databricks comparison table
- Section 12: Enterprise Architecture & Data Architecture — EA definition, data as side effect of application transactions
- Section 13: Collections & Golden Data Sources — definitions, 4 challenges of heterogeneous data
- Section 14: Heterogeneous Data & DDD — domain, subdomain, bounded context, ubiquitous language with examples
- Section 15: Business vs Technology Architecture — capability-to-system mapping table
- Section 16: Business Architecture Patterns & Golden Source Rules — 3 patterns, 5 golden source rules (R1–R5)
- Section 17: Data Delivery Contracts, Silo Elimination & Data Staging — contract elements table, data mesh, staging when/when-not
- New CSS components: `.evo-strip`/`.evo-item`/`.evo-dot`/`.evo-body` (vertical evolution timeline), `.arch-box`/`.arch-app`/`.arch-hub`/`.arch-line` (architecture diagrams), `.pill` variants (green/red/yellow/blue/purple)
- JS syntax check: passed; no console errors on load

---

## 2026-04-29

### [bug] Lessons learned — Module 04 guide missing `expired_data` saveAsTable step
- `lessons-learned/bug-fixes.md`: Part 3 of the guide jumped from identifying expired rows directly to saving `retained_data`, skipping the `saveAsTable("expired_data")` step; without a catalog entry, students cannot tag the table "Expired" in OpenMetadata and cannot complete D2; root cause: guide was written from policy logic without tracing the full notebook execution

### [feature] Lessons learned — PySpark saveAsTable format anti-pattern
- `lessons-learned/bug-fixes.md`: added entry "Do Not Specify `.format()` When Saving a Plain DataFrame to a Table" — covers `.format("parquet")` breaking Delta DML, redundant `.format("delta")`, the correct pattern (omit format for plain saves, explicit Delta only when using Delta features), with code examples showing BAD / UNNECESSARY / GOOD cases

### [feature] Module 04 deliverables — notebook viewer updated to actual ipynb content
- `classroom-activities/data-governance/module-04-deliverables.html`: D1 notebook viewer rebuilt from `Module04_Data_Lifecycle.ipynb` — 16 cells (11 code + 5 markdown section headers); path corrected to `/Volumes/workspace/default/Volume/`; cells 10–11 include live execution output (`Archive completed: 2026-04-29 17:46:17.023459`); markdown section headers (Archive Process, Verify Archive Movement, Deletion Workflow, Delta Version Tracking, Lifecycle Automation Script) rendered with dark blue background
- D2 screenshots expanded from 2 slots to 4 (2a lifecycle classification, 2b transactions_active, 2c transactions_archive, 2d expired_data); screenshots renamed from macOS timestamp format using Python to handle narrow no-break space in filenames

### [feature] Module 04 — Data Lifecycle Management (FinBank case study) created
- Created `classroom-activities/data-governance/module-04.html` — full lab guide with 6 task accordions (Parts 1–6), dataset preview table, lifecycle status badges, SQL blocks with teal left border, deliverables list, link bar, and reflection
  - Part 1 (teal): Dataset Setup & Active/Historical Partitioning (Steps 1–5)
  - Part 2 (blue): Archive Process — Save & Verify Tables (Steps 6–8)
  - Part 3 (red): Deletion Workflow — 7-Year Retention Rule (Steps 9–11)
  - Part 4 (purple): Delta Version Tracking — History & Rollback (Steps 12–14)
  - Part 5 (green): Lifecycle Automation Script & Audit Logging (Steps 15–16)
  - Part 6 (amber): OpenMetadata Lifecycle Tags & Recovery Planning (Steps 17–19)
  - Teal color scheme: `.page-badge { background: #0e7490 }`, `.case-title { color: #22d3ee }`
  - JS syntax check: passed (no errors)
- Created `classroom-activities/data-governance/module-04-deliverables.html` — standalone student submission page
  - Teal color scheme matching lab guide
  - Progress bar: 4 steps, all marked done
  - **D1**: 8-cell notebook viewer (CSV load, active/historical split, table save, SQL verification, expired data identification, retained table save, Delta UPDATE + DESCRIBE HISTORY, automation script + structured log)
  - **D2**: 2 screenshot slots with `onerror` placeholder fallback; LifecycleStage tag reference table (Active/Archived/Expired/Deleted); table tagging summary
  - **D3**: Retention policy table (Archive boundary, Deletion rule, Version Tracking, Automation) with regulatory citations (SOX, Dodd-Frank, GDPR Article 5); proof-of-deletion log entry block
  - **D4**: Recovery strategy table — 3 scenarios (accidental deletion, system failure, compliance audit) with specific SQL commands and RTO commitments
  - Reflection: 5-step process, 4 key learnings, 3 blocker cards, Final Status checklist (6 items)
- Updated `classroom-activities/data-governance/index.html`: added Module 04 card (teal accent, Delta Lake/Lifecycle/Retention Policy/Compliance Audit tags) with links to both files

---

## 2026-04-28

### [feature] `class-notes/data-governance/module-04.html` — Module 4: Data Sustainment class notes
- 17-section class notes page covering: Data Sustainment definition, Governance Roles & Hats (8-role matrix), People Layers (Strategic/Tactical/Operational), Controls & Data Flow (preventive/detective/corrective), Data Completeness, Validation Rules (6 rule types with scenarios), Governance Capability Model (5 levels incl. MDM golden records), Quality Assessment (7 dimensions), Data Availability (5 failure types), Knowing & Finding Data (catalog, data dictionary, terminology conflict), Redundancy/Hierarchy/Aggregation, Relationships & Data Repurposing, Security & Authorization (RBAC/ABAC/DAC/MAC + direct vs indirect), Organizational Contexts (legacy/cloud-native/regulated), Challenges & Strategies, Data Administration, Lifecycle Risk Points
- New card components: `.cap-row` / `.cap-level` capability maturity bars; `.risk-row` 4-column lifecycle risk cards
- Sticky TOC with 5 groups; JS scroll-based active highlighting; smooth scroll on click

## 2026-04-26

### [feature] Data Governance homepage — Module 03 card added
- `classroom-activities/data-governance/index.html`: added Module 03 card (red accent, HIPAA/PHI/PII tags) with links to `module-03.html` and `module-03-deliverables.html`
- Module 02 status badge updated from "New" to "Live"; link label updated from "Deliverables Checklist" to "Student Submission" to match Module 01 and 03 phrasing

### [feature] Module 03 deliverables page — separate file matching module-01/02 pattern
- Created `classroom-activities/data-governance/module-03-deliverables.html` — standalone student submission page following exact same structure as `module-02-deliverables.html`
  - Navbar: back link to module-03.html
  - Progress bar: 4 steps, all marked done
  - **D1**: full 7-cell Jupyter-style notebook viewer with syntax-highlighted PySpark, sample output table, and before/after masking comparison
  - **D2**: 4 screenshots with `onerror` placeholder fallback (deliverable-2a-roles, 2b-datasensitivity-tags, 2c-column-tagging, 3-security-policies); insight strips explain tag semantics and role routing
  - **D3**: policy summary table (5 policies with scope, key rule)
  - **D4**: risk heat matrix (R1-R3), HIPAA CFR citation table, Databricks + OpenMetadata compliance side-by-side, academic BAA gap callout
  - Reflection: Process steps, Key Learnings (4 topics), Blockers (3 cards), Final Status checklist
  - Export PDF button (print-safe CSS)
- Updated `classroom-activities/data-governance/module-03.html`:
  - Removed expanded deliverables accordions and compact grid (moved all content to deliverables page)
  - Added `.deliv-list` and `.deliv-link-bar` CSS
  - Deliverables section now shows simple 4-item "Required Submissions" card + link bar to deliverables page

---

## 2026-04-23

### [feature] Workshop Proposal v2 + cross-navigation between all three docs
- `workshop-planning/implications-of-ai-for-police-firefighters-paramedics-proposal-v2.html`: new 1-hour format proposal (bundled)
- `proposal-v1.html`: floating `.__workshop-nav` bar appended — links to Planning Doc and v2
- `proposal-v2.html`: floating `.__workshop-nav` bar appended — links to Planning Doc and v1
- `implications-of-ai-for-police-firefighters-paramedics.html`: "Workshop proposals" section added at top of Context tab with styled buttons linking to v1 and v2
- `index.html`: v2 card added to Workshop Planning section; section count 2→3; nav badge 2→3

### [refactor] Workshop file renamed
- `seattle-ai-literacy.html` → `implications-of-ai-for-police-firefighters-paramedics.html`
- Updated href, card name, meta path, icon, and search tags in `index.html`

### [feature] Workshop Proposal v1 + Case Studies tab
- Added `workshop-planning/implications-of-ai-for-police-firefighters-paramedics-proposal-v1.html` — formal stakeholder proposal document (v1)
- Added `📁 Case Studies` tab to `implications-of-ai-for-police-firefighters-paramedics.html`: Corti×SFD (Seattle), Longeye×Redmond PD + Prepared 911 (Washington), Overland AI×Cal Fire (US)
- Updated `index.html`: new card for proposal v1, section count 1→2, nav badge 1→2

### [feature] Case Studies tab — 4 real deployments organized by region
- Added new tab `📁 Case Studies` (`tab-case-studies`) to `implications-of-ai-for-police-firefighters-paramedics.html`
- Organized into 3 regions with dashed placeholder cards for future additions
- **Seattle:** Corti × Seattle Fire Dept / Medic One — 149k calls/yr, 0.25% → full review coverage, 13% stroke call reduction, rapid COVID protocol deployment (Aug 2024)
- **Washington:** Longeye × Redmond PD — 60 hrs of calls processed in minutes; Prepared 911 — language access, notes vs. transcription gap, surge hold time reduction
- **Rest of US:** Overland AI × Cal Fire — Seattle-founded autonomous ULTRA ground vehicles detecting smoke pre-911 in remote wildfire terrain (GeekWire 2026)
- Added CSS: `.cs-card`, `.cs-card-header`, `.cs-tool-name`, `.cs-agency`, `.cs-loc-badge` (Seattle/WA/US variants), `.cs-body`, `.cs-section-lbl`, `.cs-stats`, `.cs-stat`, `.cs-add-card`

### [feature] KPI Impact tab — 22 KPIs across Police, Fire, and EMS
- Added new tab `📊 KPI Impact` (`tab-kpis`) to `implications-of-ai-for-police-firefighters-paramedics.html`
- **Police (8 KPIs):** Positive — report writing time, officer time-in-service, bulk evidence review speed, gunshot detection response. Negative — report accuracy/Brady risk, racial enforcement disparity, CJIS exposure, community trust
- **Fire (6 KPIs):** Positive — wildfire detection lead time (25 min earlier), hotspot coverage, resource pre-positioning. Negative — false alarm rate, fire-risk neighborhood equity, crew situational awareness dependency
- **EMS/Paramedics (8 KPIs):** Positive — PCR documentation time (up to 80% reduction), cardiac arrest recognition speed, language access wait time, 911 surge hold time, NEMSIS compliance. Negative — clinical translation accuracy (cyanosis omission example), AI triage error rate (1 in 20), HIPAA exposure
- Each KPI shows: current baseline, AI-adjusted outlook, ▲/▼ direction pill, key tool(s)
- Facilitator takeaway card: no tool moves only one direction; negative KPIs compound without governance; unmeasured negatives are highest-risk
- Added `.pill-red` CSS class

### [feature] AI Tools tab — 15 curated first-responder tools
- Added new tab `🛠️ AI Tools` (`tab-tools`) to `implications-of-ai-for-police-firefighters-paramedics.html`
- Source: `clarkngo.github.io/AI-tools/?category=First+Responder` — fetched and embedded all 15 tools
- Organized into 4 sections: Police & Investigations (Code Four, Axon Draft One, Truleo, Mark43, Axon Fusus, SoundThinking, Longeye), EMS & Paramedics (ImageTrend Elite, ESO, Corti), Fire & Wildfire Detection (Pano AI, OroraTech), Dispatch & 911 (Prepared 911, Carbyne, RapidSOS)
- Each tool card: emoji, linked name, department track badge(s), description, feature tags
- Traffic Light placement guide table mapping all tools to Green/Yellow with key caution per tool
- Added CSS: `.tools-grid`, `.tool-card`, `.tool-name`, `.tool-emoji`, `.tool-desc`, `.tool-tags`, `.tool-tag`

### [feature] Seattle AI Literacy — title change and full content refresh for first-responder audience
- **Title changed** across all surfaces: `<title>`, breadcrumb, page header, subtitle, tags → "Implications of AI for Police, Firefighters, & Paramedics"
- **Context tab:** Workshop goal rewritten to name Code Four, Longeye, CJIS, HIPAA, KCPAO, and the specific audience. Signals table "Workshop Implication" column rewritten with first-responder-specific tactics
- **Audience tab:** Full rewrite — 6 first-responder roles replacing generic city tiers: Police Officers – Patrol, Detectives & Investigators, Firefighters & Station Crews, Paramedics & EMTs, 911 Dispatchers, Command & Leadership. Room composition questions updated to match
- **Key Themes tab:** All 8 card descriptions rewritten for public safety context. Priority mapping columns changed to Police-Detectives / Fire-Crews / Paramedics-EMS / Command
- **Workshop Formats tab:** All 4 formats rewritten — lightning talk opens with Code Four frog, scenario workshop uses hallucinated DUI / 911 translation / vendor bias audit, learning series 5 sessions rebuilt for first responders
- **Sample Workshop #1:** Title card updated to new workshop name
- **Open Questions tab:** Full rewrite — 10 questions specific to SPD/SFD/EMS rooms, tool deployment status, KCPAO stance, and field hallucination reporting

### [feature] Seattle AI Literacy — Hands-On Activities tab
- Added new tab `🎮 Hands-On Activities` (`tab-activities`) to `workshop-planning/seattle-ai-literacy.html`
- 5 facilitator-ready scenarios with setup, source input, sample AI conversation, and reveal-on-demand answer key
- **S1 — The Hallucinated DUI Report (Police):** Source notes vs. Code Four AI draft; participants find 4 hallucinations including a flipped denial and wrong charge
- **S2 — The 60-Hour Call Stack (Investigations):** Longeye-style call summary; AI fabricates one of three supporting calls; teaches cross-verification before warrant
- **S3 — The Language-Barrier 911 Call (EMS/Dispatch):** Prepared translation drops "se está poniendo azul" (turning blue / cyanosis); changes dispatch code from fall to potential cardiac
- **S4 — The Bias Audit (Leadership):** Vendor predictive patrol tool with 73% training data from 3 historically over-policed districts; feedback loop analysis; recommended reject criteria
- **S5 — The Safe Prompt Challenge (All):** Unsafe vs. safe prompt side-by-side producing same raw notes; identifies invented weapon, cause, and intent; shows 4 safe-prompt constraint clauses
- Added CSS: `.scenario-block`, `.track-badge` (police/ems/investigations/leadership/all), `.chat-bubble` (user/ai), `.input-box`, `.scenario-answer` (reveal toggle), `.reveal-btn`
- Added JS: `toggleAnswer(id)` toggles answer visibility and button label between "Reveal Answer" / "Hide Answer"

### [feature] Seattle AI Literacy — Real-world tools, risks, and safe use guidance
- `workshop-planning/seattle-ai-literacy.html`: Added three new subsections to the Safe-Vibe Lab Proposal tab
- **2a. Real-world tools in deployment:** Code Four (Utah/Heber City, $30/officer/month, 1–2 hr manual report time, shape-shifted-to-frog hallucination example, still requires human correction; FOX 13 link), Longeye (Redmond PD, 60 hours of phone calls processed in minutes), Prepared (notes vs. transcription gap detection, real-time AI translation, hold time reduction; YouTube link)
- **2b. Risks we cannot ignore:** AI reinforces bias (predictive feedback loops), AI-generated reports pose legal risks (Brady exposure, wrongful charges) — cites Fair and Just Prosecution June 2025 report with PDF link
- **2c. So what now? Using AI safely:** Expands on the "given the risks, how do we proceed?" question with three principles — human-in-the-loop on all evidentiary output, use AI where error is recoverable, build the audit habit before tools arrive — plus university positioning and a workshop takeaway prompt

### [feature] Data Governance — Module 3: Data Protection
- Created `class-notes/data-governance/module-03.html` with 22 sections following the Module 1/2 design system (dark theme, sticky TOC, def/concept/insight/warn cards, flow diagrams, compare tables)
- **Section coverage:** CIA Triad → Data as Strategic Asset → Data Classification (4-tier chart: Public/Internal/Confidential/Restricted) → Planning Data Protection → Network & Perimeter Security → Data Lineage & Transit → Encryption (DEK/KEK/KMS/CMEK hierarchy) → IAM evolution (Kerberos/LDAP/SAML/OAuth/OIDC/Zero Trust) → Cloud Data Protection (shared responsibility, JIT, PIM, CMEK, conditional access) → Physical Security & IoT → Data Exfiltration threats & prevention table → DLP → Agile protection (SIEM, differential privacy, event threat detection) → Best Practices → Culture of Data Privacy (role-based training table) → Leadership & company personas → Transparency & incident response lifecycle (Detect/Respond/Remediate/Learn) → Data Security & Recovery (RTO/RPO, 3-2-1 rule, immutable backups) → Data Privacy & HIPAA (GDPR/HIPAA/CCPA/PCI-DSS table) → Regulations & legal interplay → Data Culture (Intentional/Trustworthy/Scalable) → Beyond Data Literacy / ISACA (CISA/CISM/CRISC/COBIT)

## 2026-04-22

### [ux] Seattle AI Literacy — modern layout and readability pass
- `workshop-planning/seattle-ai-literacy.html`: Plus Jakarta Sans, refined color tokens, layered page background, hero-style page header, pill-style tab bar with focus rings, larger body type and line-height, elevated cards with hover, improved tables (striping, wrapping first column), stronger quote block, resource card hover lift, tab enter animation, reduced-motion overrides

### [feature] Seattle AI Literacy — Safe-Vibe Public Safety Lab proposal tab
- Added new tab `Safe-Vibe Lab Proposal` to `workshop-planning/seattle-ai-literacy.html` (`tab-safe-vibe-proposal`) with university-led initiative framing, competitor landscape, case studies, 2026 day-in-the-life narrative, BWC lab focus, and School President alignment table

---

## 2026-04-21

### [feature] Seattle AI Literacy workshop page — added Sample Workshop #1 tab
- Updated `workshop-planning/seattle-ai-literacy.html` to add a new tab button and section: `Sample Workshop #1`
- Added full "AI on the Front Lines" workshop blueprint for SPD, SFD, and Seattle EMTs, including 4-part agenda (landscape, implications, prompt lab, policy roadmap)
- Included detailed hands-on activity (`Incident Report Refiner`) and materials checklist (slide deck, prompting cheat sheet, data privacy guide, feedback form)
- Added SPD compliance visual to the workshop tab (`assets/spd-use-case-diagram-2025-2026.png`) with contextual caption for prohibited vs conditional vs permitted AI use
- Added Washington AI policy framework visual (`assets/wa-ai-policy-framework.png`) with caption tying statewide priorities to Seattle workshop governance context
- Added click-to-zoom lightbox behavior for workshop images (open on image click, close via backdrop, close button, or Escape key)
- Added local source document `assets/Washington_AI_Blueprint.pdf` and linked it in the Resources tab as "Washington AI Blueprint (PDF)"
- Added university-partner 2-hour workshop variant in `tab-sample-workshop-1`, including Ground Truth context, Traffic Light policy table, Redline exercise flow, strategy module, and university preparation checklist
- Added EMS/Fire "Hands-on Sandbox" expansion to the sample workshop tab: Radio-to-PCR activity, syndromic deployment scenario, multi-agent dispatcher exercise, Private-RAG lab setup, policy green-light table, and Seattle AI Incident Card checklist
- Added a high-level overview and in-tab subsection navigation for `Sample Workshop #1` using anchor jump links (visuals, modules, activities, Private-RAG, policy table, incident card)
- Increased color contrast for the Sample Workshop #1 overview/navigation area (stronger tinted panel, brighter link chips, higher-contrast hover state)
- Added a new Pillar 3 alignment section in `Sample Workshop #1`: workforce upskilling summary, module-to-objective mapping, implementation gap-mender framing, and participation takeaway
- Refreshed `Sample Workshop #1` visual design to reduce reading fatigue: themed tab background, higher-contrast section labels, alternating card accent rails, richer table striping, and an at-a-glance meta summary strip
- Added a dedicated 60-minute NCyTE-style hands-on lab block in `Sample Workshop #1` with 3 tracks (Police Redline, EMS/Fire Structured Triage, Leadership Bias/Equity audit) and defined checkout deliverables

---

## 2026-05-03

### [feature] Team Project — HDD Failure Prediction (Backblaze Drive Stats)
- New directory: `team-project/hdd-failure/`
- New file: `team-project/hdd-failure/index.html` — full 5-tab project workspace for the Big Data & ML course, gold/yellow accent theme
  - **Tab 1 — Domain Learning:** S.M.A.R.T. attribute explanation, bathtub curve (early-life/steady-state/wear-out), Backblaze Drive Stats facts (30M+ drive-days, ~1.13% AFR), predictive SMART attributes table (smart_5, 9, 187, 188, 197, 198), label engineering challenge (30-day window function), temporal split warning
  - **Tab 2 — Team Action Items:** 4-member task boards (M1: Data Ingestion & Label Engineering, M2: EDA & Baseline, M3: ML Pipeline, M4: Paper Lead) with deliverables: `01_data_ingestion_labeling.ipynb`, `02_eda_backblaze.ipynb`, `03_ml_pipeline_gbt.ipynb`, `team_paper_hdd.docx`
  - **Tab 3 — Project Framework:** GBTClassifier pipeline diagram, success criteria (AUC-ROC > 0.85, recall > 0.70, beat Backblaze baseline rule), known challenges (extreme class imbalance, dataset size, quarterly schema changes, label window logic)
  - **Tab 4 — Course Alignment:** all 10 course chapters mapped with emphasis on Ch. 7 (optimization), Ch. 8 (Streaming — highly relevant for daily snapshots), Ch. 9 (Data Lakes for schema evolution)
  - **Tab 5 — Paper Guide:** EDSIG/CONISAR structure with page budgets, Backblaze-specific citation guidance
- New file: `team-project/hdd-failure/pm.html` — 5-tab interactive PM dashboard (gold theme, localStorage keys `pm-hdd-tasks-v1` / `pm-hdd-ai-v1`)
  - 36 tasks across M1–M4 with Kanban click-to-cycle (To Do → In Progress → Done)
  - 8-row risk register (extreme class imbalance, dataset size, schema changes, label window error, temporal leakage, CrossValidator runtime, SMART nulls, Spark justification)
  - Special "Label Engineering Review" meeting between M1 and M3
  - Same dashboard/timeline/meeting accordion structure as PdM PM dashboard
- Updated `team-project/index.html`: added HDD project card; Active Projects count: 1 → 2
- Updated main `index.html`: added HDD collection card to Team Projects section; nav badge 1 → 2; section count 1 project → 2 projects
- JS syntax checks: both files pass `node --check`

---

## 2026-04-19

### [feature] PM Dashboard for Predictive Maintenance team project
- New file: `team-project/predictive-maintenance/pm.html` — 5-tab interactive project management dashboard
- **Tab 1 — Dashboard:** per-member progress cards with live progress bars (driven by localStorage task state); overall completion bar; next-actions priority list
- **Tab 2 — Task Board:** interactive Kanban with 36 tasks across M1–M4; click-to-cycle status (To Do → In Progress → Done → To Do); state persists in localStorage; Reset All button
- **Tab 3 — Timeline:** 6-week Gantt-style table with per-member tasks per week, milestone markers, and key dependency table
- **Tab 4 — Risks:** 8-row risk register with severity/probability ratings and mitigations (class imbalance, CrossValidator runtime, StringIndexer label order, etc.)
- **Tab 5 — Meetings:** 4 accordion meeting entries (Kickoff, Data Handoff, Mid-project, Final Review) each with agenda and action item checkboxes persisted in localStorage
- Added PM Dashboard button link to `team-project/predictive-maintenance/index.html` header
- Bug fix: task-list text overflow in Team Action Items tab — switched from flex anonymous text node to JS-wrapped `.task-text` span with `min-width:0; flex:1; overflow-wrap:break-word`

### [feature] Team Projects section — Predictive Maintenance
- New top-level directory `team-project/` added under Classroom in sidebar nav and main `index.html`
- New file: `team-project/index.html` — collection index listing all team projects
- New file: `team-project/predictive-maintenance/index.html` — full 5-tab project workspace for the Big Data & ML course team project
- **Tab 1 — Domain Learning:** PdM maintenance types (reactive → predictive), AI4I 2020 dataset details sourced directly from Matzka IEEE AI4I 2020 paper, all 5 failure modes with exact trigger thresholds (TWF/HDF/PWF/OSF/RNF), feature importance findings, XAI concepts (explainable decision trees, LIME), class imbalance visualization (3.39% failure rate), asymmetric cost insight (false negative = 30× false positive)
- **Tab 2 — Team Action Items:** 4-member task boards (M1: Data Engineering Lead, M2: EDA & Analytics Lead, M3: ML Pipeline Engineer, M4: Paper & Presentation Lead) with numbered tasks and named deliverable notebooks; coordination checkpoint table
- **Tab 3 — Project Framework:** abstract, Spark ML pipeline diagram, 5-section framework table with owners, success criteria cards, known challenges with mitigations (class imbalance, RNF unpredictability, CrossValidator runtime)
- **Tab 4 — Course Alignment:** all 10 course chapters mapped to project tasks; quick-reference API table for every Spark/MLlib class used
- **Tab 5 — Paper Guide:** EDSIG/CONISAR structure (7 sections with page budgets), 3 required references with citation text

---

## 2026-04-18

### [feature] Workshop Planning section — AI Literacy for Seattle City Staff
- New section `workshop-planning/` added to `index.html` with sidebar nav link
- New file: `workshop-planning/seattle-ai-literacy.html` — planning document for a future AI literacy workshop targeting Seattle City staff
- Content: 6 tabs (Context, Audience, Key Themes, Workshop Formats, Open Questions, Resources)
- Extracts intelligence from City of Seattle 2025–2026 AI Plan (Pillar 3: Workforce Upskilling), AI Policy POL-211, and CTAB resources
- Audience segments: Officials, Managers, Front-line Employees, Technologists
- Theme priority matrix mapping 8 content themes to 4 audience tiers
- 4 workshop format options: Lightning Talk, Half-Day, Scenario-Based, Learning Series
- 9 open questions covering audience, format, and outcome decisions

---

## 2026-04-15

### [feature] Module 02 deliverables page with supporting evidence
- New file: `classroom-activities/data-governance/module-02-deliverables.html` — student submission page with 4 required screenshot deliverables (D1 Business Glossary, D2 Governance Policies, D3 Metadata Catalog, D4 Lineage Diagram) and D5 Reflection (medallion architecture visual, process steps, key learnings, roadblocks, final status checklist)
- Supporting evidence section with 5 supplementary screenshots: `00-databricks-raw-data.png`, `00-connection-test-success.png`, `00-custom-property-steward.png`, `00-governance-policies-overview.png`, `00-schema-column-level-tags.png`
- Created `module-02/submission/` directory for screenshot assets
- Wired deliverables link into `index.html` Module 02 card

### [feature] Data Governance classroom activities section homepage + Module 02 lab
- New file: `classroom-activities/data-governance/index.html` — section homepage listing Module 01 and Module 02 as navigatable cards with links to case study, deliverables, and lab guide
- New file: `classroom-activities/data-governance/module-02.html` — full lab guide for "GlobalTrust Bank: The Duplicate Records Crisis"; covers Part 1 (Databricks data quality: upload, profiling, 4 quality checks, 4 cleansing steps, optional Great Expectations validation) and Part 2 (OpenMetadata: metadata ingestion, business glossary, data classification tags, metadata cataloging, governance policies, lineage tracking, retention policies); includes sample dataset with highlighted DQ issues, code blocks with syntax highlighting, expected outputs table, 6 deliverables, and learning outcomes
- Updated `module-01.html` navbar and breadcrumb to link back to new section homepage
- Updated `module-01-deliverables.html` breadcrumb to link back to section homepage and Module 01
- JS syntax checks pass on all new files

### [feature] Add Module 2 card to homepage
- Added Module 2 collection card to the Class Notes section in `index.html`; bumped section count label from "1 module" to "2 modules"



### [feature] Data Governance Module 2 class notes
- New file: `class-notes/data-governance/module-02.html`
- 19 sections covering the full arc of Module 2: When Data Quality Fails, Six Dimensions of Quality, Source System Landscape, Enterprise Data Dictionary, Top-Down vs Bottom-Up dictionary building, Semantic Matching & NLP (addresses student question on same-concept different-name fields), Data Cataloging & Metadata Management (dual-layer metadata, policy decoupling, sensitivity shift, data residency, visibility vs access), OLTP→OLAP→Reporting integration patterns (batch/NRT/streaming comparison table), Data Assessment & Profiling, Data Normalization, Data Lineage Tracking, Data Transmission & ETL (tools table: Kafka, Spark, Airflow, Informatica, SAP, Oracle EDQ, Databricks), Key Management & Encryption (KMS, TPM), Identity & Access Management (conditional policies, no/partial/full access, four governance decisions table), Data Retention & Deletion, External Data Acquisition, Governance Tools Landscape (Collibra, Alation, Purview, Informatica, OpenMetadata, Apache Atlas, Databricks Unity Catalog), Automation at Scale, and The Bigger Picture (discoverability, security, accountability)
- Matches module-01.html design system exactly; JS syntax verified

## 2026-04-14

### [feature] AI4I 2020 dataset guide — domain knowledge section added
- New section in `deep-dives/ai4i-2020-dataset-guide.html`: **Domain Knowledge — Why the Data Looks the Way It Does**
- 6 subsections: CNC Milling Fundamentals (sensor-to-physics table), 5 Failure Modes in Depth (physical mechanism, operator observation, trigger rationale, cost of missing), Feature Correlations (4 callout blocks on torque/wear/temp/power relationships), Product Type significance (L/M/H table + modeling implication), Synthetic vs. Real data (side-by-side cards + generalization caveat), ML Intuition (asymmetric cost structure, alarm fatigue, why tree models dominate)
- New CSS: `.dk-prose`, `.dk-table`, `.dk-fm`, `.dk-callout` (blue/orange/purple/green), `.dk-row`, `.cost-grid`, `.cost-card`, `.dk-subhead`

## 2026-04-13

### [feature] AI4I 2020 Predictive Maintenance Dataset Guide — new deep dive
- New file: `deep-dives/ai4i-2020-dataset-guide.html` — reference guide for the Kaggle AI4I 2020 milling dataset
- Feature dictionary: all 14 columns with type, range, description, and modeling notes (leakage warnings, encoding notes)
- 5 failure mode cards (TWF, HDF, PWF, OSF, RNF) — each with case count, trigger condition, key features, and ML insight; color-coded by mode
- Class imbalance visual: bar charts for Machine Failure (96.6% / 3.4%) and per-mode breakdown
- Derived features table + Python code snippet: Power [W], Temp Delta [K], OSF Factor, Tool Wear Rate — with formulas and failure mode mapping
- 8 ML modeling considerations: class imbalance, data leakage, feature engineering priority, model choice, SHAP/XAI, multi-label vs binary, RNF handling, threshold calibration
- Dataset quick stats grid + citation box with links to Kaggle, UCI ML Repository, and the companion PdM primer
- `deep-dives/index.html`: added entry card (03) in Live Entries grid
- `index.html`: Deep Dives nav badge 1 → 2; section count "1 entry" → "2 entries"; AI4I card added to Deep Dives section; Primer nav badge 4 → 5

## 2026-04-12

### [ux] `classroom-activities/data-governance/module-01-deliverables.html` — timeline collapsed by default with expand affordance
- Starts collapsed; animation fires only on first expand via `hasPlayed` flag
- Header now a bordered pill button (`border: 1px solid #30363d`, hover → blue border + tinted bg)
- Always-visible summary row: three pills (6 phases, 20 steps, 3 blockers resolved) + italic "click to expand" hint that fades on header hover

### [ux] `classroom-activities/data-governance/module-01-deliverables.html` — collapsible timeline
- "How I Built This" header is now a click-to-toggle; chevron rotates ▼↔▶; body fades and slides via `max-height` + `opacity` transition
- Root cause of initial clipping bug: `position: static` on `.tl-body` let absolutely-positioned spine/dot children escape `overflow: hidden`; fixed with `position: relative`

### [refactor] `classroom-activities/data-governance/module-01/` — rename long case study folder
- Renamed `Module 01 Case Study Enterprise Data Governance Foundation/` → `module-01/` for kebab-case consistency
- Updated all 9 screenshot `src` and iframe `src` in `module-01-deliverables.html` (`module-01/submission/...`)

### [refactor] `classroom-activities/data-governance/module-01-deliverables.html` — move and rename deliverables page
- Moved from deep `submission/deliverables.html` to `data-governance/module-01-deliverables.html` alongside `module-01.html`
- Fixed all relative paths: navbar back-link (`module-01.html`), breadcrumb (`../../index.html`), 9 screenshot `src` and iframe `src` now prefixed with `Module 01 Case Study Enterprise Data Governance Foundation/submission/`

### [feature] `classroom-activities/data-governance/.../submission/deliverables.html` — process flow animation
- Added animated vertical timeline (6 phases · 20 steps) showing the full end-to-end activity workflow
- Phase 1: Env Setup (Docker, port conflict, resolution) · Phase 2: MySQL/Workbench Config (grants, default schema) · Phase 3: Airflow Ingestion (pipeline run, task logs, 0 records, filter fix) · Phase 4: Metadata Tagging (customers + orders, PII labels) · Phase 5: Ownership & Roles (steward + owner assignment) · Phase 6: Reflection (lessons-learned, deliverables html)
- CSS: `--pc`/`--pcr` custom properties for per-phase color; `tl-spine-fill` animates `height` via JS-set transition duration; alternating `node-r`/`node-l` grid; `::before` connectors; `.tag-badge` variants (err/fix/milestone)
- JS: IIFE with `PHASES` data array; DOM builder; staggered `setTimeout` at 260ms/step; Replay button resets + re-runs; stat label shows final count on completion

---

## 2026-04-09

### [feature] `index.html` — Classroom nav group and content sections
- Added "Classroom" sidebar nav section with two links: Class Notes and Class Activities (each badged with count)
- Added `data-section="class-notes"` main section: collection card linking to `class-notes/data-governance/module-01.html` with full search metadata tags
- Added `data-section="classroom-activities"` main section: collection card linking to `classroom-activities/data-governance/module-01.html`
- Both sections participate in existing sidebar filter and `/` keyword search

### [feature] `class-notes/data-governance/module-01.html` — Data Governance Module 1 class notes
- New top-level section `class-notes/` with subsection `data-governance/`
- 17-section scrollable class notes page covering: Data Mgmt vs Governance (DMBOK), data quality dimensions, data catalog & discovery, CIA triad in ETL, data lineage & auditability, MDM (4 implementation styles), 3 metadata types, enterprise architecture roles, 3 pillars of trust, and regulatory urgency
- All `<insert example>` placeholders from raw notes filled in: corrugated box manufacturing lifecycle, cross-department cascade (Widget X sales drop), Costco manual entry quality, attribution data integration (Facebook/Google/e-commerce), SOX-compliant audit trail, data splitting integrity risk, CityU EA diagram walkthrough, Thomson Reuters PDF ingestion
- Dark GitHub-style theme; sticky left-sidebar TOC with active-section highlighting via IntersectionObserver; print-safe styles; responsive collapse on mobile

---

## 2026-04-26

### [feature] `classroom-activities/data-governance/module-03.html` — Module 03 Data Protection
- Source: `Module 3.docx` — HealthSecure Inc. healthcare data breach case study
- 5 parts: Databricks data masking (email + SSN regex), OpenMetadata RBAC + DataSensitivity classification, role access matrix (Admin/Analyst/Contractor), 5 security policies (masking, RBAC, classification, audit logging, HIPAA breach notification), 8-risk register with Likelihood/Impact/Mitigation/Owner
- &ldquo;Why this answer?&rdquo; explanation panels per part; export PDF button; full @media print stylesheet

---

## 2026-04-08

### [feature] `classroom-activities/data-governance/module-01.html` — Module 01 answered case study
- New section `classroom-activities/` with subsection `data-governance/`
- `module-01.html`: full answer key for "RetailCorp: The Data Chaos Challenge"
- Covers all 6 tasks: governance org chart, business glossary (4 terms), metadata catalog (Customers + Orders with PII tags), domain classification (3 domains + cross-domain joins), 3 governance policies, Databricks notebook walkthrough
- Embeds dataset preview from `Customers.xlsx` and `Orders.xlsx`
- Accordion expand/collapse per task; dark GitHub-style theme matching existing activities

---

## 2026-04-07

### [docs] `lessons-learned/bug-fixes.md` — splice indices after earlier HTML edit
- New pattern: stale `index()` anchors when a generator prepends CSS or other content before recomputing slice positions (HOS `generate_hos_02_10.py` handout bug)

### [refactor] `hos/full-stack-dev/` — CS628 track (Module 10 nested)
- `hos/full-stack-dev/index.html` — mini-hub; Module 10 at `hos/full-stack-dev/module-10/` with `../../shared.css` and `../../index.html` back link
- Dev Foundations HOS remains `hos/dev-foundations-activities-hos/`; main hub `hos/index.html` card points at `full-stack-dev/module-10/module-10-conversation-to-design.html`

### [ux] `hos/full-stack-dev/module-10/module-10-conversation-to-design.html`
- Footer credit: "Developed by Clark Ngo." (`hos-pdf-doc-credit`)

### [ux] HOS10A module page — PDF handout styling
- `hos/full-stack-dev/module-10/module-10-pdf-theme.css` + classes on `module-10-conversation-to-design.html`: solid navy course banner, centered hero block with blue rule, green **Tools Required** and blue **Deliverables** callouts, Slack thread (`#product-dev-chat` bar + Maria/Alex/Sam bubble tints), STC footer; `body.hos-pdf10-page` + paper column on gray backdrop
- **Section 4 Architecture Overview:** ASCII diagram moved from one `<p>` per line (broken layout) to `<pre class="hos-arch-diagram">` inside `table.hos-arch-diagram-table`; component table uses `<thead>`/`<th>`; generic PDF table CSS excludes `hos-arch-diagram-table`
- **Section 2 Requirements Gathering:** wrapped in `<section class="hos-req-gathering">`, task tables `hos-req-task`; colors aligned to handout — section title `#1f3864`, task header bar `#c55a11` / white text, body `#fde9d9` / `#111` text
- **5.6 App.js / React Router:** sample code moved from one `<p>` per line to `<pre class="hos-code-snippet">` with proper JSX indentation; `table.hos-code-block-table` + CSS exclusion from generic table striping

### [ux] `hos/shared.css` + `hos/index.html`
- Hub: `.hos-hub-cross` callout for CS445 Dev Foundations; hero covers CS628 + CS445
- Styles aligned to embedded Word **Office** theme from `HOS10A_AIFirst_ConversationToDesignDoc.docx`: accent1 `#156082`, dk2 `#0E2841`, accent2 `#E97132`, accent4 `#0F9ED5`, lt2 `#E8E8E8`; Segoe UI / Inter stack; light page background; first table as gradient title banner; `p.heading` with orange left rail; callout tables with alternating tint; hub hero card with orange accent edge

## 2026-03-27

### [feature] lessons-learned/prompting.md — git / multi-workstream prompting (stash vs PR order, primer vs Wireshark mix-up)
- New section: name paths for stash vs ship, explicit numbered steps, stash push vs pop, confirm `git stash list`

### [refactor] `.gitignore` — ignore `.DS_Store`; `git rm --cached` for four tracked `.DS_Store` files so they stay local only

### [bug] lessons-learned/bug-fixes.md — document `</script>` inside inline HTML scripts
- New section: HTML parser terminates `<script>` at first `</script>` even inside JS strings; use `<\/script>` in source

## 2026-03-25

### [feature] lessons-learned — 10 new entries from history review
- **bug-fixes.md**: hardcoded count string, script-before-DOM, canvas z-index overlap, threshold/label mismatch
- **feature-dev.md**: canonical template pattern for series (build one right, then copy)
- **refactor.md**: consolidate standalone files into folder, kebab-case naming convention
- **workflow.md**: `file://` vs HTTP server, archive before replacing, commit message discipline from day one

### [feature] `index.html` — Lessons Learned section added
- New sidebar nav entry "🧠 Lessons Learned" under Meta group; collection card + 5 direct file-card shortcuts
- Links to viewer, prompting, bug-fixes, feature-dev, ux, and workflow topics

### [feature] `lessons-learned/workflow.md` — new topic: Claude Code Workflow
- Covers: branch/PR/merge cadence, plan mode, verify-one-then-batch, context window management, parallel vs sequential tool calls, git stash mid-session, CLAUDE.md purpose, commit message quality

### [feature] CLAUDE.md — workflow.md added to lessons-learned post-write checklist

### [feature] CLAUDE.md — post-write checklist now includes lessons-learned update step
- Added 5-line checklist item: after any change, check if it warrants updating `bug-fixes.md`, `feature-dev.md`, `ux.md`, `refactor.md`, or `prompting.md`

### [feature] lessons-learned/prompting.md — new entry: Ask Claude to maintain living documentation
- Documents the "should Claude do X the same way it does Y" prompting pattern
- Explains why analogy-based framing is more effective than issuing a direct rule

---

### [bug] `fetch()` failed for .md files on GitHub Pages
- **Symptom:** `Could not load root-playground.md: Failed to fetch` on GitHub Pages
- **Root cause:** GitHub Pages runs Jekyll by default; Jekyll intercepts `.md` files, transforming or blocking them so `fetch()` receives HTML or a 404 instead of raw markdown
- **Fix:** Added `.nojekyll` at repo root — disables Jekyll entirely, all files served as static assets

### [feature] Created `changelog/index.html` — visual changelog viewer
- Single-page markdown viewer (marked.js CDN) matching lessons-learned viewer style
- Sidebar grouped by category (Security, System Design, Content, Tools & Misc); home card grid with all 21 sections
- Tag badges `[feature]` `[bug]` `[ux]` `[refactor]` rendered as colored inline pills (green/red/blue/purple)
- URL param `?f=filename.md` for deep links; browser back/forward navigation supported

### [feature] Created `lessons-learned/` section — knowledge base for patterns and insights
- `lessons-learned/index.html` — single-page markdown viewer using marked.js (CDN); sidebar nav + home card grid; supports URL param `?f=filename.md` for deep links; works with `python3 -m http.server`
- `lessons-learned/feature-dev.md` — Set-based tracking, default-active seeding, 2×2 combo grid, localStorage versioning, badge count sync
- `lessons-learned/bug-fixes.md` — init order (saveState before loadState), missing re-render after loadState, default tab seeding, first-click objective completion, JS syntax errors causing blank pages
- `lessons-learned/ux.md` — overlay placement (bottom-right DOM order), objectives ordered to match page flow, choice vs auto-execute, demo null start state, export success feedback
- `lessons-learned/refactor.md` — global sed replace across N files, boolean→Set refactor, centralizing objective evaluation, removing hardcoded defaults
- `lessons-learned/prompting.md` — reference file beats description, symptom-first, batch after verify, "no + reference" redirect, compound requests as lists, planning mode

### [feature] CLAUDE.md — added Prompting Guidance section
- Claude now auto-suggests clearer prompt phrasing when it detects ambiguity (vague layout references, missing reference files, bundled tasks, presumed-fix mismatch)
- Inline suggestion format defined; only triggers when rewrite would have meaningfully changed interpretation

### [feature] CLAUDE.md — added JS State Pattern Checklist
- New section after Post-Write Checklist covering 6 state-pattern checks: saveState includes new var, loadState restores it, re-render called after load, init order guard, default-active seeding, badge count matches checks.length
- Added `lessons-learned/` → `changelog/root-playground.md` to the changelog routing table

---

## 2026-03-24

### [feature] Global attribution — metadata + copyright footer on all 353 HTML files
- **Metadata tags** (`author`, `copyright`) added to all 353 files for document attribution
- **Minimal footer** (© YYYY Clark Ngo, auto-updating) added to all 328 content files (non-index.html)
- **Lab homepages** (15 index.html files) retain full footer with LinkedIn link
- **Rationale:** Individual files may be deployed/shared on different platforms; metadata + minimal footer ensures proper attribution

### [feature] Copyright footer added to all lab homepages (10 subfolders)
- Auto-updating year via `new Date().getFullYear()` — no manual maintenance needed
- LinkedIn link (`linkedin.com/in/clarkngo`) with hover state
- Applied to: `coding-agents/`, `crypto-vuln-labs/`, `cryptography-labs/`, `encryption-labs/`, `prototypes/security/cy615/`, `security/`, `system-design-labs/`, `system-design-learn/`, `trainer-series/`, `case-studies/`
- Styling adapts: dark GitHub theme for dark-background labs; Tailwind colors for `system-design-learn` (light theme)

### [bug] Copyright year script executing before DOM element existed
- **Symptom:** Year span displayed empty (no year shown)
- **Root cause:** `document.getElementById('copyright-year')` was called inside the main `<script>` block, before the `<footer>` HTML was rendered
- **Fix:** Moved the copyright year script to a separate `<script>` tag placed **after** the footer HTML, ensuring the element is in DOM before the script runs
- **Files:** `crypto-vuln-labs/`, `cryptography-labs/`, `system-design-labs/`, week1-lab, week2-lab (all had script in wrong position)

---

## 2026-03-23

### [feature] CLAUDE.md created — agent diagnostic instructions
- **Why:** Lab 09 canvas was blank due to a JS syntax error (apostrophes in single-quoted strings). It took too long to diagnose because behavioral debugging was tried before syntax checking.
- **Contents:**
  - JS syntax check command: `sed -n '/<script>/,/<\/script>/p' <file> | grep -v '<.script' | node --check /dev/stdin`
  - Debugging order: (1) syntax check → (2) check globals exist → (3) console logs → (4) manual draw test → (5) runtime/timing issues
  - Post-write checklist: syntax check passes, no console errors, key elements visible
- **Common pitfall documented:** Single-quoted strings with apostrophes (`it's`, `don't`, `can't`) — use backtick template literals instead

### [feature] Case Studies & Trainer Series added to main index.html
- New sidebar nav section "Case Studies & Training" with two links and badge counts (10 each)
- Full content sections added: `data-section="case-studies"` and `data-section="trainer-series"`
- 11 cards each (hub card + 10 content cards) with section groups, thumbnails, and tags
- Inserted before the Simulators section in the content layout

### [feature] Coding Agents section updated
- Badge count updated to 9
- Lab 09 card added to main index.html coding-agents content section
