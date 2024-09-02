for t in range(int(input())):
    ip = input()
    n = len(ip) 
    if ip[0:2] == ip[n-2:n]: print("YES")
    else: print("NO")