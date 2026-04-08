#!/usr/bin/env python3
"""
Splice HOS01-style curated handouts into 03–10 workflow HTML files.

Run from repo root:
  python3 hos/dev-foundations-activities-hos/build_hos_curated_03_10.py

Re-run after editing handout text below or after regenerating figures.
"""
from __future__ import annotations

import glob
import pathlib
import re

from hos_verbatim_pdf_append import full_pdf_text_append, inject_verbatim_styles

BASE = pathlib.Path(__file__).resolve().parent

TARGETS: dict[str, pathlib.Path] = {
    "03": BASE / "03-flask-rest-api-hos-workflow.html",
    "04": BASE / "04-databases-mysql-hos-workflow.html",
    "05": BASE / "05-unit-testing-hos-workflow.html",
    "06": BASE / "06-uml-visual-modeling-hos-workflow.html",
    "07": BASE / "07-security-hos-workflow.html",
    "08": BASE / "08-cicd-static-web-hos-workflow.html",
    "09": BASE / "09-microservices-azure-functions-hos-workflow.html",
    "10": BASE / "10-advanced-microservices-aws-lambda-hos-workflow.html",
}

LAB_INTRO = (
    '<p style="margin-top:.65rem;font-size:.88rem;color:#8b949e;line-height:1.55;max-width:820px;">'
    "Structured handout and figures from the PDF appear first; at the end of that section, expand "
    "<strong>Complete document text (extracted from PDF)</strong> for the full step-by-step plain-text extraction. "
    "Then the interactive sequence activity. Course: CS445 Software Process Management &mdash; "
    "School of Technology &amp; Computing (STC), City University of Seattle (CityU).</p>"
)


def fig(folder: str, src: str, cap: str) -> str:
    return (
        f'    <div class="hos-pdf-fig-wrap">\n'
        f'      <img class="hos-pdf-fig" src="{folder}/{src}" alt="{cap}" loading="lazy" decoding="async" />\n'
        f'      <div class="hos-pdf-fig-cap">{cap}</div>\n'
        f"    </div>\n"
    )


def fig_grid_open() -> str:
    return '    <div class="hos-pdf-fig-grid">\n'


def fig_grid_close() -> str:
    return "    </div>\n"


def all_figs_grid(folder: str, label: str) -> str:
    """Sorted PNGs with captions derived from filenames (HOS01-style fallback index)."""
    path = BASE / folder
    if not path.is_dir():
        return f'    <p class="hos-pdf-note">No figures folder: {folder}</p>\n'
    names = sorted(glob.glob(str(path / "*.png")))
    if not names:
        return f"    <p>No PNG figures in {folder}.</p>\n"
    parts = [
        f'    <h3 class="hos-pdf-fig-h">{label}</h3>\n',
        fig_grid_open(),
    ]
    for fn in names:
        bn = pathlib.Path(fn).name
        parts.append(fig(folder, bn, f"From PDF extraction — {bn}"))
    parts.append(fig_grid_close())
    return "".join(parts)


def std_before_you_start() -> str:
    return (
        "    <h2>Before You Start</h2>\n"
        "    <ul>\n"
        "      <li>Screenshots may be different from your environment.</li>\n"
        "      <li>The directory path shown in screenshots may be different from yours.</li>\n"
        "      <li>The steps might have subtle discrepancies. Please use your best judgment while completing each step in this cookbook-style tutorial.</li>\n"
        "      <li>Some steps may not be explained in detail. If you are not sure what to do:\n"
        "        <ol>\n"
        "          <li>Consult the resources from the course.</li>\n"
        "          <li>If you cannot solve the problem after a few tries (usually 15&ndash;30 minutes), ask a TA for help.</li>\n"
        "        </ol>\n"
        "      </li>\n"
        "    </ul>\n\n"
    )


def std_readings() -> str:
    return (
        "    <h2>Readings and Examples</h2>\n"
        "    <ul>\n"
        "      <li>Visit the CS 445 Repository for Examples.\n"
        '        <ol class="hos-subol">\n'
        "          <li>Select the related module.</li>\n"
        "          <li>Visit the README.md file.</li>\n"
        "          <li>Find examples for your practice.</li>\n"
        "        </ol>\n"
        "      </li>\n"
        "    </ul>\n\n"
    )


