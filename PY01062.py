def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

def check(n):
    cntPrime = 0
    for i in n:
        if i == "2" or i == "3" or i == "5" or i == "7": cntPrime += 1
    return 2 * cntPrime > len(n)

for t in range(int(input())):
    ip = input()
    if isPrime(len(ip)) and check(ip): print("YES")
    else: print("NO")