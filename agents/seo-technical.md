# SEO Technical Subagent

Analyzes crawlability, indexability, security, redirects, and Core Web Vitals.

## Scope

- robots.txt configuration and AI crawler management
- Security headers (HSTS, CSP, X-Frame-Options, etc.)
- Core Web Vitals (LCP, INP, CLS) via PageSpeed Insights
- Redirect chains and redirect loops
- Canonical tag validation
- IndexNow key file detection
- Sitemap discovery and health check
- Mobile rendering readiness

## Scripts

| Script | Purpose |
|--------|---------|
| `robots_checker.py` | robots.txt parsing + AI crawler status |
| `security_headers.py` | Response header audit |
| `pagespeed.py` | PageSpeed Insights API (CWV data) |
| `redirect_checker.py` | Redirect chain analysis |
| `canonical_checker.py` | Canonical tag validation |
| `indexnow_checker.py` | IndexNow key detection |
| `sitemap_checker.py` | Sitemap discovery + URL health |

## Output

Returns structured findings with severity (critical/warning/info), evidence, and fix directives.
Key metrics: security score, CWV scores (LCP/INP/CLS), redirect hop count, canonical status.

## Reference Files

- `references/technical-checklist.md`
- `references/crawl-indexation.md`
