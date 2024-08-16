import math as m

kt = [1]*int(1e6 + 5)
kt[0] = kt[1] = 0
for i in range(int(m.sqrt(1e6 + 5))):
    if kt[i]:
        for j in range(i*i, int(1e6 + 5), i):
            kt[j] = 0
            
for t in range(int(input())):
    n = int(input())
    ans = 0
    for i in range(n-5):
        if kt[i] and kt[i+6]:
            if kt[i+2] or kt[i+4]:
                ans += 1
    print(ans)
    