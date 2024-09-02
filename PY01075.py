from math import gcd

def solve(n, a, c):
    arr = {0: 0} 
    b = [0]  
    
    for i in range(n):
        next_arr = arr.copy() 
        for p in b:
            d = gcd(p, a[i])
            cost = arr.get(p, float('inf')) + c[i]
            if d not in next_arr or next_arr[d] > cost:
                next_arr[d] = cost
                b.append(d)
        arr = next_arr
    
    return arr.get(1, -1)

for t in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    print(solve(n, a, c))