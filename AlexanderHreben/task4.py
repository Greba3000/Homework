# Implement decorator for supressing exceptions. If exception not occure write log to console.

def supressing_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as exc:
            print(f'We had exception - {exc} {type(exc)}')
    return wrapper


@supressing_exceptions
def func(num):
    x = num / 0
    print("I'm here!")  # how it print?


if __name__ == '__main__':
    func(1)
