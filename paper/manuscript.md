# The Hidden Work of AI: Measuring Human Effort and Interaction Cost in Real-World Generative AI Conversations

**Author.** [Full name]

**Affiliation.** [Institution where the research was conducted]

**ORCID.** [ORCID]

**Corresponding author.** [Full name], [institutional email]

**Author profile.** [URL of the institutional profile page]

**CRediT.** [Author name]: conceptualization, methodology, investigation, formal analysis, writing—original draft, writing—review and editing. A second coder’s role will be added if that contribution meets Taylor & Francis authorship criteria.

**Word count.** [Counted after the results section is written. This draft excludes results.]

## Abstract

People working with generative AI often continue after the first prompt. They clarify, correct, add constraints, restore requirements the system dropped, repeat themselves, revise, verify, and redirect. This article defines that observable post-request work as human–AI interaction cost. The construct is distinct from token-weighted accounts of collaborative productivity and from taxonomies that describe collaboration behaviors without relating them to resolution. Human coders apply a reliability-checked scheme for task type, post-request actions, and behavioral ending state to a quota sample of English conversations from the public non-toxic WildChat-1M corpus. The sample supports comparison across tasks and is not offered as a census of the corpus. A stop after the first reply is coded as indeterminate rather than as success. The study asks which forms of this work occur, how their composition differs by task, and how those forms are associated with apparent resolution, continued repair, and abandonment.

**Keywords:** human–AI interaction; interaction cost; conversational repair; generative AI; WildChat

## 1. Introduction

Generative AI is commonly presented as a reduction in human effort. A person states a goal, the system produces an artifact, and the work of producing that artifact is treated as having moved from the person to the model. Evaluations that score the artifact, the time to a finished product, or the economic value of the occupation follow that presentation. They answer whether the outcome was good, fast, or valuable. They do not answer what the person had to do, after the first request, to get there.

Logs of ordinary use show that the first request is often not the last act. The user clarifies a misread goal, corrects an error, adds a constraint, repeats a requirement the system dropped, asks for another attempt, checks whether the answer is right, or leaves the exchange. That activity is observable in the conversation itself. It is easy to miss in an evaluation that keeps only the final answer.

This article names that activity human–AI interaction cost: the observable work a user expends after an initial request, while still pursuing that request, to obtain an acceptable or intended outcome from a generative AI system. The name is deliberately narrower than a claim about cognitive load, wages, or the value of the user’s time. Those quantities are not in a chat log. What the log can support is a classification of the user’s later turns.

The question is not new in spirit. Clark and Wilkes-Gibbs (1986) argued that collaborators coordinate so as to minimize the joint effort of establishing understanding, not the effort of one party alone. Clark and Brennan (1991) separated the costs of formulating a contribution, receiving one, and repairing a misunderstanding. Walker, Litman, Kamm, and Abella (1997) carried a related separation into the evaluation of spoken dialogue systems, distinguishing task success from the cost of the dialogue. Meck, Draxler, and Vogt (2023) used repair cost to compare error handling in in-car voice assistants, in this journal. The present study takes that family of ideas into opted-in conversations with ChatGPT and asks which kinds of post-request work users actually perform.

A recent task study has already made a quantitative version of interaction cost hard to ignore. Imai, İnan, and Alikhani (2026) define collaborative productivity as artifact quality relative to a token-weighted cost of the session. In their data, sessions with the same quality rating can differ by roughly seventy times in that cost, the quality–cost relationship changes with the task, and productive sessions are ones in which the agent probes early rather than leaving repair to the user. Their cost is a weighted sum of user and agent tokens. They treat repair as already contained in the token total, because another clarification adds tokens. That is the right move for a productivity index on sessions that end in a scored artifact. It does not tell an interface designer whether the tokens were a repeated constraint, a factual correction, a verification question, or a creative elaboration. Those are different design problems.

