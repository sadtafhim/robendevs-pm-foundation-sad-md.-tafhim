# Gap Analysis, Clarification Log, Non-Functional Requirements, and Writing a PRD

These four topics are essential to requirements analysis. They help ensure that client expectations are understood, missing information is identified, and requirements are properly documented before development begins.

# 1. Gap Analysis

## What Is Gap Analysis?

Gap analysis is the process of identifying missing, incomplete, or unclear requirements before development begins.

Clients often explain what they want without covering every detail. A Business Analyst (BA) or Project Manager (PM) must identify these gaps and clarify them.

For example, a client might say:

"I want users to register and log in to my website."

This raises several questions:

- What happens if someone enters an incorrect password?
- Is email verification required?
- Can users reset forgotten passwords?
- What happens if someone registers with an existing email?

These unanswered questions are gaps that need to be addressed.

## Four Important Areas of Gap Analysis

### A. Missing Flows

A missing flow occurs when an important user journey has not been defined.

For example, an e-commerce website may support product purchases, but what happens if a customer wants to cancel an order, request a return, or retry a failed payment?

These additional flows must be identified and documented.

### B. Unclear Rules

Business rules define how a system should behave under specific conditions.

For example, a client says:

"Customers should receive discounts."

You need to clarify:

- How much discount is available?
- Which products are eligible?
- Is there a minimum purchase amount?
- Can multiple discount codes be combined?
- When does the discount expire?

Clear rules prevent developers from making assumptions.

### C. Undefined Edge Cases

Edge cases are unusual situations that may occur while using a system.

For example:

- A customer tries to purchase more items than are available.
- Two customers attempt to buy the last available product.
- A product's price changes while it is in someone's cart.
- A customer submits the same order multiple times.

Identifying edge cases helps prevent unexpected behavior and data inconsistencies.

### D. Error States

Error states describe how the system should respond when something goes wrong.

For example, during login:

| Situation | Expected Behavior |
|---|---|
| Incorrect password | Display an error message. |
| Account is locked | Inform the user. |
| Server unavailable | Display an error and allow retrying. |
| Internet disconnected | Notify the user. |

Every important feature should have clearly defined error handling.

## How to Perform Gap Analysis

Review each feature and ask:

1. Are all important user flows defined?
2. Are the business rules clear?
3. Have relevant edge cases been considered?
4. Have error states been documented?

The goal is to ensure developers do not have to guess how something should work.

# 2. Clarification Log

## What Is a Clarification Log?

A clarification log is a document used to record unanswered questions during requirement analysis.

Instead of relying on memory or repeatedly discussing the same issues, the team records each question, assigns someone responsible for answering it, and tracks its progress.

A clarification log typically contains:

- **Question ID:** A unique identifier, such as Q-001.
- **Question:** The information that needs clarification.
- **Owner:** The person responsible for providing an answer.
- **Status:** Whether the question is open, in progress, or resolved.
- **Answer:** The confirmed response.

## Example of a Clarification Log

| ID | Question | Owner | Status | Answer |
|---|---|---|---|---|
| Q-001 | Is email verification required? | Client | Confirmed | Yes. |
| Q-002 | Can customers cancel paid orders? | Client | Open | Pending. |
| Q-003 | Can multiple discount codes be used? | Product Manager | Confirmed | No. |

## Why Is It Important?

A clarification log:

1. Prevents misunderstandings by keeping decisions documented.
2. Tracks unanswered questions.
3. Establishes accountability by assigning owners.
4. Gives developers a reliable reference.
5. Prevents repeated discussions about previously resolved issues.

Remember, a clarification log is not just a list of questions. It also records the decisions that help turn unclear requirements into actionable ones.

# 3. Non-Functional Requirements (NFRs)

## What Are Non-Functional Requirements?

Non-functional requirements describe how well a system should work rather than what functionality it should provide.

For example:

- Functional requirement: Users can search for products.
- Non-functional requirement: Search results should appear within two seconds under normal operating conditions.

A feature may work correctly but still provide a poor experience if it is slow, insecure, or difficult to use.

## Five Important Categories

### A. Performance

Defines how quickly and efficiently a system should operate.

Important considerations include:

- Response time
- Page loading speed
- Number of concurrent users
- Processing speed
- Scalability

Example: Product pages should load within three seconds under agreed testing conditions.

### B. Security

Defines how the system protects user information and prevents unauthorized access.

Important considerations include:

- Authentication and authorization
- Data encryption
- Secure password storage
- Session management
- Access control

Example: Users must only be able to access their own accounts and orders.

### C. Accessibility

Ensures that people with different abilities can use the system.

Important considerations include:

- Screen reader support
- Keyboard navigation
- Sufficient color contrast
- Alternative text for meaningful images
- Clear form labels and error messages

Example: Users should be able to complete a registration form without using a mouse.

### D. Device Compatibility

Defines which devices the system must support.

For example:

- Desktop computers
- Laptops
- Android smartphones
- iPhones and tablets

The interface should adapt to different screen sizes without breaking functionality.

### E. Browser Compatibility

Defines which browsers and versions the system must support.

Common examples include:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge
- Apple Safari

