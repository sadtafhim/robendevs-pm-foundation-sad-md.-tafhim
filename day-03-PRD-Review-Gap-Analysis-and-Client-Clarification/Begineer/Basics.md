
# Product Requirements Document (PRD): Structure, Reading, User Stories, and Acceptance Criteria

## 1. What Is a Product Requirements Document (PRD)?

A Product Requirements Document (PRD) explains what a product should do, who it is being built for, and what requirements it must satisfy. It helps the client and development team understand the product's purpose, features, expected behavior, and limitations.

A PRD focuses on **what needs to be built and why**, rather than how developers should implement it technically.

For example, if a client wants an e-commerce website, the PRD should explain its main goals, target users, required features, and expected functionality before development begins.

## 2. Structure of a PRD

A PRD generally contains the following sections:

### 2.1 Goals

Goals explain what the product is intended to achieve and what problems it should solve.

For example, the goals of an e-commerce website might include:

- Allow customers to purchase clothing online.
- Make product browsing easier.
- Increase online sales.
- Help the business manage orders efficiently.

Goals give the development team a clear understanding of the client's expectations and help ensure that the final product delivers the intended value.

### 2.2 Users

This section identifies who will use the product and what they need from it.

For example, an e-commerce website might have three main user types:

- **Customers:** Browse products, place orders, and track deliveries.
- **Administrators:** Manage products, prices, orders, and customer accounts.
- **Delivery personnel:** View assigned orders and update delivery statuses.

Identifying users helps the team understand their different responsibilities and ensures that important functionality is not overlooked.

### 2.3 Scope

Scope defines what is included in the project and what is excluded. It establishes clear boundaries and prevents misunderstandings between the client and development team.

Scope has two main parts:

**In Scope:** Features included in the project.

- User registration and login.
- Product browsing and searching.
- Shopping cart and checkout.
- Online payments.
- Basic order tracking.

**Out of Scope:** Features not included in the current agreement.

- Android and iOS applications.
- AI-powered product recommendations.
- Multi-vendor marketplace functionality.
- International shipping.

Clearly defining scope helps prevent **scope creep**, which occurs when additional features are introduced without properly evaluating their impact on the project's time and cost.

### 2.4 Features

Features describe the specific functionality the product must provide.

For example, an e-commerce website might include:

- User registration and login.
- Product catalog and search.
- Shopping cart.
- Checkout and payment integration.
- Order management.

Each feature should have a clear description of its expected behavior.

**Example: Shopping Cart**

Customers should be able to add products, change quantities, remove items, and view the total price before checkout.

Features break the product into manageable parts, making development, progress tracking, and testing easier.

### 2.5 User Stories

User stories describe functionality from the user's perspective. They explain what the user wants to accomplish and why.

A common format is:

**As a [user], I want [functionality] so that [benefit].**

Example:

"As a customer, I want to add products to my shopping cart so that I can purchase multiple items together."

A user story identifies:

- **User:** Who needs the functionality?
- **Functionality:** What do they want to do?
- **Benefit:** Why do they need it?

User stories help developers understand the actual needs behind a feature rather than focusing only on technical tasks.

### 2.6 Acceptance Criteria

Acceptance criteria define the specific conditions a feature must satisfy before it can be considered complete.

For example, a shopping cart might have these acceptance criteria:

- Customers can add available products to their carts.
- The cart displays product names, prices, and quantities.
- Customers can increase or decrease quantities.
- Customers can remove products.
- The total price updates automatically when quantities change.

Acceptance criteria make requirements specific and testable, reducing misunderstandings about what the client expects.

### 2.7 Non-Functional Requirements

Non-functional requirements describe how well a product should operate rather than what functionality it provides.

For example:

- **Performance:** Pages should load quickly, even with multiple users.
- **Security:** User information and payment data must be protected.
- **Usability:** The website should be easy to navigate.
- **Reliability:** The system should operate without frequent failures.
- **Scalability:** The website should handle increasing users and orders.
- **Compatibility:** The website should work across common browsers and devices.

