# Create a program that asks the user for a number and then prints out a list of all the [divisors](https://en.wikipedia.org/wiki/Divisor) of that number.


def divisors(num: int) -> list:
    output_divisors = [i for i in range(1, num + 1) if num % i == 0]
    return output_divisors


if __name__ == '__main__':
    print(f'Input some number -')
    num1 = int(input())
    print(divisors(num1))
