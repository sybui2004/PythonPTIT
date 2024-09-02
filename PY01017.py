for t in range(int(input())):
    ip = input()
    ip += "*"
    cnt = 1
    for i in range(len(ip)-1):
        if ip[i] == ip[i+1]:
            cnt += 1
        else:
            print(cnt, end = '')
            print(ip[i], end = '')
            cnt = 1
    print()  