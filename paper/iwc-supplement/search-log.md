# Search log

**Date.** 1 October 2026

**How the search was run.** Three passes on the same day. The first was public web search. The second opened public ACM Digital Library and IEEE Xplore pages. No Scopus or Web of Science search. No ACM or IEEE institutional export. Hit counts for the first two passes were not retained and are not reported. Non-scholarly pages (software-development kits, pattern blogs, and forum posts) were set aside and are not rows in the screening log.

**Owning-review check.** The queries below did not identify a review that maps what an agentic interface shows before an action, what the person can still change or refuse, and whether the approval is bound to the action that runs. The check does not cover Scopus, Web of Science, or an ACM Digital Library export. The boundary reviews are Y. Wang and G. Wang (2026) on autonomy mechanisms, Michael and Roesner (2026) on permission-policy interfaces and enforcement, and P. Wang, Li, and Tian (2026) on runtime approval, including how much information is shown at decision time.

## Queries

1. scoping review OR systematic review human approval preview before AI agent action interface HCI
2. human-in-the-loop approval interface agent tool use confirmation preview scoping review generative AI
3. CHI before executing OR tool approval OR confirm the action OR approval request LLM agent interface user 2024 2025 2026
4. plan preview OR action preview OR ask for confirmation generative AI agent interface CHI DIS UIST IJHCI
5. human-in-the-loop approval generative agent send email OR tool call interface study
6. Magentic-UI CowPilot action guards co-planning agent approval CHI 2025 2026
7. approve diff OR command OR shell command AI coding agent interface user study CHI 2024 2025 2026
8. Plan-Then-Execute LLM agents daily assistant authors venue DOI
9. Cocoa co-planning CHI 2026 authors; VeriPlan authors; CowPilot authors venue; Magentic-UI authors; DoubleAgents authors
10. action guard OR action approval OR co-planning OR suggest-then-execute AI agent CHI DIS UIST 2024 2025 2026
11. AgentClick authors; What You Approve Is What Executes authors; Assistant or Actor AI agent authors; WaitGPT authors; CowPilot published venue
12. Michael Roesner 2026 permission interfaces AI agents; Do User-Authored Permission Policies authors

13. site:dl.acm.org agent approval preview before email or tool call or action guard or diff, CHI 2024–2026
14. site:ieeexplore.ieee.org human approval preview AI agent interface before execution, 2024–2026
15. action approval OR approve the plan OR needs approval, LLM agent interface user study, CHI DIS UIST CSCW 2025–2026

The second pass was run on the same day. Scopus and Web of Science were not searched. ACM and IEEE were opened as public web pages, not as institutional exports. IEEE abstracts on physical-robot motion previews were set aside and are not rows in the screening log.

## Third pass, same day

arXiv API, `http://export.arxiv.org/api/query`, `max_results` used only to list titles. The `totalResults` value is the hit count.

16. `cat:cs.HC AND all:approval AND all:agent AND submittedDate:[202401010000 TO 202610022359]` — **19** results.
17. `cat:cs.CR AND (all:approval OR all:"human-in-the-loop") AND all:agent AND submittedDate:[202401010000 TO 202610022359]` — **111** results. All 111 titles were scanned. Records were opened only when the title concerned the approval surface, a binding between approval and execution, or a review of that surface.
18. `all:"consent integrity" OR all:"approval integrity" OR all:"stale consent" OR all:"verifiable action card" OR all:"approval laundering"` — **6** results. This set overlaps queries 16 and 17.

ACM Digital Library search URL `https://dl.acm.org/action/doSearch?AllField=agent%20approval%20preview` returned a bot-check page and no result count. No ACM hit total is reported.

Forward citations, Semantic Scholar, 1 October 2026:

- He et al. (2025), DOI 10.1145/3706598.3713218: **91** citing works. The first 50 titles were scanned. Titles 51–91 were not opened.
- Weng (2026), arXiv:2606.02668: request returned HTTP 429. Count not obtained.
- Mozannar et al. (2025), arXiv:2507.22358: request returned HTTP 429. Count not obtained.
- Google Scholar citing pages were not retrieved.

A follow-up lookup while identifying Q. Zhang (2026) also opened arXiv:2609.31301 (H. Zhang et al.). It was not in the counted arXiv result lists above.

## Records assessed

## Fourth pass, same day

OpenAlex API, `https://api.openalex.org/works`, filtered to publications from 2024-01-01 through 2026-10-01 except where noted. Every returned title was retrieved. The title list is `review/fourth-pass-titles.tsv`. Software releases, datasets, and duplicate deposit versions were set aside and are not rows in the screening log.

19. `title_and_abstract.search:approval preview agent` — **47** works.
20. `title_and_abstract.search:consent integrity agent` — **190** works.
21. `title_and_abstract.search:stale consent` — **47** works.
22. `title_and_abstract.search:verifiable action card` — **27** works.
23. `title_and_abstract.search:action guard agent` — **437** works.
24. `title.search:from approval to execution` — **5** works. This query was not date-filtered. Two records from 2006 and 2007 were about nondestructive testing and a technical execution plan, and they were set aside.

A record was assessed when the title concerned a human approval surface, a binding between an approval and the executed action, or a review of that surface, or when the title named a guard that might show a person a pending action. Automated guard-model papers whose titles did not indicate a person-facing preview were not assessed. Scopus and Web of Science were still not searched.

## Records assessed

Fifty-nine distinct scholarly records are listed in `review/screening-log.csv`. Fifteen were included. Forty-four were excluded. Twenty-one of the first thirty-two were assessed in full text in the first two passes. The eleven third-pass records were assessed at abstract, and in full HTML where an HTML version was available. The twenty-seven fourth-pass records were assessed at abstract. J. Liu et al. (2026) was also read in HTML. The Q. Zhang (2026) workshop PDF was read on 2 October 2026. An earlier abstract on the workshop web page reported 1,377 proposals and a 7.8 percent unsafe rate. The extraction uses the PDF. The approval-binding cluster is a snapshot as of 1 October 2026, after this OpenAlex pass.
