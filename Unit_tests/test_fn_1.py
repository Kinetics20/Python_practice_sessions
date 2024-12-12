import pytest

from Unit_tests.fn_1 import add_up


def test_positive_numbers():
    assert add_up(1, 2, 3) == 1.0


def test_negative_numbers():
    assert add_up(1, 2, 3) != 5.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        add_up(1, 2, 0)


def test_divide_floats():
    assert add_up(0, 1, 3) == pytest.approx(0.3333333333333333
, rel=1e-4)
