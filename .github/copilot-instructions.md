# Ultimate SEO + GEO — Copilot Instructions

This repository is a comprehensive SEO and Generative Engine Optimization (GEO) skill with
24 diagnostic Python scripts, scored audit frameworks, and AI search citation optimization.

## How to Use

All instructions are in `AGENTS.md` (compact, auto-loaded) and `SKILL.md` (full detail).
GitHub Copilot reads `AGENTS.md` automatically. If you need full step-by-step procedures,
scoring frameworks, or examples, read the relevant section from `SKILL.md`.

## Key Capabilities

- **Mode 1 — Audit**: Fetch a site, run all checks, produce a scored SEO Health Score report
- **Mode 2 — Plan**: Convert findings into a phased, prioritized roadmap
- **Mode 3 — Execute**: Produce the actual fixes (meta tags, schema, redirect maps) + verify

## Quick Start

```bash
pip install -r requirements.txt
python scripts/generate_report.py https://example.com --output report.html
```

## Reference Files

Domain knowledge is in `references/` (20 markdown files). Load only what you need per task.
See the Routing Index in `AGENTS.md` § 0 for the task-to-file mapping.

## Important Rules

- Every audit finding must have: Finding / Evidence / Impact / Fix / Confidence
- Never fabricate metrics — only report data from scripts that actually ran
- High-risk changes (robots.txt, redirects, noindex) require user confirmation before output
- For competitor sites, label all output "External Observation Only"
