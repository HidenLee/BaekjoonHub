n = int(input())
arr = [0,0,1,1] +[0]* (n -3)

for i in range(4, n + 1):
    min_value = min(float('inf'), arr[i -1])
    if i % 2 == 0:
        min_value = min(min_value, arr[i // 2])
    if i % 3 == 0:
        min_value = min(min_value, arr[i // 3])
    arr[i] = min_value + 1 if min_value != float('inf') else 100000

print(arr[n])
