n = int(input())
arr = [int(i) for i in input().split()]
cnt = 0
for i in range(0, n-1):
    if arr[i] != arr[i+1]:
        cnt += 1
print(cnt)