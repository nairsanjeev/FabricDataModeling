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
