# Changelog — Wild Rift

Path: `/wild-rift/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-05-07 (2)

### [feature] Move List guide panel — T-Hex Mecha
- Added slide-in guide panel to `wild-rift/thex-mecha.html`, open by default
- Sections: Movement, Mounting, Abilities (Mecha Only), Tips
- Color-coded key badges: cyan (movement/dismount), gold (mount/Q), green (W), red (R)
- Each ability row shows name, description, and cooldown time
- Three strategy tips at the bottom (W+Q combo, E+R follow-up, pilot fragility)
- Toggle via `?` button in HUD or `H` key; `✕` button or `H` to close
- Panel width uses `min(320px, 100%)` for narrow-viewport compatibility

## 2026-05-07 (2)

### [feature] T-Hex Mecha mini-game
- Added `wild-rift/thex-mecha.html` — single-file HTML5 Canvas game simulating the T-Hex Mecha mechanic from Wild Rift
- Hextech dark blue/gold aesthetic with grid arena, top-down perspective
- Pilot mode: WASD movement, walk to T-Hex and press F to mount
- Mecha mode: slower movement, 500 HP, 4 abilities on Q/W/E/R, G to dismount
- [Q] Missile Barrage — 5 projectiles toward mouse cursor with AoE explosions
- [W] Amplifying Field — golden pulse animation + BUFFED status (increases missile damage)
- [E] Iron Tail — 360° sweep ring animation pushing nearby enemy cubes away
- [R] Laser Beam — 3-second channeled beam following mouse cursor with continuous damage
- Enemy cubes spawn and move toward player; increase in numbers as kills accumulate
- Skill bar with per-ability cooldown overlays and timers
- HUD with pilot/mecha HP bars, kill counter, mode label, mount hint
- Added Wild Rift section to `index.html` sidebar nav and main content grid

## 2026-02-19

### [ux] Bug fixes to baron smite timing logic
- Minor corrections to `wild-rift/baron-smite.html` — 5 lines changed
- Adjusted timing or display behavior for the smite trainer

### [feature] Added Wild Rift pings tool
- `wild-rift/pings.html` — 111-line page for Wild Rift in-game ping sounds
- Added 6 audio files for ping sounds:
  - `attack.ogg` (18 KB) — attack ping
  - `danger.ogg` (15 KB) — danger/retreat ping
  - `group.ogg` (20 KB) — group up ping
  - `missing.ogg` (15 KB) — missing enemy ping
  - `omw.ogg` (24 KB) — on my way ping
  - `retreat.ogg` (20 KB) — retreat ping

---

## 2026-02-04

### [ux] UI refinements to Baron Smite trainer
- `wild-rift/baron-smite.html` — significant layout and interaction improvements (224 lines total after edit)
- Refactored game container layout and styling

### [ux] Further updates to Baron Smite interaction model
- Additional updates in same session — improved timer behavior and visual feedback

### [refactor] Renamed baron_smite.html to baron-smite.html
- File renamed from `wild-rift/baron_smite.html` to `wild-rift/baron-smite.html`

### [feature] Created Wild Rift Baron Smite timing trainer
- `wild-rift/baron_smite.html` — 248-line interactive smite timing game
  - Dark LoL-styled UI (`#050a15` background, cyan glow border)
  - Baron Nashor image (`baron_nashor.png`, 474 KB)
  - Smite sound effect (`smite_sound.mp3`, 39 KB)
  - Flash animation on smite (`body.smite-flash`)
  - Score tracking and timing feedback
- `wild-rift/test.html` — test/prototype page (156 lines)
- Also added `ai-proof-of-concepts/multi-agent-simulation.html` and `physical-ai/virtual-lidar.html` in same commit