Example: The website must support the latest two major versions of these browsers.

## Functional vs Non-Functional Requirements

| Functional Requirements | Non-Functional Requirements |
|---|---|
| Describe what the system does. | Describe how well it works. |
| Focus on features and behavior. | Focus on quality and performance. |
| Example: Users can log in. | Example: Login requests should complete within two seconds. |
| Example: Users can search products. | Example: Search results should load within two seconds. |

**Important:** NFRs should be specific and measurable whenever possible.

Instead of writing "The website should be fast," define an actual performance target.

# 4. Writing a PRD

## What Is PRD Writing?

PRD writing is the process of turning discovery notes, client discussions, and confirmed requirements into a structured Product Requirements Document.

Discovery notes are often informal and incomplete. A PRD organizes that information into clear requirements that developers, designers, and testers can follow.

## Steps to Write a PRD

### Step 1: Organize Discovery Notes

Review and organize information collected from meetings, client discussions, and stakeholder feedback.

Group related information into categories such as:

- User registration and login
- Product management
- Shopping cart
- Checkout and payment
- Order management
- Admin dashboard

### Step 2: Identify Functional Requirements

Define the specific features and actions the system must support.

Example: User Registration

- Users can register using their name, email, and password.
- The system validates submitted information.
- Users must verify their email addresses.

Requirements should be specific rather than vague.

### Step 3: Identify Non-Functional Requirements

Document the system's quality expectations and technical limitations.

These include performance, security, accessibility, scalability, and device and browser compatibility.

### Step 4: Write User Stories

User stories describe requirements from the user's perspective.

Common format:

"As a [type of user], I want [functionality] so that [goal]."

Example:

"As a customer, I want to add products to my shopping cart so that I can purchase multiple products together."

### Step 5: Define Acceptance Criteria

Acceptance criteria describe the conditions a feature must satisfy to be considered complete.

A common format is Given/When/Then.

Example:

**User Story:** As a customer, I want to log in so that I can access my account.

**Acceptance Criteria:**

- Given a registered user, when they enter the correct credentials, then they should be logged in.
- Given incorrect credentials, when they submit the form, then an error message should appear.
- Given empty required fields, when they submit the form, then validation messages should appear.

### Step 6: Perform Gap Analysis

Review the requirements and check for missing flows, unclear business rules, edge cases, and error states.

Resolve any gaps that could affect development.

### Step 7: Maintain a Clarification Log

Record unanswered questions, assign responsible people, and track their status.

Once an answer is confirmed, update the relevant PRD section.

### Step 8: Review and Validate the PRD

Share the PRD with relevant stakeholders to confirm that:

- Requirements accurately reflect client expectations.
- Features and scope are clearly defined.
- Acceptance criteria are testable.
- Business rules are documented.
- Unresolved questions are identified.

Make necessary corrections before development begins.

## What Should a PRD Contain?

| Section | Purpose |
|---|---|
| Product Overview | Explains the product and the problem it solves. |
| Goals and Objectives | Defines what the product should achieve. |
| Target Users | Identifies who will use it. |
| Scope | Defines what is included and excluded. |
| Features and Requirements | Describes required functionality. |
| User Stories | Explains requirements from the user's perspective. |
| Acceptance Criteria | Defines when features are considered complete. |
| Business Rules | Explains how the system should behave. |
| Non-Functional Requirements | Defines quality and performance expectations. |
| Edge Cases and Error States | Covers unusual situations and failures. |
| Dependencies and Constraints | Identifies limitations and dependencies. |
| Open Questions | Lists decisions that still need clarification. |

Not every PRD needs exactly the same structure. Include the sections necessary to explain the product clearly.

# 5. How Everything Works Together

These four topics are connected and form part of the same requirements documentation process.

Consider an e-commerce website:

| Stage | What Happens |
|---|---|
| Discovery | Collect the client's initial requirements. |
| Gap Analysis | Identify missing flows, unclear rules, edge cases, and errors. |
| Clarification Log | Record unanswered questions and track their answers. |
| Requirement Definition | Define features, NFRs, user stories, and acceptance criteria. |
| PRD Writing | Organize everything into a structured document. |
| Review and Approval | Confirm the requirements with stakeholders. |
| Development and Testing | Build the system and verify it against the requirements. |

**Example:**

Initial requirement: Customers should be able to purchase products.

- **Gap analysis:** What happens if payment fails?
- **Clarification question:** Can customers retry failed payments?
- **Clarification answer:** Yes, without creating a new order.
- **Functional requirement:** The system must allow customers to retry failed payments for existing orders.
- **Non-functional requirement:** Payment requests must be processed securely.
- **User story:** As a customer, I want to retry a failed payment so that I can complete my purchase.
- **Acceptance criteria:** Given a failed payment, when the customer retries with valid payment information, then the system should process the existing order's payment.
- **PRD:** Document all confirmed requirements and expected behavior.

The main idea is simple:

- **Gap Analysis:** Finds what is missing.
- **Clarification Log:** Tracks what needs answers and records decisions.
- **Non-Functional Requirements:** Define how well the system should work.
- **PRD Writing:** Brings everything together into one organized document.