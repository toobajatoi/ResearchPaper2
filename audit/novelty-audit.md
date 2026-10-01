# Novelty audit and locked contribution

**Working title.** The Hidden Work of AI: Measuring Human Effort and Interaction Cost in Real-World Generative AI Conversations

**Target.** Research article, *International Journal of Human–Computer Interaction*

**Status.** Locked before coding. This memo is the internal record of what the paper can defend. The manuscript in `paper/manuscript.md` follows it. Codes, frequencies, and interface principles are not findings until human coding is complete.

**Date of audit.** 1 October 2026

## Decision

The HCI question is sound. The original claim is not available.

A paper that introduces interaction cost, or that announces that equal-quality outcomes can hide very different amounts of human work, would repeat Imai, İnan, and Alikhani (2026). IJHCI screens out manuscripts on topics that have recently been treated with a similar question and a similar result. The defensible paper measures something that token totals do not measure: the **composition** of observable human work after the first request in unconstrained ChatGPT conversations, and the association of that composition with behavioral ending states.

The phrase “AI interaction tax” is not used in the manuscript. No weighted index is defined in advance.

## Locked construct

**Human–AI interaction cost (HAIC)** is the observable work a user does after the first request, while still pursuing that request, to obtain an acceptable or intended outcome from a generative AI system.

The primary result is a **cost profile**: which of the following actions occur, how often, and in what mix.

- Clarification
- Correction
- Constraint addition
- Requirement restoration
- Repetition
- Revision request
- Verification
- Redirection

Acceptance, abandonment, social turns, and answers to a question the assistant asked are coded, and they are not counted as cost. A full inclusion and exclusion rule for each code is in `methods/codebook-v0.md`.

## Locked claim

Prior studies describe what users do with generative AI, and a recent task study prices collaboration in tokens. This study asks which kinds of post-request human work are visible in real ChatGPT conversations, how that mix differs by task, and which kinds co-occur with apparent resolution, continued repair, or abandonment.

Three contributions:

1. A reliability-checked taxonomy of post-request human actions, developed on WildChat conversations and distinguished from follow-up typologies that were built to describe writing collaboration or grounding acts.
2. Evidence, in a bounded English sample, of how the mix of those actions differs across task types.
3. Evidence of which action types co-occur with observable ending states, followed by interface principles stated only for the action types the sample shows users repeating.

## Locked research questions

- **RQ1.** Which observable forms of post-request human work occur in real-world generative-AI conversations?
- **RQ2.** How does the composition of that work differ across task types?
- **RQ3.** How are those forms of work associated with apparent resolution, continued repair, and abandonment?
- **RQ4 (exploratory).** How do lower-repair resolved trajectories differ from prolonged or abandoned ones, and which repeated costs could an interface remove?

Out of scope: country, language comparison, model comparison, hashed IP addresses, expertise, demographics, and any claim about the full WildChat corpus.

## Locked non-claims

The paper will not claim that it introduces interaction cost, productive-versus-costly success, or the finding that a higher token cost can accompany equal or worse collaboration.

The paper will not claim ground-truth task success. WildChat contains no submitted artifact and no rubric score. Ending state is behavioral.

The paper will not report prevalence for all conversations in WildChat-1M or in any larger release. Estimates cover the analytical sample.

The paper will not treat a single-turn stop as success. A conversation that ends after the first reply is **indeterminate**. The user may have used the answer, or given up, outside the log.

Cost predictors in RQ3 are counted on user turns **before** the turn that supplies the terminal signal. Associations are not effects.

Candidate interface mechanisms (persistent constraints, visible requirements, retained corrections, a goal state, a summary prompt after repeated revision) stay in the protocol as hypotheses. They enter the discussion only if the coded sample shows the corresponding repeated cost.

## What each adjacent study already did

### Imai, İnan, and Alikhani (2026) — closest paper

*From Task Success to Productive Success: Evaluating Human-AI Collaboration by Quality and Cost* (arXiv:2609.21117).

They define collaborative productivity as outcome quality relative to interaction cost, standardized within task: \(P_z = z(Q) - z(C)\). Quality is an LLM-as-judge rubric on the submitted artifact, checked against human rubric scores. Cost is weighted tokens, \(C = \text{user tokens} + 0.5 \times \text{agent tokens}\). They state that repair is not a separate term, because clarification and reformulation already increase the token total. Sensitivity checks use user tokens only, total tokens, turn count, and other agent-token weights.

Data are session logs from structured tasks, not a public in-the-wild corpus. Collaborative Gym contributes travel planning, tabular analysis, and related-work writing, restricted to sessions with a final artifact (\(n = 184\) across those tasks in the primary artifact set; task-level samples are larger before that restriction). A new visualization task adds 42 sessions in which participants used a model to analyze WildChat-1M and submitted a figure, code, and interpretation. The WildChat corpus is the dataset those participants analyzed. It is not the conversation sample.

