"""Shared code names for the HAIC codebook, sampler, and analysis.

Column names here are the contract with methods/codebook-v0.md.
Change them only when the codebook version changes.
"""

COST_CODES = [
    "clarification",
    "correction",
    "constraint_addition",
    "requirement_restoration",
    "repetition",
    "revision_request",
    "verification",
    "redirection",
]

NONCOST_TURN_CODES = [
    "acceptance_signal",
    "abandonment_signal",
    "supplies_requested_information",
    "social",
    "context_free_repair",
    "uninterpretable",
]

TURN_CODES = COST_CODES + NONCOST_TURN_CODES

ENDING_STATES = [
    "explicit_acceptance",
    "new_goal_after_use",
    "continued_repair",
    "explicit_abandonment",
    "indeterminate",
]

APPARENT_RESOLUTION = {"explicit_acceptance", "new_goal_after_use"}

TASK_TYPES = [
    "writing",
    "coding",
    "information_seeking",
    "planning",
    "creative_production",
    "other_task",
    "non_task",
]

QUOTA_TASK_TYPES = [
    "writing",
    "coding",
    "information_seeking",
    "planning",
    "creative_production",
    "other_task",
]

SCREEN_VALUES = ["task_oriented", "non_task", "uninterpretable"]

DATASET_ID = "allenai/WildChat-1M"
ENGLISH_LABELS = {"english", "en"}
PILOT_N = 40
POOL_N = 800
MAIN_TOTAL = 360
PER_TASK = 60
IRR_N = 80
DEFAULT_SEED = 20261001
