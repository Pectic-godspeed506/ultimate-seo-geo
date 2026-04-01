# Firecrawl Extension

Full-site crawling with JavaScript rendering. Solves SPA/CSR visibility issues where
`requests`-based crawling misses JS-rendered content.

## What It Enables

- `crawl_adapter.py` uses Firecrawl backend for JS-rendered page fetching
- `site_mapper.py` uses Firecrawl map for fast URL discovery
- `generate_report.py --renderer firecrawl` for full JS-rendered audits

## Setup

1. Get a free API key at [firecrawl.dev](https://www.firecrawl.dev/)
2. Run the install script for your platform:

```bash
# Any platform (sets env var)
bash extensions/firecrawl/install-generic.sh

# Claude Code (configures MCP server)
bash extensions/firecrawl/install-claude.sh

# Cursor (configures MCP server)
bash extensions/firecrawl/install-cursor.sh
```

## Free Tier

500 credits/month. One page crawl = 1 credit. URL map = 0.5 credits per URL.

## Verification

```bash
python scripts/crawl_adapter.py https://example.com --backend firecrawl --json
```

If Firecrawl is not configured, scripts automatically fall back to the `requests` backend.
