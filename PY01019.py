for t in range(int(input())):
    s1 = input()
    s2 = s1[::-1]
    check = 1
    for i in range(len(s1) - 1):
        if abs(ord(s1[i]) - ord(s1[i+1])) != abs(ord(s2[i]) - ord(s2[i+1])): check = 0
    
    if check == 1: print("YES")
    else: print("NO")