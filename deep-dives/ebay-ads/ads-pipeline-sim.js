/**
 * eBay Ads — pipeline flow animations
 * (phase strip + packet dots on connectors + scrolling log)
 * Scenario pick: buttons only — no dropdowns.
 */
(function () {
  "use strict";

  const TECH = {
    rt: {
      title: "Real-time path",
      phases: ["Ingest", "Partition", "Stream", "Query"],
      nodes: [
        { icon: "📱", label: "Client" },
        { icon: "📨", label: "Kafka" },
        { icon: "⚡", label: "Flink" },
        { icon: "📊", label: "ClickHouse" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Ad click batch arriving at edge (JSON, 24 KB)…"] },
        { d: 450, ph: 0, log: ["warn", "> Key=seller_id → partition 7 of topic click-events"] },
        { d: 900, ph: 1, log: ["info", "> Consumer group ads-flink: offset commit lag 120 ms"], fc: 0 },
        { d: 1400, ph: 1, log: ["info", "> Watermark advanced — tumbling window 60 s closes"] },
        { d: 1900, ph: 2, log: ["warn", "> Stateful map: GMV partial sum keyed by placement_id"], fc: 1, hit: 2 },
        { d: 2500, ph: 2, log: ["info", "> Checkpoint barrier aligned — RocksDB snapshot OK"] },
        { d: 3000, ph: 3, log: ["ok", "> INSERT into ads_rt.metrics — 1 row, ReplacingMergeTree"], fc: 2, hit: 3 },
        { d: 3600, ph: 3, log: ["ok", "> Dashboard query p99 &lt; 400 ms ✓"], final: true },
      ],
    },
    batch: {
      title: "Batch ETL",
      phases: ["Extract", "Transform", "Load", "Validate"],
      nodes: [
        { icon: "🗄️", label: "HDFS" },
        { icon: "🔥", label: "Spark" },
        { icon: "🧹", label: "Dedup" },
        { icon: "📊", label: "Warehouse" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Driver: listing Parquet shards under /data/clicks/2026/03/27/…"] },
        { d: 500, ph: 0, log: ["warn", "> 14.2 M rows — catalyst broadcast join hint applied"], fc: 0 },
        { d: 1100, ph: 1, log: ["info", "> Stage 42 shuffle write 890 MB — 200 tasks"], fc: 1, hit: 1 },
        { d: 1800, ph: 2, log: ["warn", "> window(row_ts, '1 HOUR') — late events &lt; 1 %"] },
        { d: 2400, ph: 2, log: ["info", "> coalesce(400) → single parquet out"], fc: 2, hit: 2 },
        { d: 3000, ph: 3, log: ["ok", "> Validation: row counts match Kafka source ±0.02 %"], final: true },
      ],
    },
    search: {
      title: "Log / search",
      phases: ["Ship", "Index", "Refresh", "Query"],
      nodes: [
        { icon: "🖥️", label: "Service" },
        { icon: "📝", label: "Filebeat" },
        { icon: "🔍", label: "Elasticsearch" },
        { icon: "📈", label: "Kibana" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> JSON log line — correlation_id=8f3a…"] },
        { d: 400, ph: 0, log: ["warn", "> Bulk API batch 500 docs → index logs-2026.03.27"], fc: 0 },
        { d: 900, ph: 1, log: ["info", "> Refresh interval 1 s — segment merge queued"], fc: 1, hit: 2 },
        { d: 1500, ph: 2, log: ["warn", "> Shard routing: _id hash → node es-data-07"] },
        { d: 2100, ph: 3, log: ["ok", "> Discover: match query returned in 38 ms"], fc: 2, hit: 3 },
        { d: 2700, ph: 3, log: ["ok", "> Alert rule evaluated — no breach ✓"], final: true },
      ],
    },
  };

  const WORKFLOW = {
    exp: {
      title: "Experiment ramp",
      phases: ["Design", "Config", "Ramp", "Decide"],
      nodes: [
        { icon: "💡", label: "Hypothesis" },
        { icon: "🧪", label: "Touchstone" },
        { icon: "📈", label: "Traffic" },
        { icon: "✅", label: "Metrics" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Ticket EXP-4412: ranking model v3 vs control"] },
        { d: 500, ph: 0, log: ["warn", "> Power calc: N=4.1 M impressions for 80 % power"] },
        { d: 1000, ph: 1, log: ["info", "> Bucket hash(user_id) mod 100 &lt; 50 → treatment"], fc: 0 },
        { d: 1500, ph: 2, log: ["warn", "> Ramp 1 % → 10 % — auto hold on error rate &gt; 0.5 %"], fc: 1, hit: 2 },
        { d: 2200, ph: 2, log: ["info", "> XT tags flowing to Flink — CTR delta +1.8 %"] },
        { d: 2800, ph: 3, log: ["ok", "> Sequential test: p=0.031 &lt; 0.05 — ship"], fc: 2, hit: 3 },
        { d: 3400, ph: 3, log: ["ok", "> Flag treatment as default for 100 % traffic"], final: true },
      ],
    },
    dep: {
      title: "Deploy pipeline",
      phases: ["Merge", "Build", "Stage", "Prod"],
      nodes: [
        { icon: "🔀", label: "Git" },
        { icon: "🏗️", label: "CI / image" },
        { icon: "🧪", label: "Staging" },
        { icon: "🚀", label: "Production" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> PR #8821 merged — ads-api@a3f9c2d"] },
        { d: 450, ph: 0, log: ["warn", "> Jenkins #44102: docker build 3m 12s"] },
        { d: 900, ph: 1, log: ["info", "> Image pushed — digest sha256:7e4c…"], fc: 0 },
        { d: 1400, ph: 1, log: ["warn", "> Trivy scan: 0 critical CVEs"], fc: 1, hit: 2 },
        { d: 2000, ph: 2, log: ["info", "> Helm upgrade ads-api — 12/12 pods ready"] },
        { d: 2600, ph: 3, log: ["ok", "> Rolling prod — workers → beat → API (drain 45 s)"], fc: 2, hit: 3 },
        { d: 3200, ph: 3, log: ["ok", "> codeChangeScrubber → ServiceNow CHG004412 ✓"], final: true },
      ],
    },
  };

  /** Ch 1 — two planes: streaming events vs batch analytics */
  const OVERVIEW = {
    realtime: {
      title: "Streaming plane",
      phases: ["Emit", "Buffer", "Compute", "Expose"],
      nodes: [
        { icon: "👤", label: "User" },
        { icon: "📨", label: "Kafka" },
        { icon: "⚡", label: "Flink" },
        { icon: "📊", label: "Metrics API" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Impression + click events — batch 2.1 KB Avro"] },
        { d: 450, ph: 0, log: ["warn", "> Partition by placement_id — sticky keys for joins"], fc: 0 },
        { d: 950, ph: 1, log: ["info", "> topic click-events — replication 3, ISR full"], fc: 1, hit: 1 },
        { d: 1500, ph: 2, log: ["warn", "> keyed stream: GMV 60 s tumbling + late side output"], fc: 2, hit: 2 },
        { d: 2100, ph: 2, log: ["info", "> checkpoint 4.2 s — RocksDB incremental"] },
        { d: 2700, ph: 3, log: ["ok", "> REST /v1/placement-stats — cache HIT edge POP"], fc: 2, hit: 3 },
        { d: 3300, ph: 3, log: ["ok", "> p99 end-to-end &lt; 3 s for near-real-time KPIs ✓"], final: true },
      ],
    },
    batch: {
      title: "Batch / warehouse plane",
      phases: ["Land", "Transform", "Store", "Query"],
      nodes: [
        { icon: "📨", label: "Kafka" },
        { icon: "🗄️", label: "HDFS" },
        { icon: "🔥", label: "Spark" },
        { icon: "📊", label: "CH / Hive" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Kafka→HDFS connector — hourly raw partition"] },
        { d: 500, ph: 0, log: ["warn", "> Landing zone: /raw/clicks/dt=2026-03-27/"], fc: 0 },
        { d: 1000, ph: 1, log: ["info", "> Spark driver — 400 executors × 4 cores"], fc: 1, hit: 2 },
        { d: 1600, ph: 2, log: ["warn", "> Dedup + sessionize — 1.1 B rows → 890 M rows"], fc: 2, hit: 2 },
        { d: 2200, ph: 2, log: ["info", "> Parquet snappy — sort-merge by (user, ts)"] },
        { d: 2800, ph: 3, log: ["ok", "> ClickHouse bulk load — ReplacingMergeTree apply"], fc: 2, hit: 3 },
        { d: 3400, ph: 3, log: ["ok", "> Analyst SQL — cohort report 14 s ✓"], final: true },
      ],
    },
    edge: {
      title: "Serving / edge",
      phases: ["DNS", "Route", "Rank", "Respond"],
      nodes: [
        { icon: "🌐", label: "CDN" },
        { icon: "🛡️", label: "Gateway" },
        { icon: "🎯", label: "Ranker" },
        { icon: "📦", label: "Ad JSON" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> TLS 1.3 — edge cert pinning OK"] },
        { d: 400, ph: 0, log: ["warn", "> WAF: rate limit 2k rps / IP"], fc: 0 },
        { d: 900, ph: 1, log: ["info", "> Route ads-api-prod — locality us-west-2"], fc: 1, hit: 1 },
        { d: 1400, ph: 2, log: ["warn", "> Feature fetch: user_embedding + placement_ctx 6 ms"], fc: 2, hit: 2 },
        { d: 2000, ph: 2, log: ["info", "> Auction: second-price — reserve met"] },
        { d: 2600, ph: 3, log: ["ok", "> Response 200 — 4 candidates, 1 sponsored"], fc: 2, hit: 3 },
        { d: 3200, ph: 3, log: ["ok", "> TTFB p99 38 ms ✓"], final: true },
      ],
    },
  };

  /** Hub — how ecommerce / retail media ads work (conceptual, not stack-specific) */
  const RETAIL = {
    path: {
      title: "Placement path",
      phases: ["Intent", "Inventory", "Decision", "Serve + log"],
      nodes: [
        { icon: "🛒", label: "Shopper" },
        { icon: "📍", label: "Placements" },
        { icon: "⚖️", label: "Rank / auction" },
        { icon: "✨", label: "Sponsored + IDs" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Search or PDP view — placement request with context keys"] },
        { d: 420, ph: 0, log: ["warn", "> Query: wireless earbuds — slot templates resolved (rail, inline)"], fc: 0 },
        { d: 900, ph: 1, log: ["info", "> Supply side: eligible listings × active campaigns × policy"], fc: 1, hit: 1 },
        { d: 1480, ph: 2, log: ["warn", "> Score = relevance × bid × quality — floors and caps applied"], fc: 2, hit: 2 },
        { d: 2050, ph: 2, log: ["info", "> Winners picked — second-price style clearing where used"] },
        { d: 2650, ph: 3, log: ["ok", "> Response mixes organic + sponsored rows — impression IDs issued"], fc: 2, hit: 3 },
        { d: 3250, ph: 3, log: ["ok", "> Beacons ready — clicks and views become billable events ✓"], final: true },
      ],
    },
    measure: {
      title: "Measure + settle",
      phases: ["Emit", "Pipeline", "Attribute", "Report / bill"],
      nodes: [
        { icon: "👆", label: "Click / view" },
        { icon: "📨", label: "Event bus" },
        { icon: "🔗", label: "Attribution" },
        { icon: "📒", label: "Ledger" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> User taps sponsored row — click ID correlated to impression"] },
        { d: 450, ph: 0, log: ["warn", "> View and click streams — dedupe and bot filters"], fc: 0 },
        { d: 950, ph: 1, log: ["info", "> Stream or batch joins to orders — conversion window"], fc: 1, hit: 1 },
        { d: 1520, ph: 2, log: ["warn", "> Last-touch or platform rules — ROAS and CPA computed"], fc: 2, hit: 2 },
        { d: 2100, ph: 2, log: ["info", "> Seller dashboards + finance — spend vs delivery checks"] },
        { d: 2700, ph: 3, log: ["ok", "> Invoice or auto-charge — CPC, CPM, or CPS per program"], fc: 2, hit: 3 },
        { d: 3300, ph: 3, log: ["ok", "> Auditable trail — replay for disputes ✓"], final: true },
      ],
    },
  };

  /** Ch 2 — programmatic / RTB-shaped paths */
  const RTB = {
    auction: {
      title: "RTB path",
      phases: ["Request", "Value", "Bid", "Render"],
      nodes: [
        { icon: "🌐", label: "Browser" },
        { icon: "⚡", label: "Gateway" },
        { icon: "🔨", label: "Auction" },
        { icon: "✨", label: "Winner" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> OpenRTB bid request — imp id, floor CPM 0.42"] },
        { d: 450, ph: 0, log: ["warn", "> Latency budget 92 ms — trace id propagated"], fc: 0 },
        { d: 900, ph: 1, log: ["info", "> User segment + context vector lookup"], fc: 1, hit: 1 },
        { d: 1450, ph: 2, log: ["warn", "> 14 DSP seats bid — max eCPM 1.07"], fc: 2, hit: 2 },
        { d: 2000, ph: 2, log: ["info", "> Second-price clear — clearing price 0.89"] },
        { d: 2550, ph: 3, log: ["ok", "> Win notice + ad markup returned"], fc: 2, hit: 3 },
        { d: 3100, ph: 3, log: ["ok", "> Total RTT 71 ms — SLA OK ✓"], final: true },
      ],
    },
    prog: {
      title: "DSP ⇄ SSP chain",
      phases: ["Demand", "Match", "Supply", "Fill"],
      nodes: [
        { icon: "🛒", label: "DSP" },
        { icon: "🔗", label: "Exchange" },
        { icon: "📰", label: "SSP" },
        { icon: "💰", label: "Publisher" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> Campaign budget pacing — day 12 / 30"] },
        { d: 500, ph: 0, log: ["warn", "> Deal ID private-auction — seat priority"], fc: 0 },
        { d: 1000, ph: 1, log: ["info", "> Exchange: unified auction — 40 buyers"], fc: 1, hit: 1 },
        { d: 1550, ph: 2, log: ["warn", "> SSP: floor + brand safety filter"], fc: 2, hit: 2 },
        { d: 2100, ph: 2, log: ["info", "> Creative policy scan — passed"] },
        { d: 2650, ph: 3, log: ["ok", "> Impression logged — revenue share 78 / 22"], fc: 2, hit: 3 },
        { d: 3200, ph: 3, log: ["ok", "> VAST + tracking pixels fired ✓"], final: true },
      ],
    },
  };

  /** Ch 3 — observability + anomaly narrative */
  const OBSERVABILITY = {
    sherlock: {
      title: "Detect → RCA",
      phases: ["Observe", "Score", "Page", "Link"],
      nodes: [
        { icon: "📈", label: "Prometheus" },
        { icon: "🔦", label: "Sherlock" },
        { icon: "📟", label: "PagerDuty" },
        { icon: "🎛️", label: "Ctrl Center" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> scrape: ads_gmv_usd[5m] — rate stable"] },
        { d: 450, ph: 0, log: ["warn", "> ES ML: consumer lag z-score 3.1 σ"], fc: 0 },
        { d: 950, ph: 1, log: ["info", "> Sherlock: baseline vs same hour DOW — deviation 18 %"], fc: 1, hit: 1 },
        { d: 1550, ph: 2, log: ["warn", "> PD incident #I-9921 — Sev-2"], fc: 2, hit: 2 },
        { d: 2100, ph: 2, log: ["info", "> Slack #ads-war-room — on-call joined"] },
        { d: 2650, ph: 3, log: ["ok", "> Overlay: deploy 14:28 + exp ramp 14:15"], fc: 2, hit: 3 },
        { d: 3300, ph: 3, log: ["ok", "> Hypothesis: bad deploy — rollback queued ✓"], final: true },
      ],
    },
    prom: {
      title: "Threshold alerts",
      phases: ["Rule", "Eval", "Route", "Ack"],
      nodes: [
        { icon: "📋", label: "PromQL" },
        { icon: "🔔", label: "Alertmgr" },
        { icon: "💬", label: "Slack" },
        { icon: "✅", label: "Ack" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["info", "> rule: p99 &gt; 500 ms for 5 m"] },
        { d: 450, ph: 0, log: ["warn", "> vector match — ads-api 7 pods"], fc: 0 },
        { d: 900, ph: 1, log: ["info", "> group_by(service) — 1 firing series"], fc: 1, hit: 1 },
        { d: 1400, ph: 2, log: ["warn", "> route: #sre-ads + PD low-urgency"], fc: 2, hit: 2 },
        { d: 1950, ph: 2, log: ["info", "> dedupe key — no repeat 30 m"] },
        { d: 2500, ph: 3, log: ["ok", "> engineer ack — link Grafana panel"], fc: 2, hit: 3 },
        { d: 3000, ph: 3, log: ["ok", "> Silence window 2 h if deploy planned ✓"], final: true },
      ],
    },
  };

  /** Ch 5 — incident command */
  const INCIDENT = {
    sev2: {
      title: "Revenue drop",
      phases: ["Alert", "Hunt", "Fix", "Verify"],
      nodes: [
        { icon: "🚨", label: "PagerDuty" },
        { icon: "🔦", label: "Sherlock" },
        { icon: "⏪", label: "Rollback" },
        { icon: "📈", label: "GMV OK" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["warn", "> TRIGGER: GMV -22 % vs 15 m baseline"] },
        { d: 500, ph: 0, log: ["info", "> CC timeline: deploy ads-ranker@bad14 at T-4 m"], fc: 0 },
        { d: 1000, ph: 1, log: ["warn", "> Sherlock: error spike NullPointer in ranker"], fc: 1, hit: 1 },
        { d: 1550, ph: 1, log: ["info", "> ES: stack traces clustered — 1 root cause"] },
        { d: 2100, ph: 2, log: ["ok", "> kubectl rollout undo — deployment/ads-ranker"], fc: 2, hit: 2 },
        { d: 2750, ph: 2, log: ["info", "> pods 12/12 ready — canary removed"] },
        { d: 3300, ph: 3, log: ["ok", "> GMV trajectory crosses lower bound — recovery"], fc: 2, hit: 3 },
        { d: 3900, ph: 3, log: ["ok", "> Postmortem doc stub — RCA: missing null guard ✓"], final: true },
      ],
    },
    kafka: {
      title: "Pipeline lag",
      phases: ["Lag", "Scale", "Drain", "Stable"],
      nodes: [
        { icon: "📨", label: "Kafka" },
        { icon: "⚡", label: "Flink" },
        { icon: "📦", label: "Scale out" },
        { icon: "✓", label: "Healthy" },
      ],
      steps: [
        { d: 0, ph: 0, log: ["warn", "> consumer_lag &gt; 5 M — topic click-events"] },
        { d: 500, ph: 0, log: ["info", "> broker OK — ISR healthy"], fc: 0 },
        { d: 1000, ph: 1, log: ["warn", "> Flink: backpressure on map operator"], fc: 1, hit: 1 },
        { d: 1550, ph: 2, log: ["info", "> parallelism 64 → 96 — rescaling job"], fc: 2, hit: 2 },
        { d: 2200, ph: 2, log: ["warn", "> checkpoint duration 8 s — within SLA"] },
        { d: 2800, ph: 3, log: ["ok", "> lag &lt; 100 k — SLA green"], fc: 2, hit: 3 },
        { d: 3400, ph: 3, log: ["ok", "> Autoscale policy updated ✓"], final: true },
      ],
    },
  };

  function firePacket(connEl, multi) {
    if (!connEl) return;
    connEl.classList.add("eps-conn-lit");
    const count = multi ? 3 : 1;
    const spd = multi ? 380 : 520;
    for (let j = 0; j < count; j++) {
      setTimeout(() => {
        const dot = document.createElement("div");
        dot.className = "eps-pkt";
        dot.style.left = "0";
        connEl.appendChild(dot);
        requestAnimationFrame(() =>
          requestAnimationFrame(() => {
            dot.style.transition = "left " + spd + "ms linear";
            dot.style.left = "calc(100% - 9px)";
            setTimeout(() => {
              if (dot.parentNode) dot.remove();
            }, spd + 60);
          })
        );
      }, j * 120);
    }
    setTimeout(() => connEl.classList.remove("eps-conn-lit"), spd + count * 120 + 80);
  }

  function logClass(kind) {
    if (kind === "err") return "eps-tl-err";
    if (kind === "warn") return "eps-tl-warn";
    if (kind === "ok") return "eps-tl-ok";
    return "eps-tl-info";
  }

  function buildShell(root, scenarios) {
    const keys = Object.keys(scenarios);
    const btnRow = document.createElement("div");
    btnRow.className = "eps-btn-row";
    keys.forEach((k) => {
      const b = document.createElement("button");
      b.type = "button";
      b.className = "eps-scen-btn";
      b.dataset.scen = k;
      b.textContent = scenarios[k].title;
      btnRow.appendChild(b);
    });

    const phaseRow = document.createElement("div");
    phaseRow.className = "eps-phases";
    for (let i = 0; i < 4; i++) {
      const p = document.createElement("div");
      p.className = "eps-phase";
      p.id = root.id + "-ph-" + i;
      phaseRow.appendChild(p);
    }

    const flow = document.createElement("div");
    flow.className = "eps-flow";
    flow.id = root.id + "-flow";

    const log = document.createElement("div");
    log.className = "eps-log";
    log.id = root.id + "-log";

    const hint = document.createElement("p");
    hint.className = "eps-hint";
    hint.textContent = "Pick a scenario above — runs immediately (click again to replay).";

    root.appendChild(hint);
    root.appendChild(btnRow);
    root.appendChild(phaseRow);
    root.appendChild(flow);
    root.appendChild(log);

    return { keys, btnRow, phaseRow, flow, log };
  }

  function renderFlow(flowEl, scenario) {
    flowEl.innerHTML = "";
    const nodes = scenario.nodes;
    for (let i = 0; i < nodes.length; i++) {
      const n = document.createElement("div");
      n.className = "eps-node";
      n.id = flowEl.id + "-node-" + i;
      n.innerHTML =
        '<div class="eps-nd-icon">' +
        nodes[i].icon +
        '</div><div class="eps-nd-label">' +
        nodes[i].label +
        "</div>";
      flowEl.appendChild(n);
      if (i < nodes.length - 1) {
        const c = document.createElement("div");
        c.className = "eps-conn";
        c.id = flowEl.id + "-fc-" + i;
        flowEl.appendChild(c);
      }
    }
  }

  function runScenario(root, scenarios, key) {
    const s = scenarios[key];
    if (!s) return;

    const id = root.id;
    const logEl = document.getElementById(id + "-log");
    const flowEl = document.getElementById(id + "-flow");
    if (!logEl || !flowEl) return;
    const timers = root._epsTimers || [];
    timers.forEach((t) => clearTimeout(t));
    root._epsTimers = [];

    for (let i = 0; i < 4; i++) {
      const ph0 = document.getElementById(id + "-ph-" + i);
      if (ph0) {
        ph0.className = "eps-phase";
        ph0.textContent = s.phases[i] || "—";
      }
    }

    renderFlow(flowEl, s);

    logEl.innerHTML = "";
    logEl.style.display = "block";

    root.querySelectorAll(".eps-scen-btn").forEach((b) => {
      b.classList.toggle("eps-scen-active", b.dataset.scen === key);
    });

    let lastPh = -1;
    s.steps.forEach((step) => {
      const t = setTimeout(() => {
        if (step.ph !== lastPh) {
          if (lastPh >= 0) {
            const prev = document.getElementById(id + "-ph-" + lastPh);
            if (prev) {
              prev.classList.remove("eps-phase-active");
              prev.classList.add("eps-phase-done");
            }
          }
          const cur = document.getElementById(id + "-ph-" + step.ph);
          if (cur) cur.classList.add("eps-phase-active");
          lastPh = step.ph;
        }
        if (step.fc !== undefined) {
          const fc = document.getElementById(flowEl.id + "-fc-" + step.fc);
          firePacket(fc, step.multi);
        }
        if (step.hit !== undefined) {
          const hn = document.getElementById(flowEl.id + "-node-" + step.hit);
          if (hn) hn.classList.add("eps-node-hit");
        }
        const line = document.createElement("div");
        line.className = "eps-tl " + logClass(step.log[0]);
        line.textContent = step.log[1];
        logEl.appendChild(line);
        logEl.scrollTop = logEl.scrollHeight;
        if (step.final) {
          const cur = document.getElementById(id + "-ph-" + step.ph);
          if (cur) {
            cur.classList.remove("eps-phase-active");
            cur.classList.add("eps-phase-done");
          }
        }
      }, step.d);
      root._epsTimers.push(t);
    });
  }

  function wire(root, scenarios, defaultKey) {
    buildShell(root, scenarios);
    renderFlow(document.getElementById(root.id + "-flow"), scenarios[defaultKey]);
    for (let i = 0; i < 4; i++) {
      const ph = document.getElementById(root.id + "-ph-" + i);
      if (ph) ph.textContent = scenarios[defaultKey].phases[i] || "—";
    }
    root.querySelectorAll(".eps-scen-btn").forEach((b) => {
      b.addEventListener("click", () => runScenario(root, scenarios, b.dataset.scen));
    });
    runScenario(root, scenarios, defaultKey);
  }

  function wireIfPresent(id, scenarios, defaultKey, titleHtml) {
    const el = document.getElementById(id);
    if (!el) return;
    el.innerHTML = '<p class="eps-title">' + titleHtml + "</p>";
    wire(el, scenarios, defaultKey);
  }

  function init() {
    wireIfPresent(
      "eps-retail-root",
      RETAIL,
      "path",
      'Ecommerce ads — process flow <span class="eps-badge">node</span>'
    );
    wireIfPresent(
      "eps-tech-root",
      TECH,
      "rt",
      'Pipeline simulator <span class="eps-badge">Flow</span>'
    );
    wireIfPresent(
      "eps-wf-root",
      WORKFLOW,
      "exp",
      'Workflow simulator <span class="eps-badge">Flow</span>'
    );
    wireIfPresent(
      "eps-overview-root",
      OVERVIEW,
      "realtime",
      'Animated flows <span class="eps-badge">platform planes</span>'
    );
    wireIfPresent(
      "eps-rtb-root",
      RTB,
      "auction",
      'Programmatic flow <span class="eps-badge">RTB-shaped</span>'
    );
    wireIfPresent(
      "eps-obs-root",
      OBSERVABILITY,
      "sherlock",
      'Observe → alert → RCA <span class="eps-badge">stack</span>'
    );
    wireIfPresent(
      "eps-incident-root",
      INCIDENT,
      "sev2",
      'Incident command <span class="eps-badge">playbook</span>'
    );
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
