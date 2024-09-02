def isPrime(n):
    if n == 2 or n == 3: return True
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    
    return n > 1

for t in range(int(input())):
    n = input()
    kt = 1
    for i in range(0, len(n)):
        if isPrime(i) == True:
            if n[i] != "2" and n[i] != "3" and n[i] != "5" and n[i] != "7":
                kt = 0
        else:
            if n[i] == "2" or n[i] == "3" or n[i] == "5" or n[i] == "7":
                kt = 0
    
    if kt: print("YES")
    else: print("NO")