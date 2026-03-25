# Primer Changelog

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
