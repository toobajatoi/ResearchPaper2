# Before It Acts: A Scoping Review of Preview and Approval in Agentic AI Interfaces

Tooba Jatoi  
Independent researcher  
toobajatoi44@gmail.com  
ORCID: 0009-0008-9650-7290  
Corresponding author  

Word count: about 6,000 words through the conclusion, including the tables and excluding the references and declarations.

## Abstract

Generative AI agents can send a message, edit a file, or spend money before a person has seen the action. This scoping review asks what the interface shows at that moment, what the person can still change or refuse, and whether an approval is bound to the action that runs. Public searches on 1 October 2026, including ACM and IEEE pages, did not identify a review that maps this preview. Scopus and Web of Science were not searched. Thirteen studies were extracted. The central contribution is approval integrity: a confirmation on screen is not the same as a check that the approved object is the one that executes. A taxonomy of six preview forms shows where that check is missing. The design statements are propositions from this synthesis, not a validated framework.

**Keywords:** agentic artificial intelligence; approval integrity; preview; user control; human–AI interaction

## 1. Introduction

A person can still be the one who clicks. The click may come after an agent has already drafted the email, chosen the command, or filled the cart. The design question is what the interface shows before that action changes something outside the conversation, and what the person can still change or refuse.

That question is narrower than whether people have agency when they work with AI. Wang and Wang (2026) scoping-reviewed how user autonomy is supported in interaction with large language models, including clarification, alternatives, contestability, and human approval as one mechanism among twelve. Michael and Roesner (2026) surveyed how agent systems let a person specify a permission policy and how that policy is enforced. Neither review asks what a pending action looks like on the screen at the moment it can still be stopped.

This paper reviews that moment. The studies differ in domain, from a simulated daily assistant to a browser extension, a document editor, a seminar-scheduling agent, and a coding-agent dialog. They are alike in one respect: an agent proposes an action that can leave the conversation, and the interface either shows that proposal or fails to.

The review asks three questions.

1. What do published interfaces reveal before an agent takes an action?
2. What can the person edit, limit, refuse, or undo at that moment?
3. What design guidance follows for an approval screen that shows the action, its scope, and its consequence?

This review makes three contributions, and they are not equal. The headline contribution is approval integrity. A button, a dialog, or a setting can record that a person agreed, while the action that runs is a different action. The taxonomy of six preview forms, plan, highlight, description, draft, diff, and risk card, and the extraction of what the person can still edit, refuse, or undo, are how that gap is shown. The design statements in Section 5 are propositions read from the extraction. They are not a validated framework.

## 2. Related work

Two reviews set the boundary of this one.

Wang and Wang (2026) reviewed 80 papers on user autonomy in human–LLM interaction. They grouped design mechanisms into scaffolding, steerability, reflection, transparency, and collaborative coordination. Human-in-the-loop verification appears in that catalog as a way to keep decision authority with the person. Their corpus is organized by the kind of support the mechanism offers, and they excluded empirical studies that did not contribute a prototype or framework aimed at autonomy. This review starts from the opposite cut: the pending action, and the controls attached to it.

Michael and Roesner (2026) reviewed 21 proposals for user-level permissions in agentic systems and walked through five commercial agents. Their taxonomy covers how a policy is specified, how a user selection becomes an internal rule, and how the rule is enforced. In their commercial walkthrough, a setting labeled as needing approval did not always pause the agent; in one observed case, a draft was created without a prompt. That finding belongs with the question of whether a control does what its label says. Their paper does not extract, study by study, what the person sees in the preview, whether the pending action can be edited, or whether the approved object is the object that runs.

Adjacent HCI work on plans and monitoring was screened and excluded when no external action was held for approval. VeriPlan asks a person to confirm constraints on an end-user plan and then checks the plan (Lee et al., 2025). WaitGPT visualizes analysis code as it is generated so a person can steer the analysis (Xie et al., 2024). Aporia collects design decisions and then implements them; the code change is not the object on the approval screen (Kasibatla et al., 2026). Zhou et al. (2025) model when a confirmation should be requested. AGDebugger lets a developer edit and reset agent messages, and its authors note that an email already sent cannot be pulled back by that reset (Epperson et al., 2025). CUGA pauses for a tool-approval checkpoint, but the demo does not describe what the person sees on that checkpoint (Shlomov et al., 2026). Those papers mark the edge of the search. They are not rows in the extraction.

