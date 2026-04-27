# Changelog — Escape Room

Path: `escape-room/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-04-27

### [feature] The Pitt — Stryker escape room, initial release

- Created `escape-room/the-pitt/index.html` — standalone single-file escape room
- **Theme**: Post-apocalyptic (year 2147); players discover a sealed Stryker R&D bunker guarded by AI "ARIS"
- **3 chambers**, each with 3 examine items and a code lock:
  - Chamber 01 — The Airlock: code `1941` (Stryker founding year); clues via Roman numeral nameplate, Dec 8 1941 journal entry, corrupted terminal
  - Chamber 02 — The Research Lab: code `MAKO` (Stryker robotic surgery system); clues via blueprint, research notes, pre-Collapse brochure
  - Chamber 03 — The Vault: code `TOGETHER` (first word of Stryker mission statement); clues via chiseled granite inscription, Homer audio transcript, mosaic floor tiles
- **Features**: live timer, clue log per chamber, wrong-attempt tracker (dot indicators), clue modal popup, debrief screen with answers explained, Play Again reset
- **Aesthetic**: post-apocalyptic green terminal palette, scanline overlay, glow/pulse/blink CSS animations
- **Audience**: Stryker employees
