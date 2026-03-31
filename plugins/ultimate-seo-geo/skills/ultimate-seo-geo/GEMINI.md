# Ultimate SEO + GEO — Gemini CLI Context

This project is a comprehensive SEO and Generative Engine Optimization (GEO) skill with
24 diagnostic Python scripts, scored audit frameworks, and AI search citation optimization.

## Instructions

All instructions for this skill are in AGENTS.md (compact version) and SKILL.md (full version).

@AGENTS.md

## Key Commands

```bash
# Full-site audit report
python scripts/generate_report.py https://example.com --output report.html

# Install dependencies first
pip install -r requirements.txt

# Run all individual checks
bash scripts/run_individual_checks.sh https://example.com
```

## Reference Files

Domain knowledge lives in `references/`. Load only what you need per task — see the
Routing Index in AGENTS.md § 0 for the mapping of tasks to reference files and scripts.
