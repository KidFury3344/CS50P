from jar import Jar
from pytest import raises

def test_init():
    with raises(ValueError):
        jar = Jar(-3)
    with raises(TypeError):
        jar = Jar("Hello")
    jar = Jar(15)
    assert jar.capacity == 15

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(10)
    with raises(ValueError):
        jar.deposit(11)
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"

def test_withdraw():
    jar = Jar(10)
    jar.deposit(5)
    with raises(ValueError):
        jar.withdraw(10)
    jar.withdraw(4)
    assert str(jar) == "🍪"