Findings this paper must not rediscover as if they were new:

- Sessions with the same quality rating can differ by about one to two orders of magnitude in token cost. In the top quality bucket for travel planning, costs ran from 854 to 60,324 tokens (about 70.6 times).
- The quality–cost correlation is task-dependent (positive for related-work writing, negative for visualization).
- Subjective ratings are inconsistent proxies for the quality–cost tradeoff.
- Productive sessions show more agent probing early; unproductive sessions show more user repair, clarification, and probing. The authors interpret this with Clark’s principle of least collaborative effort.

Their dialogue codes are grounding acts (Shaikh et al., 2025) and positive-friction moves, applied with a model and checked on a subset. The design implication they draw is about agent behavior: probe and clarify early so the user does not inherit the repair.

**What remains.** A token weight cannot tell a designer whether the user restated a dropped constraint, corrected a fact, verified an answer, or elaborated a creative brief. Imai et al. also do not estimate which of those actions occur in ordinary ChatGPT use, where there is no assigned task and no scored artifact. This paper’s outcome is an ending state read from the log, which is weaker than their rubric and is labeled as such.

### Mysore, Das, Cao, and Sarrafzadeh (2025) — PATH

*Prototypical Human-AI Collaboration Behaviors from LLM-Assisted Writing in the Wild*, EMNLP 2025.

They study English writing sessions in Bing Copilot (about 20.5 million sessions) and WildChat (about 800,000 sessions). A GPT-4o classifier labels follow-up utterances. Principal components of those labels yield seven prototypical collaboration behaviors (PATHs) that account for about 80–85% of variance. The follow-up inventory includes restating a request, elaborating a request, requesting answers, requesting more outputs, changing style, adding content, removing content, courtesy, positive response, negative response, and an undefined residual. Explicit positive or negative feedback is uncommon (about 1–5% of sessions). Writing intent correlates with PATH.

**What remains.** PATH describes collaboration in writing and points the implication toward model alignment. It does not define a cost, does not separate requirement restoration from a new constraint, and does not relate follow-up type to resolution versus abandonment. Several PATH labels (change style, add content, remove content, restate) will appear inside HAIC codes. The codebook treats PATH as a neighboring description, not as the coding scheme. Where a PATH label and a HAIC code could both fit, HAIC codes are assigned by the inclusion rules in the codebook, which turn on whether the user is still trying to secure the initial goal and whether the requirement was already stated.

### Liu, Zhang, and Choi (2025) — implicit feedback

*User Feedback in Human-LLM Dialogues: A Lens to Understand Users But Noisy as a Learning Signal*, EMNLP 2025.

They detect implicit feedback in WildChat and LMSYS-Chat-1M, annotate each user turn after the initial prompt in 109 conversations, and test whether feedback content improves model training. Feedback is common in later turns of long conversations and is often negative. Training results are mixed: gains on short MT-Bench items, and no gain on harder WildBench items. The contribution is about learning signals.

**What remains.** Negative feedback is one observable trace of user work. Liu et al. do not organize that trace into an interaction-cost profile, and they do not ask whether particular kinds of feedback co-occur with resolution of the user’s task.

### Shaikh, Mozannar, Bansal, Fourney, and Horvitz (2025) — grounding rifts

*Navigating Rifts in Human-LLM Grounding: Study and Benchmark*, ACL 2025.

They code grounding acts on WildChat, MultiWOZ, and Bing Chat. Relative to people, the models in their logs were about three times less likely to initiate clarification and about sixteen times less likely to issue follow-up requests. Early grounding failure predicts later breakdown. RIFTS is a benchmark of situations that call for clarification or follow-up, built for model evaluation. Their act inventory includes reformulation, repair, restart, and clarification, drawing on conversation analysis (Schegloff, Jefferson, & Sacks, 1977; Clark, 1996).

**What remains.** Shaikh et al. show that people, rather than models, carry grounding work, and they build a benchmark for models. They do not produce a task-stratified profile of human post-request actions, and they do not connect a multi-type cost profile to an ending state for interface design. HAIC’s requirement restoration, constraint addition, verification, and redirection are finer descriptions of user effort than a single repair act, and they are motivated by what an interface could remember. Overlap with clarification and repair is acknowledged in the codebook so coders do not invent a private meaning for those words.

### Coding-log studies

Zhang et al. (2025; arXiv:2512.10493) combine coding conversations from LMSYS-Chat-1M and WildChat into a set they call LMSYS-WildChat (60,949 conversations). They describe linear, star, and tree interaction patterns, instruction non-compliance, and satisfaction. Tree-shaped sessions are longer and less satisfactory. A subset of multi-turn conversations (378; 80 of them in the exploratory coding) was examined by hand.

