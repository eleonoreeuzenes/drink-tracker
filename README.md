# 🥜 NuttyDrink Counter
A tiny full‑stack project that counts how many nut‑flavored drinks I’ve consumed at school by analyzing photos of the machine screen. Each drink costs 0.40 €, and the project keeps track of both the count and the total cost.

This app uses **OCR** (Optical Character Recognition) to read the text displayed on the machine (e.g., “preparando …”) and increments a counter whenever a matching drink is detected.

# Stack
- FastApi (web framework)
- Uvicorn (ASGI server to run FastAPI)
- python-multipart (handle file uploads)
- pytest (testing)
- httpx (testing async endpoints)
- pytest-asyncio (write async tests)
- ruff (linter)
- pytesseract (Tesseract OCR)
- pillow (Image processing)

# Run the project
With Docker:
```
cd backend
docker compose up -d
```

Without:
```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```