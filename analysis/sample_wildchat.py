"""Draw the WildChat-1M English pilot and screening pool in one pass.

Message text is written only under data/local/. The shareable manifest
contains keys and counts, not messages.

Usage, from the project root:

    python analysis/sample_wildchat.py draw
    python analysis/sample_wildchat.py quota --conversations data/local/pool/conversations.csv
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import numpy as np

ANALYSIS_DIR = Path(__file__).resolve().parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

from codes import (  # noqa: E402
    DATASET_ID,
    DEFAULT_SEED,
    MAIN_TOTAL,
    PER_TASK,
    PILOT_N,
    POOL_N,
    TURN_CODES,
)
from sampling import (  # noqa: E402
    conversation_key,
    is_eligible,
    iter_user_exchanges,
    reservoir_sample,
    select_quota,
    split_pilot_and_pool,
    turns_with_role,
    word_count,
)

PROJECT_ROOT = ANALYSIS_DIR.parent
LOCAL_ROOT = PROJECT_ROOT / "data" / "local"
SHARE_ROOT = PROJECT_ROOT / "data" / "share"


def minimal_record(row) -> dict:
    """Drop location, network, and moderation fields before anything is saved."""
    conversation = []
    for turn in row.get("conversation") or []:
        if not isinstance(turn, dict):
            continue
        role = turn.get("role")
        if role not in {"user", "assistant"}:
            continue
        conversation.append(
            {
                "role": role,
                "content": turn.get("content") or "",
                "language": turn.get("language"),
                "redacted": bool(turn.get("redacted")),
                "turn_identifier": turn.get("turn_identifier"),
            }
        )
    timestamp = row.get("timestamp")
    if hasattr(timestamp, "isoformat"):
        timestamp = timestamp.isoformat()
    kept = {
        "conversation_hash": row.get("conversation_hash"),
        "model": row.get("model"),
        "timestamp": timestamp,
        "language": row.get("language"),
        "redacted": bool(row.get("redacted")),
        "conversation": conversation,
    }
    kept["conversation_key"] = conversation_key(kept)
    return kept


def packet_text(sample_id: str, record: dict) -> str:
    lines = [
        f"SAMPLE_ID: {sample_id}",
        f"KEY: {record['conversation_key']}",
        f"MODEL: {record.get('model')}",
        f"REDACTED: {record.get('redacted')}",
        "",
        "Code this packet with methods/codebook-v0.md.",
        "Do not copy the message text into the deposited annotation file.",
        "",
    ]
    pending = []
    user_index = 0
    for turn in record["conversation"]:
        text = (turn.get("content") or "").strip()
        if turn.get("role") == "assistant":
            if text:
                pending.append(text)
            continue
        if turn.get("role") != "user" or not text:
            continue
        if pending:
            lines.append("--- ASSISTANT ---")
            lines.append("\n\n".join(pending))
            lines.append("")
            pending = []
        label = "initial request" if user_index == 0 else "post-request"
        lines.append(f"--- USER TURN {user_index} ({label}) ---")
        lines.append(text)
        lines.append("")
        user_index += 1
    if pending:
        lines.append("--- ASSISTANT ---")
        lines.append("\n\n".join(pending))
        lines.append("")
    return "\n".join(lines)


def write_split(split_name: str, records: list[dict], id_prefix: str, width: int) -> None:
    local_dir = LOCAL_ROOT / split_name
    packet_dir = local_dir / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    SHARE_ROOT.mkdir(parents=True, exist_ok=True)

    manifest_fields = [
        "sample_id",
        "conversation_key",
        "model",
        "timestamp",
        "n_user_turns",
        "n_assistant_turns",
        "initial_request_words",
        "redacted",
        "split",
    ]
    conversation_fields = [
        "sample_id",
        "conversation_key",
        "screen",
        "task_type",
        "ending_state",
        "ending_notes",
        "coder_id",
    ]
    turn_fields = [
        "sample_id",
        "conversation_key",
        "user_turn_index",
        "is_initial_request",
        "user_text",
        "preceding_assistant_text",
        "coder_id",
        *TURN_CODES,
    ]

    manifest_rows = []
    conversation_rows = []
    turn_rows = []

    for index, record in enumerate(records, start=1):
        sample_id = f"{id_prefix}{index:0{width}d}"
        users = turns_with_role(record["conversation"], "user")
        assistants = turns_with_role(record["conversation"], "assistant")
        initial_words = word_count(users[0].get("content", "")) if users else 0
        manifest_rows.append(
            {
                "sample_id": sample_id,
                "conversation_key": record["conversation_key"],
                "model": record.get("model"),
                "timestamp": record.get("timestamp"),
                "n_user_turns": len(users),
                "n_assistant_turns": len(assistants),
                "initial_request_words": initial_words,
                "redacted": record.get("redacted"),
                "split": split_name,
            }
        )
        conversation_rows.append(
            {
                "sample_id": sample_id,
                "conversation_key": record["conversation_key"],
                "screen": "",
                "task_type": "",
                "ending_state": "",
                "ending_notes": "",
                "coder_id": "",
            }
        )
        for exchange in iter_user_exchanges(record["conversation"]):
            row = {
                "sample_id": sample_id,
                "conversation_key": record["conversation_key"],
                "user_turn_index": exchange["user_turn_index"],
                "is_initial_request": exchange["is_initial_request"],
                "user_text": exchange["user_text"],
                "preceding_assistant_text": exchange["preceding_assistant_text"],
                "coder_id": "",
            }
            for code in TURN_CODES:
                row[code] = ""
            turn_rows.append(row)
        (packet_dir / f"{sample_id}.txt").write_text(
            packet_text(sample_id, record), encoding="utf-8"
        )

    _write_csv(SHARE_ROOT / f"{split_name}-manifest.csv", manifest_fields, manifest_rows)
    _write_csv(local_dir / "conversations.csv", conversation_fields, conversation_rows)
    _write_csv(local_dir / "turns.csv", turn_fields, turn_rows)
    (local_dir / "records.jsonl").write_text(
        "\n".join(json.dumps(record, ensure_ascii=False) for record in records) + "\n",
        encoding="utf-8",
    )


def _write_csv(path: Path, fields: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def dataset_revision(revision: str | None) -> str:
    from huggingface_hub import HfApi

    if revision:
        return revision
    info = HfApi().dataset_info(DATASET_ID)
    return info.sha


def draw(pilot_n: int, pool_n: int, seed: int, revision: str | None) -> None:
    from datasets import load_dataset

    pinned = dataset_revision(revision)
    rng = np.random.default_rng(seed)
    stream = load_dataset(DATASET_ID, split="train", revision=pinned, streaming=True)
    eligible = (minimal_record(row) for row in stream if is_eligible(row))
    sampled = reservoir_sample(eligible, pilot_n + pool_n, rng)
    if len(sampled) < pilot_n:
        raise SystemExit(f"Only {len(sampled)} eligible conversations were found.")
    pilot, pool = split_pilot_and_pool(sampled, pilot_n, rng)
    write_split("pilot", pilot, "P", 3)
    write_split("pool", pool, "S", 4)
    meta = {
        "dataset": DATASET_ID,
        "revision": pinned,
        "seed": seed,
        "pilot_n": len(pilot),
        "pool_n": len(pool),
        "drawn_at_utc": datetime.now(timezone.utc).isoformat(),
        "filters": [
            "conversation language is English",
            "at least one non-empty user turn",
            "at least one non-empty assistant turn",
        ],
        "omitted_fields": ["country", "state", "hashed_ip", "header", "openai_moderation", "detoxify_moderation"],
    }
    (SHARE_ROOT / "draw-metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Pilot: {len(pilot)} conversations in data/local/pilot")
    print(f"Pool: {len(pool)} conversations in data/local/pool")
    print(f"Manifests without message text: {SHARE_ROOT}")
    print(f"Dataset revision: {pinned}")


def quota(conversations_path: Path, per_task: int, total: int, seed: int) -> None:
    with conversations_path.open(encoding="utf-8-sig", newline="") as handle:
        coded = list(csv.DictReader(handle))
    manifest_path = SHARE_ROOT / "pool-manifest.csv"
    if not manifest_path.exists():
        raise SystemExit("Missing data/share/pool-manifest.csv. Run draw first.")
    with manifest_path.open(encoding="utf-8-sig", newline="") as handle:
        manifest = {row["sample_id"]: row for row in csv.DictReader(handle)}

    joined = []
    for row in coded:
        sample_id = row["sample_id"]
        if sample_id not in manifest:
            raise SystemExit(f"{sample_id} is not in the pool manifest.")
        if not str(row.get("screen", "")).strip() or not str(row.get("task_type", "")).strip():
            raise SystemExit(f"{sample_id} is missing screen or task_type.")
        item = dict(manifest[sample_id])
        item["screen"] = row["screen"].strip()
        item["task_type"] = row["task_type"].strip()
        item["n_user_turns"] = int(item["n_user_turns"])
        joined.append(item)

    selected, report = select_quota(joined, per_task=per_task, total=total, seed=seed)
    selected_ids = {row["sample_id"] for row in selected}
    main_dir = LOCAL_ROOT / "main"
    main_dir.mkdir(parents=True, exist_ok=True)

    def filter_csv(source: Path, dest: Path) -> None:
        with source.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            fields = reader.fieldnames or []
            rows = [row for row in reader if row["sample_id"] in selected_ids]
        _write_csv(dest, list(fields), rows)

    filter_csv(LOCAL_ROOT / "pool" / "conversations.csv", main_dir / "conversations.csv")
    filter_csv(LOCAL_ROOT / "pool" / "turns.csv", main_dir / "turns.csv")
    _write_csv(
        SHARE_ROOT / "main-manifest.csv",
        list(manifest[next(iter(manifest))].keys()) if manifest else ["sample_id"],
        selected,
    )
    (SHARE_ROOT / "quota-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    packet_dir = main_dir / "packets"
    packet_dir.mkdir(parents=True, exist_ok=True)
    for sample_id in selected_ids:
        source = LOCAL_ROOT / "pool" / "packets" / f"{sample_id}.txt"
        if source.exists():
            (packet_dir / f"{sample_id}.txt").write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    print(f"Main sample: {len(selected)} conversations in data/local/main")
    print(json.dumps(report, indent=2))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Sample English WildChat-1M conversations for HAIC coding.")
    sub = parser.add_subparsers(dest="command", required=True)

    draw_parser = sub.add_parser("draw", help="One-pass pilot and pool sample.")
    draw_parser.add_argument("--pilot-n", type=int, default=PILOT_N)
    draw_parser.add_argument("--pool-n", type=int, default=POOL_N)
    draw_parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    draw_parser.add_argument("--revision", default=None, help="Pin a Hugging Face dataset revision.")

    quota_parser = sub.add_parser("quota", help="Select the main sample from a screened pool.")
    quota_parser.add_argument("--conversations", type=Path, required=True)
    quota_parser.add_argument("--per-task", type=int, default=PER_TASK)
    quota_parser.add_argument("--total", type=int, default=MAIN_TOTAL)
    quota_parser.add_argument("--seed", type=int, default=DEFAULT_SEED)
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "draw":
        draw(args.pilot_n, args.pool_n, args.seed, args.revision)
    elif args.command == "quota":
        quota(args.conversations, args.per_task, args.total, args.seed)


if __name__ == "__main__":
    main()
