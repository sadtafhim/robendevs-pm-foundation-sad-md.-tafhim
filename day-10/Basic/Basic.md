# Product Metrics, Event Tracking, Data Quality, and Power BI Basics

These topics explain how businesses measure product performance, track user activity, maintain reliable data, and create reports to support business decisions.

## 1. Product Metrics: Active Users, Conversion, Retention, and Churn

### What Are Product Metrics?

Product metrics are measurements used to evaluate how well a product is performing.

They help businesses understand user engagement, measure growth, identify problems, and determine whether product changes are achieving their intended results.

### A. Active Users

Active users measure the number of unique users who interact with a product during a specific period.

Common measurements include:

- **DAU (Daily Active Users):** Unique users who actively use the product in one day.
- **WAU (Weekly Active Users):** Unique users who actively use the product in one week.
- **MAU (Monthly Active Users):** Unique users who actively use the product in one month.

For example, if 5,000 unique users perform meaningful activities on a platform during a month, its MAU is 5,000.

Active users help businesses understand how many people regularly use their product. If registrations increase but active users decrease, it may indicate that new users are not finding enough value to continue using the product.

The team must also define what counts as an active user. Simply opening an application may not represent meaningful engagement.

### B. Conversion Rate

Conversion rate measures the percentage of users who complete a desired action.

A conversion depends on the product's business objectives. It could include:

- Completing registration.
- Purchasing a product.
- Subscribing to a paid plan.
- Booking an appointment.
- Completing a form.

**Formula:**

Conversion Rate = (Number of Conversions / Total Eligible Users) × 100

For example, if 100 out of 1,000 website visitors make a purchase, the conversion rate is 10%.

Conversion rate helps businesses understand how effectively a product encourages users to complete important actions.

A low conversion rate may indicate problems with the user experience, pricing, checkout process, product information, or technical performance.

### C. Retention Rate

Retention measures the percentage of users who continue using a product over a specific period.

For example, if 1,000 users register in January and 400 of them return in February, the retention rate is 40%.

**Formula:**

Retention Rate = (Returning Users / Original Users) × 100

Retention helps businesses understand whether users find the product valuable enough to continue using it.

Low retention may indicate problems with onboarding, product usefulness, user experience, or feature quality.

### D. Churn Rate

Churn rate measures the percentage of customers or users who stop using a product or service during a specific period.

It is particularly important for subscription-based businesses.

**Formula:**

Churn Rate = (Customers Lost During Period / Customers at Start of Period) × 100

For example, if a service starts the month with 1,000 customers and 50 cancel their subscriptions, the monthly churn rate is 5%.

A high churn rate may indicate:

- Poor user experience.
- Lack of useful features.
- High subscription costs.
- Technical problems.
- Better alternatives from competitors.
- Poor customer support.

Businesses monitor churn to understand why customers leave and identify ways to improve retention.

### Understanding the Four Metrics

| Metric | What It Measures |
|---|---|
| Active Users | How many people use the product. |
| Conversion | How many users complete a desired action. |
| Retention | How many users continue using the product. |
| Churn | How many users stop using the product. |

Together, these metrics provide a broader understanding of product performance.

For example, a product may have many active users but a low conversion rate. This suggests that people are using the product but not completing important business actions.

Similarly, a product may attract many new users but have high churn, indicating that users are not staying for long.

## 2. Event Tracking: Analytics Events and Feature Instrumentation

### What Is Event Tracking?

Event tracking is the process of recording specific actions performed by users while interacting with a digital product.

These recorded actions are called **events**.

Examples include:

- User signed up.
- User logged in.
- Button clicked.
- Product viewed.
- Item added to cart.
- Payment completed.
- Subscription cancelled.
- File downloaded.

Event tracking helps businesses understand what users actually do inside a product rather than only measuring how many people visit it.

### A. What Is an Analytics Event?

An analytics event is a recorded user action or system activity that provides information about product usage.

An event commonly contains:

- **Event Name:** Identifies what happened, such as `user_signed_up` or `purchase_completed`.
- **User ID:** Identifies the user who performed the action, when available and appropriate.
- **Timestamp:** Records when the event occurred.
- **Event Properties:** Additional details that provide context about the action.

For example, a `purchase_completed` event may contain:

- Order ID.
- Product ID.
- Purchase amount.
- Currency.
- Payment method.

These details help businesses understand not only how many purchases happened but also what was purchased and how much revenue was generated.

### B. What Is Feature Instrumentation?

Feature instrumentation is the process of adding tracking functionality to a product so that important user interactions generate analytics events.

