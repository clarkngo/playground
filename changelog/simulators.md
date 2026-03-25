# Changelog — Simulators

Path: `/simulators/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

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
