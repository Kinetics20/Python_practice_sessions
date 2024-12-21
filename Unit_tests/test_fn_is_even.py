from Unit_tests.fn_is_even import is_even


def test_positive_is_even():
    assert is_even(4) == True


def test_negative_is_even():
    assert is_even(3) == False