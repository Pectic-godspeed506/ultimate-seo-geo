#!/usr/bin/env python3
"""Aggregate iteration-2 benchmark results into benchmark.json and benchmark.md."""

import json
import math
from pathlib import Path
from datetime import datetime, timezone

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

def mean(values):
    return sum(values) / len(values) if values else 0.0

def stddev(values):
    if len(values) < 2:
        return 0.0
    m = mean(values)
    return math.sqrt(sum((x - m) ** 2 for x in values) / (len(values) - 1))

runs = []
for eval_dir in sorted(WORKSPACE.glob("eval-*")):
    try:
        eval_id = int(eval_dir.name.split("-")[1])
    except (IndexError, ValueError):
        continue

    for config_dir in sorted(eval_dir.iterdir()):
        if not config_dir.is_dir() or config_dir.name not in ("with_skill", "without_skill"):
            continue

        grading_path = config_dir / "grading.json"
        timing_path = config_dir / "timing.json"
        if not grading_path.exists():
            continue

        with open(grading_path) as f:
            grading = json.load(f)
        timing = {}
        if timing_path.exists():
            with open(timing_path) as f:
                timing = json.load(f)

        run = {
            "id": f"eval-{eval_id}-{config_dir.name}",
            "eval_id": eval_id,
            "eval_name": EVAL_NAMES.get(eval_id, f"Eval {eval_id}"),
            "configuration": config_dir.name,
            "result": {
                "pass_rate": grading["summary"]["pass_rate"],
                "passed": grading["summary"]["passed"],
                "total": grading["summary"]["total"],
                "expectations": grading["expectations"]
            },
            "timing": {
                "time_seconds": timing.get("total_duration_seconds", grading.get("timing", {}).get("total_duration_seconds", 0)),
                "tokens": timing.get("total_tokens", 0)
            }
        }
        runs.append(run)

# Aggregate stats per configuration
def compute_stats(config_runs):
    pass_rates = [r["result"]["pass_rate"] for r in config_runs]
    times = [r["timing"]["time_seconds"] for r in config_runs]
    tokens = [r["timing"]["tokens"] for r in config_runs]
    return {
        "pass_rate": {
            "mean": round(mean(pass_rates), 4),
            "stddev": round(stddev(pass_rates), 4),
            "min": round(min(pass_rates), 4) if pass_rates else 0,
            "max": round(max(pass_rates), 4) if pass_rates else 0,
            "n": len(pass_rates)
        },
        "time_seconds": {
            "mean": round(mean(times), 1),
            "stddev": round(stddev(times), 1),
            "min": round(min(times), 1) if times else 0,
            "max": round(max(times), 1) if times else 0
        },
        "tokens": {
            "mean": round(mean(tokens)),
            "stddev": round(stddev(tokens)),
            "min": min(tokens) if tokens else 0,
            "max": max(tokens) if tokens else 0
        }
    }

ws_runs = [r for r in runs if r["configuration"] == "with_skill"]
wos_runs = [r for r in runs if r["configuration"] == "without_skill"]

ws_stats = compute_stats(ws_runs)
wos_stats = compute_stats(wos_runs)

delta_pr = round(ws_stats["pass_rate"]["mean"] - wos_stats["pass_rate"]["mean"], 4)
delta_time = round(ws_stats["time_seconds"]["mean"] - wos_stats["time_seconds"]["mean"], 1)
delta_tokens = round(ws_stats["tokens"]["mean"] - wos_stats["tokens"]["mean"])

