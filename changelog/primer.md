# Primer Changelog

## 2026-04-03

### [feature] Primer directory reorganization — industry/ subfolder
- Moved all 17 existing industry primers from `primer/<name>/` into `primer/industry/<name>/`
- Updated all moved primers: `href="../shared.css"` → `../../shared.css`, `src="../shared.js"` → `../../shared.js`, breadcrumb `href="../index.html"` → `../../index.html`
- Updated all 17 card hrefs and sidebar nav hrefs in `primer/index.html` to `industry/<name>/index.html`
- Sidebar logo updated: "Industry Primer" → "Primer", subtitle → "Industry & technology foundations"
- Page title updated to "📚 Primer", subtitle broadened to include technology domains
- Search placeholder updated to "Search primers…"
- `updateCount()` scoped to `#industry-grid` so tech cards are not counted in the industry count

### [feature] Technology Primer section — new category
- New `primer/technology/` category directory with `shared.css` stub for future tech-specific styles
- `primer/index.html` gains a "Technologies" sidebar nav group (All Technologies + Real-Time Systems links) and a `#technologies-section` card grid below the industries grid
- `filterCards()` JS extended with `TECH_INDUSTRIES` Set and `all-tech` filter case

### [feature] Real-Time Systems — first Technology Primer (9 tabs)
- New file: `primer/technology/real-time-systems/index.html`
- Loads `../../shared.css` + `../shared.css` (layered CSS pattern for tech category)
- **Tab 1 — Overview**: 6 sub-domain cards (RTOS Kernels, Scheduling Algorithms, Embedded Hardware, Safety Standards, Communication Buses, Development Tools); 5-node processing pipeline value chain (Sensor → ISR → Task Queue → Processing → Actuator); 6 market-context cards (Automotive, Avionics, Medical Devices, Industrial Control, Space & Defense, Telecom/5G RAN)
- **Tab 2 — Key Terminology**: 20 searchable glossary terms covering Determinism, Hard/Soft/Firm RT, RTOS, WCET, Latency, Jitter, Preemption, Context Switch, ISR, Priority Inversion, Mutex/Semaphore, Watchdog Timer, Tick, RMS, EDF, POSIX.1b, Time-Triggered Architecture, Hypervisor/Partitioning
- **Tab 3 — Major Players**: 4 sections — Commercial RTOS (VxWorks, QNX, INTEGRITY, LynxOS), Open-Source (FreeRTOS, Zephyr, PREEMPT_RT, RTEMS), Silicon (ARM Cortex-M/R, TI, NXP, STM32), End-User Domains (Automotive OEMs, Aerospace Primes, Medical Device Manufacturers)
- **Tab 4 — Core Metrics**: 8-row table covering Interrupt Latency, Context Switch Time, WCET, Jitter, CPU Utilization Ceiling, Deadline Miss Rate, Stack HWM, Schedulability with benchmarks
- **Tab 5 — Technology Stack**: 7 layers — MCU/Hardware, RTOS Kernel, BSP & HAL, Middleware & Stacks, Communication Buses, Dev & Debug Tools, Safety Certification Layer
- **Tab 6 — Common Workflows**: 3 workflows — (1) Preemptive Task Scheduling Cycle (5 steps), (2) ISR → Deferred Processing bottom-half pattern (5 steps), (3) Safety-Critical Boot Sequence & Watchdog Validation (5 steps)
- **Tab 7 — Trends & Challenges**: 6 trend cards — RISC-V in RT, Mixed-Criticality Systems, TSN, AI Inference on Edge, Certification Cost, Cloud-Connected RT
- **Tab 8 — Market Dynamics & Monetization**: 5 pain-point cards (Certification Cost, Toolchain Lock-In, Memory Constraints, Priority Inversion Bugs, Legacy Porting); 5-row monetization table (Commercial RTOS License, Safety Cert Package, LTS/Maintenance, Silicon Bundling, Consulting)
- **Tab 9 — Evolution & Foundations**: 8 timeline cards (1961 CTSS → 1973 Liu & Layland → 1988 VxWorks → 1993 POSIX.1b → 1995 QNX Neutrino → 2003 FreeRTOS → 2012 PREEMPT_RT → 2017 Zephyr); 6-row foundational works table (Liu & Layland 1973, Buttazzo textbook, POSIX.1b-1993, IEC 61508, DO-178C, AUTOSAR)

## 2026-03-27

### [feature] primer/insurance — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons (indices 9 and 10); progress bar gains dot-9 and dot-10; initial label updated to "Section 1 of 11"
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Policy Administration, Claims, Underwriting & Rating, Actuarial/Reserving, Telematics/IoT, Reinsurance, Regulatory/Compliance); 9-node end-to-end data flow diagram (Risk Submission → Underwriting Engine → Rating/Pricing → Policy Issuance (PAS) → Premium Collection → Claims FNOL → Claims Adjudication → Payment & Reserving → Reinsurance Recovery); 8-chip Key Protocols row (ACORD XML, ACORD AL3, EDI, ISO rating, NAIC statutory accounting, FHIR, SWIFT, HL7); 4-card Governance grid (State Regulation, NAIC Model Laws, Credit Scoring Restrictions, Catastrophe Model Governance)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering Hurricane Katrina CAT Model Failure (2005, $125B insured losses, levee breach not modeled), Texas Winter Storm Uri Business Interruption Disputes (Feb 2021, utility failure exclusion gaps), Cyber Insurance Mispricing Crisis (2020-2022, correlated loss misunderstood, combined ratios >100%), LMI Mortgage Insurance Scandal Australia (2017-2019, mis-sold to borrowers via Royal Commission), Workers Compensation Fraud Ring Detection Failure (ongoing, $34B+ annual cost, siloed carrier systems), Guidewire/Duck Creek Outages During CAT Events (recurring, 100x FNOL surge not load-tested) — each card includes what happened, what it revealed, and the lesson

### [feature] primer/healthcare — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons (indices 9 and 10); progress bar gains dot-9 and dot-10; initial label updated to "Section 1 of 11"
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Clinical Records/EHR-EMR, Medical Imaging, Lab & Diagnostics, Claims & Billing, Wearables & IoT, Pharmacy, Public Health); healthcare data flow diagram (Patient Encounter → EHR → HL7 FHIR API → HIE → Payer → Analytics → Quality Reporting/CMS); 11-chip Key Protocols row (HL7 v2, HL7 FHIR R4, DICOM, ICD-10-CM/PCS, CPT codes, SNOMED CT, LOINC, EDI 837/835, NCPDP SCRIPT, CCD/CDA, SMART on FHIR); 4-card Governance grid (HIPAA, 21st Century Cures Act, De-identification, AI & HIPAA)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering Change Healthcare Ransomware Attack (Feb 2024, ~100M records, no MFA on Citrix portal), Epic/Cerner Downtime & Diversion Protocols (recurring, medication errors 3-4x during outages), AI Diagnostic Bias — Pulse Oximetry (2020-2022, skin-tone disparity, delayed COVID treatment), Theranos Fraud (2003-2018, falsified lab results, LDT regulatory gaps), Meta Pixel PHI Transmission (2022, hospital websites leaking health data to Meta), FDA Recall of AI Diagnostic Software (ongoing, training vs. deployment distribution gap)

### [feature] primer/logistics — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons (indices 9 and 10); progress bar gains dot-9 and dot-10; initial label updated to "Section 1 of 11"
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Transportation/TMS, Warehousing/WMS, Track & Trace/telematics, International Trade/customs, Last Mile, Demand & Inventory, Carrier & Rate Data); Order-to-Delivery value-chain flow (PO → OMS → WMS → TMS → carrier → tracking → last mile → POD/invoice); EDI/trade and visibility chip rows (204/210/214, EDIFACT, ACE, GS1/RFID, ELD); 4-card governance (FMCSA/ELD, Customs 10+2, Cold Chain FSMA, Carbon/Scope 3)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid (Ever Given Suez 2021, CrowdStrike July 2024 logistics IT outage, plus four additional logistics/supply-chain case studies) with lessons per card

### [feature] primer/manufacturing — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons (indices 9 and 10); progress bar gains dot-9 and dot-10; initial label updated to "Section 1 of 11"
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Production/OT & MES, Quality, Maintenance/CMMS, Supply Chain/ERP, PLM, Energy, Digital Twin); Production Data Flow chain (raw material → ERP → MES → SCADA → historian → quality → WMS → shipping); Key Protocols chips (OPC-UA, MQTT, MTConnect, ISA-95/88, GS1, STEP, EDIFACT); 4-card Governance (ISA/IEC 62443, FDA 21 CFR Part 11, IATF 16949, Environmental/ISO 14001)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid (Norsk Hydro ransomware 2019, Boeing 737 MAX MCAS, Toyota earthquake/JIT cascades, Colonial Pipeline feedstock context, plus additional manufacturing safety/supply cases) with event / revealed / lesson structure

