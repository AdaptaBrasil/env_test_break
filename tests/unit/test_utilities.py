import src.util.utilities as math_utils

def test_add():
    assert math_utils.add(1, 2) == 3

def test_sub():
    assert math_utils.sub(1, 2) == -1

def test_mul():
    assert math_utils.mul(1, 2) == 2

def test_div():
    assert math_utils.div(1, 2) == 0.5

def test_sqrt():
    assert math_utils.sqrt(4) == 2

def test_pow():
    assert math_utils.pow(2, 3) == 8

def test_mul_by_zero():
    try:
        math_utils.div(1, 0)
    except ValueError as e:
        assert str(e) == "Can't divide by zero"

def test_div_by_zero():
    try:
        math_utils.div(1, 0)
    except ValueError as e:
        assert str(e) == "Can't divide by zero"