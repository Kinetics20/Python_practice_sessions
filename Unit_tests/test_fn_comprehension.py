from Unit_tests.fn_comprehension import create_lst_


def test_positive_fn_comprehension():
    assert create_lst_(5) == [0, 1, 2, 3, 4]


def test_negative_fn_comprehension():
    assert create_lst_(-1) != [-1]


def test_zero_fn_comprehension():
    assert create_lst_(0) == []
