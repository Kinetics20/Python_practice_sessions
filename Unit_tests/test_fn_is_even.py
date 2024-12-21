import pytest

from Unit_tests.fn_is_even import is_even


def test_positive_is_even():
    assert is_even(4) == True


def test_negative_is_even():
    assert is_even(3) == False


def test_float_is_even():
    with pytest.raises(ValueError):
        is_even(3.7)


def test_int_is_even():
    with pytest.raises(TypeError):
        is_even('Home')
