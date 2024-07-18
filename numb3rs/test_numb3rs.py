from numb3rs import validate

def test_false():
    assert validate("192.126") == False
    assert validate("192") == False
    assert validate("192.126.1111.0") == False
    assert validate("cat") == False
    
    
def test_true():
    assert validate("192.168.1.0") == True
    assert validate("192.168.255.255") == True