### [feature] primer/ai-infrastructure — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons; progress bar gains dot-9 and dot-10; initial label updated to "Section 1 of 11"
- Updated `shared.js` to dynamically compute "of N" from the number of `.progress-dot` elements, making all primers forward-compatible with variable tab counts
- **Tab 10 — Data Architecture & Flows**: 8-row Data Domains table (Source Documents, Chunked Text, Embeddings, Vector Index, Metadata Store, Conversation/Session State, Model Artifacts, Observability Logs); two-pipeline CSS flow diagram (Ingestion: S3 → Chunker → Embedding Model → Vector DB → Metadata Store; Retrieval/Inference: User Query → Query Embedder → ANN Search → BM25 Hybrid → Reranker → Context Assembly → LLM → Output Validator → Response); 7-row Key Protocols table (OpenAI API Spec, MCP, OpenAPI 3.0, gRPC, JWT, GGUF/GPTQ/AWQ, HuggingFace Model Card); 5-card Data Governance grid (Training Data Provenance, Inference Data Privacy, RAG Access Control, PII in Vector Stores, Eval Data Contamination)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering ChatGPT Chat History Exposure (March 2023, Redis cache collision), Air Canada Chatbot Liability Ruling (Feb 2024, hallucinated fare policy), Prompt Injection via Indirect Content (ongoing RAG threat), Bing Chat/Sydney Jailbreak (Feb 2023, adversarial alignment failure), Vector DB Stale Embeddings (common RAG lifecycle failure), LLM-as-Judge Bias in Evals (position/verbosity/self-enhancement bias) — each card includes incident date, what happened, root cause, and lesson

### [feature] primer/edtech — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons; progress bar gains dot-9 and dot-10; progress label updated to "of 11"
- Inline `showTab` override added after `shared.js` load to display "Section N of 11" correctly
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Student Records/SIS, Learning Activity/xAPI, Assessment, Engagement/Telemetry, Content Metadata, Financial/Enrollment, AI Interaction Logs); two-row CSS data flow diagram (xAPI pipeline: LMS → LRS → Analytics → Early Alert → Advisor Dashboard; SIS pipeline: SIS → Data Warehouse → BI → Academic Leadership); 6-card Key Protocols section (xAPI/Tin Can, SCORM 1.2/2004, cmi5, LTI 1.3+Advantage, SAML 2.0/SSO, Caliper/Ed-Fi); 5-card Data Governance section (FERPA, COPPA, Data Residency, AI and FERPA, Retention Policies)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering COVID-19 LMS Collapse (2020), Chegg Data Breach (2018), ProctorU Breach (2020), AI Cheating Detection False Positives (2022-2023), Pearson Data Breach (2018/2019), Online Proctoring Bias & Skin Tone Failures (2020-2021) — each with what happened, what it revealed, and a lesson

### [feature] primer/ecommerce — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons; progress bar gains dot-9 and dot-10; progress label updated to "of 11"
- Inline `showTab` override added after `shared.js` load to display "Section N of 11" correctly
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Product Catalog, User Behavior, Transaction, Inventory/Supply Chain, Seller/Merchant, Search/Discovery, Fraud Signals); CSS data flow diagram (clickstream pipeline via Kafka/Flink/Feature Store/ML/Redis and OMS pipeline to Snowflake/BI); 4-card Key Protocols section (HTTP/REST, GraphQL, Webhooks/SFTP, EDI, ISO 8583, PCI-DSS); 4-row Data Governance table (first-party data/cookie deprecation, CCPA/GDPR, seller data portability, PCI-DSS tokenization)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering Amazon S3 outage (2017), eBay data breach (2014), Target POS malware (2013), Shopify insider threat (2020), fake review epidemic (ongoing), recommendation amplification bias (ongoing) — each with what happened, what it revealed, and a lesson

### [feature] primer/fintech — added Tab 10 (Data Architecture & Flows) and Tab 11 (Failure Modes & Incidents)
- Tab nav expanded from 9 to 11 buttons; progress bar gains dot-9 and dot-10; progress label updated to "of 11"
- Inline `showTab` override added after `shared.js` load to display "Section N of 11" correctly
- **Tab 10 — Data Architecture & Flows**: 7-row Data Domains table (Market, Reference, Fundamental, Transaction, Alternative, Risk, Regulatory); CSS data flow diagram (exchange feed pipeline + EDGAR/XBRL pipeline); Key Protocols chip row (FIX, SWIFT, ISO 20022, XBRL, FpML, SFTP/MFT); 4-card Data Governance section (licensing costs, MNPI walls, GDPR/CCPA, SOX data lineage)
- **Tab 11 — Failure Modes & Incidents**: 6-card incident grid covering Knight Capital (2012), Flash Crash (2010), Robinhood halt (2020), SVB run (2023), LIBOR manipulation (2012), Mt. Gox collapse (2014) — each with what happened, what it revealed, and a lesson

## 2026-03-26

### [ux] primer/video-platform, ecommerce, edtech, ai-infrastructure, fintech — rewrote tab-evolution section layout
- Moved Foundational Works table to the TOP of each evolution section (before timeline)
- Replaced existing Foundational Works headings with `<div class="section-title">Foundational Works</div>`
- Replaced all `card-grid` / `card` / `card-icon` timeline blocks with new `<div class="timeline">` structure using alternating `tl-left` / `tl-right` `tl-item` rows (8 items each, odd on left, even on right)
- Added `<div class="section-title" style="margin-top:28px">Historical Timeline</div>` label before timeline div
- All content (years, titles, descriptions) preserved exactly; only markup structure and order changed

### [ux] primer/sports, restaurant, fishing, telecom — rewrote tab-evolution section layout
- Moved Foundational Works table to the TOP of each evolution section (before timeline)
- Replaced `<h3>Foundational Works</h3>` with `<div class="section-title">Foundational Works</div>`
- Replaced all `card-grid` / `card` / `card-icon` timeline blocks with new `<div class="timeline">` structure using alternating `tl-left` / `tl-right` `tl-item` rows (8 items each, odd on left, even on right)
- Added `<div class="section-title" style="margin-top:28px">Historical Timeline</div>` label before timeline div
- All content (years, titles, descriptions) preserved exactly; only markup structure changed

### [ux] primer/oil, healthcare, esports, video-game-retail — rewrote tab-evolution section layout
- Moved Foundational Works table to the TOP of each evolution section (before timeline)
- Replaced `<h3>Foundational Works</h3>` with `<div class="section-title">Foundational Works</div>`
- Replaced all `card-grid` / `card` / `card-icon` timeline blocks with new `<div class="timeline">` structure using alternating `tl-left` / `tl-right` `tl-item` rows (8 items each, odd on left, even on right)
- Added `<div class="section-title" style="margin-top:28px">Historical Timeline</div>` label before timeline div
- All content (years, titles, descriptions) preserved exactly; only markup structure changed

### [ux] primer/insurance, manufacturing, maritime, logistics — rewrote tab-evolution section layout
- Moved Foundational Works table to the TOP of each evolution section (before timeline)
- Replaced `<h3>` / inline-styled headings with `<div class="section-title">Foundational Works</div>`
- Replaced all `card-grid` / `card` / `card-icon` timeline blocks with new `<div class="timeline">` structure using alternating `tl-left` / `tl-right` `tl-item` rows (odd on left, even on right)
- Added `<div class="section-title" style="margin-top:28px">Historical Timeline</div>` label before timeline div
- manufacturing: converted second `card-grid` ("Foundational Standards &amp; Research") into a `metrics-table` with Work / Author/Year / Why It Matters columns
- All content (years, titles, descriptions, table rows) preserved exactly; only markup structure changed

## 2026-03-26 (ux — remove Live/New badges from hub)

### [ux] primer/index.html — removed all status and nav badges
- Removed all `<span class="status-badge live">Live</span>` from 17 industry cards
- Removed all `<span class="nav-badge">New</span>` from sidebar nav links
- Removed `new-badge` CSS class from all nav link elements
- Cleaned up dead CSS rules: `.nav-badge` and `.nav-link.new-badge .nav-badge`

## 2026-03-26 (refactor — fintech migration to showTab system)

### [refactor] primer/fintech — migrated from data-tab + activateTab system to canonical showTab system
- Replaced entire inline `<style>` block (lines 7–456, ~450 lines) with `<link rel="stylesheet" href="/primer/shared.css" />`
- Replaced inline `<script>` block (activateTab, dot click events, glossary addEventListener, filterGlossary, keyboard shortcut) with `<script src="/primer/shared.js"></script>`
- Simplified breadcrumb from 3-level (Playground / Industry Primer / FinTech) to canonical 2-level (Industry Primer / FinTech)
- Converted 9 tab buttons from `data-tab="..."` event-listener system to `onclick="showTab('name',idx)"` format with clean labels (removed "1.", "2." numbering prefixes)
- Replaced old progress bar (`id="progressBar"`, `id="progressLabel"`, `data-idx` dots) with canonical 9-dot bar (`id="dot-0"` through `id="dot-8"` + `id="progress-label"`)
- Converted all section elements from `<section class="tab-section" id="sec-X">` to `<div class="tab-section" id="tab-X">`: sec-overview→tab-overview, sec-terminology→tab-terminology, sec-players→tab-players, sec-metrics→tab-metrics, sec-techstack→tab-stack, sec-workflows→tab-workflows, sec-trends→tab-trends, dynamics→tab-dynamics, evolution→tab-evolution
- Glossary search input ID changed from `id="glossarySearch"` to `id="gloss-search"` for shared.js compatibility
- All glossary items converted to shared.js pattern: `onclick="toggleGloss(this)"` on `.glossary-header`; `data-term` + `data-cat` attributes replaced with `data-terms` space-separated string for shared.js filter; `.glossary-short` span removed (content merged into `.glossary-body`); `.glossary-cat` span moved inside header alongside `.glossary-term`
- Player cards migrated from old `.p-emoji`/`.p-name`/`.p-desc`/`.p-tag` classes to canonical `.player-name`/`.player-role`/`.player-tag` classes
- Metrics table removed old `.metrics-wrap` wrapper + `.metrics-category-header` row pattern; replaced with canonical `<span class="metrics-cat">` inside a colspan=4 `<td>`
- Tech stack layers migrated from `.stack-layer-content` + `.stack-chips` to canonical `.chip-row` directly inside `.stack-layer`
- Workflow steps migrated from old horizontal `.workflow-step` (`.step-num` span + `.step-name` span + `.step-desc` span + `.workflow-arrow` dividers) to canonical vertical layout (`.step-num` div + `.step-content` > `.step-title` + `.step-detail`)
- Trends section: `.trends-grid` → `.trend-grid`; `.t-icon` → `.trend-icon`; `<h3>` for title → `.trend-title` div; `<p>` → `.trend-desc` div; `.t-tag` spans removed
- All existing content (27 glossary terms, 6 player sections, metrics rows, 7 stack layers, 3 workflows, 6 trends, 5 pain point cards, 6 monetization rows, 8 timeline cards, 6 foundational works rows) preserved exactly

