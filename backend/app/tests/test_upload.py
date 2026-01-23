from pathlib import Path
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_upload_image():
    assets_dir = Path(__file__).parent / "assets"
    image_path = assets_dir / "easy_text.png"

    with image_path.open("rb") as f:
        response = client.post(
            "/upload",
            files={"file": ("easy_text.png", f, "image/png")}
        )

    assert response.status_code == 200
    assert "filename" in response.json()


def test_upload_invalid_file(tmp_path):
    # Create a fake text file
    fake_text = tmp_path / "test.txt"
    fake_text.write_text("This is a test text file.")

    with fake_text.open("rb") as f:
        response = client.post(
            "/upload",
            files={"file": ("test.txt", f, "text/plain")}
        )

    assert response.status_code == 400  # Bad Request for invalid file type