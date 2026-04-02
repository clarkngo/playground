# Changelog — Dev Foundations Activities

## 2026-04-02

### [ux] All 10 activities — dual-panel simulator replaces dropdown
- Replaced single `<select>` + one Simulate button with two side-by-side `.sim-panel` blocks, each labeled and with its own `▶ Simulate` button — no scenario selection step required
- Added `.sim-dual`, `.sim-panel`, `.sim-panel-header`, `.sim-panel-label` CSS classes; removed `.sim-controls` and `.sim-select`
- All simulator JS updated: `runSimulator(key, sfx)` signature, `_simTimers = { a: [], b: [] }` per-panel timers, all element IDs suffixed with `-a` or `-b`
- Added `@media (max-width: 620px) { .sim-dual { flex-direction: column; } }` to all activity files

### [ux] All 10 activities — Validate Architecture + Export PDF button placement normalized
- **Activities 07 and 08**: buttons were in the canvas column (below the drop zone); moved to toolbox column (below `#toolbox`) to match all other activities
- **Activity 07**: removed `&#10003;` prefix from "Validate Architecture"; added `no-pdf` class to Export PDF button
- **Activity 08**: changed button label from "Validate Pipeline" → "Validate Architecture"; removed `&#8681;` icon from "Export PDF"; added `no-pdf` class
- All 10 files now have identical button markup in `#toolbox-col`

---

## 2026-04-01

### [feature] Activities 02–10 live — full collection complete
- `02-distributed-version-control.html` — Distributed Version Control System: sequence WorkingTree → StagingIndex → LocalRepo → RemoteRepo → BranchRef → MergeEngine → CITrigger; distractors: Central Lock Server, Single Shared Branch, FTP File Upload; simulator: Distributed Git Workflow vs Centralized Lock-Based Workflow
- `03-rest-api-gateway.html` — REST API Gateway Architecture: sequence Client → DNS → LoadBalancer → APIGateway → AuthService → AppServer → Database; distractors: CDN Proxy, Message Queue, Direct DB Write; simulator: Secure API Gateway Path vs Direct Client-to-Database (Insecure)
- `04-relational-database-internals.html` — Relational Database Internals: sequence SQLParser → QueryOptimizer → ExecEngine → BufferPool → StorageEngine → WAL → DiskStorage; distractors: Full Table Scan Optimizer, Memory-Only Storage, Skip Transaction Log; simulator: Optimized Query Path vs Full Table Scan
- `05-automated-testing-pipeline.html` — Automated Testing Pipeline: sequence UnitRunner → Coverage → Integration → ReportAgg → QualityGate → ArtifactStore → DeployGate; distractors: Deploy Before Tests, Skip Coverage Check, Manual QA Only; simulator: Gate-First Pipeline vs Deploy-Before-Test Anti-Pattern
- `06-software-architecture-layers.html` — Layered Software Architecture (SOLID): sequence Presentation → Application → Domain → RepoInterface → DataAccess → Database → ExternalSvc; distractors: Business Logic in UI, Direct DB from Presentation, Circular Dependency; simulator: Clean Architecture vs Spaghetti Architecture
- `07-application-security-architecture.html` — Application Security Architecture: sequence WAF → APIGateway → AuthService → InputValidation → BusinessLogic → EncryptedStore → AuditLog; distractors: Plaintext Credentials, Skip WAF, Auth After Business Logic; simulator: Hardened Request vs Unguarded Request
- `08-cicd-pipeline-architecture.html` — CI/CD Pipeline Architecture: sequence SourceRepo → CIBuild → ArtifactReg → Staging → AutoTests → ApprovalGate → Production; distractors: Deploy to Prod Before Testing, Skip Artifact Registry, Skip Staging; simulator: Full CI/CD Pipeline Deploy vs Direct-to-Production
- `09-microservices-system-design.html` — Microservices System Design: sequence APIGateway → ServiceReg → Microservices → MsgBroker → PerSvcDB → DistCache → Observability; distractors: Shared Monolithic DB, Direct Calls Without Registry, Skip Message Broker; simulator: Microservices Architecture vs Monolithic Architecture
- `10-resilient-distributed-system.html` — Resilient Distributed System Design: sequence LoadBalancer → CircuitBreaker → RetryBackoff → Bulkhead → ReplicaSet → DistTracing → ChaosTesting; distractors: Single Point of Failure, No Circuit Breaker, Skip Replica Set; simulator: Resilient Failure vs Cascading Failure
- All 9 new activities share identical CSS/JS shell from Activity 01; only LAB_CONFIG, toolData, distractors, and simulator scenarios differ per file
- All 10 activities pass `node --check` JS syntax validation

### [feature] Homepage `index.html` created for dev-foundations collection
- `dev-foundations-activities/index.html` — dark theme landing page with 10-card activity grid, "How It Works" 4-step section, and answer key banner
- Links back to `../index.html` (root playground); card links match `01-container-runtime-architecture.html` through `10-resilient-distributed-system.html`

### [feature] `answer-key.html` — all 10 modules marked Live with correct sequences
- All status pills updated from "Planned" to "Live"; mod-badge updated to `.built` (green) for all 10 modules

---

Path: `/dev-foundations-activities/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-01

### [feature] Created Dev Foundations Activities collection — Activity 01 live, 02–10 planned
- `dev-foundations-activities/01-container-runtime-architecture.html` — Container Runtime Architecture: sequence 7 stack layers (Application Code → Dockerfile → Container Image → Container Runtime → OS Namespaces/cgroups → Host Kernel → Physical Hardware) with 4 VM-themed distractors (Full VM Hypervisor, Guest OS, Registry Cache, Reverse Proxy)
- GitHub dark theme (raw CSS, no Tailwind): `#0d1117` background, `#58a6ff` accents, `#3fb950` pass, `#f85149` fail
- Toolbox Fisher-Yates shuffles all 11 items (7 correct + 4 distractors) on each load
- Validation: count-mismatch hint fires before per-layer contextual clues (catches placed distractors cleanly)
- `removePlaced()` re-numbers canvas steps after item removal
- `dragleave` uses `!canvas.contains(e.relatedTarget)` to prevent drag-over flicker
- Student name required; PDF export blocked until Validate Architecture is clicked
- `index.html` — Added "Dev Foundations" sidebar nav entry (data-filter="dev-foundations") after Database Labs; added 10-card section div (data-section="dev-foundations") with placeholder cards 02–10 pointing to future files