Zhong, Zou, and Adams (2025; arXiv:2509.10402) release CodeChat, a WildChat-derived set of 82,845 developer–LLM conversations, and relate conversational moves to defects in generated code.

**What remains.** Both studies stay inside coding. Interaction shape and code quality are not a general account of human interaction cost across writing, planning, information seeking, and creative production.

### Wang, Bilal, and Zaman (2026) — conversational difficulty

*When AI Becomes Hard to Understand* (arXiv:2609.17301).

They analyze ChatGPT and Gemini histories contributed through Measure Protocol, focusing on finance (about 43,100 conversations) and health (about 41,500). Repeated prompting and clarification after apparent misunderstanding are indicators of conversational difficulty. Response length, readability, and lexical diversity relate to those indicators only in combination. They propose a conversational complexity budget. The theoretical lens is cognitive load. They state that repair traces are not a direct measure of load.

**What remains.** Their outcome is difficulty inferred from two repair behaviors in two high-stakes domains. This study’s outcome is the mix of post-request work and its association with ending state, across several everyday task types, in WildChat.

### Repair cost in this journal

Meck, Draxler, and Vogt (2023) study repair costs in breakdowns with in-car voice assistants and publish in *International Journal of Human–Computer Interaction*. They use the principle of least collaborative effort to compare error-handling strategies. The technology is a spoken dialogue system in a driving study, not a generative model, and the method is experimental.

The citation matters for fit. IJHCI has already treated repair cost as a human–computer interaction topic. The present study extends that concern to generative-AI logs and to the kinds of work users perform when the system is a general-purpose chatbot.

### Theory this paper uses and does not reinvent

- Clark and Wilkes-Gibbs (1986): collaborators minimize joint effort, not only one party’s effort.
- Clark and Brennan (1991): formulation, reception, and repair costs are distributed across participants. This study operationalizes the **user’s observable formulation and repair after the first request**. It does not claim to measure reception, attention, or cognitive load. Token-weighted reception cost is Imai et al.’s (2026) operationalization.
- Walker, Litman, Kamm, and Abella (1997): PARADISE separates task success from dialogue cost for spoken dialogue agents. Imai et al. already adapted that separation to human–AI collaboration. This paper cites PARADISE as ancestry and does not present a new performance function.
- Schegloff, Jefferson, and Sacks (1977): repair is an organized conversational practice. Ending-state codes follow the log. They are not a full conversation-analytic transcription.

## Positioning table

| Study | Record | Quantity | Ending or quality | This study’s distinct job |
| --- | --- | --- | --- | --- |
| Imai et al., 2026 | ~226 structured sessions with artifacts | Weighted tokens | Rubric on the artifact | Which kinds of user work, in ordinary ChatGPT logs, without a scored artifact |
| Mysore et al., 2025 | WildChat and Copilot writing sessions | Follow-up types and PATH components | Not an outcome model | Cost-relevant distinctions (restoration vs. new constraint) and ending state |
| Liu et al., 2025 | WildChat and LMSYS | Implicit feedback as a training signal | Benchmark scores after training | Effort profile, not a learning signal |
| Shaikh et al., 2025 | WildChat, MultiWOZ, Bing Chat | Grounding acts | Later breakdown; RIFTS benchmark | Multi-type human cost and interface memory of requirements |
| Zhang et al., 2025; Zhong et al., 2025 | Coding subsets | Trajectory shape; code defects | Satisfaction; code quality | Several task types, one cost profile |
| Wang et al., 2026 | Finance and health chats | Two repair indicators | Difficulty, via response form | Ending state of the user’s goal |
| Meck et al., 2023 | Driving study, voice assistant | Rated repair cost | Preference for repair strategies | Generative-AI logs, behavioral codes |

## Reviewer questions and the prepared answers

**“Imai et al. already measured interaction cost.”** They measured a token-weighted cost against rubric quality in assigned tasks. This study measures the type of post-request human action in opted-in ChatGPT logs, where quality cannot be scored the same way. The discussion will cite their 70-times result and then report action profiles, which their cost function was not built to separate.

**“PATH already classified follow-ups on WildChat.”** PATH classified writing follow-ups to describe collaboration and alignment. This study’s codes ask whether the follow-up is extra work to secure a goal the user already stated, and whether that work co-occurs with resolution or abandonment.

**“You cannot know whether the task succeeded.”** Agreed. The methods call the outcome an ending state. Indeterminate is its own category. The limitations section states that off-platform use is invisible.

