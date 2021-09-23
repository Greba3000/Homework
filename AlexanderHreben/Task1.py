# Write a Python program to calculate the length of a string without using the `len` function.


def my_len(data: str) -> int:
    num = 0
    for i in data:
        num += 1
    return num


if __name__ == '__main__':
    x = '1$Nf/.,89'
    print(my_len(x))
