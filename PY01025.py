ip = input()
tmp = ip[::-1]
ans = ""
for i in range(0, len(tmp)):
    ans += tmp[i]
    if (i + 1) % 3 == 0 and i != len(tmp) - 1:
        ans += ','

print(ans[::-1])