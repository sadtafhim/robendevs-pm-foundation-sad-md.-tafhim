# Release Readiness, Test Coverage, and Post-Release Support

These activities help a Project Manager prepare software for deployment, ensure important scenarios have been tested, and coordinate support after release.

The PM's responsibility is to coordinate developers, QA, support teams, and stakeholders to reduce release risks and ensure a smooth transition to production.

## 1. Release Readiness

### What Is Release Readiness?

Release readiness is the process of confirming that a product or feature is ready for production deployment.

Before release, the team should verify that development is complete, required testing has passed, critical bugs are resolved, and necessary approvals have been received.

### Go-Live Checklist

A go-live checklist identifies the tasks and conditions that must be completed before deployment.

The PM should coordinate the checklist and confirm that the responsible team members have completed their tasks.

**1. Development**
- Planned features are implemented.
- Development tasks are completed.
- Code reviews and required approvals are complete.
- Integrations are configured.

**2. Testing**
- Required functional and regression testing is complete.
- Critical bugs are resolved.
- Important test cases have passed.
- UAT is completed and approved.

**3. Client Approval**
- The client has reviewed the final version.
- Release scope is confirmed.
- Outstanding issues are communicated.
- Required approvals are recorded.

**4. Deployment Preparation**
- Production environment is configured.
- Deployment instructions are prepared.
- Database changes are reviewed.
- Required configurations and credentials are ready.
- Deployment responsibilities are assigned.

**5. Backup and Recovery**
- Required backups are available.
- Rollback procedures are documented.
- Recovery responsibilities are assigned.
- The team understands how to respond if deployment fails.

**6. Communication**
- Release date and time are confirmed.
- Stakeholders are informed.
- Users are notified when necessary.
- Support teams are prepared.

### What Is a Rollback Plan?

A rollback plan defines how the team will return to a previous stable version if a new release causes serious problems.

It helps the team recover quickly instead of making decisions under pressure.

### What Should a Rollback Plan Include?

**1. Rollback Conditions**

Define the situations that would require a rollback, such as:

- Critical functionality stops working.
- Users cannot log in.
- Payment processing fails.
- The application becomes unstable.
- Data integrity is affected.
- Performance drops significantly.

**2. Rollback Procedure**

Document how the technical team will restore the previous stable version.

This may involve:
- Reverting to a previous application build.
- Restoring previous configurations.
- Reversing or addressing database changes.
- Disabling a problematic feature.
- Restoring data from backups when necessary.

Database changes require special attention because reverting application code alone may not restore the previous data structure or state.

**3. Responsibilities**

Define who approves and performs the rollback. The PM coordinates the response, while the technical team handles the technical execution.

**4. Communication**

Determine how clients, stakeholders, and users will be informed if a rollback is necessary.

**5. Recovery Verification**

After rollback, the technical team must verify that the previous version is working correctly and important functionality has been restored.

### Post-Deployment Monitoring

Post-deployment monitoring involves checking the application after release to identify problems that may not have appeared during testing.

The team should monitor:

| Area | What to Check |
|---|---|
| Application performance | Loading times and response times. |
| Error rates | Application errors and failed requests. |
| Server health | CPU, memory, storage, and resource usage. |
| Database | Connection problems and failed queries. |
| User activity | Login failures and transaction problems. |
| Integrations | Whether external services and APIs are working. |

Monitoring is generally handled through technical tools, dashboards, logs, and alerts.

### PM's Responsibilities

The PM coordinates release readiness by:

- Maintaining the go-live checklist.
- Confirming testing and approvals are complete.
- Coordinating deployment schedules.
- Ensuring rollback procedures are documented.
- Confirming technical responsibilities are assigned.
- Communicating release information to stakeholders.
- Tracking deployment progress.
- Coordinating responses to post-release problems.

The PM does not need to perform the technical deployment or rollback but must ensure that the responsible engineers are prepared.

## 2. Test Coverage

### What Is Test Coverage?

