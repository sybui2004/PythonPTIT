def isPrime(n):
    if n == 2 or n == 3: return 1
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return 0
    
    if n > 1:
        return 1
    else:
        return 0

n, m = [int(i) for i in input().split()]
for i in range(n):
    arr = [isPrime(int(i)) for i in input().split()]
    print(*arr)