**“Why not classify millions of conversations with a model?”** The study has no model API, and a model judging human effort spent correcting a model would be a circular measure. Scale here is a reliability-checked sample. Population estimates for 837,989 public WildChat-1M rows are not claimed. Imai et al. and PATH already showed that model annotation of logs is possible. The contribution is the construct and the human-coded distinctions, not classifier throughput.

**“This is an NLP analysis, not HCI.”** The codes exist to identify work an interface could take off the user: remembering a constraint, restoring a requirement, holding a correction. The discussion is written from the user’s activity and the interface. Model training advice is out of scope.

## Consequences for the method

These choices follow from the audit and are specified so the codebook, sampler, and manuscript cannot drift.

- Corpus: public non-toxic `allenai/WildChat-1M` (837,989 conversations after removal of toxic rows and a later PII removal; ODC-BY). English only. At least one non-empty user turn and one non-empty assistant turn.
- The original one-million-conversation release and any larger WildChat release are not the sampling frame.
- Human coding only. No generative model assigns codes.
- Pilot of 40 conversations refines the codebook. Those 40 are excluded from confirmatory estimates.
- Main sample: quota across task types that survive screening, target 360, with single-turn and multi-turn conversations both retained inside each task.
- Second coder on 80 main-sample conversations. Cohen’s kappa per code. Revise if kappa is below 0.70.
- RQ3 uses pre-terminal rates, with task and initial-request length as controls.
- Deposited materials: codebook, conversation keys, annotations. Message text stays in the local coding files and is not redistributed.

## Sources

Clark, H. H. (1996). *Using language*. Cambridge University Press.

Clark, H. H., & Brennan, S. E. (1991). Grounding in communication. In L. B. Resnick, J. M. Levine, & S. D. Teasley (Eds.), *Perspectives on socially shared cognition* (pp. 127–149). American Psychological Association.

Clark, H. H., & Wilkes-Gibbs, D. (1986). Referring as a collaborative process. *Cognition, 22*(1), 1–39. https://doi.org/10.1016/0010-0277(86)90010-7

Imai, S., İnan, M., & Alikhani, M. (2026). *From task success to productive success: Evaluating human-AI collaboration by quality and cost* (arXiv:2609.21117). https://arxiv.org/abs/2609.21117

Liu, Y., Zhang, M. J. Q., & Choi, E. (2025). User feedback in human-LLM dialogues: A lens to understand users but noisy as a learning signal. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*. https://aclanthology.org/2025.emnlp-main.133/

Meck, A.-M., Draxler, C., & Vogt, T. (2023). Failing with grace: Exploring the role of repair costs in conversational breakdowns with in-car voice assistants. *International Journal of Human–Computer Interaction*. https://doi.org/10.1080/10447318.2023.2266791

Mysore, S., Das, D., Cao, H., & Sarrafzadeh, B. (2025). Prototypical human-AI collaboration behaviors from LLM-assisted writing in the wild. In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing*. https://aclanthology.org/2025.emnlp-main.852/

Schegloff, E. A., Jefferson, G., & Sacks, H. (1977). The preference for self-correction in the organization of repair in conversation. *Language, 53*(2), 361–382. https://doi.org/10.2307/413107

Shaikh, O., Mozannar, H., Bansal, G., Fourney, A., & Horvitz, E. (2025). Navigating rifts in human-LLM grounding: Study and benchmark. In *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)* (pp. 20832–20847). https://aclanthology.org/2025.acl-long.1016/

Walker, M. A., Litman, D. J., Kamm, C. A., & Abella, A. (1997). PARADISE: A framework for evaluating spoken dialogue agents. In *Proceedings of the 35th Annual Meeting of the Association for Computational Linguistics* (pp. 271–280). https://doi.org/10.3115/976909.979652

Wang, Y. C., Bilal, I. M., & Zaman, Q. (2026). *When AI becomes hard to understand: Cognitive demands in real-world human–AI conversations* (arXiv:2609.17301). https://arxiv.org/abs/2609.17301

Zhang, B., Zhang, L., Zhang, H., Liu, F., Wang, S., Shen, B., Fu, A., & Shi, L. (2025). *Decoding human-LLM collaboration in coding: An empirical study of multi-turn conversations in the wild* (arXiv:2512.10493). https://arxiv.org/abs/2512.10493

Zhao, W., Ren, X., Hessel, J., Cardie, C., Choi, Y., & Deng, Y. (2024). WildChat: 1M ChatGPT interaction logs in the wild. In *The Twelfth International Conference on Learning Representations*. https://openreview.net/forum?id=Bl8u7ZRlbM

Zhong, S., Zou, Y., & Adams, B. (2025). *Developer-LLM conversations: An empirical study of interactions and generated code quality* (arXiv:2509.10402). https://arxiv.org/abs/2509.10402
