# Fabric Data Modeling for AI & NLP — Hands-On Demo

## 🎯 Purpose

This repository contains a complete, hands-on demo showing how **data modeling, AI instructions, synonyms, and semantic metadata** directly impact the accuracy and reliability of natural language queries (NLP/Copilot) in Microsoft Fabric.

The demo contrasts:
- **Bad Model** — A single flat/denormalized table with technical column names, no descriptions, no measures, and no AI guidance → produces vague, inconsistent NLP answers
- **Good Model** — A proper star schema with business-friendly naming, rich descriptions, well-defined measures, AI instructions, synonyms, and data categories → produces accurate, trustworthy NLP answers

## 📁 Repository Structure

```
FabricDataModeling/
├── README.md                          ← You are here
├── data/
│   └── generate-sample-data.py        ← Fabric notebook to create sample data
├── models/
│   ├── bad-model/
│   │   └── SalesFlat.SemanticModel/   ← Flat denormalized model (the "before")
│   └── good-model/
│       └── ContosoRetailAnalytics.SemanticModel/  ← Star schema model (the "after")
├── demo/
│   ├── nlp-test-questions.md          ← Side-by-side NLP test questions
│   ├── ai-instructions-reference.md   ← AI instructions content
│   └── agent-mode-guide.md            ← VS Code Agent Mode walkthrough
└── talk-track.md                      ← Full presenter talk track
```

## 🛠 Prerequisites

- Microsoft Fabric workspace with **Fabric capacity (F64 or higher recommended for DirectLake)**
- A **Lakehouse** in the workspace
- **VS Code** with the following extensions:
  - [Fabric Synapse Extension](https://marketplace.visualstudio.com/items?itemName=synapsevscode.synapse)
  - [GitHub Copilot](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
  - [GitHub Copilot Chat](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat)
- Fabric workspace connected to **Git (Azure DevOps or GitHub)** for TMDL deployment

## 🚀 Setup Instructions

### Step 1: Create the Lakehouse

1. Navigate to your Fabric workspace
2. Click **+ New** → **Lakehouse**
3. Name it `ContosoRetailLakehouse`

### Step 2: Generate Sample Data

1. Open the lakehouse and click **Open notebook** → **New notebook**
2. Copy the contents of [`data/generate-sample-data.py`](data/generate-sample-data.py) into the notebook cells
3. Run all cells — this creates both the flat table and star schema tables

### Step 3: Create the Bad Model (Option A — From UI)

1. From the lakehouse, click **New semantic model**
2. Select only the `sales_data_flat` table
3. Name it `SalesFlat`
4. Do **NOT** add any descriptions, measures, or AI instructions (leave it raw)

### Step 3 Alt: Create the Bad Model (Option B — From TMDL via Git)

1. Connect your workspace to a Git repo
2. Copy the `models/bad-model/SalesFlat.SemanticModel/` folder into the repo
3. Update the SQL endpoint and lakehouse name in `expressions.tmdl`
4. Sync from Git to deploy

### Step 4: Create the Good Model

1. **Option A (Recommended):** Use Git integration to deploy `models/good-model/ContosoRetailAnalytics.SemanticModel/`
2. **Option B:** Create from UI, then apply all metadata manually following the TMDL definitions
3. Update the SQL endpoint and lakehouse name in `expressions.tmdl`

### Step 5: Configure AI Instructions (Good Model)

1. Open the good model in Fabric portal
2. Go to **Model settings** → **AI Instructions**
3. Copy the instructions from [`demo/ai-instructions-reference.md`](demo/ai-instructions-reference.md)
4. Also run **Prep data for AI** from the model settings

### Step 6: Run the Demo

1. Open [`talk-track.md`](talk-track.md) for the full presenter script
2. Use [`demo/nlp-test-questions.md`](demo/nlp-test-questions.md) for NLP testing
3. Follow [`demo/agent-mode-guide.md`](demo/agent-mode-guide.md) for the Agent Mode section

## ⚡ Quick Demo Flow

```
1. Show bad model → Ask NLP questions → See vague/wrong answers
2. Show good model → Ask same questions → See accurate answers
3. Open bad model in VS Code → Use Agent Mode to improve it
4. Discuss what changed and why it matters
```

## 📌 Key Takeaways

- **Star schema** is not just a best practice — it's a requirement for reliable AI
- **Descriptions** are the single most impactful metadata for NLP accuracy
- **AI Instructions** act as a "system prompt" for Copilot to understand your business
- **Synonyms** bridge the gap between business language and technical terms
- **Measures** eliminate ambiguity — without them, AI has to guess aggregations
- **VS Code Agent Mode** can accelerate model improvement dramatically
