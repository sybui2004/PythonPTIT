for t in range(int(input())) :
    n, m = [int(x) for x in input().split()]
    a = [[] * m] * n
    for i in range(n) :
        a[i] = [int(x) for x in input().split()]
    aT = []
    
    for i in range(m) :
        x = []
        for j in range(n) :
            x.append(a[j][i])
        aT.append(x)
    
    for i in range(n) :
        for j in range(n) :
            s = 0
            for z in range(m) :
                s += a[i][z] * aT[z][j]
            print(s, end = ' ')
        print()