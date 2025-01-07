def multiple_elements_list(list_1: list[int], list_2: list) -> list[int]:
    return list(map(lambda a, b: a * b, list_1, list_2))
