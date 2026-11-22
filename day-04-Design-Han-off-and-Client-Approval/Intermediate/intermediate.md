
# Design Review, Client Presentation, Approval Workflow, and Feedback Handling

These four activities are part of managing the design process. They ensure that designs meet the agreed requirements, clients understand the proposed solution, feedback is handled properly, and developers receive approved designs.

## 1. Design Review

### What Is a Design Review?

A design review is the process of checking the designer's work against the Product Requirements Document (PRD).

The goal is to make sure the designs accurately represent the required features, user flows, business rules, and expected behaviour.

The review focuses on identifying missing requirements, incomplete screens, incorrect flows, and inconsistencies before the designs are presented to the client.

### What to Check During a Design Review

| Area | What to Check |
|---|---|
| Requirement coverage | All relevant PRD requirements are represented in the designs. |
| User flows | Users can navigate between screens and complete the required actions. |
| UI elements | Required buttons, forms, fields, menus, and other components are included. |
| Business rules | The designs reflect the rules and restrictions defined in the PRD. |
| Consistency | Similar components and interactions follow consistent patterns. |
| Edge cases | Unusual situations and unsuccessful actions are properly handled. |

### Empty, Loading, and Error States

A design review must also cover how the application behaves when there is no data, when something is processing, or when something goes wrong.

| State | Meaning | What to Check |
|---|---|---|
| Empty state | No data is available to display. | A clear message explains the situation and provides a next action when appropriate. |
| Loading state | The application is retrieving data or processing an action. | A loading indicator appears so users know the application is working. |
| Error state | Something has gone wrong. | A clear error message explains the problem and provides a way to recover when possible. |

- **Empty states:** Explain why nothing is displayed instead of leaving users with a blank screen.
- **Loading states:** Provide feedback while the application processes requests. This can include spinners, progress bars, or skeleton screens.
- **Error states:** Explain what went wrong without exposing unnecessary technical details. Users should also know what to do next.

These states should be included wherever they are relevant to the requirements.

## 2. Client Presentation

### What Is a Client Presentation?

A client presentation is a meeting where the proposed designs are presented using an interactive prototype.

A prototype demonstrates how users will navigate the application and interact with its features. It may not have working backend functionality, but it shows the intended user experience.

The goal is to help the client understand the proposed solution and collect feedback before development begins.

### Preparing for the Presentation

Before the meeting:

- Review the prototype and make sure the main navigation and interactions work.
- Compare the designs against the PRD.
- Identify the main user flows to demonstrate.
- Prepare questions about unclear requirements or design decisions.
- Make sure the correct design version is being presented.

### Walking the Client Through the Prototype

The presentation should follow the order in which users would normally interact with the application.

It should cover:

- The purpose of each screen.
- What users can do on each screen.
- How users navigate between screens.
- What happens after important actions.
- How the application handles different situations.

The presentation should focus on explaining how different parts of the application connect rather than jumping randomly between screens.

### Collecting Client Feedback

The client needs an opportunity to review the designs and explain what they want changed.

Vague comments should be clarified before being recorded as actionable requests. For example, if the client says a page is confusing, the actual issue needs to be identified. It could relate to the layout, content, navigation, or functionality.

All important feedback, requested changes, questions, and decisions should be documented during the meeting.

## 3. Approval Workflow

### What Is an Approval Workflow?

An approval workflow is the process of reviewing designs, making agreed revisions, and obtaining formal client approval before development begins.

It establishes which design version has been accepted and gives developers a confirmed reference for implementation.

### Written Sign-Off

Written sign-off is formal confirmation that the client has reviewed and approved a specific design deliverable.

Approval should always be documented rather than relying only on verbal confirmation during a meeting.

It can be obtained through email, Figma comments, a signed document, or a project management tool.

A proper sign-off should include:

- Project or feature name.
- Approved design version.
- Screens or deliverables included.
- Approval date.
- Name of the person providing approval.
- Any agreed exclusions or outstanding items.

The approval must clearly identify which version the client has accepted.

### Version Naming

Version naming is the practice of assigning identifiers to design revisions so changes can be tracked and the latest approved version can be identified.

For example:

| Version | Description |
|---|---|
| V1.0 | Initial design |
| V1.1 | Minor internal revisions |
| V1.2 | Changes based on client feedback |
| V2.0 | Major design revision |
| V2.1 | Further adjustments |

A consistent naming convention and a record of approved versions prevent confusion about which designs developers should use and make it easier to track changes.

### What Happens After Approval?

Once the client approves the designs, the project moves towards development handoff.

The next steps include:

