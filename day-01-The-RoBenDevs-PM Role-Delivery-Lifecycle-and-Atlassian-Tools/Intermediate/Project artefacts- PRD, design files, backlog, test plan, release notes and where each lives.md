# Project Artefacts: PRD, Design Files, Backlog, Test Plan, Release Notes, and Where Each Lives

## 1. Introduction

### 1.1 What Are Project Artefacts?

A project artefact is any document, file, record, diagram, or deliverable created or maintained during a project's lifecycle.

In simple words, Project artefacts are the evidence and documentation of everything happening in a project.

Artefacts matter because they:

- Create a shared understanding of what is being built.
- Make decisions reviewable, traceable, and auditable.
- Reduce dependency on memory or on individual people.
- Allow work to continue across people, teams, and sprints.
- Give the client and the team a reference point when questions arise.

### 1.2 The Main Project Artefacts

1. **PRD** - Product Requirements Document - Explains what needs to be built and why.
2. **Design Files** - Explain how the product should look and work.
3. **Backlog** - Lists the work that needs to be completed.
4. **Test Plan** - Explains how the software will be tested.
5. **Release Notes** - Explain what has changed in a new software release.

There are other artefacts too, such as meeting minutes, technical documentation, architecture diagrams, user guides, and project status reports.

---

## 2. Project Artefacts at a Glance

This is the master comparison table. It answers, for every artefact: what it is for, who owns it, when it is created, where it lives, and what format it takes.

| Artefact | Purpose | Primary Owner | Created At | Where It Lives | Typical Format |
|---|---|---|---|---|---|
| PRD | Defines what to build and why | Product Manager / Business Analyst | Discovery and requirement analysis | Confluence space, shared drive, or linked Git repository file | Document (page or file) |
| Design Files | Define how the product looks and behaves | UI/UX Designer / Product Designer | After PRD approval, before development | Figma file (or equivalent design tool) | Design file, prototype, link |
| Backlog | Lists all work to be done and its priority | Product Owner | Before sprint planning, maintained continuously | Jira project backlog (also Confluence for team-shared notes) | Jira issues |
| Test Plan | Defines how the software will be tested | QA Lead / Test Manager | Before testing begins | Confluence page, linked from the Jira epic | Document |
| Release Notes | Communicate what changed in a version | Product Manager / Release Manager | At release | Confluence page, GitHub/GitLab release notes, email | Document / release page |
| Meeting Minutes | Record decisions, actions, and owners | PM / Scrum Master | After each client call or internal meeting | Confluence page | Document |
| Architecture Diagrams | Show system structure and component flow | Tech Lead / Solution Architect | During solution planning | Confluence page or repository diagram | Diagram (diagram-as-code or image) |
| Technical Documentation | Explain APIs, setup, and system behaviour | Developers / Tech Lead | During development | Repository wiki, developer portal, or Confluence | Document |
| User Guide | Explain how the end user should use the product | Technical Writer / Product Manager | Before release | Help centre, knowledge base, or Confluence | Document |
| Status Report | Communicate progress, risks, and next steps | Project Manager / PM | Weekly | Confluence page, email, or status dashboard | Document / dashboard |

### 2.1 Key Observation: Artefacts Are Not Files, They Are Sources of Truth

An artefact can live in many tools, but it should have exactly **one** authoritative location. The rest are copies or links. This is the difference between documentation and duplicated, contradictory documentation.

---

## 3. PRD - Product Requirements Document

### 3.1 What Is a PRD?

PRD stands for Product Requirements Document. A PRD tells the development team what they need to build and what the product should achieve.

A PRD answers four core questions:

1. What problem are we solving?
2. Who are we solving it for?
3. What exactly will we build?
4. How do we know when it is done?

### 3.2 What Information Does a PRD Contain?

