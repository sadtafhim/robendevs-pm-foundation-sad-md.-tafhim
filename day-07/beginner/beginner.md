# Agile Basics, Jira Hierarchy, Ticket Writing, and Definition of Ready and Done

## 1. Agile Basics: Scrum vs Kanban, Sprints, and Ceremonies

### What Is Agile?

Agile is a software development approach where work is completed in smaller parts rather than building the entire product at once.

Teams develop, test, review, and improve the product in stages. This allows them to collect feedback, adapt to changing requirements, and deliver improvements regularly.

### Key Principles of Agile

- **Iterative Development:** Work is completed in smaller cycles, with each cycle producing improvements.
- **Continuous Feedback:** Teams regularly collect feedback from clients, stakeholders, and users.
- **Flexibility:** Requirements can change as the project progresses.
- **Collaboration:** Developers, designers, testers, and stakeholders communicate regularly.
- **Continuous Improvement:** Teams review their processes and identify ways to work more effectively.

### Scrum vs Kanban

Scrum and Kanban are two approaches used to organise and manage Agile work. Both help teams track progress, but they handle work differently.

#### Scrum

Scrum is an Agile framework where work is divided into fixed periods called **Sprints**.

A Sprint is a development cycle that usually lasts between one and four weeks. During this period, the team works toward a specific goal using a selected group of tasks.

**Main characteristics:**

- Work is organised into fixed-length Sprints.
- Tasks are selected before each Sprint begins.
- Each Sprint has a specific goal.
- Progress is reviewed regularly.
- Teams follow defined Scrum events.
- Completed work is reviewed at the end of each Sprint.

#### Kanban

Kanban is an Agile approach that focuses on visualising work and managing its continuous flow.

Unlike Scrum, Kanban does not require fixed-length Sprints. Team members take new tasks when they have the capacity to work on them.

Work is usually displayed on a Kanban board with columns such as:

- **To Do:** Tasks that have not started.
- **In Progress:** Tasks currently being worked on.
- **Review:** Tasks waiting for review or testing.
- **Done:** Completed tasks.

**Main characteristics:**

- Work moves continuously rather than in fixed Sprints.
- Tasks are prioritised based on importance.
- Team members take new tasks when capacity is available.
- Work-in-progress limits prevent too many tasks from being handled simultaneously.
- The team focuses on improving workflow and reducing delays.

### Scrum vs Kanban: Key Differences

| Area | Scrum | Kanban |
|---|---|---|
| Work structure | Fixed-length Sprints | Continuous workflow |
| Planning | At the beginning of each Sprint | Continuous |
| Task selection | Selected for each Sprint | Taken when capacity is available |
| Changes | Generally controlled during a Sprint | Can be introduced continuously |
| Meetings | Defined Scrum events | No mandatory set of meetings |
| Main focus | Achieving Sprint goals | Maintaining smooth workflow |
| Work limits | Sprint capacity | Work-in-progress limits |

Neither approach is universally better. Scrum is useful when teams need structured planning and regular delivery cycles. Kanban is useful when work arrives continuously and priorities change frequently.

### What Are Sprints?

A Sprint is a fixed period during which a Scrum team works toward a specific goal.

Sprints usually last between one and four weeks.

Each Sprint follows a repeating cycle:

1. **Sprint Planning:** The team decides what work to complete.
2. **Development:** Developers work on the selected tasks.
3. **Daily Scrum:** The team coordinates progress and identifies obstacles.
4. **Sprint Review:** Completed work is demonstrated and feedback is collected.
5. **Sprint Retrospective:** The team reviews its process and identifies improvements.

Each Sprint should produce a usable product increment that meets the team's Definition of Done.

### Scrum Ceremonies (Scrum Events)

Scrum events are structured activities that help teams plan work, communicate progress, review results, and improve their processes.

#### 1. Sprint Planning

Sprint Planning takes place at the beginning of a Sprint.

The team decides what work should be completed and how it will contribute to the Sprint goal.

**Main purposes:**

- Establish the Sprint goal.
- Select work from the Product Backlog.
- Understand the requirements.
- Assess the team's capacity.
- Plan how the selected work will be completed.

#### 2. Daily Scrum (Daily Stand-up)

The Daily Scrum is a short, usually 15-minute meeting where developers coordinate their work and discuss progress.

