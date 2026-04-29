# VS Code Agent Mode — Improving a Bad Model

## Overview

This guide walks through using **VS Code Agent Mode (Copilot)** to analyze the bad `SalesFlat` model and systematically improve it for AI/NLP readiness. This is the "practical remediation" portion of the demo.

## Prerequisites

- VS Code with GitHub Copilot and Copilot Chat extensions
- The `SalesFlat.SemanticModel` TMDL files open in VS Code
- Agent Mode enabled (Copilot Chat → switch to Agent mode via the `@` dropdown or the mode selector)

---

## Demo Setup

1. Open VS Code in the `models/bad-model/SalesFlat.SemanticModel/` folder
2. Open the TMDL files so Copilot can see the model structure
3. Switch Copilot Chat to **Agent Mode**

---

## Step-by-Step Agent Mode Walkthrough

### Step 1: Analyze the Current Model

**Prompt to use:**

```
Analyze the TMDL files in this semantic model. This is a Fabric semantic model 
for retail sales data. Identify all issues that would hurt NLP/AI query accuracy, 
including:
- Column naming problems
- Missing descriptions
- Missing measures
- Missing relationships (it's a flat table instead of star schema)
- Missing AI metadata
- Data type issues
- Formatting issues

Give me a prioritized list of improvements needed to make this model AI-ready.
```

**What to show the audience:**
- Copilot analyzes the model and identifies all the problems
- It produces a prioritized list that matches what you've been teaching
- Point out: "This is exactly what we discussed — abbreviated names, no descriptions, no measures, flat table"

---

### Step 2: Add Descriptions to All Columns

**Prompt to use:**

```
Add clear, business-friendly descriptions to every column in the SalesData table. 
The descriptions should explain:
- What the column contains
- How it should be used in reporting
- What the abbreviated name actually means in business terms

For example, "amt" is the net sales amount after discounts, "cust_seg" is the 
customer business segment (Enterprise, Mid-Market, Small Business, Consumer), etc.

Update the TMDL file directly.
```

**What to show the audience:**
- Agent Mode edits the TMDL file directly, adding `///` description comments
- Each column now has business context
- "Even on a bad model, descriptions are the single most impactful improvement"

---

### Step 3: Create Business Measures

**Prompt to use:**

```
Add essential DAX measures to this semantic model for common business questions. 
Create measures for:
1. Total Sales (sum of amt column)
2. Total Cost (sum of cst_amt column)
3. Gross Profit (Total Sales - Total Cost)
4. Profit Margin % (Gross Profit / Total Sales)
5. Total Quantity (sum of qty)
6. Total Discount (sum of disc_amt)
7. Order Count (distinct count of id)
8. Average Order Value (Total Sales / Order Count)

Format currency measures as $#,##0.00 and percentages as 0.0%.
Organize them in display folders: Revenue, Profitability, Discounts.
Update the TMDL file directly.
```

**What to show the audience:**
- Copilot generates proper DAX measures
- Measures are formatted correctly
- Display folders organize the measures logically
- "Now when someone asks 'what were total sales?' there's an explicit measure to use"

---

### Step 4: Rename Columns to Business-Friendly Names

**Prompt to use:**

```
Rename the columns in the SalesData table to use clear, business-friendly names 
instead of the current abbreviated technical names. For example:
- "id" → "Order ID"
- "dt" → "Date"
- "yr" → "Year"  
- "cust_nm" → "Customer Name"
- "prod_cat" → "Product Category"
- "amt" → "Sales Amount"
- "cst_amt" → "Cost Amount"
etc.

Keep the sourceColumn values unchanged (they must match the lakehouse table). 
Only change the TMDL column display names.
Update the TMDL file directly.
```

**What to show the audience:**
- Column names become human-readable
- Source column references stay intact (important for DirectLake)
- "NLP can now understand what 'Product Category' means — it couldn't parse 'prod_cat'"

---

### Step 5: Add Formatting and Data Categories

**Prompt to use:**

```
Update the column properties in the TMDL to add:
1. Proper formatString for currency columns ($#,##0.00)
2. Proper formatString for percentage columns (0.0%)
3. dataCategory annotations where appropriate:
   - City columns → dataCategory: City
   - State columns → dataCategory: StateOrProvince
   - Country columns → dataCategory: Country
4. Set summarizeBy: none for all dimension/attribute columns
5. Set summarizeBy: none for columns that have explicit measures

Update the TMDL file directly.
```

**What to show the audience:**
- Formatting makes the model report-ready
- Data categories enable map visuals and geographic intelligence
- summarizeBy: none prevents accidental implicit aggregation

---

### Step 6: Generate AI Instructions

