# Implement a function that takes a number as an argument and returns a dictionary, where the key is a number and the value is the square of that number.


def generate_squares(num_data: int) -> dict:
    out = dict()
    for i in range(1, num_data + 1):
        out[i] = i ** 2
    return out


if __name__ == '__main__':
    print(generate_squares(2))
