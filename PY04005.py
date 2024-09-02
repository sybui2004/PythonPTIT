from math import sqrt

class Point :
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, k) :
        xx = self.x - k.x
        yy = self.y - k.y
        dist = sqrt(xx * xx + yy * yy)
        return dist

class Triangle :
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def perimeter(self) :
        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p1.distance(self.p3)
        if(max(a, b, c) * 2 >= a + b + c) : print("INVALID")
        else : print(f"{(a + b + c):.3f}")

a = []
t = int(input())
for x in range(t):
    a += [float(i) for i in input().split()]
i = 0
for index in range(t):
    triagle = Triangle(Point(a[i], a[i+1]), Point(a[i+2], a[i+3]), Point(a[i+4], a[i+5]))
    triagle.perimeter()
    i += 6
