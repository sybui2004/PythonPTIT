for t in range(int(input())):
    n, d = [int(i) for i in input().split()]
    list = input().split()
    print(*list[d:] + list[0: d])