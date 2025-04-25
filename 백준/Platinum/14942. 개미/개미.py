N = int(input())
ants = [0]+[int(input()) for _ in range(N)]
graph = [[] for _ in range(N + 1)]
for i in range(N-1):
    fr, to, cost = map(int, input().split())
    graph[fr].append((to, cost))
    graph[to].append((fr, cost))
sparse_table = [[[-1,0] for _ in range(N+1)] for _ in range(17)] # 2^17 > 1e5, [parent, cost]
depth = [0] * (N + 1)

def dfs(now, prev):
    for nxt,cost in graph[now]:
        if nxt != prev:
            sparse_table[0][nxt][0] = now
            sparse_table[0][nxt][1] = cost
            depth[nxt] = depth[now] + 1
            dfs(nxt, now)

dfs(1, -1)

for i in range(1, 17):
    for j in range(1, N + 1):
        if sparse_table[i-1][j][0] != -1:
            prev , _ = sparse_table[i-1][j]
            sparse_table[i][j][0] = sparse_table[i-1][prev][0]
            sparse_table[i][j][1] = sparse_table[i-1][j][1] + sparse_table[i-1][prev][1]

result = [0] * (N + 1)
for node in range(1, N + 1):
    e = ants[node]
    now = node
    for j in reversed(range(17)):
        if sparse_table[j][now][0] != -1 and sparse_table[j][now][1] <= e:
            e -= sparse_table[j][now][1]
            now = sparse_table[j][now][0]
    print(now)
    