Test coverage measures how much of the product's requirements, functionality, and supported usage conditions have been tested.

Testing only the main functionality is not enough. A feature might work on one browser but fail on another, or work for an administrator but fail for a regular user.

The PM should ensure that QA considers the different environments, user roles, and scenarios relevant to the product.

### Why Is Test Coverage Important?

Proper test coverage helps:

- Identify missing test scenarios.
- Reduce the risk of production defects.
- Verify functionality across supported environments.
- Check permissions for different user roles.
- Identify problems caused by unusual inputs.
- Improve confidence before release.

### 1. Device Coverage

Device coverage ensures that the product works across the devices it is designed to support.

Depending on the product, testing may include:

- Desktop computers.
- Laptops.
- Tablets.
- Smartphones.

QA should verify:

- Layout and alignment.
- Navigation and menus.
- Buttons and forms.
- Text readability.
- Image scaling.
- Touch interactions.
- Responsive behavior.

The PM should confirm which devices and screen sizes the product officially supports.

### 2. Browser Coverage

Browser coverage ensures that a web application works correctly across supported browsers.

Common browsers include Chrome, Firefox, Edge, and Safari.

QA should check:

- Page rendering and layout.
- Navigation and routing.
- Form submissions.
- JavaScript functionality.
- File uploads and downloads.
- Authentication.
- Browser-specific issues.

The PM should ensure that testing covers the browsers and versions included in the product's support requirements.

### 3. Role-Based Coverage

Role-based coverage verifies that different user types have the correct permissions and access.

For example:

| User Role | Expected Access |
|---|---|
| Admin | Can manage users, settings, and system data. |
| Manager | Can view reports and manage assigned operations. |
| Regular User | Can access standard application features. |
| Guest | Can access public information only. |

QA should verify that:

- Users can access the features allowed by their roles.
- Restricted pages cannot be accessed without permission.
- Users cannot perform unauthorised actions.
- Role-specific information is displayed correctly.
- Administrative functions are protected.

This is particularly important for applications that handle sensitive information or business operations.

### 4. Edge Case Testing

Edge cases are unusual or extreme situations that may cause unexpected behavior.

QA should consider scenarios such as:

- Submitting forms with missing information.
- Entering extremely long text.
- Uploading unsupported file formats.
- Entering negative or unusually large numbers.
- Submitting duplicate information.
- Losing internet connectivity during an operation.
- Refreshing a page during a transaction.
- Clicking a submit button multiple times.
- Entering values at minimum or maximum limits.

The goal is to ensure that the application handles unusual situations safely instead of crashing or producing incorrect results.

### Measuring Test Coverage

Test coverage can be measured by comparing requirements against the requirements that have corresponding test cases.

For example, if a feature has 20 acceptance criteria and test cases cover 18 of them:

\[
\text{Requirement Coverage} =
\frac{\text{Covered Requirements}}{\text{Total Requirements}} \times 100
\]

\[
= \frac{18}{20} \times 100 = 90\%
\]

<badge color="success">90% coverage</badge>

This means 90% of the defined requirements have test coverage.

However, 100% requirement coverage does not guarantee that software is bug-free. It only measures whether requirements have been covered, not how effectively they have been tested.

### PM's Responsibilities

The PM coordinates with QA to ensure that testing covers the necessary environments and user scenarios.

Their responsibilities include:

- Confirming supported devices and browsers.
- Ensuring important user roles are tested.
- Checking that acceptance criteria have test coverage.
- Ensuring relevant edge cases are considered.
- Tracking test execution progress.
- Identifying gaps in testing.
- Communicating testing risks before release.

## 3. Post-Release Support

### What Is Post-Release Support?

Post-release support involves monitoring and maintaining the application after it has been deployed to production.

Even after QA and UAT are completed, real-world usage may reveal unexpected problems, integration failures, or performance issues.

The PM coordinates the teams responsible for identifying, prioritising, and resolving these problems.

### What Is a Hypercare Period?

