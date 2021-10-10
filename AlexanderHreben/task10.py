# Implement a generator which will generate odd numbers endlessly.

def endless_generator():
    out_num = 1
    while True:
        yield out_num
        out_num += 2


if __name__ == "__main__":
    gen = endless_generator()
    # while True:
    #     print(next(gen))
    for i in range(20):
        print(next(gen), end=" ")
