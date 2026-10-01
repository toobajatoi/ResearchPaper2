"""Tests for sampling rules, kappa, and the analysis halt on blank codes."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ANALYSIS_DIR = Path(__file__).resolve().parent
if str(ANALYSIS_DIR) not in sys.path:
    sys.path.insert(0, str(ANALYSIS_DIR))

from analyze import CodingError, conversation_metrics, load_sheets, rq1_table, write_results  # noqa: E402
from codes import COST_CODES  # noqa: E402
from irr import cohens_kappa, select_reliability_ids  # noqa: E402
from sampling import (  # noqa: E402
    conversation_key,
    is_eligible,
    iter_user_exchanges,
    reservoir_sample,
    select_quota,
    split_pilot_and_pool,
)


def _row(language="English", user="Please write an email", assistant="Here is a draft."):
    return {
        "language": language,
        "conversation_hash": "abc",
        "timestamp": "2024-01-01T00:00:00+00:00",
        "conversation": [
            {"role": "user", "content": user, "turn_identifier": 1},
            {"role": "assistant", "content": assistant, "turn_identifier": 2},
        ],
    }


class SamplingTests(unittest.TestCase):
    def test_eligibility(self):
        self.assertTrue(is_eligible(_row()))
        self.assertTrue(is_eligible(_row(language="en")))
        self.assertFalse(is_eligible(_row(language="Spanish")))
        self.assertFalse(is_eligible(_row(user="  ")))
        self.assertFalse(is_eligible(_row(assistant="")))

    def test_key_uses_hash_timestamp_and_turn(self):
        key = conversation_key(_row())
        self.assertEqual(key, "abc|2024-01-01T00:00:00+00:00|1")

    def test_exchanges_keep_preceding_assistant_text(self):
        conversation = [
            {"role": "user", "content": "First"},
            {"role": "assistant", "content": "Answer"},
            {"role": "user", "content": "Second"},
        ]
        exchanges = list(iter_user_exchanges(conversation))
        self.assertEqual(len(exchanges), 2)
        self.assertEqual(exchanges[0]["is_initial_request"], 1)
        self.assertEqual(exchanges[1]["preceding_assistant_text"], "Answer")
        self.assertEqual(exchanges[1]["is_initial_request"], 0)

    def test_reservoir_is_deterministic_and_bounded(self):
        first = reservoir_sample(range(100), 10, np.random.default_rng(20261001))
        second = reservoir_sample(range(100), 10, np.random.default_rng(20261001))
        self.assertEqual(first, second)
        self.assertEqual(len(first), 10)
        self.assertEqual(len(set(first)), 10)

    def test_pilot_and_pool_are_disjoint(self):
        sampled = list(range(30))
        pilot, pool = split_pilot_and_pool(sampled, 5, np.random.default_rng(1))
        self.assertEqual(len(pilot), 5)
        self.assertEqual(len(pool), 25)
        self.assertEqual(len(set(pilot) & set(pool)), 0)
        self.assertEqual(sorted(pilot + pool), sampled)

    def test_quota_caps_each_task_and_keeps_both_turn_bands(self):
        rows = []
        for task in ("writing", "coding"):
            for index in range(10):
                rows.append(
                    {
                        "sample_id": f"{task}-{index}",
                        "conversation_key": f"{task}-{index}",
                        "screen": "task_oriented",
                        "task_type": task,
                        "n_user_turns": 1 if index < 4 else 3,
                    }
                )
        rows.append(
            {
                "sample_id": "chat",
                "conversation_key": "chat",
                "screen": "non_task",
                "task_type": "non_task",
                "n_user_turns": 2,
            }
        )
        selected, report = select_quota(rows, per_task=60, total=360, seed=7)
        self.assertEqual(report["selected"], 20)
        self.assertTrue(all(row["screen"] == "task_oriented" for row in selected))
        writing = [row for row in selected if row["task_type"] == "writing"]
        self.assertTrue(any(row["n_user_turns"] == 1 for row in writing))
        self.assertTrue(any(row["n_user_turns"] > 1 for row in writing))


class ReliabilityTests(unittest.TestCase):
    def test_known_kappa(self):
        kappa = cohens_kappa([1, 1, 1, 0, 0], [1, 1, 0, 0, 0])
        self.assertAlmostEqual(kappa, (0.8 - 0.48) / 0.52)

    def test_perfect_agreement(self):
        self.assertEqual(cohens_kappa([1, 0, 1], [1, 0, 1]), 1.0)

    def test_reliability_draw_is_stable(self):
        ids = [f"S{i:04d}" for i in range(100)]
        self.assertEqual(select_reliability_ids(ids, 80, 20261001), select_reliability_ids(ids, 80, 20261001))
        self.assertEqual(len(select_reliability_ids(ids, 80, 20261001)), 80)


class AnalysisTests(unittest.TestCase):
    def _sheets(self, blank=False):
        turn_rows = []
        conversation_rows = []
        for index in range(4):
            sample_id = f"M{index}"
            conversation_rows.append(
                {
                    "sample_id": sample_id,
                    "screen": "task_oriented",
                    "task_type": "writing" if index < 2 else "coding",
                    "ending_state": "indeterminate" if index == 0 else "continued_repair",
                }
            )
            for turn_index, initial in ((0, 1), (1, 0), (2, 0)):
                row = {
                    "sample_id": sample_id,
                    "user_turn_index": turn_index,
                    "is_initial_request": initial,
                    "user_text": "Write the email" if initial else "Make it shorter",
                }
                for code in COST_CODES:
                    row[code] = "" if blank and index == 0 else "0"
                if not initial and not blank:
                    row["revision_request"] = "1" if turn_index == 1 else "0"
                turn_rows.append(row)
        return pd.DataFrame(turn_rows), pd.DataFrame(conversation_rows)

    def test_preterminal_window_excludes_initial_and_last_turn(self):
        turns, conversations = self._sheets()
        metrics = conversation_metrics(turns, conversations)
        sample = metrics[metrics["sample_id"] == "M1"].iloc[0]
        self.assertEqual(sample["n_post"], 2)
        self.assertEqual(sample["n_preterminal"], 1)
        self.assertEqual(sample["post_revision_request"], 1)
        self.assertEqual(sample["pre_revision_request"], 1)

    def test_blank_codes_halt(self):
        turns, conversations = self._sheets(blank=True)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            turns.to_csv(root / "turns.csv", index=False)
            conversations.to_csv(root / "conversations.csv", index=False)
            with self.assertRaises(CodingError):
                load_sheets(root / "turns.csv", root / "conversations.csv")

    def test_rq1_counts_conversations_rather_than_inventing_a_score(self):
        turns, conversations = self._sheets()
        metrics = conversation_metrics(turns, conversations)
        table = rq1_table(metrics)
        revision = table[table["code"] == "revision_request"].iloc[0]
        self.assertEqual(int(revision["conversations_with_code"]), 4)
        with tempfile.TemporaryDirectory() as tmp:
            write_results(metrics, Path(tmp))
            self.assertTrue((Path(tmp) / "results-tables.md").exists())
            text = (Path(tmp) / "results-tables.md").read_text(encoding="utf-8")
            self.assertIn("Interface principles are not generated here.", text)


if __name__ == "__main__":
    unittest.main()
