# AI Instructions Reference — Contoso Retail Analytics

## Overview

AI Instructions are a critical feature in Microsoft Fabric semantic models that guide Copilot and NLP systems in interpreting business questions correctly. They act as a **"system prompt" for your data model**.

Below are the AI instructions to configure in the **Contoso Retail Analytics** semantic model.

---

## How to Set AI Instructions in Fabric

1. Open the semantic model in the Fabric portal
2. Click the **Settings** gear icon (or go to Model settings)
3. Navigate to **AI Instructions** (under the Q&A / Copilot section)
4. Paste the instructions below
5. Click **Save**

Alternatively, in the model view:
1. Click **Manage AI Instructions** from the ribbon
2. Paste and save

---

## AI Instructions Content

Copy and paste the following into your model's AI Instructions:

---

### About This Model

This semantic model contains retail sales data for **Contoso**, a multi-category retail company with 10 stores across the United States. The data covers the period from January 2023 to December 2025.

### Key Business Rules

- **Revenue/Sales**: Always use the `[Total Sales]` measure when answering questions about sales, revenue, income, or turnover. Do NOT sum the `SalesAmount` column directly.
- **Profitability**: Use `[Gross Profit]` for profit questions and `[Profit Margin %]` for margin/profitability percentage questions. Gross Profit = Total Sales - Total Cost.
- **Year-over-Year**: Use `[YoY Growth %]` for growth comparisons. This compares the current period to the same period in the prior year.
- **Discounts**: Use `[Total Discount]` for discount amounts and `[Discount Rate]` for the percentage of revenue given as discounts.
- **Customer metrics**: Use `[Customer Count]` for unique customer counts and `[Revenue Per Customer]` for per-customer revenue.

### Fiscal Calendar

Contoso's fiscal year runs from **July 1 to June 30**. For example:
- FY2025 = July 1, 2024 through June 30, 2025
- FQ1 = July - September
- FQ2 = October - December
- FQ3 = January - March
- FQ4 = April - June

When users ask about "this year" or "last year" without specifying fiscal or calendar, **default to calendar year** unless they specifically mention "fiscal year" or "FY".

### Customer Segments

Customers are classified into four segments:
- **Enterprise**: Large corporations with high-volume purchasing
- **Mid-Market**: Medium-sized businesses
- **Small Business**: Small companies and sole proprietors
- **Consumer**: Individual retail buyers

### Loyalty Program

Customer loyalty tiers from highest to lowest:
- **Platinum**: Top-tier customers, highest spending and engagement
- **Gold**: High-value customers with consistent purchasing
- **Silver**: Regular customers with moderate activity
- **Bronze**: Entry-level loyalty members or infrequent buyers

### Store Types

- **Flagship**: Largest stores with the full product line (NYC)
- **Premium**: Upscale locations in major markets (LA, Seattle, Miami)
- **Standard**: Typical retail stores in regional markets
- **Outlet**: Discount/clearance locations with lower price points (Atlanta)

### Geographic Regions

Stores and customers are organized into these sales regions:
- **Northeast**: New York, Boston, Philadelphia
- **South**: Houston, Dallas, Nashville, Charlotte, Atlanta, Miami, San Antonio
- **Midwest**: Chicago, Minneapolis, Detroit
- **West**: Los Angeles, Phoenix, Denver
- **Pacific**: Seattle, Portland, San Francisco

### Product Categories

Products are organized into 5 main categories:
1. **Electronics**: Laptops, Phones, Accessories
2. **Clothing**: Tops, Bottoms, Outerwear
3. **Home & Garden**: Kitchen, Furniture, Garden
4. **Sports & Outdoors**: Fitness, Outdoor, Team Sports
5. **Food & Beverage**: Coffee & Tea, Snacks, Specialty

### Important Relationships

- The **Calendar** table is the date dimension — always use it for date filtering
- Each sale links to exactly one Product, Customer, Store, and Promotion
- A Promotion of "No Promotion" (Key=0) means the sale was at regular price
- About 70% of sales have no promotion applied

### Common Question Patterns

- "Top products" → Sort by `[Total Sales]` descending, show `Product Name` or `Category`
- "Most profitable" → Use `[Gross Profit]` or `[Profit Margin %]`
- "Best stores" → Use `[Total Sales]` by `Store Name` or `Region`
- "Customer analysis" → Use `[Customer Count]`, `[Revenue Per Customer]` by `Segment`
- "Sales trend" → Use `[Total Sales]` over `Calendar[Month Year]` or `Calendar[Year]`
- "Weekend vs weekday" → Filter by `Calendar[Is Weekend]` where 1=Weekend, 0=Weekday
- "Discount impact" → Use `[Total Discount]` and `[Discount Rate]` by `Promotion Name`

---

## Why AI Instructions Matter

Without AI Instructions, the NLP engine must:
1. **Guess** which column or measure to use for "sales"
2. **Assume** what "profit" means (revenue? margin? net income?)
3. **Default** to arbitrary aggregations
4. **Misinterpret** business-specific terminology

With AI Instructions:
1. Every business term maps to a **specific measure**
2. Business rules are **explicitly documented**
3. Common questions have **predefined patterns**
4. Domain-specific terms (fiscal year, loyalty tier) are **clearly defined**

This is the difference between AI that **sometimes works** and AI you can **trust and scale**.