Public conversation logs make the design-relevant question askable without recruiting participants and without calling a model API. WildChat contains chats that users opted to contribute while using a service powered by GPT-3.5 and GPT-4 (Zhao et al., 2024). Subsequent studies have used those logs, and others like them, to describe writing collaboration (Mysore et al., 2025), to mine implicit feedback as a training signal (Liu et al., 2025), to model grounding failures (Shaikh et al., 2025), and to describe coding trajectories (Zhang et al., 2025; Zhong et al., 2025). Wang, Bilal, and Zaman (2026) use repeated prompting and clarification in finance and health chats as signs that a response was hard to process. Each of those studies characterizes behavior. None of them produces a reliability-checked profile of post-request human work across everyday task types and relates that profile to whether the initial goal looks resolved, still under repair, or abandoned.

The study addresses four questions.

- RQ1. Which observable forms of post-request human work occur in real-world generative-AI conversations?
- RQ2. How does the composition of that work differ across task types?
- RQ3. How are those forms of work associated with apparent resolution, continued repair, and abandonment?
- RQ4. How do lower-repair resolved trajectories differ from prolonged or abandoned ones, and which repeated costs could an interface remove?

RQ4 is exploratory. The interface answer is restricted to costs the coded sample shows users repeating. Remembering a constraint, showing the requirements still in force, and retaining a correction are hypotheses in the protocol. They are not findings of this draft, and they will not be listed as findings unless the codes support them.

The contribution is empirical and practical. The study specifies and reliability-checks a taxonomy of post-request human actions on a bounded sample of English WildChat conversations. It estimates how the mix of those actions differs by task. It estimates how the mix co-occurs with a behavioral ending state. It then states interface principles only for the repeated costs. It does not introduce the idea that interaction has a cost, and it does not offer a weighted formula for that cost.

## 2. Related work and theoretical framing

### 2.1. Cost, success, and what tokens cannot separate

Research on AI and productivity has mostly asked whether people finish more, finish faster, or finish at higher quality when a model is available. Those outcomes matter. They also treat the interaction as a black box. Imai et al. (2026) open that box for a specific kind of record: human–AI sessions on assigned tasks that end in an artifact a rubric can score. They define collaborative productivity as within-task standardized quality minus within-task standardized interaction cost. Quality is a rubric score. Cost is user tokens plus half of agent tokens, a weight they motivate by the relative speed of reading and writing (Clark & Brennan, 1991). Across travel planning, tabular analysis, related-work writing, and a visualization task, equal quality ratings hid large cost differences. Additional interaction accompanied higher quality in some tasks and lower quality in others. Subjective ratings did not reliably penalize cost once quality was held fixed. Dialogue codes on the same sessions suggested that productive collaboration moved probing onto the agent, while unproductive collaboration left clarification and repair with the user.

This article uses that result as a boundary, not as a hypothesis to retest. WildChat does not contain the submitted artifact, the rubric, or the post-task survey those authors used. A token weight on a WildChat conversation would still collapse distinct user acts into one number. The acts are the object of measurement here. Table 1 states the division of labor across the closest studies.

**Table 1.** What adjacent studies measure, and the measurement this study adds.

| Study | Record | What is measured | Outcome | Measurement added here |
| --- | --- | --- | --- | --- |
| Imai et al. (2026) | Structured task sessions with artifacts | Token-weighted interaction cost | Rubric quality of the artifact | Which user acts produce the work, in ordinary chats with no scored artifact |
| Mysore et al. (2025) | WildChat and Copilot writing sessions | Follow-up types and collaboration patterns | Not modeled as resolution | Requirement restoration versus a newly added constraint, plus ending state |
| Liu et al. (2025) | WildChat and LMSYS | Implicit feedback | Later training performance | A cost profile, not a learning signal |
| Shaikh et al. (2025) | WildChat, MultiWOZ, and Bing Chat | Grounding acts | Later breakdown; a model benchmark | A multi-type account of human post-request work for interface design |
| Zhang et al. (2025); Zhong et al. (2025) | Coding subsets of public logs | Trajectory shape; code defects | Satisfaction; code quality | The same cost profile across several task types |
| Wang et al. (2026) | Finance and health chats | Repeated prompting and clarification | Conversational difficulty | Ending state of the user’s initial goal |
| Meck et al. (2023) | Driving study with a voice assistant | Rated repair cost of error handling | Preference among repair strategies | Generative-AI logs and behavioral codes |

