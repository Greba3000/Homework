# Implement decorator with context manager support for writing execution time to log-file. See contextlib module.
import time
from contextlib import ContextDecorator


class contextmanager_with_writing_exe_time(ContextDecorator):

    def __init__(self, file_path: str, mode='a'):  # pass func?
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.start_time = time.perf_counter()  # self.start_time.time()
        self.file = open(self.file_path, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exception, value, traceback):  # exits from the context and handles exceptions
        self.stop_time = time.perf_counter()
        self.file.write(f'{self.stop_time - self.start_time:.6f} sec\n')
        self.file.close()
        print(f'ContManager.__exit__{(exception, value, traceback)}')


@contextmanager_with_writing_exe_time('log.txt')
def func1(num):
    return [i for i in range(num)]


@contextmanager_with_writing_exe_time('log.txt')
def func3(num):
    return [i + 1 for i in range(num)]


@contextmanager_with_writing_exe_time('log.txt')
def func2(num):
    list = []
    for i in range(num):
        list.append(i)
    return list


if __name__ == "__main__":
    func1(5)
    print(func1(5))
    func2(5)
    func3(5)