## 2026-03-26 (refactor — ai-infrastructure migration to showTab system)

### [refactor] primer/ai-infrastructure — migrated from data-tab system to canonical showTab system
- Replaced entire inline `<style>` block with `<link rel="stylesheet" href="/primer/shared.css" />` plus a local `<style>` block for components not covered by shared.css (term-card glossary, player-chip, metrics-category, stack-layer with layer-* colors, workflow-steps, trend-card, vc-node, grid-2/3/4)
- Removed `<header class="page-header">` wrapper; replaced with flat `<div class="breadcrumb">` + `<div class="page-header">` inside `<div class="page-wrap">`; breadcrumb simplified to 2-level (Industry Primer / AI Infrastructure); `<div class="page-title">` → `<h1>`; `<div class="page-subtitle">` → `<div class="subtitle">`
- Removed `<main class="content">` wrapper; content lives directly inside `.page-wrap`
- Converted 9 tab buttons from `data-tab="..."` event-listener system to `onclick="showTab('name',idx)"` format; nav element changed from `class="tabs"` to `class="tab-nav"`
- Added 9-dot progress bar (`#dot-0` through `#dot-8`) + `#progress-label "Section 1 of 9"`
- All 9 section elements converted: `<section class="section" id="X">` → `<div class="tab-section" id="tab-X">`, closing `</section>` → `</div>`; ID mapping: overview→tab-overview, terminology→tab-terminology, players→tab-players, metrics→tab-metrics, stack→tab-stack, workflows→tab-workflows, trends→tab-trends, dynamics→tab-dynamics, evolution→tab-evolution
- Replaced old inline `<script>` (switchTab + data-tab event listeners) with `<script src="/primer/shared.js"></script>`; retained a small local script for the ai-infrastructure-specific `.term-card` expand/collapse and `#termSearch` filter (not in shared.js which targets `.glossary-item`); updated keydown handler to call `showTab('terminology', 1)` instead of old `switchTab('terminology')`
- All existing content (35 terms, player chips, metrics rows, stack layers, workflows, trends, dynamics, evolution timeline, foundational works table) preserved exactly

## 2026-03-26 (refactor — edtech migration to showTab system)

### [refactor] primer/edtech — migrated from data-tab system to canonical showTab system
- Replaced entire inline `<style>` block with `<link rel="stylesheet" href="/primer/shared.css" />`
- Replaced inline `<script>` block with `<script src="/primer/shared.js"></script>`
- Replaced `<div class="page">` + `<nav class="breadcrumb">` + `<header class="page-header">` with canonical `<div class="page-wrap">` + `<div class="breadcrumb">` + `<div class="page-header">` structure; breadcrumb simplified to 2-level (Industry Primer / Higher Education & EdTech)
- Converted 9 tab buttons from `data-tab="..."` to `onclick="showTab('name',idx)"` format
- Added 9-dot progress bar (`#dot-0` through `#dot-8`) + `#progress-label`
- All 9 `<section class="tab-section" id="tab-...">` elements converted to `<div class="tab-section" id="tab-...">` (already had correct IDs; changed closing `</section>` to `</div>`)
- Converted `<h2 class="section-title">` / `<p class="section-desc">` to `<div class="section-title">` / `<div class="section-desc">` throughout
- Converted glossary from `.gloss-item`/`.gloss-trigger`/`.gloss-body` + JS event listeners to canonical `.glossary-item`/`.glossary-header[onclick="toggleGloss(this)"]`/`.glossary-body`; `id="glossSearch"` → `id="gloss-search"`; `data-term` → `data-terms` with full keyword strings on all 30 terms
- Converted player sections from `.players-section`/`.players-grid`/`.player-chip` to canonical `.player-section`/`.player-section-title`/`.player-grid`/`.player-card` with `.player-name` + `.player-role`
- Converted metrics from custom `.metrics-section`/`.metrics-grid`/`.metric-card` layout to canonical `.metrics-table` with `.metrics-cat` group rows covering all 6 original metric categories (enrollment, success, engagement, outcomes, platform, financial)
- Converted tech stack from `.stack-layer`/`.stack-items`/`.stack-item` + `.stack-note` to canonical `.stack-layer`/`.stack-layer-label`/`.chip-row`/`.chip` (blue/green/purple/muted variants)
- Converted workflows from `.workflow`/`.workflow-title`/`.workflow-steps`/`.wf-step`/`.wf-arrow` to canonical `.workflow`/`h3`/`.workflow-desc`/`.workflow-steps`/`.workflow-step`/`.step-num`/`.step-content`/`.step-title`/`.step-detail` (5 steps per workflow)
- Trend section already had `.trend-card` class structure; converted to canonical `.trend-grid`/`.trend-card`/`.trend-icon`/`.trend-title`/`.trend-desc`
- Market Dynamics: pain points converted from `.trends-grid` to `.card-grid`/`.card`; monetization models converted from `.metrics-grid` to `.metrics-table` with Margin Profile column; 7 monetization model rows
- Evolution: historical timeline card-grid retained (8 era cards); foundational works `.metrics-table` retained (6 rows)
- Verification: shared_css=1, shared_js=1, inline_script=0; all 9 section IDs present; 9 showTab buttons; 0 data-tab attributes

## 2026-03-26 (refactor — ecommerce migration to showTab system)

### [refactor] primer/ecommerce — migrated from data-tab system to canonical showTab system
- Replaced entire inline `<style>` block with `<link rel="stylesheet" href="/primer/shared.css" />`
- Replaced inline `<script>` block with `<script src="/primer/shared.js"></script>`
- Replaced `<header class="page-header">` + `<main class="main">` with canonical `<div class="page-wrap">` + `<div class="page-header">` structure
- Converted 9 tab buttons from `data-tab="..."` to `onclick="showTab('name',idx)"` format
- Added 9-dot progress bar (`#dot-0` through `#dot-8`) + `#progress-label`
- Converted all `<section class="section" id="...">` to `<div class="tab-section" id="tab-...">` with renamed IDs (`techstack` → `stack`)
- Converted `<h2 class="section-heading">` to `<div class="section-title">` throughout
- Converted glossary search from `id="glossarySearch"` to `id="gloss-search"`; `data-term` → `data-terms`; added `onclick="toggleGloss(this)"` to each glossary header
- Converted player cards to canonical `.player-section` / `.player-section-title` / `.player-grid` / `.player-name` / `.player-role` structure
- Converted metrics from card-grid layout to canonical `.metrics-table` with `.metrics-cat` group rows
- Converted tech stack from `.stack-section` / `.stack-chips` to canonical `.stack-layer` / `.stack-layer-label` / `.chip-row`
- Converted workflow steps to canonical `.workflow` / `.workflow-desc` / `.workflow-steps` / `.workflow-step` / `.step-num` / `.step-content` structure
- Converted trend cards to canonical `.trend-grid` / `.trend-card` / `.trend-title` / `.trend-desc`
- Verification: css_link=1, js_src=1, inline_script=0; all 9 section IDs present; 9 showTab buttons; 0 data-tab attributes

## 2026-03-26 (refactor — shared CSS/JS extraction)

### [refactor] primer/shared.css + primer/shared.js — created shared asset files
- Created `primer/shared.css` (96 lines): canonical design tokens, layout, tab system, all component classes (glossary, player, metrics-table, stack-layer, chip, workflow, trend-grid, market-note, mono-table)
- Created `primer/shared.js` (25 lines): `showTab`, `toggleGloss`, glossary search, `/` keyboard shortcut
- Both files serve all 13 showTab-system primers; data-tab primers (fintech, ecommerce, edtech, ai-infrastructure) retain inline styles (different system)

### [refactor] All 13 showTab primers — replaced inline style/script with shared file references
- **5 identical-CSS** (insurance, manufacturing, maritime, logistics, oil): removed 88-line `<style>` block + 23-line `<script>` → `<link>` + `<script src>`
- **3 multiline-CSS** (healthcare, esports, video-game-retail): removed ~100–200 line bloated `<style>` block (same rules, expanded whitespace) → shared link
- **3 duplication-bug** (sports, restaurant, video-platform): stripped `<style>` blocks that duplicated rules already in canonical
- **2 with genuine extras** (telecom, fishing): replaced `<style>` with `<link>` + small inline `<style>` for primer-specific rules only (3 rules for telecom, 4 for fishing)
- Verification: `shared.js` node --check PASS; all 13 primers: css_link=1, js_src=1, inline_script=0
- **Lines eliminated**: ~1,144 CSS + ~299 JS = ~1,443 total lines removed from primer files

## 2026-03-26 (bugfix — fintech tab system)

