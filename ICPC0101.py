n = int(input())
list = [int(i) for i in input().split()]
i = 0
while i < len(list) - 1:
    if (list[i] + list[i + 1]) % 2 == 0:
        list.pop(i + 1)
        list.pop(i)
        if i > 0:
            i -= 1
    else:
        i += 1
print(len(list))   