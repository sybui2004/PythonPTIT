for t in range(int(input())):
    n = int(input())
    list = [int(i) for i in input().split()]
    list.sort()
    ans = 0
    for i in range(n - 2):
        l, r = i + 1, n - 1
        while l < r:
            total = list[i] + list[l] + list[r]
            if total == 0:
                ans += 1
                l += 1
            elif total < 0:
                l += 1
            else:
                r -= 1
    print(ans)