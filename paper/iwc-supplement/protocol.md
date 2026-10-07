# Protocol: Before It Acts

**Status.** Current protocol corresponding to the submitted manuscript. A superseded 1 October 2026 draft with different question wording is retained in the review record and is not this file.

**Title.** Before It Acts: A Scoping Review of Preview and Approval in Agentic AI Interfaces

**Author.** Omitted from this file for double-anonymized review. The name and affiliation are on the title page.

**Date.** 1 October 2026

**Reporting guide.** Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR; Tricco et al., 2018, https://doi.org/10.7326/M18-0850). The completed checklist is `prisma-scr-checklist.md`.

## Question

When a generative AI system is about to send, edit, book, delete, or otherwise change something, what does the interface show the person, and what can that person still change or refuse?

The questions below are those reported in the submitted manuscript. They preserve the scope of the 1 October 2026 protocol.

1. What object do agentic interfaces reported in the included evidence present before an action changes state outside the conversation?
2. For each interface, what does the source report about editing that object, refusing it, limiting its scope in advance, and undoing it after execution?
3. Which reports bind the approved object to the object that executes, and what evidence tests whether people notice when the two diverge?

## What this review is not

- It is not a review of user autonomy in conversation with language models. Y. Wang and G. Wang (2026) already scoping-reviewed that literature.
- It is not a survey of how agent permission policies are specified and enforced. Michael and Roesner (2026) already surveyed that literature.
- It is not a systematic analysis of runtime-approval security mechanisms. P. Wang, Li, and Tian (2026) already coded that design space, including how much information is shown at decision time. This review adds a chart of what the person can still edit, refuse, or undo, and whether the approval is bound to the executed action. Security work has already named that binding property.
- It is not a rerun of any experiment in the included set.
- Industry pattern guides, software-development-kit pages, and forum posts are not evidence.

If a paper already owned the question of what the preview shows, what the person can still change, and whether the approval is bound to the action that runs, this review would stop. The searches on 1 October 2026 did not identify that review. That statement is limited to those searches. The three papers above are boundaries. They are not extracted as interface cases.

## Eligibility

**Include** a paper if it describes a generative or agentic AI interface in which a person can see a proposed action before that action changes something outside the conversation, or if it reports what the person could inspect or refuse at that moment. The action may be a message, file change, purchase, booking, web step, shell command, or other tool call. Preprints are eligible and are labeled as preprints. Security papers are eligible only when they describe what the approval surface shows.

**Exclude** a paper if it is only a chatbot usability study, creative co-writing with no pending action, a model of when to ask with no description of the screen, end-user planning that does not execute an external action, a survey of permission architectures, documentation, or a pattern guide.

## Sources and search

Searches were run on 1 October 2026. The first two passes used public web search and public ACM and IEEE pages. Scopus and Web of Science were not searched, and there was no institutional export. The third pass queried the arXiv API for `cs.HC` and `cs.CR` and recorded `totalResults`. A direct ACM Digital Library search returned a bot check and no hit count. Forward-citation chasing retrieved a partial Semantic Scholar list for He et al. (2025) only. The fourth pass queried the OpenAlex API, retrieved every title for six queries, and recorded the counts. The queries are in `search-log.md`.

## Screening and extraction

All records were screened by the author against the predefined eligibility criteria. The author made the inclusion and exclusion decisions, charted the included reports, applied the analytical codes, and verified each extracted field against the corresponding source. There was no second human screener and no agreement statistic. Exclusions are in `screening-log.csv`.

Each included paper is one row in `extraction.csv`, with these columns:

- proposed action
- what is shown
- what can be edited
- refuse path
- reversibility
- whether approval is tied to that exact action

A cell is marked “not reported” when the paper does not say. Design propositions are written only after this sheet exists, and only where the extracted studies support them.

## Synthesis

The review codes each included row for preview form, edit, refuse, scope set in advance, undo of an external commit, and binding between the approved object and the executed object. The code definitions are in Section 3.5 of the manuscript. A report may contribute to more than one preview form. The review does not pool statistics. A review count uses the included rows as its denominator. A source count is printed only as published by that paper. Design propositions are written only where the coded sheet supports them, and each proposition states the question the sheet does not answer.
