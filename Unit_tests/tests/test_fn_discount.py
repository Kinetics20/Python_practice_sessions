from Unit_tests.fn_discount import calc_discount


def test_valid_discount():
    assert calc_discount(100, 20) == 80
    assert calc_discount(50, 10) == 45
    assert calc_discount(0.01, 0.01) == 0.01 * (1 - 0.01 / 100)
    assert calc_discount(50, 99.99) == 50 * (1 - 99.99 / 100)
