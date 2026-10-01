"""Inter-rater reliability for the HAIC coding sheets.

Cohen's kappa is computed per binary turn code, and for task type and
ending state. Blank cells are unfinished coding, not zeros.
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

import numpy as np

ANALYSIS_DIR = Path(__file__).resolve().parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

from codes import COST_CODES, DEFAULT_SEED, ENDING_STATES, IRR_N, TASK_TYPES, TURN_CODES  # noqa: E402


def cohens_kappa(left, right):
    """Nominal Cohen's kappa. Returns None when agreement is undefined."""
    if len(left) != len(right):
        raise ValueError("rating lists differ in length")
    if not left:
        return None
    labels = sorted(set(left) | set(right), key=str)
    index = {label: position for position, label in enumerate(labels)}
    size = len(labels)
    matrix = [[0] * size for _ in range(size)]
    for a, b in zip(left, right):
        matrix[index[a]][index[b]] += 1
    n = len(left)
    observed = sum(matrix[i][i] for i in range(size)) / n
    row_rates = [sum(matrix[i]) / n for i in range(size)]
    col_rates = [sum(matrix[i][j] for i in range(size)) / n for j in range(size)]
    expected = sum(row_rates[i] * col_rates[i] for i in range(size))
    if expected == 1:
        return 1.0 if observed == 1 else None
    return (observed - expected) / (1 - expected)


def select_reliability_ids(sample_ids, n: int = IRR_N, seed: int = DEFAULT_SEED):
    ids = sorted(set(sample_ids))
    if n > len(ids):
        raise ValueError(f"requested {n} reliability conversations but only {len(ids)} are available")
    rng = np.random.default_rng(seed)
    chosen = rng.choice(len(ids), size=n, replace=False)
    return sorted(ids[int(i)] for i in chosen)


def _read_csv(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _pair_rows(primary, secondary, keys):
    def index(rows):
        found = {}
        for row in rows:
            key = tuple(row[name] for name in keys)
            if key in found:
                raise ValueError(f"duplicate key {key}")
            found[key] = row
        return found

    left = index(primary)
    right = index(secondary)
    shared = sorted(set(left) & set(right))
    only_left = sorted(set(left) - set(right))
    only_right = sorted(set(right) - set(left))
    return shared, left, right, only_left, only_right


def _as_binary(value, code, key):
    text = str(value).strip()
    if text == "":
        raise ValueError(f"blank {code} at {key}; enter 0 or 1")
    if text not in {"0", "1"}:
        raise ValueError(f"illegal {code} value {text!r} at {key}")
    return int(text)


def compare(primary_turns, secondary_turns, primary_conversations, secondary_conversations):
    turn_keys = ("sample_id", "user_turn_index")
    shared, left, right, only_left, only_right = _pair_rows(primary_turns, secondary_turns, turn_keys)
    if only_left or only_right:
        raise ValueError(
            f"turn sheets do not cover the same rows (only primary {len(only_left)}, only secondary {len(only_right)})"
        )
    reports = []
    for code in TURN_CODES:
        a = [_as_binary(left[key][code], code, key) for key in shared]
        b = [_as_binary(right[key][code], code, key) for key in shared]
        reports.append(
            {
                "variable": code,
                "level": "turn",
                "n": len(shared),
                "prevalence_primary": sum(a) / len(a) if a else None,
                "kappa": cohens_kappa(a, b),
                "role": "cost" if code in COST_CODES else "other",
            }
        )

    conv_keys = ("sample_id",)
    shared_c, left_c, right_c, missing_l, missing_r = _pair_rows(
        primary_conversations, secondary_conversations, conv_keys
    )
    if missing_l or missing_r:
        raise ValueError("conversation sheets do not cover the same sample ids")
    for field, allowed in (("task_type", set(TASK_TYPES)), ("ending_state", set(ENDING_STATES))):
        a = []
        b = []
        for key in shared_c:
            av = left_c[key][field].strip()
            bv = right_c[key][field].strip()
            if av not in allowed or bv not in allowed:
                raise ValueError(f"illegal {field} at {key}: {av!r} vs {bv!r}")
            a.append(av)
            b.append(bv)
        reports.append(
            {
                "variable": field,
                "level": "conversation",
                "n": len(shared_c),
                "prevalence_primary": None,
                "kappa": cohens_kappa(a, b),
                "role": "descriptor",
            }
        )
    return reports


def _fmt(value):
    if value is None:
        return "undefined"
    return f"{value:.3f}"


def write_report(reports, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Inter-rater reliability",
        "",
        "Cohen's kappa. A cost-code kappa below 0.70 means the codebook still needs revision before confirmatory reporting.",
        "",
        "| Variable | Level | N | Primary prevalence | Kappa | Role |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in reports:
        prevalence = "—" if row["prevalence_primary"] is None else f"{row['prevalence_primary']:.3f}"
        lines.append(
            f"| {row['variable']} | {row['level']} | {row['n']} | {prevalence} | {_fmt(row['kappa'])} | {row['role']} |"
        )
    below = [
        row["variable"]
        for row in reports
        if row["role"] == "cost" and (row["kappa"] is None or row["kappa"] < 0.70)
    ]
    lines.extend(["", "## Decision", ""])
    if below:
        lines.append(
            "Revise the codebook before confirmatory analysis. Kappa is under 0.70 or undefined for: "
            + ", ".join(below)
            + "."
        )
    else:
        lines.append("Every cost code has kappa of at least 0.70 on this overlap.")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute HAIC inter-rater reliability.")
    parser.add_argument("--select-from", type=Path, help="Manifest or conversation CSV whose sample_id column is the frame.")
    parser.add_argument("--n", type=int, default=IRR_N)
    parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    parser.add_argument("--out-ids", type=Path, default=Path("data/share/reliability-ids.csv"))
    parser.add_argument("--primary-turns", type=Path)
    parser.add_argument("--secondary-turns", type=Path)
    parser.add_argument("--primary-conversations", type=Path)
    parser.add_argument("--secondary-conversations", type=Path)
    parser.add_argument("--out", type=Path, default=Path("analysis/output/irr-report.md"))
    args = parser.parse_args()
    if args.select_from:
        with args.select_from.open(encoding="utf-8-sig", newline="") as handle:
            ids = [row["sample_id"] for row in csv.DictReader(handle)]
        chosen = select_reliability_ids(ids, args.n, args.seed)
        args.out_ids.parent.mkdir(parents=True, exist_ok=True)
        with args.out_ids.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["sample_id"])
            writer.writeheader()
            writer.writerows({"sample_id": sample_id} for sample_id in chosen)
        print(f"Wrote {len(chosen)} ids to {args.out_ids}")
        return
    required = [
        args.primary_turns,
        args.secondary_turns,
        args.primary_conversations,
        args.secondary_conversations,
    ]
    if any(path is None for path in required):
        raise SystemExit("Provide the four coding sheets, or pass --select-from to draw the reliability subset.")
    reports = compare(
        _read_csv(args.primary_turns),
        _read_csv(args.secondary_turns),
        _read_csv(args.primary_conversations),
        _read_csv(args.secondary_conversations),
    )
    write_report(reports, args.out)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
