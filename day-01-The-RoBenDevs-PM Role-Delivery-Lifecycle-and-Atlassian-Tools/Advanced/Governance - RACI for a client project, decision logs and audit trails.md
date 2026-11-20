
# Project Governance: RACI Matrix, Decision Logs, and Audit Trails

## 1. What is Project Governance?

Project Governance is a framework of rules, responsibilities, processes, and controls used to manage a project. It defines who makes decisions, who is responsible, and how the project is monitored.

A software project involves requirements, designs, development, testing, deadlines, and client approvals. Without clear responsibilities, tasks can be missed, decisions can be delayed, and misunderstandings can occur.

Project Governance prevents these problems by defining responsibilities, decision-making authority, and documentation processes.

### Main Elements of Project Governance

| Element | Meaning |
|---|---|
| Roles and Responsibilities | Who performs which tasks? |
| Decision Authority | Who approves decisions? |
| Accountability | Who is answerable for the results? |
| Documentation | Where are decisions and changes recorded? |
| Monitoring and Control | How is project progress tracked? |
| Compliance | Are agreed processes followed? |

## 2. RACI Matrix – Defining Roles and Responsibilities

RACI is a framework used to assign responsibilities to team members.

In a software project, people like the Client, Project Manager (PM), Business Analyst (BA), Designer, Technical Lead, Developer, and QA Engineer have different responsibilities.

For example:
- Business Analyst gathers requirements.
- Designer creates UI designs.
- Developer builds features.
- QA Engineer tests the application.
- Project Manager coordinates the team.

The RACI Matrix clarifies everyone's involvement in each activity.

RACI stands for Responsible, Accountable, Consulted, and Informed.

### Understanding the Four RACI Roles

**R – Responsible**

The person who performs the actual work and completes the task.

Example: The Designer creates UI screens, while the Developer writes code.

**In simple words:** Who does the task?

**A – Accountable**

The person who owns the final outcome and ensures the task is completed correctly.

Example: The Technical Lead ensures the development follows technical standards.

Each activity should ideally have only one Accountable person.

**In simple words:** Who is answerable for the result?

**C – Consulted**

People whose knowledge or opinions are needed before making a decision or completing a task.

Example: The Business Analyst consults the Technical Lead before finalizing technical requirements.

Communication is two-way because their feedback is needed.

**In simple words:** Whose input do we need?

**I – Informed**

People who need updates about a task or decision but don't actively participate in it.

Example: The Project Manager informs the Client when a feature is completed.

Communication is usually one-way.

**In simple words:** Who needs to know?

### Example of a RACI Matrix in a Software Project

| Project Activity | Client | PM | BA | Designer | Tech Lead | Developer | QA |
|---|---|---|---|---|---|---|---|
| Gather requirements | C | A | R | I | C | I | C |
| Prepare PRD | C | A | R | C | C | I | C |
| Approve requirements | A | C | R | I | C | I | C |
| Create UI designs | C | I | C | R/A | C | I | C |
| Approve UI designs | A | R | C | C | I | I | I |
| Develop features | I | I | C | C | A | R | I |
| Perform testing | I | I | C | I | C | C | R/A |
| Coordinate release | I | A | C | I | R | R | C |
| Approve business release | A | R | C | I | C | I | C |

### How to Understand This Matrix in Practice

Suppose the team is gathering requirements for an e-commerce website.

- BA is Responsible for collecting and documenting requirements.
- PM is Accountable for coordinating the activity.
- Technical Lead and QA are Consulted for technical and testing input.
- Designer and Developer are Informed about the requirements.

During development:

- Developer is Responsible for writing code.
- Technical Lead is Accountable for technical quality.
- BA and Designer are Consulted when clarification is needed.
- Client and QA are Informed about progress.

The RACI Matrix prevents confusion and helps everyone understand their responsibilities.

## 3. Decision Log – Recording Important Project Decisions

A Decision Log is a document that records important decisions made during a project.

Software projects involve decisions about features, designs, technologies, deadlines, budgets, and requirements.

For example, a Client initially chooses PayPal but later decides to use Stripe. This change affects development, integration, and testing.

If the decision is not documented, team members might continue using the original plan.

A Decision Log records what was decided, when, why, and who approved it.

### What Information Does a Decision Log Contain?

- **Decision ID:** Unique identification number.
- **Date:** When the decision was made.
- **Decision:** What was agreed upon.
- **Reason:** Why the decision was made.
- **Decision Maker:** Who approved the decision.
- **Contributors:** Who provided input.
- **Impact:** How it affects scope, cost, timeline, or quality.
- **Status:** Proposed, Approved, Rejected, or Superseded.
- **Reference:** Link to supporting documents or approvals.

### Typical Decision Log Structure

