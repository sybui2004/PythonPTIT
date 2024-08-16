for t in range(int(input())):
    p, q = input().split()
    list = input().split()
    if len(list) == 2:
        x1, x2 = list
    else:
        x1 = list[0]
        x2 = input()
    val1 = int(x1.replace(p, q)) + int(x2.replace(p, q))
    val2 = int(x1.replace(q, p)) + int(x2.replace(q, p))
    if p > q:
        print(val1, val2)
    else:
        print(val2, val1)
    
    
    