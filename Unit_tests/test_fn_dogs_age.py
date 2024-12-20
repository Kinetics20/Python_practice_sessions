import pytest

from Unit_tests.fn_dogs_age import dogs_age_2


def test_positive_age_case_1():
    assert dogs_age_2(2) == 21


def test_positive_age_case_2():
    assert dogs_age_2(3.5) != 40


def test_negative_age_case():
    with pytest.raises(ValueError):
        dogs_age_2(-1)


def test_other_value_case():
    with pytest.raises(TypeError):
        dogs_age_2('dog')


def test_other_value_case_2():
    with pytest.raises(TypeError):
        dogs_age_2(True)