1. **Finalise design files:** Organise approved screens, components, assets, and prototypes.
2. **Hand over to developers:** Share the approved designs and relevant documentation.
3. **Clarify interactions:** Explain how buttons, forms, navigation, and other components should behave.
4. **Prepare development tasks:** Translate requirements and designs into development tasks or Jira stories.
5. **Support implementation:** Clarify missing design details and answer development questions.
6. **Review implementation:** Compare the developed interface against the approved designs and identify discrepancies.

Approval does not mean designs can never change. However, changes after sign-off must be documented and assessed through the change management process. Significant changes may require updated approval.

## 4. Feedback Handling

### What Is Feedback Handling?

Feedback handling is the process of collecting, organising, prioritising, and communicating client feedback to the designer.

The goal is to turn client comments into clear, actionable requests that the design team can understand and address.

### Grouping Client Feedback

Client feedback should be organised by category so it is easier to understand and manage.

| Category | Description |
|---|---|
| Visual | Changes to colours, spacing, typography, layout, or appearance. |
| Functional | Changes to how a feature or interaction works. |
| Usability | Improvements that make the application easier to use. |
| Content | Changes to text, labels, descriptions, or displayed information. |
| Scope-related | Requests that introduce new features or change agreed requirements. |

Grouping feedback helps distinguish between simple design adjustments and requests that may require further analysis.

### Prioritising Feedback

Not every request has the same level of importance. Some changes are necessary to meet requirements, while others are optional improvements.

The MoSCoW prioritisation method can be used to organise feedback.

| Priority | Meaning |
|---|---|
| Must Have | Essential changes required to meet the agreed requirements. |
| Should Have | Important improvements that should be included if possible. |
| Could Have | Useful but non-essential improvements. |
| Won't Have | Changes excluded from the current scope or release. |

Feedback prioritisation should consider:

- **Business importance:** How important is the change to the business?
- **User impact:** Does it affect the user's ability to complete an important task?
- **Functional impact:** Does it address missing or incorrect functionality?
- **Scope:** Is the request already included in the agreed requirements?
- **Time and cost:** How much additional effort will it require?

Requests that introduce new functionality should be assessed separately rather than treated as ordinary design revisions.

### Passing Feedback to the Designer

Feedback must be clearly documented before being passed to the designer.

Vague client comments should not be forwarded without explaining what needs to change or why.

A useful feedback record includes:

| Field | Purpose |
|---|---|
| Feedback ID | Unique reference for tracking the request. |
| Screen/Feature | Identifies where the change is required. |
| Client feedback | Records what the client said or requested. |
| Required change | Explains what needs to be addressed. |
| Category | Identifies the type of feedback. |
| Priority | Indicates its importance. |
| Reference | Links to the relevant screen or prototype. |
| Owner | Identifies who is responsible. |
| Status | Tracks the request until completion. |

Each request must clearly communicate what needs to change, where the change is required, why it matters, and how important it is.

### Tracking Feedback

Each feedback request should be tracked until it has been completed, rejected, or deferred.

Common statuses include:

- **New:** Feedback has been received.
- **Under Review:** The team is evaluating the request.
- **Approved:** The requested change has been accepted.
- **In Progress:** The designer is working on it.
- **Completed:** The change has been made.
- **Rejected:** The request has been declined.
- **Deferred:** The change has been moved to a later release.

### Handling Scope Changes

Not all feedback falls within the original project scope.

When a client requests a new feature or changes an agreed requirement, the following steps apply:

1. Compare the request with the existing PRD and agreed scope.
2. Identify whether it introduces new functionality.
3. Discuss the technical impact with the relevant team.
4. Assess the impact on time, cost, and resources.
5. Communicate the impact to the client.
6. Obtain approval before proceeding.

This prevents additional requests from becoming unplanned work.

## 5. How These Processes Work Together

The four activities form a continuous process:

1. **Design Review:** Check the designs against the PRD and identify missing requirements or incomplete states.
2. **Client Presentation:** Walk the client through the prototype and collect feedback.
3. **Feedback Handling:** Group, prioritise, document, and assign the requested changes.
4. **Design Revisions:** The designer makes the agreed changes, and the updated designs are reviewed.
5. **Approval Workflow:** Obtain written sign-off for the final design version.
6. **Development Handoff:** Share the approved designs and documentation with developers.

The review and feedback process may repeat until the client approves the designs.

## 6. Responsibilities

| Activity | Responsibility |
|---|---|
| Design review | Check designs against the PRD and identify missing requirements or states. |
| Client presentation | Present the prototype and explain the user flows. |
| Feedback collection | Document client comments, questions, and requested changes. |
| Feedback prioritisation | Group requests, assess their importance, and identify scope changes. |
| Designer communication | Turn client feedback into clear, actionable instructions. |
| Approval | Obtain written sign-off and maintain version records. |
| Development handoff | Ensure developers receive the approved designs and relevant documentation. |

