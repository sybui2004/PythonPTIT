def Try(n, st, en, tmp):
    if n == 1:
        print(f"{st} -> {en}")
    else:
        Try(n-1, st, tmp, en)
        print(f"{st} -> {en}")
        Try(n-1, tmp, en, st)


n = int(input())
Try(n, 'A', 'C', 'B')