PARADISE (Walker et al., 1997) remains the evaluation ancestor for separating success from dialogue cost. Imai et al. (2026) already adapted that separation to human–AI collaboration and combined the two quantities in an index. This study does not propose a replacement index. If a later factor analysis of the codes supports a composite, that composite will be reported as a secondary description. The primary result is the profile of action types.

### 2.2. Descriptions of what users do with generative AI

Mysore et al. (2025) analyzed English writing sessions from Bing Copilot and from WildChat. They classified follow-up utterances, including restating a request, elaborating it, asking a question about the generation, requesting more outputs, changing style, adding content, and removing content. Seven components accounted for most of the variance in those follow-ups. Writing intent correlated with the components. Explicit praise and complaint were uncommon. The implication they draw is about aligning models to writing intents.

Those follow-up labels are neighbors of the codes in this study, and they are not the same codes. A request to “make it shorter” can be a new constraint, the restoration of a length limit the user already set, or a stylistic revision. The difference matters if the design response is a memory of requirements rather than a general instruction to accept feedback. The codebook tells coders how to make that distinction. It does not import the PATH inventory as a cost inventory.

Liu et al. (2025) studied implicit feedback in WildChat and LMSYS-Chat-1M. In a densely annotated subset, feedback was common in later turns and often negative. Using the content of that feedback as a training signal helped on short benchmark items and did not help on harder ones. Their question is whether the user’s reaction can teach the model. The question here is what kinds of reaction constitute extra human work, and which of those kinds co-occur with an observable end to the initial goal.

Shaikh, Mozannar, Bansal, Fourney, and Horvitz (2025) coded grounding acts in WildChat, MultiWOZ, and Bing Chat. People initiated clarification and follow-up far more often than the models did. Early grounding failure predicted later breakdown. They released RIFTS, a benchmark of moments that call for clarification or follow-up, and tested whether models handle those moments. The finding that users carry grounding work is assumed here, not retested as a novelty. The coding scheme in this study starts from the user’s later turns and separates kinds of effort an interface could remember: a constraint added once, a requirement the model dropped, a factual correction, a check on uncertainty, and a change of goal.

Coding-specific studies describe shape and software quality rather than a general cost profile. Zhang et al. (2025) assembled 60,949 coding conversations from LMSYS-Chat-1M and WildChat and distinguished linear, star, and tree trajectories, with tree-shaped sessions longer and less satisfactory. Zhong et al. (2025) examined developer–LLM conversations derived from WildChat and related conversational moves to defects in generated code. Both are evidence that multi-turn coding is full of repair. They do not estimate the mix of repair types in writing, planning, information seeking, and creative production under one scheme.

Wang et al. (2026) come closest on the outcome side of difficulty. In finance and health conversations with ChatGPT and Gemini, they treat fragmented repetition and clarification after apparent misunderstanding as behavioral signs that a response was hard to handle. Length, readability, and lexical diversity predicted those signs only in combination. They are explicit that the signs are not a measure of cognitive load. This study shares the decision to read difficulty from repair behavior. It uses a wider set of user acts, several task types, and an ending state for the initial goal. It does not model response readability.

### 2.3. Repair as an HCI problem

Conversation analysis treats repair as the organized set of practices by which people handle trouble in speaking, hearing, or understanding (Schegloff, Jefferson, & Sacks, 1977). Grounding research treats mutual understanding as something participants build, with costs on both sides (Clark & Brennan, 1991; Clark & Wilkes-Gibbs, 1986). HCI research on spoken dialogue systems has used those ideas to compare how a system should respond when understanding fails (Meck et al., 2023).

