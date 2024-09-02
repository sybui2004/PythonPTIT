for t in range(int(input())):
    n = input()
    if len(n) % 2 == 0:
        print("NO")
        continue
    
    sz = len(n)
    
    if n[0] == n[1]:
        print("NO")
        continue
    
    kt = 1
    for i in range(0, sz-2):
        if i % 2 == 0 and n[i] != n[i+2]:
            kt = 0
            break
    
    if kt:
        print("YES")
    else:
        print("NO")

    