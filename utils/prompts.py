# utils/prompts.py
import json
def get_analysis_prompt(text):
    return f"""
Analyze the following documentation content for:

1. Structure and Flow
2. Completeness (details + examples)
3. Style (based on Microsoft Style Guide: clarity, tone, conciseness)

Respond in JSON with keys:
- structure_and_flow: {{"assessment": "...", "suggestions": []}},
- completeness: {{"assessment": "...", "suggestions": []}},
- style_guidelines: {{"assessment": "...", "suggestions": []}}

Content:
{text}
"""
def get_rewrite_prompt(original_text, suggestions):
    return f"""
You are a technical writing assistant. Improve the following documentation article based on the suggestions provided.

--- Original Article ---
{original_text}

--- Suggestions ---
{json.dumps(suggestions, indent=2)}

--- Instructions ---
Only revise the text. Do NOT explain or annotate changes.
Focus on improving:
- Readability
- Clarity
- Tone
- Sentence structure

Output the revised article.
"""
