while True:
    arr = [int(i) for i in input().split()]
    if arr.count(0) == 4:
        break
    ans = 0
    while arr.count(arr[0]) != 4:
        tmp = arr.copy()
        for i in range(4):
            arr[i] = abs(tmp[i] - tmp[(i + 1) % 4])
        ans += 1
    print(ans)