def calc_discount(price: float, discount: float) -> float:
    """
    Function calculates price after apply the discount .
    :param price: amount in any currency
    :type price: float
    :param discount: value between 0 and 100
    :type discount: float
    :return: price after discount
    :rtype: float
    :raises: ValueError if price or discount is invalid
        price must be greater than 0 and discount must be greater than 0 and less than 100
    """
    if price <= 0:
        raise ValueError("Price must be greater than 0")
    if not (0 <= discount <= 100):
        raise ValueError("Discount must be between 0 and 100")

    return price * (1 - discount / 100)
