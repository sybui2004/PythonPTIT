import math as m

base_str = '0123456789ABCDEF'

t = int(input())
for tt in range(t):
    b = int(m.log2(int(input())))
    str = input()
    while len(str) % b:
        str = '0' + str
    pow = [1, 2, 4, 8]
    
    ans = ''
    for i in range(0, len(str), b):
        tmp = 0
        for j in range(i + b, i, -1):
            tmp += int(str[2*i + b - j])*pow[j - i - 1]
        ans += base_str[tmp]
    print(ans)