Common discussion points include:

- What has been completed?
- What is being worked on next?
- Are there any blockers?

The purpose is to identify problems early and keep the team aligned.

#### 3. Sprint Review

The Sprint Review takes place near the end of a Sprint.

The team demonstrates completed work to stakeholders and collects feedback.

**Main purposes:**

- Demonstrate completed features.
- Collect stakeholder feedback.
- Review progress toward product goals.
- Identify changes to future priorities.

#### 4. Sprint Retrospective

The Sprint Retrospective is an internal team meeting held after the Sprint Review.

The team discusses its working process and identifies improvements for future Sprints.

Common discussion points include:

- What went well?
- What problems occurred?
- What slowed down development?
- What should change in the next Sprint?

The focus is on improving the process rather than blaming individuals.

#### 5. The Sprint

The Sprint is the overall fixed period that contains the other Scrum events.

During this period, the team works toward the Sprint goal and produces a usable product increment.

---

## 2. Jira Hierarchy: Epics, Stories, Tasks, Sub-tasks, and Bugs

### What Is Jira?

Jira is a project management and issue-tracking tool developed by Atlassian.

Software development teams use it to organise tasks, assign responsibilities, track progress, manage bugs, and coordinate development work.

In Jira, individual pieces of work are represented as **issues**.

An issue can contain:

- Title and description.
- Assignee.
- Priority.
- Status.
- Due date.
- Acceptance criteria.
- Attachments.
- Comments.

Jira provides different issue types to organise work based on its size and purpose.

### Understanding the Jira Hierarchy

The Jira hierarchy helps teams break large requirements into smaller, manageable pieces of work.

#### 1. Epic

An Epic is a large body of work that groups multiple related Stories and Tasks under one broader objective.

It represents a significant feature or area of functionality that usually requires several smaller issues to complete.

**Example:**

Epic: User Authentication System

This Epic might contain:

- User registration.
- User login.
- Password reset.
- Email verification.
- Logout functionality.

**Purpose of an Epic:**

- Organise large features.
- Group related work.
- Track progress toward broader objectives.
- Show how smaller tasks contribute to the overall product.

#### 2. Story

A Story, commonly called a User Story, describes a feature or requirement from the perspective of the person who will use it.

A common format is:

"As a [type of user], I want [functionality], so that [benefit]."

**Example:**

"As a registered user, I want to reset my password so that I can regain access to my account if I forget my login credentials."

A Story should explain the user's need and expected functionality rather than dictate every technical implementation detail.

**Purpose of a Story:**

- Explain user needs.
- Describe expected functionality.
- Provide context for developers.
- Establish a basis for acceptance criteria.

#### 3. Task

A Task represents a specific piece of work that needs to be completed.

It does not necessarily describe something directly requested by a user. It can represent technical, operational, or project-related work.

**Example:**

Tasks for an authentication system might include:

- Set up the authentication database.
- Configure the email service.
- Create authentication API endpoints.
- Implement password encryption.

Tasks help teams organise the work required to deliver a feature.

#### 4. Sub-task

A Sub-task is a smaller piece of work created under a parent issue, such as a Story or Task.

It divides larger work into smaller steps that can be assigned and tracked separately.

**Example:**

A Story called "User Registration" might contain:

- Create the registration form.
- Implement input validation.
- Connect the registration API.
- Add email verification.
- Test the registration process.

**Purpose of Sub-tasks:**

- Break complex work into smaller steps.
- Distribute work among team members.
- Track individual progress.
- Clarify responsibilities.

#### 5. Bug

A Bug represents an error, defect, or unexpected behaviour in a software application.

It is created when the application does not work as intended.

**Example:**

A user enters the correct email address and password but receives an "Invalid credentials" error.

A Bug should document the problem so developers can investigate and fix it.

A well-written Bug usually includes:

- **Bug Title:** A short description of the issue.
- **Environment:** Where the issue occurs, such as browser, device, or operating system.
- **Steps to Reproduce:** Instructions for recreating the problem.
- **Expected Result:** What should happen.
- **Actual Result:** What happens instead.
- **Attachments:** Screenshots, recordings, or relevant logs.

### Difference Between Jira Issue Types

