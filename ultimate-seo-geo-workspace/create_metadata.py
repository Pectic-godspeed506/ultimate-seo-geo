#!/usr/bin/env python3
"""Create eval_metadata.json files for iteration-2 from evals.json."""
import json
from pathlib import Path

EVALS_PATH = Path("/Users/myk/.claude/skills/seo/plugins/ultimate-seo-geo/skills/ultimate-seo-geo/evals/evals.json")
WORKSPACE = Path("/Users/myk/Desktop/ai-projects/ultimate-seo-geo/ultimate-seo-geo-workspace/iteration-2")

EVAL_NAMES = {
    1: "Full SEO Audit (psybear.co YMYL)",
    2: "Local HVAC Schema (sonoranair.com)",
    3: "SaaS Schema (Docupilot)",
    4: "E-commerce Migration (Magento→Shopify)",
    5: "Sourdough Recipe Blog SEO",
    6: "Google Ads PPC — NEGATIVE",
    7: "Regional Newspaper Publisher",
    8: "Scoped robots.txt + sitemap only",
    9: "International SEO (hreflang)",
    10: "Pre-launch SaaS SEO pillars",
    11: "Traffic Drop Recovery (core update)",
    12: "GEO/AI Citations (TaskForge SaaS)",
    13: "Robots.txt Block All — Risk Gate",
    14: "CWV Technical Audit — No Fabrication",
}

with open(EVALS_PATH) as f:
    data = json.load(f)

evals_by_id = {e["id"]: e for e in data["evals"]}

for eval_id, eval_data in evals_by_id.items():
    eval_dir = WORKSPACE / f"eval-{eval_id}"
    eval_dir.mkdir(exist_ok=True)

    metadata = {
        "eval_id": eval_id,
        "eval_name": EVAL_NAMES.get(eval_id, f"Eval {eval_id}"),
        "prompt": eval_data["prompt"],
        "assertions": eval_data.get("assertions", [])
    }

    # Write to eval dir AND both config dirs (viewer needs it in config dirs)
    for target in [eval_dir, eval_dir / "with_skill", eval_dir / "without_skill"]:
        target.mkdir(exist_ok=True)
        with open(target / "eval_metadata.json", "w") as f:
            json.dump(metadata, f, indent=2)

    print(f"eval-{eval_id}: {EVAL_NAMES.get(eval_id, '?')}")

print(f"\nCreated metadata for {len(evals_by_id)} evals")
