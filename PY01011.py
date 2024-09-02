for t in range(int(input())):
    n = int(input())
    queue = []
    list = [0, 2, 4, 6, 8]
    for i in list:
        if i != 0: queue.append(i)
    
    while len(queue) != 0:
        tmp = queue.pop(0)
        if int(str(tmp) + str(tmp)[::-1]) < n: print(str(tmp) + str(tmp)[::-1], end = ' ')
        for i in list:
            val = tmp * 10 + i
            if int(str(val) + str(val)[::-1]) < n: queue.append(val)
            else: break
    print()