<!-- Audit output example — referenced from SKILL.md § 2 -->

# Audit Output Example (3-finding excerpt)

```
# SEO Audit Report — greenleaf.io
Date: 2026-03-15 | Business Type: SaaS | Audited Pages: 8 | Confidence: Medium

## SEO Health Score: 61/100
positive_signals=14, deficit_signals=9, base=61, Critical −15×0, Warning −5×2 = 51 → adjusted 61

## 🟠 High Priority

Finding: No Organization or SoftwareApplication schema on any page
Evidence: 0 JSON-LD blocks found across 8 pages; competitors average 3 schema types
Impact: Missing rich results; 0% AI citation eligibility — schema increases citation ~2.5×
Fix: Add Organization schema to homepage, SoftwareApplication + AggregateRating to /pricing
Confidence: Confirmed | Severity: 🟠 High

Finding: LCP 4.8s on homepage — hero image is 1.2MB unoptimized PNG
Evidence: PageSpeed Insights mobile score 38; LCP element: <img src="/hero-dashboard.png">
Impact: Poor CWV = deprioritized in mobile rankings; FCP > 0.4s reduces AI citations by 3×
Fix: Convert to WebP (target <200KB), add fetchpriority="high", preload via <link>
Confidence: Confirmed | Severity: 🟠 High

## ⚡ Quick Wins

Finding: Title tags use "Home | Greenleaf" pattern — keyword absent
Evidence: Homepage title "Home | Greenleaf" instead of primary keyword
Impact: ~15% CTR loss vs. keyword-leading titles at same position
Fix: Rewrite to "Project Management for Remote Teams | Greenleaf"
Confidence: Confirmed | Severity: 🟡 Medium
```
