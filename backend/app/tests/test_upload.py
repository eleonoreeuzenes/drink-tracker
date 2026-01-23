from fastapi.testclient import TestClient
from app.main import app
from pathlib import Path

client = TestClient(app)

def test_upload_image(tmp_path):
    # Create a fake image file
    fake_image = tmp_path / "test.jpg"
    fake_image.write_bytes(b"fake image bytes")

    with fake_image.open("rb") as f:
        response = client.post(
            "/upload",
            files={"file": ("test.jpg", f, "image/jpeg")}
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