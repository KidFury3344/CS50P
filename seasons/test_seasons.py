from seasons import get_minutes

def test_get_minutes():
        assert get_minutes("2023-07-08") == "Five hundred seventy-one thousand, six hundred eighty minutes"
        assert get_minutes("1999-01-01") == "Thirteen million, four hundred sixty-five thousand, four hundred forty minutes"