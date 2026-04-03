# Conversation to Design — Changelog

All changes to the `conversation-to-design/` collection.

---

## 2026-04-02

### [feature] Launch conversation-to-design collection (10 activities)

New interactive series teaching requirements engineering from unstructured team conversations.
Each activity is a self-contained HTML file with a shared 7-step engine and a `const SCENARIO` data object.

**Files created:**
- `conversation-to-design/index.html` — collection index with 10 activity cards and "How It Works" guide
- `conversation-to-design/01-employee-chat-rag.html` — Slack thread, RAG system for employee records
- `conversation-to-design/02-ecommerce-inventory.html` — Zoom chat, real-time inventory sync across 12 warehouses
- `conversation-to-design/03-ride-sharing-platform.html` — Slack thread, driver matching and geospatial dispatch
- `conversation-to-design/04-healthcare-scheduling.html` — Email thread, HIPAA/FHIR appointment scheduling
- `conversation-to-design/05-social-media-feed.html` — Slack thread, ML-ranked feed with hybrid fan-out
- `conversation-to-design/06-banking-transactions.html` — Jira thread, ACID/exactly-once/fraud detection
- `conversation-to-design/07-video-streaming.html` — Slack thread, RTMP ingest, HLS, DVR buffer
- `conversation-to-design/08-iot-sensor-dashboard.html` — Slack thread, 2000-sensor ingestion and edge buffering
- `conversation-to-design/09-support-ticketing.html` — Slack thread, replacing Zendesk with ML auto-routing
- `conversation-to-design/10-food-delivery.html` — Discord thread, 8-state order machine and driver dispatch

**7-Step activity structure:**
1. The Conversation — read-only Slack/email/Jira/Discord thread rendering
2. Actors and Goals — checkbox selection with distractor actors
3. Functional Requirements — drag-and-drop triage (Valid vs. Hallucinated)
4. Non-Functional Requirements — click-to-assign category (Privacy/Performance/Usability/Reliability) + Explicit/Implied toggle
5. Open Questions — checkbox identification of conversation gaps
6. Design Doc Builder — radio/checklist/dropdown for Problem Statement, Goals, Non-Goals, Tech Stack
7. Architecture Challenge — drag-and-drop sequence + component-responsibility matching

**Engine features:**
- `const SCENARIO` data pattern separates content from engine across all 10 files
- `localStorage` persistence per activity (`ctd-{slug}` key)
- Deterministic avatar colors from speaker name hash
- 7-segment progress bar with done/current/locked states
- Score summary after Step 7 with per-step breakdown
- Slack-style dark thread renderer with backtick-to-`<code>` conversion and divider support
- JS syntax check passed for all 10 files

**Root index.html updated:**
- Added sidebar nav link "Conversation to Design" (badge: 10)
- Added `data-section="conversation-to-design"` section block with 10 file-cards
