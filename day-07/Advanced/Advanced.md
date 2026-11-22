# Release Planning, Velocity, and Risk Planning

## 1. Release Planning

Release planning determines which features, improvements, and bug fixes will be included in a software release and when they are expected to be delivered.

### Versions and Releases

A version identifies a specific state of a software product. A common format is **Major.Minor.Patch** (e.g., `2.4.1`).

- **Major:** Significant changes or new functionality.
- **Minor:** New features and improvements.
- **Patch:** Bug fixes and small corrections.

In Jira, issues can be assigned to a release using the **Fix Version** field. This helps teams track which tasks must be completed for each release.

### Milestones

A milestone is an important checkpoint that represents progress towards a project goal.

Examples include:
- Design completion.
- Development completion.
- Testing completion.
- Client approval.
- Production deployment.

Milestones track project progress, while releases represent product versions delivered to users.

### Roadmaps

A roadmap provides a high-level view of planned features, milestones, and delivery timelines.

Jira roadmaps can help teams:
- Organise work across multiple epics.
- Track planned dates and progress.
- Identify dependencies.
- Monitor upcoming releases.

Release dates should be based on realistic estimates and updated when priorities, scope, or timelines change. Roadmap dates are forecasts, not guaranteed deadlines.

## 2. Velocity

Velocity measures how much work a team completes during a sprint, usually using story points.

It helps teams forecast future delivery based on previous sprint performance.

### Calculating Velocity

Velocity is the total story points of completed work in a sprint.

**Formula:**

\[
\text{Velocity} = \text{Total Completed Story Points}
\]

For example, if a team completes 20, 24, 22, and 26 points across four sprints:

\[
\text{Average Velocity} = \frac{20+24+22+26}{4}=23
\]

The team's average velocity is 23 points per sprint.

### Forecasting Delivery

Velocity can estimate how many sprints are needed to complete the remaining work.

**Formula:**

\[
\text{Estimated Sprints} = \frac{\text{Remaining Story Points}}{\text{Average Velocity}}
\]

For example, if 115 points remain and the average velocity is 23:

\[
\frac{115}{23}=5 \text{ sprints}
\]

With two-week sprints, the estimated duration is 10 weeks.

### Using Velocity with Clients

Project managers can use historical velocity to explain expected delivery timelines.

Forecasts should be reviewed when team capacity, project scope, technical complexity, or dependencies change.

**Important considerations:**
- Count only work that meets the Definition of Done.
- Velocity measures completed work, not hours worked.
- Each team's velocity is different and should not be compared across teams.
- Use several sprints to establish a reliable average.
- Velocity is a forecasting tool, not a measure of individual performance.

## 3. Risk Planning

Risk planning identifies potential problems that could affect project scope, timeline, budget, or quality. It also defines actions to reduce their impact.

### Identifying Risks

Common types of project risks include:

- **Technical:** Complex integrations, unfamiliar technologies, or performance issues.
- **Requirements:** Unclear specifications, missing acceptance criteria, or changing requirements.
- **Resources:** Staff unavailability or insufficient technical expertise.
- **External:** Delayed approvals, third-party outages, or external API changes.

### Risk Assessment

Each risk should be evaluated based on:

- **Likelihood:** How likely it is to happen.
- **Impact:** How seriously it could affect the project.

High-likelihood and high-impact risks should receive priority.

Teams should document each risk, assign an owner, and define how it will be handled.

### Buffers

A buffer is additional time or capacity reserved for unexpected work or delays.

Common types include:

- **Time Buffer:** Extra time in the project schedule.
- **Sprint Capacity Buffer:** Uncommitted capacity for unexpected tasks.
- **Release Buffer:** Additional time for final testing, bug fixes, and deployment.

Buffers should be based on actual project risks rather than added randomly.

### Spikes

A spike is a time-limited research task used to investigate something the team does not fully understand.

Spikes are useful when:
- An API or technology is unfamiliar.
- Technical requirements are unclear.
- Multiple implementation approaches exist.
- A task cannot be estimated confidently.

The outcome should be useful information, a recommendation, or a proof of concept. This helps the team estimate and plan the actual development work more accurately.

### Risk Register

A risk register records and tracks identified project risks.

It typically includes:

- **Risk ID:** Unique identifier.
- **Description:** Explanation of the potential problem.
- **Likelihood and Impact:** Assessment of the risk.
- **Priority:** Overall risk level.
- **Owner:** Person responsible for monitoring it.
- **Mitigation Plan:** Actions to reduce the risk.
- **Status:** Current state of the risk.

The register should be reviewed regularly as new risks may appear during development.

### Mitigation and Contingency Planning

- **Risk Mitigation:** Actions taken to reduce the likelihood or impact of a risk.
- **Contingency Planning:** An alternative plan to follow if the risk actually occurs.

For example, testing an external API early is mitigation. Having an alternative integration approach ready is contingency planning.

## 4. How These Activities Work Together

- **Release Planning:** Defines what will be delivered and when.
- **Velocity:** Uses past sprint performance to forecast delivery timelines.
- **Risk Planning:** Identifies uncertainties and prepares responses to potential problems.
