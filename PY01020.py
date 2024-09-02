for t in range(int(input())):
    ip = input()
    if ip[len(ip) - 2: len(ip)] == '86': print("YES")
    else: print("NO")