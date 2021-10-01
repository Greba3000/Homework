# A singleton is a class that allows only a single instance of itself to be created and gives access to that created instance.
# Implement singleton logic inside your custom class using a method to initialize class instance.


class Singleton:  # class Singleton(object): for __init__
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


if __name__ == "__main__":
    p = Singleton()
    f = Singleton()
    z = Singleton()
    print(p is f, z is f)