A product may have all the required features but still provide a poor experience if it is slow, unreliable, or insecure. Non-functional requirements help ensure the product meets the expected quality standards.

## 3. Reading a PRD: Understanding Every Section Before Raising Questions

Reading a PRD involves understanding the requirements, how they relate to one another, and whether anything is missing, unclear, or inconsistent.

Before raising questions or starting development, review the following:

### 3.1 Understand the Product Goals

Identify why the product is being developed, what problem it solves, and what the client expects to achieve.

Understanding the goals helps you evaluate whether the proposed features support the product's main purpose.

### 3.2 Identify the Users

Understand who will use the system, what actions they can perform, and whether different users have different permissions.

For example, if customers can place orders, the system must also provide administrators with a way to manage those orders.

### 3.3 Review the Scope

Check what is included and excluded. Do not assume that a feature is part of the project simply because it seems necessary.

For example, online payments do not automatically mean that multiple payment gateways, international currencies, or automatic refunds are included.

### 3.4 Examine Every Feature

Understand what each feature should actually do rather than relying on its name.

For example, a login feature should clarify:

- Whether users log in using email or phone numbers.
- Whether password recovery is available.
- What happens when incorrect credentials are entered.
- Whether repeated failed attempts result in account restrictions.

### 3.5 Connect User Stories With Acceptance Criteria

Check whether each user story has clear acceptance criteria.

For example:

**User Story:**

"As a customer, I want to reset my password so that I can regain access to my account."

**Acceptance Criteria:**

- Customers can request a reset using their registered email.
- The system sends a password reset link.
- The link expires after a defined period.
- Customers can create a new password using a valid link.

If the expected behavior is unclear or the acceptance criteria are missing, further clarification may be necessary.

### 3.6 Identify Missing or Conflicting Requirements

Look for information that is missing, unclear, or inconsistent across sections.

For example:

- The goals mention online payments, but payment integration is missing from the scope.
- Customers can track orders, but the document does not explain how delivery statuses are updated.
- Users can register, but email verification is not mentioned.
- The website must support mobile devices, but responsive design requirements are unclear.

Read the entire PRD before raising questions. Sometimes information that appears missing in one section is explained elsewhere.

## 4. User Stories and the INVEST Criteria

### 4.1 The User Story Format

A user story describes a requirement from the perspective of the person using the product.

The standard format is:

**As a [user], I want [functionality] so that [benefit].**

Example:

"As a customer, I want to filter products by size and color so that I can find clothing that matches my preferences."

This identifies the user, the functionality they need, and the benefit they expect.

User stories also help break large features into smaller requirements. For example, an authentication system can be divided into separate stories for registration, login, password recovery, and email verification.

### 4.2 The INVEST Criteria

INVEST is a set of six principles used to evaluate whether a user story is well-written.

**I – Independent**

A story should be as independent as possible so it can be developed and tested without unnecessary dependencies on other stories.

**N – Negotiable**

A story should describe the required outcome without unnecessarily restricting how developers achieve it. Details can be discussed and refined with stakeholders.

**V – Valuable**

A story should provide meaningful value to the user or business by solving a problem or helping achieve a goal.

**E – Estimable**

The development team should have enough information to estimate the effort required. Vague requirements need further clarification.

**S – Small**

A story should be small enough to complete within a reasonable development period. Large stories should be divided into smaller ones.

**T – Testable**

A story should have clear conditions that allow the team to verify whether the functionality works as expected.

For example, "As a customer, I want the website to be user-friendly" is difficult to estimate and test because it does not describe specific behavior.

A better story would be:

"As a customer, I want to filter products by category so that I can find relevant items more quickly."

This describes a specific functionality that developers can estimate and testers can verify.

## 5. Acceptance Criteria: The Given/When/Then Format

Acceptance criteria define the conditions a feature must meet to be accepted as complete.

A commonly used format is **Given/When/Then**, which describes a scenario in three parts:

- **Given:** The initial situation or conditions.
- **When:** The action performed by the user or system.
- **Then:** The expected result.

### 5.1 Example: Successful Login

**User Story:**

"As a customer, I want to log in to my account so that I can access my personal information and manage my orders."

