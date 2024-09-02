from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        tmp = gcd(self.numerator, self.denominator)
        self.numerator //= tmp
        self.denominator //= tmp

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

numerator, denominator = [int(i) for i in input().split()]
fraction = Fraction(numerator, denominator)
fraction.simplify()
print(fraction)