| Issue Type | Main Purpose |
|---|---|
| Epic | Groups a large body of related work |
| Story | Describes a user requirement |
| Task | Represents a specific piece of work |
| Sub-task | Breaks a parent issue into smaller steps |
| Bug | Documents a software defect |

**Important:** A Bug is a separate issue type and is not necessarily a child of a Story. In standard Jira configurations, Stories, Tasks, and Bugs can be grouped under Epics, while Sub-tasks belong to standard issues. The exact hierarchy can vary depending on Jira configuration.

---

## 3. Writing Jira Tickets

### What Is a Jira Ticket?

A Jira ticket is a documented unit of work that describes something the development team needs to build, investigate, improve, or fix.

It provides the information necessary to understand:

- What needs to be done.
- Why it is required.
- How the functionality should behave.
- How completion will be evaluated.

A good ticket should be clear, specific, understandable, and actionable.

### 1. Writing Clear Titles

The title is the first thing team members see when looking at a Jira board or issue list.

It should communicate the main purpose of the ticket without requiring someone to open the full description.

A good title should:

- Clearly describe the work.
- Be specific rather than vague.
- Use simple language.
- Focus on one main requirement.
- Avoid unnecessary details.

| Poor Title | Better Title |
|---|---|
| Login issue | Fix login failure with valid credentials |
| Registration | Implement user registration form |
| Payment problem | Fix payment failure during checkout |
| Button issue | Correct submit button alignment on mobile |

### 2. Writing Descriptions

The description explains the requirement in more detail.

It provides the context developers, designers, and testers need to understand the work.

A good description should explain:

- **Background:** Why is this task needed?
- **Requirement:** What needs to be implemented or fixed?
- **Expected Behaviour:** How should the functionality work?
- **Business Rules:** Are there specific conditions or restrictions?
- **Dependencies:** Does the task depend on another feature, service, or task?

**Example: Implement User Registration Form**

Create a registration form that allows new users to create an account using their name, email address, and password.

The form should validate all required fields before submission and check whether the email address is already registered.

After successful registration, the system should send a verification email to the user.

### 3. Writing Acceptance Criteria

Acceptance criteria define the specific conditions that must be satisfied for a ticket to be considered complete.

They establish a shared understanding between stakeholders, developers, and testers about what the feature must achieve.

A commonly used format is **Given / When / Then**:

- **Given:** Describes the initial situation or condition.
- **When:** Describes the action performed.
- **Then:** Describes the expected result.

**Example: User Registration**

**Scenario 1: Successful Registration**

- Given a user enters valid registration information.
- When the user submits the registration form.
- Then the system creates the account and sends a verification email.

**Scenario 2: Invalid Email**

- Given a user enters an invalid email address.
- When the user submits the registration form.
- Then the system displays an appropriate validation message.

**Scenario 3: Existing Email**

- Given an email address is already registered.
- When the user attempts to register using that email.
- Then the system prevents account creation and displays an appropriate message.

**Scenario 4: Missing Required Fields**

- Given the user leaves one or more required fields empty.
- When the user submits the form.
- Then the system displays validation messages for the missing fields.

**What Makes Good Acceptance Criteria?**

- **Clear:** Each condition should be easy to understand.
- **Testable:** A tester should be able to verify whether it passes or fails.
- **Specific:** Avoid vague statements such as "the form should work properly."
- **Complete:** Cover important scenarios, including errors and edge cases.
- **Relevant:** Each criterion should relate directly to the ticket's requirement.

### 4. Adding Attachments

Attachments provide supporting information that may be difficult to explain through text alone.

Common Jira attachments include:

| Attachment | Purpose |
|---|---|
| Screenshots | Show a visual issue or expected interface |
| Design Files | Provide UI layouts and design references |
| Screen Recordings | Demonstrate bugs or user interactions |
| Documents | Provide additional requirements or specifications |
| API Documentation | Explain endpoints, request formats, and responses |
| Error Logs | Help developers investigate technical problems |

Attachments should be relevant, clearly named, and accessible to the people working on the ticket.

### Complete Example of a Jira Ticket

**Issue Type:** Story

**Title:** Implement User Registration Form

**Description**

As a new user, I want to create an account using my name, email address, and password so that I can access the application.

**Requirements**

- Provide name, email, and password fields.
- Validate all required fields.
- Prevent registration with an existing email.
- Send an email verification link after successful registration.

