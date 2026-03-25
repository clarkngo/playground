# Changelog — System Design Labs

Path: `/system-design/` and `/system-design-labs/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-02-25

### [refactor] Moved system-design game and course files to prototypes/
- `system-design/system-design-game.html` deleted from system-design/ and moved to `prototypes/system-design/`
- `system-design/system-design-course.html` moved to `prototypes/system-design/`
- New system-design case studies added: `autonomous-ai-agent.html`, `collaborative-document-editor.html`, `database-sharding-and-scaling.html`, `e-commerce-scalability.html`, `global-cdn.html`, `message-queues-and-asynchronous-workers.html`, `microservices-service-discovery.html`, `multi-region-disastery-recovery.html`, `real-time-data-processing-and-iot.html`, `secure-banking-transaction.html`
- Each case study is approximately 207 lines with consistent interactive format

### [feature] Added system design case studies (9 scenarios)
- Collaborative Document Editor
- Database Sharding and Scaling
- E-Commerce Scalability
- Global CDN
- Message Queues and Async Workers
- Microservices Service Discovery
- Multi-Region Disaster Recovery
- Real-Time Data Processing and IoT
- Secure Banking Transaction
- Autonomous AI Agent scenario

---

## 2026-02-13

### [feature] Added system design course and digital twins explainer
- `system-design/system-design-course.html` — large 2162-line React-based interactive course
- Uses React 18 via CDN with Tailwind CSS

---

## 2026-01-06

### [feature] Created System Design Architect drag-and-drop game
- `system-design/system-design-game.html` — interactive drag-and-drop architecture game (117 lines)
- Toolbox with components: User Client, Load Balancer, Web Server, Database
- Drop zone canvas for building architecture diagrams
- "Validate Architecture" button checks component arrangement
- PDF export via html2pdf.js
- Added to main `index.html` homepage
