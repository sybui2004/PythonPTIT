for t in range(int(input())):
    ip = input()
    kt = 0
    chan = 0
    le = 1
    for i in range(len(ip)):
        if i % 2 == 0:
            chan += int(ip[i])
        else:
            if ip[i] != "0":
                kt = 1
                le *= int(ip[i])
    print(chan, end = ' ')
    if kt == 0:
        print(0)
    else:
        print(le)