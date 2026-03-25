# Changelog — Security

Path: `/security/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-20

### [refactor] Moved security/ to prototypes/security/ for CY615 labs
- Relocated `security/cy615/` entire folder tree under `prototypes/security/cy615/`
- Moved `GUIDE-software-security-apps.md`, `architect-gate` variants, `bof-3-dragon-gene-combinator.html`, `hidden-script-v0.html`, `integer-trap-v0.html`, `work-progress.html` to `prototypes/security/`
- Updated `security/index.html` with new layout and card-based navigation
- Updated `security/cryptography.html` and `security/secure-header.html` with revised content

---

## 2026-03-16

### [feature] Added CY615 course lab suite under security/
- Created `security/cy615/index.html` — course hub with lab card grid (10 labs)
- Created `security/cy615/shared.css` — shared dark-theme stylesheet for all CY615 labs
- Created `security/cy615/shared.js` — shared JavaScript utilities
- Created `security/cy615/week1-lab/index.html` — Week 1 interactive lab (472 lines)
- Created `security/cy615/week2-lab/index.html` — Week 2 interactive lab (533 lines)
- Updated `security/index.html` with CY615 section entry

---

## 2025-12-18

### [refactor] Consolidated all security files into security/ folder
- Moved 18 standalone HTML files from root into `security/` directory:
  - `architect-gate v01.html`, `architect-gate-v0.html`, `architect-gate.html`
  - `brute-force-balance.html`, `cost-of-insecurity.html`, `cryptography.html`
  - `data-integrity.html`, `hidden-script-v0.html`, `integer-trap-v0.html`, `integer-trap.html`
  - `invisible-request.html`, `malicious-link.html`, `missing-gate.html`
  - `poisoned-script.html`, `salted-vault.html`, `secure-header.html`, `shattered-database.html`
- Also moved `GUIDE-software-security-apps.md` into the security folder

---

## 2025-12-16

### [feature] Added SDLC secure coding exercises (5 new labs)
- `cryptography.html` — cryptography secure coding exercise
- `data-integrity.html` — data integrity secure coding exercise
- `invisible-request.html` — invisible/hidden request attack exercise (552 lines)
- `poisoned-script.html` — poisoned/malicious script injection exercise (488 lines)
- `secure-header.html` — HTTP security headers exercise (297 lines)

---

## 2025-12-14

### [feature] Added "The Shattered Database" secure coding exercise
- `shattered-database.html` — 593-line interactive PyScript exercise covering SQL injection defense
- Uses PyScript for in-browser Python execution
- Split-panel layout: scenario/instructions left, code editor right
- Includes syntax guide, good/bad code examples, PDF export

---

## 2025-12-13

### [feature] Added 4 new SDLC security activities
- `brute-force-balance.html` — brute force attack mitigation exercise (PyScript)
- `bof-3-dragon-gene-combinator.html` — buffer overflow themed exercise using BoF3 dragon gene combiner
- `architect-gate.html` / `architect-gate-v0.html` / `architect-gate v01.html` — access control gate exercises
- `missing-gate.html` / `hidden-script-v0.html` — missing authentication and hidden script exercises
- `salted-vault.html` — password salting/hashing exercise
- `malicious-link.html` — malicious link/phishing awareness exercise

---

## 2025-11-25

### [ux] Minor edits to cost-of-insecurity content
- Revised text content and layout in `cost-of-insecurity.html`
- Removed one trailing line

---

## 2025-11-20

### [feature] Created "The Cost of Insecurity" interactive lab
- `cost-of-insecurity.html` — 616-line interactive security awareness lab
- Features CIA triad drag-and-drop sorter, cost calculator sliders, code vulnerability quiz
- Dark/light mode toggle, beginner AI prompts, sticky header
- Created initial `index.html` homepage with playground navigation
