# SEO Performance Subagent

Measures and evaluates Core Web Vitals and page load performance.

## Scope

- Core Web Vitals: LCP, INP, CLS (field + lab data)
- Performance score (0-100)
- Render-blocking resources
- Image optimization opportunities
- JavaScript execution impact
- Server response time (TTFB)

## Scripts

| Script | Purpose |
|--------|---------|
| `pagespeed.py` | PageSpeed Insights API for CWV data |
| `image_checker.py` | Image alt coverage + optimization |

## CWV Thresholds (current as of 2026)

| Metric | Good | Needs Improvement | Poor |
|--------|------|--------------------|------|
| LCP | < 2.5s | 2.5-4.0s | > 4.0s |
| INP | < 200ms | 200-500ms | > 500ms |
| CLS | < 0.1 | 0.1-0.25 | > 0.25 |

INP replaced FID March 2024. Never reference FID.

## Output

Returns performance score, individual CWV metrics (field and lab),
and prioritized optimization opportunities.

## Reference Files

- `references/technical-checklist.md`
- `references/image-seo.md`
