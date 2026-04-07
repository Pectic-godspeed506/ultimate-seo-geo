> **Progressive disclosure:** Load this file only when the current task maps to this section (see `SKILL.md` §0). Do not load all procedure files for narrow tasks.

## 6. Content Quality & E-E-A-T

### Key Policy Updates

| Update | Date | Impact |
|---|---|---|
| **E-E-A-T universal** | December 2025 | Applies to ALL competitive queries — not just YMYL |
| **AI content quality** | September 2025 QRG | AI content acceptable if genuine E-E-A-T; penalized without unique value |
| **Helpful Content System merged** | March 2024 | Merged into core algorithm — helpfulness weighted continuously |
| **Google AI Mode** | May 2025 | Available in 180+ countries; delivers **zero blue links** — AI citation is the only visibility mechanism; traditional rankings do not appear |

### Functional Page Exemption (check before auditing content)

**Before applying any content-quality or thin-content checks, classify the page type.** Functional pages have a task-completion purpose — minimal copy is correct design, not a content problem.

| Page type | Examples | Content audit rule |
|---|---|---|
| **Functional / task UI** | Sign up, Sign in, Log in, Register, Create account, Forgot password, Reset password, Join, Membership enroll, Checkout, Cart, Account dashboard, Profile settings | **Skip word-count checks entirely. Do NOT flag as thin content. Do NOT recommend adding more copy.** |
| **Landing / marketing** | Pricing, Features, About, Blog, Service pages | Apply full content audit below |
| **Content** | Blog posts, guides, case studies | Apply full content audit below |

**For functional pages, relevant checks are:** page title accuracy, meta description clarity, form label quality, error message usability, trust signals (SSL badge, privacy link), and schema (`WebPage`, `BreadcrumbList`). Never flag low word count.

---

### Content Audit — Step by Step

1. **Read the page in full.** Comprehensive coverage? Named author with credentials?
2. **Score each E-E-A-T factor** — see `references/eeat-framework.md` for the full scoring framework and factor weights.
3. **Identify the weakest factor** — this is the highest-leverage fix.
4. **Check word count**: Blog post 1,500+, Service page 800+, Homepage 500+, Product page 300+. These are topical coverage floors, not targets — Google has confirmed word count is NOT a direct ranking factor. A focused 500-word page that thoroughly answers the query outranks a padded 2,000-word page. Cover the topic fully, then stop.
5. **Check for thin content signals**: copied definitions, no original research, no first-hand examples, no author bio.
6. **Recommend specific additions** — not "add experience signals," but "add a section with real test results showing [specific outcome] from [specific test]."

**Key insight**: AI can mimic expertise but not fabricate genuine Experience. First-hand signals are the #1 E-E-A-T differentiator post-Dec 2025.

**Don't**: Recommend increasing word count as a standalone fix. Padding is a negative signal.

For the E-E-A-T scoring framework with factor weights, content quality minimums table, readability grade targets, and 2025 spam categories (expired domain abuse, site reputation abuse, scaled content abuse), see `references/eeat-framework.md` and `references/content-eeat.md`.

For the full **80-item CORE-EEAT content audit** (8 dimensions, Pass/Partial/Fail scoring, content-type weight tables, 3 veto items, GEO Score vs. SEO Score), see `references/core-eeat-framework.md`. Use this for deep content quality assessments.

For the **40-item CITE domain authority audit** (Citation/Identity/Trust/Eminence, domain-type weights, veto items that cap score at 39, Diagnosis Matrix for CITE × CORE-EEAT strategy), see `references/cite-domain-rating.md`. Use this for domain-level authority assessments.

→ See `references/eeat-framework.md` `references/content-eeat.md` `references/core-eeat-framework.md` `references/cite-domain-rating.md` | Run `scripts/article_seo.py` Run `scripts/readability.py` Run `scripts/duplicate_content.py`

---

## 6b. Content Pruning & Refresh

For sites older than 2 years, content decay is often higher leverage than creating new content.

### Step by Step

1. **Export all URLs from GSC** → Performance → Last 16 months → Download CSV. Sort by impressions descending.
2. **Categorize every page** into one of four buckets:

| Bucket | Criteria | Action |
|---|---|---|
| **Refresh** | Had impressions 12–16 months ago, traffic declined, topic still relevant | Update content, improve E-E-A-T, add question headings, update lastModified |
| **Prune** | < 10 impressions in 12 months, no backlinks, outdated | 301 redirect to most relevant page, then delete |
| **Consolidate** | Multiple pages covering the same topic | Merge into one strong page; redirect all others |
| **Keep** | Stable or growing traffic, strong E-E-A-T | Monitor monthly |

3. **For each Prune**: zero backlinks → 301 redirect then delete. Has backlinks → consolidate first.
4. **For each Consolidate**: pick strongest page, incorporate best content, 301 redirect weaker pages, update all internal links.

**Don't**: Prune pages with external backlinks without redirecting. Losing backlink equity from an unredirected prune is worse than keeping mediocre content.

For freshness thresholds by content type, see `references/content-eeat.md`.

→ See `references/content-eeat.md`
