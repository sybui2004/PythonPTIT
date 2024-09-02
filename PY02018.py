n = int(input())
arr = [int(i) for i in input().split()]
kt = 1
for i in range(1, n + 1):
    if i not in arr:
        kt = 0
        print(i)
        break
if kt: print(n + 1)