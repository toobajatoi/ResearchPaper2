# Codebook v0: Human–AI interaction cost

**Version.** 0, pre-pilot. Do not treat these rules as validated.

**Status.** Candidate codes for the pilot of 40 conversations. Revise only after human pilot coding, using `analysis/pilot_diagnostics.py` and the procedure in `methods/pilot-procedure.md`. Do not assign these codes with a generative model.

**Unit of coding.** One row per user message. Do not split a message into sentences. A message may receive more than one code.

**What is being measured.** Human–AI interaction cost is the observable work a user does after the first request, while still pursuing that request. Column names below match `analysis/codes.py`. Enter `1` or `0` in every code column. Leave nothing blank once a turn has been coded. A blank means “not yet coded,” not “absent.”

Constructed illustrations appear in quotation marks. They are training examples, not quotations from WildChat.

## Materials for each conversation

Read the packet in order. The packet shows user and assistant messages only. It does not include IP address, country, state, or request headers. Ignore those if they appear anywhere else.

Code two files:

- `conversations.csv`, one row per conversation: `screen`, `task_type`, `ending_state`, `ending_notes`.
- `turns.csv`, one row per user message: the binary columns listed below.

Code the conversation row before the turn rows. If `screen` is `non_task` or `uninterpretable`, set `task_type` accordingly, set `ending_state` to `indeterminate`, write a short note, and set every turn-level code to `0`. Do not force a task reading onto chit-chat.

## Screen (conversation)

| Value | Include when | Exclude when |
| --- | --- | --- |
| `task_oriented` | The user asks the assistant to produce, change, explain, decide, plan, or otherwise accomplish something that could be done well or badly. | The exchange has no identifiable task. |
| `non_task` | Greeting only, bot testing (“say hello”), chit-chat with no task, role-play that never asks for an output, or a jailbreak or policy probe as the point of the conversation. | A jailbreak wrapper around a real task. Code the task, and mention the wrapper in `ending_notes`. |
| `uninterpretable` | Empty residue, redaction placeholders that remove the goal, or a language mix in which the coder cannot tell what was asked. | A difficult but still readable request. Those stay `task_oriented`. |

## Task type (conversation)

Assign one task type from the **initial user message**. Use a later user message only when the first message is too thin to classify (“help me with this”) and a later message states the same goal.

If the user later starts a second task, keep the task type of the **initial** goal.

| Value | Include when the initial goal is to… | Exclude (use the other code instead) |
| --- | --- | --- |
| `writing` | Produce or revise nonfiction prose that is itself the deliverable: email, essay, summary, post, translation, resume, recommendation. | Fiction, poetry, song, script, or game narrative (`creative_production`). Code (`coding`). |
| `creative_production` | Produce fiction, poetry, lyrics, a script, a character, a game scene, or an image or video prompt whose point is the creative artifact. | A professional email or essay (`writing`). |
| `coding` | Write, debug, explain, convert, or review code, or configure a program. | A prose explanation of a concept with no code requested (`information_seeking`). |
| `information_seeking` | Answer a question, explain a concept, compare options, or retrieve a fact, where the deliverable is an answer rather than a document the user will send. | A finished document (`writing`) or a plan of action (`planning`). |
| `planning` | Make an itinerary, schedule, study plan, strategy, or ordered procedure for the user to carry out. | A one-step factual answer (`information_seeking`). |
| `other_task` | A readable task that fits none of the above, including calculation, data description without code, and shopping choice that is neither a plan nor a fact lookup. | Forcing a near match. Use the nearer specific code when one clearly fits. |
| `non_task` | `screen` is `non_task`. | — |

## Ending state (conversation)

Judge the **initial goal only**. Evidence must be inside the log. Off-platform use is invisible.

The last user message is the usual place to look. An earlier message can settle the initial goal when a later message starts a new one.

| Value | Include when | Exclude when |
| --- | --- | --- |
| `explicit_acceptance` | The user affirms the output for the initial goal (“this works,” “perfect, thanks”) and does not keep repairing it. | Thanks that arrive while the user is still requesting repairs. That pattern is `continued_repair` if the conversation ends in repair. Polite thanks alone, with no sign the goal was met, are not acceptance. |
| `new_goal_after_use` | The user treats the initial output as usable and moves to a different goal (“good, now turn it into a shorter post”). The move shows the first goal is no longer being repaired. | A move that drops the first goal as a failure (“forget it, just write a tweet”). That is `explicit_abandonment` of the initial goal if the user rejects it, or `new_goal_after_use` only when the first output is kept. When unsure, prefer `indeterminate` and explain in `ending_notes`. |
| `continued_repair` | The last move aimed at the initial goal is still a clarification, correction, constraint, restoration, repetition, revision, or verification. | A last message that only accepts or only abandons. |
| `explicit_abandonment` | The user stops the initial goal in words: “never mind,” “this isn’t working,” “stop,” “I’ll do it myself,” or an explicit rejection without a replacement they accept. | Silence. Silence is `indeterminate`. |
| `indeterminate` | The log ends with no signal about the initial goal. This includes every conversation with only one user message. It also includes a trailing “thanks” that does not say the output was acceptable. | Any of the signals above. |

