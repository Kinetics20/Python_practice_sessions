import pytest

from Unit_tests.fn_filter_e_n import filter_odd_numbers


def test_valid_input():
    assert filter_odd_numbers([1, 2, 3, 4, 5]) == [1, 3, 5]
    assert filter_odd_numbers([10, 15, 20, 25]) == [15, 25]
    assert filter_odd_numbers([0, -1, -2, -3]) == [-1, -3]


def test_empty_list():
    assert filter_odd_numbers([]) == []


def test_no_odd_numbers():
    assert filter_odd_numbers([2, 4, 6, 8]) == []
    assert filter_odd_numbers([0, -2, -4]) == []


def test_all_odd_numbers():
    assert filter_odd_numbers([1, 3, 5, 7]) == [1, 3, 5, 7]
    assert filter_odd_numbers([-1, -3, -5]) == [-1, -3, -5]


def test_invalid_input_not_list():
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers("string")
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers(12345)
    with pytest.raises(TypeError, match="Input must be a list"):
        filter_odd_numbers(None)