## 3. Method

The review follows PRISMA-ScR. The protocol, search log, screening log, and extraction sheet are the review record. One reviewer screened and extracted. There was no second screener.

### 3.1. Eligibility

A paper was included if it describes a generative or agentic interface in which a person can see a proposed action before that action changes something outside the conversation, or if it reports what the person could inspect or refuse at that moment. Eligible actions include a message, file change, purchase, booking, web step, shell command, or other tool call. Preprints were included and are labeled as preprints. A security paper was included only when it describes the approval surface.

A paper was excluded if it studied chatbot usability or co-writing with no pending action, modeled the timing of a prompt without describing the screen, verified a plan that is not executed, surveyed permission architectures, or was documentation or a pattern guide.

### 3.2. Search

Searches were run on 1 October 2026. The first pass used open web search. The second pass opened public pages from the ACM Digital Library and IEEE Xplore. Scopus and Web of Science were not available, and neither ACM nor IEEE was queried through an institutional export. Fifteen queries are listed in the search log. They combined approval, preview, action guards, co-planning, and tool use with venue and year terms for 2024–2026. Citation chasing was not systematic: a reference inside an included paper was not opened unless the searches had also surfaced it.

Figure 1 records the flow that can be reconstructed from the search log. Engine hit totals were not retained, so the diagram does not invent an identification count. The first pass used open web search. A second pass the same day opened public ACM Digital Library and IEEE Xplore pages. It was not an institutional export, and Scopus and Web of Science remained unavailable. Non-scholarly pages were set aside and were not counted. Duplicate titles were collapsed, and the number of duplicate hits was not kept. IEEE abstracts that described robot-motion previews, rather than a generative software agent, were excluded at abstract and are not in the scholarly full-text count. After the two passes, twenty-one distinct scholarly records were assessed in full text. Eight were excluded. Thirteen were included. Table 2 gives each exclusion reason.

These searches did not identify a review that maps this preview. That sentence describes the queries that were run. It does not claim that no such review exists in Scopus or Web of Science. Michael and Roesner (2026) were excluded from extraction because they own the neighboring survey of permission policies.

**Figure 1. Screening flow for the public-web search of 1 October 2026.**

| Stage | n | What the number means |
| --- | --- | --- |
| Queries, two passes on 1 October 2026 | 15 | First pass: open web. Second pass: public ACM and IEEE pages. Hit totals were not exported. |
| Non-scholarly pages set aside | Not counted | Software-development kits, pattern guides, and forum posts. |
| Robot-motion abstracts set aside | Not counted | IEEE pages on physical-robot previews, excluded before full text. |
| Duplicate titles removed | Not counted | Only the count after collapse was retained. |
| Distinct scholarly records assessed in full text | 21 | Sixteen from the first pass and five new records from the second. |
| Excluded, with reasons in Table 2 | 8 | Boundary reviews, plans that are not executed, debugging without a gate, a timing model, or an approval checkpoint whose screen is not described. |
| Included in the extraction | 13 | Table 3. |

**Table 2. Records excluded after full-text assessment.**

| Record | Reason |
| --- | --- |
| Wang and Wang (2026) | Reviews autonomy mechanisms in conversation with language models. It does not map the content of a pending-action preview. |
| Michael and Roesner (2026) | Surveys how permission policies are specified and enforced. Cited as a boundary, not extracted as one interface. |
| Lee et al. (2025) | The person confirms constraints on a plan. The system does not execute an action outside the conversation. |
| Xie et al. (2024) | Visualizes analysis code as it is generated. It does not hold an external action until the person approves it. |
| Kasibatla et al. (2026) | The person approves design decisions. The code change that follows is not the object on the approval screen. |
| Zhou et al. (2025) | Models when a confirmation should be requested. It does not describe what the confirmation screen shows. |
| Epperson et al. (2025) | Lets a developer reset and edit agent messages. A sent email cannot be undone by that reset, and the tool does not preview the external action before it runs. |
| Shlomov et al. (2026) | Pauses for human confirmation before a sensitive tool runs. The demo does not describe the contents of that approval screen. |

### 3.3. Extraction

