from Unit_tests.fn_comprehension_2 import create_list_compr_factorial


def test_zero():
    assert create_list_compr_factorial(0) == []


def test_one():
    assert create_list_compr_factorial(1) == [0]


def test_positive():
    assert create_list_compr_factorial(5) == [0, 1, 4, 9, 16]
