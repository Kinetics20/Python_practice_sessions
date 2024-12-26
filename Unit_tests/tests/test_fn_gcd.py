from Unit_tests.fn_gcd import gcd


def test_gcd_positive_numbers():
    assert gcd(54, 24) == 6
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1


def test_gcd_negative_numbers():
    assert gcd(-54, 24) == 6
    assert gcd(54, -24) == 6
    assert gcd(-54, -24) == 6


def test_gcd_zero():
    assert gcd(0, 5) == 5
    assert gcd(5, 0) == 0
    assert gcd(0, 0) == 0