**Prompt to use:**

```
Generate comprehensive AI Instructions for this retail sales semantic model. 
The instructions should cover:

1. What this model contains (Contoso retail sales data, 2023-2025)
2. Which measures to use for common questions (sales, profit, growth)
3. Business rules (fiscal year = July-June, customer segments, loyalty tiers)
4. How to interpret specific columns
5. Common question patterns and which measures/columns to use
6. Region definitions
7. Product category hierarchy

Format this as a clear, well-structured text that can be pasted into the 
Fabric model's AI Instructions setting.
```

**What to show the audience:**
- Copilot generates comprehensive AI instructions
- These can be directly pasted into Fabric model settings
- "This is the system prompt for your data — it tells Copilot how to interpret your business"

---

### Step 7: Recommend Star Schema Refactoring

**Prompt to use:**

```
This flat table model has significant issues for AI/NLP. Recommend a star schema 
refactoring plan:

1. What dimension tables should be extracted?
2. What should the fact table contain?
3. What relationships should be created?
4. What hierarchies should be defined?

Create new TMDL files for the recommended star schema showing the full model 
structure with tables, relationships, measures, and descriptions. This should 
be a complete, production-ready semantic model definition.
```

**What to show the audience:**
- Agent generates a full star schema design
- New TMDL files for each dimension table
- Relationships file connecting fact to dimensions
- "This is the transformation from 'flat and confused' to 'structured and AI-ready'"

---

## Key Talking Points During Agent Mode Demo

### What Agent Mode Does Well
- Quickly analyzes model structure and identifies gaps
- Generates DAX measures with correct syntax
- Creates comprehensive descriptions from column patterns
- Understands TMDL format and edits files correctly
- Can generate AI instructions from model context

### What Still Requires Human Judgment
- **Business rules**: Agent doesn't know your fiscal year or segment definitions without being told
- **Measure priority**: Which measures matter most to your organization
- **Naming conventions**: What your business calls things vs. technical names
- **Data quality**: Agent can't fix source data issues
- **Validation**: Always review generated DAX for correctness

### The Meta Point
> "Agent Mode is incredibly powerful for accelerating model improvement. But notice — 
> the quality of the output depends entirely on the quality of your prompts. 
> Just like NLP query accuracy depends on your model metadata, Agent Mode 
> accuracy depends on how well you can describe what you need. 
> **Context in, quality out. That's the theme of this entire session.**"

---

## Before & After Summary

| Aspect | Before (Bad Model) | After (Agent-Improved) |
|--------|-------------------|----------------------|
| Column names | `cust_nm`, `prod_cat`, `amt` | Customer Name, Product Category, Sales Amount |
| Descriptions | None | Rich business descriptions on every column |
| Measures | None (raw columns only) | 8+ well-defined DAX measures |
| Formatting | None | Currency, percentage, integer formatting |
| Data categories | None | City, State, Country on geographic columns |
| AI Instructions | None | Comprehensive business context |
| Display folders | None | Revenue, Profitability, Discounts |
| Star schema | Single flat table | Recommended refactoring plan |

---

## Time Estimate for Demo

- Step 1 (Analyze): ~2 minutes
- Step 2 (Descriptions): ~2 minutes
- Step 3 (Measures): ~2 minutes
- Step 4 (Rename): ~2 minutes
- Step 5 (Formatting): ~1 minute
- Step 6 (AI Instructions): ~2 minutes
- Step 7 (Star Schema): ~3 minutes

**Total Agent Mode section: ~15 minutes**

---

## Backup Plan

If Agent Mode is slow or has issues during the live demo:
1. Have the good model TMDL files pre-opened in a separate VS Code window
2. Show the diff between bad and good model files
3. Walk through what Agent Mode would have generated
4. Use the pre-recorded screenshots in the `assets/` folder if available

---

## Part 2: Build a Semantic Model from Scratch — CSV to Star Schema (Using Agent Mode + Modeling MCP Server)

### Overview

This section demonstrates the full end-to-end journey: starting from a **raw CSV file** with denormalized order data and using **VS Code Agent Mode** together with the **Power BI Modeling MCP Server** to create a production-ready, AI-optimized semantic model — entirely from within VS Code.

> **Key message to the audience:** "You don't need to start in the Fabric portal. With Agent Mode and the Modeling MCP server, you can go from a CSV file to a deployed semantic model without ever leaving VS Code."

### Prerequisites

- VS Code with **GitHub Copilot Agent Mode** enabled
- **Power BI Modeling MCP Server** configured in VS Code (provides `model_operations`, `table_operations`, `measure_operations`, `relationship_operations`, etc.)
- The sample CSV file: [`data/sample-orders.csv`](../data/sample-orders.csv)
- A Fabric workspace with a Lakehouse (for eventual deployment)