Map used later in analysis, not during coding:

- Apparent resolution = `explicit_acceptance` or `new_goal_after_use`
- Continued repair = `continued_repair`
- Abandonment = `explicit_abandonment`
- Indeterminate = `indeterminate`

Coders record the fine value. They do not collapse it.

## Turn-level rules

1. The first user message is the initial request. Set all cost codes to `0` on that row, except `context_free_repair` when the rule below applies. Also set `social` to `1` if the first message is only a greeting plus a task; still do not put the task itself in a cost code.
2. Cost codes apply only to later user messages, and only for work on the **same** goal as the initial request.
3. A message that starts a different goal is `redirection` (see below). Do not also assign same-goal repair codes for the new goal.
4. Multi-label when two inclusion rules are truly met. Then apply the priority rules, which remove the losing code.
5. Code what the user does, not what you infer the assistant deserved.
6. If a message is only an answer to a question the assistant asked, use `supplies_requested_information`. Add a cost code only when the message also meets that cost code’s inclusion rule.

### Priority when two codes compete

Apply these after the inclusion rules. Remove the code that loses.

| If both seem to fit | Keep | Drop |
| --- | --- | --- |
| The user changes something material | `revision_request` | `repetition` |
| The requirement already appeared in an earlier user message and the assistant missed it | `requirement_restoration` | `constraint_addition` |
| The user claims a factual error or a missed instruction | `correction` | `revision_request` |
| The user asks “are you sure?” without stating the error | `verification` | `correction` |
| The user explains the original meaning because the assistant missed it | `clarification` | `constraint_addition` |
| The user both restores an old requirement and adds a new one | both `requirement_restoration` and `constraint_addition` | neither |
| The message leaves the initial goal | `redirection` | same-goal cost codes |

## Cost codes

These eight columns are the cost profile.

### `clarification`

**Include.** The user explains what they meant because the assistant misunderstood, asked, or answered a different reading. The content was already the user’s meaning.

Illustration: Initial request, “Write a professional email asking for an extension.” Later, “No, I meant an extension on the assignment, not on the rental.”

**Exclude.** A limit that was not part of the original meaning (`constraint_addition`). A claim that a date or fact in the answer is wrong (`correction`). A restatement that adds nothing and changes nothing (`repetition`).

### `correction`

**Include.** The user states that the assistant’s output is factually wrong, internally inconsistent, or fails an instruction the user already gave.

Illustrations: “The treaty was signed in 1919, not 1918.” “You used Python 2 syntax.” “I asked for five items and you wrote four.”

**Exclude.** A preference about tone or length with no correctness claim (`revision_request` or `constraint_addition`). A question that only seeks reassurance (`verification`).

### `constraint_addition`

**Include.** The user adds a limit or condition that was **not** in the initial request or in any earlier user message.

Illustrations: “Keep it under 100 words.” “Don’t mention the personal circumstances.” “Use bullet points.”

**Exclude.** The same limit already stated earlier and missed by the assistant (`requirement_restoration`). A claim that the assistant got a fact wrong (`correction`).

### `requirement_restoration`

**Include.** The user repeats a requirement that already appeared in the initial request or in an earlier user message, because the assistant dropped it or violated it.

Illustrations: “You forgot that I said no personal information.” “I still need it under 100 words.” “Keep the first paragraph from your previous answer, as I asked.”

**Exclude.** The first time that requirement appears (`constraint_addition`, or part of the initial request, which is not cost). A new stylistic request that does not point back (`revision_request`).

### `repetition`

**Include.** The user asks again for essentially the same thing, without a material correction, new constraint, restoration, or revision. Near-duplicates and “try again” with no new instruction qualify.

Illustrations: The user pastes the same request a second time. “Write the email again.” “Same thing, regenerate.”

**Exclude.** Any material change in instruction. That is `revision_request`, `constraint_addition`, `requirement_restoration`, or `correction`, and `repetition` is dropped.

### `revision_request`

**Include.** The user asks for another attempt and specifies a change in tone, emphasis, structure, selection, or wording that is not a factual correction and not the restoration of an earlier requirement.

Illustrations: “Try again but less formal.” “This is still too apologetic.” “Make the opening warmer.”

**Exclude.** “Make it shorter” when no length limit was stated before: that is `constraint_addition`. “Make it shorter” when the user already set a length and the assistant missed it: `requirement_restoration`. A bare “try again”: `repetition`.

PATH-style labels such as “change style,” “add content,” and “remove content” (Mysore et al., 2025) are not codes here. Use them only as a reminder to decide among `revision_request`, `constraint_addition`, and `requirement_restoration`.

### `verification`

**Include.** The user asks the assistant to confirm correctness, sources, or uncertainty, without yet stating that an error exists.

Illustrations: “Are you sure this is correct?” “What is the source for that date?” “How confident are you?”

**Exclude.** The user states the error (`correction`). The user asks for a new section (`revision_request` or `constraint_addition`).

### `redirection`

