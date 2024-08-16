for t in range(int(input())):
    str = input()
    check = 1
    for i in str:
        if i != '4' and i != '7': check = 0

    if check == 1: print("YES")
    else: print("NO")