Developers implement tracking code in the relevant parts of the application.

For example, a registration feature may track:

1. Registration page viewed.
2. Registration form submitted.
3. Registration completed.
4. Registration failed.

Each action generates a separate event.

This allows businesses to understand how users move through the registration process and identify where they encounter problems.

### C. How Event Tracking Works

Event tracking generally involves four steps:

1. **Identify important actions:** Decide which user interactions are important to measure based on product goals.
2. **Define events and properties:** Establish consistent event names and determine what information each event should contain.
3. **Implement tracking:** Developers add tracking functionality to the relevant parts of the application.
4. **Collect and analyse events:** An analytics platform collects the events and presents the information through reports and dashboards.

### D. Why Event Tracking Matters

Event tracking helps businesses:

- Measure feature usage.
- Understand user journeys.
- Identify where users abandon processes.
- Analyse conversion funnels.
- Evaluate newly released features.
- Detect technical problems through failure events.

For example, if many users open a checkout page but few complete their purchases, event data can help identify where users are leaving the process.

Event tracking must be implemented correctly. Duplicate events, missing properties, inconsistent naming, and incorrect tracking can produce misleading reports.

## 3. Data Quality: Completeness, Accuracy, Consistency, and Timeliness

### What Is Data Quality?

Data quality refers to how reliable, correct, and useful collected information is.

Businesses use data to prepare reports, measure performance, understand customers, and make decisions. However, collected data is not automatically reliable.

It may contain missing information, incorrect values, inconsistent formats, or outdated records.

Four important dimensions of data quality are completeness, accuracy, consistency, and timeliness.

### A. Completeness

Completeness refers to whether all required information is available in a dataset.

Data is incomplete when important fields or records are missing.

For example, a customer database may contain a customer name and ID but have no email address, even though email is required for communication.

**How to maintain completeness:**

- Identify mandatory fields.
- Validate required information during data entry.
- Monitor missing values.
- Ensure important events are recorded.
- Check that data collection processes capture all required information.

### B. Accuracy

Accuracy refers to whether information correctly represents the actual situation.

Data is inaccurate when it contains incorrect or misleading values.

For example, recording a transaction as $500 instead of $50 would create inaccurate financial reports.

**How to maintain accuracy:**

- Validate data before accepting it.
- Use appropriate formats and restrictions.
- Check information against reliable sources.
- Identify unusual or unrealistic values.
- Correct errors when they are discovered.

Accuracy is especially important for financial reporting, customer records, and business decisions.

### C. Consistency

Consistency refers to whether information follows the same standards and formats across records, systems, and reports.

Data becomes inconsistent when the same information is represented differently.

For example, a country might be recorded as:

- Bangladesh
- BD
- BGD
- bangladesh

Although these values refer to the same country, using different formats can create problems when filtering or analysing data.

**How to maintain consistency:**

- Establish standard data formats.
- Use common naming conventions.
- Maintain consistent measurement units.
- Apply the same rules across systems.
- Avoid duplicate records.
- Ensure reports use the same definitions.

### D. Timeliness

Timeliness refers to whether data is available and updated when it is needed.

Data becomes outdated when it is not refreshed frequently enough.

For example, an inventory system that does not update stock quantities after purchases may display incorrect product availability.

**How to maintain timeliness:**

- Define how frequently data should be updated.
- Automate data synchronization where possible.
- Monitor delays in data collection.
- Establish regular reporting schedules.
- Ensure important information is available when required.

### Comparing the Four Dimensions

| Dimension | Main Question | Common Problem |
|---|---|---|
| Completeness | Is all required data available? | Missing information |
| Accuracy | Is the information correct? | Incorrect values |
| Consistency | Does the data follow the same standards? | Different formats |
| Timeliness | Is the data up to date? | Outdated information |

### Why Data Quality Matters

Poor data quality can lead to incorrect reports and poor business decisions.

For example:

- Missing transactions create a completeness problem.
- Incorrect sales amounts create an accuracy problem.
- Different currency formats create a consistency problem.
- Delayed transaction updates create a timeliness problem.

Maintaining data quality helps businesses produce reliable reports and make informed decisions.

## 4. Power BI Basics: Connecting Data Sources, Building Tables, and Creating Charts

### What Is Power BI?

Microsoft Power BI is a business intelligence and data visualization platform used to collect, organize, analyse, and present data through interactive reports and dashboards.

It helps businesses turn raw data into information that is easier to understand.

Common uses include:

- Business performance reporting.
- Sales and revenue analysis.
- Customer behaviour analysis.
- Project performance monitoring.
- Financial reporting.
- Operational dashboards.

