> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 15. Programmatic SEO

### Step by Step

1. **Assess data source** — Each record must have ≥3 distinct data points beyond the variable name.
2. **Design template** — Unique injection: title, H1, meta description, ≥30% of body content.
3. **Apply quality gates** — Hard stops below.
4. **Build internal linking** — Programmatic pages must link to pillar and cluster pages.
5. **noindex thin records** from day one.
6. **Human review** — 5–10% sample before publishing >100 pages.

### Quality Gates (Non-Negotiable)

| Threshold | Action |
|---|---|
| >100 pages | ⚠️ WARNING — review content differentiation |
| >500 pages OR <30% unique content | 🛑 HARD STOP |
| <40% differentiation | Flag as thin content risk |

**Don't**: Approve city pages where only the city name changes — March 2024 Core Update target (60–80% traffic declines seen).

**Scaled Content Abuse enforcement timeline:**
- **November 2024**: Site reputation abuse enforcement escalated — publishing programmatic content under a high-authority domain you don't own triggers penalties
- **June 2025**: Wave of manual actions targeting AI-generated content at scale
- **August 2025**: SpamBrain update enhanced pattern detection for AI content farms and link schemes
- **Result**: Google reported 45% reduction in low-quality, unoriginal content in search results post-March 2024
- **Progressive rollout rule**: Publish in batches of 50–100 pages. Monitor indexing and rankings for 2–4 weeks before expanding. Never publish 500+ programmatic pages simultaneously without explicit quality review.

**Automated audit**: Run `scripts/programmatic_seo_auditor.py URL --depth 2 --max-pages 100 --json` to auto-detect template URL patterns and audit each group for boilerplate ratio, content uniqueness, title/description/H1 duplication, and cross-linking health. The script flags pages below the 30% uniqueness hard stop (scaled content abuse) and 40% warning threshold.

→ See `references/programmatic-seo.md` (12 playbooks taxonomy, data-asset-to-playbook decision matrix, data defensibility hierarchy, Scaled Content Abuse enforcement timeline with dates, uniqueness calculation formula, progressive rollout strategy)