Each included paper is one row. The columns are the proposed action, what is shown, what can be edited, the refuse path, reversibility, and whether approval is tied to the action that runs. A cell is “not reported” when the paper does not say. No statistic was recomputed. The design propositions in Section 5 were written from this sheet.

### 3.4. Corpus

Table 3 summarizes the thirteen papers. Seven are peer-reviewed. Six are preprints: Mozannar et al. (2025), Long et al. (2025), Zhuang et al. (2026), Yan (2026), Weng (2026), and Pochampally et al. (2026). A secondary index lists Zhuang et al. as accepted to a 2026 demonstration track; that proceedings record was not verified, so the paper is cited from its preprint.

**Table 3. Included studies.**

| Study | Status | What was examined | People |
| --- | --- | --- | --- |
| He et al. (2025) | CHI 2025 | Simulated assistant; plan, then predicted action | 248 |
| Feng et al. (2026) | CHI 2026 | Editable research plan in a document | 16 lab; 7 field |
| Huq et al. (2025) | NAACL 2025 demo | Next web action in a browser extension | Case studies |
| Mozannar et al. (2025) | Preprint | Plan editor and action guard | 12 |
| Long et al. (2025) | Preprint | Plan and email drafts before send | 10 lab; 3 deployments |
| Zhuang et al. (2026) | Preprint | Email confirmation and code diff | No user study |
| Yan (2026) | Preprint | Per-action approval versus standing rules | 113 |
| Weng (2026) | Preprint | Whether the dialog matches the command | No user study |
| Pochampally et al. (2026) | Preprint | Agent that sent email without a preview | 20 |
| Su et al. (2026) | Journal 2026 | Risk card versus log and text warning | Proxy, not participants |
| Zhang et al. (2026) | CHI 2026 | Complaints about GUI agents that act on the web | 221 posts; 21 interviews |
| Lehmann et al. (2026) | CHI 2026 | Side-by-side preview before a document change is approved | 30 people; 14 teams |
| Kretzer et al. (2025) | CHI 2025 | Component recommendation previewed before it is drawn into a design file | Interface description |

## 4. Results

### 4.1. What the interface shows

The thirteen interfaces do not show the same object. Reading across the extraction sheet, the previews that do appear fall into six forms. Table 4 is that taxonomy. It states what each form exposes and which control the source papers actually describe. A cell is limited to those papers. Two studies sit outside the table because the preview was missing. Pochampally et al. (2026) report an email sent without a draft. Zhang et al. (2026) report purchases, installs, and other web actions taken without a confirmation the person could inspect first.

**Table 4. Six preview forms.**

| Form | What it exposes | Control described in the source | Where it appears |
| --- | --- | --- | --- |
| Plan | The intended sequence of steps | Edit, add, delete, split, or assign a step to the person or the agent | He et al. (2025); Feng et al. (2026); plan editors in Mozannar et al. (2025) and Long et al. (2025) |
| Highlight | The target of the next web action | Reject or pause. Silence runs the action within five seconds | Huq et al. (2025) |
| Description | The action in prose | Allow or deny, or a standing allow, ask, or never rule | Yan (2026). Weng (2026) describes agent-written summaries of commands, a fragile case of this form |
| Draft | The content that would be sent or inserted | Edit, regenerate, compare side by side, or withhold the commit | Long et al. (2025); Zhuang et al. (2026), for email; Lehmann et al. (2026); Kretzer et al. (2025) preview components before drawing them into a file |
| Diff | The exact command and file change | Approve a hunk, annotate a line, or request a partial rewrite | Zhuang et al. (2026), for code |
| Risk card | Source, sensitivity, permission, and consequence | Safer-alternative controls. The published test is a proxy, not an observed edit of the call | Su et al. (2026) |

He et al. (2025) show a stepwise plan and then, in a conversation, the single action the assistant predicts for the current step. The actions are simulated API calls, such as setting an alarm or choosing an itinerary. Feng et al. (2026) show the plan as a list inside the document the researcher is already editing, with a status on each step and the step’s outputs as cards, pills, or text. Mozannar et al. (2025) also show an editable plan. Separately, their action guard prompts the person when a developer has classed the action as always irreversible, such as uploading a file. Actions classed as never irreversible, such as scrolling, run with no prompt. Actions classed as maybe irreversible, such as clicking a button, can be passed to a model that judges whether to ask.