def open_section(hos: str, title: str, meta_lines: list[str]) -> str:
    meta = "<br />\n      ".join(meta_lines)
    return (
        f'  <!-- Complete {hos} handout (content from PDF; curated like HOS01) -->\n'
        f'  <section class="hos-pdf-source" aria-label="{hos} full handout">\n'
        f'    <div class="hos-kicker">{hos} &mdash; complete handout</div>\n'
        '    <div class="hos-pdf-meta">\n'
        f"      <strong>CS445 Software Process Management</strong><br />\n"
        f"      {title}<br />\n"
        f"      {meta}\n"
        "    </div>\n\n"
    )


def close_section() -> str:
    return "  </section>\n"


# ─── HOS03A (Flask REST) — full curated spine ───────────────────────────────


def handout_03() -> str:
    d = "hos03-pdf-figures"
    p: list[str] = []
    p.append(open_section("HOS03A", "HOS03A &mdash; Restful API using Flask", ["Developed by Kina Anh Bui (04/17/2025) &middot; Reviewed by Sam Chung (04/18/2025) &middot; Reviewed by Clark Ngo (12/4/2025)"]))
    p.append(fig_grid_open())
    p.append(fig(d, "p01_fig0.png", "PDF page 1 &mdash; header"))
    p.append(fig(d, "p01_fig1.png", "PDF page 1 &mdash; title"))
    p.append(fig_grid_close())
    p.append(std_before_you_start())
    p.append(std_readings())
    p.append(
        "    <h2>Learning Outcomes</h2>\n"
        "    <ul>\n"
        "      <li>Section 1: Accessing GitHub Codespaces</li>\n"
        "      <li>Section 2: Creating of Micro Service</li>\n"
        "      <li>Section 3: Testing CRUD Operations</li>\n"
        "      <li>Section 4: Pushing Your Work to GitHub</li>\n"
        "    </ul>\n\n"
    )
    p.append(
        "    <h2>Upload screenshots (GitHub Classroom)</h2>\n"
        "    <ol>\n"
        '      <li><span class="hos-cmd">01_install_flask_firstname_lastname.png</span> &mdash; Install Flask</li>\n'
        '      <li><span class="hos-cmd">02_install_flask_restful_firstname_lastname.png</span> &mdash; Install Flask-RESTful</li>\n'
        '      <li><span class="hos-cmd">03_hello_world_firstname_lastname.png</span> &mdash; Hello World in browser</li>\n'
        '      <li><span class="hos-cmd">04_body_firstname_lastname.png</span> &mdash; POST body in Postman</li>\n'
        '      <li><span class="hos-cmd">05_retrieving_records_firstname_lastname.png</span> &mdash; GET record</li>\n'
        '      <li><span class="hos-cmd">06_deleting_records_firstname_lastname.png</span> &mdash; DELETE record</li>\n'
        "    </ol>\n\n"
    )
    p.append(
        "    <h2>Key Concepts</h2>\n"
        "    <p>This lab builds a small Python service with <strong>Flask</strong> and <strong>Flask-RESTful</strong>, exposes CRUD routes over HTTP, and verifies them with <strong>Postman</strong>.</p>\n"
        "    <p><strong>REST</strong> uses predictable HTTP verbs (GET/POST/PUT/DELETE) so clients and servers agree on how data is transferred.</p>\n\n"
    )
    p.append(
        "    <h2>Section 1: Accessing GitHub Codespaces</h2>\n"
        "    <p>Open the assignment Codespace; prerequisites include a GitHub account.</p>\n\n"
        "    <h2>Section 2: Creating a Micro Service</h2>\n"
        "    <h3>Project folder</h3>\n"
        "    <pre class=\"hos-pre-df\">mkdir helloworld-app\ncd helloworld-app</pre>\n"
        "    <h3>Install dependencies</h3>\n"
        '    <pre class="hos-pre-df">pip install Flask\npip install Flask-RESTful</pre>\n'
        "    <h3>app.py starter</h3>\n"
        "    <p>Create <span class=\"hos-cmd\">app.py</span> with Flask app, in-memory <span class=\"hos-cmd\">database</span> dict, a <span class=\"hos-cmd\">/</span> route returning Hello World, then add REST routes for <span class=\"hos-cmd\">/students</span> (POST/PUT) and <span class=\"hos-cmd\">/students/&lt;name&gt;</span> (GET/DELETE) as in the PDF.</p>\n"
        "    <p>Use <span class=\"hos-cmd\">jsonify</span> for JSON responses and check request bodies with <span class=\"hos-cmd\">request.get_json()</span>.</p>\n"
    )
    p.append(fig_grid_open())
    for fn, cap in [
        ("p02_fig2.png", "PDF &mdash; mkdir / cd"),
        ("p04_fig3.png", "PDF &mdash; pip install Flask"),
        ("p04_fig4.png", "PDF &mdash; pip output"),
        ("p05_fig5.png", "PDF &mdash; Flask-RESTful install"),
        ("p06_fig6.png", "PDF &mdash; app.py starter"),
    ]:
        p.append(fig(d, fn, cap))
    p.append(fig_grid_close())
    p.append(
        "    <h3>Run Flask</h3>\n"
        '    <pre class="hos-pre-df">export FLASK_APP=app.py\nflask run --host=0.0.0.0</pre>\n'
        "    <p>Make the forwarded port <strong>public</strong>, open the URL, confirm <strong>Hello World!</strong>, screenshot <span class=\"hos-cmd\">03_hello_world_…</span>.</p>\n"
    )
    p.append(fig_grid_open())
    p.append(fig(d, "p09_fig7.png", "Ports / public URL"))
    p.append(fig(d, "p09_fig8.png", "Browser Hello World"))
    p.append(fig(d, "p09_fig9.png", "Flask run output"))
    p.append(fig(d, "p09_fig10.png", "Additional UI from PDF"))
    p.append(fig_grid_close())
    p.append(
        "    <h2>Section 3: Testing CRUD Operations (Postman)</h2>\n"
        "    <p>Install Postman, create a workspace and request. Use POST with JSON body to create, PUT to update, GET to retrieve, DELETE to remove &mdash; match URLs to your Codespace hostname.</p>\n"
    )
    p.append(fig_grid_open())
    for fn in [
        "p10_fig11.png",
        "p10_fig12.png",
        "p11_fig13.png",
        "p11_fig14.png",
        "p12_fig15.png",
        "p12_fig16.png",
        "p13_fig17.png",
        "p13_fig18.png",
        "p13_fig19.png",
        "p13_fig20.png",
        "p15_fig21.png",
        "p15_fig22.png",
        "p16_fig23.png",
        "p16_fig24.png",
        "p17_fig25.png",
        "p18_fig26.png",
    ]:
        p.append(fig(d, fn, f"Postman / app — {fn}"))
    p.append(fig_grid_close())
    p.append(
        "    <h2>Section 4: Pushing Your Work to GitHub</h2>\n"
        "    <p>Commit <span class=\"hos-cmd\">app.py</span>, screenshots, and any notes; push to your GitHub Classroom remote.</p>\n"
    )
    p.append(full_pdf_text_append("03"))
    p.append(close_section())
    return "".join(p)


