def isPrime(n):
    if n == 2 or n == 3: return True
    if n == 1 or n % 2 == 0: return False
    for i in range(5, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        
    return True

for t in range(int(input())):
    n = input()
    if isPrime(len(n)) == False:
        print("NO")
        continue
    
    cnt = 0
    
    for i in n:
        if i == "2" or i == "3" or i == "5" or i == "7":
            cnt += 1
    
    if len(n) >= 2 * cnt:
        print("NO")
        continue

    print("YES")