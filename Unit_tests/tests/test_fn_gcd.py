from Unit_tests.fn_gcd import gcd


def test_gcd_positive_numbers():
    assert gcd(54, 24) == 6
    assert gcd(48, 18) == 6
    assert gcd(101, 103) == 1