### [bug] primer/fintech — Market Dynamics and Evolution tabs non-functional
- **Symptom:** Clicking "Market Dynamics & Monetization" showed nothing; Evolution tab entirely dead; dots 7–8 click unresponsive
- **Root cause 1:** `sections["dynamics"]` looked up `id="sec-dynamics"` but the section has `id="dynamics"` — `getElementById` returned `null`
- **Root cause 2:** `sections` map and `tabOrder` array both omitted `"evolution"` entirely — tab button had no wired section
- **Root cause 3:** Dots 7 and 8 used `id="dot-7/8"` with no `data-idx` attribute; JS dot-click handler reads `dot.dataset.idx` (undefined), so clicking those dots did nothing
- **Fix:** Updated `sections["dynamics"]` to reference correct ID; added `sections["evolution"]` entry; added `"evolution"` to `tabOrder`; changed dot 7/8 from `id=` to `data-idx=`; added "9." prefix to Evolution tab button label
- JS syntax check: PASS

## 2026-03-26 (batch 8 — telecom Evolution & Foundations + hub updates)

### [feature] primer/telecom — Tab 9: Evolution & Foundations
- Added `<section class="tab-section" id="tab-evolution">` to `primer/telecom/index.html`
- 8 timeline cards: Bell & Monopoly Seed (1876–1906) → Bell System Era → AT&T Breakup (1984) → 1G–3G Wireless (1983–2000) → Telecom Act & Data Era (1996–2007) → 4G LTE & Un-carrier (2009–2013) → 5G & Sprint Merger (2018–2020) → Network Maturity & AI (2021–Present)
- 6 foundational works: Shannon 1948, MFJ/AT&T Divestiture, Telecom Act 1996, 3GPP Releases 8/15/16, GSMA Mobile Economy Report, Innovator's Dilemma
- JS syntax check: PASS

### [feature] primer/index.html — manufacturing card + nav link + section count update
- Added `manufacturing` nav link (📦 Manufacturing (Packaging), New badge) to sidebar
- Added `manufacturing` industry card with full search keywords, description, and tags
- Updated all 16 existing primer cards from `8 / 8 sections` / `· 8 sections` → `9 / 9 sections` / `· 9 sections`
- Manufacturing card shows `9 / 9 sections` from initial creation

### [feature] CLAUDE.md — updated primer-building instructions to 9 tabs
- Changed "8 tabs" → "9 tabs"; updated tab table to include Tab 9 (Evolution & Foundations, `tab-evolution`)
- Updated progress label spec: `"Section N of 9"` with 9 dots (dot-0 through dot-8)
- Renamed Tab 8 to "Market Dynamics & Monetization" in table
- Added Tab 9 content spec: 8 timeline milestone cards + foundational works metrics-table

## 2026-03-26 (batch 6 — manufacturing / corrugated packaging)

### [feature] Manufacturing — Corrugated Packaging industry primer
- Created `primer/manufacturing/index.html` — comprehensive single-page primer with 9-tab navigation
- Title: "Manufacturing — Corrugated Packaging"; features IP, Smurfit WestRock, PCA
- Header tags: [corrugated packaging] [containerboard] [converting] [e-commerce]
- Tab 1 Overview: 6 sub-sector cards + value chain (Timber/OCC through Recycling) + 6 market context cards
- Tab 2 Terminology: 20 searchable accordion terms covering materials, structure, testing, equipment, printing, and industry bodies
- Tab 3 Major Players: 4 categories — Integrated Producers, Independent Converters, Specialty/Protective, Equipment/Technology
- Tab 4 Core Metrics: 4 metric categories — Mill Production, Converting Efficiency, Financial, Quality & Customer (25 metrics total)
- Tab 5 Technology Stack: 7 layers from CAD/prepress to sustainability analytics
- Tab 6 Workflows: 3 workflows — Custom Box Quote-to-Ship, Corrugator Trim Optimization, E-Commerce Packaging Qualification
- Tab 7 Trends: 6 trend cards — E-Commerce Surge, Price Cycles, Sustainability, Digital Printing, Automation, Consolidation
- Tab 8 Market Dynamics: 5 pain point cards + 6-model monetization table
- Tab 9 Evolution: 9 timeline milestone cards (1817–2020s) + 8 foundational standards cards (TAPPI, ASTM, ISTA-6, ISO 2233, McKee formula)

## 2026-03-26 (batch 7 — Evolution & Foundations tab)

### [feature] primer/logistics, video-platform, oil, fishing — Tab 9: Evolution & Foundations
- Added `<section id="tab-evolution" class="tab-section">` to all four primers, immediately before the closing page-wrap `</div>`
- Each section: 8 timeline cards (`.card-grid` + `.card` with `.card-icon` for era label) + `.metrics-table` (Work | Author/Year | Why It Matters)
- logistics: Railroad 1800s → COVID Resilience/Nearshoring 2020+; 6 foundational works (The Goal, Taylor, Machine That Changed the World, SCOR Model, The Box, Amazon Leadership Principles)
- video-platform: Motion Picture/Broadcast 1888–1950s → Monetization Maturity 2022+; 6 foundational works (McLuhan, Betamax Case, DMCA §512, YouTube Partner Program, Kahneman, Nielsen)
- oil: Drake Well 1859 → Energy Transition Tension 2021+; 6 foundational works (The Prize, Hubbert Peak, Tragedy of Commons, Texas RRC, MacKay, IPCC Reports)
- fishing: Artisanal/Sail-era → Digital Integration/Climate Stress 2020+; 6 foundational works (Tragedy of Commons, Magnuson-Stevens Act, End of the Line, FAO Code of Conduct, Four Fish, MSC Standard)
- All four JS syntax checks pass (`node --check`)

## 2026-03-26 (batch 5 — Evolution & Foundations tab)

### [feature] primer/healthcare, esports, video-game-retail, insurance — Tab 9: Evolution & Foundations
- Added `<section id="tab-evolution" class="tab-section">` to all four primers, immediately before the closing page-wrap `</div>`
- Each section: 8 timeline cards (`.card-grid` + `.card` with `.card-icon` for era label) + `.metrics-table` (Work | Author/Year | Why It Matters)
- Healthcare: X-Ray 1895 → AI/Value-Based Care 2021+; 6 foundational works (FDA Device Amendments, ISO 13485, ISO 14971, Charnley hip paper, HIPAA, Crossing the Quality Chasm)
- Esports: 1972 Spacewar tournament → 2022 org restructuring; 5 foundational works (T.L. Taylor, Homo Ludens, Twitch DMCA framework, KeSPA, Riot LCS ruleset)
- Video Game Retail: Arcade origins 1972 → collectibles/retro 2021+; 5 foundational works (NES Seal of Quality, McLuhan Understanding Media, Steam model, Kerr 2006, ESRB)
- Insurance: Lloyd's 1688 → AI underwriting/climate risk 2017+; 6 foundational works (McCarran-Ferguson, ISO CGL, Against the Gods, NAIC Model Laws, CAT Modeling text, ASOPs)
- All four JS syntax checks pass (`node --check`)

### [feature] primer/fintech, ecommerce, edtech, ai-infrastructure — Tab 9: Evolution & Foundations
- Added `<section id="evolution">` (fintech, ecommerce, ai-infrastructure) and `<section id="tab-evolution">` (edtech) to all four primers
- Each section contains: 8-card historical timeline (decade-by-decade milestones) + `.metrics-table` of foundational papers, books, and standards
- Section classes match each file's existing pattern: `tab-section` (fintech, edtech), `section` (ecommerce, ai-infrastructure)
- All four JS syntax checks pass (`node --check`)

### [feature] primer/restaurant, sports, maritime — Tab 9: Evolution & Foundations
- Added `id="tab-evolution"` `class="tab-section"` section to restaurant, sports, and maritime primers
- restaurant: 8 timeline cards (Ancient–Medieval → 2020-Present) + 6 foundational works (Escoffier, HACCP, Flandrin/Montanari, ServSafe, FSMA, Menu Engineering Matrix)
- sports: 8 timeline cards (1891 Naismith invention → 2020-Present Bubble/Betting era) + 6 foundational works (Holzman philosophy, CBA, Moneyball, Basketball on Paper, Second Spectrum, PASPA repeal)
- maritime: 8 timeline cards (3000 BC ancient routes → 2023-Present Red Sea crisis) + 6 foundational works (The Box, SOLAS, MARPOL, Incoterms, UNCLOS, ISM Code)
- All three JS syntax checks pass (`node --check`)

## 2026-03-26 (batch 4 — new industries + Market Dynamics)

### [feature] primer/index.html — 6 new industry cards + nav links
- Added maritime, telecom, logistics, video-platform, oil, fishing cards to the industry grid with `data-search` attributes
- Added 6 new nav links to sidebar (with "New" badges)
- Updated all existing and new cards to show "8 / 8 sections" (Market Dynamics tab added to all primers)

