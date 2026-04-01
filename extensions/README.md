# Extensions

Optional add-ons that integrate external data sources into the Ultimate SEO + GEO agent.

Extensions are **platform-neutral** — each includes adapters for multiple AI coding platforms.

## Available Extensions

| Extension | What It Does | Free Tier |
|-----------|-------------|-----------|
| **Firecrawl** | Full-site crawling with JavaScript rendering | 500 credits/month |
| **DataForSEO** | Live SERP data, keyword research, backlink profiles | Trial credits |

## How Extensions Work

Each extension follows a self-contained structure:

```
extensions/<name>/
  extension.json     # Manifest (name, version, env vars, MCP config)
  README.md          # Setup guide
  install-generic.sh # Platform-agnostic install (env vars only)
  install-claude.sh  # Claude Code adapter (MCP server config)
  install-cursor.sh  # Cursor adapter (MCP server config)
```

## Install

### Generic (any platform)

```bash
bash extensions/firecrawl/install-generic.sh
```

### Claude Code

```bash
bash extensions/firecrawl/install-claude.sh
```

### Cursor

```bash
bash extensions/firecrawl/install-cursor.sh
```

## Design Principles

1. **Core works without extensions** — all scripts function with just `requests` + `beautifulsoup4`
2. **Extensions enrich, not replace** — when available, scripts auto-detect and use richer data
3. **Graceful degradation** — if an extension is not installed, scripts fall back silently
4. **No vendor lock-in** — extensions use a standard `extension.json` manifest, not platform-specific formats
