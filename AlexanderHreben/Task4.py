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
        print(f"{self.name} can walk")
        return f"{self.name} can walk"

    def walk(self):
        return print(f"{self.bird_name} bird can walk")


class FlyingBird(Bird):

    def __init__(self, name, ration='grains'):
        super().__init__(name)
        self.bird_ration = ration

    def __str__(self) -> str:
        print(f"{self.bird_name} can walk and fly")
        return f"{self.bird_name} can walk and fly"

    def fly(self):
        return print(f"{self.bird_name} bird can fly")

    def eat(self):
        return print(f"It eats mostly {self.bird_ration}")


class NonFlyingBird(Bird):

    def __init__(self, name, ration='fish'):
        super().__init__(name)
        self.bird_ration = ration

    def __str__(self) -> str:
        print(f"{self.bird_name} bird can walk and swim")
        return f"{self.bird_name} bird can walk and swim"

    def swim(self):
        return print(f"{self.bird_name} bird can swim")

    def eat(self):
        return print(f"It eats mostly {self.bird_ration}")


class SuperBird(NonFlyingBird, FlyingBird):

    def __str__(self) -> str:
        print(f"{self.bird_name} bird can walk, swim and fly")
        return f"{self.bird_name} bird can walk, swim and fly"

    def eat(self):
        return print(f"It eats {self.bird_ration}")


if __name__ == "__main__":
    b = Bird("Any")
    b.walk()
    print(dir(b))

    p = NonFlyingBird("Penguin", "fish")
    p.swim()
    # p.fly()
    p.eat()
    print(dir(p))

    c = FlyingBird("Canary")
    str(c)
    c.eat()
    print(dir(c))

    s = SuperBird("Gull")
    str(s)
    s.eat()
    print(dir(s))
