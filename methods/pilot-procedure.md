# After the pilot: revision, reliability, analysis, and the manuscript

Version 0 of the codebook is unchanged. No WildChat conversations have been coded in this workspace, so there is no empirical basis for a version 1. Revising the codes before the pilot would invent distinctions. The steps below are the ones to run after a person has coded the packets.

## 1. Draw the sample

From the project root, with the WildChat-1M terms accepted on Hugging Face:

```
python analysis/sample_wildchat.py draw
```

This writes 40 pilot packets to `data/local/pilot/packets/` and 800 pool packets to `data/local/pool/packets/`. Message text stays in `data/local/`, which is git-ignored. Keys and counts go to `data/share/`.

## 2. Code the pilot by hand

Use `methods/codebook-v0.md`. Fill `data/local/pilot/conversations.csv` and `data/local/pilot/turns.csv`. Every code cell is `0` or `1`. Blanks mean unfinished. Do not use a generative model to fill them.

## 3. Read the diagnostics, then revise

```
python analysis/pilot_diagnostics.py
```

The report is `analysis/output/pilot-diagnostics.md`. It lists codes that never occur, codes that always occur together, and cost codes placed on the initial request.

Decisions go in `methods/codebook-changelog.md`. Copy `methods/codebook-v0.md` to `methods/codebook-v1.md` and edit the copy. Do not change version 0 after pilot coding has started. Recode the pilot under version 1 if a rule changed enough that the old labels are no longer the construct.

A code with no instances in 40 conversations can be kept if the inclusion rule is still needed for a rarer event, but the changelog must say why. A pair that coders cannot separate is merged.

## 4. Screen the pool and draw the main sample

Code `screen` and `task_type` on `data/local/pool/conversations.csv` under the codebook version you will actually use. Then:

```
python analysis/sample_wildchat.py quota --conversations data/local/pool/conversations.csv
```

Code the selected packets in `data/local/main/` at turn level. The 40 pilot conversations are not in this sample.

## 5. Reliability

Draw 80 main-sample conversations with seed 20261001:

```
python analysis/irr.py --select-from data/share/main-manifest.csv --n 80
```

The ids are written to `data/share/reliability-ids.csv`. Give the second coder copies of those packets and empty coding sheets. When both sheets are complete:

```
python analysis/irr.py --primary-turns data/local/main/turns.csv --secondary-turns data/local/main/turns-coder-b.csv --primary-conversations data/local/main/conversations.csv --secondary-conversations data/local/main/conversations-coder-b.csv
```

If any cost-code kappa is below 0.70, revise that distinction, recode it, and compute kappa again. Report prevalence next to kappa. The paper cannot claim a validated taxonomy without this step.

## 6. Confirmatory tables

```
python analysis/analyze.py --turns data/local/main/turns.csv --conversations data/local/main/conversations.csv
```

Tables land in `analysis/output/results-tables.md`. Paste the numbers into `paper/manuscript.md` sections 4.1–4.3. The script does not write the prose and does not write interface principles.

RQ4 candidates are `analysis/output/rq4-candidates.csv`. Read those packets. Fill section 4.4 from the reading.

## 7. Design implications

Fill manuscript section 5.2 only after step 6. Keep a principle only when the coded sample shows the corresponding cost recurring.

- Repeated constraint addition or requirement restoration: a visible, persistent list of requirements.
- Repeated correction: a retained correction the next reply has to respect.
- Long repair that does not resolve: an explicit goal state, and an offer to restate requirements before another attempt.

Drop any of these that the codes do not show. Do not add a weighted interaction-cost formula unless a factor structure in the coded profiles actually supports one. If it does, report it as a secondary description and say what it hides.

## 8. Close the manuscript before submission

Replace every `[Pending]` block. Recount the abstract so it stays at or under 150 words and states the actual findings in one or two sentences. Insert the word count. Add the second coder’s name under authorship or acknowledgments, using Taylor & Francis authorship criteria. Add the data-repository identifier to the data-availability statement. Send `paper/cover-letter.md` only when the institutional email, profile URL, and results are real.

Until those fields are filled, the manuscript is not a submission.