### A. Connecting a Data Source

A data source is where the information used in a report comes from.

Common data sources include:

- Excel spreadsheets.
- CSV files.
- SQL databases.
- SharePoint.
- Web-based sources.
- Cloud services.

**How to connect a data source:**

1. Open Power BI Desktop.
2. Select **Get Data**.
3. Choose a source, such as Excel or CSV.
4. Select the file or provide connection details.
5. Preview the available data.
6. Select the required tables or sheets.
7. Choose **Load** to import the data.

Once imported, the data becomes available for creating reports and visualizations.

### What Is Power Query?

Power Query is a data preparation tool built into Power BI.

It allows users to clean and transform data before using it in reports.

Common operations include:

- Removing duplicate records.
- Removing unnecessary columns.
- Renaming columns.
- Changing data types.
- Filtering rows.
- Replacing missing or incorrect values.
- Combining data from different sources.

For example, Power Query can remove duplicate transactions and unnecessary columns from a sales spreadsheet before it is used in a report.

### B. Building Tables

A table displays information using rows and columns.

Each row represents a record, while each column represents a particular type of information.

For example, a sales table might contain:

| Order ID | Product | Quantity | Revenue |
|---|---|---|---|
| 101 | Laptop | 2 | $2,000 |
| 102 | Mouse | 5 | $100 |
| 103 | Keyboard | 3 | $150 |

**How to build a table in Power BI:**

1. Open a report in Power BI Desktop.
2. Select the **Table visual** from the Visualizations panel.
3. Select the fields you want to display.
4. Add the fields to the table.
5. Arrange the columns in the required order.
6. Adjust column widths and formatting.

Tables are useful when users need to inspect detailed records, such as individual transactions, customer information, or product details.

### C. Creating Bar Charts

A bar chart compares numerical values across different categories.

Each bar represents a category, and its length represents the corresponding value.

For example, a business might compare sales across product categories.

| Product | Sales |
|---|---:|
| Laptops | 500 |
| Phones | 800 |
| Tablets | 300 |
| Accessories | 600 |

**How to create a bar chart in Power BI:**

1. Select the **Clustered Bar Chart** visual.
2. Add a category field to the Y-axis.
3. Add a numerical field, such as sales, to the X-axis.
4. Adjust the sorting if necessary.
5. Customize the title, labels, and appearance.

Bar charts are useful for:

- Comparing sales across products.
- Comparing revenue across departments.
- Comparing customers across regions.
- Identifying the highest and lowest performing categories.

They are best suited for comparing separate categories.

### D. Creating Line Charts

A line chart shows how numerical values change over time.

It displays data points connected by lines, making it easier to identify trends and patterns.

For example, a business might monitor monthly revenue.

| Month | Revenue |
|---|---:|
| January | $2,000 |
| February | $2,500 |
| March | $2,200 |
| April | $3,000 |
| May | $3,500 |

**How to create a line chart in Power BI:**

1. Select the **Line Chart** visual.
2. Add a date or time field to the X-axis.
3. Add a numerical field, such as revenue, to the Y-axis.
4. Ensure the dates are displayed in the correct order.
5. Customize the title, labels, and formatting.

Line charts are useful for:

- Monitoring monthly revenue.
- Tracking active users over time.
- Measuring website traffic.
- Monitoring customer growth.
- Identifying seasonal patterns.

They are best suited for showing changes and trends over time.

### E. Understanding Different Visualizations

| Visualization | Main Purpose | Best Used For |
|---|---|---|
| Table | Displaying detailed records | Reviewing individual transactions |
| Bar Chart | Comparing categories | Comparing product sales |
| Line Chart | Showing changes over time | Tracking monthly revenue |

Choosing the correct visualization makes reports easier to understand.

For example, a bar chart is suitable for comparing sales across product categories, while a line chart is more suitable for tracking monthly sales trends.

### F. Building a Basic Power BI Report

After connecting a data source and creating visualizations, users can combine them into a single report.

A basic sales report might contain:

- **Total Revenue:** Overall sales revenue.
- **Total Orders:** Number of completed orders.
- **Revenue by Product:** A bar chart comparing product sales.
- **Monthly Revenue Trend:** A line chart showing changes in revenue over time.

Power BI reports can also include filters and slicers, allowing users to view information for specific dates, products, departments, or regions.

Power BI helps businesses:

- Analyse large amounts of data.
- Identify trends and patterns.
- Compare business performance.
- Monitor important metrics.
- Present information through visual reports.
- Share insights with stakeholders.