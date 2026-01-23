from PIL import Image
import pytesseract
from pathlib import Path


def extract_text(image_path: Path) -> str:
    """Extract text from an image using Tesseract OCR."""
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