**Include.** The user leaves the initial goal and sets a different task. This is work of steering, and it is also evidence for the ending state of the initial goal. Code the ending state separately on the conversation row.

Illustrations: “Forget the email. Write a tweet instead.” “New question: what is the capital of Portugal?”

**Exclude.** A change that still serves the initial goal (“now make the email shorter”). That stays a same-goal cost code. Do not mark it as redirection.

## Other turn columns (not in the cost profile)

### `acceptance_signal`

**Include.** This message affirms the output or clearly uses it as done.

**Exclude.** Thanks with no judgment. Continued repair in the same message: do not mark acceptance.

### `abandonment_signal`

**Include.** This message quits the initial goal in words.

**Exclude.** Silence, and redirection that keeps the first output (`new_goal_after_use` has `redirection` and does not require `abandonment_signal`).

### `supplies_requested_information`

**Include.** The assistant asked for a missing detail and the user provides it.

Illustration: Assistant, “What course is this for?” User, “History 201.”

**Exclude.** Coding this as `clarification` unless the user also corrects a misunderstanding. Supplying a requested detail is coordination. It becomes cost only when a cost-code rule is also met.

### `social`

**Include.** Greeting, thanks, apology, or other phatic text. If the same message also contains a task or a repair, mark `social` and the other codes that apply.

**Exclude.** Using thanks as a substitute for a cost code.

### `context_free_repair`

**Include.** Only on the **first** user message, and only when that message rejects or corrects an output that does not appear in this conversation (“No, I meant a formal email”).

**Exclude.** Ordinary first requests. Later-turn repairs. This flag is **not** part of the cost profile, because the prior model output is unobserved.

### `uninterpretable`

**Include.** This user message cannot be coded (empty, fully redacted, or unreadable). Set other codes on that row to `0`.

**Exclude.** A message that is merely rude or short. Code the function you can see.

## Worked conversations

These are constructed. They show the intended reading of the audit’s examples.

### Conversation A — one request, then stop

1. User: “Write a professional email asking for an extension.”
2. Assistant: a complete email.
3. End of log.

Conversation: `screen=task_oriented`, `task_type=writing`, `ending_state=indeterminate`.

Turn 0: all codes `0`. There is no later user turn. Do not code acceptance.

### Conversation B — several interventions, then a new use

1. User: “Write a professional email asking for an extension.”
2. Assistant: a very formal email that mentions a family emergency.
3. User: “No, make it less formal.”
4. Assistant: a revised email that still mentions the emergency.
5. User: “Don’t mention the personal circumstances.”
6. Assistant: a revised email.
7. User: “Keep the first paragraph from your previous answer.”
8. Assistant: a revised email that drops that paragraph.
9. User: “This is still too apologetic.”
10. Assistant: a revised email.
11. User: “Good. Now make a two-line version I can text.”

Conversation: `task_type=writing`, `ending_state=new_goal_after_use`.

| User turn | Codes |
| --- | --- |
| 0 initial | all `0` |
| “less formal” | `revision_request=1` (new tone; formality was not specified before) |
| “Don’t mention the personal circumstances.” | `constraint_addition=1` |
| “Keep the first paragraph…” | `requirement_restoration=1` only if an earlier user message asked to keep it. In this script, nothing earlier asked for that, so the first statement of “keep the first paragraph” is `constraint_addition=1`. If the assistant then drops it and the user says “I told you to keep the first paragraph,” that later message is `requirement_restoration=1`. |
| “still too apologetic” | `revision_request=1` |
| “Good. Now make a two-line version…” | `acceptance_signal=1`, `redirection=1`. No same-goal repair code. |

Pre-terminal cost, as the analysis script computes it, uses user turns after the first and before this last message.

### Conversation C — explicit quit

1. User: “Draft a study plan for my statistics exam on Friday.”
2. Assistant: a plan for a biology exam.
3. User: “I said statistics.”
4. Assistant: still biology.
5. User: “Never mind, I’ll do it myself.”

Conversation: `task_type=planning`, `ending_state=explicit_abandonment`.

Turn “I said statistics.” is `clarification=1` (restoring the original meaning the assistant missed). If the coder instead hears a correctness claim about the subject of the plan, `correction` may also seem to fit. Priority: the user is repairing the assistant’s reading of the request, so keep `clarification` and drop `correction` unless the user also flags a false fact inside an otherwise on-topic plan.

Turn “Never mind…” is `abandonment_signal=1`. It is the terminal signal, so the analysis excludes it from the pre-terminal cost predictors.

## What coders do not decide

- Whether the assistant’s answer was actually good.
- Whether the user was skilled.
- Country, model, or identity. The packet omits location and network fields on purpose.
- A numeric interaction-cost score. Enter codes only.

## Pilot instruction

Code all 40 pilot packets independently if you are the primary coder. Do not discuss individual items with the second coder until the reliability set for the **main** sample is submitted. The pilot may be discussed after both people have coded it, because the pilot exists to revise this codebook. Record every proposed rule change in `methods/codebook-changelog.md` with the sample id that motivated it. Do not edit this file in place after coding starts. Copy it to `methods/codebook-v1.md` when the revision is agreed.
