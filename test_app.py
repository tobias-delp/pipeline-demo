from app import add, div


def test_add():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, 3) == 2


def test_add_failed():
    assert add(2, 2) == 4


def test_div_zero():
    assert div(12, 0) == 0
