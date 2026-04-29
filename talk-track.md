# Demo Talk Track — Data Modeling for AI-Ready Semantic Models in Microsoft Fabric

## Session Overview

**Title:** From "AI Sometimes Works" to "AI We Can Trust and Scale"
**Duration:** ~60 minutes (adjustable to 45 or 90)
**Format:** Live demo with talk track

---

## Pre-Demo Checklist

- [ ] Fabric workspace open with both semantic models deployed
- [ ] Lakehouse with sample data generated
- [ ] `SalesFlat` (bad model) accessible in Fabric portal
- [ ] `Contoso Retail Analytics` (good model) accessible in Fabric portal
- [ ] VS Code open with bad model TMDL files
- [ ] Copilot/Agent Mode ready in VS Code
- [ ] Two browser tabs: one for each model's Q&A/Copilot view
- [ ] This talk track open on a secondary screen or printed
- [ ] Backup screenshots prepared in case of connectivity issues

---

## PART 1: SETTING THE STAGE (5 minutes)

### Slide / Opening

> **PRESENTER:**
>
> "How many of you have tried asking natural language questions against your data in Fabric or Power BI — and gotten answers that were... let's say... *creative*?"
>
> [Pause for audience reaction]
>
> "You're not alone. Most teams hit a wall where AI produces answers that are technically *a number*, but not a *trusted* number. Today, we're going to look at exactly **why** that happens and **what to do about it**."
>
> "Here's the thing that most people don't realize: **AI is only as good as the semantic model behind it**. The most advanced AI in the world cannot give you a reliable answer if it doesn't understand your data. And 'understanding your data' means a lot more than just connecting to a table."
>
> "Today we're going to see this firsthand. We have two semantic models built on the exact same data — same products, same customers, same transactions. One is modeled the way most teams do it when they're moving fast. The other is modeled the way you need to do it when you want AI you can trust."
>
> "Let's see the difference."

---

## PART 2: THE BAD MODEL — "What Most Teams Build" (10 minutes)

### Show the Bad Model Structure

> **PRESENTER:**
>
> [Navigate to the SalesFlat model in Fabric portal → Model view]
>
> "Here's our first model. It's called 'SalesFlat.' Let's look at the structure."
>
> "What do you see? One table. `SalesData`. 33 columns. Everything jammed into a single flat, denormalized table."
>
> [Click on the table to show columns]
>
> "Look at these column names: `amt`, `cst_amt`, `disc_pct`, `cust_nm`, `prod_cat`, `is_wknd`, `qtr`. Can you tell me right now — what does `amt` mean? Is it sales amount? Order amount? List price amount? What currency? Before or after discounts?"
>
> [Pause]
>
> "And that's just the naming. Notice there are **no descriptions** on any column. No measures defined. No relationships — because everything is in one table. No hierarchies. No formatting."
>
> "This is what I call a 'data dump' model. It works for SQL queries where you write the logic yourself. But it's terrible for AI, because AI has to **infer** everything that's missing."
>
> "Let's see what happens when we ask questions."

### Live NLP Testing — Bad Model

> **PRESENTER:**
>
> [Open Q&A or Copilot for the SalesFlat model]

#### Question 1: "What were total sales last year?"

> "Let's start simple. 'What were total sales last year?'"
>
> [Type the question and wait for response]
>
> "Look at this. [Describe what happened — likely summed `amt` but maybe picked the wrong column. Or it picked a random year. Or it returned a count instead of a sum.]"
>
> "The model has no measure called 'Total Sales.' It has a column called `amt`. AI has to guess: should I SUM it? AVERAGE it? COUNT it? And 'last year' — is that calendar year? Fiscal year? The model doesn't have a marked date table, so the AI is guessing on that too."

#### Question 2: "Which product category is most profitable?"

> "Let's try something harder. 'Which product category is most profitable?'"
>
> [Type the question and wait]
>
> "And here's where it really breaks down. There is no concept of 'profit' in this model. There's `amt` and `cst_amt`, but no measure that calculates profit. The AI would need to figure out on its own that profit = amt - cst_amt. That's a lot to ask."
>
> [Show the result — likely wrong or fails]

