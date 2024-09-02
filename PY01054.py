for t in range(int(input())):
    n = input()
    ans = 1
    for i in n:
        if i != "0":
            ans *= int(i)
    
    print(ans)