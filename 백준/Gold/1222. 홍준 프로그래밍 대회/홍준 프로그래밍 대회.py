import math
N = int(input())
M = tuple(map(int, input().split()))

array = [0] * 2000001
MAX_INDEX = 0
for i in M:
    MAX_INDEX = max(MAX_INDEX, i)
    for j in range(1,int(math.sqrt(i))+1):
        if i % j == 0:
            array[j] += 1
            if i != j * j:
                array[i // j] += 1
ans = 0
for i in range(1, MAX_INDEX+1):
    if array[i] < 2:
        continue
    ans = max(ans,i * array[i])
print(ans)