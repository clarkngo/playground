#!/usr/bin/env python3
"""
Generate HOS02A–HOS10A activity HTML pages from PDFs (same shell as 01).
Run from repo: python3 hos/dev-foundations-activities-hos/generate_hos_02_10.py
"""
from __future__ import annotations

import glob
import html
import json
import os
import re

BASE = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.expanduser("~/Downloads/cs445-hos")
EXTRACT_TXT = os.path.join(BASE, "_pdf_extracts")
TEMPLATE = os.path.join(BASE, "01-github-codespaces-hos-workflow.html")

MODULES = [
    {
        "id": "02",
        "slug": "02-git-repositories-refactoring-hos-workflow",
        "pdf_file": "HOS02A - Git Repositories and Refactoring.pdf",
        "hos": "HOS02A",
        "title": "Git Repositories and Refactoring",
        "badge": "CS445 HOS02A &mdash; Git in Codespaces",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS02A Git",
        "storage_key": "dfa-hos02a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below, then the interactive sequence. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace (in-repo)"),
            ("GitBranch", "git checkout -b feature branch"),
            ("GitStatus", "git status (review changes)"),
            ("GitAdd", "git add (stage files)"),
            ("GitCommit", "git commit -m \"message\""),
            ("GitPush", "git push origin branch"),
            ("GitPullSubmit", "git pull / push &mdash; sync &amp; submit"),
        ],
        "distractors": [
            ("DebugFirst", "Start debugger before staging files"),
            ("ForceMain", "git push --force to main only"),
            ("SkipAdd", "git commit without git add"),
            ("FtpUpload", "Upload ZIP via FTP instead of git"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: open the Codespace; you are already in the clone (Section 1).",
            "GitBranch": "Step 2: create/switch to a feature branch to isolate work (screenshot 01).",
            "GitStatus": "Step 3: run git status to see modified/untracked files before staging.",
            "GitAdd": "Step 4: stage changes with git add before committing.",
            "GitCommit": "Step 5: commit with a message to save local history.",
            "GitPush": "Step 6: push your branch to GitHub so the remote has your commits.",
            "GitPullSubmit": "Step 7: pull remote updates if needed, then submit per Classroom (Section 4).",
        },
        "passMessage": "HOS02A workflow verified: Codespace, branch, status, add, commit, push, then sync/submit.",
        "sim_good_key": "gitflow",
        "sim_bad_key": "commitempty",
        "sim_title": "Git staging path vs empty commit",
        "sim_sub": "Panel A: status &rarr; add &rarr; commit &rarr; push. Panel B: committing with nothing staged fails or warns.",
        "sim_label_a": "Happy git path",
        "sim_label_b": "Commit without staged files",
        "why": [
            ("green", "Feature branches", "Isolate work with git checkout -b so main stays stable; merge via PR in the PDF."),
            ("blue", "Staging matters", "git add selects what goes into the next commit; git status shows the pipeline."),
            ("yellow", "Codespaces + Git", "Terminal has Git preinstalled; no separate clone when opening the assignment repo."),
            ("purple", "Your goal", "Follow the screenshot order: branch, list branches, status, add, commit, push, pull, tooling."),
        ],
        "scenario": "Sequence the <strong>seven steps</strong> of the HOS02A Git cookbook: open the workspace, branch, inspect status, stage, commit, push to GitHub, then sync/submit. Decoys include wrong Git hygiene.",
        "prompts": (
            "Why must <strong>git add</strong> come before <strong>git commit</strong> in this lab?",
            "When do you use <strong>git pull</strong> versus <strong>git push</strong> with origin?",
        ),
    },
    {
        "id": "03",
        "slug": "03-flask-rest-api-hos-workflow",
        "pdf_file": "HOS03A - Restful API using Flask.pdf",
        "hos": "HOS03A",
        "title": "RESTful API using Flask",
        "badge": "CS445 HOS03A &mdash; Flask REST",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS03A Flask",
        "storage_key": "dfa-hos03a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("PipFlask", "pip install Flask"),
            ("PipRestful", "pip install Flask-RESTful"),
            ("BuildApp", "Implement app.py / CRUD resources"),
            ("RunTest", "Run API &amp; test endpoints"),
            ("Screenshots", "Capture required screenshots"),
            ("GitPush", "git push (submit to GitHub)"),
        ],
        "distractors": [
            ("DjangoFirst", "Start with Django admin only"),
            ("NoVenv", "Skip Python environment setup"),
            ("SqlOnly", "Write only raw SQL files"),
            ("PostmanBefore", "Install Postman before Flask"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Section 1 &mdash; open the Codespace for the assignment repo.",
            "PipFlask": "Step 2: install Flask (screenshot 01).",
            "PipRestful": "Step 3: install Flask-RESTful (screenshot 02).",
            "BuildApp": "Step 4: Section 2 &mdash; build the microservice with REST resources.",
            "RunTest": "Step 5: Section 3 &mdash; test CRUD operations (Postman/curl).",
            "Screenshots": "Step 6: capture Hello World, body, retrieve, delete screenshots per PDF.",
            "GitPush": "Step 7: Section 4 &mdash; push your work to GitHub.",
        },
        "passMessage": "HOS03A workflow verified: Codespace, Flask stack, implement CRUD, test, document with screenshots, push.",
        "sim_good_key": "flaskok",
        "sim_bad_key": "flaskimport",
        "sim_title": "Flask app boots vs import error",
        "sim_sub": "Panel A: Flask + resources respond 200. Panel B: missing Flask package or bad import.",
        "sim_label_a": "REST handler OK",
        "sim_label_b": "ModuleNotFoundError",
        "why": [
            ("green", "REST basics", "Resources map to HTTP verbs; Flask-RESTful structures CRUD cleanly."),
            ("blue", "Microservice", "Small focused service matches the PDF microservice section."),
            ("yellow", "Testing", "Verify GET/POST/DELETE before declaring done."),
            ("purple", "Goal", "Install deps, code app, test, screenshot, push."),
        ],
        "scenario": "Order the HOS03A steps from environment setup through submission. Dependencies before application code; tests before final git push.",
        "prompts": (
            "What makes an API <strong>RESTful</strong> in this lab?",
            "How do Flask and Flask-RESTful differ in responsibility?",
        ),
    },
    {
        "id": "04",
        "slug": "04-databases-mysql-hos-workflow",
        "pdf_file": "HOS04A - Databases.pdf",
        "pdf_file_alt": "HOS04A - Databases - without Docker.pdf",
        "hos": "HOS04A",
        "title": "Databases (MySQL + Adminer)",
        "badge": "CS445 HOS04A &mdash; Databases",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS04A DB",
        "storage_key": "dfa-hos04a-canvas",
        "lab_intro": "Merged cookbook text from both HOS04A PDFs (Docker and without-Docker variants) is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("DockerMySQL", "Start MySQL / stack (Docker)"),
            ("AdminerLogin", "Open Adminer &amp; log in"),
            ("SqlCreate", "CREATE database/table"),
            ("CrudOps", "INSERT / READ / UPDATE / DELETE"),
            ("Screenshots", "Screenshot each CRUD step"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("MongoOnly", "Use MongoDB only, skip SQL"),
            ("NoDocker", "Run MySQL on host OS without container"),
            ("DropDbFirst", "DROP DATABASE before CREATE"),
            ("SkipAdminer", "Use only CLI mysql forever"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Section 1 &mdash; Codespace with assignment repo.",
            "DockerMySQL": "Step 2: Section 2 &mdash; MySQL in Docker per PDF (image/Dockerfile).",
            "AdminerLogin": "Step 3: log into Adminer web UI (screenshot 01 login, 02 dbe).",
            "SqlCreate": "Step 4: CREATE schema/table as instructed.",
            "CrudOps": "Step 5: run INSERT, READ, UPDATE, DELETE operations.",
            "Screenshots": "Step 6: capture 03&ndash;07 screenshots.",
            "GitPush": "Step 7: Section 4 &mdash; push to GitHub.",
        },
        "passMessage": "HOS04A workflow verified: bring up DB stack, Adminer, SQL DDL/DML, screenshots, push.",
        "sim_good_key": "dbup",
        "sim_bad_key": "dbdown",
        "sim_title": "DB port reachable vs connection refused",
        "sim_sub": "Panel A: container listening 3306. Panel B: client fires before server ready.",
        "sim_label_a": "MySQL accepting",
        "sim_label_b": "Connection refused",
        "why": [
            ("green", "Containers", "Dockerfile bundles Python + MySQL + Adminer per key concepts."),
            ("blue", "CRUD", "Relational ops map to SQL statements in the lab."),
            ("yellow", "Adminer", "Web UI speeds verification vs raw mysql client only."),
            ("purple", "Goal", "Login, create data, prove CRUD, submit artifacts."),
        ],
        "scenario": "Sequence database lab steps: environment, running data tier, Adminer access, SQL work, evidence, git push.",
        "prompts": (
            "Why use <strong>Adminer</strong> alongside MySQL for this assignment?",
            "How does <strong>CREATE</strong> differ from <strong>INSERT</strong> here?",
        ),
    },
    {
        "id": "05",
        "slug": "05-unit-testing-hos-workflow",
        "pdf_file": "HOS05A - Unit Testing.pdf",
        "hos": "HOS05A",
        "title": "Unit Testing",
        "badge": "CS445 HOS05A &mdash; Unit tests",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS05A Tests",
        "storage_key": "dfa-hos05a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("InstallPytest", "Install pytest / test deps"),
            ("WriteTests", "Write unit test modules"),
            ("RunPytest", "Run pytest (collect &amp; execute)"),
            ("Coverage", "Review coverage / failures"),
            ("FixRetest", "Fix code &amp; re-run tests"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("E2eOnly", "Only E2E browser tests, no units"),
            ("SkipAssert", "Tests without assertions"),
            ("ProdData", "Run tests against production DB"),
            ("ManualOnly", "Manual checklist replaces pytest"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: open Codespace for the repo.",
            "InstallPytest": "Step 2: install testing tools from the PDF.",
            "WriteTests": "Step 3: author test_*.py with assertions.",
            "RunPytest": "Step 4: execute pytest and read output.",
            "Coverage": "Step 5: interpret coverage or failure reports.",
            "FixRetest": "Step 6: iterate until green.",
            "GitPush": "Step 7: push passing suite + screenshots.",
        },
        "passMessage": "HOS05A workflow verified: tool setup, write tests, run, analyze, iterate, submit.",
        "sim_good_key": "testpass",
        "sim_bad_key": "testfail",
        "sim_title": "Green suite vs failing assertion",
        "sim_sub": "Panel A: tests pass. Panel B: assertion error stops the run.",
        "sim_label_a": "pytest OK",
        "sim_label_b": "AssertionError",
        "why": [
            ("green", "Fast feedback", "Unit tests catch regressions early."),
            ("blue", "Automation", "pytest collects tests deterministically."),
            ("yellow", "Quality", "Assertions document expected behavior."),
            ("purple", "Goal", "Install, write, run, fix, ship."),
        ],
        "scenario": "Order the unit-testing workflow: environment, dependencies, author tests, execute pytest, review results, iterate, push.",
        "prompts": (
            "What belongs in a <strong>unit</strong> test versus an integration test?",
            "How does pytest discover which functions to run?",
        ),
    },
    {
        "id": "06",
        "slug": "06-uml-visual-modeling-hos-workflow",
        "pdf_file": "HOS06A - UML Visual Modeling.pdf",
        "hos": "HOS06A",
        "title": "UML Visual Modeling",
        "badge": "CS445 HOS06A &mdash; UML",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS06A UML",
        "storage_key": "dfa-hos06a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("InstallTool", "Install modeling extension/tool"),
            ("AuthorModel", "Author UML diagrams"),
            ("Validate", "Validate / layout diagram"),
            ("Export", "Export or save artifacts"),
            ("DocReadme", "Attach to README / docs"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("WordArt", "Use only WordArt shapes"),
            ("NoLegend", "Skip legend and stereotypes"),
            ("RandomColors", "Colors with no semantics"),
            ("SkipReview", "Push without peer review"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Codespace for assignment.",
            "InstallTool": "Step 2: install PlantUML or PDF-specified VS Code tooling.",
            "AuthorModel": "Step 3: create class/sequence diagrams per lab.",
            "Validate": "Step 4: check syntax/errors in preview.",
            "Export": "Step 5: export PNG/SVG or save sources.",
            "DocReadme": "Step 6: link artifacts in repo docs.",
            "GitPush": "Step 7: push diagrams to GitHub.",
        },
        "passMessage": "HOS06A workflow verified: tool up, model, validate, export, document, push.",
        "sim_good_key": "umlok",
        "sim_bad_key": "umlerr",
        "sim_title": "Diagram renders vs syntax error",
        "sim_sub": "Panel A: PlantUML/Graphviz renders. Panel B: typo breaks parser.",
        "sim_label_a": "Render OK",
        "sim_label_b": "Parse error",
        "why": [
            ("green", "Communication", "UML aligns devs on structure and behavior."),
            ("blue", "Tooling", "Extensions automate layout and export."),
            ("yellow", "As-built", "Models should reflect code or planned design."),
            ("purple", "Goal", "Model, export, share in repo."),
        ],
        "scenario": "Sequence UML lab steps: open workspace, install visual tooling, author diagrams, validate, export, document, push.",
        "prompts": (
            "When do you use a <strong>class</strong> diagram versus a <strong>sequence</strong> diagram?",
            "How do stereotypes &laquo;interface&raquo; help readers?",
        ),
    },
    {
        "id": "07",
        "slug": "07-security-hos-workflow",
        "pdf_file": "HOS07A - Security.pdf",
        "hos": "HOS07A",
        "title": "Security",
        "badge": "CS445 HOS07A &mdash; Security",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS07A Security",
        "storage_key": "dfa-hos07a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("ThreatModel", "Identify threats / assets"),
            ("Controls", "Apply controls (auth, secrets, TLS)"),
            ("ScanDeps", "Scan dependencies / lint security"),
            ("HardenConfig", "Harden configuration"),
            ("Verify", "Verify mitigations / test"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("PlaintextPw", "Store passwords plaintext for debug"),
            ("DisableTls", "Disable TLS to go faster"),
            ("ShareKeys", "Commit AWS keys to main"),
            ("IgnoreCve", "Ignore all CVE alerts"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Codespace with assignment repo.",
            "ThreatModel": "Step 2: enumerate assets and attackers (per PDF).",
            "Controls": "Step 3: choose defenses: authentication, encryption, etc.",
            "ScanDeps": "Step 4: run security scanners on dependencies.",
            "HardenConfig": "Step 5: fix insecure defaults.",
            "Verify": "Step 6: retest / demonstrate mitigation.",
            "GitPush": "Step 7: push report and code changes.",
        },
        "passMessage": "HOS07A workflow verified: assess, control, scan, harden, verify, submit.",
        "sim_good_key": "secok",
        "sim_bad_key": "secleak",
        "sim_title": "Secrets in env vs committed .env",
        "sim_sub": "Panel A: secrets via environment. Panel B: key committed to git history.",
        "sim_label_a": "Secret via env",
        "sim_label_b": "Leak in repo",
        "why": [
            ("green", "Defense in depth", "Multiple layers reduce blast radius."),
            ("blue", "Automation", "Scanners catch known vulns early."),
            ("yellow", "Least privilege", "Limit access per assignment guidance."),
            ("purple", "Goal", "Model threats, implement controls, evidence, push."),
        ],
        "scenario": "Order the security cookbook: workspace, assess risk, implement controls, scan, harden, verify, submit.",
        "prompts": (
            "What is the difference between <strong>authentication</strong> and <strong>authorization</strong>?",
            "Why avoid committing API keys even in private repos?",
        ),
    },
    {
        "id": "08",
        "slug": "08-cicd-static-web-hos-workflow",
        "pdf_file": "HOS08A - CICD.pdf",
        "hos": "HOS08A",
        "title": "CI/CD (Static Web + pipeline)",
        "badge": "CS445 HOS08A &mdash; CI/CD",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS08A CI/CD",
        "storage_key": "dfa-hos08a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("StaticSite", "Author static site (index.html)"),
            ("GitPushBranch", "Push to GitHub (trigger CI)"),
            ("GitHubActions", "GitHub Actions workflow runs"),
            ("AzureSWA", "Azure Static Web Apps deploy"),
            ("VerifyLive", "Verify live URL / hello pages"),
            ("GitPushFinal", "Finalize &amp; document submission"),
        ],
        "distractors": [
            ("ManualFtp", "Manual FTP only, no CI"),
            ("SkipActions", "Delete workflow YAML"),
            ("ProdBranch", "Deploy straight from unreviewed branch"),
            ("NoStaging", "Skip staging slot always"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Codespace for static site sources.",
            "StaticSite": "Step 2: Section 1 &mdash; create static website files.",
            "GitPushBranch": "Step 3: push to GitHub to feed the pipeline.",
            "GitHubActions": "Step 4: Section 2 &mdash; CI/CD integration (Actions YAML).",
            "AzureSWA": "Step 5: deploy to Azure Static Web Apps per PDF.",
            "VerifyLive": "Step 6: hit hello / hello world URLs (screenshots).",
            "GitPushFinal": "Step 7: Section 4 &mdash; submit evidence to GitHub.",
        },
        "passMessage": "HOS08A workflow verified: static content, push, automated build/deploy, verify live site, submit.",
        "sim_good_key": "cicdok",
        "sim_bad_key": "cicdfail",
        "sim_title": "Green pipeline vs failed workflow",
        "sim_sub": "Panel A: Actions success then SWA deploy. Panel B: YAML error fails build.",
        "sim_label_a": "Pipeline green",
        "sim_label_b": "Workflow failed",
        "why": [
            ("green", "Automation", "CI/CD removes manual deploy toil."),
            ("blue", "GitHub Actions", "YAML workflows live with code."),
            ("yellow", "Static Web Apps", "CDN-hosted frontends integrate with Git."),
            ("purple", "Goal", "Push triggers build; verify production URL."),
        ],
        "scenario": "Order CI/CD lab steps: author site, push source, let Actions run, deploy to Azure SWA, verify, submit screenshots.",
        "prompts": (
            "What is the difference between <strong>CI</strong> and <strong>CD</strong> in this lab?",
            "Why tie deployment to a Git push?",
        ),
    },
    {
        "id": "09",
        "slug": "09-microservices-azure-functions-hos-workflow",
        "pdf_file": "HOS09A - Microservices.pdf",
        "hos": "HOS09A",
        "title": "Microservices (Azure Functions)",
        "badge": "CS445 HOS09A &mdash; Azure Functions",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS09A Microservices",
        "storage_key": "dfa-hos09a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC.",
        "toolData": [
            ("OpenCodespace", "Open GitHub Codespace"),
            ("InstallAzExt", "Install Azure Functions + Azurite extensions"),
            ("ScaffoldFunc", "Scaffold / configure Azure Function"),
            ("LocalRun", "Run locally with Azurite"),
            ("TestHttp", "Test HTTP trigger / daysbetween"),
            ("DeployAzure", "Deploy to Azure (if required)"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("LambdaOnAzure", "Confuse with AWS Lambda only"),
            ("NoStorage", "Skip storage emulator entirely"),
            ("HardcodeKeys", "Hardcode subscription keys in repo"),
            ("SkipPython", "Use unsupported runtime"),
        ],
        "clues": {
            "OpenCodespace": "Step 1: Codespace with prerequisites (PDF lists VS Code extensions).",
            "InstallAzExt": "Step 2: install Azure Functions + Azurite extensions.",
            "ScaffoldFunc": "Step 3: create function project per Section 1.",
            "LocalRun": "Step 4: run locally using Azurite storage emulator.",
            "TestHttp": "Step 5: exercise HTTP function (screenshot 01 daysbetween).",
            "DeployAzure": "Step 6: deploy to Azure subscription when instructed.",
            "GitPush": "Step 7: Section 2 &mdash; push work to GitHub.",
        },
        "passMessage": "HOS09A workflow verified: extensions, scaffold, local run with Azurite, test, deploy, push.",
        "sim_good_key": "azok",
        "sim_bad_key": "azfail",
        "sim_title": "Function host starts vs missing storage",
        "sim_sub": "Panel A: Azurite + host running. Panel B: storage emulator not started.",
        "sim_label_a": "Host + Azurite",
        "sim_label_b": "Storage offline",
        "why": [
            ("green", "Serverless", "Azure Functions scale automatically; you ship handlers."),
            ("blue", "Event-driven", "HTTP triggers map to microservice endpoints."),
            ("yellow", "Local dev", "Azurite mimics cloud storage offline."),
            ("purple", "Goal", "Configure, test locally, deploy, submit."),
        ],
        "scenario": "Order Azure Functions lab: Codespace, extensions, function code, local test with Azurite, verify HTTP, deploy, git push.",
        "prompts": (
            "How do Azure Functions relate to <strong>microservices</strong>?",
            "Why run <strong>Azurite</strong> during development?",
        ),
    },
    {
        "id": "10",
        "slug": "10-advanced-microservices-aws-lambda-hos-workflow",
        "pdf_file": "HOS10A - Advanced Microservices.pdf",
        "hos": "HOS10A",
        "title": "Advanced Microservices (AWS Lambda)",
        "badge": "CS445 HOS10A &mdash; AWS Lambda",
        "nav_pill": "Dev Foundations (HOS) &rsaquo; HOS10A Advanced",
        "storage_key": "dfa-hos10a-canvas",
        "lab_intro": "Full cookbook text from the PDF is below. CS445 Software Process Management &mdash; CityU STC. (PDF Section 1 heading says Azure Function; content is AWS Lambda.)",
        "toolData": [
            ("AwsAccount", "AWS account / sign in (Free Tier)"),
            ("CreateLambda", "Create Lambda function in console"),
            ("PasteCode", "Paste lambda_function.py code"),
            ("ConfigureTest", "Configure test event / API"),
            ("InvokeTest", "Invoke test &amp; capture screenshot"),
            ("Iterate", "Iterate delete/test per PDF"),
            ("GitPush", "git push (submit)"),
        ],
        "distractors": [
            ("GcpOnly", "Use only Google Cloud Run"),
            ("RootKeys", "Use root account keys in code"),
            ("PublicBucket", "Make S3 bucket world-writable"),
            ("SkipIam", "Use * wildcard on all IAM roles"),
        ],
        "clues": {
            "AwsAccount": "Step 1: PDF &mdash; AWS sign-in / Free Tier note.",
            "CreateLambda": "Step 2: search Lambda, create function with runtime settings.",
            "PasteCode": "Step 3: paste leap-year sample into lambda_function.py.",
            "ConfigureTest": "Step 4: configure query params / API per instructions.",
            "InvokeTest": "Step 5: run test (screenshot 01 Test).",
            "Iterate": "Step 6: delete or adjust resources (screenshot 02 Delete).",
            "GitPush": "Step 7: Section 2 &mdash; push repository work.",
        },
        "passMessage": "HOS10A workflow verified: AWS console, Lambda author, test invoke, cleanup, submit.",
        "sim_good_key": "lambdaok",
        "sim_bad_key": "lambdaerr",
        "sim_title": "200 OK invoke vs handler exception",
        "sim_sub": "Panel A: Lambda returns JSON body. Panel B: Python exception in handler.",
        "sim_label_a": "Invoke success",
        "sim_label_b": "Runtime error",
        "why": [
            ("green", "Managed runtime", "AWS runs your handler without VMs to patch."),
            ("blue", "Pay per use", "Good fit for bursty class workloads on Free Tier."),
            ("yellow", "HTTP front door", "API Gateway can expose Lambda (per course extensions)."),
            ("purple", "Goal", "Create, code, test, tear down responsibly, push repo."),
        ],
        "scenario": "Order AWS Lambda lab: account access, create function, implement handler, configure test, invoke, cleanup, git push.",
        "prompts": (
            "What is inside the <strong>event</strong> object for an HTTP API Lambda?",
            "Why use <strong>Free Tier</strong> guardrails in class?",
        ),
    },
]


def extract_images(pdf_path: str, out_dir: str) -> None:
    os.makedirs(out_dir, exist_ok=True)
    import fitz

    doc = fitz.open(pdf_path)
    idx = 0
    for pno in range(len(doc)):
        page = doc[pno]
        for img in page.get_images(full=True):
            xref = img[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha > 3:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                fname = "p%02d_fig%d.png" % (pno + 1, idx)
                pix.save(os.path.join(out_dir, fname))
                idx += 1
                pix = None
            except Exception:
                pass
    doc.close()


def pdf_text_all_pages(pdf_path: str) -> str:
    import fitz

    doc = fitz.open(pdf_path)
    try:
        return "\n\n".join(page.get_text() for page in doc)
    finally:
        doc.close()


def _figure_grid_html(fig_dir_rel: str) -> str:
    figs = sorted(glob.glob(os.path.join(BASE, fig_dir_rel, "*.png")))
    parts = []
    for fn in figs:
        bn = os.path.basename(fn)
        parts.append(
            '<div class="hos-pdf-fig-wrap"><img class="hos-pdf-fig" src="%s/%s" loading="lazy" decoding="async" alt="Figure %s from PDF"/>'
            '<div class="hos-pdf-fig-cap">%s</div></div>'
            % (fig_dir_rel, bn, html.escape(bn), html.escape(bn))
        )
    return (
        '<div class="hos-pdf-fig-all-grid">\n%s\n</div>' % "\n".join(parts)
        if parts
        else "<p>No figures extracted.</p>"
    )


def build_handout(
    hos: str,
    full_text: str,
    fig_dir_rel: str,
    *,
    alt_text: str | None = None,
    alt_fig_dir_rel: str | None = None,
) -> str:
    esc = html.escape(full_text)
    grid = _figure_grid_html(fig_dir_rel)

    alt_block = ""
    if alt_text is not None and alt_text.strip():
        alt_esc = html.escape(alt_text)
        alt_grid = _figure_grid_html(alt_fig_dir_rel) if alt_fig_dir_rel else "<p>No alternate figure folder.</p>"
        alt_block = (
            '    <details class="hos-pdf-verbatim-details">\n'
            "      <summary class=\"hos-pdf-sum\">Complete document text &mdash; without Docker variant (extracted)</summary>\n"
            '      <pre class="hos-pdf-full-raw">%s</pre>\n'
            "    </details>\n"
            '    <h3 class="hos-pdf-fig-h">Figures from PDF (without Docker variant)</h3>\n'
            "    %s\n"
        ) % (alt_esc, alt_grid)

    if alt_block:
        meta = (
            "Below: <strong>full plain-text extraction</strong> from the primary PDF, merged with the "
            "<strong>without-Docker</strong> variant, followed by <strong>extractable images</strong> from each. "
            "If layout differs, defer to the original PDFs."
        )
        fig_h3_primary = '    <h3 class="hos-pdf-fig-h">Figures from PDF (Docker / primary handout)</h3>\n'
    else:
        meta = (
            "Below: <strong>full plain-text extraction</strong> from the official PDF, followed by "
            "<strong>all extractable images</strong> embedded in reading order. If layout differs, defer to the original PDF."
        )
        fig_h3_primary = '    <h3 class="hos-pdf-fig-h">Figures from PDF</h3>\n'

    return (
        '  <!-- Complete %s handout (generated: PDF text + figures) -->\n'
        '  <section class="hos-pdf-source" aria-label="%s full handout">\n'
        '    <div class="hos-kicker">%s &mdash; complete PDF content</div>\n'
        "    <p class=\"hos-pdf-meta\">%s</p>\n"
        '    <details open class="hos-pdf-verbatim-details">\n'
        '      <summary class="hos-pdf-sum">Complete document text (extracted)</summary>\n'
        '      <pre class="hos-pdf-full-raw">%s</pre>\n'
        "    </details>\n"
        "%s"
        "    %s\n"
        "%s"
        "  </section>\n"
    ) % (hos, hos, hos, meta, esc, fig_h3_primary, grid, alt_block)


def sim_js(m: dict) -> str:
    gk, bk = m["sim_good_key"], m["sim_bad_key"]
    return (
        """  var SIM_SCENARIOS = {
    %s: {
      phases: ["Step 1", "Step 2", "Step 3", "Done"],
      nodes: [
        { i: "&#127760;", l: "Workspace" },
        { i: "&#9881;&#65039;", l: "Tooling" },
        { i: "&#9989;", l: "Verify" },
        { i: "&#8593;", l: "Ship" }
      ],
      steps: [
        { d: 0, ph: 0, log: ["info",  "> Context ready..."] },
        { d: 900, ph: 1, log: ["blue",  "> Primary action succeeds"], fc: 0 },
        { d: 1800, ph: 2, log: ["ok",    "> Checks pass"], fc: 1 },
        { d: 2700, ph: 3, log: ["ok",    "> Ready to submit"], fc: 2 },
        { d: 4000, ph: 3, log: ["ok",    "&#9650; Happy path matches PDF order"], final: true }
      ],
      result: "<strong>Happy path:</strong> Follow the handout sequence; complete each gate before moving on."
    },
    %s: {
      phases: ["Risk", "Block", "Fix", "Retry"],
      nodes: [
        { i: "&#9888;", l: "Issue" },
        { i: "&#10060;", l: "Blocked" },
        { i: "&#128295;", l: "Fix" },
        { i: "&#9989;", l: "OK" }
      ],
      steps: [
        { d: 0, ph: 0, log: ["warn",  "> Preconditions not met..."] },
        { d: 900, ph: 1, log: ["warn",  "> Step fails fast"], fc: 0 },
        { d: 1800, ph: 2, log: ["info",  "> Correct the issue (see PDF troubleshooting)"] },
        { d: 2700, ph: 3, log: ["ok",    "> Retry succeeds"], fc: 2 },
        { d: 4000, ph: 3, log: ["warn",  "&#9660; Anti-pattern: skipping a required step"], final: true }
      ],
      result: "<strong>Blocked path:</strong> The PDF expects prerequisites and ordering; fix the failing step before continuing."
    }
  };
"""
        % (gk, bk)
    )


def esc_html_body(s: str) -> str:
    """Escape for HTML body; avoids &amp;amp; when MODULES strings already use entities."""
    return html.escape(html.unescape(s))


def ref_html(m: dict) -> str:
    rows = []
    icons = ("&#127760;", "&#128295;", "&#128230;", "&#9889;", "&#128640;", "&#128194;", "&#8593;")
    for i, (t, label) in enumerate(m["toolData"]):
        ic = icons[i % len(icons)]
        clue = m["clues"].get(t, "")
        rows.append(
            '<div class="ref-item"><div class="ref-item-name"><span class="ref-icon">%s</span>%s</div>'
            '<div class="ref-item-desc">%s<div class="ref-item-hint">&#128161; From HOS PDF sequence.</div></div></div>'
            % (ic, esc_html_body(label), esc_html_body(clue))
        )
    for t, label in m["distractors"]:
        rows.append(
            '<div class="ref-item"><div class="ref-item-name"><span class="ref-icon">&#9888;</span>%s (decoy)</div>'
            '<div class="ref-item-desc">Not part of the canonical seven-step spine for this lab.</div></div>'
            % esc_html_body(label)
        )
    body = "\n".join(rows)
    return (
        '  <div class="ref-section no-pdf">\n'
        '    <div class="ref-header" onclick="toggleRef(this)">\n'
        "      <div>\n"
        '        <div class="ref-header-title">&#128196; Step reference (%s)</div>\n'
        '        <div class="ref-header-sub">Click to expand &mdash; draggable steps</div>\n'
        "      </div>\n"
        '      <span class="ref-toggle">&#9660;</span>\n'
        "    </div>\n"
        '    <div class="ref-body">\n%s\n    </div>\n  </div>\n'
    ) % (m["hos"], body)


def why_html(m: dict) -> str:
    cards = []
    for wclass, title, txt in m["why"]:
        cards.append(
            '<div class="why-card"><div class="why-card-label %s">%s</div><p>%s</p></div>'
            % (html.escape(wclass), html.escape(title), html.escape(txt))
        )
    return (
        '  <div class="why-section">\n    <div class="why-section-title">Why This Matters</div>\n'
        '    <div class="why-grid">\n      %s\n    </div>\n  </div>\n'
    ) % "\n      ".join(cards)


def main() -> None:
    with open(TEMPLATE, "r", encoding="utf-8") as f:
        template = f.read()

    mid_style_inject = """
    .hos-pdf-verbatim-details { margin: 1rem 0; }
    .hos-pdf-sum { cursor: pointer; color: #58a6ff; font-weight: 700; font-size: .85rem; }
    .hos-pdf-full-raw {
      max-height: 70vh;
      overflow: auto;
      background: #0d1117;
      border: 1px solid #30363d;
      border-radius: 8px;
      padding: 1rem;
      font-size: .72rem;
      line-height: 1.45;
      color: #c9d1d9;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .hos-pdf-fig-h { font-size: .9rem; color: #58a6ff; margin: 1.25rem 0 0.5rem; }
    .hos-pdf-fig-all-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
      gap: 0.75rem;
      margin-top: 0.5rem;
    }
"""

    for m in MODULES:
        # HOS02A–HOS10A curated handouts (HOS01-style HTML); do not overwrite with generated <pre> dumps.
        if m["id"] in ("02", "03", "04", "05", "06", "07", "08", "09", "10"):
            print(
                "Skip HOS%sA (curated handout) — use build_hos02_curated_handout.py or build_hos_curated_03_10.py"
                % m["id"]
            )
            continue

        pdf_path = os.path.join(PDF_DIR, m["pdf_file"])
        if not os.path.isfile(pdf_path):
            raise SystemExit("Missing PDF: " + pdf_path)
        fig_dir = "hos%s-pdf-figures" % m["id"]
        extract_images(pdf_path, os.path.join(BASE, fig_dir))

        with open(os.path.join(EXTRACT_TXT, "hos%s_full.txt" % m["id"]), "r", encoding="utf-8") as f:
            full_text = f.read()

        alt_text = None
        alt_fig_rel = None
        if m.get("pdf_file_alt"):
            alt_pdf = os.path.join(PDF_DIR, m["pdf_file_alt"])
            if not os.path.isfile(alt_pdf):
                raise SystemExit("Missing alternate PDF: " + alt_pdf)
            alt_fig_rel = "hos%sb-pdf-figures" % m["id"]
            extract_images(alt_pdf, os.path.join(BASE, alt_fig_rel))
            alt_text = pdf_text_all_pages(alt_pdf)

        handout = build_handout(
            m["hos"], full_text, fig_dir, alt_text=alt_text, alt_fig_dir_rel=alt_fig_rel
        )

        t = template
        if "hos-pdf-full-raw" not in t:
            t = t.replace("</style>", mid_style_inject + "\n  </style>", 1)

        # Slice anchors must be computed on `t` after optional CSS inject — inject shifts all body indices.
        start = t.index("  <!-- Complete HOS01A handout")
        end = t.index("  <!-- Why & Purpose -->")
        t = t[:start] + handout + t[end:]

        # why section replace: find <!-- Why & Purpose --> through closing </div> of why-section
        w0 = t.index("  <!-- Why & Purpose -->")
        w1 = t.index("  <!-- Simulator -->", w0)
        t = t[:w0] + why_html(m) + t[w1:]

        # Simulator titles
        t = re.sub(
            r'<div class="sim-title">.*?</div>\s*<div class="sim-sub">.*?</div>',
            '<div class="sim-title">&#128187; %s</div>\n    <div class="sim-sub">%s</div>'
            % (m["sim_title"].replace("&", "&amp;"), m["sim_sub"].replace("&", "&amp;")),
            t,
            count=1,
            flags=re.DOTALL,
        )
        t = t.replace("Codespaces + Docker (happy path)", m["sim_label_a"])
        t = t.replace("docker build without Dockerfile", m["sim_label_b"])
        t = t.replace("runSimulator('codespace','a')", "runSimulator('%s','a')" % m["sim_good_key"])
        t = t.replace("runSimulator('badbuild','b')", "runSimulator('%s','b')" % m["sim_bad_key"])

        # Scenario
        scen = (
            '  <!-- Scenario -->\n'
            '  <div class="scenario-box">\n    <strong>The objective:</strong> %s<br><br>\n'
            "    <strong>Think about:</strong> Follow the PDF learning outcomes; decoys are out of order or out of scope.\n  </div>\n"
        ) % html.escape(m["scenario"])
        s0 = t.index("  <!-- Scenario -->")
        s1 = t.index("  <!-- Component Reference -->", s0)
        t = t[:s0] + scen + t[s1:]

        # Ref section
        r0 = t.index("  <!-- Component Reference -->")
        r1 = t.index("  <!-- Main layout -->", r0)
        t = t[:r0] + ref_html(m) + t[r1:]

        # Nav pill
        t = re.sub(
            r'<span class="nav-pill">.*?</span>',
            '<span class="nav-pill">%s</span>' % m["nav_pill"],
            t,
            count=1,
        )
        t = re.sub(
            r"<title>.*?</title>",
            "<title>Dev Foundations (HOS) | %s — %s</title>" % (m["hos"], html.escape(m["title"])),
            t,
            count=1,
        )
        t = re.sub(
            r'<span class="lab-badge">.*?</span>\s*<h1>.*?</h1>',
            '<span class="lab-badge">%s</span>\n    <h1>%s</h1>'
            % (m["badge"], html.escape(m["title"])),
            t,
            count=1,
            flags=re.DOTALL,
        )
        intro = '<p style="margin-top:.65rem;font-size:.88rem;color:#8b949e;line-height:1.55;max-width:820px;">%s</p>' % m[
            "lab_intro"
        ]
        t = re.sub(
            r'<p style="margin-top:\.65rem[^>]*>.*?</p>',
            intro,
            t,
            count=1,
        )

        # Prompts (keep HTML like <strong> inside prompt strings)
        p1, p2 = m["prompts"]
        # Must close last prompt-item, prompt-grid, and prompt-guide (three </div>), or a spare
        # prompt-guide </div> remains and duplicates when we insert the replacement block.
        t = re.sub(
            r"      <!-- AI prompts -->[\s\S]*?<div class=\"prompt-guide no-pdf\">[\s\S]*?</div>\s*</div>\s*</div>",
            "      <!-- AI prompts -->\n"
            '      <div class="prompt-guide no-pdf">\n'
            "        <div class=\"prompt-guide-title\">AI study prompts (%s)</div>\n"
            '        <div class="prompt-grid">\n'
            "          <div class=\"prompt-item\">%s</div>\n"
            "          <div class=\"prompt-item\">%s</div>\n"
            "        </div>\n"
            "      </div>"
            % (m["hos"], p1, p2),
            t,
            count=1,
        )

        # LAB_CONFIG + toolData + STORAGE_KEY + SIM_SCENARIOS block
        tool_lines = ",\n    ".join("{ type: %s, label: %s }" % (json.dumps(a), json.dumps(b)) for a, b in m["toolData"])
        dis_lines = ",\n    ".join("{ type: %s, label: %s }" % (json.dumps(a), json.dumps(b)) for a, b in m["distractors"])
        order = ",\n      ".join(json.dumps(x[0]) for x in m["toolData"])
        clue_lines = ",\n      ".join("%s: %s" % (json.dumps(k), json.dumps(v)) for k, v in m["clues"].items())

        lab_block = (
            "  const toolData = [\n    %s\n  ];\n\n  const distractors = [\n    %s\n  ];\n\n  const LAB_CONFIG = {\n"
            "    correctOrder: [\n      %s\n    ],\n    clues: {\n      %s\n    },\n    passMessage: %s\n  };\n"
        ) % (
            tool_lines,
            dis_lines,
            order,
            clue_lines,
            json.dumps(m["passMessage"]),
        )

        t = re.sub(
            r"  const toolData = \[[\s\S]*?  \};\n\n  function toggleRef",
            lab_block + "\n  function toggleRef",
            t,
            count=1,
        )

        t = t.replace('var STORAGE_KEY = "dfa-hos01a-canvas";', 'var STORAGE_KEY = "%s";' % m["storage_key"])

        t = re.sub(
            r"  var SIM_SCENARIOS = \{[\s\S]*?  \};\n\n  function _firePkt",
            sim_js(m) + "\n  function _firePkt",
            t,
            count=1,
        )

        t = t.replace(
            "// Correct-order steps (HOS01A cookbook spine)",
            "// Correct-order steps (%s cookbook spine)" % m["hos"],
        )

        out_path = os.path.join(BASE, m["slug"] + ".html")
        with open(out_path, "w", encoding="utf-8") as out:
            out.write(t)
        print("Wrote", out_path)


if __name__ == "__main__":
    main()
