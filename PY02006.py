for t in range(int(input())):
    kt = 1
    n = int(input())
    a = sorted([int(x) for x in input().split()])
    b = sorted([int(x) for x in input().split()])
    for i in range(n) :
        if a[i] > b[i] :
            kt = 0
            break
    if kt == 1 : print("YES")
    else : print("NO")