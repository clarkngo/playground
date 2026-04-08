#!/usr/bin/env python3
"""Inject Data Governance tab into industry primers (O'Reilly-style framing)."""
from __future__ import annotations

import re
from pathlib import Path

from datagov_data import DATA

ROOT = Path(__file__).resolve().parents[1]
INDUSTRY = ROOT / "industry"
BOOK_HREF = "../../../data-gov-book/index.html"


def esc(s: str) -> str:
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def build_body(data: dict, wrapper: str = "section") -> str:
    intro = esc(data["intro"])
    rows = "".join(
        f"<tr><td>{esc(a)}</td><td>{esc(b)}</td><td>{esc(c)}</td></tr>\n        "
        for a, b, c in data["rows"]
    )
    cards = "".join(
        f'<div class="card"><h3>{esc(t)}</h3><p>{esc(p)}</p></div>\n      '
        for t, p in data["cards"]
    )
    close = "section" if wrapper == "section" else "div"
    return f"""  <!-- 10. Data Governance -->
  <{wrapper} class="tab-section" id="tab-datagov">
    <div class="section-title">Data Governance</div>
    <p class="section-desc">{intro}</p>
    <p class="section-desc" style="margin-top:10px;opacity:.95">Framed after <em>Data Governance: The Definitive Guide</em> (O&rsquo;Reilly): governance covers <strong>decision rights, policy, metadata, quality, privacy, and lifecycle</strong> &mdash; complementary to the Data Architecture tab. See the <a href="{BOOK_HREF}">interactive Data Governance supplement</a> in this playground.</p>

    <div class="section-title" style="font-size:15px;margin-top:20px;margin-bottom:12px;">Governance lenses (industry-specific)</div>
    <table class="metrics-table">
      <thead><tr><th>Practice area</th><th>What &ldquo;good&rdquo; looks like</th><th>Examples in this industry</th></tr></thead>
      <tbody>
        {rows}
      </tbody>
    </table>

    <div class="section-title" style="font-size:15px;margin-top:28px;margin-bottom:12px;">Operating realities</div>
    <div class="card-grid">
      {cards}
    </div>
  </{close}>

"""


# (find this exact substring, replacement for dataarch opening only — comment upgraded to 11)
MARKERS = [
    (
        "  <!-- 10. Data Architecture & Flows -->\n  <section class=\"tab-section\" id=\"tab-dataarch\">",
        "  <!-- 11. Data Architecture & Flows -->\n  <section class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    (
        "  <!-- ── Section 10: Data Architecture & Flows ── -->\n  <section class=\"tab-section\" id=\"tab-dataarch\">",
        "  <!-- ── Section 11: Data Architecture & Flows ── -->\n  <section class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    (
        "<!-- Tab 10: Data Architecture & Flows -->\n<section class=\"tab-section\" id=\"tab-dataarch\">",
        "<!-- Tab 11: Data Architecture & Flows -->\n<section class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    (
        "  <!-- ===== SECTION 10: DATA ARCHITECTURE & FLOWS ===== -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
        "  <!-- ===== SECTION 11: DATA ARCHITECTURE & FLOWS ===== -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    (
        "  <!-- ══════════════════════════════════════════════\n       SECTION 10 — DATA ARCHITECTURE & FLOWS\n  ══════════════════════════════════════════════ -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
        "  <!-- ══════════════════════════════════════════════\n       SECTION 11 — DATA ARCHITECTURE & FLOWS\n  ══════════════════════════════════════════════ -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    # E-commerce uses <div class="tab-section"> (not <section>)
    (
        "  <!-- ── Section 10: Data Architecture & Flows ── -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
        "  <!-- ── Section 11: Data Architecture & Flows ── -->\n  <div class=\"tab-section\" id=\"tab-dataarch\">",
    ),
    # AI infrastructure uses id="tab-data-arch" and id before class
    (
        "  <!-- 10. Data Architecture & Flows -->\n  <div id=\"tab-data-arch\" class=\"tab-section\">",
        "  <!-- 11. Data Architecture & Flows -->\n  <div id=\"tab-data-arch\" class=\"tab-section\">",
    ),
]


def patch_nav(html: str) -> str:
    html = html.replace("showTab('dataarch',9)", "showTab('dataarch',10)")
    html = html.replace("showTab('data-arch',9)", "showTab('data-arch',10)")
    html = html.replace("showTab('incidents',10)", "showTab('incidents',11)")
    html = html.replace("showTab('failures',10)", "showTab('failures',11)")
    datagov_btn = '\n    <button class="tab-btn" onclick="showTab(\'datagov\',9)">Data Governance</button>'
    html = re.sub(
        r'(<button class="tab-btn" onclick="showTab\(\'evolution\',8\)">[^<]+</button>)',
        r"\1" + datagov_btn,
        html,
        count=1,
    )
    if 'id="dot-11"' not in html:
        html = html.replace(
            '<div class="progress-dot" id="dot-10"></div>',
            '<div class="progress-dot" id="dot-10"></div><div class="progress-dot" id="dot-11"></div>',
            1,
        )
    html = re.sub(
        r'(<span class="progress-label"[^>]*>Section 1 of )11(</span>)',
        r"\g<1>12\2",
        html,
        count=1,
    )
    return html


def inject_file(path: Path, slug: str, data: dict) -> bool:
    html = path.read_text(encoding="utf-8")
    if 'id="tab-datagov"' in html:
        print(f"  skip (exists): {slug}")
        return False
    wrapper = "div" if slug == "edtech" else "section"
    body = build_body(data, wrapper=wrapper)
    done = False
    for old_open, new_open in MARKERS:
        if old_open in html:
            html = html.replace(old_open, body + new_open, 1)
            done = True
            break
    if not done:
        print(f"  FAIL no marker: {slug}")
        return False
    html = patch_nav(html)
    path.write_text(html, encoding="utf-8")
    print(f"  ok: {slug}")
    return True


def main() -> None:
    for slug, payload in DATA.items():
        p = INDUSTRY / slug / "index.html"
        if not p.exists():
            print(f"missing file: {p}")
            continue
        inject_file(p, slug, payload)


if __name__ == "__main__":
    main()
