def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

for t in range(int(input())):
    ip = input()
    if isPrime(int(ip[0:3])) and isPrime(int(ip[len(ip) - 3: len(ip)])): print("YES")
    else: print("NO")