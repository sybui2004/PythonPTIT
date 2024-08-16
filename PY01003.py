for t in range(int(input())):
    list = [int(i) for i in input()]
    for i in range(len(list) - 1, 0, -1):
        if list[i] >= 5:
            list[i - 1] = list[i - 1] + 1
        list[i] = 0
    if list[0] == 10:
        list[0] = 0
        list = [1] + list
    s = ""
    for i in list:
        s += str(i)
    print(s)
