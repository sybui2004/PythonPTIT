for t in range(int(input())):
    n = input()
    if len(n) < 3: 
        print("NO")
        continue
    pos = 0
    while pos < len(n) - 1:
        if n[pos] < n[pos + 1]:
            pos += 1
        else: break
    kt = 0
    while pos < len(n) - 1:
        if n[pos] <= n[pos + 1]:
            kt = 1
            break
        pos += 1
    if kt == 0: print("YES")
    else: print("NO")