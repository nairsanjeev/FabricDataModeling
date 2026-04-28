# NLP Test Questions — Side-by-Side Comparison

## Overview

Ask these same questions against **both** models to demonstrate the impact of proper data modeling, metadata, and AI instructions on NLP accuracy.

For each question, first ask the **Bad Model (SalesFlat)**, then ask the **Good Model (Contoso Retail Analytics)**.

---

## Question 1: Basic Revenue

**Ask:** _"What were total sales last year?"_

### Bad Model Expected Behavior
- **Problem**: No "Total Sales" measure exists. Model has columns `amt`, `unit_px`, `cst_amt` — which one is "sales"?
- **Likely Result**: May sum `amt` but could also try `unit_px`. No clear year definition. No date intelligence.
- **Issues**: Ambiguous column names, no measures, no date table marking

### Good Model Expected Behavior
- **Result**: Uses `[Total Sales]` measure filtered to last calendar year via `Calendar[Year]`
- **Why it works**: Explicit measure + AI instructions saying "use Total Sales for revenue questions" + proper date table

---

## Question 2: Profitability

**Ask:** _"Which product category is most profitable?"_

### Bad Model Expected Behavior
- **Problem**: No "profit" concept exists. Columns are `amt` and `cst_amt` — AI doesn't know to subtract them
- **Likely Result**: May show `amt` by `prod_cat`, which is revenue not profit. Or may fail entirely.
- **Issues**: No calculated measures, no profit definition, abbreviated column names

### Good Model Expected Behavior
- **Result**: Shows `[Gross Profit]` or `[Profit Margin %]` by `Product[Category]`, sorted descending
- **Why it works**: Profit measures are defined, AI instructions explain what "profitable" means

---

## Question 3: Regional Analysis

**Ask:** _"Show me sales by region for Q4"_

### Bad Model Expected Behavior
- **Problem**: Two "region" columns exist: `cust_region` and `store_region`. Which one? And "Q4" maps to `qtr` column but without a date table there's no context.
- **Likely Result**: May use wrong region column. May filter incorrectly on quarter.
- **Issues**: Duplicate/ambiguous dimension columns in flat table, no clear region concept

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]` by `Store[Region]` filtered to `Calendar[Quarter] = "Q4"`
- **Why it works**: Clear relationships, single Region column per dimension, proper quarter handling

---

## Question 4: Customer Intelligence

**Ask:** _"Who are our top 10 customers by revenue?"_

### Bad Model Expected Behavior
- **Problem**: Column is `cust_nm`. "Revenue" maps to... `amt`? `unit_px`? The flat table has duplicate customer rows.
- **Likely Result**: May show random customers or incorrect sums due to row duplication in flat table.
- **Issues**: Denormalized data causes double-counting, no clear revenue measure

### Good Model Expected Behavior
- **Result**: Shows top 10 `Customer[Customer Name]` by `[Total Sales]`, correctly aggregated
- **Why it works**: Star schema eliminates duplication, Revenue synonym maps to Total Sales

---

## Question 5: Year-over-Year Growth

**Ask:** _"What's the year-over-year growth?"_

### Bad Model Expected Behavior
- **Problem**: No YoY measure exists. No date table. No time intelligence. AI would need to calculate this from scratch on a flat table.
- **Likely Result**: Likely fails or returns nonsensical results. May try to compute growth but without SAMEPERIODLASTYEAR pattern.
- **Issues**: No time intelligence measures, no date table, no SAMEPERIODLASTYEAR capability

### Good Model Expected Behavior
- **Result**: Returns `[YoY Growth %]` showing percentage growth
- **Why it works**: Pre-built time intelligence measure + synonym mapping for "YoY"

---

## Question 6: Weekend Analysis

**Ask:** _"How do weekend sales compare to weekday sales?"_

### Bad Model Expected Behavior
- **Problem**: Column `is_wknd` contains 0/1 but there's no label. AI doesn't know what 0 and 1 mean. Column name "is_wknd" is cryptic.
- **Likely Result**: May show 0 and 1 values without meaning. May not understand "weekend" maps to this column at all.
- **Issues**: Abbreviated column name, no description, no semantic meaning for flag values

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]` split by `Calendar[Is Weekend]` with clear 1=Weekend/0=Weekday distinction
- **Why it works**: Column description explains the values, synonym maps "weekend" to the column

---

## Question 7: Promotion Impact

**Ask:** _"What's the average discount by promotion?"_

### Bad Model Expected Behavior
- **Problem**: Columns `disc_amt`, `disc_pct`, `promo_nm` — which discount metric? Average of the percentage or the dollar amount?
- **Likely Result**: May average `disc_pct` (the static promo percent) per row rather than calculating actual average discount given.
- **Issues**: Ambiguous column names, duplicate promo data across rows in flat table

### Good Model Expected Behavior
- **Result**: Shows average `DiscountAmount` or `[Total Discount]` by `Promotion[Promotion Name]`
- **Why it works**: Clear measure, clear dimension, AI instructions clarify discount concepts

---

