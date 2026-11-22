
# RAID Logs, Project Recovery, Jira Automation, and Dashboards

These practices help Project Managers identify potential problems, manage project delays, track dependencies, and maintain visibility throughout development.

## 1. RAID Log

### What Is a RAID Log?

A RAID log is a project management document used to identify, record, and track four important areas:

- **R – Risks:** Potential problems that could affect the project.
- **A – Assumptions:** Things the team believes to be true but has not confirmed.
- **I – Issues:** Problems that have already occurred and require resolution.
- **D – Dependencies:** Tasks or activities that rely on something else being completed first.

The purpose of a RAID log is to keep project concerns organized, assign responsibility, and ensure problems are addressed before they affect delivery.

### A. Risks

**What Is a Risk?**

A risk is an uncertain event that could negatively affect the project in the future.

Unlike an issue, a risk has not necessarily happened yet.

**Common Project Risks:**

- **Technical:** API failures, integration problems, or performance issues.
- **Resource:** Developers or designers becoming unavailable.
- **Timeline:** Tasks taking longer than estimated.
- **Client-related:** Delayed feedback or approvals.
- **Requirements:** Incomplete or misunderstood requirements.
- **External:** Third-party service downtime or compatibility issues.

**How to Record a Risk**

| Field | Description |
|---|---|
| Risk ID | Unique reference number. |
| Description | What might happen? |
| Probability | How likely is it to happen? |
| Impact | How seriously could it affect the project? |
| Priority | Overall importance of the risk. |
| Mitigation Plan | How can the risk be reduced? |
| Owner | Who is responsible for monitoring it? |
| Status | Open, Monitoring, Mitigated, or Closed. |

**Risk Probability and Impact**

Probability measures how likely a risk is to occur, while impact measures how seriously it could affect the project.

A simple scoring method is:

`Risk Score = Probability × Impact`

For example, if both are rated from 1 to 5:

`4 × 5 = 20`

The risk score is 20 out of 25, indicating a high-priority risk.

| Score | Priority |
|---|---|
| 1–5 | Low |
| 6–12 | Medium |
| 13–25 | High |

These ranges are examples and can be adjusted to suit the project.

**Risk Mitigation vs. Contingency**

- **Risk:** What might go wrong?
- **Mitigation:** What can be done to reduce its likelihood or impact?
- **Contingency:** What will the team do if it actually happens?

Example:

- Risk: Payment gateway downtime.
- Mitigation: Test the integration and monitor provider availability.
- Contingency: Temporarily disable payment processing and communicate the issue while the provider resolves it.

### B. Assumptions

**What Is an Assumption?**

An assumption is something the team believes to be true when planning or executing a project but has not fully confirmed.

Incorrect assumptions can lead to unexpected work and delays.

**Common Project Assumptions:**

- The client will provide content on time.
- Designs will be approved before development.
- Third-party APIs will support required functionality.
- Existing databases can support new features.
- Required team members will remain available.
- The client will provide necessary system access.

**How to Record an Assumption**

| Field | Description |
|---|---|
| Assumption ID | Unique reference number. |
| Description | What is being assumed? |
| Reason | Why is the team making this assumption? |
| Validation Method | How will it be confirmed? |
| Owner | Who is responsible for checking it? |
| Deadline | When should it be confirmed? |
| Status | Unverified, Confirmed, or Invalidated. |

**Why Should Assumptions Be Tracked?**

Assumptions should be verified because treating unconfirmed information as fact can affect project planning.

Example:

- **Assumption:** The client will provide product images before development.
- **Validation:** The Business Analyst confirms the delivery date with the client.
- **If confirmed:** Development proceeds as planned.
- **If invalidated:** The team discusses alternatives or adjusts the timeline.

An invalid assumption may create a new risk or an active issue.

### C. Issues

**What Is an Issue?**

An issue is a problem that has already occurred and is currently affecting the project.

Unlike a risk, an issue requires action because the problem already exists.

**Common Project Issues:**

- Developers cannot access required systems.
- API integration is failing.
- A client rejects an important design.
- A feature fails its acceptance criteria.
- A task misses its deadline.
- Testing identifies critical bugs.

**How to Record an Issue**

| Field | Description |
|---|---|
| Issue ID | Unique reference number. |
| Description | What has happened? |
| Impact | How is the project affected? |
| Priority | How urgently must it be resolved? |
| Action Plan | What needs to happen to resolve it? |
| Owner | Who is responsible for resolving it? |
| Due Date | When should it be resolved? |
| Status | Open, In Progress, Resolved, or Closed. |

**How to Manage Issues**