Generative chat shifts the trouble. The system often produces a fluent answer rather than a non-understanding, and the user then has to decide whether the answer missed the goal, violated a constraint, or needs a different form. The user’s next message is the evidence this study can code. It is evidence of observable work. It is not evidence of how hard the user thought, how long they looked at the answer, or whether they used the answer outside the window.

That limit is why ending state is defined behaviorally. Explicit acceptance, a later turn that uses the result and starts a new goal, continued repair of the same goal, and explicit abandonment can be seen in the log. A conversation that simply stops cannot. The stop is indeterminate. Treating it as success would inflate the apparent ease of the system. Treating it as abandonment would inflate the apparent failure. Indeterminate is its own category.

### 2.4. The gap this study fills

The literature now supports three statements. Users do a variety of things after the first prompt. Much of the grounding work falls on the user. A token-based cost, set against rubric quality, shows that good artifacts can be cheap or expensive in assigned tasks. The open measurement is the composition of the user’s post-request work in unconstrained ChatGPT conversations, its variation across task types, and its association with behavioral signs that the initial goal was resolved, is still being repaired, or was dropped. The design stake is whether an interface can hold the requirements that users currently have to type again.

## 3. Materials and methods

### 3.1. Construct and codes

Human–AI interaction cost is operationalized as a profile of eight actions on user messages after the first message of a conversation, while the user is still pursuing the initial goal.

- **Clarification.** The user explains the meaning they already had, because the assistant missed it or answered a different reading.
- **Correction.** The user states that the output is factually wrong, inconsistent, or noncompliant with an instruction already given.
- **Constraint addition.** The user adds a limit or condition that was not stated before.
- **Requirement restoration.** The user repeats a requirement from an earlier user message that the assistant dropped or violated.
- **Repetition.** The user asks again for essentially the same thing, with no material new instruction.
- **Revision request.** The user asks for another attempt and specifies a change in tone, emphasis, structure, or wording that is not a factual correction and not the restoration of an earlier requirement.
- **Verification.** The user asks the assistant to confirm correctness, sources, or uncertainty without stating an error.
- **Redirection.** The user leaves the initial goal and sets a different task.

A turn may receive more than one code. Priority rules remove the losing code when two inclusion rules only appear to overlap. A material change beats repetition. A requirement that was stated earlier beats a code of “new constraint.” A stated factual or instruction-following error beats a revision request. A bare “are you sure?” stays verification. Leaving the goal is redirection and does not also receive same-goal repair codes. The full inclusion, exclusion, and priority rules, with constructed illustrations, are the coder instructions in Appendix A.

Four further turn marks are recorded and are not part of the cost profile: an acceptance signal, an abandonment signal, an answer to a question the assistant asked, and social text such as thanks. Supplying a detail the assistant requested is coordination. It becomes cost only when a cost rule is also met. A first message that corrects an output not present in the conversation is flagged as context-free repair and is excluded from the profile, because the prior model turn is unobserved.

Task type is assigned from the initial user message: writing, coding, information seeking, planning, creative production, or other task. Non-task exchanges (greetings, bot tests, chit-chat with no ask, and jailbreaks whose point is the jailbreak) are screened out of the quota. A jailbreak wrapped around a real task is coded as the task.

Ending state refers to the initial goal only.

- **Explicit acceptance.** The user affirms the output and does not keep repairing it.
- **New goal after use.** The user treats the output as usable and moves to a different goal.
- **Continued repair.** The last move aimed at the initial goal is still one of the cost actions.
- **Explicit abandonment.** The user quits the initial goal in words.
- **Indeterminate.** The log ends with no signal. Every single-message conversation is indeterminate. A trailing “thanks” with no judgment is indeterminate.

Apparent resolution, used in the regression, is the union of explicit acceptance and new goal after use. Coders record the fine category.

### 3.2. Data

The sampling frame is the public non-toxic release `allenai/WildChat-1M` (Zhao et al., 2024), licensed under the Open Data Commons Attribution License. The dataset card lists 837,989 conversations after the removal of toxic conversations and a later removal of conversations flagged for personal or sensitive information. Users contributed the chats through affirmative opt-in while using a chatbot served by GPT-3.5 or GPT-4. The gated release that retains toxic conversations, and any larger WildChat release, are not in the frame.

