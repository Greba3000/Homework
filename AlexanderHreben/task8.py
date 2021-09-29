# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.


def get_pairs(data: list) -> list[tuple]:
    out = list()
    if len(data) == 1:
        return
    else:
        for num in range(len(data) - 1):
            out.append(tuple([data[num], data[num + 1]]))
        return out


if __name__ == '__main__':
    x1 = [1, 2, 3, 8, 9]
    x2 = ['need', 'to', 'sleep', 'more']
    x3 = [1]

    print(get_pairs(x1))
    print(get_pairs(x2))
    print(get_pairs(x3))
