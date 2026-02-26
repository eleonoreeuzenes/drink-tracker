from pathlib import Path
from doctr.io import DocumentFile
from doctr.models import ocr_predictor

model = ocr_predictor(pretrained=True)

def extract_text(image_path: Path) -> str:
    doc = DocumentFile.from_images(str(image_path))

    result = model(doc)

    lines = []
    for page in result.pages:
        for block in page.blocks:
            for line in block.lines:
                words = [w.value for w in line.words]
                if words:
                    lines.append(" ".join(words))

    text = " ".join(lines).strip()

    return text if text else ""
