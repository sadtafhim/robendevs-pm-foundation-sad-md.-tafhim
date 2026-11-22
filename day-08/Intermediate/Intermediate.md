
# Blocker Triage, Scope Changes, and Sprint Metrics

These practices help Agile teams resolve blockers, manage changing requirements, and measure sprint performance. They help teams maintain clear priorities and realistic delivery expectations.

## 1. Blocker Triage

### What Is Blocker Triage?

Blocker triage is the process of identifying issues that prevent work from progressing, determining their causes, and assigning them to the right person for resolution.

Blockers generally require one of three types of decisions: client, design, or engineering.

### Types of Blockers

**1. Client Blockers**

Issues caused by missing business information, clarification, or approval.

Common examples:
- Unclear business requirements.
- Missing business rules.
- Delayed client approval.
- Changes to agreed requirements.

**Responsible person:** Client, Product Owner, or Business Analyst.

**2. Design Blockers**

Issues caused by missing or unclear design information.

Common examples:
- Missing UI designs or assets.
- Unclear user interactions.
- Missing responsive layouts.
- Undefined loading, empty, or error states.

**Responsible person:** UI/UX Designer or Design Lead.

**3. Engineering Blockers**

Technical issues preventing developers from completing their work.

Common examples:
- API integration failures.
- Database or server issues.
- Technical dependencies.
- Implementation difficulties.
- Bugs affecting other features.

**Responsible person:** Developer, Technical Lead, or Engineering Team.

### How to Perform Blocker Triage

1. **Identify the blocker:** Understand what is preventing progress.
2. **Determine the cause:** Identify whether it is related to requirements, design, engineering, or dependencies.
3. **Assign responsibility:** Identify who can resolve the issue.
4. **Assess priority:** Determine its urgency and impact on delivery.
5. **Track resolution:** Document the blocker and follow up until it is resolved.

### Prioritizing Blockers

| Priority | Meaning |
|---|---|
| Critical | Prevents important work or threatens the sprint goal. |
| High | Delays multiple tasks or creates major dependencies. |
| Medium | Affects one task without stopping other work. |
| Low | Causes minor inconvenience without significant impact. |

### Example of Blocker Triage

| Problem | Category | Responsible Person |
|---|---|---|
| Unclear payment requirements | Client | Client / Business Analyst |
| Missing checkout design | Design | UI/UX Designer |
| Payment API errors | Engineering | Backend Developer |
| Undefined mobile navigation | Design | UI/UX Designer |
| Missing refund rules | Client | Client / Business Analyst |

### Why Is Blocker Triage Important?

- Ensures issues reach the right decision-maker.
- Prevents unnecessary development delays.
- Helps prioritize urgent problems.
- Improves communication between teams.
- Keeps development work moving.

## 2. Scope Changes Mid-Sprint

### What Is a Scope Change?

A scope change occurs when a new requirement is introduced or an existing requirement is modified after the sprint or project scope has been agreed upon.

Common reasons include:
- New client requests.
- Changes in business requirements.
- Missing functionality discovered during development.
- Changes to approved designs.
- Newly identified technical requirements.

### Why Are Mid-Sprint Changes Difficult?

Introducing additional work during a sprint can affect:

- **Team capacity:** Additional work may exceed available resources.
- **Priorities:** Existing tasks may need to be delayed.
- **Dependencies:** New requirements may affect other features.
- **Timelines:** Planned delivery may be delayed.
- **Team focus:** Frequent changes can interrupt ongoing work.

Every change should be evaluated before being accepted.

### Three Ways to Handle Scope Changes

**1. Accept the Change**

Accept a change when it is necessary, manageable, and does not endanger the sprint goal.

Examples:
- Correcting a minor requirement misunderstanding.
- Fixing a small issue related to current work.
- Making a necessary adjustment with minimal additional effort.

If new work is introduced, the team may need to renegotiate existing sprint work with the Product Owner.

**2. Defer the Change**

Defer a change when it is useful but not necessary for the current sprint.

Examples:
- Adding optional functionality.
- Improving an existing interface.
- Introducing additional features that can wait.

Document the request in the product backlog and prioritize it for a future sprint.

**3. Raise a Change Request**

A formal change request is appropriate when a change significantly affects the agreed project scope, budget, timeline, resources, or contractual commitments.

Examples:
- Adding a completely new module.
- Changing the main business workflow.
- Introducing a new third-party integration.
- Replacing an approved feature with a different solution.

A change request should include:

- Description and reason for the change.
- Expected benefits.
- Additional development effort.
- Impact on project timelines.
- Cost and resource implications.
- Approval or rejection decision.

### How to Evaluate a Scope Change

| Evaluation Area | Question |
|---|---|
| Business Value | Is the change necessary or beneficial? |
| Urgency | Does it need to happen immediately? |
| Effort | How much additional work is required? |
| Dependencies | Will it affect other tasks or features? |
| Sprint Goal | Will it interfere with the sprint objective? |
| Timeline | Will it delay planned delivery? |
| Cost | Will additional resources or budget be required? |

### Scope Change Decision Process

1. **Receive the request:** Understand the requested change.
2. **Evaluate the impact:** Assess effort, urgency, dependencies, cost, and timeline.
3. **Make a decision:**
   - **Accept:** Necessary and manageable within the sprint.
   - **Defer:** Useful but can wait for a future sprint.
   - **Change Request:** Significantly affects the agreed project scope.
4. **Document the decision:** Update Jira, the backlog, sprint scope, or project documentation.

### Protecting the Sprint Goal

The sprint goal should remain stable throughout the sprint.

