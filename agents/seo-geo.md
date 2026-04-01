# SEO GEO Subagent

Optimizes content for AI search citation: Google AI Overviews, ChatGPT Search, Perplexity.

## Scope

- AI crawler access verification (GPTBot, OAI-SearchBot, PerplexityBot, ClaudeBot)
- llms.txt presence and quality
- RSL 1.0 (Really Simple Licensing) detection
- Citability scoring (answer placement, passage length, structural readability)
- Entity signals (Wikidata, Wikipedia, sameAs links)
- Brand mention presence on YouTube, Reddit, LinkedIn
- Social meta tags (OG, Twitter Card)

## Scripts

| Script | Purpose |
|--------|---------|
| `robots_checker.py` | AI crawler access status |
| `llms_txt_checker.py` | llms.txt presence + quality score |
| `entity_checker.py` | Wikidata/Wikipedia/sameAs signals |
| `social_meta.py` | Open Graph + Twitter Card tags |

## Key Insights

- 44.2% of AI citations come from the first 30% of content
- Answer in first 60 words = highest citation probability
- Optimal citation passage: 134-167 words
- Blocking AI crawlers removes site from AI search entirely
- GPTBot blocking also limits ChatGPT Search citations
- Mentions > Backlinks for AI citation (0.664 vs 0.218 correlation)

## Output

Returns GEO score (0-100) across 5 dimensions: citability, structural readability,
authority signals, technical accessibility, multi-modal content.

## Reference Files

- `references/ai-search-geo.md`
- `references/entity-optimization.md`