1. Identify and document the issue.
2. Understand its cause and impact.
3. Assign a responsible person.
4. Create a resolution plan.
5. Set a deadline.
6. Monitor progress.
7. Confirm that the issue is resolved.

An issue should remain open until the resolution has been verified.

### D. Dependencies

**What Is a Dependency?**

A dependency is a relationship where one task, activity, or deliverable relies on another being completed first.

For example, frontend development may depend on approved designs, while integration testing may depend on completed backend APIs.

**Common Types of Dependencies:**

1. **Task Dependencies:** One task relies on another task being completed.
2. **Team Dependencies:** One team needs another team's output.
3. **Client Dependencies:** Work requires client information or approval.
4. **External Dependencies:** Work relies on a third-party service or provider.

**How to Record a Dependency**

| Field | Description |
|---|---|
| Dependency ID | Unique reference number. |
| Description | What does the task depend on? |
| Dependent Task | Which task is waiting? |
| Dependency Owner | Who must provide the required input? |
| Expected Date | When should it be available? |
| Impact | What happens if it is delayed? |
| Status | Pending, In Progress, or Resolved. |

**Common Dependency Relationships**

| Type | Meaning | Example |
|---|---|---|
| Finish-to-Start (FS) | One task must finish before another starts. | Design approval before development. |
| Start-to-Start (SS) | One task must start before another can start. | Documentation begins when development starts. |
| Finish-to-Finish (FF) | One task must finish before another can finish. | Testing documentation finishes when testing finishes. |
| Start-to-Finish (SF) | One task must start before another can finish. | A replacement support process starts before the old process ends. |

Finish-to-Start is the most common dependency in software development.

### E. Complete RAID Log Example

A RAID log combines all four categories into one centralized document.

| ID | Category | Description | Owner | Priority / Status |
|---|---|---|---|---|
| R01 | Risk | Payment API integration may be delayed. | Tech Lead | High |
| R02 | Risk | Client feedback may arrive late. | PM | Medium |
| A01 | Assumption | Client will provide product images before development. | BA | Unverified |
| A02 | Assumption | Existing database supports the new feature. | Tech Lead | Unverified |
| I01 | Issue | Developer cannot access the staging server. | DevOps | Open |
| I02 | Issue | Checkout page fails validation testing. | Developer | In Progress |
| D01 | Dependency | Frontend requires approved dashboard designs. | Designer | Pending |
| D02 | Dependency | Testing requires completed backend APIs. | Backend Lead | In Progress |

**How to Maintain a RAID Log**

1. **Create the log:** Identify known risks, assumptions, issues, and dependencies during project planning.
2. **Assign owners:** Every entry must have someone responsible for monitoring or resolving it.
3. **Review regularly:** Discuss high-priority risks, unresolved issues, and delayed dependencies during project meetings.
4. **Update statuses:** Record changes as new information becomes available.
5. **Close resolved items:** Document the resolution and update the status.

### Understanding the Difference Between RAID Categories

| Category | Main Question | Example |
|---|---|---|
| Risk | What might go wrong? | API integration might be delayed. |
| Assumption | What are we believing to be true? | Client will provide content on time. |
| Issue | What has already gone wrong? | API integration is currently failing. |
| Dependency | What are we waiting for? | Frontend is waiting for approved designs. |

**How RAID Categories Connect**

These categories can be related:

1. The team assumes the client will provide product images on time.
2. The assumption is not confirmed, creating a risk of development delays.
3. The client misses the delivery deadline, turning the risk into an issue.
4. Frontend development now depends on receiving the missing images.

This is why RAID logs must be updated throughout the project.

## 2. Project Recovery

### What Is Project Recovery?

Project recovery is the process of bringing a delayed or struggling project back under control through revised planning, prioritization, and corrective actions.

### A. Identify the Cause of the Delay

Common causes include:

- Tasks taking longer than estimated.
- Frequent scope changes.
- Unresolved technical blockers.
- Delayed client approvals.
- Poor communication.
- Insufficient resources.
- Unidentified dependencies.

Review Jira boards, project timelines, RAID logs, and team feedback to understand the cause.

### B. Re-Planning the Project

Re-planning means reviewing unfinished work and creating a realistic updated schedule.

1. Identify incomplete tasks.
2. Reassess the remaining effort.
3. Identify blockers and dependencies.
4. Review available team capacity.
5. Reprioritize remaining work.
6. Create an updated timeline.
7. Communicate the revised plan to stakeholders.

### C. Cutting Scope

Scope reduction means removing or postponing lower-priority requirements to focus on essential deliverables.

