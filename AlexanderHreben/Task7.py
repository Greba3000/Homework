# Implement a class Money to represent value and currency.
# You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication, addition and subtraction).
# Tip: use class attribute exchange rate which is dictionary and stores information about exchange rates to your default currency:
from functools import total_ordering


@total_ordering  # generate __gt__, __le__, __ge__
class Money:
    exchange_rate_USD = {
        "USD": 1,
        "EUR": 0.93,
        "BYN": 2.1,
        "JPY": 111.53
    }

    def __init__(self, value: (int, float), type_cur='USD'):
        self.value = value
        self.type_cur = type_cur
        self.rate = Money.exchange_rate_USD[type_cur]
        if self.type_cur not in Money.exchange_rate_USD:
            raise AttributeError(f"{self.type_cur} - Unknown type of currency")

    def __eq__(self, other):  # comparison
        if isinstance(other, (int, float)):
            return self.value == other
        elif isinstance(other, Money):
            return self.value == (other.value / other.rate) / self.rate

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.value < other
        elif isinstance(other, Money):
            return self.value < other.value * (self.rate / other.rate)

    def __add__(self, other):  # addition
        print(f'in __add__ - {other} - {self.value}')
        if isinstance(other, (int, float)):
            return Money(self.value + other, self.type_cur)
        elif isinstance(other, Money):
            return Money(self.value + (other.value / other.rate) * self.rate, self.type_cur)

    def __radd__(self, other):
        print(f'in __radd__ - {other} - {self.value}')
        return Money(other + self.value, self.type_cur)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value - other, self.type_cur)
        elif isinstance(other, Money):
            return Money(self.value - (other.value / other.rate) * self.rate, self.type_cur)

    def __rsub__(self, other):
        return Money(other - self.value, self.type_cur)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Money(self.value * other, self.type_cur)
        elif isinstance(other, Money):
            return Money(self.value * ((other.value / other.rate) * self.rate), self.type_cur)

    def __rmul__(self, other):
        return Money(other * self.value, self.type_cur)

    def __repr__(self):
        return f"{self.value:.2f} - {self.type_cur}"

        # division,
        # multiplication
        # subtraction


if __name__ == "__main__":
    x = Money(10, 'BYN')
    y = Money(11)  # define your own default value, e.g. “USD”
    z = Money(12.34, "EUR")

    # print(x == y)  # y.__eq__(x)
    # print(x + y)
    # print(y + x)
    # print(x + 10)
    # print (x.__radd__(10))
    # print(10 + x)

    # print(x * y)
    # print(y * x)
    # print(x * 10)
    # print(10 * x)

    # print(z + 3.11 * x + y * 0.8)

    print(x+y+z)
    lst = [Money(10, "BYN"), Money(11), Money(12.01, "JPY")] # why first radd??
    print(sum(lst))
