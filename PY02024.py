

def mul_digits(n):
    sum = 1
    while n > 0:
        sum *= n % 10
        n //= 10
    return sum

for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    sorted_arr = sorted(arr, key = lambda x: (mul_digits(x), x))
    print(*sorted_arr)
    