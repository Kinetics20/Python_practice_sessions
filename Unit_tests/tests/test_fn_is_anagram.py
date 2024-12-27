from Unit_tests.fn_is_anagram import is_anagram


def test_valid_anagram():
    assert is_anagram("listen", "silent") == True
    assert is_anagram("triangle", "integral") == True
    assert is_anagram("anagram", "nagaram") == True


def test_invalid_anagrams():
    assert is_anagram("hello", "world") == False
    assert is_anagram("python", "java") == False
    assert is_anagram("test", "best") == False
