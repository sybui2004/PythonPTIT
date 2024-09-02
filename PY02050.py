for t in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    st = []
    ans = [0] * n
    for i in range(n):
        while len(st) > 0 and arr[st[-1]] <= arr[i]:
            st.pop()
        if len(st) == 0:
            ans[i] = i + 1
        else:
            ans[i] = i - st[-1]
        st.append(i)
    print(*ans)