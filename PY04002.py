class Rectangle :
    def __init__(self, w, h, color) :
        self.w = w
        self.h = h
        self.color = color[0:1:].upper() + color[1::].lower()

    def is_valid(self):
        if self.w <= 0 or self.h <= 0 : return 0
        return 1
    
    def output(self) :
        if self.is_valid() == 1 : print((self.w + self.h) * 2, self.w * self.h, self.color, sep = ' ')
        else : print('INVALID')
        
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
r.output()
