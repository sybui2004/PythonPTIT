P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."

while True:
    
    ip = input().split()
    n = int(ip[0])
    if n == 0:
        break
    
    ans = ""
    for i in range(len(ip[1])):
        id = P.index(ip[1][i])
        ans += P[(id+n) % 28]
    print(ans[::-1])