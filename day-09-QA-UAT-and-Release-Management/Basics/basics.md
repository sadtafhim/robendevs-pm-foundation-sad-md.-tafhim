# QA Handoff, Testing, Bug Reporting, and PM Self-Testing

These practices help a Project Manager ensure that developed features meet requirements, defects are addressed, and the product is ready for client review or release.

The PM's responsibility is not to perform detailed QA testing but to coordinate the process, clarify expectations, track issues, and verify that important functionality is ready.

## 1. QA Handoff

### What Is QA Handoff?

QA handoff is the process of transferring completed development work to the QA team for testing.

The PM ensures that QA has enough information to understand what was developed, how it should work, and what conditions it must satisfy.

### What Should the PM Provide?

**1. Requirements**

Provide the relevant requirements so QA understands the feature's purpose and expected behavior.

**2. Acceptance Criteria**

Acceptance criteria define the conditions a feature must meet to be considered complete. They give QA clear points to verify.

**3. Test Data**

Ensure QA has suitable test accounts, sample information, and different data scenarios. Use test or anonymized data instead of exposing sensitive production information.

**4. Environment Details**

Tell QA where the feature is available and provide the necessary access information.

Common environments include:

- **Development:** Used by developers during implementation.
- **Staging:** Used for testing before release.
- **Production:** The live application used by customers.

**5. Known Issues and Limitations**

Inform QA about existing problems, incomplete functionality, or limitations that may affect testing.

**6. Related Jira Tickets**

Link the development tasks, requirements, and related issues so QA can trace what needs to be tested.

### QA Handoff Workflow

1. Developers complete the feature.
2. PM confirms that requirements and acceptance criteria are documented.
3. PM provides QA with the necessary information and access.
4. QA tests the feature and reports defects.
5. Developers fix reported issues.
6. QA retests the fixes and confirms whether the requirements are satisfied.

### PM's Responsibility

The PM should ensure that:

- Requirements are clear and up to date.
- Acceptance criteria are available.
- QA has access to the correct environment.
- Testing dependencies are resolved.
- Known issues are communicated.
- Testing progress and outstanding defects are tracked.

## 2. Testing Types

A PM should understand the main testing types to know what QA is checking, when testing is needed, and what the results mean.

### A. Smoke Testing

Smoke testing checks whether a new application build is stable enough for further testing.

It focuses on essential functionality rather than detailed feature behavior.

**PM perspective:** Confirm that the build is usable enough for QA to begin testing. If basic functions such as login or navigation fail, the team should resolve those problems before continuing.

### B. Functional Testing

Functional testing verifies whether individual features work according to their requirements.

It checks whether the application produces the expected results when users perform specific actions.

Examples include:

- Login works with valid credentials.
- Forms accept valid information.
- Invalid inputs display appropriate errors.
- User permissions are enforced.
- Buttons perform their intended actions.

**PM perspective:** Ensure that QA tests features against their acceptance criteria and reports any behavior that does not match the requirements.

### C. Regression Testing

Regression testing checks whether existing functionality still works after changes are made to the application.

A new feature or bug fix can unintentionally affect other parts of the system.

**PM perspective:** Ensure that important existing functionality is retested after significant changes, especially when features are connected or share the same components.

### D. End-to-End Testing

End-to-end testing verifies whether a complete user workflow works from beginning to end.

For example, an e-commerce purchase workflow may involve:

1. Logging in.
2. Searching for a product.
3. Adding it to the cart.
4. Entering delivery information.
5. Completing payment.
6. Receiving an order confirmation.

**PM perspective:** Identify the product's most important user journeys and ensure they are tested before release. Individual features may work correctly while the complete workflow still fails.

### Comparison of Testing Types

| Testing Type | Main Purpose |
|---|---|
| Smoke | Check whether a build is stable enough for testing. |
| Functional | Verify individual features against requirements. |
| Regression | Ensure existing functionality still works after changes. |
| End-to-End | Verify complete user workflows. |

These testing types complement each other. The testing sequence depends on the project and release process.

## 3. Bug Reporting and Management

### What Is a Bug Report?

A bug report documents a problem found during testing. It gives the development team enough information to understand, reproduce, and fix the issue.

The PM helps ensure that bugs are properly documented, prioritized, assigned, and tracked.

### What Should a Bug Report Include?

A useful bug report should contain:

| Field | Purpose |
|---|---|
| Title | Briefly describes the problem. |
| Description | Explains what is wrong. |
| Steps to reproduce | Shows how to trigger the issue. |
| Expected result | Explains what should happen. |
| Actual result | Explains what actually happened. |
| Evidence | Includes screenshots, recordings, or relevant logs. |
| Environment | Identifies the browser, device, build, and testing environment. |
| Severity | Describes how seriously the bug affects the product. |
| Priority | Determines how urgently the bug should be fixed. |
| Assignee | Identifies who is responsible for investigating or fixing it. |

### Severity vs. Priority

These two fields are related but measure different things.

**Severity** measures the impact of a defect on the product's functionality or user experience.

| Severity | Meaning |
|---|---|
| Critical | Essential functionality is unavailable or the system has a major failure. |
| High | Important functionality is significantly affected. |
| Medium | Functionality is affected, but a workaround may exist. |
| Low | Minor issue with limited impact. |