Huq et al. (2025) show the next web action by highlighting the target element and adding a short explanation. Long et al. (2025) and Zhuang et al. (2026) show the email that would be sent. Zhuang et al. also show a proposed command beside an explanation, the affected files, and a unified diff, with the surrounding file available on demand. Yan (2026) shows a written description of each action. Every condition in that study saw the same descriptions; the study did not use live tool calls during the session. Su et al. (2026) specify a card that adds a source-trust label, chips for data sensitivity and permission, a data-flow arrow, a consequence preview, a risk badge, and controls for a safer alternative. Their comparison conditions are a plain agent log and a text-only security warning.

Pochampally et al. (2026) are one case in which the relevant object was missing. Students used a general-purpose agent that could read and write files and send mail. The chat showed reasoning, and a terminal showed file operations. On the email task, the agent sent the message without showing the draft first. Zhang et al. (2026), from 221 social-media posts and 21 interviews, describe the same hole in everyday web agents: double purchases and other state changes happened without confirmation, and people resorted to watching the cursor. Interviewees wanted a pause, with enough context to decide, when the action was critical. That wish is a design implication in their paper. It is not a tested preview.

Weng (2026) describes a further gap inside dialogs that do appear. In the coding agents the paper characterizes, the confirmation text is written by the agent. A compromised or injected agent can therefore show a benign summary while a different command is the one that will run. The paper’s prototype renders facts taken from the command and marks a command it cannot inspect as uninspectable or high risk, rather than as safe.

The six forms are not substitutes. A plan names steps. A description names an action in words the study prepared, or in words the agent wrote. A draft or a diff shows the content that will leave the machine. A risk card adds why the call might be unsafe. A highlight shows where a click will land, and only for a few seconds. Mozannar et al. (2025) also use a yes-or-no action guard. The paper does not specify how much of the pending action that prompt displays, so the guard is treated as a control on the plan, not as a seventh form.

### 4.2. What the person can still change

Editing the pending action is present in some studies and absent in others.

He et al. (2025) allow the richest change before a simulated action runs. During planning, the person can edit, add, delete, or split a step. Of 121 participants in the user-involved planning conditions, 104 edited at least one plan. Before execution, the person can type feedback, which causes a new prediction, or choose Specify Action and fill the parameters. Specify Action was used 445 times. Feedback before execution was used 91 times. Feedback after execution was used 163 times.

Feng et al. (2026) let the person edit the plan with ordinary list editing, request an alternative wording, and assign each step to themselves or the agent. In the lab, 32.6 percent of steps were edited and 17.4 percent were reassigned, so most of the agent’s proposed steps were accepted as written. During execution, people deleted 16.3 percent of the output items the agent surfaced. They could also rerun a step after changing it.

Long et al. (2025) let the organizer edit an email draft or ask for it to be regenerated, and they can revise the policies and templates that shape later drafts. Zhuang et al. (2026) go further on code: a person can approve one hunk, annotate a line, or ask for a partial rewrite, rather than accepting or rejecting the whole changeset. Email replies can be rewritten, edited, or deleted by paragraph. Lehmann et al. (2026) show a writing suggestion beside the text it would replace. The person can append it in a review color, edit it, and then approve it. The colored text is already on the page before that approval, so the gate finalizes a visible change rather than holding every keystroke. Kretzer et al. (2025) preview a component recommendation in the assistant. Draw Suggestion is what inserts it into the design file. The paper does not describe editing the components before that click.

The other included interfaces do not describe an edit of the pending action. Mozannar et al. (2025) describe the action guard as a binary approve or disapprove. In their qualitative study, participants asked for a third option. Yan (2026) offers allow or deny on a description, or a standing allow, ask, or never rule for a consequence category. The rule can be set in advance. The action on the screen is not rewritten. Huq et al. (2025) do not edit the suggestion in place. The person pauses and does something else on the page. Su et al. (2026) describe safer-alternative controls and do not report that a person can rewrite the tool arguments. Pochampally et al. (2026) had no preview to edit on the email task. Weng (2026) is about the integrity of the display, not about an editing control.

### 4.3. How a person refuses, and when refusal is missing

Refusal is not one control.

