# Sampling protocol

This protocol is the sampling section of the manuscript. The script that implements it is `analysis/sample_wildchat.py`. Inclusion rules that do not touch the corpus live in `analysis/sampling.py` and are covered by `analysis/test_pipeline.py`.

## Frame

The frame is the public, non-toxic Hugging Face release `allenai/WildChat-1M` (Zhao et al., 2024). The dataset card current at the time of this protocol lists 837,989 conversations. Toxic conversations flagged by the OpenAI Moderations API or Detoxify were removed on 22 July 2024. A further removal of conversations flagged for personal or sensitive information was applied on 17 October 2024. The license is the Open Data Commons Attribution License (ODC-BY).

The original one-million-conversation collection, the gated full release that still contains toxic conversations, and any later multi-million release are outside this frame. Estimates will not be described as properties of “all of WildChat.”

WildChat was collected by offering users access to GPT-3.5 and GPT-4 in exchange for research use of the chats, with affirmative opt-in. This study adds no participants and no model API.

## What is kept and what is dropped before sampling

A conversation is eligible when all of the following hold:

- The conversation-level `language` field is English (`English` or `en`, compared without case sensitivity). That field is the most frequent detected language of the utterances.
- At least one user message has non-empty text after stripping whitespace.
- At least one assistant message has non-empty text after stripping whitespace.

Empty user submissions, which the dataset card says can occur, fall out because of the non-empty rule.

The draw does not use, and the saved files do not contain, `country`, `state`, `hashed_ip`, `header`, or the moderation arrays. `model` and `timestamp` are kept on the manifest so the sample can be described. They are not analysis variables.

Redacted conversations stay eligible. Redaction is already applied in the release. A coder marks a conversation `uninterpretable` only when the remaining text hides the goal.

## Design

One streaming pass draws a simple random sample of 840 eligible conversations with seed `20261001`. That sample is randomly partitioned into:

- a **pilot** of 40 conversations, used only to revise the codebook;
- a **screening pool** of 800 conversations, from which the main sample is quota-selected after human screening.

The partition is disjoint. Confirmatory estimates use the main sample only. Pilot conversations never enter those estimates.

The script pins the Hugging Face revision it actually read and writes that revision to `data/share/draw-metadata.json`. A later run that must reproduce the draw passes `--revision` with that value. Reservoir sampling is uniform given the stream order of that revision and the seed. NumPy’s Generator supplies the random integers.

Why 40 and 800: the pilot is large enough to see each candidate cost code more than once if the code is not extremely rare, and small enough to recode after a rule change. The pool is large enough that a task type which is only a modest share of English chats can still fill a quota of 60 after non-task conversations are screened out. If a task cannot fill 60, the quota report records the shortfall. The cap is not raised on another task to force a total of 360.

## Screening and quota

Humans screen the pool with `methods/codebook-v0.md` (or v1 if the pilot has already revised it). Each pool conversation receives `screen` and `task_type`.

The main sample keeps conversations with `screen = task_oriented` and a task type in {writing, coding, information seeking, planning, creative production, other task}. Non-task and uninterpretable conversations are counted in the screening report and then left out of the quota.

Within each task that is present, the script takes up to 60 conversations and, where both exist, about half single-user-turn and half multi-user-turn. Single-turn conversations are the indeterminate-ending cases. Dropping them would make a stop after the first reply invisible. The per-task cap is the minimum of 60 and 360 divided by the number of task types present. With all six types present, the cap is 60 and the total is 360. With fewer types present, each type still caps at 60, the total is lower, and the quota report records the unused seats. Tasks are not up-weighted to fill those seats.

Command, after the pool coding sheet is filled:

```
python analysis/sample_wildchat.py quota --conversations data/local/pool/conversations.csv
```

The command copies the selected rows and packets to `data/local/main/` and writes `data/share/main-manifest.csv` plus `data/share/quota-report.json`.

## Reliability subset

After the main sample exists, draw 80 conversations from it with seed `20261001` for the second coder:

```
python analysis/irr.py --select-from data/share/main-manifest.csv --n 80
``` The second coder works from copies of those packets and does not see the primary coder’s codes. Agreement is Cohen’s kappa on each binary turn code, and on `task_type` and `ending_state`. The threshold for proceeding without a further codebook revision is 0.70 on each cost code. Prevalence and kappa are both reported, because a rare code can look unreliable when the base rate is low.

## Files

| Path | Contains message text | Role |
| --- | --- | --- |
| `data/local/pilot/` and `data/local/pool/` and `data/local/main/` | Yes | Coding. Git-ignored. Not deposited. |
| `data/share/*-manifest.csv` | No | Keys, model, timestamp, turn counts, initial-request word count, redaction flag. |
| `data/share/draw-metadata.json` | No | Revision, seed, filter list. |

`conversation_hash` in WildChat is not a unique key. The manifest key is `conversation_hash`, the conversation timestamp in ISO format, and the first turn’s `turn_identifier`, joined with `|`.

## How to run the draw

1. Create a virtual environment and install `analysis/requirements.txt`.
2. Log in to Hugging Face and accept the terms shown on the WildChat-1M dataset page. ODC-BY still requires attribution of Zhao et al. (2024) in the paper.
3. From the project root, run `python analysis/sample_wildchat.py draw`.
4. Code `data/local/pilot/packets/` first. Do not start the pool until codebook v1 is agreed, unless the pilot is being used only as a trial and the pool will be recoded under v1.
5. Expect a full stream of the release. The download is on the order of a few gigabytes and the pass reads every training row once.

## What this protocol refuses to do

It does not sample the 4.8 million conversation release. It does not drop single-turn conversations. It does not classify task type with a model. It does not claim that the 360 conversations estimate the rate of each cost in the 837,989-row release. Quota sampling supports comparison across tasks. It is not a probability sample of English WildChat unless the screening fractions are later used as weights, and this study does not apply those weights. The manuscript will say that directly.
