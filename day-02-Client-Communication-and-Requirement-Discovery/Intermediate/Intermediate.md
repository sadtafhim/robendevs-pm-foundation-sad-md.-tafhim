
# Requirement Clarification, Expectation Management, Requirement Types, and Written Confirmation

These topics help project managers clarify client requirements, manage project expectations, understand different types of requirements, and document important agreements to avoid misunderstandings.

## 1. Requirement Clarification: Five Whys and Mock-ups

### The Five Whys Technique

The Five Whys is a technique used to identify the root cause behind a client's request or problem.

It involves repeatedly asking "Why?" until the actual business problem is understood instead of immediately accepting the client's suggested solution.

**Example:**

A client requests automated email notifications.

1. **Why?** Customers frequently contact the company about their orders.
2. **Why?** Customers cannot check their order status themselves.
3. **Why?** The website does not have an order-tracking feature.
4. **Why?** The original website was built without order tracking.
5. **Why?** The increasing number of orders has created too much work for the support team.

**Identified Problem:** The support team spends too much time answering order-related questions because customers cannot track their purchases.

**Possible Solution:** Introduce order tracking and automated email notifications.

The goal is not necessarily to ask exactly five questions but to continue asking until the root cause is understood.

### Mock-ups

A mock-up is a visual representation of how a website or application is expected to look before development begins.

It shows design elements such as colors, images, typography, buttons, and page layouts.

Mock-ups help clients visualize the proposed interface and provide feedback before development, reducing design misunderstandings and unnecessary revisions.

### Wireframe vs. Mock-up

| Wireframe | Mock-up |
|---|---|
| Shows the basic structure of a page. | Shows the expected visual appearance. |
| Focuses on layout and element placement. | Focuses on colors, typography, images, and styling. |
| Usually simple and low-detail. | Usually detailed and visually refined. |
| Helps plan the interface structure. | Helps review and finalize the visual design. |

## 2. Expectation Management: Scope, Timeline, and Budget

Expectation management is the process of ensuring that the client and project team have a realistic understanding of what the project will deliver, how long it will take, and how much it will cost.

### A. Scope Management

**Project Scope** defines the work, features, and deliverables included in a project. It establishes the boundaries of what the team is expected to complete.

A project scope should define:

1. **Project Objectives:** What the project should achieve.
2. **Features and Functionality:** What the system should do.
3. **Deliverables:** What the client will receive.
4. **Responsibilities:** What the client and development team must do.
5. **Out-of-Scope Items:** What is not included in the agreement.

**Out of Scope:** Features or services that are not included in the agreed project scope.

**Scope Creep:** The gradual addition of features or requirements without properly evaluating or controlling their impact on the project.

For example, a client initially requests an e-commerce website but gradually adds product reviews, wishlists, and loyalty points without adjusting the budget or deadline.

**How to Prevent Scope Creep:**

- Document the agreed scope and requirements.
- Clearly define included and excluded features.
- Evaluate additional requests before accepting them.
- Explain their impact on cost and timeline.
- Obtain client approval before starting additional work.
- Update project documentation when changes are approved.

### B. Timeline Management

Timeline management involves planning and tracking the time required to complete a project.

Important elements include:

1. **Start Date:** When the project begins.
2. **Milestones:** Important stages, such as design completion, development completion, and testing.
3. **Task Deadlines:** Deadlines assigned to individual activities.
4. **Testing and Review:** Time allocated for testing, bug fixing, and client feedback.
5. **Final Delivery Date:** Expected project completion date.

Project managers should set realistic deadlines, monitor progress, and communicate potential delays early.

### C. Budget Management

Budget management involves estimating, allocating, and monitoring the money required to complete a project.

Common budget components include:

- **Development Costs:** Frontend and backend development.
- **Design Costs:** UI/UX design and prototypes.
- **Testing Costs:** Quality assurance and bug fixing.
- **Infrastructure Costs:** Hosting, servers, and databases.
- **Third-Party Services:** APIs, payment gateways, and software licenses.
- **Maintenance Costs:** Ongoing support and updates, if included.

Project managers should monitor spending and discuss additional costs before accepting new work.

## 3. Requirement Types

Project requirements describe what a client expects from a software product, how it should work, and what conditions or limitations it must satisfy.

There are four main types:

1. Functional Requirements.
2. Non-Functional Requirements.
3. Business Rules.
4. Project Constraints.

### A. Functional Requirements

Functional requirements describe **what the system must do**.

They define the features, operations, and actions the software must provide.

Examples for an e-commerce website:

- Customers can register and log in.
- Customers can browse and search products.
- Customers can add products to their carts.
- Customers can place orders and make payments.
- Administrators can manage products and orders.

### B. Non-Functional Requirements

Non-functional requirements describe **how well the system must work**.

They define the quality, performance, security, and reliability standards of the software.

Common types include:

- **Performance:** How quickly the system responds.
- **Security:** How the system protects information.
- **Usability:** How easy the system is to use.
- **Reliability:** How consistently the system operates.
- **Scalability:** How well it handles increasing users and workloads.
- **Compatibility:** Which devices, browsers, and operating systems it supports.

**Example:**

