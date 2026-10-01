"""Confirmatory summaries for a finished HAIC coding sheet.

The script stops if any required cell is blank. It writes tables only.
It does not draft interface principles or fill the manuscript.
"""

from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

ANALYSIS_DIR = Path(__file__).resolve().parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

from codes import (  # noqa: E402
    APPARENT_RESOLUTION,
    COST_CODES,
    ENDING_STATES,
    SCREEN_VALUES,
    TASK_TYPES,
)


class CodingError(Exception):
    pass


def _blank_mask(series: pd.Series) -> pd.Series:
    return series.isna() | series.astype(str).str.strip().eq("")


def load_sheets(turns_path: Path, conversations_path: Path):
    turns = pd.read_csv(turns_path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
    conversations = pd.read_csv(
        conversations_path, dtype=str, keep_default_na=False, encoding="utf-8-sig"
    )
    required_turns = ["sample_id", "user_turn_index", "is_initial_request", "user_text", *COST_CODES]
    required_conversations = ["sample_id", "screen", "task_type", "ending_state"]
    for name in required_turns:
        if name not in turns.columns:
            raise CodingError(f"turns sheet is missing {name}")
    for name in required_conversations:
        if name not in conversations.columns:
            raise CodingError(f"conversations sheet is missing {name}")

    unfinished = []
    for name in ["screen", "task_type", "ending_state"]:
        unfinished.extend(conversations.loc[_blank_mask(conversations[name]), "sample_id"].tolist())
    for name in COST_CODES:
        bad = turns.loc[_blank_mask(turns[name]), "sample_id"]
        unfinished.extend(bad.tolist())
    if unfinished:
        shown = ", ".join(sorted(set(unfinished))[:12])
        raise CodingError(f"blank required codes remain, including: {shown}")

    for name in COST_CODES:
        illegal = ~turns[name].astype(str).str.strip().isin(["0", "1"])
        if illegal.any():
            raise CodingError(f"{name} contains values other than 0 and 1")
        turns[name] = turns[name].astype(int)
    turns["user_turn_index"] = turns["user_turn_index"].astype(int)
    turns["is_initial_request"] = turns["is_initial_request"].astype(int)
    conversations["screen"] = conversations["screen"].str.strip()
    conversations["task_type"] = conversations["task_type"].str.strip()
    conversations["ending_state"] = conversations["ending_state"].str.strip()
    bad_screen = ~conversations["screen"].isin(SCREEN_VALUES)
    bad_task = ~conversations["task_type"].isin(TASK_TYPES)
    bad_ending = ~conversations["ending_state"].isin(ENDING_STATES)
    if bad_screen.any() or bad_task.any() or bad_ending.any():
        raise CodingError("screen, task_type, or ending_state contains a value outside the codebook")
    return turns, conversations


def _wilson(successes: int, n: int, z: float = 1.96):
    if n == 0:
        return None, None
    p = successes / n
    denom = 1 + z**2 / n
    center = (p + z**2 / (2 * n)) / denom
    margin = z * math.sqrt(p * (1 - p) / n + z**2 / (4 * n**2)) / denom
    return center - margin, center + margin


def conversation_metrics(turns: pd.DataFrame, conversations: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for sample_id, group in turns.groupby("sample_id", sort=True):
        group = group.sort_values("user_turn_index").copy()
        for code in COST_CODES:
            group[code] = pd.to_numeric(group[code], errors="raise")
        group["is_initial_request"] = pd.to_numeric(group["is_initial_request"], errors="raise")
        initial = group[group["is_initial_request"] == 1]
        if initial.empty:
            raise CodingError(f"{sample_id} has no initial request row")
        post = group[group["is_initial_request"] == 0]
        last_index = int(group["user_turn_index"].max())
        preterminal = post[post["user_turn_index"] < last_index]
        initial_words = len(str(initial.iloc[0]["user_text"]).split())
        record = {
            "sample_id": sample_id,
            "n_user_turns": int(len(group)),
            "n_post": int(len(post)),
            "n_preterminal": int(len(preterminal)),
            "initial_request_words": initial_words,
        }
        for code in COST_CODES:
            record[f"post_{code}"] = int(post[code].sum()) if len(post) else 0
            record[f"pre_{code}"] = int(preterminal[code].sum()) if len(preterminal) else 0
            record[f"rate_post_{code}"] = record[f"post_{code}"] / len(post) if len(post) else 0.0
            record[f"rate_pre_{code}"] = (
                record[f"pre_{code}"] / len(preterminal) if len(preterminal) else 0.0
            )
            record[f"any_{code}"] = int(record[f"post_{code}"] > 0)
        rows.append(record)
    metrics = pd.DataFrame(rows)
    merged = metrics.merge(
        conversations[["sample_id", "screen", "task_type", "ending_state"]],
        on="sample_id",
        how="left",
        validate="one_to_one",
    )
    if merged["ending_state"].isna().any():
        raise CodingError("a turns sample_id has no conversation row")
    return merged


def _md_table(frame: pd.DataFrame) -> str:
    shown = frame.copy()
    for column in shown.columns:
        if pd.api.types.is_float_dtype(shown[column]):
            shown[column] = shown[column].map(lambda value: "" if pd.isna(value) else f"{value:.3f}")
    header = "| " + " | ".join(shown.columns) + " |"
    rule = "| " + " | ".join("---" for _ in shown.columns) + " |"
    body = ["| " + " | ".join(str(value) for value in row) + " |" for row in shown.itertuples(index=False)]
    return "\n".join([header, rule, *body])


def rq1_table(metrics: pd.DataFrame) -> pd.DataFrame:
    n = len(metrics)
    rows = []
    for code in COST_CODES:
        successes = int(metrics[f"any_{code}"].sum())
        low, high = _wilson(successes, n)
        rows.append(
            {
                "code": code,
                "conversations_with_code": successes,
                "proportion": successes / n if n else None,
                "wilson_low": low,
                "wilson_high": high,
                "coded_post_request_turns": int(metrics[f"post_{code}"].sum()),
            }
        )
    return pd.DataFrame(rows)


def rq2_tables(metrics: pd.DataFrame):
    analytic = metrics[metrics["screen"] == "task_oriented"].copy()
    presence_rows = []
    kw_rows = []
    for code in COST_CODES:
        counts = pd.crosstab(analytic["task_type"], analytic[f"any_{code}"])
        if counts.shape[0] > 1 and counts.shape[1] > 1:
            chi2, p_value, dof, _ = stats.chi2_contingency(counts)
        else:
            chi2, p_value, dof = None, None, None
        presence_rows.append({"code": code, "chi2": chi2, "dof": dof, "p": p_value})
        grouped = [group[f"rate_post_{code}"].to_numpy() for _, group in analytic.groupby("task_type")]
        grouped = [values for values in grouped if len(values)]
        combined = np.concatenate(grouped) if grouped else np.array([])
        if len(grouped) > 1 and np.unique(combined).size > 1:
            h_stat, h_p = stats.kruskal(*grouped)
        else:
            h_stat, h_p = None, None
        kw_rows.append({"code": code, "H": h_stat, "p": h_p})
    composition = (
        analytic.groupby("task_type")[[f"rate_post_{code}" for code in COST_CODES]]
        .mean()
        .reset_index()
    )
    return pd.DataFrame(presence_rows), pd.DataFrame(kw_rows), composition


def _ending_group(value: str) -> str:
    if value in APPARENT_RESOLUTION:
        return "apparent_resolution"
    return value


def rq3_model(metrics: pd.DataFrame):
    analytic = metrics[metrics["screen"] == "task_oriented"].copy()
    analytic["ending_group"] = analytic["ending_state"].map(_ending_group)
    counts = analytic["ending_group"].value_counts()
    keep = counts[counts >= 15].index.tolist()
    notes = []
    dropped = sorted(set(counts.index) - set(keep))
    if dropped:
        notes.append(
            "Ending groups with fewer than 15 conversations were omitted from the model: "
            + ", ".join(dropped)
            + "."
        )
    model_frame = analytic[analytic["ending_group"].isin(keep)].copy()
    rate_columns = []
    for code in COST_CODES:
        column = f"rate_pre_{code}"
        if model_frame[column].std(ddof=0) == 0:
            notes.append(f"{code} had no variance in the pre-terminal rates and was omitted.")
            continue
        rate_columns.append(column)
    if len(keep) < 2 or not rate_columns or model_frame["task_type"].nunique() < 1:
        notes.append("The regression was not fit because the coded sheet does not support it yet.")
        return None, notes

    try:
        import statsmodels.formula.api as smf
    except ImportError:
        notes.append("statsmodels is not installed, so the regression was not fit.")
        return None, notes

    formula = (
        "ending_group ~ "
        + " + ".join(rate_columns)
        + " + C(task_type) + log_initial_words"
    )
    model_frame["log_initial_words"] = np.log1p(model_frame["initial_request_words"].astype(float))
    # Indeterminate is the reference when it remains in the model.
    if "indeterminate" in keep:
        model_frame["ending_group"] = pd.Categorical(
            model_frame["ending_group"],
            categories=["indeterminate", *[name for name in keep if name != "indeterminate"]],
        )
    try:
        fit = smf.mnlogit(formula, data=model_frame).fit(disp=False, maxiter=200)
    except Exception as exc:  # statsmodels raises several numerical errors
        notes.append(f"The regression did not converge ({exc.__class__.__name__}).")
        return None, notes
    notes.append(
        "Coefficients are associations. Pre-terminal rates exclude the initial request and the last user turn."
    )
    return fit, notes


def rq4_candidates(metrics: pd.DataFrame, per_group: int = 8) -> pd.DataFrame:
    analytic = metrics[metrics["screen"] == "task_oriented"].copy()
    analytic["cost_count"] = analytic[[f"pre_{code}" for code in COST_CODES]].sum(axis=1)
    analytic["ending_group"] = analytic["ending_state"].map(_ending_group)
    resolved = analytic[analytic["ending_group"] == "apparent_resolution"]
    unresolved = analytic[analytic["ending_group"].isin(["continued_repair", "explicit_abandonment"])]
    picks = []
    if not resolved.empty:
        cutoff = resolved["cost_count"].quantile(0.25)
        low = resolved[resolved["cost_count"] <= cutoff].sort_values(["cost_count", "sample_id"])
        picks.append(low.head(per_group).assign(qualitative_group="lower_cost_resolved"))
    if not unresolved.empty:
        cutoff = unresolved["cost_count"].quantile(0.75)
        high = unresolved[unresolved["cost_count"] >= cutoff].sort_values(
            ["cost_count", "sample_id"], ascending=[False, True]
        )
        picks.append(high.head(per_group).assign(qualitative_group="higher_cost_unresolved"))
    if not picks:
        return pd.DataFrame(columns=["sample_id", "qualitative_group", "ending_state", "cost_count"])
    chosen = pd.concat(picks, ignore_index=True)
    return chosen[["sample_id", "qualitative_group", "ending_state", "task_type", "cost_count"]]


def write_results(metrics: pd.DataFrame, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    rq1 = rq1_table(metrics)
    chi, kruskal, composition = rq2_tables(metrics)
    fit, notes = rq3_model(metrics)
    candidates = rq4_candidates(metrics)
    lines = [
        "# Computed tables",
        "",
        "These tables are inputs to the results section. They are not the manuscript.",
        "Interface principles are not generated here.",
        "",
        f"Conversations in the sheet: {len(metrics)}.",
        "",
        "## RQ1",
        "",
        _md_table(rq1),
        "",
        "## RQ2 presence",
        "",
        _md_table(chi),
        "",
        "## RQ2 Kruskal-Wallis on post-request rates",
        "",
        _md_table(kruskal),
        "",
        "## RQ2 mean post-request rates by task",
        "",
        _md_table(composition),
        "",
        "## RQ3",
        "",
    ]
    if fit is None:
        lines.append("No regression table.")
    else:
        lines.append("```")
        lines.append(str(fit.summary()))
        lines.append("```")
    lines.extend(["", *notes, "", "## RQ4 candidate packets", ""])
    if candidates.empty:
        lines.append("No candidate packets. The sheet has no coded resolution or non-resolution contrast yet.")
    else:
        lines.append(_md_table(candidates))
        lines.append("")
        lines.append("Read these packets for the qualitative comparison. Write the design implications by hand.")
    (out_dir / "results-tables.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    rq1.to_csv(out_dir / "rq1.csv", index=False)
    candidates.to_csv(out_dir / "rq4-candidates.csv", index=False)


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize a finished HAIC coding sheet.")
    parser.add_argument("--turns", type=Path, required=True)
    parser.add_argument("--conversations", type=Path, required=True)
    parser.add_argument("--out", type=Path, default=Path("analysis/output"))
    args = parser.parse_args()
    turns, conversations = load_sheets(args.turns, args.conversations)
    metrics = conversation_metrics(turns, conversations)
    write_results(metrics, args.out)
    print(f"Wrote tables to {args.out}")


if __name__ == "__main__":
    main()
