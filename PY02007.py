length = 0
du = [0] * 42
while True :
    a = [int(i) for i in input().split()]
    for i in a :
        du[i % 42] = 1
    length += len(a)
    if length == 10 :
        break
ans = 0
for i in du :
    if i :
        ans += 1
print(ans)