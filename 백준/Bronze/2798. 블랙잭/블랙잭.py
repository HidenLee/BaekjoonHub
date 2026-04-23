N, M = map(int,input().split())
lst = list(map(int, input().split()))
answer = 0
for i in range(N):
    if lst[i] > M:
        continue
    for j in range(i+1,N):
        if lst[i] + lst[j] > M:
            continue
        for k in range(j+1,N):
            if lst[i] + lst[j] + lst[k] > M:
                continue
            answer = max(answer, lst[i] + lst[j] + lst[k])
print(answer)            