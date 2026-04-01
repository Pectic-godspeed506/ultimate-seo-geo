# Where to Submit Ultimate SEO + GEO Plugin

Organized by priority. Higher-priority venues reach the exact audience that will use the plugin.

---

## Tier 1 — Plugin Marketplaces (highest priority)

These are where developers discover and install plugins directly.

### 1. Claude Code Official Plugin Directory

**URL:** <https://github.com/anthropics/claude-plugins-official>
**Submission form:** <https://clau.de/plugin-directory-submission>

**Instructions:**

1. Fill out the plugin directory submission form with the GitHub repo URL (`mykpono/ultimate-seo-geo`)
2. Anthropic runs automated quality and security review
3. Approved plugins get listed and can be installed via `/plugin install ultimate-seo-geo@claude-plugins-official`
4. High-quality plugins may receive an "Anthropic Verified" badge

**Status:** The repo already supports marketplace install (`/plugin marketplace add mykpono/ultimate-seo-geo`). Submitting to the official directory gives broader discoverability.

---

### 2. Cursor Marketplace

**URL:** <https://cursor.com/marketplace/publish>

**Instructions:**

1. Ensure the repo has a `.cursor-plugin/plugin.json` manifest (or adapt the existing `.claude-plugin/plugin.json`)
2. Use the [plugin template](https://github.com/cursor/plugin-template) as reference for required fields
3. Submit at cursor.com/marketplace/publish
4. Cursor team manually reviews every plugin before listing
5. Once approved, users can install via `/add-plugin` or browse it on cursor.com/marketplace

**Prep needed:** May need to create a Cursor-specific plugin manifest. The skill already works in Cursor via `~/.claude/skills/`, but marketplace listing makes it one-click install.

---

### 3. The Skills Directory

**URL:** <https://www.theskills.directory/>
**GitHub:** <https://github.com/theskillsdirectory/skills>

**Instructions:**

Option A — Pull request:

1. Fork `theskillsdirectory/skills`
2. Create `skills/ultimate-seo-geo/SKILL.md` using their template from `template/SKILL.md`
3. Fill in YAML frontmatter: name, description (single line), version, compatible_agents (Claude Code, Cursor — tested; others — untested), categories, job_roles, author, github, license
4. Open a pull request

Option B — Web form:

1. Go to <https://www.theskills.directory/submit>
2. Fill in the form fields

**Important:** Description must be a single line (multi-line breaks YAML). List only agents you've actually tested under "tested".

---

## Tier 2 — Curated GitHub Lists

These lists are where developers browse for tools. High-star lists drive sustained GitHub traffic.

### 4. awesome-claude-code-plugins (654 stars)

**URL:** <https://github.com/ccplugins/awesome-claude-code-plugins>

**Instructions:**

1. Check which category fits best (likely "Marketing Growth" or "Code Quality Testing")
2. Fork the repo
3. Add an entry for `ultimate-seo-geo` with a one-line description and link
4. Open a pull request following their contribution guidelines

---

### 5. awesome-claude-code by subinium (68 stars)

**URL:** <https://github.com/subinium/awesome-claude-code>

**Instructions:**

1. Fork the repo
2. Add under the "Skills" or "Plugins" section
3. Open a pull request

**Note:** This list requires 1,000+ stars for inclusion. May need to wait until the repo reaches that threshold, or reach out to the maintainer for an exception given the tool's depth.

---

### 6. hekmon8/awesome-claude-code-plugins

**URL:** <https://github.com/hekmon8/awesome-claude-code-plugins>

**Instructions:**

1. Fork, add entry under appropriate category
2. Open a pull request

---

## Tier 3 — Developer Communities (launch posts)

Posts here drive initial traffic spikes and GitHub stars.

### 7. Hacker News — Show HN

**URL:** <https://news.ycombinator.com/submit>

**Instructions:**

1. Title format: `Show HN: Ultimate SEO + GEO — open-source Claude/Cursor plugin for site audits and AI search optimization`
2. URL: Link to the GitHub repo
3. Write a text comment immediately after posting explaining what it does, what's novel (GEO + traditional SEO in one, 25 scripts, scored findings, three modes), and link to a demo or sample report
4. Best posting times: weekday mornings US Eastern (9-11 AM ET, Tuesday-Thursday)

---

### 8. Dev.to

**URL:** <https://dev.to/new>

**Instructions:**

1. Write an article like: "I built an open-source SEO + GEO plugin for Claude Code and Cursor — here's what it does"
2. Include: problem statement, architecture diagram, sample output, installation steps
3. Tags: `#seo`, `#ai`, `#opensource`, `#webdev`
4. Dev.to SEO/GEO articles have gotten strong traction recently (see similar posts from 2026)

---

### 9. Reddit

Post in these subreddits (follow each sub's self-promotion rules):

| Subreddit | Angle | Rules to note |
|---|---|---|
| **r/ClaudeAI** (~120K members) | "I built an SEO + GEO plugin for Claude Code" | Check self-promo limits |
| **r/cursor** (~80K members) | "SEO/GEO skill that works in Cursor" | Flair as "Show & Tell" |
| **r/SEO** (~200K members) | "Free open-source tool that audits SEO + AI search readiness" | No direct links in posts; describe the tool, add GitHub link in comments |
| **r/bigseo** (~30K members) | Technical deep-dive on the audit methodology | Professional tone; focus on methodology |
| **r/webdev** (~2M members) | "Open source SEO audit tool with 25 Python scripts" | Show & Tell posts welcome |
| **r/SideProject** (~150K members) | Launch announcement | Built for show-and-tell |
| **r/opensource** (~60K members) | "MIT-licensed SEO + GEO plugin for AI coding assistants" | Must be genuinely open source (it is) |

**Timing:** Space posts across 1-2 weeks so you don't look spammy.

---

### 10. Product Hunt

**URL:** <https://www.producthunt.com/posts/new>

**Instructions:**

1. Create a product page: name, tagline, description, screenshots/GIFs, link
2. Tagline idea: "Open-source SEO + AI search audit skill for Claude Code & Cursor"
3. Prepare: maker comment, 3-5 screenshots (sample audit output, architecture, install flow)
4. Schedule launch for a Tuesday-Thursday for best visibility
5. Rally early upvotes from your network in the first 1-2 hours

---

## Tier 4 — AI Tool Directories (SEO backlinks + organic discovery)

Free submission. Lower traffic but good for backlinks and long-tail discovery.

| Directory | URL | Monthly Traffic |
|---|---|---|
| **Future Tools** | <https://www.futuretools.io/submit-a-tool> | ~1M |
| **There's An AI For That** | <https://theresanaiforthat.com/submit/> | ~4M |
| **AI Tools Directory** | <https://ai-toolsdirectory.com/submit-new-listing/> | ~77K |
| **Supertools** | <https://supertools.therundown.ai/submit> | ~311K |
| **Dang.ai** | <https://dang.ai/submit> | ~131K |
| **AI Tools Arena** | <https://www.aitoolsarena.com/submit> | ~84K |
| **SaaS AI Tools** | <https://saasaitools.com/submit-tool/> | ~15K |
| **AI of the Day** | <https://aioftheday.com/submit/> | ~17K |
| **Directory for AI** | <https://directoryforai.com/submit-tool/> | — |
| **AITools Directory (.com)** | <https://www.aitools-directory.com/submit> | — |

**Batch alternative:** Web Directory Center (<https://webdirectorycenter.com/>) offers a done-for-you service to submit to 100+ AI directories at once.

**Comprehensive list:** TheAISurf (<https://theaisurf.com/ai-tools-directory-top-artificial-intelligence-solutions>) has a ranked list of 200+ directories with domain authority, submission type, and niche focus.

---

## Tier 5 — Social & Content Marketing (ongoing)

### 11. LinkedIn

**Instructions:**

1. Write a launch post on your personal profile describing the plugin, what problem it solves, and link to GitHub
2. Publish a long-form article with architecture breakdown + use cases
3. Share in relevant LinkedIn groups: SEO professionals, AI/ML practitioners, developer communities
4. Your profile is already linked in the README — use it

---

### 12. Twitter / X

**Instructions:**

1. Thread format works well: "I built an open-source SEO + GEO plugin for Claude Code. Here's what it does (thread)"
2. Tag @AnthropicAI, @cursor_ai, relevant SEO influencers
3. Include a GIF or screenshot of audit output
4. Use hashtags: #SEO #GEO #ClaudeCode #OpenSource #AI

---

### 13. YouTube

**Instructions:**

1. Record a 5-10 min demo: install the plugin, run a real audit, walk through the output
2. Title: "Free SEO Audit in 60 Seconds with Claude Code — Ultimate SEO + GEO Plugin"
3. Good for long-term organic traffic from "Claude Code SEO" searches

---

## Suggested Launch Order

| Week | Actions |
|---|---|
| **Week 1** | Submit to Claude Official Directory, Cursor Marketplace, The Skills Directory |
| **Week 1** | Submit PRs to awesome-lists (4, 5, 6) |
| **Week 2** | Publish Dev.to article, post on r/ClaudeAI and r/cursor |
| **Week 2** | Submit to top 5 AI directories (Future Tools, TAAFT, Supertools, Dang, AI Tools Arena) |
| **Week 3** | Launch on Product Hunt (Tuesday-Thursday) |
| **Week 3** | Post Show HN, r/SEO, r/bigseo, r/webdev |
| **Week 3** | LinkedIn launch post + Twitter thread |
| **Week 4** | Submit to remaining AI directories (batch) |
| **Week 4** | Post on r/SideProject, r/opensource |
| **Ongoing** | YouTube demo, LinkedIn articles, update listings after new releases |
