# Subagent Capability Definitions

Platform-neutral descriptions of parallel workers for SEO audits. Each file describes
what a subagent is responsible for, which scripts it runs, and what it reports back.

## How Platforms Use These

| Platform | Interpretation |
|----------|---------------|
| **Cursor** | Host AI reads these and uses its Task tool to spawn parallel subagents |
| **Claude Code** | Can be installed as `~/.claude/agents/` with YAML frontmatter added |
| **Copilot / Gemini / others** | Host AI reads as context for how to parallelize audit work |

## Subagents

| Agent | Scope | Scripts |
|-------|-------|---------|
| seo-technical | Crawlability, security, CWV, redirects | robots_checker, security_headers, pagespeed, redirect_checker |
| seo-content | E-E-A-T, readability, article quality, duplicates | article_seo, readability, duplicate_content, meta_lengths_checker |
| seo-schema | Structured data validation | validate_schema |
| seo-geo | AI search visibility, llms.txt, entity signals | robots_checker (AI crawlers), llms_txt_checker, entity_checker |
| seo-performance | Core Web Vitals, page speed | pagespeed |
| seo-links | Internal links, broken links, backlink profile | internal_links, broken_links, link_profile, backlink_analyzer |

## Orchestration Pattern

During a full audit (`generate_report.py`), the host AI can:
1. Run `site_mapper.py` to discover URLs
2. Spawn subagents in parallel, each covering their scope
3. Collect results and deduplicate findings with `finding_verifier.py`
4. Merge into a unified Health Score report
