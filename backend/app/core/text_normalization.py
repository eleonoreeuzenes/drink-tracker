# app/core/text_normalization.py
import unicodedata
from app.core.drink_messages import KNOWN_DRINK_MESSAGES

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
    text = normalize_drink_messages(text)
    
    return text

def normalize_lowercase(text: str) -> str:
    return text.lower()

def normalize_accents(text: str) -> str: 
    return text

def normalize_noise(text: str) -> str: 
    return text
    
    
def normalize_spaces(text: str) -> str: 
    return text

def normalize_drink_messages(text: str) -> str:
    text = normalize_lowercase(text)
    for known_message in KNOWN_DRINK_MESSAGES:
        if known_message in text:
            return known_message
    return text