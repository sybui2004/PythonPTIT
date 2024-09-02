for t in range(int(input())) :
    n, m = [int(x) for x in input().split()]
    x = [[]] * n
    h = [[]] * 3
    ans = 0
    for i in range(n): 
        x[i] = [int(x) for x in input().split()]
    for i in range(3): 
        h[i] = [int(x) for x in input().split()]
    for i in range(1, n-1) :
        for j in range(1, m-1) :
            ans += x[i - 1][j - 1] * h[0][0] 
            ans += x[i - 1][j] * h[0][1]
            ans += x[i - 1][j + 1] * h[0][2]
            ans += x[i][j - 1] * h[1][0]
            ans += x[i][j] * h[1][1]
            ans += x[i][j + 1] * h[1][2]
            ans += x[i + 1][j - 1] * h[2][0]
            ans += x[i + 1][j] * h[2][1]
            ans += x[i + 1][j + 1] * h[2][2]
    print(ans)