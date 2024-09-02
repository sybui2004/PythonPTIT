import math
a, K, N = [int(i) for i in input().split()]
tmp = math.ceil(a / K)
b = K * tmp - a
if b == 0: b += K
if a + b > N: print(-1)
else : 
    while a + b <= N:
        print(b, end = ' ')
        b += K