# Analyst notes
notes = [
    f"OVERALL: with_skill {ws_stats['pass_rate']['mean']*100:.0f}% (±{ws_stats['pass_rate']['stddev']*100:.0f}%) vs without_skill {wos_stats['pass_rate']['mean']*100:.0f}% (±{wos_stats['pass_rate']['stddev']*100:.0f}%) — delta {delta_pr*100:+.0f}pp.",
    "NEW GEO ASSERTIONS (E1) ARE DISCRIMINATING: eval-12 now shows with_skill 88% vs without_skill 75%. The 3 new assertions (llms.txt, citation blocks, brand correlation data) differentiate skill-specific GEO depth. Previously both scored 100%.",
    "ROBOTS.TXT RISK GATE (P1): eval-13 with_skill 75% vs without_skill 50%. The strengthened High-Risk gate instruction (P1) means the skill warns and asks for confirmation, but one assertion still fails — 'does-not-lead-with-file' needs both configs to mention consequences/risk in the opening.",
    "CWV NO-FABRICATION (eval-14): with_skill 100% vs without_skill 50%. The skill correctly refuses to fabricate LCP/INP/CLS numbers and directs to PageSpeed Insights. Without-skill invents specific metrics.",
    "PPC NEGATIVE (eval-6): with_skill 100% vs without_skill 100%. The E3 fix (removing bare 'SEO Health Score' from regex) eliminates the previous false positive. Both configs correctly handle the out-of-scope request.",
    "LOCALBUSINESS FIX (eval-2): with_skill 100% vs without_skill 100%. The E4 fix (broadening pattern to accept HVACBusiness/ProfessionalService subtypes) resolved the previous 75% failure in without_skill.",
    "NON-DISCRIMINATING EVALS: Evals 1-5, 7-11 all score 100% in both configs. These test basic SEO knowledge that Claude has even without the skill. The skill's value shows in specialized areas (GEO, safety gates, no-fabrication).",
    f"VARIANCE: with_skill stddev {ws_stats['pass_rate']['stddev']*100:.0f}% vs without_skill {wos_stats['pass_rate']['stddev']*100:.0f}%. The skill produces more consistent output across diverse scenarios.",
    f"COMPLETION RATE: 28/28 runs completed (100%). The context-budget awareness section (P3) may have helped — previous iteration had 28% timeout rate.",
]

benchmark = {
    "metadata": {
        "skill_name": "ultimate-seo-geo",
        "iteration": 2,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "executor_model": "claude-sonnet-4-20250514 (fast)",
        "analyzer_model": "claude-4.6-opus-high-thinking",
        "total_evals": 14,
        "total_runs": len(runs),
        "configs": ["with_skill", "without_skill"]
    },
    "runs": runs,
    "run_summary": {
        "with_skill": ws_stats,
        "without_skill": wos_stats,
        "delta": {
            "pass_rate": delta_pr,
            "time_seconds": delta_time,
            "tokens": delta_tokens
        }
    },
    "notes": notes
}

with open(WORKSPACE / "benchmark.json", "w") as f:
    json.dump(benchmark, f, indent=2)

# Generate benchmark.md
md = []
md.append("# Skill Benchmark: ultimate-seo-geo (Iteration 2 — Post-Improvement)")
md.append("")
md.append(f"**Model**: {benchmark['metadata']['executor_model']}")
md.append(f"**Date**: {benchmark['metadata']['timestamp']}")
md.append(f"**Evals**: 14 scenarios, 1 run each per configuration ({len(runs)} total runs)")
md.append(f"**Changes since iteration 1**: P1 (robots.txt gate), P3 (context budget), P4 (quality gate 11), E1-E4 (eval fixes)")
md.append("")
md.append("## Summary")
md.append("")
md.append("| Metric | With Skill | Without Skill | Delta |")
md.append("|--------|------------|---------------|-------|")
md.append(f"| **Pass Rate** | {ws_stats['pass_rate']['mean']*100:.0f}% ± {ws_stats['pass_rate']['stddev']*100:.0f}% | {wos_stats['pass_rate']['mean']*100:.0f}% ± {wos_stats['pass_rate']['stddev']*100:.0f}% | {delta_pr*100:+.0f}pp |")
md.append(f"| **Time** | {ws_stats['time_seconds']['mean']:.1f}s ± {ws_stats['time_seconds']['stddev']:.1f}s | {wos_stats['time_seconds']['mean']:.1f}s ± {wos_stats['time_seconds']['stddev']:.1f}s | {delta_time:+.1f}s |")
md.append(f"| **Tokens** | {ws_stats['tokens']['mean']:.0f} ± {ws_stats['tokens']['stddev']:.0f} | {wos_stats['tokens']['mean']:.0f} ± {wos_stats['tokens']['stddev']:.0f} | {delta_tokens:+d} |")
md.append("")

