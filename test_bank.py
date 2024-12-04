from bank import value

def test_здравствуйте():
    assert value("Здравствуйте, Маша!") == "$0"

def test_здрасти():
    assert value("Здрасти, Маша!") == "$20"

def test_hello():
    assert value("hello, Wwww!") == "$100"