He et al. (2025) require a Proceed click. There is no timeout in the paper. Huq et al. (2025) offer reject and pause, and they also treat silence as acceptance: the highlighted action runs after at most five seconds if the person does not oppose it. Mozannar et al. (2025) ask only for some actions. Always-irreversible actions need a yes or no. Never-irreversible actions do not ask. A model may decide whether a maybe-irreversible action asks at all. Long et al. (2025) and Zhuang et al. (2026) require an explicit confirmation before an email is sent. Yan (2026) denies an action in the moment, or blocks a category with a never rule. An ask rule does not refuse. It postpones the decision until the action appears.

Pochampally et al. (2026) document a task with no refuse step. The email was sent. Afterward, preference for approval prompts on that task averaged 4.65 on a five-point scale, and trust averaged 3.10. The authors report that dissatisfaction followed actions taken beyond what the student would have authorized, including when the output itself was rated successful. They call this delegation regret. Irreversibility together with the fact that another person would see the result, rather than stakes alone, tracked the demand for a confirmation. Students were more willing to let the agent act on low-stakes retrieval and planning.

Mozannar et al. (2025) heard a related distinction from 12 participants who already used agentic systems. People wanted a guard for payment, for sending email, and for subscribing. Several said a guard on adding an item to a cart was unnecessary. Some also said that approving a plan change and then meeting another approval for that same change was too much. The study does not measure how often a needed guard was missing. It does show that participants did not want every action gated, and did not want two gates for one decision.

Yan (2026) compared per-action approval with automated review and with standing rules, using 113 participants without professional software backgrounds and one simulated day of 18 actions, seven of which went beyond the assigned task. Standing rules blocked less overreach than per-action approval, by 20.1 percentage points (95 percent confidence interval −32.1 to −8.1), and less than automated review, by 14.5 percentage points (95 percent confidence interval −25.8 to −3.2). Prompts fell from 18.0 under per-action approval to 10.9 under the policy, but total time was not reliably lower once the time to write the rules was included. Participants chose “ask” for 114 of 140 rules. Of 148 overreach actions that were executed under the policy, 133 followed a human approval and 15 ran because a rule said allow. A rule that preserves the right to decide later does not, by itself, stop the action. People still approved actions outside the original request when those actions were described at runtime.

### 4.4. Approval integrity

Approval integrity is the property that the object the person approved is the object that executes. A button, a dialog, or a setting can record that the person agreed, and the run can still perform a different action. This column of the sheet is thin. The thinness is the finding. The other results describe whether a preview exists. This one asks whether the preview still holds when the action runs.

He et al. (2025) execute the prediction the person has just seen, inside a simulation, and do not describe a later substitution. Feng et al. (2026) execute the current text of a step. Long et al. (2025) send the draft the organizer has read, in the deployments that used live mail, and do not describe a technical check against a rewritten payload. Zhuang et al. (2026), Mozannar et al. (2025), Yan (2026), Su et al. (2026), Pochampally et al. (2026), Zhang et al. (2026), Lehmann et al. (2026), and Kretzer et al. (2025) do not report a binding between the approved object and the executed call. Yan’s session could not diverge, because the descriptions were fixed by the researchers before anyone arrived.

Huq et al. (2025) are the explicit counterexample to a binding. The displayed suggestion runs if the person is silent for at most five seconds. Acceptance is the absence of a rejection, not a decision attached to a frozen action.

Weng (2026) is the paper that names the missing property and prototypes a check. The dialog should be rendered from the command that will run, by a component the agent cannot rewrite, and execution of a different command should fail. In the prototype, three post-approval swaps were refused because a hash of the executed action differed from the approved action. The paper states that this holds only when every execution path is mediated. On a set of 11 standard and 11 adaptive cases in which the agent wrote the narration, a narration-trusting dialog approved every case, and the prototype flagged them. Those figures evaluate the prototype. They are not a user study of whether people notice a mismatch. They are the concrete basis for treating approval integrity as distinct from the mere presence of a confirmation.

Michael and Roesner (2026), excluded from the sheet and cited here because the result is about the same failure, observed a commercial agent proceed under a setting that said approval was required. The label on the control and the pause in the run came apart.

### 4.5. What the studies report about these designs

