"""Diagnostics that show which v0 codes the pilot actually used.

Run this after the 40 pilot conversations are coded. Use the output to
decide merges and splits. This script does not rewrite the codebook.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

ANALYSIS_DIR = Path(__file__).resolve().parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

from analyze import CodingError, load_sheets  # noqa: E402
from codes import COST_CODES  # noqa: E402


def diagnostics(turns: pd.DataFrame, conversations: pd.DataFrame) -> str:
    post = turns[turns["is_initial_request"].astype(int) == 0]
    lines = [
        "# Pilot diagnostics",
        "",
        f"Conversations: {conversations['sample_id'].nunique()}.",
        f"Post-request user turns: {len(post)}.",
        "",
        "## Cost-code frequency on post-request turns",
        "",
        "| Code | Turns | Turn proportion | Conversations with at least one |",
        "| --- | --- | --- | --- |",
    ]
    for code in COST_CODES:
        turns_with = int(post[code].sum()) if len(post) else 0
        proportion = turns_with / len(post) if len(post) else 0
        conversations_with = int(post.loc[post[code] == 1, "sample_id"].nunique()) if len(post) else 0
        lines.append(f"| {code} | {turns_with} | {proportion:.3f} | {conversations_with} |")

    lines.extend(["", "## Pairwise co-occurrence on post-request turns", ""])
    if post.empty:
        lines.append("No post-request turns were coded.")
    else:
        lines.append("| Code A | Code B | Turns with both |")
        lines.append("| --- | --- | --- |")
        for i, left in enumerate(COST_CODES):
            for right in COST_CODES[i + 1 :]:
                both = int(((post[left] == 1) & (post[right] == 1)).sum())
                if both:
                    lines.append(f"| {left} | {right} | {both} |")
    initial_cost = turns[turns["is_initial_request"].astype(int) == 1]
    violations = int(initial_cost[COST_CODES].sum().sum()) if len(initial_cost) else 0
    lines.extend(
        [
            "",
            "## Rule check",
            "",
            f"Cost codes marked on initial-request rows: {violations}. The codebook sets those to 0.",
            "",
            "A code with zero turns is a candidate to drop or to redefine with a clearer example.",
            "A pair that always occurs together is a candidate to merge.",
            "Write the decision in methods/codebook-changelog.md and publish it as codebook v1.",
            "Do not change confirmatory labels by editing v0 after the main sample is coded.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Describe pilot codes before codebook revision.")
    parser.add_argument("--turns", type=Path, default=Path("data/local/pilot/turns.csv"))
    parser.add_argument("--conversations", type=Path, default=Path("data/local/pilot/conversations.csv"))
    parser.add_argument("--out", type=Path, default=Path("analysis/output/pilot-diagnostics.md"))
    args = parser.parse_args()
    if not args.turns.exists() or not args.conversations.exists():
        raise SystemExit(
            "Pilot coding sheets are not in data/local/pilot/. "
            "Draw the sample, code the 40 packets by hand, then run this again."
        )
    try:
        turns, conversations = load_sheets(args.turns, args.conversations)
    except CodingError as exc:
        raise SystemExit(f"Pilot sheet is unfinished: {exc}") from exc
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(diagnostics(turns, conversations), encoding="utf-8")
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