### [feature] Telecommunications industry primer
- Created `primer/telecom/index.html` — comprehensive single-page primer with 8-tab navigation
- Featured carrier: T-Mobile (and AT&T, Verizon, Dish/EchoStar)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges, Market Dynamics
- Header tags: [wireless] [5G] [network infra] [T-Mobile]
- Overview: 6 sub-sector cards (Wireless/Mobile, Broadband/Fixed Line, Enterprise B2B, Tower Infrastructure, Satellite, MVNOs/Prepaid) + value chain + 6 market context cards
- Terminology: 20 terms — ARPU, Churn Rate, Postpaid/Prepaid, 5G NR, Spectrum, MVNO, EBITDA, Capex Intensity, EIP, Core Network, RAN, Network Slicing, eSIM, FWA, IMS, Roaming, NPS, SD-WAN, UCaaS, MNO
- Major Players: 4 categories — US National Carriers, Infrastructure & Tower, Equipment & Vendors, MVNOs & Disruptors
- Core Metrics: Subscriber Health, Financial, Network Quality, Customer Experience
- Technology Stack: 7 layers — RAN, Core Network, Transport/Backhaul, OSS/BSS, Customer/Digital, Enterprise/IoT, Data/Analytics
- Workflows: Subscriber Onboarding (5-step), 5G Site Build & Activation (5-step), Enterprise Private 5G Sale Cycle (5-step)
- Trends: 5G Monetization Lag, FWA Disruption, Network Commoditization, Open RAN, Spectrum Scarcity, Satellite/Direct-to-Device
- Market Dynamics: 5 pain-point cards (CAC, churn/switching, capex treadmill, regulatory/spectrum, ARPU pressure) + monetization table (service revenue, equipment, FWA, enterprise, wholesale, advertising, roaming)

### [feature] Logistics & Supply Chain industry primer
- Created `primer/logistics/index.html` — comprehensive single-page primer with 8-tab navigation
- Featured company: Maersk (integrated logistics transformation from ocean carrier)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges, Market Dynamics
- Header tags: [3PL] [last-mile] [supply chain] [Maersk]
- Overview: 6 sub-sector cards (3PL, Freight Brokerage, Integrated Express, Last-Mile, Warehousing/Fulfillment, Integrated Logistics) + full value chain + 6 market context cards
- Terminology: 20 terms — 3PL, Freight Forwarder, TL/LTL, Drayage, POD, Lead Time, Safety Stock, SKU, WMS, TMS, Cross-Docking, Cold Chain, Reverse Logistics, Intermodal, FOB, Demurrage, NMFC, OTD, Control Tower, Scope 3
- Major Players: Integrated Express, 3PL/Warehousing, Freight Brokerage, Logistics Technology
- Core Metrics: Delivery Performance, Cost & Efficiency, Asset Utilization, Customer & Revenue
- Technology Stack: 7 layers — Visibility/Control Tower, TMS, WMS, Warehouse Automation, Last-Mile/Route Optimization, Data/Analytics, IoT/Hardware
- Workflows: Inbound Shipment to Warehouse Receipt (5-step), E-Commerce Order Fulfillment (5-step), Freight Broker Load Execution (5-step)
- Trends: Amazon Disintermediation, Visibility as Table Stakes, Last-Mile Economics Crisis, Warehouse Automation, Nearshoring, Sustainability/Carbon
- Market Dynamics: 5 pain-point cards (rate volatility, capacity fragmentation, last-mile profitability, visibility gaps, labor/driver shortage) + monetization table (asset-based transport, brokerage take rate, 3PL warehousing, integrated logistics, SaaS/technology, fuel surcharge)

### [feature] Video Platforms & Streaming industry primer
- Created `primer/video-platform/index.html` — comprehensive single-page primer with 8-tab navigation
- Featured platforms: YouTube, Netflix, TikTok
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges, Market Dynamics
- Header tags: [YouTube] [streaming] [creator economy] [ad-supported]
- Overview: 6 sub-sector cards (UGC, SVOD, AVOD/FAST, Live Streaming, Short-Form Video, Professional/Educational) + value chain + 6 market context cards
- Terminology: 20 terms — CPM, RPM, Watch Time/AVD, Retention Curve, CTR, Algorithm, Monetization Threshold, CPL, SVOD/AVOD/TVOD/FAST, Churn Rate, Content ID, Mid-Roll/Pre-Roll/Bumper, Shorts Fund/Creator Fund, DAU/MAU, Transcoding/ABR, CDN, CTV, Channel Membership/Super Chat, Video SEO, Audience Retention Signal
- Major Players: UGC/Short-Form, SVOD/Premium, AVOD/FAST, Creator Economy & Infrastructure
- Core Metrics: Audience & Reach, Content Performance, Monetization, Platform Health
- Technology Stack: 7 layers — Video Ingest/Processing, CDN/Delivery, Recommendation/Discovery, Ad Tech, Creator Tools/Analytics, Search/Metadata, Trust & Safety
- Workflows: YouTube Video Production & Upload Lifecycle (5-step), Streaming Platform Content Licensing Deal (5-step), YouTube Ad Campaign Setup (5-step)
- Trends: Attention Economy vs Creator Burnout, CTV Living Room Shift, TikTok Pressure/Ban Risk, AI-Generated Content, Subscription Fatigue, Creator Monetization Diversification
- Market Dynamics: 5 pain-point cards (algorithm dependency, content moderation at scale, creator economics imbalance, streaming profitability crisis, piracy/Content ID evasion) + monetization table (CPM advertising, subscription SVOD, hybrid ad+sub, transactional TVOD, live donations, licensing, creator commerce)

### [feature] Oil & Gas industry primer
- Created `primer/oil/index.html` — comprehensive single-page primer with 8-tab navigation
- Featured companies: ExxonMobil, Chevron, Saudi Aramco, SLB (Schlumberger), Halliburton
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges, Market Dynamics
- Header tags: [upstream] [refining] [OPEC] [energy transition]
- Overview: 6 sub-sector cards (Upstream/E&P, Midstream, Downstream/Refining, NOCs, Oilfield Services, LNG) + full value chain + 6 market context cards
- Terminology: 20 terms — Brent/WTI, Barrel, Upstream/Midstream/Downstream, Proved Reserves, Reserve Replacement Ratio, Lifting Cost, Breakeven Price, Crack Spread, Fracking, OPEC+, Henry Hub, LNG, Wellbore/Completion, API Gravity, Wet/Dry Gas, EUR, Day Rate, Netback, Carbon Intensity, Royalty/Working Interest
- Major Players: Integrated Majors/IOCs, E&P/Independents, National Oil Companies, Oilfield Services
- Core Metrics: Production & Reserves, Financial, Drilling Efficiency, Downstream/Refining
- Technology Stack: 7 layers — Seismic/Exploration, Drilling/Completion, Production Optimization, Midstream Operations, Refinery Process Control, Data/Analytics, ESG/Carbon
- Workflows: Shale Well Drilling & Completion (5-step), Crude Oil Trading & Physical Delivery (5-step), Refinery Crude Procurement & Scheduling (5-step)
- Trends: Energy Transition vs Demand Reality, US Shale Maturity & Consolidation, OPEC+ Cohesion, Methane Regulation/ESG, LNG as Bridge Fuel, Digital Oilfield/AI
- Market Dynamics: 5 pain-point cards (commodity price volatility, permitting/regulatory uncertainty, asset stranding risk, workforce/skill gap, water management in shale) + monetization table (upstream E&P, midstream tolls, downstream refining, oilfield services, LNG tolling, trading/marketing)

### [feature] Commercial Fishing & Aquaculture industry primer
- Created `primer/fishing/index.html` — comprehensive single-page primer with 8-tab navigation
- Featured companies: Mowi, Trident Seafoods, Cermaq, Maruha Nichiro
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges, Market Dynamics
- Header tags: [wild-catch] [aquaculture] [seafood supply chain] [sustainability]
- Overview: 6 sub-sector cards (Wild-Catch, Aquaculture/Fish Farming, Processing/Value-Added, Seafood Distribution/Wholesale, Retail/Food Service, Fishmeal/Feed) + value chain + 6 market context cards
- Terminology: 18 terms — IUU Fishing, MSC, ASC, TAC, ITQ, Bycatch, FIFO Ratio, Biomass, FCR, Sea Lice, Traceability, DWT, Purse Seine, Longlining, Cold Chain Integrity, Roe/ROE Value, Smolt, SRS/IHN
- Major Players: Wild-Catch/Processors, Aquaculture, Distribution/Wholesale, Seafood Tech/Sustainability
- Core Metrics: Wild-Catch, Aquaculture, Processing, Market & Supply Chain
- Technology Stack: 7 layers — Vessel Monitoring/Navigation, Aquaculture Operations, Feed/Precision Feeding, Processing Automation, Cold Chain/Logistics, Traceability/Compliance, Market Data/Analytics
- Workflows: Alaska Pollock Fishing Season Operations (5-step), Atlantic Salmon Farm Grow-Out Cycle (5-step), Seafood Restaurant Supply Chain — Dock to Plate (5-step)
- Trends: Aquaculture Technology/Land-Based RAS, Overfishing & Stock Recovery, Alternative Protein in Feed, Traceability/IUU Crackdown, Climate Change Impacts, DTC & Premiumization
- Market Dynamics: 5 pain-point cards (quota/regulatory volatility, disease/mortality risk, volatile ex-vessel prices, labor/crew availability, cold chain/food safety compliance) + monetization table (wild-catch commodity, value-added processing, aquaculture salmon, DTC subscription, fishmeal/fish oil, data/traceability platform)

### [feature] Market Dynamics tab added to all existing primers (11 primers)
- Added 8th tab "Market Dynamics" with pain-point cards + monetization models table to: insurance, restaurant, sports, esports, video-game-retail, maritime, healthcare, fintech, ecommerce, edtech, ai-infrastructure
- showTab-system primers: added tab button + progress dot-7 via sed; added section HTML via Edit
- data-tab-system primers (ecommerce, edtech, ai-infrastructure): added `data-tab="dynamics"` button + section HTML
- JS "of 7" updated to "of 8" across all primers (sed batch + per-file fix)
- All JS syntax checks PASS

