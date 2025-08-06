from calculator import add

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 10) == 9
    assert add(6, -2) == 4