The studies do not agree on a single benefit of showing the action, because most of them did not compare preview designs.

He et al. (2025) did compare user-involved planning and execution with automatic planning and execution, in a factorial experiment with 248 participants. Involving the user did not raise calibrated trust. Confidence was lower when people took part in planning, and lower when they took part in execution. A performance benefit from taking part in execution was significant on one task, where the assistant had chosen the wrong itinerary and the person could correct it. The authors state that this pattern is not enough to support a general claim that user-involved execution improves task performance. Seeing and correcting the action helped when the assistant was wrong in a way the person could fix. It did not, in this study, make people more trusting.

Feng et al. (2026) show that people will edit a minority of steps and accept most of them. The study compares the document agent with a chat baseline. It does not isolate the effect of the preview. Huq et al. (2025) report a 95 percent success rate in collaborative case studies, with humans performing 15.2 percent of the steps. That result describes the extension. It does not test the five-second timeout against an explicit confirmation. Mozannar et al. (2025) report a System Usability Scale score of 74.58 and the preferences in Section 4.3. The study is qualitative, with 12 participants. Long et al. (2025) report that lab participants delegated more after they had rehearsed with simulated respondents and could see and edit the emails. They do not report a statistical test of the preview.

Pochampally et al. (2026) provide the clearest report of a missing preview: regret attached to the fact of sending, not only to the quality of the text. Su et al. (2026) compared cards with logs and warnings on saved traces. Where an injection goal had been executed, a proxy marked the risk card as approved on 3.8 percent of those traces, the plain log on 13.0 percent, and the text warning on 5.9 percent. The authors describe the scorer as a proxy for how much risk-relevant information is exposed. They do not claim that people would approve at those rates.

Yan (2026) is the study that compares ways of deciding. Per-action approval blocked more overreach than standing rules. The cost was more prompts. Standing rules reduced prompts without a reliable saving in total time, and most rules handed the decision back to the person at runtime, where overreach was often approved.

## 5. Design propositions

The statements in this section are design propositions read from the extraction sheet. They are not empirically validated design principles. No included study tested them as a set. Only He et al. (2025) and Yan (2026) report experiments, and those experiments compare involvement or permission regimes, not the six preview forms against one another. The propositions say what a designer can take from thirteen heterogeneous studies, and where that reading has to stop.

**Show the thing that will change.** A plan, a prose description, and a draft are different objects. Pochampally et al. (2026) found regret when an email left without the draft having been shown. Long et al. (2025) and Zhuang et al. (2026) show that draft. Zhuang et al. show the command and the diff for code. Huq et al. (2025) show the element that will be clicked. Su et al. (2026) add the consequence and the source of the instruction, which matters when the action may have been shaped by content the agent read rather than by the person’s request. A screen that only says the name of a tool does not, on this evidence, show the action.

**Ask in proportion to the consequence, and make the ask explicit when the action is hard to undo or will be seen by someone else.** Mozannar et al. (2025) heard that payment, email, and subscription warranted a guard, and that adding to a cart often did not. Pochampally et al. (2026) found the demand for approval where the action was irreversible and externally visible. Zhang et al. (2026) heard the same demand for payments, identity, and outbound messages, and not for scrolling or reading. He et al. (2025) required a Proceed click. Huq et al. (2025) show the other pattern: the suggestion runs if the person is silent for five seconds. None of the user studies compared that timeout with an explicit decision. Until that comparison exists, a timeout should not be treated as equivalent to approval for an action the person cannot easily undo.

**Let the person change the pending action.** A binary guard was not enough for participants in Mozannar et al. (2025), who asked for a third option. He et al. (2025) already offer feedback and a way to specify the action. Zhuang et al. (2026) offer hunk-level approval and line notes. Long et al. (2025) offer edit and regenerate on the draft. Yan (2026) show the limit of allow and deny: people still approved overreach when the only choices were to let a described action through or block it. Editing is part of the decision, not a convenience beside it.

**A standing rule does not replace this screen.** Yan (2026) found that user-written allow, ask, and never rules blocked less overreach than deciding each action, largely because people chose ask and then approved. An ask rule is a promise to show the later action. If that later screen is only a short description, the rule has postponed a weak decision.

