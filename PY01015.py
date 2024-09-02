for t in range(int(input())):
    ip = input()
    kt = 1
    for i in range(0, len(ip) - 1):
        if ip[i] > ip[i+1]: kt = 0
    if kt == 1: print("YES")
    else: print("NO")