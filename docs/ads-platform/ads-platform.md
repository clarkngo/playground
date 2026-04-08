Here is a comprehensive, structured summary of the terms, technologies, concepts, processes, and workflows discussed across the sources. This is designed to serve as a high-level foundational knowledge base for mastering an Advertising Platform / Infrastructure domain. 

### 1. Core Advertising Concepts & Terminology
These terms form the business foundation of the advertising and monetization domain.
*   **Advertising Programs:** 
    *   **PLS (Promoted Listings Standard):** Cost-per-sale ads.
    *   **PLA (Promoted Listings Advanced):** Cost-per-click (CPC) ads based on keyword targeting.
    *   **PLX (Promoted Listings Express):** A simpler ads tier.
    *   **SFA (Seller-Funded Ads):** Ads funded directly by the seller.
    *   **Promoted Display / Brand Solutions:** Self-service solutions and targeted banner campaigns.
*   **Monetization Models:** 
    *   **CPM (Cost Per Mil):** Cost per thousand impressions.
    *   **CPC (Cost Per Click):** Advertisers pay only when an ad is clicked.
    *   **CPA/CPO (Cost Per Acquisition/Order):** Payment based on a user action or purchase.
    *   **Fixed Price / Tenancy:** Event-based advertising paid at a flat rate (e.g., Homepage takeover).
*   **Key Performance Indicators (KPIs):**
    *   **GMV (Gross Merchandise Value) / PL-Enabled GMV:** Total sales amount; PL-Enabled refers to the GMV directly driven by Promoted Listings.
    *   **ROAS (Return on Ad Spend):** GMV divided by ad revenue.
    *   **Attribution Ratio:** The percentage of sales attributed to ad clicks.
    *   **Take Rate / Sold Ad Rate:** The effective fee rate charged for sold ads.
*   **Ad Tech Ecosystem terms:**
    *   **DSP (Demand-Side Platform) & SSP (Supply-Side Platform):** Platforms that allow programmatic buying (advertisers) and selling (publishers) of ad inventory.
    *   **RTB (Real-Time Bidding):** The dynamic auction environment for buying and selling ad impressions programmatically.

### 2. Technologies & Tech Stack
The platform operates on a massive, distributed microservices and big data infrastructure.
*   **Data & Streaming:**
    *   **Rheos & Kafka:** The internal messaging and event streaming platforms used for real-time data flow (e.g., tracking clicks and impressions).
    *   **Apache Flink & Spark:** Used for real-time and offline data processing, aggregations, and batch jobs.
    *   **Hadoop (Apollo/Hermes):** Used for heavy offline batch processing, merging, and deduplication tasks.
*   **Databases & Search:**
    *   **ClickHouse (NuColumnar):** A highly performant columnar database used for real-time metrics, analytics, and reporting.
    *   **Elasticsearch (Pronto):** Used for log storage, anomaly detection, monitoring, and storing aggregated metadata.
    *   **Cassini:** The core internal search engine.
*   **Infrastructure & Ops:**
    *   **Tess.io / Kubernetes:** The container orchestration platform used for deploying backend microservices, Celery workers, and web apps.
    *   **Control Center (Shepherd):** The internal observability hub to monitor system health, metrics, alerts, and recent code/experiment changes.
    *   **Sherlock.IO & Prometheus / Grafana:** Used for time-series metrics monitoring, logging, and setting up PromQL-based alerting rules.
*   **Front-End & Middleware:**
    *   **MFE (Merch Front End) & Nori:** Rendering layers and middleware that structure data for the client and handle the asynchronous loading of ad modules.

### 3. Core Concepts
*   **Tracking & Pathing (Sojourner):** The system used to track user behavior (clicks, page views) via UBI (User Behavior Interaction) tables. It relies heavily on tags like `siid` (Source Impression ID) and `ciid` (Current Impression ID) to accurately map the path a user took through the site, even accounting for multiple tabs or missing data.
*   **Experimentation (A/B Testing):** Managed via tools like Touchstone. The platform uses legacy `et` tags (placement-level) and newer `xt` tags (event-level) to monitor the near-real-time impact of experimental algorithms on revenue and user engagement.
*   **AdBlocker Mitigation:** A framework that rotates rendering "strategies" on the Search Results Page (SRP) to prevent browser AdBlockers from hiding sponsored listings.

### 4. Processes
*   **Incident Management & On-Call (SRE):**
    *   **Alerting:** Alerts fire via PagerDuty and Slack when thresholds (e.g., sudden GMV or click drops) are breached.
    *   **Triaging:** On-call engineers (L1 Infra, L2 Domain/QE) have 15 minutes to respond. They use tools like Sherlock, CAL logs, and Control Center to isolate the issue (e.g., checking if an experiment ramped up, if a batch job failed, or if an Avro schema changed).
    *   **Remediation & RCA:** The team rolls back the problematic code or configuration. A Post-Mortem / Root Cause Analysis (RCA) is documented to trace the failure, analyze revenue impact, and implement preventative measures.
*   **Contracting & Sales (Hive CRM):**
    *   Sales reps use Hive (Salesforce) to create Insertion Orders (IOs). Standard contracts use templates, while Non-Standard contracts (like programmatic or custom partnerships) require Legal and Controlling approval via a Contract Management System (CMS).
    *   Once signed, campaigns are pushed to the ad server (like DFP/Google Ad Manager), which syncs impression data back to Hive for billing.

### 5. Workflows
*   **Data Validation Workflow:** Ensures data integrity across the pipeline. Users set up scheduled jobs that cross-check accuracy (e.g., validating that metrics match between ClickHouse, HDFS, and Elasticsearch) and send automated success/failure emails.
*   **Code Rollout & Deployment Workflow:**
    *   Developers push code (PRs) linked to Jira tickets.
    *   Jenkins builds the Docker images, which are then deployed sequentially (e.g., Workers -> Beat -> API) to Pre-Prod/Staging, and finally to Production via the Cloud Console.
    *   A `codeChangeScrubber` tracks these deployments in ServiceNow, logging the changes into the Control Center so any metric anomalies can be visually correlated with recent deployments.
*   **Front-End Optimization Workflow (Vision Zero):** 
    *   To prevent site degradation, ads are given strict SLAs for loading. If backend services (like Cassini or pricing) time out, the rendering layer uses "Napkin" for asynchronous/lazy loading to prevent the page from collapsing.