A conversation is eligible when its conversation-level language field is English and it contains at least one non-empty user message and one non-empty assistant message. Country, state, hashed IP address, and request headers are not read and are not written into the coding files. Model name and timestamp are stored on a text-free manifest so the sample can be described. They are not predictors.

`conversation_hash` is not unique. The key used in the manifest is the hash, the conversation timestamp, and the first turn identifier.

### 3.3. Sample

The draw is a single streaming pass, seed 20261001, implemented in `analysis/sample_wildchat.py`. It takes a simple random sample of 840 eligible English conversations and partitions that sample at random into a pilot of 40 and a screening pool of 800. The pilot is used only to revise the codebook. It is excluded from confirmatory estimates.

Humans screen the pool. The main sample keeps task-oriented conversations and fills a quota across the task types that are present. The cap is 60 conversations per task and 360 overall. With fewer than six task types present, each present type still caps at 60 and the total is lower. Unused seats are not given to another task. Within each task, the draw keeps both single-user-turn and multi-user-turn conversations when both exist, so indeterminate stops are not designed out of the sample. The quota rule is deterministic given the seed and is tested in `analysis/test_pipeline.py`.

This quota supports comparison across tasks. It is not a probability sample of English WildChat, and the estimates will not be weighted back to the 837,989-row release. The manuscript will report the screening counts so a reader can see how many pool conversations were non-task or uninterpretable.

The dataset revision actually read is recorded in `data/share/draw-metadata.json` at the time of the draw. Message text stays in local coding packets. The deposited files are the codebook, the keys, and the annotations.

### 3.4. Coding procedure

Coding is human. A generative model is not used to assign codes. An automatic label would conflict with the decision to avoid a model API, and it would make a model the judge of the work users spent correcting a model.

The coder reads a packet that contains only the ordered user and assistant messages, a sample identifier, the model name, and a redaction flag. For each conversation the coder sets screen, task type, and ending state. For each user message the coder sets every code column to 0 or 1. A blank cell means the row is unfinished, and the analysis script refuses to run while blanks remain.

The first user message is the initial request. Cost codes on that message are 0. Later messages are coded for work on the same goal. A message that starts a new goal is redirection, and the ending state of the initial goal is judged separately.

The pilot of 40 conversations is coded first. Diagnostics (`analysis/pilot_diagnostics.py`) report which codes occur, which codes never occur, and which codes co-occur. The codebook is revised from those diagnostics and from coder notes. The revised instructions become version 1 before the pool is coded for the confirmatory sample. Version 0 is not edited in place after coding under it has started.

### 3.5. Reliability

A second coder independently codes 80 conversations drawn from the main sample with seed 20261001 (`python analysis/irr.py --select-from data/share/main-manifest.csv --n 80`). The second coder does not see the primary codes. Cohen’s kappa is computed for each binary turn code and for task type and ending state. Each cost code is expected to reach at least 0.70. A cost code below that threshold sends the codebook back for revision and recoding of the affected distinction. Prevalence is reported beside kappa so a rare code is not described as merely unreliable. The second coder is a researcher. No research participants are recruited.

### 3.6. Analysis

The coded sheet is summarized by `analysis/analyze.py`. The script writes tables. It does not write interface principles.

For RQ1, the estimate is the proportion of main-sample conversations that contain each cost code at least once, with a Wilson confidence interval, plus the count of post-request turns carrying the code. Post-request means every user message after the first.

For RQ2, the composition is the mean, within each task, of the conversation-level rate of each code. The rate is the number of post-request turns with the code divided by the number of post-request turns. A conversation with no post-request turn has rate zero and remains in the descriptive table, because “no further work in the log” is part of the phenomenon. A Kruskal–Wallis test compares rates across tasks for each code. A chi-square test compares presence of the code across tasks. Tests are omitted when a code has no variation or a table has no contrast, and the omission is reported rather than replaced with a result.