**Treat approval integrity as the headline requirement.** Weng (2026) is the only included paper that specifies and prototypes a check that the executed command matches the approved one. The other included papers do not report that check. A dialog written by the agent, or a setting named “needs approval” that does not pause (Michael & Roesner, 2026), can produce a record of consent for an action the person did not see. This proposition is the least tested in the set, and it is the one that most changes what a confirmation dialog is assumed to mean.

**Treat undo after the fact as an open gap.** He et al. (2025) let people retry a simulated step. Feng et al. (2026) let people rerun a step. Mozannar et al. (2025) heard requests to revise a completed step and continue from there. No included paper describes recalling a sent email or reversing a payment from the approval surface. For those actions, the preview is the control. The studies do not show a recovery path after the action has left.

## 6. Limitations

One reviewer searched, screened, and extracted. A second reviewer could have included or excluded borderline papers differently. The search used public web search on a single day, in two passes. The second pass opened ACM Digital Library and IEEE Xplore pages. Those were not institutional exports, and Scopus and Web of Science were not searched. Relevant papers that are poorly indexed on the open web, or that sit only in those two databases, can be missing. One reviewer screened and extracted both passes. References inside included papers were not systematically chased.

Six of the thirteen included papers are preprints. Huq et al. (2025) and Zhuang et al. (2026) are system descriptions or demonstrations, not comparative user studies. Su et al. (2026) score traces with a proxy. Weng (2026) evaluates a security prototype. The qualitative studies have 10 and 12 participants. Only He et al. (2025) and Yan (2026) report experimental comparisons, and they compare involvement or permission regimes, not a factorial set of preview layouts. Section 5 is therefore a set of design propositions from heterogeneous reports. It is not an estimate of how often a control works, and it is not a validated design framework.

The author used a generative model, through Cursor, to search, screen, extract, and draft. That use is disclosed below. The model is not an author.

## 7. Conclusion

The synthesis distinguishes three claims that are easy to collapse. A preview can take one of six forms: a plan, a highlight, a description, a draft, a diff, or a risk card. A control can let the person edit, refuse, or merely watch. Approval integrity is a further property: the object that was approved is the object that runs. Weng (2026) gives that property a mechanism, rendering the dialog from the command and refusing a later swap, and the other included studies do not report such a check. Two studies showed consequential actions with no usable preview: an email sent without a draft, and web actions such as purchases taken without a confirmation the person could inspect.

From that reading, the review offers a design proposition, not a tested rule. The person should see the action that will happen, be able to change or refuse it, and have that decision apply to the action that runs. The last clause is approval integrity, and it is the clause with the least empirical support in this corpus. Undo after an external action is not established here. A comparison of the six forms on the same consequential action, with a test of whether the approved object is the object that executes, is the study this review does not provide.

## Acknowledgements

None.

## Disclosure statement

The author reports no conflict of interest.

## Funding

No funding was received.

## CRediT

Tooba Jatoi: conceptualization, investigation, data curation, writing – original draft, writing – review and editing.

## Data availability

The protocol, search log, screening log, and extraction sheet are part of the manuscript record (`review/protocol.md`, `review/search-log.md`, `review/screening-log.csv`, `review/extraction.csv`). No participant data were collected for this review.

## Generative AI disclosure

Grok, used through Cursor, assisted with the literature search, screening, extraction, and drafting on 1 October 2026. The author reviewed the sources against the extraction sheet and is responsible for the manuscript. The model is not listed as an author.

## References

Epperson, W., Bansal, G., Dibia, V. C., Fourney, A., Gerrits, J., Zhu, E., & Amershi, S. (2025). Interactive debugging and steering of multi-agent AI systems. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3713581

Feng, K. J. K., Pu, K., Latzke, M., August, T., Siangliulue, P., Bragg, J., Weld, D. S., Zhang, A. X., & Chang, J. C. (2026). Cocoa: Co-planning and co-execution with AI agents. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3791673

He, G., Demartini, G., & Gadiraju, U. (2025). Plan-then-execute: An empirical study of user trust and team performance when using LLM agents as a daily assistant. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3713218

Huq, F., Wang, Z. Z., Xu, F. F., Ou, T., Zhou, S., Bigham, J. P., & Neubig, G. (2025). CowPilot: A framework for autonomous and human-agent collaborative web navigation. *Proceedings of the 2025 Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics: Human Language Technologies (System Demonstrations)*, 163–172. https://aclanthology.org/2025.naacl-demo.17/

