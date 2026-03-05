# tests/core/test_fuzzy_matching.py

from app.core.fuzzy_matching import match_drink_message


def test_match_latte():
    assert match_drink_message("preparand0 latte gourrnad") == "preparando latte gourmand"  # noqa: E501

def test_match_chocolat():
    assert match_drink_message("preparando ch0colat gourmad") == "preparando chocolat gourmand"  # noqa: E501

def test_no_match_below_threshold():
    assert match_drink_message("random text that means nothing") is None