For RQ3, the predictors are pre-terminal rates. The pre-terminal window is every user message after the first and before the last. The last user message is reserved as evidence for the ending state, so the same tokens are not used as both the predictor and the outcome. Conversations whose only user message is the initial request contribute a pre-terminal rate of zero. The outcome is the ending group: apparent resolution, continued repair, explicit abandonment, or indeterminate. A group with fewer than 15 conversations is omitted from the model and named in the note. The model is a multinomial logit of ending group on the pre-terminal rates, task type, and the natural log of one plus the initial request’s word count. Indeterminate is the reference category when it remains in the model. Rates with no variance are dropped. Coefficients are associations. A sensitivity refits the model with rates computed on all post-request turns, including the last, and the manuscript will say if the pattern depends on that choice.

For RQ4, the script lists up to eight lower-cost conversations among those coded as apparent resolution and up to eight higher-cost conversations among those coded as continued repair or explicit abandonment, using quartiles of the pre-terminal cost count. The qualitative comparison of those packets is done by hand. Design statements are written only after that reading, and only for action types that recur.

No interaction-cost index is computed unless the coded profiles, after the fact, show a structure that a composite would summarize without hiding the distinctions the study exists to make.

### 3.7. Ethics

The study is a secondary analysis of a public, opt-in corpus. It collects no new user data. It does not attempt to link hashed IP addresses to people, and those fields are excluded from the working files. Quotations in the article, when results are written, will be short, stripped of names and contact details, and checked against the redaction already present in the release. Packets marked uninterpretable because redaction removed the goal are not forced into a task type.

## 4. Results

No estimates are reported in this draft. Results will be inserted only after human coding of the pilot, revision of the codebook, reliability coding, and analysis of the main sample. The script that produces the tables refuses to run on a sheet with blank codes, so an unfinished sheet cannot be summarized into frequencies by accident.

### 4.1. Forms of post-request work (RQ1)

[Pending. Conversation-level proportions, Wilson intervals, and turn counts for the eight cost codes.]

### 4.2. Composition across task types (RQ2)

[Pending. Mean rates by task, with the Kruskal–Wallis and chi-square tests that the data support.]

### 4.3. Association with ending state (RQ3)

[Pending. Multinomial logit of ending group on pre-terminal rates, task, and initial-request length, plus the sensitivity that includes the last user turn.]

### 4.4. Trajectories (RQ4)

[Pending. Qualitative comparison of the packets listed by the analysis script.]

## 5. Discussion

### 5.1. How the estimates will be read

The discussion will stay inside what the codes can support. A higher rate of requirement restoration in one task means that, in this sample, users in that task more often restated a requirement the assistant had already been given. It does not mean the assistant failed more often in an absolute sense, because an unstated failure that the user silently accepted is indeterminate, not a restoration. A positive association between pre-terminal correction and continued repair means those two codes travel together in the log. It does not mean that correcting the assistant causes the conversation to fail, and it does not mean that users should correct less.

Comparisons with Imai et al. (2026) will be drawn at the level of the construct. Where their sessions separate costly success from productive success by tokens and rubric quality, this study can separate kinds of user work and kinds of ending. It cannot reproduce their seventy-fold cost ratio, because it does not use their cost function or their quality scores. Where Mysore et al. (2025) describe how writing follow-ups cluster, this study can say which of those surface behaviors were coded as new constraints, restored requirements, or revisions, if the sample contains them.

The absence of a weighted index will be maintained if the profiles are not one-dimensional. A single score that adds a verification question to a repeated correction would recreate the problem the study is designed to avoid.

### 5.2. Interface implications

[Pending. Principles will be stated only for cost codes that recur in the main sample. The protocol’s hypotheses, which are not findings, are that repeated constraint addition and requirement restoration would be reduced by a visible, persistent requirement list; that repeated correction would be reduced by a retained correction the next turn must respect; and that long repair sequences would be reduced by an explicit goal state and by an offer to restate the requirements before another attempt. Each hypothesis will be kept, narrowed, or dropped after RQ4.]

