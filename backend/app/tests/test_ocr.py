from app.services.ocr_service import extract_text
from pathlib import Path


def test_extract_text_with_real_image():
    # Path to your real test image
    assets_dir = Path(__file__).parent / "assets"
    image_path = assets_dir / "easy_text.png"
    print(f"Testing OCR on image: {image_path}")

    text = extract_text(image_path)

    assert text == "This text is\neasy to extract."
