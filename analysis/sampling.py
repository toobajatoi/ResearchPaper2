"""Pure sampling rules for the WildChat HAIC draw.

The Hugging Face download lives in sample_wildchat.py. Functions here
are deterministic and tested without the corpus.
"""

from __future__ import annotations

from collections import defaultdict

import numpy as np

from codes import ENGLISH_LABELS, QUOTA_TASK_TYPES


def normalize_language(value) -> str:
    if value is None:
        return ""
    return str(value).strip().casefold()


def is_english(value) -> bool:
    return normalize_language(value) in ENGLISH_LABELS


def message_text(turn) -> str:
    if not isinstance(turn, dict):
        return ""
    content = turn.get("content")
    if content is None:
        return ""
    return str(content).strip()


def turns_with_role(conversation, role: str):
    if not conversation:
        return []
    kept = []
    for turn in conversation:
        if not isinstance(turn, dict):
            continue
        if turn.get("role") != role:
            continue
        if not message_text(turn):
            continue
        kept.append(turn)
    return kept


def is_eligible(row) -> bool:
    """English conversation with at least one non-empty user and assistant turn."""
    if not isinstance(row, dict):
        return False
    if not is_english(row.get("language")):
        return False
    conversation = row.get("conversation") or []
    if not turns_with_role(conversation, "user"):
        return False
    if not turns_with_role(conversation, "assistant"):
        return False
    return True


def conversation_key(row) -> str:
    """Stable id. conversation_hash alone is not unique in WildChat-1M."""
    conversation = row.get("conversation") or []
    first_turn_id = ""
    for turn in conversation:
        if isinstance(turn, dict) and turn.get("turn_identifier") is not None:
            first_turn_id = str(turn.get("turn_identifier"))
            break
    timestamp = row.get("timestamp")
    if hasattr(timestamp, "isoformat"):
        timestamp = timestamp.isoformat()
    return f"{row.get('conversation_hash', '')}|{timestamp}|{first_turn_id}"


def word_count(text: str) -> int:
    return len([part for part in str(text).split() if part])


def iter_user_exchanges(conversation):
    """Yield user turns paired with the assistant text since the previous user turn."""
    pending_assistant = []
    user_index = 0
    for turn in conversation or []:
        if not isinstance(turn, dict):
            continue
        role = turn.get("role")
        text = message_text(turn)
        if role == "assistant":
            if text:
                pending_assistant.append(text)
            continue
        if role != "user" or not text:
            continue
        yield {
            "user_turn_index": user_index,
            "is_initial_request": int(user_index == 0),
            "user_text": text,
            "preceding_assistant_text": "\n\n".join(pending_assistant),
            "turn_identifier": turn.get("turn_identifier"),
        }
        user_index += 1
        pending_assistant = []


def reservoir_sample(items, k: int, rng: np.random.Generator):
    """Sample k items uniformly from a stream. Order of the reservoir is not shuffled."""
    if k < 0:
        raise ValueError("k must be non-negative")
    chosen = []
    seen = 0
    for item in items:
        seen += 1
        if len(chosen) < k:
            chosen.append(item)
            continue
        if k == 0:
            continue
        j = int(rng.integers(0, seen))
        if j < k:
            chosen[j] = item
    return chosen


def split_pilot_and_pool(sampled, pilot_n: int, rng: np.random.Generator):
    """Partition one simple random sample into a disjoint pilot and pool."""
    ordered = list(sampled)
    if pilot_n > len(ordered):
        raise ValueError("pilot_n exceeds the number of sampled conversations")
    order = rng.permutation(len(ordered))
    shuffled = [ordered[int(i)] for i in order]
    pilot = shuffled[:pilot_n]
    pool = shuffled[pilot_n:]
    return pilot, pool


def _take(items, n: int, rng: np.random.Generator):
    if n <= 0 or not items:
        return []
    if n >= len(items):
        return list(items)
    indices = rng.choice(len(items), size=n, replace=False)
    return [items[int(i)] for i in indices]


def _balance_turn_bands(items, n: int, rng: np.random.Generator):
    """Keep single-turn and multi-turn conversations in the same task quota."""
    ordered = sorted(items, key=lambda row: row["conversation_key"])
    single = [row for row in ordered if int(row["n_user_turns"]) <= 1]
    multi = [row for row in ordered if int(row["n_user_turns"]) > 1]
    if n >= len(ordered):
        return ordered
    if not single or not multi:
        return _take(ordered, n, rng)
    n_single = min(len(single), max(1, n // 2))
    n_multi = n - n_single
    if n_multi > len(multi):
        n_single += n_multi - len(multi)
        n_multi = len(multi)
    if n_single > len(single):
        n_multi += n_single - len(single)
        n_single = len(single)
    return _take(single, n_single, rng) + _take(multi, n_multi, rng)


def select_quota(conversations, per_task: int, total: int, seed: int):
    """Equal caps per observed task. Does not inflate a task to force `total`."""
    if per_task < 1:
        raise ValueError("per_task must be positive")
    if total < 1:
        raise ValueError("total must be positive")

    eligible = []
    for row in conversations:
        screen = str(row.get("screen", "")).strip()
        task = str(row.get("task_type", "")).strip()
        if screen != "task_oriented":
            continue
        if task not in QUOTA_TASK_TYPES:
            continue
        if row.get("n_user_turns") is None:
            raise ValueError(f"missing n_user_turns for {row.get('conversation_key')}")
        eligible.append(row)

    by_task = defaultdict(list)
    for row in eligible:
        by_task[row["task_type"]].append(row)

    present = [task for task in QUOTA_TASK_TYPES if by_task[task]]
    if not present:
        return [], {"present_tasks": [], "shortfall": {}, "selected": 0}

    capped = min(per_task, total // len(present))
    if capped < 1:
        capped = 1

    rng = np.random.default_rng(seed)
    selected = []
    shortfall = {}
    for task in present:
        ask = min(capped, len(by_task[task]))
        got = _balance_turn_bands(by_task[task], ask, rng)
        selected.extend(got)
        if len(got) < capped:
            shortfall[task] = {"requested": capped, "available": len(by_task[task]), "selected": len(got)}

    report = {
        "present_tasks": present,
        "per_task_cap": capped,
        "shortfall": shortfall,
        "selected": len(selected),
        "target_total": total,
    }
    return selected, report