### [feature] Market Dynamics tab added to ecommerce, edtech, and ai-infrastructure primers
- Added 8th tab button (`data-tab="dynamics"`) to `primer/ecommerce/index.html`, `primer/edtech/index.html`, and `primer/ai-infrastructure/index.html`
- No progress dots exist in any of the three files; no dot or label changes were needed
- ecommerce: new `<section class="section" id="dynamics">` — 5 pain-point trend-cards + 6 monetization metric-cards matching file's existing card/grid patterns
- edtech: new `<section class="tab-section" id="tab-dynamics">` (ID prefixed per JS `getElementById("tab-" + target)` convention) — 5 pain-point trend-cards + 6 monetization metric-cards
- ai-infrastructure: new `<section id="dynamics" class="section">` — 5 pain-point trend-cards (grid-2 layout) + 6 monetization metric-rows (metrics-category pattern)
- All three files pass JS syntax check (`node --check`)

### [feature] Market Dynamics tab content added to esports, video-game-retail, and maritime primers
- Added `#tab-dynamics` section to `primer/esports/index.html` — 5 pain-point cards (org profitability crisis, publisher dependency risk, broadcast rights value gap, mobile vs PC economics, player career lifecycle) + monetization table (6 models: sponsorship & brand deals, in-game cosmetics, media rights, merch & apparel, creator & streaming revenue, prize pool winnings)
- Added `#tab-dynamics` section to `primer/video-game-retail/index.html` — 5 pain-point cards (digital distribution cannibalization, publisher DTC & subscription bypass, pre-owned margin under pressure, gray market key resellers, inventory complexity & price decay) + monetization table (6 models: new physical game sales, pre-owned, hardware, digital aggregation, collectibles & merch, trade-in credit float)
- Added `#tab-dynamics` section to `primer/maritime/index.html` — 5 pain-point cards (rate cycle volatility, alliance concentration risk, geopolitical route disruption, decarbonization cost burden, demurrage & detention controversy) + monetization table (6 models: spot freight rate, long-term contract, D&D fees, THC, logistics & integrated services, vessel charter)
- JS syntax checks passed for all three files

### [feature] Market Dynamics tab content added to insurance, restaurant, sports primers
- Added `#tab-dynamics` section to `primer/insurance/index.html` — 5 pain-point cards (regulatory rate-filing lag, catastrophe & climate exposure, social inflation & litigation, InsurTech disintermediation, fraud detection) + monetization table (6 models: written premium, investment income, captive agent, D2C, reinsurance ceding commission, MGA/program business)
- Added `#tab-dynamics` section to `primer/restaurant/index.html` — 5 pain-point cards (3PD commission trap, labor/minimum wage, lease & occupancy, food cost inflation, review & reputation dependency) + monetization table (6 models: dine-in, counter service/fast-casual, 3PD, direct online ordering, catering & B2B, ghost kitchen/virtual brand)
- Added `#tab-dynamics` section to `primer/sports/index.html` — 5 pain-point cards (salary cap escalation, media rights cliff, sports betting cannibalization, international expansion economics, arena economics & real estate) + monetization table (6 models: national media rights, gate/ticket, naming rights & sponsorship, merchandise & licensing, sports betting partnerships, local media/DTC)
- JS syntax checks passed for all three files

### [feature] Market Dynamics section added to healthcare and fintech primers
- Added `<!-- 8. Market Dynamics -->` section to `primer/healthcare/index.html` (`id="tab-dynamics"`) — 5 cards (Regulatory Clearance Timeline, Reimbursement Access Complexity, IDN Consolidation, Cybersecurity & Connected Device Risk, Clinical Evidence Requirements) + Monetization Models table (Capital Equipment Sales, Disposables/Consumables, Service Contracts, Value-Based Contracts, Digital Health SaaS, Direct Sales Force)
- Added `<!-- 8. Market Dynamics -->` section to `primer/fintech/index.html` (`id="dynamics"`) — 5 cards (Regulatory Fragmentation, Legacy Core Banking Integration, Trust & Security, Unit Economics at Scale, AI Bias & Fair Lending Risk) + Monetization Models table (NIM, Interchange Fees, SaaS/API Pricing, AUM Fee, Trading Revenue/PFOF, Lending Spread)

### [feature] Maritime & Shipping industry primer
- Created `primer/maritime/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured carriers: Maersk, MSC, CMA CGM, COSCO/OOCL, Hapag-Lloyd, ONE, Evergreen, Yang Ming
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header tags: [container shipping] [port ops] [freight] [supply chain]
- Overview: 6 sub-sector cards (Container Shipping, Bulk Carriers, Port Operations, Ship Management, Freight Forwarding & Logistics, Maritime Finance & Insurance) + full value chain (Shipper → Freight Forwarder → Ocean Carrier → Port/Terminal → Customs → Inland Transport → Consignee) + 6 market context cards (Maersk, MSC, CMA CGM, Alliance System, Spot vs Contract rates, IMO 2050)
- Terminology: 20 searchable/expandable terms — TEU, FCL/LCL, Bill of Lading, Dead Freight, Demurrage & Detention, NVOCC, Freight Rate, BAF/CAF, ETA/ETD, Port Congestion, Dry-Docking, Flag State, IMO, Incoterms, SCFI, Slot Charter, Charter Party, GRI/PSS, AIS, CII
- Major Players: 4 categories — Container Lines (8 carriers), Ports & Terminal Operators (PSA, DP World, Hutchison, APM Terminals, ICTSI), Freight Forwarders & 3PL (Kuehne+Nagel, DB Schenker, Expeditors, Flexport, C.H. Robinson/Bolloré), Maritime Tech & Data (Windward, Kpler, Freightos, ZeroNorth/Nautilus Labs)
- Core Metrics: Fleet & Capacity (TEU capacity, utilization, vessel count, avg age, fuel efficiency), Rate & Revenue (spot vs contract, SCFI, yield per TEU, revenue per TEU), Port & Terminal (berth utilization, crane moves/hr, vessel turnaround, throughput, dwell time), Operations (schedule reliability, on-time arrival, bunker cost/TEU, CO2/TEU/NM, D&D revenue)
- Technology Stack: 7 layers — Vessel Management (DNV Nauticus, ShipNet, Danaos, AIS), Port & Terminal OS (NAVIS TOS, Tideworks, Jade, CTMS), Freight Booking (Freightos, Flexport, project44, Inttra), Rate Management (CargoSphere, Xeneta, Drewry, FBX), Fleet Analytics & Decarb (Nautilus Labs, ZeroNorth, Wartsila Voyage), Trade Compliance & Docs (CargoWise, Descartes, CrimsonLogic, WAVE eBL), AI & Predictive (Windward, Kpler, IBM Sterling, Portcast)
- Workflows: 3 detailed flows — Container Booking to Vessel Load (5-step), Port Call Operations — Container Terminal (5-step), Freight Rate Negotiation Cycle (5-step)
- Trends: 6 trend cards — Decarbonization & Green Fuels, Digital Freight Platforms, Supply Chain Resilience Post-2021, Alliance Consolidation & Antitrust, Autonomous & Remote Vessels, Red Sea & Geopolitical Risk

## 2026-03-25 (batch 3)

### [feature] Insurance industry primer
- Created `primer/insurance/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured carriers: Allstate, State Farm, Geico, Progressive
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [p&c insurance] [actuarial] [claims] [telematics]
- Overview: 6 sub-sector cards (P&C, Life & Annuity, Health Insurance, Reinsurance, InsurTech, Commercial/Specialty) + insurance value chain (Risk Assessment → Underwriting → Policy Issuance → Premium Collection → Claims Management → Subrogation/Recovery) + 6 market context cards
- Terminology: 18 searchable/expandable terms — Combined Ratio, Loss Ratio, Expense Ratio, Underwriting, Actuary, Premium, Deductible, FNOL, Subrogation, Reinsurance, NAIC, Telematics, Bird Rights (analogy), MLE, Policyholder Surplus, Direct Written Premium, Adverse Selection, Moral Hazard
- Major Players: 4 categories — Personal Lines Carriers (Allstate, State Farm, Geico, Progressive, USAA), Commercial & Specialty (Travelers, Chubb, Zurich, AIG, Markel), Reinsurers (Munich Re, Swiss Re, Berkshire), InsurTech (Lemonade, Root, Hippo, Oscar)
- Core Metrics: Underwriting (combined ratio, loss ratio, expense ratio, policy count, renewal rate), Claims (frequency, severity, LAE ratio, cycle time, fraud rate), Distribution (acquisition cost, agent count, retention rate, NPS), Financial (DWP, investment yield, RoE, solvency ratio)
- Technology Stack: 7 layers — Core Policy Admin (Guidewire, Duck Creek, Applied Epic), Underwriting & Pricing (Verisk, ISO, telematics platforms), Claims Management (Mitchell, CCC, Snapsheet), Data & Analytics (Snowflake, Tableau, SAS), AI & Fraud Detection (Shift Technology, FRISS), Customer & Distribution (Salesforce, agency portals), Compliance (NAIC SERFF)
- Workflows: 3 detailed flows — Auto Quote-to-Bind Process (5-step), Auto Claims FNOL to Settlement (5-step), Actuarial Rate Filing (5-step)
- Trends: 6 trend cards — Telematics & Usage-Based Insurance, AI Underwriting, Direct-to-Consumer Disruption, Climate Risk & Catastrophe Modeling, Embedded Insurance, Real-Time Claims via AI