#### Question 3: "Show me sales by region for Q4"

> "'Show me sales by region for Q4.'"
>
> [Type and wait]
>
> "Now we have a fun problem. This flat table has TWO region columns: `cust_region` and `store_region`. Which one does 'region' mean? The AI has to guess. And `qtr` — is that the right column for Q4? What year? Q4 of when?"
>
> "See how the ambiguity compounds? Each unclear column adds uncertainty, and when you stack multiple ambiguities in one question, the confidence collapses."

#### Question 4: "How do weekend sales compare to weekday sales?"

> "'How do weekend sales compare to weekday sales?'"
>
> [Type and wait]
>
> "The column is called `is_wknd`. Values are 0 and 1. Does the AI know that 1 means weekend? Does it know to split on this column? The column name `is_wknd` doesn't scream 'weekend flag' to an NLP engine."

### The Verdict

> "So out of four questions, how many did we get reliable, trustworthy answers for?"
>
> [Pause]
>
> "Probably zero. Maybe one partially correct. This is common and leads to frustration. But is it the AI's fault? **No.** The AI is doing its best with what we gave it. We gave it a soup of abbreviated columns with no context. What did we expect?"
>
> "Let me show you what happens when we do this right."

---

## PART 3: THE GOOD MODEL — "What AI Actually Needs" (15 minutes)

### Show the Good Model Structure

> **PRESENTER:**
>
> [Navigate to the Contoso Retail Analytics model in Fabric portal → Model view]
>
> "Here's our second model. Same data. Same products, customers, stores, and transactions. But look at the structure."
>
> [Show the model diagram]
>
> "We have a **star schema**: a central `Sales` fact table connected to five dimension tables — `Calendar`, `Product`, `Customer`, `Store`, and `Promotion`. Each table has a single, clear purpose."
>
> "Let's look at the differences."

### Walk Through Key Improvements

#### 1. Column Names & Descriptions

> [Click on the Product table]
>
> "Look at the column names: `Product Name`, `Category`, `Subcategory`, `Brand`. Not `prod_nm` or `prod_cat`. Business-friendly, human-readable names."
>
> [Hover over a column to show the description]
>
> "And every single column has a **description**. The Category column says: *'The top-level product grouping. Categories include: Electronics, Clothing, Home & Garden, Sports & Outdoors, and Food & Beverage.'*"
>
> "When Copilot gets a question about 'product categories,' it now knows exactly which column to use AND what values exist. No more guessing."

#### 2. Measures

> [Click on the Sales table and expand the measures]
>
> "We have **14 well-defined measures** organized in display folders:"
>
> "**Revenue:** Total Sales, Total Quantity, Average Order Value, Order Count"
> "**Profitability:** Total Cost, Gross Profit, Profit Margin %"
> "**Discounts:** Total Discount, Discount Rate"
> "**Time Intelligence:** Total Sales SPLY, YoY Growth %"
> "**Customer:** Customer Count, Revenue Per Customer"
>
> "Each measure has a description explaining exactly what it calculates and when to use it. The Total Sales description says: *'Total Sales represents the total net revenue across all transactions. This is the primary revenue measure and should be used whenever someone asks about sales, revenue, or income.'*"
>
> "That description is not just for humans — **Copilot reads that too**."

#### 3. Relationships & Hierarchies

> [Show the model diagram with relationship lines]
>
> "The star schema means every question is unambiguous. When someone says 'region,' the AI looks at the Store table's Region column — there's only one Region per dimension table. No confusion."
>
> [Show a hierarchy]
>
> "We have hierarchies like Category → Subcategory → Product Name. And Country → Region → State → City. These tell the AI how to drill down and at what level to answer."

#### 4. Calendar/Date Table

> [Click on Calendar table]
>
> "The Calendar table is marked as the **Date table**. It has proper month sorting (Month sorts by Month Number, not alphabetically). It has fiscal year support (FY runs July to June). It has an Is Weekend flag with clear documentation."
>
> "This is the foundation for time intelligence. Without a proper date table, there is no 'last year,' no 'Q4,' no 'year-over-year.' The AI simply cannot answer time-based questions without this."

