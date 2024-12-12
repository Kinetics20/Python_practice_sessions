import pytest
from Unit_tests.fn_1 import add_up


def test_positive_numbers():
    assert add_up(1, 2, 3) == 1.0


def test_negative_numbers():
    assert add_up(1, 2, 3) != 5.0