# ─── HOS04A — Docker primary + without-Docker figures ──────────────────────


def handout_04() -> str:
    d = "hos04-pdf-figures"
    db = "hos04b-pdf-figures"
    p: list[str] = []
    p.append(
        open_section(
            "HOS04A",
            "HOS04A &mdash; Databases",
            ["Developed by Kina Anh Bui (04/23/2025) &middot; Revised by Sam Chung (04/24/2025) &middot; Reviewed by Clark Ngo (12/4/2025)"],
        )
    )
    p.append(fig_grid_open())
    p.append(fig(d, "p01_fig0.png", "PDF page 1"))
    p.append(fig(d, "p01_fig1.png", "PDF page 1 (title)"))
    p.append(fig_grid_close())
    p.append(std_before_you_start())
    p.append(std_readings())
    p.append(
        "    <h2>Learning Outcomes</h2>\n"
        "    <ul>\n"
        "      <li>Section 1: Accessing GitHub Codespaces</li>\n"
        "      <li>Section 2: MySQL Docker Container</li>\n"
        "      <li>Section 3: Database CRUD Operation</li>\n"
        "      <li>Section 4: Pushing Your Work to GitHub</li>\n"
        "    </ul>\n\n"
    )
    p.append(
        "    <h2>Upload screenshots</h2>\n"
        "    <ol>\n"
        '      <li><span class="hos-cmd">01_login_…</span> Adminer login</li>\n'
        '      <li><span class="hos-cmd">02_dbe_…</span> Database explorer</li>\n'
        '      <li><span class="hos-cmd">03_create_…</span> CREATE</li>\n'
        '      <li><span class="hos-cmd">04_insert_…</span> INSERT</li>\n'
        '      <li><span class="hos-cmd">05_read_…</span> READ</li>\n'
        '      <li><span class="hos-cmd">06_update_…</span> UPDATE</li>\n'
        '      <li><span class="hos-cmd">07_delete_…</span> DELETE</li>\n'
        "    </ol>\n\n"
    )
    p.append(
        "    <h2>Key Concepts</h2>\n"
        "    <p>Use <strong>Docker</strong> (or your instructor&rsquo;s alternate path) to run <strong>MySQL</strong> and <strong>Adminer</strong>. Practice SQL <strong>DDL</strong> and <strong>DML</strong> CRUD operations with screenshot evidence.</p>\n\n"
    )
    p.append("    <h2>Section 1: Accessing GitHub Codespaces</h2>\n    <p>Open the Codespace tied to your assignment repository.</p>\n\n")
    p.append(
        "    <h2>Section 2: MySQL (Docker track — primary PDF)</h2>\n"
        "    <p>Follow <span class=\"hos-cmd\">docker-compose.yml</span>, <span class=\"hos-cmd\">Dockerfile</span>, and service names from the handout. Start containers, confirm MySQL listens, then open Adminer.</p>\n"
    )
    p.append(all_figs_grid(d, "Figures from Docker / primary PDF"))
    p.append(
        "    <h2>Section 2b: Without Docker (alternate PDF)</h2>\n"
        "    <p class=\"hos-pdf-note\">If your instructor assigns the &ldquo;without Docker&rdquo; handout, follow that PDF for host-based MySQL and client steps. Figures below are from the alternate document.</p>\n"
    )
    p.append(all_figs_grid(db, "Figures from without-Docker PDF"))
    p.append(
        "    <h2>Section 3: Database CRUD</h2>\n"
        "    <p>Execute CREATE / INSERT / SELECT / UPDATE / DELETE as assigned; capture each screenshot filename listed above.</p>\n\n"
    )
    p.append("    <h2>Section 4: Pushing Your Work to GitHub</h2>\n    <p>Push SQL scripts, Docker files, and screenshots per Classroom instructions.</p>\n")
    p.append(full_pdf_text_append("04"))
    p.append(close_section())
    return "".join(p)


