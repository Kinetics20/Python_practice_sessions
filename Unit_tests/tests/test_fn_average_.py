from Unit_tests.fn_average_ import calc_average


def test_positive_numbers():
    assert calc_average([1, 2, 3, 4, 5]) == 3.0


def test_negative_numbers():
    assert calc_average([-1, -2, -3, -4, -5]) == -3.0
