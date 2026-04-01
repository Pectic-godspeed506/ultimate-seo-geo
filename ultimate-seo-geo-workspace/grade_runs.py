#!/usr/bin/env python3
"""Grade all benchmark runs using assertion patterns from evals.json."""

import json
import re
import os
from pathlib import Path
from datetime import datetime, timezone

WORKSPACE = Path("/Users/myk/Desktop/ai-projects/ultimate-seo-geo/ultimate-seo-geo-workspace/iteration-1")
EVALS_PATH = Path("/Users/myk/.claude/skills/seo/plugins/ultimate-seo-geo/skills/ultimate-seo-geo/evals/evals.json")

EVAL_ID_MAP = {
    "eval-1-full-seo-audit": 1,
    "eval-2-local-hvac-schema": 2,
    "eval-3-google-ads-negative": 6,
    "eval-4-geo-ai-citations": 12,
    "eval-5-robots-block-all": 13,
    "eval-6-cwv-technical-audit": 14,
}

def load_evals():
    with open(EVALS_PATH) as f:
        data = json.load(f)
    return {e["id"]: e for e in data["evals"]}

def evaluate_assertion(assertion, text):
    """Evaluate a single assertion against the response text. Returns (passed, evidence)."""
    atype = assertion.get("type", "")
    aid = assertion.get("id", "unknown")
    desc = assertion.get("description", "")

    if atype == "contains_pattern":
        pattern = assertion["pattern"]
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        if match:
            ctx_start = max(0, match.start() - 40)
            ctx_end = min(len(text), match.end() + 40)
            return True, f"Pattern matched: ...{text[ctx_start:ctx_end]}..."
        return False, f"Pattern '{pattern}' not found in response"

    elif atype == "contains_any":
        values = assertion.get("values", [])
        for v in values:
            if v.lower() in text.lower():
                idx = text.lower().index(v.lower())
                ctx_start = max(0, idx - 30)
                ctx_end = min(len(text), idx + len(v) + 30)
                return True, f"Found '{v}': ...{text[ctx_start:ctx_end]}..."
        return False, f"None of {values} found in response"

    elif atype == "contains_all":
        values = assertion.get("values", [])
        missing = [v for v in values if v.lower() not in text.lower()]
        if not missing:
            return True, f"All required values found: {values}"
        return False, f"Missing values: {missing}"

    elif atype == "not_contains_any":
        values = assertion.get("values", [])
        found = []
        for v in values:
            if v.lower() in text.lower():
                found.append(v)
        if not found:
            return True, f"Correctly does not contain any of {values}"
        return False, f"Incorrectly contains: {found}"

    elif atype == "not_contains_pattern":
        pattern = assertion["pattern"]
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        if match:
            ctx_start = max(0, match.start() - 40)
            ctx_end = min(len(text), match.end() + 40)
            return False, f"Pattern should NOT match but found: ...{text[ctx_start:ctx_end]}..."
        return True, f"Correctly does not match pattern '{pattern}'"

    return False, f"Unknown assertion type: {atype}"

def grade_run(eval_data, response_text):
    """Grade a single run against eval assertions."""
    assertions = eval_data.get("assertions", [])
    results = []
    passed_count = 0

    for assertion in assertions:
        passed, evidence = evaluate_assertion(assertion, response_text)
        if passed:
            passed_count += 1
        results.append({
            "text": assertion.get("description", assertion.get("id", "")),
            "passed": passed,
            "evidence": evidence
        })

    total = len(assertions)
    return {
        "expectations": results,
        "summary": {
            "passed": passed_count,
            "failed": total - passed_count,
            "total": total,
            "pass_rate": round(passed_count / total, 4) if total > 0 else 0.0
        }
    }

def main():
    evals = load_evals()
    graded = 0
    skipped = 0

    for eval_dir in sorted(WORKSPACE.glob("eval-*")):
        eval_name = eval_dir.name
        eval_id = EVAL_ID_MAP.get(eval_name)
        if eval_id is None:
            print(f"Skipping unknown eval: {eval_name}")
            continue

        eval_data = evals.get(eval_id)
        if eval_data is None:
            print(f"No eval data for id {eval_id}")
            continue

        for config_dir in sorted(eval_dir.iterdir()):
            if not config_dir.is_dir():
                continue
            config = config_dir.name
            if config not in ("with_skill", "without_skill"):
                continue

            for run_dir in sorted(config_dir.glob("run-*")):
                response_path = run_dir / "outputs" / "response.md"
                if not response_path.exists():
                    skipped += 1
                    continue

                response_text = response_path.read_text()
                if len(response_text) < 50:
                    print(f"WARNING: Very short response in {run_dir} ({len(response_text)} chars)")
                    skipped += 1
                    continue

                grading = grade_run(eval_data, response_text)
                grading["timing"] = {
                    "total_duration_seconds": 0.0
                }
                grading["execution_metrics"] = {
                    "output_chars": len(response_text),
                    "total_tool_calls": 0,
                    "errors_encountered": 0
                }

                grading_path = run_dir / "grading.json"
                with open(grading_path, "w") as f:
                    json.dump(grading, f, indent=2)

                status = "PASS" if grading["summary"]["pass_rate"] >= 0.5 else "FAIL"
                print(f"{status}: {eval_name}/{config}/{run_dir.name} — "
                      f"{grading['summary']['passed']}/{grading['summary']['total']} "
                      f"({grading['summary']['pass_rate']*100:.0f}%)")
                graded += 1

    print(f"\nGraded: {graded} runs, Skipped: {skipped} missing/empty responses")

if __name__ == "__main__":
    main()
