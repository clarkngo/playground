# Token Usage Log

Tracks Claude token consumption per session in this project.
Pull from: `~/.claude/projects/-Users-clark-playground/<session-id>.jsonl`

**How to read this file:**
- `input` = tokens Claude read (your messages + context)
- `output` = tokens Claude generated
- `cache_read` = tokens served from prompt cache (cheap: $0.30/M vs $3/M)
- `cache_write` = tokens written to cache (one-time cost at $3.75/M)
- `est_cost` = estimated USD at Sonnet 4.6 rates

**Sonnet 4.6 pricing (per 1M tokens):**
| Type | Rate |
|---|---|
| Input | $3.00 |
| Output | $15.00 |
| Cache read | $0.30 |
| Cache write | $3.75 |

**Usage guidance:**
- Subagents each spin up a fresh context window — 10 agents = 10× the context overhead
- Large files in context (HTML primers ~60–80KB each) add to input tokens every turn
- Cache read is ~10× cheaper than input — long sessions benefit from prompt caching
- Output tokens are 5× more expensive than input — verbose responses cost more

---

## 2026-03-30

| Session ID | Date | Input | Output | Cache Read | Cache Write | Est. Cost | Notes |
|---|---|---|---|---|---|---|---|
| eb01eb5a | 2026-03-30 | 1,524 | 69,863 | 11,563,960 | — | ~$9.10 | Primer section creation + 4 industry primers |

---

## 2026-03-27

| Session ID | Date | Input | Output | Cache Read | Cache Write | Est. Cost | Notes |
|---|---|---|---|---|---|---|---|
| dc23fc3c | 2026-03-27 | 683 | 215,405 | 40,220,969 | — | ~$23.29 | Data Architecture & Flows + Failure Modes tabs (all 12 primers) |

---

## 2026-03-25

| Session ID | Date | Input | Output | Cache Read | Cache Write | Est. Cost | Notes |
|---|---|---|---|---|---|---|---|
| 31a3a01b | 2026-03-25 | 11,723 | 862,571 | 245,071,345 | — | ~$115.67 | Bulk primer builds (insurance, logistics, manufacturing, healthcare + others); heavy subagent use drove cache reads |

---

## Patterns & Observations

### High-cost patterns (avoid when possible)
- **Subagent storms** — launching 10+ agents simultaneously multiplies context overhead; each agent re-reads the same shared context. The 2026-03-25 session cost ~$115 largely due to subagent parallelism.
- **Re-reading large HTML files** — each 80KB primer file adds ~20K tokens to context per read. Minimize full-file reads; use targeted line ranges.
- **Redundant changelog agents** — spawning a dedicated agent just to append 3 lines to a changelog file costs ~$0.50–1.00 per agent invocation.

### Low-cost patterns (prefer)
- **Direct Python scripting** — the 2026-03-30 batch injection of 9 primers via a single Python script used ~$9 total vs. ~$90+ via subagents.
- **Targeted grep/sed before reading** — reading only the lines you need (e.g., `sed -n '26,40p'`) instead of full file reads.
- **Shared.js / shared.css** — extracting common JS/CSS to shared files reduces per-primer file size and therefore context cost per edit.

### Rate limit notes
- Claude Code rate limits reset at **3am America/Los_Angeles**
- Subagents share the same rate limit pool as the main conversation
- Hitting limits mid-task leaves files in partial states — prefer completing work in fewer, larger operations
| 2026-03-30 19:47 | 1,564 | 105,535 | 15,578,417 | $11.3991 | auto-hook snapshot <!-- hook:1774925223 -->
