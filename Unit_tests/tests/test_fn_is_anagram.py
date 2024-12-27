from Unit_tests.fn_is_anagram import is_anagram


def test_valid_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("anagram", "nagaram") == True