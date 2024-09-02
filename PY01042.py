for t in range(int(input())):
    n = input()
    kt = 1
    for i in n:
        if i != "0" and i != "1" and i != "2":
            kt = 0
            break
        
    if kt: print("YES")
    else: print("NO")