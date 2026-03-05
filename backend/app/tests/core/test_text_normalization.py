# tests/core/test_text_normalization.py

from app.core.text_normalization import normalize_text


def test_normalize_text_basic():
    assert normalize_text("Préparando Latte Gourrnad.") == "preparando latte gourrnad"

def test_normalize_text_noise():
    assert normalize_text("preparando_latte|gourmand") == "preparando latte gourmand"

def test_normalize_text_spaces():
    assert normalize_text("  preparando   latte   gourmand ") == "preparando latte gourmand"  # noqa: E501