### [feature] Restaurant & Food Service industry primer
- Created `primer/restaurant/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured concepts: Ramen shop, poke shop (fast-casual)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [food service] [fast-casual] [ghost kitchen] [unit economics]
- Overview: 6 sub-sector cards (QSR, Fast-Casual, Full-Service, Ghost Kitchens, Food Halls, Catering) + restaurant value chain (Supplier → Receiving → Prep/Kitchen → FOH Service → POS/Payment → Delivery/Takeout) + 6 market context cards
- Terminology: 16 searchable/expandable terms — FOH/BOH, Cover, Table Turn, Food Cost %, Prime Cost, Mise en Place, 86, PAR, RevPASH, Menu Engineering, 3PD Commission, Ghost Kitchen, HACCP, Same-Store Sales, Labor Cost %, POS
- Major Players: 4 categories — QSR & Fast-Casual Chains (McDonald's, Chipotle, Sweetgreen, Cava, Pokeworks), Delivery Platforms (DoorDash, Uber Eats, Grubhub), Restaurant Tech (Toast, Square, Olo, SevenRooms), Suppliers & Distributors (Sysco, US Foods, local farms)
- Core Metrics: Financial Health (food cost %, labor cost %, prime cost %, gross profit per cover), Operational (table turn time, covers/day, RevPASH, avg ticket, order error rate), Delivery & Digital (3PD mix %, delivery margin, online order %, avg delivery rating), Growth (same-store sales growth, unit-level EBITDA, payback period)
- Technology Stack: 7 layers — POS (Toast, Square, Revel), Kitchen Display (KDS), Online Ordering & Aggregation (Olo, DoorDash Storefront), Inventory & Procurement (MarketMan, BlueCart), Reservations & Waitlist (OpenTable, Resy, Yelp Waitlist), Analytics & Reporting (Restaurant365, Avero), Payments & Loyalty (Stripe, Square, app-based loyalty)
- Workflows: 3 detailed flows — Daily Opening Prep Sequence (5-step), Poke Bowl Order Fulfillment — FOH to Pickup (5-step), End-of-Day Close & Reporting (5-step)
- Trends: 6 trend cards — Ghost Kitchen Expansion, Dynamic Menu Pricing, 3PD Commission Pressure, AI-Driven Demand Forecasting, Sustainability & Sourcing Transparency, Labor Cost Automation

### [feature] Sports & Athletics industry primer
- Created `primer/sports/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured league: NBA (basketball)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [nba] [sports analytics] [media rights] [salary cap]
- Overview: 6 sub-sector cards (Professional Leagues, Media & Broadcast, Sports Betting, Team Operations, Sports Technology, Sponsorship & Brand) + sports value chain (League/Commissioner → Team Ownership → Coaching Staff → Player Roster → Broadcast/Media → Fans & Bettors) + 6 market context cards
- Terminology: 15 searchable/expandable terms — Salary Cap, Bird Rights, Max/Supermax Contract, MLE (Mid-Level Exception), Net Rating, TS% (True Shooting), PER, EPM/RAPTOR/BPM, Pace, Media Rights, Luxury Tax, Trade Deadline, Draft Pick/Lottery, Load Management, Second Spectrum
- Major Players: 4 categories — NBA Teams & Ownership (Golden State, Boston, Lakers, Celtics), Media & Broadcast (ESPN/ABC, TNT, Amazon Prime, Apple TV+), Sports Tech & Analytics (Second Spectrum, Synergy Sports, Sportradar, Genius Sports), Venues & Operations (AEG, Oak View Group, Ticketmaster/Live Nation)
- Core Metrics: On-Court (net rating, TS%, pace, AST/TO ratio, ORtg/DRtg, EPM), Team Business (gate revenue, media revenue share, luxury tax bill, payroll efficiency), Media & Fan Engagement (TV ratings, streaming viewers, social followers, jersey sales, arena attendance), Betting (handle, hold %, market share)
- Technology Stack: 7 layers — Player Tracking (Second Spectrum, Hawk-Eye, SportVU), Video & Analytics (Synergy, nba.com/stats, Catapult), Broadcast (EVS, ChyronHego, IBM Watson Highlights), Sports Betting Integration (Sportradar, Genius Sports, OpenBet), Fan Experience (NBA App, Ticketmaster, arena Wi-Fi), Team Operations (Catapult GPS, Kitman Labs, force plates), Data & Visualization (Tableau, Python/R, STATS Perform)
- Workflows: 3 detailed flows — NBA Draft Scouting Pipeline (5-step), In-Game Coaching & Analytics (5-step), Salary Cap & Roster Construction (5-step)
- Trends: 6 trend cards — Sports Betting Normalization, Direct-to-Consumer Streaming, AI in Coaching & Player Development, International Expansion (NBA Global), Arena as Experience Hub, Sports Data as Competitive Moat

### [feature] primer/index.html — 3 new industry cards + nav links (insurance, restaurant, sports)
- Added insurance, restaurant, and sports cards to the industry grid with `data-search` attributes
- Added 3 new nav links to sidebar (with "New" badge) for insurance, restaurant, and sports

## 2026-03-25 (batch 2)

### [feature] Healthcare & MedTech industry primer
- Created `primer/healthcare/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured company: Stryker (Mako robotic platform, ortho, neurotechnology, MedSurg)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [medical devices] [surgical robotics] [digital health] [clinical]
- Overview: 6 sub-sector cards (Medical Devices, Surgical Robotics, Diagnostics, Digital Health, Hospital Systems, Pharma Interface) + MedTech value chain (R&D → Clinical Trials → FDA Clearance → Manufacturing → Distribution → Hospital/OR → Patient Outcome) + 6 market context cards
- Terminology: 25 searchable/expandable terms — 510(k), PMA, De Novo, Device Classification, CE Mark/MDR, UDI, IDE, IDN, GPO, VAC, ASC, Capital Equipment vs. Consumables, DRG, CPT Code, Mako, Total Joint Arthroplasty, Biocompatibility, Sterilization, GMP/ISO 13485, Post-Market Surveillance, DICOM/PACS, EHR/Epic, HIPAA, PROMs, Trauma & Spine
- Major Players: 4 categories — Large-Cap OEMs (Stryker, Medtronic, J&J MedTech, Zimmer Biomet, Boston Scientific, Abbott), Surgical Robotics (Intuitive, Mako, ROSA, Hugo), Imaging & Diagnostics (Siemens, GE HealthCare, Philips, Hologic), Health Systems & Purchasing (HCA, Mayo Clinic, Vizient GPO, Epic)
- Core Metrics: Commercial Performance (organic growth, gross margin, ASP, installed base, procedures/system, win rate), Operational & R&D (R&D%, clearance timeline, recall rate, DSO, inventory turns), Clinical Outcomes (revision rate, PROMs, SSI rate, LOS, implant positioning accuracy)
- Technology Stack: 7 layers — Imaging & Standards (DICOM, PACS, HL7 FHIR), Surgical Planning (Mako pre-op CT, Brainlab), Robotic Platforms (Mako, da Vinci, ROSA, Hugo), EHR/Integration (Epic, Cerner, FHIR R4), AI & Analytics (Aidoc, Nuance DAX, Med-Gemini), IoT & Connectivity (remote monitoring, wearables), Regulatory & Quality (Veeva Vault, MasterControl, GUDID)
- Workflows: 3 detailed flows — FDA 510(k) Clearance Process (7-step), Stryker Mako Surgical Case Day-of Workflow (6-step), Hospital Device Procurement / VAC Process (5-step)
- Trends: 6 trend cards — Surgical Robotics Expansion, AI in Diagnostic Imaging, ASC Shift, Value-Based Care Pressure, Digital Health Integration, Regulatory Complexity & MDR
- JS: tab switching, glossary search, click-to-expand terms, `/` keyboard shortcut, progress dots

### [feature] eSports & Competitive Gaming industry primer
- Created `primer/esports/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured title: Wild Rift (League of Legends: Wild Rift by Riot Games / Garena SEA) and WCS (Wild Rift Champions SEA)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [competitive gaming] [mobile esports] [streaming] [Wild Rift]
- Overview: 6 sub-sector cards (Tournament Ecosystem, Team Orgs, Streaming & Media, Sponsorships, Mobile eSports, Creator Economy) + eSports value chain (Developer → Tournament Org → Teams/Players → Broadcast → Sponsors → Fans) + 6 market context cards
- Terminology: 18 searchable/expandable terms — MOBA, KDA, Meta, Draft/Pick & Ban, Major Objectives (Wild Rift), Roles & Lanes, Gank, CS/Farm, MMR/Elo, WCS Champions SEA, Esports Org, Prize Pool, Media Rights, Skins & Cosmetics, Battle Pass, Scrim, Patch/Balance Update, Content Creator/Streamer
- Major Players: 4 categories — Publishers (Riot, Valve, Activision Blizzard, Tencent/Garena), Esports Orgs (T1, Cloud9, FaZe Clan, Team Flash, RSG, 100 Thieves), Broadcast & Streaming (Twitch, YouTube Gaming, Nimo TV/Booyah, FACEIT/ESL), Sponsors (HyperX, Red Bull, Logitech G, BMW/Mercedes)
- Core Metrics: Viewership (peak CCV, hours watched, AMA, unique viewers), Team & Org Business (sponsorship revenue, merch GMV, social following, engagement rate, team valuation), Player Performance — Wild Rift (KDA, damage share, CS/min, objective participation, vision score)
- Technology Stack: 7 layers — Game Platform, Broadcast & Production, Tournament Platforms, Player Analytics, Streaming CDN, Team Comms & Ops, Anti-Cheat & Security
- Workflows: 3 detailed flows — Pro Team Weekly Preparation Cycle (6-step, patch analysis through post-match debrief), Tournament Production Match Day Ops (6-step), Esports Org Sponsorship Deal Lifecycle (5-step)
- Trends: 6 trend cards — Mobile Esports Explosion, Org Profitability Crisis, AI Coaching & Analytics, Regionalization vs. Global Format, Creator Economy Blurring, Franchise League Debate

