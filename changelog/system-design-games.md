# Changelog — System Design Games

Path: `/system-design/` (game files), `/prototypes/system-design/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-02-25

### [refactor] Game files moved to prototypes/
- `system-design/system-design-game.html` moved to `prototypes/system-design/system-design-game.html`
- `system-design/system-design-course.html` moved to `prototypes/system-design/system-design-course.html`

### [feature] Added architect sandbox and AI agent prototypes
- `prototypes/system-design/architect-sandbox.html` — PASS/FAIL architecture validation tool using Mermaid.js diagrams (157 lines)
  - Checkbox-based component selector drives live Mermaid diagram rendering
  - Pass/fail assessment with feedback on required components
- `prototypes/system-design/autonomous-ai-agent-v-1.html` — autonomous AI agent system design prototype (149 lines)
- `prototypes/system-design/docker.html` — Docker architecture exploration (122 lines)
- `prototypes/system-design/scalability.html` — scalability concepts interactive page (238 lines)
- `prototypes/system-design/veritystream.html` — VerityStream scenario design (85 lines)

---

## 2026-01-06

### [feature] Created System Design Architect drag-and-drop game
- `system-design/system-design-game.html` — 117-line interactive architecture game
- Drag-and-drop toolbox: User Client, Load Balancer, Web Server, Database
- Drop zone canvas with component ordering validation
- "Validate Architecture" button — checks arrangement and provides feedback
- PDF export support via html2pdf.js
- Added to main `index.html` homepage navigation
