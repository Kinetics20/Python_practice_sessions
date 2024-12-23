def reverse_str(s: str) -> str:
    """
    Function returns reversed string
    :param s: The s is a parameter taken by reverse_str. Must be not empty
    :type s: str
    :raises TypeError: If s is not a string
    :return: reversed string
    :rtype: str
    """
    if not isinstance(s, str):
        raise TypeError('s is not a string')
    return s[::-1]


print(reverse_str('Where is my wallet ?'))
