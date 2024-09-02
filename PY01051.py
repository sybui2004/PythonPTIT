for t in range(int(input())):
    n = input()
    sum = 0
    for i in n:
        sum += int(i)
    
    
    if str(sum) == str(sum)[::-1] and len(str(sum)) > 1: print("YES")
    else: print("NO")