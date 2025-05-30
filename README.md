# MoEngage Documentation Analyzer (Agent 1)

This project implements an AI-powered Documentation Analyzer Agent for improving MoEngage help articles using readability metrics and LLM analysis. The tool reads a documentation article and outputs a structured JSON report with suggestions across four criteria.

---

## 🔍 Task Overview

**Goal**: Automatically review and suggest improvements for MoEngage documentation content.

**Input**: URL of a public MoEngage documentation article  
**Output**: JSON report containing:
- Readability analysis (for a marketer persona)
- Structure & flow feedback
- Completeness (examples, details)
- Style guideline assessment (clarity, tone, conciseness)

---

## 📁 File Structure
moengage_doc_agent/
├── analyze.py
├── utils/
│   ├── fetcher.py       # HTML content scraper
│   ├── readability.py   # Readability analysis
│   ├── llm_api.py       # LLM integration (e.g., OpenAI)
│   └── prompts.py       # Prompts for evaluation
├── outputs/
│   └── sample_output.json
├── README.md
└── requirements.txt


---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/moengage-doc-analyzer.git
cd moengage-doc-analyzer

pip install -r requirements.txt

Set the OPENAI_API_KEY as an environment variable:
export OPENAI_API_KEY=your-api-key-here

🚀 How to Run

analyze.py <documentation_url>
Example: analyze.py https://help.moengage.com/hc/en-us/articles/360033580571
Output will be saved in outputs/sample_output.json.