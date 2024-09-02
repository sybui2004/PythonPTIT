def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

for t in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    
    if isPrime(sum):
        print("YES")
    else:
        print("NO")