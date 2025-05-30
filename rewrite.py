# rewrite.py
import sys
import json
from utils.fetcher import extract_article_text
from utils.prompts import get_rewrite_prompt
from utils.llm_api import get_llm_analysis

def load_suggestions(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def rewrite_document(url, suggestions_file):
    # Step 1: Get original content
    original = extract_article_text(url)
    if not original:
        print("Failed to fetch original article content.")
        return

    # Step 2: Load suggestions from Agent 1
    suggestions = load_suggestions(suggestions_file)

    # Step 3: Build prompt for rewriting
    prompt = get_rewrite_prompt(original, {
        "readability": suggestions.get("readability", {}).get("suggestions", []),
        "style_guidelines": suggestions.get("style_guidelines", {}).get("suggestions", [])
    })

    # Step 4: Run LLM
    improved = get_llm_analysis(prompt)

    # Step 5: Save result
    with open("outputs/revised_output.txt", "w", encoding="utf-8") as f:
        f.write(improved.strip())

    print("✅ Revised article saved to outputs/revised_output.txt")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python rewrite.py <documentation_url> <suggestions_json_path>")
        sys.exit(1)

    url = sys.argv[1]
    suggestions_file = sys.argv[2]

    rewrite_document(url, suggestions_file)
