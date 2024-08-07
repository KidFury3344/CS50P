from um import count


def test_value():
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2

def test_zero():
    assert count("yummy") == 0
    assert count("ummy") == 0

def test_punctuation():
    assert count("um?") == 1