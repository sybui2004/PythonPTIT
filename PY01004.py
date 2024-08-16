import math

def isPrime(n):
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n == 1: return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for t in range(int(input())):
    n = int(input())
    k = 0
    
    for i in range(1, n):
        if math.gcd(n, i) == 1: k += 1
        
    if isPrime(k): print('YES')
    else: print('NO')