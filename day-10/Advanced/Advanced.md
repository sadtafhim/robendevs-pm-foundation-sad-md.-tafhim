
# DAX Basics, Data Modelling in Power BI, and Data-Driven Decision Making

These topics explain how to calculate business metrics, organize data, and use analytics to make informed product decisions.

## 1. DAX Basics: Calculated Columns and Measures

### A. What Is DAX?

DAX (Data Analysis Expressions) is a formula language used in Power BI to calculate metrics, analyse data, and create custom business calculations.

Common uses include calculating revenue, profit, averages, customer counts, and conversion rates.

### B. Calculated Columns

A calculated column creates a new column using a DAX formula. It calculates and stores a value for each row.

Example:
```dax
Total Sales = Sales[Quantity] * Sales[Unit Price]
```

**Uses:**
- Creating new values from existing columns.
- Categorizing records.
- Creating labels and classifications.
- Supporting filtering and grouping.

### C. Measures

A measure is a DAX calculation that summarizes data. Its result is calculated when needed based on the filters applied in a report.

Common examples:

```dax
Total Revenue = SUM(Sales[Revenue])

Total Orders = COUNTROWS(Sales)

Average Revenue = AVERAGE(Sales[Revenue])

Total Customers = DISTINCTCOUNT(Sales[CustomerID])
```

Measures are commonly used for KPIs, totals, averages, and dashboard calculations.

### D. Calculated Columns vs. Measures

| Calculated Columns | Measures |
|---|---|
| Calculate values for individual rows. | Calculate summarized results. |
| Results are stored in the data model. | Results are calculated when needed. |
| Useful for filtering and grouping. | Useful for totals and KPIs. |
| Use row context. | Use filter context. |

**Remember:**
- Calculated column = Value for each record.
- Measure = Result for the selected data.

### E. Filter Context

Filter context refers to the filters that determine which data a measure uses.

For example, selecting a particular month or product automatically changes the measure's result.

## 2. Data Modelling in Power BI

### A. What Is Data Modelling?

Data modelling is the process of organizing data into tables and creating relationships between them.

It allows Power BI to combine information from multiple tables for analysis.

### B. Primary Keys and Foreign Keys

- **Primary Key (PK):** A column that uniquely identifies each record in a table.
- **Foreign Key (FK):** A column that references the primary key of another table.

These keys establish relationships between tables.

### C. Types of Relationships

1. **One-to-Many (1:*):** One record in a table can relate to multiple records in another table. Example: One customer can have multiple orders.

2. **One-to-One (1:1):** Each record in one table relates to exactly one record in another table.

3. **Many-to-Many (*:*):** Multiple records in one table can relate to multiple records in another table. A bridge table is often used to manage this relationship.

### D. Cardinality

Cardinality defines how records in two tables relate to each other, such as one-to-one, one-to-many, or many-to-many.

Choosing the correct cardinality helps prevent inaccurate calculations and filtering problems.

### E. Star Schema

A star schema is a common Power BI data modelling structure consisting of:

- **Fact Tables:** Contain measurable transactions and activities, such as sales, revenue, and quantities.
- **Dimension Tables:** Contain descriptive information, such as customers, products, dates, and locations.

Dimension tables connect to the fact table through matching keys.

### F. Creating Relationships in Power BI

1. Import the required tables.
2. Open Model View.
3. Identify matching columns.
4. Connect the related columns.
5. Select the correct relationship type.
6. Verify that the relationships work correctly.

**Why Data Modelling Matters:**
- Connects information from multiple tables.
- Reduces unnecessary duplication.
- Improves calculation accuracy.
- Creates organized and reliable reports.

## 3. Data-Driven Decision Making

### A. What Is Data-Driven Decision Making?

It is the process of using data, analysis, and measurable evidence to make business or product decisions instead of relying entirely on assumptions.

### B. What Is a Dashboard Insight?

A dashboard insight is a meaningful finding discovered through data analysis.

Examples include:
- Decreasing active users.
- Increasing customer churn.
- Low feature usage.
- Declining conversion rates.
- High user drop-off.

Insights help teams identify problems and opportunities.

### C. Turning Insights into Product Recommendations

1. **Identify the Problem:** Find an issue through dashboard metrics.
2. **Investigate the Data:** Examine trends, user behaviour, and possible causes.
3. **Identify the Cause:** Determine what might be contributing to the problem.
4. **Recommend a Solution:** Suggest a specific product improvement.
5. **Define Expected Outcomes:** Identify what should improve.
6. **Prioritize:** Evaluate business impact, development effort, and cost.
7. **Measure Results:** Compare metrics before and after implementation.

### D. What Makes a Good Product Recommendation?

- **Evidence-Based:** Supported by data or user feedback.
- **Specific:** Clearly explains what should change.
- **Measurable:** Includes metrics to evaluate success.
- **Realistic:** Considers time, resources, and technical limitations.
- **Business-Focused:** Supports objectives such as improving retention or increasing conversion.

### E. Common Mistakes

- Making decisions based on a single metric.
- Assuming correlation means causation.
- Ignoring user feedback.
- Using inaccurate or incomplete data.
- Making recommendations without measurable outcomes.
- Ignoring implementation costs and effort.

## 4. How These Topics Work Together

1. **Data Modelling:** Organizes tables and establishes relationships.
2. **DAX:** Calculates business metrics.
3. **Dashboard Analysis:** Presents metrics and identifies insights.
4. **Product Recommendations:** Turns insights into improvements and measures their results.

**Overall Goal:** Turn raw data into meaningful insights and use those insights to make informed product and business decisions.
