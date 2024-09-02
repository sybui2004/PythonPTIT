def Try(i, arr):
    if len(arr) == k:
        print(*arr)
        return
    for j in range(i, n):
        Try(j + 1, arr + [list[j]])


n, k = [int(i) for i in input().split()]
list = sorted(set({int(i) for i in input().split()}))
n = len(list)

Try(0, [])