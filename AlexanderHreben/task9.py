# Implement a bunch of functions which receive a changeable number of strings and return next parameters:
# 1) characters that appear in all strings
# 2) characters that appear in at least one string
# 3) characters that appear at least in two strings
# 4) characters of alphabet, that were not used in any string
# Note: use string.ascii_lowercase for list of alphabet letters

import string


def test_1_1(*args: str) -> set:
    print(type(string.ascii_lowercase), string.ascii_lowercase)
    out = set(string.ascii_lowercase)
    return out.intersection(*args)  # set.intersection() return set that contains the items that exist in all set


def test_1_2(*args: str):
    out = set()
    out.update(*args)
    return out


def test_1_3(*args: str):
    out = set()
    for num_str in range(len(args)):
        for elem in range(num_str):
            out.update(set(args[num_str]).intersection(set(args[elem])))
    return out


def test_1_4(*args: str):
    return set(string.ascii_lowercase).difference(*args)


if __name__ == '__main__':
    print(test_1_1("hello", "world", "python"))
    print(test_1_2("hello", "world", "python"))
    print(test_1_3("hello", "world", "python"))
    print(test_1_4("hello", "world", "python"))
