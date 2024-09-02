for t in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    
    if sum % 3 == 0: print("YES")
    else: print("NO")
    