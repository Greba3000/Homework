#  Write a Python program to convert a given tuple of positive integers into an integer.


def tuple_to_str(data: tuple) -> int:
    string = ''
    for elem in data:
        string += str(elem)
    return int(string)


if __name__ == "__main__":
    t = (1, 2, 3, 4)
    print(f'Num {tuple_to_str(t)} have {type(tuple_to_str(t))}')
