# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.

import math


def product_all_num(data: list[int]) -> list[int]:
    out = list()
    for num in data:
        out.append(int(math.prod(data) / num))  # / return float
    return out


if __name__ == '__main__':
    x1 = [1, 2, 3, 4, 5]
    x2 = [3, 2, 1]

    print(product_all_num(x1))
    print(product_all_num(x2))
