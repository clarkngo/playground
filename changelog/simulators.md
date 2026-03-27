# Changelog — Simulators

Path: `/simulators/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-27

### [bug] Wireshark simulator — script terminated early by embedded `</script>` in sample HTML
- **Symptom:** Page loaded but the simulator did not run (blank packet list, controls inert).
- **Root cause:** The HTTP “200 OK” scenario data included a literal `</script>` inside a string. HTML parsers end the enclosing `<script>` at the first `</script>` substring, even inside JavaScript source.
- **Fix:** `simulators/wireshark-simulator.html` — escape the closing tag as `<\/script>` in the embedded sample; fold the multi-line HTML body into one template literal so the script is valid JavaScript.

## 2026-03-20

### [feature] Created Wireshark Network Analysis Simulator
- `simulators/wireshark-simulator.html` — 1750-line full-featured Wireshark UI simulator
  - Faithful recreation of Wireshark's 3-pane layout: packet list, packet details, hex dump
  - Toolbar with capture controls, display filter bar with quick-filter buttons
  - Step-by-step guided analysis mode with progress bar and "Next Step" navigation
  - Simulated packet capture with protocol color coding:
    - ARP (pale yellow), ICMP (blue), TCP (light purple), UDP (light blue)
    - HTTP (green), DNS (light blue), TLS (light green), DHCP (cream)
  - Display filter input with real-time validation (green/red border feedback)
  - Packet details tree view and hex dump pane
  - Insight panel (bottom-right) with contextual explanations per step
  - Step preview bar shows upcoming packet description
  - Dark navbar with GitHub-style color scheme
- Added Wireshark Simulator card to main `index.html`
