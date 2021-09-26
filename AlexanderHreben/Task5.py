# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple of a given integer's digits.


def get_digits(data: int) -> tuple[int]:
    out = tuple([int(num) for num in str(data)])  # int is not iterable
    return out


if __name__ == '__main__':
    x = 19234567
    print(get_digits(x))