**Priority** determines how urgently the team should address the bug. It considers business impact, user impact, release deadlines, and other project needs.

| Priority | Meaning |
|---|---|
| Urgent | Requires immediate attention. |
| High | Should be fixed as soon as possible. |
| Medium | Should be addressed in the planned development cycle. |
| Low | Can wait until more important issues are resolved. |

A bug's severity and priority do not always match.

For example, a serious issue in an rarely used internal feature may have high severity but lower immediate priority. A minor visual issue on a page needed for an important client presentation may have low severity but high priority.

### PM's Role in Bug Prioritization

The PM should consider:

- How many users are affected.
- Whether important business functionality is blocked.
- Whether a workaround exists.
- Whether the issue affects revenue or customer experience.
- Whether it blocks other development work.
- Whether it affects an upcoming release or client commitment.

The PM should coordinate with QA, developers, and the Product Owner when deciding which issues need immediate attention.

### Bug Management Workflow

1. QA identifies a defect.
2. QA creates a bug in Jira with clear reproduction steps and evidence.
3. Severity and priority are assessed.
4. PM reviews the business impact and coordinates prioritization.
5. The bug is assigned to a developer.
6. The developer investigates and fixes it.
7. QA retests the fix.
8. The bug is closed if resolved or reopened if the problem remains.

### What Should the PM Track?

- Open critical and high-priority bugs.
- Bugs blocking important features or releases.
- Issues waiting for developer assignment.
- Bugs awaiting retesting.
- Reopened defects.
- Outstanding issues that must be communicated to the client.

The PM should also ensure that unresolved defects are visible to relevant stakeholders before release decisions are made.

## 4. PM Self-Testing

### What Is PM Self-Testing?

PM self-testing is the process of personally checking important features and user workflows before presenting the product to a client or approving it for the next stage.

It is an additional quality check, not a replacement for formal QA testing.

### Why Should a PM Self-Test?

- Identify obvious problems before client demonstrations.
- Verify that important requirements have been implemented.
- Check whether major user journeys work.
- Understand the product's current condition.
- Identify missing functionality or incomplete work.
- Avoid presenting features with known major issues.

### What Should a PM Check?

The PM should focus on important functionality rather than attempting to test every possible scenario.

**1. Authentication**
- Can users log in and log out?
- Does password recovery work?
- Are invalid login attempts handled correctly?

**2. Navigation**
- Do important links and buttons work?
- Do users reach the correct pages?
- Are important sections accessible?

**3. Forms and Data**
- Are required fields validated?
- Are valid inputs accepted?
- Are error and success messages displayed?
- Is submitted information saved correctly?

**4. Main User Workflows**
- Can users complete the product's main activities?
- Does information pass correctly between connected features?
- Does the workflow produce the expected result?

**5. User Interface**
- Are important elements displayed correctly?
- Do images and assets load?
- Does the layout work on relevant screen sizes?
- Are loading, empty, and error states handled?

### PM Self-Testing Process

1. **Review Requirements:** Understand what the feature is expected to do.
2. **Identify Key User Flows:** Select the most important workflows to check.
3. **Use the Application:** Perform the actions as an actual user would.
4. **Compare Results:** Check whether the behavior matches the requirements.
5. **Report Problems:** Create Jira issues or share findings with QA and developers.

### PM Self-Testing vs. QA Testing

| Area | PM Self-Testing | QA Testing |
|---|---|---|
| Purpose | Check readiness for client review or release. | Verify software quality. |
| Focus | Important user flows and overall experience. | Detailed functionality and defect identification. |
| Approach | Basic manual checks. | Structured testing against planned scenarios. |
| Coverage | Selected important features. | Broader planned test coverage. |
| Responsibility | Project Manager | QA Team |
| Output | Readiness feedback and reported issues. | Test results and bug reports. |

### PM Pre-Client Checklist

- [ ] Application opens without major errors.
- [ ] Login and logout work correctly.
- [ ] Main navigation links work.
- [ ] Important buttons perform their intended actions.
- [ ] Forms accept valid information.
- [ ] Invalid inputs display appropriate errors.
- [ ] Important user workflows can be completed.
- [ ] Data is saved and displayed correctly.
- [ ] Images and assets load properly.
- [ ] Layout works on relevant screen sizes.
- [ ] Loading, empty, and error states are handled.
- [ ] Critical and high-priority bugs have been reviewed.

PM self-testing does not guarantee that a feature is defect-free. Formal QA testing must still be completed before the product is considered ready for release.

## How These Practices Work Together

1. **QA Handoff:** The PM ensures QA receives clear requirements, acceptance criteria, test data, and environment details.
2. **Testing:** QA performs the necessary testing to verify functionality and identify defects.
3. **Bug Management:** The PM coordinates prioritization, assignment, tracking, and resolution of reported issues.
4. **PM Self-Testing:** The PM checks important user workflows and confirms that major issues have been addressed before client presentation.

Together, these practices help maintain product quality, reduce delivery risks, and ensure that stakeholders have a clear understanding of the product's readiness.