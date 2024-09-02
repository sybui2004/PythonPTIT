import math

def isPrime(n):
    if n == 2 or n == 3: return True
    if n == 1 or n % 2 == 0: return False
    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
        
    return True

def sum_digit(n):
    ans = 0
    while n > 0:
        ans += n % 10
        n //= 10
    return ans
for t in range(int(input())):
    a, b = [int(i) for i in input().split()]
    if isPrime(sum_digit(math.gcd(a, b))): print("YES")
    else: print("NO")