## Question 8: Store Performance

**Ask:** _"Which store has the highest profit margin?"_

### Bad Model Expected Behavior
- **Problem**: No profit margin concept exists. Would need to calculate (amt - cst_amt) / amt per store. Column `store_nm` exists but on a flat table this means lots of row scanning.
- **Likely Result**: Likely fails. May try to do something with `amt` only.
- **Issues**: No profit margin measure, no star schema for efficient store-level aggregation

### Good Model Expected Behavior
- **Result**: Shows `[Profit Margin %]` by `Store[Store Name]`, sorted descending
- **Why it works**: Measure exists, store dimension is clean, AI instructions define "profit margin"

---

## Question 9: Trend Analysis

**Ask:** _"Show monthly revenue trend for the last 2 years"_

### Bad Model Expected Behavior
- **Problem**: Month column is `mo` (text), year is `yr`. No proper date hierarchy. No sort order. "Revenue" is ambiguous.
- **Likely Result**: May show months in alphabetical order (April, August, December...) instead of chronological. Revenue calculation unclear.
- **Issues**: No sort-by-column, no date hierarchy, text month names sort wrong

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]` by `Calendar[Month Year]` properly sorted chronologically for 2024-2025
- **Why it works**: Month sorted by MonthNumber, Month Year sorted by YearMonth, proper date hierarchy

---

## Question 10: Segment Revenue

**Ask:** _"What's revenue per customer segment?"_

### Bad Model Expected Behavior
- **Problem**: `cust_seg` is an abbreviated column name. "Revenue" maps to `amt` (maybe?). Segment values exist but joined to every row.
- **Likely Result**: May work partially but with wrong aggregation or wrong column. "cust_seg" might not be recognized as "customer segment".
- **Issues**: Abbreviated names block NLP understanding, no synonym mapping

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]` and/or `[Revenue Per Customer]` by `Customer[Segment]`
- **Why it works**: Synonyms map "customer segment" → `Segment`, "revenue" → `Total Sales`

---

## Question 11: Fiscal Year Analysis

**Ask:** _"How did we perform in FY2025?"_

### Bad Model Expected Behavior
- **Problem**: `fy` column exists but NLP may not connect "FY2025" to `fy`. No AI instructions explain fiscal year meaning.
- **Likely Result**: May not understand what FY2025 means or may filter wrong dates.
- **Issues**: No fiscal year context, abbreviated column name

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]`, `[Gross Profit]`, `[Profit Margin %]` filtered to `Calendar[Fiscal Year] = "FY2025"`
- **Why it works**: AI instructions define fiscal year periods, column is clearly named, synonyms recognize "FY"

---

## Question 12: Multi-Dimension Analysis

**Ask:** _"Compare Electronics vs Clothing sales by region for Platinum customers"_

### Bad Model Expected Behavior
- **Problem**: Complex multi-filter question. Columns `prod_cat`, `cust_region` or `store_region` (?), `cust_loyalty` — severe ambiguity on every dimension.
- **Likely Result**: Likely fails or produces wrong results. Too many ambiguous columns.
- **Issues**: Flat table with duplicated dimensions, ambiguous region, ambiguous aggregation

### Good Model Expected Behavior
- **Result**: Shows `[Total Sales]` by `Product[Category]` (filtered to Electronics, Clothing) by `Store[Region]`, filtered to `Customer[Loyalty Tier] = "Platinum"`
- **Why it works**: Clear dimensions with relationships, AI instructions define loyalty tiers, synonyms work

---

## Summary Scoring

| Question | Bad Model | Good Model |
|----------|-----------|------------|
| 1. Total sales last year | ⚠️ Partial/wrong | ✅ Correct |
| 2. Most profitable category | ❌ Fails | ✅ Correct |
| 3. Sales by region Q4 | ⚠️ Ambiguous | ✅ Correct |
| 4. Top 10 customers | ⚠️ Duplicated | ✅ Correct |
| 5. YoY growth | ❌ Fails | ✅ Correct |
| 6. Weekend vs weekday | ⚠️ Cryptic | ✅ Correct |
| 7. Avg discount by promo | ⚠️ Confused | ✅ Correct |
| 8. Best store by margin | ❌ Fails | ✅ Correct |
| 9. Monthly revenue trend | ⚠️ Wrong sort | ✅ Correct |
| 10. Revenue per segment | ⚠️ Partial | ✅ Correct |
| 11. FY2025 performance | ⚠️ Wrong filter | ✅ Correct |
| 12. Multi-dim analysis | ❌ Fails | ✅ Correct |

**Bad Model: 0 correct, 5 partial, 4 fails**
**Good Model: 12 correct**

---

## Demo Tips

1. **Screen split**: Open both models side by side in Fabric portal
2. **Ask the same question**: Type the identical question in both Q&A/Copilot panels
3. **Pause on failures**: Let the audience see the bad model struggle before showing the good one
4. **Show the "why"**: After each comparison, briefly explain which metadata element made the difference
5. **Build momentum**: Start with easy questions (1-3) and build to harder ones (10-12)
