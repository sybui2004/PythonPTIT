for t in range(int(input())):
    n = input()
    if len(n) % 2 == 0:
        n += n[len(n) - 2]
    if n == n[::-1]: print("YES")
    else: print("NO")