Hypercare is a temporary period of increased support immediately after a software release.

During this period, developers, QA, and support teams closely monitor the application and respond quickly to reported problems.

It helps ensure that the product remains stable while users begin using the new release.

Hypercare may last a few days or several weeks, depending on the complexity and risk of the release.

### What Happens During Hypercare?

**1. Increased Monitoring**

The team closely monitors application performance, errors, integrations, and important business operations.

**2. Faster Issue Resolution**

Reported problems receive quicker attention, especially when they affect critical functionality.

**3. User Support**

The support team helps users understand new functionality and resolve problems.

**4. Regular Status Updates**

The PM coordinates updates between developers, QA, support teams, and clients.

**5. Stability Verification**

The team confirms that important functionality works correctly and that no critical unresolved issues remain.

### What Is Incident Handling?

Incident handling is the process of identifying, reporting, investigating, resolving, and documenting problems affecting a live application.

Examples include:

- Users being unable to log in.
- Payment transactions failing.
- Application pages not loading.
- Database connection failures.
- External integrations becoming unavailable.
- Unexpected application crashes.
- Significant performance degradation.

### Incident Handling Process

**1. Incident Identification**

An issue is identified through user reports, monitoring alerts, support tickets, or internal observations.

**2. Incident Logging**

The issue is recorded in an incident management system.

A useful incident record includes:
- Incident title and description.
- Time reported.
- Affected functionality.
- Number of affected users.
- Relevant screenshots or logs.
- Current status.

**3. Incident Classification**

The team evaluates the incident based on its impact and urgency.

| Severity | Description | Response |
|---|---|---|
| Critical | Major outage or serious business disruption. | Immediate attention. |
| High | Important functionality is unavailable or severely affected. | Urgent investigation. |
| Medium | Limited functionality is affected, but a workaround exists. | Scheduled resolution. |
| Low | Minor issue with limited impact. | Normal support process. |

Response targets should follow the organisation's incident management policy.

**4. Incident Assignment**

Assign the incident to the appropriate developer, support engineer, or technical team.

**5. Investigation and Resolution**

The technical team investigates the cause and applies a fix or workaround.

**6. Verification**

QA or the relevant technical team confirms that the issue has been resolved.

**7. Closure and Documentation**

The incident is closed after verification. The team records what happened, how it was resolved, and whether preventive action is needed.

### Client Communication During Post-Release Support

The PM should keep the client informed about the product's condition, reported problems, resolution progress, and any actions required from their side.

Communication should be clear, accurate, and based on confirmed information.

**What Should Be Communicated?**

- **Release Confirmation:** Confirm when deployment is complete, including the release version and deployment time.
- **Reported Issues:** Inform the client about significant problems affecting the product.
- **Resolution Progress:** Explain what is being investigated, what has been resolved, and what remains outstanding.
- **Expected Resolution Time:** Share estimates only when confirmed by the technical team.
- **Workarounds:** Explain temporary solutions when a permanent fix is not immediately available.
- **Final Confirmation:** Notify the client when an issue is resolved and the affected functionality has been verified.

### PM's Responsibilities

The PM coordinates post-release support by:

- Organising the hypercare period.
- Coordinating developers, QA, and support teams.
- Tracking incident reports and progress.
- Ensuring incidents are prioritised correctly.
- Communicating significant issues to clients.
- Tracking resolution timelines.
- Coordinating retesting after fixes.
- Preparing post-release status updates.
- Ensuring unresolved issues are documented and handed over.

Once the hypercare period ends and the application is stable, responsibility can transition to the regular maintenance or support team.

## How These Activities Work Together

1. **Release Readiness:** The team confirms that development, testing, approvals, deployment preparation, and recovery procedures are complete.
2. **Test Coverage:** QA verifies that the product has been tested across supported devices, browsers, user roles, and relevant edge cases.
3. **Post-Release Support:** After deployment, the team monitors the application, handles incidents, supports users, and communicates with the client.
