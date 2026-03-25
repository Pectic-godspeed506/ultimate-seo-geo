# Changelog

## [1.2.0] - 2026-03-24

### Added

- `scripts/score_eval_transcript.py` — score saved model transcripts against `evals/evals.json` (`--eval-id`, `--all-fixtures`).
- `scripts/meta_lengths_checker.py` — title, meta description, and H1 length/presence from local HTML or `--url`.
- `evals/fixtures/eval{1–10}_pass.txt` — golden transcripts; CI runs `score_eval_transcript.py --all-fixtures`.
- `evals/evals.json` — four new scenarios (7–10): news publisher, scoped technical-only, international, pre-launch strategy.
- `references/finding-verifier-example.json` + `finding-verifier-context-example.json` — sample input for `finding_verifier.py`.

### Changed

- **SKILL.md** — §0 routing index; “when not to run Mode 1” table; §1 routing notes; §2 lab/PSI evidence rule + industry preset table; §21 script list + evidence integrity + `pip install -r requirements.txt`; version **1.2.0**.
- **README** — script/eval counts, `score_eval_transcript` / `meta_lengths_checker`, **Updating the Claude Code plugin** (cache refresh).
- **references/audit-script-matrix.md** — meta lengths row, eval/QA section, `score_eval_transcript`, finding_verifier CLI + examples.
- **scripts/run_individual_checks.sh** — runs `meta_lengths_checker` when HTML fetch succeeds.
- **CI** (`.github/workflows/validate-plugin.yml`) — `py_compile` all `scripts/*.py` + eval fixture regression.
- Marketplace + `plugin.json` descriptions and version **1.2.0**.

## [1.1.2] - 2026-03-24

### Added

- `sitemap_checker.py`, `local_signals_checker.py`, `image_checker.py` — URL/HTML checks for crawl/sitemap, local surface signals, and image alt coverage.
- `references/audit-script-matrix.md` — maps each audit step to its script and example CLI (plus **reference-only** rows where no script exists by design).
- `scripts/run_individual_checks.sh` — runs each diagnostic sequentially (JSON samples); bundled beside audit scripts in the plugin tree.
- `requirements.txt` — `requests` + `beautifulsoup4` for fetch/HTML scripts.

### Changed

- `RELEASE.md` §3 — points to the audit matrix and `run_individual_checks.sh` smoke path.
- `generate_report.py` wired to schema JSON-LD validation, image alt, sitemap, local, and IndexNow **probe** (keyless) sections + scoring and dashboard blocks.
- `validate_schema.py` supports `--json` for tooling; `indexnow_checker.py` supports `--probe` without `--key`.
- Skill §21 + README updated for **23** audit scripts; README documents `requirements.txt` and PEP 668 venv use.

### Fixed

- `generate_report.py` — On-Page table no longer crashes when `canonical` is JSON `null`.

## [1.1.1] - 2026-03-24

### Changed

- Skill YAML `description` tightened to stay within common 1024-character limits while preserving trigger terms.
- Plugin bundle (`setup-plugin.sh`) now copies **`scripts/`** (all audit `.py` files except `check-plugin-sync.py`) and **`evals/`** into `plugins/.../skills/ultimate-seo-geo/` so Claude Code plugin installs can run `python scripts/...` as documented.

## [1.1.0] - 2026-03-24

### Added

- Reference library expanded: `core-eeat-framework.md`, `cite-domain-rating.md`, `entity-optimization.md` (CORE-EEAT, CITE domain authority, entity / Knowledge Graph signals).
- Credits updated for CORE-EEAT benchmark, CITE Domain Rating, Entity Optimizer, and AI SEO / GEO content optimizer sources.
- Skill routing extended for CORE-EEAT / CITE scoring, entity optimization, and related triggers.

### Changed

- Documentation alignment: `generate_report.py` wording reflects the bundled pipeline (not a literal “19 scripts” count); §21 clarifies orchestration vs optional parallel subagents.

## [1.0.0] - 2026-03-23

### Initial Public Release

**Core Capabilities**

- Full-site SEO audits with SEO Health Score (0–100) and prioritized findings
- Generative Engine Optimization (GEO) for AI Overviews, ChatGPT, Perplexity
- Technical SEO, on-page, content/E-E-A-T, schema, links, local, international, programmatic SEO
- Site migration playbooks and analytics alignment
- Bundled Python audit scripts and eval scenarios
