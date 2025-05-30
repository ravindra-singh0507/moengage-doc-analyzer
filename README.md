# 📘 MoEngage Documentation Improvement Agent

This project is a submission for the **MoEngage Tech Intern Assignment**, focused on building an **AI-powered assistant** to improve the quality of public documentation at [help.moengage.com](https://help.moengage.com).

It consists of two agents:

- **Agent 1: Documentation Analyzer** — Evaluates an article and generates actionable suggestions.
- **Agent 2: Documentation Rewriter** — Optionally rewrites the article using Agent 1's suggestions.

---

## 🚀 Features

### Agent 1: Documentation Analyzer

Analyzes a MoEngage documentation article using LLMs and readability metrics. Generates structured improvement suggestions based on:

1. **Readability for a Marketer**
2. **Structure and Flow**
3. **Completeness of Information & Examples**
4. **Adherence to Style Guidelines** (based on Microsoft Style Guide)

#### ✅ Output Format

A structured **JSON report** like:

json
{
  "url": "https://help.moengage.com/...",
  "readability": {
    "assessment": "...",
    "suggestions": [...]
  },
  "structure_and_flow": {
    "assessment": "...",
    "suggestions": [...]
  },
  "completeness": {
    "assessment": "...",
    "suggestions": [...]
  },
  "style_guidelines": {
    "assessment": "...",
    "suggestions": [...]
  }
}

Agent 2: Documentation Rewriter (Bonus)
Takes the original article + Agent 1’s suggestions and rewrites the content using an LLM. Focuses on:
Improving clarity and tone
Rephrasing passive or complex sentences
Simplifying jargon

### Project Structure
moengage-doc-agent/
├── analyze.py                # Agent 1 main runner
├── rewrite.py                # Agent 2 main runner
├── outputs/
│   ├── sample_output.json    # Example analysis
│   └── revised_output.txt    # Example rewritten article
├── utils/
│   ├── fetcher.py            # Scrapes article content
│   ├── readability.py        # Computes readability scores
│   ├── llm_api.py            # Handles OpenAI API integration
│   └── prompts.py            # LLM prompt templates
├── requirements.txt
└── README.md

### Setup Instructions
1. Clone the repository
   https://github.com/ravindra-singh0507/moengage-doc-analyzer
   cd moengage-doc-analyzer
2. Install dependencies
   pip install -r requirements.txt
3. Set your OpenAI API key
   set OPENAI_API_KEY=sk-your-key
4. Run Agent 1
   python analyze.py "https://help.moengage.com/hc/en-us/articles/..."
   Output saved to: outputs/sample_output.json
5. Run Agent 2
   python rewrite.py "https://help.moengage.com/hc/en-us/articles/..." outputs/sample_output.json
   Output saved to: outputs/revised_output.txt
