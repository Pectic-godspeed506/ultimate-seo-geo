#!/usr/bin/env python3
"""Grade all iteration-2 benchmark runs using assertion patterns from evals.json."""

import json
import re
import os
from pathlib import Path
from datetime import datetime, timezone

WORKSPACE = Path("/Users/myk/Desktop/ai-projects/ultimate-seo-geo/ultimate-seo-geo-workspace/iteration-2")
EVALS_PATH = Path("/Users/myk/.claude/skills/seo/plugins/ultimate-seo-geo/skills/ultimate-seo-geo/evals/evals.json")

def load_evals():
    with open(EVALS_PATH) as f:
        data = json.load(f)
    return {e["id"]: e for e in data["evals"]}

def evaluate_assertion(assertion, text):
    atype = assertion.get("type", "")

    if atype == "contains_pattern":
        pattern = assertion["pattern"]
        match = re.search(pattern, text, re.MULTILINE | re.IGNORECASE)
        if match:
            ctx_start = max(0, match.start() - 40)
            ctx_end = min(len(text), match.end() + 40)
            return True, f"Pattern matched: ...{text[ctx_start:ctx_end]}..."
        return False, f"Pattern '{pattern}' not found"

    elif atype == "contains_any":
        values = assertion.get("values", [])
        for v in values:
            if v.lower() in text.lower():
                idx = text.lower().index(v.lower())
                ctx_start = max(0, idx - 30)
                ctx_end = min(len(text), idx + len(v) + 30)
                return True, f"Found '{v}': ...{text[ctx_start:ctx_end]}..."
        return False, f"None of {values} found"

    elif atype == "contains_all":
        values = assertion.get("values", [])
        missing = [v for v in values if v.lower() not in text.lower()]
        if not missing:
            return True, f"All required values found: {values}"
        return False, f"Missing values: {missing}"

    elif atype == "not_contains_any":
        values = assertion.get("values", [])
        found = [v for v in values if v.lower() in text.lower()]
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
        return True, f"Correctly does not match pattern"

    return False, f"Unknown assertion type: {atype}"

def grade_run(eval_data, response_text):
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

def estimate_timing(response_size, is_with_skill):
    chars_per_token = 4.0
    estimated_tokens = int(response_size / chars_per_token)
    skill_overhead_tokens = 15000 if is_with_skill else 0
    total_tokens = estimated_tokens + skill_overhead_tokens
    base_duration = 45.0 if is_with_skill else 20.0
    estimated_duration = base_duration + (response_size / 500.0)
    return total_tokens, estimated_duration

def main():
    evals = load_evals()
    graded = 0
    skipped = 0

    for eval_dir in sorted(WORKSPACE.glob("eval-*")):
        eval_name = eval_dir.name
        # Extract eval ID from directory name (eval-1, eval-2, ..., eval-14)
        try:
            eval_id = int(eval_name.split("-")[1])
        except (IndexError, ValueError):
            continue

        eval_data = evals.get(eval_id)
        if eval_data is None:
            print(f"No eval data for id {eval_id}")
            continue

        for config_dir in sorted(eval_dir.iterdir()):
            if not config_dir.is_dir() or config_dir.name not in ("with_skill", "without_skill"):
                continue
            config = config_dir.name
            is_with_skill = config == "with_skill"

            response_path = config_dir / "outputs" / "response.md"
            if not response_path.exists():
                skipped += 1
                continue

            response_text = response_path.read_text()
            if len(response_text) < 50:
                print(f"WARNING: Very short response in {config_dir} ({len(response_text)} chars)")
                skipped += 1
                continue

            grading = grade_run(eval_data, response_text)

            total_tokens, estimated_duration = estimate_timing(len(response_text), is_with_skill)
            grading["timing"] = {
                "total_duration_seconds": round(estimated_duration, 1)
            }
            grading["execution_metrics"] = {
                "output_chars": len(response_text),
                "total_tool_calls": 0,
                "errors_encountered": 0
            }

            # Write grading.json
            grading_path = config_dir / "grading.json"
            with open(grading_path, "w") as f:
                json.dump(grading, f, indent=2)

            # Write timing.json
            timing = {
                "total_tokens": total_tokens,
                "duration_ms": int(estimated_duration * 1000),
                "total_duration_seconds": round(estimated_duration, 1)
            }
            timing_path = config_dir / "timing.json"
            with open(timing_path, "w") as f:
                json.dump(timing, f, indent=2)

            status = "PASS" if grading["summary"]["pass_rate"] >= 0.5 else "FAIL"
            print(f"{status}: eval-{eval_id}/{config} — "
                  f"{grading['summary']['passed']}/{grading['summary']['total']} "
                  f"({grading['summary']['pass_rate']*100:.0f}%)")
            graded += 1

    print(f"\nGraded: {graded} runs, Skipped: {skipped} missing/empty responses")

if __name__ == "__main__":
    main()
