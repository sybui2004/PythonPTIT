for t in range(int(input())):
    ip = input()
    ip = ip + "*"
    cnt = 0
    c = ip[0]
    for i in ip[1:]:
        if i.isdigit():
            cnt = cnt * 10 + int(i)
        else:
            for j in range(cnt):
                print(c, end='')
            cnt = 0
            c = i
    print()