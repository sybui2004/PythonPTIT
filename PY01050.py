n = int(input())
def check(s):
    cntA = 0
    cntB = 0
    cntC = 0
    for i in s:
        if i == "A":
            cntA += 1
        elif i == "B":
            cntB += 1
        else:
            cntC += 1
    
    return cntA > 0 and cntB > 0 and cntC > 0 and (cntA <= cntB) and (cntB <= cntC)

results = []

def custom_sort(arr):
    def custom_key(x):
        return (len(x), x)

    return sorted(arr, key=custom_key)

def Try(i):
    if len(i) <= n and check(i):
        results.append(i)
    if len(i) > n:
        return
    Try(i + "A")
    Try(i + "B")
    Try(i + "C")

Try("A")
Try("B")
Try("C")

results = custom_sort(results)

for i in results:
    print(i)
