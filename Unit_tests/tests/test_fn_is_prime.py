import pytest

from Unit_tests.fn_is_prime import is_prime


def test_prime_numbers():
    assert is_prime(2) == True
    assert is_prime(5) == True
    assert is_prime(13) == True


def test_negative_numbers():
    assert is_prime(-2) == False
    assert is_prime(-1) == False
    assert is_prime(0) == False


def test_is_prime_str():
    with pytest.raises(TypeError):
        is_prime("Home")
    with pytest.raises(TypeError):
        is_prime(["Home", 2])
    with pytest.raises(TypeError):
        is_prime({2: "Home", 3: 'SEa'})
    with pytest.raises(TypeError):
        is_prime(3.1525)


def test_non_prime_numbers():
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(9) == False
