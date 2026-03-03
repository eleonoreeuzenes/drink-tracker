# app/core/text_normalization.py

from app.core.drink_messages import KNOWN_DRINK_MESSAGES
import unicodedata 
import re

def normalize_text(text: str) -> str:
    """
    Normalize text
    - to lowercase
    - remove accents
    - remove special characters
    - remove extra spaces
    - normalize known drink messages
    """
    text = normalize_lowercase(text)
    text = normalize_accents(text)
    text = normalize_noise(text)
    text = normalize_spaces(text)
    
    return text

def normalize_lowercase(text: str) -> str:
    return text.lower()

def normalize_accents(text: str) -> str: 
    normalized = unicodedata.normalize("NFD", text)
    return "".join(c for c in normalized if unicodedata.category(c) != "Mn")


def normalize_noise(text: str) -> str: 
    # Remove all characters that are not letters, numbers, or whitespace
    return re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    
    
def normalize_spaces(text: str) -> str: 
    return re.sub(r"\s+", " ", text).strip()

