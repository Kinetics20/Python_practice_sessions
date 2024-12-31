def factorial(n: int) -> int:
    """
    Returns the factorial of n.

    :param n: the integer.
    :type n: int
    :return: int number of factorial of n.
    :rtype: int
    :raises: ValueError if n is negative or higher than 999.
             RecursionError if n is higher than 999.
    """
    if n < 0:
        raise ValueError("n must be positive")
    if n > 998:
        raise RecursionError("n must be smaller than 999")

    return 1 if n == 0 else n * factorial(n - 1)


print(factorial(20))
