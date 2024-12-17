from src.util.utilities import add, sub, mul, div, sqrt, pow

def test_add():
    assert add(1, 2) == 3

def test_sub():
    assert sub(1, 2) == -1

def test_mul():
    assert mul(1, 2) == 2

def test_div():
    assert div(1, 2) == 0.5

def test_sqrt():
    assert sqrt(4) == 2

def test_pow():
    assert pow(2, 3) == 8

def test_mul_by_zero():
    try:
        div(1, 0)
    except ValueError as e:
        assert str(e) == "Can't divide by zero"

def test_div_by_zero():
    try:
        div(1, 0)
    except ValueError as e:
        assert str(e) == "Can't divide by zero"