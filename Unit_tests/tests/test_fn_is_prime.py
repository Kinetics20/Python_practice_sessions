from Unit_tests.fn_is_prime import is_prime


def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(13) == True


def test_negative_numbers():
    assert is_prime(-2) == False
    assert is_prime(-1) == False
    assert is_prime(0) == False
