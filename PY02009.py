for t in range(int(input())):
    n = int(input())
    dict_num = {}
    cnt = 0
    for i in range(n):
        x = int(input())
        if x in dict_num:
            dict_num[x] += 1
        else:
            dict_num[x] = 1
        cnt = max(cnt, dict_num[x])
    ans = 1000
    for i in dict_num:
        if dict_num[i] == cnt:
            ans = min(ans, i)
    print(ans)