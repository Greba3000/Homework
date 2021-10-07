# Implement a decorator `call_once` which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments.

def call_once(func):
    def wrapper(*args):
        if wrapper.args:
            return func(*wrapper.args)
        wrapper.args = args
        return func(*args)

    wrapper.args = None
    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


print(sum_of_numbers(14, 42))
# >>> 55
print(sum_of_numbers(999, 100))
# >>> 55
print(sum_of_numbers(134, 412))
# >>> 55
print(sum_of_numbers(856, 232))
# >>> 55