- Functional: Customers can log in.
- Non-Functional: The login process should complete within two seconds under agreed conditions.

### C. Business Rules

Business rules are policies and conditions that define how a business operates.

They determine what is allowed, restricted, or required within the system.

Examples:

- Customers cannot purchase out-of-stock products.
- Orders above ৳5,000 qualify for free delivery.
- Customers can return products within seven days.
- Only administrators can change product prices.
- Expired discount codes cannot be used.

**Business Rules vs. Functional Requirements**

- **Business Rule:** Customers cannot order out-of-stock products.
- **Functional Requirement:** The system must check product availability before allowing an order.

A business rule defines what the business requires, while a functional requirement explains what the software must do to enforce that rule.

### D. Project Constraints

Constraints are limitations that affect how a project can be planned, developed, and delivered.

Common types include:

- **Budget Constraints:** Limited money available for development.
- **Time Constraints:** Fixed deadlines or delivery schedules.
- **Technical Constraints:** Required technologies or existing systems.
- **Resource Constraints:** Limited developers, skills, or equipment.
- **Legal Constraints:** Laws and regulations the project must follow.
- **Platform Constraints:** Restrictions on supported devices or platforms.

**Business Rules vs. Constraints**

- **Business Rule:** Customers can return products within seven days.
- **Constraint:** The website must be completed within three months.

Business rules define how the business operates, while constraints define the limitations within which the project must operate.

### E. Documenting Requirements

A **Software Requirements Specification (SRS)** is a structured document that records the software's requirements, functionality, quality standards, business rules, and constraints.

A requirement record generally includes:

- **Requirement ID:** Unique identifier for tracking.
- **Requirement Name:** Short description.
- **Requirement Type:** Functional, non-functional, business rule, or constraint.
- **Description:** What is required.
- **Priority:** Importance of the requirement.
- **Acceptance Criteria:** Conditions that must be met for acceptance.
- **Source:** Where the requirement came from.

Requirements should be clear, specific, and measurable wherever possible.

For example:

- Vague: The website should be fast.
- Better: Product pages should load within three seconds under agreed test conditions.

## 4. Written Confirmation: Email and Confluence

### What Is Written Confirmation?

Written confirmation means recording important project discussions, decisions, and agreements so everyone has the same understanding of what was agreed upon.

It prevents misunderstandings caused by relying only on verbal discussions.

### Why Is Written Confirmation Important?

- **Prevents Misunderstandings:** Everyone has the same understanding of agreements.
- **Creates Accountability:** Responsibilities and deadlines are recorded.
- **Provides Evidence:** Creates a written record of decisions and approvals.
- **Tracks Changes:** Records what changed and when.
- **Avoids Disputes:** Provides a reference when disagreements occur.
- **Maintains Continuity:** Team members can review previous decisions.

Important agreements to document include project scope, requirements, deadlines, budget, design approvals, and change requests.

### A. When to Use Email

Email is best for direct communication with clients, stakeholders, and team members.

Use it to:

- Confirm project scope and requirements.
- Request or confirm approvals.
- Confirm deadlines and budget.
- Discuss additional requests and their impact.
- Summarize meeting decisions.
- Notify stakeholders about changes.

### B. When to Use Confluence

Confluence is a documentation platform used to organize and maintain project information in one central location.

Use it to:

- Document project scope and requirements.
- Store meeting notes and decisions.
- Maintain project timelines and milestones.
- Record change requests and approvals.
- Maintain project documentation and decision history.

### Email vs. Confluence

| Email | Confluence |
|---|---|
| Best for direct communication. | Best for organized documentation. |
| Used to confirm agreements and request approvals. | Used to maintain project records. |
| Keeps a history of conversations. | Keeps project information in one central location. |
| Useful for notifying people about changes. | Useful for tracking requirements, decisions, and changes. |

### C. Using Both Together

1. The client requests an additional feature.
2. The project manager evaluates its impact on cost and timeline.
3. The project manager emails the client with the details.
4. The client approves the change through email.
5. The project manager updates the documentation in Confluence.
6. The development team is informed about the approved change.

This ensures that agreements are confirmed with the client and recorded for the entire team.

### Best Practices for Written Confirmation

- Confirm important agreements promptly.
- Use clear language.
- Record responsibilities and deadlines.
- Document changes to scope, budget, and timeline.
- Keep project documentation updated.
- Record who approved important decisions and changes.

## Key Takeaways

1. **Five Whys:** Identify the root cause behind a client's request instead of immediately accepting their proposed solution.
2. **Mock-ups:** Visualize and review the expected interface before development.
3. **Expectation Management:** Set realistic expectations regarding project scope, timeline, and budget.
4. **Scope Creep:** Control additional requirements through proper evaluation and approval.
5. **Requirement Types:** Understand functional requirements, non-functional requirements, business rules, and constraints.
6. **SRS:** Document requirements clearly so they can be developed, tracked, and tested.
7. **Written Confirmation:** Record important agreements and approvals through email and maintain organized project documentation in Confluence.

**Remember:** Clear requirements, realistic expectations, and documented agreements help prevent misunderstandings, control project changes, and ensure the final product meets the client's expectations.
