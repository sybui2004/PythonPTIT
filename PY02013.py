while True:
    n = int(input())
    if n == 0:
        break
    ans = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else: 
            n = (3 * n + 1)
        ans += 1
    print(ans)