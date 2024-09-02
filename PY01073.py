def Try(str):
    if len(str) == n:
        print(str)
        return
    for i in range(n):
        if visited[i]:
            visited[i] = 0
            Try(str + ip[i])
            visited[i] = 1


ip = input()
n = len(ip)
visited = [1] * (n+1)
Try("")