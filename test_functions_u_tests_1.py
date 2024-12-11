import pytest

from functions_u_tests_1 import divide


def test_divide_positive_numbers():
    assert divide(20, 5) == 4.0


def test_divide_numbers_negative():
    assert divide(20, 5) != 10.0


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(20, 0)
