# Protocol: Before It Acts

**Title.** Before It Acts: A Scoping Review of Preview and Approval in Agentic AI Interfaces

**Author.** Tooba Jatoi, Independent researcher, toobajatoi44@gmail.com, ORCID 0009-0008-9650-7290

**Date.** 1 October 2026

**Reporting guide.** Preferred Reporting Items for Systematic reviews and Meta-Analyses extension for Scoping Reviews (PRISMA-ScR).

## Question

When a generative AI system is about to send, edit, book, delete, or otherwise change something, what does the interface show the person, and what can that person still change or refuse?

1. What do published interfaces reveal before an agent takes an action?
2. What can the person edit, limit, refuse, or undo at that moment?
3. What design guidance follows from those studies for an approval screen that shows the action, its scope, and its consequence?

## What this review is not

- It is not a review of user autonomy in conversation with language models. Wang and Wang (2026) already scoping-reviewed that literature.
- It is not a survey of how agent permission policies are specified and enforced. Michael and Roesner (2026) already surveyed that literature.
- It is not a rerun of any experiment in the included set.
- Industry pattern guides, software-development-kit pages, and forum posts are not evidence.

If a paper already owned the question of what the preview shows and what the person can still change, this review would stop. Public-web searches on 1 October 2026 did not identify a review that maps this preview. That statement is limited to those searches. Michael and Roesner (2026) own the adjacent question of permission-policy interfaces and enforcement. They are cited as a boundary and are not extracted as an interface case.

## Eligibility

**Include** a paper if it describes a generative or agentic AI interface in which a person can see a proposed action before that action changes something outside the conversation, or if it reports what the person could inspect or refuse at that moment. The action may be a message, file change, purchase, booking, web step, shell command, or other tool call. Preprints are eligible and are labeled as preprints. Security papers are eligible only when they describe what the approval surface shows.

**Exclude** a paper if it is only a chatbot usability study, creative co-writing with no pending action, a model of when to ask with no description of the screen, end-user planning that does not execute an external action, a survey of permission architectures, documentation, or a pattern guide.

## Sources and search

Searches were run on 1 October 2026 through public web search. Institutional access to Scopus, Web of Science, and IEEE Xplore was not available, and the ACM Digital Library was not queried through its own export. The manuscript states this limit. The queries and the scholarly records opened from them are listed in `review/search-log.md`.

## Screening and extraction

One reviewer screened titles and abstracts, then the opened full text. There was no second screener. Exclusions are in `review/screening-log.csv`.

Each included paper is one row in `review/extraction.csv`, with these columns:

- proposed action
- what is shown
- what can be edited
- refuse path
- reversibility
- whether approval is tied to that exact action

A cell is marked “not reported” when the paper does not say. Design guidance is written only after this sheet exists, and only where the extracted studies support it.

## Synthesis

The review groups the rows by what the interface shows and what the person can still do. It does not pool statistics. Numbers are reported only as published by the source paper.
