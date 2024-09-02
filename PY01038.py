for t in range(int(input())):
    n = int(input())
    cnt = 0
    while n % 7 != 0 and cnt < 1000:
        n = str(n)
        tmp = n[::-1]
        n = int(n) + int(tmp)
    if n % 7 == 0: print(n)
    else: print(-1)        