| Section | What it explains |
|---|---|
| Project Overview | What is the project? |
| Business Objective | Why are we building it? |
| Target Users | Who will use the product? |
| Scope | What is included and excluded? |
| Functional Requirements | What should the system do? |
| Non-functional Requirements | How well should it work? |
| User Stories | What do users want to achieve? |
| Acceptance Criteria | How do we know a feature is complete? |
| Dependencies | What other systems or teams are required? |
| Risks | What could go wrong? |
| Questions | What we need to know further? |

### 3.3 Who Creates and Maintains the PRD?

- **Business Analyst** - Often the primary author.
- **Product Manager** - Owns scope, priorities, and business alignment.
- **Product Owner** - Validates that it reflects the product vision.
- **Client Stakeholders** - Provide input and give final approval.

### 3.4 Where the PRD Lives

- Confluence page under a dedicated Requirements or Product space.
- Shared drive (Google Drive / SharePoint) when a client requires their own repository.
- A file in a Git repository when the client treats documentation as code.
- Jira epic linked to the PRD, so every story traces back to a requirement.

---

## 4. Design Files - UI/UX Designs

### 4.1 What Are Design Files?

Design files are visual documents that show how the software or application should look and behave. The PRD explains **what** to build. Design files explain **how** it should look and how users interact with it.

### 4.2 What Do Design Files Contain?

| Design artefact | Purpose |
|---|---|
| Wireframes | Basic layout and structure |
| UI Designs | Final visual appearance |
| UX Flows | How users move through the application |
| Prototypes | Interactive demonstration of the design |
| Design System | Reusable colors, fonts, buttons, components |
| Responsive Designs | Desktop, tablet, and mobile layouts |

### 4.3 Who Creates Design Files?

- UI Designer
- UX Designer
- Product Designer

Product Managers, BAs, developers, and QA engineers may review them.

### 4.4 Where Design Files Live

- Figma (or an equivalent design and prototyping tool) as the single source of truth.
- Exported assets in a shared design repository when engineering needs direct file access.
- Design links attached to Jira stories, so developers open the approved frame directly from the ticket.

---

## 5. Backlog - Product Backlog and Sprint Backlog

### 5.1 What Is a Backlog?

The backlog tells the team what work needs to be done, what its priority is, and who is responsible for it. A backlog is an organized list of work that needs to be completed in a project.

### Product Backlog

The product backlog contains all planned work for the product.

### Sprint Backlog

A sprint backlog contains the selected work that the development team plans to complete during a particular sprint.

### 5.2 Product Backlog vs. Sprint Backlog

| Factor | Product Backlog | Sprint Backlog |
|---|---|---|
| Scope | All planned work for the product | Work selected for one sprint only |
| Owner | Product Owner | Development team, coordinated by Scrum Master |
| Time horizon | Long term and continuously updated | Short term, fixed for the sprint duration |
| Prioritization | Ordered by product value and priority | Ordered by what the team can complete |
| Changes | Reordered at any time as strategy changes | Locked once the sprint starts (scope freeze) |
| Purpose | Visibility and ordering of everything planned | Commitment and focus for the current sprint |
| Where It Lives | Jira product backlog | Jira sprint board / sprint scope |

### 5.3 A Typical Backlog Item May Include:

1. Issue ID
2. User story or task description
3. Priority
4. Acceptance criteria
5. Story points or estimated effort
6. Assignee
7. Status
8. Sprint assignment
9. Dependencies
10. Related design and requirement links

### 5.4 Who Manages the Backlog?

- **Product Owner:** prioritizes product work.
- **Scrum Master:** facilitates the Scrum process.
- **Developers:** break work into technical tasks and manage implementation.
- **QA:** contributes testing tasks and quality considerations.
- **Business Analyst:** helps clarify and refine requirements.

### 5.5 Where the Backlog Lives

- Jira project backlog, with issues typed as stories, tasks, bugs, and epics.
- Jira board views (Kanban or Scrum) for daily work tracking.
- A Confluence page for a static, human-readable snapshot for client or stakeholder review.

---

## 6. Test Plan - Software Testing Documentation

### 6.1 What Is a Test Plan?

