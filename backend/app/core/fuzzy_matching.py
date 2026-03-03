from rapidfuzz import fuzz, process
from app.core.drink_messages import KNOWN_DRINK_MESSAGES

def match_drink_message(normalized_text: str) -> str | None:
    best_match = process.extractOne(normalized_text, KNOWN_DRINK_MESSAGES, scorer=fuzz.partial_ratio)
    if best_match is None: return None

    match, score, index = best_match

    if score < 70:
        return None

    return match