#### 5. AI Instructions

> [Go to Model settings → AI Instructions]
>
> "And here's the secret weapon — **AI Instructions**. This is literally a system prompt for Copilot. Let me read a bit of this."
>
> [Read key sections]:
> - "Always use the Total Sales measure when answering questions about sales, revenue, income, or turnover"
> - "Fiscal year runs from July 1 to June 30"
> - "Enterprise = large corporations, Mid-Market = medium businesses..."
> - "When asking about top products, sort by Total Sales descending"
>
> "This is like giving Copilot a training manual for YOUR specific business. It's not generic AI — it's AI that understands Contoso."

#### 6. Synonyms / Linguistic Schema

> "We also configured **synonyms** through the linguistic schema. 'Revenue' maps to Total Sales. 'COGS' maps to Total Cost. 'Buyer' maps to Customer. 'YoY' maps to the Year-over-Year Growth measure."
>
> "This bridges the gap between how business users talk and how the model is technically structured."

#### 7. Verified Answers (Preview)

> "There's one more feature I want to highlight — **Verified Answers**. This is a preview feature that lets you pin specific visuals as the definitive answer to common questions."
>
> [Open a Power BI report connected to the good model]
>
> "Here's how it works:"
>
> 1. "Find a visual that answers a common business question — like a chart showing Total Sales by Product Category."
> 2. "Right-click the visual and select **'Set up verified answer'**."
> 3. "Add common phrases or questions users might ask — like 'What are sales by category?', 'Show me revenue by product group', 'Which department sells the most?'"
>
> "Now when a user asks any of those related questions in Copilot chat, instead of generating a new answer, Copilot will show **your saved verified answer** — the exact visual you curated."
>
> "Think of it as **bookmarking the correct answer** for your most important business questions. It removes all uncertainty — the answer isn't generated, it's **verified by you**."
>
> "This is especially powerful for:"
> - "Executive dashboard KPIs that must always look the same"
> - "Regulated metrics where the calculation method matters"
> - "Frequently asked questions where you want instant, consistent responses"

### Live NLP Testing — Good Model

> **PRESENTER:**
>
> [Open Q&A or Copilot for the Contoso Retail Analytics model]
>
> "Now let's ask the **exact same questions**."

#### Question 1: "What were total sales last year?"

> [Type the question]
>
> "Look at that. [Total Sales] for 2025, formatted as currency, using the Calendar table to determine 'last year.' Accurate, formatted, trusted."
>
> "What changed? The Total Sales measure, the Calendar date table, and the AI instruction that says 'use Total Sales for revenue questions.'"

#### Question 2: "Which product category is most profitable?"

> [Type the question]
>
> "Gross Profit by Product Category, sorted descending. [Name the top category]. The AI knew to use the Gross Profit measure because the AI instructions define 'profitable' as Gross Profit."
>
> "Remember, the bad model couldn't even attempt this. No profit measure existed."

#### Question 3: "Show me sales by region for Q4"

> [Type the question]
>
> "Total Sales by Region for Q4, no ambiguity. The AI picked Store Region (the correct one for 'sales by region'), and knew Q4 means October through December."
>
> "One Region column per dimension. Star schema eliminates the ambiguity."

#### Question 4: "How do weekend sales compare to weekday sales?"

> [Type the question]
>
> "Total Sales split by Is Weekend — Weekend vs. Weekday. Clean, clear, correct."
>
> "The column description and synonyms mapped 'weekend' to the right column, and the description explains what the 0/1 values mean."

#### Bonus Questions

> [Ask 2-3 more from the test questions doc]:
>
> "Let's push harder. 'What's the year-over-year growth?'"
>
> [Shows YoY Growth % — works perfectly]
>
> "'Who are our top 10 customers by revenue?'"
>
> [Shows top 10 Customer Name by Total Sales — no duplication]
>
> "'Compare Electronics vs Clothing sales by region for Platinum customers'"
>
> [Complex multi-dimension query — works because star schema + AI instructions]

