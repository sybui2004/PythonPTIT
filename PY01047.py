def isPrime(n):
    if n == 2 or n == 3: return True
    if n == 1 or n % 2 == 0: return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

for t in range(int(input())):
    n = input()
    val = n[len(n)-4: len(n)]
    val = int(val)
    if isPrime(val): print("YES")
    else: print("NO")