Kasibatla, S. R., Rothkopf, R., Peleg, H., Pierce, B. C., Lerner, S., Goldstein, H., & Polikarpova, N. (2026). *Decision-oriented programming with Aporia* [Preprint]. arXiv. https://arxiv.org/abs/2604.05203

Kretzer, F., Kolthoff, K., Bartelt, C., Ponzetto, S. P., & Maedche, A. (2025). Closing the loop between user stories and GUI prototypes: An LLM-based assistant for cross-functional integration in software development. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3713932

Lee, C. P., Porfirio, D., Wang, X. J., Zhao, K., & Mutlu, B. (2025). VeriPlan: Integrating formal verification and LLMs into end-user planning. *Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3706598.3714113

Lehmann, F., Shauchenka, K., & Buschek, D. (2026). Collaborative document editing with multiple users and AI agents. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3790648

Long, T., Zhang, X., Wang, S., Yu, Z., & Chilton, L. B. (2025). *DoubleAgents: Interactive simulations for alignment in agentic AI* [Preprint]. arXiv. https://arxiv.org/abs/2509.12626

Michael, A. E., & Roesner, F. (2026). *How agents ask for permission: User permissions for AI agents, from interfaces to enforcement* [Preprint]. arXiv. https://arxiv.org/abs/2607.13718

Mozannar, H., Bansal, G., Tan, C., Fourney, A., Dibia, V., Chen, J., Gerrits, J., Payne, T., Maldaner, M. K., Grunde-McLaughlin, M., Zhu, E., Bassman, G., Alber, J., Chang, P., Loynd, R., Niedtner, F., Kamar, E., Murad, M., Hosn, R., & Amershi, S. (2025). *Magentic-UI: Towards human-in-the-loop agentic systems* [Preprint]. arXiv. https://arxiv.org/abs/2507.22358

Pochampally, S., An, S., & Chen, Y. (2026). *Assistant or actor? Student trust, control, and delegation regret when using a general-purpose AI agent* [Preprint]. arXiv. https://arxiv.org/abs/2607.18257

Shlomov, S., Shoham, I., Oved, A., & Ship, H. (2026). Governance by construction for generalist agents. *Proceedings of the ACM Conference on AI and Agentic Systems*. https://doi.org/10.1145/3786335.3813192

Su, W., Rao, H., & Ma, E. (2026). Privacy and data-integrity risk cards for LLM agents: A UI/UX design framework for tool-approval oversight under prompt injection attacks. *International Journal of Graphic Design, 4*(1), 186–191. https://doi.org/10.51903/ijgd.v4i1.3699

Wang, Y., & Wang, G. (2026). User autonomy in human-LLM interaction: A scoping review. *Proceedings of the Extended Abstracts of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772363.3798855

Weng, X. (2026). *What you approve is what executes: Consent integrity for black-box LLM agents* [Preprint]. arXiv. https://arxiv.org/abs/2606.02668

Xie, L., Zheng, C., Xia, H., Qu, H., & Zhu-Tian, C. (2024). WaitGPT: Monitoring and steering conversational LLM agent in data analysis with on-the-fly code visualization. *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*. https://doi.org/10.1145/3654777.3676374

Yan, T. (2026). *Do user-authored permission policies improve protection against AI agent overreach?* [Preprint]. arXiv. https://arxiv.org/abs/2608.27443

Zhang, S., Chen, J., Gao, Z., Gao, J., Yi, X., & Li, H. (2026). Characterizing unintended consequences of GUI agents for web browsing. *Proceedings of the 2026 CHI Conference on Human Factors in Computing Systems*. https://doi.org/10.1145/3772318.3790696

Zhou, J., Roy, A., Gupta, S., Weitekamp, D., & MacLellan, C. J. (2025). *When should users check? Modeling confirmation frequency in multi-step agentic AI tasks* [Preprint]. arXiv. https://arxiv.org/abs/2510.05307

Zhuang, H., Xing, H., & Zhang, X. (2026). *AgentClick: A skill-based human-in-the-loop review layer for terminal AI agents* [Preprint]. arXiv. https://arxiv.org/abs/2604.16520
