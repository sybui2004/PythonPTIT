import math
for t in range(int(input())):
    n = int(input())
    if n == 1:
        print(1)
        continue
    else:
        print(1, end = '')
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                cnt = 0
                while n % i == 0:
                    cnt += 1
                    n //= i
                print(' * ', end = '')
                print(i, end = '')
                print("^", end = '')
                print(cnt, end = '')
        if n > 1:
            print(' * ', end = '')
            print(n, end = '')
            print("^", end = '')
            print(1, end = '')
        print()
        
        