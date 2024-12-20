from Unit_tests.fn_dogs_age import dogs_age_2


def test_positive_age_case_1():
    assert dogs_age_2(2) == 21


def test_positive_age_case_2():
    assert dogs_age_2(3.5) != 40