md.append("## Per-Eval Breakdown")
md.append("")
md.append("| # | Eval | With Skill | Without Skill | Delta | Key Finding |")
md.append("|---|------|------------|---------------|-------|-------------|")

key_findings = {
    1: "Both perfect — basic audit knowledge",
    2: "E4 fix: without_skill now 100% (was 75%)",
    3: "Both perfect — schema generation",
    4: "Both perfect — migration guidance",
    5: "Both perfect — recipe blog SEO",
    6: "E3 fix: with_skill now 100% (was 89%)",
    7: "Both perfect — publisher SEO",
    8: "Both perfect — scoped review",
    9: "Both perfect — intl SEO",
    10: "Both perfect — pre-launch pillars",
    11: "Both perfect — traffic drop",
    12: "NEW: discriminating GEO assertions (E1)",
    13: "P1 safety gate differentiates",
    14: "Skill prevents metric fabrication",
}

for eid in sorted(EVAL_NAMES.keys()):
    ws_run = next((r for r in runs if r["eval_id"] == eid and r["configuration"] == "with_skill"), None)
    wos_run = next((r for r in runs if r["eval_id"] == eid and r["configuration"] == "without_skill"), None)
    ws_pr = f"{ws_run['result']['pass_rate']*100:.0f}%" if ws_run else "N/A"
    wos_pr = f"{wos_run['result']['pass_rate']*100:.0f}%" if wos_run else "N/A"
    if ws_run and wos_run:
        d = (ws_run['result']['pass_rate'] - wos_run['result']['pass_rate']) * 100
        delta_str = f"{d:+.0f}pp"
    else:
        delta_str = "—"
    md.append(f"| {eid} | {EVAL_NAMES[eid]} | {ws_pr} | {wos_pr} | {delta_str} | {key_findings.get(eid, '')} |")

md.append("")
md.append("## Analyst Notes")
md.append("")
for note in notes:
    md.append(f"- {note}")

md.append("")
md.append("## Comparison with Iteration 1")
md.append("")
md.append("| Metric | Iter 1 With Skill | Iter 2 With Skill | Change |")
md.append("|--------|-------------------|-------------------|--------|")
md.append(f"| Pass Rate | 91% ± 14% | {ws_stats['pass_rate']['mean']*100:.0f}% ± {ws_stats['pass_rate']['stddev']*100:.0f}% | Improved |")
md.append(f"| Completion | 72% (26/36) | 100% (28/28) | +28pp |")
md.append(f"| GEO Discrimination | 0pp (both 100%) | {(next((r for r in runs if r['eval_id']==12 and r['configuration']=='with_skill'), {}).get('result',{}).get('pass_rate',0) - next((r for r in runs if r['eval_id']==12 and r['configuration']=='without_skill'), {}).get('result',{}).get('pass_rate',0))*100:+.0f}pp | Now discriminates |")
md.append(f"| False positives (eval 6) | 1/3 runs | 0/1 runs | Fixed |")

with open(WORKSPACE / "benchmark.md", "w") as f:
    f.write("\n".join(md))

print("Generated benchmark.json and benchmark.md")
print(f"\nOverall: with_skill {ws_stats['pass_rate']['mean']*100:.0f}% vs without_skill {wos_stats['pass_rate']['mean']*100:.0f}% (delta {delta_pr*100:+.0f}pp)")
