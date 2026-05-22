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
| 2026-03-31 09:05 | 11,741 | 864,913 | 245,833,936 | $116.3286 | auto-hook snapshot <!-- hook:1774973152 -->
| 2026-04-01 14:12 | 51 | 10,089 | 930,040 | $1.0896 | auto-hook snapshot <!-- hook:1775077952 -->
| 2026-04-01 19:01 | 295 | 59,516 | 17,310,992 | $14.0864 | auto-hook snapshot <!-- hook:1775095295 -->
| 2026-04-02 01:54 | 1,959 | 159,743 | 23,855,969 | $19.7649 | auto-hook snapshot <!-- hook:1775120092 -->
| 2026-04-02 06:58 | 2,580 | 187,842 | 27,125,928 | $22.3970 | auto-hook snapshot <!-- hook:1775138321 -->
| 2026-04-02 11:11 | 28 | 25,739 | 518,062 | $0.7746 | auto-hook snapshot <!-- hook:1775153496 -->
| 2026-04-03 00:13 | 50 | 29,764 | 1,787,497 | $1.8275 | auto-hook snapshot <!-- hook:1775200405 -->
| 2026-04-03 02:56 | 116 | 116,954 | 4,653,517 | $7.0097 | auto-hook snapshot <!-- hook:1775210162 -->
| 2026-04-03 05:24 | 50 | 8,821 | 883,785 | $0.6461 | auto-hook snapshot <!-- hook:1775219046 -->
| 2026-04-03 10:50 | 153 | 40,524 | 7,379,859 | $4.1282 | auto-hook snapshot <!-- hook:1775238649 -->
| 2026-04-06 23:29 | 108 | 33,293 | 4,755,845 | $2.8218 | auto-hook snapshot <!-- hook:1775543387 -->
| 2026-04-07 14:08 | 15,351 | 26,465 | 800,460 | $1.3731 | auto-hook snapshot <!-- hook:1775596132 -->
| 2026-04-07 16:15 | 23,715 | 79,526 | 11,832,093 | $8.9830 | auto-hook snapshot <!-- hook:1775603701 -->
| 2026-04-07 17:31 | 23,715 | 79,526 | 11,832,093 | $8.9830 | auto-hook snapshot <!-- hook:1775608289 -->
| 2026-04-07 19:59 | 23,715 | 79,526 | 11,832,093 | $8.9830 | auto-hook snapshot <!-- hook:1775617167 -->
| 2026-04-08 11:06 | 14 | 836 | 193,043 | $0.1563 | auto-hook snapshot <!-- hook:1775671592 -->
| 2026-04-08 12:26 | 7,334 | 38,521 | 2,274,473 | $2.6935 | auto-hook snapshot <!-- hook:1775676381 -->
| 2026-04-09 01:20 | 594 | 32,638 | 760,120 | $1.0050 | auto-hook snapshot <!-- hook:1775722820 -->
| 2026-04-09 22:00 | 33 | 33,939 | 598,018 | $0.9464 | auto-hook snapshot <!-- hook:1775797253 -->
| 2026-04-09 23:03 | 230 | 90,032 | 9,480,884 | $6.7654 | auto-hook snapshot <!-- hook:1775801009 -->
| 2026-04-10 12:30 | 669 | 56,432 | 4,594,113 | $4.4232 | auto-hook snapshot <!-- hook:1775849436 -->
| 2026-04-12 17:52 | 703 | 58,411 | 5,843,735 | $5.1749 | auto-hook snapshot <!-- hook:1776041576 -->
| 2026-04-12 18:53 | 791 | 109,282 | 10,722,516 | $9.0183 | auto-hook snapshot <!-- hook:1776045182 -->
| 2026-04-12 19:53 | 925 | 126,646 | 15,363,098 | $10.9022 | auto-hook snapshot <!-- hook:1776048825 -->
| 2026-04-13 23:31 | 6,828 | 14,175 | 1,677,875 | $2.1704 | auto-hook snapshot <!-- hook:1776148296 -->
| 2026-04-14 00:34 | 7,020 | 125,475 | 12,890,973 | $8.7814 | auto-hook snapshot <!-- hook:1776152043 -->
| 2026-04-14 10:10 | 317 | 114,365 | 14,031,951 | $9.2661 | auto-hook snapshot <!-- hook:1776186611 -->
| 2026-04-14 23:54 | 16 | 15,859 | 314,373 | $0.6355 | auto-hook snapshot <!-- hook:1776236048 -->
| 2026-04-15 15:26 | 56 | 12,474 | 1,279,584 | $1.1129 | auto-hook snapshot <!-- hook:1776291980 -->
| 2026-04-16 01:39 | 148 | 65,714 | 4,714,386 | $5.3142 | auto-hook snapshot <!-- hook:1776328789 -->
| 2026-04-16 10:17 | 210 | 100,153 | 8,714,795 | $8.1229 | auto-hook snapshot <!-- hook:1776359820 -->
| 2026-04-16 14:03 | 210 | 100,153 | 8,714,795 | $8.1229 | auto-hook snapshot <!-- hook:1776373385 -->
| 2026-04-16 16:33 | 236 | 102,626 | 10,076,381 | $9.3274 | auto-hook snapshot <!-- hook:1776382384 -->
| 2026-04-16 22:08 | 263 | 106,015 | 12,219,003 | $10.8052 | auto-hook snapshot <!-- hook:1776402513 -->
| 2026-04-18 02:37 | 125 | 60,235 | 5,155,673 | $4.2134 | auto-hook snapshot <!-- hook:1776505053 -->
| 2026-04-18 03:37 | 134 | 71,166 | 4,194,703 | $3.5153 | auto-hook snapshot <!-- hook:1776508653 -->
| 2026-04-19 15:14 | 35 | 14,572 | 601,723 | $1.0050 | auto-hook snapshot <!-- hook:1776636847 -->
| 2026-04-19 16:17 | 176 | 116,442 | 7,523,120 | $6.5609 | auto-hook snapshot <!-- hook:1776640673 -->
| 2026-04-21 09:51 | 231 | 177,733 | 12,326,923 | $10.1139 | auto-hook snapshot <!-- hook:1776790291 -->
| 2026-04-21 11:53 | 231 | 177,733 | 12,326,923 | $10.1139 | auto-hook snapshot <!-- hook:1776797584 -->
| 2026-04-21 13:01 | 231 | 177,733 | 12,326,923 | $10.1139 | auto-hook snapshot <!-- hook:1776801666 -->
| 2026-04-21 16:28 | 231 | 177,733 | 12,326,923 | $10.1139 | auto-hook snapshot <!-- hook:1776814081 -->
| 2026-04-23 09:41 | 981 | 135,669 | 17,739,678 | $11.8564 | auto-hook snapshot <!-- hook:1776962517 -->
| 2026-04-23 11:16 | 981 | 135,669 | 17,739,678 | $11.8564 | auto-hook snapshot <!-- hook:1776968194 -->
| 2026-04-23 12:16 | 981 | 135,669 | 17,739,678 | $11.8564 | auto-hook snapshot <!-- hook:1776971813 -->
| 2026-04-23 15:42 | 981 | 135,669 | 17,739,678 | $11.8564 | auto-hook snapshot <!-- hook:1776984121 -->
| 2026-04-24 02:29 | 981 | 135,669 | 17,739,678 | $11.8564 | auto-hook snapshot <!-- hook:1777022999 -->
| 2026-04-26 21:24 | 7,403 | 110,833 | 6,209,220 | $7.0931 | auto-hook snapshot <!-- hook:1777263880 -->
| 2026-04-27 13:14 | 7,544 | 224,569 | 16,684,734 | $13.0834 | auto-hook snapshot <!-- hook:1777320890 -->
| 2026-04-28 14:42 | 7,544 | 224,569 | 16,684,734 | $13.0834 | auto-hook snapshot <!-- hook:1777412574 -->
| 2026-04-28 20:41 | 991 | 224,353 | 18,053,431 | $13.8960 | auto-hook snapshot <!-- hook:1777434114 -->
| 2026-04-29 10:30 | 7,579 | 305,636 | 17,806,094 | $16.8196 | auto-hook snapshot <!-- hook:1777483812 -->
| 2026-04-29 11:36 | 7,623 | 377,019 | 21,187,046 | $19.3289 | auto-hook snapshot <!-- hook:1777487804 -->
| 2026-05-03 09:34 | 247 | 207,390 | 13,344,793 | $11.8371 | auto-hook snapshot <!-- hook:1777826098 -->
| 2026-05-05 20:43 | 32 | 15,388 | 1,010,815 | $1.0933 | auto-hook snapshot <!-- hook:1778039001 -->
| 2026-05-06 11:38 | 1,028 | 321,704 | 21,351,764 | $18.1646 | auto-hook snapshot <!-- hook:1778092700 -->
| 2026-05-06 13:46 | 2,402 | 341,824 | 24,038,812 | $19.8516 | auto-hook snapshot <!-- hook:1778100399 -->
| 2026-05-07 02:07 | 2,283 | 72,979 | 789,416 | $2.0387 | auto-hook snapshot <!-- hook:1778144820 -->
| 2026-05-07 13:15 | 17 | 5,535 | 412,524 | $0.4961 | auto-hook snapshot <!-- hook:1778184959 -->
| 2026-05-10 11:53 | 7,706 | 528,749 | 27,625,772 | $25.1144 | auto-hook snapshot <!-- hook:1778439212 -->
| 2026-05-10 13:55 | 7,822 | 659,280 | 36,882,221 | $31.9140 | auto-hook snapshot <!-- hook:1778446516 -->
| 2026-05-11 12:10 | 7,853 | 677,846 | 40,162,653 | $34.4738 | auto-hook snapshot <!-- hook:1778526643 -->
| 2026-05-12 20:49 | 2,464 | 484,149 | 27,197,220 | $23.9032 | auto-hook snapshot <!-- hook:1778644155 -->
| 2026-05-17 02:43 | 306 | 258,768 | 14,889,716 | $13.9314 | auto-hook snapshot <!-- hook:1779011017 -->
| 2026-05-17 03:49 | 454 | 351,286 | 27,188,257 | $19.4391 | auto-hook snapshot <!-- hook:1779014945 -->
| 2026-05-19 20:36 | 2,490 | 498,235 | 29,372,704 | $25.7450 | auto-hook snapshot <!-- hook:1779248162 -->
| 2026-05-21 21:25 | 7,909 | 773,448 | 42,183,273 | $37.3477 | auto-hook snapshot <!-- hook:1779423906 -->
| 2026-05-21 22:39 | 7,977 | 805,197 | 47,865,480 | $39.8089 | auto-hook snapshot <!-- hook:1779428382 -->
