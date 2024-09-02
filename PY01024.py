def sum_digit(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def check(n):
    n = str(n)
    for i in range(0, len(n) - 1):
        if abs(ord(n[i]) - ord(n[i+1])) != 2:
            return False
    return True
for t in range(int(input())):
    n = int(input())
    if sum_digit(n) % 10 == 0 and check(n): print("YES")
    else: print("NO")
    