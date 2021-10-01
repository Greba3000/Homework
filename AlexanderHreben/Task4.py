# Create hierarchy out of birds.
# Implement 4 classes:
# * class `Bird` with an attribute `name` and methods `fly` and `walk`.
# * class `FlyingBird` with attributes `name`, `ration`, and with the same methods. `ration` must have default value.
# Implement the method `eat` which will describe its typical ration.
# * class `NonFlyingBird` with same characteristics but which obviously without attribute `fly`.
# Add same "eat" method but with other implementation regarding the swimming bird tastes.
# * class `SuperBird` which can do all of it: walk, fly, swim and eat.
# But be careful which "eat" method you inherit.

# Implement str() function call for each class.


class Bird:

    def __init__(self, name: str):
        self.bird_name = name

    def __str__(self) -> str:
        return f"{self.bird_name} can walk and fly"

    def walk(self):
        return f"{self.bird_name} bird can walk"

    def fly(self):
        return f"{self.bird_name} bird can fly"


class FlyingBird(Bird):

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.bird_ration = ration

    def eat(self):
        return f"It eats mostly {self.bird_ration}"


class NonFlyingBird(Bird):

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.bird_ration = ration

    def __str__(self) -> str:
        return f"{self.bird_name} bird can walk and swim"

    def __getattribute__(self, item):  # prohibits use fly
        if item == 'fly':
            raise AttributeError(f'{self.bird_name} object has no attribute {item}!!!')
        else:
            return object.__getattribute__(self, item)

    def swim(self):
        return f"{self.bird_name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.bird_ration}"


class SuperBird(NonFlyingBird, FlyingBird):

    def __str__(self) -> str:
        return f"{self.bird_name} bird can walk, swim and fly"

    def __getattribute__(self, item):  # allows use fly
        return object.__getattribute__(self, item)


if __name__ == "__main__":
    b = Bird("Any")
    print(f'{b.fly()}\n{b.walk()}')
    print(str(b))
    # print(dir(b))
    # print(Bird.__mro__)

    c = FlyingBird("Canary")
    print(str(c))
    print(c.fly())
    print(c.eat())
    # print(dir(c))
    # print(FlyingBird.__mro__)

    p = NonFlyingBird("Penguin", "fish")
    print(p.swim())
    print(p.eat())
    print(str(p))
    # p.fly()
    # print(dir(p))
    # print(NonFlyingBird.__mro__)

    s = SuperBird("Gull")
    print(str(s))
    print(f'{s.eat()}\n{s.fly()}\n{s.walk()}\n{s.swim()}')
    # print(dir(s))
    # print(SuperBird.__mro__)
