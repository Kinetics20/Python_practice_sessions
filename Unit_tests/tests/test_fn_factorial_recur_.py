from Functional_Programming.decorators_practice import factorial


def test_positive_factorial():
    assert factorial(2) == 2
    assert factorial(10) == 2432902008176640000