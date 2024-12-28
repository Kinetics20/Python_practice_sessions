import pytest

from Unit_tests.fn_discount import calc_discount


def test_valid_discount():
    assert calc_discount(100, 20) == 80
    assert calc_discount(50, 10) == 45
    assert calc_discount(0.01, 0.01) == 0.01 * (1 - 0.01 / 100)
    assert calc_discount(50, 99.99) == 50 * (1 - 99.99 / 100)


def test_invalid_prices():
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        calc_discount(0, 20)
    with pytest.raises(ValueError, match="Price must be greater than 0"):
        calc_discount(-10, 0)


def test_invalid_discount():
    with pytest.raises(ValueError, match="Discount must be greater than 0"):
        calc_discount(100, 0)
    with pytest.raises(ValueError, match="Discount must be greater than 0"):
        calc_discount(100, 100)
    with pytest.raises(ValueError, match="Discount must be greater than 0"):
        calc_discount(100, -10)
    with pytest.raises(ValueError, match="Discount must be greater than 0"):
        calc_discount(100, 150)
