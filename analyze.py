import sys
import json
from utils.fetcher import extract_article_text
from utils.readability import assess_readability
from utils.prompts import get_analysis_prompt
from utils.llm_api import get_llm_analysis

def analyze(url):
    content = extract_article_text(url)

    if not content or "error" in content:
        return {
            "url": url,
            "error": "Unable to extract article content",
            "details": content.get("error", "")
        }

    text = content["content"]

    # Readability
    readability_report = assess_readability(text)

    # LLM analysis
    prompt = get_analysis_prompt(text)
    llm_response = get_llm_analysis(prompt)

    # Combine
    report = {
        "url": url,
        "readability": readability_report
    }

    try:
        llm_json = json.loads(llm_response)
        report.update(llm_json)
    except Exception as e:
        report["llm_error"] = f"Failed to parse LLM response: {e}"
        report["raw_llm_output"] = llm_response

    return report

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    final_report = analyze(url)

    with open("outputs/sample_output.json", "w", encoding="utf-8") as f:
        json.dump(final_report, f, indent=2, ensure_ascii=False)

    print("Analysis complete. Output saved to outputs/sample_output.json")
