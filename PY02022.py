def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

n = int(input())
a = [int(i) for i in input().split()]
dd = {}
for i in a:
    if isPrime(i):
        if i in dd:
            dd[i] += 1
        else:
            dd[i] = 1
for i in dd:
    print(i, end =" ")
    print(dd[i])