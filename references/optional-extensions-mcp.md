# Optional extensions and MCP (Firecrawl, DataForSEO)

**MCP and these extensions are optional.** All bundled audit scripts run with only `requests` and `beautifulsoup4` (`pip install -r requirements.txt`). Extensions add richer crawling and live SERP/backlink data when you configure them in your environment.

## What each extension adds

| Extension | What it adds | Typical free tier |
|-----------|----------------|-------------------|
| **Firecrawl** | JavaScript-rendered crawling (full-site / dynamic pages) | Vendor plan (e.g. monthly credits) |
| **DataForSEO** | Live SERP, keywords, backlinks, on-page/Lighthouse via MCP | Trial credits |

When MCP tools from DataForSEO are available, use them per `references/procedures/21-script-toolbox.md` (DataForSEO MCP table) and `references/ai-search-geo.md` (GEO visibility checks).

## Claude Code plugin installs (no monorepo checkout)

The plugin bundle includes `scripts/` and `references/` but **not** the `extensions/` shell installers. Use a full clone of the repository to run install scripts, or copy commands from the paths below.

**Repository:** [github.com/mykpono/ultimate-seo-geo](https://github.com/mykpono/ultimate-seo-geo)

After cloning:

```bash
# Firecrawl — env vars only (any host)
bash extensions/firecrawl/install-generic.sh

# Firecrawl — Claude Code MCP config
bash extensions/firecrawl/install-claude.sh

# Firecrawl — Cursor MCP config
bash extensions/firecrawl/install-cursor.sh
```

```bash
# DataForSEO — same pattern
bash extensions/dataforseo/install-generic.sh
bash extensions/dataforseo/install-claude.sh
bash extensions/dataforseo/install-cursor.sh
```

Each extension folder contains `README.md`, `extension.json` (MCP package name and env vars), and the install scripts above.

## Monorepo users

If you already have the full repo at disk, see **`extensions/README.md`** for the same install flow and design principles (graceful degradation, no vendor lock-in).
