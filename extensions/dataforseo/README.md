# DataForSEO Extension

Live SERP data, keyword research, backlink profiles, on-page analysis, and AI visibility tracking.

## What It Enables

- `backlink_analyzer.py --source dataforseo` for live backlink data
- Live SERP analysis for any keyword
- Keyword volume, difficulty, and intent classification
- AI visibility checking (LLM mentions of your brand)
- Competitor backlink gap analysis with live data

## Setup

1. Create an account at [dataforseo.com](https://dataforseo.com/)
2. Run the install script for your platform:

```bash
# Any platform (sets env vars)
bash extensions/dataforseo/install-generic.sh

# Claude Code (configures MCP server)
bash extensions/dataforseo/install-claude.sh

# Cursor (configures MCP server)
bash extensions/dataforseo/install-cursor.sh
```

## Verification

```bash
python scripts/backlink_analyzer.py --source dataforseo --target-url https://example.com --json
```
