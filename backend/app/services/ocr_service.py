from pathlib import Path

from doctr.io import DocumentFile
from doctr.models import ocr_predictor

from app.core.fuzzy_matching import match_drink_message
from app.core.text_normalization import normalize_text

model = ocr_predictor(pretrained=True)

def extract_raw_text(image_path: Path) -> str:
    doc = DocumentFile.from_images(str(image_path))

    result = model(doc)

    lines = []
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                words = [w.value for w in line.words]
                if words:
                    lines.append(" ".join(words))

    return " ".join(lines).strip()

def interpret_text(text: str) -> str | None:
    normalized_text = normalize_text(text)
    match = match_drink_message(normalized_text)
    if match:
        return match
    else:
        return normalize_text or ""

def extract_text(image_path: Path) -> str:
    raw_text = extract_raw_text(image_path)
    return interpret_text(raw_text)
