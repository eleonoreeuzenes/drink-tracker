from pathlib import Path

import pytesseract
from PIL import Image


def extract_text(image_path: Path) -> str:
    """Extract text from an image using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
