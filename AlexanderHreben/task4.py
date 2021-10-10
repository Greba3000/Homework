# Implement decorator for supressing exceptions. If exception not occure write log to console.

def supressing_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(f'We had exception - {exc} {type(exc)} in {func}')
    return wrapper


@supressing_exceptions
def func1(num):
    x = num / 0
    print("I'm here! func1")  # how it print? Neither because except stops script execution

def func2():
    print("I'm here! func2")

if __name__ == '__main__':
    func1(1)
    func2()
