from twttr import shorten
import sys

def main():
    test_shorten()
    

def test_shorten():
    assert shorten("test") == "tst"
    assert shorten("test.") == "tst."
    assert shorten("tEst") == "tst"
    assert shorten("test0") == "tst0"

if __name__ == "__main__":
    main()