| Field | Meaning |
|---|---|
| Decision ID | Unique identification number |
| Date | When the decision was made |
| Decision | What was decided |
| Reason | Why it was decided |
| Decision Maker | Who approved it |
| Contributors | Who provided input |
| Impact | Effect on the project |
| Status | Current decision status |
| Reference | Link to supporting records |

### Example of a Decision Log

**DEC-001**

**Status:** Approved

**Decision:** Use Stripe instead of PayPal.

**Date:** 18 November 2026

**Decision Maker:** Client

**Contributors:** PM, Tech Lead, BA

**Reason:** Client preference and available integration options.

**Impact:** Backend integration and QA test cases need updating.

### How Does a Decision Log Work in Practice?

Suppose the Client requests a different payment gateway during a project meeting.

1. PM discusses the request with the BA and Technical Lead.
2. The team reviews its business and technical impact.
3. Client approves Stripe instead of PayPal.
4. PM or BA records the decision in the Decision Log.
5. The team uses this record as the official reference.

If a Developer later asks why Stripe was selected, the PM can check the Decision Log.

A Decision Log prevents misunderstandings and keeps important decisions documented.

## 4. Audit Trail – Tracking Project Activities and Changes

An Audit Trail is a chronological record of actions, activities, and changes made during a project.

While a Decision Log records decisions, an Audit Trail records what actually happened.

For example, when a BA updates the PRD, the Audit Trail can record:
- Who updated the document.
- When it was updated.
- What was changed.
- Which document version was affected.

Similarly, Git records code changes, including who made them and when.

An Audit Trail provides a history of project activities and helps maintain accountability.

### What Information Does an Audit Trail Contain?

- **Event ID:** Unique identification number.
- **Date and Time:** When the activity happened.
- **User:** Who performed the action.
- **Action:** What was done.
- **Previous Value:** Original information.
- **New Value:** Updated information.
- **Reference:** Related task or document.
- **Approval:** Who approved the change, if required.

### Typical Audit Trail Structure

| Field | Explanation |
|---|---|
| Event ID | Unique event identifier |
| Date and Time | When the activity happened |
| User | Who performed the action |
| Action | What was done |
| Previous Value | Original information |
| New Value | Updated information |
| Reference | Related task or document |
| Approval | Who approved the change |

### Example of an Audit Trail

**Activity:** Document Updated

**Date:** 20 November 2026 · 10:15 AM

**User:** Business Analyst

**Action:** Updated the PRD.

**Change:** Added guest checkout requirements.

**Reference:** PRD v1.2

### What Activities Should Have an Audit Trail?

**A. Requirement Changes**

Record every important requirement modification.

Example: When the BA adds a new feature to the PRD, record who made the change, what was added, and when it happened.

This helps the team track how requirements change over time.

**B. Design Changes**

Record important design updates and approvals.

Example: If the Designer changes the checkout page after Client feedback, the team can check who made the change and which version was approved.

**C. Development Changes**

Track code modifications, bug fixes, and new features.

Tools like Git record:
- Who made the changes.
- Which files were modified.
- When the changes were submitted.
- What was included in the commit.

The team can also track which version was deployed to development, staging, or production.

**D. Project Management Changes**

Record changes to project plans and assignments.

Examples:
- Updating deadlines.
- Changing task priorities.
- Reassigning responsibilities.
- Modifying sprint plans.

This helps the team understand how project plans have changed.

**E. Approval Activities**

Record important approvals from authorized people.

Examples:
- Client approves the PRD.
- Client approves UI designs.
- Client authorizes production release.

These records prevent disagreements about whether something was officially approved.

### How Does an Audit Trail Work in Practice?

Suppose the Client requests a guest checkout feature after approving the initial requirements.

1. BA updates the PRD.
2. Document history records the update and version.
3. PM reviews the change and obtains approval.
4. Developer implements the feature and commits the code to Git.
5. QA tests the feature.

Each activity leaves a record in the relevant system.

If a problem occurs later, the team can check who made each change, when it happened, and whether it was approved.

An Audit Trail provides a reliable history of project activities.

## 5. Difference Between RACI, Decision Log, and Audit Trail

These three tools serve different purposes in Project Governance.

- **RACI Matrix:** Defines who is responsible for each activity.
- **Decision Log:** Records important decisions and why they were made.
- **Audit Trail:** Tracks actions, changes, and their history.

### Comparison Table

| Criteria | RACI | Decision Log | Audit Trail |
|---|---|---|---|
| Main Purpose | Define responsibilities | Record decisions | Track activities and changes |
| Main Question | Who does what? | What was decided? | Who did what and when? |
| Focus | Ownership | Decision-making | History and traceability |
| Created | During project planning | Throughout project | Throughout project |
| Updated | When roles change | When decisions occur | When activities occur |
| Common Format | Responsibility matrix | Decision register | Activity history |
| Main Owner | PM | PM / BA | Tool administrators / PM / Process owners |


