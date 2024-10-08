n = int(input())
matrix = [[]] * n

for i in range(n):
    matrix[i] = [int(i) for i in input().split()]

sum_up, sum_down = 0, 0
for i in range(n):
    for j in range(n):
        if i < j:
            sum_down += matrix[i][j]
        elif i > j:
            sum_up += matrix[i][j]

k = int(input())
difference = abs(sum_up - sum_down)
if difference <= k: 
    print("YES")
else:
    print("NO")
print(difference)