from fuel import convert, gauge
from pytest import raises

def test_convert():
    with raises(ZeroDivisionError):
        assert convert("2/0")
    with raises(ValueError):
        assert convert("2/1")
    assert convert("2/3") == 67

def test_gauge():
    assert gauge(67) == "67%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"