### The Revelation

> "Same data. Same AI engine. Same questions. Completely different results."
>
> "The difference isn't the AI — **the difference is the model**."
>
> [Pause for impact]
>
> "This is why I say: **if you're getting bad AI answers, don't blame the AI. Look at your model.**"

---

## PART 4: WHAT MADE THE DIFFERENCE — The Checklist (5 minutes)

> **PRESENTER:**
>
> "Let me break down exactly what we changed, in priority order of impact:"

### The AI-Readiness Checklist

> "**#1: Star Schema.** This is non-negotiable. A flat table creates ambiguity in every question. Star schema gives each concept a single home. One source of truth for Region. One source of truth for Product Category. One source of truth for Date."
>
> "**#2: Descriptions.** This is the single highest-impact metadata element. Descriptions on tables, columns, and measures are how AI understands your data. Think of them as a data dictionary that Copilot can read."
>
> "**#3: Measures.** Without explicit measures, AI has to guess aggregations. Should I SUM this? AVERAGE it? COUNT it? Measures encode your business logic — Total Sales, Gross Profit, Profit Margin. Defined once, used correctly every time."
>
> "**#4: AI Instructions.** The system prompt for your model. Business rules, fiscal calendars, segment definitions, common question patterns. This is your expert knowledge, codified."
>
> "**#5: Synonyms.** Bridge the gap between business language and technical terms. Revenue = Total Sales. COGS = Total Cost. Buyer = Customer. FY = Fiscal Year."
>
> "**#6: Column Naming.** Business-friendly names that NLP can parse. 'Product Category' not 'prod_cat'. 'Customer Name' not 'cust_nm'."
>
> "**#7: Formatting & Data Categories.** Currency formatting, percentage formatting, geographic data categories. These make the output usable and enable features like map visuals."
>
> "**#8: Hierarchies.** Give AI a drill path. Category → Subcategory → Product. Year → Quarter → Month → Date. These structure how AI navigates your dimensions."

### The Data Dictionary Mindset

> "Notice something? Most of these are things you'd put in a **data dictionary**. Descriptions, definitions, business rules, valid values, relationships."
>
> "The best way to think about AI-ready modeling is this: **treat your semantic model as a living data dictionary**. If a new analyst joined your team tomorrow, could they understand your model just by reading the metadata? If yes, Copilot can understand it too. If not, Copilot is as confused as that new analyst would be."

---

## PART 5: PREP DATA FOR AI & VERIFIED ANSWERS (5 minutes)

> **PRESENTER:**
>
> "Fabric actually has a built-in feature to help with this. It's called **Prep data for AI**."
>
> [Navigate to the model settings → find Prep data for AI]
>
> "This feature analyzes your model and:"
> - "Identifies columns and tables missing descriptions"
> - "Suggests descriptions based on column names and data patterns"
> - "Helps generate synonyms"
> - "Flags potential issues"
>
> "It's not a silver bullet — you still need human review and business context — but it's a fantastic starting point, especially for large models with hundreds of columns."
>
> [Run or show the feature]
>
> "Think of Prep data for AI as your AI readiness assessment. It tells you the gaps. You fill them with business knowledge."

### Setting Up Verified Answers (Live Demo)

> **PRESENTER:**
>
> "Let me show you one more powerful feature — **Verified Answers**. This lets you pin specific report visuals as the guaranteed answer to common questions."
>
> [Open a Power BI report connected to the Contoso Retail Analytics model]
>
> "Let's say this bar chart shows Total Sales by Product Category — one of the most common questions executives ask."
>
> [Right-click the visual]
>
> 1. "I right-click the visual and select **'Set up verified answer'**."
> 2. "Now I add common phrases users might ask: 'What are sales by category?', 'Revenue by product type', 'Show me sales by department'."
> 3. "I save it. Done."
>
> "Now when anyone asks Copilot a related question, they get **this exact visual** — not a generated guess, but the verified, curated answer you approved."
>
> "This is a game-changer for:"
> - "**Consistency** — everyone sees the same answer"
> - "**Trust** — the answer is human-verified, not AI-generated"
> - "**Speed** — Copilot returns it instantly without computation"
>
> "Combine verified answers with AI instructions and synonyms, and you have a complete AI guidance layer: synonyms handle vocabulary, AI instructions handle business rules, and verified answers handle your most critical questions."

