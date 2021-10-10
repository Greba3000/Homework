# Implement function for check that number is even, at least 3. Throw different exceptions for this errors.
# Custom exceptions must be derived from custom base exception(not Base Exception class).

class MyException(Exception):
    pass


class MyTypeError(MyException):
    pass


class MyValueError(MyException):
    pass


def is_num_even(num: int) -> bool:
    if not isinstance(num, int):
        raise MyTypeError(f'"{num}" - incorrect data type! You can use only integer.')
    elif num <= 3:
        raise MyValueError(f'"{num}" - incorrect data value! You can use only integer more than 3.')
    elif num % 2 != 0:
        raise MyValueError(f'"{num}" - incorrect data value! You can use only EVEN integer.')
    return True


if __name__ == "__main__":
    print(is_num_even(5))
