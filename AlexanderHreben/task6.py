# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.
x1 = 'Python is simple and effective!'
x2 = 'Any pythonista like namespaces a lot.'


def get_longest_word(data: str) -> str:
    check_list = data.split()
    return max(check_list, key=len)


if __name__ == '__main__':
    x1 = 'Python is simple and effective!'
    x2 = 'Any pythonista like namespaces a lot.'

    print(get_longest_word(x1))
    print(get_longest_word(x2))
