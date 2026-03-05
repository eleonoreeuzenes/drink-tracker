# tests/services/test_extract_text_pipeline.py

from pathlib import Path
from app.services.ocr_service import extract_text

def test_extract_text_with_real_image():
    # Path to this test file
    test_dir = Path(__file__).parent

    # Path to the assets folder
    assets_dir = test_dir.parent / "assets"

    # Path to the image
    image_path = assets_dir / "test_coffee.jpg"

    assert image_path.exists(), f"Image not found: {image_path}"

    result = extract_text(image_path)

    assert result == "preparando cafe gourmand"
