# utils/readability.py
import textstat

def assess_readability(text):
    flesch = textstat.flesch_reading_ease(text)
    fog = textstat.gunning_fog(text)
    score_summary = {
        "flesch_reading_ease": flesch,
        "gunning_fog": fog,
        "assessment": "",
        "suggestions": []
    }

    if flesch < 50:
        score_summary["assessment"] = "Difficult to read for a non-technical marketer."
        score_summary["suggestions"].append("Simplify complex sentences.")
    else:
        score_summary["assessment"] = "Generally readable for a marketer."

    return score_summary
