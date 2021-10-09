# Implement your custom iterator class called MySquareIterator which gives squares of elements of collection it iterates through.


class MySquareIterator:

    def __init__(self, data):
        self.data = data
        # self.index = 0 # после первой итерации значение индекса уйдет за ренж

    def __iter__(self):
        print("I'm here!__iter__")
        self.index = 0
        return self

    def __next__(self):
        print("I'm here!__next__")
        if self.index >= len(self.data):
            raise StopIteration
        res = self.data[self.index] ** 2
        self.index += 1
        return res


if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)
    for item in itr:
        print(item)