### What the CSV Contains

The file `data/sample-orders.csv` contains 25 denormalized retail order records with columns spanning orders, customers, products, stores, and promotions — all mashed into a single flat table. This is the typical "data dump" export that analysts receive.

---

### Step 1: Load the CSV and Design a Star Schema

**Goal:** Have Agent Mode analyze the raw CSV and generate a complete star schema design with proper dimension and fact tables.

**Prompt to use:**

```
I have a retail orders CSV file at data/sample-orders.csv. Analyze its structure 
and design a proper star schema semantic model from it.

Specifically:
1. Read the CSV file and understand all the columns and data
2. Design a star schema with:
   - A central Fact table (Sales/Orders) containing only keys, quantities, and amounts
   - A Calendar/Date dimension extracted from the order dates
   - A Customer dimension (name, email, city, state, region, segment, loyalty tier)
   - A Product dimension (name, category, subcategory, brand)
   - A Store dimension (name, city, state, region, type)
   - A Promotion dimension (name, category, discount percent)
3. Create surrogate keys (integer keys) for each dimension
4. Define the relationships between fact and dimension tables

Output the full star schema design as a set of TMDL files in a new folder 
called models/csv-demo/RetailAnalytics.SemanticModel/definition/. Include 
model.tmdl, relationships.tmdl, expressions.tmdl, and a tables/ folder with 
one file per table.

Use DirectLake partition mode pointing to a lakehouse. Use 'DatabaseQuery' 
as the expression source name.
```

**What to show the audience:**
- Agent Mode reads and understands the CSV structure
- It identifies which columns belong to which dimension
- It creates surrogate keys and maps the relationships
- It generates a full set of TMDL files — a complete semantic model from a CSV
- "We went from a flat CSV to a star schema design in under a minute"

---

### Step 2: Optimize the Schema for Performance

**Goal:** Refactor the generated semantic model for production readiness — schema-level changes only (no measures, no descriptions yet).

**Prompt to use:**

```
Review the semantic model TMDL files in models/csv-demo/RetailAnalytics.SemanticModel/definition/ 
and optimize the schema for performance and AI/NLP readiness. Make ONLY structural 
schema changes — do not add measures or descriptions yet.

Specifically:
1. Ensure all dimension key columns have summarizeBy: none
2. Ensure all foreign key columns in the fact table have summarizeBy: none and are hidden (isHidden: true)
3. Set the Calendar table's dataCategory to Time and mark the Date column as isKey: true
4. Add sortByColumn where needed (e.g., Month Name sorted by Month Number)
5. Add proper data types — ensure dates are dateTime, amounts are double/decimal, keys are int64
6. Add geographic dataCategory tags: City, StateOrProvince, Country on the appropriate columns
7. Add formatString for currency columns ($#,##0.00) and percentage columns (0.0%)
8. Create hierarchies:
   - Product: Category → Subcategory → Product Name
   - Customer Geography: Region → State → City
   - Store Geography: Region → State → City → Store Name
   - Calendar: Year → Quarter → Month → Date
9. Verify all relationships are correct (many-to-one from fact to dimensions, single direction)

Update the TMDL files directly. Only make schema and structural changes in this step.
```

**What to show the audience:**
- Agent Mode makes targeted structural improvements across all TMDL files
- Keys are hidden, dimensions are tagged, hierarchies are created
- "These are the changes that make the AI engine actually understand your model structure — hidden keys mean Copilot won't try to aggregate them, data categories enable geo features, hierarchies give AI a drill path"
- "Notice we're being disciplined — schema first, then clarity, then measures. Each layer builds on the last."

---

### Step 3: Improve Model Clarity and Reduce Ambiguity

**Goal:** Add business-friendly names and comprehensive descriptions to make the model interpretable by both humans and AI.

**Prompt to use:**

```
Improve the clarity and reduce ambiguity in the semantic model at 
models/csv-demo/RetailAnalytics.SemanticModel/definition/.

1. RENAME columns to clear, business-friendly names where needed:
   - Remove underscores and abbreviations (e.g., "cust_city" → "City", "discount_pct" → "Discount Percent")
   - Use natural language names that an NLP engine can parse
   - Keep sourceColumn values unchanged — only rename the TMDL display names

2. ADD DESCRIPTIONS to every table explaining:
   - What the table represents
   - How it should be used in analysis
   - For the fact table: emphasize using measures instead of raw columns

3. ADD DESCRIPTIONS to every column explaining:
   - What the column contains in business terms
   - Valid values or ranges where relevant (e.g., "Customer segments: Enterprise, Mid-Market, Small Business, Consumer")
   - How the column relates to common business questions
   - For geographic columns: mention the data category

4. ADD DESCRIPTIONS to all hierarchies explaining the drill path

Update the TMDL files directly. Make the model self-documenting — if a new 
analyst or an AI system reads only the metadata, they should fully understand 
the model without any external documentation.
```

