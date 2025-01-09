from Unit_tests.fn_map_conc_list import repeat_strings_with_map


def test_positive_list():
    assert repeat_strings_with_map(["A", "B", "C", "D"], [1, 2, 3, 4]) == ['A', 'BB', 'CCC', 'DDDD']
