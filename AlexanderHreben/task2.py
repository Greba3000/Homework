# Implement context manager for opening and working with file, including handling exceptions with @contextmanager decorator.
from contextlib import contextmanager


@contextmanager
def file_open(file_path, mode='r'):
    try:
        print('Opening file')
        file_obj = open(file_path, mode, encoding='utf-8')
        yield file_obj  # return
    except Exception as exc:
        print(f"We had an error - {exc} {type(exc)}")
    finally:
        print('Closing file')
        file_obj.close()


if __name__ == '__main__':
    with file_open('test1.txt', 'w') as file:
        print(f'Inside the context resource = {file}')
        raise Exception('SomeError')

    # print('Not in context manager')