### [feature] Video Game Retail industry primer
- Created `primer/video-game-retail/index.html` — comprehensive single-page primer with 7-tab navigation
- Featured platform: GameStop (video game retail aggregator / marketplace)
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: tag-row with [retail] [digital distribution] [pre-owned market] [GameStop]
- Overview: 6 sub-sector cards (Physical Retail, Digital Storefronts, Pre-Owned & Resale, Subscription Gaming, Collector Market, Marketplace Aggregators) + retail value chain (Publisher → Distributor → Retailer → Consumer → Secondary Market) + 6 market context cards
- Terminology: 18 searchable/expandable terms — SKU, MSRP, Trade-In, Pre-Owned, Pre-Order, DLC, Game Pass/Subscription, Digital Key, Attach Rate, Sell-Through Rate, Inventory Turns, AAA Title, Indie Games, Limited/Collector Edition, Platform Exclusivity, Gray Market/Key Resellers, GMV, Back Catalog
- Major Players: 4 categories — Physical Retailers (GameStop, Best Buy, Walmart/Target, Amazon), Digital Storefronts (Steam, PlayStation Store, Xbox Store, Nintendo eShop, Epic Games Store), Subscription Services (Xbox Game Pass Ultimate, PlayStation Plus, EA Play, Apple Arcade), Marketplace & Resale (GameStop, StockX, eBay, WATA Games/VGA)
- Core Metrics: Retail Performance (gross margin by category, AOV, trade-in rate, pre-owned mix, launch week sell-through), Digital Platform (take rate, MAU/DAU, subscriber count, digital vs. physical ratio), Marketplace/Aggregator — GameStop (GMV, take rate, catalog depth, price accuracy/freshness, user library size)
- Technology Stack: 7 layers — E-Commerce Platform, POS, Digital Delivery APIs (Steam, Xbox, PSN, IGDB), Price Intelligence (IsThereAnyDeal, CheapShark, eBay API), Inventory & ERP, Payments, Analytics & Personalization
- Workflows: 3 detailed flows — Game Launch Day Operations (5-step), Pre-Owned Trade-In & Resale Process (5-step), Digital Storefront Game Listing Pipeline including GameStop aggregation (5-step)
- Trends: 6 trend cards — Digital-First Shift, Subscription Cannibalization, Collector Market & Nostalgia Premium, AI-Driven Trade-In Pricing, Cross-Platform Play Reducing Lock-In, Marketplace Aggregation as Consumer Value

### [feature] primer/index.html — 3 new industry cards + nav links added
- Added healthcare, esports, and video-game-retail cards to the industry grid with searchable data-search attributes
- Added 3 new nav links to sidebar (with "New" badge) for each new industry

## 2026-03-25

### [feature] Higher Education & EdTech industry primer
- Created `primer/edtech/index.html` — comprehensive single-page primer with 7-tab navigation
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: breadcrumb back to `../index.html`, title, subtitle, tag-row with [academia] [curriculum design] [ai literacy]
- Overview: sub-sector grid and value chain diagram covering the Higher Ed & EdTech landscape
- Terminology: 30 searchable/expandable glossary terms covering LMS, VLE, SCORM, xAPI, cmi5, LTI, MOOC, OPM, ITS, adaptive learning, Bloom's Taxonomy, HyFlex, micro-credentials, and more
- Major Players: 6 categories — LMS Platforms, MOOCs & Online Learning, EdTech Tools (Classroom & Engagement), AI & Adaptive Learning, Corporate L&D, Infrastructure (Video, Auth, Proctoring)
- Core Metrics: 6 categories — Enrollment & Access, Student Success, Engagement (Platform), Outcomes, Platform Health, Financial
- Technology Stack: 7 layers — Content Creation, LMS, Video & Lecture Capture, Assessment & Proctoring, Analytics & Student Success, AI Layer, Identity & Authentication
- Workflows: 3 detailed flows — Course Design Lifecycle, Student Success Pipeline, AI-Augmented Instruction (Instructor-as-Agent Model)
- Trends: 6 trend cards — AI Tutoring & Khanmigo-style Assistants, Credential Inflation & Stackable Micro-credentials, HyFlex & Hybrid-Native Design, AI Literacy as Core Curriculum, Academic Integrity in the LLM Era, OPM Model Under Pressure
- JS: tab switching, glossary search filter with hidden class toggling, click-to-expand term cards, `/` keyboard shortcut to focus search
- No apostrophes in JS strings; all strings use double quotes or template literals

### [feature] AI Infrastructure & Research Ops industry primer
- Created `primer/ai-infrastructure/index.html` — comprehensive single-page primer with 7-tab navigation
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: breadcrumb back to `../index.html`, title, subtitle, tag-row with [rag] [multi-agent] [mlops] [llmops]
- Overview: 6 sub-sector cards (Foundation Models, Vector DB, Orchestration, MLOps, Observability, Sovereign AI), full value chain diagram
- Terminology: ~35 searchable/expandable glossary terms covering RAG, vector embeddings, chunking, KV cache, quantization, RLHF/DPO, multi-agent, MCP, LLMOps, prompt injection, LoRA, semantic caching, structured output, and more
- Major Players: 8 categories — Foundation Models, Vector DBs, Orchestration Frameworks, MLOps, Model Serving, Cloud Platforms, Observability, Hardware
- Core Metrics: 6 categories — Retrieval Quality (Precision@K, Recall@K, MRR, NDCG), RAG Faithfulness (RAGAS), Generation Quality (BLEU/ROUGE/BERTScore/LLM-as-judge), Inference Performance (TTFT, TPS, P95/P99), System Reliability, Business metrics
- Technology Stack: 7 layered architecture panels (Data, Embedding, Retrieval, Orchestration, LLM, Observability, Deployment)
- Workflows: 3 detailed flows — Enterprise RAG Pipeline, Multi-Agent Orchestration, MLOps Model Lifecycle
- Trends: 6 trend cards — Agentic AI at Scale, RAG vs Long Context, On-Device Inference, Multimodal Agents, Sovereign AI, Evaluation Crisis
- JS: tab switching, glossary search filter with term count, click-to-expand term cards, `/` keyboard shortcut to focus search
- No apostrophes in JS strings; all strings use concatenation with double quotes

### [feature] Financial Services & FinTech industry primer
- Created `primer/fintech/index.html` — full single-page primer with 7-tab navigation
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Header: breadcrumb, title with emoji, subtitle, tag-row with [commerce] [data science] [capital markets]
- Progress dot indicator showing active section with label "Section N of 7"
- Overview: 4 industry cards, 6-card sub-sector grid, value chain diagram (Capital Sources → Intermediaries → Markets → End Users)
- Terminology: 28 searchable/expandable glossary terms across 8 categories (Data, Payments, Performance, Risk, Funds, Markets, Compliance, DeFi, Trading, AI)
- Major Players: 6 sector sections with 22 player cards (Data, Investment Banks, FinTech, Asset Management, RegTech, Infrastructure)
- Core Metrics: table format across 4 categories (Performance, Risk, Banking, FinTech/Business) with formula, description, and benchmarks
- Technology Stack: 7 layers with chip badges (Data, Processing, Models, Storage, APIs, Frontend, Compliance/Audit)
- Workflows: 3 detailed step-by-step flows (Trade Lifecycle 7-step, Financial Analysis Pipeline 5-step, Agentic Finance Pattern 6-step)
- Trends: 6 trend cards (Agentic Finance, DeFi/CBDCs, RegTech/AI, Real-Time Everything, Alternative Data, Embedded Finance)
- JS: tab switching, glossary search filter, click-to-expand glossary, `/` keyboard shortcut, progress dots
- No apostrophes in JS strings; all strings use double quotes or template literals

### [feature] E-Commerce & Digital Marketplaces industry primer
- Created `primer/ecommerce/index.html` — full single-page primer with 7-tab navigation
- Tabs: Overview, Key Terminology, Major Players, Core Metrics, Technology Stack, Common Workflows, Trends & Challenges
- Overview includes sub-sector grid (6 cards) and interactive value chain diagram
- Terminology section: ~30 glossary terms with search filter and click-to-expand; `/` keyboard shortcut focuses search
- Major Players: 6 categories (Platforms, Commerce Enablement, Payments, Logistics, Marketing/AdTech, Fraud/Trust) with 27 player cards
- Core Metrics: Business Health, Customer, Conversion Funnel (visual bar), Operations, Search & Discovery, Advertising
- Technology Stack: 7 layers with chip badges and explanatory notes
- Workflows: 3 detailed step-by-step flows (Order Lifecycle, Search Ranking Pipeline, Seller Onboarding)
- Trends: 6 trend cards (AI Personalization, Social Commerce, Quick Commerce, Marketplace Integrity, Supply Chain Resilience, Recommerce)

## 2026-03-24

### [feature] Initial Primer section created
- Created `primer/` directory and `primer/index.html` landing page
- Structured with sidebar nav, search, industry card grid, and about section
- Cards designed to support status badges (live / wip / coming-soon) and progress bars
- Scheduled task created to periodically prompt for new industries to add
- Section and nav entry added to root `index.html`
