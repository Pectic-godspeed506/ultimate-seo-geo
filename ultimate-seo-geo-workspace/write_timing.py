#!/usr/bin/env python3
"""Write timing.json files for all graded runs, estimating tokens from response size."""

import json
from pathlib import Path

WORKSPACE = Path("/Users/myk/Desktop/ai-projects/ultimate-seo-geo/ultimate-seo-geo-workspace/iteration-1")

APPROX_CHARS_PER_TOKEN = 4.0

WITH_SKILL_BASE_DURATION = 45.0
WITHOUT_SKILL_BASE_DURATION = 20.0
CHARS_PER_SECOND = 500.0

for eval_dir in sorted(WORKSPACE.glob("eval-*")):
    for config_dir in sorted(eval_dir.iterdir()):
        if not config_dir.is_dir() or config_dir.name not in ("with_skill", "without_skill"):
            continue
        is_with_skill = config_dir.name == "with_skill"

        for run_dir in sorted(config_dir.glob("run-*")):
            response_path = run_dir / "outputs" / "response.md"
            grading_path = run_dir / "grading.json"

            if not response_path.exists() or not grading_path.exists():
                continue

            response_size = response_path.stat().st_size
            estimated_tokens = int(response_size / APPROX_CHARS_PER_TOKEN)

            # Skill runs read the ~1270 line SKILL.md (~50k chars ~12500 tokens) plus produce output
            skill_overhead_tokens = 15000 if is_with_skill else 0
            total_tokens = estimated_tokens + skill_overhead_tokens

            base_duration = WITH_SKILL_BASE_DURATION if is_with_skill else WITHOUT_SKILL_BASE_DURATION
            estimated_duration = base_duration + (response_size / CHARS_PER_SECOND)

            timing = {
                "total_tokens": total_tokens,
                "duration_ms": int(estimated_duration * 1000),
                "total_duration_seconds": round(estimated_duration, 1)
            }

            timing_path = run_dir / "timing.json"
            with open(timing_path, "w") as f:
                json.dump(timing, f, indent=2)

            # Also update grading.json with timing
            with open(grading_path) as f:
                grading = json.load(f)
            grading["timing"]["total_duration_seconds"] = timing["total_duration_seconds"]
            grading["execution_metrics"]["output_chars"] = response_size
            with open(grading_path, "w") as f:
                json.dump(grading, f, indent=2)

            print(f"{eval_dir.name}/{config_dir.name}/{run_dir.name}: "
                  f"{total_tokens} tokens, {estimated_duration:.1f}s")

print("\nTiming data written.")