A common prioritization method is **MoSCoW**:

| Priority | Meaning |
|---|---|
| Must Have | Essential functionality required for the product. |
| Should Have | Important functionality that adds significant value. |
| Could Have | Useful improvements that can be postponed. |
| Won't Have Now | Features excluded from the current release. |

Any reduction in agreed project scope should be discussed and approved through the appropriate process.

### D. Communicating with the Client

When a project is delayed, the Project Manager should communicate:

- Completed work.
- Current delays.
- Reasons for the delays.
- Impact on the delivery timeline.
- Actions being taken.
- Recommended scope adjustments.
- Decisions or approvals required from the client.

Communication should be transparent and based on realistic expectations.

### E. Creating a Recovery Plan

| Area | Recovery Action |
|---|---|
| Timeline | Create a revised delivery schedule. |
| Scope | Prioritize essential features and postpone optional work. |
| Resources | Review team availability and workload. |
| Dependencies | Resolve critical internal and external dependencies. |
| Risks | Update the RAID log and mitigation plans. |
| Communication | Provide regular stakeholder updates. |

Monitor the recovery plan regularly to ensure the corrective actions are working.

## 3. Jira Automation and Dashboards

### A. Jira Automation

**What Is Jira Automation?**

Jira Automation allows repetitive project management activities to happen automatically based on predefined rules.

An automation rule generally has three elements:

- **Trigger:** The event that starts the rule.
- **Condition:** The requirement that must be satisfied.
- **Action:** What Jira should do when the condition is met.

**Examples of Jira Automation**

1. **Automatic Task Assignment:** Assign newly created issues based on predefined rules.
2. **Blocker Notifications:** Notify responsible team members when an issue is marked as blocked.
3. **Overdue Reminders:** Notify assignees when tasks pass their due dates.
4. **Related Issue Updates:** Update related issues when a specific workflow event occurs.
5. **Completion Notifications:** Notify stakeholders when tasks move to Done.

**Example: Overdue Task Reminder**

- **Trigger:** A scheduled rule runs daily.
- **Condition:** Find issues past their due dates that are not Done.
- **Action:** Send a reminder to the assigned team member.

**Why Is Jira Automation Useful?**

- Reduces repetitive administrative work.
- Improves task management consistency.
- Helps identify overdue tasks.
- Keeps relevant people informed.
- Reduces missed updates.
- Improves team coordination.

Automation supports project management but does not replace human decisions about scope, priorities, and delivery.

### B. Jira Dashboards

**What Is a Jira Dashboard?**

A Jira dashboard is a customizable workspace that displays project information through visual components called gadgets.

It provides a centralized view of project progress without requiring managers to review every individual issue.

**Common Jira Dashboard Gadgets**

| Gadget | Purpose |
|---|---|
| Sprint Burndown Chart | Shows remaining sprint work over time. |
| Sprint Health | Provides an overview of sprint progress. |
| Pie Chart | Displays issues grouped by status, priority, or assignee. |
| Created vs. Resolved Chart | Compares newly created and resolved issues. |
| Filter Results | Displays issues matching a saved filter. |
| Assigned to Me | Shows tasks assigned to the current user. |
| Activity Stream | Displays recent Jira activity. |

**What Should a Project Manager Monitor?**

- Total tasks and their statuses.
- Completed and remaining sprint work.
- Overdue tasks.
- High-priority issues.
- Unresolved blockers.
- Work assigned to each team member.
- Sprint progress and delivery trends.

**Why Are Jira Dashboards Important?**

- Provide centralized project visibility.
- Help identify delays and bottlenecks.
- Improve stakeholder communication.
- Simplify project reporting.
- Help monitor team workload.
- Support better planning and decision-making.

### Jira Automation vs. Jira Dashboards

| Area | Jira Automation | Jira Dashboards |
|---|---|---|
| Purpose | Automate repetitive actions. | Display project information. |
| Function | Performs predefined actions. | Visualizes project data. |
| Example | Notify someone about an overdue task. | Display all overdue tasks. |
| Benefit | Saves time and reduces manual work. | Improves project visibility. |

Both features work together: automation helps maintain and communicate project information, while dashboards help teams monitor that information.

## How These Practices Work Together

1. **RAID Log:** Identifies and tracks risks, assumptions, issues, and dependencies before they disrupt delivery.
2. **Project Recovery:** Provides a structured approach to managing delays through revised planning and scope prioritization.
3. **Jira Automation and Dashboards:** Automate repetitive activities and provide visibility into project progress.

Together, these practices help Project Managers identify problems early, manage delivery challenges, and keep projects organized.
