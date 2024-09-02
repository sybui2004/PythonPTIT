def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

n, x = [int(i) for i in input().split()]
cnt = 2
n += 1
while n > 0:
    print(x, end = ' ')
    while isPrime(cnt) != True:
        cnt += 1
    x +=cnt
    cnt += 1
    n -= 1