### 5.3. Fit with the journal

The object of the study is the user’s work and the interface that currently makes that work necessary. The methods produce no new model and no training recipe. That scope is intentional. A result that stopped at “users send many follow-up messages” would not be an HCI result. The result this design can support is a statement about which follow-ups are repeated human work, and what an interface would have to remember in order to take that work off the user.

## 6. Limitations

The ending state is not task success. Users can accept a wrong answer, abandon a conversation and succeed elsewhere, or stop because the first answer was enough. Indeterminate is the honest code for the last of these, and it is also the code for a quiet failure. The two cannot be separated here.

The sample is English conversations from one public, non-toxic release of one chatbot service collected under an opt-in research arrangement. Users who opted in, and tasks that remain after toxicity filtering, may differ from general ChatGPT use. Quota sampling balances task types for comparison. It does not estimate the share of each task in the full release.

The coder sees text, not timing, attention, or edits the user typed and deleted. Two messages with the same code can cost the user very different effort. The study claims an observable classification, not a measure of workload in the sense of subjective or physiological load (see also Wang et al., 2026, on the gap between repair traces and cognitive load).

Multi-label coding and priority rules will leave residual disagreement. The reliability threshold is the check. A code that cannot be applied consistently will be merged or dropped in version 1 of the codebook, and the manuscript will report that change rather than defend the original list.

The pre-terminal window is conservative. In a conversation with one follow-up, that follow-up is the ending evidence and does not enter the RQ3 predictors. Short repairs are therefore visible in the RQ1 and RQ2 profiles and weak in the regression. The sensitivity that includes the last turn is reported for that reason.

The author used a generative AI assistant to search the literature, draft text, and write the sampling and analysis scripts. That assistance is disclosed below. It is a limitation on the drafting process, not a source of conversation codes. The codes, the reliability coefficients, and the findings still have to be produced by human coding. Until they exist, this document is a methods-complete manuscript without results, and it should not be submitted.

## 7. Conclusion

[Pending. The conclusion will restate the cost profile, the task differences the tests support, and the interface implications tied to repeated codes. It will not add a weighted index unless the coded structure supports one.]

## Acknowledgments

[Pending. Name the second coder here if they should be acknowledged rather than listed as an author.]

## Declaration of interest

The authors report there are no competing interests to declare.

## Funding

No funding was obtained for the reported work.

## Declaration of generative AI use

The author used a generative AI assistant (Grok, accessed through the Cursor editor) to search the literature, draft manuscript text, and write the sampling and analysis scripts. The author reviewed and revised the drafted text and is responsible for the manuscript. The assistant did not assign codes to WildChat conversations. All empirical codes are assigned by human coders under the codebook. No generative model is part of the measurement.

## Data availability

The conversation corpus is WildChat-1M (Zhao et al., 2024), available from the Allen Institute for AI on Hugging Face under the Open Data Commons Attribution License: https://huggingface.co/datasets/allenai/WildChat-1M. This study will deposit the codebook, the conversation keys, and the human annotations in a public repository before submission, and will place the repository identifier here. Message text will not be redistributed. `conversation_hash` alone does not identify a unique WildChat row; the deposited key joins that hash with the conversation timestamp and the first turn identifier. Readers can recover the text from the original release. The local coding packets, which contain message text, are working files and are not part of the deposit.

## References

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

## Appendix A. Coder instructions

The coder-facing codebook, version 0, is `methods/codebook-v0.md`. It will be inserted here in full at submission, using the version under which the main sample was coded. Version 0 is the pre-pilot instructions. It is not revised until the pilot diagnostics exist.

## Appendix B. Sampling and analysis implementation

The sampling protocol is `methods/sampling-protocol.md`. The draw, the reliability calculation, the pilot diagnostics, and the confirmatory tables are `analysis/sample_wildchat.py`, `analysis/irr.py`, `analysis/pilot_diagnostics.py`, and `analysis/analyze.py`.