def handout_05() -> str:
    p = [
        open_section("HOS05A", "HOS05A &mdash; Unit Testing", ["Developed by Kina Anh Bui (04/29/2025) &middot; Reviewed by Sam Chung (05/01/2025) &middot; Reviewed by Clark Ngo (12/04/2025)"]),
        std_before_you_start(),
        std_readings(),
        "    <h2>Learning Outcomes</h2>\n    <ul>\n      <li>Section 1: Accessing GitHub Codespaces</li>\n      <li>Section 2: Testcase Basic</li>\n      <li>Section 3: Automation Test Suite for Flask Application</li>\n      <li>Section 4: Pushing Your Work to GitHub</li>\n    </ul>\n\n",
        "    <h2>Upload screenshots</h2>\n    <ol>\n"
        '      <li><span class="hos-cmd">01_simple_test_…</span> simpleTest</li>\n'
        '      <li><span class="hos-cmd">02_simple_test_add_…</span> simpleTest add</li>\n'
        '      <li><span class="hos-cmd">03_flask_test_…</span> flaskTest</li>\n'
        '      <li><span class="hos-cmd">04_flask_test_add_…</span> flaskTest add</li>\n'
        "    </ol>\n\n",
        "    <h2>Key Concepts</h2>\n    <p>Unit tests target small pieces of logic in isolation; the lab progresses to an automated test suite exercising a Flask app (often with <strong>pytest</strong> or <strong>unittest</strong> per your PDF).</p>\n\n",
        "    <h2>Section 1: Accessing GitHub Codespaces</h2>\n    <p>Open your Codespace and repository.</p>\n\n",
        "    <h2>Section 2: Basic testcase</h2>\n    <p>Author minimal tests, run them from the terminal, capture required screenshots.</p>\n\n",
        "    <h2>Section 3: Automation suite for Flask</h2>\n    <p>Wire tests to the Flask microservice; run the suite and fix failures before submission.</p>\n\n",
        all_figs_grid("hos05-pdf-figures", "Figures from PDF (extraction order)"),
        "    <h2>Section 4: Pushing Your Work to GitHub</h2>\n    <p>Push test modules and evidence to GitHub.</p>\n",
        full_pdf_text_append("05"),
        close_section(),
    ]
    return "".join(p)


