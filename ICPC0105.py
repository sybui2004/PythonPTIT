t = int(input())
for tt in range(t):
    s = input()
    ans = 0
    n = 0
    for i in range(len(s)):
        if s[i].isalpha():
            if i > 0 and s[i-1].isdigit(): ans = max(ans, n)
            n = 0
        else:
            n = n * 10 + int(s[i])
    if s[len(s)-1].isdigit(): ans = max(ans, n)
    print(ans)
        