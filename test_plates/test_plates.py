from plates import is_valid

def test_length():
    assert is_valid("A") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAAA222") == False

def test_characters():
    assert is_valid("A222") == False
    assert is_valid("AA222") == True

def test_numbers():
    assert is_valid("AA02") == False
    assert is_valid("AA20") == True
    assert is_valid("AA2A") == False
    
def test_punctuation():
    assert is_valid("AA.20") == False