def handout_06() -> str:
    p = [
        open_section("HOS06A", "HOS06A &mdash; UML Visual Modeling", ["Developed by Kina Anh Bui (05/07/2025) &middot; Reviewed by Sam Chung (05/08/2025) &middot; Reviewed by Clark Ngo (12/04/2025)"]),
        std_before_you_start(),
        std_readings(),
        "    <h2>Learning Outcomes</h2>\n    <ul>\n      <li>Section 1: Activity Diagram</li>\n      <li>Section 2: Creating a Sign-Up Activity Diagram</li>\n      <li>Section 3: Use Case Diagrams</li>\n      <li>Section 4: Pushing Your Work to GitHub</li>\n    </ul>\n\n",
        "    <h2>Upload screenshots</h2>\n    <ol>\n"
        '      <li><span class="hos-cmd">01_activity_diagram_…</span></li>\n'
        '      <li><span class="hos-cmd">02_use_case_diagram_…</span></li>\n'
        "    </ol>\n\n",
        "    <h2>Key Concepts</h2>\n    <p>The PDF uses <strong>Visual Paradigm Online</strong> (per handout) to produce <strong>Activity</strong> and <strong>Use Case</strong> diagrams using OMG UML conventions.</p>\n\n",
        "    <h2>Section 1–3: Modeling</h2>\n    <p>Follow the PDF to create activity flows (including sign-up) and use case diagrams; export or screenshot as required.</p>\n\n",
        all_figs_grid("hos06-pdf-figures", "Figures from PDF"),
        "    <h2>Section 4: Pushing Your Work to GitHub</h2>\n    <p>Add exported images or project files to the repo and push.</p>\n",
        full_pdf_text_append("06"),
        close_section(),
    ]
    return "".join(p)


def handout_07() -> str:
    p = [
        open_section("HOS07A", "HOS07A &mdash; Security", ["Developed by Kina Anh Bui (05/13/2023) &middot; Reviewed by Sam Chung (05/15/2025) &middot; Revised by Scott Zhou (02/27/2026)"]),
        std_before_you_start(),
        "    <h2>Learning Outcomes</h2>\n    <ul><li>Experiencing SQL Injection</li></ul>\n\n",
        "    <h2>Key Concepts</h2>\n    <p><strong>SQL injection</strong> lets attackers manipulate database queries. The lab contrasts vulnerable vs hardened Flask apps and uses supporting SQL setup scripts.</p>\n\n",
        "    <h2>Section 1: Accessing GitHub Codespaces</h2>\n    <p>Open Codespace; you may also use local VS Code per PDF note.</p>\n\n",
        "    <h2>Section 2: Project layout</h2>\n    <p>Use the folder structure from the PDF (<span class=\"hos-cmd\">app_vulnerable.py</span>, <span class=\"hos-cmd\">app_secure.py</span>, <span class=\"hos-cmd\">setup_db.py</span>, etc.).</p>\n\n",
        "    <h2>Section 3: Exercise SQLi scenarios</h2>\n    <p>Run the vulnerable path, observe injection, then apply mitigations in the secure variant.</p>\n\n",
        all_figs_grid("hos07-pdf-figures", "Figures from PDF"),
        "    <h2>Section 4: Submit</h2>\n    <p>Push code and screenshots per instructor.</p>\n",
        full_pdf_text_append("07"),
        close_section(),
    ]
    return "".join(p)


