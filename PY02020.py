n = int(input())
a = [float(i) for i in input().split()]
ma, mi = max(a), min(a)
ans = 0
cnt = 0
for i in a:
    if i != ma and i != mi:
        ans += i
        cnt += 1
ans /= cnt
print(f"{ans:.2f}")