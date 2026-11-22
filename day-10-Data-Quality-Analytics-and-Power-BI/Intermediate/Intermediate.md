
# Funnels, Cohorts, Power Query, Dashboard Design, and Analytics Tracking Requirements

These topics explain how businesses analyse user behaviour, prepare data, create dashboards, and define which user activities should be tracked during product development.

## 1. Funnels and Cohorts

### A. Funnels

A funnel tracks the steps users take to complete a process. It helps identify where users abandon the process and measures conversion between stages.

**Example: E-commerce Funnel**

| Stage | Users |
|---|---:|
| Visited website | 1,000 |
| Viewed product | 700 |
| Added to cart | 400 |
| Started checkout | 250 |
| Completed purchase | 150 |

Overall conversion rate = (150 / 1,000) × 100 = 15%.

### B. Funnel Drop-Off

Drop-off refers to users who leave a process without completing the next step.

Funnel analysis helps businesses:
- Identify where users abandon a process.
- Measure conversion rates.
- Find problems in registration, onboarding, and checkout.
- Improve user journeys.

### C. Cohorts

A cohort is a group of users who share a common characteristic or experience within a specific period.

Common cohort types:
- **Acquisition Cohorts:** Group users by when or how they joined.
- **Behavioural Cohorts:** Group users by actions they performed.
- **Retention Cohorts:** Track how many users continue using a product over time.

**Example: Retention Cohort**

| Registration Cohort | Month 0 | Month 1 | Month 2 |
|---|---:|---:|---:|
| January | 100% | 60% | 40% |
| February | 100% | 70% | 50% |
| March | 100% | 75% | 55% |

This shows what percentage of each registration group remained active over time.

### D. Funnels vs. Cohorts

| Funnels | Cohorts |
|---|---|
| Track users through a sequence of steps. | Group users by shared characteristics. |
| Identify where users drop off. | Analyse behaviour over time. |
| Focus on conversion. | Focus on retention and engagement. |

## 2. Power Query: Cleaning and Shaping Data

### A. What Is Power Query?

Power Query is a data preparation tool in Power BI and Excel. It helps clean, organize, and transform raw data before analysis.

### B. Common Data Cleaning Operations

1. **Remove Duplicates:** Eliminate repeated records.
2. **Remove Columns:** Remove unnecessary information.
3. **Handle Missing Values:** Replace, remove, or retain missing data depending on the requirements.
4. **Change Data Types:** Ensure columns use the correct formats, such as text, numbers, and dates.
5. **Rename Columns:** Replace unclear column names with understandable labels.
6. **Filter Rows:** Keep only records that meet specific conditions.
7. **Split or Merge Columns:** Separate or combine information.

### C. Data Shaping

Data shaping means changing the structure of data to make it suitable for analysis.

Common operations:
- **Merge:** Combine tables using a shared column.
- **Append:** Combine rows from multiple tables.
- **Pivot:** Convert row values into columns.
- **Unpivot:** Convert columns into rows.
- **Group:** Organize records based on common values.

### D. Power Query Workflow in Power BI

1. Connect to a data source such as Excel, CSV, or a database.
2. Open Power Query Editor using Transform Data.
3. Clean the data by removing duplicates and correcting formats.
4. Shape the data by filtering, merging, or appending tables.
5. Select Close & Apply to load the prepared data.
6. Use the data to build reports and dashboards.

**Why It Matters:** Power Query improves data quality, reduces manual work, and allows saved transformation steps to run again when data is refreshed.

## 3. Dashboard Design

### A. What Is a Dashboard?

A dashboard is a visual display of important business information and performance metrics in one place.

Common elements include:
- Charts and graphs.
- KPI cards.
- Tables.
- Filters.
- Summary metrics.

### B. Choosing the Right Chart

| Visualization | Purpose |
|---|---|
| Bar Chart | Compare values across categories. |
| Line Chart | Show trends and changes over time. |
| Pie/Donut Chart | Show proportions of a whole. |
| Table/Matrix | Display detailed information. |
| KPI Card | Highlight important metrics such as revenue or conversion rate. |

### C. Dashboard Design Principles

1. **Prioritize Important Information:** Make key metrics easy to find.
2. **Use a Clear Layout:** Place summary metrics first, followed by charts and detailed information.
3. **Avoid Unnecessary Charts:** Include only visualizations that serve a purpose.
4. **Use Consistent Colours:** Maintain consistent colour meanings.
5. **Use Clear Labels:** Give charts descriptive titles, labels, and units.
6. **Use Filters Carefully:** Allow users to filter by dates, categories, or regions.
7. **Maintain Consistency:** Use consistent fonts, spacing, and alignment.

**What Makes a Good Dashboard?**

A good dashboard presents relevant information clearly, makes important metrics easy to understand, and helps users identify trends and performance problems without overwhelming them.

## 4. Analytics Tracking Requirements in a PRD

### A. What Are Tracking Requirements?

Tracking requirements define which user actions should be recorded for analytics purposes.

They specify:
- What should be tracked.
- When an event should trigger.
- What information should be collected.
- Why the event is important.

These requirements are documented in the Product Requirements Document (PRD).

### B. What Is an Analytics Event?

An analytics event is a recorded user action or system activity.

Examples:
- `user_registered`
- `product_viewed`
- `checkout_started`
- `payment_completed`

Tracking requirements help ensure developers implement the necessary analytics and QA can verify that events work correctly.

### C. What Should a Tracking Requirement Include?

1. **Event Name:** A unique, consistently formatted name.
2. **Description:** Explains what the event represents.
3. **Trigger Condition:** Defines exactly when the event should be recorded.
4. **Event Properties:** Additional information collected, such as user ID, product ID, amount, or timestamp.
5. **User Identification:** Defines how the associated user is identified.
6. **Expected Behaviour:** Specifies rules such as preventing duplicate events and excluding sensitive information.

### D. Example: Registration Tracking

**Feature:** User Registration

**Objective:** Measure registration attempts and successful account creation.

| Event Name | Trigger | Properties |
|---|---|---|
| `registration_page_viewed` | Registration page is displayed. | Page name, timestamp |
| `registration_form_submitted` | User submits the form. | Form type, timestamp |
| `registration_completed` | Account is successfully created. | User ID, registration method |
| `registration_failed` | Registration fails. | Error category, registration method |

These requirements tell developers what to implement and QA what to verify.

### E. PM/BA Responsibilities

1. **Understand the Feature:** Identify important user actions and business measurement goals.
2. **Identify Events:** Decide which actions need tracking.
3. **Define Event Details:** Specify names, triggers, and properties.
4. **Update the PRD:** Document tracking requirements alongside functional requirements.
5. **Coordinate with Developers:** Clarify implementation expectations.
6. **Coordinate with QA:** Verify events, properties, and duplicate prevention.
7. **Verify After Release:** Confirm events are received correctly in the analytics platform.

### F. Functional vs. Analytics Tracking Requirements
Functional requirements ensure the feature works, while tracking requirements ensure its usage can be measured.

| Functional Requirements | Analytics Tracking Requirements |
|---|---|
| Define what a feature should do. | Define what user actions should be recorded. |
| Focus on product functionality. | Focus on collecting behavioural data. |
| Verified through functional testing. | Verified through event tracking tests. |

**Example:**
- Functional: Users must be able to submit a registration form.
- Tracking: The system must record `registration_form_submitted` whenever a user submits the form.