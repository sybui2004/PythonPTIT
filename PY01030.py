import math

n, k = map(int, input().split())
start = 10**(k-1)
end = 10**(k)
cnt = 0
kt = 0
for i in range(start, end):
    if math.gcd(n, i) == 1: 
        print(i, end = ' ')
        cnt += 1
        kt = 1
    if cnt % 10 == 0 and kt == 1:
        print()
        kt = 0
    