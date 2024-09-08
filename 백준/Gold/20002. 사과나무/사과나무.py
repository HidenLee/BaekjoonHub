N = int(input())
table = []
prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
for idx in range(1,N+1):
    table.append(list(map(int,input().split())))
    for jdx in range(1,N+1):
        prefix_sum[idx][jdx] = prefix_sum[idx-1][jdx] + prefix_sum[idx][jdx-1] - prefix_sum[idx-1][jdx-1] + table[idx-1][jdx-1]

ans = -1001
for k in range(1,N+1):
    for idx in range(k,N+1):
        for jdx in range(k,N+1):
            temp = prefix_sum[idx][jdx] - prefix_sum[idx-k][jdx] - prefix_sum[idx][jdx-k] + prefix_sum[idx-k][jdx-k]
            ans = max(temp,ans)

print(ans)