In Scrum, scope can be clarified and renegotiated between the Developers and Product Owner as more information becomes available. However, changes should not endanger the sprint goal.

If the sprint goal becomes obsolete, the Product Owner can cancel the sprint. This should be an exceptional situation.

### Why Is Scope Management Important?

- Prevents uncontrolled additions to sprint work.
- Maintains clear development priorities.
- Keeps delivery expectations realistic.
- Reduces unnecessary interruptions.
- Ensures significant changes are evaluated and approved.
- Maintains alignment between clients and development teams.

## 3. Sprint Metrics

### What Are Sprint Metrics?

Sprint metrics are measurements used to understand team performance, monitor development progress, and improve future sprint planning.

Three commonly used sprint metrics are:

1. Burndown charts.
2. Velocity.
3. Carry-over work.

### A. Burndown Charts

#### What Is a Burndown Chart?

A burndown chart visually tracks how much work remains in a sprint over time.

It compares:
- **Remaining work:** Work that has not been completed.
- **Time:** Days remaining in the sprint.
- **Ideal progress:** Expected rate of work completion.

#### How Does It Work?

Suppose a team starts a sprint with 40 story points of planned work.

| Sprint Day | Remaining Work |
|---|---|
| Day 1 | 40 points |
| Day 3 | 34 points |
| Day 5 | 27 points |
| Day 7 | 18 points |
| Day 9 | 8 points |
| Day 10 | 0 points |

As tasks are completed, the remaining work should decrease.

#### How to Interpret a Burndown Chart

- **Actual progress follows the ideal line:** Work is progressing as expected.
- **Actual progress is above the ideal line:** More work remains than expected, indicating possible delays.
- **Actual progress is below the ideal line:** Work is being completed faster than expected.
- **The chart remains flat:** Little or no work is being completed.

#### Why Are Burndown Charts Useful?

- Track remaining sprint work.
- Identify delays early.
- Monitor progress against the sprint timeline.
- Highlight periods with little progress.
- Support discussions about blockers and priorities.

A burndown chart shows progress but does not explain why delays occur. The team must investigate the underlying causes.

### B. Velocity

#### What Is Velocity?

Velocity measures how many story points a team completes during a sprint.

It helps estimate the team's historical delivery capacity and plan future sprints.

#### Calculating Average Velocity

Suppose a team completes the following story points:

| Sprint | Completed Story Points |
|---|---|
| Sprint 1 | 24 |
| Sprint 2 | 28 |
| Sprint 3 | 26 |
| Sprint 4 | 30 |

Average velocity:

`(24 + 28 + 26 + 30) / 4 = 27 story points`

The team's average velocity is 27 story points per sprint.

#### How Is Velocity Used in Sprint Planning?

Suppose the team has an average velocity of 27 points and the backlog contains:

- Feature A: 8 points.
- Feature B: 5 points.
- Feature C: 8 points.
- Feature D: 5 points.
- Feature E: 8 points.

Total: 34 points.

Since the team's average velocity is 27, selecting all five features may be unrealistic.

The team could select Features A, B, C, and D, totaling 26 points, and leave Feature E for a future sprint.

Velocity is a planning reference, not a guaranteed delivery target. Team availability, complexity, and dependencies must also be considered.

#### Why Is Velocity Useful?

- Estimates future sprint capacity.
- Supports release planning.
- Helps forecast delivery timelines.
- Identifies changes in delivery patterns.
- Improves sprint planning decisions.

**Important:** Velocity should not be used to compare different teams or evaluate individual developers. Story points are relative estimates, and teams may estimate work differently.

### C. Carry-Over Work

#### What Is Carry-Over?

Carry-over refers to work planned for a sprint but not completed before the sprint ends.

Unfinished work is returned to the product backlog and reconsidered during future sprint planning.

#### Why Does Carry-Over Happen?

Common reasons include:
- Tasks were underestimated.
- Requirements were unclear.
- Technical issues caused delays.
- External dependencies were not resolved.
- Priorities changed during the sprint.
- Team members became unavailable.
- Unexpected complexity was discovered.

#### How to Handle Carry-Over Work

1. **Identify unfinished tasks:** Review issues that have not reached the Definition of Done.
2. **Understand the cause:** Determine why the work was not completed.
3. **Reassess remaining work:** Check whether the original estimate is still accurate.
4. **Return work to the product backlog:** Reassess and prioritize unfinished tasks.
5. **Plan future work:** Decide whether to include the tasks in the next sprint based on priority and available capacity.

#### Why Is Carry-Over Important?

Tracking carry-over helps identify recurring planning and delivery problems.

For example, consistently carrying over tasks may indicate poor estimation, unclear requirements, or unresolved dependencies.

Understanding these patterns helps improve future sprint planning.

### Comparing the Three Sprint Metrics

| Metric | What It Measures | Main Purpose |
|---|---|---|
| Burndown | Remaining work over time | Monitor sprint progress |
| Velocity | Completed story points per sprint | Forecast future capacity |
| Carry-over | Unfinished sprint work | Identify planning and delivery problems |

### Using Sprint Metrics Together

Each metric provides a different view of sprint performance:

- **Burndown:** Shows how work progresses during a sprint.
- **Velocity:** Shows how much work the team typically completes.
- **Carry-over:** Shows what remains unfinished.

For example, if a team consistently plans 35 story points but completes only 25, its metrics may reveal:

- Burndown shows slower-than-expected progress.
- Velocity indicates an average capacity of 25 points.
- Carry-over shows approximately 10 unfinished points.

This suggests the team may be overcommitting during sprint planning.

The team can use this information to plan more realistically based on historical performance, available capacity, and dependencies.
