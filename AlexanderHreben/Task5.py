# Implement a decorator `remember_result` which remembers last result of function it decorates and prints it before next call.

def remember_result(func):
    def wrapper(*args):
        print(f"Last result = '{wrapper.last_result}'")
        current_result = func(*args)
        wrapper.last_result = current_result
        return current_result

    wrapper.last_result = None
    return wrapper


@remember_result
def sum_list(*args):
    result_str = ""
    result_int = 0
    if isinstance(args[0], int):
        for item in args:
            result_int += item
        print(f"Current result = '{result_int}'")
        return result_int
    else:
        for item in args:
            result_str += item
        print(f"Current result = '{result_str}'")
        return result_str


if __name__ == "__main__":
    sum_list("a", "b")
    # >> > "Last result = 'None'"
    # >> > "Current result = 'ab'"
    sum_list("abc", "cde")
    # >> > "Last result = 'ab'"
    # >> > "Current result = 'abccde'"
    sum_list(3, 4, 5)
    # >> > "Last result = 'abccde'"
    # >> > "Current result = '12'"
