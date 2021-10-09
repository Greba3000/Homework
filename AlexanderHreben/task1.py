# Implement class-based context manager for opening and working with file, including handling exceptions. Do not use 'with open()'. Pass filename and mode via constructor.
# from os.path import exists
#
# if not exists(file_name):
#     raise FileNotFoundError('File is not found!')


class ContManager:
    def __init__(self, file_path: str, mode='r'):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        print('ContManager.__enter__()')
        self.file = open(self.file_path, self.mode, encoding='utf-8')
        return self.file

    def __exit__(self, exception, value, traceback):  # exits from the context and handles exceptions
        """
        :param exception: Exception type or None.
        :param value: Exception object or None.
        :param traceback: Traceback object or None.
        """
        self.file.close()
        print(f'ContManager.__exit__{(exception, value, traceback)}')


if __name__ == '__main__':
    with ContManager('test1.txt', 'a') as cont:
        print(f'Inside the context resource = {cont}')
        #raise Exception('SomeError')

    # print('Not in context manager')