**Acceptance Criteria:**

**Scenario: Successful Login**

- **Given:** The customer has a registered account and is on the login page.
- **When:** The customer enters a valid email address and password and clicks the login button.
- **Then:** The system authenticates the customer and redirects them to the account dashboard.

### 5.2 Cover Different Scenarios

A feature should not be tested only under ideal conditions. Acceptance criteria should also cover possible errors and alternative situations.

For example, a login feature might include:

**Scenario 1: Incorrect Password**

- **Given:** The customer has a registered account.
- **When:** The customer enters an incorrect password.
- **Then:** The system rejects the login attempt and displays an error message.

**Scenario 2: Empty Required Fields**

- **Given:** The customer is on the login page.
- **When:** The customer submits the form without entering the required information.
- **Then:** The system displays validation messages.

**Scenario 3: Password Recovery**

- **Given:** The customer is on the login page.
- **When:** The customer selects the forgot password option.
- **Then:** The system provides a way to request a password reset.

Writing multiple scenarios makes the expected behavior clearer and gives testers specific conditions to verify.

### 5.3 Why Given/When/Then Is Useful

It gives everyone a shared understanding of how a feature should behave.

- **Developers** know what functionality to implement.
- **Testers** can use the scenarios to create test cases.
- **Designers** understand which interface states and messages are needed.
- **Clients** can confirm whether the expected behavior matches their requirements.

### 5.4 User Stories vs. Acceptance Criteria

| User Stories | Acceptance Criteria |
|---|---|
| Explain what the user wants and why. | Define what must happen for acceptance. |
| Focus on user needs. | Focus on expected system behavior. |
| Describe requirements at a higher level. | Provide specific, testable conditions. |
| Explain the purpose of a feature. | Determine whether the feature is complete. |

For example:

**User Story:**

"As a customer, I want to add products to my shopping cart so that I can purchase multiple items together."

**Acceptance Criteria:**

- Customers can add products to their carts.
- The cart displays selected products.
- Customers can update quantities.
- The total price updates automatically.
- Customers can remove products.

The user story explains the need, while the acceptance criteria define what must work to satisfy it.

## 6. How Everything Connects in a PRD

Each section contributes to a complete understanding of the product.

1. **Goals:** Why are we building the product?
2. **Users:** Who will use it?
3. **Scope:** What is included and excluded?
4. **Features:** What capabilities should it provide?
5. **User Stories:** What does each user want to accomplish?
6. **Acceptance Criteria:** How do we determine whether it works correctly?
7. **Non-Functional Requirements:** What quality standards must it meet?

For example, an e-commerce website might have the following requirement:

- **Goal:** Allow customers to purchase clothing online.
- **User:** Customers who want to browse and buy products.
- **Scope:** Product browsing, shopping carts, checkout, and order management.
- **Feature:** Shopping cart functionality.
- **User Story:** As a customer, I want to add products to my cart so that I can purchase them later.
- **Acceptance Criteria:** Customers can add products, update quantities, remove items, and view the updated total.
- **Non-Functional Requirement:** Cart updates should happen without noticeable delays.

Together, these sections explain the product's purpose, required functionality, expected behavior, and quality standards.

## 7. The Project Manager's Responsibility When Working With a PRD

A project manager should review the PRD carefully before passing requirements to the development team.

Their responsibilities include:

- Understanding the product goals and business objectives.
- Identifying users and their responsibilities.
- Checking whether the scope is clearly defined.
- Reviewing features for missing or unclear functionality.
- Ensuring user stories describe meaningful user needs.
- Checking whether acceptance criteria are specific and testable.
- Reviewing non-functional requirements such as security and performance.
- Identifying missing or conflicting information.
- Confirming important decisions with the client before development begins.

For example, if the PRD says customers should be able to track orders but does not explain how delivery statuses are updated, the project manager should ask:

"Should administrators update order statuses manually, or should they update automatically through integration with a delivery service?"

This matters because the answer can affect development effort, project timelines, and cost.

The main responsibility is to resolve uncertainties before they become problems during development.
