import math as m

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

for t in range(int(input())):
    n = int(input())
    check = 0
    sum = 0
    for i in str(n):
        sum += factorial(int(i))
    
    if sum == n: print("Yes")
    else: print("No")
    
    
        
    