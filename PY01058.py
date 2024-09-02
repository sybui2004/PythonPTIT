def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

for t in range(int(input())):
    n = input()
    if isPrime(int(n[len(n) - 4: len(n)])): print("YES")
    else: print("NO")