**What to show the audience:**
- Every table and column gets a rich, business-friendly description
- Column names become human-readable
- "This is the single most impactful change for NLP accuracy. Descriptions are what Copilot reads to understand your data. Think of it as writing a data dictionary directly into your model."
- "Notice the principle: a new analyst should understand the model just from the metadata. If a human can understand it, AI can too."

---

### Step 4: Enrich the Model with Key Business Metrics

**Goal:** Add a comprehensive set of DAX measures that a business analyst would need for day-to-day reporting and executive dashboards.

**Prompt to use:**

```
Enrich the semantic model at models/csv-demo/RetailAnalytics.SemanticModel/definition/ 
with a comprehensive set of DAX measures. Think like a business analyst building 
an executive dashboard for a retail company — what measures would you need to answer 
the CEO's questions?

Create measures in these categories and organize them in display folders:

📊 Revenue & Volume (display folder: "Revenue")
- Total Sales (net revenue after discounts)
- Total Quantity (units sold)  
- Order Count (distinct orders)
- Average Order Value (revenue per order)
- Average Selling Price (revenue per unit)

💰 Profitability (display folder: "Profitability")
- Total Cost (cost of goods sold)
- Gross Profit (sales minus cost)
- Profit Margin % (gross profit as % of sales)
- Average Profit Per Order

🏷️ Discounts & Promotions (display folder: "Discounts")
- Total Discount Amount
- Discount Rate % (discount as % of gross revenue)
- Orders with Promotion (count of orders that had a promotion)
- Promotion Penetration % (% of orders with promotions)

📅 Time Intelligence (display folder: "Time Intelligence")  
- Total Sales SPLY (same period last year using SAMEPERIODLASTYEAR)
- YoY Growth % (year-over-year percentage change)
- Sales MTD (month-to-date running total)
- Sales YTD (year-to-date running total)

👥 Customer Metrics (display folder: "Customer")
- Customer Count (distinct customers)
- Revenue Per Customer (average spend per customer)
- New vs Returning Customer Count (if trackable)

Each measure MUST have:
- A clear description explaining what it calculates and when to use it
- Proper formatString ($#,##0.00 for currency, 0.0% for percentages, #,##0 for counts)
- A lineageTag (generate unique GUIDs)

Add all measures to the Sales (fact) table. Update the TMDL files directly.
```

**What to show the audience:**
- Agent Mode creates 20+ production-ready measures across 5 categories
- Each measure has a description that doubles as AI guidance
- Display folders keep the model organized
- "Without these measures, every question is ambiguous. With them, 'what were total sales?' has exactly one answer — the Total Sales measure."
- "Notice we asked Agent Mode to think like a business analyst — the prompt context directly shapes the quality of the output. This is the same principle as AI Instructions for Copilot: context in, quality out."

---

### Wrap-Up: The Full Journey

> **PRESENTER:**
>
> "Let's recap what we just did, entirely from within VS Code:"
>
> | Step | What We Did | Why It Matters |
> |------|-------------|----------------|
> | **Step 1** | Designed star schema from CSV | Eliminates ambiguity — every concept has one home |
> | **Step 2** | Optimized schema structure | Hidden keys, data categories, hierarchies enable AI features |
> | **Step 3** | Added names & descriptions | The #1 factor in NLP accuracy — AI reads your metadata |
> | **Step 4** | Added business measures | Removes aggregation guesswork — explicit answers to common questions |
>
> "We started with a flat CSV file and ended with a production-ready, AI-optimized semantic model — complete with star schema, hierarchies, descriptions, and 20+ measures. No portal, no Power BI Desktop, no manual edits."
>
> "From here, you could deploy this to Fabric with a single command using the Modeling MCP server's `DeployToFabric` operation, add AI Instructions and synonyms, and immediately start getting accurate Copilot answers."
>
> "**That's the power of Agent Mode + MCP: the entire semantic modeling workflow, from data to deployment, in one tool.**"

### Time Estimate

- Step 1 (Star Schema Design): ~3 minutes
- Step 2 (Schema Optimization): ~2 minutes
- Step 3 (Names & Descriptions): ~3 minutes
- Step 4 (Business Measures): ~3 minutes

**Total CSV-to-Model section: ~12 minutes**
