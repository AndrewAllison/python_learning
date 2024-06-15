from string_examples import (
    format_string,
    concatenate_string,
    find_substring,
    replace_substring,
    slice_string,
)


def test_concatenate_string():
    assert concatenate_string("String 1", " String 2") == "String 1 String 2"
    assert concatenate_string("", "Python") == "Python"
    assert concatenate_string("Py", "") == "Py"


def test_slice_string():
    assert slice_string("Hello, World!", 7, 12) == "World"
    assert slice_string("Python", 0, 3) == "Pyt"
    assert slice_string("Python", 3, 6) == "hon"


def test_find_substring():
    assert find_substring("Hello, World!", "World") == 7
    assert find_substring("Hello, World!", "Python") == -1
    assert find_substring("Python Programming", "Prog") == 7


def test_replace_substring():
    assert replace_substring("Hello, World!", "World", "Python") == "Hello, Python!"
    assert replace_substring("ababab", "a", "b") == "bbbbbb"
    assert replace_substring("ababab", "ab", "cd") == "cdcdcd"


def test_format_string():
    assert format_string("Hello", "Andy") == "Hello, Andy"