A test plan is a document that explains how the QA team will test the software. The PRD explains what the software should do. The test plan explains how the team will verify that it works correctly.

### 6.2 What Does a Test Plan Contain?

| Section | Description |
|---|---|
| Test Objective | What are we trying to verify? |
| Scope | What will be tested? |
| Out of Scope | What will not be tested? |
| Testing Types | Functional, performance, security, etc. |
| Test Environment | Browser, OS, server, devices |
| Test Strategy | How testing will be performed |
| Test Data | Data required for testing |
| Roles and Responsibilities | Who performs testing? |
| Entry Criteria | Conditions before testing starts |
| Exit Criteria | Conditions before testing finishes |
| Risks | Potential testing challenges |
| Schedule | When testing will happen |

### 6.3 Who Creates the Test Plan?

Usually:

- QA Lead
- Test Manager
- Senior QA Engineer

### 6.4 Where the Test Plan Lives

- Confluence page, linked from the Jira epic and the release ticket.
- Test cases themselves in a test management tool (or as Jira test sub-tasks) when the team tracks case-level execution.
- A QA folder inside the repository when the client requires test documentation as code.

---

## 7. Test Plan vs. Test Case

This is an important interview question.

**Test Plan:** Explains the overall testing approach.
**Test Case:** Explains the exact steps to test an individual scenario.

| Factor | Test Plan | Test Case |
|---|---|---|
| Scope | The whole testing effort for a project or release | One specific scenario or condition |
| Focus | Strategy, scope, environment, schedule, and risks | Exact steps, inputs, expected outputs |
| Created By | QA Lead / Test Manager | QA Engineer, based on the test plan |
| Level of Detail | High level and strategic | Detailed and procedural |
| Change Frequency | Updated per project, release, or phase | Created and updated per scenario |
| Question It Answers | How will we test? | What exactly do we do to test this? |
| Typical Contents | Objective, scope, types, environment, entry/exit criteria, risks, roles, schedule | Preconditions, step-by-step actions, test data, expected result, pass/fail status |
| Where It Lives | Confluence page | Test management tool or Jira test issue |
| One-to-many | One test plan covers many test cases | Each test case traces back to the plan |

---

## 8. Release Notes - Software Release Documentation

### 8.1 What Are Release Notes?

Release notes are documents that explain what has changed in a new version of a software product. Release notes tell users, stakeholders, and internal teams what new features, improvements, bug fixes, and changes are included in a release.

### 8.2 What Do Release Notes Contain?

| Section | Purpose |
|---|---|
| Release Version | Identifies the software version |
| Release Date | When the version was released |
| New Features | Newly added functionality |
| Improvements | Enhancements to existing features |
| Bug Fixes | Issues resolved |
| Breaking Changes | Changes that may affect existing integrations |
| Known Issues | Issues that remain unresolved |
| Upgrade Instructions | How to move to the new version, if needed |

### 8.3 Who Prepares Release Notes?

Usually:

- Product Manager
- Product Owner
- Technical Writer
- Release Manager
- Development Team

### 8.4 Where Release Notes Live

- Confluence page for internal and client-facing announcements.
- GitHub or GitLab release notes attached to the tagged version.
- Changelog file in the repository (CHANGELOG.md) for a running history.
- Email or a release announcement page for client communication.

---

## 9. Artefact Comparison Summary

This table compares the five core artefacts side by side, which is the format most commonly asked for in interviews.

