class MyNumberCollection:

    def __init__(self, start: int, end=None, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.collection = self.create_collection(start, end, step)

    def __repr__(self):
        return str(self.collection)

    def __add__(self, other):
        return self.collection + other.collection

    def __getitem__(self, index):
        return self.collection[index] ** 2

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.collection):
            raise StopIteration
        res = self.collection[self.index]
        self.index += 1
        return res

    @staticmethod
    def create_collection(start, stop, step):
        out_collection = list()
        if isinstance(start, tuple):
            for elem_tuple in start:
                MyNumberCollection.is_elem_int(elem_tuple)
            out_collection = list(start)
        else:
            MyNumberCollection.is_elem_int(start, stop, step)
            out_collection = list(range(start, stop, step))
            if stop not in out_collection:
                out_collection.append(stop)
        return out_collection

    @staticmethod
    def is_elem_int(*elem):
        for i in elem:
            if not isinstance(i, int):
                raise TypeError(f'"{i}" is not integer. You can use only integer!')

    def append(self, data):
        MyNumberCollection.is_elem_int(data)
        self.collection.append(data)


if __name__ == "__main__":
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
    # col3 = MyNumberCollection((1, 2, 3, "4", 5))
    col1.append(7)
    print(col1, type(col1))
    print(col1 + col2)
    print(col2 + col1, type(col2 + col1))

    print(col1)
    print(col2)
    print(col2[4])
    for item in col1:
        print(item)
