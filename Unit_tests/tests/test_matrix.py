from Unit_tests.matrix import create_matrix


def test_matrix_size_1():
    assert create_matrix(1) == [[1]]


def test_matrix_size_2():
    assert create_matrix(2) == [[1, 2], [3, 4]]
