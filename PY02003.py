import heapq

hamming_set = set()
heap = []
order = {}

heapq.heappush(heap, 1)
hamming_set.add(1)
count = 1

while heap:
    val = heapq.heappop(heap)
    order[val] = count
    count += 1
    
    if val > 10**18:
        break
    
    for i in [2, 3, 5]:
        new_val = val * i
        if new_val not in hamming_set:
            hamming_set.add(new_val)
            heapq.heappush(heap, new_val)

for t in range(int(input())):
    n = int(input())
    if n in order:
        print(order[n])
    else:
        print("Not in sequence")