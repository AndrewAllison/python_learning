"""
Some examples of string usage in python
"""

SIMPLE_STRING = "I am a mere simple string"
QUOTES_IN_STRING = "He is called 'Johnny'"


def demonstrate_strings():
    """
    this is a simple demo method
    :return:
    """
    print(SIMPLE_STRING)
    print(QUOTES_IN_STRING)


def concatenate_string(string1, string2):
    """
    Function to concatenate 2 strings together

    :param string1: string - First string to concat
    :param string2: string - Second string that will be concatenated
    :return: string - representation of the two concatenated strings
    """
    return string1 + string2


def slice_string(base_string, start, end):
    """
    Slices a string with a start and end point

    :param base_string: string - The string to be sliced
    :param start: int - the start index of the slice
    :param end: int - the end index of the slice
    :return: string - A sliced string of the desired params
    """
    return base_string[start:end]


def find_substring(s, substring):
    return s.find(substring)


def replace_substring(s, old, new):
    return s.replace(old, new)


def format_string(s, name):
    return f"{s}, {name}"


if __name__ == "__main__":
    demonstrate_strings()
