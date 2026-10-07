# Protocol: Before It Acts (superseded draft)

**Status.** SUPERSEDED. This file is retained as a historical draft of the 1 October 2026 protocol. It is not the protocol reported in the submitted manuscript. The current protocol is `protocol.md`.

**Title.** Before It Acts: A Scoping Review of Preview and Approval in Agentic AI Interfaces

**Author.** Tooba Jatoi, Independent researcher, Karachi, Pakistan, toobajatoi44@gmail.com, ORCID 0009-0008-9650-7290

**Date.** 1 October 2026

**Reporting guide.** Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR; Tricco et al., 2018, https://doi.org/10.7326/M18-0850). The completed checklist is `review/prisma-scr-checklist.md`.

## Question

When a generative AI system is about to send, edit, book, delete, or otherwise change something, what does the interface show the person, and what can that person still change or refuse?

1. What do published interfaces reveal before an agent takes an action?
2. What can the person edit, limit, refuse, or undo at that moment?
3. What design guidance follows from those studies for an approval screen that shows the action, its scope, and its consequence?

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

Searches were run on 1 October 2026. The first two passes used public web search and public ACM and IEEE pages. Scopus and Web of Science were not searched, and there was no institutional export. The third pass queried the arXiv API for `cs.HC` and `cs.CR` and recorded `totalResults`. A direct ACM Digital Library search returned a bot check and no hit count. Forward-citation chasing retrieved a partial Semantic Scholar list for He et al. (2025) only. The fourth pass queried the OpenAlex API, retrieved every title for six queries, and recorded the counts. The queries are in `review/search-log.md`.

## Screening and extraction

The author read the retrieved sources between 1 October and 7 October 2026 and separately confirmed the screening labels and the extraction cells against those sources. A generative model proposed the searches, the screening decisions, and the extraction cells. The deposited log records the confirmed decisions. No label was changed. There was no second human screener and no agreement statistic. Exclusions are in `review/screening-log.csv`.

Each included paper is one row in `review/extraction.csv`, with these columns:

- proposed action
- what is shown
- what can be edited
- refuse path
- reversibility
- whether approval is tied to that exact action

A cell is marked “not reported” when the paper does not say. Design guidance is written only after this sheet exists, and only where the extracted studies support it.

## Synthesis

The review codes each included row for preview form, edit, refuse, scope set in advance, undo of an external commit, and binding between the approved object and the executed object. The code definitions are in Section 3.5 of the manuscript. A report may contribute to more than one preview form. The review does not pool statistics. A review count uses the included rows as its denominator. A source count is printed only as published by that paper. Design propositions are written only where the coded sheet supports them, and each proposition states the question the sheet does not answer.