---

## PART 6: VS CODE AGENT MODE — Automated Model Improvement (15 minutes)

> **PRESENTER:**
>
> "Now, let's say you have an existing model like our bad one — a flat table, no metadata, abbreviated names. Remodeling the whole thing by hand sounds painful. Let me show you how **VS Code Agent Mode** can accelerate this dramatically."
>
> [Switch to VS Code with the bad model TMDL files open]

### Step 1: Analyze the Model

> "First, let's ask Copilot to analyze what's wrong."
>
> [Open Agent Mode in Copilot Chat, type]:
> ```
> Analyze the TMDL files in this semantic model. Identify all issues 
> that would hurt NLP/AI query accuracy.
> ```
>
> [Wait for response]
>
> "Look — it immediately identifies: abbreviated column names, no descriptions, no measures, flat table structure, no formatting. This matches everything we just discussed."

### Step 2: Add Descriptions

> "Let's fix the most impactful issue first — descriptions."
>
> [Type]:
> ```
> Add clear, business-friendly descriptions to every column in the 
> SalesData table. Explain what each abbreviated name means. 
> Update the TMDL file directly.
> ```
>
> [Watch as Agent Mode edits the file]
>
> "Watch this — it's editing the TMDL file directly. Adding description comments to every column. `amt` gets described as 'The net sales amount after discounts.' `cust_seg` gets 'The customer business segment: Enterprise, Mid-Market, Small Business, or Consumer.'"
>
> "In about 30 seconds, we added descriptions that would have taken an hour manually."

### Step 3: Create Measures

> "Now let's add the measures we need."
>
> [Type]:
> ```
> Add DAX measures for Total Sales (sum of amt), Total Cost (sum of cst_amt), 
> Gross Profit, Profit Margin %, Total Quantity, Total Discount, Order Count, 
> and Average Order Value. Format currencies as $#,##0.00.
> ```
>
> [Watch as measures are created]
>
> "Eight measures, properly formatted, organized in display folders. The measure DAX is correct, the format strings are right. This is production-ready."

### Step 4: Generate AI Instructions

> "And the final piece — AI instructions."
>
> [Type]:
> ```
> Generate comprehensive AI Instructions for this retail sales model 
> covering business rules, measure usage, fiscal calendar, and 
> common question patterns.
> ```
>
> [Show the generated instructions]
>
> "Complete AI instructions ready to paste into Fabric. Business rules, measure mappings, segment definitions — all generated from the model context."

### The Meta Point

> "Here's the beautiful irony. We used AI (Copilot Agent Mode) to make our model ready for AI (Copilot in Fabric). The AI is helping us prepare for the AI."
>
> "But notice — **the quality of Copilot's improvements depended on the quality of our prompts**. We had to tell it what `amt` means. We had to describe our business segments. We had to provide the fiscal year definition."
>
> "**Context in, quality out.** That's the theme of this entire session, whether we're talking about NLP queries or Agent Mode prompts."

---

## PART 7: KEY TAKEAWAYS & CALL TO ACTION (5 minutes)

> **PRESENTER:**
>
> "Let me leave you with the key takeaways."

### Takeaway 1: The Model IS the AI Strategy

> "If you want better AI answers, don't look at the AI layer first. **Look at your semantic model.** A well-modeled dataset with rich metadata will produce good results with basic AI. A poorly modeled dataset will produce bad results no matter how advanced the AI is."

### Takeaway 2: Star Schema Is Non-Negotiable

> "For AI and NLP, star schema isn't a nice-to-have — it's the foundation. It eliminates ambiguity by giving every concept a single home. One Region column. One Date table. One Customer Name. No duplicates, no confusion."

### Takeaway 3: Descriptions Are Your Highest-Impact Investment

