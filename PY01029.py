import math
for t in range(int(input())):
    n = input()
    rev = n[::-1]
    n = int(n)
    rev = int(rev)
    if math.gcd(n, rev) == 1: print("YES")
    else: print("NO")