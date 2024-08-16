import math as m

kt = [1]*int(1e6 + 5)
kt[0] = kt[1] = 0
for i in range(int(m.sqrt(1e6 + 5))):
    if kt[i]:
        for j in range(i*i, int(1e6 + 5), i):
            kt[j] = 0
    
for t in range(int(input())):
    n = int(input())
    list = []
    for i in range(1, n):
        if kt[i] and kt[int(str(i)[::-1])] and i != int(str(i)[::-1]) and int(str(i)[::-1]) <= n:
            if i not in list: list.append(i)
            if int(str(i)[::-1]) not in list: list.append(int(str(i)[::-1]))
    
    print(*list)
        
    