> "If you do nothing else from this session, go add descriptions to your columns and measures. Descriptions are what Copilot reads to understand your data. They're the difference between 'I see a column called amt' and 'I know this is net revenue after discounts.'"

### Takeaway 4: Think Like a Data Dictionary

> "The best question to ask yourself: **if a brand new analyst joined your team, could they understand this model just by reading the metadata?** If yes, AI can too. If no, you have work to do."

### Takeaway 5: AI Instructions Are Your Business Rules Layer

> "AI Instructions in Fabric are a game-changer. They're a direct conversation with Copilot about YOUR specific business. Fiscal calendar, segment definitions, measure preferences — they all go here. Don't skip this."

### Takeaway 6: Agent Mode Accelerates, But Doesn't Replace Expertise

> "VS Code Agent Mode is incredibly powerful for accelerating model improvements. But it needs your domain knowledge to produce the right results. It's a multiplier, not a replacement."

### The One-Liner

> "**From 'AI sometimes works' to 'AI we can trust and scale' — the path goes through your semantic model.**"
>
> "Thank you. I'd love to take questions."

---

## APPENDIX: Q&A Preparation

### Anticipated Questions & Answers

**Q: "Does this work with Import mode or just DirectLake?"**
> A: "Everything we showed applies regardless of storage mode. Star schema, descriptions, measures, AI instructions — these are model properties that work with Import, DirectQuery, and DirectLake."

**Q: "How long does it take to make an existing model AI-ready?"**
> A: "It depends on the model size. For a model with 5-10 tables, you can do the core work (descriptions + measures + AI instructions) in a day using Agent Mode. A full star schema redesign is a bigger project, but the metadata improvements alone provide massive value."

**Q: "Can we automate this with CI/CD?"**
> A: "Absolutely. TMDL files are text-based and version-controllable. You can enforce metadata standards through code reviews, build validation checks for missing descriptions, and deploy through Git integration. Treat your semantic model like code."

**Q: "What about models with 100+ tables?"**
> A: "Prioritize. Start with the tables and measures that answer 80% of your business questions. Use Prep data for AI to identify the biggest gaps. Use Agent Mode to batch-process descriptions. You don't need perfection — you need enough context for AI to be reliable."

**Q: "Do synonyms matter that much?"**
> A: "Synonyms are the bridge between business vernacular and technical terms. If your CFO says 'topline' and your model has 'Total Sales,' synonyms make that connection. They're not mandatory, but they significantly reduce NLP failures for domain-specific terminology."

**Q: "Is this just for Copilot or does it help regular Power BI Q&A too?"**
> A: "Both. Q&A and Copilot both read the semantic model metadata. Everything we showed — descriptions, synonyms, measures, the linguistic schema — benefits both Q&A and Copilot. Investing in your model improves every AI/NLP experience."

**Q: "What about row-level security?"**
> A: "RLS is orthogonal to AI readiness. You should have RLS for data security, and it works with Copilot. But RLS doesn't help or hurt NLP accuracy — that's about model structure and metadata."

---

## Timing Guide

| Section | Duration | Running Total |
|---------|----------|---------------|
| Part 1: Setting the Stage | 5 min | 5 min |
| Part 2: Bad Model Demo | 10 min | 15 min |
| Part 3: Good Model Demo | 15 min | 30 min |
| Part 4: What Made the Difference | 5 min | 35 min |
| Part 5: Prep Data for AI & Verified Answers | 5 min | 40 min |
| Part 6: VS Code Agent Mode | 15 min | 55 min |
| Part 7: Takeaways | 5 min | 60 min |

### Shortened Version (45 min)
- Reduce Part 2 to 3 questions (5 min)
- Reduce Part 3 to 3 questions (10 min)
- Skip Part 5 (Prep data for AI)
- Reduce Agent Mode to 2 steps (8 min)

### Extended Version (90 min)
- Add hands-on exercise: attendees improve a model on their own
- Adding deeper dive into linguistic schema and synonym configuration
- More Agent Mode examples with advanced prompts
- Extended Q&A (15 min)
