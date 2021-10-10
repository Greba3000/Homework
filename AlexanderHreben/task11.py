# Implement a generator which will geterate [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) endlessly.

def endless_fib_generator():
    fib1 = fib2 = 1
    while True:
        yield fib1
        fib1, fib2 = fib2, fib1 + fib2


if __name__ == "__main__":
    gen = endless_fib_generator()
    # while True:
    #     print(next(gen))
    for i in range(20):
        print(next(gen), end=" ")
