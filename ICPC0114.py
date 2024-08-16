import math as m

def isPrime(n):
    if n == 2 or n== 3: return True
    if n % 2 == 0 or n == 1: return False
    for i in range(5, int(m.sqrt(n)), 2):
        if n % i == 0: return False
    
    return True

def sum_digit(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans
for t in range(int(input())):
    n = int(input())
    check = 0
    if isPrime(n) and isPrime(int(str(n)[::-1])) and isPrime(sum_digit(n)):
        for i in str(n):
            if i == '2' or i == '3' or i == '5' or i == '7': check = 1
            else: check = 0
    
    if check == 1: print("Yes")
    else: print("No")
    
    
        
    