| Factor | PRD | Design Files | Backlog | Test Plan | Release Notes |
|---|---|---|---|---|---|
| Main Question | What and why? | How should it look and work? | What work is needed? | How will we verify it works? | What changed in this version? |
| Audience | Client, stakeholders, whole team | Designers, developers, QA | Product Owner and delivery team | QA, developers, client | Users, client, support, internal teams |
| Owner | PM / Business Analyst | UI/UX or Product Designer | Product Owner | QA Lead / Test Manager | PM / Product Owner / Release Manager |
| Stage | Discovery and analysis | Design | Planning and refinement | Testing | Release |
| Lifespan | Updated until scope is signed off | Updated until the feature is built | Updated continuously | Updated per phase or release | Frozen once the version ships |
| Level of Detail | Requirements and acceptance criteria | Layouts, flows, components | Prioritized work items | Approach, scope, and strategy | User-facing change summary |
| Format | Document | Design file and prototype | Jira issues | Document | Document or release page |
| Key Link | Links to goals and scope | Links to PRD requirements | Stories link to PRD and design | Links to requirements and stories | Links to stories, fixes, and tickets |

---

## 10. How All These Artefacts Work Together in a Real Project

### 10.1 End-to-End Project Workflow

1. **Step 1 - Business Requirement**

   The business wants to build an e-commerce website.

2. **Step 2 - PRD Creation**

   The BA or Product Manager documents requirements, features, and acceptance criteria.
   `PRD`

3. **Step 3 - UI/UX Design**

   Designers create wireframes, screen designs, and user flows.
   `Design Files`

4. **Step 4 - Backlog Creation**

   The Product Owner creates user stories and tasks in Jira and prioritizes them.
   `Backlog`

5. **Step 5 - Development**

   Developers implement the selected features based on requirements and approved designs.

6. **Step 6 - Testing**

   QA prepares the test plan, executes test cases, and reports defects.
   `Test Plan`

7. **Step 7 - Release**

   The team deploys the approved software and documents the delivered changes.
   `Release Notes`

### 10.2 Artefact Flow Across the Lifecycle

```text
Business Requirement
          |
          v
       PRD  <------------------->  Design Files
          |        (refine together)     |
          v                             v
       Backlog  <-------------------  Backlog
          |
          v
    Development
          |
          v
     Test Plan
          |
          v
    Release Notes
```

### 10.3 Traceability: Why This Matters

Every artefact should be traceable to the one before it. This is called **traceability**, and it is what lets a PM answer client questions quickly and defensibly.

| If the client asks... | Trace through... |
|---|---|
| "Why was this feature built?" | Feature -> Backlog story -> PRD requirement -> Business objective |
| "Where is the design for this screen?" | Jira story -> Linked design file -> Design frame |
| "How was this tested?" | Test case -> Test Plan -> PRD acceptance criteria |
| "What changed in this release?" | Release note -> Jira issues closed -> Stories completed |
| "Who approved this scope?" | PRD approval record -> Decision log / client sign-off |

### 10.4 Common Failure Points

| Failure | What It Looks Like | Fix |
|---|---|---|
| Artefacts out of sync | PRD says one thing, backlog says another | Single source of truth plus links between artefacts |
| Design drift | Developers build from memory instead of the approved frame | Link the design file on every story |
| Untested acceptance criteria | Features ship without matching PRD criteria | Trace criteria to test cases before exit |
| Missing release documentation | Client hears about changes only after deploy | Treat release notes as a release gate |
| Duplicate documents | Two versions of a PRD, no owner | Name one authoritative location, link the rest |

---

## 11. Key Takeaways

- Project artefacts are the documented evidence of a project's lifecycle.
- The PRD says **what** to build, design files say **how** it should work, the backlog says **what work** is needed, the test plan says **how it will be verified**, and release notes say **what changed**.
- Each artefact has a clear owner, a defined stage, and one authoritative location.
- Traceability between artefacts is what turns documentation into a working delivery system.

### 11.1 Interview Questions to Prepare

1. What is the difference between a PRD and a test plan?
2. What is the difference between a test plan and a test case?
3. What is the difference between a product backlog and a sprint backlog?
4. Where do you keep the PRD, and why did you choose that location?
5. How do you make sure the design, the backlog, and the release notes stay aligned?

---

## 12. Related Artefacts

- Meeting minutes
- Technical documentation
- Architecture diagrams
- User guides
- Project status reports
- Decision logs and audit trails (see *Governance - RACI for a client project, decision logs and audit trails*)