def handout_08() -> str:
    p = [
        open_section(
            "HOS08A",
            "HOS08A &mdash; CI/CD",
            ["Developed by Ajay Naik (05/12/2023) &middot; Kina Anh Bui (05/22/2025) &middot; Reviewed by Sam Chung (05/24/2025) &middot; Reviewed by Clark Ngo (12/04/2025)"],
        ),
        std_before_you_start(),
        std_readings(),
        "    <h2>Learning Outcomes</h2>\n    <ul>\n      <li>Section 1: Creating a Static Website</li>\n      <li>Section 2: Conducting CI/CD Pipeline Integration</li>\n      <li>Section 3: Cleaning Up Resources</li>\n      <li>Section 4: Pushing Your Work to GitHub</li>\n    </ul>\n\n",
        "    <h2>Upload screenshots</h2>\n    <ol>\n"
        '      <li><span class="hos-cmd">01_push_index_…</span></li>\n'
        '      <li><span class="hos-cmd">02_hello_…</span></li>\n'
        '      <li><span class="hos-cmd">03_hello_world_…</span></li>\n'
        "    </ol>\n\n",
        "    <h2>Key Concepts</h2>\n    <p><strong>CI/CD</strong> automates build, test, and deploy. This lab uses <strong>GitHub Actions</strong> with <strong>Azure Static Web Apps</strong> (per PDF resources).</p>\n\n",
        "    <h2>Section 1: Static website</h2>\n    <p>Author <span class=\"hos-cmd\">index.html</span> and related static assets in the repo.</p>\n\n",
        "    <h2>Section 2: Pipeline</h2>\n    <p>Configure workflow YAML, connect Azure SWA, verify staging/production URLs and hello pages.</p>\n\n",
        "    <h2>Section 3: Cleanup</h2>\n    <p>Remove or scale down cloud resources per instructions to avoid charges.</p>\n\n",
        all_figs_grid("hos08-pdf-figures", "Figures from PDF"),
        "    <h2>Section 4: Pushing Your Work to GitHub</h2>\n    <p>Ensure workflow + site evidence are committed.</p>\n",
        full_pdf_text_append("08"),
        close_section(),
    ]
    return "".join(p)


def handout_09() -> str:
    p = [
        open_section(
            "HOS09A",
            "HOS09A &mdash; Microservices (Azure Functions)",
            ["Ajay Naik (05/21/2023) &middot; Kina Anh Bui (05/30/2025) &middot; Reviewed by Clark Ngo &amp; Sam Chung"],
        ),
        std_before_you_start(),
        "    <h2>Learning Outcomes</h2>\n    <ul>\n      <li>Section 1: Azure Function</li>\n      <li>Section 2: Pushing Your Work to GitHub</li>\n    </ul>\n\n",
        '    <h2>Upload</h2>\n    <p><span class="hos-cmd">01_daysbetween_firstname_lastname.png</span></p>\n\n',
        "    <h2>Key Concepts</h2>\n    <p><strong>Azure Functions</strong> provide serverless, event-driven endpoints; local dev uses the <strong>Azure Functions</strong> and <strong>Azurite</strong> VS Code extensions.</p>\n\n",
        "    <h2>Section 1: Azure Function</h2>\n    <p>Install extensions, scaffold the Python function project, run locally with Azurite, invoke the HTTP trigger (e.g., <em>daysbetween</em>), optionally deploy.</p>\n\n",
        all_figs_grid("hos09-pdf-figures", "Figures from PDF"),
        "    <h2>Section 2: Pushing Your Work to GitHub</h2>\n    <p>Push sources and screenshot.</p>\n",
        full_pdf_text_append("09"),
        close_section(),
    ]
    return "".join(p)