**Acceptance Criteria**

1. Users can register using valid information.
2. Required fields cannot be left empty.
3. Invalid email addresses trigger validation messages.
4. Existing email addresses cannot be registered again.
5. Successful registration triggers a verification email.

**Attachments**

- Registration form design.
- Validation error screenshots.
- Email verification flow reference.

**Priority:** High

**Status:** To Do

---

## 4. Definition of Ready (DoR) and Definition of Done (DoD)

Definition of Ready and Definition of Done establish shared standards for deciding when work can begin and when it can be considered complete.

Although they sound similar, they serve different purposes.

### What Is Definition of Ready (DoR)?

Definition of Ready describes the conditions a Story, Task, or requirement should satisfy before the development team starts working on it.

Its purpose is to ensure the team has enough information and clarity to complete the work without unnecessary confusion.

**Common Definition of Ready criteria:**

#### 1. Clear Requirement

The ticket clearly explains what needs to be developed or fixed.

Developers should understand the purpose of the work without making major assumptions.

#### 2. Acceptance Criteria Are Defined

The ticket includes clear and testable acceptance criteria that explain what the completed functionality must achieve.

#### 3. Required Designs Are Available

If the task involves UI or UX development, the necessary designs, prototypes, and references should be available.

#### 4. Dependencies Are Identified

External services, APIs, integrations, or other tasks required for completion should be identified.

#### 5. Scope Is Understandable

The team understands what is included in the task and what is outside its scope.

#### 6. Estimates Are Available

The team has enough information to estimate the effort required, if estimation is part of its process.

#### 7. No Major Unresolved Questions

Important questions about functionality, business rules, or expected behaviour should be answered before development begins.

**Example:**

A Story titled "Implement Payment Gateway" should not be considered ready if the payment provider has not been selected, API documentation is unavailable, and the expected payment flow is unclear.

The team needs these details before development can begin effectively.

### What Is Definition of Done (DoD)?

Definition of Done describes the conditions that must be satisfied before a task or feature can be considered complete.

It establishes a shared quality standard and ensures completed work meets the team's expectations.

Finishing the coding alone is not enough. The implementation may still require testing, code review, documentation, or other quality checks.

**Common Definition of Done criteria:**

#### 1. Development Is Completed

The required functionality has been implemented according to the ticket's requirements.

#### 2. Acceptance Criteria Are Satisfied

All defined acceptance criteria have been met and the feature behaves as expected.

#### 3. Testing Is Completed

The functionality has been tested for errors, unexpected behaviour, and relevant edge cases.

#### 4. Code Review Is Completed

The code has been reviewed according to the team's process, and required changes have been addressed.

#### 5. No Critical Bugs Remain

There are no unresolved critical defects preventing the implementation from meeting the agreed quality standard.

#### 6. Documentation Is Updated

Relevant technical or user documentation has been updated where necessary.

#### 7. Changes Are Integrated

The code has been merged into the appropriate branch and integrated into the required environment according to the team's workflow.

**Example:**

A developer completes the user registration feature.

Before the Story can be marked Done:

- The registration form works correctly.
- All acceptance criteria pass.
- Input validation works.
- Email verification functions correctly.
- Required tests pass.
- Code review is completed.

Only after satisfying the agreed Definition of Done can the Story be considered complete.

### Definition of Ready vs Definition of Done

| Area | Definition of Ready | Definition of Done |
|---|---|---|
| Purpose | Determines whether work can begin | Determines whether work is complete |
| Timing | Before development | After implementation |
| Main Focus | Clarity and preparation | Quality and completion |
| Requirements | Clearly documented | Successfully implemented |
| Acceptance Criteria | Defined and understood | Satisfied and verified |
| Dependencies | Identified | Required dependencies integrated |
| Testing | Test expectations understood | Required testing completed |
| Result | Ready to Start | Completed |

### How DoR and DoD Work Together

1. **Requirement Created:** A new Story or Task is added to Jira.
2. **Definition of Ready:** Requirements are clear, acceptance criteria are defined, and dependencies are understood.
3. **Development Begins:** Developers implement the required functionality.
4. **Testing and Review:** The implementation is tested and reviewed.
5. **Definition of Done:** All agreed completion and quality requirements are satisfied.
6. **Work Completed:** The task or feature is considered Done.
