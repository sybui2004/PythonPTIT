from math import gcd

class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self):
        tmp = gcd(self.numerator, self.denominator)
        self.numerator //= tmp
        self.denominator //= tmp
    
    def add(self, x) :
        new_numerator = self.denominator * x.numerator + x.denominator * self.numerator
        new_denominator = self.denominator * x.denominator
        self.numerator = new_numerator
        self.denominator = new_denominator
    
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

ip = [int(i) for i in input().split()]
p = Fraction(ip[0], ip[1])
q = Fraction(ip[2], ip[3])
p.add(q)
p.simplify()
print(p)
