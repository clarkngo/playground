# Changelog — CityU Tools

Path: `/cityu-tools/`
Tags: `[bug]` `[feature]` `[ux]` `[refactor]`

---

## 2026-03-16

### [bug] Fixed pop-up blocker issue in multi-tab launcher
- Added one line to `cityu-tools/multi-tab-launcher.html` to allow pop-ups to open correctly

---

## 2026-03-02

### [feature] Created CityU Tools section with two utilities
- `cityu-tools/multi-tab-launcher.html` — bulk URL tab launcher (141 lines)
  - Streamlit-styled dark UI (red accent `#ff4b4b`, dark background `#0e1117`)
  - Textarea for pasting multiple URLs (one per line)
  - "Launch All Tabs" button opens each URL in a new browser tab
  - Designed for quickly opening sets of student/course links
- `cityu-tools/generate-links.html` — link generation utility (233 lines)
  - Generates sets of links from templates or patterns
  - Useful for creating batches of course-related URLs