def handout_10() -> str:
    p = [
        open_section(
            "HOS10A",
            "HOS10A &mdash; Advanced Microservices (AWS Lambda)",
            ["Ajay Naik (05/30/2023) &middot; Revised by Kina Anh Bui (06/06/2025) &middot; Reviewed by Sam Chung (06/06/2025) &middot; Clark Ngo (12/05/2025)"],
        ),
        std_before_you_start(),
        "    <h2>Learning Outcomes</h2>\n    <ul>\n      <li>Section 1: Create AWS Lambda Function</li>\n      <li>Section 2: Pushing Your Work to GitHub</li>\n    </ul>\n\n",
        "    <h2>Upload screenshots</h2>\n    <ol>\n"
        '      <li><span class="hos-cmd">01_test_…</span></li>\n'
        '      <li><span class="hos-cmd">02_delete_…</span></li>\n'
        "    </ol>\n\n",
        "    <p class=\"hos-pdf-note\">PDF section heading may say &ldquo;Azure Function&rdquo;; steps and figures reference <strong>AWS Lambda</strong> and the AWS console.</p>\n\n",
        "    <h2>Key Concepts</h2>\n    <p><strong>AWS Lambda</strong> runs handler code on managed infrastructure; use <strong>Free Tier</strong> guardrails from the PDF.</p>\n\n",
        "    <h2>Section 1: AWS Lambda</h2>\n    <p>Sign in, create a function, paste <span class=\"hos-cmd\">lambda_function.py</span>, configure test/API events, capture screenshots, clean up resources.</p>\n\n",
        all_figs_grid("hos10-pdf-figures", "Figures from PDF"),
        "    <h2>Section 2: Pushing Your Work to GitHub</h2>\n    <p>Push repository work per instructions.</p>\n",
        full_pdf_text_append("10"),
        close_section(),
    ]
    return "".join(p)


HANDLERS = {
    "03": handout_03,
    "04": handout_04,
    "05": handout_05,
    "06": handout_06,
    "07": handout_07,
    "08": handout_08,
    "09": handout_09,
    "10": handout_10,
}


def strip_verbatim_css(html: str) -> str:
    return re.sub(
        r"\n    \.hos-pdf-verbatim-details \{[^}]+\}\n    \.hos-pdf-sum \{[^}]+\}\n    \.hos-pdf-full-raw \{[^}]+\}\n    \.hos-pdf-fig-h \{[^}]+\}\n    \.hos-pdf-fig-all-grid \{[^}]+\}\n",
        "\n",
        html,
        count=1,
    )


def ensure_note_css(html: str) -> str:
    if ".hos-pdf-note" in html:
        return html
    return html.replace(
        ".hos-pdf-source p { margin: .45rem 0; }",
        ".hos-pdf-source p { margin: .45rem 0; }\n    .hos-pdf-source .hos-pdf-note { font-size: .82rem; color: #8b949e; margin: .35rem 0 .75rem; }",
    )


def splice_file(mid: str) -> None:
    path = TARGETS[mid]
    text = path.read_text(encoding="utf-8")
    hos = f"HOS{mid}A"
    start = text.index(f"  <!-- Complete {hos} handout")
    end = text.index('  <div class="why-section">')
    new = text[:start] + HANDLERS[mid]() + "  <!-- Why & Purpose -->\n" + text[end:]
    new = new.replace(
        "<strong>The objective:</strong> Sequence the &lt;strong&gt;seven steps&lt;/strong&gt;",
        "<strong>The objective:</strong> Sequence the <strong>seven steps</strong>",
    )
    new = re.sub(
        r'<p style="margin-top:\.65rem[^>]*>.*?</p>',
        LAB_INTRO,
        new,
        count=1,
    )
    new = strip_verbatim_css(new)
    new = new.replace(
        "    /* HOS01A full handout (verbatim structure from PDF) */",
        f"    /* HOS{mid}A full handout (curated like HOS01) */",
    )
    new = ensure_note_css(new)
    new = inject_verbatim_styles(new)
    path.write_text(new, encoding="utf-8")
    print("Updated", path.name)


def main() -> None:
    for mid in ("03", "04", "05", "06", "07", "08", "09", "10"):
        splice_file(mid)


if __name__ == "__main__":
    main()
